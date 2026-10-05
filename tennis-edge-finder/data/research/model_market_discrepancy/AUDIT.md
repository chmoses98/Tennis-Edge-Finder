# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-05T01:52Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 12,386): 0-3 13.2%, 3-5 9.1%, 5-10 19.0%, 10-15 15.1%, 15-25 19.6%, 25-40 14.7%, 40+ 9.4%; median gap 12.71 pp.
* **Where the extremes live**: 96.8% of >=25 pp gaps are off the ATP/WTA main tour (ITF 74.2%, Challenger 13.4%, doubles 6.2%). Main tour: ATP 5.5% and WTA 9.4% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 2,986): MARKET_ALREADY_SETTLED_WHEN_PRICED 46.6%, STALE_QUOTE 25.8%, POOR_DATA 5.7%, BOOK_QUALITY 5.6%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 2.9%, IDENTITY_AMBIGUOUS 2.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%. By class: coverage 46.6%, market_freshness 25.8%, market_freshness/coverage 8.9%, data 8.5%, execution 5.6%, mapping 2.5%, model_calibration_or_unknown 2.0%.
* **Stale / settled / in-play**: 71.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 55.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 2,986 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 14.9% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 0.6%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 6.9% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 824.0 points vs 1937.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.142, Gen-2 0.926, Gen-1 ledger 0.907 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 109 model 0.2293 vs Kalshi 0.1905; n 28 model 0.3342 vs Kalshi 0.1438.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%). Not implemented here.

## 1. Observations

* 40,466 model-market comparisons (70,554 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 17,296 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-04T12:50:25.421786+00:00'], shadow board 11,972 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-05T01:48:10.842462+00:00'], Model 4 3,323 rows, 8,482 settled tickers, 1,905 tickers with an external scan.
* By model: {"gen1_ledger": 9971, "gen1_elo": 6020, "fair_v1": 6020, "gen2": 6020, "gen1_sr": 6020, "model4_fundamental": 3212, "model4_conditioned": 3203}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 12,386 | 13.2 | 9.1 | 19.0 | 15.1 | 19.6 | 14.7 | 9.4 | 12.71 | 43.7% | 24.1% |
| MW fair_v1 | 6,020 | 13.2 | 8.5 | 18.2 | 15.4 | 18.7 | 15.4 | 10.6 | 13.09 | 44.7% | 26.0% |
| MW gen1_elo | 6,020 | 13.3 | 8.8 | 19.7 | 14.7 | 18.4 | 15.2 | 9.9 | 12.53 | 43.5% | 25.2% |
| MW gen1_ledger | 6,366 | 13.2 | 9.6 | 19.8 | 14.7 | 20.4 | 14.0 | 8.3 | 12.23 | 42.7% | 22.3% |
| MW gen1_sr | 6,020 | 9.3 | 7.2 | 16.4 | 13.7 | 22.2 | 18.5 | 12.8 | 16.44 | 53.4% | 31.3% |
| MW gen2 | 6,020 | 11.1 | 6.6 | 16.4 | 14.1 | 20.5 | 17.3 | 14.0 | 15.77 | 51.8% | 31.4% |
| all families model4_conditioned | 3,203 | 18.6 | 15.9 | 28.7 | 22.3 | 10.7 | 2.2 | 1.7 | 7.34 | 14.5% | 3.9% |
| all families model4_fundamental | 3,212 | 14.4 | 10.3 | 28.4 | 21.6 | 16.0 | 6.5 | 2.8 | 9.46 | 25.3% | 9.3% |

Configurable thresholds (primary): >=5pp 77.8%, >=10pp 58.8%, >=15pp 43.7%, >=20pp 33.2%, >=25pp 24.1%, >=30pp 17.6%, >=40pp 9.4%, >=50pp 4.3%
Executable gap (model outside the book, before fees): median 10.27pp; >=10pp 50.7%, >=25pp 21.3%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 308 | 19.8 | 15.9 | 25.0 | 15.9 | 16.6 | 3.2 | 3.6 | 7.34 | 23.4% | 6.8% |
| CHALLENGER | 1,262 | 15.8 | 10.7 | 16.9 | 16.5 | 15.1 | 14.0 | 10.9 | 12.21 | 40.1% | 25.0% |
| ITF_MEN | 1,757 | 11.8 | 8.3 | 19.5 | 14.9 | 17.9 | 15.1 | 12.5 | 13.02 | 45.5% | 27.7% |
| ITF_WOMEN | 2,162 | 9.8 | 6.1 | 15.4 | 15.3 | 21.8 | 20.1 | 11.5 | 16.48 | 53.4% | 31.6% |
| WTA | 435 | 23.0 | 10.6 | 25.8 | 12.6 | 18.9 | 6.7 | 2.5 | 8.16 | 28.1% | 9.2% |
| WTA125 | 96 | 12.5 | 4.2 | 16.7 | 27.1 | 17.7 | 13.5 | 8.3 | 12.84 | 39.6% | 21.9% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 308 | 19.8 | 12.7 | 23.7 | 15.9 | 18.8 | 5.2 | 3.9 | 8.77 | 27.9% | 9.1% |
| CHALLENGER | 1,262 | 13.9 | 6.3 | 19.4 | 14.5 | 18.6 | 16.2 | 11.1 | 13.46 | 45.9% | 27.3% |
| ITF_MEN | 1,757 | 9.3 | 6.9 | 17.4 | 15.4 | 20.3 | 16.7 | 14.0 | 15.45 | 51.0% | 30.7% |
| ITF_WOMEN | 2,162 | 8.0 | 6.0 | 12.7 | 12.0 | 21.5 | 20.4 | 19.4 | 19.93 | 61.3% | 39.8% |
| WTA | 435 | 20.5 | 5.5 | 16.8 | 15.6 | 22.3 | 16.8 | 2.5 | 12.98 | 41.6% | 19.3% |
| WTA125 | 96 | 5.2 | 5.2 | 14.6 | 18.8 | 24.0 | 16.7 | 15.6 | 19.03 | 56.2% | 32.3% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 308 | 26.9 | 13.0 | 28.2 | 9.4 | 10.1 | 8.4 | 3.9 | 7.03 | 22.4% | 12.3% |
| CHALLENGER | 1,262 | 16.4 | 9.9 | 22.3 | 13.7 | 13.2 | 12.9 | 11.7 | 10.48 | 37.7% | 24.6% |
| ITF_MEN | 1,757 | 10.4 | 9.2 | 18.2 | 15.7 | 18.9 | 15.2 | 12.4 | 13.53 | 46.6% | 27.7% |
| ITF_WOMEN | 2,162 | 9.9 | 6.3 | 16.1 | 14.2 | 23.7 | 19.9 | 9.8 | 16.99 | 53.5% | 29.8% |
| WTA | 435 | 23.4 | 14.0 | 29.4 | 15.6 | 11.5 | 4.4 | 1.6 | 6.99 | 17.5% | 6.0% |
| WTA125 | 96 | 15.6 | 5.2 | 22.9 | 30.2 | 14.6 | 9.4 | 2.1 | 11.29 | 26.0% | 11.5% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 72 | 23.6 | 22.2 | 34.7 | 12.5 | 6.9 | 0.0 | 0.0 | 6.26 | 6.9% | 0.0% |
| CHALLENGER | 938 | 21.1 | 14.8 | 25.4 | 15.1 | 14.4 | 6.4 | 2.8 | 7.42 | 23.6% | 9.2% |
| DOUBLES | 384 | 5.7 | 3.9 | 9.9 | 10.4 | 21.9 | 20.8 | 27.3 | 24.07 | 70.0% | 48.2% |
| ITF_MEN | 2,087 | 14.0 | 9.2 | 18.8 | 14.1 | 20.8 | 13.6 | 9.5 | 12.46 | 43.9% | 23.1% |
| ITF_WOMEN | 2,033 | 8.8 | 8.2 | 17.2 | 14.5 | 23.6 | 19.0 | 8.8 | 15.64 | 51.4% | 27.8% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 363 | 15.4 | 9.4 | 25.6 | 22.3 | 17.6 | 8.8 | 0.8 | 9.8 | 27.3% | 9.6% |
| WTA125 | 340 | 13.2 | 10.0 | 21.5 | 16.8 | 22.6 | 12.1 | 3.8 | 11.33 | 38.5% | 15.9% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 307 | 19.5 | 16.0 | 25.1 | 16.0 | 16.6 | 3.3 | 3.6 | 7.34 | 23.4% | 6.8% |
| CHALLENGER | 944 | 20.0 | 13.0 | 19.7 | 18.6 | 16.2 | 8.6 | 3.8 | 9.22 | 28.6% | 12.4% |
| ITF_MEN | 1,108 | 15.5 | 11.7 | 24.6 | 16.5 | 17.9 | 9.8 | 4.1 | 9.65 | 31.7% | 13.8% |
| ITF_WOMEN | 1,484 | 12.9 | 7.8 | 18.3 | 17.6 | 22.8 | 16.0 | 4.5 | 13.18 | 43.3% | 20.5% |
| WTA | 434 | 23.0 | 10.6 | 25.8 | 12.7 | 18.9 | 6.5 | 2.5 | 8.16 | 27.9% | 9.0% |
| WTA125 | 90 | 13.3 | 4.4 | 17.8 | 28.9 | 17.8 | 12.2 | 5.6 | 11.83 | 35.6% | 17.8% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 307 | 19.9 | 12.4 | 23.8 | 16.0 | 18.9 | 5.2 | 3.9 | 8.82 | 28.0% | 9.1% |
| CHALLENGER | 944 | 17.4 | 7.6 | 23.2 | 16.8 | 19.5 | 12.3 | 3.2 | 10.53 | 35.0% | 15.5% |
| ITF_MEN | 1,108 | 12.6 | 8.8 | 21.5 | 18.0 | 21.5 | 12.1 | 5.7 | 11.83 | 39.3% | 17.8% |
| ITF_WOMEN | 1,484 | 9.5 | 7.8 | 14.3 | 11.6 | 24.5 | 19.1 | 13.2 | 17.31 | 56.8% | 32.3% |
| WTA | 434 | 20.5 | 5.5 | 16.8 | 15.7 | 22.4 | 16.6 | 2.5 | 12.96 | 41.5% | 19.1% |
| WTA125 | 90 | 5.6 | 5.6 | 14.4 | 20.0 | 25.6 | 17.8 | 11.1 | 17.56 | 54.4% | 28.9% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 62 | 24.2 | 25.8 | 35.5 | 12.9 | 1.6 | 0.0 | 0.0 | 5.45 | 1.6% | 0.0% |
| CHALLENGER | 765 | 23.4 | 17.4 | 28.1 | 14.6 | 13.9 | 2.5 | 0.1 | 6.68 | 16.5% | 2.6% |
| DOUBLES | 345 | 5.8 | 3.8 | 10.1 | 10.4 | 21.7 | 21.2 | 27.0 | 24.1 | 69.9% | 48.1% |
| ITF_MEN | 1,478 | 17.2 | 11.1 | 22.1 | 15.4 | 20.8 | 9.9 | 3.6 | 9.92 | 34.3% | 13.5% |
| ITF_WOMEN | 1,380 | 10.7 | 9.8 | 20.6 | 16.6 | 24.7 | 15.5 | 2.1 | 12.27 | 42.3% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 334 | 15.6 | 9.9 | 26.4 | 23.1 | 18.3 | 6.9 | 0.0 | 9.55 | 25.1% | 6.9% |
| WTA125 | 261 | 15.7 | 11.1 | 25.7 | 19.9 | 21.1 | 6.1 | 0.4 | 9.33 | 27.6% | 6.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 384 | 5.7 | 3.9 | 9.9 | 10.4 | 21.9 | 20.8 | 27.3 | 24.07 | 70.0% | 48.2% |
| singles | 5,982 | 13.6 | 10.0 | 20.4 | 15.0 | 20.3 | 13.5 | 7.1 | 11.8 | 40.9% | 20.6% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 1,364 | 15.2 | 8.9 | 19.1 | 15.2 | 16.1 | 13.5 | 11.9 | 12.13 | 41.5% | 25.4% |
| Hard | 4,180 | 12.5 | 8.5 | 18.2 | 15.1 | 19.6 | 15.8 | 10.3 | 13.5 | 45.7% | 26.1% |
| UNKNOWN | 476 | 13.0 | 6.7 | 15.6 | 19.3 | 18.5 | 17.4 | 9.4 | 13.38 | 45.4% | 26.9% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,825 | 16.9 | 10.0 | 20.7 | 15.7 | 16.8 | 11.8 | 8.2 | 10.55 | 36.8% | 20.0% |
| B | 924 | 16.0 | 10.2 | 16.6 | 18.0 | 16.8 | 10.7 | 11.8 | 11.82 | 39.3% | 22.5% |
| C | 942 | 12.9 | 9.0 | 22.0 | 13.4 | 16.2 | 15.3 | 11.2 | 12.57 | 42.7% | 26.4% |
| D | 1,065 | 11.2 | 8.7 | 16.8 | 14.3 | 20.9 | 16.0 | 12.2 | 14.44 | 49.0% | 28.2% |
| F | 1,264 | 7.6 | 4.4 | 14.0 | 15.8 | 23.0 | 23.8 | 11.3 | 18.45 | 58.1% | 35.1% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,940 | 18.8 | 12.3 | 25.4 | 16.6 | 16.6 | 7.1 | 3.2 | 8.71 | 26.9% | 10.3% |
| B | 1,058 | 13.5 | 9.8 | 21.5 | 15.5 | 19.9 | 12.4 | 7.4 | 11.64 | 39.7% | 19.8% |
| C | 1,278 | 11.1 | 8.7 | 15.6 | 14.2 | 22.0 | 15.3 | 13.2 | 15.18 | 50.5% | 28.5% |
| D | 971 | 11.6 | 8.3 | 20.7 | 11.8 | 23.8 | 15.2 | 8.4 | 13.79 | 47.5% | 23.7% |
| F | 1,119 | 6.7 | 7.0 | 12.6 | 13.8 | 22.6 | 24.8 | 12.6 | 18.91 | 60.0% | 37.4% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 2,302 | 16.4 | 9.5 | 19.2 | 16.4 | 16.9 | 11.9 | 9.7 | 11.2 | 38.5% | 21.6% |
| LIMITED | 1,371 | 14.4 | 10.5 | 21.4 | 14.4 | 15.8 | 13.3 | 10.3 | 11.32 | 39.4% | 23.6% |
| POOR | 2,347 | 9.3 | 6.3 | 15.2 | 15.1 | 22.2 | 20.1 | 11.6 | 16.64 | 54.0% | 31.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 341 | 34.3 | 22.9 | 33.1 | 6.5 | 2.4 | 0.9 | 0.0 | 4.16 | 3.2% | 0.9% |
| GAME_SPREAD | 406 | 19.9 | 16.5 | 37.0 | 16.0 | 8.9 | 1.2 | 0.5 | 6.59 | 10.6% | 1.7% |
| MATCH_WINNER | 6,366 | 13.2 | 9.6 | 19.8 | 14.7 | 20.4 | 14.0 | 8.3 | 12.23 | 42.7% | 22.3% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 1,702 | 21.7 | 13.4 | 30.6 | 17.2 | 13.6 | 2.8 | 0.7 | 7.04 | 17.0% | 3.4% |
| TOTAL_GAMES | 1,132 | 9.9 | 9.4 | 26.5 | 24.9 | 17.0 | 8.0 | 4.4 | 10.66 | 29.3% | 12.4% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,148 | 26.8 | 30.5 | 24.5 | 0.6 | 15.6 | 1.5 | 0.5 | 4.47 | 17.6% | 2.0% |
| GAME_SPREAD | 628 | 35.7 | 15.3 | 26.4 | 17.8 | 2.4 | 1.8 | 0.6 | 4.68 | 4.8% | 2.4% |
| TOTAL_GAMES | 1,427 | 4.4 | 4.5 | 33.1 | 41.6 | 10.3 | 2.9 | 3.1 | 10.67 | 16.3% | 6.0% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,148 | 23.9 | 14.6 | 30.3 | 9.8 | 13.2 | 7.1 | 1.3 | 6.38 | 21.5% | 8.4% |
| GAME_SPREAD | 628 | 17.0 | 10.0 | 24.2 | 22.9 | 17.4 | 6.2 | 2.2 | 9.82 | 25.8% | 8.4% |
| TOTAL_GAMES | 1,436 | 5.7 | 7.0 | 28.8 | 30.4 | 17.6 | 6.3 | 4.2 | 10.98 | 28.1% | 10.5% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 6,020 | 44.7% | 26.0% | 13.09 | 34.1% | 14.9% | 10.34 |
| gen1_elo | 6,020 | 43.5% | 25.2% | 12.53 | 32.5% | 14.7% | 9.56 |
| gen1_sr | 6,020 | 53.4% | 31.3% | 16.44 | 43.9% | 20.4% | 13.17 |
| gen2 | 6,020 | 51.8% | 31.4% | 15.77 | 44.0% | 22.0% | 13.0 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 2,085 | 17.5 | 12.0 | 23.0 | 15.8 | 18.3 | 10.1 | 3.3 | 9.48 | 31.8% | 13.4% |
| STALE | 3,935 | 10.9 | 6.6 | 15.6 | 15.2 | 18.9 | 18.2 | 14.4 | 15.97 | 51.6% | 32.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,360 | 15.1 | 10.5 | 21.9 | 15.9 | 20.0 | 12.1 | 4.6 | 10.71 | 36.7% | 16.7% |
| STALE | 3,006 | 11.0 | 8.7 | 17.5 | 13.4 | 20.9 | 16.1 | 12.5 | 14.77 | 49.4% | 28.6% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 12,386 | 0 | 5445 | 6941 | 32.4 | 217.7 | 1400.4 |
| ge_15pp | 5,411 | 0 | 1894 | 3517 | 39.9 | 506.6 | 1380.4 |
| ge_25pp | 2,986 | 0 | 841 | 2145 | 54.3 | 626.3 | 1380.4 |
| lt_10pp | 5,108 | 0 | 2687 | 2421 | 29.1 | 59.8 | 1201.9 |

Current slate `SL-20261005T015239Z-ca590a7a`: 492 priced rows, quote age at build {'median': 44.3, 'max': 103.9}, freshness {'STALE': 492}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 154 | 23.4 | 11.7 | 18.8 | 21.4 | 18.2 | 5.8 | 0.7 | 7.76 | 24.7% | 6.5% |
| MARKETS_AGREE | 8 | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.96 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 12 | 0.0 | 0.0 | 8.3 | 50.0 | 41.7 | 0.0 | 0.0 | 14.32 | 41.7% | 0.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 6,020 | 175 (2.9%) | 6.9% | 0.0% | {"EXTERNAL_STALE": 154, "AGREES_WITH_KALSHI": 12, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 2,693 | 43 (1.6%) | 11.6% | 0.0% | {"EXTERNAL_STALE": 38, "AGREES_WITH_KALSHI": 5} |
| fair_v1_ge_25pp | 1,566 | 10 (0.6%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 10} |
| fair_v1_ge_25pp_pregame_clean | 650 | 10 (1.5%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 10} |
| fair_v1_lt_10pp | 2,397 | 93 (3.9%) | 1.1% | 0.0% | {"EXTERNAL_STALE": 83, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1, "AGREES_WITH_KALSHI": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 1,219 | 12.5 | 7.4 | 19.6 | 16.4 | 20.1 | 14.9 | 9.1 | 12.82 | 44.1% | 24.0% |
| 4-10x | 789 | 12.9 | 11.3 | 16.9 | 14.2 | 17.9 | 16.0 | 10.9 | 13.37 | 44.7% | 26.9% |
| <2x | 3,252 | 14.1 | 9.0 | 18.9 | 15.4 | 18.2 | 13.6 | 10.8 | 12.39 | 42.6% | 24.4% |
| >=10x | 760 | 10.7 | 5.0 | 14.1 | 15.4 | 19.7 | 23.7 | 11.4 | 17.1 | 54.9% | 35.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 1,710 | 14.2 | 8.7 | 20.2 | 16.3 | 16.7 | 12.5 | 11.5 | 11.95 | 40.6% | 24.0% |
| 300-1000 | 1,398 | 13.3 | 8.7 | 16.2 | 15.4 | 20.2 | 15.7 | 10.5 | 13.79 | 46.4% | 26.2% |
| <300 | 1,489 | 8.3 | 5.6 | 14.8 | 14.4 | 22.0 | 22.8 | 12.0 | 18.3 | 56.8% | 34.8% |
| >=3000 | 1,423 | 16.9 | 11.0 | 21.1 | 15.5 | 16.3 | 11.1 | 8.0 | 10.34 | 35.4% | 19.1% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 224 | 0.5175 | 0.3861 | 0.433 | +0.084 | -0.047 | 0.0064 ± 0.0096 |
| ratio 4-10x | 153 | 0.5731 | 0.4326 | 0.4706 | +0.102 | -0.038 | 0.0142 ± 0.0121 |
| ratio <2x | 444 | 0.5353 | 0.4159 | 0.4707 | +0.065 | -0.055 | 0.0099 ± 0.0066 |
| ratio >=10x | 162 | 0.5524 | 0.3866 | 0.4753 | +0.077 | -0.089 | 0.0106 ± 0.0145 |
| thinner_sample 1000-3000 | 272 | 0.5367 | 0.418 | 0.4596 | +0.077 | -0.042 | 0.0079 ± 0.0083 |
| thinner_sample 300-1000 | 269 | 0.5514 | 0.4212 | 0.4684 | +0.083 | -0.047 | 0.0053 ± 0.0088 |
| thinner_sample <300 | 312 | 0.5411 | 0.3787 | 0.4647 | +0.076 | -0.086 | 0.0139 ± 0.0099 |
| thinner_sample >=3000 | 130 | 0.5202 | 0.4218 | 0.4538 | +0.066 | -0.032 | 0.0139 ± 0.0099 |
| data_status ADEQUATE | 291 | 0.5263 | 0.4177 | 0.4605 | +0.066 | -0.043 | 0.0052 ± 0.0073 |
| data_status LIMITED | 211 | 0.554 | 0.4295 | 0.4882 | +0.066 | -0.059 | 0.0051 ± 0.0101 |
| data_status POOR | 481 | 0.5421 | 0.3905 | 0.4532 | +0.089 | -0.063 | 0.0148 ± 0.0075 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 159 | 0.1766 | 0.1778 | -0.0012 ± 0.0012 | 0.5263 | 0.5295 | 0.49 | 0.4755 | 0.4969 | -0.082 ± 0.0361 | -0.01 (3) |
| 3-5 | 100 | 0.1692 | 0.1677 | +0.0014 ± 0.0034 | 0.5159 | 0.5079 | 0.5106 | 0.4697 | 0.47 | -0.087 ± 0.0436 | 0.02 (1) |
| 5-10 | 205 | 0.1946 | 0.1995 | -0.0049 ± 0.0047 | 0.5741 | 0.5841 | 0.5089 | 0.4345 | 0.4976 | -0.036 ± 0.0314 | -0.0167 (3) |
| 10-15 | 170 | 0.2103 | 0.2073 | +0.0030 ± 0.0087 | 0.6038 | 0.5955 | 0.5202 | 0.3966 | 0.4471 | -0.065 ± 0.0345 | -0.0633 (3) |
| 15-25 | 212 | 0.2136 | 0.2104 | +0.0032 ± 0.0123 | 0.6146 | 0.6048 | 0.5644 | 0.3676 | 0.4623 | -0.024 ± 0.0309 | -0.02 (4) |
| 25-40 | 109 | 0.2293 | 0.1905 | +0.0388 ± 0.0256 | 0.6481 | 0.5548 | 0.6353 | 0.3231 | 0.4128 | -0.070 ± 0.0391 | -0.01 (1) |
| 40+ | 28 | 0.3342 | 0.1438 | +0.1903 ± 0.0646 | 0.9071 | 0.4478 | 0.7189 | 0.2771 | 0.2857 | -0.166 ± 0.0702 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 515 | 0.158 | 0.1593 | -0.0013 ± 0.0006 | 0.481 | 0.484 | 0.5005 | 0.4855 | 0.5282 | -0.017 ± 0.0183 | -0.0188 (8) |
| 3-5 | 332 | 0.1685 | 0.1677 | +0.0008 ± 0.0018 | 0.5126 | 0.5051 | 0.4742 | 0.4343 | 0.4458 | -0.042 ± 0.023 | 0.02 (1) |
| 5-10 | 756 | 0.1769 | 0.1774 | -0.0005 ± 0.0023 | 0.5329 | 0.5307 | 0.4724 | 0.3985 | 0.4378 | -0.015 ± 0.0154 | -0.0129 (7) |
| 10-15 | 643 | 0.1842 | 0.1698 | +0.0144 ± 0.004 | 0.5475 | 0.5014 | 0.4717 | 0.3484 | 0.3515 | -0.058 ± 0.0162 | -0.0633 (3) |
| 15-25 | 816 | 0.195 | 0.1587 | +0.0363 ± 0.0056 | 0.5788 | 0.4731 | 0.4809 | 0.2828 | 0.2904 | -0.050 ± 0.0138 | -0.017 (10) |
| 25-40 | 751 | 0.207 | 0.098 | +0.1090 ± 0.0072 | 0.6055 | 0.3163 | 0.5078 | 0.1931 | 0.1798 | -0.066 ± 0.0111 | -0.01 (1) |
| 40+ | 535 | 0.3768 | 0.0355 | +0.3413 ± 0.009 | 0.9802 | 0.1536 | 0.6215 | 0.1039 | 0.043 | -0.092 ± 0.0076 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 103 | 0.1696 | 0.1713 | -0.0017 ± 0.0014 | 0.5081 | 0.51 | 0.5104 | 0.4952 | 0.5437 | -0.045 ± 0.0406 | -0.01 (1) |
| 3-5 | 80 | 0.2022 | 0.2006 | +0.0015 ± 0.004 | 0.5832 | 0.5852 | 0.4955 | 0.4564 | 0.45 | -0.084 ± 0.0529 | 0.02 (1) |
| 5-10 | 190 | 0.1854 | 0.185 | +0.0004 ± 0.0048 | 0.5528 | 0.5503 | 0.5695 | 0.4939 | 0.5211 | -0.075 ± 0.0316 | -0.01 (4) |
| 10-15 | 164 | 0.2202 | 0.2087 | +0.0116 ± 0.0091 | 0.6284 | 0.6026 | 0.5761 | 0.4511 | 0.4756 | -0.080 ± 0.037 | -0.0667 (3) |
| 15-25 | 239 | 0.2206 | 0.1965 | +0.0241 ± 0.0114 | 0.6269 | 0.5694 | 0.5886 | 0.3914 | 0.4351 | -0.083 ± 0.0295 | -0.0167 (3) |
| 25-40 | 145 | 0.2638 | 0.2025 | +0.0613 ± 0.0231 | 0.7324 | 0.5865 | 0.6577 | 0.3478 | 0.4 | -0.104 ± 0.0393 | -0.025 (2) |
| 40+ | 62 | 0.3877 | 0.1822 | +0.2054 ± 0.0547 | 1.0734 | 0.5424 | 0.7489 | 0.259 | 0.3065 | -0.075 ± 0.053 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 418 | 0.1483 | 0.15 | -0.0017 ± 0.0006 | 0.4537 | 0.4575 | 0.5262 | 0.5115 | 0.5598 | -0.002 ± 0.0192 | -0.0217 (6) |
| 3-5 | 278 | 0.166 | 0.1642 | +0.0017 ± 0.0019 | 0.4985 | 0.4982 | 0.5288 | 0.4892 | 0.4856 | -0.056 ± 0.0249 | 0.02 (1) |
| 5-10 | 683 | 0.173 | 0.1747 | -0.0017 ± 0.0024 | 0.5212 | 0.522 | 0.5253 | 0.4499 | 0.4934 | -0.011 ± 0.016 | -0.01 (5) |
| 10-15 | 587 | 0.1866 | 0.1729 | +0.0137 ± 0.0043 | 0.5556 | 0.511 | 0.5067 | 0.3827 | 0.3969 | -0.045 ± 0.0175 | -0.0575 (4) |
| 15-25 | 883 | 0.2044 | 0.1562 | +0.0482 ± 0.0053 | 0.5979 | 0.4688 | 0.5166 | 0.3197 | 0.3012 | -0.084 ± 0.0133 | -0.0143 (7) |
| 25-40 | 796 | 0.2285 | 0.1226 | +0.1059 ± 0.0079 | 0.6606 | 0.3785 | 0.5453 | 0.2288 | 0.2211 | -0.064 ± 0.0127 | -0.015 (6) |
| 40+ | 703 | 0.4146 | 0.0558 | +0.3589 ± 0.0104 | 1.0876 | 0.2093 | 0.6649 | 0.1226 | 0.0754 | -0.080 ± 0.0085 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 160 | 0.1835 | 0.1851 | -0.0016 ± 0.0012 | 0.54 | 0.5447 | 0.5182 | 0.5038 | 0.5312 | -0.055 ± 0.034 | -0.01 (5) |
| 3-5 | 107 | 0.1701 | 0.167 | +0.0032 ± 0.0032 | 0.5124 | 0.5046 | 0.4974 | 0.4582 | 0.4393 | -0.121 ± 0.0421 | -- (0) |
| 5-10 | 201 | 0.1974 | 0.1971 | +0.0003 ± 0.0047 | 0.5839 | 0.5769 | 0.4964 | 0.4235 | 0.4527 | -0.065 ± 0.0316 | -0.01 (3) |
| 10-15 | 166 | 0.207 | 0.2094 | -0.0024 ± 0.0088 | 0.6002 | 0.6038 | 0.5448 | 0.4213 | 0.5 | -0.046 ± 0.0354 | -0.044 (5) |
| 15-25 | 209 | 0.2083 | 0.1992 | +0.0091 ± 0.012 | 0.6067 | 0.5775 | 0.5749 | 0.3814 | 0.4545 | -0.046 ± 0.0297 | -0.03 (1) |
| 25-40 | 118 | 0.2197 | 0.201 | +0.0187 ± 0.025 | 0.6285 | 0.5817 | 0.6308 | 0.3182 | 0.4407 | -0.045 ± 0.038 | 0.0 (1) |
| 40+ | 22 | 0.3697 | 0.1534 | +0.2162 ± 0.0757 | 0.9871 | 0.4705 | 0.7299 | 0.2782 | 0.2727 | -0.187 ± 0.0867 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 518 | 0.1649 | 0.1651 | -0.0003 ± 0.0006 | 0.4989 | 0.5 | 0.5104 | 0.4959 | 0.5039 | -0.048 ± 0.0179 | -0.0162 (13) |
| 3-5 | 358 | 0.17 | 0.1656 | +0.0044 ± 0.0017 | 0.5113 | 0.4996 | 0.4822 | 0.4429 | 0.4134 | -0.087 ± 0.0219 | -0.01 (2) |
| 5-10 | 760 | 0.1809 | 0.1752 | +0.0057 ± 0.0023 | 0.5433 | 0.5195 | 0.4603 | 0.3865 | 0.3855 | -0.054 ± 0.0153 | -0.01 (3) |
| 10-15 | 623 | 0.1847 | 0.1761 | +0.0086 ± 0.0042 | 0.5499 | 0.5228 | 0.482 | 0.3583 | 0.3868 | -0.033 ± 0.0168 | -0.03 (9) |
| 15-25 | 861 | 0.1859 | 0.1473 | +0.0386 ± 0.0053 | 0.5605 | 0.4452 | 0.4892 | 0.2898 | 0.2927 | -0.054 ± 0.0128 | -0.03 (2) |
| 25-40 | 725 | 0.2054 | 0.0971 | +0.1084 ± 0.0073 | 0.6017 | 0.3126 | 0.5011 | 0.184 | 0.1738 | -0.067 ± 0.011 | 0.0 (1) |
| 40+ | 503 | 0.3871 | 0.0369 | +0.3503 ± 0.0097 | 1.0117 | 0.1568 | 0.6243 | 0.1024 | 0.0398 | -0.092 ± 0.0081 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 437 | 0.2017 | 0.2017 | +0.0000 ± 0.0007 | 0.5849 | 0.5851 | 0.4969 | 0.4822 | 0.4851 | -0.039 ± 0.0216 | -0.0226 (46) |
| 3-5 | 324 | 0.1932 | 0.192 | +0.0012 ± 0.002 | 0.5676 | 0.5618 | 0.4652 | 0.4254 | 0.4352 | -0.038 ± 0.0242 | -0.0059 (32) |
| 5-10 | 664 | 0.1866 | 0.182 | +0.0046 ± 0.0025 | 0.5562 | 0.5429 | 0.4576 | 0.3842 | 0.3901 | -0.039 ± 0.0166 | -0.005 (72) |
| 10-15 | 446 | 0.2029 | 0.192 | +0.0109 ± 0.0052 | 0.5951 | 0.5645 | 0.458 | 0.3346 | 0.352 | -0.033 ± 0.0206 | 0.0016 (63) |
| 15-25 | 598 | 0.2328 | 0.2081 | +0.0247 ± 0.0073 | 0.6591 | 0.6018 | 0.5298 | 0.3369 | 0.3696 | -0.029 ± 0.0186 | -0.0216 (58) |
| 25-40 | 289 | 0.264 | 0.169 | +0.0951 ± 0.0151 | 0.7318 | 0.507 | 0.5762 | 0.265 | 0.2664 | -0.066 ± 0.0238 | -0.0216 (25) |
| 40+ | 95 | 0.427 | 0.1595 | +0.2675 ± 0.044 | 1.1976 | 0.4911 | 0.737 | 0.2273 | 0.2421 | -0.060 ± 0.0425 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 825 | 0.1907 | 0.1901 | +0.0006 ± 0.0005 | 0.5587 | 0.557 | 0.4912 | 0.4767 | 0.4642 | -0.052 ± 0.0152 | -0.0155 (82) |
| 3-5 | 600 | 0.1939 | 0.1921 | +0.0018 ± 0.0014 | 0.5674 | 0.5606 | 0.4701 | 0.4302 | 0.43 | -0.043 ± 0.0179 | -0.018 (54) |
| 5-10 | 1235 | 0.1844 | 0.178 | +0.0064 ± 0.0018 | 0.5509 | 0.5309 | 0.4424 | 0.3684 | 0.3652 | -0.044 ± 0.0121 | -0.0089 (122) |
| 10-15 | 921 | 0.1956 | 0.1825 | +0.0131 ± 0.0035 | 0.5772 | 0.5401 | 0.4478 | 0.3245 | 0.3333 | -0.035 ± 0.014 | -0.0053 (99) |
| 15-25 | 1276 | 0.2197 | 0.185 | +0.0347 ± 0.0047 | 0.6348 | 0.5435 | 0.5031 | 0.3076 | 0.3158 | -0.042 ± 0.0121 | -0.0255 (106) |
| 25-40 | 885 | 0.24 | 0.1256 | +0.1144 ± 0.0075 | 0.6803 | 0.3935 | 0.5268 | 0.2118 | 0.1887 | -0.070 ± 0.0117 | -0.0206 (47) |
| 40+ | 513 | 0.3878 | 0.0787 | +0.3092 ± 0.0136 | 1.058 | 0.2662 | 0.6513 | 0.1347 | 0.1053 | -0.072 ± 0.0126 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 983 | 1.142 ± 0.091 | 1.27 | 0.1739 | 0.182 | 0.2038 | 0.1939 |
| gen2 | 983 | 0.926 ± 0.08 | 1.178 | 0.1887 | 0.1811 | 0.2238 | 0.194 |
| gen1_elo | 983 | 1.139 ± 0.09 | 1.23 | 0.1783 | 0.1823 | 0.2026 | 0.1939 |
| gen1_sr | 983 | 1.154 ± 0.105 | 1.246 | 0.1443 | 0.1833 | 0.2192 | 0.1938 |
| gen1_ledger | 2853 | 0.907 ± 0.051 | 1.076 | 0.1634 | 0.2005 | 0.2177 | 0.1911 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 5,411)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,791 | 33.1% |
| STALE_QUOTE | market_freshness | 1,709 | 31.6% |
| POOR_DATA | data | 401 | 7.4% |
| BOOK_QUALITY | execution | 339 | 6.3% |
| LIMITED_DATA | data | 317 | 5.9% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 308 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 257 | 4.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 181 | 3.4% |
| IDENTITY_AMBIGUOUS | mapping | 105 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 3 | 0.1% |

Cause class: coverage 33.1%, market_freshness 31.6%, data 13.3%, market_freshness/coverage 9.0%, execution 6.3%, model_calibration_or_unknown 4.8%, mapping 1.9%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 94.5%, STALE_KALSHI_QUOTE 65.0%, LOW_DATA_QUALITY 63.5%, STALE_PLAYER_DATA 52.4%, THIN_PLAYER_HISTORY 52.0%, MODEL_INTERNAL_DISAGREEMENT 34.0%, ASYMMETRIC_SAMPLE_SIZE 28.8%, WIDE_SPREAD 15.2%, MODEL_HIGH_UNCERTAINTY 14.8%, PLAYER_IDENTITY_RISK 10.9%, LEVEL_TRANSFER_RISK 8.0%, EVENT_MAPPING_RISK 6.2%, LOW_DISPLAYED_LIQUIDITY 5.2%, MODEL_CALIBRATION_OUTLIER 2.0%, UNKNOWN 0.7%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 35.6%, POST_SETTLEMENT_OBSERVATION 33.1%, POSSIBLE_IN_PLAY_QUOTE 6.4%, CONFIRMED_IN_PLAY_QUOTE 1.1%

### >= ge_25 pp (N = 2,986)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,390 | 46.6% |
| STALE_QUOTE | market_freshness | 771 | 25.8% |
| POOR_DATA | data | 169 | 5.7% |
| BOOK_QUALITY | execution | 167 | 5.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 161 | 5.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 106 | 3.5% |
| LIMITED_DATA | data | 86 | 2.9% |
| IDENTITY_AMBIGUOUS | mapping | 75 | 2.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 61 | 2.0% |

Cause class: coverage 46.6%, market_freshness 25.8%, market_freshness/coverage 8.9%, data 8.5%, execution 5.6%, mapping 2.5%, model_calibration_or_unknown 2.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 96.8%, STALE_KALSHI_QUOTE 71.8%, LOW_DATA_QUALITY 67.2%, THIN_PLAYER_HISTORY 54.2%, STALE_PLAYER_DATA 50.5%, MODEL_INTERNAL_DISAGREEMENT 35.2%, ASYMMETRIC_SAMPLE_SIZE 31.4%, MODEL_HIGH_UNCERTAINTY 16.0%, WIDE_SPREAD 14.0%, PLAYER_IDENTITY_RISK 13.7%, LEVEL_TRANSFER_RISK 7.9%, EVENT_MAPPING_RISK 7.4%, LOW_DISPLAYED_LIQUIDITY 5.7%, MODEL_CALIBRATION_OUTLIER 2.9%, UNKNOWN 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 49.2%, POST_SETTLEMENT_OBSERVATION 46.6%, POSSIBLE_IN_PLAY_QUOTE 6.2%, CONFIRMED_IN_PLAY_QUOTE 1.2%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 2540, "IDENTITY_AMBIGUOUS": 446}; ticker orientation: {"VERIFIED": 2986}.

Checks: discipline:AMBIGUOUS 185, discipline:PASS 2801, identity_confidence:AMBIGUOUS 410, identity_confidence:PASS 2576, level_mapping:NA 197, level_mapping:PASS 2789, market_pair:AMBIGUOUS 66, market_pair:NA 83, market_pair:PASS 2837, model_complement:NA 52, model_complement:PASS 2934, namesake:PASS 2986, physical_match_id:NA 1420, physical_match_id:PASS 1566, player_ids:PASS 2986, same_pair_other_event:PASS 2986, ticker_orientation:PASS 2986

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 380 | 5.5% | 5.7% | 0.7% | {"market_freshness": 20, "execution": 1} | 6.88 | 0.1791 / 0.1823 (49) | 47.6% | 0.0% | 0.5% | 2.9% |
| CHALLENGER | 2,200 | 18.2% | 8.0% | 13.4% | {"coverage": 215, "market_freshness": 97, "market_freshness/coverage": 49, "data": 21, "model_calibration_or_unknown": 15, "execution": 4} | 7.51 | 0.2155 / 0.2008 (625) | 57.6% | 5.5% | 1.2% | 22.3% |
| DOUBLES | 384 | 48.2% | 48.1% | 6.2% | {"market_freshness": 106, "execution": 32, "mapping": 28, "market_freshness/coverage": 12, "coverage": 7} | 24.1 | 0.3208 / 0.2301 (163) | 60.9% | 0.0% | 100.0% | 10.2% |
| ITF_MEN | 3,844 | 25.2% | 13.7% | 32.4% | {"coverage": 541, "market_freshness": 180, "data": 88, "market_freshness/coverage": 74, "execution": 74, "mapping": 10, "model_calibration_or_unknown": 1} | 9.79 | 0.2136 / 0.188 (1350) | 56.4% | 49.3% | 5.3% | 32.7% |
| ITF_WOMEN | 4,195 | 29.8% | 19.1% | 41.8% | {"coverage": 610, "market_freshness": 320, "data": 126, "market_freshness/coverage": 92, "execution": 47, "mapping": 35, "model_calibration_or_unknown": 19} | 12.8 | 0.2031 / 0.1856 (1257) | 61.3% | 57.1% | 8.3% | 31.7% |
| OTHER | 149 | 8.1% | 7.3% | 0.4% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 798 | 9.4% | 8.1% | 2.5% | {"market_freshness": 34, "model_calibration_or_unknown": 12, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.66 | 0.2006 / 0.1964 (129) | 40.5% | 2.6% | 1.5% | 3.8% |
| WTA125 | 436 | 17.2% | 9.4% | 2.5% | {"market_freshness/coverage": 30, "model_calibration_or_unknown": 12, "market_freshness": 12, "coverage": 12, "data": 9} | 10.36 | 0.2273 / 0.204 (221) | 35.8% | 8.7% | 0.5% | 19.5% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 3 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 4 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 5 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 6 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 7 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 8 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 9 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 10 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 11 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 12 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 14 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
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
| 28 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 230 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 29 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.2h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 141 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 30 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 31 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 32 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 33 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 708 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 34 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 35 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 36 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 37 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 114 min (STALE); data LIMITED (grade B, thinner serve sample 2163.0, ratio 2.0); no external reference |
| 39 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 732 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 40 | `KXWTAMATCH-26OCT01YASCHW-CHW` | WTA | fair_v1 | 73% / 2% | +70 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 51 min (STALE); no external reference |
| 41 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 42 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 43 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 44 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |
| 45 | `KXITFWMATCH-26SEP30KOKUEM-KOK` | ITF_WOMEN | fair_v1 | 79% / 10% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 776 min (STALE); data LIMITED (grade C, thinner serve sample 824.0, ratio 2.35); no external reference |
| 46 | `KXITFMATCH-26SEP20WILRAH-RAH` | ITF_MEN | gen1_ledger | 72% / 4% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade B, thinner serve sample 2782.0, ratio 1.84); no external reference |
| 47 | `KXITFMATCH-26SEP26NAGTHO-NAG` | ITF_MEN | gen1_ledger | 76% / 7% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 89 min (STALE); data LIMITED (grade C, thinner serve sample 1323.0, ratio 4.45); no external reference |
| 48 | `KXITFWMATCH-26SEP26PERPRE-PER` | ITF_WOMEN | gen1_ledger | 78% / 10% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 102 min (STALE); data POOR (grade D, thinner serve sample 1020.0, ratio 2.77); no external reference |
| 49 | `KXITFMATCH-26SEP22YILAGA-AGA` | ITF_MEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 203 min (STALE); data LIMITED (grade B, thinner serve sample 2786.0, ratio 2.08); no external reference |
| 50 | `KXITFMATCH-26SEP30DIMURA-URA` | ITF_MEN | fair_v1 | 71% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.1h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 793 min (STALE); data POOR (grade F, thinner serve sample 174.0, ratio 2.63); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9679, "by_level_share_of_ge_25pp": {"ATP": 0.007, "CHALLENGER": 0.1343, "DOUBLES": 0.062, "ITF_MEN": 0.3242, "ITF_WOMEN": 0.4183, "OTHER": 0.004, "WTA": 0.0251, "WTA125": 0.0251}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.7184, "share_primary_cause_market_settled_or_in_play": 0.5549, "share_primary_cause_stale_quote_only": 0.2582}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 2986, "identity_ambiguous_share": 0.1494, "ticker_orientation": {"VERIFIED": 2986}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 1566, "with_external": 10, "coverage": 0.0064, "external_status": {"EXTERNAL_STALE": 10}, "triangulation": {"INSUFFICIENT_INPUTS": 10}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 650, "with_external": 10, "coverage": 0.0154, "external_status": {"EXTERNAL_STALE": 10}, "triangulation": {"INSUFFICIENT_INPUTS": 10}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 824.0, "median_sample_ratio": 2.27, "median_min_matches": 28.0, "median_max_days_since_last": 173.0, "share_severe_asymmetry": 0.1815, "data_status": {"POOR": 1405, "LIMITED": 968, "ADEQUATE": 613}, "comparison_lt_10pp": {"median_thinner_serve_points": 1937.0, "median_sample_ratio": 1.75, "median_min_matches": 77.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 224, "model_minus_observed": 0.0844, "kalshi_minus_observed": -0.0469, "brier_diff_model_minus_kalshi": 0.0064}, "4-10x": {"n": 153, "model_minus_observed": 0.1025, "kalshi_minus_observed": -0.038, "brier_diff_model_minus_kalshi": 0.0142}, "<2x": {"n": 444, "model_minus_observed": 0.0646, "kalshi_minus_observed": -0.0548, "brier_diff_model_minus_kalshi": 0.0099}, ">=10x": {"n": 162, "model_minus_observed": 0.0771, "kalshi_minus_observed": -0.0887, "brier_diff_model_minus_kalshi": 0.0106}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 983, "model": {"intercept": -0.607, "slope": 0.926, "slope_se": 0.08}, "kalshi_mid_same_rows": {"intercept": 0.226, "slope": 1.178, "slope_se": 0.09}, "mean_extremity_model": 0.1887, "mean_extremity_kalshi": 0.1811, "model_brier": 0.2238, "kalshi_brier": 0.194, "brier_diff_model_minus_kalshi": 0.0298, "brier_diff_se": 0.0061, "model_logloss": 0.6405, "kalshi_logloss": 0.5671}, "fair_v1": {"n": 983, "model": {"intercept": -0.391, "slope": 1.142, "slope_se": 0.091}, "kalshi_mid_same_rows": {"intercept": 0.394, "slope": 1.27, "slope_se": 0.094}, "mean_extremity_model": 0.1739, "mean_extremity_kalshi": 0.182, "model_brier": 0.2038, "kalshi_brier": 0.1939, "brier_diff_model_minus_kalshi": 0.0099, "brier_diff_se": 0.0048, "model_logloss": 0.592, "kalshi_logloss": 0.5668}, "gen1_elo": {"n": 983, "model": {"intercept": -0.413, "slope": 1.139, "slope_se": 0.09}, "kalshi_mid_same_rows": {"intercept": 0.345, "slope": 1.23, "slope_se": 0.092}, "mean_extremity_model": 0.1783, "mean_extremity_kalshi": 0.1823, "model_brier": 0.2026, "kalshi_brier": 0.1939, "brier_diff_model_minus_kalshi": 0.0088, "brier_diff_se": 0.0047, "model_logloss": 0.5909, "kalshi_logloss": 0.5667}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2601, "share_ge_15": 0.4473, "median_abs_gap": 13.09, "n": 6020}, "gen1_elo": {"share_ge_25": 0.2517, "share_ge_15": 0.4354, "median_abs_gap": 12.53, "n": 6020}, "gen1_sr": {"share_ge_25": 0.3126, "share_ge_15": 0.5342, "median_abs_gap": 16.44, "n": 6020}, "gen2": {"share_ge_25": 0.3135, "share_ge_15": 0.5184, "median_abs_gap": 15.77, "n": 6020}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1488, "share_ge_15": 0.341, "median_abs_gap": 10.34, "n": 4367}, "gen1_elo": {"share_ge_25": 0.1472, "share_ge_15": 0.3249, "median_abs_gap": 9.56, "n": 4367}, "gen1_sr": {"share_ge_25": 0.2038, "share_ge_15": 0.4392, "median_abs_gap": 13.17, "n": 4367}, "gen2": {"share_ge_25": 0.2196, "share_ge_15": 0.4403, "median_abs_gap": 13.0, "n": 4367}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 6.88, "share_ge_25_all": 0.0553, "share_ge_25_pregame_clean": 0.0569}, "WTA": {"median_abs_gap_pregame_clean": 8.66, "share_ge_25_all": 0.094, "share_ge_25_pregame_clean": 0.0807}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2223, "share_within_10pp_all": 0.4124, "share_within_10pp_pregame_clean": 0.4914, "corr_model_vs_mid_pregame_clean": 0.8321}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 159, "model_brier": 0.1766, "kalshi_brier": 0.1778, "brier_diff_model_minus_kalshi": -0.0012}, "10-15": {"n_settled": 170, "model_brier": 0.2103, "kalshi_brier": 0.2073, "brier_diff_model_minus_kalshi": 0.003}, "15-25": {"n_settled": 212, "model_brier": 0.2136, "kalshi_brier": 0.2104, "brier_diff_model_minus_kalshi": 0.0032}, "25-40": {"n_settled": 109, "model_brier": 0.2293, "kalshi_brier": 0.1905, "brier_diff_model_minus_kalshi": 0.0388}, "3-5": {"n_settled": 100, "model_brier": 0.1692, "kalshi_brier": 0.1677, "brier_diff_model_minus_kalshi": 0.0014}, "40+": {"n_settled": 28, "model_brier": 0.3342, "kalshi_brier": 0.1438, "brier_diff_model_minus_kalshi": 0.1903}, "5-10": {"n_settled": 205, "model_brier": 0.1946, "kalshi_brier": 0.1995, "brier_diff_model_minus_kalshi": -0.0049}}}`

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
