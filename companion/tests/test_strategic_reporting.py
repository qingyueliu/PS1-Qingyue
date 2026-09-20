import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from strategic_reporting import COOPERATE, DEFECT, Config, payoff, run_once, run_panel, reporting_reward


class StrategicReportingTests(unittest.TestCase):
    def test_payoff_table(self):
        self.assertEqual(payoff(COOPERATE, COOPERATE), (3, 3))
        self.assertEqual(payoff(COOPERATE, DEFECT), (0, 4))
        self.assertEqual(payoff(DEFECT, COOPERATE), (4, 0))
        self.assertEqual(payoff(DEFECT, DEFECT), (1, 1))

    def test_defection_strictly_dominates(self):
        for opponent in (COOPERATE, DEFECT):
            self.assertGreater(payoff(DEFECT, opponent)[0], payoff(COOPERATE, opponent)[0])

    def test_seed_is_repeatable(self):
        config = Config(rounds=500, condition="strategic")
        self.assertEqual(run_once(config, 7), run_once(config, 7))

    def test_panel_has_all_conditions(self):
        rows = run_panel(rounds=100, seeds=range(2))
        self.assertEqual(
            [row["condition"] for row in rows],
            ["none", "strategic", "verified", "market_linked", "high_lie_cost"],
        )

    def test_verified_reports_are_truthful_and_used(self):
        result = run_once(Config(rounds=500, condition="verified"), seed=206)
        self.assertEqual(result["honesty_pct"], 100.0)
        self.assertEqual(result["reports_used_pct"], 100.0)

    def test_higher_lie_cost_does_not_change_fixed_exploration_path(self):
        strategic = run_once(Config(rounds=500, condition="strategic"), seed=206)
        higher_cost = run_once(Config(rounds=500, condition="high_lie_cost"), seed=206)
        for metric in strategic:
            if metric != "reporter_reward":
                self.assertEqual(strategic[metric], higher_cost[metric])

    def test_downstream_bonus_only_depends_on_a_and_treatment(self):
        config = Config(condition="market_linked", cooperation_bonus=1)
        self.assertAlmostEqual(reporting_reward(config, True, COOPERATE), 1.4)
        self.assertAlmostEqual(reporting_reward(config, False, COOPERATE), 0.8)
        self.assertAlmostEqual(reporting_reward(config, True, DEFECT), 0.4)
        self.assertAlmostEqual(reporting_reward(config, False, DEFECT), -0.2)
        self.assertEqual(reporting_reward(Config(), True, COOPERATE), 0.4)

    def test_zero_bonus_is_exact_baseline(self):
        for seed in (0, 7, 206):
            self.assertEqual(run_once(Config(rounds=500), seed), run_once(Config(rounds=500, condition="market_linked", cooperation_bonus=0), seed))

    def test_metric_denominators_and_welfare(self):
        row = run_once(Config(rounds=500, condition="market_linked"), 206)
        self.assertLessEqual(row["cooperation_pct"], row["a_cooperation_pct"])
        self.assertAlmostEqual(row["welfare"], row["payoff_a"] + row["payoff_b"])
        self.assertAlmostEqual(row["reporter_reward"] - row["bonus_per_report"], 0.6 * row["honesty_pct"] / 100 - 0.2)

    def test_round_one_has_no_report(self):
        import math
        row = run_once(Config(rounds=1, condition="market_linked"), 0)
        self.assertTrue(math.isnan(row["honesty_pct"]))
        self.assertTrue(math.isnan(row["reporter_reward"]))


if __name__ == "__main__":
    unittest.main()
