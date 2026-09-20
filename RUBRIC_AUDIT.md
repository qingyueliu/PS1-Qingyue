# PS1 v2 rubric audit

This is a preparation checklist, not an instructor score and not part of the two-page main paper.

## 1. Research portfolio

- The paper connects economics (observer incentives and welfare), computation (seeded Q-learning), and behavioral science (report use versus useful information).
- The new C reward treatment is motivated by Zhengjun He; Yichen Shen's stage-incentive concern is answered explicitly.
- The baseline is rerunnable with standard-library Python, fixed seeds, saved outputs, and unit tests.
- The paper distinguishes observed synthetic results from the deferred partner-selection extension and from human evidence.
- The teaser has an editable Draw.io master and vector exports; the game remains a static artifact.
- The foundation-to-2056 roadmap and evidence limitations are explicit.

## Future research

- Vary bonus strength and longer horizons while preserving fixed matching.
- Implement partner selection only as a future extension because it adds a new action space.
- Test whether an institution can align C's private reward with A+B welfare.

## External steps before Canvas submission

- Generate and inspect the v2 PDF in Overleaf separately.
- Obtain reviewer follow-up if it is supplied, then complete Canvas submission.

## Checks completed for v2

- Ten unit tests pass, including downstream reward, welfare accounting, zero-bonus equivalence, report denominator, repeatability, and condition behavior.
- 750 seed-level runs complete: five conditions x five exploration rates x 30 seeds.
- Preserved v1 code reproduces all seven original metrics for 120 runs.
- Local game passes 20 agent/player configuration checks without NaN or undefined outputs.
- GitHub snapshot 2fc74e1 contains the reviewed source, code, notebook, original reviews, outputs, and preserved v1.
- Hugging Face commit 691e720 publishes the matching five-level, market-linked game; hosted and local HTML hashes match.
- V1 ZIP/PDF are byte-preserved; v2 PDF is deliberately not generated in this session.

## Process requirements

The original reviews remain Human-Only contributions and are stored under reviews/original/. The author response covers Yichen Shen and Zhengjun He. Reviewer follow-up and instructor grading are not invented.
