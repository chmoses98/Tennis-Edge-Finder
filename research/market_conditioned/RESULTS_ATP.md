# Market-conditioned derivative pricing (ATP)

12946 matches with a de-vigged Pinnacle price, a Gen-2 structural state and a final score.

Lower is better for every metric.

| metric | fundamental | market-conditioned | elo-conditioned |
|---|---|---|---|
| brier_over_21_5 | 0.20114 | 0.20023 | 0.20045 |
| logloss_over_21_5 | 0.56187 | 0.56029 | 0.56126 |
| abs_err_total_games | 5.91364 | 5.90298 | 5.95173 |
| sq_err_total_games | 48.30173 | 47.91897 | 49.20693 |
| brier_sets_played | 0.18896 | 0.18832 | 0.18850 |
| logloss_sets_played | 0.53015 | 0.52887 | 0.52921 |
| logloss_exact_score | 1.35038 | 1.32710 | 1.37007 |
| abs_err_game_diff | 4.10248 | 4.00667 | 4.17372 |

## Paired bootstrap, market-conditioned minus fundamental (negative favours conditioning)

| metric | diff | 95% CI | P(better) | n |
|---|---|---|---|---|
| brier_over_21_5 | -0.00090 | [-0.00152, -0.00029] | 1.00 | 12946 |
| logloss_over_21_5 | -0.00157 | [-0.00300, -0.00011] | 0.98 | 12946 |
| abs_err_total_games | -0.01066 | [-0.02553, +0.00390] | 0.93 | 12946 |
| sq_err_total_games | -0.38276 | [-0.62567, -0.13042] | 1.00 | 12946 |
| brier_sets_played | -0.00064 | [-0.00112, -0.00012] | 0.99 | 12946 |
| logloss_sets_played | -0.00128 | [-0.00231, -0.00023] | 0.99 | 12946 |
| logloss_exact_score | -0.02329 | [-0.02776, -0.01867] | 1.00 | 12946 |
| abs_err_game_diff | -0.09581 | [-0.11491, -0.07675] | 1.00 | 12946 |
