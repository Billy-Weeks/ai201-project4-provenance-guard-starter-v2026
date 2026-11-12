#!/usr/bin/env python3
"""
Provenance Guard — the web service.

    python app.py

Then, in another terminal:

    curl -X POST http://127.0.0.1:5000/ping \
      -H "Content-Type: application/json" \
      -d '{"message": "hello"}'

That's the example route. It works right now, before you've written anything.
**Leave it alone** — it's your control. When something breaks later, check that
`/ping` still answers: if it does, the problem is in your handler; if it
doesn't, it's the service itself.

Routes:

    POST /ping        the worked example. Already works. Don't edit it
    POST /submit      ← YOU BUILD THIS (Milestone 3, 4, 5)
    POST /appeal      ← YOU BUILD THIS (Milestone 5)
    GET  /content/<id>  one item's current status (stretch feature)
    GET  /log         the audit log. Already works
    GET  /health      is the service up, and is the model loaded
"""

import json
import os
import time
import uuid

from flask import Flask, jsonify, request

import audit
import config
import detector
import operations
import scoring
import stylometry

app = Flask(__name__)


# ── Rate limiting — UNIT 8 ────────────────────────────────────────────────────
# Off until you turn it on. In unit 8, Milestone 1:
#
#   1. Set RATE_LIMITING_ENABLED = True in config.py (or AI201_RATE_LIMITS=1)
#   2. Choose your numbers there
#   3. Uncomment the @limiter.limit(...) line on /submit below
#
# The order doesn't matter. While limiting is off, that decorator is a no-op
# that quietly does nothing, so uncommenting it early costs you nothing — but
# it also means no 429 until you've done step 1.
#
# The storage backend is preconfigured, which stops Flask-Limiter printing a
# warning on every start. In-memory is right for one laptop and wrong for
# anything real — a restart forgets every count.

class _LimiterOff:
    """
    Stands in for the real limiter while rate limiting is off.

    It makes @limiter.limit(...) a decorator that returns the route
    untouched, so uncommenting the line before you flip the setting is
    harmless instead of a crash on startup.
    """

    def limit(self, *args, **kwargs):
        return lambda view: view


limiter = _LimiterOff()
if config.RATE_LIMITING_ENABLED:
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address

    def rate_limit_key():
        """
        Who a request counts against.

        Falling back to the caller's address is the easy version. Unit 8's
        stretch asks about per-creator limits instead — and the difference
        matters: one script can look like a thousand callers, and one household
        can look like one.
        """
        payload = request.get_json(silent=True)
        # A body that parses as JSON but isn't an object — a bare list or
        # string — has no .get. Without this guard the key function raises
        # BEFORE the route runs, and a malformed request becomes a 500 that
        # looks like your handler crashed when your handler never ran.
        if not isinstance(payload, dict):
            return get_remote_address()
        creator = payload.get("creator_id")
        return creator if isinstance(creator, str) and creator.strip() else get_remote_address()

    limiter = Limiter(
        key_func=rate_limit_key,
        app=app,
        storage_uri=config.RATE_LIMIT_STORAGE,
        default_limits=[],
    )

    @app.errorhandler(429)
    def rate_limited(exc):
        """
        A rejected request still leaves a trace.

        ⚠️ An attack that shows up only as an absence is one you'll never find.
        """
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            payload = {}
        audit.log_rejection(
            creator_id=payload.get("creator_id", "unknown"),
            reason="rate_limited",
            limit=str(exc.description),
        )
        return jsonify({
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly.",
            "limit": str(exc.description),
        }), 429


# ── The worked example. Already works. Don't edit. ────────────────────────────

@app.post("/ping")
def ping():
    """
    Everything a route needs, in six lines.

    JSON arrives as a dict. You pull things out of it. You return a dict and
    the framework turns it into a response. That's the whole idea.
    """
    payload = request.get_json(silent=True) or {}
    return jsonify({
        "ok": True,
        "you_sent": payload.get("message"),
        "service": "provenance-guard",
    })


@app.get("/health")
def health():
    """Is the service up, and has the model been downloaded yet?"""
    import detector

    loaded = detector._model is not None
    return jsonify({
        "ok": True,
        "detector_model": config.DETECTOR_MODEL,
        "detector_loaded": loaded,
        "rate_limiting": config.RATE_LIMITING_ENABLED,
        "log_entries": len(audit.read_entries()),
    })


# ── YOU BUILD THIS ────────────────────────────────────────────────────────────

@app.post("/submit")
@limiter.limit(f"{config.RATE_LIMIT_PER_MINUTE}/minute;{config.RATE_LIMIT_PER_DAY}/day")
def submit():
    """
    Take a piece of text, decide about it, log the decision, answer.
    ← TODO — Milestones 3, 4 and 5

    Expects JSON:
        {"text": "...", "creator_id": "..."}

    Should return JSON with, at minimum:
        {"content_id": "...", "guess": "...", "confidence": 0.0, "label": "...",
         "model_score": 0.0, "style_score": 0.0}

    ⚠️ **Both signal scores go in the response, not just the log.** Unit 8's
    `run_attacks.py` and `run_eval.py` read `model_score` and `style_score`
    straight off this response and put them in your reports. Leave them out and
    every row of next unit's evidence says `null` — which is exactly the
    diagnostic you need to name a stage and a mechanism. You do not want to
    find that out after running the attack set.

    ─────────────────────────────────────────────────────────────────────────
    Build it in three passes. Do not skip ahead — the ordering is how you tell
    a broken route from a broken signal.

    **Milestone 3 — the route answers.**
      1. Return a hardcoded response. Confirm `curl` gets it back before you
         add any logic at all.
      2. Then pull `text` and `creator_id` out of the payload.
      3. Then call ONE signal — `detector.model_signal(text)` — and put the
         real number in. Leave confidence and label as placeholders.
      4. Log every submission with `audit.log_decision(...)`. The content_id
         matters: `/appeal` needs it, and a student who skips it rebuilds this
         whole flow later.

    **Milestone 4 — the second signal and the score.**
      5. Add `stylometry.style_signal(text)`.
      6. Combine them with `scoring.combine_signals(...)`.
      7. Log BOTH signal scores alongside the combined one, and put them in the
         response too. Next unit you can't diagnose anything without them.

    **Milestone 5 — the label.**
      8. `scoring.score_to_label(...)` and put the real label in the response.

    ─────────────────────────────────────────────────────────────────────────
    Worth deciding early, because unit 8's attack set will decide it for you:
    what should this do when `text` is missing, empty, or enormous? A crash on
    a malformed input is one of the most common real failures there is.
    """
    started = time.perf_counter()
    request_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())
    payload = request.get_json(silent=True) or {}

    if not isinstance(payload, dict):
        audit.log_rejection(
            creator_id="unknown",
            reason="invalid_json",
            message="Request body must be a JSON object.",
        )
        return jsonify({"error": "invalid_json", "message": "Request body must be a JSON object."}), 400

    text = payload.get("text")
    creator_id = payload.get("creator_id")
    if not isinstance(text, str) or not isinstance(creator_id, str):
        audit.log_rejection(
            creator_id=creator_id if isinstance(creator_id, str) else "unknown",
            reason="missing_fields",
            message="POST /submit requires text and creator_id.",
        )
        return jsonify({
            "error": "missing_fields",
            "message": "POST /submit requires text and creator_id.",
        }), 400
    if not text.strip():
        audit.log_rejection(
            creator_id=creator_id,
            reason="empty_text",
            message="text must not be empty.",
        )
        return jsonify({"error": "empty_text", "message": "text must not be empty."}), 400
    if len(text.split()) < 3:
        audit.log_rejection(
            creator_id=creator_id,
            reason="text_too_short",
            message="text must contain at least three tokens.",
        )
        return jsonify({
            "error": "text_too_short",
            "message": "text must contain at least three tokens.",
        }), 400
    if len(text) > config.MAX_TEXT_CHARS:
        audit.log_rejection(
            creator_id=creator_id,
            reason="text_too_long",
            message=f"text must be at most {config.MAX_TEXT_CHARS} characters.",
        )
        return jsonify({
            "error": "text_too_long",
            "message": f"text must be at most {config.MAX_TEXT_CHARS} characters.",
        }), 400

    # Stretch 3: everything from arrival to here is reading and checking input.
    stage_durations_ms = {"validation": (time.perf_counter() - started) * 1000}

    content_id = str(uuid.uuid4())
    input_summary = {
        "creator_id": creator_id,
        "text_chars": len(text),
        "text_tokens": len(text.split()),
    }

    current_stage = "detector"
    stage_started = time.perf_counter()
    try:
        model_score = detector.model_signal(text)
        stage_durations_ms["detector"] = (time.perf_counter() - stage_started) * 1000
        # Stretch 3: the detector's internal steps (tokenize, forward, score).
        stage_durations_ms.update(detector.last_timings())

        current_stage = "stylometry"
        stage_started = time.perf_counter()
        style_score = stylometry.style_signal(text)
        stage_durations_ms["stylometry"] = (time.perf_counter() - stage_started) * 1000

        current_stage = "scoring"
        stage_started = time.perf_counter()
        confidence = scoring.combine_signals(model_score, style_score)
        guess, label = scoring.score_to_label(confidence)
        stage_durations_ms["scoring"] = (time.perf_counter() - stage_started) * 1000
    except detector.DetectorUnavailable:
        stage_durations_ms.setdefault(
            current_stage,
            (time.perf_counter() - stage_started) * 1000,
        )
        duration_ms = (time.perf_counter() - started) * 1000
        operations.log_event(
            request_id=request_id,
            event="scoring_failed",
            stage="detector",
            status_code=503,
            duration_ms=duration_ms,
            input_summary=input_summary,
            output_summary={"error": "detector_unavailable"},
            error_type="DetectorUnavailable",
            stage_durations_ms=stage_durations_ms,
        )
        return jsonify({
            "error": "detector_unavailable",
            "message": "The detector is temporarily unavailable. Try again later.",
            "request_id": request_id,
        }), 503
    except Exception as exc:  # noqa: BLE001
        stage_durations_ms.setdefault(
            current_stage,
            (time.perf_counter() - stage_started) * 1000,
        )
        duration_ms = (time.perf_counter() - started) * 1000
        operations.log_event(
            request_id=request_id,
            event="scoring_failed",
            stage=current_stage,
            status_code=503,
            duration_ms=duration_ms,
            input_summary=input_summary,
            output_summary={"error": "scoring_unavailable"},
            error_type=type(exc).__name__,
            stage_durations_ms=stage_durations_ms,
        )
        return jsonify({
            "error": "scoring_unavailable",
            "message": "The submission could not be scored. Try again later.",
            "request_id": request_id,
        }), 503

    stage_started = time.perf_counter()
    audit.log_decision(
        content_id=content_id,
        creator_id=creator_id,
        guess=guess,
        model_score=model_score,
        style_score=style_score,
        combined_score=confidence,
        label=label,
        status="decided",
    )
    stage_durations_ms["audit_write"] = (time.perf_counter() - stage_started) * 1000

    operations.log_event(
        request_id=request_id,
        event="submission_completed",
        stage="completed",
        status_code=200,
        duration_ms=(time.perf_counter() - started) * 1000,
        input_summary=input_summary,
        output_summary={
            "content_id": content_id,
            "guess": guess,
            "status": "decided",
        },
        stage_durations_ms=stage_durations_ms,
    )

    return jsonify({
        "content_id": content_id,
        "request_id": request_id,
        "guess": guess,
        "confidence": confidence,
        "label": label,
        "model_score": model_score,
        "style_score": style_score,
    })

@app.post("/appeal")
def appeal():
    """Record a writer's appeal and move an existing item under review."""
    payload = request.get_json(silent=True) or {}
    if not isinstance(payload, dict):
        return jsonify({"error": "invalid_json", "message": "Request body must be a JSON object."}), 400

    content_id = payload.get("content_id")
    reasoning = payload.get("reasoning")
    if not isinstance(content_id, str) or not isinstance(reasoning, str) or not reasoning.strip():
        return jsonify({
            "error": "missing_fields",
            "message": "POST /appeal requires content_id and reasoning.",
        }), 400

    entries = audit.entries_for(content_id)
    if not entries:
        return jsonify({
            "error": "not_found",
            "message": "No submission exists for that content_id.",
        }), 404

    original = next((entry for entry in entries if entry.get("status") == "decided"), entries[0])
    appeal_entry = audit.log_appeal(
        content_id=content_id,
        creator_id=original.get("creator_id", "unknown"),
        reasoning=reasoning,
    )
    return jsonify({
        "content_id": content_id,
        "status": appeal_entry["status"],
        "message": "Appeal recorded for review.",
    })


@app.get("/content/<content_id>")
def get_content(content_id):
    """One item's original decision and its current status, read from the audit log."""
    entries = audit.entries_for(content_id)
    if not entries:
        return jsonify({
            "error": "not_found",
            "message": "No submission exists for that content_id.",
        }), 404

    original = next((entry for entry in entries if entry.get("status") == "decided"), entries[0])
    return jsonify({
        "content_id": content_id,
        "creator_id": original.get("creator_id"),
        "guess": original.get("guess"),
        "confidence": original.get("combined_score"),
        "label": original.get("label"),
        "status": entries[-1].get("status"),
    })


# ── Already works ─────────────────────────────────────────────────────────────

@app.get("/log")
def get_log():
    """
    The audit log, most recent last.

        curl "http://127.0.0.1:5000/log?limit=10"

    You need this in unit 8 to paste entries into your README, and you need it
    now to see whether your logging is actually working.
    """
    limit = request.args.get("limit", type=int)
    entries = audit.read_entries(limit=limit)
    return jsonify({"count": len(entries), "entries": entries})


# ── Unit 9 stretch: warm the detector at startup ──────────────────────────────
# Without this, the first /submit pays for loading the model (100–230 s in the
# Unit 9 runs). Loading here moves that cost to startup and records it as its
# own operational event. A failed load does not stop the service: /submit still
# returns the safe 503 path when the detector is unavailable.

def _warm_detector() -> None:
    print(f"Loading detector model '{config.DETECTOR_MODEL}' (about 2 minutes)...", flush=True)
    started = time.perf_counter()
    try:
        detector.warm_up()
    except detector.DetectorUnavailable as exc:
        operations.log_event(
            request_id="startup",
            event="startup_warmup",
            stage="detector",
            status_code=503,
            duration_ms=(time.perf_counter() - started) * 1000,
            input_summary={"model": config.DETECTOR_MODEL},
            output_summary={"detector_loaded": False, "error": str(exc)[:200]},
            error_type="DetectorUnavailable",
        )
        return
    duration_ms = (time.perf_counter() - started) * 1000
    operations.log_event(
        request_id="startup",
        event="startup_warmup",
        stage="detector",
        status_code=200,
        duration_ms=duration_ms,
        input_summary={"model": config.DETECTOR_MODEL},
        output_summary={"detector_loaded": True},
        stage_durations_ms={"detector_load": duration_ms},
    )


# With debug on, `python app.py` runs twice: a reloader parent that only watches
# files, and a child (WERKZEUG_RUN_MAIN=true) that serves requests. Warm only
# the process that serves.
_reloader_parent = (
    __name__ == "__main__"
    and config.DEBUG
    and os.environ.get("WERKZEUG_RUN_MAIN") != "true"
)
if config.DETECTOR_WARMUP and not _reloader_parent:
    _warm_detector()


def _print_startup_health() -> None:
    """Print GET /health once at startup so it's clear whether the service can score.

    Called internally through the test client just before the server starts
    listening. The warm-up has already run by then, so this shows the state
    the first real request will see. The reloader's watcher process is
    skipped, because it never loads the model.
    """
    body = app.test_client().get("/health").get_json()
    print(f"Health: {json.dumps(body, sort_keys=True)}")
    if body.get("detector_loaded"):
        print("Ready to score.")
    elif not config.DETECTOR_WARMUP:
        print("Warm-up is off (AI201_WARMUP=0): the first /submit will load the model.")
    else:
        print("Detector did NOT load. /submit will return 503 detector_unavailable.")
        print("Run `python detector.py` to download the model, then restart.")
    print()


def main():
    print(f"Provenance Guard on http://{config.HOST}:{config.PORT}")
    print(f"  detector model:  {config.DETECTOR_MODEL}")
    print(f"  rate limiting:   {'ON' if config.RATE_LIMITING_ENABLED else 'off (unit 8)'}")
    print(f"  audit log:       {config.AUDIT_LOG}")
    print()
    print("Check it's alive:")
    print(f'  curl -X POST http://{config.HOST}:{config.PORT}/ping \\')
    print('    -H "Content-Type: application/json" \\')
    print("    -d '{\"message\": \"hello\"}'")
    print()
    if not _reloader_parent:
        _print_startup_health()
    # debug=True hands out an interactive debugger, so it's local-only — see config.py
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)


if __name__ == "__main__":
    main()
