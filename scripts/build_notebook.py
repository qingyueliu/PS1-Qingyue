"""Build the self-contained Colab notebook with saved deterministic output."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
module_source = (ROOT / "companion/src/strategic_reporting.py").read_text(encoding="utf-8")
module_source = module_source.split('\nif __name__ == "__main__":', 1)[0]

saved_output = (
    "condition          coop%   honest%   used%   exploit%   welfare\n"
    "none                 3.29   n/a   n/a  12.60   2.38\n"
    "strategic            2.75  93.98  43.60  13.30   2.38\n"
    "verified             2.39 100.00 100.00  13.14   2.36\n"
    "high_lie_cost        2.75  93.98  43.60  13.30   2.38\n"
)

notebook = {
    "nbformat": 4,
    "nbformat_minor": 5,
    "metadata": {
        "colab": {"name": "strategic_reporting_qlearning.ipynb", "provenance": []},
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3"},
    },
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Strategic third-party reports in a repeated Prisoner's Dilemma\n",
                "\n",
                "**Research question.** When do third-party reports become useful for cooperation rather than merely honest?\n",
                "\n",
                "This self-contained CPU notebook reconstructs the Week 2 browser game's tabular Q-learning rules. It compares no reports, strategic reports, verified reports, and a higher lying cost across 30 fixed seeds. All outputs are synthetic model results; they do not establish human or deployed-AI behavior.\n",
            ],
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Prediction and computational check\n",
                "\n",
                "With payoffs (3,3), (0,4), (4,0), and (1,1), defection improves a player's stage payoff by one against either opposing action. Increasing C's lying cost should therefore raise or preserve honesty but should not by itself overturn A and B's incentive to defect. Verification is expected to change report use more than cooperation unless information affects partner choice, sanctions, or continuation.\n",
            ],
        },
        {
            "cell_type": "code",
            "execution_count": 1,
            "metadata": {},
            "outputs": [],
            "source": [line + "\n" for line in module_source.splitlines()],
        },
        {
            "cell_type": "code",
            "execution_count": 2,
            "metadata": {},
            "outputs": [{"name": "stdout", "output_type": "stream", "text": [saved_output]}],
            "source": ["rows = run_panel(rounds=10_000, seeds=range(30))\n", "print(format_panel(rows))\n"],
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Interpretation and next test\n",
                "\n",
                "Strategic reporting is about 94% honest, yet cooperation remains low. Making reports perfectly verified increases report use to 100% without increasing cooperation. Raising the lying cost from 0.2 to 1.0 leaves the mean unchanged because truth already dominates and the residual lies come from fixed exploration. The next study should add partner selection or an institutional consequence for verified information and rerun the same seeded panel.\n",
            ],
        },
    ],
}

out = ROOT / "companion/notebooks/strategic_reporting_qlearning.ipynb"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(notebook, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
print(out)
