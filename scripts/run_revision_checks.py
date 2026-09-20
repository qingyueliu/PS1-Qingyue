"""Run the declared v2 panel and save every seed, not selected runs.

No external data. Main comparison is market_linked minus strategic at beta=1.
The five epsilon values are a sensitivity grid, not five intelligence levels.
"""
from dataclasses import asdict
import json
import math
from pathlib import Path
from statistics import mean, pstdev, stdev
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "companion/src"))
from strategic_reporting import Config, CONDITIONS, LEVELS, run_once


def summarize(records):
    rows = []
    for epsilon in LEVELS:
        for condition in CONDITIONS:
            sample = [r for r in records if r["epsilon"] == epsilon and r["condition"] == condition]
            row = {"epsilon": epsilon, "condition": condition, "n": len(sample)}
            for metric in sample[0]["metrics"]:
                values = [r["metrics"][metric] for r in sample if r["metrics"][metric] is not None]
                row[metric] = mean(values) if values else None
                row[metric + "_sd"] = pstdev(values) if values else None
            rows.append(row)
    return rows


def main():
    records = []
    for epsilon in LEVELS:
        for condition in CONDITIONS:
            for seed in range(30):
                result = run_once(Config(condition=condition, epsilon=epsilon), seed)
                records.append({"epsilon": epsilon, "condition": condition, "seed": seed,
                    "metrics": {k: v if math.isfinite(v) else None for k, v in result.items()}})
    summary = summarize(records)
    contrasts = []
    for epsilon in LEVELS:
        pair = {c: [r for r in records if r["epsilon"] == epsilon and r["condition"] == c] for c in ("strategic", "market_linked")}
        for metric in ("cooperation_pct", "honesty_pct", "a_cooperation_pct", "welfare", "reporter_reward"):
            diffs = [b["metrics"][metric] - a["metrics"][metric] for a, b in zip(pair["strategic"], pair["market_linked"])]
            error = 1.96 * stdev(diffs) / math.sqrt(len(diffs))
            contrasts.append({"epsilon": epsilon, "metric": metric, "mean_difference": mean(diffs), "approx_95_ci": [mean(diffs)-error, mean(diffs)+error]})
    payload = {"version": "v2", "default_config": asdict(Config()), "seeds": list(range(30)),
        "levels": list(LEVELS), "conditions": list(CONDITIONS),
        "design": "Fixed matching; same A/B payoffs and learning parameters. Only market_linked adds beta=1 after A cooperates. Verified forces truth AND report use; high_lie_cost retained as v1 diagnostic.",
        "interval": "Paired by seed; mean +/- 1.96 * sample SD(difference)/sqrt(30). Approximate, descriptive; no multiplicity correction. Same seed does not guarantee identical RNG draws across unlike treatments.",
        "summary": summary, "paired_contrasts": contrasts, "runs": records}
    out = ROOT / "companion/outputs"
    (out / "ps1_revision_panel.json").write_text(json.dumps(payload, indent=2, allow_nan=False)+"\n")
    main_rows = [r for r in summary if r["epsilon"] == 0.12]
    (out / "ps1_condition_panel.json").write_text(json.dumps({"version": "v2", "rounds": 10000, "seeds": list(range(30)), "epsilon": 0.12, "results": main_rows}, indent=2, allow_nan=False)+"\n")
    lines = ["# Executed v2 synthetic results", "", "750 runs: 5 conditions x 5 exploration rates x 30 seeds; 10,000 rounds each.", "", "SD is across-seed population dispersion. Cooperation = mutual A/B cooperation; accuracy predicts B's later focal action.", "", "| epsilon | condition | mutual coop % | SD (pp) | A coop % | honesty % | predictive accuracy % | A+B welfare | C report reward | last 20% coop % |", "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for r in summary:
        vals = [r[k] for k in ("cooperation_pct", "cooperation_pct_sd", "a_cooperation_pct", "honesty_pct", "prediction_accuracy_pct", "welfare", "reporter_reward", "late_cooperation_pct")]
        lines.append(f"| {r['epsilon']:.2f} | {r['condition']} | " + " | ".join("n/a" if x is None else f"{x:.3f}" for x in vals) + " |")
    lines += ["", "## Main paired contrast (market-linked minus strategic, epsilon=0.12)", ""]
    for r in contrasts:
        if r["epsilon"] == .12:
            lines.append(f"- {r['metric']}: {r['mean_difference']:.4f}; approximate 95% interval [{r['approx_95_ci'][0]:.4f}, {r['approx_95_ci'][1]:.4f}].")
    (out / "revision_results.md").write_text("\n".join(lines)+"\n")
    print("\n".join(lines[-8:]))
    print("Saved 750 seed-level runs, summaries and paired contrasts.")


if __name__ == "__main__":
    main()
