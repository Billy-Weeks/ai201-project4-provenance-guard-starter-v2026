# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1.

Across each of three evaluation trials, no more than 1 of 10 paragraphs that I wrote myself (listed under criterion 1 in `scenarios.py`) may receive the high-confidence AI label.

**Why this target:** A false positive publicly questions a real writer's authorship. I accept that some AI-written text may pass through, because protecting human writers matters more than maximizing accusations.



---

## 2.

In each evaluation trial, the average combined score (`confidence`) of 5 clearly AI-generated texts must be at least 0.25 higher than the average combined score of 5 clearly human-written texts, where both sets are listed under criterion 2 in `scenarios.py`.

**Why this target:** The two signals are useful only if they produce meaningful separation. A 0.25 gap gives the thresholds room to distinguish confident cases while leaving an unsure band for disagreement and borderline writing.



---

## 3.

Within one evaluation run, at least one submission must receive each of the three labels—high-confidence human, unsure, and high-confidence AI—and each label must correspond to a non-overlapping score range defined by the configured thresholds.

**Why this target:** The service must represent uncertainty instead of forcing every submission into an accusation or a clearance. A reachable unsure range is especially important when the model and style signals disagree.



---

## 4.

For 5 out of 5 valid appeals, `POST /appeal` must return a success response, preserve the submitted `content_id` and reasoning, append an appeal entry to `logs/audit.jsonl`, and show the item with status `under_review` in `GET /log`.

**Why this target:** An appeal is the writer's safeguard against a false accusation. Recording every appeal and changing the status makes the response auditable instead of leaving the writer with an unsupported promise that someone will review it.



---

## 5.

For 10 checks—five requests with missing or empty `text` and five requests whose text exceeds the service's documented maximum of 10,000 characters (`config.MAX_TEXT_CHARS`)—the service must return a client-error response (`4xx`), must not return a confidence label, and must not create a `decided` audit entry.

**Why this target:** Invalid input should fail clearly at the boundary rather than crash the detector or create a misleading decision. Rejecting oversized text also protects the local model from unnecessary work and keeps the service's resource limits observable.


---

# Unit 9 — The Capstone

These criteria are for the Shape B extension declared in the Unit 9 section of `README.md`. They were written before Unit 9 feature implementation or result collection. The extension is a safe, observable failure path around detector/scoring failures.

## 1. Safe response when detector scoring fails

Across 5 out of 5 deliberately forced detector failures, `POST /submit` must return a JSON `503` response containing a stable error code, and the response must not contain `guess`, `confidence`, or `label` fields.

**Why this target:** A detector that cannot score should produce a predictable service-level failure rather than a misleading classification. Five trials make the behavior repeatable while keeping the failure test small enough to run locally.

## 2. Failed requests do not create false decisions

Across 5 out of 5 deliberately forced detector failures, the request must create no `decided` audit entry and must not appear as a successful classification in the audit history.

**Why this target:** Recording a decision when the detector failed would falsely claim that Provenance Guard evaluated the text. Zero false decisions is necessary because an incorrect provenance record is more damaging than an explicit temporary failure.

## 3. Failure visibility is complete

Across 5 out of 5 deliberately forced detector failures, the operational log must contain a timestamp, request ID, processing stage, error type, response status, and non-negative duration for the failed request.

**Why this target:** The purpose of the visibility addition is to make a failure diagnosable after the request is over. These fields identify when the failure happened, which request and stage caused it, what response was returned, and how long the failure path took.

## 4. Normal submissions do not regress

Across 9 out of 10 normal submissions after the extension, the service must return HTTP 200 with `content_id`, `guess`, `confidence`, `label`, `model_score`, and `style_score`, and must record one `decided` audit entry.

**Why this target:** The extension must preserve the system it extends. A 9-of-10 target allows for one realistic local-model or environment failure while requiring the normal request path to remain usable and fully populated.

## 5. Timing is recorded on both paths

Across 10 test requests—5 successful submissions and 5 deliberately forced detector failures—the operational log must contain a non-negative total duration in milliseconds for every request.

**Why this target:** Timing is needed to understand the operational cost of both success and failure. Requiring both paths prevents instrumentation from working only for normal decisions while leaving failures invisible.



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
