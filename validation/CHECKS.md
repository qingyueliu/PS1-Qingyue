# PS1 v2 checks — September 20, 2026

## Completed research computation

- python3 scripts/run_revision_checks.py: 750 runs completed (5 conditions x 5 exploration rates x 30 seeds), 10,000 rounds each; seed-level output saved.
- python3 -m unittest discover -s companion/tests -v: 10 tests passed.
- Main result: bonus minus strategic cooperation -0.0817 percentage points, approximate 95% interval [-0.6521, 0.4888]; honesty -0.5254 points; welfare -0.0040.
- JSON uses null for unavailable report metrics, not nonstandard NaN literals.
- scripts/build_notebook.py writes a valid nbformat 4 JSON notebook; python3 -m json.tool passed. The model panel was rerun before embedding its complete text output.
- V1 source/PDF copies match their original SHA-256 hashes.
- Tested content commit: e85f75ac3c6bb1ce65e74f7cb01244db0a2a8478.

## Remaining checks during packaging

V1 trajectory equivalence, notebook JSON, game controls, source consistency, archive integrity, and remote publication are recorded here after execution. The notebook was not executed top-to-bottom in this environment because its optional nbclient runtime was unavailable; the underlying 750-run model and all command-line checks were executed. Successful local tests do not imply that a remote upload or Canvas submission has happened.

## Explicitly not performed

- V2 PDF generation or PDF layout verification, per the author's request.
- Hosted Google Colab execution (local clean-kernel execution is recorded separately).
- Reviewer follow-up or reviewer acceptance (not supplied).
- Canvas submission.
