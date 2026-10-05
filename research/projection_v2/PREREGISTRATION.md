# Projection Engine V2 — preregistered protocol and promotion rules

Written and committed **before any V2 challenger result was computed** (2026-10-05). The commit that adds this
file is the timestamp. Nothing below may be edited after results are seen; a change needs a new, dated file
that says what changed and why, and any evaluation after it is a new research cycle.

## 1. What is being compared

| name | definition |
|---|---|
| **INCUMBENT** | the production rule in `scripts/run_tennis.py` (model_version `elo_surface_k_lo+sr_v0.1`): Elo k0=180 + surface pooling + level K + level prior; Gen-1 serve/return logit-averaged 50/50 with Elo when both players have >= 1000 Gen-1 serve+return points, else Elo alone; best-of-3 basis translated to the match format through the point probabilities. Reproduced bit-for-bit by `tennis_edge/v2/replay.py::INCUMBENT_ELO` + `finalise` (test: `tests/test_v2_engine.py`). |
| INCUMBENT_V1DATA | the same rule replayed on the `canonical_v1` table (the table production builds today, with its cross-source duplicates). Reported to separate the data fix from the model change. |
| FAIR_V1 | `fair_v1` base configuration (Model 3: Gen-2 shrunk toward the incumbent Elo by the thinner player's evidence). Reference only. |
| CHALLENGER | the single V2 specification frozen at step 3 below. |

No market price enters any of these. Market comparisons happen only after the challenger is frozen and are
reported separately (`MARKET_BENCHMARK.md`); they cannot change the challenger.

## 2. Data and temporal splits

* Data: `canonical_v2` (cross-source near-duplicates removed, mirror main-tour files, minted new players).
  Evaluation rows: every MAPPED singles match except walkovers (completed, retired, defaulted), tour by tour.
* Ratings replay from 1990; per-match records from 2005; the ensemble (stacker) for season Y is fitted only on
  seasons Y-6 .. Y-1 (seasons >= 2008), so every evaluated probability is out of sample in time.
* **Selection window 2016-2020**: all choices (Elo variant, form horizon, which feature blocks enter, stacker
  regularisation) are made here and only here.
* **Evaluation window 2021-2024**: candidates and ablations are reported; no choice is changed because of it.
* **Validation season 2025**: computed once, after the challenger is frozen.
* **Holdout 2026 YTD**: computed once, after validation, by the same frozen code.

Candour about 2026: earlier waves of this repository evaluated Elo variants on seasons 2015-2026 and Kalshi
markets from July-September 2026, so 2026 is not virgin territory for the Elo family in general. No V2
model family (margin of victory, form, context, evidence-bucketed stacker) has been evaluated on 2026 before
this file. The cleanest confirmation available is therefore (a) the 2026 holdout as defined here and (b) the
prospective shadow comparison from 2026-10-05 onward (§6), which no one has seen.

## 3. How the challenger is chosen (selection window only)

1. Elo variant: the variant in `ELO_VARIANTS` with the lowest pooled (both tours) log loss in 2016-2020.
2. Feature blocks are added greedily to the stacker in this fixed order: level slopes, experience, Gen-2
   evidence buckets, Gen-1 structural, Gen-2 short half-life, form, context, age. A block stays only if it
   lowers 2016-2020 walk-forward log loss by >= 0.0002 on BOTH tours (or by >= 0.0004 pooled with neither
   tour worse by > 0.0001).
3. Form horizon: the single horizon (30/60/120/240 d) with the lowest 2016-2020 log loss when added alone.
4. L2 strength: C in {0.01, 0.1, 1, 10}, chosen on 2016-2020 log loss.
5. The resulting specification is written to `research/projection_v2/FROZEN_CHALLENGER.json` with a hash
   before 2025 or 2026 metrics are computed.

## 4. Metrics

Primary: Brier score and log loss, symmetric orientation (a deterministic hash coin flip decides which
player is "A"). Secondary: calibration slope and intercept (logistic recalibration), ECE (10 bins),
favourite-oriented reliability tables, accuracy. Every comparison is **paired** (candidate minus incumbent
on the same matches) with a **cluster bootstrap over tournament instances** (tourney_id x season; 2,000
Poisson-weight resamples; 95% percentile interval), because matches within an event share players and
conditions.

## 5. Promotion rules (all must hold)

Computed on 2021-2025 unless stated; "segment" = tour x level group (Grand Slam, Masters 1000, Tour 250/500,
Challenger / WTA 125, ITF) with n >= 2,000.

| # | rule |
|---|---|
| P1 | For EACH tour: Brier difference 95% CI entirely below 0 AND log-loss difference 95% CI entirely below 0. |
| P2 | For EACH tour: Brier improvement point estimate >= 0.0005. |
| P3 | For EACH tour: calibration slope within [0.90, 1.10] or closer to 1 than the incumbent's; ECE no more than 0.002 above the incumbent's. |
| P4 | For EACH tour: point improvement in at least 4 of the 5 seasons 2021-2025, and no season with a significant degradation (CI entirely above 0). |
| P5 | No segment with a significant degradation (Brier CI entirely above 0) and none with a point degradation > 0.003. |
| P6 | Removing the single segment that contributes most to the improvement leaves the pooled Brier CI entirely below 0. |
| P7 | Validation season 2025 alone: Brier point improvement on each tour. |
| P8 | Holdout 2026: not significantly worse on either tour (Brier CI lower bound <= 0), pooled point estimate <= 0. |
| P9 | Operational: the live inference path reproduces the research probability for the same state (parity test), no leakage or market-import test fails, identity behaviour unchanged except as separately audited, RUN TENNIS runtime grows by < 3 minutes, full test suite green. |

If any rule fails, the challenger is **not promoted**: production stays on the incumbent and V2 runs in
shadow beside it, published with every run. That outcome is a success if it is the correct one.

The data fix (`canonical_v2`) is judged separately: it removes duplicated matches, which is an objective
defect, and is deployed only if INCUMBENT on `canonical_v2` is not significantly worse than INCUMBENT_V1DATA
on either tour (common evaluation rows, same bootstrap).

## 6. Prospective confirmation

From the first production run carrying V2 (shadow or promoted), every projected singles match records both
the incumbent and the V2 probability before the first ball, in the append-only ledger. After >= 1,500
independently settled matches the same paired comparison (P1 on the prospective sample) is reported. A
prospective result contradicting the backtest (CI entirely above 0) triggers rollback to the incumbent.
