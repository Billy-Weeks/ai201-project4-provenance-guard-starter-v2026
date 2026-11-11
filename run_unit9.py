"""Run the Unit 9 criteria against the live Flask route in-process.

Usage:

    python run_unit9.py --label before

The normal submissions use the real detector. Failure trials inject the
detector's existing `DetectorUnavailable` exception at the detector boundary.
The service writes real entries to `logs/audit.jsonl` and
`logs/operations.jsonl`; the report records only the entries created by this
run.
"""

import argparse
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

import audit
import config
import detector
import operations
from app import app


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


def _json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def _valid_normal(body: dict | None) -> bool:
    required = {
        "content_id",
        "guess",
        "confidence",
        "label",
        "model_score",
        "style_score",
    }
    return isinstance(body, dict) and required.issubset(body)


def run(label: str) -> Path:
    started_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    audit_before = len(audit.read_entries())
    operations_before = len(operations.read_events())
    client = app.test_client()

    normal_results = []
    for index, text in enumerate(NORMAL_TEXTS, start=1):
        response = client.post(
            "/submit",
            json={"text": text, "creator_id": f"unit9-normal-{label}-{index}"},
            headers={"X-Request-ID": f"unit9-{label}-normal-{index}"},
        )
        normal_results.append({
            "trial": index,
            "status": response.status_code,
            "body": response.get_json(),
        })

    failure_results = []
    with patch.object(
        detector,
        "model_signal",
        side_effect=detector.DetectorUnavailable("forced Unit 9 evaluation failure"),
    ):
        for index in range(1, 6):
            response = client.post(
                "/submit",
                json={
                    "text": NORMAL_TEXTS[index - 1],
                    "creator_id": f"unit9-failure-{label}-{index}",
                },
                headers={"X-Request-ID": f"unit9-{label}-failure-{index}"},
            )
            failure_results.append({
                "trial": index,
                "status": response.status_code,
                "body": response.get_json(),
            })

    audit_delta = audit.read_entries()[audit_before:]
    operation_delta = operations.read_events()[operations_before:]
    failure_events = [
        entry for entry in operation_delta
        if entry.get("event") == "scoring_failed"
    ]
    completed_events = [
        entry for entry in operation_delta
        if entry.get("event") == "submission_completed"
    ]
    new_decisions = [
        entry for entry in audit_delta
        if entry.get("status") == "decided"
    ]

    c1 = sum(
        result["status"] == 503
        and result["body"].get("error") == "detector_unavailable"
        and not {"guess", "confidence", "label"}.intersection(result["body"])
        for result in failure_results
    )
    c2 = 5 - len([
        entry for entry in audit_delta
        if entry.get("creator_id", "").startswith(f"unit9-failure-{label}-")
        and entry.get("status") == "decided"
    ])
    c3 = sum(
        all(field in entry for field in (
            "timestamp",
            "request_id",
            "stage",
            "error_type",
            "status_code",
            "duration_ms",
        ))
        for entry in failure_events
    )
    c4 = sum(
        result["status"] == 200 and _valid_normal(result["body"])
        for result in normal_results
    )
    timing_request_ids = {
        f"unit9-{label}-normal-{index}" for index in range(1, 6)
    } | {
        f"unit9-{label}-failure-{index}" for index in range(1, 6)
    }
    c5 = sum(
        isinstance(entry.get("duration_ms"), (int, float))
        and entry["duration_ms"] >= 0
        for entry in operation_delta
        if entry.get("event") in {"submission_completed", "scoring_failed"}
        and entry.get("request_id") in timing_request_ids
    )

    report = [
        f"# Unit 9 Run — {label}",
        "",
        f"Started: `{started_at}`",
        "",
        "## Criteria results",
        "",
        "| Criterion | Target | Result | Verdict |",
        "|---|---|---:|---|",
        f"| 1. Safe detector-failure response | 5/5 | {c1}/5 | {'MET' if c1 == 5 else 'MISSED'} |",
        f"| 2. No false decisions on detector failure | 5/5 | {c2}/5 | {'MET' if c2 == 5 else 'MISSED'} |",
        f"| 3. Complete failure visibility | 5/5 | {c3}/5 | {'MET' if c3 == 5 else 'MISSED'} |",
        f"| 4. Normal submissions remain valid | 9/10 | {c4}/10 | {'MET' if c4 >= 9 else 'MISSED'} |",
        f"| 5. Timing on both paths | 10/10 | {c5}/10 | {'MET' if c5 == 10 else 'MISSED'} |",
        "",
        "## Trial responses",
        "",
        "### Normal submissions",
        "",
    ]
    for result in normal_results:
        report.append(f"- Trial {result['trial']}: `{result['status']}` `{_json(result['body'])}`")
    report.extend(["", "### Forced detector failures", ""])
    for result in failure_results:
        report.append(f"- Trial {result['trial']}: `{result['status']}` `{_json(result['body'])}`")
    report.extend([
        "",
        "## Operational log entries",
        "",
        "```json",
    ])
    report.extend(_json(entry) for entry in operation_delta)
    report.extend([
        "```",
        "",
        "## Audit summary",
        "",
        f"- New audit entries: `{len(audit_delta)}`",
        f"- New decided entries: `{len(new_decisions)}`",
        f"- Completed operational entries: `{len(completed_events)}`",
        f"- Failure operational entries: `{len(failure_events)}`",
        "",
    ])

    output_path = config.RESULTS_DIR / f"unit9_{label}.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(report), encoding="utf-8")
    print(output_path)
    print(" ".join([
        f"C1={c1}/5",
        f"C2={c2}/5",
        f"C3={c3}/5",
        f"C4={c4}/10",
        f"C5={c5}/10",
    ]))
    return output_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--label", required=True, help="report label, such as before or after")
    args = parser.parse_args()
    run(args.label)
