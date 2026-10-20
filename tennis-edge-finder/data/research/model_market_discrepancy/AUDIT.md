# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-20T16:17Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 44,271): 0-3 14.2%, 3-5 9.5%, 5-10 19.8%, 10-15 15.4%, 15-25 19.3%, 25-40 13.9%, 40+ 7.9%; median gap 11.96 pp.
* **Where the extremes live**: 97.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 75.7%, Challenger 12.6%, doubles 6.9%). Main tour: ATP 4.8% and WTA 4.6% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 9,653): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.0%, BOOK_QUALITY 19.2%, STALE_QUOTE 17.7%, POOR_DATA 9.1%, POSSIBLY_IN_PLAY_QUOTE 5.3%, IDENTITY_AMBIGUOUS 4.4%, LIMITED_DATA 3.9%, IN_PLAY_QUOTE 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%. By class: coverage 34.0%, execution 19.2%, market_freshness 17.7%, data 13.0%, market_freshness/coverage 8.7%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.7%.
* **Stale / settled / in-play**: 50.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.7% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 9,653 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.7%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 24.5% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 507.0 points vs 1759.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.045, Gen-2 0.845, Gen-1 ledger 0.872 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 461 model 0.2251 vs Kalshi 0.2086; n 92 model 0.3021 vs Kalshi 0.176.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 188,672 model-market comparisons (306,328 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 65,500 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-20T16:08:40.683146+00:00'], shadow board 49,456 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-20T16:08:44.565994+00:00'], Model 4 23,581 rows, 17,499 settled tickers, 5,959 tickers with an external scan.
* By model: {"gen1_ledger": 44185, "gen1_elo": 24864, "fair_v1": 24864, "gen2": 24864, "gen1_sr": 24864, "model4_fundamental": 22526, "model4_conditioned": 22505}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 44,271 | 14.2 | 9.5 | 19.8 | 15.4 | 19.3 | 13.9 | 7.9 | 11.96 | 41.1% | 21.8% |
| MW fair_v1 | 24,864 | 13.3 | 8.6 | 18.3 | 15.7 | 19.9 | 14.7 | 9.4 | 13.04 | 44.0% | 24.1% |
| MW gen1_elo | 24,864 | 13.0 | 8.8 | 19.3 | 15.2 | 19.8 | 14.7 | 9.2 | 12.73 | 43.6% | 23.8% |
| MW gen1_ledger | 19,407 | 15.4 | 10.7 | 21.7 | 14.9 | 18.5 | 12.8 | 6.0 | 10.54 | 37.3% | 18.8% |
| MW gen1_sr | 24,864 | 10.0 | 7.2 | 16.7 | 14.2 | 21.4 | 18.6 | 11.9 | 15.68 | 51.9% | 30.5% |
| MW gen2 | 24,864 | 11.2 | 7.4 | 16.3 | 14.2 | 20.1 | 17.7 | 13.1 | 15.45 | 50.9% | 30.8% |
| all families model4_conditioned | 22,505 | 21.9 | 19.2 | 34.3 | 17.6 | 4.6 | 1.4 | 1.1 | 5.92 | 7.0% | 2.4% |
| all families model4_fundamental | 22,526 | 16.2 | 13.0 | 34.2 | 20.4 | 11.4 | 3.4 | 1.3 | 7.91 | 16.1% | 4.7% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.5%, >=15pp 41.1%, >=20pp 30.4%, >=25pp 21.8%, >=30pp 15.6%, >=40pp 7.9%, >=50pp 3.6%
Executable gap (model outside the book, before fees): median 8.37pp; >=10pp 45.0%, >=25pp 16.9%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,196 | 28.3 | 13.9 | 24.8 | 15.4 | 11.9 | 5.0 | 0.6 | 6.28 | 17.5% | 5.6% |
| CHALLENGER | 4,186 | 15.7 | 10.2 | 20.3 | 15.9 | 14.9 | 12.4 | 10.7 | 11.16 | 38.0% | 23.1% |
| ITF_MEN | 6,548 | 11.0 | 7.8 | 17.1 | 14.5 | 20.7 | 16.9 | 12.2 | 14.93 | 49.7% | 29.0% |
| ITF_WOMEN | 9,752 | 9.8 | 6.8 | 15.6 | 15.6 | 23.1 | 18.1 | 10.9 | 15.74 | 52.2% | 29.1% |
| WTA | 1,522 | 17.4 | 12.5 | 24.2 | 20.1 | 20.8 | 4.3 | 0.7 | 8.84 | 25.8% | 5.1% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,196 | 23.3 | 15.0 | 24.6 | 17.1 | 13.9 | 5.2 | 0.8 | 6.76 | 20.0% | 6.1% |
| CHALLENGER | 4,186 | 14.6 | 8.5 | 19.0 | 14.4 | 17.9 | 14.0 | 11.7 | 12.63 | 43.5% | 25.7% |
| ITF_MEN | 6,548 | 9.1 | 6.5 | 15.1 | 13.3 | 19.7 | 20.2 | 16.1 | 17.65 | 56.0% | 36.3% |
| ITF_WOMEN | 9,752 | 8.2 | 5.6 | 13.5 | 13.6 | 21.6 | 20.9 | 16.6 | 18.89 | 59.1% | 37.5% |
| WTA | 1,522 | 14.7 | 9.5 | 19.9 | 16.3 | 24.5 | 14.3 | 0.8 | 11.72 | 39.6% | 15.1% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,196 | 23.7 | 13.2 | 24.6 | 16.0 | 15.2 | 6.2 | 1.0 | 7.17 | 22.4% | 7.2% |
| CHALLENGER | 4,186 | 14.4 | 9.6 | 21.2 | 15.2 | 16.0 | 12.6 | 11.0 | 11.29 | 39.7% | 23.6% |
| ITF_MEN | 6,548 | 10.2 | 7.8 | 17.3 | 14.0 | 21.3 | 17.2 | 12.2 | 15.3 | 50.7% | 29.4% |
| ITF_WOMEN | 9,752 | 9.4 | 6.8 | 16.3 | 15.7 | 23.4 | 18.4 | 10.1 | 15.62 | 51.8% | 28.4% |
| WTA | 1,522 | 24.4 | 16.7 | 30.2 | 15.8 | 10.2 | 2.2 | 0.5 | 6.0 | 12.9% | 2.7% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,252 | 26.5 | 19.9 | 29.7 | 12.0 | 8.5 | 3.0 | 0.4 | 5.38 | 11.9% | 3.4% |
| CHALLENGER | 2,938 | 21.3 | 14.6 | 27.0 | 14.1 | 14.7 | 6.4 | 1.9 | 7.28 | 23.0% | 8.3% |
| DOUBLES | 1,375 | 4.6 | 4.1 | 11.5 | 10.5 | 20.9 | 26.0 | 22.6 | 24.11 | 69.4% | 48.5% |
| ITF_MEN | 5,411 | 14.2 | 8.7 | 20.6 | 15.9 | 20.4 | 13.3 | 6.8 | 11.94 | 40.6% | 20.1% |
| ITF_WOMEN | 6,545 | 12.2 | 8.9 | 19.2 | 15.2 | 21.8 | 16.5 | 6.1 | 13.04 | 44.5% | 22.6% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,005 | 22.2 | 15.8 | 29.6 | 18.1 | 10.3 | 3.7 | 0.3 | 6.98 | 14.3% | 4.0% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,146 | 28.5 | 14.1 | 25.1 | 15.3 | 11.7 | 4.8 | 0.6 | 6.17 | 17.0% | 5.3% |
| CHALLENGER | 2,978 | 20.4 | 12.5 | 25.0 | 18.3 | 15.3 | 6.6 | 2.0 | 8.41 | 23.9% | 8.6% |
| ITF_MEN | 4,807 | 13.4 | 9.5 | 20.3 | 16.4 | 21.2 | 13.7 | 5.5 | 11.98 | 40.4% | 19.2% |
| ITF_WOMEN | 7,345 | 11.5 | 8.1 | 17.6 | 17.7 | 24.9 | 15.3 | 4.9 | 13.52 | 45.1% | 20.2% |
| WTA | 1,481 | 17.6 | 12.2 | 24.1 | 20.3 | 20.7 | 4.3 | 0.7 | 8.85 | 25.8% | 5.1% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,146 | 23.5 | 15.3 | 24.7 | 17.0 | 13.8 | 5.0 | 0.7 | 6.61 | 19.5% | 5.7% |
| CHALLENGER | 2,978 | 18.2 | 10.9 | 23.6 | 17.3 | 18.1 | 9.6 | 2.3 | 9.27 | 30.0% | 11.9% |
| ITF_MEN | 4,808 | 10.7 | 7.7 | 17.4 | 15.1 | 21.7 | 18.2 | 9.2 | 14.66 | 49.1% | 27.4% |
| ITF_WOMEN | 7,345 | 9.2 | 6.4 | 14.8 | 15.0 | 23.7 | 20.4 | 10.6 | 16.7 | 54.6% | 30.9% |
| WTA | 1,481 | 14.7 | 9.5 | 19.9 | 16.1 | 24.5 | 14.5 | 0.8 | 11.75 | 39.8% | 15.3% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,212 | 26.7 | 20.1 | 29.8 | 12.2 | 8.0 | 2.9 | 0.2 | 5.32 | 11.1% | 3.1% |
| CHALLENGER | 2,562 | 22.8 | 15.7 | 28.7 | 14.0 | 14.0 | 4.2 | 0.6 | 6.71 | 18.9% | 4.8% |
| DOUBLES | 1,278 | 4.6 | 4.2 | 11.7 | 10.6 | 20.8 | 26.1 | 21.9 | 24.06 | 68.9% | 48.0% |
| ITF_MEN | 4,507 | 15.5 | 9.5 | 22.5 | 16.6 | 20.1 | 11.6 | 4.1 | 10.74 | 35.9% | 15.8% |
| ITF_WOMEN | 5,461 | 13.1 | 9.4 | 20.7 | 16.0 | 22.0 | 15.3 | 3.5 | 11.85 | 40.8% | 18.8% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 958 | 22.6 | 16.3 | 29.6 | 18.2 | 10.3 | 2.9 | 0.0 | 6.82 | 13.3% | 2.9% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,375 | 4.6 | 4.1 | 11.5 | 10.5 | 20.9 | 26.0 | 22.6 | 24.11 | 69.4% | 48.5% |
| singles | 18,032 | 16.3 | 11.2 | 22.4 | 15.3 | 18.3 | 11.8 | 4.7 | 10.02 | 34.8% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 5,615 | 13.4 | 8.9 | 19.4 | 15.7 | 18.6 | 14.6 | 9.3 | 12.64 | 42.6% | 24.0% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 15,791 | 13.6 | 8.6 | 18.3 | 15.4 | 20.2 | 14.5 | 9.4 | 13.05 | 44.1% | 23.9% |
| UNKNOWN | 3,221 | 11.7 | 8.0 | 16.7 | 17.4 | 20.5 | 15.8 | 10.0 | 13.59 | 46.3% | 25.8% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,210 | 19.7 | 11.5 | 21.2 | 16.9 | 16.0 | 8.9 | 5.8 | 9.3 | 30.7% | 14.7% |
| B | 3,197 | 12.7 | 9.1 | 20.1 | 17.2 | 18.7 | 11.8 | 10.3 | 12.12 | 40.9% | 22.2% |
| C | 3,489 | 12.4 | 8.9 | 18.9 | 14.7 | 19.8 | 15.3 | 9.9 | 13.14 | 45.1% | 25.2% |
| D | 4,089 | 12.3 | 7.9 | 16.9 | 15.6 | 22.1 | 15.7 | 9.5 | 13.98 | 47.3% | 25.2% |
| F | 6,879 | 7.9 | 5.6 | 15.1 | 14.4 | 23.2 | 21.2 | 12.6 | 17.78 | 57.0% | 33.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,555 | 23.2 | 15.8 | 28.5 | 15.1 | 11.8 | 4.1 | 1.5 | 6.68 | 17.3% | 5.6% |
| B | 2,720 | 15.9 | 10.4 | 24.1 | 16.1 | 18.8 | 10.8 | 3.9 | 9.9 | 33.5% | 14.7% |
| C | 3,815 | 10.9 | 7.2 | 18.4 | 14.4 | 21.8 | 16.3 | 10.9 | 14.46 | 49.0% | 27.2% |
| D | 2,798 | 14.0 | 9.7 | 19.8 | 14.7 | 21.0 | 14.7 | 6.2 | 12.09 | 41.9% | 20.8% |
| F | 4,519 | 10.4 | 7.9 | 15.8 | 14.5 | 22.2 | 20.7 | 8.6 | 15.76 | 51.4% | 29.2% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 8,174 | 17.9 | 10.3 | 20.6 | 16.9 | 16.4 | 9.7 | 8.2 | 10.32 | 34.3% | 17.8% |
| LIMITED | 5,498 | 14.0 | 10.2 | 20.1 | 15.6 | 19.2 | 13.5 | 7.3 | 11.69 | 40.0% | 20.8% |
| POOR | 11,192 | 9.5 | 6.5 | 15.8 | 15.0 | 22.7 | 19.0 | 11.4 | 16.05 | 53.1% | 30.4% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,810 | 26.7 | 20.9 | 34.5 | 11.8 | 4.3 | 1.5 | 0.2 | 5.19 | 6.0% | 1.7% |
| GAME_SPREAD | 4,204 | 23.1 | 15.3 | 33.4 | 17.1 | 8.5 | 2.3 | 0.3 | 6.54 | 11.1% | 2.6% |
| MATCH_WINNER | 19,407 | 15.4 | 10.7 | 21.7 | 14.9 | 18.5 | 12.8 | 6.0 | 10.54 | 37.3% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 8,918 | 30.0 | 16.9 | 30.4 | 12.6 | 8.1 | 1.6 | 0.4 | 5.39 | 10.2% | 2.0% |
| TOTAL_GAMES | 6,822 | 7.9 | 9.2 | 36.6 | 29.1 | 10.9 | 3.4 | 2.9 | 9.6 | 17.2% | 6.3% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,876 | 25.4 | 34.8 | 32.1 | 3.9 | 3.2 | 0.6 | 0.1 | 4.44 | 3.9% | 0.7% |
| GAME_SPREAD | 5,394 | 46.1 | 16.9 | 26.8 | 7.5 | 1.8 | 0.6 | 0.2 | 3.38 | 2.7% | 0.9% |
| TOTAL_GAMES | 9,235 | 4.8 | 7.3 | 40.6 | 35.2 | 7.4 | 2.4 | 2.3 | 9.72 | 12.1% | 4.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,879 | 24.3 | 17.9 | 35.5 | 12.3 | 7.2 | 2.6 | 0.3 | 5.8 | 10.1% | 2.9% |
| GAME_SPREAD | 5,397 | 19.1 | 13.3 | 28.3 | 19.9 | 14.4 | 4.2 | 0.9 | 7.97 | 19.5% | 5.0% |
| TOTAL_GAMES | 9,250 | 7.8 | 8.8 | 36.5 | 27.8 | 13.1 | 3.7 | 2.4 | 9.67 | 19.2% | 6.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 24,864 | 44.0% | 24.1% | 13.04 | 35.8% | 15.2% | 10.88 |
| gen1_elo | 24,864 | 43.6% | 23.8% | 12.73 | 35.1% | 15.2% | 10.49 |
| gen1_sr | 24,864 | 51.9% | 30.5% | 15.68 | 44.3% | 21.5% | 13.09 |
| gen2 | 24,864 | 50.9% | 30.8% | 15.45 | 44.5% | 23.1% | 13.09 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 13,216 | 15.9 | 10.4 | 21.1 | 17.3 | 20.4 | 11.6 | 3.3 | 10.72 | 35.2% | 14.9% |
| STALE | 11,648 | 10.3 | 6.6 | 15.2 | 13.9 | 19.4 | 18.2 | 16.5 | 17.04 | 54.0% | 34.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 12,875 | 16.6 | 11.2 | 22.7 | 15.0 | 17.5 | 12.2 | 4.8 | 9.85 | 34.5% | 17.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 44,271 | 12875 | 16688 | 14708 | 23.6 | 125.4 | 1400.4 |
| ge_15pp | 18,185 | 4438 | 5946 | 7801 | 25.7 | 417.9 | 1380.4 |
| ge_25pp | 9,653 | 2187 | 2559 | 4907 | 31.1 | 562.2 | 1380.4 |
| lt_10pp | 19,277 | 6503 | 7902 | 4872 | 21.6 | 47.3 | 1341.5 |

Current slate `SL-20261020T161659Z-b32bfa6e`: 608 priced rows, quote age at build {'median': 8.6, 'max': 8.6}, freshness {'FRESH': 608}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 12 | 0.0 | 0.0 | 33.3 | 0.0 | 50.0 | 16.7 | 0.0 | 20.33 | 66.7% | 16.7% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,349 | 20.0 | 10.9 | 23.2 | 18.8 | 19.4 | 7.1 | 0.7 | 9.15 | 27.2% | 7.8% |
| KALSHI_LONE_OUTLIER | 14 | 7.1 | 7.1 | 71.4 | 0.0 | 7.1 | 7.1 | 0.0 | 5.35 | 14.3% | 7.1% |
| MARKETS_AGREE | 417 | 68.1 | 31.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.14 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 911 | 0.0 | 2.6 | 34.8 | 27.4 | 24.7 | 9.8 | 0.7 | 12.39 | 35.1% | 10.4% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 24,864 | 3715 (14.9%) | 24.5% | 0.7% | {"EXTERNAL_STALE": 2349, "AGREES_WITH_KALSHI": 911, "ALL_AGREE": 417, "AGREES_WITH_MODEL": 14, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 11, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 10,948 | 968 (8.8%) | 33.1% | 1.0% | {"EXTERNAL_STALE": 638, "AGREES_WITH_KALSHI": 320, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 6,004 | 281 (4.7%) | 33.8% | 1.1% | {"EXTERNAL_STALE": 183, "AGREES_WITH_KALSHI": 95, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,944 | 266 (9.0%) | 35.0% | 1.1% | {"EXTERNAL_STALE": 170, "AGREES_WITH_KALSHI": 93, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 10,005 | 2056 (20.5%) | 16.6% | 0.7% | {"EXTERNAL_STALE": 1270, "ALL_AGREE": 417, "AGREES_WITH_KALSHI": 341, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 12, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 4,800 | 10.8 | 7.8 | 19.5 | 14.7 | 22.1 | 15.5 | 9.7 | 13.88 | 47.3% | 25.2% |
| 4-10x | 3,240 | 11.7 | 8.4 | 18.6 | 15.6 | 20.9 | 14.9 | 9.9 | 13.57 | 45.7% | 24.9% |
| <2x | 12,817 | 15.3 | 9.6 | 18.8 | 16.8 | 18.2 | 12.9 | 8.3 | 11.83 | 39.5% | 21.2% |
| >=10x | 4,007 | 11.2 | 6.5 | 15.3 | 13.7 | 21.7 | 19.3 | 12.3 | 16.29 | 53.3% | 31.6% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 6,336 | 12.7 | 8.5 | 19.7 | 16.2 | 19.7 | 13.4 | 9.8 | 12.79 | 42.9% | 23.2% |
| 300-1000 | 5,428 | 12.0 | 8.7 | 16.8 | 15.6 | 21.0 | 16.2 | 9.7 | 13.93 | 46.9% | 25.9% |
| <300 | 7,757 | 9.1 | 5.8 | 15.4 | 14.6 | 22.9 | 20.1 | 12.1 | 16.86 | 55.1% | 32.2% |
| >=3000 | 5,343 | 21.5 | 12.7 | 22.6 | 17.0 | 14.6 | 6.8 | 4.8 | 8.09 | 26.3% | 11.7% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 740 | 0.5444 | 0.4089 | 0.4986 | +0.046 | -0.090 | -0.002 ± 0.0056 |
| ratio 4-10x | 511 | 0.591 | 0.4455 | 0.5029 | +0.088 | -0.058 | 0.0123 ± 0.0072 |
| ratio <2x | 1820 | 0.5367 | 0.4148 | 0.4495 | +0.087 | -0.035 | 0.0123 ± 0.0033 |
| ratio >=10x | 626 | 0.5634 | 0.3905 | 0.4537 | +0.110 | -0.063 | 0.0106 ± 0.0073 |
| thinner_sample 1000-3000 | 1013 | 0.5431 | 0.4174 | 0.4551 | +0.088 | -0.038 | 0.0093 ± 0.0045 |
| thinner_sample 300-1000 | 865 | 0.5662 | 0.4247 | 0.4994 | +0.067 | -0.075 | -0.0001 ± 0.0054 |
| thinner_sample <300 | 1194 | 0.5541 | 0.3895 | 0.4523 | +0.102 | -0.063 | 0.0139 ± 0.0051 |
| thinner_sample >=3000 | 625 | 0.5327 | 0.4388 | 0.472 | +0.061 | -0.033 | 0.0124 ± 0.0046 |
| data_status ADEQUATE | 1070 | 0.5366 | 0.4324 | 0.4607 | +0.076 | -0.028 | 0.0109 ± 0.0038 |
| data_status LIMITED | 892 | 0.5523 | 0.4207 | 0.4832 | +0.069 | -0.062 | 0.0042 ± 0.005 |
| data_status POOR | 1735 | 0.5577 | 0.3986 | 0.4634 | +0.094 | -0.065 | 0.0106 ± 0.0041 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 552 | 0.196 | 0.1974 | -0.0014 ± 0.0007 | 0.5706 | 0.5736 | 0.5001 | 0.4851 | 0.5362 | -0.050 ± 0.0197 | -0.01 (5) |
| 3-5 | 352 | 0.2011 | 0.2008 | +0.0004 ± 0.0019 | 0.5853 | 0.5832 | 0.5051 | 0.4651 | 0.4801 | -0.088 ± 0.0246 | 0.02 (1) |
| 5-10 | 766 | 0.2008 | 0.2011 | -0.0003 ± 0.0025 | 0.5874 | 0.5862 | 0.5122 | 0.4377 | 0.4726 | -0.082 ± 0.0168 | -0.0167 (6) |
| 10-15 | 649 | 0.2128 | 0.2036 | +0.0092 ± 0.0044 | 0.6152 | 0.5888 | 0.5247 | 0.4006 | 0.4253 | -0.097 ± 0.0176 | -0.048 (5) |
| 15-25 | 825 | 0.2265 | 0.215 | +0.0115 ± 0.0063 | 0.6483 | 0.6149 | 0.578 | 0.3823 | 0.4509 | -0.086 ± 0.016 | -0.0033 (9) |
| 25-40 | 461 | 0.2251 | 0.2086 | +0.0165 ± 0.0127 | 0.6387 | 0.5998 | 0.6537 | 0.3455 | 0.4707 | -0.074 ± 0.0193 | -0.01 (1) |
| 40+ | 92 | 0.3021 | 0.176 | +0.1261 ± 0.0392 | 0.8232 | 0.5249 | 0.7541 | 0.3058 | 0.3913 | -0.125 ± 0.0376 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2688 | 0.1803 | 0.1814 | -0.0011 ± 0.0003 | 0.5354 | 0.5367 | 0.4814 | 0.4662 | 0.5019 | -0.021 ± 0.0083 | -0.0129 (17) |
| 3-5 | 1760 | 0.1958 | 0.1947 | +0.0011 ± 0.0009 | 0.5728 | 0.5666 | 0.4815 | 0.4416 | 0.4466 | -0.052 ± 0.0107 | 0.0 (2) |
| 5-10 | 3764 | 0.1962 | 0.1929 | +0.0033 ± 0.0011 | 0.575 | 0.5646 | 0.4853 | 0.4114 | 0.4256 | -0.049 ± 0.0073 | -0.0119 (21) |
| 10-15 | 3278 | 0.2032 | 0.1848 | +0.0184 ± 0.0019 | 0.5942 | 0.5428 | 0.4859 | 0.3615 | 0.3496 | -0.076 ± 0.0075 | -0.0281 (16) |
| 15-25 | 4082 | 0.209 | 0.1719 | +0.0372 ± 0.0025 | 0.6115 | 0.508 | 0.5022 | 0.3058 | 0.3099 | -0.069 ± 0.0064 | -0.0025 (44) |
| 25-40 | 3088 | 0.2234 | 0.1276 | +0.0958 ± 0.004 | 0.6414 | 0.3916 | 0.5316 | 0.2188 | 0.2257 | -0.066 ± 0.0062 | -0.01 (1) |
| 40+ | 2013 | 0.3819 | 0.0423 | +0.3396 ± 0.0052 | 0.9938 | 0.1681 | 0.6307 | 0.1065 | 0.0556 | -0.088 ± 0.0043 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 411 | 0.2008 | 0.2013 | -0.0005 ± 0.0008 | 0.5832 | 0.5844 | 0.501 | 0.4861 | 0.5085 | -0.088 ± 0.0236 | -0.01 (3) |
| 3-5 | 306 | 0.219 | 0.2178 | +0.0011 ± 0.0022 | 0.6234 | 0.6213 | 0.514 | 0.474 | 0.4739 | -0.101 ± 0.0285 | 0.02 (1) |
| 5-10 | 654 | 0.198 | 0.1991 | -0.0011 ± 0.0026 | 0.5793 | 0.5813 | 0.5478 | 0.4727 | 0.5168 | -0.069 ± 0.0179 | -0.01 (4) |
| 10-15 | 613 | 0.2188 | 0.2129 | +0.0060 ± 0.0047 | 0.6279 | 0.6126 | 0.5646 | 0.4403 | 0.4812 | -0.095 ± 0.0193 | -0.04 (5) |
| 15-25 | 883 | 0.2316 | 0.2103 | +0.0213 ± 0.0061 | 0.657 | 0.6035 | 0.5917 | 0.3954 | 0.4439 | -0.099 ± 0.0157 | -0.0133 (9) |
| 25-40 | 611 | 0.2617 | 0.1999 | +0.0618 ± 0.0114 | 0.7311 | 0.5806 | 0.66 | 0.3447 | 0.4059 | -0.111 ± 0.0177 | -0.0075 (4) |
| 40+ | 219 | 0.3665 | 0.1689 | +0.1976 ± 0.0275 | 1.0138 | 0.5053 | 0.7383 | 0.2566 | 0.3059 | -0.088 ± 0.0267 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2258 | 0.1856 | 0.1861 | -0.0005 ± 0.0003 | 0.5477 | 0.5487 | 0.5008 | 0.4859 | 0.5097 | -0.033 ± 0.0094 | -0.0133 (15) |
| 3-5 | 1527 | 0.1975 | 0.1972 | +0.0002 ± 0.0009 | 0.5726 | 0.5717 | 0.5113 | 0.4713 | 0.4866 | -0.037 ± 0.0116 | 0.02 (1) |
| 5-10 | 3326 | 0.1916 | 0.1907 | +0.0009 ± 0.0011 | 0.5658 | 0.5599 | 0.5062 | 0.4321 | 0.4645 | -0.029 ± 0.0077 | -0.0117 (6) |
| 10-15 | 2929 | 0.2005 | 0.1893 | +0.0112 ± 0.002 | 0.5887 | 0.5513 | 0.5154 | 0.3912 | 0.4104 | -0.051 ± 0.0081 | -0.0189 (18) |
| 15-25 | 4169 | 0.2182 | 0.1793 | +0.0389 ± 0.0026 | 0.6341 | 0.5271 | 0.5302 | 0.3339 | 0.3365 | -0.072 ± 0.0066 | -0.0086 (42) |
| 25-40 | 3662 | 0.2498 | 0.1385 | +0.1113 ± 0.0039 | 0.7049 | 0.4237 | 0.563 | 0.247 | 0.2307 | -0.086 ± 0.0061 | -0.0044 (18) |
| 40+ | 2802 | 0.4004 | 0.0637 | +0.3367 ± 0.0055 | 1.0552 | 0.2248 | 0.6603 | 0.1243 | 0.091 | -0.073 ± 0.0047 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 528 | 0.1991 | 0.2015 | -0.0024 ± 0.0007 | 0.5789 | 0.5848 | 0.4975 | 0.4821 | 0.5549 | -0.014 ± 0.0199 | -0.0137 (8) |
| 3-5 | 386 | 0.1948 | 0.1928 | +0.0020 ± 0.0018 | 0.5674 | 0.5627 | 0.5037 | 0.4642 | 0.4611 | -0.117 ± 0.0234 | 0.0067 (3) |
| 5-10 | 796 | 0.2012 | 0.1986 | +0.0026 ± 0.0024 | 0.5894 | 0.5797 | 0.5101 | 0.4361 | 0.4523 | -0.094 ± 0.0162 | -0.0071 (7) |
| 10-15 | 643 | 0.2084 | 0.2048 | +0.0036 ± 0.0044 | 0.6044 | 0.592 | 0.5387 | 0.4154 | 0.465 | -0.082 ± 0.0176 | -0.0317 (6) |
| 15-25 | 772 | 0.2336 | 0.2121 | +0.0215 ± 0.0064 | 0.6664 | 0.6079 | 0.5851 | 0.3914 | 0.4326 | -0.111 ± 0.0165 | -0.03 (1) |
| 25-40 | 478 | 0.2133 | 0.2165 | -0.0031 ± 0.0125 | 0.6135 | 0.6181 | 0.6628 | 0.3522 | 0.5105 | -0.051 ± 0.019 | 0.015 (2) |
| 40+ | 94 | 0.3174 | 0.1917 | +0.1257 ± 0.0406 | 0.8659 | 0.5602 | 0.7616 | 0.3091 | 0.4043 | -0.111 ± 0.0415 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2623 | 0.1876 | 0.1884 | -0.0008 ± 0.0003 | 0.5517 | 0.5532 | 0.4898 | 0.4745 | 0.4933 | -0.035 ± 0.0085 | -0.0163 (35) |
| 3-5 | 1806 | 0.1868 | 0.184 | +0.0028 ± 0.0008 | 0.5511 | 0.5442 | 0.4841 | 0.4446 | 0.4302 | -0.075 ± 0.0104 | -0.0094 (18) |
| 5-10 | 3928 | 0.1964 | 0.1905 | +0.0059 ± 0.001 | 0.5774 | 0.5578 | 0.4853 | 0.4114 | 0.4066 | -0.065 ± 0.007 | -0.01 (31) |
| 10-15 | 3129 | 0.1969 | 0.1801 | +0.0168 ± 0.0019 | 0.5785 | 0.5307 | 0.5026 | 0.3789 | 0.3733 | -0.072 ± 0.0075 | -0.015 (12) |
| 15-25 | 4167 | 0.2125 | 0.1728 | +0.0397 ± 0.0025 | 0.6197 | 0.5103 | 0.5082 | 0.3134 | 0.3091 | -0.076 ± 0.0064 | -0.03 (2) |
| 25-40 | 3064 | 0.2189 | 0.1276 | +0.0913 ± 0.0041 | 0.6314 | 0.3905 | 0.5323 | 0.2165 | 0.233 | -0.060 ± 0.0061 | 0.01 (3) |
| 40+ | 1956 | 0.3974 | 0.0475 | +0.3498 ± 0.0055 | 1.0377 | 0.1821 | 0.6427 | 0.1129 | 0.0598 | -0.090 ± 0.0047 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 889 | 0.1962 | 0.1964 | -0.0002 ± 0.0005 | 0.5725 | 0.5728 | 0.5079 | 0.4928 | 0.4972 | -0.057 ± 0.015 | -0.0224 (49) |
| 3-5 | 620 | 0.1927 | 0.1922 | +0.0005 ± 0.0014 | 0.5629 | 0.5607 | 0.4833 | 0.4435 | 0.4548 | -0.052 ± 0.0178 | -0.0194 (34) |
| 5-10 | 1315 | 0.2004 | 0.194 | +0.0063 ± 0.0018 | 0.5888 | 0.57 | 0.491 | 0.4177 | 0.4129 | -0.070 ± 0.0124 | -0.005 (78) |
| 10-15 | 845 | 0.2082 | 0.1978 | +0.0105 ± 0.0038 | 0.6047 | 0.5771 | 0.5138 | 0.3906 | 0.4083 | -0.061 ± 0.0155 | 0.0014 (64) |
| 15-25 | 1135 | 0.2306 | 0.211 | +0.0196 ± 0.0054 | 0.6588 | 0.6081 | 0.5713 | 0.3765 | 0.4256 | -0.061 ± 0.0137 | -0.0214 (59) |
| 25-40 | 684 | 0.2507 | 0.2024 | +0.0483 ± 0.0106 | 0.7092 | 0.5841 | 0.6617 | 0.3491 | 0.4269 | -0.089 ± 0.016 | -0.0219 (26) |
| 40+ | 236 | 0.354 | 0.1958 | +0.1581 ± 0.0288 | 1.0221 | 0.5734 | 0.8041 | 0.3186 | 0.4195 | -0.085 ± 0.0256 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2861 | 0.1849 | 0.1849 | -0.0001 ± 0.0003 | 0.5436 | 0.5431 | 0.5087 | 0.4934 | 0.5012 | -0.039 ± 0.0081 | -0.0157 (88) |
| 3-5 | 1974 | 0.1895 | 0.1875 | +0.0020 ± 0.0008 | 0.555 | 0.5505 | 0.4879 | 0.4482 | 0.4433 | -0.053 ± 0.0098 | -0.0209 (69) |
| 5-10 | 3961 | 0.1971 | 0.1885 | +0.0086 ± 0.001 | 0.5796 | 0.5551 | 0.488 | 0.4146 | 0.3956 | -0.071 ± 0.007 | -0.0082 (132) |
| 10-15 | 2743 | 0.2055 | 0.19 | +0.0155 ± 0.0021 | 0.5995 | 0.5581 | 0.5197 | 0.3966 | 0.3948 | -0.062 ± 0.0083 | -0.0053 (105) |
| 15-25 | 3372 | 0.2273 | 0.1972 | +0.0301 ± 0.003 | 0.6564 | 0.5739 | 0.5626 | 0.3675 | 0.39 | -0.061 ± 0.0077 | -0.0253 (107) |
| 25-40 | 2347 | 0.2593 | 0.1784 | +0.0809 ± 0.0055 | 0.7339 | 0.5227 | 0.6227 | 0.3083 | 0.3404 | -0.080 ± 0.0085 | -0.0229 (51) |
| 40+ | 1074 | 0.3805 | 0.1371 | +0.2434 ± 0.012 | 1.0779 | 0.4172 | 0.7232 | 0.2196 | 0.243 | -0.078 ± 0.0105 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3697 | 1.045 ± 0.047 | 1.171 | 0.1668 | 0.1651 | 0.2135 | 0.2044 |
| gen2 | 3697 | 0.845 ± 0.043 | 1.131 | 0.1715 | 0.1655 | 0.232 | 0.2042 |
| gen1_elo | 3697 | 1.022 ± 0.045 | 1.154 | 0.1731 | 0.1654 | 0.2128 | 0.2044 |
| gen1_sr | 3697 | 1.047 ± 0.056 | 1.207 | 0.1318 | 0.1675 | 0.2281 | 0.2039 |
| gen1_ledger | 5724 | 0.872 ± 0.032 | 1.086 | 0.1795 | 0.1803 | 0.2184 | 0.1992 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 18,185)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,130 | 22.7% |
| STALE_QUOTE | market_freshness | 3,732 | 20.5% |
| BOOK_QUALITY | execution | 3,536 | 19.4% |
| POOR_DATA | data | 2,096 | 11.5% |
| LIMITED_DATA | data | 1,237 | 6.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 980 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 926 | 5.1% |
| IDENTITY_AMBIGUOUS | mapping | 733 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 532 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 283 | 1.6% |

Cause class: coverage 22.7%, market_freshness 20.5%, execution 19.4%, data 18.3%, market_freshness/coverage 8.3%, model_calibration_or_unknown 5.1%, mapping 4.0%, model_calibration 1.6%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.2%, START_UNVERIFIABLE 94.1%, LOW_DATA_QUALITY 70.3%, THIN_PLAYER_HISTORY 59.1%, STALE_PLAYER_DATA 52.7%, STALE_KALSHI_QUOTE 42.9%, MODEL_INTERNAL_DISAGREEMENT 41.6%, ASYMMETRIC_SAMPLE_SIZE 32.7%, WIDE_SPREAD 25.3%, MODEL_HIGH_UNCERTAINTY 17.9%, PLAYER_IDENTITY_RISK 15.2%, LEVEL_TRANSFER_RISK 10.4%, EVENT_MAPPING_RISK 8.2%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 2.7%, UNKNOWN 1.0%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.2%, POST_SETTLEMENT_OBSERVATION 22.7%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 9,653)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,281 | 34.0% |
| BOOK_QUALITY | execution | 1,852 | 19.2% |
| STALE_QUOTE | market_freshness | 1,712 | 17.7% |
| POOR_DATA | data | 880 | 9.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 512 | 5.3% |
| IDENTITY_AMBIGUOUS | mapping | 423 | 4.4% |
| LIMITED_DATA | data | 378 | 3.9% |
| IN_PLAY_QUOTE | market_freshness/coverage | 332 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 216 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 67 | 0.7% |

Cause class: coverage 34.0%, execution 19.2%, market_freshness 17.7%, data 13.0%, market_freshness/coverage 8.7%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.7%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.4%, START_UNVERIFIABLE 97.1%, LOW_DATA_QUALITY 74.3%, THIN_PLAYER_HISTORY 61.8%, STALE_KALSHI_QUOTE 50.8%, STALE_PLAYER_DATA 48.0%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 34.5%, WIDE_SPREAD 25.1%, PLAYER_IDENTITY_RISK 18.6%, MODEL_HIGH_UNCERTAINTY 18.2%, EVENT_MAPPING_RISK 9.9%, LEVEL_TRANSFER_RISK 9.5%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 5.1%, EXTERNAL_MARKET_REJECTION 1.6%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.0%, POST_SETTLEMENT_OBSERVATION 34.0%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 7604, "IDENTITY_AMBIGUOUS": 2049}; ticker orientation: {"VERIFIED": 9653}.

Checks: discipline:AMBIGUOUS 667, discipline:PASS 8986, identity_confidence:AMBIGUOUS 1799, identity_confidence:PASS 7854, level_mapping:NA 679, level_mapping:PASS 8974, market_pair:AMBIGUOUS 351, market_pair:NA 228, market_pair:PASS 9074, model_complement:NA 195, model_complement:PASS 9458, namesake:PASS 9653, physical_match_id:NA 3649, physical_match_id:PASS 6004, player_ids:PASS 9653, same_pair_other_event:PASS 9653, ticker_orientation:PASS 9653

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,448 | 4.8% | 4.5% | 1.7% | {"market_freshness": 52, "model_calibration_or_unknown": 38, "data": 31, "execution": 19, "model_calibration": 12, "market_freshness/coverage": 10, "coverage": 4} | 5.89 | 0.2235 / 0.2154 (377) | 18.5% | 3.7% | 3.6% | 2.6% |
| CHALLENGER | 7,124 | 17.0% | 6.8% | 12.6% | {"coverage": 683, "market_freshness/coverage": 150, "market_freshness": 143, "data": 111, "model_calibration_or_unknown": 58, "execution": 30, "model_calibration": 23, "mapping": 14} | 7.44 | 0.2171 / 0.2072 (1730) | 35.0% | 16.9% | 3.8% | 22.2% |
| DOUBLES | 1,375 | 48.5% | 48.0% | 6.9% | {"execution": 331, "mapping": 177, "market_freshness": 106, "market_freshness/coverage": 46, "coverage": 7} | 24.06 | 0.323 / 0.2342 (358) | 17.0% | 0.0% | 100.0% | 7.0% |
| ITF_MEN | 11,959 | 25.0% | 17.5% | 31.0% | {"coverage": 1111, "execution": 613, "market_freshness": 472, "data": 416, "market_freshness/coverage": 246, "mapping": 129, "model_calibration_or_unknown": 2, "model_calibration": 1} | 11.43 | 0.215 / 0.1946 (2792) | 35.8% | 64.9% | 16.0% | 22.1% |
| ITF_WOMEN | 16,297 | 26.5% | 19.6% | 44.7% | {"coverage": 1459, "market_freshness": 862, "execution": 828, "data": 666, "market_freshness/coverage": 343, "mapping": 97, "model_calibration_or_unknown": 50, "model_calibration": 10} | 12.89 | 0.2027 / 0.1944 (3215) | 37.5% | 58.0% | 10.2% | 21.4% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,527 | 4.6% | 4.2% | 1.2% | {"market_freshness": 37, "model_calibration_or_unknown": 27, "execution": 17, "data": 11, "market_freshness/coverage": 10, "model_calibration": 10, "coverage": 4, "mapping": 1} | 7.91 | 0.2365 / 0.2304 (419) | 23.7% | 1.4% | 1.5% | 3.5% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.8% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 15 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 16 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 17 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 18 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 19 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 20 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 21 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 22 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 23 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 24 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 25 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 26 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 27 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 28 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 29 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 30 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 31 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 32 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 33 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 34 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 36 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 37 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 38 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 39 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 41 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 752 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 42 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 43 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 874 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 44 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 45 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 46 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 535 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |
| 47 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 547 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 48 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 49 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFWMATCH-26OCT16ESTLAB-LAB` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 68 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1475.0, ratio 2.28); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9706, "by_level_share_of_ge_25pp": {"ATP": 0.0172, "CHALLENGER": 0.1256, "DOUBLES": 0.0691, "ITF_MEN": 0.3097, "ITF_WOMEN": 0.447, "OTHER": 0.0012, "WTA": 0.0121, "WTA125": 0.018}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5083, "share_primary_cause_market_settled_or_in_play": 0.4273, "share_primary_cause_stale_quote_only": 0.1774}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 9653, "identity_ambiguous_share": 0.2123, "ticker_orientation": {"VERIFIED": 9653}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 6004, "with_external": 281, "coverage": 0.0468, "external_status": {"EXTERNAL_STALE": 183, "AGREES_WITH_KALSHI": 95, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 183, "MODEL_LONE_OUTLIER": 95, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3381, "share_external_supports_model": 0.0107}, "pregame_clean_ge_25pp": {"n": 2944, "with_external": 266, "coverage": 0.0904, "external_status": {"EXTERNAL_STALE": 170, "AGREES_WITH_KALSHI": 93, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 170, "MODEL_LONE_OUTLIER": 93, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3496, "share_external_supports_model": 0.0113}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 507.0, "median_sample_ratio": 2.44, "median_min_matches": 20.0, "median_max_days_since_last": 223.0, "share_severe_asymmetry": 0.2096, "data_status": {"POOR": 5320, "LIMITED": 2653, "ADEQUATE": 1680}, "comparison_lt_10pp": {"median_thinner_serve_points": 1759.0, "median_sample_ratio": 1.69, "median_min_matches": 93.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 740, "model_minus_observed": 0.0458, "kalshi_minus_observed": -0.0898, "brier_diff_model_minus_kalshi": -0.002}, "4-10x": {"n": 511, "model_minus_observed": 0.0881, "kalshi_minus_observed": -0.0575, "brier_diff_model_minus_kalshi": 0.0123}, "<2x": {"n": 1820, "model_minus_observed": 0.0872, "kalshi_minus_observed": -0.0347, "brier_diff_model_minus_kalshi": 0.0123}, ">=10x": {"n": 626, "model_minus_observed": 0.1098, "kalshi_minus_observed": -0.0632, "brier_diff_model_minus_kalshi": 0.0106}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3697, "model": {"intercept": -0.531, "slope": 0.845, "slope_se": 0.043}, "kalshi_mid_same_rows": {"intercept": 0.239, "slope": 1.131, "slope_se": 0.049}, "mean_extremity_model": 0.1715, "mean_extremity_kalshi": 0.1655, "model_brier": 0.232, "kalshi_brier": 0.2042, "brier_diff_model_minus_kalshi": 0.0278, "brier_diff_se": 0.0031, "model_logloss": 0.6608, "kalshi_logloss": 0.5908}, "fair_v1": {"n": 3697, "model": {"intercept": -0.399, "slope": 1.045, "slope_se": 0.047}, "kalshi_mid_same_rows": {"intercept": 0.319, "slope": 1.171, "slope_se": 0.049}, "mean_extremity_model": 0.1668, "mean_extremity_kalshi": 0.1651, "model_brier": 0.2135, "kalshi_brier": 0.2044, "brier_diff_model_minus_kalshi": 0.0091, "brier_diff_se": 0.0025, "model_logloss": 0.6154, "kalshi_logloss": 0.5911}, "gen1_elo": {"n": 3697, "model": {"intercept": -0.392, "slope": 1.022, "slope_se": 0.045}, "kalshi_mid_same_rows": {"intercept": 0.314, "slope": 1.154, "slope_se": 0.048}, "mean_extremity_model": 0.1731, "mean_extremity_kalshi": 0.1654, "model_brier": 0.2128, "kalshi_brier": 0.2044, "brier_diff_model_minus_kalshi": 0.0083, "brier_diff_se": 0.0025, "model_logloss": 0.6145, "kalshi_logloss": 0.5912}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2415, "share_ge_15": 0.4403, "median_abs_gap": 13.04, "n": 24864}, "gen1_elo": {"share_ge_25": 0.2384, "share_ge_15": 0.4365, "median_abs_gap": 12.73, "n": 24864}, "gen1_sr": {"share_ge_25": 0.3049, "share_ge_15": 0.5186, "median_abs_gap": 15.68, "n": 24864}, "gen2": {"share_ge_25": 0.3079, "share_ge_15": 0.5088, "median_abs_gap": 15.45, "n": 24864}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1518, "share_ge_15": 0.3576, "median_abs_gap": 10.88, "n": 19391}, "gen1_elo": {"share_ge_25": 0.1522, "share_ge_15": 0.3508, "median_abs_gap": 10.49, "n": 19389}, "gen1_sr": {"share_ge_25": 0.2147, "share_ge_15": 0.4432, "median_abs_gap": 13.09, "n": 19392}, "gen2": {"share_ge_25": 0.2305, "share_ge_15": 0.4445, "median_abs_gap": 13.09, "n": 19392}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.89, "share_ge_25_all": 0.0481, "share_ge_25_pregame_clean": 0.0453}, "WTA": {"median_abs_gap_pregame_clean": 7.91, "share_ge_25_all": 0.0463, "share_ge_25_pregame_clean": 0.0422}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2374, "share_within_10pp_all": 0.4354, "share_within_10pp_pregame_clean": 0.4874, "corr_model_vs_mid_pregame_clean": 0.8437}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 552, "model_brier": 0.196, "kalshi_brier": 0.1974, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 649, "model_brier": 0.2128, "kalshi_brier": 0.2036, "brier_diff_model_minus_kalshi": 0.0092}, "15-25": {"n_settled": 825, "model_brier": 0.2265, "kalshi_brier": 0.215, "brier_diff_model_minus_kalshi": 0.0115}, "25-40": {"n_settled": 461, "model_brier": 0.2251, "kalshi_brier": 0.2086, "brier_diff_model_minus_kalshi": 0.0165}, "3-5": {"n_settled": 352, "model_brier": 0.2011, "kalshi_brier": 0.2008, "brier_diff_model_minus_kalshi": 0.0004}, "40+": {"n_settled": 92, "model_brier": 0.3021, "kalshi_brier": 0.176, "brier_diff_model_minus_kalshi": 0.1261}, "5-10": {"n_settled": 766, "model_brier": 0.2008, "kalshi_brier": 0.2011, "brier_diff_model_minus_kalshi": -0.0003}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.531, "slope": 0.845, "slope_se": 0.043}, "kalshi_slope": {"intercept": 0.239, "slope": 1.131, "slope_se": 0.049}, "n": 3697}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.509, "slope": 0.872, "slope_se": 0.032}, "kalshi_slope": {"intercept": 0.16, "slope": 1.086, "slope_se": 0.037}, "n": 5724}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 358, "model_brier": 0.323, "kalshi_brier": 0.2342, "brier_diff_model_minus_kalshi": 0.0888, "brier_diff_se": 0.0166, "corr_model_outcome": 0.0088, "corr_kalshi_outcome": 0.2597}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
