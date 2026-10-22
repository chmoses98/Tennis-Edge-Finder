# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-22T05:57Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 48,794): 0-3 14.0%, 3-5 9.4%, 5-10 19.7%, 10-15 15.2%, 15-25 19.4%, 25-40 14.1%, 40+ 8.1%; median gap 12.14 pp.
* **Where the extremes live**: 97.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.6%, Challenger 12.0%, doubles 6.8%). Main tour: ATP 4.9% and WTA 4.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 10,814): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.5%, BOOK_QUALITY 18.4%, STALE_QUOTE 18.4%, POOR_DATA 8.9%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.5%, LIMITED_DATA 3.6%, IN_PLAY_QUOTE 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%. By class: coverage 34.5%, execution 18.4%, market_freshness 18.4%, data 12.5%, market_freshness/coverage 8.9%, mapping 4.5%, model_calibration_or_unknown 2.1%, model_calibration 0.7%.
* **Stale / settled / in-play**: 52.0% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.4% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 10,814 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.9% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.9% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 480.0 points vs 1667.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.045, Gen-2 0.847, Gen-1 ledger 0.869 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 526 model 0.2247 vs Kalshi 0.2102; n 104 model 0.2868 vs Kalshi 0.1908.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 209,283 model-market comparisons (340,861 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 70,223 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-22T05:44:38.343290+00:00'], shadow board 55,802 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-22T05:44:42.126315+00:00'], Model 4 26,243 rows, 18,678 settled tickers, 6,576 tickers with an external scan.
* By model: {"gen1_ledger": 47474, "gen1_elo": 28061, "fair_v1": 28061, "gen2": 28061, "gen1_sr": 28061, "model4_fundamental": 24796, "model4_conditioned": 24769}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 48,794 | 14.0 | 9.4 | 19.7 | 15.2 | 19.4 | 14.1 | 8.1 | 12.14 | 41.6% | 22.2% |
| MW fair_v1 | 28,061 | 12.9 | 8.5 | 18.4 | 15.6 | 20.0 | 14.9 | 9.7 | 13.21 | 44.6% | 24.7% |
| MW gen1_elo | 28,061 | 12.9 | 8.6 | 18.9 | 15.2 | 20.1 | 15.0 | 9.4 | 13.01 | 44.5% | 24.4% |
| MW gen1_ledger | 20,733 | 15.5 | 10.7 | 21.5 | 14.8 | 18.7 | 12.8 | 5.9 | 10.58 | 37.5% | 18.8% |
| MW gen1_sr | 28,061 | 9.9 | 7.0 | 16.5 | 13.8 | 21.2 | 18.8 | 12.7 | 16.08 | 52.7% | 31.5% |
| MW gen2 | 28,061 | 10.9 | 7.2 | 16.2 | 14.1 | 19.7 | 17.9 | 13.8 | 15.64 | 51.5% | 31.8% |
| all families model4_conditioned | 24,769 | 21.7 | 19.1 | 34.6 | 17.7 | 4.4 | 1.4 | 1.0 | 5.96 | 6.9% | 2.5% |
| all families model4_fundamental | 24,796 | 16.6 | 13.2 | 34.0 | 20.4 | 10.9 | 3.5 | 1.3 | 7.83 | 15.8% | 4.8% |

Configurable thresholds (primary): >=5pp 76.5%, >=10pp 56.9%, >=15pp 41.6%, >=20pp 30.9%, >=25pp 22.2%, >=30pp 15.9%, >=40pp 8.1%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.49pp; >=10pp 45.5%, >=25pp 17.2%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,408 | 28.9 | 14.0 | 24.4 | 14.7 | 12.2 | 5.1 | 0.8 | 6.17 | 18.0% | 5.8% |
| CHALLENGER | 4,443 | 15.8 | 10.0 | 20.4 | 15.6 | 14.8 | 12.4 | 10.9 | 11.09 | 38.1% | 23.3% |
| ITF_MEN | 7,691 | 10.4 | 7.5 | 17.0 | 14.7 | 21.6 | 17.1 | 11.8 | 15.15 | 50.4% | 28.9% |
| ITF_WOMEN | 11,203 | 9.4 | 6.9 | 15.8 | 15.4 | 22.7 | 18.2 | 11.5 | 15.82 | 52.5% | 29.8% |
| WTA | 1,656 | 17.0 | 13.0 | 25.5 | 19.9 | 19.4 | 4.5 | 0.7 | 8.43 | 24.6% | 5.2% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,408 | 23.7 | 14.9 | 25.0 | 17.0 | 13.5 | 5.0 | 1.0 | 6.58 | 19.5% | 6.0% |
| CHALLENGER | 4,443 | 14.8 | 8.6 | 18.7 | 14.8 | 17.4 | 13.9 | 11.8 | 12.54 | 43.2% | 25.7% |
| ITF_MEN | 7,691 | 8.5 | 6.1 | 14.5 | 13.1 | 19.8 | 20.6 | 17.4 | 18.43 | 57.8% | 38.0% |
| ITF_WOMEN | 11,203 | 8.0 | 5.6 | 13.8 | 13.4 | 20.9 | 21.1 | 17.1 | 18.93 | 59.1% | 38.2% |
| WTA | 1,656 | 14.4 | 9.9 | 21.3 | 16.4 | 23.7 | 13.7 | 0.7 | 11.18 | 38.1% | 14.4% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,408 | 24.4 | 12.8 | 24.0 | 15.9 | 14.8 | 6.9 | 1.2 | 7.3 | 23.0% | 8.1% |
| CHALLENGER | 4,443 | 14.4 | 9.4 | 20.8 | 15.2 | 16.3 | 12.8 | 11.2 | 11.42 | 40.3% | 23.9% |
| ITF_MEN | 7,691 | 10.0 | 7.5 | 17.1 | 14.1 | 22.1 | 17.4 | 11.9 | 15.51 | 51.4% | 29.3% |
| ITF_WOMEN | 11,203 | 9.5 | 6.6 | 16.2 | 15.6 | 23.1 | 18.3 | 10.7 | 15.71 | 52.1% | 29.0% |
| WTA | 1,656 | 24.3 | 16.9 | 29.6 | 16.2 | 10.2 | 2.4 | 0.4 | 6.02 | 13.0% | 2.8% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,379 | 25.6 | 19.6 | 30.6 | 11.8 | 9.0 | 3.0 | 0.4 | 5.5 | 12.4% | 3.4% |
| CHALLENGER | 3,069 | 21.4 | 14.8 | 26.6 | 14.0 | 14.7 | 6.6 | 1.9 | 7.27 | 23.1% | 8.4% |
| DOUBLES | 1,534 | 5.3 | 4.2 | 11.5 | 10.2 | 21.0 | 26.4 | 21.5 | 24.05 | 68.9% | 47.9% |
| ITF_MEN | 5,895 | 13.9 | 8.8 | 20.1 | 16.0 | 21.3 | 13.3 | 6.6 | 12.14 | 41.1% | 19.9% |
| ITF_WOMEN | 6,947 | 12.7 | 9.0 | 19.3 | 15.1 | 21.6 | 16.3 | 6.1 | 12.87 | 44.0% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,028 | 22.3 | 15.9 | 29.6 | 18.2 | 10.1 | 3.6 | 0.3 | 6.97 | 14.0% | 3.9% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,343 | 29.3 | 14.2 | 24.8 | 14.6 | 11.9 | 4.7 | 0.5 | 5.98 | 17.1% | 5.2% |
| CHALLENGER | 3,146 | 20.6 | 12.3 | 25.2 | 18.1 | 15.2 | 6.6 | 2.0 | 8.34 | 23.8% | 8.6% |
| ITF_MEN | 5,678 | 12.6 | 9.0 | 20.3 | 16.5 | 22.6 | 14.0 | 5.0 | 12.37 | 41.6% | 19.0% |
| ITF_WOMEN | 8,375 | 11.2 | 8.2 | 18.0 | 17.5 | 24.7 | 15.4 | 5.1 | 13.53 | 45.1% | 20.4% |
| WTA | 1,608 | 17.2 | 12.9 | 25.6 | 20.1 | 19.3 | 4.2 | 0.7 | 8.39 | 24.2% | 4.9% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,343 | 24.0 | 15.2 | 25.1 | 16.8 | 13.5 | 4.7 | 0.6 | 6.48 | 18.8% | 5.3% |
| CHALLENGER | 3,146 | 18.7 | 10.9 | 23.2 | 17.7 | 17.6 | 9.6 | 2.2 | 9.23 | 29.5% | 11.9% |
| ITF_MEN | 5,679 | 10.1 | 7.3 | 16.7 | 14.9 | 21.5 | 19.1 | 10.4 | 15.45 | 51.0% | 29.5% |
| ITF_WOMEN | 8,376 | 9.0 | 6.5 | 15.2 | 15.0 | 23.0 | 20.6 | 10.7 | 16.61 | 54.3% | 31.3% |
| WTA | 1,608 | 14.4 | 9.9 | 21.3 | 16.3 | 23.7 | 13.6 | 0.8 | 11.18 | 38.1% | 14.4% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,337 | 25.8 | 19.8 | 30.7 | 12.0 | 8.5 | 2.9 | 0.2 | 5.4 | 11.7% | 3.1% |
| CHALLENGER | 2,674 | 22.9 | 15.9 | 28.2 | 13.9 | 14.1 | 4.5 | 0.6 | 6.68 | 19.1% | 5.0% |
| DOUBLES | 1,426 | 5.3 | 4.3 | 11.7 | 10.4 | 20.9 | 26.4 | 21.0 | 23.88 | 68.3% | 47.4% |
| ITF_MEN | 4,931 | 15.1 | 9.5 | 21.8 | 16.8 | 21.1 | 11.6 | 4.0 | 11.13 | 36.8% | 15.7% |
| ITF_WOMEN | 5,763 | 13.6 | 9.5 | 20.7 | 15.9 | 21.8 | 15.1 | 3.4 | 11.71 | 40.3% | 18.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 978 | 22.8 | 16.5 | 29.6 | 18.2 | 10.1 | 2.9 | 0.0 | 6.82 | 13.0% | 2.9% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,534 | 5.3 | 4.2 | 11.5 | 10.2 | 21.0 | 26.4 | 21.5 | 24.05 | 68.9% | 47.9% |
| singles | 19,199 | 16.3 | 11.2 | 22.3 | 15.2 | 18.5 | 11.8 | 4.7 | 10.03 | 35.0% | 16.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 6,274 | 13.2 | 8.8 | 19.0 | 15.6 | 18.9 | 14.9 | 9.5 | 12.92 | 43.4% | 24.4% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 17,480 | 13.3 | 8.6 | 18.4 | 15.2 | 20.1 | 14.7 | 9.7 | 13.17 | 44.5% | 24.4% |
| UNKNOWN | 4,070 | 11.0 | 7.8 | 17.2 | 16.9 | 20.8 | 15.9 | 10.4 | 13.85 | 47.1% | 26.3% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,804 | 19.7 | 11.7 | 21.3 | 16.4 | 15.7 | 8.9 | 6.2 | 9.19 | 30.9% | 15.1% |
| B | 3,506 | 12.6 | 9.0 | 19.8 | 16.6 | 19.4 | 12.2 | 10.4 | 12.39 | 42.0% | 22.6% |
| C | 3,957 | 11.6 | 8.9 | 19.6 | 14.9 | 19.5 | 15.2 | 10.4 | 13.24 | 45.1% | 25.6% |
| D | 4,535 | 12.2 | 7.8 | 17.2 | 15.6 | 21.6 | 15.7 | 10.0 | 13.98 | 47.3% | 25.7% |
| F | 8,259 | 7.7 | 5.6 | 15.1 | 14.6 | 23.5 | 21.3 | 12.3 | 17.78 | 57.1% | 33.6% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,804 | 23.0 | 15.9 | 28.8 | 15.0 | 11.7 | 4.1 | 1.5 | 6.65 | 17.3% | 5.5% |
| B | 2,843 | 16.3 | 10.4 | 23.4 | 16.0 | 19.3 | 10.7 | 3.9 | 9.99 | 33.8% | 14.6% |
| C | 4,090 | 11.3 | 7.4 | 18.4 | 14.2 | 21.5 | 16.6 | 10.7 | 14.36 | 48.8% | 27.3% |
| D | 2,950 | 14.6 | 9.8 | 19.9 | 14.4 | 21.0 | 14.3 | 6.1 | 12.03 | 41.4% | 20.4% |
| F | 5,046 | 10.2 | 8.1 | 15.5 | 14.8 | 22.9 | 20.2 | 8.2 | 15.68 | 51.3% | 28.5% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 8,940 | 17.9 | 10.5 | 20.5 | 16.4 | 16.4 | 9.8 | 8.6 | 10.34 | 34.7% | 18.4% |
| LIMITED | 6,048 | 13.4 | 10.2 | 20.4 | 15.6 | 19.2 | 13.6 | 7.6 | 11.9 | 40.4% | 21.2% |
| POOR | 13,073 | 9.3 | 6.4 | 15.9 | 15.0 | 22.8 | 19.1 | 11.4 | 16.14 | 53.3% | 30.6% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,327 | 26.4 | 20.4 | 34.2 | 12.5 | 4.8 | 1.4 | 0.2 | 5.33 | 6.4% | 1.6% |
| GAME_SPREAD | 4,550 | 22.4 | 15.2 | 33.5 | 17.2 | 9.0 | 2.3 | 0.3 | 6.69 | 11.7% | 2.6% |
| MATCH_WINNER | 20,733 | 15.5 | 10.7 | 21.5 | 14.8 | 18.7 | 12.8 | 5.9 | 10.58 | 37.5% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 9,551 | 29.4 | 16.9 | 31.0 | 12.5 | 8.2 | 1.7 | 0.4 | 5.47 | 10.2% | 2.1% |
| TOTAL_GAMES | 7,289 | 8.4 | 9.6 | 36.5 | 29.0 | 10.6 | 3.2 | 2.7 | 9.51 | 16.6% | 5.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,654 | 25.4 | 34.0 | 32.5 | 4.4 | 3.0 | 0.5 | 0.2 | 4.48 | 3.7% | 0.7% |
| GAME_SPREAD | 5,937 | 45.5 | 17.0 | 27.0 | 7.7 | 1.8 | 0.8 | 0.3 | 3.48 | 2.9% | 1.1% |
| TOTAL_GAMES | 10,178 | 4.8 | 7.7 | 40.7 | 34.9 | 7.1 | 2.5 | 2.2 | 9.67 | 11.9% | 4.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,657 | 24.2 | 17.9 | 35.4 | 12.6 | 7.1 | 2.5 | 0.3 | 5.81 | 9.9% | 2.8% |
| GAME_SPREAD | 5,940 | 19.4 | 13.3 | 28.1 | 20.1 | 13.8 | 4.5 | 0.9 | 7.96 | 19.1% | 5.3% |
| TOTAL_GAMES | 10,199 | 8.4 | 9.2 | 36.4 | 27.3 | 12.6 | 3.8 | 2.4 | 9.52 | 18.7% | 6.2% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 28,061 | 44.6% | 24.7% | 13.21 | 36.3% | 15.4% | 10.98 |
| gen1_elo | 28,061 | 44.5% | 24.4% | 13.01 | 35.9% | 15.6% | 10.69 |
| gen1_sr | 28,061 | 52.7% | 31.5% | 16.08 | 45.1% | 22.3% | 13.31 |
| gen2 | 28,061 | 51.5% | 31.8% | 15.64 | 44.8% | 23.9% | 13.2 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 14,279 | 15.8 | 10.3 | 21.1 | 17.1 | 20.4 | 11.9 | 3.3 | 10.8 | 35.6% | 15.2% |
| STALE | 13,782 | 9.9 | 6.7 | 15.6 | 13.9 | 19.5 | 18.1 | 16.4 | 16.9 | 53.9% | 34.5% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 14,201 | 16.5 | 11.2 | 22.3 | 14.9 | 17.9 | 12.3 | 4.8 | 9.98 | 35.0% | 17.1% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 48,794 | 14201 | 17751 | 16842 | 24.0 | 135.7 | 1400.4 |
| ge_15pp | 20,298 | 4974 | 6379 | 8945 | 25.8 | 432.7 | 1380.4 |
| ge_25pp | 10,814 | 2431 | 2761 | 5622 | 31.6 | 574.8 | 1380.4 |
| lt_10pp | 21,053 | 7113 | 8372 | 5568 | 21.8 | 47.5 | 1341.5 |

Current slate `SL-20261022T055753Z-72f19dea`: 586 priced rows, quote age at build {'median': 13.5, 'max': 13.6}, freshness {'AGING': 586}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 22 | 0.0 | 0.0 | 22.7 | 4.5 | 40.9 | 31.8 | 0.0 | 20.48 | 72.7% | 31.8% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,588 | 19.5 | 10.9 | 23.8 | 18.6 | 19.1 | 7.4 | 0.7 | 9.12 | 27.2% | 8.1% |
| KALSHI_LONE_OUTLIER | 17 | 5.9 | 5.9 | 76.5 | 0.0 | 5.9 | 5.9 | 0.0 | 6.11 | 11.8% | 5.9% |
| MARKETS_AGREE | 500 | 66.0 | 34.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.25 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,096 | 0.0 | 2.2 | 34.9 | 25.7 | 25.6 | 10.9 | 0.8 | 12.59 | 37.2% | 11.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 28,061 | 4235 (15.1%) | 25.9% | 0.9% | {"EXTERNAL_STALE": 2588, "AGREES_WITH_KALSHI": 1096, "ALL_AGREE": 500, "SUPPORTS_MODEL_DIRECTION": 21, "AGREES_WITH_MODEL": 17, "EXTERNAL_OUTLIER": 12, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 12,525 | 1130 (9.0%) | 36.1% | 1.6% | {"EXTERNAL_STALE": 704, "AGREES_WITH_KALSHI": 408, "SUPPORTS_MODEL_DIRECTION": 16, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 6,921 | 346 (5.0%) | 37.0% | 2.3% | {"EXTERNAL_STALE": 210, "AGREES_WITH_KALSHI": 128, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,358 | 323 (9.6%) | 37.5% | 2.5% | {"EXTERNAL_STALE": 194, "AGREES_WITH_KALSHI": 121, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 11,171 | 2340 (20.9%) | 17.3% | 0.8% | {"EXTERNAL_STALE": 1402, "ALL_AGREE": 500, "AGREES_WITH_KALSHI": 406, "AGREES_WITH_MODEL": 15, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 4, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,344 | 10.5 | 7.6 | 19.3 | 14.3 | 22.4 | 15.9 | 10.0 | 14.12 | 48.3% | 25.9% |
| 4-10x | 3,677 | 10.9 | 8.4 | 19.0 | 15.3 | 21.3 | 14.8 | 10.2 | 13.76 | 46.3% | 25.0% |
| <2x | 14,234 | 14.9 | 9.6 | 18.9 | 16.6 | 18.1 | 13.2 | 8.8 | 11.97 | 40.1% | 22.0% |
| >=10x | 4,806 | 11.2 | 6.4 | 15.4 | 14.1 | 21.9 | 19.3 | 11.7 | 16.09 | 52.8% | 31.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 7,057 | 12.3 | 8.5 | 19.4 | 16.2 | 19.8 | 13.5 | 10.4 | 12.99 | 43.6% | 23.8% |
| 300-1000 | 6,086 | 11.6 | 8.7 | 17.2 | 15.2 | 20.8 | 16.4 | 10.1 | 14.0 | 47.3% | 26.5% |
| <300 | 9,210 | 8.9 | 5.7 | 15.5 | 14.8 | 23.0 | 20.0 | 12.1 | 16.85 | 55.1% | 32.1% |
| >=3000 | 5,708 | 21.6 | 12.9 | 22.9 | 16.4 | 14.4 | 7.0 | 4.8 | 8.01 | 26.2% | 11.7% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 803 | 0.5469 | 0.4093 | 0.5006 | +0.046 | -0.091 | -0.004 ± 0.0054 |
| ratio 4-10x | 554 | 0.5839 | 0.4376 | 0.4874 | +0.097 | -0.050 | 0.0145 ± 0.0069 |
| ratio <2x | 1981 | 0.5366 | 0.4122 | 0.4472 | +0.089 | -0.035 | 0.0121 ± 0.0032 |
| ratio >=10x | 712 | 0.5671 | 0.3911 | 0.4579 | +0.109 | -0.067 | 0.0073 ± 0.0069 |
| thinner_sample 1000-3000 | 1096 | 0.5426 | 0.4143 | 0.4498 | +0.093 | -0.035 | 0.0105 ± 0.0044 |
| thinner_sample 300-1000 | 941 | 0.5634 | 0.4205 | 0.492 | +0.071 | -0.072 | 0.0005 ± 0.0053 |
| thinner_sample <300 | 1349 | 0.5558 | 0.3892 | 0.4596 | +0.096 | -0.070 | 0.0098 ± 0.0048 |
| thinner_sample >=3000 | 664 | 0.5343 | 0.4388 | 0.4639 | +0.070 | -0.025 | 0.0131 ± 0.0046 |
| data_status ADEQUATE | 1146 | 0.5378 | 0.4312 | 0.452 | +0.086 | -0.021 | 0.0127 ± 0.0037 |
| data_status LIMITED | 958 | 0.5486 | 0.4156 | 0.4791 | +0.070 | -0.064 | 0.0039 ± 0.0048 |
| data_status POOR | 1946 | 0.5589 | 0.3977 | 0.4661 | +0.093 | -0.068 | 0.0081 ± 0.0039 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 592 | 0.1985 | 0.1996 | -0.0011 ± 0.0006 | 0.5765 | 0.5787 | 0.4989 | 0.4841 | 0.5304 | -0.058 ± 0.0191 | -0.01 (5) |
| 3-5 | 377 | 0.2022 | 0.2016 | +0.0006 ± 0.0019 | 0.588 | 0.5848 | 0.5004 | 0.4603 | 0.4721 | -0.095 ± 0.0238 | 0.02 (1) |
| 5-10 | 822 | 0.2023 | 0.2018 | +0.0005 ± 0.0024 | 0.5906 | 0.587 | 0.5114 | 0.4369 | 0.4659 | -0.090 ± 0.0163 | -0.0167 (6) |
| 10-15 | 701 | 0.2124 | 0.2035 | +0.0089 ± 0.0043 | 0.6142 | 0.5882 | 0.5245 | 0.4004 | 0.4251 | -0.101 ± 0.017 | -0.048 (5) |
| 15-25 | 928 | 0.2242 | 0.2133 | +0.0109 ± 0.0059 | 0.6433 | 0.6103 | 0.5762 | 0.3803 | 0.4504 | -0.088 ± 0.015 | -0.0033 (9) |
| 25-40 | 526 | 0.2247 | 0.2102 | +0.0145 ± 0.0119 | 0.6376 | 0.6043 | 0.655 | 0.3454 | 0.4734 | -0.073 ± 0.0183 | -0.01 (1) |
| 40+ | 104 | 0.2868 | 0.1908 | +0.0961 ± 0.0376 | 0.7842 | 0.5653 | 0.7516 | 0.3041 | 0.4231 | -0.092 ± 0.0368 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3010 | 0.1845 | 0.1854 | -0.0009 ± 0.0003 | 0.5441 | 0.5448 | 0.4858 | 0.4708 | 0.5056 | -0.021 ± 0.0079 | -0.0129 (17) |
| 3-5 | 1989 | 0.1985 | 0.1973 | +0.0012 ± 0.0008 | 0.5776 | 0.5715 | 0.4825 | 0.4426 | 0.447 | -0.052 ± 0.0101 | 0.0 (2) |
| 5-10 | 4232 | 0.1979 | 0.1949 | +0.0030 ± 0.001 | 0.5784 | 0.5687 | 0.4806 | 0.4065 | 0.4227 | -0.046 ± 0.0069 | -0.0119 (21) |
| 10-15 | 3677 | 0.1997 | 0.1819 | +0.0178 ± 0.0018 | 0.5858 | 0.5355 | 0.4846 | 0.36 | 0.3506 | -0.073 ± 0.007 | -0.0281 (16) |
| 15-25 | 4647 | 0.2072 | 0.1695 | +0.0377 ± 0.0024 | 0.6077 | 0.5018 | 0.5022 | 0.3057 | 0.3088 | -0.070 ± 0.006 | -0.0025 (44) |
| 25-40 | 3634 | 0.2245 | 0.1332 | +0.0913 ± 0.0038 | 0.6436 | 0.4052 | 0.5322 | 0.2196 | 0.2331 | -0.057 ± 0.0059 | -0.01 (1) |
| 40+ | 2356 | 0.3808 | 0.0439 | +0.3368 ± 0.0049 | 0.9911 | 0.1721 | 0.6317 | 0.1063 | 0.0607 | -0.081 ± 0.004 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 447 | 0.2037 | 0.2041 | -0.0004 ± 0.0007 | 0.5895 | 0.5903 | 0.5043 | 0.4894 | 0.5034 | -0.107 ± 0.023 | -0.01 (3) |
| 3-5 | 332 | 0.2206 | 0.2192 | +0.0014 ± 0.0021 | 0.6263 | 0.6236 | 0.5134 | 0.4734 | 0.4699 | -0.111 ± 0.0275 | 0.02 (1) |
| 5-10 | 712 | 0.2039 | 0.204 | -0.0002 ± 0.0025 | 0.5924 | 0.5924 | 0.5447 | 0.4699 | 0.5098 | -0.076 ± 0.0174 | -0.01 (4) |
| 10-15 | 671 | 0.2161 | 0.2093 | +0.0068 ± 0.0044 | 0.622 | 0.6045 | 0.5629 | 0.4386 | 0.4754 | -0.103 ± 0.0183 | -0.04 (5) |
| 15-25 | 961 | 0.2296 | 0.2093 | +0.0204 ± 0.0058 | 0.6522 | 0.6006 | 0.5889 | 0.3928 | 0.4433 | -0.100 ± 0.015 | -0.0133 (9) |
| 25-40 | 674 | 0.2619 | 0.2008 | +0.0611 ± 0.0109 | 0.731 | 0.5832 | 0.6559 | 0.3404 | 0.4036 | -0.108 ± 0.0169 | -0.0075 (4) |
| 40+ | 253 | 0.3601 | 0.1735 | +0.1866 ± 0.0259 | 0.9931 | 0.5189 | 0.733 | 0.2492 | 0.3123 | -0.073 ± 0.0251 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2526 | 0.1948 | 0.1949 | -0.0001 ± 0.0003 | 0.5672 | 0.5672 | 0.5081 | 0.4933 | 0.5055 | -0.046 ± 0.0091 | -0.0133 (15) |
| 3-5 | 1705 | 0.2002 | 0.2 | +0.0003 ± 0.0009 | 0.5788 | 0.5775 | 0.511 | 0.471 | 0.4862 | -0.039 ± 0.0111 | 0.02 (1) |
| 5-10 | 3749 | 0.1934 | 0.1926 | +0.0009 ± 0.0011 | 0.5692 | 0.5632 | 0.5037 | 0.4297 | 0.4628 | -0.028 ± 0.0073 | -0.0117 (6) |
| 10-15 | 3328 | 0.199 | 0.1874 | +0.0116 ± 0.0019 | 0.5849 | 0.5474 | 0.5129 | 0.3889 | 0.4056 | -0.053 ± 0.0076 | -0.0189 (18) |
| 15-25 | 4691 | 0.2158 | 0.1778 | +0.0380 ± 0.0024 | 0.6276 | 0.5226 | 0.5253 | 0.3292 | 0.3338 | -0.069 ± 0.0062 | -0.0086 (42) |
| 25-40 | 4223 | 0.251 | 0.1411 | +0.1099 ± 0.0037 | 0.7072 | 0.4303 | 0.5605 | 0.2437 | 0.2314 | -0.079 ± 0.0057 | -0.0044 (18) |
| 40+ | 3323 | 0.3967 | 0.0629 | +0.3337 ± 0.005 | 1.0448 | 0.2232 | 0.6545 | 0.1208 | 0.0882 | -0.071 ± 0.0042 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 566 | 0.1984 | 0.2008 | -0.0024 ± 0.0007 | 0.5768 | 0.5825 | 0.4962 | 0.4809 | 0.5548 | -0.015 ± 0.0192 | -0.0137 (8) |
| 3-5 | 407 | 0.1997 | 0.1976 | +0.0021 ± 0.0018 | 0.5798 | 0.5744 | 0.5038 | 0.4641 | 0.4595 | -0.120 ± 0.0229 | 0.0067 (3) |
| 5-10 | 851 | 0.2011 | 0.1978 | +0.0033 ± 0.0023 | 0.5889 | 0.5772 | 0.5092 | 0.4352 | 0.4477 | -0.099 ± 0.0157 | -0.0071 (7) |
| 10-15 | 704 | 0.2079 | 0.205 | +0.0029 ± 0.0042 | 0.6032 | 0.5923 | 0.5379 | 0.4144 | 0.4659 | -0.083 ± 0.0169 | -0.0317 (6) |
| 15-25 | 868 | 0.232 | 0.2122 | +0.0197 ± 0.0061 | 0.6625 | 0.6076 | 0.5852 | 0.3911 | 0.4366 | -0.113 ± 0.0156 | -0.03 (1) |
| 25-40 | 544 | 0.2126 | 0.2175 | -0.0049 ± 0.0117 | 0.6126 | 0.6211 | 0.6653 | 0.3538 | 0.5147 | -0.049 ± 0.0179 | 0.015 (2) |
| 40+ | 110 | 0.3006 | 0.2046 | +0.0960 ± 0.0379 | 0.8265 | 0.5957 | 0.7598 | 0.3102 | 0.4364 | -0.083 ± 0.0397 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2941 | 0.1883 | 0.189 | -0.0007 ± 0.0003 | 0.5518 | 0.5529 | 0.4895 | 0.4743 | 0.491 | -0.035 ± 0.0081 | -0.0163 (35) |
| 3-5 | 2005 | 0.1922 | 0.1897 | +0.0025 ± 0.0008 | 0.5638 | 0.5572 | 0.4849 | 0.4454 | 0.4349 | -0.070 ± 0.01 | -0.0094 (18) |
| 5-10 | 4370 | 0.1957 | 0.1898 | +0.0059 ± 0.001 | 0.5757 | 0.556 | 0.4853 | 0.4114 | 0.4082 | -0.062 ± 0.0066 | -0.01 (31) |
| 10-15 | 3531 | 0.1935 | 0.1776 | +0.0160 ± 0.0018 | 0.5708 | 0.5239 | 0.4978 | 0.3742 | 0.3713 | -0.068 ± 0.0071 | -0.015 (12) |
| 15-25 | 4786 | 0.2105 | 0.1719 | +0.0386 ± 0.0023 | 0.6151 | 0.5076 | 0.5106 | 0.3156 | 0.3142 | -0.073 ± 0.006 | -0.03 (2) |
| 25-40 | 3615 | 0.2195 | 0.1357 | +0.0837 ± 0.0039 | 0.633 | 0.4107 | 0.5367 | 0.2208 | 0.2479 | -0.047 ± 0.0059 | 0.01 (3) |
| 40+ | 2297 | 0.3948 | 0.0492 | +0.3456 ± 0.0053 | 1.0315 | 0.1856 | 0.6439 | 0.1129 | 0.0666 | -0.083 ± 0.0044 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 939 | 0.1948 | 0.1951 | -0.0002 ± 0.0005 | 0.5687 | 0.5689 | 0.5082 | 0.4931 | 0.4984 | -0.057 ± 0.0146 | -0.0224 (49) |
| 3-5 | 655 | 0.1913 | 0.1908 | +0.0005 ± 0.0014 | 0.5594 | 0.5572 | 0.4867 | 0.4469 | 0.458 | -0.053 ± 0.0173 | -0.0194 (34) |
| 5-10 | 1383 | 0.2005 | 0.194 | +0.0065 ± 0.0018 | 0.5903 | 0.57 | 0.4953 | 0.4219 | 0.4165 | -0.074 ± 0.0121 | -0.005 (78) |
| 10-15 | 907 | 0.2089 | 0.198 | +0.0109 ± 0.0037 | 0.6058 | 0.5778 | 0.5167 | 0.3935 | 0.409 | -0.065 ± 0.0151 | 0.0014 (64) |
| 15-25 | 1224 | 0.231 | 0.2101 | +0.0208 ± 0.0051 | 0.6597 | 0.6052 | 0.5728 | 0.378 | 0.4232 | -0.069 ± 0.0132 | -0.0214 (59) |
| 25-40 | 737 | 0.2486 | 0.2061 | +0.0425 ± 0.0103 | 0.7058 | 0.5931 | 0.6666 | 0.354 | 0.441 | -0.083 ± 0.0157 | -0.0219 (26) |
| 40+ | 252 | 0.3533 | 0.1959 | +0.1574 ± 0.0276 | 1.0198 | 0.5733 | 0.8064 | 0.3235 | 0.4206 | -0.094 ± 0.025 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3088 | 0.1832 | 0.1833 | -0.0002 ± 0.0003 | 0.5391 | 0.5387 | 0.5079 | 0.4926 | 0.5026 | -0.038 ± 0.0078 | -0.0157 (88) |
| 3-5 | 2125 | 0.192 | 0.1902 | +0.0018 ± 0.0008 | 0.5611 | 0.5571 | 0.4929 | 0.4532 | 0.4504 | -0.052 ± 0.0095 | -0.0209 (69) |
| 5-10 | 4295 | 0.1979 | 0.1892 | +0.0087 ± 0.001 | 0.5817 | 0.5562 | 0.4913 | 0.4177 | 0.3988 | -0.073 ± 0.0067 | -0.0082 (132) |
| 10-15 | 2954 | 0.2049 | 0.1897 | +0.0152 ± 0.002 | 0.5978 | 0.5577 | 0.5235 | 0.4004 | 0.3995 | -0.062 ± 0.008 | -0.0053 (105) |
| 15-25 | 3717 | 0.2284 | 0.1991 | +0.0293 ± 0.0029 | 0.6594 | 0.5776 | 0.5654 | 0.3699 | 0.3936 | -0.062 ± 0.0073 | -0.0253 (107) |
| 25-40 | 2557 | 0.2595 | 0.1831 | +0.0764 ± 0.0054 | 0.7357 | 0.5348 | 0.6281 | 0.3138 | 0.352 | -0.077 ± 0.0082 | -0.0229 (51) |
| 40+ | 1163 | 0.3773 | 0.1429 | +0.2344 ± 0.0117 | 1.071 | 0.4312 | 0.7284 | 0.2248 | 0.2562 | -0.072 ± 0.0104 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4050 | 1.045 ± 0.044 | 1.142 | 0.1678 | 0.1653 | 0.2136 | 0.2052 |
| gen2 | 4050 | 0.847 ± 0.041 | 1.101 | 0.17 | 0.1658 | 0.2328 | 0.2049 |
| gen1_elo | 4050 | 1.02 ± 0.043 | 1.131 | 0.1748 | 0.1654 | 0.2126 | 0.2054 |
| gen1_sr | 4050 | 1.043 ± 0.053 | 1.172 | 0.1306 | 0.1679 | 0.2289 | 0.2045 |
| gen1_ledger | 6097 | 0.869 ± 0.031 | 1.08 | 0.1822 | 0.1802 | 0.2181 | 0.1992 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 20,298)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,655 | 22.9% |
| STALE_QUOTE | market_freshness | 4,367 | 21.5% |
| BOOK_QUALITY | execution | 3,825 | 18.8% |
| POOR_DATA | data | 2,321 | 11.4% |
| LIMITED_DATA | data | 1,284 | 6.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,101 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 960 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 853 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 600 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 332 | 1.6% |

Cause class: coverage 22.9%, market_freshness 21.5%, execution 18.8%, data 17.8%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.7%, mapping 4.2%, model_calibration 1.6%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 94.3%, LOW_DATA_QUALITY 71.2%, THIN_PLAYER_HISTORY 60.0%, STALE_PLAYER_DATA 50.7%, STALE_KALSHI_QUOTE 44.1%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 33.3%, WIDE_SPREAD 25.0%, MODEL_HIGH_UNCERTAINTY 17.7%, PLAYER_IDENTITY_RISK 16.1%, LEVEL_TRANSFER_RISK 10.9%, EVENT_MAPPING_RISK 8.1%, LOW_DISPLAYED_LIQUIDITY 8.0%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.1%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.5%, POST_SETTLEMENT_OBSERVATION 22.9%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 10,814)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,732 | 34.5% |
| BOOK_QUALITY | execution | 1,990 | 18.4% |
| STALE_QUOTE | market_freshness | 1,987 | 18.4% |
| POOR_DATA | data | 962 | 8.9% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 588 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 486 | 4.5% |
| LIMITED_DATA | data | 391 | 3.6% |
| IN_PLAY_QUOTE | market_freshness/coverage | 377 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 226 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 75 | 0.7% |

Cause class: coverage 34.5%, execution 18.4%, market_freshness 18.4%, data 12.5%, market_freshness/coverage 8.9%, mapping 4.5%, model_calibration_or_unknown 2.1%, model_calibration 0.7%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.1%, LOW_DATA_QUALITY 75.0%, THIN_PLAYER_HISTORY 62.4%, STALE_KALSHI_QUOTE 52.0%, STALE_PLAYER_DATA 45.6%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 34.7%, WIDE_SPREAD 24.4%, PLAYER_IDENTITY_RISK 19.4%, MODEL_HIGH_UNCERTAINTY 17.9%, EVENT_MAPPING_RISK 9.7%, LEVEL_TRANSFER_RISK 9.7%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.6%, POST_SETTLEMENT_OBSERVATION 34.5%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 8444, "IDENTITY_AMBIGUOUS": 2370}; ticker orientation: {"VERIFIED": 10814}.

Checks: discipline:AMBIGUOUS 735, discipline:PASS 10079, identity_confidence:AMBIGUOUS 2099, identity_confidence:PASS 8715, level_mapping:NA 747, level_mapping:PASS 10067, market_pair:AMBIGUOUS 381, market_pair:NA 269, market_pair:PASS 10164, model_complement:NA 236, model_complement:PASS 10578, namesake:PASS 10814, physical_match_id:NA 3893, physical_match_id:PASS 6921, player_ids:PASS 10814, same_pair_other_event:PASS 10814, ticker_orientation:PASS 10814

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,787 | 4.9% | 4.4% | 1.7% | {"market_freshness": 53, "model_calibration_or_unknown": 43, "data": 35, "execution": 19, "market_freshness/coverage": 13, "model_calibration": 13, "coverage": 11} | 5.84 | 0.224 / 0.2168 (429) | 19.1% | 3.9% | 3.3% | 2.8% |
| CHALLENGER | 7,512 | 17.2% | 7.0% | 12.0% | {"coverage": 730, "market_freshness/coverage": 161, "market_freshness": 147, "data": 128, "model_calibration_or_unknown": 58, "execution": 30, "model_calibration": 27, "mapping": 15} | 7.42 | 0.2176 / 0.2067 (1802) | 35.1% | 17.4% | 3.9% | 22.5% |
| DOUBLES | 1,534 | 47.9% | 47.4% | 6.8% | {"execution": 377, "mapping": 193, "market_freshness": 106, "market_freshness/coverage": 52, "coverage": 7} | 23.88 | 0.3147 / 0.2359 (389) | 15.2% | 0.0% | 100.0% | 7.0% |
| ITF_MEN | 13,586 | 25.0% | 17.5% | 31.4% | {"coverage": 1252, "execution": 665, "market_freshness": 566, "data": 458, "market_freshness/coverage": 287, "mapping": 161, "model_calibration_or_unknown": 2, "model_calibration": 1} | 11.78 | 0.2141 / 0.1959 (3011) | 37.3% | 68.7% | 18.9% | 21.9% |
| ITF_WOMEN | 18,150 | 27.0% | 19.7% | 45.2% | {"coverage": 1710, "market_freshness": 1036, "execution": 868, "data": 698, "market_freshness/coverage": 403, "mapping": 111, "model_calibration_or_unknown": 55, "model_calibration": 11} | 12.87 | 0.2037 / 0.1946 (3547) | 39.5% | 56.9% | 9.9% | 22.1% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,684 | 4.7% | 4.1% | 1.2% | {"market_freshness": 39, "model_calibration_or_unknown": 27, "execution": 17, "model_calibration": 12, "data": 11, "market_freshness/coverage": 10, "coverage": 9, "mapping": 1} | 7.81 | 0.238 / 0.2305 (439) | 24.5% | 1.3% | 1.4% | 3.6% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.6% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 15 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 16 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 17 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 18 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 19 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 20 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 21 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 22 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 23 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 24 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 25 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 26 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 27 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 28 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 29 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 30 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 31 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 32 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 33 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 34 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 35 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 36 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 37 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 38 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 39 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 40 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 41 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 42 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 162 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 43 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 44 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 45 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 46 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 47 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 48 | `KXITFWMATCH-26OCT20CHAAPI-CHA` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 771 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 122.0, ratio 20.3); no external reference |
| 49 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 730 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |
| 50 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 547 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9711, "by_level_share_of_ge_25pp": {"ATP": 0.0173, "CHALLENGER": 0.1198, "DOUBLES": 0.068, "ITF_MEN": 0.3137, "ITF_WOMEN": 0.4524, "OTHER": 0.0011, "WTA": 0.0117, "WTA125": 0.0161}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5199, "share_primary_cause_market_settled_or_in_play": 0.4344, "share_primary_cause_stale_quote_only": 0.1837}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 10814, "identity_ambiguous_share": 0.2192, "ticker_orientation": {"VERIFIED": 10814}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 6921, "with_external": 346, "coverage": 0.05, "external_status": {"EXTERNAL_STALE": 210, "AGREES_WITH_KALSHI": 128, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 210, "MODEL_LONE_OUTLIER": 128, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3699, "share_external_supports_model": 0.0231}, "pregame_clean_ge_25pp": {"n": 3358, "with_external": 323, "coverage": 0.0962, "external_status": {"EXTERNAL_STALE": 194, "AGREES_WITH_KALSHI": 121, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 194, "MODEL_LONE_OUTLIER": 121, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3746, "share_external_supports_model": 0.0248}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 480.0, "median_sample_ratio": 2.45, "median_min_matches": 20.0, "median_max_days_since_last": 225.0, "share_severe_asymmetry": 0.213, "data_status": {"POOR": 6053, "LIMITED": 2885, "ADEQUATE": 1876}, "comparison_lt_10pp": {"median_thinner_serve_points": 1667.0, "median_sample_ratio": 1.71, "median_min_matches": 91.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 803, "model_minus_observed": 0.0463, "kalshi_minus_observed": -0.0913, "brier_diff_model_minus_kalshi": -0.004}, "4-10x": {"n": 554, "model_minus_observed": 0.0965, "kalshi_minus_observed": -0.0498, "brier_diff_model_minus_kalshi": 0.0145}, "<2x": {"n": 1981, "model_minus_observed": 0.0894, "kalshi_minus_observed": -0.0351, "brier_diff_model_minus_kalshi": 0.0121}, ">=10x": {"n": 712, "model_minus_observed": 0.1093, "kalshi_minus_observed": -0.0668, "brier_diff_model_minus_kalshi": 0.0073}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4050, "model": {"intercept": -0.543, "slope": 0.847, "slope_se": 0.041}, "kalshi_mid_same_rows": {"intercept": 0.226, "slope": 1.101, "slope_se": 0.046}, "mean_extremity_model": 0.17, "mean_extremity_kalshi": 0.1658, "model_brier": 0.2328, "kalshi_brier": 0.2049, "brier_diff_model_minus_kalshi": 0.0278, "brier_diff_se": 0.003, "model_logloss": 0.662, "kalshi_logloss": 0.5925}, "fair_v1": {"n": 4050, "model": {"intercept": -0.412, "slope": 1.045, "slope_se": 0.044}, "kalshi_mid_same_rows": {"intercept": 0.311, "slope": 1.142, "slope_se": 0.046}, "mean_extremity_model": 0.1678, "mean_extremity_kalshi": 0.1653, "model_brier": 0.2136, "kalshi_brier": 0.2052, "brier_diff_model_minus_kalshi": 0.0084, "brier_diff_se": 0.0025, "model_logloss": 0.6155, "kalshi_logloss": 0.5928}, "gen1_elo": {"n": 4050, "model": {"intercept": -0.395, "slope": 1.02, "slope_se": 0.043}, "kalshi_mid_same_rows": {"intercept": 0.319, "slope": 1.131, "slope_se": 0.046}, "mean_extremity_model": 0.1748, "mean_extremity_kalshi": 0.1654, "model_brier": 0.2126, "kalshi_brier": 0.2054, "brier_diff_model_minus_kalshi": 0.0073, "brier_diff_se": 0.0025, "model_logloss": 0.6142, "kalshi_logloss": 0.5932}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2466, "share_ge_15": 0.4463, "median_abs_gap": 13.21, "n": 28061}, "gen1_elo": {"share_ge_25": 0.2441, "share_ge_15": 0.4446, "median_abs_gap": 13.01, "n": 28061}, "gen1_sr": {"share_ge_25": 0.3151, "share_ge_15": 0.5274, "median_abs_gap": 16.08, "n": 28061}, "gen2": {"share_ge_25": 0.3177, "share_ge_15": 0.5148, "median_abs_gap": 15.64, "n": 28061}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1541, "share_ge_15": 0.3627, "median_abs_gap": 10.98, "n": 21784}, "gen1_elo": {"share_ge_25": 0.1556, "share_ge_15": 0.3587, "median_abs_gap": 10.69, "n": 21781}, "gen1_sr": {"share_ge_25": 0.2229, "share_ge_15": 0.4507, "median_abs_gap": 13.31, "n": 21785}, "gen2": {"share_ge_25": 0.2386, "share_ge_15": 0.4483, "median_abs_gap": 13.2, "n": 21786}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.84, "share_ge_25_all": 0.0494, "share_ge_25_pregame_clean": 0.0443}, "WTA": {"median_abs_gap_pregame_clean": 7.81, "share_ge_25_all": 0.0469, "share_ge_25_pregame_clean": 0.0414}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2345, "share_within_10pp_all": 0.4315, "share_within_10pp_pregame_clean": 0.4841, "corr_model_vs_mid_pregame_clean": 0.8453}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 592, "model_brier": 0.1985, "kalshi_brier": 0.1996, "brier_diff_model_minus_kalshi": -0.0011}, "10-15": {"n_settled": 701, "model_brier": 0.2124, "kalshi_brier": 0.2035, "brier_diff_model_minus_kalshi": 0.0089}, "15-25": {"n_settled": 928, "model_brier": 0.2242, "kalshi_brier": 0.2133, "brier_diff_model_minus_kalshi": 0.0109}, "25-40": {"n_settled": 526, "model_brier": 0.2247, "kalshi_brier": 0.2102, "brier_diff_model_minus_kalshi": 0.0145}, "3-5": {"n_settled": 377, "model_brier": 0.2022, "kalshi_brier": 0.2016, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 104, "model_brier": 0.2868, "kalshi_brier": 0.1908, "brier_diff_model_minus_kalshi": 0.0961}, "5-10": {"n_settled": 822, "model_brier": 0.2023, "kalshi_brier": 0.2018, "brier_diff_model_minus_kalshi": 0.0005}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.543, "slope": 0.847, "slope_se": 0.041}, "kalshi_slope": {"intercept": 0.226, "slope": 1.101, "slope_se": 0.046}, "n": 4050}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.512, "slope": 0.869, "slope_se": 0.031}, "kalshi_slope": {"intercept": 0.157, "slope": 1.08, "slope_se": 0.036}, "n": 6097}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 389, "model_brier": 0.3147, "kalshi_brier": 0.2359, "brier_diff_model_minus_kalshi": 0.0787, "brier_diff_se": 0.0157, "corr_model_outcome": 0.0207, "corr_kalshi_outcome": 0.2553}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
