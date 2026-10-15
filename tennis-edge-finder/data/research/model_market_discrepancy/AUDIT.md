# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-15T17:37Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 33,955): 0-3 14.4%, 3-5 9.4%, 5-10 20.1%, 10-15 15.3%, 15-25 18.9%, 25-40 13.6%, 40+ 8.2%; median gap 11.87 pp.
* **Where the extremes live**: 98.3% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.8%, Challenger 12.2%, doubles 6.9%). Main tour: ATP 1.4% and WTA 6.2% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 7,424): MARKET_ALREADY_SETTLED_WHEN_PRICED 37.1%, STALE_QUOTE 17.6%, BOOK_QUALITY 17.5%, POOR_DATA 8.3%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 4.0%, IN_PLAY_QUOTE 3.2%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.5%. By class: coverage 37.1%, market_freshness 17.6%, execution 17.5%, data 12.3%, market_freshness/coverage 8.8%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.5%.
* **Stale / settled / in-play**: 53.7% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 45.9% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 7,424 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.0% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 3.7%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 22.1% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 553.0 points vs 1787.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.062, Gen-2 0.867, Gen-1 ledger 0.872 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 349 model 0.2254 vs Kalshi 0.2087; n 72 model 0.29 vs Kalshi 0.1741.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 134,631 model-market comparisons (224,180 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 47,279 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-15T17:28:53.193206+00:00'], shadow board 37,471 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-15T17:28:57.303203+00:00'], Model 4 14,287 rows, 14,668 settled tickers, 4,806 tickers with an external scan.
* By model: {"gen1_ledger": 31044, "gen1_elo": 18835, "fair_v1": 18835, "gen2": 18835, "gen1_sr": 18835, "model4_fundamental": 14128, "model4_conditioned": 14119}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 33,955 | 14.4 | 9.4 | 20.1 | 15.3 | 18.9 | 13.6 | 8.2 | 11.87 | 40.8% | 21.9% |
| MW fair_v1 | 18,835 | 13.5 | 8.4 | 18.6 | 15.9 | 19.3 | 14.6 | 9.8 | 12.95 | 43.6% | 24.3% |
| MW gen1_elo | 18,835 | 13.2 | 8.9 | 19.8 | 15.2 | 19.2 | 14.3 | 9.4 | 12.46 | 42.9% | 23.8% |
| MW gen1_ledger | 15,120 | 15.5 | 10.7 | 21.9 | 14.6 | 18.4 | 12.5 | 6.3 | 10.45 | 37.2% | 18.8% |
| MW gen1_sr | 18,835 | 9.8 | 7.5 | 16.2 | 14.2 | 21.8 | 18.6 | 11.9 | 15.87 | 52.3% | 30.5% |
| MW gen2 | 18,835 | 11.5 | 7.1 | 16.4 | 14.2 | 20.3 | 17.4 | 13.1 | 15.44 | 50.9% | 30.6% |
| all families model4_conditioned | 14,119 | 21.6 | 20.1 | 35.2 | 16.6 | 4.3 | 1.1 | 0.9 | 5.81 | 6.3% | 2.0% |
| all families model4_fundamental | 14,128 | 16.8 | 13.6 | 35.7 | 19.6 | 10.6 | 2.6 | 1.1 | 7.58 | 14.3% | 3.7% |

Configurable thresholds (primary): >=5pp 76.1%, >=10pp 56.1%, >=15pp 40.8%, >=20pp 30.2%, >=25pp 21.9%, >=30pp 15.9%, >=40pp 8.2%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.49pp; >=10pp 45.4%, >=25pp 17.4%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,336 | 30.6 | 14.5 | 25.2 | 17.4 | 10.2 | 1.1 | 0.8 | 5.69 | 12.2% | 1.9% |
| CHALLENGER | 3,174 | 15.7 | 10.0 | 20.1 | 15.8 | 14.7 | 12.1 | 11.6 | 11.53 | 38.4% | 23.7% |
| ITF_MEN | 5,382 | 11.1 | 8.2 | 17.9 | 14.8 | 19.7 | 16.3 | 12.1 | 14.2 | 48.0% | 28.3% |
| ITF_WOMEN | 7,394 | 10.3 | 6.6 | 16.2 | 16.0 | 22.3 | 18.0 | 10.6 | 15.39 | 51.0% | 28.7% |
| WTA | 947 | 21.4 | 10.7 | 24.6 | 15.7 | 20.8 | 5.6 | 1.2 | 8.18 | 27.6% | 6.8% |
| WTA125 | 602 | 13.3 | 7.5 | 21.9 | 21.1 | 20.8 | 13.6 | 1.8 | 11.4 | 36.2% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,336 | 24.9 | 14.4 | 24.7 | 18.8 | 14.4 | 1.9 | 1.0 | 6.55 | 17.2% | 2.8% |
| CHALLENGER | 3,174 | 14.9 | 7.8 | 19.4 | 13.4 | 18.2 | 14.1 | 12.2 | 12.73 | 44.5% | 26.3% |
| ITF_MEN | 5,382 | 9.6 | 6.9 | 15.8 | 13.8 | 20.1 | 18.9 | 14.9 | 16.61 | 53.9% | 33.9% |
| ITF_WOMEN | 7,394 | 8.7 | 5.7 | 13.5 | 13.4 | 21.8 | 20.7 | 16.2 | 18.65 | 58.7% | 36.9% |
| WTA | 947 | 17.5 | 8.1 | 18.8 | 16.2 | 23.0 | 15.2 | 1.2 | 12.08 | 39.4% | 16.4% |
| WTA125 | 602 | 6.3 | 4.7 | 16.9 | 17.6 | 25.6 | 19.8 | 9.1 | 17.24 | 54.5% | 28.9% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,336 | 27.9 | 14.4 | 28.7 | 15.3 | 10.4 | 2.5 | 0.9 | 6.03 | 13.8% | 3.4% |
| CHALLENGER | 3,174 | 15.1 | 10.2 | 20.5 | 15.2 | 15.4 | 11.7 | 11.9 | 11.02 | 39.0% | 23.6% |
| ITF_MEN | 5,382 | 10.2 | 8.1 | 18.4 | 14.1 | 20.4 | 16.6 | 12.2 | 14.64 | 49.2% | 28.8% |
| ITF_WOMEN | 7,394 | 10.0 | 6.8 | 16.4 | 15.8 | 23.1 | 18.2 | 9.7 | 15.43 | 50.9% | 27.9% |
| WTA | 947 | 22.6 | 15.4 | 32.5 | 15.9 | 10.7 | 2.1 | 0.7 | 6.17 | 13.5% | 2.9% |
| WTA125 | 602 | 22.6 | 13.0 | 28.9 | 15.1 | 13.8 | 6.3 | 0.3 | 7.5 | 20.4% | 6.6% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 728 | 31.0 | 22.8 | 35.3 | 9.2 | 1.2 | 0.4 | 0.0 | 4.69 | 1.7% | 0.4% |
| CHALLENGER | 2,171 | 22.2 | 15.4 | 27.6 | 14.7 | 13.0 | 5.1 | 2.0 | 6.98 | 20.1% | 7.1% |
| DOUBLES | 1,025 | 5.3 | 3.8 | 11.5 | 10.7 | 18.8 | 24.6 | 25.3 | 24.85 | 68.7% | 49.9% |
| ITF_MEN | 4,642 | 14.7 | 8.5 | 20.8 | 15.4 | 20.8 | 12.6 | 7.3 | 11.88 | 40.6% | 19.9% |
| ITF_WOMEN | 5,071 | 11.7 | 9.3 | 19.6 | 14.7 | 22.3 | 16.6 | 5.7 | 13.01 | 44.7% | 22.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 653 | 21.3 | 15.3 | 27.3 | 17.1 | 13.6 | 4.9 | 0.5 | 7.52 | 19.0% | 5.4% |
| WTA125 | 681 | 20.6 | 13.5 | 22.8 | 18.4 | 14.4 | 8.2 | 2.2 | 8.27 | 24.8% | 10.4% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,322 | 30.6 | 14.4 | 25.4 | 17.5 | 10.2 | 1.1 | 0.8 | 5.75 | 12.1% | 1.9% |
| CHALLENGER | 2,271 | 20.4 | 12.5 | 25.3 | 18.4 | 15.1 | 5.9 | 2.4 | 8.31 | 23.4% | 8.3% |
| ITF_MEN | 3,912 | 13.6 | 10.1 | 21.2 | 16.5 | 20.0 | 13.1 | 5.4 | 11.32 | 38.5% | 18.5% |
| ITF_WOMEN | 5,470 | 12.3 | 8.1 | 18.5 | 18.2 | 23.7 | 14.9 | 4.3 | 12.94 | 42.9% | 19.2% |
| WTA | 927 | 21.7 | 10.0 | 24.9 | 15.8 | 20.9 | 5.5 | 1.2 | 8.18 | 27.6% | 6.7% |
| WTA125 | 578 | 13.7 | 7.3 | 21.3 | 21.4 | 21.4 | 13.5 | 1.4 | 11.49 | 36.3% | 14.9% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,322 | 24.7 | 14.5 | 24.8 | 18.8 | 14.4 | 1.8 | 1.0 | 6.58 | 17.2% | 2.8% |
| CHALLENGER | 2,271 | 19.1 | 9.9 | 24.2 | 16.2 | 18.4 | 9.5 | 2.6 | 9.08 | 30.6% | 12.2% |
| ITF_MEN | 3,913 | 11.3 | 8.2 | 18.1 | 15.5 | 22.1 | 16.3 | 8.4 | 13.96 | 46.8% | 24.7% |
| ITF_WOMEN | 5,470 | 9.9 | 6.5 | 15.2 | 14.7 | 23.9 | 19.7 | 10.0 | 16.27 | 53.7% | 29.7% |
| WTA | 927 | 17.5 | 8.0 | 18.8 | 16.2 | 23.1 | 15.3 | 1.2 | 12.12 | 39.6% | 16.5% |
| WTA125 | 578 | 6.1 | 4.8 | 17.0 | 18.0 | 25.4 | 20.4 | 8.3 | 17.21 | 54.1% | 28.7% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 708 | 31.1 | 23.0 | 35.6 | 9.3 | 0.6 | 0.4 | 0.0 | 4.66 | 1.0% | 0.4% |
| CHALLENGER | 1,869 | 24.0 | 16.8 | 29.8 | 14.5 | 12.0 | 2.4 | 0.5 | 6.37 | 15.0% | 2.9% |
| DOUBLES | 946 | 5.4 | 3.9 | 11.8 | 10.8 | 18.9 | 24.5 | 24.6 | 24.2 | 68.1% | 49.1% |
| ITF_MEN | 3,814 | 16.2 | 9.3 | 22.8 | 16.2 | 20.6 | 10.5 | 4.4 | 10.54 | 35.5% | 14.9% |
| ITF_WOMEN | 4,141 | 12.9 | 10.1 | 21.4 | 15.5 | 22.6 | 15.0 | 2.6 | 11.56 | 40.1% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 619 | 21.8 | 16.0 | 27.5 | 17.1 | 13.9 | 3.7 | 0.0 | 7.21 | 17.6% | 3.7% |
| WTA125 | 576 | 22.6 | 14.9 | 24.3 | 20.0 | 12.8 | 5.0 | 0.3 | 7.33 | 18.2% | 5.4% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,025 | 5.3 | 3.8 | 11.5 | 10.7 | 18.8 | 24.6 | 25.3 | 24.85 | 68.7% | 49.9% |
| singles | 14,095 | 16.3 | 11.2 | 22.7 | 14.9 | 18.4 | 11.6 | 5.0 | 9.95 | 34.9% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 4,417 | 13.2 | 9.0 | 19.6 | 16.0 | 18.0 | 14.3 | 9.8 | 12.65 | 42.2% | 24.2% |
| Grass | 196 | 12.2 | 11.2 | 14.8 | 14.8 | 22.4 | 17.4 | 7.1 | 14.16 | 46.9% | 24.5% |
| Hard | 12,252 | 13.9 | 8.4 | 18.5 | 15.4 | 19.7 | 14.4 | 9.7 | 12.96 | 43.8% | 24.1% |
| UNKNOWN | 1,970 | 12.1 | 7.1 | 16.9 | 18.6 | 19.1 | 15.8 | 10.2 | 13.38 | 45.2% | 26.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,475 | 19.7 | 10.7 | 20.9 | 16.9 | 15.9 | 8.9 | 7.0 | 9.56 | 31.7% | 15.8% |
| B | 2,453 | 14.3 | 9.1 | 20.1 | 16.7 | 18.1 | 12.3 | 9.5 | 11.57 | 39.9% | 21.9% |
| C | 2,720 | 12.8 | 9.5 | 19.9 | 14.4 | 19.4 | 14.2 | 9.6 | 12.63 | 43.3% | 23.9% |
| D | 3,276 | 11.4 | 7.9 | 17.7 | 16.1 | 21.9 | 15.4 | 9.4 | 13.83 | 46.7% | 24.9% |
| F | 4,911 | 8.0 | 5.3 | 15.0 | 14.9 | 21.9 | 21.7 | 13.2 | 17.94 | 56.8% | 34.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,380 | 22.8 | 15.8 | 28.9 | 15.1 | 11.3 | 4.4 | 1.7 | 6.7 | 17.4% | 6.1% |
| B | 2,276 | 14.9 | 10.0 | 24.0 | 16.3 | 19.5 | 11.1 | 4.2 | 10.18 | 34.7% | 15.2% |
| C | 2,993 | 12.2 | 7.8 | 18.3 | 14.1 | 20.2 | 15.8 | 11.6 | 13.64 | 47.6% | 27.4% |
| D | 2,276 | 14.1 | 9.8 | 20.7 | 13.6 | 21.3 | 13.9 | 6.6 | 11.86 | 41.8% | 20.5% |
| F | 3,195 | 10.1 | 7.5 | 15.2 | 13.9 | 23.7 | 20.4 | 9.1 | 16.38 | 53.2% | 29.5% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 6,168 | 18.0 | 9.7 | 20.3 | 16.8 | 16.3 | 9.9 | 9.1 | 10.55 | 35.3% | 19.0% |
| LIMITED | 4,378 | 14.9 | 10.4 | 20.8 | 15.4 | 18.7 | 12.7 | 7.1 | 11.17 | 38.5% | 19.8% |
| POOR | 8,289 | 9.5 | 6.4 | 16.1 | 15.4 | 21.9 | 19.1 | 11.6 | 15.92 | 52.5% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,050 | 31.2 | 24.5 | 36.3 | 5.5 | 1.7 | 0.7 | 0.1 | 4.49 | 2.5% | 0.7% |
| GAME_SPREAD | 2,894 | 25.8 | 16.1 | 36.6 | 16.8 | 4.1 | 0.4 | 0.2 | 5.97 | 4.7% | 0.6% |
| MATCH_WINNER | 15,120 | 15.5 | 10.7 | 21.9 | 14.6 | 18.4 | 12.5 | 6.3 | 10.45 | 37.2% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 5,533 | 33.4 | 19.6 | 31.0 | 9.6 | 5.1 | 1.1 | 0.2 | 4.69 | 6.4% | 1.4% |
| TOTAL_GAMES | 4,423 | 6.7 | 9.2 | 39.2 | 29.4 | 10.4 | 2.7 | 2.3 | 9.44 | 15.4% | 5.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,937 | 25.6 | 38.3 | 31.4 | 0.3 | 3.9 | 0.4 | 0.1 | 4.3 | 4.4% | 0.5% |
| GAME_SPREAD | 3,519 | 45.4 | 16.5 | 28.7 | 7.3 | 1.1 | 0.7 | 0.4 | 3.54 | 2.2% | 1.1% |
| TOTAL_GAMES | 5,663 | 3.4 | 6.6 | 42.7 | 36.7 | 6.8 | 1.9 | 1.9 | 9.77 | 10.6% | 3.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,937 | 26.4 | 18.8 | 37.1 | 9.1 | 6.2 | 2.1 | 0.3 | 5.47 | 8.6% | 2.4% |
| GAME_SPREAD | 3,519 | 19.6 | 13.6 | 30.3 | 20.8 | 12.8 | 2.3 | 0.7 | 7.7 | 15.8% | 3.0% |
| TOTAL_GAMES | 5,672 | 6.6 | 9.0 | 37.9 | 28.0 | 13.1 | 3.3 | 2.1 | 9.63 | 18.4% | 5.3% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 18,835 | 43.6% | 24.3% | 12.95 | 34.6% | 14.7% | 10.6 |
| gen1_elo | 18,835 | 42.9% | 23.8% | 12.46 | 33.5% | 14.5% | 10.07 |
| gen1_sr | 18,835 | 52.3% | 30.5% | 15.87 | 44.3% | 20.9% | 13.21 |
| gen2 | 18,835 | 50.9% | 30.6% | 15.44 | 44.0% | 22.3% | 12.98 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 9,978 | 16.4 | 10.4 | 21.6 | 17.4 | 19.7 | 11.3 | 3.3 | 10.46 | 34.4% | 14.6% |
| STALE | 8,857 | 10.4 | 6.2 | 15.2 | 14.2 | 18.8 | 18.2 | 17.0 | 17.09 | 54.0% | 35.2% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 8,588 | 17.3 | 11.6 | 23.6 | 14.5 | 16.9 | 11.2 | 4.9 | 9.38 | 32.9% | 16.1% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 33,955 | 8588 | 13450 | 11917 | 24.4 | 152.5 | 1400.4 |
| ge_15pp | 13,840 | 2829 | 4716 | 6295 | 26.9 | 450.2 | 1380.4 |
| ge_25pp | 7,424 | 1381 | 2053 | 3990 | 34.5 | 578.1 | 1380.4 |
| lt_10pp | 14,915 | 4513 | 6452 | 3950 | 22.6 | 48.8 | 1341.5 |

Current slate `SL-20261015T173731Z-a7188823`: 236 priced rows, quote age at build {'median': 8.8, 'max': 8.9}, freshness {'FRESH': 236}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 10 | 0.0 | 0.0 | 40.0 | 0.0 | 40.0 | 20.0 | 0.0 | 20.33 | 60.0% | 20.0% |
| EXTERNAL_LONE_OUTLIER | 11 | 72.7 | 27.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,540 | 21.2 | 10.7 | 22.7 | 18.6 | 19.2 | 7.1 | 0.6 | 8.86 | 26.8% | 7.7% |
| KALSHI_LONE_OUTLIER | 7 | 14.3 | 0.0 | 57.1 | 0.0 | 14.3 | 14.3 | 0.0 | 5.14 | 28.6% | 14.3% |
| MARKETS_AGREE | 263 | 71.9 | 28.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.04 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 519 | 0.0 | 3.7 | 34.3 | 28.7 | 24.3 | 8.5 | 0.6 | 11.7 | 33.3% | 9.1% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 18,835 | 2350 (12.5%) | 22.1% | 0.7% | {"EXTERNAL_STALE": 1540, "AGREES_WITH_KALSHI": 519, "ALL_AGREE": 263, "EXTERNAL_OUTLIER": 11, "SUPPORTS_MODEL_DIRECTION": 9, "AGREES_WITH_MODEL": 7, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 8,212 | 594 (7.2%) | 29.1% | 1.4% | {"EXTERNAL_STALE": 413, "AGREES_WITH_KALSHI": 173, "SUPPORTS_MODEL_DIRECTION": 6, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 4,581 | 168 (3.7%) | 28.0% | 1.8% | {"EXTERNAL_STALE": 118, "AGREES_WITH_KALSHI": 47, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,135 | 158 (7.4%) | 28.5% | 1.9% | {"EXTERNAL_STALE": 110, "AGREES_WITH_KALSHI": 45, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 7,633 | 1321 (17.3%) | 14.9% | 0.6% | {"EXTERNAL_STALE": 841, "ALL_AGREE": 263, "AGREES_WITH_KALSHI": 197, "EXTERNAL_OUTLIER": 11, "AGREES_WITH_MODEL": 5, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,671 | 11.3 | 7.8 | 19.9 | 14.9 | 21.9 | 14.2 | 9.9 | 13.51 | 46.0% | 24.1% |
| 4-10x | 2,464 | 12.3 | 8.8 | 19.5 | 15.6 | 19.4 | 15.4 | 9.0 | 12.89 | 43.8% | 24.4% |
| <2x | 9,815 | 15.4 | 9.1 | 18.8 | 16.9 | 17.8 | 13.0 | 9.1 | 11.93 | 39.8% | 22.0% |
| >=10x | 2,885 | 11.1 | 6.4 | 15.2 | 13.9 | 21.1 | 19.7 | 12.6 | 16.43 | 53.4% | 32.3% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 4,919 | 13.6 | 8.2 | 19.4 | 16.1 | 19.7 | 12.8 | 10.3 | 12.69 | 42.7% | 23.0% |
| 300-1000 | 4,278 | 12.0 | 8.7 | 17.4 | 16.1 | 21.1 | 15.7 | 9.1 | 13.65 | 45.8% | 24.8% |
| <300 | 5,568 | 9.0 | 6.0 | 15.7 | 14.7 | 21.5 | 20.5 | 12.7 | 16.86 | 54.6% | 33.2% |
| >=3000 | 4,070 | 21.3 | 11.7 | 22.8 | 17.0 | 13.9 | 7.5 | 5.8 | 8.41 | 27.3% | 13.3% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 607 | 0.5374 | 0.4061 | 0.4876 | +0.050 | -0.082 | -0.0 ± 0.0059 |
| ratio 4-10x | 405 | 0.5843 | 0.4462 | 0.5111 | +0.073 | -0.065 | 0.007 ± 0.0077 |
| ratio <2x | 1461 | 0.5372 | 0.4146 | 0.4545 | +0.083 | -0.040 | 0.0111 ± 0.0038 |
| ratio >=10x | 481 | 0.5451 | 0.3773 | 0.4283 | +0.117 | -0.051 | 0.014 ± 0.008 |
| thinner_sample 1000-3000 | 825 | 0.5428 | 0.4174 | 0.4715 | +0.071 | -0.054 | 0.0048 ± 0.005 |
| thinner_sample 300-1000 | 719 | 0.5598 | 0.4229 | 0.4882 | +0.072 | -0.065 | 0.0014 ± 0.0057 |
| thinner_sample <300 | 907 | 0.5435 | 0.3826 | 0.4421 | +0.101 | -0.059 | 0.0149 ± 0.0057 |
| thinner_sample >=3000 | 503 | 0.5301 | 0.4353 | 0.4612 | +0.069 | -0.026 | 0.0144 ± 0.0052 |
| data_status ADEQUATE | 848 | 0.5335 | 0.4287 | 0.4587 | +0.075 | -0.030 | 0.0091 ± 0.0043 |
| data_status LIMITED | 748 | 0.5512 | 0.4223 | 0.4906 | +0.060 | -0.068 | 0.0023 ± 0.0054 |
| data_status POOR | 1358 | 0.5487 | 0.394 | 0.4543 | +0.094 | -0.060 | 0.012 ± 0.0046 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 451 | 0.1928 | 0.1943 | -0.0015 ± 0.0007 | 0.5636 | 0.5666 | 0.4922 | 0.4772 | 0.5299 | -0.040 ± 0.0217 | -0.01 (5) |
| 3-5 | 288 | 0.1905 | 0.1907 | -0.0003 ± 0.0021 | 0.5608 | 0.56 | 0.5087 | 0.4688 | 0.4896 | -0.071 ± 0.0262 | 0.02 (1) |
| 5-10 | 624 | 0.1947 | 0.1953 | -0.0005 ± 0.0027 | 0.574 | 0.573 | 0.5095 | 0.4351 | 0.4679 | -0.080 ± 0.0184 | -0.0167 (6) |
| 10-15 | 525 | 0.2119 | 0.2033 | +0.0086 ± 0.0049 | 0.6115 | 0.5884 | 0.5203 | 0.3964 | 0.4229 | -0.086 ± 0.0196 | -0.048 (5) |
| 15-25 | 645 | 0.2303 | 0.2177 | +0.0127 ± 0.0072 | 0.6558 | 0.6217 | 0.5763 | 0.3811 | 0.4481 | -0.074 ± 0.0182 | -0.0129 (7) |
| 25-40 | 349 | 0.2254 | 0.2087 | +0.0167 ± 0.0146 | 0.6416 | 0.5991 | 0.6448 | 0.3363 | 0.4642 | -0.061 ± 0.0224 | -0.01 (1) |
| 40+ | 72 | 0.29 | 0.1741 | +0.1160 ± 0.0438 | 0.7878 | 0.5206 | 0.7443 | 0.2967 | 0.3889 | -0.113 ± 0.0433 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2119 | 0.1764 | 0.1776 | -0.0012 ± 0.0003 | 0.5262 | 0.5275 | 0.4783 | 0.4632 | 0.5007 | -0.018 ± 0.0093 | -0.0129 (17) |
| 3-5 | 1307 | 0.1933 | 0.1915 | +0.0017 ± 0.001 | 0.5673 | 0.559 | 0.4809 | 0.4413 | 0.4361 | -0.063 ± 0.0123 | 0.0 (2) |
| 5-10 | 2904 | 0.1914 | 0.1894 | +0.0020 ± 0.0012 | 0.5647 | 0.5567 | 0.4839 | 0.41 | 0.4304 | -0.044 ± 0.0082 | -0.0119 (21) |
| 10-15 | 2503 | 0.2015 | 0.1827 | +0.0188 ± 0.0021 | 0.589 | 0.5373 | 0.4797 | 0.3552 | 0.3424 | -0.076 ± 0.0085 | -0.0281 (16) |
| 15-25 | 3037 | 0.2077 | 0.172 | +0.0357 ± 0.0029 | 0.6076 | 0.5072 | 0.5009 | 0.3048 | 0.3138 | -0.064 ± 0.0075 | -0.0059 (39) |
| 25-40 | 2387 | 0.2199 | 0.127 | +0.0930 ± 0.0046 | 0.6332 | 0.3904 | 0.5284 | 0.2153 | 0.2275 | -0.058 ± 0.0071 | -0.01 (1) |
| 40+ | 1604 | 0.3737 | 0.0438 | +0.3300 ± 0.0058 | 0.9729 | 0.1723 | 0.6254 | 0.1051 | 0.0586 | -0.083 ± 0.0049 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 345 | 0.1976 | 0.1979 | -0.0002 ± 0.0008 | 0.5765 | 0.5771 | 0.5013 | 0.4861 | 0.5043 | -0.082 ± 0.0252 | -0.01 (3) |
| 3-5 | 234 | 0.2093 | 0.2085 | +0.0009 ± 0.0024 | 0.6005 | 0.5999 | 0.5169 | 0.4768 | 0.4829 | -0.079 ± 0.0313 | 0.02 (1) |
| 5-10 | 532 | 0.1987 | 0.1982 | +0.0006 ± 0.0029 | 0.5806 | 0.5794 | 0.5536 | 0.4788 | 0.5132 | -0.071 ± 0.02 | -0.01 (4) |
| 10-15 | 483 | 0.2121 | 0.2043 | +0.0078 ± 0.0052 | 0.6103 | 0.5928 | 0.5681 | 0.4436 | 0.4783 | -0.087 ± 0.0213 | -0.04 (5) |
| 15-25 | 720 | 0.2288 | 0.2086 | +0.0202 ± 0.0067 | 0.6496 | 0.5995 | 0.588 | 0.3911 | 0.4417 | -0.087 ± 0.0173 | -0.0188 (8) |
| 25-40 | 461 | 0.2656 | 0.2013 | +0.0643 ± 0.0132 | 0.7435 | 0.5841 | 0.6624 | 0.348 | 0.4056 | -0.108 ± 0.0208 | -0.02 (3) |
| 40+ | 179 | 0.3563 | 0.1809 | +0.1755 ± 0.031 | 0.9856 | 0.5335 | 0.7393 | 0.259 | 0.3296 | -0.063 ± 0.0307 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1807 | 0.1827 | 0.183 | -0.0003 ± 0.0003 | 0.5406 | 0.5412 | 0.497 | 0.4823 | 0.5047 | -0.034 ± 0.0104 | -0.0133 (15) |
| 3-5 | 1149 | 0.1924 | 0.1917 | +0.0007 ± 0.001 | 0.5595 | 0.5578 | 0.5155 | 0.4755 | 0.4865 | -0.040 ± 0.0131 | 0.02 (1) |
| 5-10 | 2527 | 0.1913 | 0.1885 | +0.0027 ± 0.0013 | 0.5651 | 0.5551 | 0.5153 | 0.4415 | 0.4618 | -0.042 ± 0.0088 | -0.0117 (6) |
| 10-15 | 2215 | 0.1944 | 0.1808 | +0.0136 ± 0.0023 | 0.5736 | 0.5307 | 0.5176 | 0.3932 | 0.4036 | -0.058 ± 0.0092 | -0.02 (17) |
| 15-25 | 3221 | 0.2162 | 0.1767 | +0.0395 ± 0.0029 | 0.6282 | 0.5209 | 0.5322 | 0.3358 | 0.3365 | -0.073 ± 0.0075 | -0.0095 (41) |
| 25-40 | 2777 | 0.2481 | 0.1383 | +0.1097 ± 0.0045 | 0.7036 | 0.4215 | 0.5609 | 0.2445 | 0.2315 | -0.082 ± 0.0071 | -0.0113 (15) |
| 40+ | 2165 | 0.3991 | 0.0684 | +0.3307 ± 0.0064 | 1.0467 | 0.2374 | 0.6637 | 0.1271 | 0.1007 | -0.066 ± 0.0055 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 446 | 0.1916 | 0.1943 | -0.0027 ± 0.0007 | 0.5619 | 0.5686 | 0.4915 | 0.4763 | 0.5538 | +0.001 ± 0.0211 | -0.0137 (8) |
| 3-5 | 318 | 0.1875 | 0.1857 | +0.0018 ± 0.0019 | 0.5509 | 0.5463 | 0.4942 | 0.4548 | 0.4528 | -0.112 ± 0.0253 | 0.0067 (3) |
| 5-10 | 652 | 0.1993 | 0.1965 | +0.0029 ± 0.0026 | 0.5854 | 0.5751 | 0.5042 | 0.4305 | 0.4448 | -0.089 ± 0.0178 | -0.0071 (7) |
| 10-15 | 511 | 0.2085 | 0.2088 | -0.0002 ± 0.005 | 0.6048 | 0.6013 | 0.5373 | 0.4143 | 0.4795 | -0.059 ± 0.0201 | -0.044 (5) |
| 15-25 | 595 | 0.2355 | 0.2116 | +0.0239 ± 0.0073 | 0.6706 | 0.6077 | 0.5836 | 0.3902 | 0.4252 | -0.105 ± 0.0187 | -0.03 (1) |
| 25-40 | 365 | 0.2111 | 0.2128 | -0.0017 ± 0.0141 | 0.6098 | 0.6087 | 0.6502 | 0.3402 | 0.4959 | -0.040 ± 0.0215 | 0.0 (1) |
| 40+ | 67 | 0.3098 | 0.1842 | +0.1256 ± 0.0472 | 0.8354 | 0.5436 | 0.749 | 0.2957 | 0.3881 | -0.101 ± 0.0493 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2032 | 0.1831 | 0.1842 | -0.0011 ± 0.0003 | 0.5408 | 0.5429 | 0.4825 | 0.4672 | 0.5005 | -0.019 ± 0.0096 | -0.0163 (35) |
| 3-5 | 1391 | 0.1856 | 0.1828 | +0.0028 ± 0.0009 | 0.5477 | 0.5411 | 0.476 | 0.4367 | 0.4227 | -0.076 ± 0.0118 | -0.0094 (18) |
| 5-10 | 3082 | 0.1929 | 0.1871 | +0.0058 ± 0.0012 | 0.5697 | 0.5503 | 0.4793 | 0.4055 | 0.401 | -0.065 ± 0.0078 | -0.01 (31) |
| 10-15 | 2364 | 0.1952 | 0.1811 | +0.0140 ± 0.0022 | 0.5747 | 0.5322 | 0.4969 | 0.3736 | 0.3786 | -0.062 ± 0.0087 | -0.03 (9) |
| 15-25 | 3101 | 0.2094 | 0.1708 | +0.0386 ± 0.0029 | 0.6133 | 0.5052 | 0.5048 | 0.3096 | 0.3102 | -0.070 ± 0.0074 | -0.03 (2) |
| 25-40 | 2342 | 0.2144 | 0.1252 | +0.0892 ± 0.0046 | 0.6205 | 0.3848 | 0.5253 | 0.2097 | 0.2301 | -0.054 ± 0.007 | 0.0 (1) |
| 40+ | 1549 | 0.3869 | 0.0462 | +0.3407 ± 0.0062 | 1.0101 | 0.1788 | 0.6339 | 0.1077 | 0.0587 | -0.085 ± 0.0052 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 770 | 0.1969 | 0.1973 | -0.0003 ± 0.0006 | 0.5752 | 0.5756 | 0.5045 | 0.4895 | 0.4974 | -0.047 ± 0.016 | -0.0224 (49) |
| 3-5 | 551 | 0.1938 | 0.1936 | +0.0003 ± 0.0015 | 0.5657 | 0.5635 | 0.4796 | 0.4399 | 0.4537 | -0.043 ± 0.0188 | -0.0194 (34) |
| 5-10 | 1160 | 0.1958 | 0.1901 | +0.0057 ± 0.0019 | 0.5772 | 0.5613 | 0.4875 | 0.414 | 0.4129 | -0.063 ± 0.0131 | -0.0055 (77) |
| 10-15 | 728 | 0.2072 | 0.1968 | +0.0104 ± 0.0041 | 0.6026 | 0.5754 | 0.5034 | 0.3805 | 0.3984 | -0.051 ± 0.0165 | 0.0014 (64) |
| 15-25 | 979 | 0.2326 | 0.2123 | +0.0203 ± 0.0058 | 0.6635 | 0.6105 | 0.5626 | 0.368 | 0.4137 | -0.052 ± 0.0147 | -0.0216 (58) |
| 25-40 | 566 | 0.2514 | 0.1957 | +0.0557 ± 0.0115 | 0.7088 | 0.5686 | 0.6452 | 0.3324 | 0.3975 | -0.081 ± 0.0173 | -0.0219 (26) |
| 40+ | 193 | 0.3701 | 0.1933 | +0.1769 ± 0.0321 | 1.0713 | 0.5679 | 0.793 | 0.3026 | 0.3886 | -0.075 ± 0.029 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2302 | 0.1883 | 0.1884 | -0.0001 ± 0.0003 | 0.5525 | 0.5518 | 0.5025 | 0.4871 | 0.4978 | -0.034 ± 0.009 | -0.0157 (88) |
| 3-5 | 1585 | 0.1879 | 0.1855 | +0.0024 ± 0.0009 | 0.5502 | 0.5445 | 0.4885 | 0.4489 | 0.4391 | -0.056 ± 0.0109 | -0.0209 (69) |
| 5-10 | 3239 | 0.1927 | 0.1852 | +0.0075 ± 0.0011 | 0.5698 | 0.5482 | 0.4806 | 0.407 | 0.3958 | -0.063 ± 0.0077 | -0.0085 (131) |
| 10-15 | 2173 | 0.2037 | 0.1894 | +0.0143 ± 0.0023 | 0.5948 | 0.557 | 0.5095 | 0.3864 | 0.3898 | -0.056 ± 0.0093 | -0.0053 (105) |
| 15-25 | 2736 | 0.2296 | 0.1985 | +0.0310 ± 0.0033 | 0.6623 | 0.5765 | 0.5547 | 0.3597 | 0.379 | -0.059 ± 0.0086 | -0.0255 (106) |
| 25-40 | 1866 | 0.2538 | 0.1695 | +0.0843 ± 0.006 | 0.7196 | 0.5008 | 0.607 | 0.2926 | 0.3178 | -0.075 ± 0.0092 | -0.0229 (51) |
| 40+ | 908 | 0.3842 | 0.1314 | +0.2528 ± 0.0128 | 1.0905 | 0.4006 | 0.7088 | 0.202 | 0.2192 | -0.068 ± 0.0115 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2954 | 1.062 ± 0.052 | 1.173 | 0.169 | 0.1715 | 0.2108 | 0.2021 |
| gen2 | 2954 | 0.867 ± 0.047 | 1.123 | 0.1774 | 0.1715 | 0.2289 | 0.2019 |
| gen1_elo | 2954 | 1.043 ± 0.05 | 1.163 | 0.1739 | 0.172 | 0.2097 | 0.2019 |
| gen1_sr | 2954 | 1.078 ± 0.061 | 1.191 | 0.1366 | 0.1734 | 0.2248 | 0.2017 |
| gen1_ledger | 4947 | 0.872 ± 0.035 | 1.075 | 0.1773 | 0.1863 | 0.2179 | 0.1977 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 13,840)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,491 | 25.2% |
| STALE_QUOTE | market_freshness | 2,858 | 20.6% |
| BOOK_QUALITY | execution | 2,488 | 18.0% |
| POOR_DATA | data | 1,523 | 11.0% |
| LIMITED_DATA | data | 993 | 7.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 758 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 656 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 531 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 391 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 151 | 1.1% |

Cause class: coverage 25.2%, market_freshness 20.6%, data 18.2%, execution 18.0%, market_freshness/coverage 8.3%, model_calibration_or_unknown 4.7%, mapping 3.8%, model_calibration 1.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.1%, START_UNVERIFIABLE 96.0%, LOW_DATA_QUALITY 69.2%, THIN_PLAYER_HISTORY 58.0%, STALE_PLAYER_DATA 52.9%, STALE_KALSHI_QUOTE 45.5%, MODEL_INTERNAL_DISAGREEMENT 39.2%, ASYMMETRIC_SAMPLE_SIZE 31.8%, WIDE_SPREAD 23.8%, MODEL_HIGH_UNCERTAINTY 17.1%, PLAYER_IDENTITY_RISK 13.8%, LEVEL_TRANSFER_RISK 8.4%, EVENT_MAPPING_RISK 8.0%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 3.5%, EXTERNAL_MARKET_REJECTION 1.8%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 27.6%, POST_SETTLEMENT_OBSERVATION 25.2%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 7,424)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,755 | 37.1% |
| STALE_QUOTE | market_freshness | 1,309 | 17.6% |
| BOOK_QUALITY | execution | 1,300 | 17.5% |
| POOR_DATA | data | 615 | 8.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 409 | 5.5% |
| IDENTITY_AMBIGUOUS | mapping | 321 | 4.3% |
| LIMITED_DATA | data | 295 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 241 | 3.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 145 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 34 | 0.5% |

Cause class: coverage 37.1%, market_freshness 17.6%, execution 17.5%, data 12.3%, market_freshness/coverage 8.8%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.0%, START_UNVERIFIABLE 98.3%, LOW_DATA_QUALITY 72.8%, THIN_PLAYER_HISTORY 60.3%, STALE_KALSHI_QUOTE 53.7%, STALE_PLAYER_DATA 48.1%, MODEL_INTERNAL_DISAGREEMENT 40.2%, ASYMMETRIC_SAMPLE_SIZE 33.7%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 17.6%, PLAYER_IDENTITY_RISK 17.4%, EVENT_MAPPING_RISK 9.8%, LOW_DISPLAYED_LIQUIDITY 8.0%, LEVEL_TRANSFER_RISK 7.4%, MODEL_CALIBRATION_OUTLIER 4.5%, EXTERNAL_MARKET_REJECTION 0.9%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 39.9%, POST_SETTLEMENT_OBSERVATION 37.1%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 5943, "IDENTITY_AMBIGUOUS": 1481}; ticker orientation: {"VERIFIED": 7424}.

Checks: discipline:AMBIGUOUS 511, discipline:PASS 6913, identity_confidence:AMBIGUOUS 1289, identity_confidence:PASS 6135, level_mapping:NA 523, level_mapping:PASS 6901, market_pair:AMBIGUOUS 272, market_pair:NA 175, market_pair:PASS 6977, model_complement:NA 142, model_complement:PASS 7282, namesake:PASS 7424, physical_match_id:NA 2843, physical_match_id:PASS 4581, player_ids:PASS 7424, same_pair_other_event:PASS 7424, ticker_orientation:PASS 7424

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,064 | 1.4% | 1.4% | 0.4% | {"market_freshness": 20, "execution": 8, "market_freshness/coverage": 1} | 5.24 | 0.2093 / 0.2118 (255) | 16.4% | 0.5% | 5.4% | 1.7% |
| CHALLENGER | 5,345 | 17.0% | 5.9% | 12.2% | {"coverage": 550, "market_freshness/coverage": 112, "market_freshness": 111, "data": 58, "model_calibration_or_unknown": 47, "execution": 13, "model_calibration": 9, "mapping": 6} | 7.2 | 0.2171 / 0.2038 (1402) | 37.6% | 9.2% | 2.4% | 22.5% |
| DOUBLES | 1,025 | 49.9% | 49.1% | 6.9% | {"execution": 208, "mapping": 151, "market_freshness": 106, "market_freshness/coverage": 39, "coverage": 7} | 24.2 | 0.331 / 0.2339 (314) | 22.8% | 0.0% | 100.0% | 7.7% |
| ITF_MEN | 10,024 | 24.4% | 16.8% | 33.0% | {"coverage": 953, "execution": 508, "market_freshness": 372, "data": 327, "market_freshness/coverage": 202, "mapping": 85, "model_calibration_or_unknown": 2} | 11.02 | 0.2127 / 0.1948 (2492) | 36.7% | 60.1% | 11.5% | 22.9% |
| ITF_WOMEN | 12,465 | 26.1% | 18.5% | 43.8% | {"coverage": 1228, "market_freshness": 625, "execution": 542, "data": 491, "market_freshness/coverage": 250, "mapping": 73, "model_calibration_or_unknown": 35, "model_calibration": 10} | 12.44 | 0.202 / 0.1922 (2662) | 39.2% | 57.8% | 10.0% | 22.9% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,600 | 6.2% | 5.5% | 1.3% | {"market_freshness": 36, "model_calibration_or_unknown": 22, "data": 11, "market_freshness/coverage": 10, "model_calibration": 8, "execution": 7, "coverage": 4, "mapping": 1} | 7.84 | 0.2398 / 0.2312 (289) | 26.4% | 1.3% | 1.7% | 3.4% |
| WTA125 | 1,283 | 12.8% | 10.1% | 2.2% | {"model_calibration_or_unknown": 37, "market_freshness": 37, "market_freshness/coverage": 35, "data": 23, "coverage": 12, "execution": 9, "model_calibration": 7, "mapping": 4} | 9.52 | 0.2155 / 0.2057 (445) | 23.6% | 8.0% | 4.2% | 10.1% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 5 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 6 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 7 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 15.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 928 min (STALE); no external reference |
| 8 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 9 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 10 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 11 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 12 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 13 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 14 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 15 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 16 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 17 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 18 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 19 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 20 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 21 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 22 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 23 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 24 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 25 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 26 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 27 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 28 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 29 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 30 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 31 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 874 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 32 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 33 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 34 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 33 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 35 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 36 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 37 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 39 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 40 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 41 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 42 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 43 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 44 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 45 | `KXATPCHALLENGERMATCH-26OCT13GIUSEA-SEA` | CHALLENGER | fair_v1 | 76% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 243 min (STALE); no external reference |
| 46 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 760 min (STALE); no external reference |
| 47 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 48 | `KXITFWMATCH-26OCT13MAMSTR-MAM` | ITF_WOMEN | fair_v1 | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 406 min (STALE); data LIMITED (grade C, thinner serve sample 879.0, ratio 2.64); no external reference |
| 49 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 50 | `KXITFMATCH-26OCT13VISMUE-MUE` | ITF_MEN | fair_v1 | 25% / 98% | -74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 103 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 0.0); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9827, "by_level_share_of_ge_25pp": {"ATP": 0.0039, "CHALLENGER": 0.122, "DOUBLES": 0.0688, "ITF_MEN": 0.3299, "ITF_WOMEN": 0.4383, "OTHER": 0.0016, "WTA": 0.0133, "WTA125": 0.0221}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5374, "share_primary_cause_market_settled_or_in_play": 0.4587, "share_primary_cause_stale_quote_only": 0.1763}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 7424, "identity_ambiguous_share": 0.1995, "ticker_orientation": {"VERIFIED": 7424}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 4581, "with_external": 168, "coverage": 0.0367, "external_status": {"EXTERNAL_STALE": 118, "AGREES_WITH_KALSHI": 47, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 118, "MODEL_LONE_OUTLIER": 47, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.2798, "share_external_supports_model": 0.0179}, "pregame_clean_ge_25pp": {"n": 2135, "with_external": 158, "coverage": 0.074, "external_status": {"EXTERNAL_STALE": 110, "AGREES_WITH_KALSHI": 45, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 110, "MODEL_LONE_OUTLIER": 45, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.2848, "share_external_supports_model": 0.019}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 553.0, "median_sample_ratio": 2.39, "median_min_matches": 20.0, "median_max_days_since_last": 204.0, "share_severe_asymmetry": 0.2015, "data_status": {"POOR": 3967, "LIMITED": 2116, "ADEQUATE": 1341}, "comparison_lt_10pp": {"median_thinner_serve_points": 1787.0, "median_sample_ratio": 1.7, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 607, "model_minus_observed": 0.0498, "kalshi_minus_observed": -0.0816, "brier_diff_model_minus_kalshi": -0.0}, "4-10x": {"n": 405, "model_minus_observed": 0.0732, "kalshi_minus_observed": -0.0649, "brier_diff_model_minus_kalshi": 0.007}, "<2x": {"n": 1461, "model_minus_observed": 0.0827, "kalshi_minus_observed": -0.0399, "brier_diff_model_minus_kalshi": 0.0111}, ">=10x": {"n": 481, "model_minus_observed": 0.1169, "kalshi_minus_observed": -0.051, "brier_diff_model_minus_kalshi": 0.014}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2954, "model": {"intercept": -0.543, "slope": 0.867, "slope_se": 0.047}, "kalshi_mid_same_rows": {"intercept": 0.234, "slope": 1.123, "slope_se": 0.053}, "mean_extremity_model": 0.1774, "mean_extremity_kalshi": 0.1715, "model_brier": 0.2289, "kalshi_brier": 0.2019, "brier_diff_model_minus_kalshi": 0.027, "brier_diff_se": 0.0035, "model_logloss": 0.6533, "kalshi_logloss": 0.5858}, "fair_v1": {"n": 2954, "model": {"intercept": -0.391, "slope": 1.062, "slope_se": 0.052}, "kalshi_mid_same_rows": {"intercept": 0.325, "slope": 1.173, "slope_se": 0.054}, "mean_extremity_model": 0.169, "mean_extremity_kalshi": 0.1715, "model_brier": 0.2108, "kalshi_brier": 0.2021, "brier_diff_model_minus_kalshi": 0.0087, "brier_diff_se": 0.0028, "model_logloss": 0.6088, "kalshi_logloss": 0.5859}, "gen1_elo": {"n": 2954, "model": {"intercept": -0.373, "slope": 1.043, "slope_se": 0.05}, "kalshi_mid_same_rows": {"intercept": 0.327, "slope": 1.163, "slope_se": 0.053}, "mean_extremity_model": 0.1739, "mean_extremity_kalshi": 0.172, "model_brier": 0.2097, "kalshi_brier": 0.2019, "brier_diff_model_minus_kalshi": 0.0078, "brier_diff_se": 0.0028, "model_logloss": 0.6073, "kalshi_logloss": 0.5856}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2432, "share_ge_15": 0.436, "median_abs_gap": 12.95, "n": 18835}, "gen1_elo": {"share_ge_25": 0.2375, "share_ge_15": 0.4293, "median_abs_gap": 12.46, "n": 18835}, "gen1_sr": {"share_ge_25": 0.3048, "share_ge_15": 0.5232, "median_abs_gap": 15.87, "n": 18835}, "gen2": {"share_ge_25": 0.3055, "share_ge_15": 0.5088, "median_abs_gap": 15.44, "n": 18835}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1474, "share_ge_15": 0.346, "median_abs_gap": 10.6, "n": 14480}, "gen1_elo": {"share_ge_25": 0.1452, "share_ge_15": 0.3353, "median_abs_gap": 10.07, "n": 14479}, "gen1_sr": {"share_ge_25": 0.2094, "share_ge_15": 0.4433, "median_abs_gap": 13.21, "n": 14480}, "gen2": {"share_ge_25": 0.2228, "share_ge_15": 0.4398, "median_abs_gap": 12.98, "n": 14481}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.24, "share_ge_25_all": 0.0141, "share_ge_25_pregame_clean": 0.0138}, "WTA": {"median_abs_gap_pregame_clean": 7.84, "share_ge_25_all": 0.0619, "share_ge_25_pregame_clean": 0.055}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2385, "share_within_10pp_all": 0.4393, "share_within_10pp_pregame_clean": 0.4978, "corr_model_vs_mid_pregame_clean": 0.8463}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 451, "model_brier": 0.1928, "kalshi_brier": 0.1943, "brier_diff_model_minus_kalshi": -0.0015}, "10-15": {"n_settled": 525, "model_brier": 0.2119, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.0086}, "15-25": {"n_settled": 645, "model_brier": 0.2303, "kalshi_brier": 0.2177, "brier_diff_model_minus_kalshi": 0.0127}, "25-40": {"n_settled": 349, "model_brier": 0.2254, "kalshi_brier": 0.2087, "brier_diff_model_minus_kalshi": 0.0167}, "3-5": {"n_settled": 288, "model_brier": 0.1905, "kalshi_brier": 0.1907, "brier_diff_model_minus_kalshi": -0.0003}, "40+": {"n_settled": 72, "model_brier": 0.29, "kalshi_brier": 0.1741, "brier_diff_model_minus_kalshi": 0.116}, "5-10": {"n_settled": 624, "model_brier": 0.1947, "kalshi_brier": 0.1953, "brier_diff_model_minus_kalshi": -0.0005}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.543, "slope": 0.867, "slope_se": 0.047}, "kalshi_slope": {"intercept": 0.234, "slope": 1.123, "slope_se": 0.053}, "n": 2954}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.508, "slope": 0.872, "slope_se": 0.035}, "kalshi_slope": {"intercept": 0.152, "slope": 1.075, "slope_se": 0.039}, "n": 4947}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 314, "model_brier": 0.331, "kalshi_brier": 0.2339, "brier_diff_model_minus_kalshi": 0.0971, "brier_diff_se": 0.0179, "corr_model_outcome": -0.0027, "corr_kalshi_outcome": 0.2513}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
