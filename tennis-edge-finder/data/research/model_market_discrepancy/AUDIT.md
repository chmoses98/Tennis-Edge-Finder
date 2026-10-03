# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-03T11:52Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 10,987): 0-3 13.3%, 3-5 9.0%, 5-10 19.4%, 10-15 14.9%, 15-25 19.6%, 25-40 14.3%, 40+ 9.6%; median gap 12.57 pp.
* **Where the extremes live**: 96.7% of >=25 pp gaps are off the ATP/WTA main tour (ITF 74.5%, Challenger 12.0%, doubles 7.0%). Main tour: ATP 3.8% and WTA 9.4% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 2,616): MARKET_ALREADY_SETTLED_WHEN_PRICED 47.1%, STALE_QUOTE 23.8%, POOR_DATA 6.3%, BOOK_QUALITY 5.8%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IN_PLAY_QUOTE 3.8%, LIMITED_DATA 3.1%, IDENTITY_AMBIGUOUS 2.6%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%. By class: coverage 47.1%, market_freshness 23.8%, data 9.4%, market_freshness/coverage 9.2%, execution 5.8%, mapping 2.6%, model_calibration_or_unknown 2.2%.
* **Stale / settled / in-play**: 70.1% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 56.3% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 2,616 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 14.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 0.5%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 7.6% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 824.0 points vs 1980.5 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.114, Gen-2 0.948, Gen-1 ledger 0.885 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 90 model 0.2352 vs Kalshi 0.181; n 26 model 0.3509 vs Kalshi 0.1453.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 35,102 model-market comparisons (60,644 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 16,564 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-03T11:49:58.967266+00:00'], shadow board 9,857 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-03T11:50:01.333504+00:00'], Model 4 2,926 rows, 8,238 settled tickers, 1,807 tickers with an external scan.
* By model: {"gen1_ledger": 9633, "gen1_elo": 4959, "fair_v1": 4959, "gen2": 4959, "gen1_sr": 4959, "model4_fundamental": 2821, "model4_conditioned": 2812}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 10,987 | 13.3 | 9.0 | 19.4 | 14.9 | 19.6 | 14.3 | 9.6 | 12.57 | 43.4% | 23.8% |
| MW fair_v1 | 4,959 | 13.5 | 8.4 | 18.6 | 15.1 | 18.7 | 14.9 | 10.9 | 13.01 | 44.5% | 25.8% |
| MW gen1_elo | 4,959 | 13.0 | 8.8 | 19.9 | 15.0 | 18.2 | 14.8 | 10.3 | 12.5 | 43.2% | 25.1% |
| MW gen1_ledger | 6,028 | 13.2 | 9.4 | 20.1 | 14.7 | 20.4 | 13.8 | 8.4 | 12.21 | 42.5% | 22.2% |
| MW gen1_sr | 4,959 | 9.7 | 7.0 | 16.7 | 13.3 | 22.4 | 18.5 | 12.4 | 16.35 | 53.3% | 30.9% |
| MW gen2 | 4,959 | 11.2 | 6.3 | 16.6 | 14.8 | 20.1 | 17.2 | 13.7 | 15.48 | 51.0% | 30.9% |
| all families model4_conditioned | 2,812 | 18.6 | 15.5 | 29.6 | 23.8 | 8.2 | 2.4 | 1.9 | 7.37 | 12.5% | 4.3% |
| all families model4_fundamental | 2,821 | 14.5 | 10.7 | 30.0 | 21.8 | 14.6 | 5.5 | 3.0 | 9.09 | 23.0% | 8.4% |

Configurable thresholds (primary): >=5pp 77.7%, >=10pp 58.3%, >=15pp 43.4%, >=20pp 32.9%, >=25pp 23.8%, >=30pp 17.6%, >=40pp 9.6%, >=50pp 4.3%
Executable gap (model outside the book, before fees): median 10.25pp; >=10pp 50.6%, >=25pp 21.2%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 241 | 22.4 | 17.4 | 27.4 | 12.9 | 14.9 | 1.2 | 3.7 | 6.16 | 19.9% | 5.0% |
| CHALLENGER | 858 | 14.8 | 9.2 | 15.8 | 16.3 | 15.6 | 15.2 | 13.1 | 13.29 | 43.8% | 28.2% |
| ITF_MEN | 1,605 | 12.0 | 8.4 | 19.8 | 14.9 | 17.6 | 14.8 | 12.6 | 12.81 | 44.9% | 27.4% |
| ITF_WOMEN | 1,736 | 10.6 | 6.3 | 15.8 | 15.1 | 21.6 | 18.8 | 11.8 | 15.91 | 52.1% | 30.5% |
| WTA | 435 | 23.0 | 10.6 | 25.8 | 12.6 | 18.9 | 6.7 | 2.5 | 8.16 | 28.1% | 9.2% |
| WTA125 | 84 | 14.3 | 4.8 | 17.9 | 23.8 | 20.2 | 14.3 | 4.8 | 12.4 | 39.3% | 19.1% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 241 | 23.2 | 12.9 | 24.9 | 16.2 | 17.0 | 1.7 | 4.2 | 7.08 | 22.8% | 5.8% |
| CHALLENGER | 858 | 11.1 | 5.1 | 17.7 | 16.4 | 18.9 | 18.1 | 12.7 | 14.93 | 49.6% | 30.8% |
| ITF_MEN | 1,605 | 9.9 | 6.2 | 17.5 | 15.6 | 20.3 | 16.4 | 14.1 | 15.39 | 50.8% | 30.5% |
| ITF_WOMEN | 1,736 | 8.9 | 6.2 | 14.1 | 12.7 | 20.4 | 19.8 | 18.0 | 18.5 | 58.2% | 37.8% |
| WTA | 435 | 20.5 | 5.5 | 16.8 | 15.6 | 22.3 | 16.8 | 2.5 | 12.98 | 41.6% | 19.3% |
| WTA125 | 84 | 6.0 | 6.0 | 16.7 | 20.2 | 22.6 | 15.5 | 13.1 | 15.56 | 51.2% | 28.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 241 | 28.2 | 12.9 | 28.6 | 10.8 | 9.1 | 6.6 | 3.7 | 6.53 | 19.5% | 10.4% |
| CHALLENGER | 858 | 15.2 | 8.3 | 21.1 | 14.0 | 13.5 | 14.1 | 13.9 | 11.53 | 41.5% | 28.0% |
| ITF_MEN | 1,605 | 10.2 | 9.7 | 18.7 | 16.0 | 17.9 | 15.6 | 12.0 | 13.04 | 45.5% | 27.5% |
| ITF_WOMEN | 1,736 | 9.6 | 6.6 | 16.6 | 14.4 | 23.9 | 18.4 | 10.4 | 16.49 | 52.7% | 28.9% |
| WTA | 435 | 23.4 | 14.0 | 29.4 | 15.6 | 11.5 | 4.4 | 1.6 | 6.99 | 17.5% | 6.0% |
| WTA125 | 84 | 16.7 | 6.0 | 22.6 | 29.8 | 13.1 | 10.7 | 1.2 | 10.92 | 25.0% | 11.9% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 72 | 23.6 | 22.2 | 34.7 | 12.5 | 6.9 | 0.0 | 0.0 | 6.26 | 6.9% | 0.0% |
| CHALLENGER | 807 | 21.2 | 13.8 | 26.6 | 16.1 | 13.3 | 6.4 | 2.6 | 7.45 | 22.3% | 9.0% |
| DOUBLES | 381 | 5.8 | 3.9 | 9.7 | 10.5 | 22.1 | 20.7 | 27.3 | 24.04 | 70.1% | 48.0% |
| ITF_MEN | 2,044 | 14.2 | 9.2 | 18.9 | 14.0 | 20.7 | 13.5 | 9.4 | 12.4 | 43.7% | 22.9% |
| ITF_WOMEN | 1,875 | 8.9 | 8.3 | 17.5 | 14.1 | 23.9 | 18.4 | 9.0 | 15.43 | 51.2% | 27.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 363 | 15.4 | 9.4 | 25.6 | 22.3 | 17.6 | 8.8 | 0.8 | 9.8 | 27.3% | 9.6% |
| WTA125 | 337 | 13.3 | 9.5 | 21.7 | 16.9 | 22.9 | 11.9 | 3.9 | 11.35 | 38.6% | 15.7% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 240 | 22.1 | 17.5 | 27.5 | 12.9 | 15.0 | 1.2 | 3.8 | 6.19 | 20.0% | 5.0% |
| CHALLENGER | 631 | 18.7 | 11.4 | 19.3 | 19.5 | 16.8 | 9.2 | 5.1 | 10.34 | 31.1% | 14.3% |
| ITF_MEN | 1,015 | 15.8 | 11.8 | 24.9 | 16.6 | 17.2 | 9.6 | 4.0 | 9.47 | 30.8% | 13.6% |
| ITF_WOMEN | 1,161 | 14.5 | 8.3 | 19.1 | 17.6 | 22.8 | 13.0 | 4.7 | 12.6 | 40.5% | 17.7% |
| WTA | 434 | 23.0 | 10.6 | 25.8 | 12.7 | 18.9 | 6.5 | 2.5 | 8.16 | 27.9% | 9.0% |
| WTA125 | 81 | 14.8 | 4.9 | 18.5 | 24.7 | 19.8 | 12.3 | 4.9 | 11.65 | 37.0% | 17.3% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 240 | 23.3 | 12.5 | 25.0 | 16.2 | 17.1 | 1.7 | 4.2 | 7.29 | 22.9% | 5.8% |
| CHALLENGER | 631 | 13.8 | 6.5 | 22.4 | 20.0 | 20.4 | 12.8 | 4.1 | 11.92 | 37.4% | 17.0% |
| ITF_MEN | 1,015 | 13.3 | 7.7 | 21.7 | 17.9 | 21.3 | 12.6 | 5.5 | 11.89 | 39.4% | 18.1% |
| ITF_WOMEN | 1,161 | 10.8 | 8.1 | 16.1 | 12.5 | 23.6 | 17.3 | 11.5 | 15.94 | 52.4% | 28.8% |
| WTA | 434 | 20.5 | 5.5 | 16.8 | 15.7 | 22.4 | 16.6 | 2.5 | 12.96 | 41.5% | 19.1% |
| WTA125 | 81 | 6.2 | 6.2 | 16.1 | 21.0 | 23.5 | 16.1 | 11.1 | 15.33 | 50.6% | 27.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 62 | 24.2 | 25.8 | 35.5 | 12.9 | 1.6 | 0.0 | 0.0 | 5.45 | 1.6% | 0.0% |
| CHALLENGER | 660 | 23.6 | 16.1 | 29.4 | 15.8 | 12.4 | 2.6 | 0.1 | 6.68 | 15.2% | 2.7% |
| DOUBLES | 344 | 6.1 | 3.8 | 9.9 | 10.5 | 21.8 | 20.9 | 27.0 | 24.02 | 69.8% | 48.0% |
| ITF_MEN | 1,454 | 17.3 | 11.1 | 22.1 | 15.1 | 20.7 | 10.0 | 3.6 | 9.87 | 34.3% | 13.6% |
| ITF_WOMEN | 1,270 | 10.9 | 9.8 | 21.3 | 16.2 | 24.9 | 14.7 | 2.2 | 12.16 | 41.7% | 16.9% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 334 | 15.6 | 9.9 | 26.4 | 23.1 | 18.3 | 6.9 | 0.0 | 9.55 | 25.1% | 6.9% |
| WTA125 | 259 | 15.8 | 10.4 | 25.9 | 20.1 | 21.2 | 6.2 | 0.4 | 9.54 | 27.8% | 6.6% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 381 | 5.8 | 3.9 | 9.7 | 10.5 | 22.1 | 20.7 | 27.3 | 24.04 | 70.1% | 48.0% |
| singles | 5,647 | 13.7 | 9.8 | 20.8 | 15.0 | 20.3 | 13.3 | 7.1 | 11.75 | 40.7% | 20.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 1,078 | 15.5 | 8.5 | 18.9 | 14.6 | 15.9 | 14.0 | 12.6 | 12.33 | 42.5% | 26.6% |
| Hard | 3,549 | 12.8 | 8.6 | 18.8 | 14.8 | 19.4 | 15.1 | 10.4 | 13.16 | 44.9% | 25.5% |
| UNKNOWN | 332 | 14.2 | 5.7 | 14.8 | 19.3 | 19.9 | 15.1 | 11.1 | 13.72 | 46.1% | 26.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,548 | 17.4 | 10.2 | 20.7 | 14.8 | 17.3 | 11.1 | 8.5 | 10.4 | 36.9% | 19.6% |
| B | 708 | 17.5 | 10.7 | 17.2 | 16.8 | 15.7 | 10.2 | 11.9 | 11.17 | 37.7% | 22.0% |
| C | 821 | 12.2 | 8.2 | 22.3 | 13.5 | 16.9 | 15.7 | 11.2 | 12.93 | 43.9% | 26.9% |
| D | 922 | 11.2 | 7.7 | 17.7 | 14.4 | 20.8 | 15.6 | 12.6 | 14.48 | 49.0% | 28.2% |
| F | 960 | 7.6 | 4.6 | 13.8 | 16.2 | 22.5 | 22.9 | 12.4 | 18.48 | 57.8% | 35.3% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,858 | 18.7 | 12.0 | 26.2 | 16.8 | 16.3 | 6.9 | 3.1 | 8.63 | 26.3% | 10.0% |
| B | 996 | 13.8 | 9.5 | 21.5 | 16.1 | 19.4 | 12.4 | 7.3 | 11.56 | 39.2% | 19.8% |
| C | 1,245 | 11.2 | 8.3 | 15.7 | 13.8 | 22.2 | 15.4 | 13.2 | 15.33 | 50.8% | 28.6% |
| D | 926 | 11.1 | 8.1 | 20.6 | 11.9 | 24.1 | 15.3 | 8.9 | 14.25 | 48.3% | 24.2% |
| F | 1,003 | 6.9 | 7.2 | 12.3 | 13.3 | 23.1 | 24.2 | 13.1 | 18.97 | 60.4% | 37.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 1,917 | 16.7 | 9.6 | 19.8 | 15.8 | 16.9 | 11.2 | 10.0 | 10.95 | 38.0% | 21.2% |
| LIMITED | 1,142 | 14.7 | 10.2 | 21.4 | 13.4 | 16.4 | 13.7 | 10.2 | 11.48 | 40.2% | 23.8% |
| POOR | 1,900 | 9.5 | 6.0 | 15.6 | 15.4 | 21.9 | 19.3 | 12.4 | 16.55 | 53.5% | 31.6% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 341 | 34.3 | 22.9 | 33.1 | 6.5 | 2.4 | 0.9 | 0.0 | 4.16 | 3.2% | 0.9% |
| GAME_SPREAD | 406 | 19.9 | 16.5 | 37.0 | 16.0 | 8.9 | 1.2 | 0.5 | 6.59 | 10.6% | 1.7% |
| MATCH_WINNER | 6,028 | 13.2 | 9.4 | 20.1 | 14.7 | 20.4 | 13.8 | 8.4 | 12.21 | 42.5% | 22.2% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 1,702 | 21.7 | 13.4 | 30.6 | 17.2 | 13.6 | 2.8 | 0.7 | 7.04 | 17.0% | 3.4% |
| TOTAL_GAMES | 1,132 | 9.9 | 9.4 | 26.5 | 24.9 | 17.0 | 8.0 | 4.4 | 10.66 | 29.3% | 12.4% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 883 | 28.8 | 32.7 | 26.9 | 0.7 | 8.7 | 1.7 | 0.5 | 4.27 | 10.9% | 2.1% |
| GAME_SPREAD | 565 | 36.6 | 15.0 | 25.3 | 17.9 | 2.5 | 1.9 | 0.7 | 4.55 | 5.1% | 2.6% |
| TOTAL_GAMES | 1,364 | 4.5 | 4.5 | 33.1 | 41.3 | 10.3 | 3.1 | 3.2 | 10.72 | 16.6% | 6.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 883 | 26.2 | 16.8 | 33.8 | 8.2 | 9.8 | 4.3 | 1.0 | 5.79 | 15.2% | 5.3% |
| GAME_SPREAD | 565 | 17.5 | 10.3 | 25.5 | 23.2 | 15.9 | 5.1 | 2.5 | 9.56 | 23.5% | 7.6% |
| TOTAL_GAMES | 1,373 | 5.8 | 7.0 | 29.4 | 29.9 | 17.0 | 6.3 | 4.4 | 10.91 | 27.8% | 10.8% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4,959 | 44.5% | 25.8% | 13.01 | 33.1% | 14.0% | 9.99 |
| gen1_elo | 4,959 | 43.2% | 25.1% | 12.5 | 31.2% | 14.0% | 9.51 |
| gen1_sr | 4,959 | 53.3% | 30.9% | 16.35 | 43.5% | 19.6% | 12.7 |
| gen2 | 4,959 | 51.0% | 30.9% | 15.48 | 42.7% | 20.9% | 12.83 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 1,869 | 17.8 | 12.2 | 23.3 | 15.7 | 18.4 | 9.6 | 3.2 | 9.29 | 31.1% | 12.8% |
| STALE | 3,090 | 10.9 | 6.1 | 15.7 | 14.7 | 18.9 | 18.1 | 15.6 | 16.45 | 52.5% | 33.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,260 | 15.2 | 10.4 | 22.0 | 16.0 | 19.8 | 12.0 | 4.7 | 10.67 | 36.4% | 16.7% |
| STALE | 2,768 | 10.9 | 8.3 | 17.8 | 13.2 | 21.1 | 15.8 | 12.8 | 14.82 | 49.8% | 28.6% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 10,987 | 0 | 5129 | 5858 | 31.2 | 216.0 | 1400.4 |
| ge_15pp | 4,770 | 0 | 1770 | 3000 | 39.7 | 515.8 | 1380.4 |
| ge_25pp | 2,616 | 0 | 783 | 1833 | 54.3 | 637.8 | 1380.4 |
| lt_10pp | 4,582 | 0 | 2545 | 2037 | 28.5 | 54.8 | 1201.9 |

Current slate `SL-20261003T115226Z-85fe40d9`: 74 priced rows, quote age at build {'median': 26.3, 'max': 72.4}, freshness {'AGING': 61, 'STALE': 13}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 137 | 21.2 | 10.9 | 21.9 | 21.2 | 20.4 | 4.4 | 0.0 | 7.89 | 24.8% | 4.4% |
| MARKETS_AGREE | 8 | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.96 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 12 | 0.0 | 0.0 | 8.3 | 50.0 | 41.7 | 0.0 | 0.0 | 14.32 | 41.7% | 0.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 4,959 | 158 (3.2%) | 7.6% | 0.0% | {"EXTERNAL_STALE": 137, "AGREES_WITH_KALSHI": 12, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 2,205 | 39 (1.8%) | 12.8% | 0.0% | {"EXTERNAL_STALE": 34, "AGREES_WITH_KALSHI": 5} |
| fair_v1_ge_25pp | 1,279 | 6 (0.5%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 6} |
| fair_v1_ge_25pp_pregame_clean | 498 | 6 (1.2%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 6} |
| fair_v1_lt_10pp | 2,006 | 84 (4.2%) | 1.2% | 0.0% | {"EXTERNAL_STALE": 74, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1, "AGREES_WITH_KALSHI": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 976 | 12.1 | 7.2 | 18.6 | 15.5 | 20.0 | 16.3 | 10.4 | 13.71 | 46.7% | 26.7% |
| 4-10x | 663 | 12.1 | 8.9 | 18.4 | 15.1 | 17.9 | 16.3 | 11.3 | 13.67 | 45.6% | 27.6% |
| <2x | 2,738 | 14.9 | 9.3 | 19.2 | 14.9 | 18.1 | 12.9 | 10.7 | 12.08 | 41.7% | 23.6% |
| >=10x | 582 | 10.7 | 5.7 | 15.8 | 15.5 | 19.8 | 20.3 | 12.4 | 16.17 | 52.4% | 32.6% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 1,334 | 14.5 | 8.8 | 20.5 | 15.3 | 17.2 | 11.9 | 11.8 | 11.95 | 40.9% | 23.7% |
| 300-1000 | 1,209 | 13.0 | 7.4 | 16.7 | 15.9 | 20.0 | 16.5 | 10.5 | 14.12 | 47.0% | 27.0% |
| <300 | 1,162 | 8.5 | 5.8 | 15.2 | 14.2 | 21.3 | 21.4 | 13.4 | 18.18 | 56.2% | 34.8% |
| >=3000 | 1,254 | 17.5 | 11.2 | 21.4 | 14.9 | 16.4 | 10.4 | 8.1 | 9.98 | 34.9% | 18.5% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 194 | 0.5154 | 0.3828 | 0.4175 | +0.098 | -0.035 | 0.0123 ± 0.0105 |
| ratio 4-10x | 140 | 0.5855 | 0.4495 | 0.4857 | +0.100 | -0.036 | 0.0121 ± 0.0125 |
| ratio <2x | 394 | 0.5331 | 0.4141 | 0.4569 | +0.076 | -0.043 | 0.0121 ± 0.0069 |
| ratio >=10x | 136 | 0.5529 | 0.3918 | 0.4559 | +0.097 | -0.064 | 0.0197 ± 0.0156 |
| thinner_sample 1000-3000 | 229 | 0.5374 | 0.4174 | 0.4541 | +0.083 | -0.037 | 0.0088 ± 0.0092 |
| thinner_sample 300-1000 | 248 | 0.5567 | 0.4279 | 0.4637 | +0.093 | -0.036 | 0.0076 ± 0.0092 |
| thinner_sample <300 | 272 | 0.5392 | 0.3807 | 0.4485 | +0.091 | -0.068 | 0.0212 ± 0.0104 |
| thinner_sample >=3000 | 115 | 0.5168 | 0.4208 | 0.4348 | +0.082 | -0.014 | 0.0162 ± 0.0102 |
| data_status ADEQUATE | 245 | 0.5238 | 0.4157 | 0.4449 | +0.079 | -0.029 | 0.0081 ± 0.0079 |
| data_status LIMITED | 191 | 0.5583 | 0.4362 | 0.4974 | +0.061 | -0.061 | 0.0024 ± 0.0107 |
| data_status POOR | 428 | 0.5426 | 0.3936 | 0.4369 | +0.106 | -0.043 | 0.0213 ± 0.0078 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 144 | 0.1771 | 0.1778 | -0.0006 ± 0.0012 | 0.5272 | 0.529 | 0.4947 | 0.4801 | 0.4931 | -0.094 ± 0.0383 | -0.01 (3) |
| 3-5 | 89 | 0.1739 | 0.1717 | +0.0022 ± 0.0036 | 0.5286 | 0.5187 | 0.5203 | 0.4793 | 0.4719 | -0.102 ± 0.0469 | 0.02 (1) |
| 5-10 | 184 | 0.2019 | 0.2042 | -0.0023 ± 0.005 | 0.5895 | 0.5946 | 0.5157 | 0.4412 | 0.4891 | -0.053 ± 0.0337 | -0.0167 (3) |
| 10-15 | 146 | 0.2154 | 0.2091 | +0.0063 ± 0.0095 | 0.6141 | 0.6002 | 0.5246 | 0.4005 | 0.4384 | -0.071 ± 0.0373 | -0.0633 (3) |
| 15-25 | 185 | 0.2118 | 0.208 | +0.0038 ± 0.0131 | 0.611 | 0.5963 | 0.5617 | 0.3656 | 0.4541 | -0.027 ± 0.0326 | -0.02 (4) |
| 25-40 | 90 | 0.2352 | 0.181 | +0.0542 ± 0.0277 | 0.6592 | 0.5337 | 0.6174 | 0.3041 | 0.3667 | -0.077 ± 0.0423 | -0.01 (1) |
| 40+ | 26 | 0.3509 | 0.1453 | +0.2057 ± 0.0675 | 0.9495 | 0.453 | 0.7195 | 0.2762 | 0.2692 | -0.176 ± 0.0753 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 436 | 0.1663 | 0.1672 | -0.0010 ± 0.0007 | 0.4989 | 0.5013 | 0.5063 | 0.4915 | 0.5275 | -0.027 ± 0.0206 | -0.0188 (8) |
| 3-5 | 269 | 0.1752 | 0.1741 | +0.0011 ± 0.0021 | 0.5313 | 0.522 | 0.4973 | 0.4571 | 0.4647 | -0.052 ± 0.0262 | 0.02 (1) |
| 5-10 | 625 | 0.1848 | 0.1827 | +0.0021 ± 0.0025 | 0.5497 | 0.5413 | 0.473 | 0.3993 | 0.424 | -0.034 ± 0.0172 | -0.0129 (7) |
| 10-15 | 509 | 0.1952 | 0.1778 | +0.0174 ± 0.0046 | 0.5722 | 0.5201 | 0.4785 | 0.3544 | 0.3458 | -0.071 ± 0.0185 | -0.0633 (3) |
| 15-25 | 683 | 0.1913 | 0.1564 | +0.0349 ± 0.006 | 0.5701 | 0.465 | 0.4798 | 0.2823 | 0.2899 | -0.051 ± 0.0149 | -0.017 (10) |
| 25-40 | 617 | 0.213 | 0.0962 | +0.1168 ± 0.0078 | 0.6188 | 0.3142 | 0.5046 | 0.1901 | 0.1637 | -0.074 ± 0.0122 | -0.01 (1) |
| 40+ | 454 | 0.3713 | 0.0357 | +0.3356 ± 0.0096 | 0.9681 | 0.152 | 0.6178 | 0.1045 | 0.0441 | -0.092 ± 0.0083 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 87 | 0.1797 | 0.1813 | -0.0016 ± 0.0016 | 0.5329 | 0.5352 | 0.5301 | 0.5155 | 0.5747 | -0.033 ± 0.0444 | -0.01 (1) |
| 3-5 | 67 | 0.2138 | 0.2119 | +0.0019 ± 0.0045 | 0.609 | 0.6116 | 0.4989 | 0.4598 | 0.4478 | -0.085 ± 0.0591 | 0.02 (1) |
| 5-10 | 171 | 0.1846 | 0.1793 | +0.0053 ± 0.005 | 0.551 | 0.5362 | 0.5729 | 0.497 | 0.4912 | -0.111 ± 0.0328 | -0.01 (4) |
| 10-15 | 154 | 0.2223 | 0.2086 | +0.0137 ± 0.0094 | 0.6335 | 0.6031 | 0.5771 | 0.4526 | 0.4675 | -0.085 ± 0.0378 | -0.0667 (3) |
| 15-25 | 205 | 0.2216 | 0.1946 | +0.0271 ± 0.0122 | 0.6283 | 0.5638 | 0.5806 | 0.3837 | 0.4195 | -0.088 ± 0.0314 | -0.0167 (3) |
| 25-40 | 126 | 0.253 | 0.1958 | +0.0573 ± 0.0243 | 0.7065 | 0.5672 | 0.6571 | 0.3465 | 0.4048 | -0.089 ± 0.0404 | -0.025 (2) |
| 40+ | 54 | 0.3802 | 0.1959 | +0.1843 ± 0.0606 | 1.0546 | 0.5767 | 0.7524 | 0.2608 | 0.3333 | -0.055 ± 0.0597 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 345 | 0.1609 | 0.1628 | -0.0019 ± 0.0007 | 0.4832 | 0.4883 | 0.554 | 0.5394 | 0.5913 | -0.000 ± 0.0219 | -0.0217 (6) |
| 3-5 | 217 | 0.1788 | 0.1757 | +0.0031 ± 0.0023 | 0.5281 | 0.5264 | 0.5482 | 0.5089 | 0.4885 | -0.069 ± 0.0285 | 0.02 (1) |
| 5-10 | 563 | 0.1767 | 0.1741 | +0.0026 ± 0.0027 | 0.5293 | 0.5171 | 0.5193 | 0.4439 | 0.4618 | -0.040 ± 0.0177 | -0.01 (5) |
| 10-15 | 523 | 0.1894 | 0.1741 | +0.0153 ± 0.0046 | 0.5626 | 0.5147 | 0.515 | 0.3909 | 0.3996 | -0.050 ± 0.0184 | -0.0575 (4) |
| 15-25 | 703 | 0.2064 | 0.1567 | +0.0497 ± 0.0059 | 0.6013 | 0.4696 | 0.5112 | 0.3153 | 0.2916 | -0.091 ± 0.0148 | -0.0143 (7) |
| 25-40 | 671 | 0.2225 | 0.1184 | +0.1041 ± 0.0084 | 0.6469 | 0.3664 | 0.5451 | 0.2295 | 0.2235 | -0.062 ± 0.0135 | -0.015 (6) |
| 40+ | 571 | 0.4034 | 0.0614 | +0.3420 ± 0.012 | 1.0596 | 0.2218 | 0.6624 | 0.1246 | 0.0893 | -0.069 ± 0.01 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 135 | 0.1793 | 0.1811 | -0.0018 ± 0.0013 | 0.5292 | 0.534 | 0.5201 | 0.5055 | 0.5481 | -0.043 ± 0.037 | -0.01 (5) |
| 3-5 | 100 | 0.1705 | 0.168 | +0.0026 ± 0.0033 | 0.5146 | 0.5084 | 0.5 | 0.4606 | 0.45 | -0.113 ± 0.0434 | -- (0) |
| 5-10 | 176 | 0.207 | 0.2056 | +0.0014 ± 0.0051 | 0.6056 | 0.5959 | 0.5061 | 0.4336 | 0.4602 | -0.068 ± 0.0345 | -0.01 (3) |
| 10-15 | 153 | 0.2111 | 0.2077 | +0.0034 ± 0.0092 | 0.6083 | 0.5972 | 0.5511 | 0.4273 | 0.4837 | -0.065 ± 0.0371 | -0.044 (5) |
| 15-25 | 181 | 0.2101 | 0.2003 | +0.0099 ± 0.0128 | 0.6115 | 0.5803 | 0.5757 | 0.3828 | 0.453 | -0.046 ± 0.0319 | -0.03 (1) |
| 25-40 | 98 | 0.234 | 0.1909 | +0.0431 ± 0.0273 | 0.6598 | 0.5596 | 0.6078 | 0.2947 | 0.3776 | -0.064 ± 0.0409 | 0.0 (1) |
| 40+ | 21 | 0.3707 | 0.1604 | +0.2102 ± 0.0791 | 0.9917 | 0.4892 | 0.7365 | 0.2879 | 0.2857 | -0.191 ± 0.0908 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 407 | 0.1701 | 0.1704 | -0.0003 ± 0.0007 | 0.5091 | 0.5102 | 0.5098 | 0.4951 | 0.516 | -0.039 ± 0.0206 | -0.0162 (13) |
| 3-5 | 298 | 0.1787 | 0.1737 | +0.0050 ± 0.0019 | 0.533 | 0.5193 | 0.487 | 0.4477 | 0.4094 | -0.098 ± 0.0244 | -0.01 (2) |
| 5-10 | 615 | 0.1935 | 0.1869 | +0.0067 ± 0.0026 | 0.5716 | 0.5455 | 0.4683 | 0.3945 | 0.3886 | -0.061 ± 0.0175 | -0.01 (3) |
| 10-15 | 526 | 0.1902 | 0.1736 | +0.0166 ± 0.0045 | 0.5625 | 0.5138 | 0.4884 | 0.3646 | 0.3612 | -0.068 ± 0.0182 | -0.03 (9) |
| 15-25 | 722 | 0.1835 | 0.1481 | +0.0354 ± 0.0057 | 0.5545 | 0.4463 | 0.4899 | 0.2912 | 0.3019 | -0.046 ± 0.014 | -0.03 (2) |
| 25-40 | 596 | 0.2141 | 0.0968 | +0.1173 ± 0.008 | 0.6209 | 0.3138 | 0.4978 | 0.1804 | 0.156 | -0.075 ± 0.0122 | 0.0 (1) |
| 40+ | 429 | 0.388 | 0.0354 | +0.3525 ± 0.0099 | 1.0135 | 0.153 | 0.6237 | 0.1048 | 0.035 | -0.101 ± 0.0084 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 423 | 0.205 | 0.2051 | -0.0001 ± 0.0007 | 0.5926 | 0.5931 | 0.5006 | 0.4859 | 0.4894 | -0.040 ± 0.0221 | -0.0226 (46) |
| 3-5 | 303 | 0.1944 | 0.193 | +0.0014 ± 0.002 | 0.5704 | 0.5635 | 0.4621 | 0.4223 | 0.429 | -0.043 ± 0.0251 | -0.0059 (32) |
| 5-10 | 644 | 0.1888 | 0.1838 | +0.0050 ± 0.0025 | 0.5612 | 0.5475 | 0.4602 | 0.3868 | 0.3913 | -0.041 ± 0.0169 | -0.005 (72) |
| 10-15 | 428 | 0.2037 | 0.1914 | +0.0124 ± 0.0053 | 0.5968 | 0.5614 | 0.4603 | 0.3366 | 0.3481 | -0.039 ± 0.021 | 0.0016 (63) |
| 15-25 | 572 | 0.2332 | 0.2082 | +0.0250 ± 0.0074 | 0.6593 | 0.6025 | 0.5298 | 0.3368 | 0.3689 | -0.031 ± 0.0191 | -0.0216 (58) |
| 25-40 | 274 | 0.2689 | 0.1707 | +0.0982 ± 0.0156 | 0.7429 | 0.5118 | 0.577 | 0.2657 | 0.2628 | -0.068 ± 0.0246 | -0.0216 (25) |
| 40+ | 94 | 0.4254 | 0.1611 | +0.2643 ± 0.0443 | 1.1952 | 0.4956 | 0.7368 | 0.2289 | 0.2447 | -0.060 ± 0.0429 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 779 | 0.1944 | 0.1939 | +0.0005 ± 0.0005 | 0.5672 | 0.5658 | 0.4952 | 0.4807 | 0.4698 | -0.052 ± 0.0158 | -0.0155 (82) |
| 3-5 | 546 | 0.1976 | 0.1956 | +0.0019 ± 0.0015 | 0.5751 | 0.5674 | 0.4674 | 0.4276 | 0.4249 | -0.047 ± 0.0189 | -0.018 (54) |
| 5-10 | 1173 | 0.1875 | 0.1806 | +0.0068 ± 0.0019 | 0.558 | 0.5378 | 0.4455 | 0.3715 | 0.3666 | -0.046 ± 0.0125 | -0.0089 (122) |
| 10-15 | 862 | 0.1981 | 0.1838 | +0.0143 ± 0.0037 | 0.5826 | 0.5416 | 0.4512 | 0.3276 | 0.3318 | -0.041 ± 0.0145 | -0.0053 (99) |
| 15-25 | 1197 | 0.221 | 0.1861 | +0.0349 ± 0.0049 | 0.6372 | 0.5467 | 0.5038 | 0.3083 | 0.3166 | -0.043 ± 0.0125 | -0.0255 (106) |
| 25-40 | 823 | 0.2451 | 0.1287 | +0.1163 ± 0.0079 | 0.6916 | 0.4022 | 0.5289 | 0.2137 | 0.1883 | -0.071 ± 0.0123 | -0.0206 (47) |
| 40+ | 486 | 0.3897 | 0.0797 | +0.3101 ± 0.014 | 1.0652 | 0.2671 | 0.6537 | 0.1373 | 0.107 | -0.074 ± 0.013 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 864 | 1.114 ± 0.097 | 1.222 | 0.1716 | 0.1838 | 0.2072 | 0.1939 |
| gen2 | 864 | 0.948 ± 0.086 | 1.154 | 0.188 | 0.1829 | 0.2241 | 0.1943 |
| gen1_elo | 864 | 1.087 ± 0.094 | 1.208 | 0.1768 | 0.1841 | 0.2069 | 0.1939 |
| gen1_sr | 864 | 1.142 ± 0.111 | 1.219 | 0.1443 | 0.1853 | 0.2202 | 0.1938 |
| gen1_ledger | 2738 | 0.885 ± 0.051 | 1.058 | 0.1626 | 0.1995 | 0.2197 | 0.1923 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 4,770)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,591 | 33.4% |
| STALE_QUOTE | market_freshness | 1,403 | 29.4% |
| POOR_DATA | data | 379 | 8.0% |
| BOOK_QUALITY | execution | 312 | 6.5% |
| LIMITED_DATA | data | 298 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 281 | 5.9% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 243 | 5.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 167 | 3.5% |
| IDENTITY_AMBIGUOUS | mapping | 93 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 3 | 0.1% |

Cause class: coverage 33.4%, market_freshness 29.4%, data 14.2%, market_freshness/coverage 9.4%, execution 6.5%, model_calibration_or_unknown 5.1%, mapping 1.9%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 94.3%, LOW_DATA_QUALITY 64.0%, STALE_KALSHI_QUOTE 62.9%, STALE_PLAYER_DATA 54.0%, THIN_PLAYER_HISTORY 51.7%, MODEL_INTERNAL_DISAGREEMENT 32.8%, ASYMMETRIC_SAMPLE_SIZE 28.0%, WIDE_SPREAD 14.6%, MODEL_HIGH_UNCERTAINTY 13.6%, PLAYER_IDENTITY_RISK 10.8%, LEVEL_TRANSFER_RISK 8.4%, EVENT_MAPPING_RISK 6.8%, LOW_DISPLAYED_LIQUIDITY 4.9%, MODEL_CALIBRATION_OUTLIER 2.2%, UNKNOWN 0.8%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 35.9%, POST_SETTLEMENT_OBSERVATION 33.4%, POSSIBLE_IN_PLAY_QUOTE 6.7%, CONFIRMED_IN_PLAY_QUOTE 1.2%

### >= ge_25 pp (N = 2,616)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,231 | 47.1% |
| STALE_QUOTE | market_freshness | 622 | 23.8% |
| POOR_DATA | data | 165 | 6.3% |
| BOOK_QUALITY | execution | 151 | 5.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 142 | 5.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 100 | 3.8% |
| LIMITED_DATA | data | 81 | 3.1% |
| IDENTITY_AMBIGUOUS | mapping | 67 | 2.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 57 | 2.2% |

Cause class: coverage 47.1%, market_freshness 23.8%, data 9.4%, market_freshness/coverage 9.2%, execution 5.8%, mapping 2.6%, model_calibration_or_unknown 2.2%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 96.7%, STALE_KALSHI_QUOTE 70.1%, LOW_DATA_QUALITY 67.8%, THIN_PLAYER_HISTORY 54.2%, STALE_PLAYER_DATA 51.8%, MODEL_INTERNAL_DISAGREEMENT 33.6%, ASYMMETRIC_SAMPLE_SIZE 30.3%, MODEL_HIGH_UNCERTAINTY 14.8%, PLAYER_IDENTITY_RISK 13.4%, WIDE_SPREAD 13.2%, EVENT_MAPPING_RISK 8.2%, LEVEL_TRANSFER_RISK 7.8%, LOW_DISPLAYED_LIQUIDITY 5.4%, MODEL_CALIBRATION_OUTLIER 3.2%, UNKNOWN 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 49.9%, POST_SETTLEMENT_OBSERVATION 47.1%, POSSIBLE_IN_PLAY_QUOTE 6.4%, CONFIRMED_IN_PLAY_QUOTE 1.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 2234, "IDENTITY_AMBIGUOUS": 382}; ticker orientation: {"VERIFIED": 2616}.

Checks: discipline:AMBIGUOUS 183, discipline:PASS 2433, identity_confidence:AMBIGUOUS 350, identity_confidence:PASS 2266, level_mapping:NA 195, level_mapping:PASS 2421, market_pair:AMBIGUOUS 62, market_pair:NA 75, market_pair:PASS 2479, model_complement:NA 46, model_complement:PASS 2570, namesake:PASS 2616, physical_match_id:NA 1337, physical_match_id:PASS 1279, player_ids:PASS 2616, same_pair_other_event:PASS 2616, ticker_orientation:PASS 2616

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 313 | 3.8% | 4.0% | 0.5% | {"market_freshness": 12} | 6.14 | 0.1791 / 0.1823 (49) | 39.3% | 0.0% | 0.6% | 3.5% |
| CHALLENGER | 1,665 | 18.9% | 8.4% | 12.0% | {"coverage": 168, "market_freshness": 74, "market_freshness/coverage": 39, "data": 17, "model_calibration_or_unknown": 14, "execution": 3} | 7.86 | 0.2258 / 0.208 (538) | 52.4% | 4.0% | 0.7% | 22.5% |
| DOUBLES | 381 | 48.0% | 48.0% | 7.0% | {"market_freshness": 106, "execution": 32, "mapping": 27, "market_freshness/coverage": 12, "coverage": 6} | 24.02 | 0.3237 / 0.228 (160) | 61.2% | 0.0% | 100.0% | 9.7% |
| ITF_MEN | 3,649 | 24.9% | 13.6% | 34.7% | {"coverage": 502, "market_freshness": 163, "data": 89, "execution": 73, "market_freshness/coverage": 70, "mapping": 10, "model_calibration_or_unknown": 1} | 9.71 | 0.2129 / 0.1872 (1309) | 55.4% | 49.1% | 5.3% | 32.3% |
| ITF_WOMEN | 3,611 | 28.9% | 17.2% | 39.8% | {"coverage": 542, "market_freshness": 220, "data": 121, "market_freshness/coverage": 81, "execution": 34, "mapping": 28, "model_calibration_or_unknown": 16} | 12.33 | 0.2063 / 0.1863 (1156) | 58.1% | 53.9% | 6.2% | 32.7% |
| OTHER | 149 | 8.1% | 7.3% | 0.5% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 798 | 9.4% | 8.1% | 2.9% | {"market_freshness": 34, "model_calibration_or_unknown": 12, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.66 | 0.2006 / 0.1964 (129) | 40.5% | 2.6% | 1.5% | 3.8% |
| WTA125 | 421 | 16.4% | 9.1% | 2.6% | {"market_freshness/coverage": 30, "model_calibration_or_unknown": 12, "market_freshness": 11, "data": 8, "coverage": 8} | 10.39 | 0.2261 / 0.2035 (219) | 34.4% | 9.0% | 0.5% | 19.2% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 3 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 4 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 5 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 6 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
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
| 18 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 19 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 20 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 21 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 22 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 22 min (AGING); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 23 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 24 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 25 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 230 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 26 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.2h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 141 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 27 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 28 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 29 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 66 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 30 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 31 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 32 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 33 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 34 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.9h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 671 min (STALE); no external reference |
| 36 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 407 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 37 | `KXWTAMATCH-26OCT01YASCHW-CHW` | WTA | fair_v1 | 73% / 2% | +70 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 51 min (STALE); no external reference |
| 38 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 39 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 40 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 41 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |
| 42 | `KXITFWMATCH-26SEP30KOKUEM-KOK` | ITF_WOMEN | fair_v1 | 79% / 10% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 776 min (STALE); data LIMITED (grade C, thinner serve sample 824.0, ratio 2.35); no external reference |
| 43 | `KXITFMATCH-26SEP20WILRAH-RAH` | ITF_MEN | gen1_ledger | 72% / 4% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade B, thinner serve sample 2782.0, ratio 1.84); no external reference |
| 44 | `KXITFMATCH-26SEP26NAGTHO-NAG` | ITF_MEN | gen1_ledger | 76% / 7% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 89 min (STALE); data LIMITED (grade C, thinner serve sample 1323.0, ratio 4.45); no external reference |
| 45 | `KXITFWMATCH-26SEP26PERPRE-PER` | ITF_WOMEN | gen1_ledger | 78% / 10% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 102 min (STALE); data POOR (grade D, thinner serve sample 1020.0, ratio 2.77); no external reference |
| 46 | `KXITFMATCH-26SEP22YILAGA-AGA` | ITF_MEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 203 min (STALE); data LIMITED (grade B, thinner serve sample 2786.0, ratio 2.08); no external reference |
| 47 | `KXITFMATCH-26SEP30DIMURA-URA` | ITF_MEN | fair_v1 | 71% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.5h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 220 min (STALE); data POOR (grade F, thinner serve sample 174.0, ratio 2.63); no external reference |
| 48 | `KXITFWMATCH-26OCT01TANVED-TAN` | ITF_WOMEN | fair_v1 | 76% / 8% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 8.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 492 min (STALE); no external reference |
| 49 | `KXITFWMATCH-26SEP20LLIBON-BON` | ITF_WOMEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 69 min (STALE); data POOR (grade D, thinner serve sample 1210.0, ratio 3.0); no external reference |
| 50 | `KXATPCHALLENGERDOUBLES-26SEP17ARESTEBLASCH-BLASCH` | DOUBLES | gen1_ledger | 95% / 28% | +67 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 79 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9668, "by_level_share_of_ge_25pp": {"ATP": 0.0046, "CHALLENGER": 0.1204, "DOUBLES": 0.07, "ITF_MEN": 0.3471, "ITF_WOMEN": 0.3983, "OTHER": 0.0046, "WTA": 0.0287, "WTA125": 0.0264}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.7007, "share_primary_cause_market_settled_or_in_play": 0.5631, "share_primary_cause_stale_quote_only": 0.2378}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 2616, "identity_ambiguous_share": 0.146, "ticker_orientation": {"VERIFIED": 2616}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 1279, "with_external": 6, "coverage": 0.0047, "external_status": {"EXTERNAL_STALE": 6}, "triangulation": {"INSUFFICIENT_INPUTS": 6}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 498, "with_external": 6, "coverage": 0.012, "external_status": {"EXTERNAL_STALE": 6}, "triangulation": {"INSUFFICIENT_INPUTS": 6}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 824.0, "median_sample_ratio": 2.27, "median_min_matches": 27.0, "median_max_days_since_last": 172.0, "share_severe_asymmetry": 0.164, "data_status": {"POOR": 1210, "LIMITED": 891, "ADEQUATE": 515}, "comparison_lt_10pp": {"median_thinner_serve_points": 1980.5, "median_sample_ratio": 1.71, "median_min_matches": 80.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 194, "model_minus_observed": 0.0979, "kalshi_minus_observed": -0.0347, "brier_diff_model_minus_kalshi": 0.0123}, "4-10x": {"n": 140, "model_minus_observed": 0.0998, "kalshi_minus_observed": -0.0362, "brier_diff_model_minus_kalshi": 0.0121}, "<2x": {"n": 394, "model_minus_observed": 0.0763, "kalshi_minus_observed": -0.0428, "brier_diff_model_minus_kalshi": 0.0121}, ">=10x": {"n": 136, "model_minus_observed": 0.097, "kalshi_minus_observed": -0.0641, "brier_diff_model_minus_kalshi": 0.0197}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 864, "model": {"intercept": -0.65, "slope": 0.948, "slope_se": 0.086}, "kalshi_mid_same_rows": {"intercept": 0.182, "slope": 1.154, "slope_se": 0.095}, "mean_extremity_model": 0.188, "mean_extremity_kalshi": 0.1829, "model_brier": 0.2241, "kalshi_brier": 0.1943, "brier_diff_model_minus_kalshi": 0.0298, "brier_diff_se": 0.0064, "model_logloss": 0.6409, "kalshi_logloss": 0.5675}, "fair_v1": {"n": 864, "model": {"intercept": -0.444, "slope": 1.114, "slope_se": 0.097}, "kalshi_mid_same_rows": {"intercept": 0.303, "slope": 1.222, "slope_se": 0.098}, "mean_extremity_model": 0.1716, "mean_extremity_kalshi": 0.1838, "model_brier": 0.2072, "kalshi_brier": 0.1939, "brier_diff_model_minus_kalshi": 0.0134, "brier_diff_se": 0.0051, "model_logloss": 0.5997, "kalshi_logloss": 0.5665}, "gen1_elo": {"n": 864, "model": {"intercept": -0.428, "slope": 1.087, "slope_se": 0.094}, "kalshi_mid_same_rows": {"intercept": 0.302, "slope": 1.208, "slope_se": 0.097}, "mean_extremity_model": 0.1768, "mean_extremity_kalshi": 0.1841, "model_brier": 0.2069, "kalshi_brier": 0.1939, "brier_diff_model_minus_kalshi": 0.013, "brier_diff_se": 0.005, "model_logloss": 0.6004, "kalshi_logloss": 0.5664}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2579, "share_ge_15": 0.4446, "median_abs_gap": 13.01, "n": 4959}, "gen1_elo": {"share_ge_25": 0.2509, "share_ge_15": 0.4325, "median_abs_gap": 12.5, "n": 4959}, "gen1_sr": {"share_ge_25": 0.3089, "share_ge_15": 0.5332, "median_abs_gap": 16.35, "n": 4959}, "gen2": {"share_ge_25": 0.3087, "share_ge_15": 0.5102, "median_abs_gap": 15.48, "n": 4959}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1398, "share_ge_15": 0.3307, "median_abs_gap": 9.99, "n": 3562}, "gen1_elo": {"share_ge_25": 0.1404, "share_ge_15": 0.3125, "median_abs_gap": 9.51, "n": 3562}, "gen1_sr": {"share_ge_25": 0.1957, "share_ge_15": 0.4346, "median_abs_gap": 12.7, "n": 3562}, "gen2": {"share_ge_25": 0.2092, "share_ge_15": 0.427, "median_abs_gap": 12.83, "n": 3562}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 6.14, "share_ge_25_all": 0.0383, "share_ge_25_pregame_clean": 0.0397}, "WTA": {"median_abs_gap_pregame_clean": 8.66, "share_ge_25_all": 0.094, "share_ge_25_pregame_clean": 0.0807}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2231, "share_within_10pp_all": 0.417, "share_within_10pp_pregame_clean": 0.4981, "corr_model_vs_mid_pregame_clean": 0.8275}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 144, "model_brier": 0.1771, "kalshi_brier": 0.1778, "brier_diff_model_minus_kalshi": -0.0006}, "10-15": {"n_settled": 146, "model_brier": 0.2154, "kalshi_brier": 0.2091, "brier_diff_model_minus_kalshi": 0.0063}, "15-25": {"n_settled": 185, "model_brier": 0.2118, "kalshi_brier": 0.208, "brier_diff_model_minus_kalshi": 0.0038}, "25-40": {"n_settled": 90, "model_brier": 0.2352, "kalshi_brier": 0.181, "brier_diff_model_minus_kalshi": 0.0542}, "3-5": {"n_settled": 89, "model_brier": 0.1739, "kalshi_brier": 0.1717, "brier_diff_model_minus_kalshi": 0.0022}, "40+": {"n_settled": 26, "model_brier": 0.3509, "kalshi_brier": 0.1453, "brier_diff_model_minus_kalshi": 0.2057}, "5-10": {"n_settled": 184, "model_brier": 0.2019, "kalshi_brier": 0.2042, "brier_diff_model_minus_kalshi": -0.0023}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.565, "slope": 0.885, "slope_se": 0.051}, "kalshi_slope": {"intercept": 0.083, "slope": 1.058, "slope_se": 0.053}, "n": 2738}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 160, "model_brier": 0.3237, "kalshi_brier": 0.228, "brier_diff_model_minus_kalshi": 0.0957, "brier_diff_se": 0.026, "corr_model_outcome": -0.0918, "corr_kalshi_outcome": 0.3335}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
