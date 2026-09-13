# PS1 rubric audit

This is a preparation checklist, not an instructor score and not part of the two-page main paper.

## 1. Research portfolio (60 points)

Current evidence for the Q 70--84 band:

- The paper connects economics (credible incentives and welfare), computation (seeded Q-learning), and behavioral science (calibrated trust versus payoff learning).
- The central baseline is rerunnable with standard-library Python, fixed seeds, saved results, and unit tests.
- The paper distinguishes obtained synthetic results from future partner-selection tests and from human evidence.
- The teaser has an editable Draw.io master and vector exports; the static game has no external dependencies.
- The foundation-to-2056 roadmap and evidence limitations are explicit.

Potential route toward Q 85--100:

- Implement the proposed partner-selection treatment, pre-register its directional test, and report seed-level uncertainty rather than only means.
- Explain more precisely when the third party benefits from downstream manipulation; the current reporter has an intrinsic truth reward but no instrumental payoff from A's decision.

Threshold blockers before submission:

- Upload this project version to the public fork `https://github.com/qingyueliu/PS1-Qingyue`.
- Confirm the Colab link runs from a clean session.
- Confirm the published Hugging Face interaction works in a signed-out browser window.
- Replace `[ADD COMMIT]` with the exact submitted commit hash.
- Confirm the email address, field-photo authorship, workshop role, and acknowledgements.

## 2. Peer review (15 points)

This work cannot be prepared by AI. Complete two Human-Only reviews through the authorized class channel. For each one, identify a concrete strength, one feasible priority improvement, and a scientific-communication question; state which paper location, figure, notebook cell, or demo behavior you actually checked. After each author responds, explain whether the main concern was resolved.

## 3. Author response (10 points)

After receiving both reviews, answer every substantive concern. For each response, cite a page, section, figure, notebook cell, or output; say whether the point was changed, retained, or deferred and why; distinguish completed checks from future plans.

## 4. Revision (15 points)

Preserve this v1 and create v2. Keep a traceable table containing: reviewer concern, decision, affected artifact/location, concrete change, command or interaction rerun, observed result, and remaining limitation. Update Appendix E to explain the intellectual change, not only the wording change.

## Checks already completed for v1

- Six unit tests pass: payoff matrix, strict dominance, seed repeatability, condition coverage, verified-report behavior, and the fixed-exploration higher-cost comparison.
- Thirty fixed seeds and 10,000 focal rounds per condition reproduce the saved means.
- The PDF renders without overlap or clipping; the five numbered main sections occupy two pages.
- The ZIP archive passes an integrity check.
