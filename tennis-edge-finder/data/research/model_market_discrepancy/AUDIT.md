# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-12T16:11Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 30,065): 0-3 14.6%, 3-5 9.7%, 5-10 20.2%, 10-15 15.4%, 15-25 18.5%, 25-40 13.4%, 40+ 8.1%; median gap 11.67 pp.
* **Where the extremes live**: 98.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.1%, Challenger 12.4%, doubles 7.1%). Main tour: ATP 1.5% and WTA 6.3% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 6,484): MARKET_ALREADY_SETTLED_WHEN_PRICED 38.9%, BOOK_QUALITY 17.5%, STALE_QUOTE 16.2%, POOR_DATA 8.1%, POSSIBLY_IN_PLAY_QUOTE 5.6%, LIMITED_DATA 4.2%, IDENTITY_AMBIGUOUS 3.8%, IN_PLAY_QUOTE 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.4%. By class: coverage 38.9%, execution 17.5%, market_freshness 16.2%, data 12.3%, market_freshness/coverage 9.1%, mapping 3.8%, model_calibration_or_unknown 1.9%, model_calibration 0.4%.
* **Stale / settled / in-play**: 54.0% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 48.0% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 6,484 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 17.7% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 2.9%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 21.3% of the time and with the model 0.6%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 611.0 points vs 1905.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.063, Gen-2 0.866, Gen-1 ledger 0.869 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 280 model 0.219 vs Kalshi 0.2012; n 62 model 0.2951 vs Kalshi 0.1745.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 120,150 model-market comparisons (197,379 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 44,579 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-12T16:02:41.077474+00:00'], shadow board 31,783 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-12T16:02:44.845139+00:00'], Model 4 13,601 rows, 13,123 settled tickers, 3,712 tickers with an external scan.
* By model: {"gen1_ledger": 29375, "gen1_elo": 15971, "fair_v1": 15971, "gen2": 15971, "gen1_sr": 15971, "model4_fundamental": 13450, "model4_conditioned": 13441}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 30,065 | 14.6 | 9.7 | 20.2 | 15.4 | 18.5 | 13.4 | 8.1 | 11.67 | 40.1% | 21.6% |
| MW fair_v1 | 15,971 | 13.9 | 8.8 | 18.7 | 16.0 | 18.6 | 14.3 | 9.7 | 12.67 | 42.7% | 24.1% |
| MW gen1_elo | 15,971 | 13.5 | 9.1 | 20.3 | 15.0 | 18.7 | 14.2 | 9.2 | 12.09 | 42.1% | 23.5% |
| MW gen1_ledger | 14,094 | 15.4 | 10.7 | 21.9 | 14.7 | 18.5 | 12.4 | 6.3 | 10.47 | 37.2% | 18.7% |
| MW gen1_sr | 15,971 | 10.1 | 7.9 | 16.6 | 14.5 | 21.6 | 17.9 | 11.4 | 15.35 | 50.9% | 29.3% |
| MW gen2 | 15,971 | 12.0 | 7.4 | 16.5 | 14.3 | 20.1 | 17.0 | 12.8 | 14.94 | 49.8% | 29.8% |
| all families model4_conditioned | 13,441 | 21.8 | 20.1 | 35.8 | 16.1 | 4.2 | 1.1 | 0.9 | 5.79 | 6.2% | 2.0% |
| all families model4_fundamental | 13,450 | 16.6 | 13.3 | 35.9 | 19.9 | 10.6 | 2.6 | 1.1 | 7.64 | 14.3% | 3.8% |

Configurable thresholds (primary): >=5pp 75.7%, >=10pp 55.5%, >=15pp 40.1%, >=20pp 29.8%, >=25pp 21.6%, >=30pp 15.8%, >=40pp 8.1%, >=50pp 3.6%
Executable gap (model outside the book, before fees): median 8.25pp; >=10pp 44.7%, >=25pp 17.3%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,294 | 30.3 | 14.5 | 24.6 | 17.9 | 10.6 | 1.2 | 0.8 | 5.84 | 12.6% | 2.0% |
| CHALLENGER | 2,828 | 15.8 | 10.1 | 20.1 | 15.9 | 14.5 | 12.1 | 11.5 | 11.51 | 38.1% | 23.7% |
| ITF_MEN | 4,409 | 11.5 | 8.8 | 18.2 | 14.9 | 19.1 | 15.3 | 12.2 | 13.77 | 46.7% | 27.5% |
| ITF_WOMEN | 6,106 | 10.2 | 6.7 | 15.8 | 16.2 | 21.6 | 18.6 | 10.8 | 15.46 | 51.1% | 29.4% |
| WTA | 834 | 21.5 | 11.2 | 25.3 | 16.1 | 19.2 | 5.5 | 1.3 | 8.0 | 26.0% | 6.8% |
| WTA125 | 500 | 12.8 | 8.2 | 23.6 | 19.6 | 19.2 | 14.6 | 2.0 | 11.14 | 35.8% | 16.6% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,294 | 24.0 | 14.6 | 24.3 | 19.2 | 14.8 | 1.9 | 1.0 | 6.9 | 17.8% | 2.9% |
| CHALLENGER | 2,828 | 15.3 | 7.5 | 19.4 | 13.4 | 18.1 | 14.2 | 12.1 | 12.73 | 44.5% | 26.3% |
| ITF_MEN | 4,409 | 10.3 | 7.5 | 16.6 | 14.7 | 19.8 | 17.9 | 13.2 | 15.45 | 50.9% | 31.2% |
| ITF_WOMEN | 6,106 | 8.9 | 5.8 | 12.8 | 12.9 | 21.6 | 20.9 | 17.1 | 19.11 | 59.6% | 38.0% |
| WTA | 834 | 18.8 | 8.5 | 18.4 | 15.7 | 22.8 | 14.5 | 1.3 | 11.64 | 38.6% | 15.8% |
| WTA125 | 500 | 4.8 | 4.2 | 19.4 | 19.0 | 24.2 | 18.6 | 9.8 | 16.79 | 52.6% | 28.4% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,294 | 27.4 | 14.4 | 29.2 | 15.1 | 10.5 | 2.5 | 0.9 | 6.1 | 14.0% | 3.5% |
| CHALLENGER | 2,828 | 15.3 | 10.2 | 20.9 | 15.4 | 14.9 | 11.7 | 11.6 | 10.76 | 38.2% | 23.3% |
| ITF_MEN | 4,409 | 10.5 | 8.8 | 18.9 | 13.8 | 20.0 | 15.7 | 12.4 | 14.04 | 48.0% | 28.0% |
| ITF_WOMEN | 6,106 | 9.8 | 6.8 | 16.5 | 15.6 | 22.7 | 19.0 | 9.6 | 15.52 | 51.2% | 28.6% |
| WTA | 834 | 22.7 | 15.0 | 33.7 | 15.3 | 10.1 | 2.4 | 0.8 | 6.12 | 13.3% | 3.2% |
| WTA125 | 500 | 22.0 | 10.8 | 29.8 | 15.2 | 14.6 | 7.2 | 0.4 | 7.96 | 22.2% | 7.6% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 705 | 30.6 | 22.7 | 35.9 | 9.1 | 1.3 | 0.4 | 0.0 | 4.73 | 1.7% | 0.4% |
| CHALLENGER | 1,949 | 22.2 | 15.8 | 27.2 | 14.8 | 13.0 | 5.0 | 2.0 | 6.93 | 20.1% | 7.0% |
| DOUBLES | 913 | 4.5 | 3.2 | 11.4 | 11.4 | 19.3 | 24.8 | 25.5 | 25.37 | 69.5% | 50.3% |
| ITF_MEN | 4,192 | 14.8 | 8.5 | 21.1 | 15.6 | 20.4 | 12.2 | 7.4 | 11.75 | 40.0% | 19.6% |
| ITF_WOMEN | 4,915 | 11.6 | 9.3 | 19.5 | 14.6 | 22.5 | 16.7 | 5.8 | 13.12 | 45.0% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 630 | 21.4 | 14.9 | 26.8 | 17.3 | 14.0 | 5.1 | 0.5 | 7.7 | 19.5% | 5.6% |
| WTA125 | 641 | 19.5 | 14.2 | 22.0 | 18.6 | 14.8 | 8.6 | 2.3 | 8.37 | 25.7% | 10.9% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,280 | 30.2 | 14.4 | 24.8 | 18.0 | 10.6 | 1.1 | 0.9 | 5.84 | 12.5% | 1.9% |
| CHALLENGER | 2,061 | 20.1 | 12.5 | 25.1 | 18.5 | 15.1 | 6.1 | 2.6 | 8.32 | 23.8% | 8.7% |
| ITF_MEN | 3,116 | 14.4 | 11.0 | 21.8 | 16.8 | 19.1 | 11.9 | 4.9 | 10.65 | 35.9% | 16.9% |
| ITF_WOMEN | 4,352 | 12.6 | 8.4 | 18.5 | 18.8 | 23.3 | 14.9 | 3.4 | 12.65 | 41.6% | 18.3% |
| WTA | 821 | 21.6 | 10.6 | 25.7 | 16.2 | 19.2 | 5.4 | 1.3 | 8.09 | 25.9% | 6.7% |
| WTA125 | 479 | 13.4 | 7.9 | 23.0 | 20.0 | 19.8 | 14.4 | 1.5 | 11.31 | 35.7% | 15.9% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,280 | 23.9 | 14.7 | 24.4 | 19.2 | 14.8 | 1.9 | 1.0 | 6.9 | 17.7% | 2.9% |
| CHALLENGER | 2,061 | 19.5 | 9.4 | 24.1 | 16.0 | 18.6 | 9.8 | 2.7 | 9.19 | 31.0% | 12.4% |
| ITF_MEN | 3,117 | 12.5 | 9.1 | 19.4 | 16.6 | 21.4 | 15.2 | 6.0 | 12.54 | 42.6% | 21.1% |
| ITF_WOMEN | 4,352 | 10.4 | 6.9 | 14.6 | 14.1 | 24.3 | 19.6 | 10.1 | 16.41 | 54.0% | 29.7% |
| WTA | 821 | 18.6 | 8.3 | 18.5 | 16.0 | 22.8 | 14.5 | 1.3 | 11.73 | 38.6% | 15.8% |
| WTA125 | 479 | 4.8 | 4.4 | 19.6 | 19.4 | 23.8 | 19.2 | 8.8 | 16.14 | 51.8% | 28.0% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 685 | 30.7 | 22.9 | 36.2 | 9.2 | 0.6 | 0.4 | 0.0 | 4.7 | 1.0% | 0.4% |
| CHALLENGER | 1,678 | 24.0 | 17.3 | 29.3 | 14.7 | 12.1 | 2.1 | 0.5 | 6.31 | 14.7% | 2.6% |
| DOUBLES | 846 | 4.5 | 3.2 | 11.7 | 11.5 | 19.4 | 24.6 | 25.2 | 24.68 | 69.2% | 49.8% |
| ITF_MEN | 3,392 | 16.5 | 9.3 | 23.3 | 16.5 | 20.2 | 9.8 | 4.2 | 10.21 | 34.3% | 14.0% |
| ITF_WOMEN | 4,025 | 12.8 | 10.0 | 21.4 | 15.4 | 22.8 | 15.0 | 2.7 | 11.65 | 40.5% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 596 | 22.0 | 15.6 | 27.0 | 17.3 | 14.3 | 3.9 | 0.0 | 7.22 | 18.1% | 3.9% |
| WTA125 | 543 | 21.4 | 15.8 | 23.6 | 20.4 | 13.1 | 5.3 | 0.4 | 7.5 | 18.8% | 5.7% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 913 | 4.5 | 3.2 | 11.4 | 11.4 | 19.3 | 24.8 | 25.5 | 25.37 | 69.5% | 50.3% |
| singles | 13,181 | 16.1 | 11.2 | 22.7 | 14.9 | 18.4 | 11.6 | 5.0 | 9.96 | 35.0% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 3,650 | 13.4 | 9.4 | 20.6 | 15.9 | 16.9 | 13.8 | 10.0 | 12.05 | 40.7% | 23.8% |
| Grass | 82 | 11.0 | 21.9 | 14.6 | 7.3 | 25.6 | 18.3 | 1.2 | 11.46 | 45.1% | 19.5% |
| Hard | 10,651 | 14.4 | 8.6 | 18.6 | 15.9 | 18.9 | 14.1 | 9.6 | 12.64 | 42.6% | 23.7% |
| UNKNOWN | 1,588 | 11.7 | 8.0 | 15.5 | 17.6 | 19.8 | 16.9 | 10.6 | 14.09 | 47.3% | 27.5% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,967 | 20.1 | 10.8 | 21.1 | 17.1 | 15.2 | 8.7 | 7.1 | 9.44 | 31.0% | 15.8% |
| B | 2,156 | 14.3 | 9.4 | 19.9 | 17.1 | 17.4 | 12.0 | 9.8 | 11.43 | 39.2% | 21.9% |
| C | 2,343 | 13.3 | 9.7 | 19.5 | 14.6 | 19.0 | 14.7 | 9.2 | 12.61 | 42.9% | 23.9% |
| D | 2,841 | 10.8 | 8.5 | 18.0 | 16.0 | 22.0 | 14.7 | 10.0 | 13.8 | 46.7% | 24.7% |
| F | 3,664 | 7.9 | 5.3 | 14.8 | 14.9 | 20.9 | 22.9 | 13.4 | 18.36 | 57.2% | 36.3% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,161 | 22.3 | 15.9 | 28.7 | 15.3 | 11.7 | 4.5 | 1.7 | 6.8 | 17.8% | 6.2% |
| B | 2,184 | 15.3 | 9.8 | 24.0 | 16.2 | 19.1 | 11.2 | 4.3 | 10.18 | 34.7% | 15.5% |
| C | 2,801 | 12.3 | 7.6 | 18.1 | 14.4 | 20.4 | 15.7 | 11.4 | 13.64 | 47.6% | 27.2% |
| D | 2,198 | 14.1 | 9.8 | 21.0 | 13.3 | 21.7 | 13.8 | 6.3 | 11.85 | 41.8% | 20.1% |
| F | 2,750 | 9.3 | 7.5 | 14.8 | 14.1 | 23.8 | 20.8 | 9.8 | 16.77 | 54.3% | 30.6% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 5,470 | 18.4 | 9.9 | 20.2 | 17.1 | 15.4 | 9.6 | 9.4 | 10.42 | 34.4% | 19.0% |
| LIMITED | 3,943 | 15.3 | 10.5 | 20.7 | 15.6 | 18.4 | 12.8 | 6.7 | 11.02 | 37.9% | 19.5% |
| POOR | 6,558 | 9.2 | 6.8 | 16.2 | 15.4 | 21.4 | 19.2 | 11.8 | 15.99 | 52.4% | 31.1% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,914 | 31.3 | 24.1 | 36.5 | 5.6 | 1.8 | 0.7 | 0.1 | 4.52 | 2.6% | 0.8% |
| GAME_SPREAD | 2,811 | 25.5 | 15.8 | 36.9 | 17.0 | 4.2 | 0.4 | 0.2 | 6.04 | 4.8% | 0.6% |
| MATCH_WINNER | 14,094 | 15.4 | 10.7 | 21.9 | 14.7 | 18.5 | 12.4 | 6.3 | 10.47 | 37.2% | 18.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 5,305 | 33.1 | 19.5 | 30.9 | 9.8 | 5.3 | 1.2 | 0.2 | 4.76 | 6.7% | 1.4% |
| TOTAL_GAMES | 4,227 | 6.7 | 9.0 | 39.1 | 29.8 | 10.3 | 2.7 | 2.4 | 9.49 | 15.4% | 5.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,790 | 25.6 | 37.9 | 31.7 | 0.3 | 4.0 | 0.4 | 0.1 | 4.32 | 4.5% | 0.6% |
| GAME_SPREAD | 3,404 | 45.0 | 16.2 | 29.2 | 7.4 | 1.1 | 0.7 | 0.4 | 3.59 | 2.3% | 1.1% |
| TOTAL_GAMES | 5,247 | 3.3 | 6.5 | 43.7 | 36.2 | 6.5 | 1.8 | 2.0 | 9.68 | 10.3% | 3.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,790 | 26.2 | 18.5 | 37.2 | 9.3 | 6.4 | 2.1 | 0.3 | 5.54 | 8.8% | 2.4% |
| GAME_SPREAD | 3,404 | 18.9 | 13.1 | 30.3 | 21.4 | 13.2 | 2.4 | 0.7 | 7.88 | 16.3% | 3.1% |
| TOTAL_GAMES | 5,256 | 6.5 | 8.7 | 38.4 | 28.4 | 12.7 | 3.2 | 2.1 | 9.67 | 18.1% | 5.4% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 15,971 | 42.7% | 24.1% | 12.67 | 32.7% | 13.7% | 10.18 |
| gen1_elo | 15,971 | 42.1% | 23.5% | 12.09 | 31.9% | 13.5% | 9.58 |
| gen1_sr | 15,971 | 50.9% | 29.3% | 15.35 | 41.9% | 18.9% | 12.52 |
| gen2 | 15,971 | 49.8% | 29.8% | 14.94 | 42.2% | 20.7% | 12.43 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 8,454 | 16.8 | 11.0 | 21.6 | 17.5 | 18.8 | 11.1 | 3.3 | 10.16 | 33.1% | 14.3% |
| STALE | 7,517 | 10.6 | 6.3 | 15.4 | 14.3 | 18.4 | 18.0 | 17.0 | 16.86 | 53.4% | 35.0% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 7,562 | 17.4 | 11.7 | 23.9 | 14.7 | 16.8 | 10.9 | 4.6 | 9.25 | 32.4% | 15.6% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 30,065 | 7562 | 11926 | 10577 | 24.2 | 144.1 | 1400.4 |
| ge_15pp | 12,058 | 2446 | 4088 | 5524 | 27.4 | 443.4 | 1380.4 |
| ge_25pp | 6,484 | 1177 | 1804 | 3503 | 34.5 | 574.8 | 1380.4 |
| lt_10pp | 13,374 | 4006 | 5807 | 3561 | 22.6 | 49.0 | 1341.5 |

Current slate `SL-20261012T161112Z-9c6de465`: 368 priced rows, quote age at build {'median': 8.8, 'max': 8.9}, freshness {'FRESH': 368}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 8 | 0.0 | 0.0 | 37.5 | 0.0 | 37.5 | 25.0 | 0.0 | 20.45 | 62.5% | 25.0% |
| EXTERNAL_LONE_OUTLIER | 8 | 62.5 | 37.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.43 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,165 | 22.1 | 11.3 | 22.9 | 18.8 | 18.3 | 6.2 | 0.3 | 8.47 | 24.8% | 6.5% |
| KALSHI_LONE_OUTLIER | 3 | 0.0 | 0.0 | 66.7 | 0.0 | 33.3 | 0.0 | 0.0 | 5.14 | 33.3% | 0.0% |
| MARKETS_AGREE | 207 | 72.0 | 28.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.03 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 377 | 0.0 | 4.0 | 36.3 | 30.8 | 20.4 | 7.7 | 0.8 | 11.24 | 28.9% | 8.5% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 15,971 | 1768 (11.1%) | 21.3% | 0.6% | {"EXTERNAL_STALE": 1165, "AGREES_WITH_KALSHI": 377, "ALL_AGREE": 207, "EXTERNAL_OUTLIER": 8, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 3, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 6,813 | 404 (5.9%) | 27.0% | 1.5% | {"EXTERNAL_STALE": 289, "AGREES_WITH_KALSHI": 109, "SUPPORTS_MODEL_DIRECTION": 5, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp | 3,845 | 110 (2.9%) | 29.1% | 1.8% | {"EXTERNAL_STALE": 76, "AGREES_WITH_KALSHI": 32, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_ge_25pp_pregame_clean | 1,657 | 104 (6.3%) | 28.8% | 1.9% | {"EXTERNAL_STALE": 72, "AGREES_WITH_KALSHI": 30, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_lt_10pp | 6,599 | 1029 (15.6%) | 14.8% | 0.4% | {"EXTERNAL_STALE": 657, "ALL_AGREE": 207, "AGREES_WITH_KALSHI": 152, "EXTERNAL_OUTLIER": 8, "AGREES_WITH_MODEL": 2, "SUPPORTS_MODEL_DIRECTION": 2, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,168 | 11.7 | 8.4 | 19.7 | 15.0 | 21.3 | 13.9 | 10.0 | 13.24 | 45.2% | 23.9% |
| 4-10x | 2,136 | 11.9 | 9.0 | 19.2 | 15.3 | 19.6 | 15.7 | 9.3 | 13.04 | 44.6% | 25.0% |
| <2x | 8,594 | 15.9 | 9.4 | 18.9 | 17.2 | 17.0 | 12.6 | 9.0 | 11.67 | 38.7% | 21.6% |
| >=10x | 2,073 | 10.7 | 6.6 | 16.0 | 13.5 | 19.9 | 20.8 | 12.6 | 16.51 | 53.3% | 33.4% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 4,222 | 14.1 | 8.3 | 19.4 | 15.9 | 18.8 | 12.7 | 10.7 | 12.5 | 42.2% | 23.4% |
| 300-1000 | 3,737 | 12.1 | 9.0 | 17.2 | 16.0 | 21.0 | 15.6 | 9.1 | 13.57 | 45.7% | 24.7% |
| <300 | 4,204 | 8.5 | 6.2 | 15.8 | 14.7 | 20.7 | 21.1 | 12.9 | 17.11 | 54.8% | 34.0% |
| >=3000 | 3,808 | 21.2 | 11.8 | 22.5 | 17.7 | 13.6 | 7.4 | 5.8 | 8.46 | 26.7% | 13.1% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 509 | 0.5376 | 0.4061 | 0.4813 | +0.056 | -0.075 | 0.0019 ± 0.0064 |
| ratio 4-10x | 343 | 0.5818 | 0.4415 | 0.519 | +0.063 | -0.077 | 0.0029 ± 0.0085 |
| ratio <2x | 1218 | 0.5381 | 0.4176 | 0.4589 | +0.079 | -0.041 | 0.0106 ± 0.004 |
| ratio >=10x | 350 | 0.5508 | 0.382 | 0.4371 | +0.114 | -0.055 | 0.0142 ± 0.0096 |
| thinner_sample 1000-3000 | 684 | 0.543 | 0.4189 | 0.4751 | +0.068 | -0.056 | 0.0041 ± 0.0054 |
| thinner_sample 300-1000 | 620 | 0.564 | 0.4252 | 0.4855 | +0.079 | -0.060 | 0.004 ± 0.0062 |
| thinner_sample <300 | 689 | 0.5448 | 0.385 | 0.4557 | +0.089 | -0.071 | 0.0118 ± 0.0066 |
| thinner_sample >=3000 | 427 | 0.5268 | 0.4334 | 0.4567 | +0.070 | -0.023 | 0.015 ± 0.0055 |
| data_status ADEQUATE | 687 | 0.5291 | 0.4266 | 0.4512 | +0.078 | -0.025 | 0.0099 ± 0.0047 |
| data_status LIMITED | 658 | 0.5547 | 0.4252 | 0.4939 | +0.061 | -0.069 | 0.0021 ± 0.0057 |
| data_status POOR | 1075 | 0.5516 | 0.3979 | 0.4651 | +0.086 | -0.067 | 0.0108 ± 0.0051 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 375 | 0.1922 | 0.1935 | -0.0013 ± 0.0008 | 0.5626 | 0.5655 | 0.4911 | 0.4762 | 0.52 | -0.051 ± 0.0237 | -0.01 (3) |
| 3-5 | 246 | 0.1914 | 0.1929 | -0.0015 ± 0.0022 | 0.5629 | 0.565 | 0.5087 | 0.469 | 0.5041 | -0.058 ± 0.0283 | 0.02 (1) |
| 5-10 | 508 | 0.1991 | 0.2016 | -0.0025 ± 0.003 | 0.5825 | 0.588 | 0.5182 | 0.4442 | 0.4882 | -0.077 ± 0.0208 | -0.0125 (4) |
| 10-15 | 434 | 0.2122 | 0.2045 | +0.0077 ± 0.0054 | 0.6124 | 0.5902 | 0.5178 | 0.394 | 0.4217 | -0.093 ± 0.0216 | -0.0633 (3) |
| 15-25 | 515 | 0.228 | 0.216 | +0.0120 ± 0.008 | 0.6508 | 0.6196 | 0.5751 | 0.3805 | 0.4485 | -0.076 ± 0.0204 | -0.0133 (6) |
| 25-40 | 280 | 0.219 | 0.2012 | +0.0178 ± 0.0159 | 0.6281 | 0.5782 | 0.6485 | 0.34 | 0.4643 | -0.073 ± 0.0238 | -0.01 (1) |
| 40+ | 62 | 0.2951 | 0.1745 | +0.1206 ± 0.0473 | 0.8037 | 0.5243 | 0.7482 | 0.3023 | 0.3871 | -0.131 ± 0.0477 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1877 | 0.1761 | 0.1771 | -0.0010 ± 0.0003 | 0.5263 | 0.5272 | 0.4771 | 0.4621 | 0.4965 | -0.022 ± 0.0098 | -0.0188 (8) |
| 3-5 | 1169 | 0.1956 | 0.194 | +0.0016 ± 0.001 | 0.5729 | 0.5644 | 0.4778 | 0.4382 | 0.4337 | -0.063 ± 0.0131 | 0.02 (1) |
| 5-10 | 2528 | 0.1931 | 0.1909 | +0.0022 ± 0.0013 | 0.5679 | 0.5603 | 0.4868 | 0.4131 | 0.4308 | -0.050 ± 0.0088 | -0.0082 (17) |
| 10-15 | 2204 | 0.2009 | 0.1832 | +0.0177 ± 0.0023 | 0.5877 | 0.538 | 0.4786 | 0.3541 | 0.3448 | -0.075 ± 0.0091 | -0.0475 (4) |
| 15-25 | 2575 | 0.205 | 0.1698 | +0.0352 ± 0.0032 | 0.602 | 0.5025 | 0.4977 | 0.3018 | 0.3126 | -0.063 ± 0.0081 | -0.0048 (29) |
| 25-40 | 2097 | 0.2193 | 0.1233 | +0.0960 ± 0.0048 | 0.6319 | 0.3815 | 0.5287 | 0.215 | 0.2222 | -0.064 ± 0.0074 | -0.01 (1) |
| 40+ | 1428 | 0.3711 | 0.0439 | +0.3272 ± 0.0062 | 0.968 | 0.1738 | 0.6224 | 0.1061 | 0.0574 | -0.085 ± 0.0052 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 283 | 0.1963 | 0.1963 | -0.0000 ± 0.0009 | 0.5754 | 0.5756 | 0.4959 | 0.481 | 0.4841 | -0.096 ± 0.028 | -0.01 (1) |
| 3-5 | 192 | 0.2134 | 0.2137 | -0.0004 ± 0.0027 | 0.609 | 0.6113 | 0.5242 | 0.484 | 0.5052 | -0.063 ± 0.035 | 0.02 (1) |
| 5-10 | 446 | 0.1965 | 0.1957 | +0.0008 ± 0.0032 | 0.5746 | 0.5731 | 0.556 | 0.4809 | 0.5112 | -0.076 ± 0.0218 | -0.01 (4) |
| 10-15 | 407 | 0.2162 | 0.207 | +0.0091 ± 0.0057 | 0.6192 | 0.6 | 0.5766 | 0.452 | 0.4816 | -0.097 ± 0.0233 | -0.05 (4) |
| 15-25 | 585 | 0.2236 | 0.2081 | +0.0155 ± 0.0074 | 0.6359 | 0.5986 | 0.5965 | 0.3994 | 0.4632 | -0.083 ± 0.0192 | -0.01 (5) |
| 25-40 | 369 | 0.2725 | 0.1974 | +0.0751 ± 0.0146 | 0.7637 | 0.5739 | 0.6701 | 0.3562 | 0.3957 | -0.137 ± 0.023 | -0.025 (2) |
| 40+ | 138 | 0.3457 | 0.1908 | +0.1549 ± 0.0359 | 0.972 | 0.556 | 0.7536 | 0.277 | 0.3696 | -0.058 ± 0.0354 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1614 | 0.1818 | 0.1822 | -0.0004 ± 0.0004 | 0.5395 | 0.5402 | 0.4925 | 0.478 | 0.5006 | -0.032 ± 0.011 | -0.0217 (6) |
| 3-5 | 1027 | 0.1954 | 0.1948 | +0.0006 ± 0.0011 | 0.566 | 0.5645 | 0.5163 | 0.4764 | 0.4878 | -0.039 ± 0.014 | 0.02 (1) |
| 5-10 | 2220 | 0.1883 | 0.1855 | +0.0028 ± 0.0014 | 0.5581 | 0.5475 | 0.5138 | 0.44 | 0.4599 | -0.044 ± 0.0093 | -0.01 (5) |
| 10-15 | 1945 | 0.1974 | 0.1824 | +0.0150 ± 0.0024 | 0.5809 | 0.5347 | 0.5226 | 0.3983 | 0.4031 | -0.066 ± 0.0098 | -0.02 (14) |
| 15-25 | 2771 | 0.2137 | 0.1748 | +0.0389 ± 0.0031 | 0.6228 | 0.5169 | 0.5349 | 0.3391 | 0.3414 | -0.075 ± 0.008 | -0.0026 (27) |
| 25-40 | 2421 | 0.2489 | 0.1364 | +0.1125 ± 0.0048 | 0.7073 | 0.4164 | 0.5617 | 0.2459 | 0.2276 | -0.089 ± 0.0075 | -0.015 (6) |
| 40+ | 1880 | 0.4024 | 0.0679 | +0.3345 ± 0.0068 | 1.0546 | 0.2372 | 0.6669 | 0.13 | 0.1011 | -0.070 ± 0.0059 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 370 | 0.1946 | 0.1972 | -0.0026 ± 0.0008 | 0.5687 | 0.5755 | 0.4993 | 0.4842 | 0.5622 | -0.003 ± 0.0233 | -0.0133 (6) |
| 3-5 | 260 | 0.1876 | 0.1868 | +0.0008 ± 0.0021 | 0.551 | 0.5492 | 0.5018 | 0.4625 | 0.4731 | -0.102 ± 0.0282 | -0.01 (1) |
| 5-10 | 542 | 0.2004 | 0.1988 | +0.0017 ± 0.0029 | 0.5877 | 0.5812 | 0.5086 | 0.4348 | 0.4557 | -0.090 ± 0.0199 | -0.01 (4) |
| 10-15 | 417 | 0.2111 | 0.2124 | -0.0013 ± 0.0055 | 0.611 | 0.6079 | 0.5362 | 0.4137 | 0.482 | -0.063 ± 0.0225 | -0.044 (5) |
| 15-25 | 492 | 0.2324 | 0.2094 | +0.0230 ± 0.008 | 0.6647 | 0.6036 | 0.5811 | 0.3882 | 0.4268 | -0.105 ± 0.0204 | -0.03 (1) |
| 25-40 | 285 | 0.2014 | 0.2071 | -0.0057 ± 0.0157 | 0.586 | 0.5936 | 0.6527 | 0.341 | 0.5018 | -0.044 ± 0.0232 | 0.0 (1) |
| 40+ | 54 | 0.3218 | 0.1811 | +0.1407 ± 0.0526 | 0.8688 | 0.5393 | 0.7515 | 0.2988 | 0.3704 | -0.143 ± 0.0544 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1757 | 0.1841 | 0.185 | -0.0010 ± 0.0004 | 0.5438 | 0.5455 | 0.4872 | 0.4722 | 0.5043 | -0.022 ± 0.0103 | -0.0183 (23) |
| 3-5 | 1217 | 0.1853 | 0.183 | +0.0022 ± 0.001 | 0.5464 | 0.541 | 0.4801 | 0.4407 | 0.4322 | -0.072 ± 0.0127 | -0.0243 (7) |
| 5-10 | 2712 | 0.1917 | 0.1869 | +0.0047 ± 0.0012 | 0.5665 | 0.5506 | 0.4812 | 0.4074 | 0.4111 | -0.059 ± 0.0084 | -0.01 (18) |
| 10-15 | 2075 | 0.1955 | 0.1819 | +0.0136 ± 0.0023 | 0.5754 | 0.5328 | 0.4931 | 0.37 | 0.3759 | -0.063 ± 0.0093 | -0.03 (9) |
| 15-25 | 2696 | 0.2094 | 0.171 | +0.0384 ± 0.0031 | 0.6137 | 0.5065 | 0.5027 | 0.3074 | 0.3093 | -0.070 ± 0.008 | -0.03 (2) |
| 25-40 | 2061 | 0.2129 | 0.1199 | +0.0931 ± 0.0048 | 0.617 | 0.3715 | 0.5231 | 0.2064 | 0.2213 | -0.059 ± 0.0072 | 0.0 (1) |
| 40+ | 1360 | 0.3853 | 0.0462 | +0.3391 ± 0.0065 | 1.0074 | 0.1803 | 0.6306 | 0.1082 | 0.0559 | -0.088 ± 0.0055 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 677 | 0.2024 | 0.2032 | -0.0008 ± 0.0006 | 0.5873 | 0.5889 | 0.5001 | 0.4851 | 0.5052 | -0.032 ± 0.0173 | -0.0226 (46) |
| 3-5 | 493 | 0.1994 | 0.1986 | +0.0008 ± 0.0016 | 0.5793 | 0.5756 | 0.4796 | 0.4399 | 0.4483 | -0.048 ± 0.0201 | -0.0058 (33) |
| 5-10 | 1022 | 0.1914 | 0.1856 | +0.0058 ± 0.002 | 0.5666 | 0.5516 | 0.4792 | 0.4057 | 0.4041 | -0.064 ± 0.0137 | -0.0049 (73) |
| 10-15 | 652 | 0.2039 | 0.1946 | +0.0093 ± 0.0043 | 0.596 | 0.5709 | 0.495 | 0.3721 | 0.3942 | -0.045 ± 0.0173 | 0.0014 (64) |
| 15-25 | 871 | 0.2353 | 0.2102 | +0.0252 ± 0.0061 | 0.67 | 0.6059 | 0.554 | 0.3598 | 0.3938 | -0.059 ± 0.0156 | -0.0216 (58) |
| 25-40 | 496 | 0.2538 | 0.1909 | +0.0629 ± 0.0122 | 0.7152 | 0.557 | 0.6418 | 0.3285 | 0.3831 | -0.090 ± 0.0184 | -0.0216 (25) |
| 40+ | 168 | 0.3597 | 0.1922 | +0.1675 ± 0.0346 | 1.0498 | 0.565 | 0.7921 | 0.2982 | 0.3988 | -0.068 ± 0.0309 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2123 | 0.1915 | 0.1917 | -0.0003 ± 0.0003 | 0.5589 | 0.5585 | 0.502 | 0.4867 | 0.5002 | -0.031 ± 0.0095 | -0.0155 (82) |
| 3-5 | 1457 | 0.1904 | 0.1878 | +0.0026 ± 0.0009 | 0.5558 | 0.5494 | 0.4858 | 0.4462 | 0.4345 | -0.058 ± 0.0114 | -0.0148 (63) |
| 5-10 | 2973 | 0.1898 | 0.1819 | +0.0079 ± 0.0012 | 0.5631 | 0.5408 | 0.4756 | 0.4019 | 0.3885 | -0.066 ± 0.0079 | -0.0087 (125) |
| 10-15 | 2007 | 0.1992 | 0.186 | +0.0132 ± 0.0024 | 0.5848 | 0.5499 | 0.5048 | 0.3818 | 0.3896 | -0.051 ± 0.0096 | -0.0053 (105) |
| 15-25 | 2536 | 0.231 | 0.1981 | +0.0329 ± 0.0035 | 0.6663 | 0.5757 | 0.5513 | 0.3563 | 0.3711 | -0.062 ± 0.0089 | -0.0255 (106) |
| 25-40 | 1720 | 0.2539 | 0.1654 | +0.0885 ± 0.0062 | 0.7208 | 0.4901 | 0.6037 | 0.2888 | 0.3081 | -0.080 ± 0.0095 | -0.0206 (47) |
| 40+ | 844 | 0.3857 | 0.1247 | +0.2610 ± 0.0131 | 1.0972 | 0.3845 | 0.7068 | 0.1977 | 0.2097 | -0.074 ± 0.0115 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2420 | 1.063 ± 0.057 | 1.184 | 0.1686 | 0.1693 | 0.2105 | 0.2023 |
| gen2 | 2420 | 0.866 ± 0.051 | 1.124 | 0.1832 | 0.1689 | 0.2278 | 0.2021 |
| gen1_elo | 2420 | 1.051 ± 0.056 | 1.171 | 0.1729 | 0.1697 | 0.2093 | 0.2023 |
| gen1_sr | 2420 | 1.066 ± 0.065 | 1.209 | 0.142 | 0.1709 | 0.2234 | 0.2018 |
| gen1_ledger | 4379 | 0.869 ± 0.038 | 1.079 | 0.1747 | 0.1873 | 0.2181 | 0.1969 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 12,058)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,194 | 26.5% |
| STALE_QUOTE | market_freshness | 2,379 | 19.7% |
| BOOK_QUALITY | execution | 2,177 | 18.1% |
| POOR_DATA | data | 1,268 | 10.5% |
| LIMITED_DATA | data | 935 | 7.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 672 | 5.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 576 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 395 | 3.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 361 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 101 | 0.8% |

Cause class: coverage 26.5%, market_freshness 19.7%, data 18.3%, execution 18.1%, market_freshness/coverage 8.6%, model_calibration_or_unknown 4.8%, mapping 3.3%, model_calibration 0.8%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.5%, START_UNVERIFIABLE 95.7%, LOW_DATA_QUALITY 67.8%, STALE_PLAYER_DATA 56.6%, THIN_PLAYER_HISTORY 56.2%, STALE_KALSHI_QUOTE 45.8%, MODEL_INTERNAL_DISAGREEMENT 37.9%, ASYMMETRIC_SAMPLE_SIZE 30.4%, WIDE_SPREAD 23.9%, MODEL_HIGH_UNCERTAINTY 16.4%, PLAYER_IDENTITY_RISK 11.9%, LEVEL_TRANSFER_RISK 9.0%, EVENT_MAPPING_RISK 7.8%, LOW_DISPLAYED_LIQUIDITY 7.4%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 1.4%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 29.0%, POST_SETTLEMENT_OBSERVATION 26.5%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### >= ge_25 pp (N = 6,484)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,523 | 38.9% |
| BOOK_QUALITY | execution | 1,138 | 17.5% |
| STALE_QUOTE | market_freshness | 1,049 | 16.2% |
| POOR_DATA | data | 523 | 8.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 364 | 5.6% |
| LIMITED_DATA | data | 274 | 4.2% |
| IDENTITY_AMBIGUOUS | mapping | 243 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 224 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 123 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 23 | 0.4% |

Cause class: coverage 38.9%, execution 17.5%, market_freshness 16.2%, data 12.3%, market_freshness/coverage 9.1%, mapping 3.8%, model_calibration_or_unknown 1.9%, model_calibration 0.4%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.2%, START_UNVERIFIABLE 98.1%, LOW_DATA_QUALITY 71.5%, THIN_PLAYER_HISTORY 58.5%, STALE_KALSHI_QUOTE 54.0%, STALE_PLAYER_DATA 51.2%, MODEL_INTERNAL_DISAGREEMENT 39.1%, ASYMMETRIC_SAMPLE_SIZE 32.6%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 17.5%, PLAYER_IDENTITY_RISK 15.1%, EVENT_MAPPING_RISK 9.7%, LEVEL_TRANSFER_RISK 7.8%, LOW_DISPLAYED_LIQUIDITY 7.6%, MODEL_CALIBRATION_OUTLIER 4.7%, EXTERNAL_MARKET_REJECTION 0.7%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 41.8%, POST_SETTLEMENT_OBSERVATION 38.9%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.7%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 5338, "IDENTITY_AMBIGUOUS": 1146}; ticker orientation: {"VERIFIED": 6484}.

Checks: discipline:AMBIGUOUS 459, discipline:PASS 6025, identity_confidence:AMBIGUOUS 980, identity_confidence:PASS 5504, level_mapping:NA 471, level_mapping:PASS 6013, market_pair:AMBIGUOUS 226, market_pair:NA 155, market_pair:PASS 6103, model_complement:NA 122, model_complement:PASS 6362, namesake:PASS 6484, physical_match_id:NA 2639, physical_match_id:PASS 3845, player_ids:PASS 6484, same_pair_other_event:PASS 6484, ticker_orientation:PASS 6484

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,999 | 1.5% | 1.4% | 0.4% | {"market_freshness": 20, "execution": 8, "market_freshness/coverage": 1} | 5.28 | 0.2127 / 0.2136 (235) | 16.6% | 0.4% | 5.5% | 1.7% |
| CHALLENGER | 4,777 | 16.9% | 5.9% | 12.4% | {"coverage": 482, "market_freshness": 109, "market_freshness/coverage": 102, "data": 49, "model_calibration_or_unknown": 42, "execution": 12, "mapping": 6, "model_calibration": 4} | 7.2 | 0.2162 / 0.2025 (1136) | 38.8% | 8.3% | 2.3% | 21.7% |
| DOUBLES | 913 | 50.3% | 49.8% | 7.1% | {"execution": 176, "mapping": 139, "market_freshness": 106, "market_freshness/coverage": 31, "coverage": 7} | 24.68 | 0.3377 / 0.23 (256) | 25.6% | 0.0% | 100.0% | 7.3% |
| ITF_MEN | 8,601 | 23.6% | 15.4% | 31.4% | {"coverage": 850, "execution": 423, "market_freshness": 278, "data": 275, "market_freshness/coverage": 182, "mapping": 23, "model_calibration_or_unknown": 2} | 10.45 | 0.2114 / 0.1937 (2143) | 37.3% | 54.4% | 7.1% | 24.3% |
| ITF_WOMEN | 11,021 | 26.3% | 18.0% | 44.7% | {"coverage": 1167, "execution": 499, "market_freshness": 466, "data": 439, "market_freshness/coverage": 227, "mapping": 69, "model_calibration_or_unknown": 24, "model_calibration": 9} | 12.27 | 0.205 / 0.1935 (2379) | 38.5% | 57.9% | 9.7% | 24.0% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,464 | 6.3% | 5.5% | 1.4% | {"market_freshness": 36, "model_calibration_or_unknown": 20, "data": 11, "market_freshness/coverage": 10, "execution": 6, "model_calibration": 4, "coverage": 4, "mapping": 1} | 7.76 | 0.221 / 0.2181 (221) | 27.4% | 1.4% | 1.8% | 3.2% |
| WTA125 | 1,141 | 13.4% | 10.5% | 2.4% | {"market_freshness/coverage": 34, "model_calibration_or_unknown": 33, "market_freshness": 32, "data": 23, "coverage": 12, "execution": 9, "model_calibration": 6, "mapping": 4} | 9.26 | 0.225 / 0.2139 (387) | 23.8% | 8.0% | 4.1% | 10.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 5 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 6 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 17.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1037 min (STALE); no external reference |
| 7 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 8 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 9 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 10 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 11 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 12 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 13 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 14 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 15 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 16 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 18 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 19 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 20 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 21 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 22 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 23 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 24 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 25 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 26 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 27 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 28 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 29 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 30 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 31 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 32 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 33 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 34 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 64 min (STALE); no external reference |
| 35 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 36 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 37 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 110 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 38 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 39 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 40 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 253 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 41 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 42 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 43 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 44 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 45 | `KXITFWMATCH-26OCT08ARISAV-SAV` | ITF_WOMEN | fair_v1 | 75% / 2% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 46 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 47 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.2h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 141 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 48 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 49 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 50 | `KXITFMATCH-26OCT09DELSTE-DEL` | ITF_MEN | fair_v1 | 78% / 6% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.9h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 780 min (STALE); data POOR (grade F, thinner serve sample 477.0, ratio 8.93); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9814, "by_level_share_of_ge_25pp": {"ATP": 0.0045, "CHALLENGER": 0.1243, "DOUBLES": 0.0708, "ITF_MEN": 0.3135, "ITF_WOMEN": 0.4473, "OTHER": 0.0019, "WTA": 0.0142, "WTA125": 0.0236}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5403, "share_primary_cause_market_settled_or_in_play": 0.4797, "share_primary_cause_stale_quote_only": 0.1618}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 6484, "identity_ambiguous_share": 0.1767, "ticker_orientation": {"VERIFIED": 6484}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 3845, "with_external": 110, "coverage": 0.0286, "external_status": {"EXTERNAL_STALE": 76, "AGREES_WITH_KALSHI": 32, "SUPPORTS_MODEL_DIRECTION": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 76, "MODEL_LONE_OUTLIER": 32, "ALL_THREE_DISAGREE": 2}, "share_external_agrees_with_kalshi": 0.2909, "share_external_supports_model": 0.0182}, "pregame_clean_ge_25pp": {"n": 1657, "with_external": 104, "coverage": 0.0628, "external_status": {"EXTERNAL_STALE": 72, "AGREES_WITH_KALSHI": 30, "SUPPORTS_MODEL_DIRECTION": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 72, "MODEL_LONE_OUTLIER": 30, "ALL_THREE_DISAGREE": 2}, "share_external_agrees_with_kalshi": 0.2885, "share_external_supports_model": 0.0192}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 611.0, "median_sample_ratio": 2.31, "median_min_matches": 21.0, "median_max_days_since_last": 198.0, "share_severe_asymmetry": 0.1851, "data_status": {"POOR": 3333, "LIMITED": 1951, "ADEQUATE": 1200}, "comparison_lt_10pp": {"median_thinner_serve_points": 1905.0, "median_sample_ratio": 1.66, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 509, "model_minus_observed": 0.0563, "kalshi_minus_observed": -0.0753, "brier_diff_model_minus_kalshi": 0.0019}, "4-10x": {"n": 343, "model_minus_observed": 0.0628, "kalshi_minus_observed": -0.0774, "brier_diff_model_minus_kalshi": 0.0029}, "<2x": {"n": 1218, "model_minus_observed": 0.0792, "kalshi_minus_observed": -0.0413, "brier_diff_model_minus_kalshi": 0.0106}, ">=10x": {"n": 350, "model_minus_observed": 0.1137, "kalshi_minus_observed": -0.0551, "brier_diff_model_minus_kalshi": 0.0142}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2420, "model": {"intercept": -0.54, "slope": 0.866, "slope_se": 0.051}, "kalshi_mid_same_rows": {"intercept": 0.224, "slope": 1.124, "slope_se": 0.059}, "mean_extremity_model": 0.1832, "mean_extremity_kalshi": 0.1689, "model_brier": 0.2278, "kalshi_brier": 0.2021, "brier_diff_model_minus_kalshi": 0.0257, "brier_diff_se": 0.0038, "model_logloss": 0.6512, "kalshi_logloss": 0.5863}, "fair_v1": {"n": 2420, "model": {"intercept": -0.381, "slope": 1.063, "slope_se": 0.057}, "kalshi_mid_same_rows": {"intercept": 0.334, "slope": 1.184, "slope_se": 0.061}, "mean_extremity_model": 0.1686, "mean_extremity_kalshi": 0.1693, "model_brier": 0.2105, "kalshi_brier": 0.2023, "brier_diff_model_minus_kalshi": 0.0082, "brier_diff_se": 0.003, "model_logloss": 0.6083, "kalshi_logloss": 0.5866}, "gen1_elo": {"n": 2420, "model": {"intercept": -0.357, "slope": 1.051, "slope_se": 0.056}, "kalshi_mid_same_rows": {"intercept": 0.338, "slope": 1.171, "slope_se": 0.059}, "mean_extremity_model": 0.1729, "mean_extremity_kalshi": 0.1697, "model_brier": 0.2093, "kalshi_brier": 0.2023, "brier_diff_model_minus_kalshi": 0.007, "brier_diff_se": 0.003, "model_logloss": 0.6066, "kalshi_logloss": 0.5866}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2407, "share_ge_15": 0.4266, "median_abs_gap": 12.67, "n": 15971}, "gen1_elo": {"share_ge_25": 0.2347, "share_ge_15": 0.4214, "median_abs_gap": 12.09, "n": 15971}, "gen1_sr": {"share_ge_25": 0.2934, "share_ge_15": 0.5089, "median_abs_gap": 15.35, "n": 15971}, "gen2": {"share_ge_25": 0.2975, "share_ge_15": 0.4982, "median_abs_gap": 14.94, "n": 15971}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1368, "share_ge_15": 0.3274, "median_abs_gap": 10.18, "n": 12109}, "gen1_elo": {"share_ge_25": 0.1348, "share_ge_15": 0.319, "median_abs_gap": 9.58, "n": 12108}, "gen1_sr": {"share_ge_25": 0.1891, "share_ge_15": 0.4191, "median_abs_gap": 12.52, "n": 12109}, "gen2": {"share_ge_25": 0.2072, "share_ge_15": 0.4219, "median_abs_gap": 12.43, "n": 12110}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.28, "share_ge_25_all": 0.0145, "share_ge_25_pregame_clean": 0.0142}, "WTA": {"median_abs_gap_pregame_clean": 7.76, "share_ge_25_all": 0.0628, "share_ge_25_pregame_clean": 0.055}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2426, "share_within_10pp_all": 0.4448, "share_within_10pp_pregame_clean": 0.5071, "corr_model_vs_mid_pregame_clean": 0.852}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 375, "model_brier": 0.1922, "kalshi_brier": 0.1935, "brier_diff_model_minus_kalshi": -0.0013}, "10-15": {"n_settled": 434, "model_brier": 0.2122, "kalshi_brier": 0.2045, "brier_diff_model_minus_kalshi": 0.0077}, "15-25": {"n_settled": 515, "model_brier": 0.228, "kalshi_brier": 0.216, "brier_diff_model_minus_kalshi": 0.012}, "25-40": {"n_settled": 280, "model_brier": 0.219, "kalshi_brier": 0.2012, "brier_diff_model_minus_kalshi": 0.0178}, "3-5": {"n_settled": 246, "model_brier": 0.1914, "kalshi_brier": 0.1929, "brier_diff_model_minus_kalshi": -0.0015}, "40+": {"n_settled": 62, "model_brier": 0.2951, "kalshi_brier": 0.1745, "brier_diff_model_minus_kalshi": 0.1206}, "5-10": {"n_settled": 508, "model_brier": 0.1991, "kalshi_brier": 0.2016, "brier_diff_model_minus_kalshi": -0.0025}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.54, "slope": 0.866, "slope_se": 0.051}, "kalshi_slope": {"intercept": 0.224, "slope": 1.124, "slope_se": 0.059}, "n": 2420}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.515, "slope": 0.869, "slope_se": 0.038}, "kalshi_slope": {"intercept": 0.147, "slope": 1.079, "slope_se": 0.042}, "n": 4379}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 256, "model_brier": 0.3377, "kalshi_brier": 0.23, "brier_diff_model_minus_kalshi": 0.1077, "brier_diff_se": 0.0203, "corr_model_outcome": -0.035, "corr_kalshi_outcome": 0.2806}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
