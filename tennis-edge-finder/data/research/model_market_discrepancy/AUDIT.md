# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-01T06:09Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 8,872): 0-3 13.2%, 3-5 9.5%, 5-10 19.8%, 10-15 14.6%, 15-25 19.7%, 25-40 14.1%, 40+ 9.1%; median gap 12.39 pp.
* **Where the extremes live**: 97.4% of >=25 pp gaps are off the ATP/WTA main tour (ITF 74.1%, Challenger 11.6%, doubles 8.2%). Main tour: ATP 2.4% and WTA 7.6% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 2,064): MARKET_ALREADY_SETTLED_WHEN_PRICED 43.0%, STALE_QUOTE 22.5%, POOR_DATA 7.5%, BOOK_QUALITY 6.5%, POSSIBLY_IN_PLAY_QUOTE 6.1%, IN_PLAY_QUOTE 5.8%, LIMITED_DATA 3.7%, IDENTITY_AMBIGUOUS 2.8%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%. By class: coverage 43.0%, market_freshness 22.5%, market_freshness/coverage 11.9%, data 11.2%, execution 6.5%, mapping 2.8%, model_calibration_or_unknown 2.0%.
* **Stale / settled / in-play**: 65.2% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 54.9% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 2,064 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 16.7% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 0.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 8.0% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 666.0 points vs 1969.5 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.198, Gen-2 0.933, Gen-1 ledger 0.901 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 68 model 0.2385 vs Kalshi 0.1851; n 16 model 0.3076 vs Kalshi 0.132.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%). Not implemented here.

## 1. Observations

* 26,341 model-market comparisons (45,203 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 15,296 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-01T06:04:48.027931+00:00'], shadow board 6,765 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-01T06:04:51.615565+00:00'], Model 4 1,896 rows, 7,566 settled tickers, 1,765 tickers with an external scan.
* By model: {"gen1_ledger": 9019, "gen1_elo": 3402, "fair_v1": 3402, "gen2": 3402, "gen1_sr": 3402, "model4_fundamental": 1858, "model4_conditioned": 1856}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 8,872 | 13.2 | 9.5 | 19.8 | 14.6 | 19.7 | 14.1 | 9.1 | 12.39 | 43.0% | 23.3% |
| MW fair_v1 | 3,402 | 13.1 | 9.3 | 19.0 | 14.6 | 19.0 | 14.7 | 10.3 | 12.84 | 43.9% | 25.0% |
| MW gen1_elo | 3,402 | 14.1 | 8.3 | 19.7 | 15.0 | 18.7 | 14.8 | 9.4 | 12.46 | 43.0% | 24.3% |
| MW gen1_ledger | 5,470 | 13.2 | 9.5 | 20.2 | 14.7 | 20.2 | 13.8 | 8.4 | 12.18 | 42.4% | 22.2% |
| MW gen1_sr | 3,402 | 9.8 | 6.5 | 17.2 | 13.9 | 21.0 | 18.8 | 12.8 | 16.0 | 52.6% | 31.6% |
| MW gen2 | 3,402 | 10.6 | 6.4 | 16.3 | 15.8 | 19.7 | 17.2 | 14.0 | 15.39 | 50.9% | 31.2% |
| all families model4_conditioned | 1,856 | 20.3 | 15.4 | 29.8 | 21.3 | 9.5 | 1.8 | 2.0 | 7.08 | 13.2% | 3.8% |
| all families model4_fundamental | 1,858 | 14.3 | 10.9 | 31.4 | 21.9 | 13.6 | 5.3 | 2.7 | 8.82 | 21.6% | 8.0% |

Configurable thresholds (primary): >=5pp 77.4%, >=10pp 57.6%, >=15pp 43.0%, >=20pp 32.1%, >=25pp 23.3%, >=30pp 17.4%, >=40pp 9.1%, >=50pp 4.1%
Executable gap (model outside the book, before fees): median 9.95pp; >=10pp 49.8%, >=25pp 20.6%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 177 | 22.6 | 21.5 | 23.2 | 11.3 | 18.1 | 1.7 | 1.7 | 5.88 | 21.5% | 3.4% |
| CHALLENGER | 645 | 16.1 | 9.5 | 15.3 | 16.3 | 16.3 | 13.3 | 13.2 | 13.16 | 42.8% | 26.5% |
| ITF_MEN | 1,061 | 11.4 | 9.1 | 19.8 | 13.2 | 18.5 | 16.0 | 12.0 | 13.25 | 46.5% | 28.0% |
| ITF_WOMEN | 1,197 | 10.6 | 7.2 | 16.5 | 15.0 | 21.1 | 18.6 | 11.0 | 15.37 | 50.6% | 29.6% |
| WTA | 256 | 18.8 | 12.5 | 33.6 | 12.5 | 18.0 | 4.7 | 0.0 | 7.45 | 22.7% | 4.7% |
| WTA125 | 66 | 10.6 | 6.1 | 16.7 | 30.3 | 21.2 | 10.6 | 4.5 | 12.4 | 36.4% | 15.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 177 | 23.7 | 14.1 | 23.7 | 15.8 | 18.1 | 2.3 | 2.3 | 6.54 | 22.6% | 4.5% |
| CHALLENGER | 645 | 10.5 | 6.2 | 18.8 | 17.4 | 16.9 | 17.1 | 13.2 | 14.64 | 47.1% | 30.2% |
| ITF_MEN | 1,061 | 10.0 | 5.6 | 16.2 | 16.6 | 19.3 | 17.6 | 14.7 | 15.48 | 51.6% | 32.3% |
| ITF_WOMEN | 1,197 | 8.4 | 6.3 | 13.3 | 13.5 | 19.7 | 20.1 | 18.6 | 18.5 | 58.4% | 38.7% |
| WTA | 256 | 16.0 | 5.9 | 19.5 | 16.8 | 27.3 | 13.7 | 0.8 | 13.39 | 41.8% | 14.4% |
| WTA125 | 66 | 4.5 | 4.5 | 16.7 | 22.7 | 27.3 | 12.1 | 12.1 | 15.56 | 51.5% | 24.2% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 177 | 34.5 | 12.4 | 24.9 | 10.2 | 9.6 | 6.8 | 1.7 | 5.46 | 18.1% | 8.5% |
| CHALLENGER | 645 | 16.3 | 7.1 | 19.7 | 16.3 | 15.5 | 13.6 | 11.5 | 11.99 | 40.6% | 25.1% |
| ITF_MEN | 1,061 | 10.2 | 9.7 | 18.3 | 15.1 | 18.3 | 16.7 | 11.8 | 13.33 | 46.8% | 28.5% |
| ITF_WOMEN | 1,197 | 10.3 | 6.8 | 17.3 | 14.2 | 23.3 | 18.2 | 9.9 | 16.02 | 51.5% | 28.1% |
| WTA | 256 | 26.9 | 10.9 | 31.6 | 14.8 | 13.7 | 1.9 | 0.0 | 6.68 | 15.6% | 1.9% |
| WTA125 | 66 | 18.2 | 4.5 | 24.2 | 30.3 | 15.2 | 7.6 | 0.0 | 10.52 | 22.7% | 7.6% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 71 | 23.9 | 22.5 | 35.2 | 11.3 | 7.0 | 0.0 | 0.0 | 6.19 | 7.0% | 0.0% |
| CHALLENGER | 754 | 21.4 | 13.7 | 26.7 | 15.5 | 13.7 | 6.5 | 2.6 | 7.44 | 22.8% | 9.2% |
| DOUBLES | 347 | 5.8 | 3.8 | 9.8 | 10.1 | 21.9 | 20.2 | 28.5 | 24.15 | 70.6% | 48.7% |
| ITF_MEN | 1,807 | 13.7 | 9.1 | 18.9 | 13.7 | 20.9 | 14.1 | 9.6 | 12.75 | 44.6% | 23.7% |
| ITF_WOMEN | 1,652 | 8.8 | 8.6 | 17.7 | 14.5 | 23.2 | 18.3 | 9.0 | 15.2 | 50.5% | 27.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 363 | 15.4 | 9.4 | 25.6 | 22.3 | 17.6 | 8.8 | 0.8 | 9.8 | 27.3% | 9.6% |
| WTA125 | 327 | 13.8 | 9.8 | 20.8 | 16.8 | 23.6 | 11.3 | 4.0 | 11.35 | 38.8% | 15.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 176 | 22.2 | 21.6 | 23.3 | 11.4 | 18.2 | 1.7 | 1.7 | 5.88 | 21.6% | 3.4% |
| CHALLENGER | 475 | 20.2 | 12.2 | 18.1 | 19.4 | 16.8 | 8.0 | 5.3 | 9.93 | 30.1% | 13.3% |
| ITF_MEN | 738 | 15.4 | 11.8 | 24.4 | 14.6 | 18.4 | 11.1 | 4.2 | 9.63 | 33.7% | 15.3% |
| ITF_WOMEN | 848 | 14.3 | 8.8 | 19.2 | 17.8 | 22.1 | 13.4 | 4.4 | 12.39 | 39.9% | 17.8% |
| WTA | 255 | 18.8 | 12.6 | 33.7 | 12.6 | 18.0 | 4.3 | 0.0 | 7.44 | 22.4% | 4.3% |
| WTA125 | 65 | 10.8 | 6.2 | 16.9 | 30.8 | 21.5 | 9.2 | 4.6 | 12.01 | 35.4% | 13.9% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 176 | 23.9 | 13.6 | 23.9 | 15.9 | 18.2 | 2.3 | 2.3 | 6.56 | 22.7% | 4.5% |
| CHALLENGER | 475 | 12.8 | 7.8 | 23.4 | 21.1 | 18.5 | 12.2 | 4.2 | 11.51 | 34.9% | 16.4% |
| ITF_MEN | 738 | 12.6 | 7.0 | 19.8 | 19.0 | 21.1 | 13.8 | 6.6 | 12.57 | 41.6% | 20.5% |
| ITF_WOMEN | 848 | 9.8 | 8.2 | 15.2 | 14.0 | 22.4 | 18.3 | 12.0 | 15.98 | 52.7% | 30.3% |
| WTA | 255 | 16.1 | 5.9 | 19.6 | 16.9 | 27.4 | 13.3 | 0.8 | 13.22 | 41.6% | 14.1% |
| WTA125 | 65 | 4.6 | 4.6 | 16.9 | 23.1 | 27.7 | 12.3 | 10.8 | 15.33 | 50.8% | 23.1% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 59 | 25.4 | 25.4 | 35.6 | 11.9 | 1.7 | 0.0 | 0.0 | 4.87 | 1.7% | 0.0% |
| CHALLENGER | 618 | 23.8 | 16.0 | 29.6 | 14.9 | 12.8 | 2.8 | 0.2 | 6.67 | 15.7% | 2.9% |
| DOUBLES | 266 | 6.4 | 3.4 | 9.8 | 10.2 | 22.2 | 21.1 | 27.1 | 24.11 | 70.3% | 48.1% |
| ITF_MEN | 1,288 | 16.7 | 10.8 | 22.5 | 14.7 | 20.6 | 11.0 | 3.7 | 9.98 | 35.3% | 14.8% |
| ITF_WOMEN | 1,127 | 10.7 | 9.9 | 21.4 | 16.5 | 24.1 | 15.0 | 2.4 | 12.16 | 41.5% | 17.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 255 | 15.3 | 9.0 | 25.5 | 23.5 | 19.6 | 7.1 | 0.0 | 10.01 | 26.7% | 7.1% |
| WTA125 | 248 | 16.5 | 10.9 | 25.0 | 19.4 | 21.4 | 6.5 | 0.4 | 9.32 | 28.2% | 6.9% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 347 | 5.8 | 3.8 | 9.8 | 10.1 | 21.9 | 20.2 | 28.5 | 24.15 | 70.6% | 48.7% |
| singles | 5,123 | 13.7 | 9.9 | 20.9 | 15.0 | 20.1 | 13.3 | 7.1 | 11.69 | 40.5% | 20.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 764 | 15.7 | 8.5 | 18.5 | 14.0 | 17.8 | 13.3 | 12.2 | 12.14 | 43.3% | 25.5% |
| Hard | 2,419 | 12.2 | 9.8 | 19.5 | 14.5 | 19.4 | 14.8 | 9.8 | 12.9 | 43.9% | 24.6% |
| UNKNOWN | 219 | 14.2 | 6.8 | 14.6 | 17.8 | 18.7 | 18.3 | 9.6 | 13.77 | 46.6% | 27.9% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 967 | 17.7 | 12.4 | 21.5 | 15.3 | 16.8 | 9.9 | 6.4 | 9.8 | 33.1% | 16.3% |
| B | 429 | 13.5 | 11.0 | 16.8 | 18.9 | 17.0 | 10.5 | 12.3 | 12.17 | 39.9% | 22.8% |
| C | 577 | 14.0 | 8.8 | 24.6 | 12.7 | 15.1 | 14.0 | 10.8 | 11.39 | 39.9% | 24.8% |
| D | 655 | 11.6 | 9.0 | 16.6 | 13.7 | 21.8 | 15.0 | 12.2 | 14.53 | 49.0% | 27.2% |
| F | 774 | 7.9 | 5.3 | 14.7 | 13.6 | 23.3 | 23.3 | 12.0 | 18.88 | 58.5% | 35.3% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,695 | 18.8 | 12.0 | 26.7 | 16.8 | 16.6 | 6.5 | 2.6 | 8.5 | 25.7% | 9.1% |
| B | 903 | 13.6 | 9.1 | 21.6 | 17.1 | 18.7 | 12.5 | 7.4 | 11.56 | 38.6% | 19.9% |
| C | 1,118 | 11.1 | 8.7 | 15.7 | 13.8 | 21.8 | 15.4 | 13.6 | 15.33 | 50.8% | 29.0% |
| D | 840 | 11.3 | 8.3 | 19.9 | 11.9 | 24.2 | 15.6 | 8.8 | 14.34 | 48.6% | 24.4% |
| F | 914 | 6.5 | 7.7 | 12.8 | 12.0 | 22.8 | 24.7 | 13.6 | 19.78 | 61.1% | 38.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 1,189 | 15.6 | 11.3 | 20.2 | 16.6 | 17.2 | 10.3 | 8.9 | 10.65 | 36.3% | 19.2% |
| LIMITED | 771 | 15.8 | 10.8 | 23.5 | 13.6 | 14.4 | 12.7 | 9.2 | 9.99 | 36.3% | 21.9% |
| POOR | 1,442 | 9.7 | 6.9 | 15.5 | 13.5 | 22.9 | 19.4 | 12.0 | 17.02 | 54.3% | 31.4% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 325 | 34.8 | 23.1 | 32.9 | 5.8 | 2.5 | 0.9 | 0.0 | 4.14 | 3.4% | 0.9% |
| GAME_SPREAD | 394 | 20.3 | 16.5 | 36.3 | 16.0 | 9.1 | 1.3 | 0.5 | 6.5 | 10.9% | 1.8% |
| MATCH_WINNER | 5,470 | 13.2 | 9.5 | 20.2 | 14.7 | 20.2 | 13.8 | 8.4 | 12.18 | 42.4% | 22.2% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 1,686 | 21.9 | 13.5 | 29.9 | 17.4 | 13.8 | 2.8 | 0.7 | 7.06 | 17.2% | 3.4% |
| TOTAL_GAMES | 1,120 | 9.9 | 9.0 | 26.2 | 25.2 | 17.1 | 8.0 | 4.5 | 10.68 | 29.6% | 12.5% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 672 | 29.0 | 30.8 | 27.1 | 0.9 | 10.0 | 1.9 | 0.3 | 4.31 | 12.2% | 2.2% |
| GAME_SPREAD | 397 | 37.8 | 12.1 | 23.9 | 21.2 | 3.0 | 1.5 | 0.5 | 5.02 | 5.0% | 2.0% |
| TOTAL_GAMES | 787 | 3.9 | 3.9 | 35.1 | 38.8 | 12.3 | 1.8 | 4.2 | 10.59 | 18.3% | 6.0% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 672 | 23.5 | 17.7 | 33.5 | 8.8 | 10.7 | 4.8 | 1.0 | 5.88 | 16.5% | 5.8% |
| GAME_SPREAD | 397 | 17.6 | 11.3 | 23.9 | 22.2 | 17.1 | 5.8 | 2.0 | 9.62 | 24.9% | 7.8% |
| TOTAL_GAMES | 789 | 4.8 | 4.8 | 33.3 | 32.8 | 14.3 | 5.5 | 4.4 | 10.9 | 24.2% | 9.9% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3,402 | 43.9% | 25.0% | 12.84 | 33.2% | 13.8% | 9.98 |
| gen1_elo | 3,402 | 43.0% | 24.3% | 12.46 | 31.9% | 13.9% | 9.58 |
| gen1_sr | 3,402 | 52.6% | 31.6% | 16.0 | 43.7% | 20.5% | 13.14 |
| gen2 | 3,402 | 50.9% | 31.2% | 15.39 | 43.0% | 21.3% | 13.05 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 1,530 | 17.2 | 12.6 | 23.0 | 15.4 | 19.1 | 9.7 | 3.1 | 9.33 | 31.9% | 12.8% |
| STALE | 1,872 | 9.8 | 6.7 | 15.7 | 14.0 | 18.9 | 18.8 | 16.1 | 16.97 | 53.8% | 34.9% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,110 | 15.1 | 10.3 | 21.9 | 15.9 | 20.0 | 12.2 | 4.7 | 10.78 | 36.8% | 16.8% |
| STALE | 2,360 | 10.6 | 8.6 | 18.1 | 13.0 | 20.5 | 15.9 | 13.4 | 14.82 | 49.8% | 29.3% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 8,872 | 0 | 4640 | 4232 | 29.1 | 132.3 | 1400.4 |
| ge_15pp | 3,814 | 0 | 1633 | 2181 | 33.6 | 384.9 | 1380.4 |
| ge_25pp | 2,064 | 0 | 719 | 1345 | 43.9 | 590.3 | 1380.4 |
| lt_10pp | 3,759 | 0 | 2277 | 1482 | 27.4 | 53.7 | 1102.2 |

Current slate `SL-20261001T060903Z-e287b410`: 493 priced rows, quote age at build {'median': 25.5, 'max': 59.7}, freshness {'AGING': 413, 'STALE': 80}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 118 | 21.2 | 11.0 | 20.3 | 21.2 | 24.6 | 1.7 | 0.0 | 7.95 | 26.3% | 1.7% |
| MARKETS_AGREE | 8 | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.96 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 11 | 0.0 | 0.0 | 9.1 | 45.5 | 45.5 | 0.0 | 0.0 | 13.64 | 45.5% | 0.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 3,402 | 138 (4.1%) | 8.0% | 0.0% | {"EXTERNAL_STALE": 118, "AGREES_WITH_KALSHI": 11, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 1,495 | 36 (2.4%) | 13.9% | 0.0% | {"EXTERNAL_STALE": 31, "AGREES_WITH_KALSHI": 5} |
| fair_v1_ge_25pp | 850 | 2 (0.2%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 2} |
| fair_v1_ge_25pp_pregame_clean | 353 | 2 (0.6%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 2} |
| fair_v1_lt_10pp | 1,410 | 72 (5.1%) | 1.4% | 0.0% | {"EXTERNAL_STALE": 62, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1, "AGREES_WITH_KALSHI": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 682 | 13.1 | 8.1 | 17.9 | 15.5 | 20.8 | 15.0 | 9.7 | 13.52 | 45.5% | 24.6% |
| 4-10x | 494 | 12.8 | 9.7 | 18.4 | 14.4 | 18.6 | 14.2 | 11.9 | 13.01 | 44.7% | 26.1% |
| <2x | 1,796 | 14.0 | 10.5 | 20.2 | 15.1 | 17.7 | 12.9 | 9.6 | 11.57 | 40.2% | 22.5% |
| >=10x | 430 | 10.0 | 6.3 | 16.1 | 11.4 | 21.6 | 22.3 | 12.3 | 18.39 | 56.3% | 34.6% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 831 | 13.0 | 9.4 | 22.1 | 15.4 | 17.8 | 11.8 | 10.5 | 11.98 | 40.1% | 22.3% |
| 300-1000 | 846 | 14.4 | 8.8 | 18.0 | 15.6 | 19.3 | 14.8 | 9.2 | 12.93 | 43.3% | 24.0% |
| <300 | 940 | 8.5 | 6.3 | 15.1 | 11.8 | 22.4 | 21.9 | 13.9 | 18.88 | 58.3% | 35.9% |
| >=3000 | 785 | 17.4 | 13.6 | 21.3 | 16.1 | 15.7 | 9.0 | 6.9 | 9.53 | 31.6% | 15.9% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 136 | 0.5273 | 0.3971 | 0.4412 | +0.086 | -0.044 | 0.0109 ± 0.0127 |
| ratio 4-10x | 103 | 0.5795 | 0.4469 | 0.4951 | +0.084 | -0.048 | 0.0086 ± 0.0142 |
| ratio <2x | 261 | 0.5369 | 0.4159 | 0.4789 | +0.058 | -0.063 | 0.0075 ± 0.0081 |
| ratio >=10x | 96 | 0.5315 | 0.3612 | 0.4479 | +0.084 | -0.087 | 0.0174 ± 0.0195 |
| thinner_sample 1000-3000 | 137 | 0.5559 | 0.4376 | 0.4818 | +0.074 | -0.044 | -0.0005 ± 0.0113 |
| thinner_sample 300-1000 | 170 | 0.5561 | 0.4306 | 0.5118 | +0.044 | -0.081 | -0.0041 ± 0.0107 |
| thinner_sample <300 | 219 | 0.5321 | 0.3709 | 0.4384 | +0.094 | -0.067 | 0.0245 ± 0.0117 |
| thinner_sample >=3000 | 70 | 0.5046 | 0.4124 | 0.4286 | +0.076 | -0.016 | 0.0197 ± 0.0122 |
| data_status ADEQUATE | 139 | 0.5257 | 0.4203 | 0.4604 | +0.065 | -0.040 | 0.0046 ± 0.0098 |
| data_status LIMITED | 135 | 0.5731 | 0.4575 | 0.5185 | +0.055 | -0.061 | -0.0014 ± 0.0118 |
| data_status POOR | 322 | 0.5346 | 0.3822 | 0.4503 | +0.084 | -0.068 | 0.0171 ± 0.0092 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 99 | 0.1894 | 0.191 | -0.0016 ± 0.0016 | 0.5568 | 0.561 | 0.4992 | 0.4842 | 0.5051 | -0.104 ± 0.0477 | -0.01 (3) |
| 3-5 | 65 | 0.1653 | 0.1641 | +0.0011 ± 0.0042 | 0.5062 | 0.5002 | 0.5347 | 0.4938 | 0.4923 | -0.097 ± 0.0538 | 0.02 (1) |
| 5-10 | 122 | 0.2011 | 0.207 | -0.0059 ± 0.0062 | 0.5854 | 0.5959 | 0.5272 | 0.4525 | 0.5328 | -0.047 ± 0.042 | -0.02 (1) |
| 10-15 | 99 | 0.2156 | 0.215 | +0.0007 ± 0.0117 | 0.6162 | 0.6141 | 0.5276 | 0.4026 | 0.4646 | -0.058 ± 0.0469 | -0.0633 (3) |
| 15-25 | 127 | 0.2071 | 0.2049 | +0.0022 ± 0.0155 | 0.5991 | 0.5869 | 0.5519 | 0.3561 | 0.4567 | -0.019 ± 0.0379 | -0.015 (2) |
| 25-40 | 68 | 0.2385 | 0.1851 | +0.0533 ± 0.0328 | 0.6675 | 0.5431 | 0.6053 | 0.2866 | 0.3529 | -0.073 ± 0.05 | -0.01 (1) |
| 40+ | 16 | 0.3076 | 0.132 | +0.1756 ± 0.0837 | 0.7987 | 0.4203 | 0.6612 | 0.2147 | 0.25 | -0.080 ± 0.0809 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 242 | 0.1821 | 0.1828 | -0.0008 ± 0.001 | 0.5385 | 0.5397 | 0.5213 | 0.5064 | 0.5372 | -0.045 ± 0.0287 | -0.0188 (8) |
| 3-5 | 174 | 0.1774 | 0.1765 | +0.0009 ± 0.0026 | 0.5319 | 0.5239 | 0.4918 | 0.4515 | 0.454 | -0.058 ± 0.0331 | 0.02 (1) |
| 5-10 | 350 | 0.1845 | 0.1906 | -0.0060 ± 0.0034 | 0.5458 | 0.5548 | 0.4839 | 0.4103 | 0.4914 | +0.009 ± 0.0234 | -0.015 (2) |
| 10-15 | 281 | 0.1832 | 0.1745 | +0.0087 ± 0.0062 | 0.5435 | 0.5114 | 0.4668 | 0.3423 | 0.3701 | -0.040 ± 0.0249 | -0.0633 (3) |
| 15-25 | 413 | 0.1854 | 0.1529 | +0.0324 ± 0.0077 | 0.5556 | 0.4561 | 0.4648 | 0.2673 | 0.2857 | -0.043 ± 0.0188 | -0.02 (3) |
| 25-40 | 408 | 0.2135 | 0.0856 | +0.1279 ± 0.0092 | 0.6191 | 0.286 | 0.4906 | 0.1703 | 0.1324 | -0.083 ± 0.0139 | -0.01 (1) |
| 40+ | 292 | 0.3584 | 0.0336 | +0.3249 ± 0.0112 | 0.9261 | 0.1449 | 0.6061 | 0.0933 | 0.0411 | -0.077 ± 0.0098 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 58 | 0.1698 | 0.1716 | -0.0018 ± 0.0018 | 0.5115 | 0.5153 | 0.4904 | 0.4757 | 0.5517 | -0.036 ± 0.0529 | -0.01 (1) |
| 3-5 | 41 | 0.2315 | 0.2299 | +0.0016 ± 0.0061 | 0.6414 | 0.642 | 0.5081 | 0.4689 | 0.4634 | -0.098 ± 0.0806 | 0.02 (1) |
| 5-10 | 113 | 0.1945 | 0.1891 | +0.0054 ± 0.0062 | 0.5754 | 0.5586 | 0.5667 | 0.4909 | 0.4779 | -0.131 ± 0.0417 | -0.01 (3) |
| 10-15 | 111 | 0.208 | 0.2017 | +0.0063 ± 0.0107 | 0.6003 | 0.5851 | 0.5855 | 0.4614 | 0.5045 | -0.066 ± 0.0442 | -0.0667 (3) |
| 15-25 | 147 | 0.2244 | 0.2117 | +0.0127 ± 0.015 | 0.6375 | 0.6008 | 0.5804 | 0.3829 | 0.4558 | -0.058 ± 0.0388 | -0.01 (1) |
| 25-40 | 87 | 0.2679 | 0.1704 | +0.0976 ± 0.0276 | 0.7378 | 0.5081 | 0.6386 | 0.3282 | 0.3218 | -0.168 ± 0.0451 | -0.02 (1) |
| 40+ | 39 | 0.3609 | 0.2109 | +0.1500 ± 0.0742 | 0.9958 | 0.615 | 0.7456 | 0.2533 | 0.359 | +0.001 ± 0.0679 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 189 | 0.1433 | 0.1449 | -0.0016 ± 0.001 | 0.4417 | 0.4461 | 0.5295 | 0.5149 | 0.5608 | -0.013 ± 0.0272 | -0.0217 (6) |
| 3-5 | 101 | 0.1787 | 0.1772 | +0.0015 ± 0.0034 | 0.5199 | 0.519 | 0.5493 | 0.5093 | 0.505 | -0.064 ± 0.0431 | 0.02 (1) |
| 5-10 | 320 | 0.1993 | 0.2007 | -0.0014 ± 0.0038 | 0.5852 | 0.5797 | 0.5265 | 0.4513 | 0.4938 | -0.023 ± 0.0253 | -0.01 (4) |
| 10-15 | 329 | 0.1845 | 0.1765 | +0.0080 ± 0.0058 | 0.5481 | 0.5186 | 0.5179 | 0.3937 | 0.4316 | -0.026 ± 0.0236 | -0.0575 (4) |
| 15-25 | 402 | 0.1976 | 0.1642 | +0.0333 ± 0.008 | 0.5809 | 0.4854 | 0.5047 | 0.3094 | 0.3308 | -0.052 ± 0.0203 | -0.01 (1) |
| 25-40 | 425 | 0.2277 | 0.1004 | +0.1272 ± 0.0097 | 0.655 | 0.323 | 0.5246 | 0.2083 | 0.1694 | -0.097 ± 0.0156 | -0.02 (1) |
| 40+ | 394 | 0.3966 | 0.0598 | +0.3369 ± 0.0143 | 1.0422 | 0.2152 | 0.6531 | 0.1169 | 0.0812 | -0.066 ± 0.0117 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 92 | 0.1687 | 0.1718 | -0.0031 ± 0.0015 | 0.5067 | 0.5142 | 0.526 | 0.5121 | 0.5652 | -0.046 ± 0.043 | 0.0 (3) |
| 3-5 | 62 | 0.1663 | 0.1643 | +0.0020 ± 0.0042 | 0.504 | 0.4987 | 0.53 | 0.4907 | 0.4839 | -0.134 ± 0.0566 | -- (0) |
| 5-10 | 118 | 0.203 | 0.2047 | -0.0017 ± 0.0061 | 0.5938 | 0.5923 | 0.524 | 0.4535 | 0.5085 | -0.049 ± 0.0418 | -0.01 (2) |
| 10-15 | 112 | 0.2235 | 0.2256 | -0.0021 ± 0.0112 | 0.6391 | 0.6377 | 0.551 | 0.4263 | 0.5089 | -0.051 ± 0.0449 | -0.05 (4) |
| 15-25 | 125 | 0.2035 | 0.207 | -0.0035 ± 0.0154 | 0.5966 | 0.5931 | 0.5746 | 0.3813 | 0.488 | -0.022 ± 0.0384 | -0.03 (1) |
| 25-40 | 74 | 0.2405 | 0.1815 | +0.0590 ± 0.0315 | 0.6765 | 0.5349 | 0.5948 | 0.2775 | 0.3378 | -0.076 ± 0.0478 | 0.0 (1) |
| 40+ | 13 | 0.3177 | 0.1578 | +0.1599 ± 0.1041 | 0.8214 | 0.4818 | 0.6902 | 0.2304 | 0.3077 | -0.055 ± 0.0988 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 225 | 0.1661 | 0.1671 | -0.0010 ± 0.001 | 0.5019 | 0.5037 | 0.5347 | 0.5202 | 0.5378 | -0.053 ± 0.0276 | -0.015 (8) |
| 3-5 | 156 | 0.1921 | 0.1906 | +0.0015 ± 0.0028 | 0.5618 | 0.5581 | 0.5118 | 0.4724 | 0.4744 | -0.077 ± 0.0361 | -- (0) |
| 5-10 | 357 | 0.1813 | 0.1784 | +0.0029 ± 0.0033 | 0.5422 | 0.5224 | 0.4778 | 0.4055 | 0.4286 | -0.034 ± 0.0225 | -0.01 (2) |
| 10-15 | 301 | 0.1959 | 0.184 | +0.0119 ± 0.0062 | 0.5757 | 0.535 | 0.487 | 0.3629 | 0.3821 | -0.055 ± 0.0247 | -0.042 (5) |
| 15-25 | 447 | 0.1748 | 0.146 | +0.0288 ± 0.0072 | 0.534 | 0.4407 | 0.4721 | 0.2747 | 0.302 | -0.035 ± 0.0176 | -0.03 (2) |
| 25-40 | 405 | 0.2167 | 0.0929 | +0.1238 ± 0.0097 | 0.6274 | 0.3024 | 0.4932 | 0.1714 | 0.1407 | -0.077 ± 0.0147 | 0.0 (1) |
| 40+ | 269 | 0.3744 | 0.0339 | +0.3404 ± 0.0124 | 0.9751 | 0.1459 | 0.6103 | 0.0916 | 0.0335 | -0.084 ± 0.0102 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 370 | 0.2067 | 0.2066 | +0.0001 ± 0.0008 | 0.5956 | 0.5956 | 0.5076 | 0.4929 | 0.4865 | -0.051 ± 0.0237 | -0.0226 (46) |
| 3-5 | 273 | 0.1934 | 0.1938 | -0.0004 ± 0.0021 | 0.5676 | 0.5652 | 0.4657 | 0.4258 | 0.4542 | -0.024 ± 0.0265 | -0.0059 (32) |
| 5-10 | 581 | 0.1876 | 0.1829 | +0.0047 ± 0.0027 | 0.5584 | 0.5453 | 0.4649 | 0.3917 | 0.3976 | -0.041 ± 0.0178 | -0.0049 (70) |
| 10-15 | 381 | 0.2019 | 0.1885 | +0.0134 ± 0.0056 | 0.5919 | 0.5551 | 0.4519 | 0.3284 | 0.336 | -0.045 ± 0.0221 | 0.002 (61) |
| 15-25 | 513 | 0.234 | 0.2097 | +0.0243 ± 0.0079 | 0.6609 | 0.6055 | 0.5311 | 0.3378 | 0.3723 | -0.031 ± 0.0202 | -0.0216 (58) |
| 25-40 | 251 | 0.2624 | 0.1673 | +0.0951 ± 0.0162 | 0.7248 | 0.5043 | 0.5678 | 0.2561 | 0.259 | -0.061 ± 0.0256 | -0.0216 (25) |
| 40+ | 90 | 0.4349 | 0.1592 | +0.2757 ± 0.0452 | 1.223 | 0.4921 | 0.7344 | 0.2252 | 0.2333 | -0.065 ± 0.044 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 672 | 0.1982 | 0.1976 | +0.0005 ± 0.0006 | 0.5761 | 0.5744 | 0.501 | 0.4862 | 0.4673 | -0.062 ± 0.0171 | -0.0155 (82) |
| 3-5 | 496 | 0.1992 | 0.1986 | +0.0006 ± 0.0016 | 0.5786 | 0.5743 | 0.4729 | 0.4329 | 0.4456 | -0.034 ± 0.02 | -0.018 (54) |
| 5-10 | 1042 | 0.1857 | 0.1794 | +0.0062 ± 0.002 | 0.5544 | 0.5352 | 0.4497 | 0.3759 | 0.3752 | -0.043 ± 0.0133 | -0.0089 (119) |
| 10-15 | 759 | 0.1963 | 0.1815 | +0.0149 ± 0.0039 | 0.5774 | 0.5366 | 0.4445 | 0.3208 | 0.3228 | -0.044 ± 0.0153 | -0.0051 (95) |
| 15-25 | 1052 | 0.2223 | 0.1881 | +0.0342 ± 0.0053 | 0.6403 | 0.5514 | 0.5055 | 0.3098 | 0.3203 | -0.043 ± 0.0134 | -0.0255 (106) |
| 25-40 | 733 | 0.2453 | 0.1287 | +0.1166 ± 0.0084 | 0.6914 | 0.4023 | 0.5277 | 0.212 | 0.1869 | -0.070 ± 0.0131 | -0.0206 (47) |
| 40+ | 443 | 0.3941 | 0.0834 | +0.3106 ± 0.0149 | 1.0773 | 0.2785 | 0.6562 | 0.1406 | 0.1084 | -0.076 ± 0.0141 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 596 | 1.198 ± 0.125 | 1.254 | 0.1642 | 0.1821 | 0.2061 | 0.196 |
| gen2 | 596 | 0.933 ± 0.106 | 1.158 | 0.1828 | 0.1808 | 0.2261 | 0.1968 |
| gen1_elo | 596 | 1.157 ± 0.121 | 1.237 | 0.1715 | 0.1822 | 0.205 | 0.1959 |
| gen1_sr | 596 | 1.135 ± 0.137 | 1.223 | 0.1403 | 0.183 | 0.223 | 0.1961 |
| gen1_ledger | 2459 | 0.901 ± 0.055 | 1.075 | 0.161 | 0.1995 | 0.2197 | 0.1917 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 3,814)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,132 | 29.7% |
| STALE_QUOTE | market_freshness | 1,018 | 26.7% |
| POOR_DATA | data | 358 | 9.4% |
| BOOK_QUALITY | execution | 284 | 7.4% |
| LIMITED_DATA | data | 273 | 7.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 255 | 6.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 206 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 202 | 5.3% |
| IDENTITY_AMBIGUOUS | mapping | 83 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 3 | 0.1% |

Cause class: coverage 29.7%, market_freshness 26.7%, data 16.5%, market_freshness/coverage 12.1%, execution 7.4%, model_calibration_or_unknown 5.3%, mapping 2.2%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 94.8%, LOW_DATA_QUALITY 66.5%, STALE_PLAYER_DATA 58.1%, STALE_KALSHI_QUOTE 57.2%, THIN_PLAYER_HISTORY 53.7%, MODEL_INTERNAL_DISAGREEMENT 32.5%, ASYMMETRIC_SAMPLE_SIZE 29.8%, WIDE_SPREAD 16.1%, PLAYER_IDENTITY_RISK 12.1%, MODEL_HIGH_UNCERTAINTY 10.2%, LEVEL_TRANSFER_RISK 9.5%, EVENT_MAPPING_RISK 7.7%, LOW_DISPLAYED_LIQUIDITY 4.2%, MODEL_CALIBRATION_OUTLIER 2.1%, UNKNOWN 0.9%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 32.8%, POST_SETTLEMENT_OBSERVATION 29.7%, POSSIBLE_IN_PLAY_QUOTE 7.5%, CONFIRMED_IN_PLAY_QUOTE 2.9%

### >= ge_25 pp (N = 2,064)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 888 | 43.0% |
| STALE_QUOTE | market_freshness | 464 | 22.5% |
| POOR_DATA | data | 155 | 7.5% |
| BOOK_QUALITY | execution | 134 | 6.5% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 126 | 6.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 120 | 5.8% |
| LIMITED_DATA | data | 77 | 3.7% |
| IDENTITY_AMBIGUOUS | mapping | 58 | 2.8% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 42 | 2.0% |

Cause class: coverage 43.0%, market_freshness 22.5%, market_freshness/coverage 11.9%, data 11.2%, execution 6.5%, mapping 2.8%, model_calibration_or_unknown 2.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 97.4%, LOW_DATA_QUALITY 71.4%, STALE_KALSHI_QUOTE 65.2%, THIN_PLAYER_HISTORY 56.9%, STALE_PLAYER_DATA 56.7%, MODEL_INTERNAL_DISAGREEMENT 33.1%, ASYMMETRIC_SAMPLE_SIZE 32.4%, PLAYER_IDENTITY_RISK 15.4%, WIDE_SPREAD 14.4%, MODEL_HIGH_UNCERTAINTY 11.1%, EVENT_MAPPING_RISK 9.5%, LEVEL_TRANSFER_RISK 9.2%, LOW_DISPLAYED_LIQUIDITY 4.2%, MODEL_CALIBRATION_OUTLIER 2.9%, UNKNOWN 0.3%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 46.3%, POST_SETTLEMENT_OBSERVATION 43.0%, POSSIBLE_IN_PLAY_QUOTE 7.1%, CONFIRMED_IN_PLAY_QUOTE 3.2%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 1719, "IDENTITY_AMBIGUOUS": 345}; ticker orientation: {"VERIFIED": 2064}.

Checks: discipline:AMBIGUOUS 169, discipline:PASS 1895, identity_confidence:AMBIGUOUS 318, identity_confidence:PASS 1746, level_mapping:NA 181, level_mapping:PASS 1883, market_pair:AMBIGUOUS 56, market_pair:NA 52, market_pair:PASS 1956, model_complement:NA 28, model_complement:PASS 2036, namesake:PASS 2064, physical_match_id:NA 1214, physical_match_id:PASS 850, player_ids:PASS 2064, same_pair_other_event:PASS 2064, ticker_orientation:PASS 2064

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 248 | 2.4% | 2.5% | 0.3% | {"market_freshness": 6} | 5.88 | 0.1838 / 0.1834 (45) | 33.9% | 0.0% | 0.8% | 5.2% |
| CHALLENGER | 1,399 | 17.2% | 7.4% | 11.6% | {"coverage": 127, "market_freshness": 50, "market_freshness/coverage": 32, "data": 15, "model_calibration_or_unknown": 13, "execution": 3} | 7.45 | 0.2197 / 0.1998 (482) | 48.7% | 4.4% | 0.8% | 21.9% |
| DOUBLES | 347 | 48.7% | 48.1% | 8.2% | {"market_freshness": 80, "market_freshness/coverage": 36, "execution": 28, "mapping": 20, "coverage": 5} | 24.11 | 0.3236 / 0.2197 (143) | 58.8% | 0.0% | 100.0% | 23.3% |
| ITF_MEN | 2,868 | 25.3% | 15.0% | 35.1% | {"coverage": 356, "market_freshness": 147, "data": 83, "market_freshness/coverage": 66, "execution": 62, "mapping": 10, "model_calibration_or_unknown": 1} | 9.89 | 0.2126 / 0.1851 (1068) | 49.3% | 52.7% | 5.8% | 29.4% |
| ITF_WOMEN | 2,849 | 28.3% | 17.6% | 39.0% | {"coverage": 388, "market_freshness": 161, "data": 117, "market_freshness/coverage": 70, "execution": 32, "mapping": 26, "model_calibration_or_unknown": 11} | 12.24 | 0.2086 / 0.1921 (959) | 52.2% | 56.0% | 7.2% | 30.7% |
| OTHER | 149 | 8.1% | 7.3% | 0.6% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 619 | 7.6% | 5.7% | 2.3% | {"market_freshness/coverage": 14, "data": 9, "market_freshness": 9, "model_calibration_or_unknown": 6, "execution": 4, "coverage": 4, "mapping": 1} | 8.47 | 0.1995 / 0.1973 (113) | 31.0% | 3.4% | 1.9% | 17.6% |
| WTA125 | 393 | 15.3% | 8.3% | 2.9% | {"market_freshness/coverage": 27, "model_calibration_or_unknown": 9, "market_freshness": 9, "data": 8, "coverage": 7} | 10.43 | 0.2317 / 0.2049 (203) | 32.8% | 9.7% | 0.5% | 20.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 2 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 3 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 4 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 5 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 6 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 7 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 8 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 9 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 10 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 11 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 12 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 13 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 14 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 15 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 16 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 17 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 18 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 19 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 20 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 21 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 22 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 708 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 23 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 24 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 25 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 26 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 27 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | IN_PLAY_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | first-ball truth shows the match under way at the quote time; quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 28 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 114 min (STALE); data LIMITED (grade B, thinner serve sample 2163.0, ratio 2.0); no external reference |
| 29 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 30 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 31 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | IN_PLAY_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | first-ball truth shows the match under way at the quote time; quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 32 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |
| 33 | `KXITFWMATCH-26SEP30KOKUEM-KOK` | ITF_WOMEN | fair_v1 | 79% / 10% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 86 min (STALE); data LIMITED (grade C, thinner serve sample 824.0, ratio 2.35); no external reference |
| 34 | `KXITFMATCH-26SEP20WILRAH-RAH` | ITF_MEN | gen1_ledger | 72% / 4% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade B, thinner serve sample 2782.0, ratio 1.84); no external reference |
| 35 | `KXITFMATCH-26SEP26NAGTHO-NAG` | ITF_MEN | gen1_ledger | 76% / 7% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 89 min (STALE); data LIMITED (grade C, thinner serve sample 1323.0, ratio 4.45); no external reference |
| 36 | `KXITFWMATCH-26SEP26PERPRE-PER` | ITF_WOMEN | gen1_ledger | 78% / 10% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 102 min (STALE); data POOR (grade D, thinner serve sample 1020.0, ratio 2.77); no external reference |
| 37 | `KXITFMATCH-26SEP22YILAGA-AGA` | ITF_MEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 203 min (STALE); data LIMITED (grade B, thinner serve sample 2786.0, ratio 2.08); no external reference |
| 38 | `KXITFMATCH-26SEP30DIMURA-URA` | ITF_MEN | fair_v1 | 71% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.1h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 793 min (STALE); data POOR (grade F, thinner serve sample 174.0, ratio 2.63); no external reference |
| 39 | `KXITFWMATCH-26SEP20LLIBON-BON` | ITF_WOMEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 69 min (STALE); data POOR (grade D, thinner serve sample 1210.0, ratio 3.0); no external reference |
| 40 | `KXATPCHALLENGERDOUBLES-26SEP17ARESTEBLASCH-BLASCH` | DOUBLES | gen1_ledger | 95% / 28% | +67 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 79 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 41 | `KXITFWMATCH-26SEP24BOUKUR-BOU` | ITF_WOMEN | gen1_ledger | 76% / 8% | +67 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 113 min (STALE); data POOR (grade D, thinner serve sample 1497.0, ratio 2.48); no external reference |
| 42 | `KXATPCHALLENGERMATCH-26SEP28TABSAN-SAN` | CHALLENGER | gen1_ledger | 70% / 4% | +67 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 48 min (STALE); no external reference |
| 43 | `KXITFWMATCH-26SEP22SHCPAS-PAS` | ITF_WOMEN | gen1_ledger | 69% / 2% | +66 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 199 min (STALE); data POOR (grade F, thinner serve sample 239.0, ratio 5.93); no external reference |
| 44 | `KXITFWMATCH-26SEP29KRURAY-KRU` | ITF_WOMEN | fair_v1 | 78% / 12% | +66 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 126 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 223.0); no external reference |
| 45 | `KXWTADOUBLES-26SEP20DETKHRPRETAR-PRETAR` | DOUBLES | gen1_ledger | 84% / 18% | +66 | IN_PLAY_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | first-ball truth shows the match under way at the quote time; quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 46 | `KXITFWMATCH-26SEP30BIOKRO-KRO` | ITF_WOMEN | fair_v1 | 68% / 2% | +66 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 170 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 3.24); no external reference |
| 47 | `KXITFMATCH-26SEP12EFSMOR-MOR` | ITF_MEN | gen1_ledger | 67% / 2% | +66 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 36 min (STALE); data LIMITED (grade B, thinner serve sample 3783.0, ratio 1.33); no external reference |
| 48 | `KXATPCHALLENGERDOUBLES-26SEP17TROUCHBAYKAD-TROUCH` | DOUBLES | gen1_ledger | 87% / 21% | +66 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 21 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 49 | `KXITFWMATCH-26SEP30BRAKUH-BRA` | ITF_WOMEN | fair_v1 | 82% / 16% | +65 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 53 min (STALE); no external reference |
| 50 | `KXITFMATCH-26SEP23BAKBAL-BAK` | ITF_MEN | gen1_ledger | 69% / 4% | +65 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 89.0, ratio 20.62); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9744, "by_level_share_of_ge_25pp": {"ATP": 0.0029, "CHALLENGER": 0.1163, "DOUBLES": 0.0819, "ITF_MEN": 0.3513, "ITF_WOMEN": 0.39, "OTHER": 0.0058, "WTA": 0.0228, "WTA125": 0.0291}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.6516, "share_primary_cause_market_settled_or_in_play": 0.5493, "share_primary_cause_stale_quote_only": 0.2248}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 2064, "identity_ambiguous_share": 0.1672, "ticker_orientation": {"VERIFIED": 2064}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 850, "with_external": 2, "coverage": 0.0024, "external_status": {"EXTERNAL_STALE": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 2}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 353, "with_external": 2, "coverage": 0.0057, "external_status": {"EXTERNAL_STALE": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 2}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 666.0, "median_sample_ratio": 2.5, "median_min_matches": 23.0, "median_max_days_since_last": 176.0, "share_severe_asymmetry": 0.1788, "data_status": {"POOR": 1019, "LIMITED": 725, "ADEQUATE": 320}, "comparison_lt_10pp": {"median_thinner_serve_points": 1969.5, "median_sample_ratio": 1.71, "median_min_matches": 79.5}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 136, "model_minus_observed": 0.0862, "kalshi_minus_observed": -0.0441, "brier_diff_model_minus_kalshi": 0.0109}, "4-10x": {"n": 103, "model_minus_observed": 0.0844, "kalshi_minus_observed": -0.0483, "brier_diff_model_minus_kalshi": 0.0086}, "<2x": {"n": 261, "model_minus_observed": 0.058, "kalshi_minus_observed": -0.0631, "brier_diff_model_minus_kalshi": 0.0075}, ">=10x": {"n": 96, "model_minus_observed": 0.0836, "kalshi_minus_observed": -0.0867, "brier_diff_model_minus_kalshi": 0.0174}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 596, "model": {"intercept": -0.61, "slope": 0.933, "slope_se": 0.106}, "kalshi_mid_same_rows": {"intercept": 0.232, "slope": 1.158, "slope_se": 0.115}, "mean_extremity_model": 0.1828, "mean_extremity_kalshi": 0.1808, "model_brier": 0.2261, "kalshi_brier": 0.1968, "brier_diff_model_minus_kalshi": 0.0293, "brier_diff_se": 0.0078, "model_logloss": 0.6449, "kalshi_logloss": 0.5718}, "fair_v1": {"n": 596, "model": {"intercept": -0.381, "slope": 1.198, "slope_se": 0.125}, "kalshi_mid_same_rows": {"intercept": 0.403, "slope": 1.254, "slope_se": 0.12}, "mean_extremity_model": 0.1642, "mean_extremity_kalshi": 0.1821, "model_brier": 0.2061, "kalshi_brier": 0.196, "brier_diff_model_minus_kalshi": 0.01, "brier_diff_se": 0.0061, "model_logloss": 0.5951, "kalshi_logloss": 0.57}, "gen1_elo": {"n": 596, "model": {"intercept": -0.363, "slope": 1.157, "slope_se": 0.121}, "kalshi_mid_same_rows": {"intercept": 0.412, "slope": 1.237, "slope_se": 0.117}, "mean_extremity_model": 0.1715, "mean_extremity_kalshi": 0.1822, "model_brier": 0.205, "kalshi_brier": 0.1959, "brier_diff_model_minus_kalshi": 0.0091, "brier_diff_se": 0.0062, "model_logloss": 0.5954, "kalshi_logloss": 0.5697}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2499, "share_ge_15": 0.4394, "median_abs_gap": 12.84, "n": 3402}, "gen1_elo": {"share_ge_25": 0.2428, "share_ge_15": 0.4295, "median_abs_gap": 12.46, "n": 3402}, "gen1_sr": {"share_ge_25": 0.3157, "share_ge_15": 0.5259, "median_abs_gap": 16.0, "n": 3402}, "gen2": {"share_ge_25": 0.3122, "share_ge_15": 0.5091, "median_abs_gap": 15.39, "n": 3402}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1381, "share_ge_15": 0.3316, "median_abs_gap": 9.98, "n": 2557}, "gen1_elo": {"share_ge_25": 0.1388, "share_ge_15": 0.3187, "median_abs_gap": 9.58, "n": 2557}, "gen1_sr": {"share_ge_25": 0.2053, "share_ge_15": 0.4372, "median_abs_gap": 13.14, "n": 2557}, "gen2": {"share_ge_25": 0.2131, "share_ge_15": 0.4298, "median_abs_gap": 13.05, "n": 2557}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.88, "share_ge_25_all": 0.0242, "share_ge_25_pregame_clean": 0.0255}, "WTA": {"median_abs_gap_pregame_clean": 8.47, "share_ge_25_all": 0.0759, "share_ge_25_pregame_clean": 0.0569}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2262, "share_within_10pp_all": 0.4237, "share_within_10pp_pregame_clean": 0.5007, "corr_model_vs_mid_pregame_clean": 0.8319}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 99, "model_brier": 0.1894, "kalshi_brier": 0.191, "brier_diff_model_minus_kalshi": -0.0016}, "10-15": {"n_settled": 99, "model_brier": 0.2156, "kalshi_brier": 0.215, "brier_diff_model_minus_kalshi": 0.0007}, "15-25": {"n_settled": 127, "model_brier": 0.2071, "kalshi_brier": 0.2049, "brier_diff_model_minus_kalshi": 0.0022}, "25-40": {"n_settled": 68, "model_brier": 0.2385, "kalshi_brier": 0.1851, "brier_diff_model_minus_kalshi": 0.0533}, "3-5": {"n_settled": 65, "model_brier": 0.1653, "kalshi_brier": 0.1641, "brier_diff_model_minus_kalshi": 0.0011}, "40+": {"n_settled": 16, "model_brier": 0.3076, "kalshi_brier": 0.132, "brier_diff_model_minus_kalshi": 0.1756}, "5-10": {"n_settled": 122, "model_brier": 0.2011, "kalshi_brier": 0.207, "brier_diff_model_minus_kalshi": -0.0059}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%)
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap).
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 143, "model_brier": 0.3236, "kalshi_brier": 0.2197, "brier_diff_model_minus_kalshi": 0.1038, "brier_diff_se": 0.0277, "corr_model_outcome": -0.059, "corr_kalshi_outcome": 0.3814}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
