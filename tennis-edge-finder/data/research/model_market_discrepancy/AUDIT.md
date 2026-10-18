# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-18T05:03Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 37,647): 0-3 14.4%, 3-5 9.5%, 5-10 19.9%, 10-15 15.4%, 15-25 18.9%, 25-40 13.7%, 40+ 8.3%; median gap 11.89 pp.
* **Where the extremes live**: 97.8% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.4%, Challenger 12.0%, doubles 7.1%). Main tour: ATP 2.8% and WTA 5.4% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 8,261): MARKET_ALREADY_SETTLED_WHEN_PRICED 35.8%, BOOK_QUALITY 18.6%, STALE_QUOTE 18.1%, POOR_DATA 8.4%, POSSIBLY_IN_PLAY_QUOTE 5.3%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 3.9%, IN_PLAY_QUOTE 3.2%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.5%. By class: coverage 35.8%, execution 18.6%, market_freshness 18.1%, data 12.2%, market_freshness/coverage 8.5%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.5%.
* **Stale / settled / in-play**: 52.9% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 44.3% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 8,261 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.4% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 23.1% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 553.0 points vs 1841.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.054, Gen-2 0.853, Gen-1 ledger 0.877 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 378 model 0.2265 vs Kalshi 0.2071; n 78 model 0.3044 vs Kalshi 0.1729.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 154,384 model-market comparisons (253,764 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 55,481 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-18T04:56:51.035346+00:00'], shadow board 41,640 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-18T04:56:53.754996+00:00'], Model 4 17,440 rows, 15,630 settled tickers, 5,368 tickers with an external scan.
* By model: {"gen1_ledger": 37147, "gen1_elo": 20942, "fair_v1": 20942, "gen2": 20942, "gen1_sr": 20942, "model4_fundamental": 16739, "model4_conditioned": 16730}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 37,647 | 14.4 | 9.5 | 19.9 | 15.4 | 18.9 | 13.7 | 8.3 | 11.89 | 40.8% | 21.9% |
| MW fair_v1 | 20,942 | 13.5 | 8.5 | 18.4 | 15.8 | 19.2 | 14.6 | 9.9 | 13.0 | 43.8% | 24.5% |
| MW gen1_elo | 20,942 | 13.1 | 9.0 | 19.5 | 15.2 | 19.3 | 14.3 | 9.6 | 12.53 | 43.2% | 23.9% |
| MW gen1_ledger | 16,705 | 15.6 | 10.8 | 21.7 | 14.8 | 18.4 | 12.5 | 6.2 | 10.47 | 37.1% | 18.7% |
| MW gen1_sr | 20,942 | 9.7 | 7.4 | 16.5 | 14.2 | 21.6 | 18.6 | 12.1 | 15.84 | 52.2% | 30.7% |
| MW gen2 | 20,942 | 11.4 | 7.1 | 16.5 | 14.1 | 19.9 | 17.6 | 13.3 | 15.43 | 50.9% | 30.9% |
| all families model4_conditioned | 16,730 | 21.4 | 19.3 | 34.4 | 17.4 | 4.7 | 1.6 | 1.2 | 5.94 | 7.4% | 2.7% |
| all families model4_fundamental | 16,739 | 16.2 | 13.0 | 34.8 | 20.2 | 11.1 | 3.3 | 1.4 | 7.84 | 15.8% | 4.8% |

Configurable thresholds (primary): >=5pp 76.1%, >=10pp 56.2%, >=15pp 40.8%, >=20pp 30.4%, >=25pp 21.9%, >=30pp 15.9%, >=40pp 8.3%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.3pp; >=10pp 44.8%, >=25pp 17.2%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,651 | 29.5 | 13.8 | 24.6 | 17.3 | 11.5 | 2.6 | 0.7 | 6.09 | 14.8% | 3.3% |
| CHALLENGER | 3,430 | 15.9 | 10.1 | 20.1 | 15.8 | 14.3 | 12.4 | 11.3 | 11.32 | 38.0% | 23.7% |
| ITF_MEN | 5,856 | 11.0 | 8.0 | 17.5 | 14.9 | 19.8 | 16.3 | 12.5 | 14.48 | 48.6% | 28.8% |
| ITF_WOMEN | 8,183 | 10.2 | 6.7 | 15.9 | 15.4 | 22.3 | 18.2 | 11.3 | 15.69 | 51.8% | 29.5% |
| WTA | 1,168 | 19.6 | 12.1 | 24.4 | 18.4 | 19.5 | 5.0 | 0.9 | 8.2 | 25.5% | 6.0% |
| WTA125 | 654 | 13.3 | 7.5 | 23.7 | 20.2 | 19.9 | 13.5 | 2.0 | 11.14 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,651 | 23.6 | 14.2 | 24.6 | 18.4 | 14.4 | 3.6 | 1.1 | 6.9 | 19.1% | 4.7% |
| CHALLENGER | 3,430 | 14.7 | 8.1 | 19.3 | 13.7 | 17.9 | 14.3 | 12.0 | 12.68 | 44.2% | 26.3% |
| ITF_MEN | 5,856 | 9.3 | 6.7 | 15.7 | 13.6 | 19.8 | 19.4 | 15.4 | 16.95 | 54.6% | 34.8% |
| ITF_WOMEN | 8,183 | 8.5 | 5.6 | 13.7 | 13.3 | 21.1 | 20.9 | 16.9 | 18.89 | 58.8% | 37.7% |
| WTA | 1,168 | 17.3 | 7.8 | 20.2 | 15.8 | 22.8 | 15.1 | 1.0 | 11.68 | 38.9% | 16.1% |
| WTA125 | 654 | 6.7 | 4.7 | 17.1 | 17.6 | 25.8 | 19.1 | 8.9 | 16.79 | 53.8% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,651 | 26.4 | 13.6 | 26.3 | 16.6 | 13.1 | 3.2 | 0.8 | 6.53 | 17.1% | 4.0% |
| CHALLENGER | 3,430 | 15.0 | 10.3 | 20.6 | 15.1 | 15.5 | 12.0 | 11.6 | 11.03 | 39.1% | 23.6% |
| ITF_MEN | 5,856 | 10.0 | 8.1 | 17.9 | 14.2 | 20.6 | 16.7 | 12.5 | 14.97 | 49.8% | 29.2% |
| ITF_WOMEN | 8,183 | 9.7 | 6.9 | 16.4 | 15.5 | 22.9 | 18.2 | 10.4 | 15.58 | 51.5% | 28.6% |
| WTA | 1,168 | 23.2 | 16.5 | 31.4 | 15.3 | 10.9 | 2.0 | 0.6 | 6.05 | 13.5% | 2.6% |
| WTA125 | 654 | 22.6 | 12.2 | 29.4 | 15.8 | 13.9 | 5.8 | 0.3 | 7.73 | 20.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,026 | 28.3 | 20.4 | 32.5 | 11.7 | 5.2 | 1.9 | 0.1 | 5.06 | 7.2% | 2.1% |
| CHALLENGER | 2,374 | 22.4 | 15.2 | 27.4 | 14.2 | 13.5 | 5.3 | 2.1 | 6.94 | 20.9% | 7.4% |
| DOUBLES | 1,197 | 4.9 | 4.0 | 10.4 | 10.9 | 20.7 | 25.7 | 23.3 | 24.22 | 69.8% | 49.0% |
| ITF_MEN | 4,918 | 14.6 | 8.6 | 20.7 | 15.8 | 20.9 | 12.5 | 7.0 | 11.86 | 40.3% | 19.5% |
| ITF_WOMEN | 5,460 | 11.8 | 9.1 | 19.0 | 14.8 | 22.2 | 16.9 | 6.2 | 13.2 | 45.3% | 23.1% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 855 | 21.4 | 16.3 | 29.5 | 17.4 | 10.9 | 4.2 | 0.3 | 6.97 | 15.4% | 4.6% |
| WTA125 | 726 | 21.5 | 13.9 | 22.2 | 18.3 | 14.2 | 7.8 | 2.1 | 8.14 | 24.1% | 9.9% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,619 | 29.7 | 13.8 | 24.9 | 17.1 | 11.4 | 2.2 | 0.7 | 6.01 | 14.4% | 3.0% |
| CHALLENGER | 2,455 | 20.6 | 12.7 | 25.2 | 18.2 | 14.8 | 6.1 | 2.3 | 8.23 | 23.2% | 8.4% |
| ITF_MEN | 4,247 | 13.5 | 10.0 | 20.9 | 16.8 | 20.1 | 13.2 | 5.6 | 11.54 | 38.9% | 18.7% |
| ITF_WOMEN | 6,108 | 12.1 | 8.0 | 18.1 | 17.6 | 23.7 | 15.3 | 5.1 | 13.3 | 44.2% | 20.5% |
| WTA | 1,146 | 19.7 | 11.5 | 24.7 | 18.5 | 19.6 | 5.0 | 1.0 | 8.27 | 25.6% | 5.9% |
| WTA125 | 628 | 13.7 | 7.3 | 23.2 | 20.5 | 20.5 | 13.1 | 1.6 | 11.25 | 35.2% | 14.6% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,619 | 23.7 | 14.4 | 24.6 | 18.5 | 14.3 | 3.5 | 0.9 | 6.86 | 18.7% | 4.4% |
| CHALLENGER | 2,455 | 18.7 | 10.5 | 24.1 | 16.4 | 18.3 | 9.6 | 2.5 | 9.08 | 30.4% | 12.1% |
| ITF_MEN | 4,248 | 11.0 | 8.0 | 18.2 | 15.4 | 21.9 | 17.1 | 8.4 | 14.12 | 47.4% | 25.5% |
| ITF_WOMEN | 6,108 | 9.5 | 6.4 | 15.3 | 14.7 | 23.1 | 20.2 | 10.7 | 16.57 | 54.1% | 31.0% |
| WTA | 1,146 | 17.2 | 7.7 | 20.2 | 15.9 | 22.9 | 15.2 | 1.1 | 11.73 | 39.1% | 16.2% |
| WTA125 | 628 | 6.5 | 4.9 | 17.2 | 18.0 | 25.8 | 19.6 | 8.0 | 16.66 | 53.3% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 996 | 28.4 | 20.6 | 32.8 | 11.8 | 4.5 | 1.7 | 0.1 | 5.03 | 6.3% | 1.8% |
| CHALLENGER | 2,051 | 24.1 | 16.5 | 29.4 | 13.9 | 12.7 | 2.7 | 0.7 | 6.34 | 16.1% | 3.4% |
| DOUBLES | 1,106 | 5.0 | 4.2 | 10.6 | 11.1 | 20.5 | 25.9 | 22.7 | 24.09 | 69.2% | 48.6% |
| ITF_MEN | 4,068 | 16.0 | 9.4 | 22.6 | 16.7 | 20.6 | 10.6 | 4.2 | 10.61 | 35.4% | 14.7% |
| ITF_WOMEN | 4,504 | 12.8 | 9.8 | 20.6 | 15.7 | 22.4 | 15.4 | 3.4 | 11.89 | 41.2% | 18.8% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 818 | 21.8 | 16.8 | 29.7 | 17.5 | 11.0 | 3.3 | 0.0 | 6.82 | 14.3% | 3.3% |
| WTA125 | 616 | 23.5 | 15.4 | 23.7 | 19.8 | 12.5 | 4.7 | 0.3 | 7.2 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,197 | 4.9 | 4.0 | 10.4 | 10.9 | 20.7 | 25.7 | 23.3 | 24.22 | 69.8% | 49.0% |
| singles | 15,508 | 16.4 | 11.3 | 22.6 | 15.1 | 18.2 | 11.5 | 4.9 | 9.91 | 34.6% | 16.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 4,859 | 13.3 | 8.9 | 19.2 | 15.8 | 18.1 | 14.6 | 10.1 | 12.76 | 42.8% | 24.7% |
| Grass | 236 | 11.4 | 11.0 | 17.8 | 13.6 | 23.7 | 14.8 | 7.6 | 14.16 | 46.2% | 22.5% |
| Hard | 13,561 | 13.9 | 8.5 | 18.4 | 15.4 | 19.6 | 14.4 | 9.8 | 12.96 | 43.7% | 24.2% |
| UNKNOWN | 2,286 | 12.1 | 7.2 | 17.0 | 18.1 | 19.0 | 15.9 | 10.6 | 13.48 | 45.6% | 26.6% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,174 | 19.7 | 10.8 | 21.1 | 17.3 | 15.8 | 8.8 | 6.5 | 9.48 | 31.1% | 15.3% |
| B | 2,731 | 13.5 | 9.1 | 19.7 | 16.4 | 18.4 | 12.1 | 10.8 | 12.12 | 41.2% | 22.8% |
| C | 3,043 | 12.8 | 9.5 | 19.6 | 14.1 | 19.0 | 14.9 | 10.1 | 12.77 | 44.0% | 25.0% |
| D | 3,513 | 11.9 | 7.9 | 17.3 | 15.7 | 21.9 | 15.5 | 9.8 | 13.97 | 47.2% | 25.3% |
| F | 5,481 | 8.1 | 5.4 | 14.8 | 14.8 | 21.9 | 21.6 | 13.4 | 17.94 | 56.9% | 35.0% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,966 | 23.1 | 15.9 | 29.0 | 15.2 | 11.2 | 4.2 | 1.5 | 6.68 | 16.8% | 5.7% |
| B | 2,422 | 15.2 | 10.1 | 23.9 | 16.4 | 19.2 | 11.0 | 4.2 | 10.16 | 34.4% | 15.2% |
| C | 3,328 | 11.7 | 7.6 | 17.6 | 14.4 | 21.3 | 16.3 | 11.1 | 14.34 | 48.8% | 27.4% |
| D | 2,427 | 14.1 | 9.7 | 20.3 | 13.9 | 21.0 | 14.2 | 6.8 | 12.04 | 41.9% | 21.0% |
| F | 3,562 | 10.2 | 7.6 | 14.9 | 14.2 | 23.4 | 20.5 | 9.1 | 16.34 | 53.1% | 29.6% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 6,996 | 17.9 | 9.7 | 20.4 | 17.0 | 16.3 | 9.7 | 8.9 | 10.54 | 35.0% | 18.6% |
| LIMITED | 4,800 | 14.6 | 10.5 | 20.6 | 15.2 | 18.5 | 13.2 | 7.5 | 11.36 | 39.2% | 20.7% |
| POOR | 9,146 | 9.6 | 6.5 | 15.8 | 15.2 | 21.8 | 19.1 | 11.9 | 16.01 | 52.8% | 31.0% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,950 | 27.9 | 22.3 | 35.1 | 10.3 | 3.1 | 1.1 | 0.2 | 4.98 | 4.4% | 1.3% |
| GAME_SPREAD | 3,426 | 24.6 | 15.4 | 35.2 | 17.6 | 5.8 | 1.1 | 0.2 | 6.21 | 7.1% | 1.3% |
| MATCH_WINNER | 16,705 | 15.6 | 10.8 | 21.7 | 14.8 | 18.4 | 12.5 | 6.2 | 10.47 | 37.1% | 18.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 7,481 | 31.0 | 18.2 | 30.7 | 11.8 | 6.6 | 1.2 | 0.5 | 5.07 | 8.3% | 1.7% |
| TOTAL_GAMES | 5,561 | 6.7 | 8.9 | 37.4 | 28.7 | 11.6 | 3.8 | 3.0 | 9.67 | 18.3% | 6.8% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,849 | 24.9 | 36.0 | 31.3 | 3.1 | 3.8 | 0.7 | 0.2 | 4.42 | 4.7% | 0.9% |
| GAME_SPREAD | 4,045 | 45.8 | 16.6 | 27.8 | 7.4 | 1.4 | 0.7 | 0.3 | 3.47 | 2.4% | 1.0% |
| TOTAL_GAMES | 6,836 | 4.0 | 6.6 | 41.0 | 35.6 | 7.5 | 2.8 | 2.5 | 9.85 | 12.7% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,849 | 25.1 | 17.6 | 36.2 | 11.2 | 6.9 | 2.5 | 0.4 | 5.72 | 9.8% | 2.9% |
| GAME_SPREAD | 4,045 | 19.3 | 13.6 | 29.1 | 20.5 | 13.4 | 3.1 | 0.9 | 7.84 | 17.5% | 4.0% |
| TOTAL_GAMES | 6,845 | 6.8 | 8.7 | 36.9 | 27.6 | 13.2 | 4.2 | 2.6 | 9.72 | 20.0% | 6.8% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 20,942 | 43.8% | 24.5% | 13.0 | 35.0% | 15.2% | 10.7 |
| gen1_elo | 20,942 | 43.2% | 23.9% | 12.53 | 34.0% | 14.9% | 10.17 |
| gen1_sr | 20,942 | 52.2% | 30.7% | 15.84 | 44.4% | 21.3% | 13.18 |
| gen2 | 20,942 | 50.9% | 30.9% | 15.43 | 44.1% | 22.8% | 13.02 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 11,138 | 16.4 | 10.4 | 21.5 | 17.4 | 19.6 | 11.3 | 3.3 | 10.47 | 34.3% | 14.7% |
| STALE | 9,804 | 10.2 | 6.3 | 15.0 | 14.0 | 18.8 | 18.3 | 17.4 | 17.32 | 54.5% | 35.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 10,173 | 17.2 | 11.5 | 23.0 | 14.8 | 17.1 | 11.5 | 4.9 | 9.57 | 33.4% | 16.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 37,647 | 10173 | 14610 | 12864 | 23.8 | 150.2 | 1400.4 |
| ge_15pp | 15,361 | 3400 | 5108 | 6853 | 26.2 | 455.5 | 1380.4 |
| ge_25pp | 8,261 | 1663 | 2225 | 4373 | 33.1 | 592.1 | 1380.4 |
| lt_10pp | 16,502 | 5262 | 7015 | 4225 | 21.8 | 48.5 | 1341.5 |

Current slate `SL-20261018T050342Z-b309e74c`: 1084 priced rows, quote age at build {'median': 7.3, 'max': 7.3}, freshness {'FRESH': 1084}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 11 | 0.0 | 0.0 | 36.4 | 0.0 | 45.5 | 18.2 | 0.0 | 20.19 | 63.6% | 18.2% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,881 | 21.6 | 10.7 | 22.8 | 18.8 | 18.7 | 6.8 | 0.5 | 8.65 | 26.1% | 7.3% |
| KALSHI_LONE_OUTLIER | 11 | 9.1 | 0.0 | 72.7 | 0.0 | 9.1 | 9.1 | 0.0 | 5.2 | 18.2% | 9.1% |
| MARKETS_AGREE | 332 | 69.3 | 30.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.13 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 674 | 0.0 | 3.1 | 35.5 | 28.6 | 23.4 | 8.6 | 0.7 | 11.81 | 32.8% | 9.3% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 20,942 | 2921 (14.0%) | 23.1% | 0.7% | {"EXTERNAL_STALE": 1881, "AGREES_WITH_KALSHI": 674, "ALL_AGREE": 332, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 11, "SUPPORTS_MODEL_DIRECTION": 10, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 9,162 | 720 (7.9%) | 30.7% | 1.2% | {"EXTERNAL_STALE": 490, "AGREES_WITH_KALSHI": 221, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 5,136 | 204 (4.0%) | 30.9% | 1.5% | {"EXTERNAL_STALE": 138, "AGREES_WITH_KALSHI": 63, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,459 | 192 (7.8%) | 31.8% | 1.6% | {"EXTERNAL_STALE": 128, "AGREES_WITH_KALSHI": 61, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 8,471 | 1654 (19.5%) | 15.7% | 0.7% | {"EXTERNAL_STALE": 1037, "ALL_AGREE": 332, "AGREES_WITH_KALSHI": 260, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 9, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 4,040 | 11.3 | 7.8 | 19.3 | 14.8 | 21.7 | 14.8 | 10.4 | 13.83 | 46.8% | 25.1% |
| 4-10x | 2,685 | 12.6 | 8.8 | 19.4 | 15.3 | 19.2 | 15.2 | 9.5 | 12.89 | 43.9% | 24.7% |
| <2x | 10,947 | 15.4 | 9.3 | 18.9 | 16.9 | 17.7 | 12.9 | 8.9 | 11.87 | 39.6% | 21.8% |
| >=10x | 3,270 | 10.8 | 6.3 | 15.1 | 13.9 | 21.2 | 19.7 | 13.0 | 16.48 | 53.8% | 32.7% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 5,541 | 13.2 | 8.4 | 19.3 | 16.0 | 19.6 | 13.1 | 10.4 | 12.83 | 43.1% | 23.5% |
| 300-1000 | 4,631 | 12.1 | 8.7 | 17.2 | 15.7 | 20.7 | 16.0 | 9.6 | 13.74 | 46.3% | 25.6% |
| <300 | 6,224 | 9.1 | 5.9 | 15.4 | 14.7 | 21.6 | 20.3 | 13.0 | 16.96 | 54.9% | 33.3% |
| >=3000 | 4,546 | 21.4 | 11.9 | 22.8 | 17.3 | 14.0 | 7.2 | 5.5 | 8.28 | 26.6% | 12.6% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 642 | 0.5383 | 0.4044 | 0.4844 | +0.054 | -0.080 | 0.0015 ± 0.0059 |
| ratio 4-10x | 428 | 0.5842 | 0.4473 | 0.5047 | +0.080 | -0.057 | 0.0087 ± 0.0075 |
| ratio <2x | 1597 | 0.5364 | 0.415 | 0.4502 | +0.086 | -0.035 | 0.0126 ± 0.0036 |
| ratio >=10x | 520 | 0.5468 | 0.3784 | 0.4192 | +0.128 | -0.041 | 0.0173 ± 0.0078 |
| thinner_sample 1000-3000 | 908 | 0.5428 | 0.4173 | 0.4615 | +0.081 | -0.044 | 0.0081 ± 0.0048 |
| thinner_sample 300-1000 | 753 | 0.5616 | 0.4225 | 0.4861 | +0.076 | -0.064 | 0.0028 ± 0.0057 |
| thinner_sample <300 | 974 | 0.5429 | 0.3827 | 0.4312 | +0.112 | -0.049 | 0.0175 ± 0.0055 |
| thinner_sample >=3000 | 552 | 0.5292 | 0.4362 | 0.4692 | +0.060 | -0.033 | 0.0131 ± 0.0049 |
| data_status ADEQUATE | 944 | 0.5329 | 0.4287 | 0.4597 | +0.073 | -0.031 | 0.0101 ± 0.0041 |
| data_status LIMITED | 795 | 0.552 | 0.4228 | 0.4855 | +0.067 | -0.063 | 0.0048 ± 0.0052 |
| data_status POOR | 1448 | 0.5489 | 0.3935 | 0.4448 | +0.104 | -0.051 | 0.0141 ± 0.0044 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 494 | 0.1925 | 0.1938 | -0.0014 ± 0.0007 | 0.563 | 0.5658 | 0.4942 | 0.4795 | 0.5304 | -0.042 ± 0.0207 | -0.01 (5) |
| 3-5 | 310 | 0.1948 | 0.1942 | +0.0006 ± 0.002 | 0.5706 | 0.568 | 0.5053 | 0.4654 | 0.4774 | -0.080 ± 0.0257 | 0.02 (1) |
| 5-10 | 671 | 0.1978 | 0.1971 | +0.0006 ± 0.0026 | 0.5811 | 0.5776 | 0.5104 | 0.4361 | 0.4635 | -0.083 ± 0.0177 | -0.0167 (6) |
| 10-15 | 562 | 0.2137 | 0.2049 | +0.0088 ± 0.0048 | 0.616 | 0.5917 | 0.5186 | 0.3947 | 0.4199 | -0.086 ± 0.0191 | -0.048 (5) |
| 15-25 | 694 | 0.2292 | 0.2129 | +0.0163 ± 0.0068 | 0.6529 | 0.6108 | 0.5759 | 0.381 | 0.438 | -0.083 ± 0.0174 | -0.0033 (9) |
| 25-40 | 378 | 0.2265 | 0.2071 | +0.0194 ± 0.014 | 0.6424 | 0.5964 | 0.6463 | 0.3375 | 0.4603 | -0.064 ± 0.0214 | -0.01 (1) |
| 40+ | 78 | 0.3044 | 0.1729 | +0.1315 ± 0.0422 | 0.8211 | 0.5186 | 0.7435 | 0.296 | 0.3718 | -0.122 ± 0.0414 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2311 | 0.18 | 0.1812 | -0.0012 ± 0.0003 | 0.5348 | 0.5361 | 0.4791 | 0.464 | 0.4994 | -0.019 ± 0.009 | -0.0129 (17) |
| 3-5 | 1445 | 0.1927 | 0.1907 | +0.0021 ± 0.0009 | 0.5658 | 0.5566 | 0.4792 | 0.4394 | 0.4318 | -0.064 ± 0.0117 | 0.0 (2) |
| 5-10 | 3122 | 0.1937 | 0.1913 | +0.0025 ± 0.0012 | 0.5702 | 0.5615 | 0.4822 | 0.4084 | 0.427 | -0.044 ± 0.0079 | -0.0119 (21) |
| 10-15 | 2703 | 0.2016 | 0.1824 | +0.0192 ± 0.0021 | 0.5893 | 0.5368 | 0.4795 | 0.3548 | 0.3407 | -0.076 ± 0.0082 | -0.0281 (16) |
| 15-25 | 3301 | 0.208 | 0.1691 | +0.0388 ± 0.0028 | 0.6078 | 0.5009 | 0.502 | 0.3058 | 0.3066 | -0.070 ± 0.0071 | -0.0025 (44) |
| 25-40 | 2598 | 0.223 | 0.1256 | +0.0973 ± 0.0044 | 0.6398 | 0.3879 | 0.5289 | 0.2158 | 0.2209 | -0.064 ± 0.0067 | -0.01 (1) |
| 40+ | 1769 | 0.3783 | 0.042 | +0.3363 ± 0.0055 | 0.9846 | 0.1678 | 0.6266 | 0.1052 | 0.0537 | -0.087 ± 0.0045 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 366 | 0.1976 | 0.198 | -0.0004 ± 0.0008 | 0.5765 | 0.5774 | 0.5015 | 0.4863 | 0.5055 | -0.081 ± 0.0245 | -0.01 (3) |
| 3-5 | 255 | 0.2114 | 0.2105 | +0.0009 ± 0.0023 | 0.6054 | 0.6045 | 0.5154 | 0.4755 | 0.4784 | -0.082 ± 0.0304 | 0.02 (1) |
| 5-10 | 584 | 0.199 | 0.1985 | +0.0005 ± 0.0028 | 0.5816 | 0.5804 | 0.5476 | 0.4728 | 0.5068 | -0.070 ± 0.019 | -0.01 (4) |
| 10-15 | 526 | 0.2177 | 0.21 | +0.0077 ± 0.005 | 0.6234 | 0.6057 | 0.567 | 0.4426 | 0.4772 | -0.090 ± 0.021 | -0.04 (5) |
| 15-25 | 762 | 0.2287 | 0.2073 | +0.0213 ± 0.0065 | 0.6489 | 0.5969 | 0.5875 | 0.391 | 0.4383 | -0.089 ± 0.0167 | -0.0133 (9) |
| 25-40 | 503 | 0.2669 | 0.1956 | +0.0713 ± 0.0125 | 0.7443 | 0.5716 | 0.6584 | 0.3434 | 0.3897 | -0.114 ± 0.0196 | -0.0075 (4) |
| 40+ | 191 | 0.3649 | 0.1779 | +0.1870 ± 0.0301 | 1.0145 | 0.527 | 0.741 | 0.2585 | 0.3194 | -0.071 ± 0.0295 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1945 | 0.1824 | 0.1828 | -0.0003 ± 0.0003 | 0.54 | 0.5406 | 0.502 | 0.4874 | 0.5069 | -0.035 ± 0.01 | -0.0133 (15) |
| 3-5 | 1231 | 0.1936 | 0.1927 | +0.0009 ± 0.001 | 0.5621 | 0.5598 | 0.5145 | 0.4745 | 0.4817 | -0.043 ± 0.0128 | 0.02 (1) |
| 5-10 | 2791 | 0.1921 | 0.1896 | +0.0025 ± 0.0012 | 0.5668 | 0.5579 | 0.5101 | 0.4361 | 0.4579 | -0.039 ± 0.0084 | -0.0117 (6) |
| 10-15 | 2396 | 0.1978 | 0.1869 | +0.0109 ± 0.0022 | 0.5814 | 0.5459 | 0.5191 | 0.3946 | 0.4157 | -0.047 ± 0.009 | -0.0189 (18) |
| 15-25 | 3442 | 0.2168 | 0.1755 | +0.0412 ± 0.0028 | 0.6288 | 0.5184 | 0.5313 | 0.335 | 0.3312 | -0.076 ± 0.0072 | -0.0086 (42) |
| 25-40 | 3047 | 0.25 | 0.1349 | +0.1151 ± 0.0042 | 0.7067 | 0.4148 | 0.5587 | 0.2427 | 0.2205 | -0.088 ± 0.0066 | -0.0044 (18) |
| 40+ | 2397 | 0.4011 | 0.066 | +0.3351 ± 0.006 | 1.0583 | 0.2309 | 0.6623 | 0.1255 | 0.0947 | -0.069 ± 0.0051 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 474 | 0.1942 | 0.1965 | -0.0022 ± 0.0007 | 0.5682 | 0.5737 | 0.4972 | 0.482 | 0.5464 | -0.015 ± 0.0208 | -0.0137 (8) |
| 3-5 | 351 | 0.1893 | 0.1874 | +0.0018 ± 0.0019 | 0.5552 | 0.5509 | 0.497 | 0.4574 | 0.4558 | -0.111 ± 0.0243 | 0.0067 (3) |
| 5-10 | 702 | 0.2017 | 0.1976 | +0.0041 ± 0.0025 | 0.5906 | 0.5773 | 0.5029 | 0.4291 | 0.4345 | -0.095 ± 0.0172 | -0.0071 (7) |
| 10-15 | 550 | 0.207 | 0.2054 | +0.0016 ± 0.0048 | 0.6015 | 0.5937 | 0.5373 | 0.4144 | 0.4727 | -0.065 ± 0.0191 | -0.0317 (6) |
| 15-25 | 643 | 0.2349 | 0.2091 | +0.0258 ± 0.007 | 0.6696 | 0.6021 | 0.5842 | 0.3909 | 0.4199 | -0.109 ± 0.0179 | -0.03 (1) |
| 25-40 | 392 | 0.2125 | 0.2128 | -0.0003 ± 0.0136 | 0.6121 | 0.6092 | 0.6516 | 0.3422 | 0.4949 | -0.043 ± 0.0209 | 0.015 (2) |
| 40+ | 75 | 0.3237 | 0.1866 | +0.1371 ± 0.045 | 0.8679 | 0.5501 | 0.7473 | 0.2945 | 0.3733 | -0.107 ± 0.0471 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2201 | 0.1855 | 0.1863 | -0.0008 ± 0.0003 | 0.5475 | 0.5489 | 0.4844 | 0.4691 | 0.4934 | -0.027 ± 0.0093 | -0.0163 (35) |
| 3-5 | 1517 | 0.1876 | 0.1839 | +0.0036 ± 0.0009 | 0.5527 | 0.5439 | 0.4764 | 0.4369 | 0.4113 | -0.087 ± 0.0113 | -0.0094 (18) |
| 5-10 | 3322 | 0.1947 | 0.1885 | +0.0063 ± 0.0011 | 0.5747 | 0.5536 | 0.4807 | 0.4068 | 0.3992 | -0.067 ± 0.0076 | -0.01 (31) |
| 10-15 | 2560 | 0.1957 | 0.1804 | +0.0154 ± 0.0021 | 0.576 | 0.5299 | 0.4963 | 0.3729 | 0.373 | -0.065 ± 0.0083 | -0.015 (12) |
| 15-25 | 3414 | 0.2074 | 0.1678 | +0.0396 ± 0.0027 | 0.6085 | 0.4981 | 0.5045 | 0.3095 | 0.3064 | -0.071 ± 0.007 | -0.03 (2) |
| 25-40 | 2542 | 0.2179 | 0.1237 | +0.0942 ± 0.0044 | 0.6281 | 0.3816 | 0.5258 | 0.2097 | 0.2231 | -0.059 ± 0.0066 | 0.01 (3) |
| 40+ | 1693 | 0.3942 | 0.0461 | +0.3481 ± 0.0059 | 1.0278 | 0.1789 | 0.6382 | 0.1097 | 0.0561 | -0.089 ± 0.005 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 824 | 0.195 | 0.1951 | -0.0001 ± 0.0005 | 0.5703 | 0.5703 | 0.5079 | 0.4929 | 0.4964 | -0.051 ± 0.0154 | -0.0224 (49) |
| 3-5 | 577 | 0.1948 | 0.1939 | +0.0010 ± 0.0015 | 0.5679 | 0.5645 | 0.4795 | 0.4397 | 0.4454 | -0.052 ± 0.0185 | -0.0194 (34) |
| 5-10 | 1213 | 0.1977 | 0.1918 | +0.0059 ± 0.0019 | 0.5826 | 0.5654 | 0.4879 | 0.4144 | 0.4122 | -0.064 ± 0.0128 | -0.005 (78) |
| 10-15 | 770 | 0.2074 | 0.1964 | +0.0110 ± 0.004 | 0.6032 | 0.5744 | 0.5072 | 0.3842 | 0.4 | -0.054 ± 0.0161 | 0.0014 (64) |
| 15-25 | 1022 | 0.2336 | 0.2119 | +0.0217 ± 0.0057 | 0.6656 | 0.6098 | 0.5659 | 0.371 | 0.4139 | -0.056 ± 0.0144 | -0.0214 (59) |
| 25-40 | 591 | 0.2481 | 0.1954 | +0.0527 ± 0.0112 | 0.7004 | 0.5686 | 0.6481 | 0.3361 | 0.4061 | -0.079 ± 0.0168 | -0.0219 (26) |
| 40+ | 198 | 0.3755 | 0.1901 | +0.1854 ± 0.0316 | 1.081 | 0.5609 | 0.7922 | 0.3012 | 0.3788 | -0.081 ± 0.0284 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2495 | 0.1872 | 0.1872 | -0.0000 ± 0.0003 | 0.5502 | 0.5493 | 0.5042 | 0.4889 | 0.4986 | -0.035 ± 0.0086 | -0.0157 (88) |
| 3-5 | 1696 | 0.1893 | 0.187 | +0.0023 ± 0.0008 | 0.5537 | 0.5485 | 0.485 | 0.4454 | 0.4369 | -0.054 ± 0.0106 | -0.0209 (69) |
| 5-10 | 3415 | 0.1941 | 0.186 | +0.0081 ± 0.0011 | 0.5731 | 0.5502 | 0.4828 | 0.4092 | 0.3947 | -0.066 ± 0.0075 | -0.0082 (132) |
| 10-15 | 2316 | 0.204 | 0.1898 | +0.0143 ± 0.0023 | 0.596 | 0.5578 | 0.5106 | 0.3876 | 0.3912 | -0.055 ± 0.009 | -0.0053 (105) |
| 15-25 | 2881 | 0.229 | 0.1975 | +0.0315 ± 0.0033 | 0.6607 | 0.5745 | 0.5578 | 0.3625 | 0.3811 | -0.059 ± 0.0084 | -0.0253 (107) |
| 25-40 | 1950 | 0.2543 | 0.1685 | +0.0858 ± 0.0059 | 0.7197 | 0.4991 | 0.6083 | 0.2942 | 0.3174 | -0.078 ± 0.009 | -0.0229 (51) |
| 40+ | 932 | 0.3875 | 0.13 | +0.2576 ± 0.0126 | 1.0967 | 0.398 | 0.7093 | 0.2029 | 0.2146 | -0.072 ± 0.0112 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3187 | 1.054 ± 0.05 | 1.17 | 0.168 | 0.171 | 0.2123 | 0.2017 |
| gen2 | 3187 | 0.853 ± 0.045 | 1.128 | 0.1749 | 0.171 | 0.2307 | 0.2017 |
| gen1_elo | 3187 | 1.041 ± 0.049 | 1.155 | 0.1735 | 0.1714 | 0.211 | 0.2016 |
| gen1_sr | 3187 | 1.048 ± 0.059 | 1.187 | 0.1347 | 0.1727 | 0.2269 | 0.2015 |
| gen1_ledger | 5195 | 0.877 ± 0.034 | 1.078 | 0.1773 | 0.1851 | 0.218 | 0.1975 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 15,361)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,742 | 24.4% |
| STALE_QUOTE | market_freshness | 3,174 | 20.7% |
| BOOK_QUALITY | execution | 2,905 | 18.9% |
| POOR_DATA | data | 1,670 | 10.9% |
| LIMITED_DATA | data | 1,072 | 7.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 812 | 5.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 744 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 619 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 434 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 189 | 1.2% |

Cause class: coverage 24.4%, market_freshness 20.7%, execution 18.9%, data 17.8%, market_freshness/coverage 8.1%, model_calibration_or_unknown 4.8%, mapping 4.0%, model_calibration 1.2%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.8%, START_UNVERIFIABLE 95.1%, LOW_DATA_QUALITY 69.3%, THIN_PLAYER_HISTORY 57.7%, STALE_PLAYER_DATA 52.0%, STALE_KALSHI_QUOTE 44.6%, MODEL_INTERNAL_DISAGREEMENT 39.9%, ASYMMETRIC_SAMPLE_SIZE 32.0%, WIDE_SPREAD 24.8%, MODEL_HIGH_UNCERTAINTY 17.7%, PLAYER_IDENTITY_RISK 14.6%, LEVEL_TRANSFER_RISK 8.6%, EVENT_MAPPING_RISK 8.3%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 2.1%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 26.8%, POST_SETTLEMENT_OBSERVATION 24.4%, POSSIBLE_IN_PLAY_QUOTE 5.6%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 8,261)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,959 | 35.8% |
| BOOK_QUALITY | execution | 1,536 | 18.6% |
| STALE_QUOTE | market_freshness | 1,495 | 18.1% |
| POOR_DATA | data | 694 | 8.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 436 | 5.3% |
| IDENTITY_AMBIGUOUS | mapping | 358 | 4.3% |
| LIMITED_DATA | data | 318 | 3.9% |
| IN_PLAY_QUOTE | market_freshness/coverage | 268 | 3.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 158 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 39 | 0.5% |

Cause class: coverage 35.8%, execution 18.6%, market_freshness 18.1%, data 12.2%, market_freshness/coverage 8.5%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.8%, START_UNVERIFIABLE 97.8%, LOW_DATA_QUALITY 73.2%, THIN_PLAYER_HISTORY 60.2%, STALE_KALSHI_QUOTE 52.9%, STALE_PLAYER_DATA 47.4%, MODEL_INTERNAL_DISAGREEMENT 40.9%, ASYMMETRIC_SAMPLE_SIZE 33.9%, WIDE_SPREAD 24.7%, MODEL_HIGH_UNCERTAINTY 18.1%, PLAYER_IDENTITY_RISK 17.9%, EVENT_MAPPING_RISK 10.0%, LOW_DISPLAYED_LIQUIDITY 7.9%, LEVEL_TRANSFER_RISK 7.6%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.1%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 38.6%, POST_SETTLEMENT_OBSERVATION 35.8%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 6573, "IDENTITY_AMBIGUOUS": 1688}; ticker orientation: {"VERIFIED": 8261}.

Checks: discipline:AMBIGUOUS 587, discipline:PASS 7674, identity_confidence:AMBIGUOUS 1478, identity_confidence:PASS 6783, level_mapping:NA 599, level_mapping:PASS 7662, market_pair:AMBIGUOUS 294, market_pair:NA 207, market_pair:PASS 7760, model_complement:NA 174, model_complement:PASS 8087, namesake:PASS 8261, physical_match_id:NA 3125, physical_match_id:PASS 5136, player_ids:PASS 8261, same_pair_other_event:PASS 8261, ticker_orientation:PASS 8261

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,677 | 2.8% | 2.5% | 0.9% | {"market_freshness": 31, "data": 18, "execution": 13, "market_freshness/coverage": 8, "model_calibration_or_unknown": 4, "coverage": 2} | 5.53 | 0.2088 / 0.2068 (295) | 16.6% | 2.4% | 4.6% | 2.3% |
| CHALLENGER | 5,804 | 17.0% | 6.1% | 12.0% | {"coverage": 588, "market_freshness/coverage": 125, "market_freshness": 123, "data": 71, "model_calibration_or_unknown": 46, "execution": 21, "model_calibration": 9, "mapping": 6} | 7.13 | 0.217 / 0.2049 (1485) | 36.7% | 10.8% | 2.5% | 22.4% |
| DOUBLES | 1,197 | 49.0% | 48.6% | 7.1% | {"execution": 266, "mapping": 166, "market_freshness": 106, "market_freshness/coverage": 42, "coverage": 7} | 24.09 | 0.323 / 0.2339 (334) | 19.6% | 0.0% | 100.0% | 7.6% |
| ITF_MEN | 10,774 | 24.5% | 16.8% | 32.0% | {"coverage": 1040, "execution": 533, "market_freshness": 407, "data": 358, "market_freshness/coverage": 209, "mapping": 94, "model_calibration_or_unknown": 2} | 11.13 | 0.2135 / 0.194 (2622) | 36.4% | 61.6% | 12.9% | 22.8% |
| ITF_WOMEN | 13,643 | 26.9% | 19.8% | 44.5% | {"coverage": 1305, "market_freshness": 752, "execution": 674, "data": 531, "market_freshness/coverage": 271, "mapping": 86, "model_calibration_or_unknown": 43, "model_calibration": 10} | 12.77 | 0.2034 / 0.1913 (2781) | 38.9% | 57.1% | 10.1% | 22.2% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,023 | 5.4% | 4.8% | 1.3% | {"market_freshness": 36, "model_calibration_or_unknown": 23, "execution": 15, "data": 11, "market_freshness/coverage": 10, "model_calibration": 9, "coverage": 4, "mapping": 1} | 7.66 | 0.2362 / 0.2312 (341) | 23.0% | 1.7% | 1.8% | 2.9% |
| WTA125 | 1,380 | 12.5% | 9.9% | 2.1% | {"model_calibration_or_unknown": 38, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.2185 / 0.2069 (482) | 22.9% | 7.4% | 5.1% | 9.9% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 5 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 6 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 7 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 15.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 928 min (STALE); no external reference |
| 9 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 10 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 11 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 12 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 13 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 14 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 15 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 16 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 17 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 18 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 19 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 20 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 768 min (STALE); no external reference |
| 22 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 23 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 24 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 25 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 26 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 27 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 28 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 29 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 30 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 31 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 32 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 33 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 752 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 34 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 35 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 36 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 37 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 38 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 39 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 547 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 40 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 41 | `KXITFWMATCH-26OCT16ESTLAB-LAB` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 68 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1475.0, ratio 2.28); no external reference |
| 42 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 43 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 44 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 45 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 46 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 47 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 48 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 49 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 50 | `KXATPCHALLENGERMATCH-26OCT13GIUSEA-SEA` | CHALLENGER | fair_v1 | 76% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 243 min (STALE); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9776, "by_level_share_of_ge_25pp": {"ATP": 0.0092, "CHALLENGER": 0.1197, "DOUBLES": 0.0711, "ITF_MEN": 0.3199, "ITF_WOMEN": 0.4445, "OTHER": 0.0015, "WTA": 0.0132, "WTA125": 0.0209}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5294, "share_primary_cause_market_settled_or_in_play": 0.4434, "share_primary_cause_stale_quote_only": 0.181}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 8261, "identity_ambiguous_share": 0.2043, "ticker_orientation": {"VERIFIED": 8261}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 5136, "with_external": 204, "coverage": 0.0397, "external_status": {"EXTERNAL_STALE": 138, "AGREES_WITH_KALSHI": 63, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 138, "MODEL_LONE_OUTLIER": 63, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3088, "share_external_supports_model": 0.0147}, "pregame_clean_ge_25pp": {"n": 2459, "with_external": 192, "coverage": 0.0781, "external_status": {"EXTERNAL_STALE": 128, "AGREES_WITH_KALSHI": 61, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 128, "MODEL_LONE_OUTLIER": 61, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3177, "share_external_supports_model": 0.0156}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 553.0, "median_sample_ratio": 2.41, "median_min_matches": 21.0, "median_max_days_since_last": 210.0, "share_severe_asymmetry": 0.2063, "data_status": {"POOR": 4417, "LIMITED": 2358, "ADEQUATE": 1486}, "comparison_lt_10pp": {"median_thinner_serve_points": 1841.0, "median_sample_ratio": 1.67, "median_min_matches": 93.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 642, "model_minus_observed": 0.0539, "kalshi_minus_observed": -0.0801, "brier_diff_model_minus_kalshi": 0.0015}, "4-10x": {"n": 428, "model_minus_observed": 0.0796, "kalshi_minus_observed": -0.0574, "brier_diff_model_minus_kalshi": 0.0087}, "<2x": {"n": 1597, "model_minus_observed": 0.0862, "kalshi_minus_observed": -0.0352, "brier_diff_model_minus_kalshi": 0.0126}, ">=10x": {"n": 520, "model_minus_observed": 0.1276, "kalshi_minus_observed": -0.0408, "brier_diff_model_minus_kalshi": 0.0173}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3187, "model": {"intercept": -0.552, "slope": 0.853, "slope_se": 0.045}, "kalshi_mid_same_rows": {"intercept": 0.219, "slope": 1.128, "slope_se": 0.051}, "mean_extremity_model": 0.1749, "mean_extremity_kalshi": 0.171, "model_brier": 0.2307, "kalshi_brier": 0.2017, "brier_diff_model_minus_kalshi": 0.029, "brier_diff_se": 0.0033, "model_logloss": 0.6575, "kalshi_logloss": 0.5855}, "fair_v1": {"n": 3187, "model": {"intercept": -0.415, "slope": 1.054, "slope_se": 0.05}, "kalshi_mid_same_rows": {"intercept": 0.296, "slope": 1.17, "slope_se": 0.052}, "mean_extremity_model": 0.168, "mean_extremity_kalshi": 0.171, "model_brier": 0.2123, "kalshi_brier": 0.2017, "brier_diff_model_minus_kalshi": 0.0106, "brier_diff_se": 0.0027, "model_logloss": 0.6122, "kalshi_logloss": 0.5853}, "gen1_elo": {"n": 3187, "model": {"intercept": -0.41, "slope": 1.041, "slope_se": 0.049}, "kalshi_mid_same_rows": {"intercept": 0.286, "slope": 1.155, "slope_se": 0.051}, "mean_extremity_model": 0.1735, "mean_extremity_kalshi": 0.1714, "model_brier": 0.211, "kalshi_brier": 0.2016, "brier_diff_model_minus_kalshi": 0.0095, "brier_diff_se": 0.0027, "model_logloss": 0.6103, "kalshi_logloss": 0.585}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2452, "share_ge_15": 0.4375, "median_abs_gap": 13.0, "n": 20942}, "gen1_elo": {"share_ge_25": 0.2386, "share_ge_15": 0.432, "median_abs_gap": 12.53, "n": 20942}, "gen1_sr": {"share_ge_25": 0.3066, "share_ge_15": 0.5222, "median_abs_gap": 15.84, "n": 20942}, "gen2": {"share_ge_25": 0.3094, "share_ge_15": 0.5087, "median_abs_gap": 15.43, "n": 20942}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1518, "share_ge_15": 0.3497, "median_abs_gap": 10.7, "n": 16203}, "gen1_elo": {"share_ge_25": 0.1488, "share_ge_15": 0.3403, "median_abs_gap": 10.17, "n": 16202}, "gen1_sr": {"share_ge_25": 0.2132, "share_ge_15": 0.4441, "median_abs_gap": 13.18, "n": 16203}, "gen2": {"share_ge_25": 0.2284, "share_ge_15": 0.4412, "median_abs_gap": 13.02, "n": 16204}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.53, "share_ge_25_all": 0.0284, "share_ge_25_pregame_clean": 0.0252}, "WTA": {"median_abs_gap_pregame_clean": 7.66, "share_ge_25_all": 0.0539, "share_ge_25_pregame_clean": 0.0484}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2394, "share_within_10pp_all": 0.4383, "share_within_10pp_pregame_clean": 0.4944, "corr_model_vs_mid_pregame_clean": 0.8417}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 494, "model_brier": 0.1925, "kalshi_brier": 0.1938, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 562, "model_brier": 0.2137, "kalshi_brier": 0.2049, "brier_diff_model_minus_kalshi": 0.0088}, "15-25": {"n_settled": 694, "model_brier": 0.2292, "kalshi_brier": 0.2129, "brier_diff_model_minus_kalshi": 0.0163}, "25-40": {"n_settled": 378, "model_brier": 0.2265, "kalshi_brier": 0.2071, "brier_diff_model_minus_kalshi": 0.0194}, "3-5": {"n_settled": 310, "model_brier": 0.1948, "kalshi_brier": 0.1942, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 78, "model_brier": 0.3044, "kalshi_brier": 0.1729, "brier_diff_model_minus_kalshi": 0.1315}, "5-10": {"n_settled": 671, "model_brier": 0.1978, "kalshi_brier": 0.1971, "brier_diff_model_minus_kalshi": 0.0006}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.552, "slope": 0.853, "slope_se": 0.045}, "kalshi_slope": {"intercept": 0.219, "slope": 1.128, "slope_se": 0.051}, "n": 3187}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.518, "slope": 0.877, "slope_se": 0.034}, "kalshi_slope": {"intercept": 0.139, "slope": 1.078, "slope_se": 0.038}, "n": 5195}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 334, "model_brier": 0.323, "kalshi_brier": 0.2339, "brier_diff_model_minus_kalshi": 0.0891, "brier_diff_se": 0.0171, "corr_model_outcome": 0.015, "corr_kalshi_outcome": 0.2585}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
