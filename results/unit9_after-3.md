# Unit 9 Run — after-3

Started: `2026-11-11T23:00:37+00:00`

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

- Trial 1: `200` `{"confidence": 0.138, "content_id": "243f7c00-a849-4535-ac3d-974075a12b23", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0071, "request_id": "unit9-after-3-normal-1", "style_score": 0.3343}`
- Trial 2: `200` `{"confidence": 0.1412, "content_id": "58a85e68-656d-4995-88e1-c20e986a86ef", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0125, "request_id": "unit9-after-3-normal-2", "style_score": 0.3343}`
- Trial 3: `200` `{"confidence": 0.1693, "content_id": "ec919c4a-0c17-4d42-ab89-86534928e03e", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0228, "request_id": "unit9-after-3-normal-3", "style_score": 0.389}`
- Trial 4: `200` `{"confidence": 0.1547, "content_id": "756f98f9-d5b8-4a16-a1d7-a54b7d067e59", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0367, "request_id": "unit9-after-3-normal-4", "style_score": 0.3317}`
- Trial 5: `200` `{"confidence": 0.2761, "content_id": "fc51fa74-822b-447f-8758-a4023f25d361", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.2383, "request_id": "unit9-after-3-normal-5", "style_score": 0.3328}`
- Trial 6: `200` `{"confidence": 0.1401, "content_id": "50640223-e047-4109-b983-bf402d44a6cd", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0127, "request_id": "unit9-after-3-normal-6", "style_score": 0.3312}`
- Trial 7: `200` `{"confidence": 0.1419, "content_id": "65a5e34a-3e30-4078-ba3f-e09937ac0158", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0147, "request_id": "unit9-after-3-normal-7", "style_score": 0.3328}`
- Trial 8: `200` `{"confidence": 0.1781, "content_id": "fe8cb107-4291-49cb-8383-b6d262e79244", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0357, "request_id": "unit9-after-3-normal-8", "style_score": 0.3916}`
- Trial 9: `200` `{"confidence": 0.1426, "content_id": "551afddf-a492-4c3f-84b0-477116199e5c", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0162, "request_id": "unit9-after-3-normal-9", "style_score": 0.3323}`
- Trial 10: `200` `{"confidence": 0.1507, "content_id": "208bceb7-b5b6-4e27-8c80-610fd72b27d9", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0289, "request_id": "unit9-after-3-normal-10", "style_score": 0.3333}`

### Forced detector failures

- Trial 1: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after-3-failure-1"}`
- Trial 2: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after-3-failure-2"}`
- Trial 3: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after-3-failure-3"}`
- Trial 4: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after-3-failure-4"}`
- Trial 5: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after-3-failure-5"}`

## Operational log entries

```json
{"duration_ms": 157665.862, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-3-1", "text_chars": 70, "text_tokens": 9}, "output": {"content_id": "243f7c00-a849-4535-ac3d-974075a12b23", "guess": "human", "status": "decided"}, "request_id": "unit9-after-3-normal-1", "stage": "completed", "stage_durations_ms": {"detector": 157659.52159000153, "scoring": 0.016747006156947464, "stylometry": 0.43989400001009926}, "status_code": 200, "timestamp": "2026-11-11T23:03:04.881+00:00"}
{"duration_ms": 105.152, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-3-2", "text_chars": 70, "text_tokens": 9}, "output": {"content_id": "58a85e68-656d-4995-88e1-c20e986a86ef", "guess": "human", "status": "decided"}, "request_id": "unit9-after-3-normal-2", "stage": "completed", "stage_durations_ms": {"detector": 99.72528599610087, "scoring": 0.006740003300365061, "stylometry": 0.06462400051532313}, "status_code": 200, "timestamp": "2026-11-11T23:03:04.995+00:00"}
{"duration_ms": 149.819, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-3-3", "text_chars": 66, "text_tokens": 11}, "output": {"content_id": "ec919c4a-0c17-4d42-ab89-86534928e03e", "guess": "human", "status": "decided"}, "request_id": "unit9-after-3-normal-3", "stage": "completed", "stage_durations_ms": {"detector": 142.3532039989368, "scoring": 0.008741000783629715, "stylometry": 0.10210100299445912}, "status_code": 200, "timestamp": "2026-11-11T23:03:05.152+00:00"}
{"duration_ms": 139.989, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-3-4", "text_chars": 66, "text_tokens": 10}, "output": {"content_id": "756f98f9-d5b8-4a16-a1d7-a54b7d067e59", "guess": "human", "status": "decided"}, "request_id": "unit9-after-3-normal-4", "stage": "completed", "stage_durations_ms": {"detector": 131.21359499928076, "scoring": 0.012604999938048422, "stylometry": 0.08685499778948724}, "status_code": 200, "timestamp": "2026-11-11T23:03:05.301+00:00"}
{"duration_ms": 136.937, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-3-5", "text_chars": 69, "text_tokens": 11}, "output": {"content_id": "fc51fa74-822b-447f-8758-a4023f25d361", "guess": "human", "status": "decided"}, "request_id": "unit9-after-3-normal-5", "stage": "completed", "stage_durations_ms": {"detector": 128.76296800095588, "scoring": 0.00776100205257535, "stylometry": 0.08568399789510295}, "status_code": 200, "timestamp": "2026-11-11T23:03:05.447+00:00"}
{"duration_ms": 122.019, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-3-6", "text_chars": 65, "text_tokens": 10}, "output": {"content_id": "50640223-e047-4109-b983-bf402d44a6cd", "guess": "human", "status": "decided"}, "request_id": "unit9-after-3-normal-6", "stage": "completed", "stage_durations_ms": {"detector": 114.46481699385913, "scoring": 0.007579998055007309, "stylometry": 0.08977200195658952}, "status_code": 200, "timestamp": "2026-11-11T23:03:05.578+00:00"}
{"duration_ms": 191.322, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-3-7", "text_chars": 67, "text_tokens": 9}, "output": {"content_id": "65a5e34a-3e30-4078-ba3f-e09937ac0158", "guess": "human", "status": "decided"}, "request_id": "unit9-after-3-normal-7", "stage": "completed", "stage_durations_ms": {"detector": 182.34386899712263, "scoring": 0.011572999937925488, "stylometry": 0.10891399870160967}, "status_code": 200, "timestamp": "2026-11-11T23:03:05.779+00:00"}
{"duration_ms": 132.817, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-3-8", "text_chars": 60, "text_tokens": 10}, "output": {"content_id": "fe8cb107-4291-49cb-8383-b6d262e79244", "guess": "human", "status": "decided"}, "request_id": "unit9-after-3-normal-8", "stage": "completed", "stage_durations_ms": {"detector": 123.6238109995611, "scoring": 0.008591996447648853, "stylometry": 0.09151799895334989}, "status_code": 200, "timestamp": "2026-11-11T23:03:05.921+00:00"}
{"duration_ms": 135.393, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-3-9", "text_chars": 67, "text_tokens": 10}, "output": {"content_id": "551afddf-a492-4c3f-84b0-477116199e5c", "guess": "human", "status": "decided"}, "request_id": "unit9-after-3-normal-9", "stage": "completed", "stage_durations_ms": {"detector": 124.30226700234925, "scoring": 0.009155999578069896, "stylometry": 0.1046030010911636}, "status_code": 200, "timestamp": "2026-11-11T23:03:06.065+00:00"}
{"duration_ms": 142.297, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-3-10", "text_chars": 69, "text_tokens": 10}, "output": {"content_id": "208bceb7-b5b6-4e27-8c80-610fd72b27d9", "guess": "human", "status": "decided"}, "request_id": "unit9-after-3-normal-10", "stage": "completed", "stage_durations_ms": {"detector": 135.1413450029213, "scoring": 0.008390001312363893, "stylometry": 0.09970500104827806}, "status_code": 200, "timestamp": "2026-11-11T23:03:06.218+00:00"}
{"duration_ms": 0.108, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after-3-1", "text_chars": 70, "text_tokens": 9}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after-3-failure-1", "stage": "detector", "stage_durations_ms": {"detector": 0.05324299854692072}, "status_code": 503, "timestamp": "2026-11-11T23:03:06.228+00:00"}
{"duration_ms": 0.079, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after-3-2", "text_chars": 70, "text_tokens": 9}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after-3-failure-2", "stage": "detector", "stage_durations_ms": {"detector": 0.04340599843999371}, "status_code": 503, "timestamp": "2026-11-11T23:03:06.238+00:00"}
{"duration_ms": 0.068, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after-3-3", "text_chars": 66, "text_tokens": 11}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after-3-failure-3", "stage": "detector", "stage_durations_ms": {"detector": 0.03660299989860505}, "status_code": 503, "timestamp": "2026-11-11T23:03:06.248+00:00"}
{"duration_ms": 0.065, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after-3-4", "text_chars": 66, "text_tokens": 10}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after-3-failure-4", "stage": "detector", "stage_durations_ms": {"detector": 0.03226900298614055}, "status_code": 503, "timestamp": "2026-11-11T23:03:06.257+00:00"}
{"duration_ms": 0.074, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after-3-5", "text_chars": 69, "text_tokens": 11}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after-3-failure-5", "stage": "detector", "stage_durations_ms": {"detector": 0.03891300002578646}, "status_code": 503, "timestamp": "2026-11-11T23:03:06.266+00:00"}
```

## Audit summary

- New audit entries: `10`
- New decided entries: `10`
- Completed operational entries: `10`
- Failure operational entries: `5`
