# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-20T12:24Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 43,925): 0-3 14.3%, 3-5 9.5%, 5-10 19.8%, 10-15 15.4%, 15-25 19.3%, 25-40 13.8%, 40+ 7.9%; median gap 11.94 pp.
* **Where the extremes live**: 97.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 75.6%, Challenger 12.5%, doubles 7.0%). Main tour: ATP 4.8% and WTA 4.6% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 9,543): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.8%, BOOK_QUALITY 19.3%, STALE_QUOTE 17.8%, POOR_DATA 9.2%, POSSIBLY_IN_PLAY_QUOTE 5.3%, IDENTITY_AMBIGUOUS 4.4%, LIMITED_DATA 3.8%, IN_PLAY_QUOTE 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%. By class: coverage 33.8%, execution 19.3%, market_freshness 17.8%, data 13.0%, market_freshness/coverage 8.7%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.7%.
* **Stale / settled / in-play**: 50.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 9,543 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.3% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.7%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 24.4% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 504.0 points vs 1759.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.048, Gen-2 0.845, Gen-1 ledger 0.877 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 450 model 0.2236 vs Kalshi 0.2098; n 92 model 0.3021 vs Kalshi 0.176.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 186,852 model-market comparisons (303,387 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 65,148 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-20T12:11:35.220496+00:00'], shadow board 48,931 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-20T12:11:39.818720+00:00'], Model 4 23,265 rows, 17,284 settled tickers, 5,941 tickers with an external scan.
* By model: {"gen1_ledger": 43934, "gen1_elo": 24599, "fair_v1": 24599, "gen2": 24599, "gen1_sr": 24599, "model4_fundamental": 22270, "model4_conditioned": 22252}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 43,925 | 14.3 | 9.5 | 19.8 | 15.4 | 19.3 | 13.8 | 7.9 | 11.94 | 41.0% | 21.7% |
| MW fair_v1 | 24,599 | 13.3 | 8.6 | 18.4 | 15.7 | 19.9 | 14.6 | 9.4 | 13.01 | 43.9% | 24.0% |
| MW gen1_elo | 24,599 | 13.1 | 8.9 | 19.4 | 15.2 | 19.8 | 14.6 | 9.1 | 12.7 | 43.5% | 23.7% |
| MW gen1_ledger | 19,326 | 15.4 | 10.7 | 21.7 | 14.9 | 18.5 | 12.8 | 6.0 | 10.54 | 37.3% | 18.8% |
| MW gen1_sr | 24,599 | 10.0 | 7.3 | 16.7 | 14.2 | 21.4 | 18.6 | 11.8 | 15.64 | 51.8% | 30.4% |
| MW gen2 | 24,599 | 11.2 | 7.4 | 16.4 | 14.2 | 20.1 | 17.7 | 13.0 | 15.43 | 50.8% | 30.7% |
| all families model4_conditioned | 22,252 | 21.9 | 19.3 | 34.4 | 17.5 | 4.6 | 1.4 | 1.0 | 5.92 | 7.0% | 2.4% |
| all families model4_fundamental | 22,270 | 16.3 | 13.0 | 34.2 | 20.4 | 11.4 | 3.4 | 1.3 | 7.9 | 16.0% | 4.7% |

Configurable thresholds (primary): >=5pp 76.2%, >=10pp 56.4%, >=15pp 41.0%, >=20pp 30.3%, >=25pp 21.7%, >=30pp 15.6%, >=40pp 7.9%, >=50pp 3.5%
Executable gap (model outside the book, before fees): median 8.35pp; >=10pp 44.9%, >=25pp 16.8%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,170 | 28.2 | 14.0 | 24.9 | 15.6 | 11.7 | 5.0 | 0.6 | 6.22 | 17.2% | 5.5% |
| CHALLENGER | 4,147 | 15.7 | 10.2 | 20.4 | 16.0 | 14.9 | 12.3 | 10.7 | 11.15 | 37.9% | 23.0% |
| ITF_MEN | 6,471 | 11.0 | 7.8 | 17.1 | 14.5 | 20.6 | 16.8 | 12.2 | 14.91 | 49.6% | 29.0% |
| ITF_WOMEN | 9,645 | 9.9 | 6.8 | 15.8 | 15.5 | 23.2 | 18.0 | 10.8 | 15.65 | 52.0% | 28.8% |
| WTA | 1,506 | 17.5 | 12.6 | 24.1 | 20.0 | 20.9 | 4.3 | 0.7 | 8.81 | 25.9% | 5.1% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,170 | 23.2 | 15.1 | 24.7 | 17.1 | 13.9 | 5.2 | 0.8 | 6.72 | 19.9% | 6.0% |
| CHALLENGER | 4,147 | 14.7 | 8.5 | 19.0 | 14.4 | 17.9 | 14.0 | 11.7 | 12.55 | 43.5% | 25.6% |
| ITF_MEN | 6,471 | 9.1 | 6.5 | 15.2 | 13.3 | 19.7 | 20.2 | 16.0 | 17.62 | 55.9% | 36.2% |
| ITF_WOMEN | 9,645 | 8.2 | 5.6 | 13.5 | 13.6 | 21.7 | 20.8 | 16.5 | 18.85 | 59.0% | 37.3% |
| WTA | 1,506 | 14.7 | 9.6 | 19.9 | 16.1 | 24.6 | 14.4 | 0.8 | 11.73 | 39.8% | 15.2% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,170 | 23.7 | 13.4 | 24.8 | 16.0 | 15.2 | 6.0 | 1.0 | 7.1 | 22.1% | 7.0% |
| CHALLENGER | 4,147 | 14.4 | 9.6 | 21.2 | 15.3 | 16.0 | 12.4 | 11.1 | 11.2 | 39.5% | 23.5% |
| ITF_MEN | 6,471 | 10.3 | 7.8 | 17.3 | 13.9 | 21.3 | 17.1 | 12.2 | 15.22 | 50.7% | 29.4% |
| ITF_WOMEN | 9,645 | 9.5 | 6.8 | 16.3 | 15.7 | 23.4 | 18.3 | 10.0 | 15.58 | 51.6% | 28.2% |
| WTA | 1,506 | 24.4 | 16.7 | 30.2 | 15.7 | 10.2 | 2.3 | 0.5 | 6.0 | 12.9% | 2.7% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,240 | 26.6 | 19.9 | 29.7 | 12.0 | 8.4 | 3.0 | 0.4 | 5.38 | 11.8% | 3.4% |
| CHALLENGER | 2,917 | 21.4 | 14.6 | 27.1 | 14.1 | 14.6 | 6.4 | 1.9 | 7.26 | 23.0% | 8.3% |
| DOUBLES | 1,372 | 4.5 | 4.1 | 11.5 | 10.5 | 20.9 | 25.9 | 22.6 | 24.11 | 69.4% | 48.5% |
| ITF_MEN | 5,396 | 14.2 | 8.7 | 20.6 | 15.9 | 20.5 | 13.3 | 6.8 | 11.93 | 40.6% | 20.1% |
| ITF_WOMEN | 6,517 | 12.2 | 8.9 | 19.2 | 15.2 | 21.8 | 16.6 | 6.1 | 13.04 | 44.5% | 22.6% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,003 | 22.2 | 15.8 | 29.4 | 18.1 | 10.4 | 3.7 | 0.3 | 6.97 | 14.4% | 4.0% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,127 | 28.4 | 14.1 | 25.2 | 15.4 | 11.6 | 4.7 | 0.6 | 6.17 | 16.8% | 5.3% |
| CHALLENGER | 2,962 | 20.3 | 12.5 | 25.1 | 18.3 | 15.3 | 6.6 | 2.0 | 8.38 | 23.8% | 8.5% |
| ITF_MEN | 4,759 | 13.4 | 9.5 | 20.3 | 16.4 | 21.1 | 13.7 | 5.5 | 11.94 | 40.4% | 19.3% |
| ITF_WOMEN | 7,276 | 11.5 | 8.2 | 17.8 | 17.6 | 24.9 | 15.2 | 4.9 | 13.46 | 44.9% | 20.1% |
| WTA | 1,465 | 17.7 | 12.3 | 24.0 | 20.1 | 20.8 | 4.3 | 0.8 | 8.85 | 25.9% | 5.1% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,127 | 23.4 | 15.3 | 24.7 | 17.1 | 13.8 | 5.0 | 0.7 | 6.63 | 19.5% | 5.7% |
| CHALLENGER | 2,962 | 18.2 | 10.8 | 23.6 | 17.2 | 18.2 | 9.6 | 2.3 | 9.3 | 30.1% | 11.9% |
| ITF_MEN | 4,760 | 10.7 | 7.7 | 17.4 | 15.1 | 21.7 | 18.2 | 9.2 | 14.64 | 49.1% | 27.4% |
| ITF_WOMEN | 7,276 | 9.2 | 6.5 | 14.8 | 15.0 | 23.7 | 20.3 | 10.5 | 16.66 | 54.5% | 30.8% |
| WTA | 1,465 | 14.7 | 9.6 | 19.9 | 15.9 | 24.6 | 14.6 | 0.8 | 12.02 | 40.0% | 15.4% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,202 | 26.8 | 20.1 | 29.9 | 12.2 | 7.9 | 2.8 | 0.2 | 5.32 | 11.0% | 3.1% |
| CHALLENGER | 2,545 | 22.8 | 15.7 | 28.8 | 13.9 | 13.9 | 4.2 | 0.6 | 6.68 | 18.8% | 4.9% |
| DOUBLES | 1,276 | 4.5 | 4.2 | 11.7 | 10.7 | 20.8 | 26.1 | 22.0 | 24.06 | 68.9% | 48.1% |
| ITF_MEN | 4,502 | 15.5 | 9.4 | 22.5 | 16.7 | 20.2 | 11.6 | 4.2 | 10.77 | 35.9% | 15.7% |
| ITF_WOMEN | 5,444 | 13.0 | 9.5 | 20.6 | 16.1 | 22.0 | 15.3 | 3.5 | 11.84 | 40.8% | 18.8% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 956 | 22.7 | 16.3 | 29.5 | 18.2 | 10.4 | 2.9 | 0.0 | 6.82 | 13.3% | 2.9% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,372 | 4.5 | 4.1 | 11.5 | 10.5 | 20.9 | 25.9 | 22.6 | 24.11 | 69.4% | 48.5% |
| singles | 17,954 | 16.3 | 11.2 | 22.4 | 15.3 | 18.3 | 11.8 | 4.7 | 10.03 | 34.8% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 5,564 | 13.5 | 9.0 | 19.4 | 15.8 | 18.5 | 14.6 | 9.3 | 12.6 | 42.4% | 23.9% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 15,646 | 13.6 | 8.6 | 18.4 | 15.4 | 20.2 | 14.4 | 9.4 | 13.02 | 43.9% | 23.8% |
| UNKNOWN | 3,152 | 11.7 | 7.9 | 16.9 | 17.3 | 20.5 | 15.9 | 9.9 | 13.55 | 46.2% | 25.7% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,150 | 19.7 | 11.5 | 21.3 | 16.9 | 16.0 | 8.9 | 5.7 | 9.3 | 30.6% | 14.6% |
| B | 3,166 | 12.8 | 9.2 | 20.1 | 17.1 | 18.7 | 11.8 | 10.3 | 12.04 | 40.8% | 22.1% |
| C | 3,455 | 12.5 | 9.0 | 18.9 | 14.7 | 19.9 | 15.2 | 9.8 | 13.1 | 44.9% | 25.0% |
| D | 4,057 | 12.3 | 7.9 | 17.0 | 15.7 | 22.0 | 15.6 | 9.5 | 13.96 | 47.1% | 25.1% |
| F | 6,771 | 7.9 | 5.6 | 15.1 | 14.4 | 23.2 | 21.2 | 12.6 | 17.78 | 57.0% | 33.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,535 | 23.2 | 15.8 | 28.5 | 15.2 | 11.7 | 4.1 | 1.5 | 6.68 | 17.3% | 5.6% |
| B | 2,706 | 15.9 | 10.5 | 24.1 | 16.1 | 18.9 | 10.8 | 3.8 | 9.9 | 33.4% | 14.6% |
| C | 3,802 | 10.9 | 7.3 | 18.4 | 14.4 | 21.9 | 16.3 | 10.9 | 14.48 | 49.0% | 27.2% |
| D | 2,791 | 14.0 | 9.6 | 19.8 | 14.7 | 21.0 | 14.7 | 6.2 | 12.1 | 41.9% | 20.8% |
| F | 4,492 | 10.4 | 7.9 | 15.7 | 14.5 | 22.2 | 20.7 | 8.6 | 15.84 | 51.5% | 29.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 8,098 | 17.9 | 10.4 | 20.6 | 16.9 | 16.4 | 9.6 | 8.1 | 10.27 | 34.1% | 17.7% |
| LIMITED | 5,450 | 14.1 | 10.3 | 20.2 | 15.6 | 19.2 | 13.4 | 7.3 | 11.62 | 39.9% | 20.7% |
| POOR | 11,051 | 9.6 | 6.5 | 15.9 | 15.0 | 22.7 | 18.9 | 11.4 | 16.03 | 53.0% | 30.3% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,772 | 26.7 | 21.0 | 34.7 | 11.7 | 4.2 | 1.5 | 0.2 | 5.18 | 5.8% | 1.7% |
| GAME_SPREAD | 4,173 | 23.1 | 15.4 | 33.4 | 17.0 | 8.5 | 2.2 | 0.3 | 6.52 | 11.0% | 2.6% |
| MATCH_WINNER | 19,326 | 15.4 | 10.7 | 21.7 | 14.9 | 18.5 | 12.8 | 6.0 | 10.54 | 37.3% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 8,862 | 30.1 | 16.9 | 30.4 | 12.5 | 8.1 | 1.5 | 0.4 | 5.38 | 10.1% | 1.9% |
| TOTAL_GAMES | 6,777 | 7.9 | 9.2 | 36.6 | 29.1 | 10.9 | 3.5 | 2.9 | 9.6 | 17.3% | 6.3% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,790 | 25.4 | 34.8 | 32.1 | 3.7 | 3.2 | 0.6 | 0.1 | 4.44 | 3.9% | 0.7% |
| GAME_SPREAD | 5,339 | 46.1 | 16.9 | 26.9 | 7.5 | 1.8 | 0.6 | 0.2 | 3.38 | 2.6% | 0.8% |
| TOTAL_GAMES | 9,123 | 4.8 | 7.4 | 40.6 | 35.1 | 7.4 | 2.5 | 2.3 | 9.72 | 12.1% | 4.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,793 | 24.4 | 17.9 | 35.6 | 12.2 | 7.2 | 2.5 | 0.3 | 5.79 | 10.0% | 2.9% |
| GAME_SPREAD | 5,342 | 19.1 | 13.3 | 28.4 | 19.9 | 14.4 | 4.1 | 0.9 | 7.96 | 19.4% | 5.0% |
| TOTAL_GAMES | 9,135 | 7.7 | 8.8 | 36.5 | 27.8 | 13.2 | 3.7 | 2.4 | 9.67 | 19.2% | 6.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 24,599 | 43.9% | 24.0% | 13.01 | 35.7% | 15.1% | 10.85 |
| gen1_elo | 24,599 | 43.5% | 23.7% | 12.7 | 35.0% | 15.2% | 10.48 |
| gen1_sr | 24,599 | 51.8% | 30.4% | 15.64 | 44.3% | 21.4% | 13.09 |
| gen2 | 24,599 | 50.8% | 30.7% | 15.43 | 44.4% | 23.0% | 13.08 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 13,065 | 16.0 | 10.4 | 21.2 | 17.3 | 20.3 | 11.5 | 3.2 | 10.68 | 35.1% | 14.8% |
| STALE | 11,534 | 10.3 | 6.6 | 15.2 | 14.0 | 19.4 | 18.1 | 16.3 | 16.98 | 53.9% | 34.5% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 12,794 | 16.6 | 11.2 | 22.7 | 15.0 | 17.5 | 12.2 | 4.8 | 9.86 | 34.4% | 17.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 43,925 | 12794 | 16537 | 14594 | 23.7 | 123.5 | 1400.4 |
| ge_15pp | 18,005 | 4408 | 5873 | 7724 | 25.7 | 416.0 | 1380.4 |
| ge_25pp | 9,543 | 2172 | 2524 | 4847 | 31.1 | 562.2 | 1380.4 |
| lt_10pp | 19,161 | 6462 | 7852 | 4847 | 21.7 | 47.3 | 1341.5 |

Current slate `SL-20261020T122439Z-8bdd73c9`: 658 priced rows, quote age at build {'median': 13.5, 'max': 13.6}, freshness {'AGING': 658}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 12 | 0.0 | 0.0 | 33.3 | 0.0 | 50.0 | 16.7 | 0.0 | 20.33 | 66.7% | 16.7% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,332 | 20.1 | 10.8 | 23.5 | 18.7 | 19.1 | 7.0 | 0.7 | 9.05 | 26.8% | 7.8% |
| KALSHI_LONE_OUTLIER | 14 | 7.1 | 7.1 | 71.4 | 0.0 | 7.1 | 7.1 | 0.0 | 5.35 | 14.3% | 7.1% |
| MARKETS_AGREE | 410 | 68.0 | 31.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.1 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 898 | 0.0 | 2.7 | 34.6 | 27.6 | 24.6 | 9.9 | 0.6 | 12.37 | 35.1% | 10.5% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 24,599 | 3678 (14.9%) | 24.4% | 0.7% | {"EXTERNAL_STALE": 2332, "AGREES_WITH_KALSHI": 898, "ALL_AGREE": 410, "AGREES_WITH_MODEL": 14, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 11, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 10,798 | 951 (8.8%) | 33.1% | 1.1% | {"EXTERNAL_STALE": 626, "AGREES_WITH_KALSHI": 315, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 5,909 | 278 (4.7%) | 33.8% | 1.1% | {"EXTERNAL_STALE": 181, "AGREES_WITH_KALSHI": 94, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,909 | 264 (9.1%) | 34.8% | 1.1% | {"EXTERNAL_STALE": 169, "AGREES_WITH_KALSHI": 92, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 9,930 | 2042 (20.6%) | 16.4% | 0.7% | {"EXTERNAL_STALE": 1269, "ALL_AGREE": 410, "AGREES_WITH_KALSHI": 335, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 12, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 4,741 | 10.8 | 7.9 | 19.5 | 14.7 | 22.1 | 15.4 | 9.7 | 13.84 | 47.1% | 25.0% |
| 4-10x | 3,212 | 11.6 | 8.5 | 18.6 | 15.6 | 20.9 | 14.9 | 9.9 | 13.57 | 45.7% | 24.8% |
| <2x | 12,695 | 15.3 | 9.7 | 18.9 | 16.8 | 18.2 | 12.8 | 8.3 | 11.77 | 39.3% | 21.1% |
| >=10x | 3,951 | 11.3 | 6.4 | 15.4 | 13.6 | 21.6 | 19.4 | 12.3 | 16.24 | 53.2% | 31.6% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 6,272 | 12.7 | 8.6 | 19.8 | 16.2 | 19.7 | 13.3 | 9.7 | 12.7 | 42.7% | 23.0% |
| 300-1000 | 5,373 | 12.0 | 8.8 | 16.8 | 15.7 | 21.0 | 16.1 | 9.6 | 13.84 | 46.7% | 25.8% |
| <300 | 7,649 | 9.1 | 5.8 | 15.4 | 14.5 | 22.9 | 20.1 | 12.1 | 16.86 | 55.1% | 32.2% |
| >=3000 | 5,305 | 21.5 | 12.7 | 22.6 | 17.0 | 14.6 | 6.8 | 4.8 | 8.08 | 26.2% | 11.6% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 728 | 0.5453 | 0.4098 | 0.5014 | +0.044 | -0.092 | -0.0024 ± 0.0056 |
| ratio 4-10x | 504 | 0.5923 | 0.4477 | 0.506 | +0.086 | -0.058 | 0.0114 ± 0.0072 |
| ratio <2x | 1793 | 0.5364 | 0.4149 | 0.4512 | +0.085 | -0.036 | 0.0119 ± 0.0033 |
| ratio >=10x | 614 | 0.5635 | 0.3896 | 0.4544 | +0.109 | -0.065 | 0.0101 ± 0.0074 |
| thinner_sample 1000-3000 | 995 | 0.543 | 0.4171 | 0.4573 | +0.086 | -0.040 | 0.0095 ± 0.0045 |
| thinner_sample 300-1000 | 859 | 0.5666 | 0.4249 | 0.4994 | +0.067 | -0.074 | 0.0001 ± 0.0055 |
| thinner_sample <300 | 1167 | 0.5546 | 0.3906 | 0.4559 | +0.099 | -0.065 | 0.0123 ± 0.0051 |
| thinner_sample >=3000 | 618 | 0.5325 | 0.439 | 0.4725 | +0.060 | -0.034 | 0.0121 ± 0.0046 |
| data_status ADEQUATE | 1053 | 0.5359 | 0.4319 | 0.4625 | +0.073 | -0.031 | 0.0108 ± 0.0038 |
| data_status LIMITED | 884 | 0.5527 | 0.421 | 0.4842 | +0.069 | -0.063 | 0.0043 ± 0.005 |
| data_status POOR | 1702 | 0.5584 | 0.3996 | 0.4659 | +0.092 | -0.066 | 0.0096 ± 0.0042 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 546 | 0.1969 | 0.1984 | -0.0015 ± 0.0007 | 0.5728 | 0.5759 | 0.4993 | 0.4843 | 0.5385 | -0.048 ± 0.0199 | -0.01 (5) |
| 3-5 | 347 | 0.2 | 0.1997 | +0.0003 ± 0.0019 | 0.5828 | 0.581 | 0.506 | 0.4659 | 0.4813 | -0.087 ± 0.0246 | 0.02 (1) |
| 5-10 | 754 | 0.1997 | 0.2006 | -0.0009 ± 0.0025 | 0.5851 | 0.5854 | 0.5125 | 0.4379 | 0.4761 | -0.079 ± 0.017 | -0.0167 (6) |
| 10-15 | 640 | 0.2141 | 0.2046 | +0.0095 ± 0.0045 | 0.6182 | 0.5909 | 0.5248 | 0.4006 | 0.4234 | -0.100 ± 0.0178 | -0.048 (5) |
| 15-25 | 810 | 0.2267 | 0.2157 | +0.0109 ± 0.0064 | 0.6476 | 0.6167 | 0.5789 | 0.3833 | 0.4531 | -0.085 ± 0.0162 | -0.0033 (9) |
| 25-40 | 450 | 0.2236 | 0.2098 | +0.0138 ± 0.0128 | 0.6354 | 0.6025 | 0.6545 | 0.3464 | 0.4756 | -0.073 ± 0.0196 | -0.01 (1) |
| 40+ | 92 | 0.3021 | 0.176 | +0.1261 ± 0.0392 | 0.8232 | 0.5249 | 0.7541 | 0.3058 | 0.3913 | -0.125 ± 0.0376 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2634 | 0.1808 | 0.1821 | -0.0013 ± 0.0003 | 0.5368 | 0.5385 | 0.4807 | 0.4656 | 0.5065 | -0.016 ± 0.0084 | -0.0129 (17) |
| 3-5 | 1703 | 0.1957 | 0.1947 | +0.0010 ± 0.0009 | 0.5729 | 0.567 | 0.4829 | 0.4431 | 0.4492 | -0.052 ± 0.0109 | 0.0 (2) |
| 5-10 | 3658 | 0.1963 | 0.1937 | +0.0025 ± 0.0011 | 0.5751 | 0.5666 | 0.4851 | 0.4112 | 0.4295 | -0.045 ± 0.0074 | -0.0119 (21) |
| 10-15 | 3210 | 0.2045 | 0.1868 | +0.0177 ± 0.0019 | 0.5968 | 0.547 | 0.4865 | 0.362 | 0.353 | -0.073 ± 0.0076 | -0.0281 (16) |
| 15-25 | 3997 | 0.2085 | 0.1725 | +0.0361 ± 0.0026 | 0.6087 | 0.5095 | 0.5022 | 0.306 | 0.3127 | -0.067 ± 0.0065 | -0.0025 (44) |
| 25-40 | 3011 | 0.222 | 0.1279 | +0.0941 ± 0.0041 | 0.6383 | 0.3922 | 0.5315 | 0.2187 | 0.2282 | -0.064 ± 0.0063 | -0.01 (1) |
| 40+ | 1982 | 0.3811 | 0.0428 | +0.3383 ± 0.0052 | 0.9919 | 0.1696 | 0.6304 | 0.1071 | 0.0565 | -0.088 ± 0.0043 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 407 | 0.2012 | 0.2018 | -0.0006 ± 0.0008 | 0.5844 | 0.5858 | 0.5029 | 0.488 | 0.5111 | -0.088 ± 0.0238 | -0.01 (3) |
| 3-5 | 299 | 0.2178 | 0.2168 | +0.0010 ± 0.0022 | 0.6206 | 0.6189 | 0.5157 | 0.4757 | 0.4783 | -0.098 ± 0.0286 | 0.02 (1) |
| 5-10 | 646 | 0.198 | 0.1993 | -0.0013 ± 0.0026 | 0.5792 | 0.5818 | 0.5479 | 0.4728 | 0.5186 | -0.068 ± 0.0181 | -0.01 (4) |
| 10-15 | 605 | 0.2191 | 0.2131 | +0.0060 ± 0.0047 | 0.6287 | 0.6131 | 0.5643 | 0.4399 | 0.481 | -0.095 ± 0.0195 | -0.04 (5) |
| 15-25 | 869 | 0.2318 | 0.2108 | +0.0210 ± 0.0061 | 0.6561 | 0.6048 | 0.5924 | 0.3961 | 0.4453 | -0.098 ± 0.0158 | -0.0133 (9) |
| 25-40 | 598 | 0.262 | 0.2006 | +0.0614 ± 0.0115 | 0.7319 | 0.5824 | 0.6619 | 0.3465 | 0.408 | -0.113 ± 0.0179 | -0.0075 (4) |
| 40+ | 215 | 0.3655 | 0.1714 | +0.1941 ± 0.0279 | 1.0131 | 0.5113 | 0.74 | 0.2584 | 0.3116 | -0.085 ± 0.0271 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2225 | 0.1866 | 0.1872 | -0.0006 ± 0.0003 | 0.5502 | 0.5513 | 0.5023 | 0.4873 | 0.5115 | -0.033 ± 0.0095 | -0.0133 (15) |
| 3-5 | 1472 | 0.1977 | 0.1978 | -0.0001 ± 0.0009 | 0.5732 | 0.5732 | 0.5154 | 0.4754 | 0.4952 | -0.033 ± 0.0118 | 0.02 (1) |
| 5-10 | 3237 | 0.1917 | 0.1916 | +0.0001 ± 0.0011 | 0.566 | 0.5619 | 0.5079 | 0.4339 | 0.4711 | -0.025 ± 0.0078 | -0.0117 (6) |
| 10-15 | 2865 | 0.2007 | 0.1893 | +0.0115 ± 0.002 | 0.5896 | 0.5514 | 0.5158 | 0.3914 | 0.4098 | -0.053 ± 0.0082 | -0.0189 (18) |
| 15-25 | 4066 | 0.2177 | 0.1802 | +0.0374 ± 0.0026 | 0.6301 | 0.5292 | 0.531 | 0.3347 | 0.3409 | -0.069 ± 0.0067 | -0.0086 (42) |
| 25-40 | 3579 | 0.2493 | 0.1396 | +0.1097 ± 0.004 | 0.7038 | 0.4262 | 0.5638 | 0.2479 | 0.2339 | -0.084 ± 0.0062 | -0.0044 (18) |
| 40+ | 2751 | 0.4003 | 0.0642 | +0.3360 ± 0.0055 | 1.0554 | 0.2263 | 0.6607 | 0.125 | 0.092 | -0.073 ± 0.0047 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 521 | 0.1997 | 0.2023 | -0.0026 ± 0.0007 | 0.5806 | 0.5869 | 0.498 | 0.4827 | 0.5605 | -0.010 ± 0.0201 | -0.0137 (8) |
| 3-5 | 382 | 0.1945 | 0.1926 | +0.0019 ± 0.0018 | 0.5667 | 0.5623 | 0.5021 | 0.4626 | 0.4607 | -0.116 ± 0.0234 | 0.0067 (3) |
| 5-10 | 785 | 0.2007 | 0.1985 | +0.0022 ± 0.0024 | 0.5881 | 0.5797 | 0.5101 | 0.4362 | 0.4548 | -0.092 ± 0.0164 | -0.0071 (7) |
| 10-15 | 633 | 0.2086 | 0.2056 | +0.0030 ± 0.0045 | 0.6048 | 0.5938 | 0.5388 | 0.4155 | 0.4676 | -0.080 ± 0.0178 | -0.0317 (6) |
| 15-25 | 759 | 0.2341 | 0.2127 | +0.0213 ± 0.0065 | 0.6674 | 0.6097 | 0.5869 | 0.3931 | 0.4348 | -0.112 ± 0.0167 | -0.03 (1) |
| 25-40 | 465 | 0.2111 | 0.2171 | -0.0060 ± 0.0126 | 0.6083 | 0.6195 | 0.6619 | 0.3517 | 0.514 | -0.048 ± 0.0192 | 0.015 (2) |
| 40+ | 94 | 0.3174 | 0.1917 | +0.1257 ± 0.0406 | 0.8659 | 0.5602 | 0.7616 | 0.3091 | 0.4043 | -0.111 ± 0.0415 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2553 | 0.1887 | 0.1896 | -0.0009 ± 0.0003 | 0.5547 | 0.5565 | 0.4886 | 0.4733 | 0.4955 | -0.032 ± 0.0087 | -0.0163 (35) |
| 3-5 | 1763 | 0.1879 | 0.1852 | +0.0026 ± 0.0008 | 0.5534 | 0.547 | 0.4838 | 0.4443 | 0.4317 | -0.074 ± 0.0105 | -0.0094 (18) |
| 5-10 | 3849 | 0.196 | 0.1908 | +0.0052 ± 0.0011 | 0.5763 | 0.5588 | 0.4856 | 0.4118 | 0.4115 | -0.061 ± 0.0071 | -0.01 (31) |
| 10-15 | 3054 | 0.1977 | 0.1817 | +0.0160 ± 0.0019 | 0.5806 | 0.534 | 0.5 | 0.3764 | 0.3739 | -0.069 ± 0.0077 | -0.015 (12) |
| 15-25 | 4066 | 0.2118 | 0.1735 | +0.0384 ± 0.0026 | 0.6181 | 0.5119 | 0.5085 | 0.3136 | 0.3128 | -0.073 ± 0.0065 | -0.03 (2) |
| 25-40 | 2989 | 0.2179 | 0.1276 | +0.0903 ± 0.0041 | 0.6292 | 0.3904 | 0.5313 | 0.2156 | 0.2335 | -0.059 ± 0.0062 | 0.01 (3) |
| 40+ | 1921 | 0.3961 | 0.0475 | +0.3485 ± 0.0056 | 1.0343 | 0.1822 | 0.642 | 0.1127 | 0.0604 | -0.090 ± 0.0047 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 879 | 0.1967 | 0.1969 | -0.0002 ± 0.0005 | 0.5739 | 0.5742 | 0.5086 | 0.4936 | 0.4983 | -0.057 ± 0.0152 | -0.0224 (49) |
| 3-5 | 612 | 0.1938 | 0.1934 | +0.0005 ± 0.0014 | 0.5658 | 0.5637 | 0.4823 | 0.4425 | 0.4542 | -0.051 ± 0.0179 | -0.0194 (34) |
| 5-10 | 1306 | 0.1999 | 0.1939 | +0.0060 ± 0.0018 | 0.5877 | 0.5697 | 0.4909 | 0.4176 | 0.4142 | -0.069 ± 0.0124 | -0.005 (78) |
| 10-15 | 833 | 0.2077 | 0.1976 | +0.0102 ± 0.0038 | 0.6033 | 0.5769 | 0.5142 | 0.3911 | 0.4094 | -0.061 ± 0.0156 | 0.0014 (64) |
| 15-25 | 1129 | 0.2313 | 0.211 | +0.0203 ± 0.0054 | 0.6603 | 0.6081 | 0.5709 | 0.376 | 0.4234 | -0.063 ± 0.0137 | -0.0214 (59) |
| 25-40 | 670 | 0.2494 | 0.2029 | +0.0465 ± 0.0107 | 0.7063 | 0.5851 | 0.6603 | 0.348 | 0.4284 | -0.086 ± 0.0162 | -0.0219 (26) |
| 40+ | 232 | 0.3485 | 0.197 | +0.1515 ± 0.029 | 1.0068 | 0.5758 | 0.804 | 0.3181 | 0.4267 | -0.077 ± 0.0257 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2789 | 0.1864 | 0.1865 | -0.0000 ± 0.0003 | 0.5474 | 0.5467 | 0.5073 | 0.492 | 0.4987 | -0.040 ± 0.0082 | -0.0157 (88) |
| 3-5 | 1927 | 0.1915 | 0.1894 | +0.0021 ± 0.0008 | 0.5599 | 0.5552 | 0.4875 | 0.4478 | 0.4416 | -0.054 ± 0.01 | -0.0209 (69) |
| 5-10 | 3896 | 0.1972 | 0.1889 | +0.0084 ± 0.001 | 0.5799 | 0.5561 | 0.4876 | 0.4143 | 0.3963 | -0.071 ± 0.007 | -0.0082 (132) |
| 10-15 | 2660 | 0.2035 | 0.1897 | +0.0138 ± 0.0021 | 0.5941 | 0.5578 | 0.5194 | 0.3963 | 0.4011 | -0.057 ± 0.0084 | -0.0053 (105) |
| 15-25 | 3348 | 0.2277 | 0.1973 | +0.0304 ± 0.003 | 0.6572 | 0.5741 | 0.5625 | 0.3673 | 0.3892 | -0.062 ± 0.0077 | -0.0253 (107) |
| 25-40 | 2280 | 0.2556 | 0.1783 | +0.0773 ± 0.0056 | 0.7239 | 0.5221 | 0.6202 | 0.3063 | 0.3434 | -0.074 ± 0.0086 | -0.0229 (51) |
| 40+ | 1056 | 0.3772 | 0.1369 | +0.2404 ± 0.0121 | 1.069 | 0.4156 | 0.7229 | 0.2186 | 0.2462 | -0.073 ± 0.0105 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3639 | 1.048 ± 0.047 | 1.172 | 0.1666 | 0.1644 | 0.2134 | 0.2048 |
| gen2 | 3639 | 0.845 ± 0.043 | 1.129 | 0.1718 | 0.1648 | 0.232 | 0.2046 |
| gen1_elo | 3639 | 1.024 ± 0.046 | 1.156 | 0.1727 | 0.1648 | 0.2126 | 0.2048 |
| gen1_sr | 3639 | 1.046 ± 0.056 | 1.203 | 0.1322 | 0.1667 | 0.228 | 0.2044 |
| gen1_ledger | 5661 | 0.877 ± 0.033 | 1.084 | 0.179 | 0.1801 | 0.2181 | 0.1994 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 18,005)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,071 | 22.6% |
| STALE_QUOTE | market_freshness | 3,711 | 20.6% |
| BOOK_QUALITY | execution | 3,506 | 19.5% |
| POOR_DATA | data | 2,085 | 11.6% |
| LIMITED_DATA | data | 1,221 | 6.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 965 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 916 | 5.1% |
| IDENTITY_AMBIGUOUS | mapping | 729 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 523 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 278 | 1.5% |

Cause class: coverage 22.6%, market_freshness 20.6%, execution 19.5%, data 18.4%, market_freshness/coverage 8.3%, model_calibration_or_unknown 5.1%, mapping 4.0%, model_calibration 1.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.2%, START_UNVERIFIABLE 94.2%, LOW_DATA_QUALITY 70.3%, THIN_PLAYER_HISTORY 59.1%, STALE_PLAYER_DATA 53.0%, STALE_KALSHI_QUOTE 42.9%, MODEL_INTERNAL_DISAGREEMENT 41.5%, ASYMMETRIC_SAMPLE_SIZE 32.7%, WIDE_SPREAD 25.3%, MODEL_HIGH_UNCERTAINTY 17.9%, PLAYER_IDENTITY_RISK 15.2%, LEVEL_TRANSFER_RISK 10.3%, EVENT_MAPPING_RISK 8.2%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 2.7%, UNKNOWN 1.0%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.1%, POST_SETTLEMENT_OBSERVATION 22.6%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 9,543)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,228 | 33.8% |
| BOOK_QUALITY | execution | 1,840 | 19.3% |
| STALE_QUOTE | market_freshness | 1,703 | 17.8% |
| POOR_DATA | data | 875 | 9.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 503 | 5.3% |
| IDENTITY_AMBIGUOUS | mapping | 422 | 4.4% |
| LIMITED_DATA | data | 365 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 326 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 215 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 66 | 0.7% |

Cause class: coverage 33.8%, execution 19.3%, market_freshness 17.8%, data 13.0%, market_freshness/coverage 8.7%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.7%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.4%, START_UNVERIFIABLE 97.1%, LOW_DATA_QUALITY 74.4%, THIN_PLAYER_HISTORY 61.8%, STALE_KALSHI_QUOTE 50.8%, STALE_PLAYER_DATA 48.3%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 34.6%, WIDE_SPREAD 25.2%, PLAYER_IDENTITY_RISK 18.7%, MODEL_HIGH_UNCERTAINTY 18.2%, EVENT_MAPPING_RISK 10.0%, LEVEL_TRANSFER_RISK 9.5%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 5.1%, EXTERNAL_MARKET_REJECTION 1.5%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.8%, POST_SETTLEMENT_OBSERVATION 33.8%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 7511, "IDENTITY_AMBIGUOUS": 2032}; ticker orientation: {"VERIFIED": 9543}.

Checks: discipline:AMBIGUOUS 666, discipline:PASS 8877, identity_confidence:AMBIGUOUS 1784, identity_confidence:PASS 7759, level_mapping:NA 678, level_mapping:PASS 8865, market_pair:AMBIGUOUS 348, market_pair:NA 224, market_pair:PASS 8971, model_complement:NA 191, model_complement:PASS 9352, namesake:PASS 9543, physical_match_id:NA 3634, physical_match_id:PASS 5909, player_ids:PASS 9543, same_pair_other_event:PASS 9543, ticker_orientation:PASS 9543

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,410 | 4.8% | 4.5% | 1.7% | {"market_freshness": 51, "model_calibration_or_unknown": 37, "data": 30, "execution": 19, "model_calibration": 12, "market_freshness/coverage": 10, "coverage": 3} | 5.9 | 0.2214 / 0.2144 (365) | 18.6% | 3.6% | 3.7% | 2.4% |
| CHALLENGER | 7,064 | 17.0% | 6.9% | 12.5% | {"coverage": 674, "market_freshness/coverage": 146, "market_freshness": 142, "data": 108, "model_calibration_or_unknown": 61, "execution": 30, "model_calibration": 22, "mapping": 14} | 7.41 | 0.2163 / 0.206 (1708) | 35.0% | 16.8% | 3.7% | 22.0% |
| DOUBLES | 1,372 | 48.5% | 48.1% | 7.0% | {"execution": 331, "mapping": 177, "market_freshness": 106, "market_freshness/coverage": 45, "coverage": 7} | 24.06 | 0.3202 / 0.2346 (353) | 17.1% | 0.0% | 100.0% | 7.0% |
| ITF_MEN | 11,867 | 24.9% | 17.5% | 31.0% | {"coverage": 1096, "execution": 610, "market_freshness": 471, "data": 413, "market_freshness/coverage": 239, "mapping": 128, "model_calibration_or_unknown": 2, "model_calibration": 1} | 11.41 | 0.2153 / 0.1957 (2754) | 35.8% | 64.6% | 15.9% | 22.0% |
| ITF_WOMEN | 16,162 | 26.3% | 19.5% | 44.6% | {"coverage": 1431, "market_freshness": 856, "execution": 819, "data": 655, "market_freshness/coverage": 340, "mapping": 97, "model_calibration_or_unknown": 48, "model_calibration": 10} | 12.84 | 0.2032 / 0.1952 (3175) | 37.5% | 58.1% | 10.2% | 21.3% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,509 | 4.6% | 4.2% | 1.2% | {"market_freshness": 37, "model_calibration_or_unknown": 26, "execution": 17, "data": 11, "market_freshness/coverage": 10, "model_calibration": 10, "coverage": 4, "mapping": 1} | 7.91 | 0.2343 / 0.2296 (415) | 23.7% | 1.4% | 1.5% | 3.5% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.8% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 207 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 15 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 16 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 17 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 18 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 19 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 20 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 21 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 22 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 23 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 24 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 25 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 26 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 27 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 28 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 213 min (STALE); no external reference |
| 29 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 30 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 31 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 32 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 33 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 34 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 92 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 36 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 37 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 38 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | POOR_DATA | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 39 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 41 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 752 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 42 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 43 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 44 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 45 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 46 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 535 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |
| 47 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 33 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 48 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 49 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFWMATCH-26OCT16ESTLAB-LAB` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 68 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1475.0, ratio 2.28); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9709, "by_level_share_of_ge_25pp": {"ATP": 0.017, "CHALLENGER": 0.1254, "DOUBLES": 0.0698, "ITF_MEN": 0.3102, "ITF_WOMEN": 0.446, "OTHER": 0.0013, "WTA": 0.0122, "WTA125": 0.0182}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5079, "share_primary_cause_market_settled_or_in_play": 0.4252, "share_primary_cause_stale_quote_only": 0.1785}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 9543, "identity_ambiguous_share": 0.2129, "ticker_orientation": {"VERIFIED": 9543}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 5909, "with_external": 278, "coverage": 0.047, "external_status": {"EXTERNAL_STALE": 181, "AGREES_WITH_KALSHI": 94, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 181, "MODEL_LONE_OUTLIER": 94, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3381, "share_external_supports_model": 0.0108}, "pregame_clean_ge_25pp": {"n": 2909, "with_external": 264, "coverage": 0.0908, "external_status": {"EXTERNAL_STALE": 169, "AGREES_WITH_KALSHI": 92, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 169, "MODEL_LONE_OUTLIER": 92, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3485, "share_external_supports_model": 0.0114}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 504.0, "median_sample_ratio": 2.46, "median_min_matches": 20.0, "median_max_days_since_last": 223.0, "share_severe_asymmetry": 0.21, "data_status": {"POOR": 5264, "LIMITED": 2627, "ADEQUATE": 1652}, "comparison_lt_10pp": {"median_thinner_serve_points": 1759.0, "median_sample_ratio": 1.68, "median_min_matches": 93.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 728, "model_minus_observed": 0.044, "kalshi_minus_observed": -0.0916, "brier_diff_model_minus_kalshi": -0.0024}, "4-10x": {"n": 504, "model_minus_observed": 0.0863, "kalshi_minus_observed": -0.0583, "brier_diff_model_minus_kalshi": 0.0114}, "<2x": {"n": 1793, "model_minus_observed": 0.0852, "kalshi_minus_observed": -0.0363, "brier_diff_model_minus_kalshi": 0.0119}, ">=10x": {"n": 614, "model_minus_observed": 0.1091, "kalshi_minus_observed": -0.0648, "brier_diff_model_minus_kalshi": 0.0101}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3639, "model": {"intercept": -0.524, "slope": 0.845, "slope_se": 0.043}, "kalshi_mid_same_rows": {"intercept": 0.243, "slope": 1.129, "slope_se": 0.049}, "mean_extremity_model": 0.1718, "mean_extremity_kalshi": 0.1648, "model_brier": 0.232, "kalshi_brier": 0.2046, "brier_diff_model_minus_kalshi": 0.0273, "brier_diff_se": 0.0031, "model_logloss": 0.6605, "kalshi_logloss": 0.5919}, "fair_v1": {"n": 3639, "model": {"intercept": -0.391, "slope": 1.048, "slope_se": 0.047}, "kalshi_mid_same_rows": {"intercept": 0.327, "slope": 1.172, "slope_se": 0.05}, "mean_extremity_model": 0.1666, "mean_extremity_kalshi": 0.1644, "model_brier": 0.2134, "kalshi_brier": 0.2048, "brier_diff_model_minus_kalshi": 0.0086, "brier_diff_se": 0.0026, "model_logloss": 0.615, "kalshi_logloss": 0.5921}, "gen1_elo": {"n": 3639, "model": {"intercept": -0.379, "slope": 1.024, "slope_se": 0.046}, "kalshi_mid_same_rows": {"intercept": 0.326, "slope": 1.156, "slope_se": 0.049}, "mean_extremity_model": 0.1727, "mean_extremity_kalshi": 0.1648, "model_brier": 0.2126, "kalshi_brier": 0.2048, "brier_diff_model_minus_kalshi": 0.0077, "brier_diff_se": 0.0026, "model_logloss": 0.614, "kalshi_logloss": 0.5922}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2402, "share_ge_15": 0.439, "median_abs_gap": 13.01, "n": 24599}, "gen1_elo": {"share_ge_25": 0.237, "share_ge_15": 0.4351, "median_abs_gap": 12.7, "n": 24599}, "gen1_sr": {"share_ge_25": 0.3037, "share_ge_15": 0.5177, "median_abs_gap": 15.64, "n": 24599}, "gen2": {"share_ge_25": 0.3068, "share_ge_15": 0.508, "median_abs_gap": 15.43, "n": 24599}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1513, "share_ge_15": 0.3566, "median_abs_gap": 10.85, "n": 19223}, "gen1_elo": {"share_ge_25": 0.1515, "share_ge_15": 0.3498, "median_abs_gap": 10.48, "n": 19221}, "gen1_sr": {"share_ge_25": 0.2144, "share_ge_15": 0.4428, "median_abs_gap": 13.09, "n": 19224}, "gen2": {"share_ge_25": 0.23, "share_ge_15": 0.4441, "median_abs_gap": 13.08, "n": 19224}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.9, "share_ge_25_all": 0.0475, "share_ge_25_pregame_clean": 0.0448}, "WTA": {"median_abs_gap_pregame_clean": 7.91, "share_ge_25_all": 0.0462, "share_ge_25_pregame_clean": 0.0421}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2378, "share_within_10pp_all": 0.4362, "share_within_10pp_pregame_clean": 0.4881, "corr_model_vs_mid_pregame_clean": 0.8435}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 546, "model_brier": 0.1969, "kalshi_brier": 0.1984, "brier_diff_model_minus_kalshi": -0.0015}, "10-15": {"n_settled": 640, "model_brier": 0.2141, "kalshi_brier": 0.2046, "brier_diff_model_minus_kalshi": 0.0095}, "15-25": {"n_settled": 810, "model_brier": 0.2267, "kalshi_brier": 0.2157, "brier_diff_model_minus_kalshi": 0.0109}, "25-40": {"n_settled": 450, "model_brier": 0.2236, "kalshi_brier": 0.2098, "brier_diff_model_minus_kalshi": 0.0138}, "3-5": {"n_settled": 347, "model_brier": 0.2, "kalshi_brier": 0.1997, "brier_diff_model_minus_kalshi": 0.0003}, "40+": {"n_settled": 92, "model_brier": 0.3021, "kalshi_brier": 0.176, "brier_diff_model_minus_kalshi": 0.1261}, "5-10": {"n_settled": 754, "model_brier": 0.1997, "kalshi_brier": 0.2006, "brier_diff_model_minus_kalshi": -0.0009}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.524, "slope": 0.845, "slope_se": 0.043}, "kalshi_slope": {"intercept": 0.243, "slope": 1.129, "slope_se": 0.049}, "n": 3639}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.505, "slope": 0.877, "slope_se": 0.033}, "kalshi_slope": {"intercept": 0.162, "slope": 1.084, "slope_se": 0.037}, "n": 5661}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 353, "model_brier": 0.3202, "kalshi_brier": 0.2346, "brier_diff_model_minus_kalshi": 0.0856, "brier_diff_se": 0.0166, "corr_model_outcome": 0.0122, "corr_kalshi_outcome": 0.2598}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
