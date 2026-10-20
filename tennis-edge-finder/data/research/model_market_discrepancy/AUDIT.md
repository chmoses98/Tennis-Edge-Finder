# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-20T04:31Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 42,546): 0-3 14.3%, 3-5 9.5%, 5-10 19.9%, 10-15 15.4%, 15-25 19.2%, 25-40 13.8%, 40+ 7.9%; median gap 11.91 pp.
* **Where the extremes live**: 97.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 75.4%, Challenger 12.6%, doubles 7.2%). Main tour: ATP 4.4% and WTA 4.6% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 9,223): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.3%, BOOK_QUALITY 19.5%, STALE_QUOTE 17.8%, POOR_DATA 9.0%, POSSIBLY_IN_PLAY_QUOTE 5.2%, IDENTITY_AMBIGUOUS 4.4%, LIMITED_DATA 3.8%, IN_PLAY_QUOTE 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.6%. By class: coverage 34.3%, execution 19.5%, market_freshness 17.8%, data 12.8%, market_freshness/coverage 8.5%, mapping 4.4%, model_calibration_or_unknown 2.1%, model_calibration 0.6%.
* **Stale / settled / in-play**: 51.0% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.8% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 9,223 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.5%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 23.9% of the time and with the model 0.6%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 514.0 points vs 1787.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.057, Gen-2 0.85, Gen-1 ledger 0.883 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 438 model 0.2236 vs Kalshi 0.2081; n 87 model 0.297 vs Kalshi 0.1766.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 180,876 model-market comparisons (293,653 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 63,463 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-20T04:21:29.289950+00:00'], shadow board 47,336 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-20T04:21:32.142144+00:00'], Model 4 22,373 rows, 16,908 settled tickers, 5,837 tickers with an external scan.
* By model: {"gen1_ledger": 42864, "gen1_elo": 23799, "fair_v1": 23799, "gen2": 23799, "gen1_sr": 23799, "model4_fundamental": 21417, "model4_conditioned": 21399}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 42,546 | 14.3 | 9.5 | 19.9 | 15.4 | 19.2 | 13.8 | 7.9 | 11.91 | 40.9% | 21.7% |
| MW fair_v1 | 23,799 | 13.3 | 8.6 | 18.4 | 15.9 | 19.7 | 14.6 | 9.4 | 12.99 | 43.7% | 24.0% |
| MW gen1_elo | 23,799 | 13.0 | 9.0 | 19.4 | 15.2 | 19.7 | 14.5 | 9.2 | 12.66 | 43.4% | 23.7% |
| MW gen1_ledger | 18,747 | 15.5 | 10.7 | 21.7 | 14.9 | 18.5 | 12.7 | 6.0 | 10.53 | 37.2% | 18.7% |
| MW gen1_sr | 23,799 | 10.0 | 7.3 | 16.8 | 14.2 | 21.4 | 18.4 | 11.8 | 15.61 | 51.7% | 30.3% |
| MW gen2 | 23,799 | 11.3 | 7.4 | 16.4 | 14.3 | 20.1 | 17.6 | 13.0 | 15.38 | 50.7% | 30.6% |
| all families model4_conditioned | 21,399 | 21.9 | 19.1 | 34.4 | 17.6 | 4.7 | 1.4 | 1.1 | 5.94 | 7.1% | 2.4% |
| all families model4_fundamental | 21,417 | 16.2 | 13.0 | 34.3 | 20.5 | 11.4 | 3.4 | 1.3 | 7.91 | 16.1% | 4.7% |

Configurable thresholds (primary): >=5pp 76.2%, >=10pp 56.3%, >=15pp 40.9%, >=20pp 30.2%, >=25pp 21.7%, >=30pp 15.5%, >=40pp 7.9%, >=50pp 3.6%
Executable gap (model outside the book, before fees): median 8.28pp; >=10pp 44.7%, >=25pp 16.7%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,091 | 28.6 | 13.7 | 25.0 | 15.9 | 11.6 | 4.6 | 0.6 | 6.31 | 16.7% | 5.2% |
| CHALLENGER | 4,013 | 15.4 | 10.3 | 20.2 | 16.1 | 14.7 | 12.3 | 10.9 | 11.31 | 38.0% | 23.3% |
| ITF_MEN | 6,260 | 10.9 | 7.8 | 17.2 | 14.7 | 20.5 | 16.6 | 12.3 | 14.82 | 49.4% | 28.8% |
| ITF_WOMEN | 9,312 | 10.0 | 6.8 | 15.8 | 15.6 | 23.0 | 18.1 | 10.8 | 15.61 | 51.9% | 28.9% |
| WTA | 1,463 | 17.8 | 12.5 | 24.2 | 19.7 | 20.9 | 4.2 | 0.8 | 8.65 | 25.8% | 5.0% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,091 | 23.4 | 15.3 | 24.4 | 17.2 | 13.9 | 4.9 | 0.9 | 6.76 | 19.7% | 5.8% |
| CHALLENGER | 4,013 | 14.7 | 8.3 | 18.7 | 14.3 | 18.0 | 14.1 | 11.9 | 12.77 | 44.0% | 26.0% |
| ITF_MEN | 6,260 | 9.2 | 6.5 | 15.4 | 13.4 | 19.7 | 19.9 | 15.9 | 17.48 | 55.5% | 35.8% |
| ITF_WOMEN | 9,312 | 8.3 | 5.6 | 13.6 | 13.7 | 21.5 | 20.8 | 16.6 | 18.84 | 58.9% | 37.3% |
| WTA | 1,463 | 14.9 | 9.5 | 19.9 | 16.1 | 24.2 | 14.6 | 0.8 | 11.66 | 39.6% | 15.4% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,091 | 23.8 | 13.6 | 25.1 | 16.3 | 14.7 | 5.6 | 0.9 | 7.04 | 21.2% | 6.5% |
| CHALLENGER | 4,013 | 14.4 | 9.8 | 21.2 | 15.1 | 15.9 | 12.3 | 11.3 | 11.2 | 39.5% | 23.6% |
| ITF_MEN | 6,260 | 10.0 | 7.9 | 17.5 | 14.0 | 21.3 | 16.9 | 12.3 | 15.15 | 50.5% | 29.2% |
| ITF_WOMEN | 9,312 | 9.5 | 6.9 | 16.2 | 15.8 | 23.2 | 18.4 | 10.0 | 15.57 | 51.6% | 28.3% |
| WTA | 1,463 | 24.7 | 16.7 | 30.1 | 15.4 | 10.3 | 2.3 | 0.5 | 6.0 | 13.1% | 2.8% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,206 | 26.9 | 20.2 | 30.1 | 11.8 | 7.9 | 2.8 | 0.2 | 5.3 | 10.9% | 3.1% |
| CHALLENGER | 2,804 | 21.6 | 14.7 | 27.2 | 13.9 | 14.5 | 6.2 | 1.9 | 7.17 | 22.6% | 8.1% |
| DOUBLES | 1,357 | 4.5 | 4.1 | 11.1 | 10.6 | 20.9 | 26.2 | 22.6 | 24.11 | 69.6% | 48.7% |
| ITF_MEN | 5,238 | 14.2 | 8.7 | 20.7 | 15.9 | 20.7 | 12.9 | 6.8 | 11.89 | 40.4% | 19.8% |
| ITF_WOMEN | 6,270 | 12.1 | 8.8 | 19.2 | 15.2 | 22.0 | 16.7 | 6.1 | 13.15 | 44.7% | 22.8% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 991 | 22.4 | 16.0 | 29.1 | 18.2 | 10.3 | 3.7 | 0.3 | 6.9 | 14.3% | 4.0% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,049 | 28.8 | 13.8 | 25.3 | 15.8 | 11.4 | 4.3 | 0.6 | 6.17 | 16.4% | 4.9% |
| CHALLENGER | 2,853 | 20.1 | 12.7 | 25.1 | 18.6 | 15.1 | 6.5 | 2.0 | 8.36 | 23.5% | 8.4% |
| ITF_MEN | 4,588 | 13.3 | 9.6 | 20.4 | 16.6 | 21.0 | 13.5 | 5.5 | 11.91 | 40.1% | 19.1% |
| ITF_WOMEN | 7,021 | 11.6 | 8.1 | 17.8 | 17.6 | 24.6 | 15.4 | 4.8 | 13.42 | 44.8% | 20.2% |
| WTA | 1,424 | 18.0 | 12.2 | 24.1 | 19.8 | 20.9 | 4.2 | 0.8 | 8.65 | 25.9% | 5.0% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,049 | 23.6 | 15.5 | 24.4 | 17.2 | 13.8 | 4.8 | 0.7 | 6.63 | 19.3% | 5.5% |
| CHALLENGER | 2,853 | 18.4 | 10.6 | 23.3 | 17.2 | 18.5 | 9.6 | 2.4 | 9.46 | 30.4% | 11.9% |
| ITF_MEN | 4,589 | 10.8 | 7.8 | 17.7 | 15.1 | 21.7 | 17.9 | 9.0 | 14.46 | 48.5% | 26.9% |
| ITF_WOMEN | 7,021 | 9.1 | 6.4 | 14.9 | 15.0 | 23.6 | 20.4 | 10.6 | 16.71 | 54.5% | 30.9% |
| WTA | 1,424 | 14.9 | 9.5 | 19.8 | 16.0 | 24.2 | 14.8 | 0.8 | 11.72 | 39.8% | 15.6% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,168 | 27.1 | 20.5 | 30.3 | 12.0 | 7.4 | 2.6 | 0.1 | 5.25 | 10.1% | 2.7% |
| CHALLENGER | 2,442 | 23.1 | 15.9 | 29.0 | 13.6 | 13.9 | 3.9 | 0.6 | 6.58 | 18.4% | 4.5% |
| DOUBLES | 1,261 | 4.5 | 4.3 | 11.3 | 10.8 | 20.9 | 26.3 | 22.0 | 24.07 | 69.2% | 48.3% |
| ITF_MEN | 4,368 | 15.5 | 9.4 | 22.5 | 16.8 | 20.4 | 11.2 | 4.1 | 10.72 | 35.7% | 15.3% |
| ITF_WOMEN | 5,238 | 12.8 | 9.3 | 20.6 | 16.1 | 22.2 | 15.5 | 3.5 | 11.93 | 41.2% | 19.0% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 945 | 22.9 | 16.5 | 29.1 | 18.2 | 10.4 | 3.0 | 0.0 | 6.8 | 13.3% | 3.0% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,357 | 4.5 | 4.1 | 11.1 | 10.6 | 20.9 | 26.2 | 22.6 | 24.11 | 69.6% | 48.7% |
| singles | 17,390 | 16.3 | 11.2 | 22.5 | 15.3 | 18.3 | 11.7 | 4.7 | 9.99 | 34.7% | 16.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 5,381 | 13.5 | 9.0 | 19.4 | 15.8 | 18.4 | 14.5 | 9.4 | 12.6 | 42.2% | 23.9% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 15,246 | 13.7 | 8.6 | 18.4 | 15.5 | 20.1 | 14.3 | 9.4 | 12.99 | 43.8% | 23.7% |
| UNKNOWN | 2,935 | 11.3 | 7.9 | 16.8 | 17.9 | 20.3 | 15.9 | 9.9 | 13.55 | 46.2% | 25.9% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,960 | 19.6 | 11.4 | 21.4 | 17.1 | 16.0 | 8.8 | 5.8 | 9.33 | 30.6% | 14.6% |
| B | 3,074 | 12.9 | 9.1 | 20.2 | 17.1 | 18.5 | 11.8 | 10.5 | 12.04 | 40.8% | 22.3% |
| C | 3,363 | 12.7 | 9.0 | 19.0 | 14.8 | 19.8 | 14.9 | 9.8 | 12.93 | 44.5% | 24.7% |
| D | 3,960 | 12.2 | 8.0 | 17.0 | 15.8 | 22.0 | 15.4 | 9.5 | 13.94 | 47.0% | 24.9% |
| F | 6,442 | 7.8 | 5.6 | 15.1 | 14.6 | 22.9 | 21.4 | 12.7 | 17.83 | 57.0% | 34.0% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,424 | 23.3 | 15.9 | 28.6 | 15.2 | 11.5 | 4.1 | 1.4 | 6.61 | 17.0% | 5.5% |
| B | 2,630 | 15.7 | 10.2 | 24.1 | 16.4 | 19.1 | 10.7 | 3.9 | 10.02 | 33.7% | 14.6% |
| C | 3,725 | 10.9 | 7.4 | 18.1 | 14.4 | 21.9 | 16.4 | 10.9 | 14.59 | 49.2% | 27.3% |
| D | 2,725 | 14.0 | 9.7 | 20.0 | 14.4 | 21.0 | 14.6 | 6.3 | 12.08 | 41.9% | 20.9% |
| F | 4,243 | 10.3 | 7.8 | 15.6 | 14.5 | 22.6 | 20.6 | 8.7 | 15.95 | 51.9% | 29.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 7,896 | 17.9 | 10.3 | 20.7 | 17.1 | 16.4 | 9.5 | 8.2 | 10.29 | 34.1% | 17.7% |
| LIMITED | 5,285 | 14.3 | 10.2 | 20.2 | 15.5 | 19.2 | 13.3 | 7.3 | 11.6 | 39.8% | 20.6% |
| POOR | 10,618 | 9.5 | 6.6 | 15.9 | 15.1 | 22.5 | 18.9 | 11.4 | 16.0 | 52.9% | 30.4% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,648 | 26.8 | 21.2 | 34.8 | 11.6 | 4.1 | 1.4 | 0.2 | 5.16 | 5.7% | 1.6% |
| GAME_SPREAD | 4,087 | 23.4 | 15.4 | 33.5 | 17.1 | 8.0 | 2.2 | 0.3 | 6.47 | 10.5% | 2.5% |
| MATCH_WINNER | 18,747 | 15.5 | 10.7 | 21.7 | 14.9 | 18.5 | 12.7 | 6.0 | 10.53 | 37.2% | 18.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 8,701 | 30.3 | 17.1 | 30.4 | 12.4 | 8.0 | 1.3 | 0.4 | 5.31 | 9.8% | 1.8% |
| TOTAL_GAMES | 6,657 | 7.6 | 9.0 | 36.7 | 29.1 | 11.1 | 3.5 | 2.9 | 9.63 | 17.5% | 6.4% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,487 | 25.4 | 34.6 | 32.3 | 3.7 | 3.2 | 0.6 | 0.2 | 4.46 | 4.0% | 0.7% |
| GAME_SPREAD | 5,120 | 46.1 | 16.9 | 27.0 | 7.4 | 1.7 | 0.6 | 0.2 | 3.4 | 2.6% | 0.9% |
| TOTAL_GAMES | 8,792 | 4.7 | 7.1 | 40.5 | 35.3 | 7.5 | 2.5 | 2.3 | 9.77 | 12.4% | 4.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,490 | 24.3 | 17.8 | 35.8 | 12.1 | 7.2 | 2.5 | 0.3 | 5.8 | 10.0% | 2.8% |
| GAME_SPREAD | 5,123 | 19.2 | 13.3 | 28.4 | 20.0 | 14.2 | 4.0 | 0.9 | 7.95 | 19.1% | 4.9% |
| TOTAL_GAMES | 8,804 | 7.5 | 8.6 | 36.4 | 27.9 | 13.3 | 3.8 | 2.4 | 9.7 | 19.5% | 6.2% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 23,799 | 43.7% | 24.0% | 12.99 | 35.5% | 15.1% | 10.82 |
| gen1_elo | 23,799 | 43.4% | 23.7% | 12.66 | 34.7% | 15.1% | 10.46 |
| gen1_sr | 23,799 | 51.7% | 30.3% | 15.61 | 44.2% | 21.3% | 13.06 |
| gen2 | 23,799 | 50.7% | 30.6% | 15.38 | 44.3% | 22.9% | 13.07 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 12,702 | 16.0 | 10.4 | 21.3 | 17.4 | 20.1 | 11.5 | 3.2 | 10.64 | 34.9% | 14.8% |
| STALE | 11,097 | 10.3 | 6.6 | 15.2 | 14.1 | 19.3 | 18.0 | 16.6 | 16.99 | 53.8% | 34.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 12,215 | 16.7 | 11.3 | 22.7 | 15.0 | 17.5 | 12.0 | 4.8 | 9.79 | 34.3% | 16.8% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 42,546 | 12215 | 16174 | 14157 | 23.6 | 131.0 | 1400.4 |
| ge_15pp | 17,393 | 4185 | 5722 | 7486 | 25.7 | 431.4 | 1380.4 |
| ge_25pp | 9,223 | 2050 | 2465 | 4708 | 31.3 | 574.7 | 1380.4 |
| lt_10pp | 18,582 | 6197 | 7690 | 4695 | 21.7 | 47.5 | 1341.5 |

Current slate `SL-20261020T043148Z-f53ad35c`: 687 priced rows, quote age at build {'median': 10.7, 'max': 10.8}, freshness {'AGING': 687}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 11 | 0.0 | 0.0 | 36.4 | 0.0 | 45.5 | 18.2 | 0.0 | 20.19 | 63.6% | 18.2% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,243 | 20.1 | 10.8 | 23.5 | 18.9 | 19.0 | 7.0 | 0.6 | 9.0 | 26.6% | 7.6% |
| KALSHI_LONE_OUTLIER | 12 | 8.3 | 0.0 | 75.0 | 0.0 | 8.3 | 8.3 | 0.0 | 5.35 | 16.7% | 8.3% |
| MARKETS_AGREE | 383 | 68.9 | 31.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.08 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 837 | 0.0 | 2.8 | 35.1 | 28.2 | 23.9 | 9.4 | 0.6 | 12.02 | 33.9% | 10.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 23,799 | 3498 (14.7%) | 23.9% | 0.6% | {"EXTERNAL_STALE": 2243, "AGREES_WITH_KALSHI": 837, "ALL_AGREE": 383, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 12, "SUPPORTS_MODEL_DIRECTION": 10, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 10,409 | 890 (8.6%) | 31.9% | 1.0% | {"EXTERNAL_STALE": 597, "AGREES_WITH_KALSHI": 284, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 5,711 | 257 (4.5%) | 32.7% | 1.2% | {"EXTERNAL_STALE": 170, "AGREES_WITH_KALSHI": 84, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,797 | 243 (8.7%) | 33.7% | 1.2% | {"EXTERNAL_STALE": 158, "AGREES_WITH_KALSHI": 82, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 9,616 | 1949 (20.3%) | 16.3% | 0.7% | {"EXTERNAL_STALE": 1223, "ALL_AGREE": 383, "AGREES_WITH_KALSHI": 317, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 10, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 4,572 | 10.9 | 7.8 | 19.5 | 14.9 | 21.9 | 15.3 | 9.7 | 13.82 | 46.9% | 25.0% |
| 4-10x | 3,114 | 11.8 | 8.6 | 18.8 | 15.7 | 20.2 | 15.1 | 9.9 | 13.37 | 45.2% | 25.0% |
| <2x | 12,324 | 15.3 | 9.6 | 18.9 | 16.9 | 18.2 | 12.6 | 8.4 | 11.72 | 39.2% | 21.0% |
| >=10x | 3,789 | 11.1 | 6.4 | 15.3 | 13.6 | 21.7 | 19.6 | 12.2 | 16.36 | 53.6% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 6,073 | 12.7 | 8.5 | 19.7 | 16.3 | 19.7 | 13.2 | 9.9 | 12.71 | 42.8% | 23.1% |
| 300-1000 | 5,227 | 12.1 | 8.8 | 16.9 | 15.8 | 20.9 | 16.1 | 9.6 | 13.82 | 46.6% | 25.7% |
| <300 | 7,310 | 8.9 | 5.9 | 15.5 | 14.7 | 22.6 | 20.1 | 12.2 | 16.86 | 55.0% | 32.3% |
| >=3000 | 5,189 | 21.5 | 12.5 | 22.7 | 17.1 | 14.5 | 6.8 | 4.8 | 8.09 | 26.2% | 11.7% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 709 | 0.5436 | 0.409 | 0.4937 | +0.050 | -0.085 | 0.0003 ± 0.0057 |
| ratio 4-10x | 487 | 0.5926 | 0.4504 | 0.5154 | +0.077 | -0.065 | 0.0079 ± 0.0072 |
| ratio <2x | 1735 | 0.538 | 0.4168 | 0.4507 | +0.087 | -0.034 | 0.012 ± 0.0034 |
| ratio >=10x | 592 | 0.5639 | 0.3897 | 0.4493 | +0.115 | -0.060 | 0.0118 ± 0.0075 |
| thinner_sample 1000-3000 | 975 | 0.5439 | 0.4175 | 0.4585 | +0.086 | -0.041 | 0.0095 ± 0.0046 |
| thinner_sample 300-1000 | 842 | 0.5664 | 0.4255 | 0.4988 | +0.068 | -0.073 | 0.0002 ± 0.0054 |
| thinner_sample <300 | 1108 | 0.5557 | 0.3927 | 0.4549 | +0.101 | -0.062 | 0.0132 ± 0.0053 |
| thinner_sample >=3000 | 598 | 0.5325 | 0.4392 | 0.4649 | +0.068 | -0.026 | 0.0133 ± 0.0047 |
| data_status ADEQUATE | 1024 | 0.5354 | 0.431 | 0.457 | +0.078 | -0.026 | 0.0114 ± 0.0039 |
| data_status LIMITED | 866 | 0.5537 | 0.4226 | 0.4873 | +0.066 | -0.065 | 0.0034 ± 0.005 |
| data_status POOR | 1633 | 0.5595 | 0.4016 | 0.4648 | +0.095 | -0.063 | 0.0106 ± 0.0042 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 533 | 0.196 | 0.1973 | -0.0013 ± 0.0007 | 0.5706 | 0.5733 | 0.4968 | 0.4818 | 0.5328 | -0.051 ± 0.0202 | -0.01 (5) |
| 3-5 | 339 | 0.1984 | 0.1976 | +0.0008 ± 0.0019 | 0.5791 | 0.5758 | 0.5055 | 0.4655 | 0.4749 | -0.091 ± 0.0249 | 0.02 (1) |
| 5-10 | 728 | 0.199 | 0.1993 | -0.0002 ± 0.0025 | 0.5835 | 0.5821 | 0.5128 | 0.4384 | 0.4725 | -0.083 ± 0.0172 | -0.0167 (6) |
| 10-15 | 624 | 0.2145 | 0.206 | +0.0086 ± 0.0046 | 0.6189 | 0.5942 | 0.5269 | 0.4027 | 0.4295 | -0.096 ± 0.0181 | -0.048 (5) |
| 15-25 | 774 | 0.2275 | 0.2147 | +0.0128 ± 0.0065 | 0.6488 | 0.6143 | 0.5814 | 0.3861 | 0.4509 | -0.090 ± 0.0166 | -0.0033 (9) |
| 25-40 | 438 | 0.2236 | 0.2081 | +0.0155 ± 0.0129 | 0.6354 | 0.5987 | 0.6553 | 0.3474 | 0.4749 | -0.076 ± 0.0198 | -0.01 (1) |
| 40+ | 87 | 0.297 | 0.1766 | +0.1204 ± 0.0404 | 0.8103 | 0.527 | 0.7594 | 0.3102 | 0.4023 | -0.126 ± 0.0388 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2539 | 0.1803 | 0.1816 | -0.0013 ± 0.0003 | 0.5355 | 0.5369 | 0.479 | 0.4639 | 0.5026 | -0.019 ± 0.0086 | -0.0129 (17) |
| 3-5 | 1636 | 0.1937 | 0.1918 | +0.0019 ± 0.0009 | 0.5681 | 0.5597 | 0.4821 | 0.4423 | 0.437 | -0.064 ± 0.011 | 0.0 (2) |
| 5-10 | 3483 | 0.1946 | 0.1914 | +0.0032 ± 0.0011 | 0.5714 | 0.5612 | 0.4853 | 0.4116 | 0.4246 | -0.051 ± 0.0075 | -0.0119 (21) |
| 10-15 | 3110 | 0.2051 | 0.1868 | +0.0183 ± 0.0019 | 0.5978 | 0.5468 | 0.4887 | 0.3641 | 0.3534 | -0.076 ± 0.0077 | -0.0281 (16) |
| 15-25 | 3769 | 0.2092 | 0.1725 | +0.0367 ± 0.0027 | 0.6097 | 0.5093 | 0.503 | 0.3068 | 0.3125 | -0.069 ± 0.0067 | -0.0025 (44) |
| 25-40 | 2904 | 0.2222 | 0.127 | +0.0953 ± 0.0041 | 0.6387 | 0.3906 | 0.532 | 0.2194 | 0.2269 | -0.067 ± 0.0064 | -0.01 (1) |
| 40+ | 1932 | 0.3796 | 0.0428 | +0.3368 ± 0.0053 | 0.9879 | 0.1696 | 0.6298 | 0.107 | 0.0569 | -0.087 ± 0.0044 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 398 | 0.1994 | 0.2 | -0.0006 ± 0.0008 | 0.5806 | 0.5819 | 0.5042 | 0.4892 | 0.5126 | -0.085 ± 0.0239 | -0.01 (3) |
| 3-5 | 288 | 0.2166 | 0.2157 | +0.0009 ± 0.0022 | 0.6166 | 0.6155 | 0.5162 | 0.4764 | 0.4792 | -0.097 ± 0.0292 | 0.02 (1) |
| 5-10 | 626 | 0.1988 | 0.1991 | -0.0004 ± 0.0027 | 0.5809 | 0.5814 | 0.5462 | 0.4712 | 0.5112 | -0.073 ± 0.0184 | -0.01 (4) |
| 10-15 | 587 | 0.2172 | 0.2113 | +0.0058 ± 0.0048 | 0.6243 | 0.6088 | 0.5681 | 0.4437 | 0.4855 | -0.094 ± 0.0197 | -0.04 (5) |
| 15-25 | 843 | 0.2312 | 0.21 | +0.0211 ± 0.0062 | 0.6543 | 0.603 | 0.5922 | 0.396 | 0.4448 | -0.098 ± 0.0161 | -0.0133 (9) |
| 25-40 | 577 | 0.2629 | 0.1991 | +0.0638 ± 0.0117 | 0.7342 | 0.579 | 0.6645 | 0.3494 | 0.4073 | -0.118 ± 0.0182 | -0.0075 (4) |
| 40+ | 204 | 0.3678 | 0.1756 | +0.1922 ± 0.0291 | 1.0227 | 0.5218 | 0.7445 | 0.2622 | 0.3186 | -0.084 ± 0.0283 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2170 | 0.1853 | 0.186 | -0.0007 ± 0.0003 | 0.547 | 0.5483 | 0.5024 | 0.4875 | 0.5134 | -0.031 ± 0.0096 | -0.0133 (15) |
| 3-5 | 1384 | 0.1967 | 0.1961 | +0.0006 ± 0.001 | 0.5698 | 0.5681 | 0.5154 | 0.4755 | 0.4855 | -0.044 ± 0.0121 | 0.02 (1) |
| 5-10 | 3105 | 0.1908 | 0.1891 | +0.0017 ± 0.0012 | 0.5636 | 0.5562 | 0.5072 | 0.4332 | 0.4605 | -0.035 ± 0.0079 | -0.0117 (6) |
| 10-15 | 2737 | 0.1998 | 0.1889 | +0.0110 ± 0.0021 | 0.5878 | 0.55 | 0.5195 | 0.3949 | 0.4154 | -0.051 ± 0.0084 | -0.0189 (18) |
| 15-25 | 3903 | 0.2176 | 0.1797 | +0.0378 ± 0.0027 | 0.6297 | 0.528 | 0.5317 | 0.3354 | 0.3408 | -0.070 ± 0.0068 | -0.0086 (42) |
| 25-40 | 3429 | 0.2504 | 0.1381 | +0.1122 ± 0.004 | 0.7067 | 0.4228 | 0.5633 | 0.2471 | 0.2298 | -0.088 ± 0.0063 | -0.0044 (18) |
| 40+ | 2645 | 0.4014 | 0.0645 | +0.3369 ± 0.0057 | 1.059 | 0.2267 | 0.6618 | 0.125 | 0.0926 | -0.072 ± 0.0048 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 512 | 0.1979 | 0.2005 | -0.0025 ± 0.0007 | 0.5765 | 0.5825 | 0.4985 | 0.4832 | 0.5566 | -0.014 ± 0.0202 | -0.0137 (8) |
| 3-5 | 374 | 0.1943 | 0.1921 | +0.0021 ± 0.0018 | 0.5663 | 0.5612 | 0.5 | 0.4604 | 0.4545 | -0.119 ± 0.0236 | 0.0067 (3) |
| 5-10 | 764 | 0.201 | 0.1978 | +0.0032 ± 0.0024 | 0.5888 | 0.5778 | 0.5082 | 0.4343 | 0.4463 | -0.098 ± 0.0166 | -0.0071 (7) |
| 10-15 | 610 | 0.2095 | 0.2072 | +0.0023 ± 0.0046 | 0.6068 | 0.5976 | 0.5416 | 0.4184 | 0.4738 | -0.076 ± 0.0182 | -0.0317 (6) |
| 15-25 | 722 | 0.234 | 0.2111 | +0.0229 ± 0.0067 | 0.6665 | 0.6061 | 0.5899 | 0.3965 | 0.4335 | -0.116 ± 0.0171 | -0.03 (1) |
| 25-40 | 452 | 0.2115 | 0.2143 | -0.0028 ± 0.0127 | 0.6094 | 0.6126 | 0.6633 | 0.3535 | 0.5111 | -0.054 ± 0.0194 | 0.015 (2) |
| 40+ | 89 | 0.3108 | 0.1932 | +0.1177 ± 0.0416 | 0.8465 | 0.5643 | 0.7657 | 0.3136 | 0.4157 | -0.111 ± 0.043 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2428 | 0.1872 | 0.1882 | -0.0010 ± 0.0003 | 0.5512 | 0.553 | 0.4876 | 0.4723 | 0.4984 | -0.029 ± 0.0089 | -0.0163 (35) |
| 3-5 | 1698 | 0.189 | 0.186 | +0.0030 ± 0.0008 | 0.5557 | 0.5484 | 0.4818 | 0.4423 | 0.4246 | -0.080 ± 0.0107 | -0.0094 (18) |
| 5-10 | 3723 | 0.195 | 0.1888 | +0.0062 ± 0.0011 | 0.5742 | 0.554 | 0.4849 | 0.411 | 0.404 | -0.068 ± 0.0072 | -0.01 (31) |
| 10-15 | 2902 | 0.198 | 0.1818 | +0.0161 ± 0.002 | 0.5811 | 0.5337 | 0.501 | 0.3774 | 0.3742 | -0.071 ± 0.0079 | -0.015 (12) |
| 15-25 | 3874 | 0.2118 | 0.1723 | +0.0395 ± 0.0026 | 0.6176 | 0.5091 | 0.5105 | 0.3159 | 0.3123 | -0.076 ± 0.0067 | -0.03 (2) |
| 25-40 | 2880 | 0.2186 | 0.1262 | +0.0924 ± 0.0042 | 0.6303 | 0.3874 | 0.5316 | 0.216 | 0.2306 | -0.064 ± 0.0063 | 0.01 (3) |
| 40+ | 1868 | 0.3943 | 0.0475 | +0.3468 ± 0.0057 | 1.029 | 0.1822 | 0.6413 | 0.1124 | 0.061 | -0.089 ± 0.0048 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 857 | 0.1962 | 0.1964 | -0.0002 ± 0.0005 | 0.5727 | 0.573 | 0.5069 | 0.4919 | 0.4982 | -0.054 ± 0.0153 | -0.0224 (49) |
| 3-5 | 604 | 0.1937 | 0.1929 | +0.0007 ± 0.0014 | 0.5655 | 0.5626 | 0.4821 | 0.4423 | 0.4503 | -0.054 ± 0.0181 | -0.0194 (34) |
| 5-10 | 1282 | 0.1997 | 0.1934 | +0.0063 ± 0.0019 | 0.587 | 0.5687 | 0.4906 | 0.4173 | 0.4119 | -0.070 ± 0.0126 | -0.005 (78) |
| 10-15 | 819 | 0.2085 | 0.1975 | +0.0110 ± 0.0039 | 0.605 | 0.5769 | 0.5147 | 0.3916 | 0.4066 | -0.064 ± 0.0157 | 0.0014 (64) |
| 15-25 | 1101 | 0.2323 | 0.2113 | +0.0210 ± 0.0054 | 0.662 | 0.6087 | 0.5721 | 0.3772 | 0.4223 | -0.065 ± 0.0139 | -0.0214 (59) |
| 25-40 | 652 | 0.2473 | 0.2012 | +0.0461 ± 0.0108 | 0.7005 | 0.5814 | 0.6583 | 0.3463 | 0.4264 | -0.085 ± 0.0163 | -0.0219 (26) |
| 40+ | 229 | 0.3492 | 0.194 | +0.1552 ± 0.0291 | 1.0088 | 0.5691 | 0.8045 | 0.3186 | 0.4236 | -0.081 ± 0.0256 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2698 | 0.1868 | 0.1869 | -0.0001 ± 0.0003 | 0.5483 | 0.5476 | 0.5062 | 0.4909 | 0.4993 | -0.038 ± 0.0083 | -0.0157 (88) |
| 3-5 | 1860 | 0.1905 | 0.1878 | +0.0027 ± 0.0008 | 0.5572 | 0.551 | 0.488 | 0.4483 | 0.4349 | -0.061 ± 0.0101 | -0.0209 (69) |
| 5-10 | 3776 | 0.1964 | 0.1878 | +0.0086 ± 0.0011 | 0.5777 | 0.5537 | 0.4887 | 0.4152 | 0.3957 | -0.072 ± 0.0071 | -0.0082 (132) |
| 10-15 | 2562 | 0.2043 | 0.1896 | +0.0147 ± 0.0021 | 0.5953 | 0.5577 | 0.5213 | 0.3983 | 0.3993 | -0.061 ± 0.0086 | -0.0053 (105) |
| 15-25 | 3228 | 0.2288 | 0.1977 | +0.0311 ± 0.0031 | 0.6586 | 0.5754 | 0.5636 | 0.3683 | 0.3882 | -0.065 ± 0.0079 | -0.0253 (107) |
| 25-40 | 2196 | 0.2543 | 0.1759 | +0.0784 ± 0.0056 | 0.7201 | 0.5167 | 0.6192 | 0.3057 | 0.3406 | -0.077 ± 0.0087 | -0.0229 (51) |
| 40+ | 1037 | 0.3742 | 0.1372 | +0.2371 ± 0.0122 | 1.0618 | 0.4164 | 0.7223 | 0.2187 | 0.2488 | -0.072 ± 0.0106 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3523 | 1.057 ± 0.048 | 1.189 | 0.1671 | 0.1638 | 0.213 | 0.2039 |
| gen2 | 3523 | 0.85 ± 0.044 | 1.147 | 0.1727 | 0.1642 | 0.2314 | 0.2039 |
| gen1_elo | 3523 | 1.034 ± 0.046 | 1.171 | 0.1733 | 0.1641 | 0.2122 | 0.2039 |
| gen1_sr | 3523 | 1.057 ± 0.057 | 1.222 | 0.1329 | 0.166 | 0.2274 | 0.2037 |
| gen1_ledger | 5544 | 0.883 ± 0.033 | 1.09 | 0.1786 | 0.1801 | 0.2181 | 0.1989 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 17,393)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,000 | 23.0% |
| STALE_QUOTE | market_freshness | 3,568 | 20.5% |
| BOOK_QUALITY | execution | 3,426 | 19.7% |
| POOR_DATA | data | 1,981 | 11.4% |
| LIMITED_DATA | data | 1,188 | 6.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 902 | 5.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 871 | 5.0% |
| IDENTITY_AMBIGUOUS | mapping | 709 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 491 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 257 | 1.5% |

Cause class: coverage 23.0%, market_freshness 20.5%, execution 19.7%, data 18.2%, market_freshness/coverage 8.0%, model_calibration_or_unknown 5.0%, mapping 4.1%, model_calibration 1.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.4%, START_UNVERIFIABLE 94.2%, LOW_DATA_QUALITY 70.2%, THIN_PLAYER_HISTORY 58.7%, STALE_PLAYER_DATA 52.6%, STALE_KALSHI_QUOTE 43.0%, MODEL_INTERNAL_DISAGREEMENT 41.1%, ASYMMETRIC_SAMPLE_SIZE 32.6%, WIDE_SPREAD 25.7%, MODEL_HIGH_UNCERTAINTY 18.0%, PLAYER_IDENTITY_RISK 15.1%, LEVEL_TRANSFER_RISK 9.9%, EVENT_MAPPING_RISK 8.4%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 2.5%, UNKNOWN 1.0%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.4%, POST_SETTLEMENT_OBSERVATION 23.0%, POSSIBLE_IN_PLAY_QUOTE 5.5%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 9,223)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,162 | 34.3% |
| BOOK_QUALITY | execution | 1,801 | 19.5% |
| STALE_QUOTE | market_freshness | 1,640 | 17.8% |
| POOR_DATA | data | 827 | 9.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 479 | 5.2% |
| IDENTITY_AMBIGUOUS | mapping | 409 | 4.4% |
| LIMITED_DATA | data | 350 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 303 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 196 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 56 | 0.6% |

Cause class: coverage 34.3%, execution 19.5%, market_freshness 17.8%, data 12.8%, market_freshness/coverage 8.5%, mapping 4.4%, model_calibration_or_unknown 2.1%, model_calibration 0.6%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.6%, START_UNVERIFIABLE 97.2%, LOW_DATA_QUALITY 74.2%, THIN_PLAYER_HISTORY 61.4%, STALE_KALSHI_QUOTE 51.0%, STALE_PLAYER_DATA 48.0%, MODEL_INTERNAL_DISAGREEMENT 42.0%, ASYMMETRIC_SAMPLE_SIZE 34.7%, WIDE_SPREAD 25.5%, PLAYER_IDENTITY_RISK 18.6%, MODEL_HIGH_UNCERTAINTY 18.2%, EVENT_MAPPING_RISK 10.2%, LEVEL_TRANSFER_RISK 8.9%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 5.1%, EXTERNAL_MARKET_REJECTION 1.4%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.1%, POST_SETTLEMENT_OBSERVATION 34.3%, POSSIBLE_IN_PLAY_QUOTE 5.6%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 7267, "IDENTITY_AMBIGUOUS": 1956}; ticker orientation: {"VERIFIED": 9223}.

Checks: discipline:AMBIGUOUS 661, discipline:PASS 8562, identity_confidence:AMBIGUOUS 1711, identity_confidence:PASS 7512, level_mapping:NA 673, level_mapping:PASS 8550, market_pair:AMBIGUOUS 342, market_pair:NA 219, market_pair:PASS 8662, model_complement:NA 186, model_complement:PASS 9037, namesake:PASS 9223, physical_match_id:NA 3512, physical_match_id:PASS 5711, player_ids:PASS 9223, same_pair_other_event:PASS 9223, ticker_orientation:PASS 9223

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,297 | 4.4% | 4.1% | 1.6% | {"market_freshness": 47, "model_calibration_or_unknown": 30, "data": 29, "execution": 17, "market_freshness/coverage": 10, "model_calibration": 10, "coverage": 2} | 5.84 | 0.2198 / 0.2114 (357) | 18.4% | 3.5% | 3.8% | 2.4% |
| CHALLENGER | 6,817 | 17.0% | 6.6% | 12.6% | {"coverage": 667, "market_freshness/coverage": 145, "market_freshness": 135, "data": 103, "model_calibration_or_unknown": 53, "execution": 28, "model_calibration": 16, "mapping": 14} | 7.36 | 0.2175 / 0.2064 (1674) | 35.2% | 16.2% | 3.6% | 22.3% |
| DOUBLES | 1,357 | 48.7% | 48.3% | 7.2% | {"execution": 327, "mapping": 176, "market_freshness": 106, "market_freshness/coverage": 45, "coverage": 7} | 24.07 | 0.3206 / 0.2346 (352) | 17.2% | 0.0% | 100.0% | 7.1% |
| ITF_MEN | 11,498 | 24.7% | 17.2% | 30.8% | {"coverage": 1077, "execution": 592, "market_freshness": 444, "data": 386, "market_freshness/coverage": 222, "mapping": 118, "model_calibration_or_unknown": 2} | 11.36 | 0.2153 / 0.1951 (2688) | 35.9% | 63.7% | 15.1% | 22.1% |
| ITF_WOMEN | 15,582 | 26.4% | 19.7% | 44.6% | {"coverage": 1392, "market_freshness": 832, "execution": 806, "data": 625, "market_freshness/coverage": 311, "mapping": 95, "model_calibration_or_unknown": 45, "model_calibration": 10} | 12.88 | 0.2014 / 0.1937 (3081) | 37.6% | 58.2% | 10.3% | 21.3% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,454 | 4.6% | 4.2% | 1.2% | {"market_freshness": 36, "model_calibration_or_unknown": 25, "execution": 17, "data": 11, "market_freshness/coverage": 10, "model_calibration": 9, "coverage": 4, "mapping": 1} | 7.83 | 0.2385 / 0.2317 (385) | 23.6% | 1.4% | 1.5% | 3.5% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.9% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 5 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 6 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 7 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 8 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 9 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 10 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 207 min (STALE); no external reference |
| 11 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 12 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 13 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 14 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 15 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 16 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 17 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 18 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 19 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 20 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 21 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 22 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 23 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 24 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 25 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 26 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 27 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 28 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 29 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 30 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 12.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 768 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 31 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 32 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 33 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 34 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 35 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 162 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 36 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 37 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 38 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 39 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 40 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 246 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |
| 41 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 42 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 547 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 43 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 44 | `KXITFWMATCH-26OCT16ESTLAB-LAB` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 68 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1475.0, ratio 2.28); no external reference |
| 45 | `KXITFWMATCH-26OCT19VLABOU-VLA` | ITF_WOMEN | fair_v1 | 77% / 2% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.2h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 140 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 3.13); no external reference |
| 46 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 47 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 48 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 49 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.8h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 359 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 50 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9721, "by_level_share_of_ge_25pp": {"ATP": 0.0157, "CHALLENGER": 0.1259, "DOUBLES": 0.0717, "ITF_MEN": 0.308, "ITF_WOMEN": 0.4463, "OTHER": 0.0013, "WTA": 0.0123, "WTA125": 0.0189}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5105, "share_primary_cause_market_settled_or_in_play": 0.4276, "share_primary_cause_stale_quote_only": 0.1778}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 9223, "identity_ambiguous_share": 0.2121, "ticker_orientation": {"VERIFIED": 9223}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 5711, "with_external": 257, "coverage": 0.045, "external_status": {"EXTERNAL_STALE": 170, "AGREES_WITH_KALSHI": 84, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 170, "MODEL_LONE_OUTLIER": 84, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3268, "share_external_supports_model": 0.0117}, "pregame_clean_ge_25pp": {"n": 2797, "with_external": 243, "coverage": 0.0869, "external_status": {"EXTERNAL_STALE": 158, "AGREES_WITH_KALSHI": 82, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 158, "MODEL_LONE_OUTLIER": 82, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3374, "share_external_supports_model": 0.0123}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 514.0, "median_sample_ratio": 2.47, "median_min_matches": 20.0, "median_max_days_since_last": 220.0, "share_severe_asymmetry": 0.2095, "data_status": {"POOR": 5057, "LIMITED": 2564, "ADEQUATE": 1602}, "comparison_lt_10pp": {"median_thinner_serve_points": 1787.0, "median_sample_ratio": 1.67, "median_min_matches": 94.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 709, "model_minus_observed": 0.05, "kalshi_minus_observed": -0.0847, "brier_diff_model_minus_kalshi": 0.0003}, "4-10x": {"n": 487, "model_minus_observed": 0.0772, "kalshi_minus_observed": -0.065, "brier_diff_model_minus_kalshi": 0.0079}, "<2x": {"n": 1735, "model_minus_observed": 0.0873, "kalshi_minus_observed": -0.034, "brier_diff_model_minus_kalshi": 0.012}, ">=10x": {"n": 592, "model_minus_observed": 0.1146, "kalshi_minus_observed": -0.0596, "brier_diff_model_minus_kalshi": 0.0118}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3523, "model": {"intercept": -0.527, "slope": 0.85, "slope_se": 0.044}, "kalshi_mid_same_rows": {"intercept": 0.245, "slope": 1.147, "slope_se": 0.05}, "mean_extremity_model": 0.1727, "mean_extremity_kalshi": 0.1642, "model_brier": 0.2314, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0275, "brier_diff_se": 0.0032, "model_logloss": 0.6593, "kalshi_logloss": 0.5901}, "fair_v1": {"n": 3523, "model": {"intercept": -0.401, "slope": 1.057, "slope_se": 0.048}, "kalshi_mid_same_rows": {"intercept": 0.322, "slope": 1.189, "slope_se": 0.051}, "mean_extremity_model": 0.1671, "mean_extremity_kalshi": 0.1638, "model_brier": 0.213, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0091, "brier_diff_se": 0.0026, "model_logloss": 0.6138, "kalshi_logloss": 0.5901}, "gen1_elo": {"n": 3523, "model": {"intercept": -0.394, "slope": 1.034, "slope_se": 0.046}, "kalshi_mid_same_rows": {"intercept": 0.314, "slope": 1.171, "slope_se": 0.05}, "mean_extremity_model": 0.1733, "mean_extremity_kalshi": 0.1641, "model_brier": 0.2122, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0083, "brier_diff_se": 0.0026, "model_logloss": 0.6128, "kalshi_logloss": 0.5901}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.24, "share_ge_15": 0.4374, "median_abs_gap": 12.99, "n": 23799}, "gen1_elo": {"share_ge_25": 0.2367, "share_ge_15": 0.4335, "median_abs_gap": 12.66, "n": 23799}, "gen1_sr": {"share_ge_25": 0.3027, "share_ge_15": 0.5171, "median_abs_gap": 15.61, "n": 23799}, "gen2": {"share_ge_25": 0.3064, "share_ge_15": 0.507, "median_abs_gap": 15.38, "n": 23799}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1506, "share_ge_15": 0.3546, "median_abs_gap": 10.82, "n": 18569}, "gen1_elo": {"share_ge_25": 0.1506, "share_ge_15": 0.3473, "median_abs_gap": 10.46, "n": 18567}, "gen1_sr": {"share_ge_25": 0.213, "share_ge_15": 0.4419, "median_abs_gap": 13.06, "n": 18569}, "gen2": {"share_ge_25": 0.2291, "share_ge_15": 0.443, "median_abs_gap": 13.07, "n": 18570}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.84, "share_ge_25_all": 0.044, "share_ge_25_pregame_clean": 0.0413}, "WTA": {"median_abs_gap_pregame_clean": 7.83, "share_ge_25_all": 0.046, "share_ge_25_pregame_clean": 0.0418}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.238, "share_within_10pp_all": 0.4368, "share_within_10pp_pregame_clean": 0.4888, "corr_model_vs_mid_pregame_clean": 0.8431}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 533, "model_brier": 0.196, "kalshi_brier": 0.1973, "brier_diff_model_minus_kalshi": -0.0013}, "10-15": {"n_settled": 624, "model_brier": 0.2145, "kalshi_brier": 0.206, "brier_diff_model_minus_kalshi": 0.0086}, "15-25": {"n_settled": 774, "model_brier": 0.2275, "kalshi_brier": 0.2147, "brier_diff_model_minus_kalshi": 0.0128}, "25-40": {"n_settled": 438, "model_brier": 0.2236, "kalshi_brier": 0.2081, "brier_diff_model_minus_kalshi": 0.0155}, "3-5": {"n_settled": 339, "model_brier": 0.1984, "kalshi_brier": 0.1976, "brier_diff_model_minus_kalshi": 0.0008}, "40+": {"n_settled": 87, "model_brier": 0.297, "kalshi_brier": 0.1766, "brier_diff_model_minus_kalshi": 0.1204}, "5-10": {"n_settled": 728, "model_brier": 0.199, "kalshi_brier": 0.1993, "brier_diff_model_minus_kalshi": -0.0002}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.527, "slope": 0.85, "slope_se": 0.044}, "kalshi_slope": {"intercept": 0.245, "slope": 1.147, "slope_se": 0.05}, "n": 3523}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.514, "slope": 0.883, "slope_se": 0.033}, "kalshi_slope": {"intercept": 0.156, "slope": 1.09, "slope_se": 0.038}, "n": 5544}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 352, "model_brier": 0.3206, "kalshi_brier": 0.2346, "brier_diff_model_minus_kalshi": 0.0861, "brier_diff_se": 0.0167, "corr_model_outcome": 0.0143, "corr_kalshi_outcome": 0.2592}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
