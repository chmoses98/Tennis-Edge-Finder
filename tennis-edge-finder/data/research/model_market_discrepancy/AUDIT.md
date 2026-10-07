# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-07T13:59Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 22,612): 0-3 13.5%, 3-5 9.6%, 5-10 19.8%, 10-15 15.3%, 15-25 18.9%, 25-40 14.3%, 40+ 8.5%; median gap 12.17 pp.
* **Where the extremes live**: 98.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.5%, Challenger 12.9%, doubles 5.1%). Main tour: ATP 1.8% and WTA 8.3% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 5,172): MARKET_ALREADY_SETTLED_WHEN_PRICED 39.6%, STALE_QUOTE 18.7%, BOOK_QUALITY 16.8%, POOR_DATA 8.3%, POSSIBLY_IN_PLAY_QUOTE 5.0%, LIMITED_DATA 3.8%, IN_PLAY_QUOTE 3.0%, IDENTITY_AMBIGUOUS 2.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.1%. By class: coverage 39.6%, market_freshness 18.7%, execution 16.8%, data 12.2%, market_freshness/coverage 8.1%, mapping 2.5%, model_calibration_or_unknown 2.1%, model_calibration 0.1%.
* **Stale / settled / in-play**: 57.7% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 47.7% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 5,172 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 16.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 1.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 11.1% of the time and with the model 0.2%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 601.0 points vs 1712.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.165, Gen-2 0.942, Gen-1 ledger 0.954 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 199 model 0.212 vs Kalshi 0.1975; n 48 model 0.2891 vs Kalshi 0.1739.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%). Not implemented here.

## 1. Observations

* 84,262 model-market comparisons (141,668 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 32,274 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-07T13:52:27.416231+00:00'], shadow board 23,465 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-07T13:52:31.625652+00:00'], Model 4 8,453 rows, 10,087 settled tickers, 2,493 tickers with an external scan.
* By model: {"gen1_ledger": 20445, "gen1_elo": 11791, "fair_v1": 11791, "gen2": 11791, "gen1_sr": 11791, "model4_fundamental": 8331, "model4_conditioned": 8322}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 22,612 | 13.5 | 9.6 | 19.8 | 15.3 | 18.9 | 14.3 | 8.5 | 12.17 | 41.8% | 22.9% |
| MW fair_v1 | 11,791 | 12.8 | 8.9 | 18.3 | 16.0 | 18.6 | 15.2 | 10.2 | 13.09 | 44.1% | 25.5% |
| MW gen1_elo | 11,791 | 12.6 | 9.0 | 19.6 | 14.9 | 19.5 | 14.8 | 9.6 | 12.71 | 43.9% | 24.4% |
| MW gen1_ledger | 10,821 | 14.4 | 10.4 | 21.3 | 14.7 | 19.2 | 13.3 | 6.7 | 11.19 | 39.3% | 20.1% |
| MW gen1_sr | 11,791 | 10.0 | 7.7 | 15.9 | 14.2 | 21.7 | 18.7 | 11.9 | 15.85 | 52.3% | 30.6% |
| MW gen2 | 11,791 | 11.7 | 7.1 | 15.9 | 14.4 | 19.9 | 17.6 | 13.4 | 15.41 | 50.9% | 31.0% |
| all families model4_conditioned | 8,322 | 21.9 | 20.4 | 35.1 | 16.2 | 4.7 | 0.9 | 0.8 | 5.76 | 6.4% | 1.7% |
| all families model4_fundamental | 8,331 | 16.4 | 13.3 | 34.5 | 20.4 | 11.1 | 3.1 | 1.2 | 7.78 | 15.4% | 4.3% |

Configurable thresholds (primary): >=5pp 76.9%, >=10pp 57.1%, >=15pp 41.8%, >=20pp 31.3%, >=25pp 22.9%, >=30pp 16.7%, >=40pp 8.5%, >=50pp 3.6%
Executable gap (model outside the book, before fees): median 8.54pp; >=10pp 45.9%, >=25pp 18.4%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 831 | 25.9 | 16.7 | 24.3 | 17.1 | 13.2 | 1.4 | 1.3 | 5.96 | 16.0% | 2.8% |
| CHALLENGER | 2,109 | 14.3 | 11.3 | 18.5 | 16.3 | 12.9 | 13.5 | 13.2 | 12.03 | 39.6% | 26.7% |
| ITF_MEN | 3,358 | 10.4 | 8.4 | 18.8 | 14.5 | 19.7 | 15.2 | 13.0 | 14.15 | 47.9% | 28.2% |
| ITF_WOMEN | 4,673 | 10.2 | 6.7 | 16.0 | 16.1 | 21.7 | 19.4 | 9.8 | 15.41 | 50.9% | 29.2% |
| WTA | 524 | 23.3 | 9.7 | 24.4 | 16.6 | 17.6 | 6.3 | 2.1 | 8.25 | 25.9% | 8.4% |
| WTA125 | 296 | 12.5 | 6.8 | 20.9 | 25.3 | 14.2 | 17.6 | 2.7 | 11.39 | 34.5% | 20.3% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 831 | 21.3 | 15.2 | 23.9 | 18.4 | 17.1 | 2.5 | 1.6 | 6.9 | 21.2% | 4.1% |
| CHALLENGER | 2,109 | 14.8 | 7.3 | 17.7 | 13.5 | 18.5 | 14.7 | 13.5 | 13.43 | 46.7% | 28.2% |
| ITF_MEN | 3,358 | 10.2 | 7.2 | 16.7 | 14.7 | 19.8 | 17.7 | 13.7 | 15.48 | 51.2% | 31.4% |
| ITF_WOMEN | 4,673 | 8.9 | 6.1 | 12.9 | 13.1 | 20.9 | 21.5 | 16.5 | 18.87 | 58.9% | 38.0% |
| WTA | 524 | 21.8 | 5.0 | 17.6 | 15.5 | 21.6 | 16.6 | 2.1 | 12.76 | 40.3% | 18.7% |
| WTA125 | 296 | 5.1 | 2.4 | 16.9 | 23.6 | 19.3 | 19.9 | 12.8 | 16.69 | 52.0% | 32.8% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 831 | 25.9 | 11.6 | 29.4 | 17.2 | 10.9 | 3.6 | 1.4 | 6.85 | 16.0% | 5.1% |
| CHALLENGER | 2,109 | 15.4 | 11.2 | 19.6 | 14.2 | 14.0 | 12.5 | 13.1 | 11.01 | 39.6% | 25.6% |
| ITF_MEN | 3,358 | 9.4 | 8.8 | 18.2 | 13.7 | 21.2 | 15.6 | 13.0 | 14.97 | 49.8% | 28.6% |
| ITF_WOMEN | 4,673 | 9.6 | 6.9 | 16.5 | 15.6 | 23.6 | 19.1 | 8.5 | 15.57 | 51.3% | 27.7% |
| WTA | 524 | 23.1 | 13.2 | 34.7 | 14.5 | 9.5 | 3.6 | 1.3 | 6.99 | 14.5% | 5.0% |
| WTA125 | 296 | 20.9 | 11.8 | 28.0 | 17.9 | 15.2 | 5.4 | 0.7 | 7.86 | 21.3% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 411 | 28.0 | 21.2 | 38.0 | 11.7 | 1.2 | 0.0 | 0.0 | 5.22 | 1.2% | 0.0% |
| CHALLENGER | 1,353 | 22.8 | 16.2 | 26.7 | 14.1 | 12.3 | 5.6 | 2.2 | 6.78 | 20.2% | 7.8% |
| DOUBLES | 587 | 3.9 | 3.1 | 13.1 | 12.4 | 23.0 | 21.3 | 23.2 | 22.7 | 67.5% | 44.5% |
| ITF_MEN | 3,426 | 13.5 | 8.5 | 19.9 | 15.3 | 20.8 | 13.4 | 8.6 | 12.35 | 42.9% | 22.0% |
| ITF_WOMEN | 3,997 | 11.5 | 9.5 | 19.2 | 13.9 | 22.3 | 17.5 | 6.1 | 13.32 | 45.9% | 23.6% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 432 | 19.4 | 11.8 | 25.7 | 19.2 | 15.7 | 7.4 | 0.7 | 8.66 | 23.8% | 8.1% |
| WTA125 | 466 | 15.2 | 12.7 | 22.3 | 19.5 | 17.8 | 9.4 | 3.0 | 9.93 | 30.3% | 12.4% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 827 | 25.9 | 16.6 | 24.3 | 17.2 | 13.3 | 1.4 | 1.3 | 6.01 | 16.1% | 2.8% |
| CHALLENGER | 1,500 | 18.6 | 14.5 | 23.9 | 18.9 | 13.9 | 7.2 | 3.0 | 8.38 | 24.1% | 10.2% |
| ITF_MEN | 2,446 | 12.7 | 10.6 | 22.3 | 16.0 | 19.8 | 12.6 | 6.1 | 11.18 | 38.4% | 18.6% |
| ITF_WOMEN | 3,397 | 12.6 | 8.4 | 18.8 | 18.5 | 23.2 | 15.4 | 3.1 | 12.71 | 41.7% | 18.6% |
| WTA | 522 | 23.4 | 9.8 | 24.5 | 16.5 | 17.6 | 6.1 | 2.1 | 8.2 | 25.9% | 8.2% |
| WTA125 | 285 | 13.0 | 7.0 | 20.7 | 25.6 | 14.4 | 17.5 | 1.8 | 11.31 | 33.7% | 19.3% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 827 | 21.2 | 15.1 | 24.1 | 18.4 | 17.2 | 2.5 | 1.6 | 6.9 | 21.3% | 4.1% |
| CHALLENGER | 1,500 | 19.5 | 9.6 | 22.3 | 16.3 | 19.3 | 10.1 | 2.9 | 9.63 | 32.3% | 13.0% |
| ITF_MEN | 2,446 | 12.1 | 8.5 | 19.5 | 16.8 | 20.8 | 15.2 | 7.0 | 12.73 | 43.0% | 22.2% |
| ITF_WOMEN | 3,397 | 10.4 | 7.2 | 14.9 | 14.2 | 23.0 | 20.0 | 10.3 | 16.26 | 53.3% | 30.3% |
| WTA | 522 | 21.8 | 5.0 | 17.6 | 15.5 | 21.5 | 16.5 | 2.1 | 12.73 | 40.0% | 18.6% |
| WTA125 | 285 | 5.3 | 2.5 | 17.2 | 24.6 | 18.2 | 20.7 | 11.6 | 15.35 | 50.5% | 32.3% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 396 | 28.3 | 21.5 | 38.1 | 11.9 | 0.2 | 0.0 | 0.0 | 5.06 | 0.2% | 0.0% |
| CHALLENGER | 1,138 | 25.0 | 18.4 | 29.1 | 13.7 | 11.7 | 2.1 | 0.1 | 6.16 | 13.9% | 2.2% |
| DOUBLES | 536 | 3.9 | 3.0 | 13.4 | 12.3 | 23.5 | 21.1 | 22.8 | 22.7 | 67.3% | 43.8% |
| ITF_MEN | 2,750 | 15.3 | 9.4 | 22.1 | 16.3 | 20.6 | 11.2 | 5.0 | 11.04 | 36.9% | 16.2% |
| ITF_WOMEN | 3,235 | 12.9 | 10.4 | 21.1 | 14.7 | 22.7 | 15.7 | 2.5 | 11.62 | 40.8% | 18.1% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 402 | 19.9 | 12.4 | 26.4 | 19.4 | 16.2 | 5.7 | 0.0 | 8.4 | 21.9% | 5.7% |
| WTA125 | 383 | 17.2 | 14.1 | 25.1 | 22.4 | 15.9 | 5.0 | 0.3 | 8.88 | 21.1% | 5.2% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 587 | 3.9 | 3.1 | 13.1 | 12.4 | 23.0 | 21.3 | 23.2 | 22.7 | 67.5% | 44.5% |
| singles | 10,234 | 15.0 | 10.8 | 21.8 | 14.8 | 19.0 | 12.9 | 5.8 | 10.68 | 37.7% | 18.6% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 2,762 | 13.0 | 9.6 | 20.1 | 15.7 | 16.0 | 14.8 | 10.9 | 12.36 | 41.7% | 25.6% |
| Hard | 7,951 | 12.8 | 8.7 | 18.3 | 15.8 | 19.3 | 15.1 | 10.0 | 13.25 | 44.4% | 25.1% |
| UNKNOWN | 1,078 | 12.1 | 8.3 | 13.6 | 18.3 | 20.3 | 17.4 | 10.0 | 14.16 | 47.7% | 27.4% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,407 | 17.8 | 11.4 | 20.2 | 17.1 | 14.9 | 10.3 | 8.3 | 10.16 | 33.6% | 18.6% |
| B | 1,462 | 14.8 | 9.8 | 19.7 | 17.2 | 16.4 | 11.9 | 10.2 | 11.18 | 38.4% | 22.1% |
| C | 1,830 | 12.3 | 9.6 | 21.3 | 14.9 | 18.4 | 14.3 | 9.2 | 12.55 | 41.9% | 23.5% |
| D | 2,245 | 11.4 | 8.8 | 16.4 | 16.3 | 23.0 | 15.2 | 9.0 | 14.08 | 47.2% | 24.2% |
| F | 2,847 | 7.1 | 5.0 | 14.9 | 14.6 | 20.8 | 23.5 | 14.1 | 18.59 | 58.4% | 37.6% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 2,963 | 21.1 | 14.9 | 27.2 | 15.9 | 13.2 | 5.4 | 2.2 | 7.3 | 20.9% | 7.7% |
| B | 1,641 | 14.3 | 10.0 | 24.2 | 15.5 | 18.6 | 12.0 | 5.4 | 10.4 | 36.0% | 17.4% |
| C | 2,148 | 12.0 | 8.2 | 19.3 | 14.8 | 21.1 | 14.6 | 10.0 | 13.18 | 45.7% | 24.6% |
| D | 1,846 | 12.9 | 9.2 | 21.0 | 13.3 | 22.4 | 14.9 | 6.4 | 12.55 | 43.7% | 21.3% |
| F | 2,223 | 9.0 | 7.7 | 13.6 | 13.3 | 23.3 | 22.3 | 10.8 | 17.27 | 56.4% | 33.1% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 3,874 | 16.8 | 10.6 | 19.5 | 17.2 | 15.2 | 10.5 | 10.1 | 10.85 | 35.9% | 20.7% |
| LIMITED | 2,789 | 14.0 | 10.5 | 21.7 | 15.4 | 17.4 | 13.5 | 7.4 | 11.1 | 38.3% | 20.9% |
| POOR | 5,128 | 9.0 | 6.7 | 15.5 | 15.4 | 21.8 | 19.8 | 11.8 | 16.36 | 53.4% | 31.6% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,721 | 29.7 | 26.3 | 36.7 | 5.5 | 1.7 | 0.2 | 0.0 | 4.47 | 1.9% | 0.2% |
| GAME_SPREAD | 1,799 | 24.0 | 15.3 | 36.9 | 18.8 | 4.6 | 0.3 | 0.2 | 6.2 | 5.0% | 0.4% |
| MATCH_WINNER | 10,821 | 14.4 | 10.4 | 21.3 | 14.7 | 19.2 | 13.3 | 6.7 | 11.19 | 39.3% | 20.1% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 3,358 | 29.2 | 18.7 | 31.5 | 11.5 | 7.4 | 1.4 | 0.3 | 5.25 | 9.1% | 1.7% |
| TOTAL_GAMES | 2,722 | 7.6 | 9.4 | 38.1 | 29.3 | 10.0 | 3.3 | 2.4 | 9.45 | 15.7% | 5.7% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,052 | 24.5 | 39.4 | 29.2 | 0.3 | 5.9 | 0.6 | 0.2 | 4.34 | 6.6% | 0.8% |
| GAME_SPREAD | 2,106 | 45.5 | 14.2 | 29.7 | 8.6 | 1.1 | 0.6 | 0.2 | 3.59 | 1.8% | 0.8% |
| TOTAL_GAMES | 3,164 | 3.5 | 6.2 | 44.4 | 36.6 | 6.0 | 1.4 | 1.8 | 9.66 | 9.3% | 3.2% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,052 | 25.4 | 18.2 | 35.5 | 9.9 | 7.3 | 3.1 | 0.5 | 5.62 | 10.9% | 3.6% |
| GAME_SPREAD | 2,106 | 19.4 | 13.2 | 26.4 | 22.8 | 14.5 | 3.0 | 0.7 | 8.34 | 18.2% | 3.8% |
| TOTAL_GAMES | 3,173 | 5.9 | 8.6 | 38.9 | 28.7 | 12.5 | 3.3 | 2.2 | 9.65 | 18.0% | 5.5% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 11,791 | 44.1% | 25.5% | 13.09 | 34.3% | 15.2% | 10.55 |
| gen1_elo | 11,791 | 43.9% | 24.4% | 12.71 | 34.0% | 14.6% | 10.13 |
| gen1_sr | 11,791 | 52.3% | 30.6% | 15.85 | 43.5% | 20.3% | 12.98 |
| gen2 | 11,791 | 50.9% | 31.0% | 15.41 | 43.2% | 22.2% | 12.77 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 5,675 | 15.3 | 11.4 | 21.5 | 17.3 | 18.7 | 12.1 | 3.6 | 10.43 | 34.4% | 15.7% |
| STALE | 6,116 | 10.4 | 6.5 | 15.3 | 14.8 | 18.5 | 18.2 | 16.3 | 16.55 | 53.0% | 34.5% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 4,289 | 16.2 | 11.6 | 23.8 | 14.5 | 17.4 | 12.1 | 4.4 | 9.64 | 33.9% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 22,612 | 4289 | 9147 | 9176 | 25.7 | 167.2 | 1400.4 |
| ge_15pp | 9,448 | 1454 | 3243 | 4751 | 30.2 | 440.0 | 1380.4 |
| ge_25pp | 5,172 | 708 | 1482 | 2982 | 39.8 | 549.3 | 1380.4 |
| lt_10pp | 9,692 | 2214 | 4373 | 3105 | 24.4 | 52.9 | 1201.9 |

Current slate `SL-20261007T135932Z-52e88066`: 354 priced rows, quote age at build {'median': 7.4, 'max': 7.5}, freshness {'FRESH': 354}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 1 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 20.71 | 100.0% | 0.0% |
| EXTERNAL_LONE_OUTLIER | 2 | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.98 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 409 | 20.1 | 12.0 | 22.0 | 21.0 | 17.1 | 7.3 | 0.5 | 8.64 | 24.9% | 7.8% |
| MARKETS_AGREE | 35 | 71.4 | 28.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 56 | 0.0 | 3.6 | 23.2 | 37.5 | 25.0 | 10.7 | 0.0 | 12.68 | 35.7% | 10.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 11,791 | 503 (4.3%) | 11.1% | 0.2% | {"EXTERNAL_STALE": 409, "AGREES_WITH_KALSHI": 56, "ALL_AGREE": 35, "EXTERNAL_OUTLIER": 2, "SUPPORTS_MODEL_DIRECTION": 1} |
| fair_v1_ge_15pp | 5,195 | 123 (2.4%) | 16.3% | 0.8% | {"EXTERNAL_STALE": 102, "AGREES_WITH_KALSHI": 20, "SUPPORTS_MODEL_DIRECTION": 1} |
| fair_v1_ge_25pp | 3,002 | 38 (1.3%) | 15.8% | 0.0% | {"EXTERNAL_STALE": 32, "AGREES_WITH_KALSHI": 6} |
| fair_v1_ge_25pp_pregame_clean | 1,360 | 38 (2.8%) | 15.8% | 0.0% | {"EXTERNAL_STALE": 32, "AGREES_WITH_KALSHI": 6} |
| fair_v1_lt_10pp | 4,709 | 273 (5.8%) | 5.5% | 0.0% | {"EXTERNAL_STALE": 221, "ALL_AGREE": 35, "AGREES_WITH_KALSHI": 15, "EXTERNAL_OUTLIER": 2} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 2,369 | 11.0 | 8.7 | 20.5 | 15.7 | 21.0 | 14.0 | 9.2 | 12.82 | 44.1% | 23.1% |
| 4-10x | 1,739 | 11.1 | 9.4 | 17.9 | 14.4 | 20.8 | 17.2 | 9.0 | 14.09 | 47.1% | 26.3% |
| <2x | 6,155 | 14.6 | 9.5 | 18.3 | 16.9 | 17.0 | 13.7 | 10.2 | 12.34 | 40.8% | 23.8% |
| >=10x | 1,528 | 10.1 | 6.0 | 15.4 | 14.8 | 19.0 | 21.3 | 13.4 | 16.57 | 53.7% | 34.8% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 2,966 | 13.5 | 8.5 | 20.5 | 15.8 | 17.5 | 13.1 | 11.1 | 12.25 | 41.7% | 24.2% |
| 300-1000 | 2,874 | 12.1 | 9.4 | 16.6 | 15.9 | 21.6 | 16.0 | 8.3 | 13.69 | 46.0% | 24.4% |
| <300 | 3,318 | 7.9 | 6.1 | 15.4 | 14.9 | 20.8 | 21.5 | 13.5 | 17.51 | 55.8% | 35.0% |
| >=3000 | 2,633 | 18.8 | 12.2 | 21.4 | 17.8 | 13.8 | 9.0 | 7.1 | 9.45 | 29.8% | 16.1% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 344 | 0.5349 | 0.4032 | 0.4651 | +0.070 | -0.062 | 0.0016 ± 0.0077 |
| ratio 4-10x | 259 | 0.5883 | 0.4489 | 0.5367 | +0.052 | -0.088 | -0.0052 ± 0.0095 |
| ratio <2x | 736 | 0.5436 | 0.4163 | 0.4633 | +0.080 | -0.047 | 0.0104 ± 0.0054 |
| ratio >=10x | 246 | 0.5607 | 0.3847 | 0.4593 | +0.101 | -0.075 | 0.0128 ± 0.0118 |
| thinner_sample 1000-3000 | 418 | 0.5457 | 0.4224 | 0.4641 | +0.082 | -0.042 | 0.005 ± 0.0069 |
| thinner_sample 300-1000 | 428 | 0.5712 | 0.4319 | 0.4977 | +0.073 | -0.066 | 0.0005 ± 0.0074 |
| thinner_sample <300 | 519 | 0.5519 | 0.3881 | 0.4798 | +0.072 | -0.092 | 0.0077 ± 0.0077 |
| thinner_sample >=3000 | 220 | 0.5244 | 0.4235 | 0.4409 | +0.084 | -0.017 | 0.0169 ± 0.0079 |
| data_status ADEQUATE | 423 | 0.5307 | 0.4234 | 0.4444 | +0.086 | -0.021 | 0.0103 ± 0.0061 |
| data_status LIMITED | 370 | 0.5659 | 0.4337 | 0.5 | +0.066 | -0.066 | -0.0001 ± 0.0077 |
| data_status POOR | 792 | 0.5562 | 0.3995 | 0.4798 | +0.076 | -0.080 | 0.0072 ± 0.006 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 234 | 0.18 | 0.181 | -0.0009 ± 0.0009 | 0.5343 | 0.5367 | 0.4961 | 0.4818 | 0.5085 | -0.089 ± 0.0296 | -0.01 (3) |
| 3-5 | 162 | 0.1808 | 0.1816 | -0.0008 ± 0.0027 | 0.5405 | 0.5395 | 0.5103 | 0.4702 | 0.4938 | -0.083 ± 0.0342 | 0.02 (1) |
| 5-10 | 327 | 0.1997 | 0.2014 | -0.0017 ± 0.0037 | 0.5854 | 0.5881 | 0.5221 | 0.4481 | 0.4893 | -0.094 ± 0.0257 | -0.0167 (3) |
| 10-15 | 274 | 0.2191 | 0.2178 | +0.0013 ± 0.0071 | 0.6262 | 0.6194 | 0.5328 | 0.4084 | 0.4635 | -0.089 ± 0.0282 | -0.0633 (3) |
| 15-25 | 341 | 0.2171 | 0.2108 | +0.0063 ± 0.0097 | 0.623 | 0.6093 | 0.5701 | 0.3738 | 0.4545 | -0.070 ± 0.0248 | -0.02 (4) |
| 25-40 | 199 | 0.212 | 0.1975 | +0.0145 ± 0.0188 | 0.6108 | 0.5691 | 0.6466 | 0.3355 | 0.4673 | -0.065 ± 0.0274 | -0.01 (1) |
| 40+ | 48 | 0.2891 | 0.1739 | +0.1152 ± 0.0532 | 0.7828 | 0.5229 | 0.7471 | 0.301 | 0.3958 | -0.124 ± 0.0537 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1035 | 0.1623 | 0.1631 | -0.0008 ± 0.0004 | 0.4907 | 0.4916 | 0.4851 | 0.4703 | 0.5111 | -0.030 ± 0.0128 | -0.0188 (8) |
| 3-5 | 734 | 0.1867 | 0.1831 | +0.0036 ± 0.0013 | 0.5532 | 0.5394 | 0.4735 | 0.434 | 0.4033 | -0.098 ± 0.0161 | 0.02 (1) |
| 5-10 | 1542 | 0.1875 | 0.1852 | +0.0022 ± 0.0016 | 0.5559 | 0.5477 | 0.4861 | 0.4122 | 0.4326 | -0.057 ± 0.011 | -0.0129 (7) |
| 10-15 | 1344 | 0.1955 | 0.1832 | +0.0123 ± 0.0029 | 0.5745 | 0.537 | 0.4758 | 0.351 | 0.3638 | -0.066 ± 0.0117 | -0.0633 (3) |
| 15-25 | 1705 | 0.1978 | 0.1649 | +0.0329 ± 0.0039 | 0.5841 | 0.4902 | 0.4897 | 0.2931 | 0.3079 | -0.065 ± 0.0098 | -0.017 (10) |
| 25-40 | 1553 | 0.214 | 0.1205 | +0.0935 ± 0.0055 | 0.6197 | 0.3744 | 0.5258 | 0.2121 | 0.2222 | -0.060 ± 0.0084 | -0.01 (1) |
| 40+ | 1084 | 0.3646 | 0.0475 | +0.3171 ± 0.0073 | 0.9508 | 0.1836 | 0.6199 | 0.1064 | 0.0646 | -0.077 ± 0.0062 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 180 | 0.188 | 0.1881 | -0.0001 ± 0.0011 | 0.5554 | 0.5564 | 0.493 | 0.478 | 0.4667 | -0.126 ± 0.0343 | -0.01 (1) |
| 3-5 | 115 | 0.2068 | 0.2057 | +0.0011 ± 0.0034 | 0.5931 | 0.5944 | 0.4983 | 0.4585 | 0.4609 | -0.092 ± 0.0457 | 0.02 (1) |
| 5-10 | 282 | 0.193 | 0.1917 | +0.0013 ± 0.0039 | 0.5686 | 0.5643 | 0.5688 | 0.4932 | 0.5177 | -0.091 ± 0.027 | -0.01 (4) |
| 10-15 | 272 | 0.2227 | 0.2106 | +0.0122 ± 0.007 | 0.6334 | 0.6088 | 0.5874 | 0.463 | 0.4816 | -0.127 ± 0.0292 | -0.0667 (3) |
| 15-25 | 380 | 0.2211 | 0.2057 | +0.0154 ± 0.0092 | 0.6288 | 0.592 | 0.5983 | 0.4006 | 0.4658 | -0.096 ± 0.024 | -0.0167 (3) |
| 25-40 | 254 | 0.2555 | 0.1998 | +0.0557 ± 0.0175 | 0.7126 | 0.5802 | 0.6663 | 0.3545 | 0.4213 | -0.123 ± 0.0281 | -0.025 (2) |
| 40+ | 102 | 0.3441 | 0.187 | +0.1571 ± 0.042 | 0.9542 | 0.5492 | 0.7596 | 0.2765 | 0.3725 | -0.063 ± 0.0395 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 936 | 0.1679 | 0.1684 | -0.0006 ± 0.0004 | 0.5038 | 0.506 | 0.5001 | 0.4857 | 0.5 | -0.052 ± 0.0142 | -0.0217 (6) |
| 3-5 | 602 | 0.1861 | 0.1817 | +0.0044 ± 0.0014 | 0.5427 | 0.5338 | 0.5099 | 0.4699 | 0.4352 | -0.090 ± 0.0177 | 0.02 (1) |
| 5-10 | 1337 | 0.1812 | 0.179 | +0.0022 ± 0.0017 | 0.5397 | 0.5301 | 0.5076 | 0.4331 | 0.454 | -0.051 ± 0.0118 | -0.01 (5) |
| 10-15 | 1233 | 0.1902 | 0.1744 | +0.0158 ± 0.003 | 0.5656 | 0.5174 | 0.5233 | 0.3992 | 0.4006 | -0.081 ± 0.0122 | -0.0575 (4) |
| 15-25 | 1780 | 0.2079 | 0.1719 | +0.0361 ± 0.0039 | 0.6062 | 0.5079 | 0.5299 | 0.3346 | 0.3421 | -0.077 ± 0.01 | -0.0143 (7) |
| 25-40 | 1706 | 0.2416 | 0.1339 | +0.1078 ± 0.0056 | 0.6858 | 0.4098 | 0.5587 | 0.2417 | 0.2315 | -0.085 ± 0.0089 | -0.015 (6) |
| 40+ | 1403 | 0.3988 | 0.0711 | +0.3277 ± 0.0081 | 1.0418 | 0.2462 | 0.668 | 0.1305 | 0.1076 | -0.064 ± 0.0068 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 243 | 0.1881 | 0.1905 | -0.0024 ± 0.001 | 0.554 | 0.5608 | 0.5093 | 0.4943 | 0.5514 | -0.040 ± 0.0282 | -0.01 (5) |
| 3-5 | 168 | 0.1808 | 0.1791 | +0.0017 ± 0.0026 | 0.5363 | 0.5323 | 0.5005 | 0.4613 | 0.4583 | -0.135 ± 0.0346 | -- (0) |
| 5-10 | 331 | 0.1928 | 0.1933 | -0.0005 ± 0.0036 | 0.5704 | 0.5682 | 0.5185 | 0.4449 | 0.4804 | -0.089 ± 0.0248 | -0.01 (3) |
| 10-15 | 261 | 0.2154 | 0.2167 | -0.0013 ± 0.0071 | 0.6209 | 0.6188 | 0.545 | 0.4218 | 0.4904 | -0.082 ± 0.0285 | -0.044 (5) |
| 15-25 | 335 | 0.2202 | 0.2091 | +0.0111 ± 0.0097 | 0.6363 | 0.6028 | 0.5797 | 0.3863 | 0.4537 | -0.085 ± 0.0248 | -0.03 (1) |
| 25-40 | 205 | 0.2014 | 0.2058 | -0.0045 ± 0.0184 | 0.5859 | 0.591 | 0.651 | 0.339 | 0.4976 | -0.048 ± 0.0267 | 0.0 (1) |
| 40+ | 42 | 0.3172 | 0.1727 | +0.1445 ± 0.058 | 0.849 | 0.5198 | 0.738 | 0.286 | 0.3571 | -0.137 ± 0.0602 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1025 | 0.1723 | 0.1737 | -0.0013 ± 0.0005 | 0.5147 | 0.5179 | 0.4848 | 0.4696 | 0.5132 | -0.023 ± 0.013 | -0.0162 (13) |
| 3-5 | 732 | 0.184 | 0.1798 | +0.0043 ± 0.0012 | 0.5439 | 0.5352 | 0.4754 | 0.4359 | 0.4016 | -0.110 ± 0.0163 | -0.01 (2) |
| 5-10 | 1616 | 0.1798 | 0.1762 | +0.0036 ± 0.0016 | 0.54 | 0.5251 | 0.4803 | 0.4064 | 0.4177 | -0.060 ± 0.0104 | -0.01 (3) |
| 10-15 | 1290 | 0.1924 | 0.1814 | +0.0110 ± 0.0029 | 0.5675 | 0.5302 | 0.4921 | 0.3688 | 0.3845 | -0.065 ± 0.0117 | -0.03 (9) |
| 15-25 | 1818 | 0.1988 | 0.1639 | +0.0348 ± 0.0038 | 0.59 | 0.4888 | 0.491 | 0.2938 | 0.3064 | -0.063 ± 0.0096 | -0.03 (2) |
| 25-40 | 1496 | 0.2129 | 0.1188 | +0.0941 ± 0.0056 | 0.6166 | 0.3684 | 0.5223 | 0.2042 | 0.2186 | -0.061 ± 0.0084 | 0.0 (1) |
| 40+ | 1020 | 0.3781 | 0.0481 | +0.3300 ± 0.0078 | 0.9902 | 0.1858 | 0.626 | 0.1053 | 0.0608 | -0.079 ± 0.0065 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 515 | 0.1999 | 0.2003 | -0.0003 ± 0.0007 | 0.5805 | 0.5817 | 0.4978 | 0.483 | 0.4932 | -0.040 ± 0.0197 | -0.0226 (46) |
| 3-5 | 388 | 0.1963 | 0.196 | +0.0003 ± 0.0018 | 0.575 | 0.5725 | 0.4793 | 0.4396 | 0.4588 | -0.038 ± 0.0223 | -0.0059 (32) |
| 5-10 | 804 | 0.1876 | 0.1825 | +0.0051 ± 0.0023 | 0.5578 | 0.5448 | 0.4688 | 0.3953 | 0.398 | -0.056 ± 0.0154 | -0.005 (72) |
| 10-15 | 524 | 0.2 | 0.1903 | +0.0096 ± 0.0048 | 0.5873 | 0.5611 | 0.4731 | 0.3501 | 0.3721 | -0.040 ± 0.0189 | 0.0016 (63) |
| 15-25 | 713 | 0.2344 | 0.2112 | +0.0231 ± 0.0067 | 0.6642 | 0.608 | 0.5391 | 0.3453 | 0.3843 | -0.045 ± 0.0173 | -0.0216 (58) |
| 25-40 | 392 | 0.249 | 0.1781 | +0.0709 ± 0.0133 | 0.6974 | 0.5278 | 0.608 | 0.2946 | 0.3367 | -0.071 ± 0.0201 | -0.0216 (25) |
| 40+ | 132 | 0.345 | 0.1805 | +0.1644 ± 0.0379 | 0.9738 | 0.5377 | 0.7603 | 0.2663 | 0.3712 | -0.034 ± 0.0334 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1343 | 0.1849 | 0.185 | -0.0001 ± 0.0004 | 0.5424 | 0.5425 | 0.4956 | 0.4804 | 0.4877 | -0.041 ± 0.0117 | -0.0155 (82) |
| 3-5 | 962 | 0.1858 | 0.1841 | +0.0017 ± 0.0011 | 0.5482 | 0.544 | 0.4893 | 0.4496 | 0.4522 | -0.047 ± 0.0139 | -0.018 (54) |
| 5-10 | 2014 | 0.1803 | 0.174 | +0.0063 ± 0.0014 | 0.5397 | 0.5221 | 0.4656 | 0.3917 | 0.3883 | -0.058 ± 0.0094 | -0.0089 (122) |
| 10-15 | 1427 | 0.1946 | 0.1819 | +0.0127 ± 0.0028 | 0.5749 | 0.5406 | 0.4833 | 0.3602 | 0.37 | -0.051 ± 0.0112 | -0.0053 (99) |
| 15-25 | 1890 | 0.2234 | 0.1957 | +0.0278 ± 0.004 | 0.645 | 0.569 | 0.5328 | 0.3373 | 0.364 | -0.048 ± 0.0103 | -0.0255 (106) |
| 25-40 | 1348 | 0.2396 | 0.1508 | +0.0889 ± 0.0067 | 0.6773 | 0.4555 | 0.5733 | 0.258 | 0.2767 | -0.067 ± 0.0103 | -0.0206 (47) |
| 40+ | 666 | 0.3544 | 0.102 | +0.2524 ± 0.0132 | 0.9663 | 0.3256 | 0.6679 | 0.1633 | 0.1772 | -0.056 ± 0.0116 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 1585 | 1.165 ± 0.075 | 1.247 | 0.1687 | 0.1673 | 0.2062 | 0.1999 |
| gen2 | 1585 | 0.942 ± 0.065 | 1.165 | 0.1853 | 0.1668 | 0.225 | 0.1999 |
| gen1_elo | 1585 | 1.147 ± 0.073 | 1.237 | 0.1729 | 0.1675 | 0.2048 | 0.1997 |
| gen1_sr | 1585 | 1.176 ± 0.084 | 1.255 | 0.1424 | 0.1691 | 0.2205 | 0.1997 |
| gen1_ledger | 3468 | 0.954 ± 0.046 | 1.111 | 0.1675 | 0.1935 | 0.2148 | 0.1931 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 9,448)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,600 | 27.5% |
| STALE_QUOTE | market_freshness | 2,155 | 22.8% |
| BOOK_QUALITY | execution | 1,679 | 17.8% |
| POOR_DATA | data | 1,001 | 10.6% |
| LIMITED_DATA | data | 622 | 6.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 460 | 4.9% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 440 | 4.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 255 | 2.7% |
| IDENTITY_AMBIGUOUS | mapping | 223 | 2.4% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 13 | 0.1% |

Cause class: coverage 27.5%, market_freshness 22.8%, execution 17.8%, data 17.2%, market_freshness/coverage 7.6%, model_calibration_or_unknown 4.7%, mapping 2.4%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.7%, START_UNVERIFIABLE 96.0%, LOW_DATA_QUALITY 69.1%, THIN_PLAYER_HISTORY 58.7%, STALE_PLAYER_DATA 58.4%, STALE_KALSHI_QUOTE 50.3%, MODEL_INTERNAL_DISAGREEMENT 37.4%, ASYMMETRIC_SAMPLE_SIZE 31.8%, WIDE_SPREAD 24.3%, MODEL_HIGH_UNCERTAINTY 15.5%, PLAYER_IDENTITY_RISK 10.7%, LEVEL_TRANSFER_RISK 8.5%, LOW_DISPLAYED_LIQUIDITY 7.3%, EVENT_MAPPING_RISK 7.1%, MODEL_CALIBRATION_OUTLIER 2.8%, UNKNOWN 0.5%, EXTERNAL_MARKET_REJECTION 0.3%, EXTERNAL_MARKET_CONFIRMATION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 29.7%, POST_SETTLEMENT_OBSERVATION 27.5%, POSSIBLE_IN_PLAY_QUOTE 5.3%, CONFIRMED_IN_PLAY_QUOTE 0.7%

### >= ge_25 pp (N = 5,172)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,049 | 39.6% |
| STALE_QUOTE | market_freshness | 965 | 18.7% |
| BOOK_QUALITY | execution | 869 | 16.8% |
| POOR_DATA | data | 431 | 8.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 259 | 5.0% |
| LIMITED_DATA | data | 198 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 158 | 3.0% |
| IDENTITY_AMBIGUOUS | mapping | 128 | 2.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 111 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 4 | 0.1% |

Cause class: coverage 39.6%, market_freshness 18.7%, execution 16.8%, data 12.2%, market_freshness/coverage 8.1%, mapping 2.5%, model_calibration_or_unknown 2.1%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 98.0%, LOW_DATA_QUALITY 71.6%, THIN_PLAYER_HISTORY 60.5%, STALE_KALSHI_QUOTE 57.7%, STALE_PLAYER_DATA 54.1%, MODEL_INTERNAL_DISAGREEMENT 39.5%, ASYMMETRIC_SAMPLE_SIZE 34.0%, WIDE_SPREAD 23.3%, MODEL_HIGH_UNCERTAINTY 16.8%, PLAYER_IDENTITY_RISK 13.2%, EVENT_MAPPING_RISK 8.0%, LOW_DISPLAYED_LIQUIDITY 7.7%, LEVEL_TRANSFER_RISK 7.4%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 0.1%, UNKNOWN 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 42.1%, POST_SETTLEMENT_OBSERVATION 39.6%, POSSIBLE_IN_PLAY_QUOTE 5.5%, CONFIRMED_IN_PLAY_QUOTE 0.8%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 4336, "IDENTITY_AMBIGUOUS": 836}; ticker orientation: {"VERIFIED": 5172}.

Checks: discipline:AMBIGUOUS 261, discipline:PASS 4911, identity_confidence:AMBIGUOUS 683, identity_confidence:PASS 4489, level_mapping:NA 273, level_mapping:PASS 4899, market_pair:AMBIGUOUS 192, market_pair:NA 122, market_pair:PASS 4858, model_complement:NA 90, model_complement:PASS 5082, namesake:PASS 5172, physical_match_id:NA 2170, physical_match_id:PASS 3002, player_ids:PASS 5172, same_pair_other_event:PASS 5172, ticker_orientation:PASS 5172

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,242 | 1.8% | 1.9% | 0.4% | {"market_freshness": 20, "execution": 3} | 5.63 | 0.1882 / 0.188 (99) | 22.4% | 0.2% | 6.2% | 1.5% |
| CHALLENGER | 3,462 | 19.3% | 6.8% | 12.9% | {"coverage": 413, "market_freshness": 107, "market_freshness/coverage": 78, "model_calibration_or_unknown": 41, "data": 25, "execution": 4, "model_calibration": 1} | 6.92 | 0.2224 / 0.2051 (808) | 47.9% | 5.2% | 1.5% | 23.8% |
| DOUBLES | 587 | 44.5% | 43.8% | 5.1% | {"market_freshness": 106, "execution": 81, "mapping": 48, "market_freshness/coverage": 19, "coverage": 7} | 22.7 | 0.31 / 0.2223 (180) | 39.9% | 0.0% | 100.0% | 8.7% |
| ITF_MEN | 6,784 | 25.1% | 17.4% | 32.9% | {"coverage": 678, "execution": 374, "market_freshness": 258, "data": 249, "market_freshness/coverage": 121, "mapping": 19, "model_calibration_or_unknown": 2} | 11.11 | 0.2108 / 0.1908 (1689) | 40.8% | 56.2% | 6.5% | 23.4% |
| ITF_WOMEN | 8,670 | 26.6% | 18.4% | 44.6% | {"coverage": 934, "market_freshness": 417, "execution": 390, "data": 331, "market_freshness/coverage": 158, "mapping": 55, "model_calibration_or_unknown": 22, "model_calibration": 2} | 12.27 | 0.2007 / 0.1912 (1829) | 42.1% | 59.9% | 10.5% | 23.5% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 956 | 8.3% | 7.1% | 1.5% | {"market_freshness": 34, "model_calibration_or_unknown": 16, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.35 | 0.2051 / 0.202 (141) | 34.8% | 2.2% | 1.3% | 3.4% |
| WTA125 | 762 | 15.5% | 11.2% | 2.3% | {"market_freshness/coverage": 31, "model_calibration_or_unknown": 28, "market_freshness": 21, "data": 13, "coverage": 12, "execution": 8, "mapping": 4, "model_calibration": 1} | 10.01 | 0.225 / 0.2099 (265) | 28.0% | 5.6% | 3.9% | 12.3% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 5 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 6 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 7 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 8 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 9 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 10 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 11 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 12 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 13 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 14 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 15 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 16 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 17 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 18 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 19 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 20 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 21 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 22 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 23 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 24 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 25 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 64 min (STALE); no external reference |
| 26 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 27 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 28 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 29 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 30 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 31 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 799 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 32 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 33 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 34 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 35 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 36 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 826 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 37 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 114 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 38 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 39 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 40 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 66 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 41 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 42 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 43 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 44 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 45 | `KXATPCHALLENGERMATCH-26OCT06BARSAM-SAM` | CHALLENGER | fair_v1 | 84% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 139 min (STALE); no external reference |
| 46 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 47 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 114 min (STALE); data LIMITED (grade B, thinner serve sample 2163.0, ratio 2.0); no external reference |
| 48 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 732 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 49 | `KXWTAMATCH-26OCT01YASCHW-CHW` | WTA | fair_v1 | 73% / 2% | +70 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 51 min (STALE); no external reference |
| 50 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9803, "by_level_share_of_ge_25pp": {"ATP": 0.0044, "CHALLENGER": 0.1294, "DOUBLES": 0.0505, "ITF_MEN": 0.3289, "ITF_WOMEN": 0.4464, "OTHER": 0.0023, "WTA": 0.0153, "WTA125": 0.0228}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5766, "share_primary_cause_market_settled_or_in_play": 0.4768, "share_primary_cause_stale_quote_only": 0.1866}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 5172, "identity_ambiguous_share": 0.1616, "ticker_orientation": {"VERIFIED": 5172}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 3002, "with_external": 38, "coverage": 0.0127, "external_status": {"EXTERNAL_STALE": 32, "AGREES_WITH_KALSHI": 6}, "triangulation": {"INSUFFICIENT_INPUTS": 32, "MODEL_LONE_OUTLIER": 6}, "share_external_agrees_with_kalshi": 0.1579, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 1360, "with_external": 38, "coverage": 0.0279, "external_status": {"EXTERNAL_STALE": 32, "AGREES_WITH_KALSHI": 6}, "triangulation": {"INSUFFICIENT_INPUTS": 32, "MODEL_LONE_OUTLIER": 6}, "share_external_agrees_with_kalshi": 0.1579, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 601.0, "median_sample_ratio": 2.35, "median_min_matches": 19.0, "median_max_days_since_last": 197.0, "share_severe_asymmetry": 0.1841, "data_status": {"POOR": 2759, "LIMITED": 1475, "ADEQUATE": 938}, "comparison_lt_10pp": {"median_thinner_serve_points": 1712.0, "median_sample_ratio": 1.77, "median_min_matches": 71.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 344, "model_minus_observed": 0.0698, "kalshi_minus_observed": -0.0619, "brier_diff_model_minus_kalshi": 0.0016}, "4-10x": {"n": 259, "model_minus_observed": 0.0516, "kalshi_minus_observed": -0.0878, "brier_diff_model_minus_kalshi": -0.0052}, "<2x": {"n": 736, "model_minus_observed": 0.0803, "kalshi_minus_observed": -0.047, "brier_diff_model_minus_kalshi": 0.0104}, ">=10x": {"n": 246, "model_minus_observed": 0.1014, "kalshi_minus_observed": -0.0747, "brier_diff_model_minus_kalshi": 0.0128}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 1585, "model": {"intercept": -0.597, "slope": 0.942, "slope_se": 0.065}, "kalshi_mid_same_rows": {"intercept": 0.239, "slope": 1.165, "slope_se": 0.074}, "mean_extremity_model": 0.1853, "mean_extremity_kalshi": 0.1668, "model_brier": 0.225, "kalshi_brier": 0.1999, "brier_diff_model_minus_kalshi": 0.0251, "brier_diff_se": 0.0048, "model_logloss": 0.6423, "kalshi_logloss": 0.5814}, "fair_v1": {"n": 1585, "model": {"intercept": -0.41, "slope": 1.165, "slope_se": 0.075}, "kalshi_mid_same_rows": {"intercept": 0.38, "slope": 1.247, "slope_se": 0.077}, "mean_extremity_model": 0.1687, "mean_extremity_kalshi": 0.1673, "model_brier": 0.2062, "kalshi_brier": 0.1999, "brier_diff_model_minus_kalshi": 0.0063, "brier_diff_se": 0.0039, "model_logloss": 0.5976, "kalshi_logloss": 0.5812}, "gen1_elo": {"n": 1585, "model": {"intercept": -0.379, "slope": 1.147, "slope_se": 0.073}, "kalshi_mid_same_rows": {"intercept": 0.389, "slope": 1.237, "slope_se": 0.076}, "mean_extremity_model": 0.1729, "mean_extremity_kalshi": 0.1675, "model_brier": 0.2048, "kalshi_brier": 0.1997, "brier_diff_model_minus_kalshi": 0.0051, "brier_diff_se": 0.0038, "model_logloss": 0.5959, "kalshi_logloss": 0.5806}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2546, "share_ge_15": 0.4406, "median_abs_gap": 13.09, "n": 11791}, "gen1_elo": {"share_ge_25": 0.2442, "share_ge_15": 0.4391, "median_abs_gap": 12.71, "n": 11791}, "gen1_sr": {"share_ge_25": 0.3055, "share_ge_15": 0.5228, "median_abs_gap": 15.85, "n": 11791}, "gen2": {"share_ge_25": 0.31, "share_ge_15": 0.5089, "median_abs_gap": 15.41, "n": 11791}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1515, "share_ge_15": 0.3434, "median_abs_gap": 10.55, "n": 8977}, "gen1_elo": {"share_ge_25": 0.1456, "share_ge_15": 0.3395, "median_abs_gap": 10.13, "n": 8977}, "gen1_sr": {"share_ge_25": 0.2033, "share_ge_15": 0.4354, "median_abs_gap": 12.98, "n": 8977}, "gen2": {"share_ge_25": 0.2219, "share_ge_15": 0.432, "median_abs_gap": 12.77, "n": 8977}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.63, "share_ge_25_all": 0.0185, "share_ge_25_pregame_clean": 0.0188}, "WTA": {"median_abs_gap_pregame_clean": 8.35, "share_ge_25_all": 0.0826, "share_ge_25_pregame_clean": 0.0714}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2311, "share_within_10pp_all": 0.4286, "share_within_10pp_pregame_clean": 0.4924, "corr_model_vs_mid_pregame_clean": 0.8471}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 234, "model_brier": 0.18, "kalshi_brier": 0.181, "brier_diff_model_minus_kalshi": -0.0009}, "10-15": {"n_settled": 274, "model_brier": 0.2191, "kalshi_brier": 0.2178, "brier_diff_model_minus_kalshi": 0.0013}, "15-25": {"n_settled": 341, "model_brier": 0.2171, "kalshi_brier": 0.2108, "brier_diff_model_minus_kalshi": 0.0063}, "25-40": {"n_settled": 199, "model_brier": 0.212, "kalshi_brier": 0.1975, "brier_diff_model_minus_kalshi": 0.0145}, "3-5": {"n_settled": 162, "model_brier": 0.1808, "kalshi_brier": 0.1816, "brier_diff_model_minus_kalshi": -0.0008}, "40+": {"n_settled": 48, "model_brier": 0.2891, "kalshi_brier": 0.1739, "brier_diff_model_minus_kalshi": 0.1152}, "5-10": {"n_settled": 327, "model_brier": 0.1997, "kalshi_brier": 0.2014, "brier_diff_model_minus_kalshi": -0.0017}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%)
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap).
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 180, "model_brier": 0.31, "kalshi_brier": 0.2223, "brier_diff_model_minus_kalshi": 0.0877, "brier_diff_se": 0.0237, "corr_model_outcome": -0.0064, "corr_kalshi_outcome": 0.369}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
