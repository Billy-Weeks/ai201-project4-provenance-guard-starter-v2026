# Unit 9 Run — after-2

Started: `2026-11-11T22:57:47+00:00`

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

- Trial 1: `200` `{"confidence": 0.138, "content_id": "366c0335-e19c-4eeb-ba12-4f7949df8781", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0071, "request_id": "unit9-after-2-normal-1", "style_score": 0.3343}`
- Trial 2: `200` `{"confidence": 0.1412, "content_id": "28e1d0a6-19da-41a5-b554-30bf2d23b990", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0125, "request_id": "unit9-after-2-normal-2", "style_score": 0.3343}`
- Trial 3: `200` `{"confidence": 0.1693, "content_id": "505678b3-10a8-45c2-a0f8-301d8378aecf", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0228, "request_id": "unit9-after-2-normal-3", "style_score": 0.389}`
- Trial 4: `200` `{"confidence": 0.1547, "content_id": "03ae7c02-37fe-402f-8f12-6d25f44a44ff", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0367, "request_id": "unit9-after-2-normal-4", "style_score": 0.3317}`
- Trial 5: `200` `{"confidence": 0.2761, "content_id": "a6cb48f5-6749-46a2-bdd9-bd348bd4b418", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.2383, "request_id": "unit9-after-2-normal-5", "style_score": 0.3328}`
- Trial 6: `200` `{"confidence": 0.1401, "content_id": "aaa9bed6-70af-4fad-85ac-1f1d53641541", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0127, "request_id": "unit9-after-2-normal-6", "style_score": 0.3312}`
- Trial 7: `200` `{"confidence": 0.1419, "content_id": "60518025-835c-4a6a-b7cb-b323f73bd6e5", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0147, "request_id": "unit9-after-2-normal-7", "style_score": 0.3328}`
- Trial 8: `200` `{"confidence": 0.1781, "content_id": "a9c20b95-4ddf-4a39-91fd-2a04def35225", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0357, "request_id": "unit9-after-2-normal-8", "style_score": 0.3916}`
- Trial 9: `200` `{"confidence": 0.1426, "content_id": "116d5804-fc95-4a28-a571-8e09c47401e4", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0162, "request_id": "unit9-after-2-normal-9", "style_score": 0.3323}`
- Trial 10: `200` `{"confidence": 0.1507, "content_id": "132b999b-9534-40e4-9559-ed9a7f14a2c8", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0289, "request_id": "unit9-after-2-normal-10", "style_score": 0.3333}`

### Forced detector failures

- Trial 1: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after-2-failure-1"}`
- Trial 2: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after-2-failure-2"}`
- Trial 3: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after-2-failure-3"}`
- Trial 4: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after-2-failure-4"}`
- Trial 5: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after-2-failure-5"}`

## Operational log entries

```json
{"duration_ms": 164581.841, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-2-1", "text_chars": 70, "text_tokens": 9}, "output": {"content_id": "366c0335-e19c-4eeb-ba12-4f7949df8781", "guess": "human", "status": "decided"}, "request_id": "unit9-after-2-normal-1", "stage": "completed", "stage_durations_ms": {"detector": 164573.61541799764, "scoring": 0.014758996258024126, "stylometry": 0.3009469946846366}, "status_code": 200, "timestamp": "2026-11-11T23:00:22.515+00:00"}
{"duration_ms": 121.54, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-2-2", "text_chars": 70, "text_tokens": 9}, "output": {"content_id": "28e1d0a6-19da-41a5-b554-30bf2d23b990", "guess": "human", "status": "decided"}, "request_id": "unit9-after-2-normal-2", "stage": "completed", "stage_durations_ms": {"detector": 114.00240399962058, "scoring": 0.008398004865739495, "stylometry": 0.07187300070654601}, "status_code": 200, "timestamp": "2026-11-11T23:00:22.646+00:00"}
{"duration_ms": 156.996, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-2-3", "text_chars": 66, "text_tokens": 11}, "output": {"content_id": "505678b3-10a8-45c2-a0f8-301d8378aecf", "guess": "human", "status": "decided"}, "request_id": "unit9-after-2-normal-3", "stage": "completed", "stage_durations_ms": {"detector": 147.81319499888923, "scoring": 0.007980001100804657, "stylometry": 0.11317399912513793}, "status_code": 200, "timestamp": "2026-11-11T23:00:22.812+00:00"}
{"duration_ms": 168.402, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-2-4", "text_chars": 66, "text_tokens": 10}, "output": {"content_id": "03ae7c02-37fe-402f-8f12-6d25f44a44ff", "guess": "human", "status": "decided"}, "request_id": "unit9-after-2-normal-4", "stage": "completed", "stage_durations_ms": {"detector": 153.64484299789183, "scoring": 0.008481998520437628, "stylometry": 0.09551099356031045}, "status_code": 200, "timestamp": "2026-11-11T23:00:22.990+00:00"}
{"duration_ms": 196.899, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-2-5", "text_chars": 69, "text_tokens": 11}, "output": {"content_id": "a6cb48f5-6749-46a2-bdd9-bd348bd4b418", "guess": "human", "status": "decided"}, "request_id": "unit9-after-2-normal-5", "stage": "completed", "stage_durations_ms": {"detector": 187.5708760053385, "scoring": 0.007246002496685833, "stylometry": 0.07449199620168656}, "status_code": 200, "timestamp": "2026-11-11T23:00:23.201+00:00"}
{"duration_ms": 134.903, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-2-6", "text_chars": 65, "text_tokens": 10}, "output": {"content_id": "aaa9bed6-70af-4fad-85ac-1f1d53641541", "guess": "human", "status": "decided"}, "request_id": "unit9-after-2-normal-6", "stage": "completed", "stage_durations_ms": {"detector": 126.21864499669755, "scoring": 0.00911600363906473, "stylometry": 0.09727400174597278}, "status_code": 200, "timestamp": "2026-11-11T23:00:23.345+00:00"}
{"duration_ms": 127.548, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-2-7", "text_chars": 67, "text_tokens": 9}, "output": {"content_id": "60518025-835c-4a6a-b7cb-b323f73bd6e5", "guess": "human", "status": "decided"}, "request_id": "unit9-after-2-normal-7", "stage": "completed", "stage_durations_ms": {"detector": 119.34519200440263, "scoring": 0.008600996807217598, "stylometry": 0.09386499732499942}, "status_code": 200, "timestamp": "2026-11-11T23:00:23.484+00:00"}
{"duration_ms": 128.211, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-2-8", "text_chars": 60, "text_tokens": 10}, "output": {"content_id": "a9c20b95-4ddf-4a39-91fd-2a04def35225", "guess": "human", "status": "decided"}, "request_id": "unit9-after-2-normal-8", "stage": "completed", "stage_durations_ms": {"detector": 120.00934200477786, "scoring": 0.008212999091483653, "stylometry": 0.0864690009620972}, "status_code": 200, "timestamp": "2026-11-11T23:00:23.621+00:00"}
{"duration_ms": 129.163, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-2-9", "text_chars": 67, "text_tokens": 10}, "output": {"content_id": "116d5804-fc95-4a28-a571-8e09c47401e4", "guess": "human", "status": "decided"}, "request_id": "unit9-after-2-normal-9", "stage": "completed", "stage_durations_ms": {"detector": 120.75714999809861, "scoring": 0.0066870052251033485, "stylometry": 0.07324499893002212}, "status_code": 200, "timestamp": "2026-11-11T23:00:23.760+00:00"}
{"duration_ms": 152.465, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-2-10", "text_chars": 69, "text_tokens": 10}, "output": {"content_id": "132b999b-9534-40e4-9559-ed9a7f14a2c8", "guess": "human", "status": "decided"}, "request_id": "unit9-after-2-normal-10", "stage": "completed", "stage_durations_ms": {"detector": 143.37546299793757, "scoring": 0.007901995559222996, "stylometry": 0.09356400551041588}, "status_code": 200, "timestamp": "2026-11-11T23:00:23.922+00:00"}
{"duration_ms": 0.09, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after-2-1", "text_chars": 70, "text_tokens": 9}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after-2-failure-1", "stage": "detector", "stage_durations_ms": {"detector": 0.051303002692293376}, "status_code": 503, "timestamp": "2026-11-11T23:00:23.933+00:00"}
{"duration_ms": 0.124, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after-2-2", "text_chars": 70, "text_tokens": 9}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after-2-failure-2", "stage": "detector", "stage_durations_ms": {"detector": 0.06705299892928451}, "status_code": 503, "timestamp": "2026-11-11T23:00:23.942+00:00"}
{"duration_ms": 0.073, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after-2-3", "text_chars": 66, "text_tokens": 11}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after-2-failure-3", "stage": "detector", "stage_durations_ms": {"detector": 0.038992999179754406}, "status_code": 503, "timestamp": "2026-11-11T23:00:23.952+00:00"}
{"duration_ms": 0.065, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after-2-4", "text_chars": 66, "text_tokens": 10}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after-2-failure-4", "stage": "detector", "stage_durations_ms": {"detector": 0.03235999611206353}, "status_code": 503, "timestamp": "2026-11-11T23:00:23.961+00:00"}
{"duration_ms": 0.078, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after-2-5", "text_chars": 69, "text_tokens": 11}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after-2-failure-5", "stage": "detector", "stage_durations_ms": {"detector": 0.04178900417173281}, "status_code": 503, "timestamp": "2026-11-11T23:00:23.972+00:00"}
```

## Audit summary

- New audit entries: `10`
- New decided entries: `10`
- Completed operational entries: `10`
- Failure operational entries: `5`
