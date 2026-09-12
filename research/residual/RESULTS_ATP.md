# Market-residual model (ATP)

Trained on seasons before 2024 (8142 matches), tested on 2024 onward (4804 matches). The market price is an OFFSET, so a coefficient vector of zero reproduces the market exactly and the only thing the fit can find is information the price did not already contain. 11 features were tried; that count matters when reading any single coefficient.

| forecaster | brier | log loss | ECE | cal slope |
|---|---|---|---|---|
| market (de-vigged Pinnacle) | 0.20302 | 0.58989 | 0.0150 | 1.054 |
| market + residual model | 0.20316 | 0.59022 | 0.0132 | 1.054 |

Paired Brier difference (model minus market): **+0.00014**, 95% CI [-0.00040, +0.00067], P(better) 0.31.

| feature | coefficient (standardised) |
|---|---|
| disagree_gen2 | +0.06186 |
| disagree_elo | -0.04876 |
| is_clay | +0.04859 |
| is_masters | -0.03714 |
| abs_disagree_gen2 | +0.02467 |
| is_slam | +0.01994 |
| bo5 | +0.01994 |
| model_spread | -0.01496 |
| is_grass | -0.00711 |
| fav_centered | +0.00562 |
| log_evidence | -0.00415 |
