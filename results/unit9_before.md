# Unit 9 Run — before

Started: `2026-11-11T02:21:05+00:00`

## Criteria results

| Criterion | Target | Result | Verdict |
|---|---|---:|---|
| 1. Safe detector-failure response | 5/5 | 5/5 | MET |
| 2. No false decisions on detector failure | 5/5 | 5/5 | MET |
| 3. Complete failure visibility | 5/5 | 5/5 | MET |
| 4. Normal submissions remain valid | 9/10 | 10/10 | MET |
| 5. Timing on both paths | 10/10 | 10/10 | MET |

## Trial responses

### Normal submissions

- Trial 1: `200` `{"confidence": 0.138, "content_id": "5ab1b949-4a71-4650-bd38-fa3697489ddd", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0071, "request_id": "unit9-before-normal-1", "style_score": 0.3343}`
- Trial 2: `200` `{"confidence": 0.1412, "content_id": "c87c773e-f860-4646-9562-5e1d35ec3833", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0125, "request_id": "unit9-before-normal-2", "style_score": 0.3343}`
- Trial 3: `200` `{"confidence": 0.1693, "content_id": "c6b48f9a-48b5-4719-a98e-80c5f88b0173", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0228, "request_id": "unit9-before-normal-3", "style_score": 0.389}`
- Trial 4: `200` `{"confidence": 0.1547, "content_id": "62ae07e8-7806-4c3a-ad03-cbefafc67731", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0367, "request_id": "unit9-before-normal-4", "style_score": 0.3317}`
- Trial 5: `200` `{"confidence": 0.2761, "content_id": "9b0b5dd1-abd1-4d17-b993-6d211f4764f0", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.2383, "request_id": "unit9-before-normal-5", "style_score": 0.3328}`
- Trial 6: `200` `{"confidence": 0.1401, "content_id": "852419f1-5f37-4487-882b-2e20a9464bb4", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0127, "request_id": "unit9-before-normal-6", "style_score": 0.3312}`
- Trial 7: `200` `{"confidence": 0.1419, "content_id": "7c3df5ea-db8f-4b3f-a3b3-1d54d2f0b865", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0147, "request_id": "unit9-before-normal-7", "style_score": 0.3328}`
- Trial 8: `200` `{"confidence": 0.1781, "content_id": "0476ca1f-2671-4f97-812c-87712011274c", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0357, "request_id": "unit9-before-normal-8", "style_score": 0.3916}`
- Trial 9: `200` `{"confidence": 0.1426, "content_id": "65f459d2-d1c1-4b91-beaa-5ede040e6c96", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0162, "request_id": "unit9-before-normal-9", "style_score": 0.3323}`
- Trial 10: `200` `{"confidence": 0.1507, "content_id": "679dee56-80a9-4420-902a-5e6666fc9be3", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0289, "request_id": "unit9-before-normal-10", "style_score": 0.3333}`

### Forced detector failures

- Trial 1: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-before-failure-1"}`
- Trial 2: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-before-failure-2"}`
- Trial 3: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-before-failure-3"}`
- Trial 4: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-before-failure-4"}`
- Trial 5: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-before-failure-5"}`

## Operational log entries

```json
{"duration_ms": 103040.603, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-1", "text_chars": 70, "text_tokens": 9}, "output": {"content_id": "5ab1b949-4a71-4650-bd38-fa3697489ddd", "guess": "human", "status": "decided"}, "request_id": "unit9-before-normal-1", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T02:22:43.725+00:00"}
{"duration_ms": 119.411, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-2", "text_chars": 70, "text_tokens": 9}, "output": {"content_id": "c87c773e-f860-4646-9562-5e1d35ec3833", "guess": "human", "status": "decided"}, "request_id": "unit9-before-normal-2", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T02:22:43.856+00:00"}
{"duration_ms": 145.201, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-3", "text_chars": 66, "text_tokens": 11}, "output": {"content_id": "c6b48f9a-48b5-4719-a98e-80c5f88b0173", "guess": "human", "status": "decided"}, "request_id": "unit9-before-normal-3", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T02:22:44.011+00:00"}
{"duration_ms": 137.275, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-4", "text_chars": 66, "text_tokens": 10}, "output": {"content_id": "62ae07e8-7806-4c3a-ad03-cbefafc67731", "guess": "human", "status": "decided"}, "request_id": "unit9-before-normal-4", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T02:22:44.159+00:00"}
{"duration_ms": 130.382, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-5", "text_chars": 69, "text_tokens": 11}, "output": {"content_id": "9b0b5dd1-abd1-4d17-b993-6d211f4764f0", "guess": "human", "status": "decided"}, "request_id": "unit9-before-normal-5", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T02:22:44.298+00:00"}
{"duration_ms": 115.38, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-6", "text_chars": 65, "text_tokens": 10}, "output": {"content_id": "852419f1-5f37-4487-882b-2e20a9464bb4", "guess": "human", "status": "decided"}, "request_id": "unit9-before-normal-6", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T02:22:44.422+00:00"}
{"duration_ms": 126.864, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-7", "text_chars": 67, "text_tokens": 9}, "output": {"content_id": "7c3df5ea-db8f-4b3f-a3b3-1d54d2f0b865", "guess": "human", "status": "decided"}, "request_id": "unit9-before-normal-7", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T02:22:44.558+00:00"}
{"duration_ms": 120.434, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-8", "text_chars": 60, "text_tokens": 10}, "output": {"content_id": "0476ca1f-2671-4f97-812c-87712011274c", "guess": "human", "status": "decided"}, "request_id": "unit9-before-normal-8", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T02:22:44.687+00:00"}
{"duration_ms": 118.36, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-9", "text_chars": 67, "text_tokens": 10}, "output": {"content_id": "65f459d2-d1c1-4b91-beaa-5ede040e6c96", "guess": "human", "status": "decided"}, "request_id": "unit9-before-normal-9", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T02:22:44.814+00:00"}
{"duration_ms": 133.458, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-10", "text_chars": 69, "text_tokens": 10}, "output": {"content_id": "679dee56-80a9-4420-902a-5e6666fc9be3", "guess": "human", "status": "decided"}, "request_id": "unit9-before-normal-10", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T02:22:44.955+00:00"}
{"duration_ms": 0.113, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-before-1", "text_chars": 70, "text_tokens": 9}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-before-failure-1", "stage": "detector", "status_code": 503, "timestamp": "2026-11-11T02:22:44.966+00:00"}
{"duration_ms": 0.096, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-before-2", "text_chars": 70, "text_tokens": 9}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-before-failure-2", "stage": "detector", "status_code": 503, "timestamp": "2026-11-11T02:22:44.975+00:00"}
{"duration_ms": 0.081, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-before-3", "text_chars": 66, "text_tokens": 11}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-before-failure-3", "stage": "detector", "status_code": 503, "timestamp": "2026-11-11T02:22:44.984+00:00"}
{"duration_ms": 0.074, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-before-4", "text_chars": 66, "text_tokens": 10}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-before-failure-4", "stage": "detector", "status_code": 503, "timestamp": "2026-11-11T02:22:44.992+00:00"}
{"duration_ms": 0.072, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-before-5", "text_chars": 69, "text_tokens": 11}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-before-failure-5", "stage": "detector", "status_code": 503, "timestamp": "2026-11-11T02:22:45.001+00:00"}
```

## Audit summary

- New audit entries: `10`
- New decided entries: `10`
- Completed operational entries: `10`
- Failure operational entries: `5`
