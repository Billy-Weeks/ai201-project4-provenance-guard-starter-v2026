"""Unit 9 stretch — load observation at about ten times the normal rate.

Start the service in one terminal (debug off, so there is one serving process):

    AI201_DEBUG=0 python app.py

Then in another:

    python run_load.py

Normal rate is 10 submissions per minute, the per-creator rate limit in
`config.RATE_LIMIT_PER_MINUTE`. Three one-minute phases are sent:

    baseline  10/minute  one creator_id
    load_a   100/minute  one creator_id      (the rate limiter should engage)
    load_b   100/minute  ten creator_ids     (10/minute each, limiter should not)

Requests are fired on a fixed schedule, each on its own thread, so a slow
response never slows the send rate. Client-side status and latency are recorded
per request; compute time comes from the service's own `logs/operations.jsonl`
records for the same request IDs. Writes `results/load_<timestamp>.md`.
"""

import argparse
import json
import statistics
import threading
import time
from datetime import datetime, timezone

import requests

import config
import operations


# Same ten texts as run_unit9.NORMAL_TEXTS. Copied rather than imported:
# importing run_unit9 imports app, which would load the model in this client.
NORMAL_TEXTS = [
    "A careful audit trail helps reviewers understand every classification.",
    "The service should explain failures without exposing internal details.",
    "Writers deserve a clear appeal path when a result seems incorrect.",
    "Operational records make a local service easier to diagnose later.",
    "A measured response time is more useful than an unsupported estimate.",
    "The detector reads this paragraph as one ordinary writing sample.",
    "Structured fields let another person inspect the request afterward.",
    "A safe error is preferable to a fabricated confidence score.",
    "The scoring route combines two signals before recording a decision.",
    "A reproducible test should produce evidence another reader can check.",
]


PHASES = [
    # name, requests per minute, number of creator_ids
    ("baseline", 10, 1),
    ("load_a", 100, 1),
    ("load_b", 100, 10),
]


def _percentile(values: list[float], pct: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, round(pct / 100 * len(ordered)) - 1))
    return ordered[index]


def _send(url: str, payload: dict, request_id: str, results: list, lock: threading.Lock) -> None:
    sent_at = datetime.now(timezone.utc).isoformat(timespec="milliseconds")
    started = time.perf_counter()
    try:
        response = requests.post(
            url,
            json=payload,
            headers={"X-Request-ID": request_id},
            timeout=120,
        )
        status = response.status_code
        error = None
    except requests.RequestException as exc:
        status = None
        error = type(exc).__name__
    latency_ms = (time.perf_counter() - started) * 1000
    with lock:
        results.append({
            "request_id": request_id,
            "creator_id": payload["creator_id"],
            "sent_at": sent_at,
            "status": status,
            "error": error,
            "latency_ms": round(latency_ms, 3),
        })


def run_phase(base: str, run_tag: str, name: str, per_minute: int, creators: int,
              seconds: float) -> list[dict]:
    total = round(per_minute * seconds / 60)
    interval = 60.0 / per_minute
    results: list[dict] = []
    lock = threading.Lock()
    threads = []
    start = time.perf_counter()
    for index in range(total):
        target = start + index * interval
        delay = target - time.perf_counter()
        if delay > 0:
            time.sleep(delay)
        creator = f"load-{run_tag}-{name}-{index % creators}"
        payload = {"text": NORMAL_TEXTS[index % len(NORMAL_TEXTS)], "creator_id": creator}
        request_id = f"load-{run_tag}-{name}-{index + 1}"
        thread = threading.Thread(
            target=_send,
            args=(f"{base}/submit", payload, request_id, results, lock),
        )
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    return sorted(results, key=lambda r: int(r["request_id"].rsplit("-", 1)[1]))


def summarize(name: str, per_minute: int, creators: int, results: list[dict],
              events: dict) -> dict:
    statuses: dict[str, int] = {}
    for result in results:
        key = str(result["status"]) if result["status"] is not None else f"error:{result['error']}"
        statuses[key] = statuses.get(key, 0) + 1
    accepted = [r["latency_ms"] for r in results if r["status"] == 200]
    all_latency = [r["latency_ms"] for r in results]
    phase_events = [events[r["request_id"]] for r in results if r["request_id"] in events]
    compute_ms = sum(e.get("duration_ms", 0) for e in phase_events)
    return {
        "phase": name,
        "rate": f"{per_minute}/min",
        "creators": creators,
        "sent": len(results),
        "statuses": statuses,
        "p50_all_ms": round(statistics.median(all_latency), 1) if all_latency else 0,
        "p95_all_ms": round(_percentile(all_latency, 95), 1),
        "p50_200_ms": round(statistics.median(accepted), 1) if accepted else 0,
        "p95_200_ms": round(_percentile(accepted, 95), 1),
        "max_200_ms": round(max(accepted), 1) if accepted else 0,
        "scored_events": len(phase_events),
        "compute_s": round(compute_ms / 1000, 3),
        "compute_per_scored_ms": round(compute_ms / len(phase_events), 1) if phase_events else 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default=f"http://{config.HOST}:{config.PORT}")
    parser.add_argument("--seconds", type=float, default=60.0, help="length of each phase")
    args = parser.parse_args()

    health = requests.get(f"{args.base}/health", timeout=10).json()
    if not health.get("detector_loaded"):
        raise SystemExit(f"Service is up but detector_loaded is false: {health}")
    if not health.get("rate_limiting", True):
        print("WARNING: /health reports rate limiting off")

    run_tag = datetime.now().strftime("%H%M%S")
    started_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    ops_before = len(operations.read_events())

    phase_results = {}
    for name, per_minute, creators in PHASES:
        print(f"{name}: {per_minute}/min for {args.seconds:.0f}s across {creators} creator(s)...")
        phase_results[name] = run_phase(args.base, run_tag, name, per_minute, creators, args.seconds)

    time.sleep(1)  # let the last operational lines land
    new_events = operations.read_events()[ops_before:]
    events = {e["request_id"]: e for e in new_events}

    summaries = [
        summarize(name, per_minute, creators, phase_results[name], events)
        for name, per_minute, creators in PHASES
    ]

    stamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    lines = [
        f"# Unit 9 stretch — load observation ({stamp})",
        "",
        f"Started: `{started_at}`  ·  service: `{args.base}`  ·  health: `{json.dumps(health, sort_keys=True)}`",
        "",
        "Produced by `run_load.py::main` against `python app.py` (`app.py::submit`).",
        "Latency is client-side (send to response). Compute is the sum of `duration_ms`",
        "from `logs/operations.jsonl` for the phase's request IDs (scored requests only;",
        "a `429` is rejected before scoring and writes no operational record).",
        "",
        "| Phase | Rate | Creators | Sent | Status codes | p50 all (ms) | p95 all (ms) | p50 200 (ms) | p95 200 (ms) | max 200 (ms) | Scored | Compute (s) | Compute / scored (ms) |",
        "|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for s in summaries:
        codes = ", ".join(f"{k}×{v}" for k, v in sorted(s["statuses"].items()))
        lines.append(
            f"| {s['phase']} | {s['rate']} | {s['creators']} | {s['sent']} | {codes} | "
            f"{s['p50_all_ms']} | {s['p95_all_ms']} | {s['p50_200_ms']} | {s['p95_200_ms']} | "
            f"{s['max_200_ms']} | {s['scored_events']} | {s['compute_s']} | {s['compute_per_scored_ms']} |"
        )
    for name, _, _ in PHASES:
        lines.extend(["", f"## {name} — every request", "", "```json"])
        lines.extend(json.dumps(r, sort_keys=True) for r in phase_results[name])
        lines.append("```")
    lines.extend(["", "## Operational records written during the run", "", "```json"])
    lines.extend(json.dumps(e, ensure_ascii=False) for e in new_events)
    lines.extend(["```", ""])

    output = config.RESULTS_DIR / f"load_{stamp}.md"
    output.write_text("\n".join(lines), encoding="utf-8")
    print(output)
    for s in summaries:
        print(json.dumps(s, sort_keys=True))


if __name__ == "__main__":
    main()
