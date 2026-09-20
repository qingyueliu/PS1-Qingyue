# Executed v2 synthetic results

750 runs: 5 conditions x 5 exploration rates x 30 seeds; 10,000 rounds each.

SD is across-seed population dispersion. Cooperation = mutual A/B cooperation; accuracy predicts B's later focal action.

| epsilon | condition | mutual coop % | SD (pp) | A coop % | honesty % | predictive accuracy % | A+B welfare | C report reward | last 20% coop % |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.02 | none | 45.162 | 37.893 | 47.561 | n/a | n/a | 3.905 | n/a | 32.022 |
| 0.02 | strategic | 21.985 | 16.921 | 25.085 | 98.998 | 96.270 | 2.978 | 0.394 | 2.875 |
| 0.02 | verified | 14.837 | 9.813 | 18.608 | 100.000 | 97.379 | 2.726 | 0.400 | 0.013 |
| 0.02 | market_linked | 22.187 | 17.058 | 25.290 | 97.987 | 95.551 | 2.986 | 0.641 | 2.947 |
| 0.02 | high_lie_cost | 21.985 | 16.921 | 25.085 | 98.998 | 96.270 | 2.978 | 0.386 | 2.875 |
| 0.05 | none | 20.331 | 30.264 | 24.139 | n/a | n/a | 2.962 | n/a | 15.377 |
| 0.05 | strategic | 7.640 | 6.387 | 12.267 | 97.505 | 92.140 | 2.463 | 0.385 | 0.062 |
| 0.05 | verified | 4.962 | 3.393 | 8.955 | 100.000 | 94.536 | 2.357 | 0.400 | 0.078 |
| 0.05 | market_linked | 6.585 | 5.009 | 11.251 | 96.743 | 91.678 | 2.419 | 0.493 | 0.063 |
| 0.05 | high_lie_cost | 7.640 | 6.387 | 12.267 | 97.505 | 92.140 | 2.463 | 0.365 | 0.062 |
| 0.12 | none | 3.294 | 3.736 | 9.573 | n/a | n/a | 2.384 | n/a | 0.477 |
| 0.12 | strategic | 2.745 | 1.624 | 9.882 | 93.985 | 83.727 | 2.376 | 0.364 | 0.337 |
| 0.12 | verified | 2.386 | 1.828 | 9.052 | 100.000 | 88.289 | 2.358 | 0.400 | 0.345 |
| 0.12 | market_linked | 2.663 | 2.173 | 9.782 | 93.459 | 83.398 | 2.372 | 0.458 | 0.340 |
| 0.12 | high_lie_cost | 2.745 | 1.624 | 9.882 | 93.985 | 83.727 | 2.376 | 0.316 | 0.337 |
| 0.25 | none | 2.613 | 0.593 | 14.253 | n/a | n/a | 2.569 | n/a | 2.080 |
| 0.25 | strategic | 2.370 | 0.501 | 14.180 | 87.440 | 70.639 | 2.562 | 0.325 | 1.770 |
| 0.25 | verified | 2.401 | 0.621 | 14.271 | 100.000 | 77.608 | 2.567 | 0.400 | 1.710 |
| 0.25 | market_linked | 2.376 | 0.498 | 14.191 | 87.277 | 70.532 | 2.563 | 0.465 | 1.770 |
| 0.25 | high_lie_cost | 2.370 | 0.501 | 14.180 | 87.440 | 70.639 | 2.562 | 0.224 | 1.770 |
| 0.40 | none | 4.836 | 0.375 | 21.524 | n/a | n/a | 2.859 | n/a | 4.528 |
| 0.40 | strategic | 4.619 | 0.334 | 21.435 | 80.080 | 60.569 | 2.853 | 0.280 | 4.260 |
| 0.40 | verified | 4.644 | 0.290 | 21.329 | 100.000 | 67.319 | 2.852 | 0.400 | 4.495 |
| 0.40 | market_linked | 4.635 | 0.348 | 21.456 | 79.975 | 60.524 | 2.854 | 0.494 | 4.260 |
| 0.40 | high_lie_cost | 4.619 | 0.334 | 21.435 | 80.080 | 60.569 | 2.853 | 0.121 | 4.260 |

## Main paired contrast (market-linked minus strategic, epsilon=0.12)

- cooperation_pct: -0.0817; approximate 95% interval [-0.6521, 0.4888].
- honesty_pct: -0.5254; approximate 95% interval [-0.7552, -0.2955].
- a_cooperation_pct: -0.1000; approximate 95% interval [-0.7402, 0.5402].
- welfare: -0.0040; approximate 95% interval [-0.0296, 0.0215].
- reporter_reward: 0.0946; approximate 95% interval [0.0855, 0.1036].
