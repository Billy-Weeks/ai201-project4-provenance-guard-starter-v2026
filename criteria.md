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

Across each of three evaluation trials, no more than 1 of 10 submissions that I identify as human-written may receive the high-confidence AI label.

**Why this target:** A false positive publicly questions a real writer's authorship. I accept that some AI-written text may pass through, because protecting human writers matters more than maximizing accusations.



---

## 2.

In each evaluation trial, the average combined score for the clearly-AI test set must be at least 0.25 higher than the average combined score for the clearly-human test set.

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

For 10 checks—five requests with missing or empty `text` and five requests whose text exceeds the service's documented maximum—the service must return a client-error response (`4xx`), must not return a confidence label, and must not create a `decided` audit entry.

**Why this target:** Invalid input should fail clearly at the boundary rather than crash the detector or create a misleading decision. Rejecting oversized text also protects the local model from unnecessary work and keeps the service's resource limits observable.



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
