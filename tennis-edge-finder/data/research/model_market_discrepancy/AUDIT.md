# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-04T12:55Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 12,084): 0-3 13.2%, 3-5 9.1%, 5-10 19.1%, 10-15 15.0%, 15-25 19.5%, 25-40 14.6%, 40+ 9.5%; median gap 12.6 pp.
* **Where the extremes live**: 96.7% of >=25 pp gaps are off the ATP/WTA main tour (ITF 74.3%, Challenger 13.1%, doubles 6.4%). Main tour: ATP 5.9% and WTA 9.4% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 2,903): MARKET_ALREADY_SETTLED_WHEN_PRICED 46.6%, STALE_QUOTE 24.9%, POOR_DATA 5.9%, BOOK_QUALITY 5.8%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IN_PLAY_QUOTE 3.6%, LIMITED_DATA 3.0%, IDENTITY_AMBIGUOUS 2.6%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%. By class: coverage 46.6%, market_freshness 24.9%, market_freshness/coverage 9.1%, data 8.8%, execution 5.8%, mapping 2.6%, model_calibration_or_unknown 2.2%.
* **Stale / settled / in-play**: 71.0% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 55.6% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 2,903 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 14.8% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 0.5%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 7.3% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 824.0 points vs 1948.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.104, Gen-2 0.916, Gen-1 ledger 0.892 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 101 model 0.2365 vs Kalshi 0.1889; n 28 model 0.3342 vs Kalshi 0.1438.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 38,834 model-market comparisons (67,726 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 17,296 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-04T12:50:25.421786+00:00'], shadow board 11,371 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-04T12:50:29.155606+00:00'], Model 4 3,106 rows, 8,404 settled tickers, 1,854 tickers with an external scan.
* By model: {"gen1_ledger": 9971, "gen1_elo": 5718, "fair_v1": 5718, "gen2": 5718, "gen1_sr": 5718, "model4_fundamental": 3000, "model4_conditioned": 2991}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 12,084 | 13.2 | 9.1 | 19.1 | 15.0 | 19.5 | 14.6 | 9.5 | 12.6 | 43.5% | 24.0% |
| MW fair_v1 | 5,718 | 13.3 | 8.5 | 18.4 | 15.4 | 18.5 | 15.2 | 10.7 | 12.99 | 44.4% | 25.9% |
| MW gen1_elo | 5,718 | 13.4 | 8.8 | 19.8 | 14.8 | 18.1 | 15.1 | 10.1 | 12.48 | 43.2% | 25.1% |
| MW gen1_ledger | 6,366 | 13.2 | 9.6 | 19.8 | 14.7 | 20.4 | 14.0 | 8.3 | 12.23 | 42.7% | 22.3% |
| MW gen1_sr | 5,718 | 9.5 | 7.3 | 16.5 | 13.6 | 22.1 | 18.2 | 12.8 | 16.23 | 53.1% | 30.9% |
| MW gen2 | 5,718 | 11.2 | 6.7 | 16.6 | 14.2 | 20.2 | 17.2 | 13.9 | 15.58 | 51.3% | 31.1% |
| all families model4_conditioned | 2,991 | 18.2 | 15.9 | 28.1 | 22.4 | 11.2 | 2.3 | 1.8 | 7.45 | 15.3% | 4.2% |
| all families model4_fundamental | 3,000 | 14.4 | 10.5 | 28.9 | 21.1 | 15.6 | 6.5 | 3.0 | 9.33 | 25.0% | 9.5% |

Configurable thresholds (primary): >=5pp 77.7%, >=10pp 58.5%, >=15pp 43.5%, >=20pp 33.0%, >=25pp 24.0%, >=30pp 17.6%, >=40pp 9.5%, >=50pp 4.3%
Executable gap (model outside the book, before fees): median 10.23pp; >=10pp 50.6%, >=25pp 21.2%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 286 | 20.6 | 15.4 | 26.2 | 14.0 | 16.4 | 3.5 | 3.9 | 7.11 | 23.8% | 7.3% |
| CHALLENGER | 1,166 | 15.7 | 10.8 | 16.9 | 16.4 | 15.1 | 14.0 | 11.2 | 12.2 | 40.2% | 25.1% |
| ITF_MEN | 1,711 | 11.9 | 8.4 | 19.7 | 15.0 | 17.7 | 14.8 | 12.6 | 12.81 | 45.1% | 27.4% |
| ITF_WOMEN | 2,027 | 10.2 | 6.0 | 15.6 | 15.4 | 21.3 | 19.8 | 11.8 | 16.17 | 52.8% | 31.6% |
| WTA | 435 | 23.0 | 10.6 | 25.8 | 12.6 | 18.9 | 6.7 | 2.5 | 8.16 | 28.1% | 9.2% |
| WTA125 | 93 | 12.9 | 4.3 | 17.2 | 25.8 | 18.3 | 14.0 | 7.5 | 12.79 | 39.8% | 21.5% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 286 | 20.6 | 12.2 | 24.1 | 16.1 | 17.8 | 4.9 | 4.2 | 8.01 | 26.9% | 9.1% |
| CHALLENGER | 1,166 | 13.6 | 6.3 | 19.7 | 15.0 | 18.0 | 16.1 | 11.2 | 13.44 | 45.4% | 27.4% |
| ITF_MEN | 1,711 | 9.5 | 7.0 | 17.5 | 15.2 | 20.2 | 16.7 | 14.0 | 15.41 | 50.8% | 30.6% |
| ITF_WOMEN | 2,027 | 8.2 | 6.2 | 13.0 | 12.0 | 21.1 | 20.1 | 19.2 | 19.7 | 60.5% | 39.4% |
| WTA | 435 | 20.5 | 5.5 | 16.8 | 15.6 | 22.3 | 16.8 | 2.5 | 12.98 | 41.6% | 19.3% |
| WTA125 | 93 | 5.4 | 5.4 | 15.1 | 19.4 | 24.7 | 15.1 | 15.1 | 18.48 | 54.8% | 30.1% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 286 | 26.2 | 13.3 | 26.9 | 9.8 | 10.5 | 9.1 | 4.2 | 7.14 | 23.8% | 13.3% |
| CHALLENGER | 1,166 | 16.6 | 9.6 | 22.4 | 13.6 | 13.1 | 12.8 | 11.9 | 10.48 | 37.8% | 24.7% |
| ITF_MEN | 1,711 | 10.3 | 9.3 | 18.4 | 15.7 | 18.7 | 15.1 | 12.4 | 13.47 | 46.2% | 27.5% |
| ITF_WOMEN | 2,027 | 10.0 | 6.3 | 16.3 | 14.5 | 23.2 | 19.7 | 10.0 | 16.67 | 52.9% | 29.7% |
| WTA | 435 | 23.4 | 14.0 | 29.4 | 15.6 | 11.5 | 4.4 | 1.6 | 6.99 | 17.5% | 6.0% |
| WTA125 | 93 | 16.1 | 5.4 | 23.7 | 29.0 | 14.0 | 9.7 | 2.1 | 10.92 | 25.8% | 11.8% |

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
| ATP | 285 | 20.4 | 15.4 | 26.3 | 14.0 | 16.5 | 3.5 | 3.9 | 7.19 | 23.9% | 7.4% |
| CHALLENGER | 888 | 19.4 | 13.3 | 19.8 | 18.8 | 16.1 | 8.7 | 3.9 | 9.28 | 28.7% | 12.6% |
| ITF_MEN | 1,073 | 15.8 | 11.8 | 24.9 | 16.7 | 17.5 | 9.4 | 3.9 | 9.46 | 30.9% | 13.3% |
| ITF_WOMEN | 1,375 | 13.6 | 7.7 | 18.7 | 18.0 | 22.2 | 15.2 | 4.6 | 12.8 | 42.0% | 19.8% |
| WTA | 434 | 23.0 | 10.6 | 25.8 | 12.7 | 18.9 | 6.5 | 2.5 | 8.16 | 27.9% | 9.0% |
| WTA125 | 88 | 13.6 | 4.5 | 18.2 | 27.3 | 18.2 | 12.5 | 5.7 | 11.65 | 36.4% | 18.2% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 285 | 20.7 | 11.9 | 24.2 | 16.1 | 17.9 | 4.9 | 4.2 | 8.08 | 27.0% | 9.1% |
| CHALLENGER | 888 | 16.8 | 7.8 | 23.6 | 17.3 | 18.9 | 12.3 | 3.3 | 10.53 | 34.5% | 15.5% |
| ITF_MEN | 1,073 | 12.9 | 8.8 | 21.7 | 17.8 | 21.2 | 12.2 | 5.3 | 11.65 | 38.8% | 17.5% |
| ITF_WOMEN | 1,375 | 9.8 | 8.2 | 14.7 | 11.6 | 24.1 | 18.6 | 13.0 | 17.13 | 55.7% | 31.6% |
| WTA | 434 | 20.5 | 5.5 | 16.8 | 15.7 | 22.4 | 16.6 | 2.5 | 12.96 | 41.5% | 19.1% |
| WTA125 | 88 | 5.7 | 5.7 | 14.8 | 20.4 | 26.1 | 15.9 | 11.4 | 16.39 | 53.4% | 27.3% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 62 | 24.2 | 25.8 | 35.5 | 12.9 | 1.6 | 0.0 | 0.0 | 5.45 | 1.6% | 0.0% |
| CHALLENGER | 774 | 23.1 | 17.3 | 28.0 | 14.7 | 13.7 | 2.8 | 0.3 | 6.71 | 16.8% | 3.1% |
| DOUBLES | 345 | 5.8 | 3.8 | 10.1 | 10.4 | 21.7 | 21.2 | 27.0 | 24.1 | 69.9% | 48.1% |
| ITF_MEN | 1,480 | 17.2 | 11.1 | 22.1 | 15.3 | 20.7 | 10.0 | 3.6 | 9.92 | 34.3% | 13.6% |
| ITF_WOMEN | 1,387 | 10.6 | 9.7 | 20.8 | 16.6 | 24.7 | 15.5 | 2.1 | 12.28 | 42.2% | 17.6% |
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
| Clay | 1,289 | 15.3 | 9.1 | 19.6 | 15.1 | 15.8 | 13.1 | 12.1 | 11.77 | 41.0% | 25.2% |
| Hard | 4,012 | 12.7 | 8.6 | 18.3 | 15.0 | 19.4 | 15.7 | 10.3 | 13.37 | 45.4% | 26.0% |
| UNKNOWN | 417 | 13.9 | 5.8 | 15.3 | 19.9 | 17.8 | 17.0 | 10.3 | 13.42 | 45.1% | 27.3% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,745 | 17.1 | 10.0 | 20.8 | 15.2 | 16.8 | 11.7 | 8.4 | 10.47 | 36.9% | 20.1% |
| B | 890 | 15.8 | 10.6 | 17.0 | 18.1 | 16.5 | 10.6 | 11.5 | 11.57 | 38.5% | 22.0% |
| C | 916 | 13.0 | 8.9 | 22.3 | 13.0 | 16.3 | 15.3 | 11.2 | 12.49 | 42.8% | 26.5% |
| D | 1,011 | 11.5 | 8.4 | 17.0 | 14.3 | 20.6 | 15.6 | 12.6 | 14.44 | 48.8% | 28.2% |
| F | 1,156 | 7.6 | 4.2 | 14.1 | 16.3 | 22.4 | 23.7 | 11.7 | 18.38 | 57.8% | 35.4% |

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
| ADEQUATE | 2,191 | 16.5 | 9.5 | 19.5 | 16.1 | 16.8 | 11.8 | 9.7 | 11.07 | 38.3% | 21.5% |
| LIMITED | 1,342 | 14.4 | 10.5 | 21.6 | 14.2 | 15.8 | 13.3 | 10.3 | 11.22 | 39.3% | 23.5% |
| POOR | 2,185 | 9.5 | 6.1 | 15.4 | 15.4 | 21.7 | 19.9 | 12.0 | 16.55 | 53.6% | 31.9% |

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
| EXACT_SET_SCORE | 1,062 | 25.9 | 31.2 | 23.4 | 0.6 | 16.9 | 1.6 | 0.6 | 4.5 | 19.0% | 2.2% |
| GAME_SPREAD | 565 | 36.6 | 15.0 | 25.3 | 17.9 | 2.5 | 1.9 | 0.7 | 4.55 | 5.1% | 2.6% |
| TOTAL_GAMES | 1,364 | 4.5 | 4.5 | 33.1 | 41.3 | 10.3 | 3.1 | 3.2 | 10.72 | 16.6% | 6.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,062 | 23.9 | 15.1 | 30.1 | 8.7 | 13.5 | 7.3 | 1.4 | 6.3 | 22.2% | 8.8% |
| GAME_SPREAD | 565 | 17.5 | 10.3 | 25.5 | 23.2 | 15.9 | 5.1 | 2.5 | 9.56 | 23.5% | 7.6% |
| TOTAL_GAMES | 1,373 | 5.8 | 7.0 | 29.4 | 29.9 | 17.0 | 6.3 | 4.4 | 10.91 | 27.8% | 10.8% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5,718 | 44.4% | 25.9% | 12.99 | 33.4% | 14.5% | 10.11 |
| gen1_elo | 5,718 | 43.2% | 25.1% | 12.48 | 31.8% | 14.4% | 9.51 |
| gen1_sr | 5,718 | 53.1% | 30.9% | 16.23 | 43.4% | 19.9% | 12.95 |
| gen2 | 5,718 | 51.3% | 31.1% | 15.58 | 43.2% | 21.6% | 12.8 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 2,085 | 17.5 | 12.0 | 23.0 | 15.8 | 18.3 | 10.1 | 3.3 | 9.48 | 31.8% | 13.4% |
| STALE | 3,633 | 11.0 | 6.4 | 15.8 | 15.1 | 18.6 | 18.1 | 15.0 | 16.0 | 51.7% | 33.1% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,360 | 15.1 | 10.5 | 21.9 | 15.9 | 20.0 | 12.1 | 4.6 | 10.71 | 36.7% | 16.7% |
| STALE | 3,006 | 11.0 | 8.7 | 17.5 | 13.4 | 20.9 | 16.1 | 12.5 | 14.77 | 49.4% | 28.6% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 12,084 | 0 | 5445 | 6639 | 31.7 | 206.8 | 1400.4 |
| ge_15pp | 5,257 | 0 | 1894 | 3363 | 39.8 | 480.5 | 1380.4 |
| ge_25pp | 2,903 | 0 | 841 | 2062 | 53.8 | 609.5 | 1380.4 |
| lt_10pp | 5,011 | 0 | 2687 | 2324 | 29.1 | 55.8 | 1201.9 |

Current slate `SL-20261004T125507Z-72725a6a`: 245 priced rows, quote age at build {'median': 35.9, 'max': 36.0}, freshness {'STALE': 144, 'AGING': 101}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 156 | 22.4 | 10.3 | 21.1 | 21.1 | 19.9 | 4.5 | 0.6 | 7.76 | 25.0% | 5.1% |
| MARKETS_AGREE | 8 | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.96 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 13 | 0.0 | 0.0 | 7.7 | 53.9 | 38.5 | 0.0 | 0.0 | 13.64 | 38.5% | 0.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 5,718 | 178 (3.1%) | 7.3% | 0.0% | {"EXTERNAL_STALE": 156, "AGREES_WITH_KALSHI": 13, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 2,539 | 44 (1.7%) | 11.4% | 0.0% | {"EXTERNAL_STALE": 39, "AGREES_WITH_KALSHI": 5} |
| fair_v1_ge_25pp | 1,483 | 8 (0.5%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 8} |
| fair_v1_ge_25pp_pregame_clean | 603 | 8 (1.3%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 8} |
| fair_v1_lt_10pp | 2,300 | 94 (4.1%) | 1.1% | 0.0% | {"EXTERNAL_STALE": 84, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1, "AGREES_WITH_KALSHI": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 1,153 | 12.8 | 7.1 | 19.4 | 16.5 | 19.8 | 15.0 | 9.4 | 12.82 | 44.1% | 24.4% |
| 4-10x | 747 | 12.4 | 10.4 | 17.3 | 14.7 | 17.7 | 16.1 | 11.4 | 13.57 | 45.1% | 27.4% |
| <2x | 3,093 | 14.3 | 9.2 | 19.2 | 15.1 | 17.8 | 13.3 | 11.0 | 12.14 | 42.1% | 24.2% |
| >=10x | 725 | 10.8 | 5.2 | 14.6 | 15.3 | 20.0 | 22.9 | 11.2 | 16.8 | 54.1% | 34.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 1,637 | 14.2 | 8.9 | 20.6 | 16.1 | 16.7 | 12.0 | 11.5 | 11.65 | 40.3% | 23.5% |
| 300-1000 | 1,332 | 13.4 | 8.5 | 16.4 | 15.5 | 19.8 | 15.6 | 10.7 | 13.79 | 46.2% | 26.4% |
| <300 | 1,375 | 8.5 | 5.5 | 15.0 | 14.6 | 21.4 | 22.6 | 12.4 | 18.17 | 56.4% | 35.0% |
| >=3000 | 1,374 | 17.0 | 11.0 | 21.2 | 15.1 | 16.2 | 11.2 | 8.2 | 10.21 | 35.6% | 19.4% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 208 | 0.5168 | 0.3858 | 0.4231 | +0.094 | -0.037 | 0.0099 ± 0.01 |
| ratio 4-10x | 148 | 0.5816 | 0.4406 | 0.4865 | +0.095 | -0.046 | 0.0115 ± 0.0124 |
| ratio <2x | 435 | 0.5356 | 0.4156 | 0.469 | +0.067 | -0.053 | 0.0104 ± 0.0067 |
| ratio >=10x | 153 | 0.5544 | 0.391 | 0.4771 | +0.077 | -0.086 | 0.0127 ± 0.015 |
| thinner_sample 1000-3000 | 257 | 0.5375 | 0.4182 | 0.4553 | +0.082 | -0.037 | 0.0089 ± 0.0087 |
| thinner_sample 300-1000 | 263 | 0.5554 | 0.4246 | 0.4715 | +0.084 | -0.047 | 0.005 ± 0.0089 |
| thinner_sample <300 | 297 | 0.5416 | 0.3807 | 0.4613 | +0.080 | -0.081 | 0.0171 ± 0.0102 |
| thinner_sample >=3000 | 127 | 0.5225 | 0.4242 | 0.4646 | +0.058 | -0.040 | 0.0123 ± 0.0101 |
| data_status ADEQUATE | 279 | 0.526 | 0.4177 | 0.4552 | +0.071 | -0.037 | 0.0063 ± 0.0075 |
| data_status LIMITED | 204 | 0.5606 | 0.4345 | 0.5 | +0.061 | -0.066 | 0.0035 ± 0.0104 |
| data_status POOR | 461 | 0.5429 | 0.3925 | 0.4512 | +0.092 | -0.059 | 0.0169 ± 0.0076 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 155 | 0.179 | 0.1802 | -0.0012 ± 0.0012 | 0.5323 | 0.5356 | 0.4966 | 0.4822 | 0.5032 | -0.084 ± 0.0368 | -0.01 (3) |
| 3-5 | 96 | 0.1709 | 0.1703 | +0.0006 ± 0.0035 | 0.5209 | 0.515 | 0.5194 | 0.4785 | 0.4896 | -0.079 ± 0.045 | 0.02 (1) |
| 5-10 | 198 | 0.1973 | 0.2019 | -0.0046 ± 0.0048 | 0.5796 | 0.5891 | 0.509 | 0.4342 | 0.4949 | -0.041 ± 0.0321 | -0.0167 (3) |
| 10-15 | 160 | 0.2157 | 0.2082 | +0.0074 ± 0.009 | 0.6148 | 0.5982 | 0.5214 | 0.3977 | 0.4313 | -0.076 ± 0.036 | -0.0633 (3) |
| 15-25 | 206 | 0.213 | 0.2133 | -0.0003 ± 0.0125 | 0.6134 | 0.6114 | 0.5649 | 0.3685 | 0.4709 | -0.017 ± 0.0314 | -0.02 (4) |
| 25-40 | 101 | 0.2365 | 0.1889 | +0.0476 ± 0.0267 | 0.6637 | 0.5522 | 0.6321 | 0.3182 | 0.396 | -0.075 ± 0.0414 | -0.01 (1) |
| 40+ | 28 | 0.3342 | 0.1438 | +0.1903 ± 0.0646 | 0.9071 | 0.4478 | 0.7189 | 0.2771 | 0.2857 | -0.166 ± 0.0702 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 497 | 0.1605 | 0.1618 | -0.0013 ± 0.0006 | 0.4873 | 0.4904 | 0.5065 | 0.4916 | 0.5352 | -0.017 ± 0.0188 | -0.0188 (8) |
| 3-5 | 306 | 0.1736 | 0.1739 | -0.0002 ± 0.0019 | 0.526 | 0.5215 | 0.4896 | 0.4496 | 0.4739 | -0.031 ± 0.0245 | 0.02 (1) |
| 5-10 | 708 | 0.1812 | 0.1813 | -0.0002 ± 0.0024 | 0.542 | 0.5394 | 0.4731 | 0.3989 | 0.4364 | -0.019 ± 0.0161 | -0.0129 (7) |
| 10-15 | 595 | 0.1894 | 0.1731 | +0.0163 ± 0.0042 | 0.5589 | 0.5102 | 0.4759 | 0.3526 | 0.3479 | -0.065 ± 0.017 | -0.0633 (3) |
| 15-25 | 767 | 0.196 | 0.1629 | +0.0331 ± 0.0058 | 0.581 | 0.4833 | 0.483 | 0.2853 | 0.2999 | -0.045 ± 0.0144 | -0.017 (10) |
| 25-40 | 703 | 0.2113 | 0.0962 | +0.1151 ± 0.0073 | 0.6149 | 0.3129 | 0.5058 | 0.1908 | 0.1693 | -0.070 ± 0.0115 | -0.01 (1) |
| 40+ | 518 | 0.3764 | 0.0353 | +0.3411 ± 0.0091 | 0.979 | 0.1533 | 0.6212 | 0.1039 | 0.0425 | -0.093 ± 0.0077 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 97 | 0.1773 | 0.179 | -0.0017 ± 0.0015 | 0.5278 | 0.5304 | 0.5225 | 0.5076 | 0.5567 | -0.044 ± 0.0431 | -0.01 (1) |
| 3-5 | 75 | 0.2031 | 0.2019 | +0.0012 ± 0.0042 | 0.5846 | 0.5876 | 0.4938 | 0.4547 | 0.4533 | -0.071 ± 0.0545 | 0.02 (1) |
| 5-10 | 182 | 0.1866 | 0.1851 | +0.0015 ± 0.0049 | 0.555 | 0.5504 | 0.5712 | 0.4957 | 0.5165 | -0.080 ± 0.0325 | -0.01 (4) |
| 10-15 | 160 | 0.2225 | 0.2081 | +0.0144 ± 0.0092 | 0.633 | 0.6013 | 0.5744 | 0.4493 | 0.4625 | -0.090 ± 0.0375 | -0.0667 (3) |
| 15-25 | 233 | 0.221 | 0.1964 | +0.0245 ± 0.0115 | 0.6274 | 0.5691 | 0.5888 | 0.3915 | 0.4335 | -0.083 ± 0.0298 | -0.0167 (3) |
| 25-40 | 139 | 0.2617 | 0.2047 | +0.0570 ± 0.0237 | 0.7283 | 0.5919 | 0.6598 | 0.35 | 0.4101 | -0.099 ± 0.0402 | -0.025 (2) |
| 40+ | 58 | 0.386 | 0.1899 | +0.1961 ± 0.0581 | 1.0676 | 0.5627 | 0.7579 | 0.2634 | 0.3276 | -0.065 ± 0.056 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 398 | 0.1548 | 0.1567 | -0.0019 ± 0.0007 | 0.4705 | 0.4752 | 0.5382 | 0.5236 | 0.5754 | +0.001 ± 0.0201 | -0.0217 (6) |
| 3-5 | 261 | 0.1678 | 0.1666 | +0.0012 ± 0.002 | 0.5032 | 0.5046 | 0.5364 | 0.4968 | 0.4981 | -0.046 ± 0.0255 | 0.02 (1) |
| 5-10 | 637 | 0.1748 | 0.176 | -0.0012 ± 0.0026 | 0.5248 | 0.5246 | 0.525 | 0.4494 | 0.4914 | -0.013 ± 0.0167 | -0.01 (5) |
| 10-15 | 564 | 0.1876 | 0.1726 | +0.0150 ± 0.0044 | 0.5575 | 0.5105 | 0.5064 | 0.3822 | 0.3918 | -0.049 ± 0.0178 | -0.0575 (4) |
| 15-25 | 831 | 0.2056 | 0.1581 | +0.0475 ± 0.0055 | 0.6003 | 0.4731 | 0.5181 | 0.3218 | 0.3032 | -0.084 ± 0.0138 | -0.0143 (7) |
| 25-40 | 738 | 0.2283 | 0.1247 | +0.1036 ± 0.0082 | 0.6599 | 0.3844 | 0.5473 | 0.2321 | 0.2276 | -0.063 ± 0.0133 | -0.015 (6) |
| 40+ | 665 | 0.4143 | 0.0571 | +0.3571 ± 0.0109 | 1.0855 | 0.213 | 0.6668 | 0.1227 | 0.0797 | -0.076 ± 0.0089 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 152 | 0.1866 | 0.1883 | -0.0018 ± 0.0012 | 0.5466 | 0.5517 | 0.5172 | 0.5028 | 0.5329 | -0.055 ± 0.0352 | -0.01 (5) |
| 3-5 | 103 | 0.1704 | 0.168 | +0.0024 ± 0.0033 | 0.5142 | 0.5087 | 0.5041 | 0.4649 | 0.4563 | -0.113 ± 0.0433 | -- (0) |
| 5-10 | 194 | 0.2017 | 0.2015 | +0.0002 ± 0.0048 | 0.5937 | 0.5866 | 0.496 | 0.423 | 0.4536 | -0.066 ± 0.0325 | -0.01 (3) |
| 10-15 | 160 | 0.2093 | 0.2084 | +0.0009 ± 0.009 | 0.605 | 0.6022 | 0.5454 | 0.4219 | 0.4875 | -0.055 ± 0.0363 | -0.044 (5) |
| 15-25 | 202 | 0.2068 | 0.2018 | +0.0051 ± 0.0122 | 0.6034 | 0.5838 | 0.5769 | 0.384 | 0.4653 | -0.036 ± 0.0302 | -0.03 (1) |
| 25-40 | 111 | 0.2303 | 0.1995 | +0.0308 ± 0.0259 | 0.6524 | 0.5789 | 0.624 | 0.3111 | 0.4144 | -0.057 ± 0.0397 | 0.0 (1) |
| 40+ | 22 | 0.3697 | 0.1534 | +0.2162 ± 0.0757 | 0.9871 | 0.4705 | 0.7299 | 0.2782 | 0.2727 | -0.187 ± 0.0867 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 484 | 0.1679 | 0.1681 | -0.0001 ± 0.0006 | 0.5054 | 0.5063 | 0.5093 | 0.4948 | 0.5 | -0.052 ± 0.0186 | -0.0162 (13) |
| 3-5 | 328 | 0.1781 | 0.1742 | +0.0039 ± 0.0018 | 0.5317 | 0.5218 | 0.4925 | 0.4533 | 0.4299 | -0.083 ± 0.0236 | -0.01 (2) |
| 5-10 | 712 | 0.1851 | 0.1794 | +0.0057 ± 0.0024 | 0.553 | 0.5289 | 0.4595 | 0.3857 | 0.3862 | -0.053 ± 0.016 | -0.01 (3) |
| 10-15 | 589 | 0.1882 | 0.1768 | +0.0114 ± 0.0043 | 0.5576 | 0.5258 | 0.4834 | 0.3597 | 0.3769 | -0.044 ± 0.0174 | -0.03 (9) |
| 15-25 | 816 | 0.1854 | 0.1509 | +0.0345 ± 0.0055 | 0.5595 | 0.454 | 0.4928 | 0.2937 | 0.3064 | -0.044 ± 0.0133 | -0.03 (2) |
| 25-40 | 680 | 0.2114 | 0.0972 | +0.1142 ± 0.0075 | 0.6149 | 0.3135 | 0.4995 | 0.182 | 0.1632 | -0.072 ± 0.0116 | 0.0 (1) |
| 40+ | 485 | 0.3901 | 0.0343 | +0.3558 ± 0.0095 | 1.0181 | 0.1514 | 0.624 | 0.1013 | 0.033 | -0.098 ± 0.0079 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 432 | 0.2019 | 0.2019 | +0.0001 ± 0.0007 | 0.5856 | 0.5857 | 0.4959 | 0.4812 | 0.4815 | -0.042 ± 0.0217 | -0.0226 (46) |
| 3-5 | 317 | 0.1954 | 0.1941 | +0.0013 ± 0.002 | 0.5725 | 0.5665 | 0.4665 | 0.4267 | 0.4353 | -0.040 ± 0.0246 | -0.0059 (32) |
| 5-10 | 657 | 0.1875 | 0.183 | +0.0046 ± 0.0025 | 0.5584 | 0.5455 | 0.4593 | 0.3858 | 0.3927 | -0.038 ± 0.0167 | -0.005 (72) |
| 10-15 | 443 | 0.2037 | 0.1928 | +0.0109 ± 0.0052 | 0.5968 | 0.5663 | 0.4583 | 0.335 | 0.3521 | -0.033 ± 0.0208 | 0.0016 (63) |
| 15-25 | 586 | 0.2332 | 0.2098 | +0.0235 ± 0.0074 | 0.66 | 0.6059 | 0.5307 | 0.3377 | 0.3737 | -0.026 ± 0.0189 | -0.0216 (58) |
| 25-40 | 284 | 0.2672 | 0.1684 | +0.0988 ± 0.0152 | 0.7389 | 0.5063 | 0.5757 | 0.2645 | 0.2606 | -0.069 ± 0.0241 | -0.0216 (25) |
| 40+ | 95 | 0.427 | 0.1595 | +0.2675 ± 0.044 | 1.1976 | 0.4911 | 0.737 | 0.2273 | 0.2421 | -0.060 ± 0.0425 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 806 | 0.1905 | 0.1899 | +0.0006 ± 0.0005 | 0.5585 | 0.5567 | 0.4903 | 0.4757 | 0.4615 | -0.054 ± 0.0153 | -0.0155 (82) |
| 3-5 | 575 | 0.1986 | 0.1966 | +0.0020 ± 0.0015 | 0.5777 | 0.5705 | 0.4709 | 0.4311 | 0.4278 | -0.047 ± 0.0185 | -0.018 (54) |
| 5-10 | 1205 | 0.1863 | 0.1799 | +0.0063 ± 0.0018 | 0.5552 | 0.5359 | 0.4444 | 0.3705 | 0.3685 | -0.043 ± 0.0123 | -0.0089 (122) |
| 10-15 | 900 | 0.1974 | 0.1845 | +0.0129 ± 0.0036 | 0.5812 | 0.5451 | 0.4494 | 0.326 | 0.3356 | -0.035 ± 0.0142 | -0.0053 (99) |
| 15-25 | 1242 | 0.2201 | 0.1866 | +0.0334 ± 0.0048 | 0.6356 | 0.5476 | 0.5041 | 0.3084 | 0.3205 | -0.038 ± 0.0123 | -0.0255 (106) |
| 25-40 | 863 | 0.2433 | 0.1252 | +0.1181 ± 0.0076 | 0.6876 | 0.393 | 0.5265 | 0.2112 | 0.1831 | -0.073 ± 0.0119 | -0.0206 (47) |
| 40+ | 511 | 0.3887 | 0.078 | +0.3107 ± 0.0136 | 1.0602 | 0.2648 | 0.6515 | 0.1345 | 0.1037 | -0.073 ± 0.0126 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 944 | 1.104 ± 0.092 | 1.231 | 0.173 | 0.1822 | 0.2064 | 0.1956 |
| gen2 | 944 | 0.916 ± 0.081 | 1.146 | 0.19 | 0.1814 | 0.2248 | 0.1957 |
| gen1_elo | 944 | 1.097 ± 0.09 | 1.199 | 0.1771 | 0.1826 | 0.2055 | 0.1956 |
| gen1_sr | 944 | 1.131 ± 0.105 | 1.212 | 0.1455 | 0.1837 | 0.2199 | 0.1955 |
| gen1_ledger | 2814 | 0.892 ± 0.051 | 1.063 | 0.163 | 0.2002 | 0.2188 | 0.192 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 5,257)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,740 | 33.1% |
| STALE_QUOTE | market_freshness | 1,604 | 30.5% |
| POOR_DATA | data | 403 | 7.7% |
| BOOK_QUALITY | execution | 339 | 6.5% |
| LIMITED_DATA | data | 316 | 6.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 304 | 5.8% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 261 | 5.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 179 | 3.4% |
| IDENTITY_AMBIGUOUS | mapping | 107 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 4 | 0.1% |

Cause class: coverage 33.1%, market_freshness 30.5%, data 13.7%, market_freshness/coverage 9.2%, execution 6.5%, model_calibration_or_unknown 5.0%, mapping 2.0%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 94.4%, STALE_KALSHI_QUOTE 64.0%, LOW_DATA_QUALITY 63.3%, STALE_PLAYER_DATA 54.0%, THIN_PLAYER_HISTORY 51.6%, MODEL_INTERNAL_DISAGREEMENT 33.9%, ASYMMETRIC_SAMPLE_SIZE 28.9%, WIDE_SPREAD 14.6%, MODEL_HIGH_UNCERTAINTY 14.5%, PLAYER_IDENTITY_RISK 10.9%, LEVEL_TRANSFER_RISK 8.3%, EVENT_MAPPING_RISK 6.2%, LOW_DISPLAYED_LIQUIDITY 5.1%, MODEL_CALIBRATION_OUTLIER 2.1%, UNKNOWN 0.7%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 35.7%, POST_SETTLEMENT_OBSERVATION 33.1%, POSSIBLE_IN_PLAY_QUOTE 6.5%, CONFIRMED_IN_PLAY_QUOTE 1.1%

### >= ge_25 pp (N = 2,903)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,352 | 46.6% |
| STALE_QUOTE | market_freshness | 722 | 24.9% |
| POOR_DATA | data | 171 | 5.9% |
| BOOK_QUALITY | execution | 167 | 5.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 159 | 5.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 104 | 3.6% |
| LIMITED_DATA | data | 86 | 3.0% |
| IDENTITY_AMBIGUOUS | mapping | 77 | 2.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 65 | 2.2% |

Cause class: coverage 46.6%, market_freshness 24.9%, market_freshness/coverage 9.1%, data 8.8%, execution 5.8%, mapping 2.6%, model_calibration_or_unknown 2.2%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 96.7%, STALE_KALSHI_QUOTE 71.0%, LOW_DATA_QUALITY 67.1%, THIN_PLAYER_HISTORY 54.0%, STALE_PLAYER_DATA 51.9%, MODEL_INTERNAL_DISAGREEMENT 34.9%, ASYMMETRIC_SAMPLE_SIZE 31.4%, MODEL_HIGH_UNCERTAINTY 15.8%, PLAYER_IDENTITY_RISK 13.7%, WIDE_SPREAD 13.5%, LEVEL_TRANSFER_RISK 8.1%, EVENT_MAPPING_RISK 7.5%, LOW_DISPLAYED_LIQUIDITY 5.6%, MODEL_CALIBRATION_OUTLIER 3.0%, UNKNOWN 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 49.2%, POST_SETTLEMENT_OBSERVATION 46.6%, POSSIBLE_IN_PLAY_QUOTE 6.3%, CONFIRMED_IN_PLAY_QUOTE 1.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 2472, "IDENTITY_AMBIGUOUS": 431}; ticker orientation: {"VERIFIED": 2903}.

Checks: discipline:AMBIGUOUS 185, discipline:PASS 2718, identity_confidence:AMBIGUOUS 399, identity_confidence:PASS 2504, level_mapping:NA 197, level_mapping:PASS 2706, market_pair:AMBIGUOUS 62, market_pair:NA 81, market_pair:PASS 2760, model_complement:NA 50, model_complement:PASS 2853, namesake:PASS 2903, physical_match_id:NA 1420, physical_match_id:PASS 1483, player_ids:PASS 2903, same_pair_other_event:PASS 2903, ticker_orientation:PASS 2903

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 358 | 5.9% | 6.0% | 0.7% | {"market_freshness": 20, "execution": 1} | 6.78 | 0.1791 / 0.1823 (49) | 44.4% | 0.0% | 0.6% | 3.1% |
| CHALLENGER | 2,104 | 18.0% | 8.2% | 13.1% | {"coverage": 198, "market_freshness": 90, "market_freshness/coverage": 45, "data": 21, "model_calibration_or_unknown": 19, "execution": 4, "mapping": 2} | 7.53 | 0.2207 / 0.2053 (585) | 55.6% | 5.2% | 1.2% | 21.0% |
| DOUBLES | 384 | 48.2% | 48.1% | 6.4% | {"market_freshness": 106, "execution": 32, "mapping": 28, "market_freshness/coverage": 12, "coverage": 7} | 24.1 | 0.3208 / 0.2301 (163) | 60.9% | 0.0% | 100.0% | 10.2% |
| ITF_MEN | 3,798 | 25.0% | 13.5% | 32.8% | {"coverage": 533, "market_freshness": 171, "data": 88, "market_freshness/coverage": 74, "execution": 74, "mapping": 10, "model_calibration_or_unknown": 1} | 9.74 | 0.2134 / 0.188 (1344) | 55.9% | 48.9% | 5.1% | 32.8% |
| ITF_WOMEN | 4,060 | 29.7% | 18.7% | 41.5% | {"coverage": 598, "market_freshness": 287, "data": 128, "market_freshness/coverage": 92, "execution": 47, "mapping": 35, "model_calibration_or_unknown": 19} | 12.61 | 0.2054 / 0.1868 (1225) | 60.0% | 56.2% | 7.9% | 32.0% |
| OTHER | 149 | 8.1% | 7.3% | 0.4% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 798 | 9.4% | 8.1% | 2.6% | {"market_freshness": 34, "model_calibration_or_unknown": 12, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.66 | 0.2006 / 0.1964 (129) | 40.5% | 2.6% | 1.5% | 3.8% |
| WTA125 | 433 | 17.1% | 9.5% | 2.5% | {"market_freshness/coverage": 30, "model_calibration_or_unknown": 12, "market_freshness": 12, "coverage": 11, "data": 9} | 10.17 | 0.2273 / 0.204 (221) | 35.3% | 8.8% | 0.5% | 19.4% |

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
| 8 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
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
| 20 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 21 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 22 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 23 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 153 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 24 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 25 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 22 min (AGING); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 26 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 27 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 28 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 826 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 29 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 687 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 30 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 31 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 32 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 708 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 33 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 34 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 35 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 36 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 37 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 114 min (STALE); data LIMITED (grade B, thinner serve sample 2163.0, ratio 2.0); no external reference |
| 39 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 407 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 40 | `KXWTAMATCH-26OCT01YASCHW-CHW` | WTA | fair_v1 | 73% / 2% | +70 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 51 min (STALE); no external reference |
| 41 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 42 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 43 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 44 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |
| 45 | `KXITFWMATCH-26SEP30KOKUEM-KOK` | ITF_WOMEN | fair_v1 | 79% / 10% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 553 min (STALE); data LIMITED (grade C, thinner serve sample 824.0, ratio 2.35); no external reference |
| 46 | `KXITFMATCH-26SEP20WILRAH-RAH` | ITF_MEN | gen1_ledger | 72% / 4% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade B, thinner serve sample 2782.0, ratio 1.84); no external reference |
| 47 | `KXITFMATCH-26SEP26NAGTHO-NAG` | ITF_MEN | gen1_ledger | 76% / 7% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 89 min (STALE); data LIMITED (grade C, thinner serve sample 1323.0, ratio 4.45); no external reference |
| 48 | `KXITFWMATCH-26SEP26PERPRE-PER` | ITF_WOMEN | gen1_ledger | 78% / 10% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 102 min (STALE); data POOR (grade D, thinner serve sample 1020.0, ratio 2.77); no external reference |
| 49 | `KXITFMATCH-26SEP22YILAGA-AGA` | ITF_MEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 203 min (STALE); data LIMITED (grade B, thinner serve sample 2786.0, ratio 2.08); no external reference |
| 50 | `KXITFMATCH-26SEP30DIMURA-URA` | ITF_MEN | fair_v1 | 71% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.5h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 220 min (STALE); data POOR (grade F, thinner serve sample 174.0, ratio 2.63); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9669, "by_level_share_of_ge_25pp": {"ATP": 0.0072, "CHALLENGER": 0.1306, "DOUBLES": 0.0637, "ITF_MEN": 0.3276, "ITF_WOMEN": 0.4154, "OTHER": 0.0041, "WTA": 0.0258, "WTA125": 0.0255}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.7103, "share_primary_cause_market_settled_or_in_play": 0.5563, "share_primary_cause_stale_quote_only": 0.2487}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 2903, "identity_ambiguous_share": 0.1485, "ticker_orientation": {"VERIFIED": 2903}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 1483, "with_external": 8, "coverage": 0.0054, "external_status": {"EXTERNAL_STALE": 8}, "triangulation": {"INSUFFICIENT_INPUTS": 8}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 603, "with_external": 8, "coverage": 0.0133, "external_status": {"EXTERNAL_STALE": 8}, "triangulation": {"INSUFFICIENT_INPUTS": 8}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 824.0, "median_sample_ratio": 2.3, "median_min_matches": 28.0, "median_max_days_since_last": 173.0, "share_severe_asymmetry": 0.1798, "data_status": {"POOR": 1355, "LIMITED": 961, "ADEQUATE": 587}, "comparison_lt_10pp": {"median_thinner_serve_points": 1948.0, "median_sample_ratio": 1.74, "median_min_matches": 77.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 208, "model_minus_observed": 0.0937, "kalshi_minus_observed": -0.0373, "brier_diff_model_minus_kalshi": 0.0099}, "4-10x": {"n": 148, "model_minus_observed": 0.0951, "kalshi_minus_observed": -0.0459, "brier_diff_model_minus_kalshi": 0.0115}, "<2x": {"n": 435, "model_minus_observed": 0.0667, "kalshi_minus_observed": -0.0533, "brier_diff_model_minus_kalshi": 0.0104}, ">=10x": {"n": 153, "model_minus_observed": 0.0773, "kalshi_minus_observed": -0.0861, "brier_diff_model_minus_kalshi": 0.0127}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 944, "model": {"intercept": -0.609, "slope": 0.916, "slope_se": 0.081}, "kalshi_mid_same_rows": {"intercept": 0.212, "slope": 1.146, "slope_se": 0.09}, "mean_extremity_model": 0.19, "mean_extremity_kalshi": 0.1814, "model_brier": 0.2248, "kalshi_brier": 0.1957, "brier_diff_model_minus_kalshi": 0.0291, "brier_diff_se": 0.0062, "model_logloss": 0.6427, "kalshi_logloss": 0.5714}, "fair_v1": {"n": 944, "model": {"intercept": -0.39, "slope": 1.104, "slope_se": 0.092}, "kalshi_mid_same_rows": {"intercept": 0.368, "slope": 1.231, "slope_se": 0.094}, "mean_extremity_model": 0.173, "mean_extremity_kalshi": 0.1822, "model_brier": 0.2064, "kalshi_brier": 0.1956, "brier_diff_model_minus_kalshi": 0.0108, "brier_diff_se": 0.0049, "model_logloss": 0.5979, "kalshi_logloss": 0.571}, "gen1_elo": {"n": 944, "model": {"intercept": -0.406, "slope": 1.097, "slope_se": 0.09}, "kalshi_mid_same_rows": {"intercept": 0.33, "slope": 1.199, "slope_se": 0.092}, "mean_extremity_model": 0.1771, "mean_extremity_kalshi": 0.1826, "model_brier": 0.2055, "kalshi_brier": 0.1956, "brier_diff_model_minus_kalshi": 0.0099, "brier_diff_se": 0.0049, "model_logloss": 0.5975, "kalshi_logloss": 0.5709}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2594, "share_ge_15": 0.444, "median_abs_gap": 12.99, "n": 5718}, "gen1_elo": {"share_ge_25": 0.2511, "share_ge_15": 0.4325, "median_abs_gap": 12.48, "n": 5718}, "gen1_sr": {"share_ge_25": 0.3094, "share_ge_15": 0.5306, "median_abs_gap": 16.23, "n": 5718}, "gen2": {"share_ge_25": 0.3111, "share_ge_15": 0.5129, "median_abs_gap": 15.58, "n": 5718}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1455, "share_ge_15": 0.3343, "median_abs_gap": 10.11, "n": 4143}, "gen1_elo": {"share_ge_25": 0.1441, "share_ge_15": 0.3184, "median_abs_gap": 9.51, "n": 4143}, "gen1_sr": {"share_ge_25": 0.1994, "share_ge_15": 0.4342, "median_abs_gap": 12.95, "n": 4143}, "gen2": {"share_ge_25": 0.2158, "share_ge_15": 0.4325, "median_abs_gap": 12.8, "n": 4143}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 6.78, "share_ge_25_all": 0.0587, "share_ge_25_pregame_clean": 0.0605}, "WTA": {"median_abs_gap_pregame_clean": 8.66, "share_ge_25_all": 0.094, "share_ge_25_pregame_clean": 0.0807}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2232, "share_within_10pp_all": 0.4147, "share_within_10pp_pregame_clean": 0.4945, "corr_model_vs_mid_pregame_clean": 0.8331}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 155, "model_brier": 0.179, "kalshi_brier": 0.1802, "brier_diff_model_minus_kalshi": -0.0012}, "10-15": {"n_settled": 160, "model_brier": 0.2157, "kalshi_brier": 0.2082, "brier_diff_model_minus_kalshi": 0.0074}, "15-25": {"n_settled": 206, "model_brier": 0.213, "kalshi_brier": 0.2133, "brier_diff_model_minus_kalshi": -0.0003}, "25-40": {"n_settled": 101, "model_brier": 0.2365, "kalshi_brier": 0.1889, "brier_diff_model_minus_kalshi": 0.0476}, "3-5": {"n_settled": 96, "model_brier": 0.1709, "kalshi_brier": 0.1703, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 28, "model_brier": 0.3342, "kalshi_brier": 0.1438, "brier_diff_model_minus_kalshi": 0.1903}, "5-10": {"n_settled": 198, "model_brier": 0.1973, "kalshi_brier": 0.2019, "brier_diff_model_minus_kalshi": -0.0046}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.556, "slope": 0.892, "slope_se": 0.051}, "kalshi_slope": {"intercept": 0.097, "slope": 1.063, "slope_se": 0.052}, "n": 2814}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 163, "model_brier": 0.3208, "kalshi_brier": 0.2301, "brier_diff_model_minus_kalshi": 0.0907, "brier_diff_se": 0.0257, "corr_model_outcome": -0.1018, "corr_kalshi_outcome": 0.3278}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
