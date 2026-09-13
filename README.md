# When Honest Reports Fail to Sustain Cooperation

Qingyue Liu's COMSCI/ECON 206 PS1 proposal studies a repeated Prisoner's Dilemma in which an observer can report a partner's previous action truthfully or falsely. The project asks when a credible report becomes useful for cooperation rather than merely accurate.

This project adapts the official course repository `dku-comsci-econ206-Autumn2026/ps1-overleaf-template`. The paper, editable figure, computational baseline, saved outputs, tests, and browser game are organized within that course structure.

## Research artifacts

- `main.tex`, `sections/proposal.tex`, and `appendices/supporting.tex`: ACM two-column proposal and supporting material.
- `figures/ps1_teaser.drawio`: editable Draw.io master; the PDF and SVG are vector exports of the same design.
- `companion/src/strategic_reporting.py`: deterministic Python reconstruction of the Week 2 browser model.
- `companion/notebooks/strategic_reporting_qlearning.ipynb`: self-contained Google Colab notebook with saved output.
- `companion/outputs/ps1_condition_panel.json`: parameters and means from 30 fixed seeds.
- `companion/hf_space/index.html`: static interactive game for Hugging Face Spaces.
- `GITHUB_OVERLEAF_GUIDE_CN.md`: Chinese setup and submission instructions.

## Reproduce the computational check

Python 3.10 or later is sufficient; the baseline uses only the standard library.

```bash
python companion/src/strategic_reporting.py
python -m unittest discover -s companion/tests -p 'test_strategic_reporting.py'
```

The seeded panel uses 10,000 rounds for each of seeds 0--29. It compares no reports, strategic reports, verified reports, and a higher lying cost. Outputs are synthetic learning-model results, not observations of human participants or deployed AI systems.

To try the educational game locally, open `companion/hf_space/index.html` in a browser. The automatic mode compares no reporting with strategic reporting; the notebook contains the complete four-condition seeded panel. The central claim is deliberately limited: under the specified dominant-defection game and learning rule, honest or verified reports alone do not sustain cooperation. Small differences between condition means are descriptive because the seed-level distributions overlap.

## Rubric readiness

`RUBRIC_AUDIT.md` maps the current artifacts to the instructor's four-part scorecard. The research portfolio is locally complete and rerunnable, but submission readiness still depends on uploading this version to the personal fork, checking Colab from a clean session, and replacing the commit placeholder. Peer reviews must be completed independently under the course's Human-Only rule.

## Use with Overleaf

This project adapts the course repository `dku-comsci-econ206-Autumn2026/ps1-overleaf-template`. Import the repository or its ZIP into Overleaf, select `main.tex`, choose `pdfLaTeX`, and compile twice if references are initially unresolved. Before submission, confirm the personal project links and add the final commit hash. See `GITHUB_OVERLEAF_GUIDE_CN.md` for the full workflow.

## Reuse and attribution

Student-authored code under `companion/src`, `companion/tests`, and `companion/hf_space`, plus the notebook and saved output, is released under the MIT License in `LICENSE_CODE.txt`. The course template, ACM class/style files, cited scholarship, and photographs retain their own authorship and terms; the MIT grant does not cover them.
