# Unit 9 Run — before-3

Started: `2026-11-11T22:28:40+00:00`

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

- Trial 1: `200` `{"confidence": 0.138, "content_id": "cdae8f5a-f783-478e-8837-294edc360f4f", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0071, "request_id": "unit9-before-3-normal-1", "style_score": 0.3343}`
- Trial 2: `200` `{"confidence": 0.1412, "content_id": "537babed-5c87-4b2b-b94d-b5625d5d81d3", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0125, "request_id": "unit9-before-3-normal-2", "style_score": 0.3343}`
- Trial 3: `200` `{"confidence": 0.1693, "content_id": "dff2decc-6e3d-4372-b89d-3e09c8ad8ca1", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0228, "request_id": "unit9-before-3-normal-3", "style_score": 0.389}`
- Trial 4: `200` `{"confidence": 0.1547, "content_id": "0f1ea9bf-215e-4958-a199-ffdc14b5d4e4", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0367, "request_id": "unit9-before-3-normal-4", "style_score": 0.3317}`
- Trial 5: `200` `{"confidence": 0.2761, "content_id": "f7a97933-3d76-4a62-adfd-2e9d4a183e17", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.2383, "request_id": "unit9-before-3-normal-5", "style_score": 0.3328}`
- Trial 6: `200` `{"confidence": 0.1401, "content_id": "250dcdbb-f044-4991-91be-fd65a0ce637d", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0127, "request_id": "unit9-before-3-normal-6", "style_score": 0.3312}`
- Trial 7: `200` `{"confidence": 0.1419, "content_id": "95cf48c8-d6c1-44c0-bb15-f9084d3392c6", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0147, "request_id": "unit9-before-3-normal-7", "style_score": 0.3328}`
- Trial 8: `200` `{"confidence": 0.1781, "content_id": "f8785ed0-6530-4d5c-b97f-e79c2223620e", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0357, "request_id": "unit9-before-3-normal-8", "style_score": 0.3916}`
- Trial 9: `200` `{"confidence": 0.1426, "content_id": "d4726cde-40bd-4144-a29d-7ebc99befad6", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0162, "request_id": "unit9-before-3-normal-9", "style_score": 0.3323}`
- Trial 10: `200` `{"confidence": 0.1507, "content_id": "9ca0953e-7748-45b2-a770-5d3abe018dea", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0289, "request_id": "unit9-before-3-normal-10", "style_score": 0.3333}`

### Forced detector failures

- Trial 1: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-before-3-failure-1"}`
- Trial 2: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-before-3-failure-2"}`
- Trial 3: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-before-3-failure-3"}`
- Trial 4: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-before-3-failure-4"}`
- Trial 5: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-before-3-failure-5"}`

## Operational log entries

```json
{"duration_ms": 163716.817, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-3-1", "text_chars": 70, "text_tokens": 9}, "output": {"content_id": "cdae8f5a-f783-478e-8837-294edc360f4f", "guess": "human", "status": "decided"}, "request_id": "unit9-before-3-normal-1", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T22:31:14.513+00:00"}
{"duration_ms": 128.536, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-3-2", "text_chars": 70, "text_tokens": 9}, "output": {"content_id": "537babed-5c87-4b2b-b94d-b5625d5d81d3", "guess": "human", "status": "decided"}, "request_id": "unit9-before-3-normal-2", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T22:31:14.650+00:00"}
{"duration_ms": 143.496, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-3-3", "text_chars": 66, "text_tokens": 11}, "output": {"content_id": "dff2decc-6e3d-4372-b89d-3e09c8ad8ca1", "guess": "human", "status": "decided"}, "request_id": "unit9-before-3-normal-3", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T22:31:14.801+00:00"}
{"duration_ms": 133.512, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-3-4", "text_chars": 66, "text_tokens": 10}, "output": {"content_id": "0f1ea9bf-215e-4958-a199-ffdc14b5d4e4", "guess": "human", "status": "decided"}, "request_id": "unit9-before-3-normal-4", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T22:31:14.943+00:00"}
{"duration_ms": 152.38, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-3-5", "text_chars": 69, "text_tokens": 11}, "output": {"content_id": "f7a97933-3d76-4a62-adfd-2e9d4a183e17", "guess": "human", "status": "decided"}, "request_id": "unit9-before-3-normal-5", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T22:31:15.106+00:00"}
{"duration_ms": 147.73, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-3-6", "text_chars": 65, "text_tokens": 10}, "output": {"content_id": "250dcdbb-f044-4991-91be-fd65a0ce637d", "guess": "human", "status": "decided"}, "request_id": "unit9-before-3-normal-6", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T22:31:15.264+00:00"}
{"duration_ms": 154.575, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-3-7", "text_chars": 67, "text_tokens": 9}, "output": {"content_id": "95cf48c8-d6c1-44c0-bb15-f9084d3392c6", "guess": "human", "status": "decided"}, "request_id": "unit9-before-3-normal-7", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T22:31:15.428+00:00"}
{"duration_ms": 170.888, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-3-8", "text_chars": 60, "text_tokens": 10}, "output": {"content_id": "f8785ed0-6530-4d5c-b97f-e79c2223620e", "guess": "human", "status": "decided"}, "request_id": "unit9-before-3-normal-8", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T22:31:15.610+00:00"}
{"duration_ms": 155.149, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-3-9", "text_chars": 67, "text_tokens": 10}, "output": {"content_id": "d4726cde-40bd-4144-a29d-7ebc99befad6", "guess": "human", "status": "decided"}, "request_id": "unit9-before-3-normal-9", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T22:31:15.775+00:00"}
{"duration_ms": 160.591, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-before-3-10", "text_chars": 69, "text_tokens": 10}, "output": {"content_id": "9ca0953e-7748-45b2-a770-5d3abe018dea", "guess": "human", "status": "decided"}, "request_id": "unit9-before-3-normal-10", "stage": "completed", "status_code": 200, "timestamp": "2026-11-11T22:31:15.946+00:00"}
{"duration_ms": 0.093, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-before-3-1", "text_chars": 70, "text_tokens": 9}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-before-3-failure-1", "stage": "detector", "status_code": 503, "timestamp": "2026-11-11T22:31:15.957+00:00"}
{"duration_ms": 0.146, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-before-3-2", "text_chars": 70, "text_tokens": 9}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-before-3-failure-2", "stage": "detector", "status_code": 503, "timestamp": "2026-11-11T22:31:15.968+00:00"}
{"duration_ms": 0.077, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-before-3-3", "text_chars": 66, "text_tokens": 11}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-before-3-failure-3", "stage": "detector", "status_code": 503, "timestamp": "2026-11-11T22:31:15.979+00:00"}
{"duration_ms": 0.112, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-before-3-4", "text_chars": 66, "text_tokens": 10}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-before-3-failure-4", "stage": "detector", "status_code": 503, "timestamp": "2026-11-11T22:31:15.989+00:00"}
{"duration_ms": 0.08, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-before-3-5", "text_chars": 69, "text_tokens": 11}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-before-3-failure-5", "stage": "detector", "status_code": 503, "timestamp": "2026-11-11T22:31:15.999+00:00"}
```

## Audit summary

- New audit entries: `10`
- New decided entries: `10`
- Completed operational entries: `10`
- Failure operational entries: `5`
