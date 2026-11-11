# Unit 9 Run — before-2

Started: `2026-11-11T22:00:45+00:00`

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

- Trial 1: `200` `{"confidence": 0.138, "content_id": "1497f557-243e-450c-a39b-f8e1e3ac8361", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0071, "request_id": "unit9-before-2-normal-1", "style_score": 0.3343}`
- Trial 2: `200` `{"confidence": 0.1412, "content_id": "2958b759-19a3-4c21-bf25-9c1ac71a2d04", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0125, "request_id": "unit9-before-2-normal-2", "style_score": 0.3343}`
- Trial 3: `200` `{"confidence": 0.1693, "content_id": "d5c6f33d-9ad2-4b11-a554-c5de7afce568", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0228, "request_id": "unit9-before-2-normal-3", "style_score": 0.389}`
- Trial 4: `200` `{"confidence": 0.1547, "content_id": "2a53b88c-3a1a-45ca-8f51-7d17b5391871", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0367, "request_id": "unit9-before-2-normal-4", "style_score": 0.3317}`
- Trial 5: `200` `{"confidence": 0.2761, "content_id": "1908a8de-413e-4d46-9d5e-c7cc507a973d", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.2383, "request_id": "unit9-before-2-normal-5", "style_score": 0.3328}`
- Trial 6: `200` `{"confidence": 0.1401, "content_id": "81291e13-7f0c-4062-8274-1065999fd17a", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0127, "request_id": "unit9-before-2-normal-6", "style_score": 0.3312}`
- Trial 7: `200` `{"confidence": 0.1419, "content_id": "e8980585-3c05-4058-b3f7-286330d75d7c", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0147, "request_id": "unit9-before-2-normal-7", "style_score": 0.3328}`
- Trial 8: `200` `{"confidence": 0.1781, "content_id": "492ab8a8-44b5-4b32-9801-6896e5a4b7ad", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0357, "request_id": "unit9-before-2-normal-8", "style_score": 0.3916}`
- Trial 9: `200` `{"confidence": 0.1426, "content_id": "f930441e-01d8-49f2-8dfa-c3737aa4b061", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0162, "request_id": "unit9-before-2-normal-9", "style_score": 0.3323}`
- Trial 10: `200` `{"confidence": 0.1507, "content_id": "98be43e7-26ad-44ec-a46c-3702f764999f", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0289, "request_id": "unit9-before-2-normal-10", "style_score": 0.3333}`

### Forced detector failures

- Trial 1: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-before-2-failure-1"}`
- Trial 2: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-before-2-failure-2"}`
- Trial 3: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-before-2-failure-3"}`
- Trial 4: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-before-2-failure-4"}`
- Trial 5: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-before-2-failure-5"}`

## Operational log entries

```json
{"duration_ms": 176499.317, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-2-1", "text_chars": 70, "text_tokens": 9}, "output": {"content_id": "1497f557-243e-450c-a39b-f8e1e3ac8361", "guess": "human", "status": "decided"}, "request_id": "unit9-before-2-normal-1", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T22:03:30.960+00:00"}
{"duration_ms": 123.821, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-2-2", "text_chars": 70, "text_tokens": 9}, "output": {"content_id": "2958b759-19a3-4c21-bf25-9c1ac71a2d04", "guess": "human", "status": "decided"}, "request_id": "unit9-before-2-normal-2", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T22:03:31.096+00:00"}
{"duration_ms": 163.597, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-2-3", "text_chars": 66, "text_tokens": 11}, "output": {"content_id": "d5c6f33d-9ad2-4b11-a554-c5de7afce568", "guess": "human", "status": "decided"}, "request_id": "unit9-before-2-normal-3", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T22:03:31.268+00:00"}
{"duration_ms": 137.834, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-2-4", "text_chars": 66, "text_tokens": 10}, "output": {"content_id": "2a53b88c-3a1a-45ca-8f51-7d17b5391871", "guess": "human", "status": "decided"}, "request_id": "unit9-before-2-normal-4", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T22:03:31.415+00:00"}
{"duration_ms": 151.539, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-2-5", "text_chars": 69, "text_tokens": 11}, "output": {"content_id": "1908a8de-413e-4d46-9d5e-c7cc507a973d", "guess": "human", "status": "decided"}, "request_id": "unit9-before-2-normal-5", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T22:03:31.589+00:00"}
{"duration_ms": 142.254, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-2-6", "text_chars": 65, "text_tokens": 10}, "output": {"content_id": "81291e13-7f0c-4062-8274-1065999fd17a", "guess": "human", "status": "decided"}, "request_id": "unit9-before-2-normal-6", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T22:03:31.741+00:00"}
{"duration_ms": 142.957, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-2-7", "text_chars": 67, "text_tokens": 9}, "output": {"content_id": "e8980585-3c05-4058-b3f7-286330d75d7c", "guess": "human", "status": "decided"}, "request_id": "unit9-before-2-normal-7", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T22:03:31.898+00:00"}
{"duration_ms": 155.108, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-2-8", "text_chars": 60, "text_tokens": 10}, "output": {"content_id": "492ab8a8-44b5-4b32-9801-6896e5a4b7ad", "guess": "human", "status": "decided"}, "request_id": "unit9-before-2-normal-8", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T22:03:32.068+00:00"}
{"duration_ms": 151.276, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-2-9", "text_chars": 67, "text_tokens": 10}, "output": {"content_id": "f930441e-01d8-49f2-8dfa-c3737aa4b061", "guess": "human", "status": "decided"}, "request_id": "unit9-before-2-normal-9", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T22:03:32.236+00:00"}
{"duration_ms": 148.363, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-2-10", "text_chars": 69, "text_tokens": 10}, "output": {"content_id": "98be43e7-26ad-44ec-a46c-3702f764999f", "guess": "human", "status": "decided"}, "request_id": "unit9-before-2-normal-10", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T22:03:32.401+00:00"}
{"duration_ms": 0.085, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-before-2-1", "text_chars": 70, "text_tokens": 9}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-before-2-failure-1", "stage": "detector", "status_code": 503, "timestamp": "2026-11-11T22:03:32.412+00:00"}
{"duration_ms": 0.095, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-before-2-2", "text_chars": 70, "text_tokens": 9}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-before-2-failure-2", "stage": "detector", "status_code": 503, "timestamp": "2026-11-11T22:03:32.420+00:00"}
{"duration_ms": 0.048, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-before-2-3", "text_chars": 66, "text_tokens": 11}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-before-2-failure-3", "stage": "detector", "status_code": 503, "timestamp": "2026-11-11T22:03:32.428+00:00"}
{"duration_ms": 0.048, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-before-2-4", "text_chars": 66, "text_tokens": 10}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-before-2-failure-4", "stage": "detector", "status_code": 503, "timestamp": "2026-11-11T22:03:32.436+00:00"}
{"duration_ms": 0.076, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-before-2-5", "text_chars": 69, "text_tokens": 11}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-before-2-failure-5", "stage": "detector", "status_code": 503, "timestamp": "2026-11-11T22:03:32.445+00:00"}
```

## Audit summary

- New audit entries: `10`
- New decided entries: `10`
- Completed operational entries: `10`
- Failure operational entries: `5`
