"""Deterministic baseline for strategic third-party reports in a repeated PD.

This is a Python reconstruction of the Week 2 browser demonstration.  It uses
only the standard library so it can run in a fresh Google Colab CPU session.
"""

from __future__ import annotations

from dataclasses import dataclass
import random
from statistics import mean, pstdev


COOPERATE = 0
DEFECT = 1


@dataclass(frozen=True)
class Config:
    rounds: int = 10_000
    epsilon: float = 0.12
    alpha: float = 0.12
    gamma: float = 0.85
    report_alpha: float = 0.15
    report_gamma: float = 0.80
    honesty_reward: float = 0.40
    lying_cost: float = 0.20
    cooperation_bonus: float = 1.0
    condition: str = "strategic"  # none, strategic, verified, market_linked, high_lie_cost


LEVELS = (0.02, 0.05, 0.12, 0.25, 0.40)
CONDITIONS = ("none", "strategic", "verified", "market_linked", "high_lie_cost")


def reporting_reward(config: Config, truthful: bool, a_action: int) -> float:
    """Zhengjun He's suggested link: reward C after observing A's action.

    This external bonus is not deducted from A and is not part of A+B welfare.
    C's exposure-stage payoff trains its separate action table, as in v1.
    """
    cost = 1.0 if config.condition == "high_lie_cost" else config.lying_cost
    intrinsic = config.honesty_reward if truthful else -cost
    bonus = config.cooperation_bonus if config.condition == "market_linked" and a_action == COOPERATE else 0.0
    return intrinsic + bonus


def payoff(a: int, b: int) -> tuple[int, int]:
    if a == COOPERATE and b == COOPERATE:
        return 3, 3
    if a == COOPERATE and b == DEFECT:
        return 0, 4
    if a == DEFECT and b == COOPERATE:
        return 4, 0
    return 1, 1


def choose_q(q: list[float], epsilon: float, rng: random.Random) -> int:
    if rng.random() < epsilon:
        return rng.randrange(len(q))
    best = max(q)
    return q.index(best)


def update_q(q: list[float], index: int, reward: float, alpha: float, gamma: float) -> None:
    q[index] += alpha * (reward + gamma * max(q) - q[index])


def run_once(config: Config, seed: int) -> dict[str, float]:
    if config.condition not in CONDITIONS:
        raise ValueError(f"unknown condition: {config.condition}")
    if config.rounds < 1 or not 0 <= config.epsilon <= 1:
        raise ValueError("rounds must be positive and epsilon must be in [0, 1]")
    rng = random.Random(seed)
    q_a_action = [[0.0, 0.0] for _ in range(3)]  # no signal, reported C, reported D
    q_a_trust = [0.0, 0.0]
    q_b = [0.0, 0.0]
    q_c_action = [0.0, 0.0]
    q_report = [0.0, 0.0]  # truth, lie
    mutual = honest = reports = trusted = exploit = welfare = score_a = score_b = 0
    a_coop = accurate = late_mutual = 0
    reporter_score = bonus_score = 0.0
    late_start = config.rounds * 4 // 5

    has_reports = config.condition != "none"

    for t in range(config.rounds):
        report = None
        if t > 0:
            c_prior_i = choose_q(q_c_action, config.epsilon, rng)
            b_prior_i = choose_q(q_b, config.epsilon, rng)
            c_gain, b_gain = payoff(c_prior_i, b_prior_i)
            update_q(q_c_action, c_prior_i, c_gain, config.alpha, config.gamma)
            update_q(q_b, b_prior_i, b_gain, config.alpha, config.gamma)

            if has_reports:
                reports += 1
                if config.condition == "verified":
                    truthful = True
                    claim = b_prior_i
                else:
                    report_i = choose_q(q_report, config.epsilon, rng)
                    truthful = report_i == 0
                    claim = b_prior_i if truthful else 1 - b_prior_i
                honest += int(truthful)
                report = claim

        if report is None:
            trust_i = 0
            uses_report = False
        elif config.condition == "verified":
            trust_i = 1
            uses_report = True
        else:
            trust_i = choose_q(q_a_trust, config.epsilon, rng)
            uses_report = trust_i == 1
        trusted += int(uses_report)

        signal = (report + 1) if uses_report else 0
        a_i = choose_q(q_a_action[signal], config.epsilon, rng)
        b_i = choose_q(q_b, config.epsilon, rng)
        gain_a, gain_b = payoff(a_i, b_i)
        update_q(q_a_action[signal], a_i, gain_a, config.alpha, config.gamma)
        if report is not None and config.condition != "verified":
            update_q(q_a_trust, trust_i, gain_a, config.alpha, config.gamma)
        update_q(q_b, b_i, gain_b, config.alpha, config.gamma)

        if report is not None:
            accurate += int(report == b_i)
            reward = reporting_reward(config, truthful, a_i)
            reporter_score += reward
            bonus_score += config.cooperation_bonus if config.condition == "market_linked" and a_i == COOPERATE else 0.0
            if config.condition != "verified":
                # Defer the update until A acts; beta=0 preserves the v1 trajectory.
                update_q(q_report, report_i, reward, config.report_alpha, config.report_gamma)

        score_a += gain_a
        score_b += gain_b
        welfare += gain_a + gain_b
        mutual += int(a_i == COOPERATE and b_i == COOPERATE)
        a_coop += int(a_i == COOPERATE)
        late_mutual += int(t >= late_start and a_i == COOPERATE and b_i == COOPERATE)
        exploit += int(a_i != b_i)

    return {
        "cooperation_pct": 100 * mutual / config.rounds,
        "honesty_pct": 100 * honest / reports if reports else float("nan"),
        "reports_used_pct": 100 * trusted / reports if reports else float("nan"),
        "exploit_pct": 100 * exploit / config.rounds,
        "welfare": welfare / config.rounds,
        "payoff_a": score_a / config.rounds,
        "payoff_b": score_b / config.rounds,
        "a_cooperation_pct": 100 * a_coop / config.rounds,
        "prediction_accuracy_pct": 100 * accurate / reports if reports else float("nan"),
        "reporter_reward": reporter_score / reports if reports else float("nan"),
        "bonus_per_report": bonus_score / reports if reports else float("nan"),
        "late_cooperation_pct": 100 * late_mutual / (config.rounds - late_start),
    }


def run_panel(rounds: int = 10_000, seeds: range = range(30), epsilon: float = 0.12) -> list[dict[str, float | str]]:
    rows: list[dict[str, float | str]] = []
    for condition in CONDITIONS:
        results = [run_once(Config(rounds=rounds, condition=condition, epsilon=epsilon), seed) for seed in seeds]
        row: dict[str, float | str] = {"condition": condition}
        for metric in ("cooperation_pct", "honesty_pct", "reports_used_pct", "exploit_pct", "welfare"):
            values = [float(result[metric]) for result in results]
            values = [value for value in values if value == value]
            row[metric] = mean(values) if values else float("nan")
            row[f"{metric}_sd"] = pstdev(values) if values else float("nan")
        rows.append(row)
    return rows


def format_panel(rows: list[dict[str, float | str]]) -> str:
    header = "condition          coop%   honest%   used%   exploit%   welfare"
    lines = [header]
    for row in rows:
        def cell(key: str) -> str:
            value = float(row[key])
            return "   n/a" if value != value else f"{value:7.2f}"
        lines.append(
            f"{str(row['condition']):<18}{cell('cooperation_pct')}"
            f"{cell('honesty_pct')}{cell('reports_used_pct')}"
            f"{cell('exploit_pct')}{cell('welfare')}"
        )
    return "\n".join(lines)


if __name__ == "__main__":
    print(format_panel(run_panel()))
