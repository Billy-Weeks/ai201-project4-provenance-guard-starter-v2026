# Unit 9 Run — after2-3

Started: `2026-11-12T00:07:25+00:00`

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

- Trial 1: `200` `{"confidence": 0.138, "content_id": "d1d9ab11-2365-443f-8280-c00c2ae052bd", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0071, "request_id": "unit9-after2-3-normal-1", "style_score": 0.3343}`
- Trial 2: `200` `{"confidence": 0.1412, "content_id": "cae9f289-9bc3-4809-9b8d-f9bf0cad82cd", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0125, "request_id": "unit9-after2-3-normal-2", "style_score": 0.3343}`
- Trial 3: `200` `{"confidence": 0.1693, "content_id": "1eaa2831-108e-47a0-ba00-42d8e1afb0fa", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0228, "request_id": "unit9-after2-3-normal-3", "style_score": 0.389}`
- Trial 4: `200` `{"confidence": 0.1547, "content_id": "5f331c36-9ce5-4e63-be14-e2c659097203", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0367, "request_id": "unit9-after2-3-normal-4", "style_score": 0.3317}`
- Trial 5: `200` `{"confidence": 0.2761, "content_id": "f4b35cdb-b937-4957-9959-b4d29fc4aab4", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.2383, "request_id": "unit9-after2-3-normal-5", "style_score": 0.3328}`
- Trial 6: `200` `{"confidence": 0.1401, "content_id": "3e9cbd2f-816a-4646-9126-b9b015646804", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0127, "request_id": "unit9-after2-3-normal-6", "style_score": 0.3312}`
- Trial 7: `200` `{"confidence": 0.1419, "content_id": "e3beab82-d4cb-4075-8b9b-5f1fa9589a0e", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0147, "request_id": "unit9-after2-3-normal-7", "style_score": 0.3328}`
- Trial 8: `200` `{"confidence": 0.1781, "content_id": "278ee1fe-fdbd-45ad-8122-b47469441345", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0357, "request_id": "unit9-after2-3-normal-8", "style_score": 0.3916}`
- Trial 9: `200` `{"confidence": 0.1426, "content_id": "966b87fe-8e75-459c-a118-264b554794f7", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0162, "request_id": "unit9-after2-3-normal-9", "style_score": 0.3323}`
- Trial 10: `200` `{"confidence": 0.1507, "content_id": "48ae1e9b-e1f9-4e5d-81fe-32ebec349ee1", "guess": "human", "label": "We think this was probably written by a person. If this is your work, no action is needed.", "model_score": 0.0289, "request_id": "unit9-after2-3-normal-10", "style_score": 0.3333}`

### Forced detector failures

- Trial 1: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after2-3-failure-1"}`
- Trial 2: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after2-3-failure-2"}`
- Trial 3: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after2-3-failure-3"}`
- Trial 4: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after2-3-failure-4"}`
- Trial 5: `503` `{"error": "detector_unavailable", "message": "The detector is temporarily unavailable. Try again later.", "request_id": "unit9-after2-3-failure-5"}`

## Operational log entries

```json
{"duration_ms": 455.79, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-3-1", "text_chars": 70, "text_tokens": 9}, "output": {"content_id": "d1d9ab11-2365-443f-8280-c00c2ae052bd", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-3-normal-1", "stage": "completed", "stage_durations_ms": {"detector": 447.990407999896, "scoring": 0.010329997166991234, "stylometry": 0.31152800511335954}, "status_code": 200, "timestamp": "2026-11-12T00:07:26.414+00:00"}
{"duration_ms": 118.778, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-3-2", "text_chars": 70, "text_tokens": 9}, "output": {"content_id": "cae9f289-9bc3-4809-9b8d-f9bf0cad82cd", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-3-normal-2", "stage": "completed", "stage_durations_ms": {"detector": 107.69848299969453, "scoring": 0.01086299744201824, "stylometry": 0.10616600047796965}, "status_code": 200, "timestamp": "2026-11-12T00:07:26.544+00:00"}
{"duration_ms": 147.992, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-3-3", "text_chars": 66, "text_tokens": 11}, "output": {"content_id": "1eaa2831-108e-47a0-ba00-42d8e1afb0fa", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-3-normal-3", "stage": "completed", "stage_durations_ms": {"detector": 139.71833500545472, "scoring": 0.008757997420616448, "stylometry": 0.11302699567750096}, "status_code": 200, "timestamp": "2026-11-12T00:07:26.700+00:00"}
{"duration_ms": 126.952, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-3-4", "text_chars": 66, "text_tokens": 10}, "output": {"content_id": "5f331c36-9ce5-4e63-be14-e2c659097203", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-3-normal-4", "stage": "completed", "stage_durations_ms": {"detector": 119.14818900550017, "scoring": 0.008875998901203275, "stylometry": 0.10470899724168703}, "status_code": 200, "timestamp": "2026-11-12T00:07:26.838+00:00"}
{"duration_ms": 132.541, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-3-5", "text_chars": 69, "text_tokens": 11}, "output": {"content_id": "f4b35cdb-b937-4957-9959-b4d29fc4aab4", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-3-normal-5", "stage": "completed", "stage_durations_ms": {"detector": 125.20081700495211, "scoring": 0.00664399703964591, "stylometry": 0.07456100138369948}, "status_code": 200, "timestamp": "2026-11-12T00:07:26.979+00:00"}
{"duration_ms": 140.484, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-3-6", "text_chars": 65, "text_tokens": 10}, "output": {"content_id": "3e9cbd2f-816a-4646-9126-b9b015646804", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-3-normal-6", "stage": "completed", "stage_durations_ms": {"detector": 130.70061700273072, "scoring": 0.01117299689212814, "stylometry": 0.13007000234210864}, "status_code": 200, "timestamp": "2026-11-12T00:07:27.130+00:00"}
{"duration_ms": 132.558, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-3-7", "text_chars": 67, "text_tokens": 9}, "output": {"content_id": "e3beab82-d4cb-4075-8b9b-5f1fa9589a0e", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-3-normal-7", "stage": "completed", "stage_durations_ms": {"detector": 124.47142499877373, "scoring": 0.04176099901087582, "stylometry": 0.0918079967959784}, "status_code": 200, "timestamp": "2026-11-12T00:07:27.273+00:00"}
{"duration_ms": 133.411, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-3-8", "text_chars": 60, "text_tokens": 10}, "output": {"content_id": "278ee1fe-fdbd-45ad-8122-b47469441345", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-3-normal-8", "stage": "completed", "stage_durations_ms": {"detector": 125.37425699701998, "scoring": 0.007973998435772955, "stylometry": 0.07899299816926941}, "status_code": 200, "timestamp": "2026-11-12T00:07:27.414+00:00"}
{"duration_ms": 120.691, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-3-9", "text_chars": 67, "text_tokens": 10}, "output": {"content_id": "966b87fe-8e75-459c-a118-264b554794f7", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-3-normal-9", "stage": "completed", "stage_durations_ms": {"detector": 112.95361399970716, "scoring": 0.008414004696533084, "stylometry": 0.09938499715644866}, "status_code": 200, "timestamp": "2026-11-12T00:07:27.544+00:00"}
{"duration_ms": 128.659, "error_type": null, "event": "submission_completed", "input": {"creator_id": "unit9-normal-after2-3-10", "text_chars": 69, "text_tokens": 10}, "output": {"content_id": "48ae1e9b-e1f9-4e5d-81fe-32ebec349ee1", "guess": "human", "status": "decided"}, "request_id": "unit9-after2-3-normal-10", "stage": "completed", "stage_durations_ms": {"detector": 120.96419600129593, "scoring": 0.009069000952877104, "stylometry": 0.11143899610033259}, "status_code": 200, "timestamp": "2026-11-12T00:07:27.680+00:00"}
{"duration_ms": 0.107, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after2-3-1", "text_chars": 70, "text_tokens": 9}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after2-3-failure-1", "stage": "detector", "stage_durations_ms": {"detector": 0.05995399988023564}, "status_code": 503, "timestamp": "2026-11-12T00:07:27.689+00:00"}
{"duration_ms": 0.055, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after2-3-2", "text_chars": 70, "text_tokens": 9}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after2-3-failure-2", "stage": "detector", "stage_durations_ms": {"detector": 0.02865699934773147}, "status_code": 503, "timestamp": "2026-11-12T00:07:27.696+00:00"}
{"duration_ms": 0.083, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after2-3-3", "text_chars": 66, "text_tokens": 11}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after2-3-failure-3", "stage": "detector", "stage_durations_ms": {"detector": 0.04559299850370735}, "status_code": 503, "timestamp": "2026-11-12T00:07:27.704+00:00"}
{"duration_ms": 0.045, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after2-3-4", "text_chars": 66, "text_tokens": 10}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after2-3-failure-4", "stage": "detector", "stage_durations_ms": {"detector": 0.023439999495167285}, "status_code": 503, "timestamp": "2026-11-12T00:07:27.710+00:00"}
{"duration_ms": 0.08, "error_type": "DetectorUnavailable", "event": "scoring_failed", "input": {"creator_id": "unit9-failure-after2-3-5", "text_chars": 69, "text_tokens": 11}, "output": {"error": "detector_unavailable"}, "request_id": "unit9-after2-3-failure-5", "stage": "detector", "stage_durations_ms": {"detector": 0.043425003241281956}, "status_code": 503, "timestamp": "2026-11-12T00:07:27.719+00:00"}
```

## Audit summary

- New audit entries: `10`
- New decided entries: `10`
- Completed operational entries: `10`
- Failure operational entries: `5`
