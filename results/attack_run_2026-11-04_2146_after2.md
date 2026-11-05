# Attack run — after2

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 21:46
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `4c1c5e91-a0f6-43ef-a71f-1a60b1861963` | human | 0.340 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `99040bbf-a66f-4745-82d7-bff44166c6be` | unsure | 0.479 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `df354611-aad4-4178-8772-3e179e7d2df2` | unsure | 0.590 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `a3b55743-078d-44df-b3af-d2fbba686344` | unsure | 0.605 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `db19cb99-8d81-4a40-a363-f1eb3402f398` | human | 0.350 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `55576980-7fb2-430f-a7f7-373885b4691a` | unsure | 0.453 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `2572c8a8-afbf-49cb-997b-dc227ad97e81` | unsure | 0.530 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `a5dbd217-e23c-4993-afc1-189f35f461dd` | human | 0.342 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `b6cf289e-6267-4a5c-8d9e-de00c5e10b51` | unsure | 0.609 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `80230e0b-daa0-4628-a12d-7128006e8d32` | ai | 0.869 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `fc7601eb-46b2-4148-a5ed-a581717d5f3a` | unsure | 0.579 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `2aaf50b0-79bf-44c4-94f9-747c6fcaebe9` | ai | 0.693 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `9c1f2dfb-c3ac-4502-b3ed-ef2f7d4d4934` | ai | 0.715 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `1f464849-078e-4c31-8fae-f52b9df1cf00` | ai | 0.711 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `bf3e7ed0-c244-4c63-bdd7-00bc878bc65d` | ai | 0.737 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `c6278eab-d50f-4b1b-81cd-a51d4ca8d2f4` | ai | 0.723 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `232dc74c-1a26-4fb6-ba0a-a4ec3d7bd052` | ai | 0.720 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `a9e6624f-7988-4b13-977d-93adec380c22` | human | 0.334 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `5207e8ba-2fd3-4115-8583-48cf7e804382` | unsure | 0.420 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `f28dbd13-c22e-487b-be8b-b6bac6812d23` | human | 0.257 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `6ab39644-6c3f-4a57-b3cc-771456d5f22e` | unsure | 0.559 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `1de2983f-ad67-4649-a273-c7134235ee03` | unsure | 0.478 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `96843fe5-4e38-4378-849a-b26ec7fb4774` | unsure | 0.521 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `28ff7f65-7d9d-46a3-b089-1a5a7b859eee` | unsure | 0.546 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `07e03ff2-bf33-4999-bcc3-2b37772d8955` | human | 0.069 |  |
| MF04 | malformed | text is only punctuation | 200 | `c89ad187-a97c-4663-84ea-4cf2ce1a914a` | human | 0.261 |  |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 200 | `62ebcdf0-a1fa-4a66-9c3c-5f63e3d3eda9` | ai | 0.936 |  |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1baae4e0-0059-476e-9b27-5e32b653ae25` | human | 0.147 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `148ce93f-cb34-4df1-9836-b9433d9d4108` | human | 0.147 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `fac82345-0cec-4ee7-ab60-108f1a266976` | human | 0.147 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `05c19570-8955-4435-9579-cd0cf18b7794` | human | 0.147 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `269c6d61-5d6b-4c5b-a801-0c6090fb97e1` | human | 0.147 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `10e75b92-8fa3-415f-a47f-424eef6baea4` | human | 0.147 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a6fc2737-04ac-41b9-a543-54a01845c35d` | human | 0.147 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `09b8c816-aa6f-4c8c-98ce-6301f40064c3` | human | 0.147 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b4f4fd95-5845-4c87-8754-d9eba1b16773` | human | 0.147 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `55e746a0-f4de-463b-9f3d-389e4f7f0152` | human | 0.147 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
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
  "content_id": "4c1c5e91-a0f6-43ef-a71f-1a60b1861963",
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
  "content_id": "99040bbf-a66f-4745-82d7-bff44166c6be",
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
  "content_id": "df354611-aad4-4178-8772-3e179e7d2df2",
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
  "content_id": "a3b55743-078d-44df-b3af-d2fbba686344",
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
  "content_id": "db19cb99-8d81-4a40-a363-f1eb3402f398",
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
  "content_id": "55576980-7fb2-430f-a7f7-373885b4691a",
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
  "content_id": "2572c8a8-afbf-49cb-997b-dc227ad97e81",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5304,
  "model_score": 0.5862,
  "style_score": 0.4466,
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
  "content_id": "a5dbd217-e23c-4993-afc1-189f35f461dd",
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
  "content_id": "b6cf289e-6267-4a5c-8d9e-de00c5e10b51",
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
  "content_id": "80230e0b-daa0-4628-a12d-7128006e8d32",
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
  "content_id": "fc7601eb-46b2-4148-a5ed-a581717d5f3a",
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
  "content_id": "2aaf50b0-79bf-44c4-94f9-747c6fcaebe9",
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
  "content_id": "9c1f2dfb-c3ac-4502-b3ed-ef2f7d4d4934",
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
  "content_id": "1f464849-078e-4c31-8fae-f52b9df1cf00",
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
  "content_id": "bf3e7ed0-c244-4c63-bdd7-00bc878bc65d",
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
  "content_id": "c6278eab-d50f-4b1b-81cd-a51d4ca8d2f4",
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
  "content_id": "232dc74c-1a26-4fb6-ba0a-a4ec3d7bd052",
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
  "content_id": "a9e6624f-7988-4b13-977d-93adec380c22",
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
  "content_id": "5207e8ba-2fd3-4115-8583-48cf7e804382",
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
  "content_id": "f28dbd13-c22e-487b-be8b-b6bac6812d23",
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
  "content_id": "6ab39644-6c3f-4a57-b3cc-771456d5f22e",
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
  "content_id": "1de2983f-ad67-4649-a273-c7134235ee03",
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
  "content_id": "96843fe5-4e38-4378-849a-b26ec7fb4774",
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
  "content_id": "28ff7f65-7d9d-46a3-b089-1a5a7b859eee",
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
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "07e03ff2-bf33-4999-bcc3-2b37772d8955",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.0689,
  "model_score": 0.0,
  "style_score": 0.1722,
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
  "content_id": "c89ad187-a97c-4663-84ea-4cf2ce1a914a",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.2613,
  "model_score": 0.0112,
  "style_score": 0.6364,
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
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
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
  "content_id": "62ebcdf0-a1fa-4a66-9c3c-5f63e3d3eda9",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.9357,
  "model_score": 0.9064,
  "style_score": 0.9796,
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
  "content_id": "1baae4e0-0059-476e-9b27-5e32b653ae25",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1472,
  "model_score": 0.0287,
  "style_score": 0.325,
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
  "content_id": "148ce93f-cb34-4df1-9836-b9433d9d4108",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1472,
  "model_score": 0.0287,
  "style_score": 0.325,
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
  "content_id": "fac82345-0cec-4ee7-ab60-108f1a266976",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1472,
  "model_score": 0.0287,
  "style_score": 0.325,
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
  "content_id": "05c19570-8955-4435-9579-cd0cf18b7794",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1472,
  "model_score": 0.0287,
  "style_score": 0.325,
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
  "content_id": "269c6d61-5d6b-4c5b-a801-0c6090fb97e1",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1472,
  "model_score": 0.0287,
  "style_score": 0.325,
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
  "content_id": "10e75b92-8fa3-415f-a47f-424eef6baea4",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1472,
  "model_score": 0.0287,
  "style_score": 0.325,
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
  "content_id": "a6fc2737-04ac-41b9-a543-54a01845c35d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1472,
  "model_score": 0.0287,
  "style_score": 0.325,
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
  "content_id": "09b8c816-aa6f-4c8c-98ce-6301f40064c3",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1472,
  "model_score": 0.0287,
  "style_score": 0.325,
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
  "content_id": "b4f4fd95-5845-4c87-8754-d9eba1b16773",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1472,
  "model_score": 0.0287,
  "style_score": 0.325,
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
  "content_id": "55e746a0-f4de-463b-9f3d-389e4f7f0152",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1472,
  "model_score": 0.0287,
  "style_score": 0.325,
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
