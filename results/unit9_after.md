# Unit 9 Run — after

Started: `2026-11-11T04:25:17+00:00`

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

- Trial 1: `200` `{"confidence": 0.138, "content_id": "145c832a-b464-4c90-bd0a-cb297aa31444", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0071, "request_id": "unit9-after-normal-1", "style_score": 0.3343}`
- Trial 2: `200` `{"confidence": 0.1412, "content_id": "ac325346-dffa-4e1c-be18-18c92b6a73f6", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0125, "request_id": "unit9-after-normal-2", "style_score": 0.3343}`
- Trial 3: `200` `{"confidence": 0.1693, "content_id": "057d74e6-e56b-4b90-ae23-5d85ef4ed49f", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0228, "request_id": "unit9-after-normal-3", "style_score": 0.389}`
- Trial 4: `200` `{"confidence": 0.1547, "content_id": "2f0379f4-f62b-494c-801d-9e7a0949621c", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0367, "request_id": "unit9-after-normal-4", "style_score": 0.3317}`
- Trial 5: `200` `{"confidence": 0.2761, "content_id": "b941f2e1-14d7-46dc-8506-c36e280ee7f6", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.2383, "request_id": "unit9-after-normal-5", "style_score": 0.3328}`
- Trial 6: `200` `{"confidence": 0.1401, "content_id": "254cebf2-0362-4532-997d-8a773f726112", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0127, "request_id": "unit9-after-normal-6", "style_score": 0.3312}`
- Trial 7: `200` `{"confidence": 0.1419, "content_id": "f788a670-11d2-4c45-9768-cad2163288df", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0147, "request_id": "unit9-after-normal-7", "style_score": 0.3328}`
- Trial 8: `200` `{"confidence": 0.1781, "content_id": "68deb32f-31c9-4abb-a57d-7edc9d36bd5c", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0357, "request_id": "unit9-after-normal-8", "style_score": 0.3916}`
- Trial 9: `200` `{"confidence": 0.1426, "content_id": "c1315712-69fd-4135-8468-3e4bb7ad5e3d", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0162, "request_id": "unit9-after-normal-9", "style_score": 0.3323}`
- Trial 10: `200` `{"confidence": 0.1507, "content_id": "bd8d3d3d-79c3-4a27-8e32-8c24cc383ea7", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0289, "request_id": "unit9-after-normal-10", "style_score": 0.3333}`

### Forced detector failures

- Trial 1: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after-failure-1"}`
- Trial 2: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after-failure-2"}`
- Trial 3: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after-failure-3"}`
- Trial 4: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after-failure-4"}`
- Trial 5: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after-failure-5"}`

## Operational log entries

```json
{"duration_ms": 231059.562, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-1", "text_chars": 70, "text_tokens": 9}, "output": {"content_id": "145c832a-b464-4c90-bd0a-cb297aa31444", "guess": "human", "status": "decided"}, "request_id": "unit9-after-normal-1", "stage": "completed", "stage_durations_ms": {"detector": 231047.70447099872, "scoring": 0.011382995580788702, "stylometry": 0.4828509991057217}, "status_code": 200, "timestamp": "2026-11-11T04:28:55.573+00:00"}
{"duration_ms": 114.872, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-2", "text_chars": 70, "text_tokens": 9}, "output": {"content_id": "ac325346-dffa-4e1c-be18-18c92b6a73f6", "guess": "human", "status": "decided"}, "request_id": "unit9-after-normal-2", "stage": "completed", "stage_durations_ms": {"detector": 107.57670400198549, "scoring": 0.008235998393502086, "stylometry": 0.07836200529709458}, "status_code": 200, "timestamp": "2026-11-11T04:28:55.703+00:00"}
{"duration_ms": 146.706, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-3", "text_chars": 66, "text_tokens": 11}, "output": {"content_id": "057d74e6-e56b-4b90-ae23-5d85ef4ed49f", "guess": "human", "status": "decided"}, "request_id": "unit9-after-normal-3", "stage": "completed", "stage_durations_ms": {"detector": 138.46206000016537, "scoring": 0.006201000360306352, "stylometry": 0.07209800241980702}, "status_code": 200, "timestamp": "2026-11-11T04:28:55.859+00:00"}
{"duration_ms": 133.233, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-4", "text_chars": 66, "text_tokens": 10}, "output": {"content_id": "2f0379f4-f62b-494c-801d-9e7a0949621c", "guess": "human", "status": "decided"}, "request_id": "unit9-after-normal-4", "stage": "completed", "stage_durations_ms": {"detector": 125.22401299793273, "scoring": 0.005829002475365996, "stylometry": 0.07080400246195495}, "status_code": 200, "timestamp": "2026-11-11T04:28:56.002+00:00"}
{"duration_ms": 129.171, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-5", "text_chars": 69, "text_tokens": 11}, "output": {"content_id": "b941f2e1-14d7-46dc-8506-c36e280ee7f6", "guess": "human", "status": "decided"}, "request_id": "unit9-after-normal-5", "stage": "completed", "stage_durations_ms": {"detector": 121.34789599804208, "scoring": 0.00713299959897995, "stylometry": 0.09516299905953929}, "status_code": 200, "timestamp": "2026-11-11T04:28:56.142+00:00"}
{"duration_ms": 124.305, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-6", "text_chars": 65, "text_tokens": 10}, "output": {"content_id": "254cebf2-0362-4532-997d-8a773f726112", "guess": "human", "status": "decided"}, "request_id": "unit9-after-normal-6", "stage": "completed", "stage_durations_ms": {"detector": 116.89607000153046, "scoring": 0.006212001608218998, "stylometry": 0.07084700337145478}, "status_code": 200, "timestamp": "2026-11-11T04:28:56.276+00:00"}
{"duration_ms": 134.068, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-7", "text_chars": 67, "text_tokens": 9}, "output": {"content_id": "f788a670-11d2-4c45-9768-cad2163288df", "guess": "human", "status": "decided"}, "request_id": "unit9-after-normal-7", "stage": "completed", "stage_durations_ms": {"detector": 119.36915299884276, "scoring": 0.007673996151424944, "stylometry": 0.1029740014928393}, "status_code": 200, "timestamp": "2026-11-11T04:28:56.419+00:00"}
{"duration_ms": 134.906, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-8", "text_chars": 60, "text_tokens": 10}, "output": {"content_id": "68deb32f-31c9-4abb-a57d-7edc9d36bd5c", "guess": "human", "status": "decided"}, "request_id": "unit9-after-normal-8", "stage": "completed", "stage_durations_ms": {"detector": 126.30839199846378, "scoring": 0.008087001333478838, "stylometry": 0.09269299334846437}, "status_code": 200, "timestamp": "2026-11-11T04:28:56.565+00:00"}
{"duration_ms": 152.109, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-9", "text_chars": 67, "text_tokens": 10}, "output": {"content_id": "c1315712-69fd-4135-8468-3e4bb7ad5e3d", "guess": "human", "status": "decided"}, "request_id": "unit9-after-normal-9", "stage": "completed", "stage_durations_ms": {"detector": 141.4511799957836, "scoring": 0.00660399382468313, "stylometry": 0.0869899959070608}, "status_code": 200, "timestamp": "2026-11-11T04:28:56.743+00:00"}
{"duration_ms": 179.831, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after-10", "text_chars": 69, "text_tokens": 10}, "output": {"content_id": "bd8d3d3d-79c3-4a27-8e32-8c24cc383ea7", "guess": "human", "status": "decided"}, "request_id": "unit9-after-normal-10", "stage": "completed", "stage_durations_ms": {"detector": 170.82418099744245, "scoring": 0.008342001819983125, "stylometry": 0.15307899593608454}, "status_code": 200, "timestamp": "2026-11-11T04:28:56.934+00:00"}
{"duration_ms": 0.102, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after-1", "text_chars": 70, "text_tokens": 9}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after-failure-1", "stage": "detector", "stage_durations_ms": {"detector": 0.059569996665231884}, "status_code": 503, "timestamp": "2026-11-11T04:28:56.945+00:00"}
{"duration_ms": 0.081, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after-2", "text_chars": 70, "text_tokens": 9}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after-failure-2", "stage": "detector", "stage_durations_ms": {"detector": 0.044262997107580304}, "status_code": 503, "timestamp": "2026-11-11T04:28:56.955+00:00"}
{"duration_ms": 0.077, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after-3", "text_chars": 66, "text_tokens": 11}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after-failure-3", "stage": "detector", "stage_durations_ms": {"detector": 0.03961100446758792}, "status_code": 503, "timestamp": "2026-11-11T04:28:56.965+00:00"}
{"duration_ms": 0.071, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after-4", "text_chars": 66, "text_tokens": 10}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after-failure-4", "stage": "detector", "stage_durations_ms": {"detector": 0.034830001823138446}, "status_code": 503, "timestamp": "2026-11-11T04:28:56.974+00:00"}
{"duration_ms": 0.122, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after-5", "text_chars": 69, "text_tokens": 11}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after-failure-5", "stage": "detector", "stage_durations_ms": {"detector": 0.043320003896951675}, "status_code": 503, "timestamp": "2026-11-11T04:28:56.984+00:00"}
```

## Audit summary

- New audit entries: `10`
- New decided entries: `10`
- Completed operational entries: `10`
- Failure operational entries: `5`
