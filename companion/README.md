# Reproducible companion

This folder contains the computational artifacts for Qingyue Liu's PS1 proposal on strategic third-party reports in a repeated Prisoner's Dilemma.

Run the deterministic panel:

```bash
python src/strategic_reporting.py
python -m unittest discover -s tests -p 'test_strategic_reporting.py'
```

The code uses only the Python standard library. The notebook is self-contained for Google Colab. Saved results use seeds 0--29 and 10,000 rounds per condition. The `hf_space` directory contains a static browser demonstration; its unseeded single-run outputs should not be treated as identical to the deterministic Python panel.

All outputs are synthetic learning-model results, not observations of human participants or deployed AI systems.
