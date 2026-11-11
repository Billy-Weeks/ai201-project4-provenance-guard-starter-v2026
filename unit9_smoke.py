"""Small repeatable smoke check for the Unit 9 failure extension.

Run with the project's activated environment:

    python unit9_smoke.py

The normal request uses the real detector. The failure request injects the
same `DetectorUnavailable` exception the detector raises when its model cannot
load, so the production route is tested without adding a public test switch.
Logs are redirected to a temporary directory and do not alter the repository's
existing Unit 7/8 evidence.
"""

import json
import tempfile
from pathlib import Path
from unittest.mock import patch

import audit
import config
import detector
import operations
from app import app


TEXT = (
    "The system records a clear operational trace for every submission "
    "so a later reviewer can understand what happened."
)


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="provenance-unit9-") as directory:
        log_dir = Path(directory) / "logs"
        config.LOG_DIR = log_dir
        config.AUDIT_LOG = log_dir / "audit.jsonl"
        config.OPERATIONAL_LOG = log_dir / "operations.jsonl"

        client = app.test_client()
        payload = {"text": TEXT, "creator_id": "unit9-smoke"}

        normal_response = client.post("/submit", json=payload)

        with patch.object(
            detector,
            "model_signal",
            side_effect=detector.DetectorUnavailable("forced Unit 9 smoke failure"),
        ):
            failed_response = client.post("/submit", json=payload)

        normal_body = normal_response.get_json()
        failed_body = failed_response.get_json()
        audit_entries = audit.read_entries()
        operation_entries = operations.read_events()

        assert normal_response.status_code == 200, normal_body
        assert failed_response.status_code == 503, failed_body
        assert failed_body["error"] == "detector_unavailable"
        assert "confidence" not in failed_body
        assert "label" not in failed_body
        assert sum(entry.get("status") == "decided" for entry in audit_entries) == 1

        failure_events = [
            entry for entry in operation_entries
            if entry.get("event") == "scoring_failed"
        ]
        assert len(failure_events) == 1
        failure = failure_events[0]
        for field in (
            "timestamp",
            "request_id",
            "stage",
            "error_type",
            "status_code",
            "duration_ms",
        ):
            assert field in failure, field
        assert failure["stage"] == "detector"
        assert failure["error_type"] == "DetectorUnavailable"
        assert failure["status_code"] == 503
        assert failure["duration_ms"] >= 0

        print("NORMAL", normal_response.status_code, json.dumps(normal_body, sort_keys=True))
        print("FAILURE", failed_response.status_code, json.dumps(failed_body, sort_keys=True))
        print("AUDIT_DECISIONS", sum(entry.get("status") == "decided" for entry in audit_entries))
        print("FAILURE_EVENT", json.dumps(failure, sort_keys=True))
        print("Unit 9 smoke check passed")


if __name__ == "__main__":
    main()
