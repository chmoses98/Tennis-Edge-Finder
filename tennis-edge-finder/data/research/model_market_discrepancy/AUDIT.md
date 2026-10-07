# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-07T01:47Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 20,685): 0-3 13.4%, 3-5 9.5%, 5-10 19.6%, 10-15 15.3%, 15-25 18.9%, 25-40 14.6%, 40+ 8.7%; median gap 12.29 pp.
* **Where the extremes live**: 97.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.5%, Challenger 13.3%, doubles 4.5%). Main tour: ATP 2.1% and WTA 8.5% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 4,807): MARKET_ALREADY_SETTLED_WHEN_PRICED 40.6%, STALE_QUOTE 19.3%, BOOK_QUALITY 16.7%, POOR_DATA 8.0%, POSSIBLY_IN_PLAY_QUOTE 4.6%, LIMITED_DATA 3.3%, IN_PLAY_QUOTE 2.9%, IDENTITY_AMBIGUOUS 2.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.0%. By class: coverage 40.6%, market_freshness 19.3%, execution 16.7%, data 11.3%, market_freshness/coverage 7.4%, mapping 2.5%, model_calibration_or_unknown 2.1%, model_calibration 0.0%.
* **Stale / settled / in-play**: 59.3% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 48.1% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 4,807 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 16.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 0.7%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 7.2% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 593.0 points vs 1774.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.145, Gen-2 0.932, Gen-1 ledger 0.93 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 173 model 0.2109 vs Kalshi 0.1981; n 39 model 0.3105 vs Kalshi 0.1436.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%). Not implemented here.

## 1. Observations

* 76,410 model-market comparisons (128,691 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 29,886 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-07T01:41:17.437962+00:00'], shadow board 21,320 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-07T01:41:20.624336+00:00'], Model 4 7,435 rows, 9,517 settled tickers, 2,301 tickers with an external scan.
* By model: {"gen1_ledger": 18929, "gen1_elo": 10715, "fair_v1": 10715, "gen2": 10715, "gen1_sr": 10715, "model4_fundamental": 7315, "model4_conditioned": 7306}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 20,685 | 13.4 | 9.5 | 19.6 | 15.3 | 18.9 | 14.6 | 8.7 | 12.29 | 42.1% | 23.2% |
| MW fair_v1 | 10,715 | 12.8 | 8.9 | 18.3 | 15.8 | 18.4 | 15.4 | 10.4 | 13.1 | 44.2% | 25.8% |
| MW gen1_elo | 10,715 | 12.7 | 8.7 | 19.7 | 14.8 | 19.3 | 15.0 | 9.8 | 12.73 | 44.1% | 24.8% |
| MW gen1_ledger | 9,970 | 14.1 | 10.2 | 21.1 | 14.8 | 19.3 | 13.7 | 6.8 | 11.38 | 39.8% | 20.5% |
| MW gen1_sr | 10,715 | 9.7 | 7.7 | 16.0 | 14.2 | 21.8 | 18.5 | 12.1 | 15.91 | 52.4% | 30.6% |
| MW gen2 | 10,715 | 11.3 | 7.0 | 15.9 | 14.5 | 19.9 | 17.6 | 13.7 | 15.5 | 51.1% | 31.2% |
| all families model4_conditioned | 7,306 | 21.7 | 20.3 | 34.0 | 16.7 | 5.4 | 1.0 | 0.9 | 5.84 | 7.3% | 1.9% |
| all families model4_fundamental | 7,315 | 16.4 | 13.1 | 34.1 | 20.3 | 11.2 | 3.4 | 1.3 | 7.83 | 16.0% | 4.8% |

Configurable thresholds (primary): >=5pp 77.1%, >=10pp 57.4%, >=15pp 42.1%, >=20pp 31.7%, >=25pp 23.2%, >=30pp 17.0%, >=40pp 8.7%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.59pp; >=10pp 46.0%, >=25pp 18.7%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 734 | 25.1 | 17.6 | 25.2 | 16.9 | 12.1 | 1.6 | 1.5 | 5.93 | 15.3% | 3.1% |
| CHALLENGER | 2,005 | 14.6 | 11.1 | 18.2 | 16.1 | 13.4 | 13.4 | 13.2 | 12.06 | 40.0% | 26.6% |
| ITF_MEN | 3,012 | 10.4 | 8.3 | 18.4 | 14.5 | 19.6 | 15.4 | 13.4 | 14.24 | 48.3% | 28.8% |
| ITF_WOMEN | 4,177 | 10.4 | 6.7 | 16.0 | 15.7 | 21.5 | 19.8 | 9.9 | 15.51 | 51.2% | 29.7% |
| WTA | 506 | 22.5 | 9.9 | 24.5 | 16.2 | 18.2 | 6.5 | 2.2 | 8.38 | 26.9% | 8.7% |
| WTA125 | 281 | 13.2 | 6.4 | 20.6 | 25.6 | 14.2 | 17.1 | 2.9 | 11.47 | 34.2% | 19.9% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 734 | 20.4 | 15.4 | 25.8 | 17.9 | 15.9 | 2.9 | 1.8 | 6.9 | 20.6% | 4.6% |
| CHALLENGER | 2,005 | 14.7 | 7.0 | 17.6 | 13.7 | 18.8 | 14.6 | 13.7 | 13.57 | 47.0% | 28.2% |
| ITF_MEN | 3,012 | 9.9 | 7.0 | 16.1 | 14.9 | 20.0 | 18.0 | 14.1 | 15.69 | 52.1% | 32.1% |
| ITF_WOMEN | 4,177 | 8.4 | 6.2 | 13.2 | 13.3 | 20.8 | 21.2 | 16.9 | 18.87 | 58.9% | 38.1% |
| WTA | 506 | 20.9 | 4.9 | 16.8 | 16.0 | 21.9 | 17.2 | 2.2 | 13.18 | 41.3% | 19.4% |
| WTA125 | 281 | 5.3 | 1.8 | 16.4 | 23.8 | 20.3 | 19.6 | 12.8 | 16.74 | 52.7% | 32.4% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 734 | 24.7 | 12.1 | 30.5 | 16.6 | 10.3 | 4.1 | 1.6 | 7.02 | 16.1% | 5.7% |
| CHALLENGER | 2,005 | 15.8 | 10.9 | 20.1 | 14.0 | 13.7 | 12.3 | 13.2 | 10.71 | 39.1% | 25.5% |
| ITF_MEN | 3,012 | 9.4 | 8.4 | 18.1 | 13.9 | 20.9 | 15.8 | 13.4 | 15.03 | 50.1% | 29.2% |
| ITF_WOMEN | 4,177 | 9.7 | 6.6 | 16.4 | 15.3 | 23.7 | 19.6 | 8.6 | 16.01 | 51.9% | 28.2% |
| WTA | 506 | 23.3 | 12.8 | 34.6 | 14.2 | 9.9 | 3.8 | 1.4 | 7.0 | 15.0% | 5.1% |
| WTA125 | 281 | 21.4 | 11.0 | 27.1 | 18.1 | 16.0 | 5.7 | 0.7 | 7.99 | 22.4% | 6.4% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 386 | 28.8 | 20.5 | 37.6 | 11.9 | 1.3 | 0.0 | 0.0 | 5.17 | 1.3% | 0.0% |
| CHALLENGER | 1,325 | 22.6 | 15.8 | 26.9 | 14.4 | 12.4 | 5.7 | 2.2 | 6.81 | 20.3% | 7.9% |
| DOUBLES | 494 | 4.5 | 3.0 | 13.8 | 10.9 | 23.9 | 20.6 | 23.3 | 22.7 | 67.8% | 43.9% |
| ITF_MEN | 3,136 | 13.3 | 8.4 | 19.1 | 15.6 | 20.6 | 13.9 | 9.0 | 12.55 | 43.6% | 23.0% |
| ITF_WOMEN | 3,603 | 10.6 | 9.0 | 18.8 | 14.1 | 22.7 | 18.4 | 6.4 | 13.95 | 47.6% | 24.9% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 422 | 19.0 | 11.1 | 25.8 | 19.7 | 16.1 | 7.6 | 0.7 | 8.75 | 24.4% | 8.3% |
| WTA125 | 455 | 14.9 | 12.5 | 22.0 | 19.6 | 18.2 | 9.7 | 3.1 | 10.11 | 31.0% | 12.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 730 | 25.1 | 17.4 | 25.2 | 17.0 | 12.2 | 1.6 | 1.5 | 5.93 | 15.3% | 3.1% |
| CHALLENGER | 1,420 | 19.0 | 14.2 | 23.4 | 18.7 | 14.4 | 7.2 | 3.0 | 8.47 | 24.6% | 10.2% |
| ITF_MEN | 2,169 | 12.6 | 10.7 | 22.0 | 16.2 | 19.5 | 12.7 | 6.3 | 11.21 | 38.5% | 19.0% |
| ITF_WOMEN | 3,016 | 12.9 | 8.4 | 18.8 | 17.9 | 22.9 | 15.8 | 3.3 | 12.78 | 42.0% | 19.1% |
| WTA | 504 | 22.6 | 9.9 | 24.6 | 16.1 | 18.2 | 6.3 | 2.2 | 8.36 | 26.8% | 8.5% |
| WTA125 | 271 | 13.7 | 6.6 | 20.3 | 26.2 | 14.4 | 17.0 | 1.9 | 11.47 | 33.2% | 18.8% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 730 | 20.3 | 15.3 | 25.9 | 17.8 | 16.0 | 2.9 | 1.8 | 6.9 | 20.7% | 4.7% |
| CHALLENGER | 1,420 | 19.3 | 9.2 | 22.2 | 16.6 | 19.6 | 10.2 | 2.9 | 9.92 | 32.7% | 13.1% |
| ITF_MEN | 2,169 | 12.0 | 8.5 | 18.7 | 17.0 | 21.0 | 15.5 | 7.3 | 12.95 | 43.9% | 22.9% |
| ITF_WOMEN | 3,016 | 9.9 | 7.4 | 15.0 | 14.4 | 22.8 | 19.8 | 10.8 | 16.26 | 53.3% | 30.6% |
| WTA | 504 | 21.0 | 5.0 | 16.9 | 16.1 | 21.8 | 17.1 | 2.2 | 13.18 | 41.1% | 19.2% |
| WTA125 | 271 | 5.5 | 1.9 | 16.6 | 24.7 | 19.6 | 20.3 | 11.4 | 15.85 | 51.3% | 31.7% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 373 | 28.9 | 20.6 | 38.1 | 12.1 | 0.3 | 0.0 | 0.0 | 5.11 | 0.3% | 0.0% |
| CHALLENGER | 1,111 | 24.7 | 18.0 | 29.3 | 14.0 | 11.7 | 2.2 | 0.1 | 6.17 | 14.0% | 2.2% |
| DOUBLES | 451 | 4.4 | 2.9 | 14.2 | 10.9 | 24.2 | 20.8 | 22.6 | 22.7 | 67.6% | 43.5% |
| ITF_MEN | 2,491 | 15.2 | 9.3 | 21.4 | 16.7 | 20.5 | 11.6 | 5.2 | 11.27 | 37.3% | 16.8% |
| ITF_WOMEN | 2,890 | 11.9 | 10.1 | 20.8 | 15.0 | 23.0 | 16.6 | 2.6 | 12.04 | 42.2% | 19.2% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 392 | 19.4 | 11.7 | 26.5 | 19.9 | 16.6 | 5.9 | 0.0 | 8.57 | 22.4% | 5.9% |
| WTA125 | 373 | 17.2 | 13.9 | 24.7 | 22.5 | 16.4 | 5.1 | 0.3 | 8.91 | 21.7% | 5.4% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 494 | 4.5 | 3.0 | 13.8 | 10.9 | 23.9 | 20.6 | 23.3 | 22.7 | 67.8% | 43.9% |
| singles | 9,476 | 14.6 | 10.5 | 21.5 | 15.0 | 19.0 | 13.3 | 6.0 | 10.95 | 38.3% | 19.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 2,523 | 13.2 | 9.6 | 19.7 | 15.4 | 16.1 | 14.8 | 11.3 | 12.46 | 42.2% | 26.1% |
| Hard | 7,246 | 12.7 | 8.8 | 18.3 | 15.7 | 19.3 | 15.2 | 10.0 | 13.24 | 44.5% | 25.2% |
| UNKNOWN | 946 | 12.4 | 7.8 | 14.4 | 18.0 | 18.2 | 18.4 | 10.9 | 14.16 | 47.5% | 29.3% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,107 | 17.7 | 11.3 | 20.4 | 16.9 | 14.8 | 10.4 | 8.5 | 10.16 | 33.7% | 18.9% |
| B | 1,362 | 15.4 | 9.9 | 19.3 | 17.4 | 16.4 | 11.4 | 10.1 | 11.14 | 38.0% | 21.5% |
| C | 1,639 | 12.4 | 9.8 | 21.1 | 15.0 | 18.0 | 14.5 | 9.2 | 12.36 | 41.7% | 23.7% |
| D | 1,988 | 11.4 | 8.7 | 16.4 | 15.5 | 22.7 | 16.0 | 9.2 | 14.15 | 47.9% | 25.1% |
| F | 2,619 | 6.9 | 4.9 | 14.8 | 14.5 | 20.8 | 23.7 | 14.4 | 18.86 | 58.8% | 38.0% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 2,836 | 21.0 | 14.5 | 27.1 | 16.3 | 13.3 | 5.5 | 2.3 | 7.35 | 21.1% | 7.8% |
| B | 1,501 | 14.0 | 9.9 | 23.2 | 15.9 | 19.1 | 12.2 | 5.7 | 10.94 | 37.0% | 17.9% |
| C | 1,895 | 11.6 | 8.0 | 19.3 | 14.8 | 21.5 | 14.9 | 9.9 | 13.39 | 46.3% | 24.8% |
| D | 1,670 | 12.3 | 9.0 | 20.8 | 12.9 | 22.3 | 15.9 | 6.8 | 12.94 | 45.0% | 22.7% |
| F | 2,068 | 8.6 | 7.3 | 13.3 | 13.6 | 23.1 | 23.0 | 11.1 | 17.66 | 57.2% | 34.0% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 3,586 | 16.7 | 10.5 | 19.6 | 17.2 | 15.2 | 10.6 | 10.2 | 10.91 | 36.0% | 20.8% |
| LIMITED | 2,488 | 14.4 | 10.7 | 21.5 | 15.4 | 17.1 | 13.3 | 7.5 | 11.02 | 37.9% | 20.8% |
| POOR | 4,641 | 8.9 | 6.6 | 15.5 | 15.0 | 21.7 | 20.3 | 12.1 | 16.64 | 54.0% | 32.3% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,621 | 29.9 | 26.2 | 36.8 | 5.2 | 1.7 | 0.2 | 0.0 | 4.46 | 1.8% | 0.2% |
| GAME_SPREAD | 1,599 | 23.5 | 15.4 | 37.1 | 18.6 | 4.9 | 0.3 | 0.2 | 6.19 | 5.4% | 0.5% |
| MATCH_WINNER | 9,970 | 14.1 | 10.2 | 21.1 | 14.8 | 19.3 | 13.7 | 6.8 | 11.38 | 39.8% | 20.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 3,218 | 28.9 | 18.5 | 31.7 | 11.4 | 7.7 | 1.5 | 0.3 | 5.32 | 9.5% | 1.8% |
| TOTAL_GAMES | 2,497 | 7.9 | 9.5 | 36.7 | 29.1 | 10.7 | 3.6 | 2.5 | 9.53 | 16.7% | 6.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,664 | 24.9 | 39.3 | 27.9 | 0.3 | 6.7 | 0.6 | 0.2 | 4.32 | 7.6% | 0.9% |
| GAME_SPREAD | 1,817 | 44.9 | 14.5 | 29.3 | 9.2 | 1.2 | 0.7 | 0.2 | 3.65 | 2.1% | 0.9% |
| TOTAL_GAMES | 2,825 | 3.8 | 6.1 | 42.9 | 37.0 | 6.8 | 1.6 | 2.0 | 9.79 | 10.3% | 3.5% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,664 | 25.7 | 18.0 | 35.4 | 9.3 | 7.7 | 3.4 | 0.6 | 5.61 | 11.6% | 3.9% |
| GAME_SPREAD | 1,817 | 19.0 | 13.5 | 27.1 | 22.9 | 13.3 | 3.3 | 0.8 | 8.31 | 17.4% | 4.1% |
| TOTAL_GAMES | 2,834 | 6.1 | 8.3 | 37.5 | 28.9 | 13.2 | 3.6 | 2.4 | 9.78 | 19.2% | 6.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 10,715 | 44.2% | 25.8% | 13.1 | 34.4% | 15.4% | 10.52 |
| gen1_elo | 10,715 | 44.1% | 24.8% | 12.73 | 34.0% | 14.8% | 10.11 |
| gen1_sr | 10,715 | 52.4% | 30.6% | 15.91 | 43.5% | 20.2% | 12.97 |
| gen2 | 10,715 | 51.1% | 31.2% | 15.5 | 43.4% | 22.4% | 12.83 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 5,028 | 15.5 | 11.6 | 21.7 | 17.2 | 18.5 | 11.9 | 3.7 | 10.32 | 34.1% | 15.6% |
| STALE | 5,687 | 10.4 | 6.5 | 15.3 | 14.6 | 18.4 | 18.5 | 16.3 | 16.86 | 53.2% | 34.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 3,438 | 16.0 | 11.3 | 23.8 | 15.0 | 17.0 | 12.8 | 4.1 | 9.74 | 33.9% | 16.9% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 20,685 | 3438 | 8500 | 8747 | 26.5 | 186.7 | 1400.4 |
| ge_15pp | 8,706 | 1166 | 3002 | 4538 | 31.5 | 459.9 | 1380.4 |
| ge_25pp | 4,807 | 581 | 1374 | 2852 | 42.3 | 570.6 | 1380.4 |
| lt_10pp | 8,804 | 1757 | 4083 | 2964 | 24.9 | 53.8 | 1201.9 |

Current slate `SL-20261007T014717Z-40855312`: 1111 priced rows, quote age at build {'median': 6.6, 'max': 6.6}, freshness {'FRESH': 1111}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 287 | 22.6 | 12.2 | 22.3 | 19.9 | 16.4 | 6.3 | 0.3 | 7.69 | 23.0% | 6.6% |
| MARKETS_AGREE | 21 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.51 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 24 | 0.0 | 0.0 | 29.2 | 41.7 | 25.0 | 4.2 | 0.0 | 12.11 | 29.2% | 4.2% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 10,715 | 333 (3.1%) | 7.2% | 0.0% | {"EXTERNAL_STALE": 287, "AGREES_WITH_KALSHI": 24, "ALL_AGREE": 21, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 4,741 | 73 (1.5%) | 9.6% | 0.0% | {"EXTERNAL_STALE": 66, "AGREES_WITH_KALSHI": 7} |
| fair_v1_ge_25pp | 2,764 | 20 (0.7%) | 5.0% | 0.0% | {"EXTERNAL_STALE": 19, "AGREES_WITH_KALSHI": 1} |
| fair_v1_ge_25pp_pregame_clean | 1,250 | 20 (1.6%) | 5.0% | 0.0% | {"EXTERNAL_STALE": 19, "AGREES_WITH_KALSHI": 1} |
| fair_v1_lt_10pp | 4,278 | 193 (4.5%) | 3.6% | 0.0% | {"EXTERNAL_STALE": 164, "ALL_AGREE": 21, "AGREES_WITH_KALSHI": 7, "EXTERNAL_OUTLIER": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 2,134 | 11.0 | 8.4 | 20.5 | 15.1 | 21.1 | 14.3 | 9.6 | 13.04 | 45.0% | 23.9% |
| 4-10x | 1,584 | 11.1 | 10.0 | 17.7 | 14.5 | 20.2 | 17.6 | 9.0 | 13.76 | 46.8% | 26.6% |
| <2x | 5,624 | 14.6 | 9.5 | 18.3 | 16.8 | 16.9 | 13.8 | 10.2 | 12.38 | 40.8% | 23.9% |
| >=10x | 1,373 | 10.3 | 5.8 | 15.2 | 14.7 | 18.6 | 21.4 | 14.0 | 16.92 | 54.0% | 35.4% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 2,697 | 14.0 | 8.3 | 20.6 | 15.9 | 17.0 | 12.9 | 11.3 | 12.12 | 41.2% | 24.2% |
| 300-1000 | 2,545 | 12.0 | 9.5 | 16.3 | 15.6 | 21.9 | 16.3 | 8.3 | 13.81 | 46.5% | 24.6% |
| <300 | 3,053 | 8.0 | 6.1 | 15.4 | 14.4 | 20.5 | 21.9 | 13.7 | 17.86 | 56.1% | 35.6% |
| >=3000 | 2,420 | 18.4 | 12.3 | 21.3 | 17.7 | 13.9 | 9.2 | 7.2 | 9.52 | 30.3% | 16.4% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 313 | 0.5329 | 0.3999 | 0.4537 | +0.079 | -0.054 | 0.0031 ± 0.008 |
| ratio 4-10x | 228 | 0.5926 | 0.4535 | 0.5395 | +0.053 | -0.086 | 0.0007 ± 0.01 |
| ratio <2x | 642 | 0.539 | 0.4143 | 0.4579 | +0.081 | -0.044 | 0.0119 ± 0.0057 |
| ratio >=10x | 208 | 0.5667 | 0.3914 | 0.4712 | +0.096 | -0.080 | 0.0109 ± 0.013 |
| thinner_sample 1000-3000 | 360 | 0.542 | 0.4205 | 0.4583 | +0.084 | -0.038 | 0.0059 ± 0.0074 |
| thinner_sample 300-1000 | 375 | 0.5711 | 0.4337 | 0.4987 | +0.072 | -0.065 | 0.0006 ± 0.0077 |
| thinner_sample <300 | 463 | 0.5548 | 0.3921 | 0.4838 | +0.071 | -0.092 | 0.0106 ± 0.0081 |
| thinner_sample >=3000 | 193 | 0.5165 | 0.4164 | 0.4197 | +0.097 | -0.003 | 0.0198 ± 0.0083 |
| data_status ADEQUATE | 385 | 0.5247 | 0.4184 | 0.439 | +0.086 | -0.021 | 0.0108 ± 0.0062 |
| data_status LIMITED | 304 | 0.5642 | 0.4318 | 0.4934 | +0.071 | -0.062 | -0.002 ± 0.0086 |
| data_status POOR | 702 | 0.5588 | 0.4039 | 0.4815 | +0.077 | -0.078 | 0.0107 ± 0.0063 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 209 | 0.1847 | 0.1854 | -0.0007 ± 0.001 | 0.5452 | 0.5471 | 0.4934 | 0.4791 | 0.4928 | -0.105 ± 0.0317 | -0.01 (3) |
| 3-5 | 139 | 0.1809 | 0.1832 | -0.0022 ± 0.003 | 0.5408 | 0.5433 | 0.5178 | 0.4771 | 0.518 | -0.068 ± 0.0375 | 0.02 (1) |
| 5-10 | 292 | 0.1997 | 0.203 | -0.0033 ± 0.0039 | 0.5852 | 0.5933 | 0.5242 | 0.4503 | 0.5034 | -0.084 ± 0.0275 | -0.0167 (3) |
| 10-15 | 238 | 0.2217 | 0.2164 | +0.0053 ± 0.0075 | 0.6319 | 0.6162 | 0.5249 | 0.4011 | 0.4412 | -0.104 ± 0.0302 | -0.0633 (3) |
| 15-25 | 301 | 0.2191 | 0.2109 | +0.0082 ± 0.0104 | 0.6275 | 0.6064 | 0.5721 | 0.376 | 0.4518 | -0.077 ± 0.0265 | -0.02 (4) |
| 25-40 | 173 | 0.2109 | 0.1981 | +0.0128 ± 0.0201 | 0.6083 | 0.5701 | 0.6459 | 0.3339 | 0.4682 | -0.056 ± 0.0297 | -0.01 (1) |
| 40+ | 39 | 0.3105 | 0.1436 | +0.1669 ± 0.0543 | 0.8355 | 0.4493 | 0.7382 | 0.2969 | 0.3333 | -0.170 ± 0.0539 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 852 | 0.1688 | 0.1696 | -0.0008 ± 0.0005 | 0.5052 | 0.5063 | 0.4899 | 0.4751 | 0.5164 | -0.034 ± 0.0144 | -0.0188 (8) |
| 3-5 | 616 | 0.1868 | 0.1856 | +0.0012 ± 0.0014 | 0.5524 | 0.5452 | 0.4807 | 0.4408 | 0.4399 | -0.072 ± 0.0179 | 0.02 (1) |
| 5-10 | 1295 | 0.1859 | 0.1867 | -0.0009 ± 0.0018 | 0.5524 | 0.5533 | 0.4841 | 0.4105 | 0.4525 | -0.036 ± 0.0121 | -0.0129 (7) |
| 10-15 | 1110 | 0.1962 | 0.1791 | +0.0171 ± 0.0032 | 0.5768 | 0.5276 | 0.4709 | 0.3467 | 0.3423 | -0.085 ± 0.0127 | -0.0633 (3) |
| 15-25 | 1433 | 0.1997 | 0.1596 | +0.0401 ± 0.0042 | 0.5888 | 0.4765 | 0.4883 | 0.2907 | 0.2875 | -0.085 ± 0.0105 | -0.017 (10) |
| 25-40 | 1378 | 0.2123 | 0.1189 | +0.0933 ± 0.0058 | 0.6162 | 0.3697 | 0.5214 | 0.2073 | 0.2184 | -0.056 ± 0.009 | -0.01 (1) |
| 40+ | 978 | 0.368 | 0.0399 | +0.3281 ± 0.0071 | 0.9582 | 0.1649 | 0.618 | 0.1032 | 0.0511 | -0.085 ± 0.006 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 153 | 0.1877 | 0.1872 | +0.0006 ± 0.0012 | 0.5526 | 0.5494 | 0.4912 | 0.4764 | 0.451 | -0.145 ± 0.0376 | -0.01 (1) |
| 3-5 | 99 | 0.1982 | 0.1977 | +0.0005 ± 0.0036 | 0.5723 | 0.5761 | 0.4946 | 0.4549 | 0.4646 | -0.084 ± 0.0481 | 0.02 (1) |
| 5-10 | 250 | 0.1926 | 0.1927 | -0.0001 ± 0.0042 | 0.5667 | 0.5671 | 0.5682 | 0.4931 | 0.524 | -0.089 ± 0.0288 | -0.01 (4) |
| 10-15 | 237 | 0.2322 | 0.2187 | +0.0136 ± 0.0077 | 0.6548 | 0.6279 | 0.5849 | 0.4607 | 0.4726 | -0.132 ± 0.0322 | -0.0667 (3) |
| 15-25 | 340 | 0.2234 | 0.2034 | +0.0200 ± 0.0098 | 0.6343 | 0.5864 | 0.5909 | 0.3935 | 0.4471 | -0.103 ± 0.0251 | -0.0167 (3) |
| 25-40 | 221 | 0.2593 | 0.199 | +0.0603 ± 0.0186 | 0.721 | 0.5782 | 0.6667 | 0.355 | 0.4118 | -0.133 ± 0.0304 | -0.025 (2) |
| 40+ | 91 | 0.3522 | 0.1839 | +0.1683 ± 0.0446 | 0.979 | 0.5402 | 0.7588 | 0.2716 | 0.3626 | -0.061 ± 0.0419 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 734 | 0.1688 | 0.1691 | -0.0002 ± 0.0005 | 0.505 | 0.5054 | 0.5081 | 0.4939 | 0.5041 | -0.061 ± 0.0163 | -0.0217 (6) |
| 3-5 | 488 | 0.181 | 0.1776 | +0.0034 ± 0.0015 | 0.5317 | 0.5264 | 0.5133 | 0.4736 | 0.4508 | -0.078 ± 0.0195 | 0.02 (1) |
| 5-10 | 1140 | 0.1808 | 0.1814 | -0.0007 ± 0.0019 | 0.537 | 0.5364 | 0.5139 | 0.4392 | 0.4789 | -0.036 ± 0.0129 | -0.01 (5) |
| 10-15 | 1025 | 0.1961 | 0.1777 | +0.0185 ± 0.0033 | 0.58 | 0.5244 | 0.5136 | 0.39 | 0.3815 | -0.093 ± 0.0135 | -0.0575 (4) |
| 15-25 | 1532 | 0.2089 | 0.1673 | +0.0416 ± 0.0041 | 0.6096 | 0.4971 | 0.5229 | 0.3277 | 0.3218 | -0.091 ± 0.0106 | -0.0143 (7) |
| 25-40 | 1458 | 0.2413 | 0.1288 | +0.1124 ± 0.006 | 0.685 | 0.3978 | 0.5545 | 0.2369 | 0.2174 | -0.092 ± 0.0095 | -0.015 (6) |
| 40+ | 1285 | 0.3969 | 0.0683 | +0.3287 ± 0.0084 | 1.036 | 0.2386 | 0.6651 | 0.1267 | 0.1035 | -0.064 ± 0.007 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 212 | 0.1904 | 0.1924 | -0.0021 ± 0.0011 | 0.5597 | 0.5659 | 0.5132 | 0.4984 | 0.5425 | -0.056 ± 0.0303 | -0.01 (5) |
| 3-5 | 152 | 0.1795 | 0.1782 | +0.0014 ± 0.0027 | 0.5331 | 0.5297 | 0.5046 | 0.4654 | 0.4671 | -0.129 ± 0.0367 | -- (0) |
| 5-10 | 292 | 0.1997 | 0.2001 | -0.0004 ± 0.0039 | 0.5866 | 0.5838 | 0.5185 | 0.4448 | 0.4795 | -0.093 ± 0.0267 | -0.01 (3) |
| 10-15 | 233 | 0.2143 | 0.2166 | -0.0024 ± 0.0076 | 0.6181 | 0.6191 | 0.5432 | 0.4199 | 0.4936 | -0.076 ± 0.0303 | -0.044 (5) |
| 15-25 | 293 | 0.2213 | 0.2058 | +0.0155 ± 0.0104 | 0.6389 | 0.5933 | 0.5833 | 0.3891 | 0.4471 | -0.098 ± 0.0264 | -0.03 (1) |
| 25-40 | 176 | 0.2027 | 0.2075 | -0.0047 ± 0.0201 | 0.5899 | 0.5941 | 0.6534 | 0.34 | 0.5 | -0.040 ± 0.0292 | 0.0 (1) |
| 40+ | 33 | 0.3471 | 0.1356 | +0.2115 ± 0.058 | 0.918 | 0.43 | 0.7266 | 0.2779 | 0.2727 | -0.196 ± 0.0611 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 846 | 0.1672 | 0.1681 | -0.0009 ± 0.0005 | 0.5036 | 0.5055 | 0.492 | 0.4773 | 0.5071 | -0.041 ± 0.0142 | -0.0162 (13) |
| 3-5 | 606 | 0.1877 | 0.1833 | +0.0044 ± 0.0014 | 0.552 | 0.5435 | 0.4778 | 0.4386 | 0.401 | -0.119 ± 0.0182 | -0.01 (2) |
| 5-10 | 1347 | 0.187 | 0.1829 | +0.0041 ± 0.0017 | 0.5569 | 0.5402 | 0.4837 | 0.4099 | 0.4165 | -0.067 ± 0.0116 | -0.01 (3) |
| 10-15 | 1056 | 0.1882 | 0.179 | +0.0092 ± 0.0032 | 0.558 | 0.526 | 0.483 | 0.3598 | 0.3845 | -0.059 ± 0.0129 | -0.03 (9) |
| 15-25 | 1564 | 0.2011 | 0.1594 | +0.0417 ± 0.004 | 0.5959 | 0.4781 | 0.4923 | 0.2939 | 0.2903 | -0.080 ± 0.0102 | -0.03 (2) |
| 25-40 | 1318 | 0.2132 | 0.1169 | +0.0963 ± 0.006 | 0.6179 | 0.3623 | 0.5202 | 0.2015 | 0.2132 | -0.060 ± 0.0089 | 0.0 (1) |
| 40+ | 925 | 0.3827 | 0.0409 | +0.3418 ± 0.0076 | 1.0018 | 0.1679 | 0.6245 | 0.1024 | 0.0476 | -0.087 ± 0.0063 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 489 | 0.203 | 0.2033 | -0.0003 ± 0.0007 | 0.5874 | 0.5886 | 0.4964 | 0.4816 | 0.4908 | -0.040 ± 0.0203 | -0.0226 (46) |
| 3-5 | 365 | 0.1948 | 0.1951 | -0.0003 ± 0.0019 | 0.5717 | 0.5709 | 0.4795 | 0.4398 | 0.4658 | -0.032 ± 0.0229 | -0.0059 (32) |
| 5-10 | 755 | 0.1886 | 0.184 | +0.0046 ± 0.0024 | 0.561 | 0.5482 | 0.4665 | 0.3927 | 0.3987 | -0.051 ± 0.0158 | -0.005 (72) |
| 10-15 | 500 | 0.2022 | 0.1918 | +0.0104 ± 0.0049 | 0.5931 | 0.564 | 0.4662 | 0.3432 | 0.362 | -0.043 ± 0.0195 | 0.0016 (63) |
| 15-25 | 674 | 0.2364 | 0.2114 | +0.0250 ± 0.0069 | 0.6689 | 0.6085 | 0.5352 | 0.3417 | 0.3754 | -0.046 ± 0.0178 | -0.0216 (58) |
| 25-40 | 367 | 0.2487 | 0.1759 | +0.0728 ± 0.0136 | 0.6977 | 0.5223 | 0.5995 | 0.2871 | 0.3243 | -0.067 ± 0.0207 | -0.0216 (25) |
| 40+ | 115 | 0.3769 | 0.1652 | +0.2117 ± 0.0399 | 1.0573 | 0.5018 | 0.7507 | 0.2503 | 0.313 | -0.050 ± 0.0359 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1151 | 0.1926 | 0.1931 | -0.0004 ± 0.0005 | 0.5612 | 0.5622 | 0.4938 | 0.4787 | 0.4952 | -0.033 ± 0.0128 | -0.0155 (82) |
| 3-5 | 812 | 0.1875 | 0.1869 | +0.0006 ± 0.0012 | 0.5526 | 0.551 | 0.4906 | 0.4509 | 0.4643 | -0.039 ± 0.0152 | -0.018 (54) |
| 5-10 | 1729 | 0.1839 | 0.1784 | +0.0055 ± 0.0015 | 0.5488 | 0.5322 | 0.4648 | 0.3903 | 0.3933 | -0.052 ± 0.0103 | -0.0089 (122) |
| 10-15 | 1285 | 0.1972 | 0.1849 | +0.0123 ± 0.003 | 0.5821 | 0.5468 | 0.4754 | 0.3524 | 0.3634 | -0.050 ± 0.0118 | -0.0053 (99) |
| 15-25 | 1686 | 0.2267 | 0.1928 | +0.0339 ± 0.0042 | 0.653 | 0.563 | 0.5251 | 0.3296 | 0.3405 | -0.061 ± 0.0108 | -0.0255 (106) |
| 25-40 | 1233 | 0.2376 | 0.1485 | +0.0892 ± 0.0069 | 0.6734 | 0.449 | 0.5633 | 0.2481 | 0.2652 | -0.063 ± 0.0107 | -0.0206 (47) |
| 40+ | 606 | 0.3696 | 0.0878 | +0.2818 ± 0.013 | 1.0045 | 0.2902 | 0.6607 | 0.1515 | 0.1403 | -0.069 ± 0.0116 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 1391 | 1.145 ± 0.08 | 1.257 | 0.1668 | 0.1658 | 0.208 | 0.2001 |
| gen2 | 1391 | 0.932 ± 0.07 | 1.169 | 0.1826 | 0.1658 | 0.2278 | 0.1999 |
| gen1_elo | 1391 | 1.119 ± 0.077 | 1.232 | 0.1719 | 0.166 | 0.2069 | 0.1999 |
| gen1_sr | 1391 | 1.173 ± 0.091 | 1.23 | 0.1402 | 0.1677 | 0.2228 | 0.2001 |
| gen1_ledger | 3265 | 0.93 ± 0.047 | 1.097 | 0.1648 | 0.1941 | 0.2168 | 0.1934 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 8,706)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,487 | 28.6% |
| STALE_QUOTE | market_freshness | 2,051 | 23.6% |
| BOOK_QUALITY | execution | 1,537 | 17.6% |
| POOR_DATA | data | 866 | 10.0% |
| LIMITED_DATA | data | 531 | 6.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 400 | 4.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 399 | 4.6% |
| IN_PLAY_QUOTE | market_freshness/coverage | 225 | 2.6% |
| IDENTITY_AMBIGUOUS | mapping | 203 | 2.3% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 7 | 0.1% |

Cause class: coverage 28.6%, market_freshness 23.6%, execution 17.6%, data 16.1%, market_freshness/coverage 7.2%, model_calibration_or_unknown 4.6%, mapping 2.3%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 95.9%, LOW_DATA_QUALITY 68.8%, THIN_PLAYER_HISTORY 58.7%, STALE_PLAYER_DATA 57.9%, STALE_KALSHI_QUOTE 52.1%, MODEL_INTERNAL_DISAGREEMENT 37.4%, ASYMMETRIC_SAMPLE_SIZE 31.7%, WIDE_SPREAD 24.6%, MODEL_HIGH_UNCERTAINTY 15.2%, PLAYER_IDENTITY_RISK 10.6%, LEVEL_TRANSFER_RISK 8.3%, LOW_DISPLAYED_LIQUIDITY 7.1%, EVENT_MAPPING_RISK 6.9%, MODEL_CALIBRATION_OUTLIER 2.7%, UNKNOWN 0.5%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 30.6%, POST_SETTLEMENT_OBSERVATION 28.6%, POSSIBLE_IN_PLAY_QUOTE 5.0%, CONFIRMED_IN_PLAY_QUOTE 0.7%

### >= ge_25 pp (N = 4,807)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,953 | 40.6% |
| STALE_QUOTE | market_freshness | 928 | 19.3% |
| BOOK_QUALITY | execution | 802 | 16.7% |
| POOR_DATA | data | 385 | 8.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 220 | 4.6% |
| LIMITED_DATA | data | 159 | 3.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 138 | 2.9% |
| IDENTITY_AMBIGUOUS | mapping | 118 | 2.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 102 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 2 | 0.0% |

Cause class: coverage 40.6%, market_freshness 19.3%, execution 16.7%, data 11.3%, market_freshness/coverage 7.4%, mapping 2.5%, model_calibration_or_unknown 2.1%, model_calibration 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 97.9%, LOW_DATA_QUALITY 71.5%, THIN_PLAYER_HISTORY 60.9%, STALE_KALSHI_QUOTE 59.3%, STALE_PLAYER_DATA 54.2%, MODEL_INTERNAL_DISAGREEMENT 39.7%, ASYMMETRIC_SAMPLE_SIZE 34.2%, WIDE_SPREAD 23.4%, MODEL_HIGH_UNCERTAINTY 16.5%, PLAYER_IDENTITY_RISK 13.1%, EVENT_MAPPING_RISK 7.6%, LEVEL_TRANSFER_RISK 7.5%, LOW_DISPLAYED_LIQUIDITY 7.4%, MODEL_CALIBRATION_OUTLIER 3.4%, UNKNOWN 0.1%, EXTERNAL_MARKET_REJECTION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 42.9%, POST_SETTLEMENT_OBSERVATION 40.6%, POSSIBLE_IN_PLAY_QUOTE 5.1%, CONFIRMED_IN_PLAY_QUOTE 0.8%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 4030, "IDENTITY_AMBIGUOUS": 777}; ticker orientation: {"VERIFIED": 4807}.

Checks: discipline:AMBIGUOUS 217, discipline:PASS 4590, identity_confidence:AMBIGUOUS 630, identity_confidence:PASS 4177, level_mapping:NA 229, level_mapping:PASS 4578, market_pair:AMBIGUOUS 179, market_pair:NA 119, market_pair:PASS 4509, model_complement:NA 88, model_complement:PASS 4719, namesake:PASS 4807, physical_match_id:NA 2043, physical_match_id:PASS 2764, player_ids:PASS 4807, same_pair_other_event:PASS 4807, ticker_orientation:PASS 4807

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,120 | 2.1% | 2.1% | 0.5% | {"market_freshness": 20, "execution": 3} | 5.61 | 0.1949 / 0.1839 (77) | 22.3% | 0.2% | 6.2% | 1.5% |
| CHALLENGER | 3,330 | 19.2% | 6.7% | 13.3% | {"coverage": 395, "market_freshness": 106, "market_freshness/coverage": 73, "model_calibration_or_unknown": 35, "data": 25, "execution": 4} | 6.98 | 0.2192 / 0.2021 (786) | 48.7% | 5.4% | 1.4% | 24.0% |
| DOUBLES | 494 | 43.9% | 43.5% | 4.5% | {"market_freshness": 106, "execution": 50, "mapping": 40, "market_freshness/coverage": 14, "coverage": 7} | 22.7 | 0.3142 / 0.227 (171) | 47.4% | 0.0% | 100.0% | 8.7% |
| ITF_MEN | 6,148 | 25.8% | 17.8% | 33.0% | {"coverage": 652, "execution": 356, "market_freshness": 249, "data": 206, "market_freshness/coverage": 104, "mapping": 19, "model_calibration_or_unknown": 1} | 11.23 | 0.2165 / 0.1932 (1553) | 42.9% | 56.4% | 6.7% | 24.2% |
| ITF_WOMEN | 7,780 | 27.5% | 19.1% | 44.5% | {"coverage": 882, "market_freshness": 391, "execution": 372, "data": 289, "market_freshness/coverage": 126, "mapping": 53, "model_calibration_or_unknown": 22, "model_calibration": 2} | 12.52 | 0.2019 / 0.1909 (1643) | 44.0% | 60.6% | 11.1% | 24.1% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 928 | 8.5% | 7.4% | 1.6% | {"market_freshness": 34, "model_calibration_or_unknown": 16, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.39 | 0.2026 / 0.197 (137) | 35.6% | 2.3% | 1.3% | 3.5% |
| WTA125 | 736 | 15.5% | 11.0% | 2.4% | {"market_freshness/coverage": 31, "model_calibration_or_unknown": 26, "market_freshness": 20, "data": 13, "coverage": 12, "execution": 8, "mapping": 4} | 10.08 | 0.2211 / 0.2059 (247) | 28.4% | 5.8% | 4.1% | 12.5% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 3 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 4 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 17.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1037 min (STALE); no external reference |
| 5 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 6 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 7 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 8 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 9 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 10 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 11 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 12 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 13 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 14 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 15 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 16 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 18 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 19 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 20 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 21 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 22 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 23 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 24 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 110 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 25 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 26 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 27 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 253 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 28 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 29 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 30 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 18% | +73 | BOOK_QUALITY | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 31 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 32 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 33 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 826 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 34 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 687 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 35 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 36 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 37 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 156 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 38 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 39 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 40 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 41 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 42 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 43 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 114 min (STALE); data LIMITED (grade B, thinner serve sample 2163.0, ratio 2.0); no external reference |
| 44 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 407 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 45 | `KXWTAMATCH-26OCT01YASCHW-CHW` | WTA | fair_v1 | 73% / 2% | +70 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 51 min (STALE); no external reference |
| 46 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 47 | `KXATPCHALLENGERMATCH-26OCT05CASMUN-CAS` | CHALLENGER | fair_v1 | 83% / 14% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 227 min (STALE); data POOR (grade D, thinner serve sample 814.0, ratio 3.76); no external reference |
| 48 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 49 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9787, "by_level_share_of_ge_25pp": {"ATP": 0.0048, "CHALLENGER": 0.1327, "DOUBLES": 0.0451, "ITF_MEN": 0.3301, "ITF_WOMEN": 0.4446, "OTHER": 0.0025, "WTA": 0.0164, "WTA125": 0.0237}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5933, "share_primary_cause_market_settled_or_in_play": 0.4808, "share_primary_cause_stale_quote_only": 0.1931}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 4807, "identity_ambiguous_share": 0.1616, "ticker_orientation": {"VERIFIED": 4807}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 2764, "with_external": 20, "coverage": 0.0072, "external_status": {"EXTERNAL_STALE": 19, "AGREES_WITH_KALSHI": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 19, "MODEL_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.05, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 1250, "with_external": 20, "coverage": 0.016, "external_status": {"EXTERNAL_STALE": 19, "AGREES_WITH_KALSHI": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 19, "MODEL_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.05, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 593.0, "median_sample_ratio": 2.38, "median_min_matches": 19.0, "median_max_days_since_last": 197.0, "share_severe_asymmetry": 0.1843, "data_status": {"POOR": 2595, "LIMITED": 1333, "ADEQUATE": 879}, "comparison_lt_10pp": {"median_thinner_serve_points": 1774.0, "median_sample_ratio": 1.76, "median_min_matches": 75.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 313, "model_minus_observed": 0.0792, "kalshi_minus_observed": -0.0538, "brier_diff_model_minus_kalshi": 0.0031}, "4-10x": {"n": 228, "model_minus_observed": 0.0531, "kalshi_minus_observed": -0.086, "brier_diff_model_minus_kalshi": 0.0007}, "<2x": {"n": 642, "model_minus_observed": 0.0811, "kalshi_minus_observed": -0.0437, "brier_diff_model_minus_kalshi": 0.0119}, ">=10x": {"n": 208, "model_minus_observed": 0.0956, "kalshi_minus_observed": -0.0797, "brier_diff_model_minus_kalshi": 0.0109}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 1391, "model": {"intercept": -0.617, "slope": 0.932, "slope_se": 0.07}, "kalshi_mid_same_rows": {"intercept": 0.218, "slope": 1.169, "slope_se": 0.079}, "mean_extremity_model": 0.1826, "mean_extremity_kalshi": 0.1658, "model_brier": 0.2278, "kalshi_brier": 0.1999, "brier_diff_model_minus_kalshi": 0.0279, "brier_diff_se": 0.0051, "model_logloss": 0.6486, "kalshi_logloss": 0.5809}, "fair_v1": {"n": 1391, "model": {"intercept": -0.403, "slope": 1.145, "slope_se": 0.08}, "kalshi_mid_same_rows": {"intercept": 0.376, "slope": 1.257, "slope_se": 0.083}, "mean_extremity_model": 0.1668, "mean_extremity_kalshi": 0.1658, "model_brier": 0.208, "kalshi_brier": 0.2001, "brier_diff_model_minus_kalshi": 0.0079, "brier_diff_se": 0.0041, "model_logloss": 0.6018, "kalshi_logloss": 0.5812}, "gen1_elo": {"n": 1391, "model": {"intercept": -0.386, "slope": 1.119, "slope_se": 0.077}, "kalshi_mid_same_rows": {"intercept": 0.363, "slope": 1.232, "slope_se": 0.081}, "mean_extremity_model": 0.1719, "mean_extremity_kalshi": 0.166, "model_brier": 0.2069, "kalshi_brier": 0.1999, "brier_diff_model_minus_kalshi": 0.007, "brier_diff_se": 0.004, "model_logloss": 0.6012, "kalshi_logloss": 0.5807}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.258, "share_ge_15": 0.4425, "median_abs_gap": 13.1, "n": 10715}, "gen1_elo": {"share_ge_25": 0.2479, "share_ge_15": 0.4407, "median_abs_gap": 12.73, "n": 10715}, "gen1_sr": {"share_ge_25": 0.3059, "share_ge_15": 0.524, "median_abs_gap": 15.91, "n": 10715}, "gen2": {"share_ge_25": 0.3125, "share_ge_15": 0.5114, "median_abs_gap": 15.5, "n": 10715}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1541, "share_ge_15": 0.3439, "median_abs_gap": 10.52, "n": 8110}, "gen1_elo": {"share_ge_25": 0.1482, "share_ge_15": 0.3395, "median_abs_gap": 10.11, "n": 8110}, "gen1_sr": {"share_ge_25": 0.2022, "share_ge_15": 0.4354, "median_abs_gap": 12.97, "n": 8110}, "gen2": {"share_ge_25": 0.2245, "share_ge_15": 0.4342, "median_abs_gap": 12.83, "n": 8110}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.61, "share_ge_25_all": 0.0205, "share_ge_25_pregame_clean": 0.0209}, "WTA": {"median_abs_gap_pregame_clean": 8.39, "share_ge_25_all": 0.0851, "share_ge_25_pregame_clean": 0.0737}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2292, "share_within_10pp_all": 0.4256, "share_within_10pp_pregame_clean": 0.4911, "corr_model_vs_mid_pregame_clean": 0.8425}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 209, "model_brier": 0.1847, "kalshi_brier": 0.1854, "brier_diff_model_minus_kalshi": -0.0007}, "10-15": {"n_settled": 238, "model_brier": 0.2217, "kalshi_brier": 0.2164, "brier_diff_model_minus_kalshi": 0.0053}, "15-25": {"n_settled": 301, "model_brier": 0.2191, "kalshi_brier": 0.2109, "brier_diff_model_minus_kalshi": 0.0082}, "25-40": {"n_settled": 173, "model_brier": 0.2109, "kalshi_brier": 0.1981, "brier_diff_model_minus_kalshi": 0.0128}, "3-5": {"n_settled": 139, "model_brier": 0.1809, "kalshi_brier": 0.1832, "brier_diff_model_minus_kalshi": -0.0022}, "40+": {"n_settled": 39, "model_brier": 0.3105, "kalshi_brier": 0.1436, "brier_diff_model_minus_kalshi": 0.1669}, "5-10": {"n_settled": 292, "model_brier": 0.1997, "kalshi_brier": 0.203, "brier_diff_model_minus_kalshi": -0.0033}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%)
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap).
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 171, "model_brier": 0.3142, "kalshi_brier": 0.227, "brier_diff_model_minus_kalshi": 0.0872, "brier_diff_se": 0.0247, "corr_model_outcome": -0.069, "corr_kalshi_outcome": 0.3465}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
