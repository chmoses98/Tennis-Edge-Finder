# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-07T11:54Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 22,262): 0-3 13.6%, 3-5 9.6%, 5-10 19.8%, 10-15 15.4%, 15-25 18.9%, 25-40 14.3%, 40+ 8.4%; median gap 12.15 pp.
* **Where the extremes live**: 98.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.5%, Challenger 13.0%, doubles 4.9%). Main tour: ATP 1.9% and WTA 8.3% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 5,067): MARKET_ALREADY_SETTLED_WHEN_PRICED 39.2%, STALE_QUOTE 19.2%, BOOK_QUALITY 16.8%, POOR_DATA 8.6%, POSSIBLY_IN_PLAY_QUOTE 4.8%, LIMITED_DATA 3.8%, IN_PLAY_QUOTE 2.9%, IDENTITY_AMBIGUOUS 2.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.3%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.1%. By class: coverage 39.2%, market_freshness 19.2%, execution 16.8%, data 12.3%, market_freshness/coverage 7.7%, mapping 2.5%, model_calibration_or_unknown 2.3%, model_calibration 0.1%.
* **Stale / settled / in-play**: 57.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 46.9% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 5,067 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 16.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 1.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 11.4% of the time and with the model 0.2%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 601.0 points vs 1723.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.164, Gen-2 0.942, Gen-1 ledger 0.947 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 189 model 0.2089 vs Kalshi 0.197; n 44 model 0.2973 vs Kalshi 0.1575.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%). Not implemented here.

## 1. Observations

* 82,797 model-market comparisons (139,202 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 31,956 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-07T11:46:56.955158+00:00'], shadow board 23,026 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-07T11:47:01.087698+00:00'], Model 4 8,254 rows, 9,931 settled tickers, 2,491 tickers with an external scan.
* By model: {"gen1_ledger": 20260, "gen1_elo": 11570, "fair_v1": 11570, "gen2": 11570, "gen1_sr": 11570, "model4_fundamental": 8133, "model4_conditioned": 8124}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 22,262 | 13.6 | 9.6 | 19.8 | 15.4 | 18.9 | 14.3 | 8.4 | 12.15 | 41.7% | 22.8% |
| MW fair_v1 | 11,570 | 12.8 | 8.9 | 18.4 | 16.0 | 18.6 | 15.2 | 10.0 | 13.05 | 43.9% | 25.2% |
| MW gen1_elo | 11,570 | 12.7 | 8.9 | 19.6 | 15.0 | 19.5 | 14.7 | 9.5 | 12.63 | 43.7% | 24.2% |
| MW gen1_ledger | 10,692 | 14.3 | 10.3 | 21.4 | 14.7 | 19.2 | 13.3 | 6.7 | 11.19 | 39.3% | 20.1% |
| MW gen1_sr | 11,570 | 10.0 | 7.8 | 16.0 | 14.2 | 21.8 | 18.6 | 11.7 | 15.76 | 52.1% | 30.3% |
| MW gen2 | 11,570 | 11.7 | 7.1 | 16.0 | 14.5 | 19.9 | 17.5 | 13.3 | 15.38 | 50.7% | 30.8% |
| all families model4_conditioned | 8,124 | 21.8 | 20.4 | 34.9 | 16.3 | 4.8 | 0.9 | 0.8 | 5.79 | 6.6% | 1.7% |
| all families model4_fundamental | 8,133 | 16.5 | 13.3 | 34.4 | 20.3 | 11.1 | 3.2 | 1.2 | 7.77 | 15.5% | 4.4% |

Configurable thresholds (primary): >=5pp 76.9%, >=10pp 57.1%, >=15pp 41.7%, >=20pp 31.2%, >=25pp 22.8%, >=30pp 16.6%, >=40pp 8.5%, >=50pp 3.6%
Executable gap (model outside the book, before fees): median 8.53pp; >=10pp 45.8%, >=25pp 18.3%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 812 | 25.7 | 17.0 | 24.4 | 17.0 | 13.1 | 1.5 | 1.4 | 5.94 | 15.9% | 2.8% |
| CHALLENGER | 2,084 | 14.3 | 11.4 | 18.5 | 16.3 | 13.1 | 13.3 | 13.1 | 12.01 | 39.4% | 26.4% |
| ITF_MEN | 3,296 | 10.6 | 8.4 | 18.8 | 14.6 | 19.7 | 15.1 | 12.9 | 14.02 | 47.6% | 27.9% |
| ITF_WOMEN | 4,563 | 10.4 | 6.6 | 16.0 | 16.1 | 21.8 | 19.5 | 9.6 | 15.4 | 50.8% | 29.0% |
| WTA | 520 | 23.1 | 9.6 | 24.6 | 16.5 | 17.7 | 6.3 | 2.1 | 8.32 | 26.2% | 8.5% |
| WTA125 | 295 | 12.5 | 6.8 | 20.7 | 25.4 | 14.2 | 17.6 | 2.7 | 11.47 | 34.6% | 20.3% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 812 | 21.4 | 15.0 | 24.3 | 18.2 | 16.9 | 2.6 | 1.6 | 6.9 | 21.1% | 4.2% |
| CHALLENGER | 2,084 | 14.9 | 7.3 | 17.8 | 13.6 | 18.5 | 14.5 | 13.4 | 13.38 | 46.5% | 28.0% |
| ITF_MEN | 3,296 | 10.2 | 7.1 | 16.7 | 14.8 | 20.0 | 17.7 | 13.5 | 15.46 | 51.1% | 31.2% |
| ITF_WOMEN | 4,563 | 8.9 | 6.2 | 13.0 | 13.2 | 20.9 | 21.4 | 16.4 | 18.74 | 58.7% | 37.8% |
| WTA | 520 | 21.5 | 4.8 | 17.5 | 15.6 | 21.7 | 16.7 | 2.1 | 12.96 | 40.6% | 18.9% |
| WTA125 | 295 | 5.1 | 2.4 | 16.6 | 23.7 | 19.3 | 20.0 | 12.9 | 16.74 | 52.2% | 32.9% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 812 | 25.6 | 11.7 | 29.4 | 17.2 | 10.8 | 3.7 | 1.5 | 6.85 | 16.0% | 5.2% |
| CHALLENGER | 2,084 | 15.6 | 11.2 | 19.7 | 14.2 | 14.0 | 12.4 | 13.0 | 10.93 | 39.3% | 25.3% |
| ITF_MEN | 3,296 | 9.5 | 8.9 | 18.4 | 13.7 | 21.2 | 15.4 | 13.0 | 14.94 | 49.6% | 28.4% |
| ITF_WOMEN | 4,563 | 9.7 | 6.8 | 16.6 | 15.7 | 23.7 | 19.1 | 8.3 | 15.51 | 51.2% | 27.4% |
| WTA | 520 | 23.3 | 12.9 | 34.8 | 14.4 | 9.6 | 3.6 | 1.4 | 6.99 | 14.6% | 5.0% |
| WTA125 | 295 | 21.0 | 11.9 | 27.8 | 18.0 | 15.2 | 5.4 | 0.7 | 7.73 | 21.4% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 410 | 28.1 | 21.2 | 37.8 | 11.7 | 1.2 | 0.0 | 0.0 | 5.17 | 1.2% | 0.0% |
| CHALLENGER | 1,347 | 22.8 | 16.2 | 26.7 | 14.2 | 12.2 | 5.6 | 2.2 | 6.78 | 20.1% | 7.9% |
| DOUBLES | 566 | 3.9 | 3.2 | 13.2 | 12.0 | 23.5 | 21.0 | 23.1 | 22.7 | 67.7% | 44.2% |
| ITF_MEN | 3,391 | 13.5 | 8.4 | 20.0 | 15.2 | 20.7 | 13.5 | 8.6 | 12.34 | 42.9% | 22.1% |
| ITF_WOMEN | 3,935 | 11.4 | 9.3 | 19.2 | 14.0 | 22.4 | 17.6 | 6.2 | 13.37 | 46.1% | 23.7% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 429 | 19.4 | 11.7 | 25.6 | 19.4 | 15.8 | 7.5 | 0.7 | 8.66 | 24.0% | 8.2% |
| WTA125 | 465 | 15.3 | 12.7 | 22.1 | 19.6 | 17.9 | 9.5 | 3.0 | 9.95 | 30.3% | 12.5% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 808 | 25.7 | 16.8 | 24.4 | 17.1 | 13.1 | 1.5 | 1.4 | 5.95 | 16.0% | 2.9% |
| CHALLENGER | 1,490 | 18.6 | 14.6 | 23.8 | 18.9 | 14.0 | 7.2 | 3.0 | 8.45 | 24.2% | 10.3% |
| ITF_MEN | 2,423 | 12.8 | 10.6 | 22.1 | 16.1 | 19.7 | 12.5 | 6.3 | 11.21 | 38.5% | 18.8% |
| ITF_WOMEN | 3,355 | 12.6 | 8.2 | 18.7 | 18.4 | 23.2 | 15.6 | 3.2 | 12.8 | 42.1% | 18.8% |
| WTA | 518 | 23.2 | 9.7 | 24.7 | 16.4 | 17.8 | 6.2 | 2.1 | 8.25 | 26.1% | 8.3% |
| WTA125 | 284 | 13.0 | 7.0 | 20.4 | 25.7 | 14.4 | 17.6 | 1.8 | 11.31 | 33.8% | 19.4% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 808 | 21.3 | 15.0 | 24.4 | 18.2 | 17.0 | 2.6 | 1.6 | 6.9 | 21.2% | 4.2% |
| CHALLENGER | 1,490 | 19.4 | 9.5 | 22.4 | 16.4 | 19.1 | 10.3 | 3.0 | 9.66 | 32.4% | 13.2% |
| ITF_MEN | 2,423 | 12.1 | 8.5 | 19.4 | 16.7 | 21.0 | 15.3 | 7.1 | 12.83 | 43.3% | 22.4% |
| ITF_WOMEN | 3,355 | 10.3 | 7.2 | 14.8 | 14.3 | 22.8 | 20.0 | 10.5 | 16.26 | 53.3% | 30.5% |
| WTA | 518 | 21.6 | 4.8 | 17.6 | 15.6 | 21.6 | 16.6 | 2.1 | 12.85 | 40.4% | 18.7% |
| WTA125 | 284 | 5.3 | 2.5 | 16.9 | 24.6 | 18.3 | 20.8 | 11.6 | 15.57 | 50.7% | 32.4% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 395 | 28.4 | 21.5 | 38.0 | 11.9 | 0.2 | 0.0 | 0.0 | 5.02 | 0.2% | 0.0% |
| CHALLENGER | 1,133 | 24.9 | 18.4 | 29.1 | 13.8 | 11.6 | 2.1 | 0.2 | 6.16 | 13.9% | 2.3% |
| DOUBLES | 515 | 3.9 | 3.1 | 13.6 | 11.8 | 24.1 | 20.8 | 22.7 | 22.7 | 67.6% | 43.5% |
| ITF_MEN | 2,723 | 15.3 | 9.4 | 22.2 | 16.3 | 20.6 | 11.2 | 5.0 | 11.04 | 36.8% | 16.2% |
| ITF_WOMEN | 3,189 | 12.8 | 10.2 | 21.1 | 14.9 | 22.6 | 15.8 | 2.6 | 11.66 | 40.9% | 18.3% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 399 | 19.8 | 12.3 | 26.3 | 19.6 | 16.3 | 5.8 | 0.0 | 8.4 | 22.1% | 5.8% |
| WTA125 | 382 | 17.3 | 14.1 | 24.9 | 22.5 | 16.0 | 5.0 | 0.3 | 8.89 | 21.2% | 5.2% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 566 | 3.9 | 3.2 | 13.2 | 12.0 | 23.5 | 21.0 | 23.1 | 22.7 | 67.7% | 44.2% |
| singles | 10,126 | 14.9 | 10.7 | 21.8 | 14.8 | 19.0 | 12.9 | 5.8 | 10.68 | 37.7% | 18.7% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 2,716 | 13.1 | 9.6 | 20.1 | 15.7 | 16.2 | 14.6 | 10.7 | 12.26 | 41.5% | 25.3% |
| Hard | 7,799 | 12.8 | 8.7 | 18.4 | 15.9 | 19.3 | 15.1 | 9.8 | 13.24 | 44.3% | 24.9% |
| UNKNOWN | 1,055 | 12.3 | 8.2 | 13.7 | 18.3 | 19.8 | 17.6 | 10.1 | 14.11 | 47.5% | 27.7% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,347 | 17.8 | 11.4 | 20.3 | 17.1 | 15.0 | 10.2 | 8.2 | 10.09 | 33.4% | 18.4% |
| B | 1,442 | 15.1 | 9.8 | 19.8 | 17.2 | 16.3 | 11.9 | 10.0 | 11.14 | 38.1% | 21.8% |
| C | 1,789 | 12.5 | 9.7 | 21.2 | 15.1 | 18.3 | 14.2 | 8.9 | 12.44 | 41.5% | 23.1% |
| D | 2,188 | 11.5 | 8.8 | 16.4 | 16.2 | 23.1 | 15.3 | 8.8 | 14.08 | 47.1% | 24.0% |
| F | 2,804 | 7.1 | 4.9 | 15.0 | 14.7 | 21.0 | 23.5 | 14.0 | 18.57 | 58.4% | 37.5% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 2,946 | 21.1 | 14.9 | 27.2 | 16.0 | 13.2 | 5.4 | 2.2 | 7.3 | 20.9% | 7.6% |
| B | 1,621 | 14.2 | 9.9 | 24.2 | 15.4 | 18.7 | 12.1 | 5.5 | 10.42 | 36.3% | 17.6% |
| C | 2,098 | 12.0 | 8.2 | 19.4 | 14.8 | 21.1 | 14.6 | 9.9 | 13.16 | 45.6% | 24.5% |
| D | 1,822 | 12.8 | 9.0 | 21.0 | 13.3 | 22.4 | 15.0 | 6.4 | 12.64 | 43.9% | 21.5% |
| F | 2,205 | 9.0 | 7.7 | 13.7 | 13.3 | 23.2 | 22.3 | 10.8 | 17.3 | 56.3% | 33.1% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 3,807 | 16.9 | 10.6 | 19.6 | 17.3 | 15.2 | 10.5 | 9.9 | 10.8 | 35.6% | 20.4% |
| LIMITED | 2,735 | 14.2 | 10.5 | 21.8 | 15.5 | 17.4 | 13.4 | 7.2 | 11.02 | 38.0% | 20.6% |
| POOR | 5,028 | 9.1 | 6.6 | 15.6 | 15.4 | 21.9 | 19.8 | 11.7 | 16.37 | 53.4% | 31.4% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,717 | 29.7 | 26.3 | 36.7 | 5.4 | 1.7 | 0.2 | 0.0 | 4.46 | 1.9% | 0.2% |
| GAME_SPREAD | 1,784 | 23.9 | 15.3 | 36.9 | 18.8 | 4.6 | 0.3 | 0.2 | 6.2 | 5.0% | 0.4% |
| MATCH_WINNER | 10,692 | 14.3 | 10.3 | 21.4 | 14.7 | 19.2 | 13.3 | 6.7 | 11.19 | 39.3% | 20.1% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 3,342 | 29.1 | 18.8 | 31.5 | 11.5 | 7.5 | 1.4 | 0.3 | 5.25 | 9.2% | 1.7% |
| TOTAL_GAMES | 2,701 | 7.7 | 9.4 | 37.8 | 29.3 | 10.1 | 3.3 | 2.4 | 9.45 | 15.8% | 5.7% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,976 | 24.6 | 39.4 | 28.9 | 0.3 | 6.0 | 0.6 | 0.2 | 4.33 | 6.8% | 0.8% |
| GAME_SPREAD | 2,050 | 45.4 | 14.2 | 29.8 | 8.7 | 1.1 | 0.6 | 0.2 | 3.59 | 1.8% | 0.8% |
| TOTAL_GAMES | 3,098 | 3.5 | 6.3 | 44.1 | 36.7 | 6.2 | 1.5 | 1.8 | 9.69 | 9.5% | 3.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,976 | 25.4 | 18.2 | 35.5 | 9.8 | 7.4 | 3.1 | 0.5 | 5.61 | 11.0% | 3.6% |
| GAME_SPREAD | 2,050 | 19.4 | 13.4 | 26.4 | 22.8 | 14.2 | 3.1 | 0.7 | 8.32 | 18.0% | 3.8% |
| TOTAL_GAMES | 3,107 | 6.0 | 8.5 | 38.5 | 28.8 | 12.7 | 3.4 | 2.2 | 9.67 | 18.2% | 5.6% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 11,570 | 43.9% | 25.2% | 13.05 | 34.5% | 15.3% | 10.6 |
| gen1_elo | 11,570 | 43.7% | 24.2% | 12.63 | 34.1% | 14.6% | 10.16 |
| gen1_sr | 11,570 | 52.1% | 30.3% | 15.76 | 43.7% | 20.4% | 13.01 |
| gen2 | 11,570 | 50.7% | 30.8% | 15.38 | 43.3% | 22.4% | 12.79 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 5,544 | 15.4 | 11.5 | 21.6 | 17.2 | 18.7 | 12.0 | 3.6 | 10.39 | 34.3% | 15.6% |
| STALE | 6,026 | 10.5 | 6.5 | 15.4 | 14.9 | 18.6 | 18.2 | 16.0 | 16.45 | 52.7% | 34.1% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 4,160 | 16.3 | 11.5 | 24.0 | 14.5 | 17.3 | 12.1 | 4.3 | 9.57 | 33.7% | 16.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 22,262 | 4160 | 9016 | 9086 | 25.7 | 165.3 | 1400.4 |
| ge_15pp | 9,280 | 1402 | 3192 | 4686 | 30.3 | 440.2 | 1380.4 |
| ge_25pp | 5,067 | 683 | 1456 | 2928 | 39.8 | 555.5 | 1380.4 |
| lt_10pp | 9,559 | 2154 | 4318 | 3087 | 24.4 | 52.9 | 1201.9 |

Current slate `SL-20261007T115359Z-7c8635b8`: 466 priced rows, quote age at build {'median': 7.4, 'max': 7.5}, freshness {'FRESH': 466}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 1 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 20.71 | 100.0% | 0.0% |
| EXTERNAL_LONE_OUTLIER | 2 | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.98 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 388 | 20.1 | 12.1 | 22.2 | 21.1 | 17.0 | 7.0 | 0.5 | 8.32 | 24.5% | 7.5% |
| MARKETS_AGREE | 35 | 71.4 | 28.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 55 | 0.0 | 3.6 | 23.6 | 38.2 | 25.4 | 9.1 | 0.0 | 12.56 | 34.5% | 9.1% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 11,570 | 481 (4.2%) | 11.4% | 0.2% | {"EXTERNAL_STALE": 388, "AGREES_WITH_KALSHI": 55, "ALL_AGREE": 35, "EXTERNAL_OUTLIER": 2, "SUPPORTS_MODEL_DIRECTION": 1} |
| fair_v1_ge_15pp | 5,079 | 115 (2.3%) | 16.5% | 0.9% | {"EXTERNAL_STALE": 95, "AGREES_WITH_KALSHI": 19, "SUPPORTS_MODEL_DIRECTION": 1} |
| fair_v1_ge_25pp | 2,922 | 34 (1.2%) | 14.7% | 0.0% | {"EXTERNAL_STALE": 29, "AGREES_WITH_KALSHI": 5} |
| fair_v1_ge_25pp_pregame_clean | 1,361 | 34 (2.5%) | 14.7% | 0.0% | {"EXTERNAL_STALE": 29, "AGREES_WITH_KALSHI": 5} |
| fair_v1_lt_10pp | 4,636 | 263 (5.7%) | 5.7% | 0.0% | {"EXTERNAL_STALE": 211, "ALL_AGREE": 35, "AGREES_WITH_KALSHI": 15, "EXTERNAL_OUTLIER": 2} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 2,312 | 11.1 | 8.6 | 20.7 | 15.6 | 21.0 | 13.9 | 9.0 | 12.79 | 44.0% | 23.0% |
| 4-10x | 1,710 | 11.2 | 9.5 | 18.1 | 14.5 | 20.9 | 17.1 | 8.8 | 13.96 | 46.8% | 25.9% |
| <2x | 6,047 | 14.7 | 9.5 | 18.3 | 16.9 | 17.0 | 13.6 | 9.9 | 12.24 | 40.6% | 23.5% |
| >=10x | 1,501 | 10.1 | 5.9 | 15.2 | 14.8 | 19.0 | 21.4 | 13.5 | 16.84 | 54.0% | 35.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 2,914 | 13.7 | 8.4 | 20.6 | 15.9 | 17.4 | 13.1 | 10.9 | 12.14 | 41.4% | 24.0% |
| 300-1000 | 2,801 | 12.2 | 9.5 | 16.7 | 16.0 | 21.8 | 15.8 | 8.1 | 13.67 | 45.7% | 23.9% |
| <300 | 3,266 | 7.9 | 6.0 | 15.4 | 14.8 | 20.9 | 21.6 | 13.4 | 17.52 | 55.9% | 35.0% |
| >=3000 | 2,589 | 18.7 | 12.3 | 21.5 | 17.8 | 13.8 | 8.9 | 7.0 | 9.43 | 29.7% | 15.9% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 333 | 0.5353 | 0.4021 | 0.4625 | +0.073 | -0.060 | 0.0022 ± 0.0078 |
| ratio 4-10x | 252 | 0.5865 | 0.4473 | 0.5357 | +0.051 | -0.088 | -0.0048 ± 0.0097 |
| ratio <2x | 702 | 0.5391 | 0.4137 | 0.4615 | +0.078 | -0.048 | 0.0098 ± 0.0054 |
| ratio >=10x | 233 | 0.5554 | 0.3803 | 0.4506 | +0.105 | -0.070 | 0.0151 ± 0.012 |
| thinner_sample 1000-3000 | 393 | 0.5389 | 0.4175 | 0.4555 | +0.083 | -0.038 | 0.0047 ± 0.007 |
| thinner_sample 300-1000 | 414 | 0.5701 | 0.4318 | 0.5 | +0.070 | -0.068 | -0.001 ± 0.0074 |
| thinner_sample <300 | 501 | 0.5501 | 0.3865 | 0.475 | +0.075 | -0.089 | 0.0107 ± 0.0078 |
| thinner_sample >=3000 | 212 | 0.5214 | 0.4205 | 0.4434 | +0.078 | -0.023 | 0.0144 ± 0.008 |
| data_status ADEQUATE | 409 | 0.5285 | 0.4211 | 0.4499 | +0.079 | -0.029 | 0.0074 ± 0.0061 |
| data_status LIMITED | 349 | 0.5597 | 0.4291 | 0.4871 | +0.073 | -0.058 | 0.0011 ± 0.0079 |
| data_status POOR | 762 | 0.5544 | 0.3985 | 0.4777 | +0.077 | -0.079 | 0.0085 ± 0.006 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 224 | 0.1816 | 0.1825 | -0.0009 ± 0.0009 | 0.5374 | 0.5397 | 0.4914 | 0.4771 | 0.5 | -0.093 ± 0.0302 | -0.01 (3) |
| 3-5 | 154 | 0.1814 | 0.1829 | -0.0015 ± 0.0028 | 0.5411 | 0.5421 | 0.5137 | 0.4733 | 0.5065 | -0.072 ± 0.0354 | 0.02 (1) |
| 5-10 | 318 | 0.1986 | 0.2003 | -0.0017 ± 0.0037 | 0.5832 | 0.5861 | 0.5209 | 0.447 | 0.4874 | -0.094 ± 0.0261 | -0.0167 (3) |
| 10-15 | 262 | 0.2195 | 0.2184 | +0.0011 ± 0.0073 | 0.627 | 0.6206 | 0.5272 | 0.4027 | 0.458 | -0.086 ± 0.0288 | -0.0633 (3) |
| 15-25 | 329 | 0.2175 | 0.2109 | +0.0066 ± 0.0099 | 0.6242 | 0.6092 | 0.5691 | 0.3733 | 0.4529 | -0.071 ± 0.0253 | -0.02 (4) |
| 25-40 | 189 | 0.2089 | 0.197 | +0.0119 ± 0.0191 | 0.6043 | 0.5672 | 0.6415 | 0.3307 | 0.4656 | -0.054 ± 0.028 | -0.01 (1) |
| 40+ | 44 | 0.2973 | 0.1575 | +0.1398 ± 0.0536 | 0.8013 | 0.485 | 0.7395 | 0.2936 | 0.3636 | -0.138 ± 0.0535 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 975 | 0.1642 | 0.1649 | -0.0007 ± 0.0004 | 0.4945 | 0.4953 | 0.4862 | 0.4715 | 0.5128 | -0.030 ± 0.0132 | -0.0188 (8) |
| 3-5 | 686 | 0.1839 | 0.1815 | +0.0024 ± 0.0013 | 0.5456 | 0.5357 | 0.4753 | 0.4355 | 0.4213 | -0.083 ± 0.0167 | 0.02 (1) |
| 5-10 | 1448 | 0.186 | 0.185 | +0.0010 ± 0.0017 | 0.553 | 0.5483 | 0.4836 | 0.4101 | 0.4378 | -0.050 ± 0.0114 | -0.0129 (7) |
| 10-15 | 1267 | 0.1946 | 0.1838 | +0.0108 ± 0.003 | 0.5728 | 0.5383 | 0.4749 | 0.35 | 0.3686 | -0.060 ± 0.012 | -0.0633 (3) |
| 15-25 | 1605 | 0.1992 | 0.1662 | +0.0330 ± 0.004 | 0.5876 | 0.4929 | 0.4895 | 0.2925 | 0.3072 | -0.065 ± 0.0102 | -0.017 (10) |
| 25-40 | 1478 | 0.2127 | 0.1204 | +0.0923 ± 0.0056 | 0.617 | 0.3737 | 0.5226 | 0.2092 | 0.2212 | -0.057 ± 0.0086 | -0.01 (1) |
| 40+ | 1021 | 0.3664 | 0.0425 | +0.3239 ± 0.0071 | 0.9545 | 0.1719 | 0.6183 | 0.104 | 0.0558 | -0.083 ± 0.006 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 168 | 0.1878 | 0.1875 | +0.0002 ± 0.0012 | 0.5548 | 0.5545 | 0.4909 | 0.4761 | 0.4583 | -0.134 ± 0.0356 | -0.01 (1) |
| 3-5 | 113 | 0.2036 | 0.2034 | +0.0002 ± 0.0034 | 0.5858 | 0.5893 | 0.4963 | 0.4565 | 0.469 | -0.082 ± 0.0459 | 0.02 (1) |
| 5-10 | 270 | 0.1905 | 0.19 | +0.0005 ± 0.004 | 0.5626 | 0.5605 | 0.5669 | 0.4914 | 0.5185 | -0.090 ± 0.0274 | -0.01 (4) |
| 10-15 | 261 | 0.2263 | 0.2128 | +0.0135 ± 0.0072 | 0.6413 | 0.6138 | 0.586 | 0.4617 | 0.4751 | -0.128 ± 0.03 | -0.0667 (3) |
| 15-25 | 368 | 0.22 | 0.2055 | +0.0144 ± 0.0094 | 0.6263 | 0.5915 | 0.5966 | 0.399 | 0.4674 | -0.088 ± 0.0242 | -0.0167 (3) |
| 25-40 | 243 | 0.2584 | 0.1985 | +0.0600 ± 0.0178 | 0.7203 | 0.5764 | 0.6627 | 0.3518 | 0.4115 | -0.127 ± 0.0289 | -0.025 (2) |
| 40+ | 97 | 0.3414 | 0.1863 | +0.1551 ± 0.0432 | 0.9493 | 0.5471 | 0.7554 | 0.2698 | 0.3711 | -0.052 ± 0.0405 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 858 | 0.1683 | 0.1687 | -0.0004 ± 0.0005 | 0.5052 | 0.507 | 0.5023 | 0.4881 | 0.4988 | -0.057 ± 0.0149 | -0.0217 (6) |
| 3-5 | 568 | 0.1799 | 0.1766 | +0.0033 ± 0.0014 | 0.5289 | 0.5229 | 0.5068 | 0.467 | 0.4454 | -0.077 ± 0.018 | 0.02 (1) |
| 5-10 | 1267 | 0.1777 | 0.1759 | +0.0018 ± 0.0018 | 0.5309 | 0.5234 | 0.5065 | 0.4319 | 0.4554 | -0.049 ± 0.0121 | -0.01 (5) |
| 10-15 | 1153 | 0.1935 | 0.1786 | +0.0149 ± 0.0031 | 0.5737 | 0.527 | 0.5244 | 0.4004 | 0.4059 | -0.077 ± 0.0128 | -0.0575 (4) |
| 15-25 | 1690 | 0.2072 | 0.1723 | +0.0348 ± 0.004 | 0.605 | 0.5088 | 0.5286 | 0.3336 | 0.345 | -0.073 ± 0.0102 | -0.0143 (7) |
| 25-40 | 1615 | 0.2423 | 0.1343 | +0.1080 ± 0.0058 | 0.6883 | 0.4104 | 0.557 | 0.2401 | 0.2297 | -0.085 ± 0.0092 | -0.015 (6) |
| 40+ | 1329 | 0.3967 | 0.0695 | +0.3272 ± 0.0083 | 1.0364 | 0.2424 | 0.6655 | 0.1274 | 0.1053 | -0.063 ± 0.0069 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 232 | 0.1874 | 0.1896 | -0.0023 ± 0.001 | 0.5519 | 0.5584 | 0.5093 | 0.4943 | 0.5474 | -0.044 ± 0.0287 | -0.01 (5) |
| 3-5 | 161 | 0.1806 | 0.1787 | +0.0019 ± 0.0026 | 0.5355 | 0.5313 | 0.504 | 0.4648 | 0.4596 | -0.136 ± 0.0357 | -- (0) |
| 5-10 | 320 | 0.1966 | 0.1966 | -0.0000 ± 0.0037 | 0.5793 | 0.5756 | 0.5159 | 0.4424 | 0.475 | -0.093 ± 0.0254 | -0.01 (3) |
| 10-15 | 250 | 0.2156 | 0.2182 | -0.0027 ± 0.0073 | 0.6209 | 0.6217 | 0.542 | 0.4189 | 0.492 | -0.075 ± 0.0293 | -0.044 (5) |
| 15-25 | 326 | 0.2202 | 0.2084 | +0.0117 ± 0.0099 | 0.6357 | 0.6014 | 0.5784 | 0.3847 | 0.4509 | -0.085 ± 0.0252 | -0.03 (1) |
| 25-40 | 193 | 0.2012 | 0.2021 | -0.0009 ± 0.019 | 0.5858 | 0.5816 | 0.6474 | 0.3344 | 0.487 | -0.045 ± 0.0274 | 0.0 (1) |
| 40+ | 38 | 0.3279 | 0.1536 | +0.1743 ± 0.0579 | 0.8704 | 0.4756 | 0.728 | 0.2758 | 0.3158 | -0.154 ± 0.0605 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 961 | 0.1683 | 0.1693 | -0.0011 ± 0.0005 | 0.505 | 0.5072 | 0.486 | 0.471 | 0.5078 | -0.031 ± 0.0133 | -0.0162 (13) |
| 3-5 | 688 | 0.1859 | 0.1814 | +0.0044 ± 0.0013 | 0.5482 | 0.5396 | 0.4801 | 0.4407 | 0.4041 | -0.114 ± 0.0169 | -0.01 (2) |
| 5-10 | 1512 | 0.1842 | 0.1803 | +0.0039 ± 0.0016 | 0.5503 | 0.5346 | 0.4819 | 0.4082 | 0.4173 | -0.064 ± 0.0109 | -0.01 (3) |
| 10-15 | 1194 | 0.1902 | 0.1819 | +0.0083 ± 0.0031 | 0.5619 | 0.5314 | 0.4865 | 0.3634 | 0.3894 | -0.056 ± 0.0122 | -0.03 (9) |
| 15-25 | 1740 | 0.2002 | 0.1653 | +0.0349 ± 0.0039 | 0.5932 | 0.4926 | 0.4923 | 0.295 | 0.3075 | -0.062 ± 0.0098 | -0.03 (2) |
| 25-40 | 1416 | 0.2132 | 0.1165 | +0.0968 ± 0.0057 | 0.6174 | 0.3624 | 0.5207 | 0.2026 | 0.2126 | -0.063 ± 0.0085 | 0.0 (1) |
| 40+ | 969 | 0.3807 | 0.0436 | +0.3370 ± 0.0077 | 0.9961 | 0.1753 | 0.6248 | 0.1034 | 0.0526 | -0.084 ± 0.0064 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 509 | 0.1997 | 0.1999 | -0.0003 ± 0.0007 | 0.5799 | 0.5809 | 0.4991 | 0.4843 | 0.4931 | -0.041 ± 0.0198 | -0.0226 (46) |
| 3-5 | 382 | 0.197 | 0.1968 | +0.0002 ± 0.0018 | 0.5766 | 0.5744 | 0.479 | 0.4394 | 0.4607 | -0.035 ± 0.0225 | -0.0059 (32) |
| 5-10 | 792 | 0.1883 | 0.183 | +0.0053 ± 0.0023 | 0.5597 | 0.5464 | 0.4685 | 0.3948 | 0.3965 | -0.057 ± 0.0155 | -0.005 (72) |
| 10-15 | 516 | 0.2001 | 0.1905 | +0.0096 ± 0.0048 | 0.5882 | 0.5613 | 0.4708 | 0.3478 | 0.3702 | -0.040 ± 0.0191 | 0.0016 (63) |
| 15-25 | 695 | 0.2365 | 0.2126 | +0.0238 ± 0.0068 | 0.6693 | 0.611 | 0.5353 | 0.3421 | 0.3784 | -0.043 ± 0.0176 | -0.0216 (58) |
| 25-40 | 382 | 0.2474 | 0.1766 | +0.0708 ± 0.0134 | 0.6938 | 0.5243 | 0.6043 | 0.2912 | 0.3325 | -0.067 ± 0.0202 | -0.0216 (25) |
| 40+ | 125 | 0.3566 | 0.1728 | +0.1838 ± 0.0386 | 1.0025 | 0.5201 | 0.7536 | 0.2578 | 0.344 | -0.038 ± 0.0344 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1301 | 0.1865 | 0.1865 | -0.0000 ± 0.0004 | 0.5466 | 0.5464 | 0.4952 | 0.48 | 0.4873 | -0.041 ± 0.0119 | -0.0155 (82) |
| 3-5 | 910 | 0.1898 | 0.1885 | +0.0013 ± 0.0012 | 0.5575 | 0.5541 | 0.4882 | 0.4486 | 0.4549 | -0.044 ± 0.0144 | -0.018 (54) |
| 5-10 | 1910 | 0.1814 | 0.1752 | +0.0062 ± 0.0015 | 0.5425 | 0.5253 | 0.4662 | 0.3919 | 0.3895 | -0.058 ± 0.0097 | -0.0089 (122) |
| 10-15 | 1376 | 0.1957 | 0.1827 | +0.0130 ± 0.0029 | 0.5783 | 0.5419 | 0.48 | 0.3569 | 0.3656 | -0.052 ± 0.0114 | -0.0053 (99) |
| 15-25 | 1804 | 0.2261 | 0.1971 | +0.0290 ± 0.0041 | 0.6512 | 0.5719 | 0.5262 | 0.3311 | 0.3542 | -0.049 ± 0.0106 | -0.0255 (106) |
| 25-40 | 1308 | 0.2375 | 0.1499 | +0.0876 ± 0.0068 | 0.6725 | 0.453 | 0.5696 | 0.2542 | 0.2745 | -0.062 ± 0.0104 | -0.0206 (47) |
| 40+ | 642 | 0.3594 | 0.0945 | +0.2648 ± 0.0131 | 0.9777 | 0.3077 | 0.6629 | 0.1567 | 0.1589 | -0.061 ± 0.0115 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 1520 | 1.164 ± 0.076 | 1.247 | 0.1676 | 0.1683 | 0.2062 | 0.1997 |
| gen2 | 1520 | 0.942 ± 0.067 | 1.165 | 0.184 | 0.1678 | 0.2249 | 0.1995 |
| gen1_elo | 1520 | 1.139 ± 0.075 | 1.228 | 0.1722 | 0.1685 | 0.2055 | 0.1994 |
| gen1_sr | 1520 | 1.174 ± 0.087 | 1.247 | 0.1416 | 0.17 | 0.2208 | 0.1995 |
| gen1_ledger | 3401 | 0.947 ± 0.046 | 1.1 | 0.1663 | 0.1942 | 0.2154 | 0.1932 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 9,280)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,526 | 27.2% |
| STALE_QUOTE | market_freshness | 2,161 | 23.3% |
| BOOK_QUALITY | execution | 1,645 | 17.7% |
| POOR_DATA | data | 995 | 10.7% |
| LIMITED_DATA | data | 611 | 6.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 440 | 4.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 437 | 4.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 237 | 2.5% |
| IDENTITY_AMBIGUOUS | mapping | 217 | 2.3% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 11 | 0.1% |

Cause class: coverage 27.2%, market_freshness 23.3%, execution 17.7%, data 17.3%, market_freshness/coverage 7.3%, model_calibration_or_unknown 4.7%, mapping 2.3%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.7%, START_UNVERIFIABLE 96.0%, LOW_DATA_QUALITY 69.1%, THIN_PLAYER_HISTORY 58.7%, STALE_PLAYER_DATA 58.7%, STALE_KALSHI_QUOTE 50.5%, MODEL_INTERNAL_DISAGREEMENT 37.4%, ASYMMETRIC_SAMPLE_SIZE 31.9%, WIDE_SPREAD 24.3%, MODEL_HIGH_UNCERTAINTY 15.4%, PLAYER_IDENTITY_RISK 10.7%, LEVEL_TRANSFER_RISK 8.5%, LOW_DISPLAYED_LIQUIDITY 7.2%, EVENT_MAPPING_RISK 7.1%, MODEL_CALIBRATION_OUTLIER 2.8%, UNKNOWN 0.5%, EXTERNAL_MARKET_REJECTION 0.3%, EXTERNAL_MARKET_CONFIRMATION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 29.3%, POST_SETTLEMENT_OBSERVATION 27.2%, POSSIBLE_IN_PLAY_QUOTE 5.2%, CONFIRMED_IN_PLAY_QUOTE 0.7%

### >= ge_25 pp (N = 5,067)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,987 | 39.2% |
| STALE_QUOTE | market_freshness | 971 | 19.2% |
| BOOK_QUALITY | execution | 853 | 16.8% |
| POOR_DATA | data | 434 | 8.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 243 | 4.8% |
| LIMITED_DATA | data | 190 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 146 | 2.9% |
| IDENTITY_AMBIGUOUS | mapping | 125 | 2.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 115 | 2.3% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 3 | 0.1% |

Cause class: coverage 39.2%, market_freshness 19.2%, execution 16.8%, data 12.3%, market_freshness/coverage 7.7%, mapping 2.5%, model_calibration_or_unknown 2.3%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 98.0%, LOW_DATA_QUALITY 71.5%, THIN_PLAYER_HISTORY 60.6%, STALE_KALSHI_QUOTE 57.8%, STALE_PLAYER_DATA 54.6%, MODEL_INTERNAL_DISAGREEMENT 39.6%, ASYMMETRIC_SAMPLE_SIZE 34.2%, WIDE_SPREAD 23.3%, MODEL_HIGH_UNCERTAINTY 16.7%, PLAYER_IDENTITY_RISK 13.2%, EVENT_MAPPING_RISK 8.0%, LOW_DISPLAYED_LIQUIDITY 7.6%, LEVEL_TRANSFER_RISK 7.5%, MODEL_CALIBRATION_OUTLIER 3.5%, EXTERNAL_MARKET_REJECTION 0.1%, UNKNOWN 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 41.5%, POST_SETTLEMENT_OBSERVATION 39.2%, POSSIBLE_IN_PLAY_QUOTE 5.3%, CONFIRMED_IN_PLAY_QUOTE 0.8%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 4246, "IDENTITY_AMBIGUOUS": 821}; ticker orientation: {"VERIFIED": 5067}.

Checks: discipline:AMBIGUOUS 250, discipline:PASS 4817, identity_confidence:AMBIGUOUS 670, identity_confidence:PASS 4397, level_mapping:NA 262, level_mapping:PASS 4805, market_pair:AMBIGUOUS 189, market_pair:NA 121, market_pair:PASS 4757, model_complement:NA 89, model_complement:PASS 4978, namesake:PASS 5067, physical_match_id:NA 2145, physical_match_id:PASS 2922, player_ids:PASS 5067, same_pair_other_event:PASS 5067, ticker_orientation:PASS 5067

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,222 | 1.9% | 1.9% | 0.4% | {"market_freshness": 20, "execution": 3} | 5.62 | 0.1873 / 0.1865 (97) | 22.8% | 0.2% | 6.1% | 1.6% |
| CHALLENGER | 3,431 | 19.1% | 6.8% | 13.0% | {"coverage": 404, "market_freshness": 107, "market_freshness/coverage": 73, "model_calibration_or_unknown": 43, "data": 25, "execution": 4} | 6.94 | 0.2207 / 0.2036 (794) | 48.1% | 5.2% | 1.5% | 23.5% |
| DOUBLES | 566 | 44.2% | 43.5% | 4.9% | {"market_freshness": 106, "execution": 73, "mapping": 45, "market_freshness/coverage": 19, "coverage": 7} | 22.7 | 0.3112 / 0.2239 (178) | 41.3% | 0.0% | 100.0% | 9.0% |
| ITF_MEN | 6,687 | 25.0% | 17.4% | 33.0% | {"coverage": 660, "execution": 373, "market_freshness": 262, "data": 242, "market_freshness/coverage": 114, "mapping": 19, "model_calibration_or_unknown": 1} | 11.13 | 0.2121 / 0.1911 (1647) | 41.0% | 56.3% | 6.5% | 23.0% |
| ITF_WOMEN | 8,498 | 26.6% | 18.6% | 44.6% | {"coverage": 899, "market_freshness": 419, "execution": 383, "data": 333, "market_freshness/coverage": 142, "mapping": 55, "model_calibration_or_unknown": 25, "model_calibration": 2} | 12.34 | 0.2013 / 0.191 (1763) | 42.3% | 60.0% | 10.7% | 23.0% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 949 | 8.3% | 7.2% | 1.6% | {"market_freshness": 34, "model_calibration_or_unknown": 16, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.36 | 0.2051 / 0.202 (141) | 35.1% | 2.2% | 1.3% | 3.4% |
| WTA125 | 760 | 15.5% | 11.3% | 2.3% | {"market_freshness/coverage": 31, "model_calibration_or_unknown": 28, "market_freshness": 21, "data": 13, "coverage": 12, "execution": 8, "mapping": 4, "model_calibration": 1} | 10.04 | 0.2251 / 0.2113 (259) | 28.0% | 5.7% | 4.0% | 12.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 3 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 4 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 5 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 6 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 7 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 8 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 9 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 12 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 14 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POOR_DATA | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 15 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 765 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 16 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 17 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 18 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 19 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 20 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 21 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 22 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 23 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 24 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 64 min (STALE); no external reference |
| 25 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 26 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 27 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 110 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 28 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 29 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 30 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 799 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 31 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 32 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 33 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 34 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 35 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 36 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.2h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 141 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 37 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 38 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 39 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 708 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 40 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 41 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 42 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 43 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 44 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.9h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 671 min (STALE); no external reference |
| 46 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 183 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 47 | `KXWTAMATCH-26OCT01YASCHW-CHW` | WTA | fair_v1 | 73% / 2% | +70 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 51 min (STALE); no external reference |
| 48 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 49 | `KXATPCHALLENGERMATCH-26OCT05CASMUN-CAS` | CHALLENGER | fair_v1 | 83% / 14% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 192 min (STALE); data POOR (grade D, thinner serve sample 814.0, ratio 3.76); no external reference |
| 50 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9799, "by_level_share_of_ge_25pp": {"ATP": 0.0045, "CHALLENGER": 0.1295, "DOUBLES": 0.0493, "ITF_MEN": 0.3298, "ITF_WOMEN": 0.4456, "OTHER": 0.0024, "WTA": 0.0156, "WTA125": 0.0233}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5779, "share_primary_cause_market_settled_or_in_play": 0.4689, "share_primary_cause_stale_quote_only": 0.1916}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 5067, "identity_ambiguous_share": 0.162, "ticker_orientation": {"VERIFIED": 5067}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 2922, "with_external": 34, "coverage": 0.0116, "external_status": {"EXTERNAL_STALE": 29, "AGREES_WITH_KALSHI": 5}, "triangulation": {"INSUFFICIENT_INPUTS": 29, "MODEL_LONE_OUTLIER": 5}, "share_external_agrees_with_kalshi": 0.1471, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 1361, "with_external": 34, "coverage": 0.025, "external_status": {"EXTERNAL_STALE": 29, "AGREES_WITH_KALSHI": 5}, "triangulation": {"INSUFFICIENT_INPUTS": 29, "MODEL_LONE_OUTLIER": 5}, "share_external_agrees_with_kalshi": 0.1471, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 601.0, "median_sample_ratio": 2.38, "median_min_matches": 19.0, "median_max_days_since_last": 197.0, "share_severe_asymmetry": 0.1861, "data_status": {"POOR": 2714, "LIMITED": 1439, "ADEQUATE": 914}, "comparison_lt_10pp": {"median_thinner_serve_points": 1723.0, "median_sample_ratio": 1.77, "median_min_matches": 72.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 333, "model_minus_observed": 0.0728, "kalshi_minus_observed": -0.0604, "brier_diff_model_minus_kalshi": 0.0022}, "4-10x": {"n": 252, "model_minus_observed": 0.0508, "kalshi_minus_observed": -0.0884, "brier_diff_model_minus_kalshi": -0.0048}, "<2x": {"n": 702, "model_minus_observed": 0.0776, "kalshi_minus_observed": -0.0478, "brier_diff_model_minus_kalshi": 0.0098}, ">=10x": {"n": 233, "model_minus_observed": 0.1048, "kalshi_minus_observed": -0.0703, "brier_diff_model_minus_kalshi": 0.0151}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 1520, "model": {"intercept": -0.598, "slope": 0.942, "slope_se": 0.067}, "kalshi_mid_same_rows": {"intercept": 0.239, "slope": 1.165, "slope_se": 0.075}, "mean_extremity_model": 0.184, "mean_extremity_kalshi": 0.1678, "model_brier": 0.2249, "kalshi_brier": 0.1995, "brier_diff_model_minus_kalshi": 0.0254, "brier_diff_se": 0.0049, "model_logloss": 0.6423, "kalshi_logloss": 0.5803}, "fair_v1": {"n": 1520, "model": {"intercept": -0.402, "slope": 1.164, "slope_se": 0.076}, "kalshi_mid_same_rows": {"intercept": 0.383, "slope": 1.247, "slope_se": 0.078}, "mean_extremity_model": 0.1676, "mean_extremity_kalshi": 0.1683, "model_brier": 0.2062, "kalshi_brier": 0.1997, "brier_diff_model_minus_kalshi": 0.0065, "brier_diff_se": 0.0039, "model_logloss": 0.5975, "kalshi_logloss": 0.5805}, "gen1_elo": {"n": 1520, "model": {"intercept": -0.387, "slope": 1.139, "slope_se": 0.075}, "kalshi_mid_same_rows": {"intercept": 0.374, "slope": 1.228, "slope_se": 0.077}, "mean_extremity_model": 0.1722, "mean_extremity_kalshi": 0.1685, "model_brier": 0.2055, "kalshi_brier": 0.1994, "brier_diff_model_minus_kalshi": 0.0062, "brier_diff_se": 0.0039, "model_logloss": 0.5975, "kalshi_logloss": 0.5797}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2525, "share_ge_15": 0.439, "median_abs_gap": 13.05, "n": 11570}, "gen1_elo": {"share_ge_25": 0.2421, "share_ge_15": 0.4371, "median_abs_gap": 12.63, "n": 11570}, "gen1_sr": {"share_ge_25": 0.3029, "share_ge_15": 0.5211, "median_abs_gap": 15.76, "n": 11570}, "gen2": {"share_ge_25": 0.308, "share_ge_15": 0.5073, "median_abs_gap": 15.38, "n": 11570}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1533, "share_ge_15": 0.3453, "median_abs_gap": 10.6, "n": 8878}, "gen1_elo": {"share_ge_25": 0.1465, "share_ge_15": 0.3412, "median_abs_gap": 10.16, "n": 8878}, "gen1_sr": {"share_ge_25": 0.2039, "share_ge_15": 0.4369, "median_abs_gap": 13.01, "n": 8878}, "gen2": {"share_ge_25": 0.2237, "share_ge_15": 0.4332, "median_abs_gap": 12.79, "n": 8878}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.62, "share_ge_25_all": 0.0188, "share_ge_25_pregame_clean": 0.0191}, "WTA": {"median_abs_gap_pregame_clean": 8.36, "share_ge_25_all": 0.0832, "share_ge_25_pregame_clean": 0.072}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2313, "share_within_10pp_all": 0.4294, "share_within_10pp_pregame_clean": 0.4915, "corr_model_vs_mid_pregame_clean": 0.8457}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 224, "model_brier": 0.1816, "kalshi_brier": 0.1825, "brier_diff_model_minus_kalshi": -0.0009}, "10-15": {"n_settled": 262, "model_brier": 0.2195, "kalshi_brier": 0.2184, "brier_diff_model_minus_kalshi": 0.0011}, "15-25": {"n_settled": 329, "model_brier": 0.2175, "kalshi_brier": 0.2109, "brier_diff_model_minus_kalshi": 0.0066}, "25-40": {"n_settled": 189, "model_brier": 0.2089, "kalshi_brier": 0.197, "brier_diff_model_minus_kalshi": 0.0119}, "3-5": {"n_settled": 154, "model_brier": 0.1814, "kalshi_brier": 0.1829, "brier_diff_model_minus_kalshi": -0.0015}, "40+": {"n_settled": 44, "model_brier": 0.2973, "kalshi_brier": 0.1575, "brier_diff_model_minus_kalshi": 0.1398}, "5-10": {"n_settled": 318, "model_brier": 0.1986, "kalshi_brier": 0.2003, "brier_diff_model_minus_kalshi": -0.0017}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%)
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap).
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 178, "model_brier": 0.3112, "kalshi_brier": 0.2239, "brier_diff_model_minus_kalshi": 0.0874, "brier_diff_se": 0.0239, "corr_model_outcome": -0.0196, "corr_kalshi_outcome": 0.3602}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
