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

1. A writer sends text and a `creator_id` to `POST /submit` as JSON.
2. The route creates a unique `content_id` so the submission can be audited and appealed later.
3. The detector signal in `detector.py` reads the text for meaning and predictability, then returns a model score from 0 to 1. A higher score means more likely AI-generated.
4. The style signal in `stylometry.py` measures the text’s structure, including sentence-length spread, vocabulary variety, and punctuation density, and returns a style score from 0 to 1.
5. `scoring.py::combine_signals` combines the two signal scores into one confidence score using the weights defined in `config.py`.
6. `scoring.py::score_to_label` maps that score to one of three reader-facing labels: high-confidence human, unsure, or high-confidence AI.
7. The service writes the decision and its signal scores to `logs/audit.jsonl`, then returns the `content_id`, guess, confidence, label, and both signal scores to the caller.

The planned appeal path starts when a writer sends a `content_id` and reasoning to `POST /appeal`. The service verifies that the content exists, appends the appeal to the audit log with status `under_review`, and returns a confirmation without automatically re-checking the text.

### False-positive trace

Consider a real writer who submits a plain, carefully edited paragraph. The model signal may score it as AI-like because its familiar words and predictable sentences produce low perplexity. The style signal may also score it as AI-like if the sentences have similar lengths and the vocabulary repeats. Suppose the combining rule produces an illustrative confidence score of `0.72`; with the current placeholder threshold of `0.65`, the reader would see the high-confidence AI label.

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

For a disagreement case such as plain, formal human writing, the model may produce a relatively high AI-like score because the wording is predictable while the style signal may produce a lower score because sentence lengths and vocabulary vary. The weighted average reduces the model score's effect slightly when the style signal reads the surface form as human-like, while preserving the model as the more influential signal.

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

**Moment 1**

- *What I asked for:* Help reviewing whether my acceptance criteria were measurable and testable.
- *What came back:* Suggestions for numeric targets and observable outcomes.
- *What I changed:* I selected and edited the criteria I wanted to use in `criteria.md`.

**Moment 2**

- *What I asked for:* Help implementing the second signal and combining it with the detector score.
- *What came back:* A stylometry implementation and a weighted scoring rule.
- *What I changed:* I ran calibration tests, compared the results, and documented the limitations in `README.md`.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

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
