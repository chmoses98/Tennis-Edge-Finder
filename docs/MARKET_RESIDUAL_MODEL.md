# Market-residual model (MODEL 5)

## The question, posed so the null is honest

Not "who wins", which the market already prices well, but: **when is the market's own error
predictable?** The formulation makes the market the baseline by construction:

```
logit p = logit(p_market) + X · beta
```

The price enters as an OFFSET, not as a feature. A coefficient vector of zero reproduces the market
exactly, so the fit can only discover information the price did not already contain. Any improvement has
to be earned against the market rather than against a strawman.

## Discipline

* **Strict chronology.** Trained on seasons before 2024, tested on 2024 onward. The test set is never
  touched during fitting or feature selection.
* **Strong L2.** The point is to find a robust signal, not the best in-sample fit.
* **The number of features tried is reported.** Eleven, which is the context any single coefficient has
  to be read in.
* **A transparent fitter.** Newton steps on a penalised offset logistic, about twenty lines. No black-box
  search that can be mined for a lucky pocket.

## Features tried

Gen-2 disagreement with the market, Elo disagreement, absolute Gen-2 disagreement, favourite extremity,
log serve evidence for the thinner player, clay / grass / Grand Slam / Masters indicators, best-of-five,
and the spread between the two model lanes.

## Result: no signal survives

| forecaster | Brier | log loss | ECE | calibration slope |
|---|---|---|---|---|
| market, de-vigged Pinnacle | 0.20302 | 0.58989 | 0.0150 | 1.054 |
| market + residual model | 0.20316 | 0.59022 | 0.0132 | 1.054 |

Paired Brier difference **+0.00014**, 95% CI [-0.00040, +0.00067], P(better than market) **0.31**.

The interval straddles zero and the point estimate has the wrong sign. The largest standardised
coefficient (Gen-2 disagreement, +0.062) is small, and its near-mirror (Elo disagreement, -0.049) points
the other way, which is what a diffuse non-signal looks like rather than a mechanism.

**Rejected**, recorded as R-001 in the graveyard. Retesting is justified only with materially different
features, above all order-book microstructure: depth imbalance, quote age and trade pressure, none of
which this archive is long enough to supply.

## What this does NOT show

It does not show the market is unbeatable. It shows that these eleven pieces of pre-match context add
nothing to a Pinnacle closing-style price on ATP singles. A different family, a different venue, a
different horizon or in-play information could all behave differently, and none of them was tested here.
