# Reproducible v2 experiment

The standard-library model retains the v1 learning rules and adds C's reward for A's later cooperation. See the root README and AUTHOR_RESPONSE.md for scope and reviewer contributions.

Run from repository root:

```bash
python3 scripts/run_revision_checks.py
python3 -m unittest discover -s companion/tests -v
python3 scripts/check_v1_equivalence.py
```

The full grid writes 750 per-seed results plus summaries to outputs/ps1_revision_panel.json. The default exploration panel is outputs/ps1_condition_panel.json. Both use strict JSON, with null for inapplicable report measures.

The notebook is self-contained in Colab. To regenerate its executed outputs locally:

```bash
python3 -m pip install -r companion/requirements.txt
python3 scripts/build_notebook.py
```

The game is a static educational demonstration, with unseeded browser randomness. Its automatic mode uses the same model rules, but Python and JavaScript do not share random-number streams. The player mode preserves its original 0.15/0.80 action-learning settings. It does not collect participant data.
