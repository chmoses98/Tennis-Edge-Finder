# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-01T23:05Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 10,146): 0-3 13.4%, 3-5 9.0%, 5-10 19.4%, 10-15 14.8%, 15-25 19.6%, 25-40 14.4%, 40+ 9.4%; median gap 12.56 pp.
* **Where the extremes live**: 96.7% of >=25 pp gaps are off the ATP/WTA main tour (ITF 74.2%, Challenger 12.0%, doubles 7.4%). Main tour: ATP 3.9% and WTA 9.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 2,412): MARKET_ALREADY_SETTLED_WHEN_PRICED 45.9%, STALE_QUOTE 23.1%, POOR_DATA 6.6%, BOOK_QUALITY 5.9%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IN_PLAY_QUOTE 5.2%, LIMITED_DATA 3.1%, IDENTITY_AMBIGUOUS 2.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%. By class: coverage 45.9%, market_freshness 23.1%, market_freshness/coverage 10.8%, data 9.7%, execution 5.9%, mapping 2.4%, model_calibration_or_unknown 2.1%.
* **Stale / settled / in-play**: 68.9% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 56.8% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 2,412 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 15.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 0.4%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 7.4% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 770.0 points vs 1948.5 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.166, Gen-2 0.966, Gen-1 ledger 0.904 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 80 model 0.2384 vs Kalshi 0.1762; n 21 model 0.2865 vs Kalshi 0.1302.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%). Not implemented here.

## 1. Observations

* 31,677 model-market comparisons (54,619 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 15,996 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-01T17:35:00.309201+00:00'], shadow board 8,666 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-01T23:00:04.764724+00:00'], Model 4 2,535 rows, 7,974 settled tickers, 1,679 tickers with an external scan.
* By model: {"gen1_ledger": 9335, "gen1_elo": 4360, "fair_v1": 4360, "gen2": 4360, "gen1_sr": 4360, "model4_fundamental": 2455, "model4_conditioned": 2447}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 10,146 | 13.4 | 9.0 | 19.4 | 14.8 | 19.6 | 14.4 | 9.4 | 12.56 | 43.4% | 23.8% |
| MW fair_v1 | 4,360 | 13.6 | 8.5 | 18.6 | 14.9 | 18.6 | 15.1 | 10.6 | 12.99 | 44.4% | 25.8% |
| MW gen1_elo | 4,360 | 13.2 | 8.5 | 19.9 | 14.9 | 18.4 | 15.0 | 10.1 | 12.51 | 43.4% | 25.0% |
| MW gen1_ledger | 5,786 | 13.3 | 9.4 | 20.0 | 14.7 | 20.4 | 13.8 | 8.4 | 12.23 | 42.6% | 22.3% |
| MW gen1_sr | 4,360 | 9.8 | 6.9 | 16.7 | 13.3 | 22.1 | 18.6 | 12.6 | 16.3 | 53.2% | 31.2% |
| MW gen2 | 4,360 | 11.1 | 6.4 | 16.5 | 15.3 | 19.8 | 17.1 | 13.8 | 15.32 | 50.6% | 30.9% |
| all families model4_conditioned | 2,447 | 18.6 | 15.2 | 29.1 | 24.0 | 8.9 | 2.1 | 2.0 | 7.4 | 13.1% | 4.1% |
| all families model4_fundamental | 2,455 | 13.8 | 10.6 | 30.6 | 22.3 | 14.4 | 5.2 | 3.0 | 9.1 | 22.7% | 8.2% |

Configurable thresholds (primary): >=5pp 77.6%, >=10pp 58.2%, >=15pp 43.4%, >=20pp 32.7%, >=25pp 23.8%, >=30pp 17.5%, >=40pp 9.4%, >=50pp 4.3%
Executable gap (model outside the book, before fees): median 10.09pp; >=10pp 50.2%, >=25pp 21.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 214 | 22.9 | 19.2 | 23.8 | 14.0 | 14.9 | 1.4 | 3.7 | 6.01 | 20.1% | 5.1% |
| CHALLENGER | 763 | 15.3 | 8.7 | 16.1 | 15.3 | 16.0 | 15.2 | 13.4 | 13.57 | 44.6% | 28.6% |
| ITF_MEN | 1,395 | 11.7 | 8.5 | 19.9 | 14.5 | 18.5 | 14.9 | 12.1 | 13.06 | 45.5% | 27.0% |
| ITF_WOMEN | 1,521 | 11.0 | 6.6 | 15.9 | 14.9 | 20.8 | 19.3 | 11.5 | 15.76 | 51.6% | 30.8% |
| WTA | 389 | 22.1 | 10.8 | 27.0 | 13.9 | 17.7 | 6.9 | 1.5 | 8.16 | 26.2% | 8.5% |
| WTA125 | 78 | 12.8 | 5.1 | 16.7 | 25.6 | 20.5 | 14.1 | 5.1 | 12.8 | 39.7% | 19.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 214 | 22.9 | 13.6 | 25.2 | 15.4 | 16.8 | 1.9 | 4.2 | 7.04 | 22.9% | 6.1% |
| CHALLENGER | 763 | 10.8 | 5.6 | 17.6 | 17.2 | 18.2 | 17.8 | 12.8 | 14.86 | 48.9% | 30.7% |
| ITF_MEN | 1,395 | 10.0 | 5.8 | 16.9 | 16.3 | 20.1 | 16.3 | 14.5 | 15.41 | 51.0% | 30.8% |
| ITF_WOMEN | 1,521 | 8.6 | 6.7 | 14.1 | 13.0 | 19.4 | 19.9 | 18.2 | 18.22 | 57.5% | 38.1% |
| WTA | 389 | 20.1 | 5.4 | 17.7 | 16.2 | 23.4 | 15.7 | 1.5 | 12.93 | 40.6% | 17.2% |
| WTA125 | 78 | 6.4 | 5.1 | 14.1 | 20.5 | 24.4 | 16.7 | 12.8 | 16.39 | 53.8% | 29.5% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 214 | 29.0 | 13.1 | 28.5 | 11.2 | 8.9 | 5.6 | 3.7 | 6.53 | 18.2% | 9.3% |
| CHALLENGER | 763 | 15.2 | 7.5 | 20.3 | 14.6 | 14.3 | 14.6 | 13.6 | 12.25 | 42.5% | 28.2% |
| ITF_MEN | 1,395 | 10.2 | 9.6 | 18.6 | 15.8 | 18.4 | 16.0 | 11.4 | 13.09 | 45.7% | 27.4% |
| ITF_WOMEN | 1,521 | 9.9 | 6.4 | 16.9 | 14.1 | 23.5 | 18.7 | 10.6 | 16.56 | 52.8% | 29.3% |
| WTA | 389 | 23.6 | 12.8 | 30.3 | 15.2 | 12.8 | 3.6 | 1.5 | 7.0 | 18.0% | 5.1% |
| WTA125 | 78 | 17.9 | 6.4 | 23.1 | 29.5 | 12.8 | 10.3 | 0.0 | 10.52 | 23.1% | 10.3% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 71 | 23.9 | 22.5 | 35.2 | 11.3 | 7.0 | 0.0 | 0.0 | 6.19 | 7.0% | 0.0% |
| CHALLENGER | 777 | 21.2 | 13.9 | 26.2 | 15.8 | 13.6 | 6.6 | 2.6 | 7.45 | 22.8% | 9.1% |
| DOUBLES | 363 | 5.5 | 3.9 | 9.6 | 10.5 | 21.5 | 20.7 | 28.4 | 24.32 | 70.5% | 49.0% |
| ITF_MEN | 1,942 | 14.2 | 9.0 | 18.8 | 13.5 | 21.3 | 13.7 | 9.5 | 12.59 | 44.5% | 23.2% |
| ITF_WOMEN | 1,790 | 9.1 | 8.3 | 17.5 | 14.5 | 23.2 | 18.6 | 8.9 | 15.23 | 50.7% | 27.5% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 363 | 15.4 | 9.4 | 25.6 | 22.3 | 17.6 | 8.8 | 0.8 | 9.8 | 27.3% | 9.6% |
| WTA125 | 331 | 13.6 | 9.7 | 21.1 | 17.2 | 23.3 | 11.2 | 3.9 | 11.35 | 38.4% | 15.1% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 213 | 22.5 | 19.2 | 23.9 | 14.1 | 15.0 | 1.4 | 3.8 | 6.01 | 20.2% | 5.2% |
| CHALLENGER | 558 | 19.4 | 10.8 | 19.7 | 18.5 | 17.0 | 9.3 | 5.4 | 10.14 | 31.7% | 14.7% |
| ITF_MEN | 901 | 15.7 | 11.7 | 24.4 | 15.7 | 18.2 | 10.2 | 4.2 | 9.67 | 32.6% | 14.4% |
| ITF_WOMEN | 1,017 | 14.8 | 8.8 | 19.4 | 17.8 | 22.2 | 13.1 | 3.9 | 12.37 | 39.2% | 17.0% |
| WTA | 388 | 22.2 | 10.8 | 27.1 | 13.9 | 17.8 | 6.7 | 1.6 | 8.12 | 26.0% | 8.2% |
| WTA125 | 77 | 13.0 | 5.2 | 16.9 | 26.0 | 20.8 | 13.0 | 5.2 | 12.79 | 39.0% | 18.2% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 213 | 23.0 | 13.2 | 25.4 | 15.5 | 16.9 | 1.9 | 4.2 | 7.04 | 23.0% | 6.1% |
| CHALLENGER | 558 | 13.3 | 7.2 | 22.2 | 21.0 | 19.5 | 12.5 | 4.3 | 11.73 | 36.4% | 16.9% |
| ITF_MEN | 901 | 13.1 | 7.3 | 20.3 | 18.9 | 21.0 | 13.4 | 6.0 | 12.27 | 40.4% | 19.4% |
| ITF_WOMEN | 1,017 | 10.2 | 8.8 | 16.4 | 13.1 | 22.7 | 17.5 | 11.3 | 15.52 | 51.5% | 28.8% |
| WTA | 388 | 20.1 | 5.4 | 17.8 | 16.2 | 23.4 | 15.5 | 1.6 | 12.85 | 40.5% | 17.0% |
| WTA125 | 77 | 6.5 | 5.2 | 14.3 | 20.8 | 24.7 | 16.9 | 11.7 | 16.14 | 53.2% | 28.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 59 | 25.4 | 25.4 | 35.6 | 11.9 | 1.7 | 0.0 | 0.0 | 4.87 | 1.7% | 0.0% |
| CHALLENGER | 637 | 23.7 | 16.2 | 29.2 | 15.4 | 12.9 | 2.5 | 0.2 | 6.68 | 15.5% | 2.7% |
| DOUBLES | 281 | 6.0 | 3.6 | 9.6 | 10.7 | 21.7 | 21.4 | 27.1 | 24.11 | 70.1% | 48.4% |
| ITF_MEN | 1,382 | 17.3 | 10.8 | 22.1 | 14.5 | 21.1 | 10.4 | 3.7 | 9.95 | 35.2% | 14.1% |
| ITF_WOMEN | 1,213 | 11.1 | 9.7 | 21.4 | 16.6 | 24.1 | 15.0 | 2.1 | 12.14 | 41.3% | 17.2% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 255 | 15.3 | 9.0 | 25.5 | 23.5 | 19.6 | 7.1 | 0.0 | 10.01 | 26.7% | 7.1% |
| WTA125 | 252 | 16.3 | 10.7 | 25.4 | 19.8 | 21.0 | 6.3 | 0.4 | 9.32 | 27.8% | 6.8% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 363 | 5.5 | 3.9 | 9.6 | 10.5 | 21.5 | 20.7 | 28.4 | 24.32 | 70.5% | 49.0% |
| singles | 5,423 | 13.8 | 9.8 | 20.7 | 14.9 | 20.3 | 13.4 | 7.1 | 11.8 | 40.8% | 20.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 947 | 15.7 | 8.0 | 18.6 | 14.2 | 16.8 | 14.0 | 12.7 | 12.44 | 43.5% | 26.7% |
| Hard | 3,126 | 12.9 | 9.0 | 18.9 | 14.7 | 19.2 | 15.4 | 10.1 | 13.07 | 44.6% | 25.5% |
| UNKNOWN | 287 | 13.9 | 5.6 | 15.7 | 19.9 | 19.2 | 16.0 | 9.8 | 13.49 | 45.0% | 25.8% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,311 | 17.9 | 10.3 | 21.0 | 15.2 | 17.1 | 11.1 | 7.5 | 10.17 | 35.6% | 18.5% |
| B | 595 | 16.3 | 10.9 | 17.6 | 17.8 | 14.8 | 10.8 | 11.8 | 11.56 | 37.3% | 22.5% |
| C | 744 | 12.0 | 8.3 | 22.9 | 13.7 | 16.4 | 15.5 | 11.3 | 12.91 | 43.1% | 26.8% |
| D | 808 | 12.4 | 8.4 | 17.1 | 14.1 | 20.9 | 15.0 | 12.1 | 14.16 | 48.0% | 27.1% |
| F | 902 | 7.9 | 4.7 | 13.6 | 14.2 | 23.3 | 23.7 | 12.6 | 19.2 | 59.7% | 36.4% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,762 | 18.8 | 12.0 | 26.3 | 16.9 | 16.6 | 6.8 | 2.7 | 8.57 | 26.1% | 9.5% |
| B | 957 | 14.1 | 9.1 | 21.5 | 16.5 | 18.9 | 12.3 | 7.5 | 11.55 | 38.8% | 19.9% |
| C | 1,188 | 11.2 | 8.4 | 15.6 | 14.1 | 21.8 | 15.4 | 13.6 | 15.33 | 50.8% | 29.0% |
| D | 897 | 11.4 | 8.2 | 20.3 | 11.9 | 24.0 | 15.6 | 8.6 | 14.24 | 48.2% | 24.2% |
| F | 982 | 6.8 | 7.2 | 12.4 | 12.2 | 23.5 | 24.4 | 13.3 | 19.52 | 61.3% | 37.8% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 1,631 | 16.7 | 9.6 | 20.2 | 16.3 | 16.6 | 11.2 | 9.4 | 10.82 | 37.2% | 20.6% |
| LIMITED | 1,001 | 14.5 | 10.5 | 21.9 | 13.8 | 15.6 | 13.9 | 9.9 | 11.67 | 39.4% | 23.8% |
| POOR | 1,728 | 10.1 | 6.4 | 15.2 | 14.2 | 22.4 | 19.5 | 12.3 | 17.08 | 54.2% | 31.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 325 | 34.8 | 23.1 | 32.9 | 5.8 | 2.5 | 0.9 | 0.0 | 4.14 | 3.4% | 0.9% |
| GAME_SPREAD | 394 | 20.3 | 16.5 | 36.3 | 16.0 | 9.1 | 1.3 | 0.5 | 6.5 | 10.9% | 1.8% |
| MATCH_WINNER | 5,786 | 13.3 | 9.4 | 20.0 | 14.7 | 20.4 | 13.8 | 8.4 | 12.23 | 42.6% | 22.3% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 1,686 | 21.9 | 13.5 | 29.9 | 17.4 | 13.8 | 2.8 | 0.7 | 7.06 | 17.2% | 3.4% |
| TOTAL_GAMES | 1,120 | 9.9 | 9.0 | 26.2 | 25.2 | 17.1 | 8.0 | 4.5 | 10.68 | 29.6% | 12.5% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 789 | 28.3 | 31.8 | 27.1 | 0.8 | 9.8 | 1.9 | 0.4 | 4.29 | 12.0% | 2.3% |
| GAME_SPREAD | 485 | 36.9 | 14.0 | 24.7 | 19.8 | 2.9 | 1.2 | 0.4 | 4.69 | 4.5% | 1.7% |
| TOTAL_GAMES | 1,173 | 4.5 | 4.5 | 32.2 | 41.4 | 10.9 | 2.6 | 3.8 | 10.8 | 17.3% | 6.4% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 789 | 24.2 | 17.5 | 33.6 | 8.9 | 10.0 | 4.8 | 1.0 | 5.9 | 15.8% | 5.8% |
| GAME_SPREAD | 485 | 16.7 | 10.3 | 25.8 | 24.3 | 16.3 | 4.7 | 1.9 | 9.62 | 22.9% | 6.6% |
| TOTAL_GAMES | 1,181 | 5.8 | 6.2 | 30.6 | 30.4 | 16.6 | 5.8 | 4.7 | 10.91 | 27.1% | 10.5% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4,360 | 44.4% | 25.8% | 12.99 | 33.1% | 14.0% | 9.98 |
| gen1_elo | 4,360 | 43.4% | 25.0% | 12.51 | 31.6% | 13.9% | 9.54 |
| gen1_sr | 4,360 | 53.2% | 31.2% | 16.3 | 43.7% | 19.9% | 13.0 |
| gen2 | 4,360 | 50.6% | 30.9% | 15.32 | 42.4% | 21.0% | 12.86 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 1,721 | 18.0 | 12.1 | 23.2 | 15.4 | 18.2 | 9.9 | 3.1 | 9.14 | 31.3% | 13.0% |
| STALE | 2,639 | 10.7 | 6.2 | 15.6 | 14.6 | 18.9 | 18.5 | 15.5 | 16.55 | 53.0% | 34.1% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,127 | 15.2 | 10.3 | 21.8 | 15.9 | 20.0 | 12.2 | 4.7 | 10.76 | 36.8% | 16.9% |
| STALE | 2,659 | 11.1 | 8.4 | 17.9 | 13.2 | 20.8 | 15.8 | 12.9 | 14.76 | 49.5% | 28.7% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 10,146 | 0 | 4848 | 5298 | 31.1 | 197.5 | 1400.4 |
| ge_15pp | 4,403 | 0 | 1690 | 2713 | 37.3 | 476.7 | 1380.4 |
| ge_25pp | 2,412 | 0 | 751 | 1661 | 51.9 | 624.9 | 1380.4 |
| lt_10pp | 4,245 | 0 | 2395 | 1850 | 28.1 | 55.5 | 1130.0 |

Current slate `SL-20261001T230505Z-324299e0`: 408 priced rows, quote age at build {'median': 28.7, 'max': 75.3}, freshness {'AGING': 280, 'STALE': 128}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 128 | 21.1 | 11.7 | 21.9 | 21.9 | 19.5 | 3.9 | 0.0 | 7.76 | 23.4% | 3.9% |
| MARKETS_AGREE | 8 | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.96 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 11 | 0.0 | 0.0 | 9.1 | 45.5 | 45.5 | 0.0 | 0.0 | 13.64 | 45.5% | 0.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 4,360 | 148 (3.4%) | 7.4% | 0.0% | {"EXTERNAL_STALE": 128, "AGREES_WITH_KALSHI": 11, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 1,936 | 35 (1.8%) | 14.3% | 0.0% | {"EXTERNAL_STALE": 30, "AGREES_WITH_KALSHI": 5} |
| fair_v1_ge_25pp | 1,123 | 5 (0.4%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 5} |
| fair_v1_ge_25pp_pregame_clean | 442 | 5 (1.1%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 5} |
| fair_v1_lt_10pp | 1,775 | 80 (4.5%) | 1.2% | 0.0% | {"EXTERNAL_STALE": 70, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1, "AGREES_WITH_KALSHI": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 864 | 11.9 | 7.5 | 18.4 | 15.4 | 20.8 | 15.1 | 10.9 | 13.77 | 46.8% | 25.9% |
| 4-10x | 598 | 12.2 | 9.5 | 18.6 | 14.2 | 18.1 | 16.4 | 11.0 | 13.36 | 45.5% | 27.4% |
| <2x | 2,371 | 15.1 | 9.3 | 19.4 | 15.3 | 17.6 | 13.3 | 10.1 | 11.95 | 40.9% | 23.4% |
| >=10x | 527 | 11.2 | 5.7 | 15.2 | 13.1 | 20.7 | 22.0 | 12.1 | 17.89 | 54.8% | 34.2% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 1,124 | 13.8 | 9.1 | 21.4 | 15.4 | 16.6 | 12.3 | 11.4 | 11.98 | 40.3% | 23.7% |
| 300-1000 | 1,085 | 13.6 | 7.8 | 17.1 | 15.9 | 20.0 | 15.4 | 10.1 | 13.67 | 45.5% | 25.5% |
| <300 | 1,085 | 8.8 | 5.9 | 14.6 | 12.4 | 22.3 | 22.3 | 13.6 | 18.88 | 58.2% | 35.9% |
| >=3000 | 1,066 | 18.2 | 11.3 | 21.2 | 15.8 | 15.7 | 10.5 | 7.3 | 9.96 | 33.5% | 17.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 173 | 0.5176 | 0.3875 | 0.3988 | +0.119 | -0.011 | 0.0195 ± 0.011 |
| ratio 4-10x | 128 | 0.5789 | 0.4469 | 0.4844 | +0.095 | -0.037 | 0.0103 ± 0.0125 |
| ratio <2x | 334 | 0.5309 | 0.4099 | 0.4671 | +0.064 | -0.057 | 0.0067 ± 0.0074 |
| ratio >=10x | 125 | 0.5455 | 0.3833 | 0.448 | +0.098 | -0.065 | 0.0182 ± 0.016 |
| thinner_sample 1000-3000 | 192 | 0.5378 | 0.4166 | 0.4635 | +0.074 | -0.047 | 0.0027 ± 0.0097 |
| thinner_sample 300-1000 | 223 | 0.5536 | 0.4309 | 0.4619 | +0.092 | -0.031 | 0.0079 ± 0.0091 |
| thinner_sample <300 | 258 | 0.5333 | 0.373 | 0.438 | +0.095 | -0.065 | 0.0211 ± 0.0106 |
| thinner_sample >=3000 | 87 | 0.5153 | 0.4225 | 0.4368 | +0.079 | -0.014 | 0.0171 ± 0.0117 |
| data_status ADEQUATE | 192 | 0.5226 | 0.4133 | 0.4531 | +0.070 | -0.040 | 0.0047 ± 0.009 |
| data_status LIMITED | 172 | 0.5581 | 0.4422 | 0.4942 | +0.064 | -0.052 | 0.0012 ± 0.0101 |
| data_status POOR | 396 | 0.5374 | 0.388 | 0.4318 | +0.106 | -0.044 | 0.0205 ± 0.008 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 126 | 0.1812 | 0.1821 | -0.0009 ± 0.0013 | 0.5362 | 0.5386 | 0.491 | 0.4763 | 0.5 | -0.088 ± 0.0413 | -0.01 (3) |
| 3-5 | 78 | 0.1675 | 0.1641 | +0.0034 ± 0.0038 | 0.5147 | 0.5017 | 0.5131 | 0.4721 | 0.4487 | -0.115 ± 0.0488 | 0.02 (1) |
| 5-10 | 164 | 0.194 | 0.1954 | -0.0014 ± 0.0052 | 0.5725 | 0.5745 | 0.5218 | 0.4471 | 0.4939 | -0.062 ± 0.035 | -0.02 (2) |
| 10-15 | 126 | 0.2155 | 0.2076 | +0.0080 ± 0.0102 | 0.6139 | 0.5959 | 0.5318 | 0.4077 | 0.4365 | -0.080 ± 0.0407 | -0.0633 (3) |
| 15-25 | 165 | 0.2129 | 0.2128 | +0.0001 ± 0.014 | 0.6137 | 0.6065 | 0.558 | 0.3611 | 0.4606 | -0.013 ± 0.0345 | -0.02 (4) |
| 25-40 | 80 | 0.2384 | 0.1762 | +0.0623 ± 0.0294 | 0.6668 | 0.5224 | 0.6041 | 0.2877 | 0.3375 | -0.086 ± 0.0443 | -0.01 (1) |
| 40+ | 21 | 0.2865 | 0.1302 | +0.1564 ± 0.0712 | 0.746 | 0.4159 | 0.6795 | 0.2345 | 0.2857 | -0.076 ± 0.0648 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 374 | 0.1644 | 0.1652 | -0.0008 ± 0.0007 | 0.492 | 0.4938 | 0.5053 | 0.4903 | 0.5241 | -0.033 ± 0.0221 | -0.0188 (8) |
| 3-5 | 236 | 0.1668 | 0.1659 | +0.0009 ± 0.0022 | 0.5103 | 0.502 | 0.4886 | 0.4484 | 0.4576 | -0.050 ± 0.0273 | 0.02 (1) |
| 5-10 | 533 | 0.179 | 0.1786 | +0.0005 ± 0.0027 | 0.5355 | 0.5311 | 0.4742 | 0.4009 | 0.4371 | -0.027 ± 0.0185 | -0.0133 (6) |
| 10-15 | 425 | 0.1923 | 0.1761 | +0.0162 ± 0.0051 | 0.5643 | 0.5164 | 0.48 | 0.356 | 0.3506 | -0.071 ± 0.0203 | -0.0633 (3) |
| 15-25 | 600 | 0.1905 | 0.1597 | +0.0308 ± 0.0065 | 0.5685 | 0.4725 | 0.4767 | 0.2794 | 0.2983 | -0.040 ± 0.016 | -0.017 (10) |
| 25-40 | 543 | 0.2125 | 0.0896 | +0.1229 ± 0.0081 | 0.6155 | 0.2989 | 0.4967 | 0.1797 | 0.1455 | -0.082 ± 0.0125 | -0.01 (1) |
| 40+ | 394 | 0.3648 | 0.0362 | +0.3286 ± 0.0104 | 0.9461 | 0.1532 | 0.6149 | 0.1018 | 0.0482 | -0.082 ± 0.0086 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 78 | 0.1735 | 0.176 | -0.0025 ± 0.0016 | 0.5197 | 0.5236 | 0.516 | 0.5015 | 0.5769 | -0.017 ± 0.0463 | -0.01 (1) |
| 3-5 | 60 | 0.2131 | 0.212 | +0.0012 ± 0.0048 | 0.607 | 0.612 | 0.4888 | 0.4497 | 0.45 | -0.077 ± 0.0631 | 0.02 (1) |
| 5-10 | 143 | 0.1851 | 0.1778 | +0.0073 ± 0.0054 | 0.5519 | 0.5331 | 0.5735 | 0.4976 | 0.4755 | -0.129 ± 0.0356 | -0.01 (3) |
| 10-15 | 136 | 0.219 | 0.2071 | +0.0119 ± 0.0099 | 0.6254 | 0.5992 | 0.5856 | 0.4607 | 0.4853 | -0.081 ± 0.0402 | -0.0667 (3) |
| 15-25 | 181 | 0.2176 | 0.196 | +0.0216 ± 0.013 | 0.6194 | 0.5658 | 0.5807 | 0.3841 | 0.4309 | -0.074 ± 0.0337 | -0.0167 (3) |
| 25-40 | 114 | 0.2582 | 0.1895 | +0.0688 ± 0.0251 | 0.7203 | 0.5524 | 0.6472 | 0.3389 | 0.3772 | -0.114 ± 0.0415 | -0.025 (2) |
| 40+ | 48 | 0.3647 | 0.1956 | +0.1691 ± 0.0647 | 0.9908 | 0.5767 | 0.7362 | 0.2401 | 0.3333 | -0.004 ± 0.0591 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 302 | 0.1514 | 0.1529 | -0.0015 ± 0.0007 | 0.4567 | 0.4601 | 0.5526 | 0.5381 | 0.5762 | -0.015 ± 0.0228 | -0.0217 (6) |
| 3-5 | 178 | 0.1727 | 0.1722 | +0.0005 ± 0.0024 | 0.5123 | 0.5184 | 0.5437 | 0.5045 | 0.5169 | -0.041 ± 0.0314 | 0.02 (1) |
| 5-10 | 472 | 0.175 | 0.173 | +0.0020 ± 0.0029 | 0.526 | 0.5152 | 0.5242 | 0.4489 | 0.4703 | -0.038 ± 0.0193 | -0.01 (4) |
| 10-15 | 455 | 0.1875 | 0.1748 | +0.0127 ± 0.0049 | 0.5537 | 0.5161 | 0.5226 | 0.3981 | 0.4198 | -0.040 ± 0.0199 | -0.0575 (4) |
| 15-25 | 604 | 0.2005 | 0.1581 | +0.0424 ± 0.0064 | 0.5871 | 0.4724 | 0.5077 | 0.3126 | 0.3063 | -0.076 ± 0.0162 | -0.0143 (7) |
| 25-40 | 578 | 0.2241 | 0.1121 | +0.1120 ± 0.0088 | 0.6476 | 0.3524 | 0.5358 | 0.2218 | 0.2042 | -0.076 ± 0.0141 | -0.015 (6) |
| 40+ | 516 | 0.4005 | 0.0635 | +0.3370 ± 0.0129 | 1.0492 | 0.2271 | 0.661 | 0.1228 | 0.093 | -0.061 ± 0.0105 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 121 | 0.1741 | 0.1763 | -0.0022 ± 0.0013 | 0.5172 | 0.5229 | 0.5105 | 0.4964 | 0.5455 | -0.041 ± 0.0387 | -0.01 (5) |
| 3-5 | 83 | 0.1657 | 0.1621 | +0.0035 ± 0.0036 | 0.5025 | 0.4936 | 0.5105 | 0.471 | 0.4458 | -0.136 ± 0.0475 | -- (0) |
| 5-10 | 154 | 0.1978 | 0.1974 | +0.0004 ± 0.0053 | 0.5862 | 0.5778 | 0.5062 | 0.4343 | 0.4675 | -0.062 ± 0.036 | -0.01 (2) |
| 10-15 | 136 | 0.2135 | 0.2118 | +0.0017 ± 0.0098 | 0.6145 | 0.6062 | 0.5524 | 0.4287 | 0.4926 | -0.058 ± 0.0397 | -0.044 (5) |
| 15-25 | 160 | 0.2156 | 0.2069 | +0.0087 ± 0.0139 | 0.6241 | 0.5945 | 0.5749 | 0.3812 | 0.4562 | -0.039 ± 0.0345 | -0.03 (1) |
| 25-40 | 90 | 0.2356 | 0.1841 | +0.0514 ± 0.0283 | 0.6636 | 0.5442 | 0.5998 | 0.2851 | 0.3556 | -0.071 ± 0.0425 | 0.0 (1) |
| 40+ | 16 | 0.2995 | 0.1454 | +0.1541 ± 0.0887 | 0.7771 | 0.4518 | 0.6921 | 0.2369 | 0.3125 | -0.064 ± 0.0806 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 358 | 0.1607 | 0.161 | -0.0003 ± 0.0007 | 0.4859 | 0.4867 | 0.5068 | 0.4924 | 0.514 | -0.042 ± 0.0214 | -0.0162 (13) |
| 3-5 | 241 | 0.1739 | 0.1703 | +0.0036 ± 0.0021 | 0.5187 | 0.509 | 0.4793 | 0.4401 | 0.4191 | -0.085 ± 0.0272 | -0.01 (2) |
| 5-10 | 528 | 0.1837 | 0.1799 | +0.0039 ± 0.0028 | 0.5486 | 0.5288 | 0.4629 | 0.3894 | 0.4034 | -0.042 ± 0.0185 | -0.01 (2) |
| 10-15 | 441 | 0.1941 | 0.1814 | +0.0126 ± 0.0051 | 0.5723 | 0.5318 | 0.495 | 0.3716 | 0.3832 | -0.057 ± 0.0203 | -0.03 (9) |
| 15-25 | 629 | 0.1817 | 0.1447 | +0.0370 ± 0.0061 | 0.5497 | 0.4381 | 0.4824 | 0.2837 | 0.2909 | -0.050 ± 0.0148 | -0.03 (2) |
| 25-40 | 540 | 0.2159 | 0.0967 | +0.1192 ± 0.0085 | 0.6252 | 0.3147 | 0.4967 | 0.1782 | 0.1519 | -0.078 ± 0.0129 | 0.0 (1) |
| 40+ | 368 | 0.381 | 0.0358 | +0.3452 ± 0.0109 | 0.9924 | 0.1535 | 0.6191 | 0.1011 | 0.038 | -0.091 ± 0.0088 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 403 | 0.2021 | 0.2021 | +0.0000 ± 0.0008 | 0.5845 | 0.5846 | 0.5014 | 0.4868 | 0.4864 | -0.044 ± 0.0225 | -0.0226 (46) |
| 3-5 | 285 | 0.1919 | 0.1914 | +0.0005 ± 0.0021 | 0.564 | 0.5593 | 0.4609 | 0.4211 | 0.4386 | -0.033 ± 0.0257 | -0.0059 (32) |
| 5-10 | 617 | 0.1868 | 0.1818 | +0.0050 ± 0.0026 | 0.5566 | 0.5428 | 0.4587 | 0.3854 | 0.389 | -0.042 ± 0.0172 | -0.0049 (71) |
| 10-15 | 409 | 0.2026 | 0.1904 | +0.0122 ± 0.0054 | 0.5948 | 0.5588 | 0.4568 | 0.3334 | 0.3447 | -0.041 ± 0.0214 | 0.0016 (63) |
| 15-25 | 551 | 0.2354 | 0.2099 | +0.0255 ± 0.0076 | 0.6644 | 0.6066 | 0.529 | 0.3359 | 0.3666 | -0.034 ± 0.0195 | -0.0216 (58) |
| 25-40 | 265 | 0.2623 | 0.1664 | +0.0959 ± 0.0157 | 0.7251 | 0.502 | 0.5718 | 0.2603 | 0.2604 | -0.066 ± 0.0247 | -0.0216 (25) |
| 40+ | 92 | 0.4281 | 0.1583 | +0.2698 ± 0.0445 | 1.2043 | 0.4894 | 0.7341 | 0.2267 | 0.2391 | -0.064 ± 0.043 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 750 | 0.1927 | 0.1923 | +0.0004 ± 0.0005 | 0.5625 | 0.5611 | 0.4971 | 0.4827 | 0.472 | -0.052 ± 0.016 | -0.0155 (82) |
| 3-5 | 526 | 0.1978 | 0.1965 | +0.0014 ± 0.0016 | 0.5753 | 0.5691 | 0.4673 | 0.4275 | 0.4316 | -0.041 ± 0.0194 | -0.018 (54) |
| 5-10 | 1129 | 0.1853 | 0.1788 | +0.0065 ± 0.0019 | 0.5532 | 0.5336 | 0.4435 | 0.3696 | 0.3667 | -0.045 ± 0.0127 | -0.0089 (121) |
| 10-15 | 832 | 0.198 | 0.1836 | +0.0144 ± 0.0037 | 0.5826 | 0.5409 | 0.4506 | 0.3271 | 0.3305 | -0.042 ± 0.0147 | -0.0053 (99) |
| 15-25 | 1163 | 0.2226 | 0.1878 | +0.0348 ± 0.005 | 0.641 | 0.5507 | 0.5028 | 0.3073 | 0.3156 | -0.044 ± 0.0127 | -0.0255 (106) |
| 25-40 | 797 | 0.2454 | 0.1299 | +0.1155 ± 0.0081 | 0.6922 | 0.4058 | 0.5302 | 0.215 | 0.1907 | -0.071 ± 0.0126 | -0.0206 (47) |
| 40+ | 470 | 0.3907 | 0.0809 | +0.3098 ± 0.0143 | 1.0669 | 0.2711 | 0.6549 | 0.1389 | 0.1085 | -0.075 ± 0.0134 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 760 | 1.166 ± 0.105 | 1.224 | 0.1721 | 0.1883 | 0.2041 | 0.1919 |
| gen2 | 760 | 0.966 ± 0.092 | 1.153 | 0.1886 | 0.1875 | 0.2222 | 0.1927 |
| gen1_elo | 760 | 1.13 ± 0.102 | 1.21 | 0.1779 | 0.1888 | 0.2037 | 0.1921 |
| gen1_sr | 760 | 1.172 ± 0.12 | 1.212 | 0.145 | 0.1898 | 0.2188 | 0.1919 |
| gen1_ledger | 2622 | 0.904 ± 0.053 | 1.073 | 0.1627 | 0.2009 | 0.2185 | 0.1908 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 4,403)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,428 | 32.4% |
| STALE_QUOTE | market_freshness | 1,252 | 28.4% |
| POOR_DATA | data | 365 | 8.3% |
| BOOK_QUALITY | execution | 297 | 6.8% |
| LIMITED_DATA | data | 273 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 268 | 6.1% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 221 | 5.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 213 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 83 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 3 | 0.1% |

Cause class: coverage 32.4%, market_freshness 28.4%, data 14.5%, market_freshness/coverage 10.9%, execution 6.8%, model_calibration_or_unknown 5.0%, mapping 1.9%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 94.3%, LOW_DATA_QUALITY 65.5%, STALE_KALSHI_QUOTE 61.6%, STALE_PLAYER_DATA 55.6%, THIN_PLAYER_HISTORY 53.1%, MODEL_INTERNAL_DISAGREEMENT 32.9%, ASYMMETRIC_SAMPLE_SIZE 29.0%, WIDE_SPREAD 15.5%, MODEL_HIGH_UNCERTAINTY 12.2%, PLAYER_IDENTITY_RISK 11.3%, LEVEL_TRANSFER_RISK 9.0%, EVENT_MAPPING_RISK 7.0%, LOW_DISPLAYED_LIQUIDITY 4.7%, MODEL_CALIBRATION_OUTLIER 2.2%, UNKNOWN 0.8%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 35.2%, POST_SETTLEMENT_OBSERVATION 32.4%, POSSIBLE_IN_PLAY_QUOTE 6.9%, CONFIRMED_IN_PLAY_QUOTE 2.5%

### >= ge_25 pp (N = 2,412)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,108 | 45.9% |
| STALE_QUOTE | market_freshness | 557 | 23.1% |
| POOR_DATA | data | 159 | 6.6% |
| BOOK_QUALITY | execution | 143 | 5.9% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 135 | 5.6% |
| IN_PLAY_QUOTE | market_freshness/coverage | 126 | 5.2% |
| LIMITED_DATA | data | 76 | 3.1% |
| IDENTITY_AMBIGUOUS | mapping | 58 | 2.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 50 | 2.1% |

Cause class: coverage 45.9%, market_freshness 23.1%, market_freshness/coverage 10.8%, data 9.7%, execution 5.9%, mapping 2.4%, model_calibration_or_unknown 2.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 96.7%, LOW_DATA_QUALITY 69.6%, STALE_KALSHI_QUOTE 68.9%, THIN_PLAYER_HISTORY 55.5%, STALE_PLAYER_DATA 53.4%, MODEL_INTERNAL_DISAGREEMENT 33.8%, ASYMMETRIC_SAMPLE_SIZE 31.4%, WIDE_SPREAD 14.1%, PLAYER_IDENTITY_RISK 14.1%, MODEL_HIGH_UNCERTAINTY 13.6%, EVENT_MAPPING_RISK 8.7%, LEVEL_TRANSFER_RISK 8.5%, LOW_DISPLAYED_LIQUIDITY 5.1%, MODEL_CALIBRATION_OUTLIER 3.1%, UNKNOWN 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 49.0%, POST_SETTLEMENT_OBSERVATION 45.9%, POSSIBLE_IN_PLAY_QUOTE 6.5%, CONFIRMED_IN_PLAY_QUOTE 2.8%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 2039, "IDENTITY_AMBIGUOUS": 373}; ticker orientation: {"VERIFIED": 2412}.

Checks: discipline:AMBIGUOUS 178, discipline:PASS 2234, identity_confidence:AMBIGUOUS 341, identity_confidence:PASS 2071, level_mapping:NA 190, level_mapping:PASS 2222, market_pair:AMBIGUOUS 62, market_pair:NA 66, market_pair:PASS 2284, model_complement:NA 39, model_complement:PASS 2373, namesake:PASS 2412, physical_match_id:NA 1289, physical_match_id:PASS 1123, player_ids:PASS 2412, same_pair_other_event:PASS 2412, ticker_orientation:PASS 2412

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 285 | 3.9% | 4.0% | 0.5% | {"market_freshness": 11} | 6.01 | 0.1838 / 0.1834 (45) | 35.4% | 0.0% | 0.7% | 4.6% |
| CHALLENGER | 1,540 | 18.8% | 8.3% | 12.0% | {"coverage": 153, "market_freshness": 67, "market_freshness/coverage": 37, "data": 17, "model_calibration_or_unknown": 12, "execution": 3} | 7.61 | 0.2245 / 0.2067 (513) | 52.1% | 4.3% | 0.7% | 22.4% |
| DOUBLES | 363 | 49.0% | 48.4% | 7.4% | {"market_freshness": 88, "market_freshness/coverage": 36, "execution": 28, "mapping": 20, "coverage": 6} | 24.11 | 0.3222 / 0.2257 (150) | 60.6% | 0.0% | 100.0% | 22.6% |
| ITF_MEN | 3,337 | 24.8% | 14.2% | 34.3% | {"coverage": 433, "market_freshness": 158, "data": 85, "execution": 71, "market_freshness/coverage": 70, "mapping": 10, "model_calibration_or_unknown": 1} | 9.84 | 0.2094 / 0.1835 (1221) | 54.4% | 50.9% | 5.7% | 31.6% |
| ITF_WOMEN | 3,311 | 29.0% | 17.1% | 39.8% | {"coverage": 504, "market_freshness": 195, "data": 116, "market_freshness/coverage": 76, "execution": 32, "mapping": 26, "model_calibration_or_unknown": 12} | 12.21 | 0.206 / 0.1861 (1089) | 57.2% | 54.9% | 6.7% | 32.6% |
| OTHER | 149 | 8.1% | 7.3% | 0.5% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 752 | 9.0% | 7.8% | 2.8% | {"market_freshness": 25, "market_freshness/coverage": 14, "model_calibration_or_unknown": 11, "data": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.61 | 0.1995 / 0.1973 (113) | 37.5% | 2.8% | 1.6% | 14.5% |
| WTA125 | 409 | 15.9% | 9.4% | 2.7% | {"market_freshness/coverage": 27, "model_calibration_or_unknown": 12, "market_freshness": 11, "data": 8, "coverage": 7} | 10.53 | 0.2278 / 0.204 (209) | 34.0% | 9.3% | 0.5% | 19.6% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 3 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 4 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 5 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 6 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 7 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 8 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 9 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 10 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 11 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 12 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 13 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 14 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 15 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 16 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 17 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 18 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 19 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 20 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 21 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 22 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 23 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 24 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 25 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 26 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 156 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 27 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 28 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 29 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 30 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 31 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | IN_PLAY_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | first-ball truth shows the match under way at the quote time; quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 32 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 114 min (STALE); data LIMITED (grade B, thinner serve sample 2163.0, ratio 2.0); no external reference |
| 33 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 407 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 34 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 35 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 36 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | IN_PLAY_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | first-ball truth shows the match under way at the quote time; quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 37 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |
| 38 | `KXITFWMATCH-26SEP30KOKUEM-KOK` | ITF_WOMEN | fair_v1 | 79% / 10% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 18.1h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 1101 min (STALE); data LIMITED (grade C, thinner serve sample 824.0, ratio 2.35); no external reference |
| 39 | `KXITFMATCH-26SEP20WILRAH-RAH` | ITF_MEN | gen1_ledger | 72% / 4% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade B, thinner serve sample 2782.0, ratio 1.84); no external reference |
| 40 | `KXITFMATCH-26SEP26NAGTHO-NAG` | ITF_MEN | gen1_ledger | 76% / 7% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 89 min (STALE); data LIMITED (grade C, thinner serve sample 1323.0, ratio 4.45); no external reference |
| 41 | `KXITFWMATCH-26SEP26PERPRE-PER` | ITF_WOMEN | gen1_ledger | 78% / 10% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 102 min (STALE); data POOR (grade D, thinner serve sample 1020.0, ratio 2.77); no external reference |
| 42 | `KXITFMATCH-26SEP22YILAGA-AGA` | ITF_MEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 203 min (STALE); data LIMITED (grade B, thinner serve sample 2786.0, ratio 2.08); no external reference |
| 43 | `KXITFMATCH-26SEP30DIMURA-URA` | ITF_MEN | fair_v1 | 71% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.5h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 819 min (STALE); data POOR (grade F, thinner serve sample 174.0, ratio 2.63); no external reference |
| 44 | `KXITFWMATCH-26OCT01TANVED-TAN` | ITF_WOMEN | fair_v1 | 76% / 8% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 8.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 492 min (STALE); no external reference |
| 45 | `KXITFWMATCH-26SEP20LLIBON-BON` | ITF_WOMEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 69 min (STALE); data POOR (grade D, thinner serve sample 1210.0, ratio 3.0); no external reference |
| 46 | `KXATPCHALLENGERDOUBLES-26SEP17ARESTEBLASCH-BLASCH` | DOUBLES | gen1_ledger | 95% / 28% | +67 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 79 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 47 | `KXITFWMATCH-26SEP24BOUKUR-BOU` | ITF_WOMEN | gen1_ledger | 76% / 8% | +67 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 113 min (STALE); data POOR (grade D, thinner serve sample 1497.0, ratio 2.48); no external reference |
| 48 | `KXATPCHALLENGERMATCH-26SEP28TABSAN-SAN` | CHALLENGER | gen1_ledger | 70% / 4% | +67 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 48 min (STALE); no external reference |
| 49 | `KXITFWMATCH-26SEP22SHCPAS-PAS` | ITF_WOMEN | gen1_ledger | 69% / 2% | +66 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 199 min (STALE); data POOR (grade F, thinner serve sample 239.0, ratio 5.93); no external reference |
| 50 | `KXITFWMATCH-26SEP29KRURAY-KRU` | ITF_WOMEN | fair_v1 | 78% / 12% | +66 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 126 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 223.0); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9672, "by_level_share_of_ge_25pp": {"ATP": 0.0046, "CHALLENGER": 0.1198, "DOUBLES": 0.0738, "ITF_MEN": 0.3433, "ITF_WOMEN": 0.3984, "OTHER": 0.005, "WTA": 0.0282, "WTA125": 0.0269}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.6886, "share_primary_cause_market_settled_or_in_play": 0.5676, "share_primary_cause_stale_quote_only": 0.2309}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 2412, "identity_ambiguous_share": 0.1546, "ticker_orientation": {"VERIFIED": 2412}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 1123, "with_external": 5, "coverage": 0.0045, "external_status": {"EXTERNAL_STALE": 5}, "triangulation": {"INSUFFICIENT_INPUTS": 5}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 442, "with_external": 5, "coverage": 0.0113, "external_status": {"EXTERNAL_STALE": 5}, "triangulation": {"INSUFFICIENT_INPUTS": 5}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 770.0, "median_sample_ratio": 2.35, "median_min_matches": 23.0, "median_max_days_since_last": 177.0, "share_severe_asymmetry": 0.1712, "data_status": {"POOR": 1148, "LIMITED": 828, "ADEQUATE": 436}, "comparison_lt_10pp": {"median_thinner_serve_points": 1948.5, "median_sample_ratio": 1.71, "median_min_matches": 77.5}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 173, "model_minus_observed": 0.1187, "kalshi_minus_observed": -0.0114, "brier_diff_model_minus_kalshi": 0.0195}, "4-10x": {"n": 128, "model_minus_observed": 0.0945, "kalshi_minus_observed": -0.0375, "brier_diff_model_minus_kalshi": 0.0103}, "<2x": {"n": 334, "model_minus_observed": 0.0638, "kalshi_minus_observed": -0.0572, "brier_diff_model_minus_kalshi": 0.0067}, ">=10x": {"n": 125, "model_minus_observed": 0.0975, "kalshi_minus_observed": -0.0647, "brier_diff_model_minus_kalshi": 0.0182}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 760, "model": {"intercept": -0.654, "slope": 0.966, "slope_se": 0.092}, "kalshi_mid_same_rows": {"intercept": 0.199, "slope": 1.153, "slope_se": 0.1}, "mean_extremity_model": 0.1886, "mean_extremity_kalshi": 0.1875, "model_brier": 0.2222, "kalshi_brier": 0.1927, "brier_diff_model_minus_kalshi": 0.0295, "brier_diff_se": 0.0068, "model_logloss": 0.6352, "kalshi_logloss": 0.5636}, "fair_v1": {"n": 760, "model": {"intercept": -0.449, "slope": 1.166, "slope_se": 0.105}, "kalshi_mid_same_rows": {"intercept": 0.317, "slope": 1.224, "slope_se": 0.103}, "mean_extremity_model": 0.1721, "mean_extremity_kalshi": 0.1883, "model_brier": 0.2041, "kalshi_brier": 0.1919, "brier_diff_model_minus_kalshi": 0.0121, "brier_diff_se": 0.0053, "model_logloss": 0.5911, "kalshi_logloss": 0.5617}, "gen1_elo": {"n": 760, "model": {"intercept": -0.421, "slope": 1.13, "slope_se": 0.102}, "kalshi_mid_same_rows": {"intercept": 0.33, "slope": 1.21, "slope_se": 0.101}, "mean_extremity_model": 0.1779, "mean_extremity_kalshi": 0.1888, "model_brier": 0.2037, "kalshi_brier": 0.1921, "brier_diff_model_minus_kalshi": 0.0116, "brier_diff_se": 0.0053, "model_logloss": 0.5923, "kalshi_logloss": 0.5618}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2576, "share_ge_15": 0.444, "median_abs_gap": 12.99, "n": 4360}, "gen1_elo": {"share_ge_25": 0.2502, "share_ge_15": 0.4339, "median_abs_gap": 12.51, "n": 4360}, "gen1_sr": {"share_ge_25": 0.3117, "share_ge_15": 0.5323, "median_abs_gap": 16.3, "n": 4360}, "gen2": {"share_ge_25": 0.3089, "share_ge_15": 0.5064, "median_abs_gap": 15.32, "n": 4360}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1401, "share_ge_15": 0.331, "median_abs_gap": 9.98, "n": 3154}, "gen1_elo": {"share_ge_25": 0.1389, "share_ge_15": 0.3161, "median_abs_gap": 9.54, "n": 3154}, "gen1_sr": {"share_ge_25": 0.1991, "share_ge_15": 0.4366, "median_abs_gap": 13.0, "n": 3154}, "gen2": {"share_ge_25": 0.2102, "share_ge_15": 0.4242, "median_abs_gap": 12.86, "n": 3154}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 6.01, "share_ge_25_all": 0.0386, "share_ge_25_pregame_clean": 0.0404}, "WTA": {"median_abs_gap_pregame_clean": 8.61, "share_ge_25_all": 0.0904, "share_ge_25_pregame_clean": 0.0778}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2243, "share_within_10pp_all": 0.4184, "share_within_10pp_pregame_clean": 0.4992, "corr_model_vs_mid_pregame_clean": 0.8335}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 126, "model_brier": 0.1812, "kalshi_brier": 0.1821, "brier_diff_model_minus_kalshi": -0.0009}, "10-15": {"n_settled": 126, "model_brier": 0.2155, "kalshi_brier": 0.2076, "brier_diff_model_minus_kalshi": 0.008}, "15-25": {"n_settled": 165, "model_brier": 0.2129, "kalshi_brier": 0.2128, "brier_diff_model_minus_kalshi": 0.0001}, "25-40": {"n_settled": 80, "model_brier": 0.2384, "kalshi_brier": 0.1762, "brier_diff_model_minus_kalshi": 0.0623}, "3-5": {"n_settled": 78, "model_brier": 0.1675, "kalshi_brier": 0.1641, "brier_diff_model_minus_kalshi": 0.0034}, "40+": {"n_settled": 21, "model_brier": 0.2865, "kalshi_brier": 0.1302, "brier_diff_model_minus_kalshi": 0.1564}, "5-10": {"n_settled": 164, "model_brier": 0.194, "kalshi_brier": 0.1954, "brier_diff_model_minus_kalshi": -0.0014}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%)
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap).
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 150, "model_brier": 0.3222, "kalshi_brier": 0.2257, "brier_diff_model_minus_kalshi": 0.0965, "brier_diff_se": 0.0268, "corr_model_outcome": -0.0804, "corr_kalshi_outcome": 0.3499}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
