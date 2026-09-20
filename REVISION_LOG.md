# V1 → v2 revision record — September 20, 2026

| Source/contribution | Decision and reason | Changed location | Evidence |
|---|---|---|---|
| Leung et al. (2026): RL agents, minimal third-party observation, and partner selection | Use as the related-work baseline; frame v2 as a controlled incentive extension, not a reproduction of their population or interaction-network model | Paper §1; Appendix related-work positioning and Appendix E; author response; README | Fixed A–B matching; partner selection deferred; only C's downstream cooperation bonus changes |
| Yichen Shen: distinguish honesty/cooperation; explain why accurate information changes decisions | Retain distinction; clarify expected stage-payoff gap and repeated-game limitation | Paper §§2,4; Appendix A; notebook assumptions | Both opposing actions give a one-point advantage to stage defection; unit test |
| Yichen Shen: with/without partner selection | Defer: it changes the action space; fixed matching isolates observer incentives | Paper §§2,5; Appendix D; author response | No partner-selection treatment claimed |
| Zhengjun He: A's later cooperation affects C's payoff | Adopt one beta=1 reward condition; baseline beta=0 | Model reporting_reward/run_once; notebook; game | Reward and zero-bonus equivalence tests; 30-seed matched comparison |
| Zhengjun He: reward C and the market | Separate C reward, A cooperation, mutual cooperation, A+B welfare; defer guaranteed alignment | Paper §§2–4; Appendix A; saved per-seed metrics; game | C reward rises; cooperation/welfare difference intervals include zero |
| Both reviewers: strength of credibility/usefulness distinction | Retain and make operational | Paper, author response, cumulative reflection, Appendix E | Honesty, predictive accuracy, use, cooperation measured separately |
| Prof. Luyao Zhang, separately acknowledged methodological guidance | Multiple seeds; vary one reporting incentive; hold other settings fixed | Experimental design and cumulative reflection only, not peer-review response | 750 runs across five exploration rates; not claimed as a Leung-model reproduction |
| Author's earlier game request | Retain five explained exploration levels; use as sensitivity settings | Game controls and notebook | 2%, 5%, 12%, 25%, 40%; not intelligence rankings |

Original reviews are unmodified transcriptions in reviews/original/. V1 bytes and checksums are in archive/v1/. The original editable teaser and vector export are retained and captioned as the baseline; the added condition is explained in the text. No PDF is generated in this revision.

The tested code commit is e85f75ac3c6bb1ce65e74f7cb01244db0a2a8478 and is recorded in revision_metadata.tex and ARTIFACT_LINKS.md. Later documentation commits record metadata, the concise AI-use disclosure, and related-work positioning without changing the tested code. The 750-run grid was therefore not repeated for these text-only edits. Reviewer follow-up remains unreceived.
