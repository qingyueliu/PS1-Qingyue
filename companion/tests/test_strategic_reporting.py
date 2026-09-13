import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from strategic_reporting import COOPERATE, DEFECT, Config, payoff, run_once, run_panel


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
            ["none", "strategic", "verified", "high_lie_cost"],
        )

    def test_verified_reports_are_truthful_and_used(self):
        result = run_once(Config(rounds=500, condition="verified"), seed=206)
        self.assertEqual(result["honesty_pct"], 100.0)
        self.assertEqual(result["reports_used_pct"], 100.0)

    def test_higher_lie_cost_does_not_change_fixed_exploration_path(self):
        strategic = run_once(Config(rounds=500, condition="strategic"), seed=206)
        higher_cost = run_once(Config(rounds=500, condition="high_lie_cost"), seed=206)
        self.assertEqual(strategic, higher_cost)


if __name__ == "__main__":
    unittest.main()
