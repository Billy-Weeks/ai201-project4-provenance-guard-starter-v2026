# Unit 9 Run — after2-2

Started: `2026-11-12T00:05:13+00:00`

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

- Trial 1: `200` `{"confidence": 0.138, "content_id": "372fd9c4-564e-4074-94df-37725bf32042", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0071, "request_id": "unit9-after2-2-normal-1", "style_score": 0.3343}`
- Trial 2: `200` `{"confidence": 0.1412, "content_id": "13b8d573-f5d7-48c5-99f1-ca2310962d94", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0125, "request_id": "unit9-after2-2-normal-2", "style_score": 0.3343}`
- Trial 3: `200` `{"confidence": 0.1693, "content_id": "7fd850f5-e49e-456b-bc87-67d7eb803a55", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0228, "request_id": "unit9-after2-2-normal-3", "style_score": 0.389}`
- Trial 4: `200` `{"confidence": 0.1547, "content_id": "b95d6ecc-1791-4fdd-a6bd-978c80de478f", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0367, "request_id": "unit9-after2-2-normal-4", "style_score": 0.3317}`
- Trial 5: `200` `{"confidence": 0.2761, "content_id": "df69d583-5312-45da-983e-9fd01b5c6bf5", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.2383, "request_id": "unit9-after2-2-normal-5", "style_score": 0.3328}`
- Trial 6: `200` `{"confidence": 0.1401, "content_id": "c1384d77-d159-479f-9fec-27a4f95b5987", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0127, "request_id": "unit9-after2-2-normal-6", "style_score": 0.3312}`
- Trial 7: `200` `{"confidence": 0.1419, "content_id": "fb5fb3b5-d0d1-411f-87f3-44c01069c436", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0147, "request_id": "unit9-after2-2-normal-7", "style_score": 0.3328}`
- Trial 8: `200` `{"confidence": 0.1781, "content_id": "10100857-973c-417f-904c-c3d0496648cb", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0357, "request_id": "unit9-after2-2-normal-8", "style_score": 0.3916}`
- Trial 9: `200` `{"confidence": 0.1426, "content_id": "3c0c91ac-20a8-41fc-99d0-3762d3dbf47f", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0162, "request_id": "unit9-after2-2-normal-9", "style_score": 0.3323}`
- Trial 10: `200` `{"confidence": 0.1507, "content_id": "a0c8d6ce-62b8-4962-bcfd-e69a9e295900", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0289, "request_id": "unit9-after2-2-normal-10", "style_score": 0.3333}`

### Forced detector failures

- Trial 1: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after2-2-failure-1"}`
- Trial 2: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after2-2-failure-2"}`
- Trial 3: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after2-2-failure-3"}`
- Trial 4: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after2-2-failure-4"}`
- Trial 5: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after2-2-failure-5"}`

## Operational log entries

```json
{"duration_ms": 615.609, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-2-1", "text_chars": 70, "text_tokens": 9}, "output": {"content_id": "372fd9c4-564e-4074-94df-37725bf32042", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-2-normal-1", "stage": "completed", "stage_durations_ms": {"detector": 608.1867629982298, "scoring": 0.014823002857156098, "stylometry": 0.4159029995207675}, "status_code": 200, "timestamp": "2026-11-12T00:05:13.862+00:00"}
{"duration_ms": 120.743, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-2-2", "text_chars": 70, "text_tokens": 9}, "output": {"content_id": "13b8d573-f5d7-48c5-99f1-ca2310962d94", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-2-normal-2", "stage": "completed", "stage_durations_ms": {"detector": 109.46228200191399, "scoring": 0.011716001608874649, "stylometry": 0.11046500003430992}, "status_code": 200, "timestamp": "2026-11-12T00:05:13.993+00:00"}
{"duration_ms": 149.458, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-2-3", "text_chars": 66, "text_tokens": 11}, "output": {"content_id": "7fd850f5-e49e-456b-bc87-67d7eb803a55", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-2-normal-3", "stage": "completed", "stage_durations_ms": {"detector": 137.0832190004876, "scoring": 0.01503300154581666, "stylometry": 0.24280600337078795}, "status_code": 200, "timestamp": "2026-11-12T00:05:14.151+00:00"}
{"duration_ms": 153.62, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-2-4", "text_chars": 66, "text_tokens": 10}, "output": {"content_id": "b95d6ecc-1791-4fdd-a6bd-978c80de478f", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-2-normal-4", "stage": "completed", "stage_durations_ms": {"detector": 143.2093069961411, "scoring": 0.00942299811867997, "stylometry": 0.11588699999265373}, "status_code": 200, "timestamp": "2026-11-12T00:05:14.318+00:00"}
{"duration_ms": 150.574, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-2-5", "text_chars": 69, "text_tokens": 11}, "output": {"content_id": "df69d583-5312-45da-983e-9fd01b5c6bf5", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-2-normal-5", "stage": "completed", "stage_durations_ms": {"detector": 141.52992699382594, "scoring": 0.00853099481901154, "stylometry": 0.08718800381757319}, "status_code": 200, "timestamp": "2026-11-12T00:05:14.481+00:00"}
{"duration_ms": 141.888, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-2-6", "text_chars": 65, "text_tokens": 10}, "output": {"content_id": "c1384d77-d159-479f-9fec-27a4f95b5987", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-2-normal-6", "stage": "completed", "stage_durations_ms": {"detector": 132.1483520005131, "scoring": 0.010007002856582403, "stylometry": 0.11543500295374542}, "status_code": 200, "timestamp": "2026-11-12T00:05:14.633+00:00"}
{"duration_ms": 136.255, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-2-7", "text_chars": 67, "text_tokens": 9}, "output": {"content_id": "fb5fb3b5-d0d1-411f-87f3-44c01069c436", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-2-normal-7", "stage": "completed", "stage_durations_ms": {"detector": 127.63329000154044, "scoring": 0.010162002581637353, "stylometry": 0.10871200356632471}, "status_code": 200, "timestamp": "2026-11-12T00:05:14.780+00:00"}
{"duration_ms": 141.3, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-2-8", "text_chars": 60, "text_tokens": 10}, "output": {"content_id": "10100857-973c-417f-904c-c3d0496648cb", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-2-normal-8", "stage": "completed", "stage_durations_ms": {"detector": 132.55315000424162, "scoring": 0.0077260046964511275, "stylometry": 0.07787499635014683}, "status_code": 200, "timestamp": "2026-11-12T00:05:14.932+00:00"}
{"duration_ms": 136.905, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-2-9", "text_chars": 67, "text_tokens": 10}, "output": {"content_id": "3c0c91ac-20a8-41fc-99d0-3762d3dbf47f", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-2-normal-9", "stage": "completed", "stage_durations_ms": {"detector": 127.54823700379347, "scoring": 0.009069997759070247, "stylometry": 0.11423399701016024}, "status_code": 200, "timestamp": "2026-11-12T00:05:15.079+00:00"}
{"duration_ms": 134.915, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-2-10", "text_chars": 69, "text_tokens": 10}, "output": {"content_id": "a0c8d6ce-62b8-4962-bcfd-e69a9e295900", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-2-normal-10", "stage": "completed", "stage_durations_ms": {"detector": 126.81394499668386, "scoring": 0.008938004611991346, "stylometry": 0.09568499808665365}, "status_code": 200, "timestamp": "2026-11-12T00:05:15.223+00:00"}
{"duration_ms": 0.141, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after2-2-1", "text_chars": 70, "text_tokens": 9}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after2-2-failure-1", "stage": "detector", "stage_durations_ms": {"detector": 0.08355099998880178}, "status_code": 503, "timestamp": "2026-11-12T00:05:15.233+00:00"}
{"duration_ms": 0.069, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after2-2-2", "text_chars": 70, "text_tokens": 9}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after2-2-failure-2", "stage": "detector", "stage_durations_ms": {"detector": 0.03696500061778352}, "status_code": 503, "timestamp": "2026-11-12T00:05:15.242+00:00"}
{"duration_ms": 0.079, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after2-2-3", "text_chars": 66, "text_tokens": 11}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after2-2-failure-3", "stage": "detector", "stage_durations_ms": {"detector": 0.03868399653583765}, "status_code": 503, "timestamp": "2026-11-12T00:05:15.251+00:00"}
{"duration_ms": 0.056, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after2-2-4", "text_chars": 66, "text_tokens": 10}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after2-2-failure-4", "stage": "detector", "stage_durations_ms": {"detector": 0.029668997740373015}, "status_code": 503, "timestamp": "2026-11-12T00:05:15.258+00:00"}
{"duration_ms": 0.063, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after2-2-5", "text_chars": 69, "text_tokens": 11}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after2-2-failure-5", "stage": "detector", "stage_durations_ms": {"detector": 0.03264400584157556}, "status_code": 503, "timestamp": "2026-11-12T00:05:15.267+00:00"}
```

## Audit summary

- New audit entries: `10`
- New decided entries: `10`
- Completed operational entries: `10`
- Failure operational entries: `5`
