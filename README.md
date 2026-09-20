# When Honest Reports Fail to Sustain Cooperation — PS1 v2

Qingyue Liu's COMSCI/ECON 206 PS1 v2 proposal studies a repeated Prisoner's Dilemma in which an observer can report a partner's previous action truthfully or falsely. It asks how uncertain reports affect cooperation when the observer receives a bonus after A cooperates.

This project adapts the official course repository dku-comsci-econ206-Autumn2026/ps1-overleaf-template. The paper, editable figure, computational baseline, saved outputs, tests, and browser game are organized within that course structure.

## Research positioning

Leung et al. (2026) provide the related-work baseline by studying independent RL agents that use minimal third-party observation and partner selection to support cooperation. PS1 v2 does not reproduce their population or interaction-network model. It holds A–B matching, payoffs, and learning settings fixed, defers partner selection, and changes only C's reporting incentive by adding a bonus after A cooperates. The contribution is a controlled incentive extension testing whether C's private reward improves report usefulness, A–B cooperation, and A+B welfare.

## Research artifacts

- main.tex, sections/proposal.tex, and appendices/supporting.tex: ACM two-column proposal and supporting material.
- figures/ps1_teaser.drawio: editable Draw.io master; PDF and SVG are vector exports of the same design.
- companion/src/strategic_reporting.py: standard-library reconstruction of the model.
- companion/notebooks/strategic_reporting_qlearning.ipynb: self-contained Colab notebook.
- companion/outputs/ps1_condition_panel.json: default exploration summary from 30 fixed seeds.
- companion/outputs/ps1_revision_panel.json: 750 seed-level v2 runs across five conditions and five exploration rates.
- companion/hf_space/index.html: static interactive game for Hugging Face Spaces.
- AUTHOR_RESPONSE.md, REVISION_LOG.md, reviews/, archive/v1/: response, traceability, original reviews, and preserved v1.

## Reproduce the computational check

Python 3.10 or later is sufficient for the model.

    python3 scripts/run_revision_checks.py
    python3 -m unittest discover -s companion/tests -p 'test_strategic_reporting.py'
    python3 scripts/check_v1_equivalence.py
    node scripts/check_game.mjs

The v2 panel uses 10,000 rounds for each of seeds 0--29 and five exploration rates. It compares no reports, strategic reports, verified truth with forced use, a C cooperation bonus, and the retained higher lying cost. Outputs are synthetic learning-model results, not observations of human participants or deployed AI systems.

To try the educational game locally, open companion/hf_space/index.html in a browser. It exposes no-report, strategic, market-linked, and verified conditions plus five clearly explained exploration rates. The central claim is conditional: under the specified learning rules and horizons, C's private cooperation bonus raises C's reward but does not clearly raise A+B cooperation or welfare.

## Rubric readiness

RUBRIC_AUDIT.md maps v2 to the instructor's four-part scorecard. V1, original reviews, author response, v2 source, tests, seed-level outputs, and artifact links are retained. V2 PDF compilation, remote publication, reviewer follow-up, and Canvas submission remain external steps.

## Use with Overleaf

Import the repository or this ZIP into Overleaf, select main.tex, choose pdfLaTeX, and compile twice if references are initially unresolved. Before submission, confirm personal links and add the final commit hash. See GITHUB_OVERLEAF_GUIDE_CN.md.

## Reuse and attribution

Student-authored code under companion/src, companion/tests, and companion/hf_space, plus the notebook and saved output, is released under the MIT License in LICENSE_CODE.txt. The course template, ACM class/style files, cited scholarship, and photographs retain their own authorship and terms.
