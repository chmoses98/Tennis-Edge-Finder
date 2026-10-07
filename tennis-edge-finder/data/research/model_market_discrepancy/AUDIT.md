# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-07T06:55Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 21,832): 0-3 13.6%, 3-5 9.6%, 5-10 19.9%, 10-15 15.4%, 15-25 18.9%, 25-40 14.2%, 40+ 8.4%; median gap 12.12 pp.
* **Where the extremes live**: 97.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.4%, Challenger 13.1%, doubles 4.8%). Main tour: ATP 1.9% and WTA 8.4% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 4,947): MARKET_ALREADY_SETTLED_WHEN_PRICED 39.6%, STALE_QUOTE 19.4%, BOOK_QUALITY 16.8%, POOR_DATA 8.5%, POSSIBLY_IN_PLAY_QUOTE 4.5%, LIMITED_DATA 3.7%, IN_PLAY_QUOTE 2.8%, IDENTITY_AMBIGUOUS 2.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.1%. By class: coverage 39.6%, market_freshness 19.4%, execution 16.8%, data 12.2%, market_freshness/coverage 7.3%, mapping 2.5%, model_calibration_or_unknown 2.2%, model_calibration 0.1%.
* **Stale / settled / in-play**: 58.4% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 46.9% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 4,947 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 16.3% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 1.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 8.1% of the time and with the model 0.2%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 596.0 points vs 1733.5 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.149, Gen-2 0.935, Gen-1 ledger 0.934 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 175 model 0.2106 vs Kalshi 0.1996; n 39 model 0.3105 vs Kalshi 0.1436.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%). Not implemented here.

## 1. Observations

* 81,114 model-market comparisons (136,343 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 31,536 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-07T06:48:31.278345+00:00'], shadow board 22,522 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-07T06:48:35.091960+00:00'], Model 4 8,035 rows, 9,601 settled tickers, 2,423 tickers with an external scan.
* By model: {"gen1_ledger": 20029, "gen1_elo": 11316, "fair_v1": 11316, "gen2": 11316, "gen1_sr": 11316, "model4_fundamental": 7915, "model4_conditioned": 7906}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 21,832 | 13.6 | 9.6 | 19.9 | 15.4 | 18.9 | 14.2 | 8.4 | 12.12 | 41.6% | 22.7% |
| MW fair_v1 | 11,316 | 12.9 | 8.9 | 18.4 | 16.0 | 18.7 | 15.1 | 10.0 | 13.02 | 43.8% | 25.1% |
| MW gen1_elo | 11,316 | 12.8 | 9.0 | 19.7 | 15.0 | 19.4 | 14.7 | 9.4 | 12.57 | 43.5% | 24.1% |
| MW gen1_ledger | 10,516 | 14.3 | 10.3 | 21.4 | 14.7 | 19.2 | 13.3 | 6.7 | 11.18 | 39.2% | 20.0% |
| MW gen1_sr | 11,316 | 9.9 | 7.8 | 16.1 | 14.2 | 21.8 | 18.4 | 11.7 | 15.67 | 52.0% | 30.1% |
| MW gen2 | 11,316 | 11.7 | 7.1 | 16.0 | 14.5 | 19.9 | 17.4 | 13.2 | 15.32 | 50.6% | 30.7% |
| all families model4_conditioned | 7,906 | 21.8 | 20.3 | 34.8 | 16.3 | 5.0 | 0.9 | 0.8 | 5.79 | 6.7% | 1.8% |
| all families model4_fundamental | 7,915 | 16.5 | 13.2 | 34.4 | 20.2 | 11.1 | 3.3 | 1.2 | 7.77 | 15.6% | 4.5% |

Configurable thresholds (primary): >=5pp 76.8%, >=10pp 57.0%, >=15pp 41.6%, >=20pp 31.1%, >=25pp 22.7%, >=30pp 16.6%, >=40pp 8.4%, >=50pp 3.6%
Executable gap (model outside the book, before fees): median 8.52pp; >=10pp 45.7%, >=25pp 18.2%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 791 | 25.8 | 17.1 | 24.5 | 16.9 | 12.8 | 1.5 | 1.4 | 5.93 | 15.7% | 2.9% |
| CHALLENGER | 2,057 | 14.5 | 11.3 | 18.5 | 16.2 | 13.2 | 13.2 | 13.1 | 12.01 | 39.5% | 26.3% |
| ITF_MEN | 3,219 | 10.6 | 8.6 | 18.9 | 14.6 | 19.7 | 15.0 | 12.7 | 13.99 | 47.4% | 27.7% |
| ITF_WOMEN | 4,440 | 10.4 | 6.6 | 16.1 | 16.1 | 21.9 | 19.4 | 9.5 | 15.36 | 50.7% | 28.9% |
| WTA | 516 | 22.9 | 9.7 | 24.6 | 16.5 | 17.8 | 6.4 | 2.1 | 8.36 | 26.4% | 8.5% |
| WTA125 | 293 | 12.6 | 6.8 | 20.5 | 25.3 | 14.3 | 17.8 | 2.7 | 11.47 | 34.8% | 20.5% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 791 | 21.5 | 14.9 | 24.6 | 18.1 | 16.6 | 2.6 | 1.6 | 6.9 | 20.9% | 4.3% |
| CHALLENGER | 2,057 | 14.8 | 7.3 | 17.7 | 13.7 | 18.6 | 14.4 | 13.5 | 13.38 | 46.5% | 27.9% |
| ITF_MEN | 3,219 | 10.2 | 7.2 | 16.6 | 15.0 | 20.1 | 17.6 | 13.3 | 15.43 | 51.0% | 31.0% |
| ITF_WOMEN | 4,440 | 8.8 | 6.2 | 13.1 | 13.3 | 20.9 | 21.3 | 16.4 | 18.62 | 58.6% | 37.7% |
| WTA | 516 | 21.3 | 4.8 | 17.2 | 15.7 | 21.9 | 16.9 | 2.1 | 13.03 | 40.9% | 19.0% |
| WTA125 | 293 | 5.1 | 2.4 | 16.4 | 23.6 | 19.4 | 20.1 | 13.0 | 16.74 | 52.6% | 33.1% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 791 | 25.4 | 11.9 | 29.6 | 17.2 | 10.6 | 3.8 | 1.5 | 6.85 | 15.9% | 5.3% |
| CHALLENGER | 2,057 | 15.8 | 11.1 | 19.8 | 14.2 | 13.8 | 12.3 | 13.0 | 10.76 | 39.1% | 25.3% |
| ITF_MEN | 3,219 | 9.5 | 8.9 | 18.5 | 13.8 | 21.1 | 15.3 | 12.8 | 14.8 | 49.3% | 28.2% |
| ITF_WOMEN | 4,440 | 9.8 | 6.8 | 16.5 | 15.7 | 23.8 | 19.1 | 8.2 | 15.5 | 51.1% | 27.3% |
| WTA | 516 | 23.3 | 13.0 | 34.7 | 14.3 | 9.7 | 3.7 | 1.4 | 7.0 | 14.7% | 5.0% |
| WTA125 | 293 | 21.2 | 11.9 | 27.3 | 18.1 | 15.4 | 5.5 | 0.7 | 7.73 | 21.5% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 409 | 28.1 | 21.3 | 37.6 | 11.7 | 1.2 | 0.0 | 0.0 | 5.11 | 1.2% | 0.0% |
| CHALLENGER | 1,339 | 22.7 | 16.2 | 26.7 | 14.3 | 12.2 | 5.7 | 2.2 | 6.78 | 20.1% | 7.8% |
| DOUBLES | 543 | 4.0 | 3.1 | 13.3 | 11.8 | 23.8 | 21.0 | 23.0 | 22.7 | 67.8% | 44.0% |
| ITF_MEN | 3,336 | 13.5 | 8.4 | 20.0 | 15.3 | 20.6 | 13.4 | 8.7 | 12.27 | 42.8% | 22.1% |
| ITF_WOMEN | 3,851 | 11.3 | 9.3 | 19.1 | 14.0 | 22.5 | 17.6 | 6.2 | 13.48 | 46.4% | 23.9% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 426 | 19.2 | 11.5 | 25.6 | 19.5 | 16.0 | 7.5 | 0.7 | 8.69 | 24.2% | 8.2% |
| WTA125 | 463 | 15.1 | 12.7 | 22.0 | 19.6 | 17.9 | 9.5 | 3.0 | 10.09 | 30.4% | 12.5% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 787 | 25.8 | 16.9 | 24.5 | 17.0 | 12.8 | 1.5 | 1.4 | 5.93 | 15.8% | 2.9% |
| CHALLENGER | 1,468 | 18.8 | 14.4 | 23.8 | 18.8 | 14.1 | 7.1 | 3.1 | 8.45 | 24.2% | 10.2% |
| ITF_MEN | 2,373 | 12.7 | 10.8 | 22.3 | 16.1 | 19.7 | 12.4 | 6.0 | 11.13 | 38.1% | 18.5% |
| ITF_WOMEN | 3,272 | 12.8 | 8.1 | 18.7 | 18.2 | 23.3 | 15.6 | 3.2 | 12.8 | 42.1% | 18.8% |
| WTA | 514 | 23.0 | 9.7 | 24.7 | 16.3 | 17.9 | 6.2 | 2.1 | 8.32 | 26.3% | 8.4% |
| WTA125 | 282 | 13.1 | 7.1 | 20.2 | 25.5 | 14.5 | 17.7 | 1.8 | 11.39 | 34.0% | 19.5% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 787 | 21.4 | 14.9 | 24.8 | 18.0 | 16.6 | 2.7 | 1.6 | 6.9 | 21.0% | 4.3% |
| CHALLENGER | 1,468 | 19.4 | 9.5 | 22.3 | 16.5 | 19.4 | 10.0 | 2.9 | 9.72 | 32.3% | 12.9% |
| ITF_MEN | 2,373 | 12.2 | 8.5 | 19.2 | 16.9 | 21.0 | 15.3 | 6.8 | 12.81 | 43.2% | 22.2% |
| ITF_WOMEN | 3,272 | 10.3 | 7.2 | 14.8 | 14.2 | 22.8 | 20.0 | 10.6 | 16.27 | 53.4% | 30.6% |
| WTA | 514 | 21.4 | 4.9 | 17.3 | 15.8 | 21.8 | 16.7 | 2.1 | 12.98 | 40.7% | 18.9% |
| WTA125 | 282 | 5.3 | 2.5 | 16.7 | 24.5 | 18.4 | 20.9 | 11.7 | 15.82 | 51.1% | 32.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 395 | 28.4 | 21.5 | 38.0 | 11.9 | 0.2 | 0.0 | 0.0 | 5.02 | 0.2% | 0.0% |
| CHALLENGER | 1,125 | 24.8 | 18.4 | 29.2 | 13.9 | 11.6 | 2.1 | 0.1 | 6.16 | 13.8% | 2.2% |
| DOUBLES | 500 | 4.0 | 3.0 | 13.6 | 11.8 | 24.0 | 21.2 | 22.4 | 22.69 | 67.6% | 43.6% |
| ITF_MEN | 2,690 | 15.3 | 9.4 | 22.3 | 16.4 | 20.6 | 11.2 | 5.0 | 10.98 | 36.7% | 16.2% |
| ITF_WOMEN | 3,131 | 12.7 | 10.3 | 21.1 | 14.8 | 22.8 | 15.8 | 2.6 | 11.67 | 41.1% | 18.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 396 | 19.7 | 12.1 | 26.3 | 19.7 | 16.4 | 5.8 | 0.0 | 8.43 | 22.2% | 5.8% |
| WTA125 | 380 | 17.1 | 14.2 | 24.7 | 22.6 | 16.1 | 5.0 | 0.3 | 8.91 | 21.3% | 5.3% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 543 | 4.0 | 3.1 | 13.3 | 11.8 | 23.8 | 21.0 | 23.0 | 22.7 | 67.8% | 44.0% |
| singles | 9,973 | 14.9 | 10.7 | 21.8 | 14.9 | 19.0 | 12.9 | 5.8 | 10.71 | 37.7% | 18.7% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 2,661 | 13.4 | 9.6 | 20.2 | 15.5 | 16.2 | 14.4 | 10.7 | 12.21 | 41.3% | 25.1% |
| Hard | 7,629 | 12.8 | 8.7 | 18.4 | 15.9 | 19.4 | 15.0 | 9.7 | 13.14 | 44.1% | 24.8% |
| UNKNOWN | 1,026 | 12.4 | 8.2 | 13.8 | 18.2 | 19.6 | 17.7 | 10.0 | 14.11 | 47.4% | 27.8% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,278 | 17.9 | 11.3 | 20.4 | 17.0 | 15.0 | 10.1 | 8.2 | 10.04 | 33.3% | 18.4% |
| B | 1,416 | 15.1 | 10.0 | 20.0 | 17.2 | 16.2 | 11.6 | 9.9 | 11.07 | 37.7% | 21.5% |
| C | 1,743 | 12.5 | 9.8 | 21.7 | 15.0 | 18.1 | 14.1 | 8.8 | 12.21 | 41.0% | 22.9% |
| D | 2,125 | 11.7 | 8.9 | 16.2 | 16.2 | 23.1 | 15.3 | 8.6 | 14.08 | 47.1% | 23.9% |
| F | 2,754 | 7.0 | 4.9 | 15.0 | 14.6 | 21.1 | 23.4 | 13.9 | 18.59 | 58.5% | 37.4% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 2,923 | 21.1 | 14.9 | 27.2 | 16.1 | 13.3 | 5.4 | 2.2 | 7.31 | 20.8% | 7.6% |
| B | 1,591 | 14.3 | 9.9 | 24.1 | 15.4 | 18.7 | 12.0 | 5.5 | 10.42 | 36.3% | 17.5% |
| C | 2,039 | 12.0 | 8.1 | 19.5 | 14.9 | 21.2 | 14.5 | 9.8 | 13.16 | 45.6% | 24.3% |
| D | 1,787 | 12.8 | 8.9 | 21.0 | 13.3 | 22.3 | 15.2 | 6.5 | 12.64 | 44.0% | 21.7% |
| F | 2,176 | 8.8 | 7.7 | 13.7 | 13.4 | 23.2 | 22.2 | 10.9 | 17.37 | 56.4% | 33.1% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 3,737 | 17.0 | 10.5 | 19.7 | 17.3 | 15.2 | 10.4 | 9.9 | 10.77 | 35.5% | 20.3% |
| LIMITED | 2,664 | 14.3 | 10.7 | 22.1 | 15.4 | 17.2 | 13.1 | 7.2 | 10.91 | 37.5% | 20.3% |
| POOR | 4,915 | 9.1 | 6.7 | 15.5 | 15.3 | 22.1 | 19.8 | 11.6 | 16.37 | 53.4% | 31.4% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,713 | 29.7 | 26.3 | 36.7 | 5.4 | 1.7 | 0.2 | 0.0 | 4.46 | 1.9% | 0.2% |
| GAME_SPREAD | 1,770 | 23.8 | 15.4 | 37.0 | 18.8 | 4.6 | 0.3 | 0.2 | 6.2 | 5.1% | 0.4% |
| MATCH_WINNER | 10,516 | 14.3 | 10.3 | 21.4 | 14.7 | 19.2 | 13.3 | 6.7 | 11.18 | 39.2% | 20.0% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 3,326 | 29.1 | 18.7 | 31.5 | 11.4 | 7.5 | 1.4 | 0.3 | 5.25 | 9.2% | 1.7% |
| TOTAL_GAMES | 2,680 | 7.8 | 9.4 | 37.6 | 29.3 | 10.2 | 3.4 | 2.4 | 9.45 | 15.9% | 5.8% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,892 | 24.8 | 39.2 | 28.7 | 0.3 | 6.2 | 0.6 | 0.2 | 4.33 | 7.0% | 0.8% |
| GAME_SPREAD | 1,988 | 45.3 | 14.3 | 29.7 | 8.8 | 1.1 | 0.6 | 0.2 | 3.59 | 1.9% | 0.8% |
| TOTAL_GAMES | 3,026 | 3.6 | 6.2 | 43.8 | 36.6 | 6.3 | 1.5 | 1.9 | 9.72 | 9.7% | 3.4% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,892 | 25.5 | 18.3 | 35.4 | 9.7 | 7.4 | 3.2 | 0.5 | 5.6 | 11.1% | 3.7% |
| GAME_SPREAD | 1,988 | 19.5 | 13.4 | 26.6 | 22.7 | 13.9 | 3.1 | 0.8 | 8.3 | 17.8% | 3.9% |
| TOTAL_GAMES | 3,035 | 6.0 | 8.3 | 38.5 | 28.7 | 12.8 | 3.4 | 2.3 | 9.68 | 18.5% | 5.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 11,316 | 43.8% | 25.1% | 13.02 | 34.4% | 15.2% | 10.57 |
| gen1_elo | 11,316 | 43.5% | 24.1% | 12.57 | 34.0% | 14.6% | 10.14 |
| gen1_sr | 11,316 | 52.0% | 30.1% | 15.67 | 43.6% | 20.3% | 12.98 |
| gen2 | 11,316 | 50.6% | 30.7% | 15.32 | 43.3% | 22.3% | 12.78 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 5,389 | 15.5 | 11.5 | 21.8 | 17.1 | 18.7 | 11.8 | 3.6 | 10.3 | 34.1% | 15.3% |
| STALE | 5,927 | 10.5 | 6.5 | 15.4 | 15.0 | 18.6 | 18.2 | 15.8 | 16.44 | 52.6% | 34.0% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 3,984 | 16.3 | 11.6 | 24.1 | 14.6 | 17.2 | 12.0 | 4.2 | 9.46 | 33.4% | 16.1% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 21,832 | 3984 | 8861 | 8987 | 25.9 | 169.4 | 1400.4 |
| ge_15pp | 9,081 | 1329 | 3125 | 4627 | 30.7 | 451.6 | 1380.4 |
| ge_25pp | 4,947 | 643 | 1417 | 2887 | 40.0 | 560.8 | 1380.4 |
| lt_10pp | 9,395 | 2073 | 4262 | 3060 | 24.4 | 52.9 | 1201.9 |

Current slate `SL-20261007T065506Z-47164471`: 1003 priced rows, quote age at build {'median': 7.1, 'max': 7.1}, freshness {'FRESH': 1003}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 1 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 20.71 | 100.0% | 0.0% |
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 362 | 21.0 | 12.2 | 22.6 | 21.0 | 16.3 | 6.3 | 0.6 | 7.99 | 23.2% | 6.9% |
| MARKETS_AGREE | 24 | 70.8 | 29.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.18 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 34 | 0.0 | 0.0 | 29.4 | 38.2 | 23.5 | 8.8 | 0.0 | 12.79 | 32.4% | 8.8% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 11,316 | 422 (3.7%) | 8.1% | 0.2% | {"EXTERNAL_STALE": 362, "AGREES_WITH_KALSHI": 34, "ALL_AGREE": 24, "SUPPORTS_MODEL_DIRECTION": 1, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 4,953 | 96 (1.9%) | 11.5% | 1.0% | {"EXTERNAL_STALE": 84, "AGREES_WITH_KALSHI": 11, "SUPPORTS_MODEL_DIRECTION": 1} |
| fair_v1_ge_25pp | 2,842 | 28 (1.0%) | 10.7% | 0.0% | {"EXTERNAL_STALE": 25, "AGREES_WITH_KALSHI": 3} |
| fair_v1_ge_25pp_pregame_clean | 1,323 | 28 (2.1%) | 10.7% | 0.0% | {"EXTERNAL_STALE": 25, "AGREES_WITH_KALSHI": 3} |
| fair_v1_lt_10pp | 4,553 | 237 (5.2%) | 4.2% | 0.0% | {"EXTERNAL_STALE": 202, "ALL_AGREE": 24, "AGREES_WITH_KALSHI": 10, "EXTERNAL_OUTLIER": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 2,252 | 11.1 | 8.6 | 20.9 | 15.4 | 21.1 | 13.8 | 9.2 | 12.71 | 44.0% | 23.0% |
| 4-10x | 1,675 | 11.2 | 9.6 | 18.1 | 14.6 | 21.0 | 17.0 | 8.5 | 13.76 | 46.5% | 25.5% |
| <2x | 5,921 | 14.7 | 9.5 | 18.5 | 16.9 | 17.0 | 13.5 | 9.9 | 12.17 | 40.4% | 23.4% |
| >=10x | 1,468 | 10.2 | 5.9 | 15.1 | 14.8 | 18.9 | 21.5 | 13.5 | 16.82 | 53.9% | 35.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 2,848 | 13.8 | 8.5 | 20.9 | 15.9 | 17.2 | 12.8 | 10.9 | 12.04 | 41.0% | 23.7% |
| 300-1000 | 2,721 | 12.3 | 9.5 | 16.7 | 15.9 | 22.1 | 15.6 | 7.9 | 13.66 | 45.6% | 23.5% |
| <300 | 3,207 | 8.0 | 6.0 | 15.3 | 14.8 | 20.9 | 21.7 | 13.3 | 17.55 | 55.9% | 35.0% |
| >=3000 | 2,540 | 18.8 | 12.2 | 21.5 | 17.8 | 13.8 | 8.9 | 7.0 | 9.45 | 29.7% | 15.9% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 318 | 0.5363 | 0.4034 | 0.4591 | +0.077 | -0.056 | 0.002 ± 0.0079 |
| ratio 4-10x | 231 | 0.589 | 0.4503 | 0.5368 | +0.052 | -0.086 | 0.0007 ± 0.0099 |
| ratio <2x | 660 | 0.5389 | 0.4143 | 0.4591 | +0.080 | -0.045 | 0.0109 ± 0.0056 |
| ratio >=10x | 214 | 0.5574 | 0.3842 | 0.4579 | +0.100 | -0.074 | 0.012 ± 0.0126 |
| thinner_sample 1000-3000 | 369 | 0.542 | 0.4204 | 0.4634 | +0.079 | -0.043 | 0.0042 ± 0.0073 |
| thinner_sample 300-1000 | 383 | 0.5708 | 0.4337 | 0.4987 | +0.072 | -0.065 | -0.0001 ± 0.0077 |
| thinner_sample <300 | 472 | 0.5505 | 0.3889 | 0.4767 | +0.074 | -0.088 | 0.0113 ± 0.0079 |
| thinner_sample >=3000 | 199 | 0.5181 | 0.4178 | 0.4221 | +0.096 | -0.004 | 0.0187 ± 0.0082 |
| data_status ADEQUATE | 390 | 0.5254 | 0.4189 | 0.4385 | +0.087 | -0.019 | 0.0105 ± 0.0062 |
| data_status LIMITED | 318 | 0.5642 | 0.4327 | 0.5031 | +0.061 | -0.070 | -0.0041 ± 0.0083 |
| data_status POOR | 715 | 0.5556 | 0.4013 | 0.4755 | +0.080 | -0.074 | 0.0109 ± 0.0062 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 212 | 0.1833 | 0.184 | -0.0008 ± 0.001 | 0.5418 | 0.5438 | 0.4929 | 0.4787 | 0.4953 | -0.101 ± 0.0314 | -0.01 (3) |
| 3-5 | 143 | 0.1817 | 0.1835 | -0.0018 ± 0.0029 | 0.5422 | 0.5435 | 0.5147 | 0.4741 | 0.5105 | -0.070 ± 0.037 | 0.02 (1) |
| 5-10 | 300 | 0.2 | 0.2024 | -0.0024 ± 0.0039 | 0.5863 | 0.5914 | 0.5208 | 0.4468 | 0.4933 | -0.089 ± 0.0271 | -0.0167 (3) |
| 10-15 | 244 | 0.2209 | 0.2175 | +0.0034 ± 0.0075 | 0.6301 | 0.6189 | 0.5276 | 0.4035 | 0.4508 | -0.094 ± 0.03 | -0.0633 (3) |
| 15-25 | 310 | 0.2177 | 0.2098 | +0.0079 ± 0.0102 | 0.6244 | 0.6041 | 0.5716 | 0.3762 | 0.4516 | -0.076 ± 0.026 | -0.02 (4) |
| 25-40 | 175 | 0.2106 | 0.1996 | +0.0110 ± 0.02 | 0.6077 | 0.5735 | 0.643 | 0.3314 | 0.4686 | -0.051 ± 0.0297 | -0.01 (1) |
| 40+ | 39 | 0.3105 | 0.1436 | +0.1669 ± 0.0543 | 0.8355 | 0.4493 | 0.7382 | 0.2969 | 0.3333 | -0.170 ± 0.0539 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 869 | 0.1683 | 0.1692 | -0.0009 ± 0.0005 | 0.504 | 0.5052 | 0.491 | 0.4762 | 0.5201 | -0.031 ± 0.0143 | -0.0188 (8) |
| 3-5 | 637 | 0.1871 | 0.1852 | +0.0019 ± 0.0014 | 0.5533 | 0.5442 | 0.4779 | 0.4381 | 0.4286 | -0.079 ± 0.0176 | 0.02 (1) |
| 5-10 | 1334 | 0.1852 | 0.1852 | +0.0000 ± 0.0017 | 0.5513 | 0.5493 | 0.4806 | 0.4069 | 0.4423 | -0.043 ± 0.0119 | -0.0129 (7) |
| 10-15 | 1139 | 0.1965 | 0.1821 | +0.0144 ± 0.0032 | 0.5773 | 0.5343 | 0.4736 | 0.3491 | 0.3547 | -0.074 ± 0.0126 | -0.0633 (3) |
| 15-25 | 1467 | 0.1995 | 0.1601 | +0.0393 ± 0.0041 | 0.5882 | 0.4779 | 0.4887 | 0.2916 | 0.2897 | -0.083 ± 0.0104 | -0.017 (10) |
| 25-40 | 1385 | 0.2122 | 0.1203 | +0.0919 ± 0.0059 | 0.6161 | 0.3728 | 0.5208 | 0.2068 | 0.2202 | -0.053 ± 0.009 | -0.01 (1) |
| 40+ | 983 | 0.3685 | 0.0398 | +0.3287 ± 0.0071 | 0.9597 | 0.1647 | 0.6182 | 0.1032 | 0.0509 | -0.086 ± 0.0059 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 156 | 0.187 | 0.1864 | +0.0005 ± 0.0012 | 0.5503 | 0.5474 | 0.494 | 0.4793 | 0.4551 | -0.144 ± 0.0369 | -0.01 (1) |
| 3-5 | 103 | 0.1975 | 0.1972 | +0.0003 ± 0.0035 | 0.5712 | 0.5755 | 0.4925 | 0.4527 | 0.466 | -0.078 ± 0.0471 | 0.02 (1) |
| 5-10 | 256 | 0.1956 | 0.1951 | +0.0005 ± 0.0041 | 0.5747 | 0.5725 | 0.568 | 0.493 | 0.5195 | -0.092 ± 0.0286 | -0.01 (4) |
| 10-15 | 243 | 0.2303 | 0.2176 | +0.0127 ± 0.0075 | 0.6506 | 0.6249 | 0.5812 | 0.4571 | 0.4733 | -0.126 ± 0.0317 | -0.0667 (3) |
| 15-25 | 347 | 0.2205 | 0.2034 | +0.0171 ± 0.0096 | 0.6274 | 0.5867 | 0.5943 | 0.3969 | 0.4582 | -0.095 ± 0.0248 | -0.0167 (3) |
| 25-40 | 226 | 0.2578 | 0.1989 | +0.0589 ± 0.0184 | 0.7173 | 0.5782 | 0.664 | 0.3531 | 0.4115 | -0.128 ± 0.0301 | -0.025 (2) |
| 40+ | 92 | 0.3507 | 0.1819 | +0.1687 ± 0.0441 | 0.9751 | 0.5349 | 0.7556 | 0.2692 | 0.3587 | -0.061 ± 0.0415 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 748 | 0.1684 | 0.1687 | -0.0003 ± 0.0005 | 0.5035 | 0.5042 | 0.5084 | 0.4943 | 0.5067 | -0.059 ± 0.0161 | -0.0217 (6) |
| 3-5 | 514 | 0.1802 | 0.1769 | +0.0033 ± 0.0015 | 0.5304 | 0.5252 | 0.511 | 0.4712 | 0.4494 | -0.076 ± 0.0189 | 0.02 (1) |
| 5-10 | 1174 | 0.1821 | 0.1818 | +0.0003 ± 0.0019 | 0.5411 | 0.5372 | 0.5131 | 0.4385 | 0.471 | -0.041 ± 0.0127 | -0.01 (5) |
| 10-15 | 1058 | 0.1961 | 0.1808 | +0.0154 ± 0.0033 | 0.58 | 0.531 | 0.5126 | 0.3888 | 0.3922 | -0.080 ± 0.0134 | -0.0575 (4) |
| 15-25 | 1548 | 0.2077 | 0.1676 | +0.0401 ± 0.0041 | 0.6067 | 0.4981 | 0.5253 | 0.33 | 0.3282 | -0.087 ± 0.0105 | -0.0143 (7) |
| 25-40 | 1481 | 0.2404 | 0.1294 | +0.1110 ± 0.006 | 0.6828 | 0.3993 | 0.5541 | 0.2369 | 0.2194 | -0.089 ± 0.0095 | -0.015 (6) |
| 40+ | 1291 | 0.3969 | 0.068 | +0.3290 ± 0.0083 | 1.0365 | 0.2379 | 0.6648 | 0.1266 | 0.103 | -0.064 ± 0.007 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 219 | 0.1908 | 0.1928 | -0.0021 ± 0.0011 | 0.5603 | 0.5664 | 0.5111 | 0.4962 | 0.5434 | -0.050 ± 0.0299 | -0.01 (5) |
| 3-5 | 153 | 0.1789 | 0.1774 | +0.0015 ± 0.0027 | 0.5319 | 0.5283 | 0.5032 | 0.4641 | 0.4641 | -0.130 ± 0.0365 | -- (0) |
| 5-10 | 303 | 0.1977 | 0.198 | -0.0003 ± 0.0039 | 0.5819 | 0.5786 | 0.5173 | 0.4436 | 0.4785 | -0.091 ± 0.0262 | -0.01 (3) |
| 10-15 | 234 | 0.214 | 0.2169 | -0.0029 ± 0.0075 | 0.6176 | 0.6196 | 0.5435 | 0.4201 | 0.4957 | -0.075 ± 0.0302 | -0.044 (5) |
| 15-25 | 303 | 0.221 | 0.2067 | +0.0144 ± 0.0102 | 0.6381 | 0.5952 | 0.5829 | 0.3886 | 0.4488 | -0.093 ± 0.026 | -0.03 (1) |
| 25-40 | 178 | 0.2026 | 0.2089 | -0.0062 ± 0.02 | 0.5898 | 0.5972 | 0.6503 | 0.3375 | 0.5 | -0.036 ± 0.0292 | 0.0 (1) |
| 40+ | 33 | 0.3471 | 0.1356 | +0.2115 ± 0.058 | 0.918 | 0.43 | 0.7266 | 0.2779 | 0.2727 | -0.196 ± 0.0611 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 876 | 0.1684 | 0.1693 | -0.0009 ± 0.0005 | 0.506 | 0.508 | 0.4917 | 0.4769 | 0.508 | -0.039 ± 0.014 | -0.0162 (13) |
| 3-5 | 618 | 0.1865 | 0.1819 | +0.0046 ± 0.0014 | 0.5497 | 0.5408 | 0.4762 | 0.4371 | 0.3964 | -0.121 ± 0.0179 | -0.01 (2) |
| 5-10 | 1391 | 0.185 | 0.1808 | +0.0042 ± 0.0017 | 0.5523 | 0.5352 | 0.4821 | 0.4084 | 0.4148 | -0.067 ± 0.0114 | -0.01 (3) |
| 10-15 | 1071 | 0.1887 | 0.1803 | +0.0084 ± 0.0032 | 0.5591 | 0.5286 | 0.4825 | 0.3592 | 0.3866 | -0.056 ± 0.0128 | -0.03 (9) |
| 15-25 | 1603 | 0.2017 | 0.1615 | +0.0402 ± 0.004 | 0.5969 | 0.4828 | 0.4933 | 0.2951 | 0.2951 | -0.075 ± 0.0101 | -0.03 (2) |
| 25-40 | 1325 | 0.2132 | 0.1183 | +0.0949 ± 0.006 | 0.6179 | 0.3656 | 0.5195 | 0.2011 | 0.2151 | -0.057 ± 0.009 | 0.0 (1) |
| 40+ | 930 | 0.3832 | 0.0408 | +0.3424 ± 0.0076 | 1.0028 | 0.1676 | 0.6248 | 0.1025 | 0.0473 | -0.087 ± 0.0063 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 495 | 0.2026 | 0.2028 | -0.0002 ± 0.0007 | 0.5863 | 0.5872 | 0.4992 | 0.4843 | 0.4909 | -0.043 ± 0.0202 | -0.0226 (46) |
| 3-5 | 372 | 0.1927 | 0.1929 | -0.0001 ± 0.0018 | 0.567 | 0.5658 | 0.4785 | 0.4388 | 0.4624 | -0.034 ± 0.0225 | -0.0059 (32) |
| 5-10 | 760 | 0.1888 | 0.1841 | +0.0048 ± 0.0024 | 0.5612 | 0.548 | 0.4673 | 0.3936 | 0.3987 | -0.052 ± 0.0158 | -0.005 (72) |
| 10-15 | 505 | 0.2018 | 0.1917 | +0.0100 ± 0.0049 | 0.5921 | 0.5638 | 0.467 | 0.344 | 0.3644 | -0.041 ± 0.0194 | 0.0016 (63) |
| 15-25 | 680 | 0.2364 | 0.212 | +0.0244 ± 0.0069 | 0.6689 | 0.6098 | 0.5362 | 0.3427 | 0.3779 | -0.044 ± 0.0178 | -0.0216 (58) |
| 25-40 | 369 | 0.2496 | 0.1772 | +0.0724 ± 0.0136 | 0.6996 | 0.5255 | 0.5994 | 0.2872 | 0.3252 | -0.066 ± 0.0208 | -0.0216 (25) |
| 40+ | 117 | 0.3747 | 0.1653 | +0.2094 ± 0.0395 | 1.0503 | 0.5022 | 0.7517 | 0.2526 | 0.3162 | -0.051 ± 0.0354 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1182 | 0.1918 | 0.1919 | -0.0001 ± 0.0004 | 0.559 | 0.5593 | 0.4972 | 0.482 | 0.4932 | -0.037 ± 0.0126 | -0.0155 (82) |
| 3-5 | 841 | 0.1845 | 0.1838 | +0.0007 ± 0.0012 | 0.5459 | 0.5441 | 0.49 | 0.4504 | 0.4614 | -0.040 ± 0.0148 | -0.018 (54) |
| 5-10 | 1749 | 0.1838 | 0.1781 | +0.0058 ± 0.0015 | 0.5483 | 0.5311 | 0.4652 | 0.3908 | 0.3922 | -0.054 ± 0.0102 | -0.0089 (122) |
| 10-15 | 1306 | 0.1968 | 0.1852 | +0.0115 ± 0.003 | 0.581 | 0.5475 | 0.4766 | 0.3535 | 0.3675 | -0.046 ± 0.0118 | -0.0053 (99) |
| 15-25 | 1705 | 0.2267 | 0.1939 | +0.0328 ± 0.0042 | 0.6528 | 0.5655 | 0.5265 | 0.331 | 0.3449 | -0.058 ± 0.0108 | -0.0255 (106) |
| 25-40 | 1243 | 0.2388 | 0.1502 | +0.0886 ± 0.0069 | 0.6757 | 0.4533 | 0.564 | 0.249 | 0.2671 | -0.062 ± 0.0107 | -0.0206 (47) |
| 40+ | 612 | 0.3697 | 0.0878 | +0.2819 ± 0.0129 | 1.004 | 0.2908 | 0.6612 | 0.1528 | 0.1405 | -0.070 ± 0.0115 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 1423 | 1.149 ± 0.079 | 1.25 | 0.167 | 0.1667 | 0.2074 | 0.2 |
| gen2 | 1423 | 0.935 ± 0.069 | 1.168 | 0.1826 | 0.1665 | 0.2267 | 0.1999 |
| gen1_elo | 1423 | 1.123 ± 0.077 | 1.229 | 0.1721 | 0.1669 | 0.2063 | 0.1999 |
| gen1_sr | 1423 | 1.172 ± 0.09 | 1.241 | 0.1405 | 0.1685 | 0.222 | 0.2 |
| gen1_ledger | 3298 | 0.934 ± 0.047 | 1.096 | 0.1653 | 0.1942 | 0.2165 | 0.1934 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 9,081)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,492 | 27.4% |
| STALE_QUOTE | market_freshness | 2,136 | 23.5% |
| BOOK_QUALITY | execution | 1,610 | 17.7% |
| POOR_DATA | data | 969 | 10.7% |
| LIMITED_DATA | data | 597 | 6.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 424 | 4.7% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 404 | 4.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 225 | 2.5% |
| IDENTITY_AMBIGUOUS | mapping | 215 | 2.4% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 9 | 0.1% |

Cause class: coverage 27.4%, market_freshness 23.5%, execution 17.7%, data 17.2%, market_freshness/coverage 6.9%, model_calibration_or_unknown 4.7%, mapping 2.4%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.8%, START_UNVERIFIABLE 96.0%, LOW_DATA_QUALITY 69.0%, THIN_PLAYER_HISTORY 58.7%, STALE_PLAYER_DATA 58.7%, STALE_KALSHI_QUOTE 50.9%, MODEL_INTERNAL_DISAGREEMENT 37.4%, ASYMMETRIC_SAMPLE_SIZE 31.9%, WIDE_SPREAD 24.3%, MODEL_HIGH_UNCERTAINTY 15.3%, PLAYER_IDENTITY_RISK 10.7%, LEVEL_TRANSFER_RISK 8.5%, LOW_DISPLAYED_LIQUIDITY 7.1%, EVENT_MAPPING_RISK 7.0%, MODEL_CALIBRATION_OUTLIER 2.7%, UNKNOWN 0.5%, EXTERNAL_MARKET_REJECTION 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 29.4%, POST_SETTLEMENT_OBSERVATION 27.4%, POSSIBLE_IN_PLAY_QUOTE 4.9%, CONFIRMED_IN_PLAY_QUOTE 0.7%

### >= ge_25 pp (N = 4,947)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,957 | 39.6% |
| STALE_QUOTE | market_freshness | 959 | 19.4% |
| BOOK_QUALITY | execution | 831 | 16.8% |
| POOR_DATA | data | 420 | 8.5% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 223 | 4.5% |
| LIMITED_DATA | data | 183 | 3.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 138 | 2.8% |
| IDENTITY_AMBIGUOUS | mapping | 126 | 2.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 107 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 3 | 0.1% |

Cause class: coverage 39.6%, market_freshness 19.4%, execution 16.8%, data 12.2%, market_freshness/coverage 7.3%, mapping 2.5%, model_calibration_or_unknown 2.2%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 97.9%, LOW_DATA_QUALITY 71.6%, THIN_PLAYER_HISTORY 60.7%, STALE_KALSHI_QUOTE 58.4%, STALE_PLAYER_DATA 54.7%, MODEL_INTERNAL_DISAGREEMENT 39.8%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 23.3%, MODEL_HIGH_UNCERTAINTY 16.6%, PLAYER_IDENTITY_RISK 13.3%, EVENT_MAPPING_RISK 7.9%, LEVEL_TRANSFER_RISK 7.6%, LOW_DISPLAYED_LIQUIDITY 7.5%, MODEL_CALIBRATION_OUTLIER 3.4%, UNKNOWN 0.1%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 41.8%, POST_SETTLEMENT_OBSERVATION 39.6%, POSSIBLE_IN_PLAY_QUOTE 5.0%, CONFIRMED_IN_PLAY_QUOTE 0.8%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 4141, "IDENTITY_AMBIGUOUS": 806}; ticker orientation: {"VERIFIED": 4947}.

Checks: discipline:AMBIGUOUS 239, discipline:PASS 4708, identity_confidence:AMBIGUOUS 658, identity_confidence:PASS 4289, level_mapping:NA 251, level_mapping:PASS 4696, market_pair:AMBIGUOUS 182, market_pair:NA 120, market_pair:PASS 4645, model_complement:NA 88, model_complement:PASS 4859, namesake:PASS 4947, physical_match_id:NA 2105, physical_match_id:PASS 2842, player_ids:PASS 4947, same_pair_other_event:PASS 4947, ticker_orientation:PASS 4947

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,200 | 1.9% | 1.9% | 0.5% | {"market_freshness": 20, "execution": 3} | 5.6 | 0.1932 / 0.1842 (79) | 22.2% | 0.2% | 6.1% | 1.5% |
| CHALLENGER | 3,396 | 19.0% | 6.7% | 13.1% | {"coverage": 399, "market_freshness": 107, "market_freshness/coverage": 73, "model_calibration_or_unknown": 38, "data": 25, "execution": 4} | 6.92 | 0.2204 / 0.2034 (792) | 48.4% | 5.3% | 1.4% | 23.6% |
| DOUBLES | 543 | 44.0% | 43.6% | 4.8% | {"market_freshness": 106, "execution": 66, "mapping": 46, "market_freshness/coverage": 14, "coverage": 7} | 22.69 | 0.3152 / 0.2262 (172) | 43.1% | 0.0% | 100.0% | 7.9% |
| ITF_MEN | 6,555 | 24.9% | 17.2% | 32.9% | {"coverage": 652, "execution": 361, "market_freshness": 257, "data": 235, "market_freshness/coverage": 104, "mapping": 19, "model_calibration_or_unknown": 1} | 11.1 | 0.2156 / 0.1927 (1563) | 41.4% | 56.4% | 6.5% | 22.8% |
| ITF_WOMEN | 8,291 | 26.6% | 18.6% | 44.5% | {"coverage": 882, "market_freshness": 412, "execution": 380, "data": 319, "market_freshness/coverage": 129, "mapping": 55, "model_calibration_or_unknown": 22, "model_calibration": 2} | 12.35 | 0.2012 / 0.1908 (1683) | 42.8% | 60.1% | 10.7% | 22.8% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 942 | 8.4% | 7.2% | 1.6% | {"market_freshness": 34, "model_calibration_or_unknown": 16, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.39 | 0.2026 / 0.197 (137) | 35.2% | 2.2% | 1.3% | 3.4% |
| WTA125 | 756 | 15.6% | 11.3% | 2.4% | {"market_freshness/coverage": 31, "model_calibration_or_unknown": 28, "market_freshness": 21, "data": 13, "coverage": 12, "execution": 8, "mapping": 4, "model_calibration": 1} | 10.08 | 0.2208 / 0.2064 (253) | 28.2% | 5.7% | 4.0% | 12.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 3 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 4 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 207 min (STALE); no external reference |
| 5 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 6 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 7 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 8 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 9 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 10 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 11 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 12 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 13 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 14% | +77 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 14 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 15 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 16 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 17 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 18 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 19 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 20 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 21 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 22 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 23 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 24 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 25 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 26 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 27 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 28 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 253 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 29 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 30 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 31 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 32 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 33 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 256 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 34 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 687 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 35 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 36 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 37 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 156 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 38 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 39 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 40 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 41 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 42 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 43 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.9h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 671 min (STALE); no external reference |
| 44 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 407 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 45 | `KXWTAMATCH-26OCT01YASCHW-CHW` | WTA | fair_v1 | 73% / 2% | +70 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 51 min (STALE); no external reference |
| 46 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 47 | `KXATPCHALLENGERMATCH-26OCT05CASMUN-CAS` | CHALLENGER | fair_v1 | 83% / 14% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 227 min (STALE); data POOR (grade D, thinner serve sample 814.0, ratio 3.76); no external reference |
| 48 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 49 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9794, "by_level_share_of_ge_25pp": {"ATP": 0.0046, "CHALLENGER": 0.1306, "DOUBLES": 0.0483, "ITF_MEN": 0.3293, "ITF_WOMEN": 0.4449, "OTHER": 0.0024, "WTA": 0.016, "WTA125": 0.0239}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5836, "share_primary_cause_market_settled_or_in_play": 0.4686, "share_primary_cause_stale_quote_only": 0.1939}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 4947, "identity_ambiguous_share": 0.1629, "ticker_orientation": {"VERIFIED": 4947}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 2842, "with_external": 28, "coverage": 0.0099, "external_status": {"EXTERNAL_STALE": 25, "AGREES_WITH_KALSHI": 3}, "triangulation": {"INSUFFICIENT_INPUTS": 25, "MODEL_LONE_OUTLIER": 3}, "share_external_agrees_with_kalshi": 0.1071, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 1323, "with_external": 28, "coverage": 0.0212, "external_status": {"EXTERNAL_STALE": 25, "AGREES_WITH_KALSHI": 3}, "triangulation": {"INSUFFICIENT_INPUTS": 25, "MODEL_LONE_OUTLIER": 3}, "share_external_agrees_with_kalshi": 0.1071, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 596.0, "median_sample_ratio": 2.38, "median_min_matches": 18.5, "median_max_days_since_last": 198.0, "share_severe_asymmetry": 0.1874, "data_status": {"POOR": 2662, "LIMITED": 1392, "ADEQUATE": 893}, "comparison_lt_10pp": {"median_thinner_serve_points": 1733.5, "median_sample_ratio": 1.77, "median_min_matches": 72.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 318, "model_minus_observed": 0.0772, "kalshi_minus_observed": -0.0557, "brier_diff_model_minus_kalshi": 0.002}, "4-10x": {"n": 231, "model_minus_observed": 0.0522, "kalshi_minus_observed": -0.0865, "brier_diff_model_minus_kalshi": 0.0007}, "<2x": {"n": 660, "model_minus_observed": 0.0798, "kalshi_minus_observed": -0.0448, "brier_diff_model_minus_kalshi": 0.0109}, ">=10x": {"n": 214, "model_minus_observed": 0.0995, "kalshi_minus_observed": -0.0737, "brier_diff_model_minus_kalshi": 0.012}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 1423, "model": {"intercept": -0.607, "slope": 0.935, "slope_se": 0.069}, "kalshi_mid_same_rows": {"intercept": 0.227, "slope": 1.168, "slope_se": 0.078}, "mean_extremity_model": 0.1826, "mean_extremity_kalshi": 0.1665, "model_brier": 0.2267, "kalshi_brier": 0.1999, "brier_diff_model_minus_kalshi": 0.0268, "brier_diff_se": 0.0051, "model_logloss": 0.6461, "kalshi_logloss": 0.5809}, "fair_v1": {"n": 1423, "model": {"intercept": -0.403, "slope": 1.149, "slope_se": 0.079}, "kalshi_mid_same_rows": {"intercept": 0.372, "slope": 1.25, "slope_se": 0.081}, "mean_extremity_model": 0.167, "mean_extremity_kalshi": 0.1667, "model_brier": 0.2074, "kalshi_brier": 0.2, "brier_diff_model_minus_kalshi": 0.0074, "brier_diff_se": 0.004, "model_logloss": 0.6005, "kalshi_logloss": 0.5809}, "gen1_elo": {"n": 1423, "model": {"intercept": -0.38, "slope": 1.123, "slope_se": 0.077}, "kalshi_mid_same_rows": {"intercept": 0.367, "slope": 1.229, "slope_se": 0.08}, "mean_extremity_model": 0.1721, "mean_extremity_kalshi": 0.1669, "model_brier": 0.2063, "kalshi_brier": 0.1999, "brier_diff_model_minus_kalshi": 0.0065, "brier_diff_se": 0.004, "model_logloss": 0.5998, "kalshi_logloss": 0.5805}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2511, "share_ge_15": 0.4377, "median_abs_gap": 13.02, "n": 11316}, "gen1_elo": {"share_ge_25": 0.2411, "share_ge_15": 0.4354, "median_abs_gap": 12.57, "n": 11316}, "gen1_sr": {"share_ge_25": 0.3013, "share_ge_15": 0.5197, "median_abs_gap": 15.67, "n": 11316}, "gen2": {"share_ge_25": 0.3068, "share_ge_15": 0.5063, "median_abs_gap": 15.32, "n": 11316}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1521, "share_ge_15": 0.3443, "median_abs_gap": 10.57, "n": 8696}, "gen1_elo": {"share_ge_25": 0.1459, "share_ge_15": 0.3395, "median_abs_gap": 10.14, "n": 8696}, "gen1_sr": {"share_ge_25": 0.203, "share_ge_15": 0.4358, "median_abs_gap": 12.98, "n": 8696}, "gen2": {"share_ge_25": 0.223, "share_ge_15": 0.4327, "median_abs_gap": 12.78, "n": 8696}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.6, "share_ge_25_all": 0.0192, "share_ge_25_pregame_clean": 0.0195}, "WTA": {"median_abs_gap_pregame_clean": 8.39, "share_ge_25_all": 0.0839, "share_ge_25_pregame_clean": 0.0725}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2317, "share_within_10pp_all": 0.4303, "share_within_10pp_pregame_clean": 0.4926, "corr_model_vs_mid_pregame_clean": 0.8466}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 212, "model_brier": 0.1833, "kalshi_brier": 0.184, "brier_diff_model_minus_kalshi": -0.0008}, "10-15": {"n_settled": 244, "model_brier": 0.2209, "kalshi_brier": 0.2175, "brier_diff_model_minus_kalshi": 0.0034}, "15-25": {"n_settled": 310, "model_brier": 0.2177, "kalshi_brier": 0.2098, "brier_diff_model_minus_kalshi": 0.0079}, "25-40": {"n_settled": 175, "model_brier": 0.2106, "kalshi_brier": 0.1996, "brier_diff_model_minus_kalshi": 0.011}, "3-5": {"n_settled": 143, "model_brier": 0.1817, "kalshi_brier": 0.1835, "brier_diff_model_minus_kalshi": -0.0018}, "40+": {"n_settled": 39, "model_brier": 0.3105, "kalshi_brier": 0.1436, "brier_diff_model_minus_kalshi": 0.1669}, "5-10": {"n_settled": 300, "model_brier": 0.2, "kalshi_brier": 0.2024, "brier_diff_model_minus_kalshi": -0.0024}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%)
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap).
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 172, "model_brier": 0.3152, "kalshi_brier": 0.2262, "brier_diff_model_minus_kalshi": 0.0891, "brier_diff_se": 0.0246, "corr_model_outcome": -0.0687, "corr_kalshi_outcome": 0.3509}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
