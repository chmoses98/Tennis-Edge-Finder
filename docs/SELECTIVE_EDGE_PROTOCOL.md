# Selective edge protocol

How this system is allowed to decide that it disagrees with Kalshi, and what it must do before saying so
out loud.

## The objective

Not "beat Kalshi on average" -- we do not, and Wave 3 measured how badly. The objective is to find the few
occasions where the price is wrong enough to matter, and to refuse the rest. **PASS is the expected
output.** A board that returns 147 PASS, 20 WATCH and 7 SHADOW BET out of 174 contracts is the system
working.

## The three decisions

| decision | meaning |
|---|---|
| PASS | not qualified, or no positive edge after fees. Nothing to look at. |
| WATCH | qualified and positive after fees, but at least one gate says no. Interesting, not actionable. |
| SHADOW_BET | survived every check this system knows how to run. **Not a wager and not an edge claim.** |

## selector_v1

An ordered set of gates, not a score with tuned weights -- and that is a finding, not a preference. Wave 3
fitted a logistic selector on proper-score superiority and a second on realised economics. Neither survived
its holdout. What replicated was a single abstention, so the gates carry the decision and the fitted score
rides along as information.

Gates, all of which must pass for SHADOW_BET:

1. `qualified` -- every `qualify_v1` filter
2. `positive_after_fees` -- fee-adjusted edge > 0 at the executable ask
3. `edge_is_plausible` -- fee-adjusted edge <= 15c. An upper bound, and the most important gate here.
4. `robust_to_reparameterisation` -- positive under EVERY configuration in the defensible set
5. `fair_price_is_pinned` -- the perturbation envelope is <= 15c wide
6. `data_quality_ok` -- >= 0.60
7. `level_not_abstained` -- not ITF

Thresholds were fixed on the discovery and validation blocks (2026-08-25..2026-09-06) and frozen before the
holdout was read. **Changing one is a new selector version, not an edit to this one.**

## Chronology

Eighteen days of settled Kalshi markets, cut into three consecutive blocks, each used for exactly one thing:

| block | dates | rows | used for |
|---|---|---|---|
| discovery | 2026-08-25 .. 09-02 | 2,112 | fitting. Nothing else. |
| validation | 2026-09-03 .. 09-06 | 990 | regularisation and thresholds. Never re-fitting. |
| holdout | 2026-09-07 .. 09-11 | 1,382 | read once, at the end. |

Enforced in code: `Selector.fit` raises if handed a row outside its declared window, and raises again if
the selector has been frozen. A frozen selector can be read, applied and compared; it cannot be re-fitted
to make a holdout look better.

A rule earns its holdout read by surviving validation. `R1_moderate_nonitf_evenmoney` earned one and failed
it, and the failure is the most useful number the wave produced.

## Walk-forward, not end-state

Ratings come from `data/processed/asof/`, which records every player's state after each match from a base
date. A market on day D is scored with the last checkpoint STRICTLY BEFORE D -- not before the timestamp,
before the DATE, so a player who plays twice in a day contributes neither match to a prediction made that
day. Market movement features are built only from candles that closed at or before the same cutoff as the
quote, and a test asserts that appending post-cutoff candles changes no feature.

## The four edges, and why the biggest one is the least trustworthy

See `docs/OPPORTUNITY_SCHEMA.md`. The operational point: on the discovery and validation blocks, claimed
edges above 15c realised **-3.7c** per contract, the worst band on the board, while the 3c-15c band realised
+1.1c. Against a two-sided market whose mid beats ours globally, a claimed 25c edge is far more likely to be
our error than theirs. (Honesty about the evidence: that band came back +0.6c on the holdout, so the cap
rests on the prior rather than on a replicated measurement.)

## What a SHADOW_BET is not

It is not a recommendation, not sized, and not evidence that the market is wrong. Wave 3 found **no subset
in which our probability was more accurate than the Kalshi price** -- including the subsets that returned a
profit. A positive realised return on a small sample of underdogs is what variance looks like. Every
SHADOW_BET row carries that sentence in its `reason_against`, in the object and on the board.

## REAL-MONEY AUTHORITY: OFF

There is no code path, flag, enum member or configuration in this system that expresses a real wager, and
no result in Wave 3 argues for adding one.
