# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. A writer sends text and a `creator_id` to `POST /submit` as JSON. The route rejects missing fields, empty text, or text longer than `config.MAX_TEXT_CHARS` (10,000 characters) with a `400` before any signal runs.
2. The route creates a unique `content_id` so the submission can be audited and appealed later.
3. The detector signal in `detector.py` reads the text for meaning and predictability, then returns a model score from 0 to 1. A higher score means more likely AI-generated.
4. The style signal in `stylometry.py` measures the text’s structure, including sentence-length spread, vocabulary variety, and punctuation density, and returns a style score from 0 to 1.
5. `scoring.py::combine_signals` combines the two signal scores into one confidence score using the weights defined in `config.py`.
6. `scoring.py::score_to_label` maps that score to one of three reader-facing labels: high-confidence human, unsure, or high-confidence AI.
7. The service writes the decision and its signal scores to `logs/audit.jsonl`, then returns the `content_id`, guess, confidence, label, and both signal scores to the caller.

The appeal path starts when a writer sends a `content_id` and reasoning to `POST /appeal`. The service verifies that the content exists, appends the appeal to the audit log with status `under_review`, and returns a confirmation without automatically re-checking the text.

### False-positive trace

Consider a real writer who submits a plain, carefully edited paragraph. The model signal may score it as AI-like because its familiar words and predictable sentences produce low perplexity. The style signal may also score it as AI-like if the sentences have similar lengths and the vocabulary repeats. Suppose the combining rule produces an illustrative confidence score of `0.72`; with the AI threshold of `0.65`, the reader would see the high-confidence AI label.

That is the expensive failure: the writer is being accused even though the work is theirs. The response gives them the `content_id`, score, and label, so they can send that ID and their reasoning to `POST /appeal`. The service records the appeal beside the original decision and changes the status to `under_review`. It does not silently replace the original decision or automatically re-check the writing. The thresholds and combining rule must therefore be chosen with this false-positive path in mind, especially for plain human writing.

### Endpoint contracts

`POST /submit` request:

```json
{
  "text": "The writing being evaluated.",
  "creator_id": "writer-123"
}
```

`POST /submit` response:

```json
{
  "content_id": "generated-id",
  "guess": "ai | human | unsure",
  "confidence": 0.0,
  "label": "Reader-facing label text.",
  "model_score": 0.0,
  "style_score": 0.0
}
```

`POST /appeal` request:

```json
{
  "content_id": "generated-id",
  "reasoning": "This is my own writing because ..."
}
```

`POST /appeal` response:

```json
{
  "content_id": "generated-id",
  "status": "under_review",
  "message": "Appeal recorded for review."
}
```


---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** The local language model in `detector.py` measures how predictable the text is using perplexity. Low perplexity means the model found the wording easy to predict, which is converted into a higher model score because predictable, ordinary wording can resemble generated prose.

**Why that might differ between human and AI writing:** AI-generated text often follows likely next-word patterns and therefore may be more predictable. Human writing may wander through unusual word choices or abrupt turns, producing higher perplexity and a lower AI-likelihood score.

**What it can't see:** Predictability is not authorship. Plain human writing, second-language writing, or writing with familiar vocabulary can look AI-like. Dense or ornate human writing can look human simply because it is surprising to the model. The signal also does not know who actually wrote the text.

### Signal two — the style signal

**What it measures:** `stylometry.py` measures the shape of the text rather than its meaning: sentence-length spread, the ratio of unique words to total words, and punctuation density. These measures are combined into a style score from 0 to 1, with higher meaning more likely AI.

**Why that might differ between human and AI writing:** Generated prose often has even, mid-length sentences and repeated common vocabulary. Human writing can be lumpier, with greater variation in sentence length, word choice, and punctuation.

**What it can't see:** It cannot understand the text’s meaning, authorship, or context. Any edit that changes the text’s shape—such as adding typos, splitting sentences, or inserting a quotation—can move the score without changing who wrote the underlying ideas.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** I use a weighted average. Both signals point in the same direction, where a higher score means more likely AI. When the signals disagree, the combined score stays between them and moves toward the model signal because it reads meaning while the style signal only sees surface form.

**The numbers:** `combined_score = (0.60 * model_score) + (0.40 * style_score)`. Scores from `0.00` through `0.35` are high-confidence human, scores above `0.35` and below `0.65` are unsure, and scores from `0.65` through `1.00` are high-confidence AI. These thresholds and labels are implemented in `config.py` and `scoring.py`.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**

In the first calibration run, the formal-human sample split the signals. The model read it as human-like (`model_score` `0.2361`) because its wording was not especially predictable, while the style signal read it as AI-like (`style_score` `0.6715`) because its sentences were even in length and its punctuation was sparse. The weighted average gave `0.6 * 0.2361 + 0.4 * 0.6715 = 0.4103`, which lands in the unsure band. The rule leans toward the model signal, so a strongly human-like model reading keeps an AI-looking surface shape from producing an accusation by itself. In this case, though, it did not clear the writer either; the result was "unsure," with the appeal path available.

### Milestone 4 calibration results

The latest four calibration submissions were recorded in `logs/audit.jsonl`. The service returned both signal scores and the weighted combined score for each one.

| Input | Model score | Style score | Combined score |
|---|---:|---:|---:|
| Clearly AI | 0.6037 | 0.5513 | 0.5827 |
| Clearly human | 0.5195 | 0.6009 | 0.5521 |
| Formal human | 0.2361 | 0.6715 | 0.4103 |
| Lightly edited AI | 0.3493 | 0.4297 | 0.3815 |

The clearly-AI and clearly-human samples were only `0.0306` apart in combined score, so they were not noticeably separated in this run. The model and style signals also disagreed on the formal-human sample: the model score was relatively human-like at `0.2361`, while the style score was more AI-like at `0.6715`. The weighted average produced `0.4103`, showing how the combining rule handles disagreement. This is a calibration finding to investigate, not a claim that the detector is accurate.

### Matched-length follow-up

The first calibration used short samples with different topics, lengths, and sentence structures. Because both signals are affected by wording and text shape, we ran a second set with four longer samples of roughly similar length, the same general topic, and comparable sentence counts. The purpose was to test whether the weak separation in the first run was partly caused by the sample construction rather than by the combining rule alone.

| Input | Model score | Style score | Combined score |
|---|---:|---:|---:|
| Clearly AI | 0.7809 | 0.5704 | 0.6967 |
| Clearly human | 0.2738 | 0.5919 | 0.4010 |
| Formal human | 0.6691 | 0.6618 | 0.6662 |
| Lightly edited AI | 0.6456 | 0.5918 | 0.6241 |

The clearly-AI and clearly-human combined scores were `0.2957` apart in this follow-up, compared with only `0.0306` in the first run. That supports the conclusion that short, unmatched samples contributed to the original weak separation. The formal-human sample still scored AI-like, so matching length and topic did not remove every blind spot. These results are evidence about this calibration set, not proof of authorship detection accuracy.



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | `0.00 <= score <= 0.35` | “We think this was probably written by a person. If this is your work, no action is needed.” |
| unsure | `0.35 < score < 0.65` | “We could not confidently determine who wrote this. If this is your work, you can appeal for review.” |
| high-confidence AI | `0.65 <= score <= 1.00` | “We think this was probably generated by AI. If you wrote this yourself, you can appeal for review.” |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

The unsure label states that the service lacks confidence and gives the writer a clear next step. It does not accuse the writer or present the score as proof of authorship.

**All three labels are reachable.** Each one appears in `logs/audit.jsonl` with `status: "decided"`:

| Label | `creator_id` | Combined score |
|---|---|---:|
| high-confidence human | `m5-casual-human` | 0.1341 |
| unsure | `m5-human` | 0.4010 |
| high-confidence AI | `m5-formal-human` | 0.6662 |

The high-confidence human result came from this request:

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "ugh. missed the bus AGAIN — third time this week!! Grandpa'"'"'s old Buick, rusted, coughing smoke; we pushed it two blocks? Then Marisol laughed so hard she snorted coffee everywhere. Anyway: tacos.", "creator_id": "m5-casual-human"}'
```

```json
{
  "confidence": 0.1341,
  "content_id": "9321258a-5428-46ba-9bcc-ed25cd02d2e9",
  "guess": "human",
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "model_score": 0.0497,
  "style_score": 0.2608
}
```


---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "Our community garden started because the empty lot was becoming a place where people dumped broken chairs. The first meeting was three people and a dog that kept stealing gloves. Now we have tomatoes, mint, and one pumpkin nobody admits planting. I usually go after work, when the heat has gone out of the pavement. Last week Marisol brought a chair for the corner, so somebody can sit and complain about the weeds. That is probably the most successful part of the whole project.", "creator_id": "m5-human"}'
```

```json
{
  "confidence": 0.401,
  "content_id": "90bb622a-78b8-4165-a93f-d87a19aa13aa",
  "guess": "unsure",
  "label": "We could not confidently determine who wrote this. If this is your work, you can appeal for review.",
  "model_score": 0.2738,
  "style_score": 0.5919
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id":"90bb622a-78b8-4165-a93f-d87a19aa13aa","reasoning":"This is my own writing, so I would like the result reviewed."}'
```

```json
{
  "content_id": "90bb622a-78b8-4165-a93f-d87a19aa13aa",
  "message": "Appeal recorded for review.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=2"
```

```json
{
  "count": 2,
  "entries": [
    {
      "timestamp": "2026-10-29T01:50:13+00:00",
      "content_id": "90bb622a-78b8-4165-a93f-d87a19aa13aa",
      "creator_id": "m5-human",
      "guess": "unsure",
      "model_score": 0.2738,
      "style_score": 0.5919,
      "combined_score": 0.401,
      "label": "We could not confidently determine who wrote this. If this is your work, you can appeal for review.",
      "status": "decided"
    },
    {
      "timestamp": "2026-10-29T01:52:13+00:00",
      "content_id": "90bb622a-78b8-4165-a93f-d87a19aa13aa",
      "creator_id": "m5-human",
      "event": "appeal",
      "status": "under_review",
      "reasoning": "This is my own writing, so I would like the result reviewed."
    }
  ]
}
```

---

## How I Used AI

**Moment 1 — implementing and calibrating the style signal**

- *What I asked for:* I asked the AI to implement the second signal in `stylometry.py` and connect it to the detector in `scoring.py::combine_signals`, while keeping both scores visible in the response and audit log.
- *What came back:* It implemented sentence-length spread, type-token ratio, and punctuation density; normalized them into a style score where higher means more AI-like; and combined the model and style scores with weights of `0.60` and `0.40`.
- *What I changed:* I ran the four calibration samples instead of accepting the result without testing it. The first set separated clearly-AI and clearly-human text by only `0.0306`, so I ran longer, same-topic samples; that increased the gap to `0.2957`. I documented both runs and the remaining formal-human blind spot in `README.md`.

**Moment 2 — final review against the rubric**

- *What I asked for:* A check of the finished project against the unit instructions and rubric.
- *What came back:* Three gaps. No submission had reached the high-confidence human label. My "signals split" paragraph described the opposite of my own calibration data. Criterion 5 referred to a "documented maximum" text length that did not exist, and empty text was being scored instead of rejected.
- *What I changed:* I had the AI fix all three, and I reviewed each edit before committing. A text submission reached the human label (`0.1341`) and was added under Label Variants. The disagreement paragraph was rewritten around the real formal-human numbers. `MAX_TEXT_CHARS = 10000` was added to `config.py`, along with a check in `app.py::submit` that returns `400` for empty or oversized text, and criterion 5 now names that limit.

---

## Stretch Feature

**Declared (not yet built):** `GET /content/<id>`

**What it will do:** `GET /content/<content_id>` will return one item's current status. It will read that content's entries from `logs/audit.jsonl` and return its `content_id`, `creator_id`, the original decision (`guess`, `confidence`, `label`), and its current `status`: `decided` after a submission, or `under_review` once an appeal has been recorded. An unknown `content_id` will return `404`. The route will only read the log; it will not change scoring, labels, or any existing route.

**Planned evidence:** once it is built, this section will explain what changed and show a request and response as text, both before and after an appeal.

### Built: what changed

- `app.py::get_content` adds the `GET /content/<content_id>` route. It collects every log entry for that ID with `audit.entries_for`. It reports the original decision from the `decided` entry and the current `status` from the most recent entry, so an appeal shows up as `under_review` without the original decision being overwritten.
- An unknown ID returns `404` with `{"error": "not_found"}`.
- Nothing else changed. `/submit`, `/appeal`, scoring, and labels are untouched; the route only reads `logs/audit.jsonl`.

### Request and response

Submission (`creator_id` `stretch-writer`) returned `content_id` `0f21f800-28f9-46c3-b77a-633a12f1e494`, with a confidence of `0.4495` and the "unsure" label.

Before the appeal:

```bash
$ curl http://127.0.0.1:5000/content/0f21f800-28f9-46c3-b77a-633a12f1e494
```

```json
{
  "confidence": 0.4495,
  "content_id": "0f21f800-28f9-46c3-b77a-633a12f1e494",
  "creator_id": "stretch-writer",
  "guess": "unsure",
  "label": "We could not confidently determine who wrote this. If this is your work, you can appeal for review.",
  "status": "decided"
}
```

After `POST /appeal` for that ID, which returned `"status": "under_review"`:

```bash
$ curl http://127.0.0.1:5000/content/0f21f800-28f9-46c3-b77a-633a12f1e494
```

```json
{
  "confidence": 0.4495,
  "content_id": "0f21f800-28f9-46c3-b77a-633a12f1e494",
  "creator_id": "stretch-writer",
  "guess": "unsure",
  "label": "We could not confidently determine who wrote this. If this is your work, you can appeal for review.",
  "status": "under_review"
}
```

Unknown ID:

```bash
$ curl http://127.0.0.1:5000/content/does-not-exist
```

```json
{
  "error": "not_found",
  "message": "No submission exists for that content_id."
}
```

That request returns HTTP status `404`.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 10 per minute, 200 per day

**Why those numbers and not others:**
I chose 10 submissions per minute because a real writer can submit several
pieces or corrections in a short session, while a script probing thresholds
with many variations will hit the limit quickly. I chose 200 per day because
that leaves room for a writer's normal daily activity and retries without
allowing a sustained high-volume mapping attack. The limits are keyed to a
valid `creator_id`; requests without one fall back to the caller's address.

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

`GET /health` reported `rate_limiting: true`. The first flood attempt included
one `ReadTimeout` while the detector model loaded, so I waited for the service
to warm up and repeated the test. This clean run produced 10 accepted requests
followed by 5 rate-limited requests, matching the 10-per-minute limit. The
five `429` responses were also recorded as rejected events in the audit log.

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

The runner produced 56 inputs. I marked evasion attacks as BROKE when they
avoided the AI label, false-positive attacks as BROKE when human text received
the AI label, prompt-injection attacks as BROKE only if their instruction
changed service behavior, malformed attacks as BROKE when they caused an unsafe
failure, and flood requests according to whether the limiter accepted or
rejected each request.

| ID | Family | Status | Guess | Score | Verdict |
|---|---|---:|---|---:|---|
| EV01 | evasion | 200 | human | 0.340 | BROKE |
| EV02 | evasion | 200 | unsure | 0.479 | BROKE |
| EV03 | evasion | 200 | unsure | 0.590 | BROKE |
| EV04 | evasion | 200 | unsure | 0.605 | BROKE |
| EV05 | evasion | 200 | human | 0.350 | BROKE |
| EV06 | evasion | 200 | unsure | 0.453 | BROKE |
| EV07 | evasion | 200 | unsure | 0.630 | BROKE |
| EV08 | evasion | 200 | human | 0.342 | BROKE |
| EV09 | evasion | 200 | unsure | 0.609 | BROKE |
| EV10 | evasion | 200 | ai | 0.869 | HELD |
| FP01 | false positive | 200 | unsure | 0.579 | HELD |
| FP02 | false positive | 200 | ai | 0.693 | BROKE |
| FP03 | false positive | 200 | ai | 0.715 | BROKE |
| FP04 | false positive | 200 | ai | 0.711 | BROKE |
| FP05 | false positive | 200 | ai | 0.737 | BROKE |
| FP06 | false positive | 200 | ai | 0.723 | BROKE |
| FP07 | false positive | 200 | ai | 0.720 | BROKE |
| FP08 | false positive | 200 | human | 0.334 | HELD |
| PI01 | prompt injection | 200 | unsure | 0.420 | HELD |
| PI02 | prompt injection | 200 | human | 0.257 | HELD |
| PI03 | prompt injection | 200 | unsure | 0.559 | HELD |
| PI04 | prompt injection | 200 | unsure | 0.478 | HELD |
| PI05 | prompt injection | 200 | unsure | 0.521 | HELD |
| PI06 | prompt injection | 200 | unsure | 0.546 | HELD |
| MF01 | malformed | 400 | — | — | HELD |
| MF02 | malformed | 500 | — | — | BROKE |
| MF03 | malformed | 200 | human | 0.218 | HELD |
| MF04 | malformed | 200 | human | 0.327 | HELD |
| MF05 | malformed | 200 | ai | 0.859 | HELD |
| MF06 | malformed | 200 | ai | 0.998 | HELD |
| MF07 | malformed | 200 | ai | 0.939 | HELD |
| MF08 | malformed | 400 | — | — | HELD |
| RQ01 | malformed | 400 | — | — | HELD |
| RQ02 | malformed | 400 | — | — | HELD |
| RQ03 | malformed | 400 | — | — | HELD |
| RQ04 | malformed | 400 | — | — | HELD |
| RQ05 | malformed | 400 | — | — | HELD |
| RQ06 | malformed | 400 | — | — | HELD |
| RQ07 | malformed | 400 | — | — | HELD |
| RQ08 | malformed | 400 | — | — | HELD |
| RQ09 | malformed | 400 | — | — | HELD |
| RQ10 | malformed | 400 | — | — | HELD |
| RQ11 | malformed | 400 | — | — | HELD |
| RQ12 | malformed | 400 | — | — | HELD |
| FL01_01 | flood_same_creator | 200 | human | 0.269 | BROKE |
| FL01_02 | flood_same_creator | 200 | human | 0.269 | BROKE |
| FL01_03 | flood_same_creator | 200 | human | 0.269 | BROKE |
| FL01_04 | flood_same_creator | 200 | human | 0.269 | BROKE |
| FL01_05 | flood_same_creator | 200 | human | 0.269 | BROKE |
| FL01_06 | flood_same_creator | 200 | human | 0.269 | BROKE |
| FL01_07 | flood_same_creator | 200 | human | 0.269 | BROKE |
| FL01_08 | flood_same_creator | 200 | human | 0.269 | BROKE |
| FL01_09 | flood_same_creator | 200 | human | 0.269 | BROKE |
| FL01_10 | flood_same_creator | 200 | human | 0.269 | BROKE |
| FL01_11 | flood_same_creator | 429 | — | — | HELD |
| FL01_12 | flood_same_creator | 429 | — | — | HELD |

The complete raw report is `results/attack_run_2026-11-04_1719_before.md`.


**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
{
  "combined_score": 0.2795,
  "content_id": "ef5dcabb-b021-49ab-9428-954d3ed9fac6",
  "creator_id": "flood_tester",
  "guess": "human",
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "model_score": 0.2587,
  "status": "decided",
  "style_score": 0.3107,
  "timestamp": "2026-11-03T02:38:38+00:00"
}
{
  "combined_score": 0.2795,
  "content_id": "d0b1bffe-9516-4538-8359-acccfa451d36",
  "creator_id": "flood_tester",
  "guess": "human",
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "model_score": 0.2587,
  "status": "decided",
  "style_score": 0.3107,
  "timestamp": "2026-11-03T02:38:38+00:00"
}
{
  "combined_score": 0.2795,
  "content_id": "73d748f8-99b4-49e0-b6bc-897f3ef01527",
  "creator_id": "flood_tester",
  "guess": "human",
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "model_score": 0.2587,
  "status": "decided",
  "style_score": 0.3107,
  "timestamp": "2026-11-03T02:38:38+00:00"
}
{
  "combined_score": 0.2795,
  "content_id": "ad17ea5a-2aec-40fa-8b69-bc56828ca3df",
  "creator_id": "flood_tester",
  "guess": "human",
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "model_score": 0.2587,
  "status": "decided",
  "style_score": 0.3107,
  "timestamp": "2026-11-03T02:38:38+00:00"
}
{
  "combined_score": 0.2795,
  "content_id": "bba829d7-fcd5-412f-bd51-dee699ea10b8",
  "creator_id": "flood_tester",
  "guess": "human",
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "model_score": 0.2587,
  "status": "decided",
  "style_score": 0.3107,
  "timestamp": "2026-11-03T02:38:39+00:00"
}
{
  "creator_id": "flood_tester",
  "event": "rejected",
  "limit": "10 per 1 minute",
  "reason": "rate_limited",
  "status": "rejected",
  "timestamp": "2026-11-03T02:38:39+00:00"
}
{
  "creator_id": "flood_tester",
  "event": "rejected",
  "limit": "10 per 1 minute",
  "reason": "rate_limited",
  "status": "rejected",
  "timestamp": "2026-11-03T02:38:39+00:00"
}
{
  "creator_id": "flood_tester",
  "event": "rejected",
  "limit": "10 per 1 minute",
  "reason": "rate_limited",
  "status": "rejected",
  "timestamp": "2026-11-03T02:38:39+00:00"
}
{
  "creator_id": "flood_tester",
  "event": "rejected",
  "limit": "10 per 1 minute",
  "reason": "rate_limited",
  "status": "rejected",
  "timestamp": "2026-11-03T02:38:39+00:00"
}
{
  "creator_id": "flood_tester",
  "event": "rejected",
  "limit": "10 per 1 minute",
  "reason": "rate_limited",
  "status": "rejected",
  "timestamp": "2026-11-03T02:38:39+00:00"
}
```

The selected entries below are from the staff attack run and include the
interesting evasion, false-positive, prompt-injection, malformed, and flood
outcomes. The final entry is a rejected request.

```json
{
  "timestamp": "2026-11-05T01:19:26+00:00",
  "content_id": "7d667f76-b8ea-45b7-8cef-ea74b539bd03",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "model_score": 0.7042,
  "style_score": 0.4659,
  "combined_score": 0.6089,
  "label": "We could not confidently determine who wrote this. If this is your work, you can appeal for review.",
  "status": "decided"
}
{
  "timestamp": "2026-11-05T01:19:29+00:00",
  "content_id": "f4773225-c96d-4835-a08d-3b50a6f4bb49",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "model_score": 0.7387,
  "style_score": 0.6233,
  "combined_score": 0.6925,
  "label": "We think this was probably generated by AI. If you wrote this yourself, you can appeal for review.",
  "status": "decided"
}
{
  "timestamp": "2026-11-05T01:19:29+00:00",
  "content_id": "ae520659-b11a-43c4-8f58-d713237c3559",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "model_score": 0.8816,
  "style_score": 0.4784,
  "combined_score": 0.7203,
  "label": "We think this was probably generated by AI. If you wrote this yourself, you can appeal for review.",
  "status": "decided"
}
{
  "timestamp": "2026-11-05T01:19:31+00:00",
  "content_id": "7d37397f-cd47-4712-8bff-7dd97d014992",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "model_score": 0.2044,
  "style_score": 0.3365,
  "combined_score": 0.2572,
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "status": "decided"
}
{
  "timestamp": "2026-11-05T01:19:31+00:00",
  "content_id": "56396853-5f1d-4041-94f0-bd9af2264dec",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "model_score": 0.6401,
  "style_score": 0.342,
  "combined_score": 0.5209,
  "label": "We could not confidently determine who wrote this. If this is your work, you can appeal for review.",
  "status": "decided"
}
{
  "timestamp": "2026-11-05T01:19:34+00:00",
  "content_id": "8ebcde77-9aff-45bc-b596-a9440c317f9e",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "model_score": 0.0,
  "style_score": 0.5447,
  "combined_score": 0.2179,
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "status": "decided"
}
{
  "timestamp": "2026-11-05T01:19:34+00:00",
  "content_id": "d896906e-bc7b-46c4-a93a-3d7ceb406ddc",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "model_score": 0.9969,
  "style_score": 1.0,
  "combined_score": 0.9981,
  "label": "We think this was probably generated by AI. If you wrote this yourself, you can appeal for review.",
  "status": "decided"
}
{
  "timestamp": "2026-11-05T01:19:35+00:00",
  "content_id": "25b39027-944f-4163-9abc-4136d67a6f55",
  "creator_id": "attacker_flood",
  "guess": "human",
  "model_score": 0.0287,
  "style_score": 0.6287,
  "combined_score": 0.2687,
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "status": "decided"
}
{
  "timestamp": "2026-11-05T01:19:36+00:00",
  "content_id": "09c43457-dc8f-4f4f-980f-b2695d24015f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "model_score": 0.0287,
  "style_score": 0.6287,
  "combined_score": 0.2687,
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "status": "decided"
}
{
  "timestamp": "2026-11-05T01:19:36+00:00",
  "creator_id": "attacker_flood",
  "event": "rejected",
  "reason": "rate_limited",
  "limit": "10 per 1 minute",
  "status": "rejected"
}
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it: **FP03**, the careful non-native English writer,
was labeled high-confidence AI with a combined score of `0.7145`.



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. My own writing flagged as AI | At most 1 of 10 in each trial | 1/10 | 1/10 | 1/10 | MET |
| 2. Score separation | AI average at least 0.25 above human average | 0.0460 gap | 0.0460 gap | 0.0460 gap | MISSED |
| 3. Label coverage | All three labels reachable in each run | 2/3 | 2/3 | 2/3 | MISSED |
| 4. Appeal path | 5/5 valid appeals succeed and are recorded | 5/5 | 5/5 | 5/5 | MET |
| 5. Bad input | 10/10 invalid requests return 4xx with no decision | 10/10 | 10/10 | 10/10 | MET |

**Real output from one trial**, pasted as text, naming the file and function
that produced it. The complete three-trial report is
`results/run_2026-11-04_1533_before.md`, produced by
`run_eval.py::main`, calling `app.py::submit` and the appeal path.

```json
{
  "source": "results/run_2026-11-04_1533_before.md, Trial 1",
  "produced_by": "run_eval.py::main",
  "criteria": {
    "1_my_own_writing": [
      {"status": 200, "guess": "unsure", "confidence": 0.4568, "model_score": 0.4808, "style_score": 0.4207},
      {"status": 200, "guess": "unsure", "confidence": 0.5857, "model_score": 0.6102, "style_score": 0.549},
      {"status": 200, "guess": "unsure", "confidence": 0.5916, "model_score": 0.5576, "style_score": 0.6426},
      {"status": 200, "guess": "unsure", "confidence": 0.3594, "model_score": 0.2876, "style_score": 0.4672},
      {"status": 200, "guess": "ai", "confidence": 0.6614, "model_score": 0.6389, "style_score": 0.6952},
      {"status": 200, "guess": "unsure", "confidence": 0.5176, "model_score": 0.6376, "style_score": 0.3376},
      {"status": 200, "guess": "unsure", "confidence": 0.5866, "model_score": 0.613, "style_score": 0.5471},
      {"status": 200, "guess": "unsure", "confidence": 0.4169, "model_score": 0.3437, "style_score": 0.5266},
      {"status": 200, "guess": "unsure", "confidence": 0.5281, "model_score": 0.4343, "style_score": 0.6687},
      {"status": 200, "guess": "unsure", "confidence": 0.5761, "model_score": 0.5901, "style_score": 0.5551}
    ],
    "2_score_separation": [0.5016, 0.5731, 0.5073, 0.4484, 0.5239, 0.4169, 0.5281, 0.5003, 0.3981, 0.4808],
    "3_label_coverage": [
      {"status": 200, "guess": "unsure", "confidence": 0.5016},
      {"status": 200, "guess": "ai", "confidence": 0.6614},
      {"status": 200, "guess": "unsure", "confidence": 0.4769}
    ],
    "4_appeal_path": [
      {"submit_status": 200, "appeal_status": 200, "content_id_preserved": true, "reasoning_recorded": true, "under_review": true},
      {"submit_status": 200, "appeal_status": 200, "content_id_preserved": true, "reasoning_recorded": true, "under_review": true},
      {"submit_status": 200, "appeal_status": 200, "content_id_preserved": true, "reasoning_recorded": true, "under_review": true},
      {"submit_status": 200, "appeal_status": 200, "content_id_preserved": true, "reasoning_recorded": true, "under_review": true},
      {"submit_status": 200, "appeal_status": 200, "content_id_preserved": true, "reasoning_recorded": true, "under_review": true}
    ],
    "5_bad_input": [
      {"status": 400, "guess": null, "confidence": null, "label": null},
      {"status": 400, "guess": null, "confidence": null, "label": null},
      {"status": 400, "guess": null, "confidence": null, "label": null},
      {"status": 400, "guess": null, "confidence": null, "label": null},
      {"status": 400, "guess": null, "confidence": null, "label": null},
      {"status": 400, "guess": null, "confidence": null, "label": null},
      {"status": 400, "guess": null, "confidence": null, "label": null},
      {"status": 400, "guess": null, "confidence": null, "label": null},
      {"status": 400, "guess": null, "confidence": null, "label": null},
      {"status": 400, "guess": null, "confidence": null, "label": null}
    ]
  }
}
```

**Diagnoses**

- **Criterion 2 missed — combining rule / both signals:** the five AI-style
  inputs averaged `0.5109`, while the five human-written inputs averaged
  `0.4648`, a gap of only `0.0460` instead of the target `0.25`. The model and
  style signals assigned overlapping scores to the two groups, and the current
  weighted combination (`0.6` model plus `0.4` style) preserved that overlap.
- **Criterion 3 missed — label mapping:** the run reached `unsure` and `ai`,
  but no input scored below the human threshold of `0.35`. The lowest observed
  combined score was `0.3594`, so the label mapping had no input in its
  high-confidence-human band.
- Criteria 1, 4, and 5 met their targets in all three trials. Criterion 5's
  invalid requests were stopped at the route boundary with 400 responses and
  were not turned into `decided` entries.

**Attack diagnoses**

- **EV01–EV03 and EV06–EV07 — signal two / combining rule:** the evasion text
  changed punctuation, sentence-length spread, quotations, or wording enough
  to alter the style score. The combined score then fell into the human or
  unsure band instead of the AI band, so the edits let the AI text pass.
- **EV04 and EV08 — signal one / combining rule:** unusual vocabulary raised
  perplexity in EV04, while the short below-window text in EV08 produced a low
  model score. With the model signal weighted at `0.6`, those low AI-like model
  scores pulled the combined results to `0.6051` and `0.3419`, respectively,
  so neither received the AI label.
- **EV05 and EV09 — both signals / combining rule:** the human editing pass and
  the human-style opening changed both signal inputs enough to move the result
  to human or unsure. The combining rule therefore did not preserve the AI
  signal for either attack.
- **FP02–FP07 — signal one / combining rule:** formal, structured, repetitive,
  and technical human writing received high model scores (`0.7387` to `0.8816`).
  The style signal did not offset those values enough, and the `0.6` model
  weight pushed every combined score above the `0.65` AI threshold.
- **MF02 — route/dependency boundary:** one-character text passed the route's
  empty and length checks. `detector.perplexity` then raised `ValueError` for
  fewer than three tokens, and `submit` did not catch it, so Flask returned an
  HTML 500 instead of a controlled 4xx response.
- **FL01_01–FL01_10 — rate-limiter stage:** the per-creator limit intentionally
  permits the first ten requests in a minute, so those requests were accepted.
  FL01_11 and FL01_12 were held when the same creator exceeded `10 per 1
  minute` and received 429 responses.
- **PI01–PI06 and the other malformed requests held:** the prompt text did not
  alter the fixed label message or inject fields into the JSONL audit entries,
  and the malformed requests that returned 400 or a normal decision did not
  crash the service. The one malformed attack that did break was MF02 above.

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
