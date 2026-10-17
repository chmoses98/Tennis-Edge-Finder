# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-17T12:35Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 36,314): 0-3 14.5%, 3-5 9.5%, 5-10 20.0%, 10-15 15.3%, 15-25 18.8%, 25-40 13.6%, 40+ 8.3%; median gap 11.85 pp.
* **Where the extremes live**: 97.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.8%, Challenger 12.0%, doubles 6.9%). Main tour: ATP 2.3% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 7,949): MARKET_ALREADY_SETTLED_WHEN_PRICED 36.6%, STALE_QUOTE 18.1%, BOOK_QUALITY 17.4%, POOR_DATA 8.4%, POSSIBLY_IN_PLAY_QUOTE 5.3%, IDENTITY_AMBIGUOUS 4.4%, LIMITED_DATA 4.0%, IN_PLAY_QUOTE 3.2%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.5%. By class: coverage 36.6%, market_freshness 18.1%, execution 17.4%, data 12.4%, market_freshness/coverage 8.6%, mapping 4.4%, model_calibration_or_unknown 2.0%, model_calibration 0.5%.
* **Stale / settled / in-play**: 53.6% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 45.2% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 7,949 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 23.1% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 565.0 points vs 1841.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.056, Gen-2 0.856, Gen-1 ledger 0.876 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 370 model 0.2237 vs Kalshi 0.207; n 78 model 0.3044 vs Kalshi 0.1729.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 146,359 model-market comparisons (242,454 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 51,870 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-17T12:27:36.916356+00:00'], shadow board 40,327 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-17T12:27:40.206104+00:00'], Model 4 15,950 rows, 15,346 settled tickers, 5,224 tickers with an external scan.
* By model: {"gen1_ledger": 34372, "gen1_elo": 20282, "fair_v1": 20282, "gen2": 20282, "gen1_sr": 20282, "model4_fundamental": 15434, "model4_conditioned": 15425}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 36,314 | 14.5 | 9.5 | 20.0 | 15.3 | 18.8 | 13.6 | 8.3 | 11.85 | 40.7% | 21.9% |
| MW fair_v1 | 20,282 | 13.5 | 8.5 | 18.5 | 15.7 | 19.2 | 14.6 | 10.0 | 13.0 | 43.8% | 24.6% |
| MW gen1_elo | 20,282 | 13.1 | 9.0 | 19.6 | 15.1 | 19.2 | 14.3 | 9.6 | 12.5 | 43.1% | 23.9% |
| MW gen1_ledger | 16,032 | 15.8 | 10.8 | 21.8 | 14.8 | 18.3 | 12.3 | 6.1 | 10.39 | 36.8% | 18.5% |
| MW gen1_sr | 20,282 | 9.7 | 7.5 | 16.4 | 14.2 | 21.5 | 18.7 | 12.1 | 15.87 | 52.3% | 30.8% |
| MW gen2 | 20,282 | 11.4 | 7.1 | 16.5 | 14.1 | 19.9 | 17.6 | 13.3 | 15.43 | 50.9% | 30.9% |
| all families model4_conditioned | 15,425 | 21.5 | 19.6 | 34.5 | 17.1 | 4.7 | 1.5 | 1.1 | 5.89 | 7.3% | 2.6% |
| all families model4_fundamental | 15,434 | 16.6 | 13.2 | 34.9 | 19.8 | 11.1 | 3.1 | 1.3 | 7.75 | 15.6% | 4.5% |

Configurable thresholds (primary): >=5pp 75.9%, >=10pp 56.0%, >=15pp 40.7%, >=20pp 30.3%, >=25pp 21.9%, >=30pp 15.9%, >=40pp 8.3%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.48pp; >=10pp 45.3%, >=25pp 17.5%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,499 | 30.2 | 13.9 | 24.9 | 17.3 | 10.9 | 2.0 | 0.8 | 5.93 | 13.7% | 2.8% |
| CHALLENGER | 3,339 | 15.9 | 10.1 | 20.2 | 15.7 | 14.4 | 12.2 | 11.4 | 11.32 | 38.1% | 23.7% |
| ITF_MEN | 5,772 | 10.9 | 8.1 | 17.5 | 14.8 | 19.9 | 16.4 | 12.5 | 14.52 | 48.7% | 28.9% |
| ITF_WOMEN | 7,918 | 10.4 | 6.7 | 16.0 | 15.5 | 22.1 | 18.1 | 11.2 | 15.57 | 51.4% | 29.3% |
| WTA | 1,107 | 20.2 | 12.5 | 24.7 | 16.7 | 19.6 | 5.3 | 1.0 | 7.97 | 25.9% | 6.3% |
| WTA125 | 647 | 13.0 | 7.6 | 24.0 | 20.1 | 20.1 | 13.3 | 2.0 | 11.08 | 35.4% | 15.3% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,499 | 23.9 | 14.5 | 24.4 | 18.9 | 14.5 | 2.7 | 1.1 | 6.9 | 18.4% | 3.9% |
| CHALLENGER | 3,339 | 14.8 | 8.2 | 19.3 | 13.7 | 17.8 | 14.2 | 12.1 | 12.63 | 44.0% | 26.2% |
| ITF_MEN | 5,772 | 9.4 | 6.7 | 15.8 | 13.6 | 19.8 | 19.5 | 15.3 | 16.92 | 54.6% | 34.8% |
| ITF_WOMEN | 7,918 | 8.6 | 5.7 | 13.8 | 13.2 | 21.2 | 20.8 | 16.8 | 18.8 | 58.7% | 37.5% |
| WTA | 1,107 | 17.2 | 8.0 | 20.7 | 15.4 | 22.4 | 15.2 | 1.1 | 11.5 | 38.7% | 16.3% |
| WTA125 | 647 | 6.3 | 4.8 | 17.3 | 17.8 | 25.8 | 19.0 | 9.0 | 16.74 | 53.8% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,499 | 27.2 | 13.8 | 27.4 | 16.0 | 11.9 | 2.8 | 0.9 | 6.46 | 15.5% | 3.7% |
| CHALLENGER | 3,339 | 14.8 | 10.3 | 20.8 | 15.0 | 15.5 | 11.9 | 11.7 | 11.01 | 39.1% | 23.6% |
| ITF_MEN | 5,772 | 9.9 | 8.1 | 17.9 | 14.2 | 20.6 | 16.8 | 12.5 | 14.98 | 49.9% | 29.3% |
| ITF_WOMEN | 7,918 | 9.9 | 7.0 | 16.5 | 15.6 | 22.8 | 18.1 | 10.3 | 15.47 | 51.1% | 28.4% |
| WTA | 1,107 | 23.2 | 16.4 | 31.6 | 15.2 | 10.8 | 2.2 | 0.6 | 6.05 | 13.6% | 2.8% |
| WTA125 | 647 | 22.1 | 12.4 | 29.7 | 15.6 | 14.1 | 5.9 | 0.3 | 7.73 | 20.2% | 6.2% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 878 | 29.9 | 21.2 | 33.4 | 11.3 | 2.7 | 1.4 | 0.1 | 4.87 | 4.2% | 1.5% |
| CHALLENGER | 2,286 | 22.8 | 15.2 | 27.6 | 14.5 | 12.8 | 5.1 | 2.0 | 6.88 | 19.9% | 7.1% |
| DOUBLES | 1,121 | 5.3 | 4.0 | 10.9 | 11.1 | 20.1 | 25.1 | 23.6 | 24.1 | 68.8% | 48.7% |
| ITF_MEN | 4,858 | 14.7 | 8.6 | 20.7 | 15.6 | 20.8 | 12.5 | 7.1 | 11.86 | 40.4% | 19.6% |
| ITF_WOMEN | 5,224 | 11.8 | 9.2 | 19.4 | 14.9 | 22.3 | 16.5 | 5.9 | 13.04 | 44.7% | 22.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 797 | 21.5 | 16.7 | 28.6 | 16.7 | 11.7 | 4.5 | 0.4 | 6.94 | 16.6% | 4.9% |
| WTA125 | 719 | 21.3 | 13.8 | 22.4 | 18.5 | 14.1 | 7.9 | 2.1 | 8.19 | 24.1% | 10.0% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,480 | 30.3 | 13.9 | 25.1 | 17.2 | 10.9 | 1.8 | 0.8 | 5.93 | 13.5% | 2.6% |
| CHALLENGER | 2,379 | 20.7 | 12.7 | 25.5 | 18.1 | 14.9 | 5.8 | 2.3 | 8.11 | 23.0% | 8.1% |
| ITF_MEN | 4,196 | 13.3 | 10.0 | 20.9 | 16.7 | 20.2 | 13.3 | 5.6 | 11.58 | 39.2% | 18.9% |
| ITF_WOMEN | 5,892 | 12.4 | 8.1 | 18.2 | 17.7 | 23.5 | 15.1 | 5.1 | 13.09 | 43.6% | 20.1% |
| WTA | 1,085 | 20.4 | 11.9 | 25.0 | 16.8 | 19.7 | 5.2 | 1.0 | 7.99 | 26.0% | 6.3% |
| WTA125 | 621 | 13.4 | 7.4 | 23.5 | 20.4 | 20.8 | 12.9 | 1.6 | 11.2 | 35.3% | 14.5% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,480 | 23.9 | 14.6 | 24.4 | 18.9 | 14.5 | 2.6 | 1.0 | 6.9 | 18.2% | 3.6% |
| CHALLENGER | 2,379 | 19.0 | 10.5 | 24.2 | 16.5 | 18.0 | 9.3 | 2.5 | 9.01 | 29.8% | 11.8% |
| ITF_MEN | 4,197 | 11.0 | 8.0 | 18.2 | 15.3 | 21.9 | 17.1 | 8.5 | 14.12 | 47.4% | 25.5% |
| ITF_WOMEN | 5,892 | 9.8 | 6.5 | 15.4 | 14.5 | 23.2 | 20.0 | 10.6 | 16.42 | 53.8% | 30.6% |
| WTA | 1,085 | 17.1 | 7.9 | 20.6 | 15.4 | 22.5 | 15.3 | 1.1 | 11.62 | 38.9% | 16.4% |
| WTA125 | 621 | 6.1 | 5.0 | 17.4 | 18.2 | 25.8 | 19.5 | 8.1 | 16.64 | 53.3% | 27.5% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 857 | 29.9 | 21.4 | 33.6 | 11.4 | 2.2 | 1.4 | 0.1 | 4.86 | 3.7% | 1.5% |
| CHALLENGER | 1,970 | 24.7 | 16.6 | 29.7 | 14.3 | 11.9 | 2.4 | 0.5 | 6.24 | 14.8% | 2.9% |
| DOUBLES | 1,034 | 5.4 | 4.2 | 11.1 | 11.2 | 19.8 | 25.2 | 23.0 | 23.93 | 68.1% | 48.3% |
| ITF_MEN | 4,018 | 16.1 | 9.4 | 22.6 | 16.4 | 20.6 | 10.6 | 4.3 | 10.56 | 35.4% | 14.9% |
| ITF_WOMEN | 4,282 | 12.9 | 9.9 | 21.1 | 15.8 | 22.6 | 14.8 | 2.8 | 11.65 | 40.2% | 17.7% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 760 | 21.8 | 17.2 | 28.8 | 16.7 | 11.8 | 3.5 | 0.0 | 6.76 | 15.4% | 3.5% |
| WTA125 | 609 | 23.3 | 15.3 | 24.0 | 20.0 | 12.3 | 4.8 | 0.3 | 7.25 | 17.4% | 5.1% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,121 | 5.3 | 4.0 | 10.9 | 11.1 | 20.1 | 25.1 | 23.6 | 24.1 | 68.8% | 48.7% |
| singles | 14,911 | 16.6 | 11.3 | 22.7 | 15.1 | 18.1 | 11.4 | 4.8 | 9.85 | 34.4% | 16.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 4,744 | 13.3 | 8.9 | 19.2 | 15.7 | 18.1 | 14.6 | 10.2 | 12.77 | 42.9% | 24.8% |
| Grass | 231 | 10.4 | 11.3 | 18.2 | 13.8 | 23.4 | 15.2 | 7.8 | 14.16 | 46.3% | 22.9% |
| Hard | 13,135 | 13.9 | 8.5 | 18.5 | 15.3 | 19.5 | 14.4 | 9.9 | 12.96 | 43.8% | 24.2% |
| UNKNOWN | 2,172 | 12.2 | 7.3 | 16.9 | 18.4 | 19.0 | 15.8 | 10.5 | 13.38 | 45.3% | 26.3% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,967 | 19.7 | 10.8 | 21.2 | 17.0 | 15.7 | 8.9 | 6.6 | 9.45 | 31.2% | 15.5% |
| B | 2,658 | 13.8 | 9.0 | 19.6 | 16.3 | 18.5 | 12.2 | 10.6 | 12.12 | 41.3% | 22.8% |
| C | 2,950 | 12.6 | 9.7 | 19.9 | 14.0 | 19.0 | 14.7 | 10.1 | 12.71 | 43.8% | 24.8% |
| D | 3,426 | 11.8 | 7.9 | 17.4 | 15.8 | 21.9 | 15.3 | 9.9 | 13.95 | 47.1% | 25.2% |
| F | 5,281 | 8.1 | 5.4 | 14.8 | 14.8 | 21.8 | 21.6 | 13.5 | 18.0 | 57.0% | 35.1% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,766 | 23.2 | 15.9 | 28.9 | 15.2 | 10.9 | 4.3 | 1.6 | 6.63 | 16.8% | 5.9% |
| B | 2,369 | 14.9 | 10.1 | 24.0 | 16.6 | 19.4 | 10.8 | 4.3 | 10.19 | 34.5% | 15.1% |
| C | 3,178 | 12.0 | 7.8 | 17.8 | 14.5 | 20.9 | 15.9 | 11.1 | 13.93 | 47.9% | 27.0% |
| D | 2,334 | 14.2 | 9.8 | 20.6 | 13.7 | 21.2 | 13.8 | 6.7 | 11.85 | 41.7% | 20.5% |
| F | 3,385 | 10.5 | 7.6 | 15.2 | 14.1 | 23.4 | 20.4 | 8.9 | 16.15 | 52.6% | 29.2% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 6,754 | 18.0 | 9.7 | 20.4 | 16.8 | 16.2 | 9.8 | 9.1 | 10.51 | 35.1% | 18.9% |
| LIMITED | 4,688 | 14.6 | 10.5 | 20.6 | 15.1 | 18.5 | 13.1 | 7.5 | 11.32 | 39.1% | 20.6% |
| POOR | 8,840 | 9.6 | 6.5 | 15.9 | 15.2 | 21.8 | 19.0 | 12.0 | 16.02 | 52.8% | 31.0% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,455 | 29.8 | 23.7 | 35.3 | 7.5 | 2.4 | 1.1 | 0.2 | 4.69 | 3.6% | 1.3% |
| GAME_SPREAD | 3,144 | 25.1 | 15.9 | 35.8 | 17.8 | 4.3 | 0.8 | 0.2 | 6.08 | 5.3% | 1.0% |
| MATCH_WINNER | 16,032 | 15.8 | 10.8 | 21.8 | 14.8 | 18.3 | 12.3 | 6.1 | 10.39 | 36.8% | 18.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 6,657 | 32.1 | 18.7 | 30.8 | 10.8 | 5.9 | 1.3 | 0.4 | 4.88 | 7.6% | 1.7% |
| TOTAL_GAMES | 5,060 | 6.6 | 8.7 | 37.5 | 29.1 | 11.7 | 3.6 | 2.8 | 9.68 | 18.1% | 6.4% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,347 | 25.5 | 37.2 | 31.3 | 1.2 | 3.8 | 0.7 | 0.2 | 4.33 | 4.7% | 0.9% |
| GAME_SPREAD | 3,757 | 45.3 | 16.4 | 28.2 | 7.7 | 1.3 | 0.7 | 0.3 | 3.54 | 2.4% | 1.0% |
| TOTAL_GAMES | 6,321 | 3.9 | 6.6 | 41.0 | 36.2 | 7.5 | 2.6 | 2.2 | 9.86 | 12.3% | 4.9% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,347 | 26.3 | 18.1 | 36.6 | 9.6 | 6.7 | 2.4 | 0.4 | 5.57 | 9.5% | 2.8% |
| GAME_SPREAD | 3,757 | 19.2 | 13.4 | 29.5 | 21.1 | 13.3 | 2.6 | 0.9 | 7.85 | 16.8% | 3.5% |
| TOTAL_GAMES | 6,330 | 6.9 | 8.9 | 36.6 | 27.7 | 13.5 | 4.1 | 2.4 | 9.75 | 20.0% | 6.5% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 20,282 | 43.8% | 24.6% | 13.0 | 34.9% | 15.1% | 10.64 |
| gen1_elo | 20,282 | 43.1% | 23.9% | 12.5 | 33.9% | 14.8% | 10.11 |
| gen1_sr | 20,282 | 52.3% | 30.8% | 15.87 | 44.4% | 21.4% | 13.17 |
| gen2 | 20,282 | 50.9% | 30.9% | 15.43 | 44.0% | 22.7% | 13.0 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 10,831 | 16.5 | 10.5 | 21.6 | 17.2 | 19.5 | 11.3 | 3.3 | 10.42 | 34.2% | 14.7% |
| STALE | 9,451 | 10.2 | 6.3 | 14.9 | 13.9 | 18.8 | 18.3 | 17.6 | 17.41 | 54.7% | 35.9% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 9,500 | 17.6 | 11.6 | 23.3 | 14.9 | 16.8 | 11.1 | 4.7 | 9.38 | 32.6% | 15.8% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 36,314 | 9500 | 14303 | 12511 | 23.9 | 157.6 | 1400.4 |
| ge_15pp | 14,769 | 3096 | 4995 | 6678 | 26.8 | 460.0 | 1380.4 |
| ge_25pp | 7,949 | 1502 | 2182 | 4265 | 34.5 | 597.4 | 1380.4 |
| lt_10pp | 15,986 | 4992 | 6891 | 4103 | 22.0 | 48.0 | 1341.5 |

Current slate `SL-20261017T123545Z-fddb1e62`: 490 priced rows, quote age at build {'median': 8.5, 'max': 8.6}, freshness {'FRESH': 490}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 11 | 0.0 | 0.0 | 36.4 | 0.0 | 45.5 | 18.2 | 0.0 | 20.19 | 63.6% | 18.2% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,786 | 21.4 | 10.9 | 23.1 | 18.2 | 18.9 | 7.0 | 0.6 | 8.56 | 26.4% | 7.6% |
| KALSHI_LONE_OUTLIER | 10 | 10.0 | 0.0 | 70.0 | 0.0 | 10.0 | 10.0 | 0.0 | 5.17 | 20.0% | 10.0% |
| MARKETS_AGREE | 327 | 69.1 | 30.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.11 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 645 | 0.0 | 3.3 | 36.0 | 27.9 | 23.7 | 8.4 | 0.8 | 11.7 | 32.9% | 9.2% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 20,282 | 2791 (13.8%) | 23.1% | 0.7% | {"EXTERNAL_STALE": 1786, "AGREES_WITH_KALSHI": 645, "ALL_AGREE": 327, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 10, "AGREES_WITH_MODEL": 10, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 8,874 | 693 (7.8%) | 30.6% | 1.3% | {"EXTERNAL_STALE": 472, "AGREES_WITH_KALSHI": 212, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 4,985 | 197 (4.0%) | 29.9% | 1.5% | {"EXTERNAL_STALE": 135, "AGREES_WITH_KALSHI": 59, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,369 | 186 (7.8%) | 30.6% | 1.6% | {"EXTERNAL_STALE": 126, "AGREES_WITH_KALSHI": 57, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 8,225 | 1593 (19.4%) | 15.9% | 0.7% | {"EXTERNAL_STALE": 989, "ALL_AGREE": 327, "AGREES_WITH_KALSHI": 253, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 8, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,926 | 11.3 | 7.7 | 19.4 | 14.8 | 21.9 | 14.5 | 10.5 | 13.82 | 46.8% | 24.9% |
| 4-10x | 2,604 | 12.8 | 8.9 | 19.9 | 15.2 | 18.7 | 15.0 | 9.4 | 12.64 | 43.1% | 24.4% |
| <2x | 10,620 | 15.3 | 9.3 | 18.9 | 16.7 | 17.7 | 13.0 | 9.1 | 11.91 | 39.8% | 22.1% |
| >=10x | 3,132 | 10.9 | 6.5 | 15.0 | 13.7 | 21.3 | 19.7 | 13.0 | 16.53 | 54.0% | 32.7% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 5,418 | 13.4 | 8.3 | 19.3 | 15.9 | 19.7 | 13.0 | 10.4 | 12.82 | 43.1% | 23.4% |
| 300-1000 | 4,513 | 12.0 | 8.7 | 17.3 | 15.7 | 20.8 | 15.8 | 9.6 | 13.74 | 46.3% | 25.5% |
| <300 | 5,984 | 9.0 | 6.0 | 15.5 | 14.6 | 21.4 | 20.4 | 13.1 | 16.99 | 54.9% | 33.4% |
| >=3000 | 4,367 | 21.4 | 12.0 | 22.9 | 17.0 | 13.8 | 7.3 | 5.6 | 8.3 | 26.7% | 12.9% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 632 | 0.538 | 0.4041 | 0.4842 | +0.054 | -0.080 | 0.0016 ± 0.006 |
| ratio 4-10x | 423 | 0.5838 | 0.4465 | 0.5059 | +0.078 | -0.059 | 0.008 ± 0.0075 |
| ratio <2x | 1567 | 0.5368 | 0.4147 | 0.4512 | +0.086 | -0.036 | 0.0122 ± 0.0036 |
| ratio >=10x | 511 | 0.5465 | 0.3785 | 0.4188 | +0.128 | -0.040 | 0.0172 ± 0.0078 |
| thinner_sample 1000-3000 | 889 | 0.5429 | 0.4172 | 0.4668 | +0.076 | -0.050 | 0.007 ± 0.0048 |
| thinner_sample 300-1000 | 745 | 0.5603 | 0.421 | 0.4832 | +0.077 | -0.062 | 0.003 ± 0.0057 |
| thinner_sample <300 | 960 | 0.5431 | 0.3831 | 0.4323 | +0.111 | -0.049 | 0.0173 ± 0.0055 |
| thinner_sample >=3000 | 539 | 0.5305 | 0.4365 | 0.4657 | +0.065 | -0.029 | 0.0133 ± 0.005 |
| data_status ADEQUATE | 919 | 0.534 | 0.429 | 0.4603 | +0.074 | -0.031 | 0.0098 ± 0.0041 |
| data_status LIMITED | 785 | 0.5508 | 0.4216 | 0.4854 | +0.066 | -0.064 | 0.0042 ± 0.0052 |
| data_status POOR | 1429 | 0.5488 | 0.3936 | 0.4458 | +0.103 | -0.052 | 0.014 ± 0.0045 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 482 | 0.1921 | 0.1935 | -0.0014 ± 0.0007 | 0.5621 | 0.5651 | 0.4938 | 0.4791 | 0.5311 | -0.039 ± 0.0209 | -0.01 (5) |
| 3-5 | 303 | 0.1922 | 0.1916 | +0.0006 ± 0.002 | 0.5644 | 0.5616 | 0.5074 | 0.4675 | 0.4785 | -0.082 ± 0.0258 | 0.02 (1) |
| 5-10 | 662 | 0.1976 | 0.1971 | +0.0005 ± 0.0026 | 0.5807 | 0.5774 | 0.5104 | 0.436 | 0.4637 | -0.084 ± 0.0178 | -0.0167 (6) |
| 10-15 | 554 | 0.2134 | 0.2051 | +0.0083 ± 0.0048 | 0.6154 | 0.5921 | 0.5186 | 0.3948 | 0.4224 | -0.084 ± 0.0192 | -0.048 (5) |
| 15-25 | 684 | 0.2303 | 0.2135 | +0.0168 ± 0.0069 | 0.6554 | 0.6122 | 0.5747 | 0.3796 | 0.4357 | -0.084 ± 0.0176 | -0.0033 (9) |
| 25-40 | 370 | 0.2237 | 0.207 | +0.0168 ± 0.0141 | 0.6364 | 0.596 | 0.6468 | 0.3378 | 0.4649 | -0.062 ± 0.0215 | -0.01 (1) |
| 40+ | 78 | 0.3044 | 0.1729 | +0.1315 ± 0.0422 | 0.8211 | 0.5186 | 0.7435 | 0.296 | 0.3718 | -0.122 ± 0.0414 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2263 | 0.1784 | 0.1795 | -0.0012 ± 0.0003 | 0.5306 | 0.5318 | 0.4794 | 0.4644 | 0.498 | -0.021 ± 0.009 | -0.0129 (17) |
| 3-5 | 1404 | 0.192 | 0.1898 | +0.0022 ± 0.0009 | 0.5639 | 0.5544 | 0.4793 | 0.4396 | 0.4302 | -0.066 ± 0.0118 | 0.0 (2) |
| 5-10 | 3063 | 0.1931 | 0.1904 | +0.0026 ± 0.0012 | 0.5688 | 0.5598 | 0.4815 | 0.4076 | 0.4244 | -0.047 ± 0.008 | -0.0119 (21) |
| 10-15 | 2651 | 0.2016 | 0.1831 | +0.0185 ± 0.0021 | 0.5893 | 0.5382 | 0.4797 | 0.3551 | 0.3436 | -0.074 ± 0.0083 | -0.0281 (16) |
| 15-25 | 3230 | 0.2084 | 0.1695 | +0.0388 ± 0.0028 | 0.6088 | 0.5016 | 0.5007 | 0.3044 | 0.3053 | -0.070 ± 0.0072 | -0.0025 (44) |
| 25-40 | 2533 | 0.2214 | 0.1255 | +0.0958 ± 0.0044 | 0.636 | 0.3875 | 0.5287 | 0.2153 | 0.2231 | -0.062 ± 0.0068 | -0.01 (1) |
| 40+ | 1734 | 0.3777 | 0.0424 | +0.3352 ± 0.0055 | 0.9827 | 0.1691 | 0.6266 | 0.1055 | 0.0548 | -0.086 ± 0.0046 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 359 | 0.1973 | 0.1977 | -0.0003 ± 0.0008 | 0.576 | 0.5768 | 0.502 | 0.4868 | 0.507 | -0.080 ± 0.0247 | -0.01 (3) |
| 3-5 | 247 | 0.2081 | 0.2074 | +0.0007 ± 0.0024 | 0.5981 | 0.5978 | 0.5148 | 0.4748 | 0.4818 | -0.077 ± 0.0305 | 0.02 (1) |
| 5-10 | 578 | 0.1986 | 0.1978 | +0.0008 ± 0.0028 | 0.5805 | 0.5785 | 0.5477 | 0.4728 | 0.5052 | -0.072 ± 0.0191 | -0.01 (4) |
| 10-15 | 511 | 0.2174 | 0.2101 | +0.0073 ± 0.0051 | 0.6227 | 0.6059 | 0.5678 | 0.4434 | 0.4795 | -0.087 ± 0.0212 | -0.04 (5) |
| 15-25 | 751 | 0.2278 | 0.208 | +0.0198 ± 0.0066 | 0.6472 | 0.5981 | 0.5872 | 0.3906 | 0.4421 | -0.086 ± 0.0169 | -0.0133 (9) |
| 25-40 | 499 | 0.2667 | 0.1968 | +0.0699 ± 0.0126 | 0.744 | 0.5743 | 0.6595 | 0.3445 | 0.3928 | -0.113 ± 0.0197 | -0.0075 (4) |
| 40+ | 188 | 0.3645 | 0.1762 | +0.1883 ± 0.0302 | 1.0117 | 0.5231 | 0.7405 | 0.2582 | 0.3191 | -0.072 ± 0.0295 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1908 | 0.181 | 0.1813 | -0.0003 ± 0.0003 | 0.5363 | 0.5368 | 0.5015 | 0.4868 | 0.5068 | -0.035 ± 0.0101 | -0.0133 (15) |
| 3-5 | 1205 | 0.1915 | 0.1907 | +0.0008 ± 0.001 | 0.5576 | 0.5557 | 0.5141 | 0.4741 | 0.4838 | -0.040 ± 0.0128 | 0.02 (1) |
| 5-10 | 2729 | 0.1915 | 0.1885 | +0.0029 ± 0.0012 | 0.5654 | 0.5553 | 0.5101 | 0.436 | 0.4551 | -0.042 ± 0.0084 | -0.0117 (6) |
| 10-15 | 2334 | 0.1977 | 0.1861 | +0.0116 ± 0.0022 | 0.5811 | 0.5437 | 0.518 | 0.3935 | 0.4113 | -0.050 ± 0.0091 | -0.0189 (18) |
| 15-25 | 3374 | 0.2158 | 0.1764 | +0.0395 ± 0.0029 | 0.6271 | 0.5201 | 0.5314 | 0.3351 | 0.3361 | -0.072 ± 0.0073 | -0.0086 (42) |
| 25-40 | 3001 | 0.2493 | 0.1361 | +0.1132 ± 0.0043 | 0.7052 | 0.4172 | 0.5589 | 0.243 | 0.2236 | -0.086 ± 0.0067 | -0.0044 (18) |
| 40+ | 2327 | 0.4007 | 0.0656 | +0.3352 ± 0.0061 | 1.0552 | 0.2302 | 0.662 | 0.1252 | 0.095 | -0.069 ± 0.0052 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 465 | 0.1929 | 0.1953 | -0.0024 ± 0.0007 | 0.5646 | 0.5707 | 0.4947 | 0.4795 | 0.5462 | -0.011 ± 0.0209 | -0.0137 (8) |
| 3-5 | 345 | 0.1888 | 0.1867 | +0.0021 ± 0.0019 | 0.5542 | 0.5495 | 0.4957 | 0.4562 | 0.4522 | -0.115 ± 0.0244 | 0.0067 (3) |
| 5-10 | 690 | 0.202 | 0.1974 | +0.0046 ± 0.0025 | 0.5912 | 0.5769 | 0.503 | 0.4292 | 0.4319 | -0.099 ± 0.0173 | -0.0071 (7) |
| 10-15 | 542 | 0.207 | 0.2059 | +0.0011 ± 0.0048 | 0.6014 | 0.5947 | 0.5368 | 0.4138 | 0.4742 | -0.063 ± 0.0193 | -0.0317 (6) |
| 15-25 | 631 | 0.2363 | 0.2097 | +0.0267 ± 0.0071 | 0.6731 | 0.6034 | 0.583 | 0.3897 | 0.4168 | -0.111 ± 0.0181 | -0.03 (1) |
| 25-40 | 385 | 0.2108 | 0.2122 | -0.0014 ± 0.0137 | 0.6086 | 0.6077 | 0.6515 | 0.342 | 0.4961 | -0.043 ± 0.021 | 0.015 (2) |
| 40+ | 75 | 0.3237 | 0.1866 | +0.1371 ± 0.045 | 0.8679 | 0.5501 | 0.7473 | 0.2945 | 0.3733 | -0.107 ± 0.0471 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2162 | 0.1844 | 0.1852 | -0.0009 ± 0.0003 | 0.5441 | 0.5457 | 0.4824 | 0.4671 | 0.4921 | -0.027 ± 0.0093 | -0.0163 (35) |
| 3-5 | 1487 | 0.1864 | 0.1831 | +0.0033 ± 0.0009 | 0.5496 | 0.5419 | 0.4764 | 0.4369 | 0.4156 | -0.083 ± 0.0114 | -0.0094 (18) |
| 5-10 | 3259 | 0.1949 | 0.1878 | +0.0070 ± 0.0011 | 0.5749 | 0.5521 | 0.4795 | 0.4056 | 0.3931 | -0.072 ± 0.0076 | -0.01 (31) |
| 10-15 | 2503 | 0.195 | 0.1804 | +0.0147 ± 0.0021 | 0.5744 | 0.5299 | 0.4961 | 0.3728 | 0.3755 | -0.063 ± 0.0084 | -0.015 (12) |
| 15-25 | 3312 | 0.2092 | 0.1683 | +0.0409 ± 0.0028 | 0.6127 | 0.4994 | 0.5034 | 0.3083 | 0.3025 | -0.075 ± 0.0071 | -0.03 (2) |
| 25-40 | 2487 | 0.2165 | 0.1239 | +0.0926 ± 0.0044 | 0.6251 | 0.382 | 0.5253 | 0.2093 | 0.2248 | -0.058 ± 0.0067 | 0.01 (3) |
| 40+ | 1668 | 0.3929 | 0.0464 | +0.3465 ± 0.0059 | 1.0246 | 0.1798 | 0.6376 | 0.1098 | 0.057 | -0.088 ± 0.005 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 807 | 0.1955 | 0.1956 | -0.0001 ± 0.0005 | 0.5713 | 0.5713 | 0.5084 | 0.4934 | 0.4981 | -0.049 ± 0.0156 | -0.0224 (49) |
| 3-5 | 572 | 0.1941 | 0.1932 | +0.0009 ± 0.0015 | 0.5661 | 0.5627 | 0.4805 | 0.4407 | 0.4476 | -0.051 ± 0.0185 | -0.0194 (34) |
| 5-10 | 1202 | 0.1971 | 0.1911 | +0.0061 ± 0.0019 | 0.5815 | 0.5639 | 0.4881 | 0.4145 | 0.411 | -0.065 ± 0.0129 | -0.005 (78) |
| 10-15 | 762 | 0.2071 | 0.196 | +0.0111 ± 0.004 | 0.6025 | 0.5736 | 0.5064 | 0.3833 | 0.399 | -0.054 ± 0.0162 | 0.0014 (64) |
| 15-25 | 1013 | 0.2337 | 0.2113 | +0.0224 ± 0.0057 | 0.6661 | 0.6086 | 0.5655 | 0.3706 | 0.4116 | -0.058 ± 0.0145 | -0.0214 (59) |
| 25-40 | 584 | 0.2495 | 0.1956 | +0.0539 ± 0.0113 | 0.7039 | 0.569 | 0.647 | 0.3347 | 0.4024 | -0.080 ± 0.017 | -0.0219 (26) |
| 40+ | 197 | 0.3744 | 0.1904 | +0.1840 ± 0.0317 | 1.0791 | 0.5615 | 0.7924 | 0.3009 | 0.3807 | -0.079 ± 0.0285 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2424 | 0.1868 | 0.1868 | -0.0000 ± 0.0003 | 0.5487 | 0.5478 | 0.5036 | 0.4883 | 0.4983 | -0.034 ± 0.0088 | -0.0157 (88) |
| 3-5 | 1660 | 0.1879 | 0.1853 | +0.0025 ± 0.0008 | 0.5503 | 0.5444 | 0.4864 | 0.4468 | 0.4355 | -0.057 ± 0.0106 | -0.0209 (69) |
| 5-10 | 3355 | 0.1931 | 0.1852 | +0.0080 ± 0.0011 | 0.5711 | 0.5483 | 0.4821 | 0.4085 | 0.3943 | -0.066 ± 0.0075 | -0.0082 (132) |
| 10-15 | 2252 | 0.2035 | 0.1893 | +0.0141 ± 0.0023 | 0.5944 | 0.5569 | 0.5114 | 0.3883 | 0.3925 | -0.055 ± 0.0092 | -0.0053 (105) |
| 15-25 | 2831 | 0.2304 | 0.1976 | +0.0328 ± 0.0033 | 0.664 | 0.5745 | 0.5565 | 0.3613 | 0.3765 | -0.063 ± 0.0084 | -0.0253 (107) |
| 25-40 | 1918 | 0.254 | 0.1695 | +0.0845 ± 0.0059 | 0.7196 | 0.5014 | 0.608 | 0.294 | 0.3186 | -0.076 ± 0.0091 | -0.0229 (51) |
| 40+ | 926 | 0.3873 | 0.13 | +0.2573 ± 0.0126 | 1.0958 | 0.3982 | 0.7093 | 0.2027 | 0.2149 | -0.072 ± 0.0113 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3133 | 1.056 ± 0.05 | 1.17 | 0.1685 | 0.1716 | 0.2119 | 0.2016 |
| gen2 | 3133 | 0.856 ± 0.045 | 1.131 | 0.1758 | 0.1716 | 0.2301 | 0.2015 |
| gen1_elo | 3133 | 1.039 ± 0.049 | 1.153 | 0.1737 | 0.172 | 0.211 | 0.2014 |
| gen1_sr | 3133 | 1.06 ± 0.059 | 1.192 | 0.1354 | 0.1733 | 0.2261 | 0.2013 |
| gen1_ledger | 5137 | 0.876 ± 0.034 | 1.077 | 0.1777 | 0.1858 | 0.218 | 0.1972 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 14,769)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,679 | 24.9% |
| STALE_QUOTE | market_freshness | 3,061 | 20.7% |
| BOOK_QUALITY | execution | 2,641 | 17.9% |
| POOR_DATA | data | 1,618 | 11.0% |
| LIMITED_DATA | data | 1,064 | 7.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 788 | 5.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 709 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 611 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 417 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 181 | 1.2% |

Cause class: coverage 24.9%, market_freshness 20.7%, data 18.2%, execution 17.9%, market_freshness/coverage 8.2%, model_calibration_or_unknown 4.8%, mapping 4.1%, model_calibration 1.2%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.8%, START_UNVERIFIABLE 95.5%, LOW_DATA_QUALITY 69.0%, THIN_PLAYER_HISTORY 57.6%, STALE_PLAYER_DATA 51.8%, STALE_KALSHI_QUOTE 45.2%, MODEL_INTERNAL_DISAGREEMENT 39.6%, ASYMMETRIC_SAMPLE_SIZE 31.6%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 17.7%, PLAYER_IDENTITY_RISK 14.4%, LEVEL_TRANSFER_RISK 8.3%, EVENT_MAPPING_RISK 8.0%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 3.5%, EXTERNAL_MARKET_REJECTION 2.1%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 27.3%, POST_SETTLEMENT_OBSERVATION 24.9%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 7,949)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,910 | 36.6% |
| STALE_QUOTE | market_freshness | 1,436 | 18.1% |
| BOOK_QUALITY | execution | 1,385 | 17.4% |
| POOR_DATA | data | 671 | 8.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 425 | 5.3% |
| IDENTITY_AMBIGUOUS | mapping | 352 | 4.4% |
| LIMITED_DATA | data | 318 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 255 | 3.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 158 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 39 | 0.5% |

Cause class: coverage 36.6%, market_freshness 18.1%, execution 17.4%, data 12.4%, market_freshness/coverage 8.6%, mapping 4.4%, model_calibration_or_unknown 2.0%, model_calibration 0.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.8%, START_UNVERIFIABLE 97.9%, LOW_DATA_QUALITY 72.7%, THIN_PLAYER_HISTORY 60.0%, STALE_KALSHI_QUOTE 53.6%, STALE_PLAYER_DATA 46.9%, MODEL_INTERNAL_DISAGREEMENT 40.6%, ASYMMETRIC_SAMPLE_SIZE 33.4%, WIDE_SPREAD 23.3%, MODEL_HIGH_UNCERTAINTY 18.1%, PLAYER_IDENTITY_RISK 17.7%, EVENT_MAPPING_RISK 9.7%, LOW_DISPLAYED_LIQUIDITY 8.1%, LEVEL_TRANSFER_RISK 7.3%, MODEL_CALIBRATION_OUTLIER 4.5%, EXTERNAL_MARKET_REJECTION 1.1%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 39.3%, POST_SETTLEMENT_OBSERVATION 36.6%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 6343, "IDENTITY_AMBIGUOUS": 1606}; ticker orientation: {"VERIFIED": 7949}.

Checks: discipline:AMBIGUOUS 546, discipline:PASS 7403, identity_confidence:AMBIGUOUS 1406, identity_confidence:PASS 6543, level_mapping:NA 558, level_mapping:PASS 7391, market_pair:AMBIGUOUS 284, market_pair:NA 202, market_pair:PASS 7463, model_complement:NA 169, model_complement:PASS 7780, namesake:PASS 7949, physical_match_id:NA 2964, physical_match_id:PASS 4985, player_ids:PASS 7949, same_pair_other_event:PASS 7949, ticker_orientation:PASS 7949

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,377 | 2.3% | 2.2% | 0.7% | {"market_freshness": 24, "execution": 11, "data": 11, "model_calibration_or_unknown": 5, "market_freshness/coverage": 2, "coverage": 2} | 5.4 | 0.208 / 0.2083 (273) | 15.8% | 1.7% | 5.0% | 1.7% |
| CHALLENGER | 5,625 | 16.9% | 5.8% | 12.0% | {"coverage": 581, "market_freshness/coverage": 121, "market_freshness": 112, "data": 64, "model_calibration_or_unknown": 46, "execution": 13, "model_calibration": 9, "mapping": 6} | 7.04 | 0.2171 / 0.2043 (1463) | 36.9% | 9.5% | 2.4% | 22.7% |
| DOUBLES | 1,121 | 48.7% | 48.3% | 6.9% | {"execution": 232, "mapping": 161, "market_freshness": 106, "market_freshness/coverage": 40, "coverage": 7} | 23.93 | 0.3243 / 0.2324 (330) | 20.9% | 0.0% | 100.0% | 7.8% |
| ITF_MEN | 10,630 | 24.6% | 16.9% | 33.0% | {"coverage": 1024, "execution": 527, "market_freshness": 407, "data": 358, "market_freshness/coverage": 205, "mapping": 97, "model_calibration_or_unknown": 2} | 11.13 | 0.2135 / 0.1942 (2596) | 36.3% | 61.3% | 12.5% | 22.7% |
| ITF_WOMEN | 13,142 | 26.5% | 19.1% | 43.8% | {"coverage": 1279, "market_freshness": 712, "execution": 573, "data": 522, "market_freshness/coverage": 263, "mapping": 82, "model_calibration_or_unknown": 43, "model_calibration": 10} | 12.57 | 0.2035 / 0.1913 (2757) | 39.2% | 56.6% | 10.0% | 22.6% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,904 | 5.7% | 5.1% | 1.4% | {"market_freshness": 36, "model_calibration_or_unknown": 23, "execution": 15, "data": 11, "market_freshness/coverage": 10, "model_calibration": 9, "coverage": 4, "mapping": 1} | 7.48 | 0.2329 / 0.2282 (337) | 24.0% | 1.8% | 1.9% | 3.1% |
| WTA125 | 1,366 | 12.5% | 9.8% | 2.1% | {"market_freshness/coverage": 38, "model_calibration_or_unknown": 37, "market_freshness": 37, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.2172 / 0.2063 (472) | 22.8% | 7.5% | 4.7% | 10.0% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 5 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 6 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 7 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 9 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 10 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 11 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 12 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 13 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 14 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 15 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 16 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 17 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 18 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 19 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 20 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 22 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 23 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 24 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 25 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 26 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 27 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 28 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 92 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 29 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 30 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 31 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 32 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 33 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 162 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 34 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 35 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 765 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 36 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 37 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 38 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 33 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 39 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 40 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 41 | `KXITFWMATCH-26OCT16ESTLAB-LAB` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 68 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1475.0, ratio 2.28); no external reference |
| 42 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 43 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 44 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 45 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 624 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 46 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 47 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 48 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 49 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 50 | `KXATPCHALLENGERMATCH-26OCT13GIUSEA-SEA` | CHALLENGER | fair_v1 | 76% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 243 min (STALE); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9794, "by_level_share_of_ge_25pp": {"ATP": 0.0069, "CHALLENGER": 0.1198, "DOUBLES": 0.0687, "ITF_MEN": 0.3296, "ITF_WOMEN": 0.4383, "OTHER": 0.0015, "WTA": 0.0137, "WTA125": 0.0215}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5365, "share_primary_cause_market_settled_or_in_play": 0.4517, "share_primary_cause_stale_quote_only": 0.1807}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 7949, "identity_ambiguous_share": 0.202, "ticker_orientation": {"VERIFIED": 7949}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 4985, "with_external": 197, "coverage": 0.0395, "external_status": {"EXTERNAL_STALE": 135, "AGREES_WITH_KALSHI": 59, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 135, "MODEL_LONE_OUTLIER": 59, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.2995, "share_external_supports_model": 0.0152}, "pregame_clean_ge_25pp": {"n": 2369, "with_external": 186, "coverage": 0.0785, "external_status": {"EXTERNAL_STALE": 126, "AGREES_WITH_KALSHI": 57, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 126, "MODEL_LONE_OUTLIER": 57, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3065, "share_external_supports_model": 0.0161}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 565.0, "median_sample_ratio": 2.35, "median_min_matches": 20.5, "median_max_days_since_last": 204.5, "share_severe_asymmetry": 0.2028, "data_status": {"POOR": 4227, "LIMITED": 2270, "ADEQUATE": 1452}, "comparison_lt_10pp": {"median_thinner_serve_points": 1841.0, "median_sample_ratio": 1.67, "median_min_matches": 91.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 632, "model_minus_observed": 0.0539, "kalshi_minus_observed": -0.0801, "brier_diff_model_minus_kalshi": 0.0016}, "4-10x": {"n": 423, "model_minus_observed": 0.0779, "kalshi_minus_observed": -0.0594, "brier_diff_model_minus_kalshi": 0.008}, "<2x": {"n": 1567, "model_minus_observed": 0.0856, "kalshi_minus_observed": -0.0364, "brier_diff_model_minus_kalshi": 0.0122}, ">=10x": {"n": 511, "model_minus_observed": 0.1277, "kalshi_minus_observed": -0.0403, "brier_diff_model_minus_kalshi": 0.0172}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3133, "model": {"intercept": -0.548, "slope": 0.856, "slope_se": 0.045}, "kalshi_mid_same_rows": {"intercept": 0.229, "slope": 1.131, "slope_se": 0.052}, "mean_extremity_model": 0.1758, "mean_extremity_kalshi": 0.1716, "model_brier": 0.2301, "kalshi_brier": 0.2015, "brier_diff_model_minus_kalshi": 0.0285, "brier_diff_se": 0.0034, "model_logloss": 0.6561, "kalshi_logloss": 0.585}, "fair_v1": {"n": 3133, "model": {"intercept": -0.413, "slope": 1.056, "slope_se": 0.05}, "kalshi_mid_same_rows": {"intercept": 0.301, "slope": 1.17, "slope_se": 0.053}, "mean_extremity_model": 0.1685, "mean_extremity_kalshi": 0.1716, "model_brier": 0.2119, "kalshi_brier": 0.2016, "brier_diff_model_minus_kalshi": 0.0103, "brier_diff_se": 0.0027, "model_logloss": 0.6113, "kalshi_logloss": 0.5849}, "gen1_elo": {"n": 3133, "model": {"intercept": -0.411, "slope": 1.039, "slope_se": 0.049}, "kalshi_mid_same_rows": {"intercept": 0.285, "slope": 1.153, "slope_se": 0.052}, "mean_extremity_model": 0.1737, "mean_extremity_kalshi": 0.172, "model_brier": 0.211, "kalshi_brier": 0.2014, "brier_diff_model_minus_kalshi": 0.0095, "brier_diff_se": 0.0027, "model_logloss": 0.6102, "kalshi_logloss": 0.5845}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2458, "share_ge_15": 0.4375, "median_abs_gap": 13.0, "n": 20282}, "gen1_elo": {"share_ge_25": 0.2393, "share_ge_15": 0.4314, "median_abs_gap": 12.5, "n": 20282}, "gen1_sr": {"share_ge_25": 0.308, "share_ge_15": 0.5227, "median_abs_gap": 15.87, "n": 20282}, "gen2": {"share_ge_25": 0.3092, "share_ge_15": 0.5087, "median_abs_gap": 15.43, "n": 20282}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1513, "share_ge_15": 0.3489, "median_abs_gap": 10.64, "n": 15653}, "gen1_elo": {"share_ge_25": 0.1483, "share_ge_15": 0.3388, "median_abs_gap": 10.11, "n": 15652}, "gen1_sr": {"share_ge_25": 0.2142, "share_ge_15": 0.4438, "median_abs_gap": 13.17, "n": 15653}, "gen2": {"share_ge_25": 0.2274, "share_ge_15": 0.4404, "median_abs_gap": 13.0, "n": 15654}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.4, "share_ge_25_all": 0.0231, "share_ge_25_pregame_clean": 0.0218}, "WTA": {"median_abs_gap_pregame_clean": 7.48, "share_ge_25_all": 0.0572, "share_ge_25_pregame_clean": 0.0515}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2405, "share_within_10pp_all": 0.4402, "share_within_10pp_pregame_clean": 0.4978, "corr_model_vs_mid_pregame_clean": 0.8432}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 482, "model_brier": 0.1921, "kalshi_brier": 0.1935, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 554, "model_brier": 0.2134, "kalshi_brier": 0.2051, "brier_diff_model_minus_kalshi": 0.0083}, "15-25": {"n_settled": 684, "model_brier": 0.2303, "kalshi_brier": 0.2135, "brier_diff_model_minus_kalshi": 0.0168}, "25-40": {"n_settled": 370, "model_brier": 0.2237, "kalshi_brier": 0.207, "brier_diff_model_minus_kalshi": 0.0168}, "3-5": {"n_settled": 303, "model_brier": 0.1922, "kalshi_brier": 0.1916, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 78, "model_brier": 0.3044, "kalshi_brier": 0.1729, "brier_diff_model_minus_kalshi": 0.1315}, "5-10": {"n_settled": 662, "model_brier": 0.1976, "kalshi_brier": 0.1971, "brier_diff_model_minus_kalshi": 0.0005}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.548, "slope": 0.856, "slope_se": 0.045}, "kalshi_slope": {"intercept": 0.229, "slope": 1.131, "slope_se": 0.052}, "n": 3133}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.522, "slope": 0.876, "slope_se": 0.034}, "kalshi_slope": {"intercept": 0.136, "slope": 1.077, "slope_se": 0.039}, "n": 5137}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 330, "model_brier": 0.3243, "kalshi_brier": 0.2324, "brier_diff_model_minus_kalshi": 0.0919, "brier_diff_se": 0.0173, "corr_model_outcome": 0.0188, "corr_kalshi_outcome": 0.2663}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
