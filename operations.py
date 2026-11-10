"""Structured operational visibility for Unit 9.

The audit log answers what decision was made about a piece of text. This log
answers what happened while handling the request: which request it was, which
stage ran, what response was returned, and how long the path took.
"""

import json
import threading
from datetime import datetime, timezone

import config


_lock = threading.Lock()


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds")


def log_event(
    *,
    request_id: str,
    event: str,
    stage: str,
    status_code: int,
    duration_ms: float,
    input_summary: dict,
    output_summary: dict,
    error_type: str | None = None,
) -> dict:
    """Append one request event with stable, inspectable fields."""
    entry = {
        "timestamp": _now(),
        "request_id": request_id,
        "event": event,
        "stage": stage,
        "status_code": status_code,
        "duration_ms": round(max(0.0, duration_ms), 3),
        "input": input_summary,
        "output": output_summary,
        "error_type": error_type,
    }

    config.LOG_DIR.mkdir(parents=True, exist_ok=True)
    with _lock:
        with config.OPERATIONAL_LOG.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(entry, ensure_ascii=False) + "\n")
    return entry


def read_events(limit: int | None = None) -> list[dict]:
    """Read valid operational events, oldest first."""
    if not config.OPERATIONAL_LOG.exists():
        return []

    events = []
    for line in config.OPERATIONAL_LOG.read_text(encoding="utf-8").splitlines():
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return events[-limit:] if limit else events


def clear() -> int:
    """Remove the operational log between isolated evaluation runs."""
    count = len(read_events())
    if config.OPERATIONAL_LOG.exists():
        config.OPERATIONAL_LOG.unlink()
    return count
