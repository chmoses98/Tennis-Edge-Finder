# Selector failure modes

What fooled us, characterised rather than corrected. Nothing in this file was used to change the selector
during the confirmation period; it exists so the next wave knows where to aim.

Measured on the discovery and validation blocks (2026-08-25..2026-09-06), 1,297 opportunities with a
positive fee-adjusted edge. Realised figures are after-fee P&L per contract, one contract at the displayed
ask.

## The headline failure

**Claimed +10.8c. Realised -0.9c.** Averaged over every positive-edge opportunity. The claim and the
outcome are not merely different sizes, they have different signs. Everything below is an attempt to say
where that gap lives.

## F-1. Level: ITF is where the model breaks

| level | n | claimed | realised | 95% CI |
|---|---|---|---|---|
| ITF | 763 | +11.9c | **-3.5c** | [-6.4c, -0.5c] |
| CHALLENGER | 236 | +8.9c | +4.5c | [-1.4c, +10.3c] |
| GRAND_SLAM | 257 | +9.9c | +1.3c | [-4.0c, +6.4c] |
| TOUR_500_250 | 23 | +5.6c | +5.9c | [-14.6c, +25.4c] |

Replicated on the holdout: ITF -4.8c, CI [-9.2c, -0.4c]. Two blocks, both intervals excluding zero.

Why: serve statistics exist for about 4% of ITF matches, so Gen-2 is running almost entirely on
rating-implied point probabilities, and the ratings themselves are built on a thin, high-churn population
where a player's last recorded match may be a year old and at a different level. ITF is also where identity
coverage is worst, so an unknown share of this is mis-mapped players rather than mis-modelled ones -- and
those have different fixes.

## F-2. Size of the claim: the biggest edges are the worst

| claimed edge | n | realised | 95% CI |
|---|---|---|---|
| 0-3c | 258 | -2.5c | [-7.6c, +2.7c] |
| 3-7c | 303 | +1.1c | [-3.8c, +6.1c] |
| 7-15c | 399 | +1.1c | [-3.2c, +5.4c] |
| **15c+** | 337 | **-3.8c** | [-8.2c, +0.8c] |

A claimed 25c edge against a two-sided market that beats us globally is a statement about our model, not
about the price. This did NOT replicate on the holdout (+0.6c there), so the plausibility cap in
selector_v1 rests on the prior and on F-1's mechanism, not on a replicated measurement.

## F-3. Price band: we are least wrong near even money

| ask | n | claimed | realised | 95% CI |
|---|---|---|---|---|
| 0.00-0.20 | 312 | +13.7c | -2.7c | [-5.9c, +0.6c] |
| 0.20-0.40 | 428 | +12.2c | -3.3c | [-7.5c, +0.9c] |
| 0.40-0.60 | 363 | +9.1c | **+5.1c** | [+0.2c, +10.1c] |
| 0.60-0.80 | 146 | +7.2c | -5.9c | [-13.6c, +1.7c] |
| 0.80-1.00 | 48 | +3.6c | +2.3c | [-6.3c, +9.9c] |

The even-money band looks like the one place the model earns its keep, and it is exactly the band that
carried `R1` to a +11.9c discovery result and a **-4.3c holdout**. Treat this row as a warning, not a
finding.

## F-4. Robustness does not separate good from bad

| subset | n | realised |
|---|---|---|
| edge survives every perturbation | 1,022 | -1.1c |
| edge dies under at least one | 275 | -0.2c |
| narrow envelope (<5c) | 636 | +0.9c |
| wide envelope (>=5c) | 661 | -2.7c |

An edge that survives reparameterisation is not thereby a better edge. The envelope WIDTH separates
slightly, in the expected direction, and not significantly. Robustness remains a gate in selector_v1
because refusing to act on a number we cannot pin down is defensible on its own terms -- not because it
predicts returns.

## F-5. Model consensus does not help either

| subset | n | realised |
|---|---|---|
| Gen-2 + Elo + Gen-1 all agree against the price | 1,028 | **-1.6c** |
| Gen-2 + Elo agree, Gen-1 does not | 113 | +2.0c |
| Elo disagrees with Gen-2 | 156 | +1.7c |

Agreement was the worst subset. This is not paradoxical: the three lanes share one rating substrate and are
not independent witnesses. When they agree they are usually agreeing about the same stale rating. A
market-conditioned lane would be worse still -- it is anchored to the very price it would be voting
against -- and is excluded from every consensus count by construction.

## F-6. Market movement: a real separation that did not replicate

| subset | n | realised (disc+val) | holdout |
|---|---|---|---|
| market drifted TOWARD our side in 6h | 500 | **-4.2c**, CI [-8.1c, -0.5c] | -2.2c, CI [-7.9c, +3.6c] |
| market did not | 797 | +1.2c | -1.0c |

The mechanism is attractive -- if the price has already moved our way, the information is in the price and
what remains of our disagreement is our own error -- and the discovery interval excluded zero. The holdout
separation is gone. **Rejected** as a discriminator; the drift is still reported on the board as a reason
against, because it costs nothing to say.

## F-7. Execution eats what is left

Every 1c of worse execution costs 1c of EV, and the whole positive-edge set is negative at the displayed
ask before any slippage:

| worse execution | realised |
|---|---|
| at the ask | -0.9c |
| +1c | -1.9c |
| +2c | -2.9c |
| +3c | -3.9c |

Median headroom between the ask and `bet_up_to` is 8c and only 7.6% of rows are one-tick fragile, so
fragility is not the binding constraint. Being wrong is.

## F-8. Profile of a confident miss

Claimed edge above 5c, 571 losses against 298 wins. The losses are cheaper, thinner and staler:

| | miss | hit |
|---|---|---|
| median ask | 0.26 | 0.45 |
| median serve points (thinner player) | 1,357 | 1,919 |
| median days since last recorded match | 123 | 98 |
| median data quality | 0.65 | 0.77 |
| share ITF | 67% | 52% |
| share WTA | 47% | 36% |

Read with care: cheap bets lose more often by construction, so part of this table is the price band and not
a defect. The evidence, staleness and level columns are the ones that survive that objection, and they all
point at the same place as F-1.

## Categories we could NOT test

Injury and mid-tournament retirement risk, a player returning from a long absence, and liquidity illusion
(displayed size that would vanish on contact) are all plausible failure modes for which this dataset has no
observable. They are named here so their absence from the analysis is visible.
