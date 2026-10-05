# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-05T17:37Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 13,924): 0-3 13.1%, 3-5 9.0%, 5-10 18.8%, 10-15 15.1%, 15-25 19.4%, 25-40 15.1%, 40+ 9.6%; median gap 12.81 pp.
* **Where the extremes live**: 97.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 74.5%, Challenger 14.5%, doubles 5.5%). Main tour: ATP 4.3% and WTA 9.4% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 3,431): MARKET_ALREADY_SETTLED_WHEN_PRICED 45.6%, STALE_QUOTE 24.2%, BOOK_QUALITY 8.3%, POOR_DATA 6.1%, POSSIBLY_IN_PLAY_QUOTE 5.0%, IN_PLAY_QUOTE 3.3%, LIMITED_DATA 2.8%, IDENTITY_AMBIGUOUS 2.7%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.0%. By class: coverage 45.6%, market_freshness 24.2%, data 8.9%, execution 8.3%, market_freshness/coverage 8.3%, mapping 2.7%, model_calibration_or_unknown 2.0%, model_calibration 0.0%.
* **Stale / settled / in-play**: 69.1% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 53.9% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 3,431 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 15.9% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 0.6%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 12.3% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 725.0 points vs 1886.5 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.126, Gen-2 0.918, Gen-1 ledger 0.908 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 128 model 0.2287 vs Kalshi 0.1819; n 30 model 0.3354 vs Kalshi 0.1357.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%). Not implemented here.

## 1. Observations

* 47,095 model-market comparisons (81,547 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 19,456 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-05T17:33:48.557311+00:00'], shadow board 13,872 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-05T17:33:51.587785+00:00'], Model 4 3,957 rows, 8,690 settled tickers, 1,943 tickers with an external scan.
* By model: {"gen1_ledger": 11530, "gen1_elo": 6972, "fair_v1": 6972, "gen2": 6972, "gen1_sr": 6972, "model4_fundamental": 3843, "model4_conditioned": 3834}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 13,924 | 13.1 | 9.0 | 18.8 | 15.1 | 19.4 | 15.1 | 9.6 | 12.81 | 44.0% | 24.6% |
| MW fair_v1 | 6,972 | 12.9 | 8.5 | 17.7 | 15.4 | 18.5 | 15.8 | 11.2 | 13.37 | 45.5% | 27.0% |
| MW gen1_elo | 6,972 | 12.9 | 8.6 | 19.5 | 14.4 | 18.5 | 15.6 | 10.5 | 12.9 | 44.6% | 26.1% |
| MW gen1_ledger | 6,952 | 13.2 | 9.6 | 19.9 | 14.8 | 20.2 | 14.3 | 7.9 | 12.17 | 42.5% | 22.3% |
| MW gen1_sr | 6,972 | 9.4 | 7.2 | 15.9 | 13.7 | 21.8 | 19.0 | 13.0 | 16.56 | 53.8% | 32.0% |
| MW gen2 | 6,972 | 11.0 | 6.6 | 16.1 | 13.9 | 20.2 | 17.7 | 14.4 | 16.02 | 52.4% | 32.2% |
| all families model4_conditioned | 3,834 | 19.9 | 17.4 | 30.0 | 20.2 | 9.2 | 1.9 | 1.5 | 6.75 | 12.5% | 3.3% |
| all families model4_fundamental | 3,843 | 15.1 | 11.3 | 29.8 | 21.0 | 14.5 | 5.8 | 2.4 | 8.81 | 22.7% | 8.2% |

Configurable thresholds (primary): >=5pp 77.9%, >=10pp 59.1%, >=15pp 44.0%, >=20pp 33.6%, >=25pp 24.6%, >=30pp 18.1%, >=40pp 9.6%, >=50pp 4.2%
Executable gap (model outside the book, before fees): median 9.95pp; >=10pp 49.8%, >=25pp 21.2%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 394 | 21.1 | 17.3 | 24.4 | 15.5 | 16.0 | 3.0 | 2.8 | 6.89 | 21.8% | 5.8% |
| CHALLENGER | 1,486 | 15.1 | 10.4 | 16.6 | 15.8 | 15.1 | 14.0 | 13.1 | 12.75 | 42.2% | 27.1% |
| ITF_MEN | 1,958 | 11.6 | 8.2 | 18.5 | 14.7 | 18.1 | 15.7 | 13.2 | 13.52 | 46.9% | 28.9% |
| ITF_WOMEN | 2,561 | 9.6 | 6.1 | 15.2 | 15.4 | 21.3 | 20.7 | 11.7 | 16.57 | 53.6% | 32.4% |
| WTA | 447 | 22.8 | 10.5 | 25.3 | 13.2 | 18.8 | 6.9 | 2.5 | 8.22 | 28.2% | 9.4% |
| WTA125 | 126 | 14.3 | 4.8 | 19.8 | 27.8 | 15.9 | 11.1 | 6.3 | 11.65 | 33.3% | 17.5% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 394 | 19.8 | 13.4 | 24.9 | 15.5 | 18.0 | 5.1 | 3.3 | 7.84 | 26.4% | 8.4% |
| CHALLENGER | 1,486 | 13.7 | 6.1 | 18.1 | 14.2 | 18.9 | 16.3 | 12.7 | 14.17 | 47.9% | 28.9% |
| ITF_MEN | 1,958 | 9.0 | 6.7 | 17.2 | 15.2 | 19.7 | 17.5 | 14.7 | 15.59 | 51.8% | 32.2% |
| ITF_WOMEN | 2,561 | 8.2 | 6.0 | 12.7 | 11.9 | 21.2 | 20.8 | 19.2 | 19.96 | 61.2% | 40.0% |
| WTA | 447 | 20.4 | 5.6 | 16.6 | 15.7 | 22.1 | 17.2 | 2.5 | 13.07 | 41.8% | 19.7% |
| WTA125 | 126 | 6.3 | 4.0 | 16.7 | 18.2 | 24.6 | 17.5 | 12.7 | 16.94 | 54.8% | 30.2% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 394 | 25.9 | 12.2 | 28.9 | 12.9 | 9.4 | 7.6 | 3.0 | 7.44 | 20.1% | 10.7% |
| CHALLENGER | 1,486 | 15.7 | 9.9 | 21.7 | 13.1 | 13.2 | 13.2 | 13.3 | 10.95 | 39.6% | 26.5% |
| ITF_MEN | 1,958 | 10.1 | 9.0 | 17.8 | 15.0 | 19.2 | 15.8 | 13.1 | 14.0 | 48.2% | 28.9% |
| ITF_WOMEN | 2,561 | 9.5 | 6.3 | 15.9 | 14.1 | 23.7 | 20.5 | 10.1 | 17.19 | 54.3% | 30.6% |
| WTA | 447 | 22.8 | 14.1 | 30.4 | 15.7 | 11.2 | 4.2 | 1.6 | 6.99 | 17.0% | 5.8% |
| WTA125 | 126 | 17.5 | 4.8 | 23.8 | 26.2 | 19.1 | 7.1 | 1.6 | 11.11 | 27.8% | 8.7% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 140 | 26.4 | 20.7 | 35.7 | 13.6 | 3.6 | 0.0 | 0.0 | 5.52 | 3.6% | 0.0% |
| CHALLENGER | 1,024 | 20.6 | 14.7 | 25.8 | 15.5 | 14.0 | 6.7 | 2.7 | 7.45 | 23.4% | 9.5% |
| DOUBLES | 398 | 5.5 | 3.8 | 10.6 | 10.8 | 22.1 | 20.9 | 26.4 | 23.92 | 69.3% | 47.2% |
| ITF_MEN | 2,218 | 14.0 | 9.0 | 18.7 | 14.1 | 20.7 | 14.2 | 9.4 | 12.55 | 44.3% | 23.6% |
| ITF_WOMEN | 2,298 | 8.8 | 8.1 | 17.0 | 14.5 | 23.9 | 19.6 | 8.2 | 15.77 | 51.7% | 27.8% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 375 | 16.5 | 9.1 | 25.9 | 21.6 | 17.6 | 8.5 | 0.8 | 9.56 | 26.9% | 9.3% |
| WTA125 | 350 | 13.4 | 9.7 | 21.7 | 17.7 | 22.0 | 11.7 | 3.7 | 11.23 | 37.4% | 15.4% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 393 | 20.9 | 17.3 | 24.4 | 15.5 | 16.0 | 3.0 | 2.8 | 6.9 | 21.9% | 5.9% |
| CHALLENGER | 1,061 | 19.4 | 12.8 | 20.4 | 18.5 | 16.6 | 8.2 | 4.0 | 9.19 | 28.8% | 12.2% |
| ITF_MEN | 1,283 | 15.0 | 11.3 | 22.8 | 16.2 | 18.6 | 10.8 | 5.2 | 10.21 | 34.6% | 16.1% |
| ITF_WOMEN | 1,768 | 12.5 | 7.9 | 18.1 | 17.6 | 22.8 | 16.6 | 4.4 | 13.32 | 43.8% | 21.0% |
| WTA | 446 | 22.9 | 10.5 | 25.3 | 13.2 | 18.8 | 6.7 | 2.5 | 8.2 | 28.0% | 9.2% |
| WTA125 | 120 | 15.0 | 5.0 | 20.8 | 29.2 | 15.8 | 10.0 | 4.2 | 11.47 | 30.0% | 14.2% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 393 | 19.9 | 13.2 | 24.9 | 15.5 | 18.1 | 5.1 | 3.3 | 7.92 | 26.5% | 8.4% |
| CHALLENGER | 1,061 | 17.4 | 7.6 | 22.3 | 17.5 | 20.0 | 11.6 | 3.5 | 10.66 | 35.1% | 15.1% |
| ITF_MEN | 1,283 | 11.8 | 8.3 | 21.0 | 17.7 | 20.8 | 13.5 | 6.9 | 12.28 | 41.1% | 20.3% |
| ITF_WOMEN | 1,768 | 10.1 | 7.6 | 14.1 | 11.8 | 24.1 | 19.3 | 12.9 | 17.2 | 56.4% | 32.2% |
| WTA | 446 | 20.4 | 5.6 | 16.6 | 15.7 | 22.2 | 17.0 | 2.5 | 13.03 | 41.7% | 19.5% |
| WTA125 | 120 | 6.7 | 4.2 | 16.7 | 19.2 | 25.8 | 18.3 | 9.2 | 16.0 | 53.3% | 27.5% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 130 | 26.9 | 22.3 | 36.1 | 13.8 | 0.8 | 0.0 | 0.0 | 5.36 | 0.8% | 0.0% |
| CHALLENGER | 837 | 22.6 | 17.2 | 28.6 | 15.3 | 13.4 | 2.9 | 0.1 | 6.72 | 16.4% | 3.0% |
| DOUBLES | 359 | 5.6 | 3.6 | 10.9 | 10.9 | 22.0 | 21.2 | 25.9 | 23.92 | 69.1% | 47.1% |
| ITF_MEN | 1,606 | 16.9 | 10.7 | 21.6 | 15.3 | 20.7 | 10.9 | 3.9 | 10.18 | 35.5% | 14.8% |
| ITF_WOMEN | 1,629 | 10.3 | 9.4 | 20.1 | 16.3 | 24.7 | 16.9 | 2.2 | 12.83 | 43.8% | 19.1% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 346 | 16.8 | 9.5 | 26.6 | 22.2 | 18.2 | 6.7 | 0.0 | 9.5 | 24.9% | 6.7% |
| WTA125 | 271 | 15.9 | 10.7 | 25.8 | 21.0 | 20.3 | 5.9 | 0.4 | 9.33 | 26.6% | 6.3% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 398 | 5.5 | 3.8 | 10.6 | 10.8 | 22.1 | 20.9 | 26.4 | 23.92 | 69.3% | 47.2% |
| singles | 6,554 | 13.7 | 9.9 | 20.5 | 15.0 | 20.1 | 13.9 | 6.8 | 11.79 | 40.9% | 20.8% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 1,571 | 14.5 | 9.0 | 17.6 | 15.3 | 16.5 | 14.1 | 12.9 | 12.8 | 43.5% | 27.0% |
| Hard | 4,821 | 12.5 | 8.6 | 18.1 | 15.1 | 19.3 | 15.8 | 10.5 | 13.45 | 45.7% | 26.4% |
| UNKNOWN | 580 | 12.1 | 6.2 | 14.1 | 17.8 | 17.6 | 20.2 | 12.1 | 14.79 | 49.8% | 32.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 2,100 | 16.8 | 10.3 | 19.8 | 15.7 | 16.7 | 11.4 | 9.4 | 10.83 | 37.5% | 20.8% |
| B | 992 | 15.9 | 10.5 | 17.7 | 17.4 | 16.4 | 10.6 | 11.4 | 11.36 | 38.4% | 22.0% |
| C | 1,045 | 12.8 | 9.7 | 21.1 | 13.9 | 16.2 | 15.4 | 11.0 | 12.62 | 42.6% | 26.4% |
| D | 1,242 | 11.2 | 8.0 | 16.6 | 14.9 | 21.7 | 15.8 | 11.9 | 14.55 | 49.4% | 27.7% |
| F | 1,593 | 7.4 | 4.6 | 13.6 | 15.0 | 21.3 | 25.2 | 13.0 | 19.48 | 59.5% | 38.2% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 2,101 | 19.0 | 12.5 | 25.9 | 16.9 | 15.8 | 6.9 | 3.0 | 8.39 | 25.7% | 9.9% |
| B | 1,093 | 13.5 | 9.6 | 21.6 | 15.8 | 19.9 | 12.3 | 7.1 | 11.56 | 39.4% | 19.5% |
| C | 1,361 | 11.0 | 8.7 | 15.7 | 14.2 | 22.5 | 15.4 | 12.4 | 15.17 | 50.3% | 27.9% |
| D | 1,075 | 11.2 | 8.4 | 20.9 | 12.0 | 23.7 | 16.0 | 7.8 | 13.79 | 47.5% | 23.8% |
| F | 1,322 | 7.6 | 6.7 | 12.6 | 13.4 | 22.5 | 25.3 | 11.9 | 18.82 | 59.7% | 37.2% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 2,584 | 16.3 | 9.6 | 18.9 | 16.2 | 16.7 | 11.5 | 10.6 | 11.3 | 38.9% | 22.2% |
| LIMITED | 1,533 | 14.2 | 11.3 | 20.9 | 14.6 | 15.8 | 13.4 | 9.7 | 11.32 | 38.9% | 23.1% |
| POOR | 2,855 | 9.1 | 6.0 | 14.8 | 15.0 | 21.6 | 21.0 | 12.5 | 17.39 | 55.1% | 33.5% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 605 | 32.7 | 24.5 | 35.2 | 5.3 | 1.8 | 0.5 | 0.0 | 4.35 | 2.3% | 0.5% |
| GAME_SPREAD | 590 | 22.0 | 16.4 | 35.6 | 17.1 | 7.5 | 0.8 | 0.5 | 6.2 | 8.8% | 1.4% |
| MATCH_WINNER | 6,952 | 13.2 | 9.6 | 19.9 | 14.8 | 20.2 | 14.3 | 7.9 | 12.17 | 42.5% | 22.3% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 2,014 | 24.6 | 14.8 | 30.7 | 15.4 | 11.5 | 2.3 | 0.6 | 6.37 | 14.4% | 2.9% |
| TOTAL_GAMES | 1,345 | 9.2 | 9.4 | 29.7 | 25.4 | 15.7 | 6.7 | 3.9 | 10.31 | 26.3% | 10.6% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,388 | 27.1 | 33.3 | 24.6 | 0.5 | 12.9 | 1.2 | 0.4 | 4.32 | 14.5% | 1.7% |
| GAME_SPREAD | 809 | 38.9 | 15.0 | 26.8 | 15.3 | 2.0 | 1.5 | 0.5 | 4.26 | 4.0% | 2.0% |
| TOTAL_GAMES | 1,637 | 4.3 | 5.2 | 36.2 | 39.2 | 9.6 | 2.6 | 2.8 | 10.4 | 15.0% | 5.4% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,388 | 24.6 | 15.8 | 31.5 | 9.6 | 11.2 | 6.1 | 1.1 | 6.06 | 18.4% | 7.2% |
| GAME_SPREAD | 809 | 17.8 | 10.6 | 25.1 | 23.4 | 15.7 | 5.6 | 1.9 | 9.46 | 23.1% | 7.4% |
| TOTAL_GAMES | 1,646 | 5.8 | 7.7 | 30.7 | 29.5 | 16.7 | 5.8 | 3.7 | 10.71 | 26.2% | 9.5% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 6,972 | 45.5% | 27.0% | 13.37 | 34.9% | 15.6% | 10.52 |
| gen1_elo | 6,972 | 44.6% | 26.1% | 12.9 | 33.6% | 15.4% | 9.83 |
| gen1_sr | 6,972 | 53.8% | 32.0% | 16.56 | 44.2% | 20.7% | 13.28 |
| gen2 | 6,972 | 52.4% | 32.2% | 16.02 | 44.4% | 22.6% | 13.04 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 2,603 | 16.6 | 11.9 | 21.9 | 15.9 | 18.9 | 11.0 | 3.7 | 9.95 | 33.6% | 14.7% |
| STALE | 4,369 | 10.7 | 6.5 | 15.2 | 15.0 | 18.3 | 18.7 | 15.7 | 16.5 | 52.6% | 34.4% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 420 | 14.5 | 9.5 | 23.3 | 15.5 | 16.7 | 17.4 | 3.1 | 10.49 | 37.1% | 20.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 13,924 | 420 | 6075 | 7429 | 31.2 | 225.4 | 1400.4 |
| ge_15pp | 6,129 | 156 | 2164 | 3809 | 38.2 | 466.9 | 1380.4 |
| ge_25pp | 3,431 | 86 | 973 | 2372 | 52.2 | 596.1 | 1380.4 |
| lt_10pp | 5,695 | 199 | 2945 | 2551 | 28.5 | 59.2 | 1201.9 |

Current slate `SL-20261005T173733Z-59631da8`: 884 priced rows, quote age at build {'median': 9.2, 'max': 9.2}, freshness {'FRESH': 884}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 179 | 21.8 | 12.3 | 21.8 | 21.2 | 16.8 | 5.6 | 0.6 | 7.39 | 22.9% | 6.2% |
| MARKETS_AGREE | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.02 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 27 | 0.0 | 7.4 | 37.0 | 29.6 | 22.2 | 3.7 | 0.0 | 10.8 | 25.9% | 3.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 6,972 | 219 (3.1%) | 12.3% | 0.0% | {"EXTERNAL_STALE": 179, "AGREES_WITH_KALSHI": 27, "ALL_AGREE": 12, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 3,174 | 48 (1.5%) | 14.6% | 0.0% | {"EXTERNAL_STALE": 41, "AGREES_WITH_KALSHI": 7} |
| fair_v1_ge_25pp | 1,883 | 12 (0.6%) | 8.3% | 0.0% | {"EXTERNAL_STALE": 11, "AGREES_WITH_KALSHI": 1} |
| fair_v1_ge_25pp_pregame_clean | 789 | 12 (1.5%) | 8.3% | 0.0% | {"EXTERNAL_STALE": 11, "AGREES_WITH_KALSHI": 1} |
| fair_v1_lt_10pp | 2,727 | 125 (4.6%) | 9.6% | 0.0% | {"EXTERNAL_STALE": 100, "ALL_AGREE": 12, "AGREES_WITH_KALSHI": 12, "EXTERNAL_OUTLIER": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 1,399 | 11.9 | 7.7 | 19.9 | 15.9 | 20.1 | 14.7 | 9.7 | 12.82 | 44.5% | 24.4% |
| 4-10x | 958 | 12.4 | 10.7 | 16.6 | 14.8 | 17.2 | 17.9 | 10.4 | 13.67 | 45.5% | 28.3% |
| <2x | 3,745 | 14.1 | 9.1 | 17.9 | 15.4 | 18.1 | 13.9 | 11.4 | 12.8 | 43.4% | 25.3% |
| >=10x | 870 | 10.0 | 4.7 | 14.1 | 14.9 | 19.2 | 23.6 | 13.4 | 18.08 | 56.2% | 37.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 1,872 | 13.8 | 8.7 | 19.9 | 15.9 | 16.7 | 12.6 | 12.4 | 12.14 | 41.6% | 24.9% |
| 300-1000 | 1,621 | 12.9 | 8.7 | 16.5 | 15.6 | 20.4 | 15.6 | 10.3 | 13.67 | 46.3% | 25.9% |
| <300 | 1,849 | 8.2 | 5.5 | 14.0 | 14.3 | 21.0 | 23.7 | 13.4 | 18.92 | 58.1% | 37.0% |
| >=3000 | 1,630 | 17.2 | 11.5 | 20.5 | 15.7 | 15.9 | 10.8 | 8.3 | 10.26 | 35.0% | 19.1% |

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
| 0-3 | 559 | 0.1645 | 0.1657 | -0.0012 ± 0.0006 | 0.4964 | 0.4988 | 0.5023 | 0.4875 | 0.5313 | -0.017 ± 0.0177 | -0.0188 (8) |
| 3-5 | 360 | 0.1694 | 0.1689 | +0.0006 ± 0.0018 | 0.5138 | 0.5073 | 0.477 | 0.437 | 0.4528 | -0.043 ± 0.022 | 0.02 (1) |
| 5-10 | 809 | 0.1787 | 0.1785 | +0.0001 ± 0.0022 | 0.5369 | 0.5337 | 0.4765 | 0.4027 | 0.4363 | -0.025 ± 0.015 | -0.0129 (7) |
| 10-15 | 707 | 0.1834 | 0.1705 | +0.0128 ± 0.0038 | 0.5465 | 0.5039 | 0.4697 | 0.3462 | 0.355 | -0.052 ± 0.0155 | -0.0633 (3) |
| 15-25 | 912 | 0.1959 | 0.1612 | +0.0347 ± 0.0053 | 0.5803 | 0.4792 | 0.4791 | 0.2808 | 0.2928 | -0.048 ± 0.0132 | -0.017 (10) |
| 25-40 | 881 | 0.2109 | 0.0963 | +0.1146 ± 0.0066 | 0.6139 | 0.314 | 0.5064 | 0.1904 | 0.1691 | -0.073 ± 0.0101 | -0.01 (1) |
| 40+ | 647 | 0.3736 | 0.0319 | +0.3418 ± 0.0076 | 0.9715 | 0.145 | 0.6162 | 0.1024 | 0.0355 | -0.096 ± 0.0064 | -- (0) |

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
| 0-3 | 447 | 0.1533 | 0.1548 | -0.0016 ± 0.0006 | 0.4669 | 0.4701 | 0.527 | 0.5123 | 0.5526 | -0.009 ± 0.0188 | -0.0217 (6) |
| 3-5 | 301 | 0.1683 | 0.1656 | +0.0028 ± 0.0019 | 0.5026 | 0.4994 | 0.5259 | 0.4862 | 0.4718 | -0.066 ± 0.024 | 0.02 (1) |
| 5-10 | 735 | 0.1705 | 0.1718 | -0.0013 ± 0.0023 | 0.5152 | 0.5148 | 0.5186 | 0.4435 | 0.4844 | -0.016 ± 0.0155 | -0.01 (5) |
| 10-15 | 636 | 0.1879 | 0.1758 | +0.0121 ± 0.0041 | 0.5585 | 0.5178 | 0.5095 | 0.3857 | 0.4057 | -0.043 ± 0.0168 | -0.0575 (4) |
| 15-25 | 998 | 0.2036 | 0.1598 | +0.0438 ± 0.0051 | 0.5958 | 0.4775 | 0.5137 | 0.3164 | 0.3086 | -0.076 ± 0.0127 | -0.0143 (7) |
| 25-40 | 923 | 0.2297 | 0.1187 | +0.1110 ± 0.0072 | 0.662 | 0.3701 | 0.54 | 0.2233 | 0.208 | -0.070 ± 0.0116 | -0.015 (6) |
| 40+ | 835 | 0.4117 | 0.0539 | +0.3578 ± 0.0093 | 1.076 | 0.2051 | 0.661 | 0.122 | 0.0719 | -0.083 ± 0.0076 | -0.01 (1) |

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
| 0-3 | 569 | 0.1716 | 0.1719 | -0.0002 ± 0.0006 | 0.5143 | 0.5151 | 0.5051 | 0.4905 | 0.4991 | -0.050 ± 0.0173 | -0.0162 (13) |
| 3-5 | 388 | 0.1668 | 0.1628 | +0.0040 ± 0.0016 | 0.5047 | 0.4943 | 0.4897 | 0.4503 | 0.4253 | -0.086 ± 0.0208 | -0.01 (2) |
| 5-10 | 823 | 0.183 | 0.1757 | +0.0073 ± 0.0022 | 0.5481 | 0.5222 | 0.4628 | 0.3892 | 0.3767 | -0.068 ± 0.0147 | -0.01 (3) |
| 10-15 | 666 | 0.1883 | 0.1777 | +0.0106 ± 0.0041 | 0.5582 | 0.526 | 0.4818 | 0.3582 | 0.3784 | -0.043 ± 0.0164 | -0.03 (9) |
| 15-25 | 969 | 0.1851 | 0.1493 | +0.0358 ± 0.005 | 0.5582 | 0.4499 | 0.4854 | 0.2857 | 0.2962 | -0.048 ± 0.0122 | -0.03 (2) |
| 25-40 | 854 | 0.2103 | 0.0962 | +0.1140 ± 0.0067 | 0.6133 | 0.3111 | 0.5016 | 0.1825 | 0.1651 | -0.071 ± 0.0102 | 0.0 (1) |
| 40+ | 606 | 0.3901 | 0.0333 | +0.3568 ± 0.0084 | 1.0172 | 0.1491 | 0.6246 | 0.1024 | 0.033 | -0.098 ± 0.0069 | -- (0) |

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

### >= ge_15 pp (N = 6,129)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,986 | 32.4% |
| STALE_QUOTE | market_freshness | 1,816 | 29.6% |
| BOOK_QUALITY | execution | 576 | 9.4% |
| POOR_DATA | data | 482 | 7.9% |
| LIMITED_DATA | data | 337 | 5.5% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 324 | 5.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 282 | 4.6% |
| IN_PLAY_QUOTE | market_freshness/coverage | 191 | 3.1% |
| IDENTITY_AMBIGUOUS | mapping | 129 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 6 | 0.1% |

Cause class: coverage 32.4%, market_freshness 29.6%, data 13.4%, execution 9.4%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.6%, mapping 2.1%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 94.8%, LOW_DATA_QUALITY 65.1%, STALE_KALSHI_QUOTE 62.2%, THIN_PLAYER_HISTORY 54.4%, STALE_PLAYER_DATA 53.0%, MODEL_INTERNAL_DISAGREEMENT 35.0%, ASYMMETRIC_SAMPLE_SIZE 29.6%, WIDE_SPREAD 18.1%, MODEL_HIGH_UNCERTAINTY 14.5%, PLAYER_IDENTITY_RISK 11.1%, LEVEL_TRANSFER_RISK 8.3%, EVENT_MAPPING_RISK 6.3%, LOW_DISPLAYED_LIQUIDITY 5.8%, MODEL_CALIBRATION_OUTLIER 1.9%, UNKNOWN 0.7%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 34.8%, POST_SETTLEMENT_OBSERVATION 32.4%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 1.0%

### >= ge_25 pp (N = 3,431)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,565 | 45.6% |
| STALE_QUOTE | market_freshness | 830 | 24.2% |
| BOOK_QUALITY | execution | 284 | 8.3% |
| POOR_DATA | data | 209 | 6.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 172 | 5.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 112 | 3.3% |
| LIMITED_DATA | data | 96 | 2.8% |
| IDENTITY_AMBIGUOUS | mapping | 92 | 2.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 70 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 1 | 0.0% |

Cause class: coverage 45.6%, market_freshness 24.2%, data 8.9%, execution 8.3%, market_freshness/coverage 8.3%, mapping 2.7%, model_calibration_or_unknown 2.0%, model_calibration 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 97.1%, STALE_KALSHI_QUOTE 69.1%, LOW_DATA_QUALITY 68.6%, THIN_PLAYER_HISTORY 56.8%, STALE_PLAYER_DATA 50.5%, MODEL_INTERNAL_DISAGREEMENT 36.7%, ASYMMETRIC_SAMPLE_SIZE 32.6%, WIDE_SPREAD 16.7%, MODEL_HIGH_UNCERTAINTY 15.7%, PLAYER_IDENTITY_RISK 13.9%, LEVEL_TRANSFER_RISK 8.1%, EVENT_MAPPING_RISK 7.5%, LOW_DISPLAYED_LIQUIDITY 6.3%, MODEL_CALIBRATION_OUTLIER 2.8%, UNKNOWN 0.2%, EXTERNAL_MARKET_REJECTION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 48.1%, POST_SETTLEMENT_OBSERVATION 45.6%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 1.1%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 2886, "IDENTITY_AMBIGUOUS": 545}; ticker orientation: {"VERIFIED": 3431}.

Checks: discipline:AMBIGUOUS 188, discipline:PASS 3243, identity_confidence:AMBIGUOUS 476, identity_confidence:PASS 2955, level_mapping:NA 200, level_mapping:PASS 3231, market_pair:AMBIGUOUS 99, market_pair:NA 89, market_pair:PASS 3243, model_complement:NA 58, model_complement:PASS 3373, namesake:PASS 3431, physical_match_id:NA 1548, physical_match_id:PASS 1883, player_ids:PASS 3431, same_pair_other_event:PASS 3431, ticker_orientation:PASS 3431

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 534 | 4.3% | 4.4% | 0.7% | {"market_freshness": 20, "execution": 3} | 6.31 | 0.1791 / 0.1823 (49) | 36.9% | 0.4% | 3.0% | 2.1% |
| CHALLENGER | 2,510 | 19.9% | 8.2% | 14.5% | {"coverage": 287, "market_freshness": 102, "market_freshness/coverage": 57, "data": 27, "model_calibration_or_unknown": 21, "execution": 5} | 7.63 | 0.2196 / 0.2044 (688) | 56.2% | 5.9% | 1.3% | 24.4% |
| DOUBLES | 398 | 47.2% | 47.1% | 5.5% | {"market_freshness": 106, "execution": 33, "mapping": 30, "market_freshness/coverage": 12, "coverage": 7} | 23.92 | 0.3208 / 0.2301 (163) | 58.8% | 0.0% | 100.0% | 9.8% |
| ITF_MEN | 4,176 | 26.1% | 15.4% | 31.7% | {"coverage": 566, "market_freshness": 205, "execution": 129, "data": 97, "market_freshness/coverage": 78, "mapping": 12, "model_calibration_or_unknown": 1} | 10.19 | 0.2148 / 0.1879 (1384) | 54.1% | 51.7% | 6.3% | 30.8% |
| ITF_WOMEN | 4,859 | 30.2% | 20.1% | 42.8% | {"coverage": 688, "market_freshness": 348, "data": 161, "execution": 105, "market_freshness/coverage": 97, "mapping": 48, "model_calibration_or_unknown": 21} | 13.11 | 0.203 / 0.185 (1363) | 57.4% | 60.0% | 9.6% | 30.1% |
| OTHER | 149 | 8.1% | 7.3% | 0.4% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 822 | 9.4% | 8.1% | 2.2% | {"market_freshness": 34, "model_calibration_or_unknown": 13, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "model_calibration": 1, "mapping": 1} | 8.55 | 0.2006 / 0.1964 (129) | 39.3% | 2.5% | 1.5% | 3.6% |
| WTA125 | 476 | 16.0% | 8.7% | 2.2% | {"market_freshness/coverage": 30, "market_freshness": 13, "model_calibration_or_unknown": 12, "coverage": 12, "data": 9} | 10.15 | 0.2273 / 0.204 (221) | 35.7% | 8.0% | 2.3% | 17.9% |

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
| 8 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
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
| 25 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 26 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 27 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 28 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 29 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 687 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 30 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 31 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 32 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 708 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 33 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 34 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 35 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 36 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 37 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.9h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 671 min (STALE); no external reference |
| 39 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 407 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 40 | `KXWTAMATCH-26OCT01YASCHW-CHW` | WTA | fair_v1 | 73% / 2% | +70 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 51 min (STALE); no external reference |
| 41 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 42 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 43 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 44 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |
| 45 | `KXATPCHALLENGERMATCH-26OCT05CASMUN-CAS` | CHALLENGER | fair_v1 | 83% / 14% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 103 min (STALE); data POOR (grade D, thinner serve sample 814.0, ratio 3.93); no external reference |
| 46 | `KXITFWMATCH-26SEP30KOKUEM-KOK` | ITF_WOMEN | fair_v1 | 79% / 10% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 553 min (STALE); data LIMITED (grade C, thinner serve sample 824.0, ratio 2.35); no external reference |
| 47 | `KXITFMATCH-26SEP20WILRAH-RAH` | ITF_MEN | gen1_ledger | 72% / 4% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade B, thinner serve sample 2782.0, ratio 1.84); no external reference |
| 48 | `KXITFMATCH-26SEP26NAGTHO-NAG` | ITF_MEN | gen1_ledger | 76% / 7% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 89 min (STALE); data LIMITED (grade C, thinner serve sample 1323.0, ratio 4.45); no external reference |
| 49 | `KXITFWMATCH-26SEP26PERPRE-PER` | ITF_WOMEN | gen1_ledger | 78% / 10% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 102 min (STALE); data POOR (grade D, thinner serve sample 1020.0, ratio 2.77); no external reference |
| 50 | `KXITFMATCH-26SEP22YILAGA-AGA` | ITF_MEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 203 min (STALE); data LIMITED (grade B, thinner serve sample 2786.0, ratio 2.08); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9709, "by_level_share_of_ge_25pp": {"ATP": 0.0067, "CHALLENGER": 0.1454, "DOUBLES": 0.0548, "ITF_MEN": 0.3171, "ITF_WOMEN": 0.4279, "OTHER": 0.0035, "WTA": 0.0224, "WTA125": 0.0222}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.6913, "share_primary_cause_market_settled_or_in_play": 0.5388, "share_primary_cause_stale_quote_only": 0.2419}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 3431, "identity_ambiguous_share": 0.1588, "ticker_orientation": {"VERIFIED": 3431}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 1883, "with_external": 12, "coverage": 0.0064, "external_status": {"EXTERNAL_STALE": 11, "AGREES_WITH_KALSHI": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 11, "MODEL_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.0833, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 789, "with_external": 12, "coverage": 0.0152, "external_status": {"EXTERNAL_STALE": 11, "AGREES_WITH_KALSHI": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 11, "MODEL_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.0833, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 725.0, "median_sample_ratio": 2.31, "median_min_matches": 23.0, "median_max_days_since_last": 184.0, "share_severe_asymmetry": 0.1819, "data_status": {"POOR": 1715, "LIMITED": 1020, "ADEQUATE": 696}, "comparison_lt_10pp": {"median_thinner_serve_points": 1886.5, "median_sample_ratio": 1.75, "median_min_matches": 78.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 247, "model_minus_observed": 0.0933, "kalshi_minus_observed": -0.0371, "brier_diff_model_minus_kalshi": 0.0093}, "4-10x": {"n": 170, "model_minus_observed": 0.0898, "kalshi_minus_observed": -0.0482, "brier_diff_model_minus_kalshi": 0.0132}, "<2x": {"n": 498, "model_minus_observed": 0.0677, "kalshi_minus_observed": -0.0568, "brier_diff_model_minus_kalshi": 0.0114}, ">=10x": {"n": 172, "model_minus_observed": 0.0917, "kalshi_minus_observed": -0.0801, "brier_diff_model_minus_kalshi": 0.0138}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 1087, "model": {"intercept": -0.615, "slope": 0.918, "slope_se": 0.077}, "kalshi_mid_same_rows": {"intercept": 0.228, "slope": 1.164, "slope_se": 0.085}, "mean_extremity_model": 0.1858, "mean_extremity_kalshi": 0.1815, "model_brier": 0.2261, "kalshi_brier": 0.1947, "brier_diff_model_minus_kalshi": 0.0315, "brier_diff_se": 0.0058, "model_logloss": 0.6453, "kalshi_logloss": 0.5687}, "fair_v1": {"n": 1087, "model": {"intercept": -0.404, "slope": 1.126, "slope_se": 0.087}, "kalshi_mid_same_rows": {"intercept": 0.377, "slope": 1.244, "slope_se": 0.089}, "mean_extremity_model": 0.1701, "mean_extremity_kalshi": 0.1818, "model_brier": 0.2066, "kalshi_brier": 0.195, "brier_diff_model_minus_kalshi": 0.0116, "brier_diff_se": 0.0046, "model_logloss": 0.5984, "kalshi_logloss": 0.5694}, "gen1_elo": {"n": 1087, "model": {"intercept": -0.44, "slope": 1.117, "slope_se": 0.086}, "kalshi_mid_same_rows": {"intercept": 0.309, "slope": 1.197, "slope_se": 0.086}, "mean_extremity_model": 0.175, "mean_extremity_kalshi": 0.1822, "model_brier": 0.2058, "kalshi_brier": 0.1949, "brier_diff_model_minus_kalshi": 0.0108, "brier_diff_se": 0.0045, "model_logloss": 0.5984, "kalshi_logloss": 0.5692}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2701, "share_ge_15": 0.4552, "median_abs_gap": 13.37, "n": 6972}, "gen1_elo": {"share_ge_25": 0.2612, "share_ge_15": 0.4464, "median_abs_gap": 12.9, "n": 6972}, "gen1_sr": {"share_ge_25": 0.32, "share_ge_15": 0.5376, "median_abs_gap": 16.56, "n": 6972}, "gen2": {"share_ge_25": 0.3217, "share_ge_15": 0.5241, "median_abs_gap": 16.02, "n": 6972}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1556, "share_ge_15": 0.3494, "median_abs_gap": 10.52, "n": 5071}, "gen1_elo": {"share_ge_25": 0.1536, "share_ge_15": 0.3356, "median_abs_gap": 9.83, "n": 5071}, "gen1_sr": {"share_ge_25": 0.2071, "share_ge_15": 0.4419, "median_abs_gap": 13.28, "n": 5071}, "gen2": {"share_ge_25": 0.2256, "share_ge_15": 0.4439, "median_abs_gap": 13.04, "n": 5071}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 6.31, "share_ge_25_all": 0.0431, "share_ge_25_pregame_clean": 0.044}, "WTA": {"median_abs_gap_pregame_clean": 8.55, "share_ge_25_all": 0.0937, "share_ge_25_pregame_clean": 0.0808}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2209, "share_within_10pp_all": 0.409, "share_within_10pp_pregame_clean": 0.485, "corr_model_vs_mid_pregame_clean": 0.8293}`
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
