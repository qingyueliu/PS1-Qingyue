# PS1 v2 checks — September 20, 2026

## Completed research computation

- python3 scripts/run_revision_checks.py: 750 runs completed (5 conditions x 5 exploration rates x 30 seeds), 10,000 rounds each; seed-level output saved.
- python3 -m unittest discover -s companion/tests -v: 10 tests passed.
- Main result: bonus minus strategic cooperation -0.0817 percentage points, approximate 95% interval [-0.6521, 0.4888]; honesty -0.5254 points; welfare -0.0040.
- JSON uses null for unavailable report metrics, not nonstandard NaN literals.
- scripts/build_notebook.py writes a valid nbformat 4 JSON notebook; python3 -m json.tool passed. The model panel was rerun before embedding its complete text output.
- V1 source/PDF copies match their original SHA-256 hashes.
- Tested local content commit: e85f75ac3c6bb1ce65e74f7cb01244db0a2a8478.
- Published GitHub source snapshot: 2fc74e11f58f4e041498fb0a3a9bd11201915523; the required paper, code, notebook, reviews, validation, and preserved-v1 paths were verified through the public repository tree.
- Published Hugging Face game commit: 691e7209517683153f690a88d176c30bae97bb2a; the hosted index.html SHA-256 matches the local source, and the live app exposes the market-linked condition and five exploration levels.

## Packaging checks

V1 trajectory equivalence, notebook JSON, game controls, source consistency, archive integrity, GitHub publication, and Hugging Face publication are recorded here after execution. The notebook was not executed again in hosted Colab because the code did not change after the completed 750-run model check. This avoids duplicating the same simulation solely for publication. No Canvas submission is implied.

## Explicitly not performed

- V2 PDF generation or PDF layout verification, per the author's request.
- A second hosted Google Colab execution of the unchanged 750-run panel.
- Reviewer follow-up or reviewer acceptance (not supplied).
- Canvas submission.
