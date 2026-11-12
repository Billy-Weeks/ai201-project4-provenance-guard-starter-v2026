"""Unit 9 stretch 3 — full-request latency breakdown.

    python run_latency.py            # 30 normal submissions (default)
    python run_latency.py --n 30

Imports the app in-process, so the startup warm-up (stretch 1) runs and is
logged first. Then sends N normal submissions through Flask's test client,
timing each one client-side, and pairs that with the request's
`stage_durations_ms` record in `logs/operations.jsonl`. Writes
`results/latency_<timestamp>.md` with the mean, median, 95th percentile, and
share of request time for every stage, and names the dominant stage.
"""

import argparse
import json
import statistics
import time
from datetime import datetime, timezone

import operations

_ops_before_import = len(operations.read_events())
_import_started = time.perf_counter()
from app import app  # noqa: E402  (import triggers the startup warm-up)
_import_ms = (time.perf_counter() - _import_started) * 1000

import config  # noqa: E402
from run_load import NORMAL_TEXTS  # noqa: E402  (run_load does not import app)


# Top-level stages: these do not overlap, so with `unaccounted` they add up
# to the client-side request time.
TOP_LEVEL = ["validation", "detector", "stylometry", "scoring", "audit_write"]
# Steps inside `detector`; `detector_other` is detector minus these three.
DETECTOR_STEPS = ["detector_tokenize", "detector_forward", "detector_score"]


def _pct(values: list[float], pct: float) -> float:
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, round(pct / 100 * len(ordered)) - 1))
    return ordered[index]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=30)
    args = parser.parse_args()

    started_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    run_tag = datetime.now().strftime("%H%M%S")
    client = app.test_client()

    ops_before = len(operations.read_events())
    client_ms = {}
    for index in range(1, args.n + 1):
        request_id = f"latency-{run_tag}-{index}"
        t0 = time.perf_counter()
        response = client.post(
            "/submit",
            json={
                "text": NORMAL_TEXTS[(index - 1) % len(NORMAL_TEXTS)],
                "creator_id": f"latency-{run_tag}-{index}",
            },
            headers={"X-Request-ID": request_id},
        )
        client_ms[request_id] = (time.perf_counter() - t0) * 1000
        if response.status_code != 200:
            raise SystemExit(f"{request_id}: unexpected {response.status_code} {response.get_json()}")

    all_new = operations.read_events()
    startup = [
        e for e in all_new[_ops_before_import:ops_before]
        if e.get("event") == "startup_warmup"
    ]
    events = {e["request_id"]: e for e in all_new[ops_before:]}

    rows = []
    for request_id, total in client_ms.items():
        stages = dict(events[request_id]["stage_durations_ms"])
        stages["detector_other"] = stages["detector"] - sum(stages.get(s, 0.0) for s in DETECTOR_STEPS)
        stages["unaccounted"] = total - sum(stages.get(s, 0.0) for s in TOP_LEVEL)
        stages["client_total"] = total
        rows.append(stages)

    order = (
        ["validation", "detector"]
        + DETECTOR_STEPS + ["detector_other"]
        + ["stylometry", "scoring", "audit_write", "unaccounted", "client_total"]
    )
    mean_total = statistics.mean(r["client_total"] for r in rows)
    summary = {}
    for stage in order:
        values = [r.get(stage, 0.0) for r in rows]
        summary[stage] = {
            "mean": statistics.mean(values),
            "p50": statistics.median(values),
            "p95": _pct(values, 95),
            "share": statistics.mean(values) / mean_total * 100,
        }
    dominant = max(TOP_LEVEL + ["unaccounted"], key=lambda s: summary[s]["mean"])
    dominant_step = max(DETECTOR_STEPS + ["detector_other"], key=lambda s: summary[s]["mean"])

    stamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    lines = [
        f"# Unit 9 stretch 3 — latency breakdown ({stamp})",
        "",
        f"Started: `{started_at}`  ·  requests: `{args.n}` normal submissions, in-process via Flask's test client",
        "",
        "Produced by `run_latency.py::main`. Stage times come from `stage_durations_ms` written by",
        "`app.py::submit` and `detector.py::model_signal`/`perplexity` through `operations.py::log_event`.",
        "`client_total` is measured around each `client.post(...)` call. `unaccounted` = client_total minus",
        "the top-level stages (Flask request/response handling, the operations-log write, JSON serialization).",
        "Indented rows are steps inside `detector`; they are not added again to the total.",
        "",
        "| Stage | Mean (ms) | Median (ms) | p95 (ms) | Share of mean request |",
        "|---|---:|---:|---:|---:|",
    ]
    for stage in order:
        s = summary[stage]
        name = f"↳ `{stage}`" if stage in DETECTOR_STEPS + ["detector_other"] else f"`{stage}`"
        if stage == "client_total":
            name = "**`client_total`**"
        lines.append(f"| {name} | {s['mean']:.3f} | {s['p50']:.3f} | {s['p95']:.3f} | {s['share']:.2f}% |")

    first = rows[0]
    lines.extend([
        "",
        f"**Dominant stage:** `{dominant}` at {summary[dominant]['share']:.2f}% of mean request time; "
        f"inside it, `{dominant_step}` at {summary[dominant_step]['share']:.2f}%.",
        "",
        f"**First request** (first inference after startup): client_total {first['client_total']:.1f} ms, "
        f"detector_forward {first.get('detector_forward', 0):.1f} ms.",
        "",
        "## Startup (once per process)",
        "",
        f"- Import of `app` (includes the warm-up): `{_import_ms:.1f} ms`",
        "",
        "```json",
    ])
    lines.extend(json.dumps(e, ensure_ascii=False) for e in startup)
    lines.extend(["```", "", "## Every request", "", "```json"])
    for request_id, r in zip(client_ms, rows):
        lines.append(json.dumps({"request_id": request_id, **{k: round(v, 4) for k, v in r.items()}}))
    lines.extend(["```", "", "## Operational records", "", "```json"])
    lines.extend(json.dumps(events[rid], ensure_ascii=False) for rid in client_ms)
    lines.extend(["```", ""])

    output = config.RESULTS_DIR / f"latency_{stamp}.md"
    output.write_text("\n".join(lines), encoding="utf-8")
    print(output)
    print(f"dominant={dominant} ({summary[dominant]['share']:.2f}%), step={dominant_step}")


if __name__ == "__main__":
    main()
