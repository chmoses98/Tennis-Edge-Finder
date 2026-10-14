# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-14T22:15Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 33,042): 0-3 14.4%, 3-5 9.5%, 5-10 20.1%, 10-15 15.3%, 15-25 18.8%, 25-40 13.6%, 40+ 8.2%; median gap 11.84 pp.
* **Where the extremes live**: 98.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.6%, Challenger 12.3%, doubles 7.0%). Main tour: ATP 1.4% and WTA 6.2% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 7,213): MARKET_ALREADY_SETTLED_WHEN_PRICED 37.7%, BOOK_QUALITY 17.5%, STALE_QUOTE 16.8%, POOR_DATA 8.3%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 4.0%, IN_PLAY_QUOTE 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.4%. By class: coverage 37.7%, execution 17.5%, market_freshness 16.8%, data 12.3%, market_freshness/coverage 8.9%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.4%.
* **Stale / settled / in-play**: 53.5% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 46.6% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 7,213 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.7% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 3.4%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 21.8% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 562.0 points vs 1811.5 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.061, Gen-2 0.867, Gen-1 ledger 0.87 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 342 model 0.2279 vs Kalshi 0.208; n 72 model 0.29 vs Kalshi 0.1741.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 130,919 model-market comparisons (217,239 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 46,934 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-14T22:04:34.647667+00:00'], shadow board 35,902 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-14T22:04:39.515469+00:00'], Model 4 14,127 rows, 14,409 settled tickers, 4,517 tickers with an external scan.
* By model: {"gen1_ledger": 30820, "gen1_elo": 18043, "fair_v1": 18043, "gen2": 18043, "gen1_sr": 18043, "model4_fundamental": 13968, "model4_conditioned": 13959}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 33,042 | 14.4 | 9.5 | 20.1 | 15.3 | 18.8 | 13.6 | 8.2 | 11.84 | 40.6% | 21.8% |
| MW fair_v1 | 18,043 | 13.6 | 8.5 | 18.6 | 15.9 | 19.1 | 14.5 | 9.8 | 12.92 | 43.5% | 24.3% |
| MW gen1_elo | 18,043 | 13.2 | 9.0 | 19.9 | 15.2 | 19.0 | 14.4 | 9.4 | 12.44 | 42.8% | 23.8% |
| MW gen1_ledger | 14,999 | 15.5 | 10.7 | 21.9 | 14.7 | 18.4 | 12.4 | 6.4 | 10.46 | 37.2% | 18.8% |
| MW gen1_sr | 18,043 | 9.8 | 7.6 | 16.3 | 14.2 | 21.8 | 18.4 | 11.8 | 15.71 | 52.0% | 30.2% |
| MW gen2 | 18,043 | 11.6 | 7.1 | 16.3 | 14.3 | 20.4 | 17.2 | 13.1 | 15.37 | 50.7% | 30.3% |
| all families model4_conditioned | 13,959 | 21.6 | 20.1 | 35.4 | 16.6 | 4.3 | 1.1 | 0.9 | 5.82 | 6.3% | 2.0% |
| all families model4_fundamental | 13,968 | 16.7 | 13.5 | 35.7 | 19.7 | 10.6 | 2.6 | 1.1 | 7.59 | 14.3% | 3.7% |

Configurable thresholds (primary): >=5pp 76.1%, >=10pp 56.0%, >=15pp 40.6%, >=20pp 30.1%, >=25pp 21.8%, >=30pp 15.9%, >=40pp 8.2%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.46pp; >=10pp 45.3%, >=25pp 17.5%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,325 | 30.4 | 14.6 | 25.1 | 17.6 | 10.3 | 1.1 | 0.8 | 5.71 | 12.3% | 2.0% |
| CHALLENGER | 3,103 | 15.4 | 10.0 | 20.1 | 15.8 | 14.8 | 12.2 | 11.8 | 11.66 | 38.7% | 23.9% |
| ITF_MEN | 5,098 | 11.2 | 8.3 | 17.8 | 14.9 | 19.4 | 16.1 | 12.3 | 14.14 | 47.8% | 28.4% |
| ITF_WOMEN | 7,016 | 10.4 | 6.5 | 16.1 | 15.9 | 22.2 | 18.2 | 10.6 | 15.43 | 51.0% | 28.8% |
| WTA | 924 | 21.6 | 10.7 | 24.7 | 15.8 | 20.4 | 5.6 | 1.2 | 8.16 | 27.2% | 6.8% |
| WTA125 | 577 | 12.7 | 7.6 | 22.5 | 21.3 | 20.1 | 13.9 | 1.9 | 11.33 | 35.9% | 15.8% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,325 | 24.6 | 14.4 | 24.7 | 18.9 | 14.5 | 1.9 | 1.0 | 6.59 | 17.4% | 2.9% |
| CHALLENGER | 3,103 | 14.9 | 7.5 | 19.4 | 13.5 | 18.2 | 14.2 | 12.3 | 12.78 | 44.7% | 26.5% |
| ITF_MEN | 5,098 | 9.7 | 6.9 | 16.0 | 14.2 | 20.0 | 18.4 | 14.8 | 16.3 | 53.3% | 33.3% |
| ITF_WOMEN | 7,016 | 8.8 | 5.8 | 13.1 | 13.3 | 22.0 | 20.6 | 16.4 | 18.74 | 59.0% | 37.0% |
| WTA | 924 | 17.9 | 8.0 | 18.7 | 16.3 | 22.9 | 14.9 | 1.2 | 12.08 | 39.1% | 16.1% |
| WTA125 | 577 | 6.1 | 4.2 | 17.5 | 17.7 | 25.8 | 19.2 | 9.5 | 17.24 | 54.6% | 28.8% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,325 | 27.7 | 14.5 | 28.7 | 15.4 | 10.3 | 2.5 | 0.9 | 6.03 | 13.7% | 3.4% |
| CHALLENGER | 3,103 | 14.8 | 10.2 | 20.3 | 15.2 | 15.7 | 11.8 | 12.0 | 11.2 | 39.5% | 23.8% |
| ITF_MEN | 5,098 | 10.2 | 8.2 | 18.5 | 14.1 | 20.1 | 16.4 | 12.5 | 14.53 | 49.0% | 28.9% |
| ITF_WOMEN | 7,016 | 9.9 | 6.8 | 16.5 | 15.8 | 22.8 | 18.5 | 9.6 | 15.43 | 50.9% | 28.1% |
| WTA | 924 | 22.3 | 15.7 | 32.7 | 15.9 | 10.5 | 2.2 | 0.8 | 6.14 | 13.4% | 2.9% |
| WTA125 | 577 | 22.4 | 12.1 | 29.5 | 15.1 | 14.4 | 6.2 | 0.3 | 7.55 | 21.0% | 6.6% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 722 | 31.0 | 22.7 | 35.6 | 9.0 | 1.2 | 0.4 | 0.0 | 4.7 | 1.7% | 0.4% |
| CHALLENGER | 2,117 | 22.1 | 15.4 | 27.5 | 14.9 | 13.1 | 5.0 | 2.0 | 7.0 | 20.1% | 7.0% |
| DOUBLES | 998 | 5.2 | 3.6 | 11.6 | 10.6 | 18.7 | 24.2 | 25.9 | 25.22 | 68.9% | 50.2% |
| ITF_MEN | 4,613 | 14.7 | 8.5 | 20.8 | 15.4 | 20.7 | 12.5 | 7.4 | 11.87 | 40.6% | 19.9% |
| ITF_WOMEN | 5,071 | 11.7 | 9.3 | 19.6 | 14.7 | 22.3 | 16.6 | 5.7 | 13.01 | 44.7% | 22.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 653 | 21.3 | 15.3 | 27.3 | 17.1 | 13.6 | 4.9 | 0.5 | 7.52 | 19.0% | 5.4% |
| WTA125 | 676 | 20.6 | 13.6 | 22.6 | 18.5 | 14.3 | 8.1 | 2.2 | 8.25 | 24.7% | 10.4% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,311 | 30.4 | 14.6 | 25.2 | 17.6 | 10.3 | 1.1 | 0.8 | 5.8 | 12.2% | 1.9% |
| CHALLENGER | 2,213 | 20.0 | 12.5 | 25.3 | 18.6 | 15.4 | 5.9 | 2.4 | 8.36 | 23.7% | 8.3% |
| ITF_MEN | 3,661 | 13.8 | 10.2 | 21.3 | 16.8 | 19.8 | 12.7 | 5.4 | 11.23 | 37.9% | 18.1% |
| ITF_WOMEN | 5,133 | 12.6 | 8.1 | 18.5 | 18.4 | 23.6 | 14.9 | 4.0 | 12.83 | 42.4% | 18.9% |
| WTA | 908 | 21.8 | 10.0 | 25.1 | 16.0 | 20.4 | 5.5 | 1.2 | 8.18 | 27.1% | 6.7% |
| WTA125 | 553 | 13.0 | 7.4 | 21.9 | 21.7 | 20.8 | 13.7 | 1.4 | 11.33 | 36.0% | 15.2% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,311 | 24.5 | 14.5 | 24.8 | 18.9 | 14.5 | 1.8 | 1.0 | 6.7 | 17.3% | 2.8% |
| CHALLENGER | 2,213 | 19.1 | 9.6 | 24.2 | 16.4 | 18.6 | 9.6 | 2.5 | 9.16 | 30.7% | 12.2% |
| ITF_MEN | 3,662 | 11.6 | 8.3 | 18.4 | 16.1 | 22.1 | 15.7 | 7.8 | 13.53 | 45.6% | 23.5% |
| ITF_WOMEN | 5,133 | 10.1 | 6.8 | 14.8 | 14.5 | 24.3 | 19.5 | 10.0 | 16.32 | 53.8% | 29.5% |
| WTA | 908 | 17.7 | 7.8 | 18.7 | 16.6 | 22.9 | 15.0 | 1.2 | 12.12 | 39.1% | 16.2% |
| WTA125 | 553 | 5.8 | 4.3 | 17.5 | 18.1 | 25.7 | 19.9 | 8.7 | 17.24 | 54.2% | 28.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 702 | 31.1 | 22.9 | 35.9 | 9.1 | 0.6 | 0.4 | 0.0 | 4.69 | 1.0% | 0.4% |
| CHALLENGER | 1,824 | 23.9 | 16.8 | 29.6 | 14.7 | 12.2 | 2.2 | 0.6 | 6.37 | 15.0% | 2.8% |
| DOUBLES | 921 | 5.3 | 3.7 | 11.9 | 10.6 | 19.0 | 24.1 | 25.3 | 24.32 | 68.4% | 49.4% |
| ITF_MEN | 3,789 | 16.2 | 9.3 | 22.7 | 16.3 | 20.6 | 10.4 | 4.4 | 10.52 | 35.4% | 14.9% |
| ITF_WOMEN | 4,142 | 12.9 | 10.0 | 21.5 | 15.5 | 22.6 | 15.0 | 2.6 | 11.56 | 40.1% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 619 | 21.8 | 16.0 | 27.5 | 17.1 | 13.9 | 3.7 | 0.0 | 7.21 | 17.6% | 3.7% |
| WTA125 | 572 | 22.6 | 15.0 | 24.1 | 20.1 | 12.8 | 5.1 | 0.3 | 7.33 | 18.2% | 5.4% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 998 | 5.2 | 3.6 | 11.6 | 10.6 | 18.7 | 24.2 | 25.9 | 25.22 | 68.9% | 50.2% |
| singles | 14,001 | 16.2 | 11.2 | 22.7 | 14.9 | 18.4 | 11.6 | 5.0 | 9.96 | 35.0% | 16.6% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 4,219 | 13.2 | 8.9 | 19.6 | 16.0 | 17.9 | 14.4 | 9.9 | 12.65 | 42.3% | 24.3% |
| Grass | 177 | 11.3 | 12.4 | 15.2 | 15.2 | 21.5 | 18.1 | 6.2 | 14.16 | 45.8% | 24.3% |
| Hard | 11,806 | 14.0 | 8.4 | 18.6 | 15.5 | 19.5 | 14.3 | 9.8 | 12.85 | 43.5% | 24.1% |
| UNKNOWN | 1,841 | 12.0 | 7.4 | 16.6 | 18.6 | 19.2 | 15.9 | 10.3 | 13.49 | 45.5% | 26.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,351 | 19.7 | 10.7 | 20.9 | 16.9 | 15.8 | 8.9 | 7.0 | 9.56 | 31.8% | 15.9% |
| B | 2,357 | 14.5 | 9.0 | 20.0 | 16.6 | 18.2 | 12.1 | 9.6 | 11.56 | 39.9% | 21.7% |
| C | 2,596 | 13.0 | 9.4 | 19.8 | 14.8 | 19.3 | 14.3 | 9.3 | 12.61 | 43.0% | 23.6% |
| D | 3,157 | 11.2 | 8.1 | 17.8 | 16.0 | 22.1 | 15.4 | 9.4 | 13.83 | 46.9% | 24.8% |
| F | 4,582 | 7.9 | 5.3 | 14.9 | 15.0 | 21.3 | 21.9 | 13.7 | 18.07 | 56.9% | 35.6% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,343 | 22.8 | 15.8 | 28.9 | 15.2 | 11.3 | 4.4 | 1.7 | 6.7 | 17.4% | 6.1% |
| B | 2,262 | 14.8 | 10.0 | 24.1 | 16.4 | 19.4 | 11.0 | 4.2 | 10.19 | 34.7% | 15.2% |
| C | 2,960 | 12.2 | 7.7 | 18.4 | 14.1 | 20.2 | 15.6 | 11.7 | 13.66 | 47.6% | 27.3% |
| D | 2,268 | 14.0 | 9.8 | 20.7 | 13.7 | 21.3 | 13.9 | 6.6 | 11.86 | 41.8% | 20.5% |
| F | 3,166 | 10.1 | 7.5 | 15.1 | 13.9 | 23.7 | 20.4 | 9.2 | 16.43 | 53.3% | 29.6% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 5,970 | 18.1 | 9.7 | 20.2 | 16.7 | 16.2 | 9.9 | 9.2 | 10.52 | 35.3% | 19.1% |
| LIMITED | 4,247 | 15.1 | 10.3 | 20.9 | 15.7 | 18.6 | 12.5 | 6.9 | 11.09 | 38.0% | 19.4% |
| POOR | 7,826 | 9.3 | 6.5 | 16.1 | 15.5 | 21.6 | 19.1 | 11.9 | 15.99 | 52.6% | 31.0% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,018 | 31.3 | 24.5 | 36.4 | 5.4 | 1.8 | 0.7 | 0.1 | 4.49 | 2.5% | 0.7% |
| GAME_SPREAD | 2,876 | 25.8 | 15.9 | 36.8 | 16.8 | 4.1 | 0.4 | 0.2 | 5.99 | 4.7% | 0.6% |
| MATCH_WINNER | 14,999 | 15.5 | 10.7 | 21.9 | 14.7 | 18.4 | 12.4 | 6.4 | 10.46 | 37.2% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 5,501 | 33.4 | 19.5 | 31.0 | 9.6 | 5.1 | 1.1 | 0.2 | 4.72 | 6.5% | 1.4% |
| TOTAL_GAMES | 4,402 | 6.7 | 9.1 | 39.2 | 29.6 | 10.4 | 2.7 | 2.3 | 9.45 | 15.4% | 5.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,893 | 25.6 | 38.2 | 31.5 | 0.3 | 3.9 | 0.4 | 0.1 | 4.3 | 4.4% | 0.5% |
| GAME_SPREAD | 3,489 | 45.3 | 16.4 | 28.9 | 7.3 | 1.1 | 0.7 | 0.4 | 3.56 | 2.2% | 1.1% |
| TOTAL_GAMES | 5,577 | 3.4 | 6.5 | 42.8 | 36.7 | 6.8 | 1.9 | 1.9 | 9.77 | 10.6% | 3.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,893 | 26.3 | 18.8 | 37.1 | 9.1 | 6.2 | 2.1 | 0.3 | 5.48 | 8.6% | 2.4% |
| GAME_SPREAD | 3,489 | 19.4 | 13.4 | 30.3 | 21.0 | 12.9 | 2.3 | 0.7 | 7.76 | 15.9% | 3.0% |
| TOTAL_GAMES | 5,586 | 6.6 | 8.9 | 37.9 | 28.2 | 13.1 | 3.2 | 2.1 | 9.66 | 18.4% | 5.3% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 18,043 | 43.5% | 24.3% | 12.92 | 34.1% | 14.4% | 10.5 |
| gen1_elo | 18,043 | 42.8% | 23.8% | 12.44 | 33.0% | 14.2% | 9.99 |
| gen1_sr | 18,043 | 52.0% | 30.2% | 15.71 | 43.6% | 20.2% | 12.99 |
| gen2 | 18,043 | 50.7% | 30.3% | 15.37 | 43.5% | 21.7% | 12.85 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 9,679 | 16.5 | 10.5 | 21.6 | 17.4 | 19.6 | 11.2 | 3.3 | 10.42 | 34.2% | 14.5% |
| STALE | 8,364 | 10.3 | 6.2 | 15.1 | 14.2 | 18.5 | 18.4 | 17.3 | 17.19 | 54.2% | 35.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 8,467 | 17.3 | 11.6 | 23.7 | 14.6 | 16.9 | 11.1 | 4.9 | 9.38 | 32.9% | 16.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 33,042 | 8467 | 13151 | 11424 | 24.3 | 150.1 | 1400.4 |
| ge_15pp | 13,427 | 2786 | 4594 | 6047 | 26.6 | 453.4 | 1380.4 |
| ge_25pp | 7,213 | 1357 | 1997 | 3859 | 34.5 | 583.1 | 1380.4 |
| lt_10pp | 14,544 | 4447 | 6324 | 3773 | 22.4 | 48.9 | 1341.5 |

Current slate `SL-20261014T221458Z-eef1e224`: 419 priced rows, quote age at build {'median': 10.6, 'max': 10.7}, freshness {'AGING': 419}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 9 | 0.0 | 0.0 | 33.3 | 0.0 | 44.4 | 22.2 | 0.0 | 20.47 | 66.7% | 22.2% |
| EXTERNAL_LONE_OUTLIER | 11 | 72.7 | 27.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,416 | 21.1 | 10.7 | 22.7 | 18.7 | 19.4 | 6.8 | 0.6 | 8.91 | 26.8% | 7.4% |
| KALSHI_LONE_OUTLIER | 7 | 14.3 | 0.0 | 57.1 | 0.0 | 14.3 | 14.3 | 0.0 | 5.14 | 28.6% | 14.3% |
| MARKETS_AGREE | 251 | 71.7 | 28.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.04 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 471 | 0.0 | 3.8 | 34.2 | 29.9 | 23.4 | 8.1 | 0.6 | 11.66 | 32.1% | 8.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 18,043 | 2165 (12.0%) | 21.8% | 0.7% | {"EXTERNAL_STALE": 1416, "AGREES_WITH_KALSHI": 471, "ALL_AGREE": 251, "EXTERNAL_OUTLIER": 11, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 7, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 7,842 | 538 (6.9%) | 28.1% | 1.5% | {"EXTERNAL_STALE": 379, "AGREES_WITH_KALSHI": 151, "SUPPORTS_MODEL_DIRECTION": 6, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 4,394 | 149 (3.4%) | 27.5% | 2.0% | {"EXTERNAL_STALE": 105, "AGREES_WITH_KALSHI": 41, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 1,985 | 140 (7.0%) | 27.9% | 2.1% | {"EXTERNAL_STALE": 98, "AGREES_WITH_KALSHI": 39, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 7,328 | 1221 (16.7%) | 14.7% | 0.6% | {"EXTERNAL_STALE": 772, "ALL_AGREE": 251, "AGREES_WITH_KALSHI": 179, "EXTERNAL_OUTLIER": 11, "AGREES_WITH_MODEL": 5, "SUPPORTS_MODEL_DIRECTION": 2, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,541 | 11.6 | 8.0 | 20.0 | 14.9 | 21.6 | 14.3 | 9.8 | 13.35 | 45.6% | 24.1% |
| 4-10x | 2,373 | 12.1 | 8.8 | 19.4 | 15.5 | 19.8 | 15.4 | 9.1 | 13.02 | 44.2% | 24.5% |
| <2x | 9,459 | 15.5 | 9.1 | 18.7 | 16.9 | 17.7 | 12.9 | 9.1 | 11.89 | 39.7% | 22.0% |
| >=10x | 2,670 | 10.8 | 6.4 | 15.4 | 14.2 | 20.4 | 19.9 | 13.0 | 16.44 | 53.3% | 32.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 4,706 | 13.8 | 8.2 | 19.3 | 16.0 | 19.6 | 12.7 | 10.3 | 12.62 | 42.6% | 23.0% |
| 300-1000 | 4,126 | 12.0 | 8.6 | 17.6 | 16.1 | 21.1 | 15.7 | 8.9 | 13.53 | 45.7% | 24.6% |
| <300 | 5,202 | 8.8 | 6.0 | 15.6 | 14.8 | 21.1 | 20.7 | 13.1 | 17.01 | 54.8% | 33.7% |
| >=3000 | 4,009 | 21.2 | 11.7 | 22.6 | 17.1 | 14.0 | 7.5 | 5.9 | 8.5 | 27.4% | 13.4% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 587 | 0.5376 | 0.4054 | 0.4838 | +0.054 | -0.078 | 0.001 ± 0.0061 |
| ratio 4-10x | 398 | 0.5867 | 0.4476 | 0.5126 | +0.074 | -0.065 | 0.0069 ± 0.0079 |
| ratio <2x | 1419 | 0.5375 | 0.4153 | 0.4581 | +0.079 | -0.043 | 0.0107 ± 0.0038 |
| ratio >=10x | 466 | 0.5475 | 0.3791 | 0.427 | +0.120 | -0.048 | 0.0155 ± 0.0082 |
| thinner_sample 1000-3000 | 796 | 0.5431 | 0.4187 | 0.4749 | +0.068 | -0.056 | 0.0043 ± 0.0051 |
| thinner_sample 300-1000 | 702 | 0.5609 | 0.4229 | 0.4858 | +0.075 | -0.063 | 0.0026 ± 0.0058 |
| thinner_sample <300 | 882 | 0.545 | 0.3838 | 0.4444 | +0.101 | -0.061 | 0.0149 ± 0.0058 |
| thinner_sample >=3000 | 490 | 0.5309 | 0.4355 | 0.4612 | +0.070 | -0.026 | 0.0148 ± 0.0053 |
| data_status ADEQUATE | 814 | 0.5341 | 0.4298 | 0.4631 | +0.071 | -0.033 | 0.0081 ± 0.0044 |
| data_status LIMITED | 736 | 0.5522 | 0.4235 | 0.4878 | +0.064 | -0.064 | 0.0037 ± 0.0054 |
| data_status POOR | 1320 | 0.5498 | 0.3943 | 0.4553 | +0.095 | -0.061 | 0.0124 ± 0.0047 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 437 | 0.1935 | 0.1948 | -0.0013 ± 0.0007 | 0.5653 | 0.5681 | 0.4927 | 0.4778 | 0.524 | -0.048 ± 0.0221 | -0.01 (3) |
| 3-5 | 284 | 0.1904 | 0.1909 | -0.0005 ± 0.0021 | 0.5608 | 0.5607 | 0.5095 | 0.4697 | 0.493 | -0.069 ± 0.0265 | 0.02 (1) |
| 5-10 | 604 | 0.1954 | 0.1967 | -0.0013 ± 0.0027 | 0.5759 | 0.5768 | 0.5119 | 0.4374 | 0.4752 | -0.077 ± 0.0188 | -0.0125 (4) |
| 10-15 | 506 | 0.2105 | 0.2031 | +0.0074 ± 0.005 | 0.6083 | 0.5868 | 0.5221 | 0.3985 | 0.4289 | -0.084 ± 0.0199 | -0.0633 (3) |
| 15-25 | 625 | 0.2294 | 0.2163 | +0.0131 ± 0.0072 | 0.6539 | 0.6189 | 0.5756 | 0.3806 | 0.4464 | -0.074 ± 0.0185 | -0.0133 (6) |
| 25-40 | 342 | 0.2279 | 0.208 | +0.0199 ± 0.0147 | 0.6474 | 0.5974 | 0.6439 | 0.3357 | 0.4591 | -0.065 ± 0.0226 | -0.01 (1) |
| 40+ | 72 | 0.29 | 0.1741 | +0.1160 ± 0.0438 | 0.7878 | 0.5206 | 0.7443 | 0.2967 | 0.3889 | -0.113 ± 0.0433 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2038 | 0.1774 | 0.1785 | -0.0011 ± 0.0003 | 0.5291 | 0.5303 | 0.4816 | 0.4666 | 0.502 | -0.021 ± 0.0095 | -0.0188 (8) |
| 3-5 | 1280 | 0.1943 | 0.1926 | +0.0016 ± 0.001 | 0.5696 | 0.5616 | 0.4826 | 0.443 | 0.4391 | -0.063 ± 0.0125 | 0.02 (1) |
| 5-10 | 2822 | 0.1925 | 0.191 | +0.0014 ± 0.0012 | 0.5674 | 0.561 | 0.4865 | 0.4126 | 0.4366 | -0.041 ± 0.0084 | -0.0082 (17) |
| 10-15 | 2431 | 0.2005 | 0.1824 | +0.0181 ± 0.0022 | 0.5867 | 0.5364 | 0.4798 | 0.3555 | 0.3451 | -0.074 ± 0.0086 | -0.0475 (4) |
| 15-25 | 2930 | 0.2066 | 0.1712 | +0.0354 ± 0.003 | 0.6052 | 0.5053 | 0.4999 | 0.3039 | 0.3137 | -0.063 ± 0.0076 | -0.0048 (29) |
| 25-40 | 2340 | 0.2205 | 0.1255 | +0.0950 ± 0.0046 | 0.6346 | 0.3868 | 0.5272 | 0.214 | 0.2235 | -0.061 ± 0.0071 | -0.01 (1) |
| 40+ | 1581 | 0.3734 | 0.0438 | +0.3296 ± 0.0059 | 0.9725 | 0.1725 | 0.6254 | 0.1057 | 0.0588 | -0.084 ± 0.0049 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 333 | 0.1957 | 0.1958 | -0.0002 ± 0.0009 | 0.5721 | 0.5725 | 0.5023 | 0.4871 | 0.4985 | -0.089 ± 0.0256 | -0.01 (1) |
| 3-5 | 228 | 0.2112 | 0.2105 | +0.0007 ± 0.0025 | 0.6046 | 0.6046 | 0.5196 | 0.4796 | 0.4868 | -0.078 ± 0.032 | 0.02 (1) |
| 5-10 | 520 | 0.1983 | 0.1986 | -0.0003 ± 0.003 | 0.5798 | 0.5806 | 0.5558 | 0.4809 | 0.5212 | -0.064 ± 0.0203 | -0.01 (4) |
| 10-15 | 467 | 0.2143 | 0.2061 | +0.0082 ± 0.0053 | 0.6152 | 0.5976 | 0.5728 | 0.4484 | 0.4818 | -0.090 ± 0.0218 | -0.05 (4) |
| 15-25 | 698 | 0.228 | 0.2084 | +0.0196 ± 0.0068 | 0.6475 | 0.5994 | 0.589 | 0.3921 | 0.4441 | -0.087 ± 0.0175 | -0.01 (5) |
| 25-40 | 449 | 0.2668 | 0.1976 | +0.0692 ± 0.0133 | 0.747 | 0.5743 | 0.6636 | 0.3491 | 0.3987 | -0.117 ± 0.0208 | -0.025 (2) |
| 40+ | 175 | 0.3551 | 0.1843 | +0.1708 ± 0.0316 | 0.984 | 0.5419 | 0.7418 | 0.2616 | 0.3371 | -0.060 ± 0.0313 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1748 | 0.1809 | 0.1813 | -0.0004 ± 0.0003 | 0.5365 | 0.5372 | 0.4971 | 0.4824 | 0.5057 | -0.033 ± 0.0105 | -0.0217 (6) |
| 3-5 | 1124 | 0.1942 | 0.1936 | +0.0006 ± 0.0011 | 0.5638 | 0.5624 | 0.5173 | 0.4773 | 0.4884 | -0.040 ± 0.0134 | 0.02 (1) |
| 5-10 | 2456 | 0.1913 | 0.1895 | +0.0017 ± 0.0013 | 0.5654 | 0.5578 | 0.5167 | 0.443 | 0.4699 | -0.036 ± 0.0089 | -0.01 (5) |
| 10-15 | 2141 | 0.1966 | 0.1827 | +0.0138 ± 0.0023 | 0.5786 | 0.5359 | 0.5225 | 0.3981 | 0.4078 | -0.060 ± 0.0094 | -0.02 (14) |
| 15-25 | 3125 | 0.2157 | 0.1756 | +0.0400 ± 0.003 | 0.6271 | 0.5187 | 0.533 | 0.3367 | 0.336 | -0.076 ± 0.0076 | -0.0026 (27) |
| 25-40 | 2701 | 0.248 | 0.1372 | +0.1108 ± 0.0045 | 0.7038 | 0.4181 | 0.5614 | 0.2449 | 0.2303 | -0.084 ± 0.0071 | -0.015 (6) |
| 40+ | 2127 | 0.3997 | 0.0686 | +0.3311 ± 0.0065 | 1.0484 | 0.238 | 0.6647 | 0.1276 | 0.1016 | -0.066 ± 0.0056 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 429 | 0.1944 | 0.1971 | -0.0027 ± 0.0008 | 0.5687 | 0.5757 | 0.4941 | 0.4788 | 0.5571 | +0.000 ± 0.0217 | -0.0133 (6) |
| 3-5 | 308 | 0.1843 | 0.1827 | +0.0017 ± 0.0019 | 0.5439 | 0.5397 | 0.4901 | 0.4507 | 0.4513 | -0.111 ± 0.0256 | -0.01 (1) |
| 5-10 | 634 | 0.1996 | 0.1973 | +0.0023 ± 0.0027 | 0.5862 | 0.5773 | 0.5052 | 0.4315 | 0.4495 | -0.087 ± 0.0181 | -0.01 (4) |
| 10-15 | 495 | 0.2086 | 0.2093 | -0.0007 ± 0.0051 | 0.6048 | 0.6013 | 0.5389 | 0.4163 | 0.4828 | -0.059 ± 0.0203 | -0.044 (5) |
| 15-25 | 583 | 0.2341 | 0.2114 | +0.0228 ± 0.0074 | 0.6678 | 0.6071 | 0.5825 | 0.3892 | 0.4271 | -0.102 ± 0.0189 | -0.03 (1) |
| 25-40 | 356 | 0.2138 | 0.2122 | +0.0016 ± 0.0144 | 0.6161 | 0.6075 | 0.649 | 0.3386 | 0.4888 | -0.043 ± 0.0218 | 0.0 (1) |
| 40+ | 65 | 0.3165 | 0.1747 | +0.1418 ± 0.0472 | 0.8502 | 0.5223 | 0.7504 | 0.2955 | 0.3692 | -0.124 ± 0.0479 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1933 | 0.1863 | 0.1876 | -0.0013 ± 0.0003 | 0.5491 | 0.5519 | 0.4868 | 0.4715 | 0.5101 | -0.015 ± 0.0099 | -0.0183 (23) |
| 3-5 | 1359 | 0.1838 | 0.1816 | +0.0023 ± 0.0009 | 0.5439 | 0.5384 | 0.4749 | 0.4356 | 0.4275 | -0.071 ± 0.012 | -0.0243 (7) |
| 5-10 | 2996 | 0.1934 | 0.1879 | +0.0055 ± 0.0012 | 0.571 | 0.5525 | 0.4811 | 0.4073 | 0.4052 | -0.064 ± 0.008 | -0.01 (18) |
| 10-15 | 2300 | 0.1958 | 0.1817 | +0.0142 ± 0.0022 | 0.5762 | 0.5329 | 0.4967 | 0.3736 | 0.3778 | -0.063 ± 0.0088 | -0.03 (9) |
| 15-25 | 3013 | 0.2084 | 0.1704 | +0.0380 ± 0.0029 | 0.6112 | 0.5046 | 0.5036 | 0.3083 | 0.3107 | -0.068 ± 0.0076 | -0.03 (2) |
| 25-40 | 2299 | 0.2145 | 0.1233 | +0.0912 ± 0.0046 | 0.621 | 0.3801 | 0.5231 | 0.2074 | 0.2249 | -0.056 ± 0.007 | 0.0 (1) |
| 40+ | 1522 | 0.3871 | 0.0454 | +0.3417 ± 0.0062 | 1.0109 | 0.177 | 0.6331 | 0.1077 | 0.0565 | -0.087 ± 0.0052 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 749 | 0.1974 | 0.198 | -0.0006 ± 0.0006 | 0.5758 | 0.577 | 0.505 | 0.49 | 0.506 | -0.038 ± 0.0163 | -0.0226 (46) |
| 3-5 | 538 | 0.1937 | 0.1933 | +0.0004 ± 0.0015 | 0.5659 | 0.5633 | 0.4796 | 0.4398 | 0.4517 | -0.044 ± 0.0191 | -0.0058 (33) |
| 5-10 | 1134 | 0.1946 | 0.1893 | +0.0053 ± 0.002 | 0.5748 | 0.56 | 0.4859 | 0.4124 | 0.4136 | -0.061 ± 0.0132 | -0.0049 (73) |
| 10-15 | 717 | 0.2066 | 0.1961 | +0.0105 ± 0.0041 | 0.6017 | 0.5741 | 0.501 | 0.3781 | 0.3961 | -0.050 ± 0.0166 | 0.0014 (64) |
| 15-25 | 962 | 0.2309 | 0.2121 | +0.0188 ± 0.0058 | 0.6598 | 0.6101 | 0.5618 | 0.3673 | 0.4168 | -0.047 ± 0.0148 | -0.0216 (58) |
| 25-40 | 551 | 0.2548 | 0.1952 | +0.0596 ± 0.0117 | 0.7172 | 0.5676 | 0.6434 | 0.3309 | 0.3902 | -0.085 ± 0.0176 | -0.0216 (25) |
| 40+ | 192 | 0.3714 | 0.1911 | +0.1803 ± 0.0321 | 1.0746 | 0.5631 | 0.7938 | 0.303 | 0.3854 | -0.079 ± 0.0289 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2259 | 0.1886 | 0.1888 | -0.0003 ± 0.0003 | 0.5526 | 0.5521 | 0.5033 | 0.4879 | 0.5024 | -0.030 ± 0.0091 | -0.0155 (82) |
| 3-5 | 1542 | 0.1881 | 0.1858 | +0.0024 ± 0.0009 | 0.5509 | 0.5452 | 0.4866 | 0.447 | 0.4377 | -0.055 ± 0.011 | -0.0148 (63) |
| 5-10 | 3182 | 0.1918 | 0.1846 | +0.0072 ± 0.0011 | 0.5676 | 0.547 | 0.4794 | 0.4058 | 0.3969 | -0.061 ± 0.0077 | -0.0087 (125) |
| 10-15 | 2146 | 0.2028 | 0.1887 | +0.0141 ± 0.0023 | 0.5931 | 0.5555 | 0.508 | 0.385 | 0.3891 | -0.054 ± 0.0093 | -0.0053 (105) |
| 15-25 | 2694 | 0.2286 | 0.1987 | +0.0299 ± 0.0034 | 0.6603 | 0.5769 | 0.5544 | 0.3595 | 0.3816 | -0.056 ± 0.0086 | -0.0255 (106) |
| 25-40 | 1825 | 0.2552 | 0.1686 | +0.0865 ± 0.0061 | 0.7231 | 0.4987 | 0.6059 | 0.2912 | 0.3134 | -0.077 ± 0.0093 | -0.0206 (47) |
| 40+ | 900 | 0.3862 | 0.1292 | +0.2570 ± 0.0128 | 1.0957 | 0.3958 | 0.7099 | 0.2023 | 0.2156 | -0.072 ± 0.0114 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2870 | 1.061 ± 0.052 | 1.18 | 0.1687 | 0.1712 | 0.2109 | 0.202 |
| gen2 | 2870 | 0.867 ± 0.047 | 1.126 | 0.1784 | 0.1711 | 0.2291 | 0.2018 |
| gen1_elo | 2870 | 1.038 ± 0.051 | 1.17 | 0.1731 | 0.1716 | 0.2101 | 0.202 |
| gen1_sr | 2870 | 1.069 ± 0.062 | 1.194 | 0.1376 | 0.173 | 0.2251 | 0.2016 |
| gen1_ledger | 4843 | 0.87 ± 0.035 | 1.084 | 0.1767 | 0.1865 | 0.2178 | 0.1974 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 13,427)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,446 | 25.7% |
| STALE_QUOTE | market_freshness | 2,659 | 19.8% |
| BOOK_QUALITY | execution | 2,440 | 18.2% |
| POOR_DATA | data | 1,480 | 11.0% |
| LIMITED_DATA | data | 981 | 7.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 744 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 642 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 511 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 387 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 137 | 1.0% |

Cause class: coverage 25.7%, market_freshness 19.8%, data 18.3%, execution 18.2%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.8%, mapping 3.8%, model_calibration 1.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.2%, START_UNVERIFIABLE 95.9%, LOW_DATA_QUALITY 68.9%, THIN_PLAYER_HISTORY 57.7%, STALE_PLAYER_DATA 54.4%, STALE_KALSHI_QUOTE 45.0%, MODEL_INTERNAL_DISAGREEMENT 38.9%, ASYMMETRIC_SAMPLE_SIZE 31.6%, WIDE_SPREAD 23.8%, MODEL_HIGH_UNCERTAINTY 16.7%, PLAYER_IDENTITY_RISK 13.5%, LEVEL_TRANSFER_RISK 8.6%, EVENT_MAPPING_RISK 7.8%, LOW_DISPLAYED_LIQUIDITY 7.4%, MODEL_CALIBRATION_OUTLIER 3.5%, EXTERNAL_MARKET_REJECTION 1.7%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 28.1%, POST_SETTLEMENT_OBSERVATION 25.7%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 7,213)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,722 | 37.7% |
| BOOK_QUALITY | execution | 1,266 | 17.5% |
| STALE_QUOTE | market_freshness | 1,213 | 16.8% |
| POOR_DATA | data | 598 | 8.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 402 | 5.6% |
| IDENTITY_AMBIGUOUS | mapping | 314 | 4.3% |
| LIMITED_DATA | data | 289 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 240 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 140 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 29 | 0.4% |

Cause class: coverage 37.7%, execution 17.5%, market_freshness 16.8%, data 12.3%, market_freshness/coverage 8.9%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.4%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.1%, START_UNVERIFIABLE 98.2%, LOW_DATA_QUALITY 72.7%, THIN_PLAYER_HISTORY 60.1%, STALE_KALSHI_QUOTE 53.5%, STALE_PLAYER_DATA 49.3%, MODEL_INTERNAL_DISAGREEMENT 40.0%, ASYMMETRIC_SAMPLE_SIZE 33.6%, WIDE_SPREAD 23.4%, MODEL_HIGH_UNCERTAINTY 17.4%, PLAYER_IDENTITY_RISK 17.2%, EVENT_MAPPING_RISK 9.7%, LOW_DISPLAYED_LIQUIDITY 7.6%, LEVEL_TRANSFER_RISK 7.5%, MODEL_CALIBRATION_OUTLIER 4.5%, EXTERNAL_MARKET_REJECTION 0.8%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 40.6%, POST_SETTLEMENT_OBSERVATION 37.7%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 5790, "IDENTITY_AMBIGUOUS": 1423}; ticker orientation: {"VERIFIED": 7213}.

Checks: discipline:AMBIGUOUS 501, discipline:PASS 6712, identity_confidence:AMBIGUOUS 1243, identity_confidence:PASS 5970, level_mapping:NA 513, level_mapping:PASS 6700, market_pair:AMBIGUOUS 254, market_pair:NA 173, market_pair:PASS 6786, model_complement:NA 140, model_complement:PASS 7073, namesake:PASS 7213, physical_match_id:NA 2819, physical_match_id:PASS 4394, player_ids:PASS 7213, same_pair_other_event:PASS 7213, ticker_orientation:PASS 7213

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,047 | 1.4% | 1.4% | 0.4% | {"market_freshness": 20, "execution": 8, "market_freshness/coverage": 1} | 5.24 | 0.2103 / 0.2125 (251) | 16.4% | 0.5% | 5.4% | 1.7% |
| CHALLENGER | 5,220 | 17.1% | 5.8% | 12.3% | {"coverage": 547, "market_freshness": 109, "market_freshness/coverage": 108, "data": 57, "model_calibration_or_unknown": 45, "execution": 13, "mapping": 6, "model_calibration": 5} | 7.24 | 0.218 / 0.2038 (1360) | 37.8% | 8.9% | 2.4% | 22.7% |
| DOUBLES | 998 | 50.2% | 49.4% | 7.0% | {"execution": 198, "mapping": 151, "market_freshness": 106, "market_freshness/coverage": 39, "coverage": 7} | 24.32 | 0.3343 / 0.2315 (293) | 23.4% | 0.0% | 100.0% | 7.7% |
| ITF_MEN | 9,711 | 24.3% | 16.5% | 32.8% | {"coverage": 939, "execution": 495, "market_freshness": 338, "data": 313, "market_freshness/coverage": 200, "mapping": 78, "model_calibration_or_unknown": 2} | 10.94 | 0.2124 / 0.1945 (2446) | 36.0% | 59.0% | 10.7% | 23.3% |
| ITF_WOMEN | 12,087 | 26.1% | 18.3% | 43.8% | {"coverage": 1212, "market_freshness": 567, "execution": 531, "data": 483, "market_freshness/coverage": 249, "mapping": 73, "model_calibration_or_unknown": 32, "model_calibration": 10} | 12.35 | 0.2022 / 0.1921 (2606) | 38.4% | 58.0% | 9.8% | 23.3% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,577 | 6.2% | 5.5% | 1.4% | {"market_freshness": 36, "model_calibration_or_unknown": 22, "data": 11, "market_freshness/coverage": 10, "model_calibration": 7, "execution": 7, "coverage": 4, "mapping": 1} | 7.82 | 0.2387 / 0.2306 (279) | 26.2% | 1.3% | 1.7% | 3.2% |
| WTA125 | 1,253 | 12.8% | 10.2% | 2.2% | {"model_calibration_or_unknown": 37, "market_freshness": 35, "market_freshness/coverage": 34, "data": 23, "coverage": 12, "execution": 9, "model_calibration": 7, "mapping": 4} | 9.51 | 0.2156 / 0.207 (436) | 23.0% | 8.1% | 4.3% | 10.2% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 5 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 6 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 7 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 17.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1037 min (STALE); no external reference |
| 8 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 9 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 10 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 11 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 12 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 13 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 14 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 15 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 16 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 17 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 18 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 19 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 20 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 21 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 22 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 23 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 9.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 553 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 24 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 25 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 26 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 27 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 28 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 29 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 765 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 30 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 31 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 32 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 547 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 33 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 34 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 36 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 37 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 38 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.8h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 359 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 39 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 40 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 41 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 42 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 43 | `KXATPCHALLENGERMATCH-26OCT13GIUSEA-SEA` | CHALLENGER | fair_v1 | 76% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 243 min (STALE); no external reference |
| 44 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 760 min (STALE); no external reference |
| 45 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 46 | `KXITFWMATCH-26OCT13MAMSTR-MAM` | ITF_WOMEN | fair_v1 | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 406 min (STALE); data LIMITED (grade C, thinner serve sample 879.0, ratio 2.64); no external reference |
| 47 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 48 | `KXITFMATCH-26OCT13VISMUE-MUE` | ITF_MEN | fair_v1 | 25% / 98% | -74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 103 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 0.0); no external reference |
| 49 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 50 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9825, "by_level_share_of_ge_25pp": {"ATP": 0.004, "CHALLENGER": 0.1234, "DOUBLES": 0.0695, "ITF_MEN": 0.3279, "ITF_WOMEN": 0.4377, "OTHER": 0.0017, "WTA": 0.0136, "WTA125": 0.0223}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.535, "share_primary_cause_market_settled_or_in_play": 0.4664, "share_primary_cause_stale_quote_only": 0.1682}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 7213, "identity_ambiguous_share": 0.1973, "ticker_orientation": {"VERIFIED": 7213}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 4394, "with_external": 149, "coverage": 0.0339, "external_status": {"EXTERNAL_STALE": 105, "AGREES_WITH_KALSHI": 41, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 105, "MODEL_LONE_OUTLIER": 41, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.2752, "share_external_supports_model": 0.0201}, "pregame_clean_ge_25pp": {"n": 1985, "with_external": 140, "coverage": 0.0705, "external_status": {"EXTERNAL_STALE": 98, "AGREES_WITH_KALSHI": 39, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 98, "MODEL_LONE_OUTLIER": 39, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.2786, "share_external_supports_model": 0.0214}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 562.0, "median_sample_ratio": 2.38, "median_min_matches": 20.0, "median_max_days_since_last": 204.0, "share_severe_asymmetry": 0.1995, "data_status": {"POOR": 3846, "LIMITED": 2059, "ADEQUATE": 1308}, "comparison_lt_10pp": {"median_thinner_serve_points": 1811.5, "median_sample_ratio": 1.69, "median_min_matches": 85.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 587, "model_minus_observed": 0.0538, "kalshi_minus_observed": -0.0784, "brier_diff_model_minus_kalshi": 0.001}, "4-10x": {"n": 398, "model_minus_observed": 0.0741, "kalshi_minus_observed": -0.065, "brier_diff_model_minus_kalshi": 0.0069}, "<2x": {"n": 1419, "model_minus_observed": 0.0794, "kalshi_minus_observed": -0.0428, "brier_diff_model_minus_kalshi": 0.0107}, ">=10x": {"n": 466, "model_minus_observed": 0.1204, "kalshi_minus_observed": -0.048, "brier_diff_model_minus_kalshi": 0.0155}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2870, "model": {"intercept": -0.547, "slope": 0.867, "slope_se": 0.047}, "kalshi_mid_same_rows": {"intercept": 0.232, "slope": 1.126, "slope_se": 0.054}, "mean_extremity_model": 0.1784, "mean_extremity_kalshi": 0.1711, "model_brier": 0.2291, "kalshi_brier": 0.2018, "brier_diff_model_minus_kalshi": 0.0273, "brier_diff_se": 0.0035, "model_logloss": 0.6539, "kalshi_logloss": 0.5856}, "fair_v1": {"n": 2870, "model": {"intercept": -0.39, "slope": 1.061, "slope_se": 0.052}, "kalshi_mid_same_rows": {"intercept": 0.332, "slope": 1.18, "slope_se": 0.055}, "mean_extremity_model": 0.1687, "mean_extremity_kalshi": 0.1712, "model_brier": 0.2109, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0089, "brier_diff_se": 0.0028, "model_logloss": 0.6093, "kalshi_logloss": 0.5858}, "gen1_elo": {"n": 2870, "model": {"intercept": -0.368, "slope": 1.038, "slope_se": 0.051}, "kalshi_mid_same_rows": {"intercept": 0.335, "slope": 1.17, "slope_se": 0.054}, "mean_extremity_model": 0.1731, "mean_extremity_kalshi": 0.1716, "model_brier": 0.2101, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0082, "brier_diff_se": 0.0028, "model_logloss": 0.6085, "kalshi_logloss": 0.5857}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2435, "share_ge_15": 0.4346, "median_abs_gap": 12.92, "n": 18043}, "gen1_elo": {"share_ge_25": 0.2382, "share_ge_15": 0.4281, "median_abs_gap": 12.44, "n": 18043}, "gen1_sr": {"share_ge_25": 0.3021, "share_ge_15": 0.52, "median_abs_gap": 15.71, "n": 18043}, "gen2": {"share_ge_25": 0.303, "share_ge_15": 0.5071, "median_abs_gap": 15.37, "n": 18043}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.144, "share_ge_15": 0.3406, "median_abs_gap": 10.5, "n": 13779}, "gen1_elo": {"share_ge_25": 0.1419, "share_ge_15": 0.3301, "median_abs_gap": 9.99, "n": 13778}, "gen1_sr": {"share_ge_25": 0.2025, "share_ge_15": 0.4359, "median_abs_gap": 12.99, "n": 13779}, "gen2": {"share_ge_25": 0.2167, "share_ge_15": 0.4349, "median_abs_gap": 12.85, "n": 13780}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.24, "share_ge_25_all": 0.0142, "share_ge_25_pregame_clean": 0.0139}, "WTA": {"median_abs_gap_pregame_clean": 7.82, "share_ge_25_all": 0.0621, "share_ge_25_pregame_clean": 0.055}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2392, "share_within_10pp_all": 0.4402, "share_within_10pp_pregame_clean": 0.5, "corr_model_vs_mid_pregame_clean": 0.848}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 437, "model_brier": 0.1935, "kalshi_brier": 0.1948, "brier_diff_model_minus_kalshi": -0.0013}, "10-15": {"n_settled": 506, "model_brier": 0.2105, "kalshi_brier": 0.2031, "brier_diff_model_minus_kalshi": 0.0074}, "15-25": {"n_settled": 625, "model_brier": 0.2294, "kalshi_brier": 0.2163, "brier_diff_model_minus_kalshi": 0.0131}, "25-40": {"n_settled": 342, "model_brier": 0.2279, "kalshi_brier": 0.208, "brier_diff_model_minus_kalshi": 0.0199}, "3-5": {"n_settled": 284, "model_brier": 0.1904, "kalshi_brier": 0.1909, "brier_diff_model_minus_kalshi": -0.0005}, "40+": {"n_settled": 72, "model_brier": 0.29, "kalshi_brier": 0.1741, "brier_diff_model_minus_kalshi": 0.116}, "5-10": {"n_settled": 604, "model_brier": 0.1954, "kalshi_brier": 0.1967, "brier_diff_model_minus_kalshi": -0.0013}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.547, "slope": 0.867, "slope_se": 0.047}, "kalshi_slope": {"intercept": 0.232, "slope": 1.126, "slope_se": 0.054}, "n": 2870}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.501, "slope": 0.87, "slope_se": 0.035}, "kalshi_slope": {"intercept": 0.164, "slope": 1.084, "slope_se": 0.04}, "n": 4843}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 293, "model_brier": 0.3343, "kalshi_brier": 0.2315, "brier_diff_model_minus_kalshi": 0.1029, "brier_diff_se": 0.019, "corr_model_outcome": -0.0244, "corr_kalshi_outcome": 0.2733}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
