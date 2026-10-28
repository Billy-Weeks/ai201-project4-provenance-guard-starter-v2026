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

**The rule:**

**The numbers:**

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**

This combining rule and its numbers will be selected and recorded before implementation in Milestone 4. A planned disagreement case is plain, formal human writing: the model may find its conventional wording predictable while the style signal may find its sentence and vocabulary patterns human-like. The final rule must document how that disagreement affects the combined score.



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human |  |  |
| unsure |  |  |
| high-confidence AI |  |  |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->



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
  -d '{"text": "...", "creator_id": "..."}'
```

```json

```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "...", "reasoning": "..."}'
```

```json

```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json

```

---

## How I Used AI

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

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
