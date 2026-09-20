# PS1 v2 — Author response

Author: Qingyue Liu  
Proposal: When Honest Reports Fail to Sustain Cooperation  
Reviewers: Yichen Shen and Zhengjun He  
Revision date: September 20, 2026

## What I retain and why

I retain the central question: how do third-party reports of uncertain truthfulness affect cooperation among learning agents in a repeated Prisoner's Dilemma? Both reviewers recognized the distinction between honesty or credibility and socially useful cooperation. I preserve that distinction, the A–B payoff matrix, fixed matching, and the original learning rules. The revision adds one focused reporting incentive rather than treating all suggested extensions as required changes. The original v1 ZIP/PDF and supplied reviews are preserved in archive/v1/ and reviews/original/.

## Related-work positioning

Leung et al. (2026) are the related-work baseline for RL agents using minimal third-party observation and partner selection to support cooperation. This revision does not reproduce their population or interaction-network model. It keeps A–B matching, payoffs, and learning settings fixed, defers partner selection, and changes only C's reporting incentive by adding a bonus after A cooperates. I therefore describe the contribution as a controlled incentive extension that tests whether C's private reward improves report usefulness, A–B cooperation, and A+B welfare.

## Response to Yichen Shen

Yichen's main question was why accurate reports would change a decision when defection remains dominant. I adopted this clarification in Sections 2 and 4 and Appendix A. If p denotes B's cooperation probability, A earns 3p from cooperation and 1+3p from defection in the stage game. A more accurate signal can change p without changing that one-point payoff gap. I now distinguish this stage-game statement from claims about repeated-game strategies or the convergence of the learning algorithm. Honest reporting of B's past action is also separated from correctly predicting B's subsequent action.

I defer Yichen's proposed controlled comparison with and without partner selection. Choosing a partner would change the available actions and add a mechanism beyond the present observer-incentive question. Keeping matching fixed allows a cleaner test of the reporting incentive. Partner selection remains explicit future work; the new experiment is not presented as implementing his deferred suggestion. This decision preserves the project's direction while responding to the economic concern behind the suggestion.

## Response to Zhengjun He

I adopted Zhengjun's concrete proposal that C's payoff depend on A's later cooperation. In the new market-linked condition, C receives the original honesty reward of 0.4 or lying penalty of 0.2, plus beta=1 when A subsequently cooperates. The strategic baseline sets beta=0. The update occurs after A acts. A/B payoffs, pairing, rounds, and learning parameters are held fixed within each matched comparison.

This also addresses Zhengjun's question about rewards for C and the market. I report C's reporting reward separately from A's cooperation, mutual cooperation, and A+B welfare. The bonus is externally supplied and is not deducted from A; its funding cost is outside the model. Rewarding A's cooperation can expose A to defection and therefore does not guarantee social benefit. Designing a mechanism that guarantees private/social alignment is deferred; I do not claim the proposed bonus solves that problem.

## Evidence and checks

The full grid contains 750 synthetic runs: five conditions, five exploration rates, 30 seeds, and 10,000 rounds per run. At the default 12% exploration rate, strategic versus market-linked honesty is 93.98% versus 93.46%; mutual cooperation is 2.75% versus 2.66%; C's reporting reward is 0.364 versus 0.458. The paired cooperation difference is -0.082 percentage points, with approximate 95% interval [-0.652, 0.489]. A+B welfare changes by -0.0040 with interval [-0.0296, 0.0215]. Thus C benefits without clear evidence of improved cooperation or welfare.

Low exploration changes the picture: at 2%, strategic cooperation averages 21.99% over the full run but 2.88% in the final 20%. I narrowed the conclusion accordingly. The verified benchmark forces both truth and report use, so I also clarified that it is not a pure credibility comparison.

Changes are traceable in REVISION_LOG.md. The notebook, per-seed outputs, unit checks, and browser checks are documented in validation/CHECKS.md. Appendix D contains this response's decisions, and the cumulative reflection and Appendix E explain their intellectual consequences. ARTIFACT_LINKS.md records artifacts and commit identifiers. No v2 PDF was generated at my request; final Overleaf layout review remains pending. Reviewer follow-up has not been supplied, and I do not imply reviewer approval.

AI-use dates and purposes are disclosed in Appendix A. The original reviews remain the reviewers' own words.
