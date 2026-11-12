# Unit 9 Run — after2-1

Started: `2026-11-12T00:02:57+00:00`

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

- Trial 1: `200` `{"confidence": 0.138, "content_id": "e96810fb-12e7-41fd-8ba4-349ce33c8777", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0071, "request_id": "unit9-after2-1-normal-1", "style_score": 0.3343}`
- Trial 2: `200` `{"confidence": 0.1412, "content_id": "7930eb5d-f87e-4653-8e3d-2e85d1f40804", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0125, "request_id": "unit9-after2-1-normal-2", "style_score": 0.3343}`
- Trial 3: `200` `{"confidence": 0.1693, "content_id": "69da219d-3fc1-415b-b8de-d8c2b391a88f", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0228, "request_id": "unit9-after2-1-normal-3", "style_score": 0.389}`
- Trial 4: `200` `{"confidence": 0.1547, "content_id": "ec48e8f5-ee4e-47a2-9ed2-e977e8ef29f0", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0367, "request_id": "unit9-after2-1-normal-4", "style_score": 0.3317}`
- Trial 5: `200` `{"confidence": 0.2761, "content_id": "e88123ff-303e-4271-8080-b8ddc87fcca1", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.2383, "request_id": "unit9-after2-1-normal-5", "style_score": 0.3328}`
- Trial 6: `200` `{"confidence": 0.1401, "content_id": "d1332799-b233-417b-961e-1d9e05be1de0", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0127, "request_id": "unit9-after2-1-normal-6", "style_score": 0.3312}`
- Trial 7: `200` `{"confidence": 0.1419, "content_id": "0da5ff6e-b660-4783-8482-40743218faf7", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0147, "request_id": "unit9-after2-1-normal-7", "style_score": 0.3328}`
- Trial 8: `200` `{"confidence": 0.1781, "content_id": "c30479b6-3b81-40f9-8c14-a5c7945dd3c5", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0357, "request_id": "unit9-after2-1-normal-8", "style_score": 0.3916}`
- Trial 9: `200` `{"confidence": 0.1426, "content_id": "b84de390-c86e-4860-9972-d715ec606267", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0162, "request_id": "unit9-after2-1-normal-9", "style_score": 0.3323}`
- Trial 10: `200` `{"confidence": 0.1507, "content_id": "5eb09e70-15b4-4fcf-88d0-76bc65b55113", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0289, "request_id": "unit9-after2-1-normal-10", "style_score": 0.3333}`

### Forced detector failures

- Trial 1: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after2-1-failure-1"}`
- Trial 2: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after2-1-failure-2"}`
- Trial 3: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after2-1-failure-3"}`
- Trial 4: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after2-1-failure-4"}`
- Trial 5: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after2-1-failure-5"}`

## Operational log entries

```json
{"duration_ms": 609.109, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-1-1", "text_chars": 70, "text_tokens": 9}, "output": {"content_id": "e96810fb-12e7-41fd-8ba4-349ce33c8777", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-1-normal-1", "stage": "completed", "stage_durations_ms": {"detector": 601.661894004792, "scoring": 0.010241994459647685, "stylometry": 0.30520300060743466}, "status_code": 200, "timestamp": "2026-11-12T00:02:57.733+00:00"}
{"duration_ms": 118.495, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-1-2", "text_chars": 70, "text_tokens": 9}, "output": {"content_id": "7930eb5d-f87e-4653-8e3d-2e85d1f40804", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-1-normal-2", "stage": "completed", "stage_durations_ms": {"detector": 107.05374799726997, "scoring": 0.009242001397069544, "stylometry": 0.08682799671078101}, "status_code": 200, "timestamp": "2026-11-12T00:02:57.860+00:00"}
{"duration_ms": 147.478, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-1-3", "text_chars": 66, "text_tokens": 11}, "output": {"content_id": "69da219d-3fc1-415b-b8de-d8c2b391a88f", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-1-normal-3", "stage": "completed", "stage_durations_ms": {"detector": 138.9497409982141, "scoring": 0.0068350054789334536, "stylometry": 0.0798639957793057}, "status_code": 200, "timestamp": "2026-11-12T00:02:58.017+00:00"}
{"duration_ms": 140.087, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-1-4", "text_chars": 66, "text_tokens": 10}, "output": {"content_id": "ec48e8f5-ee4e-47a2-9ed2-e977e8ef29f0", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-1-normal-4", "stage": "completed", "stage_durations_ms": {"detector": 131.5785600017989, "scoring": 0.0065990025177598, "stylometry": 0.07517799531342462}, "status_code": 200, "timestamp": "2026-11-12T00:02:58.167+00:00"}
{"duration_ms": 143.191, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-1-5", "text_chars": 69, "text_tokens": 11}, "output": {"content_id": "e88123ff-303e-4271-8080-b8ddc87fcca1", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-1-normal-5", "stage": "completed", "stage_durations_ms": {"detector": 134.74820999545045, "scoring": 0.008372997399419546, "stylometry": 0.09946600039256737}, "status_code": 200, "timestamp": "2026-11-12T00:02:58.320+00:00"}
{"duration_ms": 152.093, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-1-6", "text_chars": 65, "text_tokens": 10}, "output": {"content_id": "d1332799-b233-417b-961e-1d9e05be1de0", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-1-normal-6", "stage": "completed", "stage_durations_ms": {"detector": 137.59907799976645, "scoring": 0.008586997864767909, "stylometry": 0.10432500130264089}, "status_code": 200, "timestamp": "2026-11-12T00:02:58.482+00:00"}
{"duration_ms": 201.166, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-1-7", "text_chars": 67, "text_tokens": 9}, "output": {"content_id": "0da5ff6e-b660-4783-8482-40743218faf7", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-1-normal-7", "stage": "completed", "stage_durations_ms": {"detector": 189.0190209960565, "scoring": 0.010225994628854096, "stylometry": 0.15441200230270624}, "status_code": 200, "timestamp": "2026-11-12T00:02:58.695+00:00"}
{"duration_ms": 167.339, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-1-8", "text_chars": 60, "text_tokens": 10}, "output": {"content_id": "c30479b6-3b81-40f9-8c14-a5c7945dd3c5", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-1-normal-8", "stage": "completed", "stage_durations_ms": {"detector": 156.05825500097126, "scoring": 0.008957002137321979, "stylometry": 0.12252099986653775}, "status_code": 200, "timestamp": "2026-11-12T00:02:58.874+00:00"}
{"duration_ms": 156.207, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-1-9", "text_chars": 67, "text_tokens": 10}, "output": {"content_id": "b84de390-c86e-4860-9972-d715ec606267", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-1-normal-9", "stage": "completed", "stage_durations_ms": {"detector": 141.39201900252374, "scoring": 0.00821400317363441, "stylometry": 0.09847099863691255}, "status_code": 200, "timestamp": "2026-11-12T00:02:59.040+00:00"}
{"duration_ms": 148.363, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-1-10", "text_chars": 69, "text_tokens": 10}, "output": {"content_id": "5eb09e70-15b4-4fcf-88d0-76bc65b55113", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-1-normal-10", "stage": "completed", "stage_durations_ms": {"detector": 139.1567850005231, "scoring": 0.00855499820318073, "stylometry": 0.1046270044753328}, "status_code": 200, "timestamp": "2026-11-12T00:02:59.200+00:00"}
{"duration_ms": 0.108, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after2-1-1", "text_chars": 70, "text_tokens": 9}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after2-1-failure-1", "stage": "detector", "stage_durations_ms": {"detector": 0.06201399810379371}, "status_code": 503, "timestamp": "2026-11-12T00:02:59.211+00:00"}
{"duration_ms": 0.128, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after2-1-2", "text_chars": 70, "text_tokens": 9}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after2-1-failure-2", "stage": "detector", "stage_durations_ms": {"detector": 0.04747400089399889}, "status_code": 503, "timestamp": "2026-11-12T00:02:59.222+00:00"}
{"duration_ms": 0.08, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after2-1-3", "text_chars": 66, "text_tokens": 11}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after2-1-failure-3", "stage": "detector", "stage_durations_ms": {"detector": 0.04228400212014094}, "status_code": 503, "timestamp": "2026-11-12T00:02:59.231+00:00"}
{"duration_ms": 0.09, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after2-1-4", "text_chars": 66, "text_tokens": 10}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after2-1-failure-4", "stage": "detector", "stage_durations_ms": {"detector": 0.042571002268232405}, "status_code": 503, "timestamp": "2026-11-12T00:02:59.240+00:00"}
{"duration_ms": 0.112, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after2-1-5", "text_chars": 69, "text_tokens": 11}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after2-1-failure-5", "stage": "detector", "stage_durations_ms": {"detector": 0.05378900095820427}, "status_code": 503, "timestamp": "2026-11-12T00:02:59.250+00:00"}
```

## Audit summary

- New audit entries: `10`
- New decided entries: `10`
- Completed operational entries: `10`
- Failure operational entries: `5`
