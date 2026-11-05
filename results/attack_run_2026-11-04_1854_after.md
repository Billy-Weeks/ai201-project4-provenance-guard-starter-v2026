# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 18:54
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `87088942-b55c-41ba-9b70-d73213719528` | human | 0.340 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `f086743a-9d27-4435-9baa-9058232c7201` | unsure | 0.479 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `d6b46294-5262-4dc2-9b35-2f9bc0072f6b` | unsure | 0.590 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `048ed5dc-a50a-4127-9287-72c891379da2` | unsure | 0.605 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `9835d987-57d0-4355-bcc5-b7e4bf781753` | human | 0.350 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `dcb7943f-0b0e-4d54-988c-acd09eac2294` | unsure | 0.453 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `56d9534f-69da-4fe1-92c4-78ee16dad3ba` | unsure | 0.630 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `110b304c-efee-4cca-91bc-d3ff5736b970` | human | 0.342 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `1bc3b670-d438-43ac-a467-4760beda0da8` | unsure | 0.609 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `f0fe6e4a-0603-4403-b69b-0d7779930587` | ai | 0.869 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `a570ba58-facc-41e1-ab70-85b8cf3dd653` | unsure | 0.579 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `560a3cb0-94e1-4cfd-ba37-778a9b4ac762` | ai | 0.693 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `c1dc8ed7-a2cd-4c85-8767-bb15c151a84f` | ai | 0.715 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `bb039295-80e1-402c-8e2a-42c64f5db428` | ai | 0.711 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `b96f3df9-e830-41a6-b200-5347329281e4` | ai | 0.737 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `a11b7860-3bf3-48d5-8547-0db7ca6a0e3a` | ai | 0.723 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `262783f1-1923-4bd8-872d-ecc12d493e14` | ai | 0.720 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `b304256f-57ad-4fe3-826f-76d19b9b9d4b` | human | 0.334 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `74b4dcd1-6841-4ed5-9f72-b127340bcbe9` | unsure | 0.420 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `892062c9-a15f-4375-9406-3243206d33e2` | human | 0.257 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `fb21963b-1cd3-433d-814c-c0631e48912e` | unsure | 0.559 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `ecd80f73-de63-41c2-b629-2ebdf2ddd9eb` | unsure | 0.478 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `f957f7d7-b9e7-4b4e-a9e5-236f00f85361` | unsure | 0.521 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `9bac6ea2-cc92-4839-9bb6-f61eca06f426` | unsure | 0.546 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `e4a19ef6-20cb-46b0-a948-4d9ecf9a9b44` | human | 0.218 |  |
| MF04 | malformed | text is only punctuation | 200 | `e1e1048e-7f10-44f2-9c72-46caf844e22c` | human | 0.327 |  |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 200 | `3437ca7b-6f3c-4854-996f-51fd2a92d0fd` | ai | 0.939 |  |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `effb66bc-01b6-4ecc-99cf-d8e10c146745` | human | 0.269 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3376bbe9-032f-4142-b579-26427f610bd1` | human | 0.269 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ae987380-54a1-49a7-b8c8-018136d158cd` | human | 0.269 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `90a928ec-2564-4794-b230-018de8c3cf4b` | human | 0.269 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `310c99f7-cef1-42c2-8291-e555a1803a8d` | human | 0.269 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ac9f6a7e-1991-4c9e-9eb0-de549c2fc17c` | human | 0.269 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `249df03f-9e9d-4d8f-954f-318cf3b16c41` | human | 0.269 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f8bd308d-a13f-45f3-a8c7-65c88ebc2ba8` | human | 0.269 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `03654767-7aa3-4bbb-a3bd-a76b32dc911c` | human | 0.269 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2465ebad-d0a6-434e-a91b-a51790b36b72` | human | 0.269 |  |
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
  "content_id": "87088942-b55c-41ba-9b70-d73213719528",
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
  "content_id": "f086743a-9d27-4435-9baa-9058232c7201",
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
  "content_id": "d6b46294-5262-4dc2-9b35-2f9bc0072f6b",
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
  "content_id": "048ed5dc-a50a-4127-9287-72c891379da2",
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
  "content_id": "9835d987-57d0-4355-bcc5-b7e4bf781753",
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
  "content_id": "dcb7943f-0b0e-4d54-988c-acd09eac2294",
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
  "content_id": "56d9534f-69da-4fe1-92c4-78ee16dad3ba",
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
  "content_id": "110b304c-efee-4cca-91bc-d3ff5736b970",
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
  "content_id": "1bc3b670-d438-43ac-a467-4760beda0da8",
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
  "content_id": "f0fe6e4a-0603-4403-b69b-0d7779930587",
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
  "content_id": "a570ba58-facc-41e1-ab70-85b8cf3dd653",
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
  "content_id": "560a3cb0-94e1-4cfd-ba37-778a9b4ac762",
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
  "content_id": "c1dc8ed7-a2cd-4c85-8767-bb15c151a84f",
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
  "content_id": "bb039295-80e1-402c-8e2a-42c64f5db428",
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
  "content_id": "b96f3df9-e830-41a6-b200-5347329281e4",
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
  "content_id": "a11b7860-3bf3-48d5-8547-0db7ca6a0e3a",
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
  "content_id": "262783f1-1923-4bd8-872d-ecc12d493e14",
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
  "content_id": "b304256f-57ad-4fe3-826f-76d19b9b9d4b",
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
  "content_id": "74b4dcd1-6841-4ed5-9f72-b127340bcbe9",
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
  "content_id": "892062c9-a15f-4375-9406-3243206d33e2",
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
  "content_id": "fb21963b-1cd3-433d-814c-c0631e48912e",
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
  "content_id": "ecd80f73-de63-41c2-b629-2ebdf2ddd9eb",
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
  "content_id": "f957f7d7-b9e7-4b4e-a9e5-236f00f85361",
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
  "content_id": "9bac6ea2-cc92-4839-9bb6-f61eca06f426",
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
  "content_id": "e4a19ef6-20cb-46b0-a948-4d9ecf9a9b44",
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
  "content_id": "e1e1048e-7f10-44f2-9c72-46caf844e22c",
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
  "content_id": "3437ca7b-6f3c-4854-996f-51fd2a92d0fd",
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
  "content_id": "effb66bc-01b6-4ecc-99cf-d8e10c146745",
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
  "content_id": "3376bbe9-032f-4142-b579-26427f610bd1",
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
  "content_id": "ae987380-54a1-49a7-b8c8-018136d158cd",
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
  "content_id": "90a928ec-2564-4794-b230-018de8c3cf4b",
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
  "content_id": "310c99f7-cef1-42c2-8291-e555a1803a8d",
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
  "content_id": "ac9f6a7e-1991-4c9e-9eb0-de549c2fc17c",
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
  "content_id": "249df03f-9e9d-4d8f-954f-318cf3b16c41",
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
  "content_id": "f8bd308d-a13f-45f3-a8c7-65c88ebc2ba8",
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
  "content_id": "03654767-7aa3-4bbb-a3bd-a76b32dc911c",
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
  "content_id": "2465ebad-d0a6-434e-a91b-a51790b36b72",
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
