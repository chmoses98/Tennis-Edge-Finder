# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-05T18:21Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 14,427): 0-3 13.0%, 3-5 9.1%, 5-10 18.8%, 10-15 15.1%, 15-25 19.3%, 25-40 15.1%, 40+ 9.6%; median gap 12.82 pp.
* **Where the extremes live**: 97.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 74.7%, Challenger 14.7%, doubles 5.3%). Main tour: ATP 3.8% and WTA 9.3% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 3,562): MARKET_ALREADY_SETTLED_WHEN_PRICED 45.2%, STALE_QUOTE 23.7%, BOOK_QUALITY 9.5%, POOR_DATA 6.1%, POSSIBLY_IN_PLAY_QUOTE 4.8%, IN_PLAY_QUOTE 3.1%, LIMITED_DATA 2.8%, IDENTITY_AMBIGUOUS 2.7%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.1%. By class: coverage 45.2%, market_freshness 23.7%, execution 9.5%, data 8.8%, market_freshness/coverage 8.0%, mapping 2.7%, model_calibration_or_unknown 2.1%, model_calibration 0.1%.
* **Stale / settled / in-play**: 68.2% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 53.1% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 3,562 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 16.1% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 0.7%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 13.8% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 688.0 points vs 1886.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.126, Gen-2 0.918, Gen-1 ledger 0.908 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 128 model 0.2287 vs Kalshi 0.1819; n 30 model 0.3354 vs Kalshi 0.1357.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%). Not implemented here.

## 1. Observations

* 49,568 model-market comparisons (85,363 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 20,369 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-05T18:15:34.834545+00:00'], shadow board 14,439 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-05T18:15:39.439473+00:00'], Model 4 4,276 rows, 8,690 settled tickers, 1,950 tickers with an external scan.
* By model: {"gen1_ledger": 12231, "gen1_elo": 7256, "fair_v1": 7256, "gen2": 7256, "gen1_sr": 7256, "model4_fundamental": 4161, "model4_conditioned": 4152}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 14,427 | 13.0 | 9.1 | 18.8 | 15.1 | 19.3 | 15.1 | 9.6 | 12.82 | 44.0% | 24.7% |
| MW fair_v1 | 7,256 | 12.8 | 8.7 | 17.6 | 15.3 | 18.5 | 15.8 | 11.3 | 13.38 | 45.6% | 27.1% |
| MW gen1_elo | 7,256 | 12.8 | 8.6 | 19.5 | 14.3 | 18.6 | 15.6 | 10.6 | 12.97 | 44.8% | 26.2% |
| MW gen1_ledger | 7,171 | 13.3 | 9.5 | 20.0 | 14.8 | 20.2 | 14.4 | 7.8 | 12.16 | 42.4% | 22.2% |
| MW gen1_sr | 7,256 | 9.4 | 7.3 | 15.9 | 13.7 | 21.6 | 19.0 | 13.0 | 16.51 | 53.6% | 32.0% |
| MW gen2 | 7,256 | 10.9 | 6.7 | 16.1 | 13.8 | 20.2 | 17.7 | 14.5 | 16.05 | 52.4% | 32.2% |
| all families model4_conditioned | 4,152 | 20.4 | 18.0 | 30.5 | 19.4 | 8.6 | 1.7 | 1.4 | 6.55 | 11.7% | 3.1% |
| all families model4_fundamental | 4,161 | 15.5 | 11.6 | 30.5 | 20.7 | 13.9 | 5.5 | 2.2 | 8.54 | 21.6% | 7.7% |

Configurable thresholds (primary): >=5pp 77.9%, >=10pp 59.1%, >=15pp 44.0%, >=20pp 33.6%, >=25pp 24.7%, >=30pp 18.2%, >=40pp 9.6%, >=50pp 4.2%
Executable gap (model outside the book, before fees): median 9.73pp; >=10pp 49.2%, >=25pp 21.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 426 | 21.4 | 18.3 | 24.4 | 15.5 | 15.0 | 2.8 | 2.6 | 6.46 | 20.4% | 5.4% |
| CHALLENGER | 1,532 | 14.8 | 10.3 | 16.5 | 15.7 | 14.9 | 14.1 | 13.6 | 12.91 | 42.7% | 27.7% |
| ITF_MEN | 2,031 | 11.5 | 8.3 | 18.5 | 14.6 | 18.1 | 15.9 | 13.2 | 13.59 | 47.2% | 29.1% |
| ITF_WOMEN | 2,675 | 9.5 | 6.3 | 15.1 | 15.4 | 21.5 | 20.6 | 11.6 | 16.57 | 53.7% | 32.2% |
| WTA | 453 | 22.7 | 10.4 | 25.2 | 13.5 | 18.8 | 7.1 | 2.4 | 8.28 | 28.3% | 9.5% |
| WTA125 | 139 | 14.4 | 6.5 | 20.1 | 27.3 | 15.1 | 10.8 | 5.8 | 11.47 | 31.6% | 16.6% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 426 | 19.5 | 14.3 | 25.6 | 15.5 | 17.1 | 4.9 | 3.0 | 7.72 | 25.1% | 8.0% |
| CHALLENGER | 1,532 | 13.6 | 6.1 | 17.9 | 14.0 | 18.9 | 16.3 | 13.2 | 14.45 | 48.4% | 29.5% |
| ITF_MEN | 2,031 | 8.9 | 6.8 | 17.0 | 15.3 | 19.6 | 17.6 | 14.9 | 15.66 | 52.0% | 32.5% |
| ITF_WOMEN | 2,675 | 8.3 | 6.1 | 12.7 | 11.7 | 21.5 | 20.8 | 18.9 | 19.92 | 61.2% | 39.7% |
| WTA | 453 | 20.3 | 5.5 | 16.6 | 15.7 | 22.1 | 17.4 | 2.4 | 13.18 | 41.9% | 19.9% |
| WTA125 | 139 | 6.5 | 3.6 | 17.3 | 19.4 | 24.5 | 16.6 | 12.2 | 16.14 | 53.2% | 28.8% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 426 | 25.8 | 12.2 | 29.3 | 13.6 | 9.2 | 7.0 | 2.8 | 7.44 | 19.0% | 9.9% |
| CHALLENGER | 1,532 | 15.6 | 9.8 | 21.5 | 12.9 | 13.2 | 13.2 | 13.8 | 11.08 | 40.3% | 27.0% |
| ITF_MEN | 2,031 | 9.8 | 9.1 | 17.7 | 14.9 | 19.3 | 16.1 | 13.1 | 14.13 | 48.4% | 29.1% |
| ITF_WOMEN | 2,675 | 9.3 | 6.2 | 16.0 | 14.2 | 23.9 | 20.4 | 10.1 | 17.18 | 54.3% | 30.5% |
| WTA | 453 | 22.5 | 14.1 | 30.9 | 15.7 | 11.0 | 4.2 | 1.6 | 6.99 | 16.8% | 5.7% |
| WTA125 | 139 | 19.4 | 4.3 | 24.5 | 23.7 | 20.1 | 6.5 | 1.4 | 10.52 | 28.1% | 7.9% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 173 | 26.6 | 21.4 | 36.4 | 12.7 | 2.9 | 0.0 | 0.0 | 5.4 | 2.9% | 0.0% |
| CHALLENGER | 1,037 | 20.5 | 14.7 | 26.0 | 15.3 | 13.9 | 6.8 | 2.7 | 7.45 | 23.4% | 9.6% |
| DOUBLES | 406 | 5.4 | 3.7 | 10.8 | 11.1 | 22.4 | 20.7 | 25.9 | 23.68 | 69.0% | 46.6% |
| ITF_MEN | 2,285 | 13.9 | 8.8 | 18.7 | 14.3 | 20.7 | 14.2 | 9.4 | 12.58 | 44.3% | 23.6% |
| ITF_WOMEN | 2,384 | 8.8 | 8.0 | 16.9 | 14.4 | 23.9 | 19.8 | 8.1 | 15.82 | 51.8% | 27.9% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 381 | 17.1 | 8.9 | 26.0 | 21.3 | 17.6 | 8.4 | 0.8 | 9.55 | 26.8% | 9.2% |
| WTA125 | 356 | 13.8 | 9.6 | 21.6 | 18.3 | 21.6 | 11.5 | 3.6 | 11.05 | 36.8% | 15.2% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 425 | 21.2 | 18.4 | 24.5 | 15.5 | 15.1 | 2.8 | 2.6 | 6.47 | 20.5% | 5.4% |
| CHALLENGER | 1,082 | 19.2 | 12.8 | 20.6 | 18.5 | 16.4 | 8.2 | 4.2 | 9.22 | 28.8% | 12.4% |
| ITF_MEN | 1,350 | 14.7 | 11.3 | 22.6 | 16.1 | 18.6 | 11.4 | 5.4 | 10.31 | 35.4% | 16.8% |
| ITF_WOMEN | 1,855 | 12.2 | 8.2 | 17.9 | 17.6 | 23.2 | 16.5 | 4.3 | 13.37 | 44.0% | 20.8% |
| WTA | 452 | 22.8 | 10.4 | 25.2 | 13.5 | 18.8 | 6.9 | 2.4 | 8.25 | 28.1% | 9.3% |
| WTA125 | 133 | 15.0 | 6.8 | 21.1 | 28.6 | 15.0 | 9.8 | 3.8 | 11.03 | 28.6% | 13.5% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 425 | 19.5 | 14.1 | 25.6 | 15.5 | 17.2 | 4.9 | 3.1 | 7.73 | 25.2% | 8.0% |
| CHALLENGER | 1,082 | 17.4 | 7.7 | 22.4 | 17.5 | 20.0 | 11.6 | 3.6 | 10.66 | 35.1% | 15.2% |
| ITF_MEN | 1,350 | 11.6 | 8.3 | 20.6 | 17.7 | 20.7 | 13.8 | 7.3 | 12.46 | 41.8% | 21.1% |
| ITF_WOMEN | 1,855 | 10.2 | 7.5 | 14.2 | 11.8 | 24.4 | 19.2 | 12.6 | 17.18 | 56.3% | 31.9% |
| WTA | 452 | 20.4 | 5.5 | 16.6 | 15.7 | 22.1 | 17.3 | 2.4 | 13.12 | 41.8% | 19.7% |
| WTA125 | 133 | 6.8 | 3.8 | 17.3 | 20.3 | 25.6 | 17.3 | 9.0 | 15.79 | 51.9% | 26.3% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 163 | 27.0 | 22.7 | 36.8 | 12.9 | 0.6 | 0.0 | 0.0 | 5.22 | 0.6% | 0.0% |
| CHALLENGER | 850 | 22.5 | 17.2 | 28.8 | 15.1 | 13.3 | 3.1 | 0.1 | 6.72 | 16.5% | 3.2% |
| DOUBLES | 367 | 5.5 | 3.5 | 11.2 | 11.2 | 22.3 | 21.0 | 25.3 | 23.62 | 68.7% | 46.3% |
| ITF_MEN | 1,673 | 16.6 | 10.5 | 21.5 | 15.5 | 20.7 | 11.1 | 4.1 | 10.42 | 35.9% | 15.2% |
| ITF_WOMEN | 1,715 | 10.4 | 9.3 | 19.8 | 16.1 | 24.8 | 17.4 | 2.3 | 13.01 | 44.4% | 19.7% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 352 | 17.3 | 9.4 | 26.7 | 21.9 | 18.2 | 6.5 | 0.0 | 9.28 | 24.7% | 6.5% |
| WTA125 | 277 | 16.2 | 10.5 | 25.6 | 21.7 | 19.9 | 5.8 | 0.4 | 9.33 | 26.0% | 6.1% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 406 | 5.4 | 3.7 | 10.8 | 11.1 | 22.4 | 20.7 | 25.9 | 23.68 | 69.0% | 46.6% |
| singles | 6,765 | 13.7 | 9.9 | 20.6 | 15.0 | 20.0 | 14.0 | 6.7 | 11.76 | 40.8% | 20.8% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 1,637 | 14.1 | 9.0 | 17.3 | 15.5 | 16.7 | 14.2 | 13.1 | 12.95 | 44.0% | 27.3% |
| Hard | 5,017 | 12.4 | 8.8 | 18.2 | 15.0 | 19.1 | 15.8 | 10.5 | 13.38 | 45.5% | 26.4% |
| UNKNOWN | 602 | 12.0 | 6.2 | 13.8 | 17.6 | 17.4 | 20.4 | 12.6 | 15.29 | 50.5% | 33.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 2,178 | 16.7 | 10.7 | 19.5 | 15.8 | 16.4 | 11.3 | 9.7 | 10.83 | 37.4% | 21.0% |
| B | 1,017 | 15.7 | 10.5 | 18.2 | 17.5 | 16.4 | 10.4 | 11.2 | 11.17 | 38.0% | 21.6% |
| C | 1,081 | 12.8 | 9.8 | 20.7 | 13.8 | 16.5 | 15.6 | 10.8 | 12.69 | 42.9% | 26.5% |
| D | 1,293 | 11.0 | 8.0 | 16.4 | 14.9 | 22.0 | 15.8 | 11.8 | 14.88 | 49.6% | 27.6% |
| F | 1,687 | 7.3 | 4.7 | 13.8 | 14.9 | 20.9 | 25.1 | 13.3 | 19.47 | 59.3% | 38.4% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 2,158 | 19.2 | 12.6 | 26.2 | 16.8 | 15.5 | 6.8 | 2.9 | 8.22 | 25.2% | 9.7% |
| B | 1,111 | 13.5 | 9.4 | 21.7 | 15.9 | 20.0 | 12.2 | 7.2 | 11.64 | 39.4% | 19.4% |
| C | 1,398 | 11.1 | 8.5 | 15.8 | 14.2 | 22.8 | 15.4 | 12.1 | 15.17 | 50.4% | 27.5% |
| D | 1,110 | 11.1 | 8.2 | 21.0 | 12.2 | 23.6 | 16.2 | 7.7 | 13.79 | 47.5% | 23.9% |
| F | 1,394 | 7.8 | 6.9 | 12.6 | 13.4 | 22.2 | 25.4 | 11.8 | 18.82 | 59.4% | 37.2% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 2,663 | 16.3 | 9.9 | 18.8 | 16.3 | 16.5 | 11.4 | 10.8 | 11.3 | 38.8% | 22.3% |
| LIMITED | 1,592 | 14.1 | 11.4 | 20.9 | 14.6 | 15.9 | 13.4 | 9.5 | 11.3 | 38.9% | 22.9% |
| POOR | 3,001 | 9.0 | 6.1 | 14.8 | 14.9 | 21.6 | 21.0 | 12.6 | 17.44 | 55.2% | 33.6% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 733 | 31.9 | 25.5 | 35.5 | 4.9 | 1.8 | 0.4 | 0.0 | 4.35 | 2.2% | 0.4% |
| GAME_SPREAD | 682 | 22.4 | 15.8 | 36.2 | 17.4 | 6.9 | 0.7 | 0.4 | 6.17 | 8.1% | 1.2% |
| MATCH_WINNER | 7,171 | 13.3 | 9.5 | 20.0 | 14.8 | 20.2 | 14.4 | 7.8 | 12.16 | 42.4% | 22.2% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 2,166 | 25.6 | 15.4 | 30.9 | 14.7 | 10.7 | 2.2 | 0.5 | 6.09 | 13.4% | 2.7% |
| TOTAL_GAMES | 1,455 | 8.9 | 9.5 | 30.9 | 25.6 | 15.1 | 6.2 | 3.8 | 10.14 | 25.1% | 10.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,504 | 27.1 | 34.4 | 24.5 | 0.5 | 11.9 | 1.1 | 0.4 | 4.3 | 13.4% | 1.5% |
| GAME_SPREAD | 901 | 40.2 | 14.7 | 27.3 | 14.3 | 1.8 | 1.3 | 0.4 | 4.1 | 3.5% | 1.8% |
| TOTAL_GAMES | 1,747 | 4.3 | 5.6 | 37.3 | 38.4 | 9.3 | 2.5 | 2.8 | 10.27 | 14.5% | 5.2% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,504 | 25.1 | 16.2 | 32.1 | 9.4 | 10.5 | 5.7 | 1.0 | 5.95 | 17.2% | 6.7% |
| GAME_SPREAD | 901 | 18.2 | 10.9 | 26.1 | 23.2 | 14.9 | 5.1 | 1.7 | 9.24 | 21.6% | 6.8% |
| TOTAL_GAMES | 1,756 | 5.9 | 8.1 | 31.4 | 29.2 | 16.3 | 5.5 | 3.5 | 10.6 | 25.4% | 9.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 7,256 | 45.6% | 27.1% | 13.38 | 35.1% | 15.7% | 10.56 |
| gen1_elo | 7,256 | 44.8% | 26.2% | 12.97 | 33.8% | 15.4% | 9.98 |
| gen1_sr | 7,256 | 53.6% | 32.0% | 16.51 | 44.1% | 20.6% | 13.25 |
| gen2 | 7,256 | 52.4% | 32.2% | 16.05 | 44.4% | 22.6% | 13.04 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 2,736 | 16.2 | 12.2 | 21.6 | 15.9 | 19.1 | 11.2 | 3.7 | 9.98 | 34.0% | 14.9% |
| STALE | 4,520 | 10.7 | 6.5 | 15.2 | 15.0 | 18.1 | 18.7 | 15.8 | 16.49 | 52.6% | 34.5% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 639 | 14.7 | 9.2 | 23.0 | 15.2 | 17.2 | 17.2 | 3.4 | 10.55 | 37.9% | 20.7% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 14,427 | 639 | 6208 | 7580 | 30.9 | 225.6 | 1400.4 |
| ge_15pp | 6,349 | 242 | 2219 | 3888 | 37.9 | 466.9 | 1380.4 |
| ge_25pp | 3,562 | 132 | 999 | 2431 | 51.6 | 585.5 | 1380.4 |
| lt_10pp | 5,903 | 300 | 3002 | 2601 | 28.3 | 59.8 | 1201.9 |

Current slate `SL-20261005T182127Z-8835c96c`: 918 priced rows, quote age at build {'median': 14.6, 'max': 14.6}, freshness {'AGING': 918}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 197 | 20.8 | 13.2 | 21.8 | 20.8 | 17.3 | 5.6 | 0.5 | 7.39 | 23.4% | 6.1% |
| MARKETS_AGREE | 15 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.09 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 34 | 0.0 | 14.7 | 38.2 | 23.5 | 17.6 | 5.9 | 0.0 | 9.16 | 23.5% | 5.9% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 7,256 | 247 (3.4%) | 13.8% | 0.0% | {"EXTERNAL_STALE": 197, "AGREES_WITH_KALSHI": 34, "ALL_AGREE": 15, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 3,308 | 54 (1.6%) | 14.8% | 0.0% | {"EXTERNAL_STALE": 46, "AGREES_WITH_KALSHI": 8} |
| fair_v1_ge_25pp | 1,968 | 14 (0.7%) | 14.3% | 0.0% | {"EXTERNAL_STALE": 12, "AGREES_WITH_KALSHI": 2} |
| fair_v1_ge_25pp_pregame_clean | 830 | 14 (1.7%) | 14.3% | 0.0% | {"EXTERNAL_STALE": 12, "AGREES_WITH_KALSHI": 2} |
| fair_v1_lt_10pp | 2,834 | 144 (5.1%) | 12.5% | 0.0% | {"EXTERNAL_STALE": 110, "AGREES_WITH_KALSHI": 18, "ALL_AGREE": 15, "EXTERNAL_OUTLIER": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 1,455 | 11.8 | 7.9 | 19.9 | 15.8 | 20.1 | 14.8 | 9.8 | 12.98 | 44.7% | 24.5% |
| 4-10x | 1,004 | 12.2 | 10.8 | 16.8 | 14.6 | 17.3 | 17.9 | 10.3 | 13.57 | 45.5% | 28.2% |
| <2x | 3,894 | 14.0 | 9.3 | 17.8 | 15.5 | 17.9 | 14.0 | 11.5 | 12.81 | 43.4% | 25.5% |
| >=10x | 903 | 9.9 | 4.8 | 13.9 | 14.8 | 19.5 | 23.4 | 13.7 | 18.17 | 56.6% | 37.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 1,923 | 13.6 | 8.8 | 19.8 | 16.0 | 16.7 | 12.6 | 12.6 | 12.22 | 41.9% | 25.2% |
| 300-1000 | 1,686 | 12.7 | 8.8 | 16.5 | 15.4 | 20.6 | 15.8 | 10.2 | 13.79 | 46.6% | 26.0% |
| <300 | 1,955 | 8.1 | 5.6 | 14.0 | 14.3 | 20.9 | 23.6 | 13.5 | 18.88 | 58.0% | 37.1% |
| >=3000 | 1,692 | 17.4 | 11.9 | 20.4 | 15.8 | 15.5 | 10.7 | 8.3 | 10.11 | 34.5% | 19.0% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 247 | 0.5184 | 0.388 | 0.4251 | +0.093 | -0.037 | 0.0093 ± 0.009 |
| ratio 4-10x | 170 | 0.578 | 0.4401 | 0.4882 | +0.090 | -0.048 | 0.0132 ± 0.0114 |
| ratio <2x | 498 | 0.5355 | 0.4111 | 0.4679 | +0.068 | -0.057 | 0.0114 ± 0.0063 |
| ratio >=10x | 172 | 0.551 | 0.3792 | 0.4593 | +0.092 | -0.080 | 0.0138 ± 0.0143 |
| thinner_sample 1000-3000 | 291 | 0.5405 | 0.4206 | 0.4536 | +0.087 | -0.033 | 0.0089 ± 0.0081 |
| thinner_sample 300-1000 | 294 | 0.5562 | 0.4248 | 0.4728 | +0.083 | -0.048 | 0.0067 ± 0.0084 |
| thinner_sample <300 | 358 | 0.5373 | 0.3712 | 0.4553 | +0.082 | -0.084 | 0.0168 ± 0.0093 |
| thinner_sample >=3000 | 144 | 0.5182 | 0.4194 | 0.4583 | +0.060 | -0.039 | 0.0142 ± 0.0094 |
| data_status ADEQUATE | 318 | 0.5287 | 0.4198 | 0.4528 | +0.076 | -0.033 | 0.008 ± 0.007 |
| data_status LIMITED | 223 | 0.5553 | 0.4291 | 0.4933 | +0.062 | -0.064 | 0.0034 ± 0.0099 |
| data_status POOR | 546 | 0.5418 | 0.3872 | 0.4505 | +0.091 | -0.063 | 0.0171 ± 0.007 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 171 | 0.1812 | 0.1823 | -0.0011 ± 0.0011 | 0.5371 | 0.5401 | 0.4967 | 0.4824 | 0.5029 | -0.081 ± 0.0348 | -0.01 (3) |
| 3-5 | 109 | 0.1749 | 0.1756 | -0.0007 ± 0.0033 | 0.5287 | 0.5267 | 0.5175 | 0.4768 | 0.5046 | -0.068 ± 0.0418 | 0.02 (1) |
| 5-10 | 219 | 0.1957 | 0.2 | -0.0043 ± 0.0045 | 0.5763 | 0.5853 | 0.5139 | 0.4397 | 0.4977 | -0.049 ± 0.0305 | -0.0167 (3) |
| 10-15 | 189 | 0.2141 | 0.2106 | +0.0035 ± 0.0083 | 0.6135 | 0.6029 | 0.5167 | 0.3931 | 0.4392 | -0.066 ± 0.0333 | -0.0633 (3) |
| 15-25 | 241 | 0.215 | 0.2102 | +0.0049 ± 0.0116 | 0.6177 | 0.605 | 0.5596 | 0.3629 | 0.4523 | -0.030 ± 0.0291 | -0.02 (4) |
| 25-40 | 128 | 0.2287 | 0.1819 | +0.0469 ± 0.0232 | 0.6466 | 0.5342 | 0.6255 | 0.3129 | 0.3906 | -0.075 ± 0.0349 | -0.01 (1) |
| 40+ | 30 | 0.3354 | 0.1357 | +0.1998 ± 0.0606 | 0.9067 | 0.4279 | 0.7106 | 0.2678 | 0.2667 | -0.167 ± 0.0655 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 561 | 0.1648 | 0.1659 | -0.0011 ± 0.0006 | 0.497 | 0.4994 | 0.5017 | 0.4869 | 0.5312 | -0.017 ± 0.0177 | -0.0188 (8) |
| 3-5 | 361 | 0.169 | 0.1684 | +0.0006 ± 0.0018 | 0.5126 | 0.5061 | 0.4759 | 0.436 | 0.4515 | -0.043 ± 0.0219 | 0.02 (1) |
| 5-10 | 811 | 0.1787 | 0.1785 | +0.0002 ± 0.0022 | 0.5369 | 0.5334 | 0.4763 | 0.4025 | 0.4353 | -0.026 ± 0.0149 | -0.0129 (7) |
| 10-15 | 712 | 0.1826 | 0.1696 | +0.0129 ± 0.0038 | 0.5449 | 0.5018 | 0.4691 | 0.3455 | 0.3539 | -0.053 ± 0.0154 | -0.0633 (3) |
| 15-25 | 916 | 0.1954 | 0.1605 | +0.0349 ± 0.0053 | 0.5793 | 0.4774 | 0.4783 | 0.2799 | 0.2915 | -0.048 ± 0.0131 | -0.017 (10) |
| 25-40 | 898 | 0.211 | 0.0956 | +0.1154 ± 0.0065 | 0.6141 | 0.3122 | 0.5056 | 0.1894 | 0.167 | -0.073 ± 0.01 | -0.01 (1) |
| 40+ | 674 | 0.3737 | 0.0312 | +0.3425 ± 0.0074 | 0.9716 | 0.1435 | 0.6157 | 0.1022 | 0.0341 | -0.097 ± 0.0062 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 112 | 0.1769 | 0.1784 | -0.0014 ± 0.0014 | 0.5269 | 0.5282 | 0.5066 | 0.4917 | 0.5268 | -0.053 ± 0.0398 | -0.01 (1) |
| 3-5 | 84 | 0.1976 | 0.1961 | +0.0015 ± 0.0039 | 0.5718 | 0.5736 | 0.495 | 0.4557 | 0.4524 | -0.082 ± 0.0512 | 0.02 (1) |
| 5-10 | 203 | 0.1854 | 0.1857 | -0.0003 ± 0.0046 | 0.5526 | 0.5519 | 0.5691 | 0.4938 | 0.5271 | -0.071 ± 0.0312 | -0.01 (4) |
| 10-15 | 178 | 0.2238 | 0.2132 | +0.0106 ± 0.0088 | 0.6368 | 0.6133 | 0.5806 | 0.4562 | 0.4831 | -0.083 ± 0.0355 | -0.0667 (3) |
| 15-25 | 275 | 0.2237 | 0.1992 | +0.0245 ± 0.0108 | 0.6341 | 0.5765 | 0.5832 | 0.3857 | 0.4291 | -0.087 ± 0.028 | -0.0167 (3) |
| 25-40 | 162 | 0.2627 | 0.1986 | +0.0641 ± 0.0217 | 0.7293 | 0.5775 | 0.6497 | 0.339 | 0.3889 | -0.097 ± 0.0366 | -0.025 (2) |
| 40+ | 73 | 0.381 | 0.1718 | +0.2092 ± 0.0492 | 1.0454 | 0.5148 | 0.7445 | 0.2517 | 0.3014 | -0.073 ± 0.0465 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 448 | 0.1531 | 0.1547 | -0.0015 ± 0.0006 | 0.4667 | 0.4699 | 0.5265 | 0.5118 | 0.5513 | -0.009 ± 0.0188 | -0.0217 (6) |
| 3-5 | 303 | 0.1687 | 0.1658 | +0.0030 ± 0.0019 | 0.5033 | 0.4995 | 0.5249 | 0.4853 | 0.4686 | -0.068 ± 0.0239 | 0.02 (1) |
| 5-10 | 738 | 0.1699 | 0.1712 | -0.0012 ± 0.0023 | 0.514 | 0.5132 | 0.5172 | 0.4422 | 0.4824 | -0.016 ± 0.0154 | -0.01 (5) |
| 10-15 | 638 | 0.1876 | 0.1753 | +0.0122 ± 0.0041 | 0.5577 | 0.5166 | 0.5087 | 0.3849 | 0.4044 | -0.044 ± 0.0168 | -0.0575 (4) |
| 15-25 | 1006 | 0.2029 | 0.159 | +0.0439 ± 0.005 | 0.5943 | 0.4754 | 0.5126 | 0.3152 | 0.3072 | -0.076 ± 0.0127 | -0.0143 (7) |
| 25-40 | 939 | 0.2291 | 0.1176 | +0.1116 ± 0.0071 | 0.6607 | 0.3675 | 0.5384 | 0.2216 | 0.2055 | -0.070 ± 0.0114 | -0.015 (6) |
| 40+ | 861 | 0.4117 | 0.0529 | +0.3588 ± 0.009 | 1.0753 | 0.2024 | 0.66 | 0.1215 | 0.0697 | -0.085 ± 0.0074 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 175 | 0.1902 | 0.1921 | -0.0019 ± 0.0012 | 0.5568 | 0.5622 | 0.5212 | 0.5066 | 0.5371 | -0.055 ± 0.0328 | -0.01 (5) |
| 3-5 | 116 | 0.1681 | 0.1653 | +0.0028 ± 0.003 | 0.5078 | 0.5012 | 0.5028 | 0.4633 | 0.4483 | -0.122 ± 0.0401 | -- (0) |
| 5-10 | 218 | 0.1971 | 0.1955 | +0.0016 ± 0.0045 | 0.5831 | 0.5736 | 0.4984 | 0.4254 | 0.445 | -0.077 ± 0.0301 | -0.01 (3) |
| 10-15 | 183 | 0.2164 | 0.2137 | +0.0027 ± 0.0086 | 0.6217 | 0.6133 | 0.5423 | 0.4188 | 0.4754 | -0.067 ± 0.0343 | -0.044 (5) |
| 15-25 | 237 | 0.2086 | 0.2017 | +0.0070 ± 0.0113 | 0.607 | 0.5836 | 0.5708 | 0.376 | 0.4557 | -0.043 ± 0.0281 | -0.03 (1) |
| 25-40 | 133 | 0.2238 | 0.1966 | +0.0272 ± 0.0234 | 0.6395 | 0.5699 | 0.6252 | 0.3129 | 0.4211 | -0.051 ± 0.0353 | 0.0 (1) |
| 40+ | 25 | 0.3648 | 0.1373 | +0.2275 ± 0.0667 | 0.9712 | 0.4311 | 0.711 | 0.2606 | 0.24 | -0.185 ± 0.0761 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 572 | 0.1716 | 0.1718 | -0.0002 ± 0.0006 | 0.5142 | 0.5148 | 0.5038 | 0.4892 | 0.4983 | -0.050 ± 0.0172 | -0.0162 (13) |
| 3-5 | 388 | 0.1668 | 0.1628 | +0.0040 ± 0.0016 | 0.5047 | 0.4943 | 0.4897 | 0.4503 | 0.4253 | -0.086 ± 0.0208 | -0.01 (2) |
| 5-10 | 825 | 0.183 | 0.1757 | +0.0074 ± 0.0022 | 0.5481 | 0.5219 | 0.4626 | 0.389 | 0.3758 | -0.068 ± 0.0147 | -0.01 (3) |
| 10-15 | 668 | 0.1879 | 0.1773 | +0.0107 ± 0.0041 | 0.5575 | 0.5249 | 0.4812 | 0.3576 | 0.3772 | -0.044 ± 0.0163 | -0.03 (9) |
| 15-25 | 978 | 0.1843 | 0.1482 | +0.0361 ± 0.0049 | 0.5565 | 0.4472 | 0.4844 | 0.2846 | 0.2945 | -0.049 ± 0.0121 | -0.03 (2) |
| 25-40 | 871 | 0.2101 | 0.0953 | +0.1148 ± 0.0067 | 0.6131 | 0.3089 | 0.5008 | 0.1811 | 0.163 | -0.071 ± 0.01 | 0.0 (1) |
| 40+ | 631 | 0.3913 | 0.0327 | +0.3586 ± 0.0081 | 1.02 | 0.1478 | 0.6251 | 0.1025 | 0.0317 | -0.099 ± 0.0066 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 449 | 0.2027 | 0.2026 | +0.0000 ± 0.0007 | 0.587 | 0.5874 | 0.4976 | 0.483 | 0.4855 | -0.041 ± 0.0213 | -0.0226 (46) |
| 3-5 | 332 | 0.1952 | 0.194 | +0.0013 ± 0.0019 | 0.572 | 0.566 | 0.4681 | 0.4283 | 0.4367 | -0.040 ± 0.024 | -0.0059 (32) |
| 5-10 | 683 | 0.1875 | 0.1828 | +0.0047 ± 0.0025 | 0.5584 | 0.5454 | 0.4592 | 0.3859 | 0.3909 | -0.040 ± 0.0164 | -0.005 (72) |
| 10-15 | 461 | 0.2024 | 0.1908 | +0.0117 ± 0.0051 | 0.5941 | 0.5617 | 0.458 | 0.3347 | 0.3492 | -0.035 ± 0.0202 | 0.0016 (63) |
| 15-25 | 619 | 0.2319 | 0.2093 | +0.0225 ± 0.0072 | 0.657 | 0.6041 | 0.5272 | 0.334 | 0.3732 | -0.023 ± 0.0183 | -0.0216 (58) |
| 25-40 | 310 | 0.2629 | 0.1652 | +0.0977 ± 0.0144 | 0.7287 | 0.4984 | 0.5719 | 0.2606 | 0.2581 | -0.068 ± 0.0227 | -0.0216 (25) |
| 40+ | 98 | 0.424 | 0.155 | +0.2689 ± 0.0426 | 1.187 | 0.48 | 0.7319 | 0.2239 | 0.2347 | -0.063 ± 0.0412 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 843 | 0.1922 | 0.1916 | +0.0005 ± 0.0005 | 0.5623 | 0.5608 | 0.4913 | 0.4768 | 0.4674 | -0.050 ± 0.0151 | -0.0155 (82) |
| 3-5 | 609 | 0.1949 | 0.193 | +0.0018 ± 0.0014 | 0.5695 | 0.5625 | 0.4713 | 0.4315 | 0.4302 | -0.045 ± 0.0178 | -0.018 (54) |
| 5-10 | 1256 | 0.1852 | 0.1788 | +0.0064 ± 0.0018 | 0.5526 | 0.5331 | 0.4435 | 0.3695 | 0.3662 | -0.044 ± 0.012 | -0.0089 (122) |
| 10-15 | 940 | 0.1953 | 0.1819 | +0.0134 ± 0.0035 | 0.5766 | 0.5386 | 0.4475 | 0.3242 | 0.3319 | -0.036 ± 0.0138 | -0.0053 (99) |
| 15-25 | 1306 | 0.2187 | 0.1851 | +0.0336 ± 0.0047 | 0.6324 | 0.5435 | 0.5015 | 0.3061 | 0.3178 | -0.038 ± 0.0119 | -0.0255 (106) |
| 25-40 | 916 | 0.2407 | 0.1246 | +0.1161 ± 0.0074 | 0.6815 | 0.3916 | 0.5265 | 0.2114 | 0.1856 | -0.073 ± 0.0115 | -0.0206 (47) |
| 40+ | 520 | 0.3873 | 0.0779 | +0.3094 ± 0.0134 | 1.056 | 0.2643 | 0.6504 | 0.1345 | 0.1038 | -0.073 ± 0.0125 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 1087 | 1.126 ± 0.087 | 1.244 | 0.1701 | 0.1818 | 0.2066 | 0.195 |
| gen2 | 1087 | 0.918 ± 0.077 | 1.164 | 0.1858 | 0.1815 | 0.2261 | 0.1947 |
| gen1_elo | 1087 | 1.117 ± 0.086 | 1.197 | 0.175 | 0.1822 | 0.2058 | 0.1949 |
| gen1_sr | 1087 | 1.139 ± 0.1 | 1.222 | 0.1425 | 0.1835 | 0.2215 | 0.1945 |
| gen1_ledger | 2952 | 0.908 ± 0.05 | 1.07 | 0.1622 | 0.2012 | 0.2181 | 0.1911 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 6,349)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,034 | 32.0% |
| STALE_QUOTE | market_freshness | 1,847 | 29.1% |
| BOOK_QUALITY | execution | 682 | 10.7% |
| POOR_DATA | data | 496 | 7.8% |
| LIMITED_DATA | data | 341 | 5.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 324 | 5.1% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 290 | 4.6% |
| IN_PLAY_QUOTE | market_freshness/coverage | 191 | 3.0% |
| IDENTITY_AMBIGUOUS | mapping | 136 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 8 | 0.1% |

Cause class: coverage 32.0%, market_freshness 29.1%, data 13.2%, execution 10.7%, market_freshness/coverage 8.1%, model_calibration_or_unknown 4.6%, mapping 2.1%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.8%, START_UNVERIFIABLE 94.9%, LOW_DATA_QUALITY 65.6%, STALE_KALSHI_QUOTE 61.2%, THIN_PLAYER_HISTORY 54.9%, STALE_PLAYER_DATA 53.5%, MODEL_INTERNAL_DISAGREEMENT 35.4%, ASYMMETRIC_SAMPLE_SIZE 29.8%, WIDE_SPREAD 19.5%, MODEL_HIGH_UNCERTAINTY 14.5%, PLAYER_IDENTITY_RISK 11.1%, LEVEL_TRANSFER_RISK 8.2%, EVENT_MAPPING_RISK 6.5%, LOW_DISPLAYED_LIQUIDITY 6.0%, MODEL_CALIBRATION_OUTLIER 1.9%, UNKNOWN 0.7%, EXTERNAL_MARKET_REJECTION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 34.4%, POST_SETTLEMENT_OBSERVATION 32.0%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.9%

### >= ge_25 pp (N = 3,562)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,609 | 45.2% |
| STALE_QUOTE | market_freshness | 845 | 23.7% |
| BOOK_QUALITY | execution | 339 | 9.5% |
| POOR_DATA | data | 217 | 6.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 172 | 4.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 112 | 3.1% |
| LIMITED_DATA | data | 98 | 2.8% |
| IDENTITY_AMBIGUOUS | mapping | 95 | 2.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 73 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 2 | 0.1% |

Cause class: coverage 45.2%, market_freshness 23.7%, execution 9.5%, data 8.8%, market_freshness/coverage 8.0%, mapping 2.7%, model_calibration_or_unknown 2.1%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 97.2%, LOW_DATA_QUALITY 69.0%, STALE_KALSHI_QUOTE 68.2%, THIN_PLAYER_HISTORY 57.3%, STALE_PLAYER_DATA 50.8%, MODEL_INTERNAL_DISAGREEMENT 37.2%, ASYMMETRIC_SAMPLE_SIZE 32.7%, WIDE_SPREAD 17.9%, MODEL_HIGH_UNCERTAINTY 15.6%, PLAYER_IDENTITY_RISK 13.9%, LEVEL_TRANSFER_RISK 7.9%, EVENT_MAPPING_RISK 7.5%, LOW_DISPLAYED_LIQUIDITY 6.5%, MODEL_CALIBRATION_OUTLIER 2.8%, UNKNOWN 0.2%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 47.6%, POST_SETTLEMENT_OBSERVATION 45.2%, POSSIBLE_IN_PLAY_QUOTE 5.5%, CONFIRMED_IN_PLAY_QUOTE 1.0%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 2987, "IDENTITY_AMBIGUOUS": 575}; ticker orientation: {"VERIFIED": 3562}.

Checks: discipline:AMBIGUOUS 189, discipline:PASS 3373, identity_confidence:AMBIGUOUS 495, identity_confidence:PASS 3067, level_mapping:NA 201, level_mapping:PASS 3361, market_pair:AMBIGUOUS 110, market_pair:NA 92, market_pair:PASS 3360, model_complement:NA 61, model_complement:PASS 3501, namesake:PASS 3562, physical_match_id:NA 1594, physical_match_id:PASS 1968, player_ids:PASS 3562, same_pair_other_event:PASS 3562, ticker_orientation:PASS 3562

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 599 | 3.8% | 3.9% | 0.7% | {"market_freshness": 20, "execution": 3} | 6.18 | 0.1791 / 0.1823 (49) | 34.4% | 0.3% | 3.7% | 1.8% |
| CHALLENGER | 2,569 | 20.4% | 8.3% | 14.7% | {"coverage": 306, "market_freshness": 104, "market_freshness/coverage": 57, "data": 28, "model_calibration_or_unknown": 23, "execution": 5, "model_calibration": 1} | 7.68 | 0.2196 / 0.2044 (688) | 56.3% | 5.9% | 1.3% | 24.8% |
| DOUBLES | 406 | 46.6% | 46.3% | 5.3% | {"market_freshness": 106, "execution": 33, "mapping": 31, "market_freshness/coverage": 12, "coverage": 7} | 23.62 | 0.3208 / 0.2301 (163) | 57.6% | 0.0% | 100.0% | 9.6% |
| ITF_MEN | 4,316 | 26.2% | 15.9% | 31.8% | {"coverage": 572, "market_freshness": 214, "execution": 156, "data": 99, "market_freshness/coverage": 78, "mapping": 12, "model_calibration_or_unknown": 1} | 10.4 | 0.2148 / 0.1879 (1384) | 53.3% | 52.5% | 6.7% | 30.0% |
| ITF_WOMEN | 5,059 | 30.2% | 20.2% | 42.9% | {"coverage": 707, "market_freshness": 352, "data": 168, "execution": 133, "market_freshness/coverage": 97, "mapping": 49, "model_calibration_or_unknown": 21} | 13.19 | 0.203 / 0.185 (1363) | 56.4% | 60.5% | 9.9% | 29.4% |
| OTHER | 149 | 8.1% | 7.3% | 0.3% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 834 | 9.3% | 8.1% | 2.2% | {"market_freshness": 34, "model_calibration_or_unknown": 14, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "model_calibration": 1, "mapping": 1} | 8.48 | 0.2006 / 0.1964 (129) | 38.7% | 2.5% | 1.4% | 3.6% |
| WTA125 | 495 | 15.6% | 8.5% | 2.2% | {"market_freshness/coverage": 30, "market_freshness": 13, "model_calibration_or_unknown": 12, "coverage": 12, "data": 9, "mapping": 1} | 10.06 | 0.2273 / 0.204 (221) | 34.9% | 7.7% | 2.8% | 17.2% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 3 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 4 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 5 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 6 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 7 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 8 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 9 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 10 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 11 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 12 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 14 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 15 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 16 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 17 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 18 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 19 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 20 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 110 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 21 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 22 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 23 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 153 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 24 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 25 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 22 min (AGING); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 26 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 27 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 28 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 230 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 29 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 687 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 30 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 31 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 32 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 33 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 66 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 34 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 35 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 36 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 37 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.9h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 671 min (STALE); no external reference |
| 39 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 732 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 40 | `KXWTAMATCH-26OCT01YASCHW-CHW` | WTA | fair_v1 | 73% / 2% | +70 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 51 min (STALE); no external reference |
| 41 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 42 | `KXATPCHALLENGERMATCH-26OCT05CASMUN-CAS` | CHALLENGER | fair_v1 | 83% / 14% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 192 min (STALE); data POOR (grade D, thinner serve sample 814.0, ratio 3.76); no external reference |
| 43 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 44 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |
| 46 | `KXITFWMATCH-26SEP30KOKUEM-KOK` | ITF_WOMEN | fair_v1 | 79% / 10% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 776 min (STALE); data LIMITED (grade C, thinner serve sample 824.0, ratio 2.35); no external reference |
| 47 | `KXITFMATCH-26SEP20WILRAH-RAH` | ITF_MEN | gen1_ledger | 72% / 4% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade B, thinner serve sample 2782.0, ratio 1.84); no external reference |
| 48 | `KXITFMATCH-26SEP26NAGTHO-NAG` | ITF_MEN | gen1_ledger | 76% / 7% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 89 min (STALE); data LIMITED (grade C, thinner serve sample 1323.0, ratio 4.45); no external reference |
| 49 | `KXITFWMATCH-26SEP26PERPRE-PER` | ITF_WOMEN | gen1_ledger | 78% / 10% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 102 min (STALE); data POOR (grade D, thinner serve sample 1020.0, ratio 2.77); no external reference |
| 50 | `KXITFMATCH-26SEP22YILAGA-AGA` | ITF_MEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 203 min (STALE); data LIMITED (grade B, thinner serve sample 2786.0, ratio 2.08); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9717, "by_level_share_of_ge_25pp": {"ATP": 0.0065, "CHALLENGER": 0.1471, "DOUBLES": 0.0531, "ITF_MEN": 0.3178, "ITF_WOMEN": 0.4287, "OTHER": 0.0034, "WTA": 0.0219, "WTA125": 0.0216}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.6825, "share_primary_cause_market_settled_or_in_play": 0.5314, "share_primary_cause_stale_quote_only": 0.2372}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 3562, "identity_ambiguous_share": 0.1614, "ticker_orientation": {"VERIFIED": 3562}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 1968, "with_external": 14, "coverage": 0.0071, "external_status": {"EXTERNAL_STALE": 12, "AGREES_WITH_KALSHI": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 12, "MODEL_LONE_OUTLIER": 2}, "share_external_agrees_with_kalshi": 0.1429, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 830, "with_external": 14, "coverage": 0.0169, "external_status": {"EXTERNAL_STALE": 12, "AGREES_WITH_KALSHI": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 12, "MODEL_LONE_OUTLIER": 2}, "share_external_agrees_with_kalshi": 0.1429, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 688.0, "median_sample_ratio": 2.31, "median_min_matches": 22.0, "median_max_days_since_last": 189.0, "share_severe_asymmetry": 0.1816, "data_status": {"POOR": 1803, "LIMITED": 1041, "ADEQUATE": 718}, "comparison_lt_10pp": {"median_thinner_serve_points": 1886.0, "median_sample_ratio": 1.74, "median_min_matches": 78.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 247, "model_minus_observed": 0.0933, "kalshi_minus_observed": -0.0371, "brier_diff_model_minus_kalshi": 0.0093}, "4-10x": {"n": 170, "model_minus_observed": 0.0898, "kalshi_minus_observed": -0.0482, "brier_diff_model_minus_kalshi": 0.0132}, "<2x": {"n": 498, "model_minus_observed": 0.0677, "kalshi_minus_observed": -0.0568, "brier_diff_model_minus_kalshi": 0.0114}, ">=10x": {"n": 172, "model_minus_observed": 0.0917, "kalshi_minus_observed": -0.0801, "brier_diff_model_minus_kalshi": 0.0138}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 1087, "model": {"intercept": -0.615, "slope": 0.918, "slope_se": 0.077}, "kalshi_mid_same_rows": {"intercept": 0.228, "slope": 1.164, "slope_se": 0.085}, "mean_extremity_model": 0.1858, "mean_extremity_kalshi": 0.1815, "model_brier": 0.2261, "kalshi_brier": 0.1947, "brier_diff_model_minus_kalshi": 0.0315, "brier_diff_se": 0.0058, "model_logloss": 0.6453, "kalshi_logloss": 0.5687}, "fair_v1": {"n": 1087, "model": {"intercept": -0.404, "slope": 1.126, "slope_se": 0.087}, "kalshi_mid_same_rows": {"intercept": 0.377, "slope": 1.244, "slope_se": 0.089}, "mean_extremity_model": 0.1701, "mean_extremity_kalshi": 0.1818, "model_brier": 0.2066, "kalshi_brier": 0.195, "brier_diff_model_minus_kalshi": 0.0116, "brier_diff_se": 0.0046, "model_logloss": 0.5984, "kalshi_logloss": 0.5694}, "gen1_elo": {"n": 1087, "model": {"intercept": -0.44, "slope": 1.117, "slope_se": 0.086}, "kalshi_mid_same_rows": {"intercept": 0.309, "slope": 1.197, "slope_se": 0.086}, "mean_extremity_model": 0.175, "mean_extremity_kalshi": 0.1822, "model_brier": 0.2058, "kalshi_brier": 0.1949, "brier_diff_model_minus_kalshi": 0.0108, "brier_diff_se": 0.0045, "model_logloss": 0.5984, "kalshi_logloss": 0.5692}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2712, "share_ge_15": 0.4559, "median_abs_gap": 13.38, "n": 7256}, "gen1_elo": {"share_ge_25": 0.2619, "share_ge_15": 0.4479, "median_abs_gap": 12.97, "n": 7256}, "gen1_sr": {"share_ge_25": 0.3199, "share_ge_15": 0.5364, "median_abs_gap": 16.51, "n": 7256}, "gen2": {"share_ge_25": 0.3224, "share_ge_15": 0.5245, "median_abs_gap": 16.05, "n": 7256}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1567, "share_ge_15": 0.3508, "median_abs_gap": 10.56, "n": 5297}, "gen1_elo": {"share_ge_25": 0.154, "share_ge_15": 0.3377, "median_abs_gap": 9.98, "n": 5297}, "gen1_sr": {"share_ge_25": 0.2063, "share_ge_15": 0.4408, "median_abs_gap": 13.25, "n": 5297}, "gen2": {"share_ge_25": 0.2262, "share_ge_15": 0.4442, "median_abs_gap": 13.04, "n": 5297}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 6.18, "share_ge_25_all": 0.0384, "share_ge_25_pregame_clean": 0.0391}, "WTA": {"median_abs_gap_pregame_clean": 8.48, "share_ge_25_all": 0.0935, "share_ge_25_pregame_clean": 0.0808}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2211, "share_within_10pp_all": 0.4092, "share_within_10pp_pregame_clean": 0.4838, "corr_model_vs_mid_pregame_clean": 0.828}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 171, "model_brier": 0.1812, "kalshi_brier": 0.1823, "brier_diff_model_minus_kalshi": -0.0011}, "10-15": {"n_settled": 189, "model_brier": 0.2141, "kalshi_brier": 0.2106, "brier_diff_model_minus_kalshi": 0.0035}, "15-25": {"n_settled": 241, "model_brier": 0.215, "kalshi_brier": 0.2102, "brier_diff_model_minus_kalshi": 0.0049}, "25-40": {"n_settled": 128, "model_brier": 0.2287, "kalshi_brier": 0.1819, "brier_diff_model_minus_kalshi": 0.0469}, "3-5": {"n_settled": 109, "model_brier": 0.1749, "kalshi_brier": 0.1756, "brier_diff_model_minus_kalshi": -0.0007}, "40+": {"n_settled": 30, "model_brier": 0.3354, "kalshi_brier": 0.1357, "brier_diff_model_minus_kalshi": 0.1998}, "5-10": {"n_settled": 219, "model_brier": 0.1957, "kalshi_brier": 0.2, "brier_diff_model_minus_kalshi": -0.0043}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%)
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap).
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 163, "model_brier": 0.3208, "kalshi_brier": 0.2301, "brier_diff_model_minus_kalshi": 0.0907, "brier_diff_se": 0.0257, "corr_model_outcome": -0.1018, "corr_kalshi_outcome": 0.3278}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
