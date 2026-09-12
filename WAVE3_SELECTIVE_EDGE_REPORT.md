# Wave 3: selective Kalshi mispricing detector

**2026-09-12. `chmoses98/Tennis-Edge-Finder`. REAL-MONEY AUTHORITY: OFF.**

The question was: can we identify a small subset of Kalshi tennis markets where our disagreement with the
price is more trustworthy than a random disagreement?

## The answer is no, with one exception that is an abstention rather than an edge

1. **No selector beat abstention.** Two were fitted -- one on proper-score superiority, one on realised
   after-fee economics. Both failed their holdout. The first ranked *negatively* on economics at every
   selection rate; the second returned -22% at the top 1% of validation.
2. **The one rule that replicated tells us where NOT to act.** At ITF level our positive-edge
   opportunities realised **-3.5c** per contract on discovery+validation (95% CI [-6.4c, -0.5c]) and
   **-4.8c** on the holdout (CI [-9.2c, -0.4c]). Two blocks, both intervals excluding zero, same sign.
3. **The rule that looked best failed hardest.** `R1` -- moderate edge, non-ITF, near even money, market
   not already drifting our way -- returned +11.9c on discovery and +15.6c on validation, earned its
   holdout read under the pre-registered rule, and delivered **-4.3c**. That number is the most useful
   thing this wave produced.
4. **Claimed edge does not survive contact with settlement.** Across 1,297 positive-edge opportunities the
   average claim was +10.8c and the average realisation was **-0.9c**.
5. **Where a positive return did appear, our accuracy was still worse than the price's.** The non-ITF
   holdout subset returned +10.2% ROI on 220 rows while our Brier on those same rows was 0.2248 against
   the market's 0.2159. That is what variance looks like, not what an edge looks like.

## What was built

| piece | what it does |
|---|---|
| `tennis_edge/opportunity/` | the immutable, hash-chained decision object and twelve hard qualification filters |
| `tennis_edge/models/asof.py` | walk-forward rating artifacts: every player's Elo, serve/return and Gen-2 state after each match, read strictly before the match date |
| `tennis_edge/models/fair.py` | one fair-price layer shared by research and board, plus the 13-configuration defensible perturbation set |
| `tennis_edge/selector/` | features with a leakage check, an L2 logistic selector with a chronology firewall, and selector_v1's decision gates |
| `scripts/ops/shadow_board.py` | the owner-facing board, written to the append-only store before it is rendered |
| `scripts/research/` | the dataset builder and five studies |

Docs: `docs/OPPORTUNITY_SCHEMA.md`, `docs/SELECTIVE_EDGE_PROTOCOL.md`,
`research/SELECTOR_FAILURE_MODES.md`.

## The data layer, and why it is new

The Wave 1 Kalshi backtest scored markets with rating states frozen at the end of the Sackmann forks --
one to four months stale, uniformly. Wave 3 replaced that with **walk-forward** states: a market on day D
is priced from the last checkpoint strictly before D. Two consequences:

* the ESPN results feed fixed in the last hours of Wave 2 carries both tours to **2026-09-11**, so ratings
  inside the evaluation window are days old rather than months;
* freshness becomes a real feature with real variance instead of a constant.

Also discovered while building it: the community TML mirror **does** carry ATP serve statistics through
2026-09-01, and they are concentrated exactly where Kalshi lists markets -- 2,275 Challenger and 381 ITF
matches since June. The serve-data gap is a **WTA** gap, not a tennis gap. That was not known in Wave 2.

Dataset: 2,242 settled match-winner markets (Wave 1 linked 1,869), 4,484 opportunity rows, 2026-08-25 to
2026-09-11, split chronologically into discovery (2,112 rows), validation (990) and holdout (1,382).

## The market we are trying to beat

| ask band | n | market mid | observed | difference |
|---|---|---|---|---|
| 0.05-0.10 | 151 | 0.078 | 0.073 | -0.005 |
| 0.20-0.30 | 322 | 0.246 | 0.236 | -0.010 |
| 0.40-0.50 | 431 | 0.451 | 0.443 | -0.008 |
| 0.60-0.70 | 356 | 0.649 | 0.657 | +0.008 |
| 0.80-0.90 | 271 | 0.850 | 0.867 | +0.017 |

A textbook favourite-longshot tilt of about one cent, consistent in sign across every bucket -- and
smaller than the round-trip cost. Median spread 1c, median taker fee 1.7c. Buying every contract at the
ask returns about **-5%** in every series. There is no model-free edge here, and any strategy that pays
the spread needs to be right by more than two cents before it starts.

## The selector

Target: proper-score superiority -- "was our number closer to the truth than the price was" -- not "who
wins", which we already know we lose. Fitted on discovery, L2 chosen on validation, holdout read once.

Its largest coefficients were `favouriteness` (-0.35) and `n_lanes_agreeing` (-0.29), which is the tell:
the target is dominated by how far the price sits from even money, because near 50/50 both forecasts are
close and the comparison is near-tied. It learned the geometry of the target, not a property of our
disagreement. On the holdout it ranked negatively on economics at 1%, 2%, 5% and 10%.

The economics-target selector, fitted on realised profit, did no better.

## Holdout, read once

| ranker | rate | n | hit | ROI | mean P&L 95% CI |
|---|---|---|---|---|---|
| selector score | 1% | 14 | 0.500 | -7.3% | [-0.32, +0.23] |
| fee-adjusted edge | 1% | 14 | 0.214 | +11.5% | [-0.16, +0.23] |
| robust edge | 1% | 14 | 0.214 | +9.1% | [-0.17, +0.23] |
| selector score | 5% | 69 | 0.493 | -6.5% | [-0.15, +0.08] |
| fee-adjusted edge | 5% | 69 | 0.246 | +21.5% | [-0.05, +0.15] |
| robust edge | 5% | 69 | 0.246 | +24.7% | [-0.04, +0.14] |
| selector score | 10% | 138 | 0.514 | -2.9% | [-0.10, +0.06] |
| fee-adjusted edge | 10% | 138 | 0.275 | +10.9% | [-0.04, +0.10] |
| robust edge | 10% | 138 | 0.239 | -1.0% | [-0.07, +0.07] |

Every interval contains zero. The +24.7% cell is 69 bets at an average ask of 25c; it is exactly the
"23 bets, +18% ROI" object the mandate warns about, and it is reported here as such.

## Selective calibration

Claimed edge against realised edge, holdout:

| claimed | n | claimed mean | realised | 95% CI |
|---|---|---|---|---|
| 0-2c | 68 | +0.8c | -0.2c | [-11.4c, +10.9c] |
| 2-5c | 99 | +3.5c | +2.4c | [-6.1c, +11.0c] |
| 5-10c | 157 | +7.3c | -2.5c | [-10.2c, +4.6c] |
| 10c+ | 265 | +20.5c | -2.7c | [-7.6c, +2.3c] |

Nothing here behaves like a calibrated edge. A claimed 20.5c that realises -2.7c is not a small
mis-calibration, it is a claim with no relationship to the outcome.

## The component questions

* **Robustness (Phase 4).** An edge surviving all 13 configurations realised -1.1c; one that dies under at
  least one realised -0.2c. Robustness does not predict returns. It remains a gate because refusing to act
  on a number we cannot pin down is defensible on its own terms.
* **Consensus (Phase 7).** All three fundamental lanes agreeing was the WORST subset (-1.6c). They share a
  rating substrate and are not independent witnesses; when they agree they are usually agreeing about the
  same stale rating. Market-conditioned lanes are excluded from consensus counts by construction -- a lane
  anchored to the price cannot vote against it.
* **Execution (Phase 8/9).** Median headroom between ask and `bet_up_to` is 8c and only 7.6% of rows are
  one-tick fragile, so fragility is not the binding constraint. Every extra cent of slippage costs exactly
  one cent of EV, and the whole positive-edge set is already negative at the displayed ask.
* **Movement (Phase 10).** Opportunities where the market had already drifted toward our side realised
  -4.2c, CI [-8.1c, -0.5c], on discovery+validation. On the holdout the separation vanished. Rejected as a
  discriminator; still displayed as a reason against, because saying it costs nothing.

## A bug this wave found in its own machinery

`bet_up_to` bisected on the unrounded fee and floored the result. Kalshi rounds the fee UP to the cent, so
at a 30c fair value the function returned 28c, where the real fee makes the trade exactly zero-minus. A
"bet up to" that is not payable is worse than no number. It now searches whole cents against the real fee.

## Identity coverage (Phase 17)

| | value |
|---|---|
| distinct player names on the discovery board | 9,132 |
| mapped, exact full-name match only | 6,105 (66.9%) |
| mapped, plus the guarded compound-surname alias | 6,131 (67.1%) |
| refused as ambiguous | 22 |
| registry, after admitting ESPN | 25,313 ATP / 25,186 WTA players, as-of 2026-09-11 |
| ESPN players crosswalked | 946 MAPPED, 88 no canonical match, 7 ambiguous -- all refusals kept |

The alias rule recovers a surname that GREW: Kalshi's "Nicole Melichar-Martinez" against the registry's
"Nicole Melichar". It fires only when the candidate's leading tokens exactly reproduce exactly one
registry player, that player is recently active, and nothing else is a near neighbour. Matches carry
confidence 0.9, below the 0.95 a shadow bet requires, so they restore board coverage without ever driving
a decision.

**What it deliberately does not do:** Kalshi's "Mimi Xu" is very probably the registry's "Mingge Xu". The
rule will not touch it, because "very probably" is how two different players become one rating entity, and
this project has already had that bug once. The residue is nickname substitutions, doubles specialists
absent from singles history, and genuinely new players -- and it needs a reviewed alias file, not a
smarter matcher.

## Serve-data search (Phase 18)

Bounded, as instructed, and run on a runner because the sandbox has no egress.

| candidate | result |
|---|---|
| ESPN scoreboard | 200, results only, no statistics |
| ESPN match summary | **400** for tennis; the endpoint does not serve tennis matches |
| tennisabstract.com | robots.txt **disallows** `/jsmatches/`, `/jsplayers/`, `/jsfrags/` -- the paths the data lives on. Not usable. |
| api.wtatennis.com | 404 |
| recently-pushed WTA repositories | 6 inspected. Two (`filmo90/tennis_v2_wta`, `saraygarcia/wta-tennis-analytics`) ship Sackmann-shaped WTA CSVs WITH serve columns -- and neither has a file for 2026. The newest are 2015 and 2022. They are copies of the same frozen upstream. |

The finding that matters is the one from the data layer rather than the probe: **ATP serve statistics are
current to 2026-09-01** via the TML Challenger mirror, at exactly the levels Kalshi lists. **WTA serve
statistics still stop at 2026-04-27** and nothing free and permitted was found to close that. TENNIS-14
stays red.

## What would change the answer

Not a better selector. The binding constraints are, in order:

1. **Our probability is simply less accurate than Kalshi's**, on the whole board and on every subset we
   could isolate. Until that changes, selection is choosing among errors.
2. **Eighteen days.** Every interval in this report contains zero, and the two evaluation blocks are
   adjacent rather than independent -- the same players, tournaments and surfaces appear in both.
3. **The WTA serve-data gap**, which is now the only remaining half of the fundamental staleness problem.
4. **No A/B first-ball truth**, so no strict CLV, so the fastest-settling evidence channel is still shut.

**REAL-MONEY AUTHORITY: OFF.** Nothing in this wave argues for changing that, and the one rule that
replicated argues for doing less, not more.
