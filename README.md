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

**Moment 3 — Unit 8 testing and improvement**

- *What I asked for:* I used the AI as a testing partner to help organize my scenarios, check my interpretations, and connect observed failures to specific pipeline stages.
- *What came back:* The baseline showed that the system was repeatable but not well separated: formal human writing often received high AI scores, several evasion inputs moved into the unsure or human bands, and a one-character request crashed inside the detector.
- *What I changed:* I chose the crash because its mechanism was clear and its fix was limited to the route boundary. I added a minimum-token validation rule and measured it again. The fix removed the 500 and produced controlled rejections, but it did not improve the underlying score separation or label coverage.

**Moment 4 — Turning previous writing into repeatable tests**

- *What I asked for:* I asked the AI to inspect two of my previous papers, separate assignment instructions from my authored paragraphs, and help format suitable samples for `scenarios.py`.
- *What came back:* The AI identified four paragraphs from my English paper and six analysis or observation paragraphs from my lab report. It excluded headings, procedures, questions, tables, and copied instructions.
- *What I changed:* I reviewed the selections and confirmed they were my writing before using them. The AI handled the extraction and formatting, but I supplied and approved the source material; it did not invent writing and label it as mine.

**Moment 5 — Checking my diagnoses against the raw scores**

- *What I asked for:* A review of the whole Unit 8 write-up against the instructions, the rubric, and last unit's feedback.
- *What came back:* The verdicts matched the raw run files. But three evasion diagnoses named the wrong signal: EV01's typos fooled signal one (model `0.1635`), not signal two. Held/broke counts were missing, and the after attack table was only a partial table in a different format. The flood rows were marked BROKE with a diagnosis saying they worked as intended. And MF06/MF07, emoji and right-to-left text labeled AI at `0.998` and `0.939`, were marked HELD only because they did not crash.
- *What I changed:* I had the AI rewrite the diagnoses from the per-signal scores in the raw reports. This turned up the main finding of the unit: signal two scores my writing as *more* AI-like than the AI samples (−0.0845). I re-marked MF05–MF07 as BROKE under a stated rule, and added the counts and the full after table. I checked that only MF02, MF05 and MF06 differ between the two raw reports. Nothing was re-run; every number comes from the existing `results/` files and `logs/audit.jsonl`.

**Moment 6 — The second improvement (stretch)**

- *What I asked for:* A second improvement chosen from my own diagnosis, declared before it was built.
- *What came back:* The AI proposed fixing the single-sentence rule in `style_signal`. Because GPT-2's scores were identical across trials, it computed the new style score for every attack and criterion input offline and wrote an exact prediction into the declaration.
- *What I changed:* I committed the declaration first, then the one-function change, then ran both scripts myself. Every predicted number matched the measured one. I kept Criterion 3's verdict as MISSED under the original measurement method, even though the criterion's literal wording would now read as MET, because switching methods after seeing the result would not be an honest comparison.

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

**What a caller counts as:** a `creator_id`. `app.py::rate_limit_key` uses the
request's `creator_id` when it is a non-empty string, and falls back to the
caller's IP address only when it is missing or malformed. This means a
household or classroom sharing one address does not share one limit, but it
also means the limit is easy to dodge: a script that changes `creator_id` on
every request gets a fresh 10-per-minute allowance each time. The staff attack
set shows this directly: every attack submitted as its own `attacker_<id>`, so
only FL01, which reused one creator, ever reached the limit.

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
The last accepted request and the first rejected one from that flood run, as
they appear in `logs/audit.jsonl`:

```json
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
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

The runner produced 56 inputs. I marked evasion attacks as BROKE when they
avoided the AI label, false-positive attacks as BROKE when human text received
the AI label, prompt-injection attacks as BROKE only if their instruction
changed service behavior, and malformed attacks as BROKE when they crashed the
service (a 5xx) or got a high-confidence AI label for input that is not
measurable prose. The second malformed rule follows from my Criterion 1
reasoning: an accusation is the expensive mistake, and calling emoji or a
right-to-left script "probably generated by AI" is still an accusation against
whoever sent it. The flood rows are judged as one attack against the rate
limiter. Requests 1–10 fall inside the configured `10 per 1 minute` and are
accepted by design, and the limiter stopped the flood at request 11, so every
FL01 row is HELD.

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
| MF05 | malformed | 200 | ai | 0.859 | BROKE |
| MF06 | malformed | 200 | ai | 0.998 | BROKE |
| MF07 | malformed | 200 | ai | 0.939 | BROKE |
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
| FL01_01 | flood_same_creator | 200 | human | 0.269 | HELD |
| FL01_02 | flood_same_creator | 200 | human | 0.269 | HELD |
| FL01_03 | flood_same_creator | 200 | human | 0.269 | HELD |
| FL01_04 | flood_same_creator | 200 | human | 0.269 | HELD |
| FL01_05 | flood_same_creator | 200 | human | 0.269 | HELD |
| FL01_06 | flood_same_creator | 200 | human | 0.269 | HELD |
| FL01_07 | flood_same_creator | 200 | human | 0.269 | HELD |
| FL01_08 | flood_same_creator | 200 | human | 0.269 | HELD |
| FL01_09 | flood_same_creator | 200 | human | 0.269 | HELD |
| FL01_10 | flood_same_creator | 200 | human | 0.269 | HELD |
| FL01_11 | flood_same_creator | 429 | — | — | HELD |
| FL01_12 | flood_same_creator | 429 | — | — | HELD |

**Count — before:**

| Family | Attacks | Held | Broke |
|---|---:|---:|---:|
| evasion | 10 | 1 | 9 |
| false positive | 8 | 2 | 6 |
| prompt injection | 6 | 6 | 0 |
| malformed (MF + RQ) | 20 | 16 | 4 |
| flood_same_creator | 12 | 12 | 0 |
| **Total** | **56** | **37** | **19** |

The complete raw report is `results/attack_run_2026-11-04_1719_before.md`. The
Verdict column there is blank except for the one auto-marked 5xx. The marks
above are mine, applied with the rules stated at the top of this section.


**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

All ten come from `logs/audit.jsonl` during the before attack run (creator ids
`attacker_<id>`), in this order:

1. EV01: typos let AI text through as "human." The model score was 0.16, so it was signal one that was fooled.
2. EV09: the model still read it as AI (0.70), but signal two (0.47) pulled it into "unsure."
3. FP03: the worst outcome, a careful non-native writer labeled AI.
4. FP07: deliberate repetition labeled AI, with the highest model score of any FP attack (0.88).
5. PI05: tried to inject into the audit log. It held, because the log never stores the submitted text.
6. MF06: emoji only, labeled AI at 0.998.
7. MF07: right-to-left script, labeled AI at 0.939.
8. RQ01: a route-level rejection (`missing_fields`, HTTP 400).
9. FL01_10: the last flood request the limiter allowed.
10. FL01_11: the first flood request the limiter rejected (HTTP 429).

Two things the log shows that the table does not:

- Rejected entries have no `content_id`, scores or label, because no decision
  was ever made. They carry `timestamp`, `creator_id`, `status` and the reason.
- MF02, the one request that crashed with a 500, has **no entry at all**. The
  exception was raised before `audit.log_decision` or `audit.log_rejection`
  ran, so the only failure that broke the service was also the only one that
  left no trace. The short-input fix below changes that: after it, MF02 is
  logged as a `text_too_short` rejection.

```json
{
  "timestamp": "2026-11-05T01:19:22+00:00",
  "content_id": "a2f9254d-7d42-42a9-9369-c5d6111828df",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "model_score": 0.1635,
  "style_score": 0.6038,
  "combined_score": 0.3396,
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "status": "decided"
}
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
  "timestamp": "2026-11-05T01:19:28+00:00",
  "content_id": "8b5cca78-58ea-4236-bdcc-0786307877d4",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "model_score": 0.8051,
  "style_score": 0.5785,
  "combined_score": 0.7145,
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
  "content_id": "57c1761a-8218-4501-b3a1-ec7b5ca7d6f0",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "model_score": 0.9064,
  "style_score": 0.9888,
  "combined_score": 0.9394,
  "label": "We think this was probably generated by AI. If you wrote this yourself, you can appeal for review.",
  "status": "decided"
}
{
  "timestamp": "2026-11-05T01:19:35+00:00",
  "creator_id": "attacker_RQ01",
  "event": "rejected",
  "status": "rejected",
  "reason": "missing_fields",
  "message": "POST /submit requires text and creator_id."
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
  "status": "rejected",
  "reason": "rate_limited",
  "limit": "10 per 1 minute"
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

**Real output from one trial**, pasted as text. The complete three-trial report
is `results/run_2026-11-04_1533_before.md`, produced by `run_eval.py::main`,
which sends each scenario in `scenarios.py` to `app.py::submit` (and to
`app.py::appeal` for Criterion 4).

This is Criterion 3, Trial 1, copied verbatim from that file. It is the run
that shows the miss: the AI-written sample came back `unsure`, my own lab
paragraph came back `ai`, and nothing reached `human`.

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5016,
    "model_score": 0.4582,
    "style_score": 0.5667,
    "label": "We could not confidently determine who wrote this. If this is your work, you can appeal for review.",
    "sent": "The implementation of a reliable measurement system requires careful c"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6614,
    "model_score": 0.6389,
    "style_score": 0.6952,
    "label": "We think this was probably generated by AI. If you wrote this yourself, you can appeal for review.",
    "sent": "With the much large resistance values (1 M\u03a9, 470 k\u03a9, 100 k\u03a9) there was"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4769,
    "model_score": 0.4665,
    "style_score": 0.4925,
    "label": "We could not confidently determine who wrote this. If this is your work, you can appeal for review.",
    "sent": "Sometimes a result looks convincing at first because the numbers seem "
  }
]
```

A condensed view of Trial 1 for all five criteria, from the same file. The
fields are trimmed to keep it readable; the numbers are copied, not
recalculated:

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

- **Criterion 2 missed. Stage: signal two, which the combining rule then lets
  cancel signal one.** Averaged over the five AI and five human inputs, Trial 1:

  | Signal | AI average | Human average | Separation |
  |---|---:|---:|---:|
  | model (signal one) | 0.5196 | 0.3865 | +0.1331 |
  | style (signal two) | 0.4978 | 0.5823 | **−0.0845** |
  | combined (0.6 / 0.4) | 0.5109 | 0.4648 | +0.0460 |

  Signal one separates the groups in the right direction, though by less
  than 0.25 on its own. Signal two runs **backwards** on this set: it rates
  my writing as more AI-like than the AI text. Two features in
  `stylometry.style_signal` cause this. First, vocabulary variety: my lab
  paragraphs repeat technical terms (resistor, voltage, DMM, function
  generator), so their type-token ratio averages 0.77 against 0.89 for the
  AI samples, and lower variety scores as more AI. Second, sentence spread:
  one of my paragraphs is a single sentence, and `sentence_length_spread`
  returns 0 for fewer than two sentences, which `style_signal` maps to the
  most AI-like value. The third feature, punctuation density, sits around
  0.02 for both groups against the 0.20 cap, so it adds about 0.18 to every
  text and separates nothing. Because a weighted average can only land
  between its inputs, `0.6 × 0.1331 + 0.4 × (−0.0845) = 0.046`. The combining
  rule faithfully passes on a signal that points the wrong way.
- **Criterion 3 missed. Stage: signal two (the single-sentence rule), with
  signal one never going low enough to compensate.** With style scores
  between 0.34 and 0.70 for every input in the run, the combined score can
  only drop below 0.35 if the model score is very low. The lowest model
  score in the entire run was `0.2194`, for my one-sentence DC-offset
  paragraph. On its own that would have put it in the human band, but signal
  two scored it `0.6661` because it is one sentence (the zero-spread rule
  above), and `0.6 × 0.2194 + 0.4 × 0.6661 = 0.398` landed it in "unsure."
  With a style score below about 0.55, it would have reached the human label.
  The three label-coverage inputs also inverted: the AI sample got model
  `0.4582` ("unsure"), and my own lab paragraph got model `0.6389` and style
  `0.6952` ("ai"). The thresholds themselves are fine. No input reached the
  human band because of what the signals feed into them.
- Criteria 1, 4, and 5 met their targets in all three trials, with identical
  results in each trial, so there was no instability to explain. Criterion
  5's invalid requests were stopped at the route with 400 responses and no
  label. Criterion 1 met its target exactly at the limit (1 of 10 in every
  trial), and that one flagged paragraph is the same lab paragraph that
  inverted in Criterion 3.

**Attack diagnoses**

Signal scores below are copied from `results/attack_run_2026-11-04_1719_before.md`.

- **Signal one fooled: EV01 (typos), EV07 (punctuation padding), EV08 (text
  below the token window).** Model scores were `0.1635`, `0.5862` and `0.2452`,
  while the style scores stayed middling to AI-like (`0.6038`, `0.6956`,
  `0.4870`).
  Misspellings and stray punctuation marks are rare token sequences for
  GPT-2, so they raise perplexity, and `model_signal` maps higher perplexity
  to a lower AI score. EV08's short text gives the model too little context to
  find it predictable. The staff set aimed EV01 and EV07 at signal two, but
  signal two was not the stage that broke: EV07's style score of `0.6956` is
  the most AI-like of any evasion attack except EV10. The model signal
  carries `0.6` of the weight, so its drop decided the label.
- **Signal two fooled: EV02 (broken-up sentences), EV03 (pasted quotation),
  EV06 (one very long sentence and one very short), EV09 (human opening
  bolted on).** Model scores stayed AI-like (`0.5943`, `0.6662`, `0.5727`,
  `0.7042`), but style scores fell to `0.3067`, `0.4768`, `0.2729` and `0.4659`.
  Each edit changes sentence-length spread, which carries the largest style
  weight (`0.45`), and in EV09 the bolted-on human paragraph adds sentences
  of a different shape to the rest. Even where signal one still read AI
  (EV03, EV09), the combining rule averaged it with the lower style score and
  landed below `0.65`.
- **Both signals fooled: EV05 (heavy human editing pass).** Model `0.3212` and
  style `0.3930`. The editing changed both the wording (perplexity) and the
  shape (spread and vocabulary), so no stage had anything left to catch.
- **Label mapping: EV04 (unusual words).** Model `0.6114` and style `0.5956`.
  Both signals lean AI, but both sit below `0.65`, and a weighted average
  cannot exceed its larger input. So the `0.65` threshold cannot be reached
  unless at least one signal clears it. The unusual vocabulary left signal one
  just under the line, giving a combined score of `0.6051`.
- **Signal one: FP02–FP07 (formal, non-native, rubric-essay, technical,
  template, and deliberately repetitive human writing).** Model scores were
  `0.7387`–`0.8816`. Careful, conventional prose is exactly what a language
  model finds predictable, so low perplexity reads as AI. That is the blind
  spot named under Signal one above. Signal two did not pull these back
  (`0.4784`–`0.6426`) for the same reasons as in Criterion 2, and with `0.6`
  on the model, every combined score cleared `0.65`. This is one problem
  showing up six times, not six problems.
- **Route: MF02 (one character).** It passed the route's empty and length
  checks. `detector.perplexity` then raised `ValueError` because there were
  fewer than three tokens. `submit` did not catch it, so Flask returned an
  HTML 500 and no audit entry was written.
- **Route, then both signals: MF05 (one very long word), MF06 (emoji only),
  MF07 (right-to-left script).** The route lets any non-empty text through,
  and neither signal can measure these inputs. Both then fail toward "AI":
  - **Signal one:** GPT-2's byte-level tokenizer breaks each emoji, non-Latin
    character, or unbroken run of letters into several byte tokens, and once
    the first byte is seen the rest are nearly certain. Very low perplexity
    gave model scores of `0.9976`, `0.9969` and `0.9064`.
  - **Signal two:** `stylometry.words` only matches `[a-z0-9']`, so emoji and
    right-to-left (non-Latin) text contain *zero* words. Zero words gives
    zero sentence spread and zero vocabulary variety, which `style_signal` maps to the most
    AI-like values, hence style `1.0` for MF06 and `0.9888` for MF07.
- **What held, and why.**
  - **PI01–PI06:** the label text is a fixed string from `scoring.py`, and
    nothing reads the submitted text as instructions. PI05's attempted log
    injection had nowhere to land: the audit log never stores the submitted
    text, only ids, scores and the label, and every entry is written with
    `json.dumps`, so it stays one well-formed line.
  - **RQ01–RQ12, MF01, MF08:** rejected at the route with 400.
  - **MF03 and MF04:** they reached the signals but were labeled "human," so
    no one was accused.
  - **FL01:** the limiter stopped the flood at request 11.

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

**What I changed:** I added a route-boundary check in `app.py::submit` that
rejects text with fewer than three whitespace-separated tokens. It returns a
400 `text_too_short` response and writes a rejection entry before the detector
is called.

**Which diagnosis pointed at it:** the MF02 diagnosis, at the route stage.
The baseline `MF02` attack sent one character. The route accepted it because
it was non-empty and under the size limit. Then `detector.perplexity` raised
`ValueError` for fewer than three tokens, and Flask returned an unhandled 500
with no audit entry. I chose this one because the mechanism was certain and
the fix sits entirely at the route, so it cannot move any score. That keeps
the before/after comparison clean. The fix also covers MF05 and MF06, which
are under three whitespace tokens. Before the fix they did not crash; they
were accused (`0.859` and `0.998`), for the route-then-both-signals reason
diagnosed above.

Why three whitespace tokens: every whitespace-separated word becomes at least
one GPT-2 token, so any text that passes this check has at least three model
tokens. That means the `ValueError` branch in `detector.perplexity` can no
longer be reached from `/submit`.

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->

Produced by `run_attacks.py::main`; the raw report is
`results/attack_run_2026-11-04_1854_after.md`. The same 56 attacks, in the
same order, judged by the same rules as the before table. Only three rows
differ from before: MF02 (500 → 400), MF05 (200 `ai` → 400) and MF06 (200 `ai`
→ 400). I checked this row by row against both raw reports; every other row
has the same status, guess and score.

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
| MF02 | malformed | 400 | — | — | HELD |
| MF03 | malformed | 200 | human | 0.218 | HELD |
| MF04 | malformed | 200 | human | 0.327 | HELD |
| MF05 | malformed | 400 | — | — | HELD |
| MF06 | malformed | 400 | — | — | HELD |
| MF07 | malformed | 200 | ai | 0.939 | BROKE |
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
| FL01_01 | flood_same_creator | 200 | human | 0.269 | HELD |
| FL01_02 | flood_same_creator | 200 | human | 0.269 | HELD |
| FL01_03 | flood_same_creator | 200 | human | 0.269 | HELD |
| FL01_04 | flood_same_creator | 200 | human | 0.269 | HELD |
| FL01_05 | flood_same_creator | 200 | human | 0.269 | HELD |
| FL01_06 | flood_same_creator | 200 | human | 0.269 | HELD |
| FL01_07 | flood_same_creator | 200 | human | 0.269 | HELD |
| FL01_08 | flood_same_creator | 200 | human | 0.269 | HELD |
| FL01_09 | flood_same_creator | 200 | human | 0.269 | HELD |
| FL01_10 | flood_same_creator | 200 | human | 0.269 | HELD |
| FL01_11 | flood_same_creator | 429 | — | — | HELD |
| FL01_12 | flood_same_creator | 429 | — | — | HELD |

**Count — before and after:**

| Family | Attacks | Broke before | Broke after |
|---|---:|---:|---:|
| evasion | 10 | 9 | 9 |
| false positive | 8 | 6 | 6 |
| prompt injection | 6 | 0 | 0 |
| malformed (MF + RQ) | 20 | 4 | **1** |
| flood_same_creator | 12 | 0 | 0 |
| **Total** | **56** | **19** | **16** |

Held went from 37 to 40.

### Criteria Run — After

The after criteria run was produced by `run_eval.py::main` in
`results/run_2026-11-04_1855_after.md`. Every trial's numbers are identical to
the before run, so the before and after verdicts compare directly:

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. My own writing flagged as AI | At most 1 of 10 in each trial | 1/10 | 1/10 | 1/10 | MET |
| 2. Score separation | AI average at least 0.25 above human average | 0.0460 gap | 0.0460 gap | 0.0460 gap | MISSED |
| 3. Label coverage | All three labels reachable in each run | 2/3 | 2/3 | 2/3 | MISSED |
| 4. Appeal path | 5/5 valid appeals succeed and are recorded | 5/5 | 5/5 | 5/5 | MET |
| 5. Bad input | 10/10 invalid requests return 4xx with no decision | 10/10 | 10/10 | 10/10 | MET |


**Did it help, and how do I know:** Yes, for what it targeted, and only that.
Broken attacks went from 19 to 16. The only 5xx in the attack set is gone,
MF02 now leaves a `text_too_short` entry in the audit log instead of no trace,
and two false accusations (MF05, MF06) became honest 400s. The criteria run is
unchanged in every trial. That is expected, because no criterion input is
under three words, and it confirms the fix did not move any score. It did
nothing for Criteria 2 and 3 or for the evasion and false-positive attacks,
which are signal problems, not route problems.

**What it cost:** any submission under three words is now refused, even a
genuine one. MF05 shows the sharper edge: a single long word was *scorable*
before (it returned a 200), and now it is refused. The whitespace count is a
stand-in for "the model has enough to read," and it is stricter than the
model needs. It also does not protect MF07: right-to-left text with spaces
passes the check and is still accused at `0.939`.

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->

The 16 attacks still breaking, and the two missed criteria, come down to four
problems. They are ordered by harm, and each has what I would do next.

1. **False accusations: FP02–FP07, MF07, and Criterion 1's flagged lab
   paragraph.** Stage: signal one, with signal two failing to offset it (for
   MF07, the route lets unmeasurable text reach both signals). *Next:* the Criterion 2 table shows signal two
   pointing the wrong way on my writing, so I would first fix two things in
   `stylometry.py`. A single sentence should be "can't measure," not "most
   AI." And text with no `[a-z0-9']` words should be refused at the route
   rather than scored. I would also lower `WEIGHT_STYLE_SIGNAL` until those
   are fixed. *Measured prediction:* with the style weight at 0, the
   Criterion 2 gap would equal signal one's `0.1331`, which is still a miss
   but three times better. Criterion 1 would also improve, because none of my
   ten paragraphs has a model score above `0.65`. But FP02–FP07 would become
   more confident accusations, because all six have model scores above
   `0.65`. That is exactly the trade below, so it has to
   be measured, not assumed.
2. **Evasion: EV01–EV09.** Stages: signal one (EV01, EV07, EV08), signal two
   (EV02, EV03, EV06, EV09), both (EV05), and the label mapping (EV04). Simple
   edits move either signal, and a weighted average follows whichever moved.
   *Next:* nothing that would make false positives worse. On this service I
   would rather miss these than catch them by lowering the AI threshold.
3. **Criterion 3, no human label.** Its main cause is the single-sentence rule
   in item 1, so it would be re-measured after that fix rather than handled
   separately. *Done as the stretch below:* that fix produced the first human
   label in my criteria runs, but Criterion 3 as measured is still 2/3.
4. **Rate limit is per `creator_id`, and creator ids are free.** Stage: the
   route. Apart from the 12 FL01 flood rows, every staff attack used its own
   creator id, so none of the other 44 came near a limit. *Next:* add a
   per-address limit alongside the per-creator one, so that changing ids
   still runs into a ceiling.

Two smaller route gaps I found while diagnosing:

- `submit` still does not catch exceptions from the signals. The short-input
  check closes the one `ValueError` the attack set reached, but a
  `DetectorUnavailable` or any future exception would still be a bare 500
  with no audit entry.
- Rejected entries do not carry all nine audit fields. `content_id`, the
  scores and the label are absent rather than `null`, because no decision
  was made.

**Why I stopped:** the unit allows one improvement so that before and after
compare directly. I picked the one whose mechanism I was surest of and whose
fix could not move any score. Items 1–3 are scoring changes, and each one
trades false positives against missed AI text, so each would need its own
full before/after run.

**Feedback from unit 7 I deliberately did not act on this unit:**

- the redundant `isinstance` check after `get_json(...) or {}` in `submit`
- the duplicated "original decision" lookup in `appeal` and `get_content`,
  which belongs in a helper in `audit.py`
- moving the `0.45/0.35/0.20` style weights and the `0.20` punctuation cap
  into `config.py`

None of these changes behavior, and the unit asks for no side changes between
the before and after runs, so I left them for after submission. The third
matters more now than it did: the `0.20` cap is why punctuation density adds
the same ~0.18 to every text in the Criterion 2 diagnosis, and item 1's fix
would be a config edit instead of a code edit if it lived in `config.py`. The
fourth piece of feedback, making calibration repeatable, I did act on: my own
writing and my comparison texts now live in `scenarios.py` and are re-run by
`run_eval.py`.



**The trade I'd make if this ran for real:**

I would prefer a wider unsure band and fewer high-confidence accusations, even
if more AI-written text passes through undetected. The people who pay for that
are readers, and honest writers whose work sits beside AI text the service
let through unlabeled. The alternative makes individual real writers pay
through public false accusations, like FP03, which is the more serious harm.

---

## Unit 8 Stretch — Second Measured Improvement

**Declared (not yet built).** This section is committed before any code
changes, so the history shows the declaration came first.

**What I will change:** in `stylometry.py`, a text with fewer than two
sentences will no longer get the most AI-like sentence-spread value. Right
now `sentence_length_spread` returns `0` when there is only one sentence, and
`style_signal` turns that into `spread_ai = 1.0`, the strongest possible "AI"
reading. After the change, a single-sentence text will be treated as having
no spread measurement. `style_signal` will leave that feature out and
reweight the two features it *can* measure (vocabulary `0.35` and punctuation
`0.20`, rescaled to sum to 1). Texts with two or more sentences will score
exactly as before. Nothing else will change: not the model signal, the
weights in `config.py`, the thresholds, or the route.

**Which diagnosis points at it:** the Criterion 2 and Criterion 3 diagnoses
above, at the signal two stage. The lowest model score in the whole run
(`0.2194`, my one-sentence DC-offset paragraph) would have reached the human
band, but the single-sentence rule pushed its style score to `0.6661` and
its combined score to `0.398`. "I could not measure this" was being scored
as "this looks like AI."

**Prediction, written before building.** Because the model signal gave
identical scores in every trial, I can recompute the new style scores for
every input offline and predict the results exactly:

| Measure | Now | Predicted after |
|---|---|---|
| Criterion 1 (my writing flagged AI) | 1/10 | 1/10, no change |
| Criterion 2 (score gap) | 0.0460 | 0.0679, still MISSED |
| Criterion 3 (labels from its three inputs) | 2/3 | 2/3, still MISSED |
| DC-offset paragraph (Criterion 2 input) | 0.398 unsure | 0.289 **human**, the first human label in any criteria run |
| Attack verdicts | 16 broke / 40 held | no verdict changes |
| EV07 (evasion) | 0.630 unsure | 0.530 unsure, further from the AI label |
| FL01 flood text, MF03, MF04 | human | still human, with lower scores |

**What it is expected to cost:** single-sentence AI text gets an easier
path. EV07 is a one-sentence evasion attack, and its score drops by `0.10`.
It is already BROKE, so the count does not change, but it moves further from
being caught.

**How it will be measured:** the same way as the first improvement:

```
python run_attacks.py --set attack_set --label after2
python run_eval.py --label after2
```

I will report a third attack table and a third criteria table in the same
format as the two above, compare them with the prediction, and state plainly
whether the change helped and what it cost.

### Built: what changed

`stylometry.py::style_signal` now counts the sentences that contain words.
With fewer than two, it scores `(0.35 × vocabulary_ai + 0.20 ×
punctuation_ai) / 0.55` and leaves sentence spread out. With two or more, it
uses the original three-feature formula unchanged. No other file changed. The
declaration above was committed first (`7e573d9`), then the code (`7c1d187`),
then these runs.

### Attack Run — After 2

Produced by `run_attacks.py::main`; the raw report is
`results/attack_run_2026-11-04_2146_after2.md`. The same 56 attacks, in the
same order, judged by the same rules as the two tables above. Compared with
the first after run, 14 rows changed score, and they are exactly the 14
inputs that are a single sentence: EV07, MF03, MF04, MF07 and FL01_01–10. No
row changed status, guess or verdict.

| ID | Family | Status | Guess | Score | Verdict |
|---|---|---:|---|---:|---|
| EV01 | evasion | 200 | human | 0.340 | BROKE |
| EV02 | evasion | 200 | unsure | 0.479 | BROKE |
| EV03 | evasion | 200 | unsure | 0.590 | BROKE |
| EV04 | evasion | 200 | unsure | 0.605 | BROKE |
| EV05 | evasion | 200 | human | 0.350 | BROKE |
| EV06 | evasion | 200 | unsure | 0.453 | BROKE |
| EV07 | evasion | 200 | unsure | 0.530 | BROKE |
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
| MF02 | malformed | 400 | — | — | HELD |
| MF03 | malformed | 200 | human | 0.069 | HELD |
| MF04 | malformed | 200 | human | 0.261 | HELD |
| MF05 | malformed | 400 | — | — | HELD |
| MF06 | malformed | 400 | — | — | HELD |
| MF07 | malformed | 200 | ai | 0.936 | BROKE |
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
| FL01_01 | flood_same_creator | 200 | human | 0.147 | HELD |
| FL01_02 | flood_same_creator | 200 | human | 0.147 | HELD |
| FL01_03 | flood_same_creator | 200 | human | 0.147 | HELD |
| FL01_04 | flood_same_creator | 200 | human | 0.147 | HELD |
| FL01_05 | flood_same_creator | 200 | human | 0.147 | HELD |
| FL01_06 | flood_same_creator | 200 | human | 0.147 | HELD |
| FL01_07 | flood_same_creator | 200 | human | 0.147 | HELD |
| FL01_08 | flood_same_creator | 200 | human | 0.147 | HELD |
| FL01_09 | flood_same_creator | 200 | human | 0.147 | HELD |
| FL01_10 | flood_same_creator | 200 | human | 0.147 | HELD |
| FL01_11 | flood_same_creator | 429 | — | — | HELD |
| FL01_12 | flood_same_creator | 429 | — | — | HELD |

**Count — before, after, after 2:**

| Family | Attacks | Broke before | Broke after | Broke after 2 |
|---|---:|---:|---:|---:|
| evasion | 10 | 9 | 9 | 9 |
| false positive | 8 | 6 | 6 | 6 |
| prompt injection | 6 | 0 | 0 | 0 |
| malformed (MF + RQ) | 20 | 4 | 1 | 1 |
| flood_same_creator | 12 | 0 | 0 | 0 |
| **Total** | **56** | **19** | **16** | **16** |

### Criteria Run — After 2

Produced by `run_eval.py::main`; the raw report is
`results/run_2026-11-04_2150_after2.md`.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. My own writing flagged as AI | At most 1 of 10 in each trial | 1/10 | 1/10 | 1/10 | MET |
| 2. Score separation | AI average at least 0.25 above human average | 0.0679 gap | 0.0679 gap | 0.0679 gap | MISSED |
| 3. Label coverage | All three labels reachable in each run | 2/3 | 2/3 | 2/3 | MISSED |
| 4. Appeal path | 5/5 valid appeals succeed and are recorded | 5/5 | 5/5 | 5/5 | MET |
| 5. Bad input | 10/10 invalid requests return 4xx with no decision | 10/10 | 10/10 | 10/10 | MET |

Real output: my one-sentence DC-offset paragraph (Criterion 2 input 9),
Trial 1, copied verbatim from `results/run_2026-11-04_2150_after2.md`. Before
this change it scored `0.3981` "unsure" with `style_score` `0.6661`:

```json
{
  "status": 200,
  "guess": "human",
  "confidence": 0.2888,
  "model_score": 0.2194,
  "style_score": 0.393,
  "label": "We think this was probably written by a person. If this is your work, no action is needed.",
  "sent": "When applying a -1 V DC offset, an inverse shift in the DC domain is p"
}
```

And the cost, EV07, copied verbatim from
`results/attack_run_2026-11-04_2146_after2.md`. Before this change it scored
`0.63` with `style_score` `0.6956`:

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

### Prediction vs. result

| Measure | Predicted | Measured |
|---|---|---|
| Criterion 1 | 1/10 | 1/10 in all three trials |
| Criterion 2 gap | 0.0679 | 0.0679 in all three trials |
| Criterion 3 | 2/3 | 2/3 in all three trials |
| DC-offset paragraph | 0.289 human | 0.2888 human in all three trials |
| Attack verdicts | no change | no change (16 broke / 40 held) |
| EV07 | 0.530 unsure | 0.5304 unsure |
| FL01, MF03, MF04 | still human, lower | 0.1472, 0.0689, 0.2613: all human |

Every prediction held to the fourth decimal place. That was expected: GPT-2's
scores are deterministic, and the change only touches the style signal,
which is plain arithmetic.

**Did it help, and how do I know:** a little, and only where the diagnosis
said it would.
- Criterion 2's gap improved from `0.0460` to `0.0679`, about 48%, but it is
  still far short of `0.25`.
- My DC-offset paragraph now gets the human label in every trial. It is the
  first human label any of my criteria runs has produced, and it comes from
  exactly the input the Criterion 3 diagnosis named.
- Criterion 3 stays MISSED as I measure it, from its own three scenario
  inputs, and I kept that method so all three tables compare directly.
  Strictly, the criterion's wording is "within one evaluation run, at least
  one submission must receive each of the three labels," and under that
  wording each after-2 trial now contains all three labels: human from the
  DC-offset paragraph, unsure and ai from the others. I am not changing the
  verdict, because that would change how the criterion is measured after
  seeing the result. I note it as the most likely next MET.
- Criteria 1, 4 and 5 and all 56 attack verdicts are unchanged.

**What it cost:** exactly the declared cost. Single-sentence text is now
judged on vocabulary and punctuation alone, and for EV07, a one-sentence
evasion attack, that lowered its score from `0.63` to `0.5304`. EV07 was
already BROKE, so the count did not change, but the attack now clears the AI
threshold by `0.12` instead of `0.02`. Any one-sentence AI text gains the
same easier path. Signal two's backwards reading on my multi-sentence
writing (the vocabulary-variety half of the Criterion 2 diagnosis) is
untouched. That is why the gap is still small, and it is the next thing to
fix.



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

---

# Unit 9 — The Capstone

## What This Extends

This unit extends the existing **Provenance Guard** service from Units 7 and 8. The original system accepts text through `POST /submit`, combines the detector and stylometry signals, assigns a label, records decisions in the audit log, supports appeals, and handles rate-limited or invalid requests.

The new work will add one bounded failure-handling layer around request processing: when scoring cannot complete normally because the detector is unavailable or raises an unexpected scoring error, the service will return a safe client-visible error and record the failure as structured operational evidence. The new records will include enough visibility to connect a request to its outcome, duration, processing stage, and failure reason without creating a misleading `decided` audit entry.

## The Shape

**Shape B — Harden against failure.**

The extension is the safe, observable failure path for detector/scoring failures. A normal request must continue to produce the existing response and audit decision. A deliberately triggered failure must return a documented error response, leave no false decision, and produce a structured failure record that can be inspected after the service has run.

The visibility work is supporting instrumentation for this failure path: it will make the failure observable after the fact, not become a separate dashboard or product feature.

### Out of scope

This unit will not retrain or recalibrate the detector, redesign the scoring model, add a new user-facing endpoint or dashboard, change the existing appeal workflow, or deploy the local model to a hosted service. It will also not change the existing rate-limit policy except where needed to preserve and test its current behavior.

The first implementation step is to define the five Unit 9 acceptance criteria in `criteria.md` before changing feature code.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
