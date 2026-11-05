# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 17:19
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `a2f9254d-7d42-42a9-9369-c5d6111828df` | human | 0.340 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `f8e361a1-cc02-4c9c-9a88-5d4c764e9970` | unsure | 0.479 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `10b7c63e-c693-4ea2-a216-2d48220d02d5` | unsure | 0.590 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `d0d99dc3-f111-4898-9a9e-66ca1c9d9adc` | unsure | 0.605 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `79aee5a5-2d06-4d3e-bb36-e5d841b8c31a` | human | 0.350 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `2aa75669-9ac7-48d2-861d-b978d287ef62` | unsure | 0.453 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `cef76e49-eb8e-4b45-9ed3-102ae883233e` | unsure | 0.630 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `d47cb1ce-cd8f-401e-8abe-091ec79dcadc` | human | 0.342 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `7d667f76-b8ea-45b7-8cef-ea74b539bd03` | unsure | 0.609 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `d9d8858e-6bd8-4877-8ff7-3921cf0e05b2` | ai | 0.869 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `ccb315ff-ac35-47a1-bf7a-e5a62652458e` | unsure | 0.579 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `f4773225-c96d-4835-a08d-3b50a6f4bb49` | ai | 0.693 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `8b5cca78-58ea-4236-bdcc-0786307877d4` | ai | 0.715 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `65447106-f54a-4e52-b1ea-ac41e4b5ae2c` | ai | 0.711 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `f85d6f95-40bd-4775-b9aa-e721ebc44170` | ai | 0.737 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `a9927bb9-c647-4a7f-aa75-587725010c81` | ai | 0.723 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `ae520659-b11a-43c4-8f58-d713237c3559` | ai | 0.720 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `795b91e0-ccd2-4b50-b8e6-504308c4993c` | human | 0.334 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `dd3dcf9e-05e7-4eb4-8c0f-2ea4d3779fec` | unsure | 0.420 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `7d37397f-cd47-4712-8bff-7dd97d014992` | human | 0.257 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `1fcfbe2f-d6c4-4df4-b5b2-3fbceb0ceb48` | unsure | 0.559 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `db51a322-e26f-4ba3-951c-ffe3fc633862` | unsure | 0.478 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `56396853-5f1d-4041-94f0-bd9af2264dec` | unsure | 0.521 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `e6cd9fd9-bd0c-4a05-9970-f7b79e2fa907` | unsure | 0.546 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `8ebcde77-9aff-45bc-b596-a9440c317f9e` | human | 0.218 |  |
| MF04 | malformed | text is only punctuation | 200 | `994bc772-70e7-4590-879c-3e329d2c6890` | human | 0.327 |  |
| MF05 | malformed | text is a very long single word | 200 | `ad335006-8fad-4bf0-8051-1e4fb2444e20` | ai | 0.859 |  |
| MF06 | malformed | text is emoji only | 200 | `d896906e-bc7b-46c4-a93a-3d7ceb406ddc` | ai | 0.998 |  |
| MF07 | malformed | text is right-to-left script | 200 | `57c1761a-8218-4501-b3a1-ec7b5ca7d6f0` | ai | 0.939 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `25b39027-944f-4163-9abc-4136d67a6f55` | human | 0.269 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9109ab16-cbad-4d74-b336-b2162b64ba10` | human | 0.269 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d4910b37-418c-4243-a19f-88327444a410` | human | 0.269 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `dd607a04-cceb-4a71-b913-7a0bd47a756d` | human | 0.269 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a3746852-447b-482f-b444-a62b6baf4ae1` | human | 0.269 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ee34d113-8fb4-4bcc-92a6-4ee0a96a1767` | human | 0.269 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `65a1f758-daf1-4468-9fa1-8144031ab08d` | human | 0.269 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3a2b5e8c-b79b-43f2-ade0-d3dbc2e098c3` | human | 0.269 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8189e0e0-2b9c-4158-9b18-bad561272f89` | human | 0.269 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `09c43457-dc8f-4f4f-980f-b2695d24015f` | human | 0.269 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "a2f9254d-7d42-42a9-9369-c5d6111828df",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.3396,
  "model_score": 0.1635,
  "style_score": 0.6038,
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "f8e361a1-cc02-4c9c-9a88-5d4c764e9970",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4793,
  "model_score": 0.5943,
  "style_score": 0.3067,
  "label": "We could not confidently determine who wrote this. If this is your work, you can appeal for review.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "10b7c63e-c693-4ea2-a216-2d48220d02d5",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5904,
  "model_score": 0.6662,
  "style_score": 0.4768,
  "label": "We could not confidently determine who wrote this. If this is your work, you can appeal for review.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "d0d99dc3-f111-4898-9a9e-66ca1c9d9adc",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6051,
  "model_score": 0.6114,
  "style_score": 0.5956,
  "label": "We could not confidently determine who wrote this. If this is your work, you can appeal for review.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "79aee5a5-2d06-4d3e-bb36-e5d841b8c31a",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.3499,
  "model_score": 0.3212,
  "style_score": 0.393,
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "2aa75669-9ac7-48d2-861d-b978d287ef62",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4528,
  "model_score": 0.5727,
  "style_score": 0.2729,
  "label": "We could not confidently determine who wrote this. If this is your work, you can appeal for review.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "cef76e49-eb8e-4b45-9ed3-102ae883233e",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.63,
  "model_score": 0.5862,
  "style_score": 0.6956,
  "label": "We could not confidently determine who wrote this. If this is your work, you can appeal for review.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "d47cb1ce-cd8f-401e-8abe-091ec79dcadc",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.3419,
  "model_score": 0.2452,
  "style_score": 0.487,
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "7d667f76-b8ea-45b7-8cef-ea74b539bd03",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.6089,
  "model_score": 0.7042,
  "style_score": 0.4659,
  "label": "We could not confidently determine who wrote this. If this is your work, you can appeal for review.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "d9d8858e-6bd8-4877-8ff7-3921cf0e05b2",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8692,
  "model_score": 0.9792,
  "style_score": 0.7041,
  "label": "We think this was probably generated by AI. If you wrote this yourself, you can appeal for review.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "ccb315ff-ac35-47a1-bf7a-e5a62652458e",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5794,
  "model_score": 0.6175,
  "style_score": 0.5223,
  "label": "We could not confidently determine who wrote this. If this is your work, you can appeal for review.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "f4773225-c96d-4835-a08d-3b50a6f4bb49",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.6925,
  "model_score": 0.7387,
  "style_score": 0.6233,
  "label": "We think this was probably generated by AI. If you wrote this yourself, you can appeal for review.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "8b5cca78-58ea-4236-bdcc-0786307877d4",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7145,
  "model_score": 0.8051,
  "style_score": 0.5785,
  "label": "We think this was probably generated by AI. If you wrote this yourself, you can appeal for review.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "65447106-f54a-4e52-b1ea-ac41e4b5ae2c",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.7109,
  "model_score": 0.8329,
  "style_score": 0.528,
  "label": "We think this was probably generated by AI. If you wrote this yourself, you can appeal for review.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "f85d6f95-40bd-4775-b9aa-e721ebc44170",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7373,
  "model_score": 0.8005,
  "style_score": 0.6426,
  "label": "We think this was probably generated by AI. If you wrote this yourself, you can appeal for review.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "a9927bb9-c647-4a7f-aa75-587725010c81",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.7229,
  "model_score": 0.8814,
  "style_score": 0.4852,
  "label": "We think this was probably generated by AI. If you wrote this yourself, you can appeal for review.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "ae520659-b11a-43c4-8f58-d713237c3559",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.7203,
  "model_score": 0.8816,
  "style_score": 0.4784,
  "label": "We think this was probably generated by AI. If you wrote this yourself, you can appeal for review.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "795b91e0-ccd2-4b50-b8e6-504308c4993c",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.3341,
  "model_score": 0.3223,
  "style_score": 0.3517,
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "dd3dcf9e-05e7-4eb4-8c0f-2ea4d3779fec",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4203,
  "model_score": 0.4625,
  "style_score": 0.357,
  "label": "We could not confidently determine who wrote this. If this is your work, you can appeal for review.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "7d37397f-cd47-4712-8bff-7dd97d014992",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2572,
  "model_score": 0.2044,
  "style_score": 0.3365,
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "1fcfbe2f-d6c4-4df4-b5b2-3fbceb0ceb48",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5589,
  "model_score": 0.5943,
  "style_score": 0.5057,
  "label": "We could not confidently determine who wrote this. If this is your work, you can appeal for review.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "db51a322-e26f-4ba3-951c-ffe3fc633862",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.478,
  "model_score": 0.4998,
  "style_score": 0.4453,
  "label": "We could not confidently determine who wrote this. If this is your work, you can appeal for review.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "56396853-5f1d-4041-94f0-bd9af2264dec",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5209,
  "model_score": 0.6401,
  "style_score": 0.342,
  "label": "We could not confidently determine who wrote this. If this is your work, you can appeal for review.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "e6cd9fd9-bd0c-4a05-9970-f7b79e2fa907",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5465,
  "model_score": 0.5583,
  "style_score": 0.5289,
  "label": "We could not confidently determine who wrote this. If this is your work, you can appeal for review.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "8ebcde77-9aff-45bc-b596-a9440c317f9e",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.2179,
  "model_score": 0.0,
  "style_score": 0.5447,
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "994bc772-70e7-4590-879c-3e329d2c6890",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.3267,
  "model_score": 0.0112,
  "style_score": 0.8,
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "ad335006-8fad-4bf0-8051-1e4fb2444e20",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.8586,
  "model_score": 0.9976,
  "style_score": 0.65,
  "label": "We think this was probably generated by AI. If you wrote this yourself, you can appeal for review.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "d896906e-bc7b-46c4-a93a-3d7ceb406ddc",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9981,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "We think this was probably generated by AI. If you wrote this yourself, you can appeal for review.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "57c1761a-8218-4501-b3a1-ec7b5ca7d6f0",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.9394,
  "model_score": 0.9064,
  "style_score": 0.9888,
  "label": "We think this was probably generated by AI. If you wrote this yourself, you can appeal for review.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "25b39027-944f-4163-9abc-4136d67a6f55",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2687,
  "model_score": 0.0287,
  "style_score": 0.6287,
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "9109ab16-cbad-4d74-b336-b2162b64ba10",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2687,
  "model_score": 0.0287,
  "style_score": 0.6287,
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "d4910b37-418c-4243-a19f-88327444a410",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2687,
  "model_score": 0.0287,
  "style_score": 0.6287,
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "dd607a04-cceb-4a71-b913-7a0bd47a756d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2687,
  "model_score": 0.0287,
  "style_score": 0.6287,
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "a3746852-447b-482f-b444-a62b6baf4ae1",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2687,
  "model_score": 0.0287,
  "style_score": 0.6287,
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "ee34d113-8fb4-4bcc-92a6-4ee0a96a1767",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2687,
  "model_score": 0.0287,
  "style_score": 0.6287,
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "65a1f758-daf1-4468-9fa1-8144031ab08d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2687,
  "model_score": 0.0287,
  "style_score": 0.6287,
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "3a2b5e8c-b79b-43f2-ade0-d3dbc2e098c3",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2687,
  "model_score": 0.0287,
  "style_score": 0.6287,
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "8189e0e0-2b9c-4158-9b18-bad561272f89",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2687,
  "model_score": 0.0287,
  "style_score": 0.6287,
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "09c43457-dc8f-4f4f-980f-b2695d24015f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2687,
  "model_score": 0.0287,
  "style_score": 0.6287,
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
