# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-17T16:09Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 36,529): 0-3 14.5%, 3-5 9.5%, 5-10 19.9%, 10-15 15.3%, 15-25 18.8%, 25-40 13.6%, 40+ 8.3%; median gap 11.86 pp.
* **Where the extremes live**: 97.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.7%, Challenger 12.0%, doubles 6.9%). Main tour: ATP 2.4% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 8,008): MARKET_ALREADY_SETTLED_WHEN_PRICED 36.6%, STALE_QUOTE 17.9%, BOOK_QUALITY 17.6%, POOR_DATA 8.4%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.4%, LIMITED_DATA 3.9%, IN_PLAY_QUOTE 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.5%. By class: coverage 36.6%, market_freshness 17.9%, execution 17.6%, data 12.3%, market_freshness/coverage 8.7%, mapping 4.4%, model_calibration_or_unknown 2.0%, model_calibration 0.5%.
* **Stale / settled / in-play**: 53.5% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 45.3% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 8,008 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.3% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 3.9%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 23.0% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 565.0 points vs 1841.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.05, Gen-2 0.852, Gen-1 ledger 0.874 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 371 model 0.2243 vs Kalshi 0.2068; n 78 model 0.3044 vs Kalshi 0.1729.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 147,718 model-market comparisons (244,364 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 52,469 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-17T16:02:48.038900+00:00'], shadow board 40,556 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-17T16:02:50.783815+00:00'], Model 4 16,229 rows, 15,504 settled tickers, 5,246 tickers with an external scan.
* By model: {"gen1_ledger": 34825, "gen1_elo": 20398, "fair_v1": 20398, "gen2": 20398, "gen1_sr": 20398, "model4_fundamental": 15655, "model4_conditioned": 15646}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 36,529 | 14.5 | 9.5 | 19.9 | 15.3 | 18.8 | 13.6 | 8.3 | 11.86 | 40.7% | 21.9% |
| MW fair_v1 | 20,398 | 13.5 | 8.5 | 18.5 | 15.7 | 19.2 | 14.6 | 10.0 | 13.0 | 43.8% | 24.6% |
| MW gen1_elo | 20,398 | 13.1 | 9.0 | 19.6 | 15.1 | 19.2 | 14.3 | 9.6 | 12.51 | 43.2% | 23.9% |
| MW gen1_ledger | 16,131 | 15.7 | 10.8 | 21.8 | 14.8 | 18.3 | 12.4 | 6.1 | 10.4 | 36.8% | 18.5% |
| MW gen1_sr | 20,398 | 9.7 | 7.5 | 16.4 | 14.1 | 21.5 | 18.7 | 12.2 | 15.89 | 52.3% | 30.8% |
| MW gen2 | 20,398 | 11.4 | 7.1 | 16.5 | 14.1 | 19.9 | 17.6 | 13.4 | 15.45 | 50.9% | 31.0% |
| all families model4_conditioned | 15,646 | 21.4 | 19.5 | 34.5 | 17.1 | 4.7 | 1.5 | 1.1 | 5.9 | 7.4% | 2.6% |
| all families model4_fundamental | 15,655 | 16.5 | 13.2 | 34.8 | 19.9 | 11.1 | 3.2 | 1.4 | 7.77 | 15.7% | 4.6% |

Configurable thresholds (primary): >=5pp 76.0%, >=10pp 56.0%, >=15pp 40.7%, >=20pp 30.3%, >=25pp 21.9%, >=30pp 15.9%, >=40pp 8.3%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.46pp; >=10pp 45.3%, >=25pp 17.5%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,527 | 30.0 | 13.9 | 24.9 | 17.3 | 10.9 | 2.2 | 0.8 | 5.98 | 13.9% | 2.9% |
| CHALLENGER | 3,347 | 15.9 | 10.1 | 20.2 | 15.7 | 14.4 | 12.2 | 11.5 | 11.37 | 38.1% | 23.8% |
| ITF_MEN | 5,791 | 10.9 | 8.1 | 17.5 | 14.8 | 19.9 | 16.4 | 12.5 | 14.54 | 48.8% | 28.9% |
| ITF_WOMEN | 7,966 | 10.4 | 6.7 | 15.9 | 15.5 | 22.2 | 18.1 | 11.3 | 15.61 | 51.5% | 29.3% |
| WTA | 1,120 | 20.2 | 12.4 | 24.4 | 17.1 | 19.6 | 5.3 | 1.0 | 8.02 | 25.9% | 6.2% |
| WTA125 | 647 | 13.0 | 7.6 | 24.0 | 20.1 | 20.1 | 13.3 | 2.0 | 11.08 | 35.4% | 15.3% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,527 | 23.8 | 14.5 | 24.5 | 18.7 | 14.4 | 3.0 | 1.2 | 6.9 | 18.5% | 4.1% |
| CHALLENGER | 3,347 | 14.8 | 8.2 | 19.3 | 13.7 | 17.7 | 14.2 | 12.1 | 12.67 | 44.0% | 26.3% |
| ITF_MEN | 5,791 | 9.3 | 6.7 | 15.7 | 13.6 | 19.8 | 19.5 | 15.4 | 16.96 | 54.7% | 34.8% |
| ITF_WOMEN | 7,966 | 8.6 | 5.7 | 13.8 | 13.2 | 21.1 | 20.8 | 16.9 | 18.87 | 58.7% | 37.6% |
| WTA | 1,120 | 17.2 | 8.0 | 20.5 | 15.4 | 22.6 | 15.2 | 1.1 | 11.59 | 38.8% | 16.2% |
| WTA125 | 647 | 6.3 | 4.8 | 17.3 | 17.8 | 25.8 | 19.0 | 9.0 | 16.74 | 53.8% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,527 | 26.9 | 13.8 | 27.2 | 16.3 | 12.2 | 2.8 | 0.8 | 6.47 | 15.8% | 3.6% |
| CHALLENGER | 3,347 | 14.8 | 10.3 | 20.8 | 15.0 | 15.5 | 11.9 | 11.7 | 11.02 | 39.1% | 23.6% |
| ITF_MEN | 5,791 | 9.9 | 8.1 | 17.9 | 14.1 | 20.6 | 16.8 | 12.6 | 14.98 | 50.0% | 29.3% |
| ITF_WOMEN | 7,966 | 9.8 | 6.9 | 16.5 | 15.5 | 22.8 | 18.1 | 10.4 | 15.5 | 51.2% | 28.5% |
| WTA | 1,120 | 23.2 | 16.2 | 31.7 | 15.2 | 10.9 | 2.1 | 0.6 | 6.05 | 13.7% | 2.8% |
| WTA125 | 647 | 22.1 | 12.4 | 29.7 | 15.6 | 14.1 | 5.9 | 0.3 | 7.73 | 20.2% | 6.2% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 903 | 29.5 | 20.9 | 33.4 | 11.5 | 3.1 | 1.4 | 0.1 | 4.93 | 4.7% | 1.6% |
| CHALLENGER | 2,291 | 22.7 | 15.3 | 27.5 | 14.5 | 12.8 | 5.2 | 2.0 | 6.88 | 20.0% | 7.1% |
| DOUBLES | 1,137 | 5.2 | 4.0 | 10.8 | 11.0 | 20.3 | 25.2 | 23.5 | 24.11 | 69.0% | 48.7% |
| ITF_MEN | 4,867 | 14.7 | 8.6 | 20.6 | 15.6 | 20.8 | 12.6 | 7.1 | 11.86 | 40.4% | 19.6% |
| ITF_WOMEN | 5,255 | 11.8 | 9.2 | 19.3 | 14.9 | 22.3 | 16.5 | 5.9 | 13.06 | 44.8% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 810 | 21.4 | 16.7 | 28.9 | 16.8 | 11.5 | 4.4 | 0.4 | 6.97 | 16.3% | 4.8% |
| WTA125 | 719 | 21.3 | 13.8 | 22.4 | 18.5 | 14.1 | 7.9 | 2.1 | 8.19 | 24.1% | 10.0% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,498 | 30.2 | 14.0 | 25.2 | 17.2 | 10.9 | 1.8 | 0.8 | 5.93 | 13.5% | 2.6% |
| CHALLENGER | 2,378 | 20.6 | 12.8 | 25.5 | 18.0 | 14.9 | 5.8 | 2.3 | 8.12 | 23.0% | 8.2% |
| ITF_MEN | 4,197 | 13.3 | 10.0 | 20.9 | 16.7 | 20.2 | 13.3 | 5.6 | 11.56 | 39.1% | 18.9% |
| ITF_WOMEN | 5,916 | 12.3 | 8.1 | 18.2 | 17.7 | 23.6 | 15.0 | 5.1 | 13.11 | 43.7% | 20.1% |
| WTA | 1,098 | 20.3 | 11.8 | 24.7 | 17.2 | 19.8 | 5.2 | 1.0 | 8.09 | 26.0% | 6.2% |
| WTA125 | 621 | 13.4 | 7.4 | 23.5 | 20.4 | 20.8 | 12.9 | 1.6 | 11.2 | 35.3% | 14.5% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,498 | 23.8 | 14.7 | 24.6 | 18.8 | 14.3 | 2.7 | 1.1 | 6.86 | 18.2% | 3.8% |
| CHALLENGER | 2,378 | 19.0 | 10.6 | 24.2 | 16.5 | 18.0 | 9.3 | 2.5 | 9.02 | 29.8% | 11.8% |
| ITF_MEN | 4,198 | 11.0 | 8.0 | 18.1 | 15.4 | 22.0 | 17.1 | 8.4 | 14.13 | 47.5% | 25.5% |
| ITF_WOMEN | 5,916 | 9.7 | 6.5 | 15.4 | 14.6 | 23.1 | 20.1 | 10.7 | 16.45 | 53.9% | 30.7% |
| WTA | 1,098 | 17.1 | 7.9 | 20.5 | 15.4 | 22.7 | 15.3 | 1.1 | 11.64 | 39.1% | 16.4% |
| WTA125 | 621 | 6.1 | 5.0 | 17.4 | 18.2 | 25.8 | 19.5 | 8.1 | 16.64 | 53.3% | 27.5% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 873 | 29.7 | 21.2 | 33.9 | 11.7 | 2.3 | 1.1 | 0.1 | 4.91 | 3.5% | 1.3% |
| CHALLENGER | 1,970 | 24.6 | 16.6 | 29.6 | 14.2 | 12.0 | 2.4 | 0.5 | 6.24 | 14.9% | 2.9% |
| DOUBLES | 1,047 | 5.2 | 4.1 | 11.1 | 11.2 | 20.1 | 25.4 | 22.8 | 23.94 | 68.4% | 48.2% |
| ITF_MEN | 4,020 | 16.1 | 9.4 | 22.5 | 16.5 | 20.6 | 10.6 | 4.2 | 10.57 | 35.4% | 14.8% |
| ITF_WOMEN | 4,306 | 12.9 | 10.0 | 21.0 | 15.8 | 22.6 | 14.9 | 2.9 | 11.66 | 40.4% | 17.8% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 773 | 21.7 | 17.2 | 29.1 | 16.8 | 11.6 | 3.5 | 0.0 | 6.8 | 15.1% | 3.5% |
| WTA125 | 609 | 23.3 | 15.3 | 24.0 | 20.0 | 12.3 | 4.8 | 0.3 | 7.25 | 17.4% | 5.1% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,137 | 5.2 | 4.0 | 10.8 | 11.0 | 20.3 | 25.2 | 23.5 | 24.11 | 69.0% | 48.7% |
| singles | 14,994 | 16.5 | 11.3 | 22.7 | 15.1 | 18.1 | 11.4 | 4.8 | 9.86 | 34.4% | 16.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 4,757 | 13.3 | 8.9 | 19.2 | 15.6 | 18.1 | 14.6 | 10.3 | 12.79 | 43.0% | 24.9% |
| Grass | 232 | 10.3 | 11.2 | 18.1 | 13.8 | 23.7 | 15.1 | 7.8 | 14.16 | 46.6% | 22.8% |
| Hard | 13,224 | 13.9 | 8.6 | 18.5 | 15.3 | 19.5 | 14.4 | 9.9 | 12.96 | 43.8% | 24.2% |
| UNKNOWN | 2,185 | 12.1 | 7.3 | 16.8 | 18.3 | 19.0 | 15.9 | 10.7 | 13.49 | 45.5% | 26.5% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,011 | 19.7 | 10.8 | 21.2 | 17.1 | 15.7 | 8.9 | 6.6 | 9.46 | 31.2% | 15.5% |
| B | 2,673 | 13.7 | 9.1 | 19.6 | 16.3 | 18.4 | 12.2 | 10.8 | 12.14 | 41.4% | 23.0% |
| C | 2,965 | 12.6 | 9.7 | 19.8 | 13.9 | 19.0 | 14.8 | 10.2 | 12.73 | 44.0% | 25.0% |
| D | 3,436 | 11.8 | 8.0 | 17.4 | 15.8 | 21.9 | 15.4 | 9.9 | 13.94 | 47.1% | 25.3% |
| F | 5,313 | 8.0 | 5.4 | 14.8 | 14.7 | 22.0 | 21.6 | 13.5 | 18.01 | 57.0% | 35.1% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,806 | 23.1 | 15.9 | 28.9 | 15.2 | 11.0 | 4.3 | 1.6 | 6.66 | 16.8% | 5.9% |
| B | 2,374 | 14.9 | 10.1 | 24.0 | 16.5 | 19.4 | 10.9 | 4.2 | 10.18 | 34.5% | 15.1% |
| C | 3,201 | 12.0 | 7.8 | 17.7 | 14.5 | 21.0 | 16.0 | 11.1 | 14.03 | 48.1% | 27.1% |
| D | 2,343 | 14.2 | 9.8 | 20.7 | 13.7 | 21.2 | 13.7 | 6.7 | 11.85 | 41.7% | 20.4% |
| F | 3,407 | 10.5 | 7.6 | 15.1 | 14.1 | 23.3 | 20.6 | 8.9 | 16.21 | 52.7% | 29.4% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 6,809 | 17.9 | 9.7 | 20.4 | 16.8 | 16.2 | 9.8 | 9.1 | 10.53 | 35.1% | 18.9% |
| LIMITED | 4,705 | 14.6 | 10.5 | 20.6 | 15.1 | 18.5 | 13.2 | 7.6 | 11.33 | 39.2% | 20.7% |
| POOR | 8,884 | 9.6 | 6.5 | 15.9 | 15.2 | 21.9 | 19.0 | 12.0 | 16.04 | 52.9% | 31.0% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,529 | 29.5 | 23.5 | 35.2 | 8.0 | 2.5 | 1.1 | 0.2 | 4.72 | 3.8% | 1.3% |
| GAME_SPREAD | 3,180 | 25.0 | 15.8 | 35.8 | 17.8 | 4.6 | 0.8 | 0.2 | 6.09 | 5.7% | 1.1% |
| MATCH_WINNER | 16,131 | 15.7 | 10.8 | 21.8 | 14.8 | 18.3 | 12.4 | 6.1 | 10.4 | 36.8% | 18.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 6,809 | 31.8 | 18.8 | 30.7 | 11.0 | 6.0 | 1.2 | 0.5 | 4.9 | 7.7% | 1.7% |
| TOTAL_GAMES | 5,152 | 6.7 | 8.8 | 37.4 | 28.9 | 11.8 | 3.6 | 2.9 | 9.68 | 18.3% | 6.5% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,429 | 25.4 | 37.0 | 31.3 | 1.5 | 3.8 | 0.7 | 0.2 | 4.34 | 4.8% | 0.9% |
| GAME_SPREAD | 3,799 | 45.2 | 16.3 | 28.4 | 7.7 | 1.4 | 0.7 | 0.3 | 3.56 | 2.4% | 1.1% |
| TOTAL_GAMES | 6,418 | 3.9 | 6.6 | 41.0 | 36.0 | 7.5 | 2.7 | 2.4 | 9.86 | 12.5% | 5.0% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,429 | 26.0 | 18.1 | 36.5 | 9.8 | 6.8 | 2.5 | 0.4 | 5.59 | 9.7% | 2.9% |
| GAME_SPREAD | 3,799 | 19.2 | 13.3 | 29.5 | 21.1 | 13.2 | 2.7 | 1.0 | 7.85 | 16.9% | 3.7% |
| TOTAL_GAMES | 6,427 | 6.9 | 8.9 | 36.5 | 27.7 | 13.5 | 4.1 | 2.5 | 9.76 | 20.1% | 6.6% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 20,398 | 43.8% | 24.6% | 13.0 | 34.9% | 15.1% | 10.65 |
| gen1_elo | 20,398 | 43.2% | 23.9% | 12.51 | 33.9% | 14.8% | 10.12 |
| gen1_sr | 20,398 | 52.3% | 30.8% | 15.89 | 44.4% | 21.4% | 13.18 |
| gen2 | 20,398 | 50.9% | 31.0% | 15.45 | 44.1% | 22.8% | 13.0 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 10,915 | 16.5 | 10.5 | 21.6 | 17.2 | 19.6 | 11.4 | 3.3 | 10.43 | 34.3% | 14.7% |
| STALE | 9,483 | 10.1 | 6.3 | 14.9 | 13.9 | 18.8 | 18.3 | 17.7 | 17.45 | 54.8% | 36.0% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 9,599 | 17.5 | 11.6 | 23.3 | 14.9 | 16.8 | 11.2 | 4.7 | 9.4 | 32.7% | 15.9% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 36,529 | 9599 | 14387 | 12543 | 23.9 | 158.7 | 1400.4 |
| ge_15pp | 14,875 | 3141 | 5028 | 6706 | 26.6 | 459.9 | 1380.4 |
| ge_25pp | 8,008 | 1526 | 2195 | 4287 | 34.4 | 597.4 | 1380.4 |
| lt_10pp | 16,062 | 5031 | 6926 | 4105 | 22.0 | 47.9 | 1341.5 |

Current slate `SL-20261017T160902Z-feb7bff7`: 544 priced rows, quote age at build {'median': 6.6, 'max': 6.6}, freshness {'FRESH': 544}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 11 | 0.0 | 0.0 | 36.4 | 0.0 | 45.5 | 18.2 | 0.0 | 20.19 | 63.6% | 18.2% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,799 | 21.5 | 10.8 | 23.0 | 18.3 | 18.8 | 7.0 | 0.6 | 8.64 | 26.4% | 7.6% |
| KALSHI_LONE_OUTLIER | 10 | 10.0 | 0.0 | 70.0 | 0.0 | 10.0 | 10.0 | 0.0 | 5.17 | 20.0% | 10.0% |
| MARKETS_AGREE | 327 | 69.1 | 30.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.11 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 646 | 0.0 | 3.2 | 35.9 | 28.0 | 23.7 | 8.4 | 0.8 | 11.68 | 32.8% | 9.1% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 20,398 | 2805 (13.8%) | 23.0% | 0.7% | {"EXTERNAL_STALE": 1799, "AGREES_WITH_KALSHI": 646, "ALL_AGREE": 327, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 10, "AGREES_WITH_MODEL": 10, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 8,935 | 696 (7.8%) | 30.5% | 1.3% | {"EXTERNAL_STALE": 475, "AGREES_WITH_KALSHI": 212, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 5,020 | 198 (3.9%) | 29.8% | 1.5% | {"EXTERNAL_STALE": 136, "AGREES_WITH_KALSHI": 59, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,374 | 186 (7.8%) | 30.6% | 1.6% | {"EXTERNAL_STALE": 126, "AGREES_WITH_KALSHI": 57, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 8,262 | 1599 (19.4%) | 15.8% | 0.7% | {"EXTERNAL_STALE": 995, "ALL_AGREE": 327, "AGREES_WITH_KALSHI": 253, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 8, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,946 | 11.2 | 7.7 | 19.4 | 14.8 | 21.9 | 14.5 | 10.5 | 13.83 | 46.9% | 25.0% |
| 4-10x | 2,616 | 12.8 | 8.9 | 19.8 | 15.2 | 18.9 | 14.9 | 9.5 | 12.69 | 43.3% | 24.4% |
| <2x | 10,684 | 15.3 | 9.3 | 18.8 | 16.7 | 17.7 | 13.0 | 9.1 | 11.91 | 39.8% | 22.1% |
| >=10x | 3,152 | 10.9 | 6.4 | 15.0 | 13.7 | 21.3 | 19.7 | 13.0 | 16.54 | 54.0% | 32.7% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 5,447 | 13.4 | 8.3 | 19.3 | 15.9 | 19.6 | 13.1 | 10.4 | 12.83 | 43.2% | 23.5% |
| 300-1000 | 4,526 | 12.0 | 8.7 | 17.3 | 15.7 | 20.8 | 15.9 | 9.7 | 13.75 | 46.4% | 25.5% |
| <300 | 6,022 | 9.0 | 6.0 | 15.5 | 14.5 | 21.5 | 20.3 | 13.1 | 16.99 | 54.9% | 33.4% |
| >=3000 | 4,403 | 21.4 | 12.0 | 22.8 | 17.1 | 13.8 | 7.3 | 5.6 | 8.3 | 26.8% | 12.9% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 637 | 0.5382 | 0.4044 | 0.4851 | +0.053 | -0.081 | 0.0014 ± 0.0059 |
| ratio 4-10x | 424 | 0.584 | 0.4468 | 0.5047 | +0.079 | -0.058 | 0.0082 ± 0.0075 |
| ratio <2x | 1584 | 0.5366 | 0.4153 | 0.4514 | +0.085 | -0.036 | 0.0122 ± 0.0036 |
| ratio >=10x | 515 | 0.5469 | 0.379 | 0.4175 | +0.129 | -0.038 | 0.0178 ± 0.0078 |
| thinner_sample 1000-3000 | 900 | 0.5433 | 0.4181 | 0.4644 | +0.079 | -0.046 | 0.0073 ± 0.0048 |
| thinner_sample 300-1000 | 748 | 0.5605 | 0.4213 | 0.484 | +0.076 | -0.063 | 0.0029 ± 0.0057 |
| thinner_sample <300 | 964 | 0.5433 | 0.3833 | 0.4315 | +0.112 | -0.048 | 0.0176 ± 0.0055 |
| thinner_sample >=3000 | 548 | 0.5295 | 0.4363 | 0.469 | +0.060 | -0.033 | 0.0131 ± 0.0049 |
| data_status ADEQUATE | 935 | 0.5336 | 0.4293 | 0.461 | +0.073 | -0.032 | 0.0099 ± 0.0041 |
| data_status LIMITED | 790 | 0.5512 | 0.422 | 0.4861 | +0.065 | -0.064 | 0.0041 ± 0.0052 |
| data_status POOR | 1435 | 0.549 | 0.3939 | 0.4446 | +0.104 | -0.051 | 0.0143 ± 0.0045 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 490 | 0.1928 | 0.1942 | -0.0014 ± 0.0007 | 0.5636 | 0.5665 | 0.4938 | 0.479 | 0.5306 | -0.040 ± 0.0208 | -0.01 (5) |
| 3-5 | 308 | 0.1953 | 0.1949 | +0.0004 ± 0.002 | 0.5716 | 0.5694 | 0.5064 | 0.4664 | 0.4805 | -0.078 ± 0.0258 | 0.02 (1) |
| 5-10 | 667 | 0.1979 | 0.1971 | +0.0008 ± 0.0026 | 0.5814 | 0.5775 | 0.5105 | 0.436 | 0.4618 | -0.085 ± 0.0178 | -0.0167 (6) |
| 10-15 | 557 | 0.2138 | 0.2054 | +0.0085 ± 0.0048 | 0.6162 | 0.5926 | 0.5192 | 0.3953 | 0.4219 | -0.086 ± 0.0192 | -0.048 (5) |
| 15-25 | 689 | 0.2299 | 0.2133 | +0.0167 ± 0.0069 | 0.6546 | 0.6118 | 0.5756 | 0.3806 | 0.4369 | -0.084 ± 0.0176 | -0.0033 (9) |
| 25-40 | 371 | 0.2243 | 0.2068 | +0.0175 ± 0.0141 | 0.6376 | 0.5956 | 0.6469 | 0.3379 | 0.4636 | -0.064 ± 0.0216 | -0.01 (1) |
| 40+ | 78 | 0.3044 | 0.1729 | +0.1315 ± 0.0422 | 0.8211 | 0.5186 | 0.7435 | 0.296 | 0.3718 | -0.122 ± 0.0414 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2300 | 0.1803 | 0.1815 | -0.0012 ± 0.0003 | 0.5355 | 0.5368 | 0.4785 | 0.4635 | 0.4987 | -0.019 ± 0.009 | -0.0129 (17) |
| 3-5 | 1419 | 0.1941 | 0.1919 | +0.0022 ± 0.0009 | 0.5686 | 0.5593 | 0.4793 | 0.4396 | 0.4306 | -0.066 ± 0.0118 | 0.0 (2) |
| 5-10 | 3105 | 0.1938 | 0.1911 | +0.0027 ± 0.0012 | 0.5703 | 0.5612 | 0.4824 | 0.4085 | 0.4254 | -0.046 ± 0.008 | -0.0119 (21) |
| 10-15 | 2666 | 0.2016 | 0.1832 | +0.0184 ± 0.0021 | 0.5894 | 0.5385 | 0.4799 | 0.3553 | 0.344 | -0.074 ± 0.0083 | -0.0281 (16) |
| 15-25 | 3263 | 0.2084 | 0.1695 | +0.0389 ± 0.0028 | 0.6088 | 0.5015 | 0.5013 | 0.3051 | 0.3059 | -0.070 ± 0.0072 | -0.0025 (44) |
| 25-40 | 2554 | 0.2215 | 0.125 | +0.0965 ± 0.0044 | 0.6365 | 0.3862 | 0.5284 | 0.2151 | 0.2216 | -0.063 ± 0.0068 | -0.01 (1) |
| 40+ | 1750 | 0.3781 | 0.0422 | +0.3359 ± 0.0055 | 0.984 | 0.1686 | 0.6267 | 0.1054 | 0.0543 | -0.087 ± 0.0046 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 365 | 0.1979 | 0.1982 | -0.0004 ± 0.0008 | 0.577 | 0.5779 | 0.502 | 0.4868 | 0.5068 | -0.080 ± 0.0246 | -0.01 (3) |
| 3-5 | 253 | 0.2102 | 0.2092 | +0.0010 ± 0.0023 | 0.6028 | 0.6016 | 0.5161 | 0.4761 | 0.4783 | -0.081 ± 0.0302 | 0.02 (1) |
| 5-10 | 582 | 0.1993 | 0.1988 | +0.0005 ± 0.0028 | 0.5822 | 0.5811 | 0.5474 | 0.4726 | 0.5069 | -0.070 ± 0.0191 | -0.01 (4) |
| 10-15 | 516 | 0.2179 | 0.2103 | +0.0076 ± 0.0051 | 0.6237 | 0.6063 | 0.568 | 0.4435 | 0.4787 | -0.089 ± 0.0212 | -0.04 (5) |
| 15-25 | 757 | 0.2283 | 0.2079 | +0.0204 ± 0.0065 | 0.6482 | 0.598 | 0.5879 | 0.3914 | 0.4412 | -0.087 ± 0.0168 | -0.0133 (9) |
| 25-40 | 499 | 0.2667 | 0.1968 | +0.0699 ± 0.0126 | 0.744 | 0.5743 | 0.6595 | 0.3445 | 0.3928 | -0.113 ± 0.0197 | -0.0075 (4) |
| 40+ | 188 | 0.3645 | 0.1762 | +0.1883 ± 0.0302 | 1.0117 | 0.5231 | 0.7405 | 0.2582 | 0.3191 | -0.072 ± 0.0295 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1938 | 0.1826 | 0.183 | -0.0004 ± 0.0003 | 0.5404 | 0.541 | 0.5022 | 0.4875 | 0.5083 | -0.034 ± 0.01 | -0.0133 (15) |
| 3-5 | 1225 | 0.1929 | 0.1918 | +0.0011 ± 0.001 | 0.5607 | 0.558 | 0.5154 | 0.4755 | 0.4808 | -0.044 ± 0.0127 | 0.02 (1) |
| 5-10 | 2759 | 0.1924 | 0.19 | +0.0024 ± 0.0012 | 0.5675 | 0.5588 | 0.5098 | 0.4357 | 0.4585 | -0.038 ± 0.0084 | -0.0117 (6) |
| 10-15 | 2363 | 0.1976 | 0.1868 | +0.0109 ± 0.0022 | 0.581 | 0.5454 | 0.519 | 0.3945 | 0.4156 | -0.047 ± 0.0091 | -0.0189 (18) |
| 15-25 | 3403 | 0.2164 | 0.1764 | +0.0401 ± 0.0028 | 0.6282 | 0.5202 | 0.5317 | 0.3355 | 0.3347 | -0.074 ± 0.0073 | -0.0086 (42) |
| 25-40 | 3014 | 0.2495 | 0.1359 | +0.1136 ± 0.0043 | 0.7057 | 0.4167 | 0.5589 | 0.2431 | 0.223 | -0.087 ± 0.0067 | -0.0044 (18) |
| 40+ | 2355 | 0.4009 | 0.0649 | +0.3360 ± 0.006 | 1.0561 | 0.2285 | 0.6617 | 0.1247 | 0.0938 | -0.070 ± 0.0051 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 470 | 0.1947 | 0.1969 | -0.0022 ± 0.0007 | 0.5692 | 0.5746 | 0.496 | 0.4807 | 0.5426 | -0.016 ± 0.021 | -0.0137 (8) |
| 3-5 | 349 | 0.1902 | 0.1883 | +0.0018 ± 0.0019 | 0.5572 | 0.5529 | 0.4966 | 0.457 | 0.4556 | -0.111 ± 0.0244 | 0.0067 (3) |
| 5-10 | 697 | 0.2017 | 0.1973 | +0.0044 ± 0.0025 | 0.5905 | 0.5767 | 0.5027 | 0.4289 | 0.4333 | -0.096 ± 0.0172 | -0.0071 (7) |
| 10-15 | 546 | 0.2076 | 0.206 | +0.0016 ± 0.0048 | 0.6026 | 0.595 | 0.5372 | 0.4142 | 0.4725 | -0.065 ± 0.0192 | -0.0317 (6) |
| 15-25 | 637 | 0.2358 | 0.2097 | +0.0261 ± 0.0071 | 0.6717 | 0.6035 | 0.5843 | 0.3911 | 0.4192 | -0.110 ± 0.018 | -0.03 (1) |
| 25-40 | 386 | 0.2114 | 0.212 | -0.0006 ± 0.0137 | 0.6097 | 0.6073 | 0.6515 | 0.342 | 0.4948 | -0.044 ± 0.021 | 0.015 (2) |
| 40+ | 75 | 0.3237 | 0.1866 | +0.1371 ± 0.045 | 0.8679 | 0.5501 | 0.7473 | 0.2945 | 0.3733 | -0.107 ± 0.0471 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2187 | 0.186 | 0.1867 | -0.0008 ± 0.0003 | 0.5484 | 0.5498 | 0.4831 | 0.4678 | 0.4906 | -0.029 ± 0.0093 | -0.0163 (35) |
| 3-5 | 1502 | 0.1883 | 0.1849 | +0.0035 ± 0.0009 | 0.5543 | 0.5459 | 0.4775 | 0.438 | 0.4148 | -0.085 ± 0.0114 | -0.0094 (18) |
| 5-10 | 3295 | 0.1951 | 0.1885 | +0.0066 ± 0.0011 | 0.5756 | 0.5535 | 0.4797 | 0.4058 | 0.3961 | -0.069 ± 0.0076 | -0.01 (31) |
| 10-15 | 2532 | 0.1964 | 0.1811 | +0.0153 ± 0.0021 | 0.5773 | 0.5315 | 0.4968 | 0.3735 | 0.3736 | -0.065 ± 0.0084 | -0.015 (12) |
| 15-25 | 3353 | 0.2084 | 0.1682 | +0.0403 ± 0.0028 | 0.611 | 0.4991 | 0.5042 | 0.3091 | 0.3048 | -0.073 ± 0.0071 | -0.03 (2) |
| 25-40 | 2508 | 0.2168 | 0.1232 | +0.0936 ± 0.0044 | 0.626 | 0.3804 | 0.5249 | 0.2089 | 0.2229 | -0.059 ± 0.0067 | 0.01 (3) |
| 40+ | 1680 | 0.3936 | 0.0463 | +0.3473 ± 0.0059 | 1.0264 | 0.1794 | 0.638 | 0.1098 | 0.0565 | -0.088 ± 0.005 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 817 | 0.1958 | 0.196 | -0.0001 ± 0.0005 | 0.5722 | 0.5722 | 0.5083 | 0.4933 | 0.4969 | -0.050 ± 0.0155 | -0.0224 (49) |
| 3-5 | 576 | 0.1948 | 0.1939 | +0.0009 ± 0.0015 | 0.5678 | 0.5645 | 0.4796 | 0.4397 | 0.4462 | -0.051 ± 0.0185 | -0.0194 (34) |
| 5-10 | 1207 | 0.1975 | 0.1916 | +0.0059 ± 0.0019 | 0.5823 | 0.5651 | 0.4882 | 0.4146 | 0.4126 | -0.064 ± 0.0129 | -0.005 (78) |
| 10-15 | 764 | 0.2076 | 0.1962 | +0.0114 ± 0.004 | 0.6036 | 0.574 | 0.5067 | 0.3836 | 0.3979 | -0.056 ± 0.0161 | 0.0014 (64) |
| 15-25 | 1019 | 0.2335 | 0.2114 | +0.0221 ± 0.0057 | 0.6654 | 0.6089 | 0.5661 | 0.3712 | 0.4132 | -0.057 ± 0.0144 | -0.0214 (59) |
| 25-40 | 585 | 0.2492 | 0.1957 | +0.0534 ± 0.0113 | 0.7031 | 0.5692 | 0.6472 | 0.335 | 0.4034 | -0.080 ± 0.017 | -0.0219 (26) |
| 40+ | 197 | 0.3744 | 0.1904 | +0.1840 ± 0.0317 | 1.0791 | 0.5615 | 0.7924 | 0.3009 | 0.3807 | -0.079 ± 0.0285 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2467 | 0.1883 | 0.1884 | -0.0000 ± 0.0003 | 0.5527 | 0.5518 | 0.504 | 0.4887 | 0.4986 | -0.034 ± 0.0087 | -0.0157 (88) |
| 3-5 | 1680 | 0.189 | 0.1867 | +0.0023 ± 0.0008 | 0.5531 | 0.5477 | 0.4847 | 0.4451 | 0.4363 | -0.055 ± 0.0106 | -0.0209 (69) |
| 5-10 | 3383 | 0.1938 | 0.186 | +0.0078 ± 0.0011 | 0.5726 | 0.5501 | 0.4827 | 0.4091 | 0.3961 | -0.064 ± 0.0075 | -0.0082 (132) |
| 10-15 | 2278 | 0.2042 | 0.1898 | +0.0144 ± 0.0023 | 0.5964 | 0.5578 | 0.511 | 0.388 | 0.3911 | -0.055 ± 0.0091 | -0.0053 (105) |
| 15-25 | 2853 | 0.2298 | 0.1975 | +0.0323 ± 0.0033 | 0.6627 | 0.5745 | 0.557 | 0.3617 | 0.3782 | -0.062 ± 0.0084 | -0.0253 (107) |
| 25-40 | 1925 | 0.2537 | 0.1691 | +0.0846 ± 0.0059 | 0.7187 | 0.5003 | 0.6075 | 0.2935 | 0.3179 | -0.076 ± 0.0091 | -0.0229 (51) |
| 40+ | 930 | 0.3877 | 0.1297 | +0.2580 ± 0.0126 | 1.0973 | 0.3973 | 0.7091 | 0.2025 | 0.214 | -0.072 ± 0.0112 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3160 | 1.05 ± 0.05 | 1.165 | 0.1682 | 0.171 | 0.2124 | 0.2019 |
| gen2 | 3160 | 0.852 ± 0.045 | 1.125 | 0.1753 | 0.171 | 0.2305 | 0.202 |
| gen1_elo | 3160 | 1.035 ± 0.049 | 1.148 | 0.1735 | 0.1714 | 0.2113 | 0.2018 |
| gen1_sr | 3160 | 1.052 ± 0.059 | 1.186 | 0.135 | 0.1727 | 0.2265 | 0.2018 |
| gen1_ledger | 5165 | 0.874 ± 0.034 | 1.075 | 0.1774 | 0.1853 | 0.2181 | 0.1976 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 14,875)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,707 | 24.9% |
| STALE_QUOTE | market_freshness | 3,062 | 20.6% |
| BOOK_QUALITY | execution | 2,684 | 18.0% |
| POOR_DATA | data | 1,624 | 10.9% |
| LIMITED_DATA | data | 1,061 | 7.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 804 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 714 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 609 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 429 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 181 | 1.2% |

Cause class: coverage 24.9%, market_freshness 20.6%, data 18.1%, execution 18.0%, market_freshness/coverage 8.3%, model_calibration_or_unknown 4.8%, mapping 4.1%, model_calibration 1.2%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.8%, START_UNVERIFIABLE 95.5%, LOW_DATA_QUALITY 69.0%, THIN_PLAYER_HISTORY 57.5%, STALE_PLAYER_DATA 51.7%, STALE_KALSHI_QUOTE 45.1%, MODEL_INTERNAL_DISAGREEMENT 39.6%, ASYMMETRIC_SAMPLE_SIZE 31.7%, WIDE_SPREAD 23.7%, MODEL_HIGH_UNCERTAINTY 17.7%, PLAYER_IDENTITY_RISK 14.4%, LEVEL_TRANSFER_RISK 8.3%, EVENT_MAPPING_RISK 8.1%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 3.5%, EXTERNAL_MARKET_REJECTION 2.1%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 27.4%, POST_SETTLEMENT_OBSERVATION 24.9%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 8,008)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,932 | 36.6% |
| STALE_QUOTE | market_freshness | 1,436 | 17.9% |
| BOOK_QUALITY | execution | 1,407 | 17.6% |
| POOR_DATA | data | 674 | 8.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 433 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 349 | 4.4% |
| LIMITED_DATA | data | 315 | 3.9% |
| IN_PLAY_QUOTE | market_freshness/coverage | 265 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 158 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 39 | 0.5% |

Cause class: coverage 36.6%, market_freshness 17.9%, execution 17.6%, data 12.3%, market_freshness/coverage 8.7%, mapping 4.4%, model_calibration_or_unknown 2.0%, model_calibration 0.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.9%, START_UNVERIFIABLE 97.9%, LOW_DATA_QUALITY 72.7%, THIN_PLAYER_HISTORY 59.9%, STALE_KALSHI_QUOTE 53.5%, STALE_PLAYER_DATA 46.8%, MODEL_INTERNAL_DISAGREEMENT 40.6%, ASYMMETRIC_SAMPLE_SIZE 33.5%, WIDE_SPREAD 23.4%, MODEL_HIGH_UNCERTAINTY 18.1%, PLAYER_IDENTITY_RISK 17.8%, EVENT_MAPPING_RISK 9.8%, LOW_DISPLAYED_LIQUIDITY 8.1%, LEVEL_TRANSFER_RISK 7.3%, MODEL_CALIBRATION_OUTLIER 4.5%, EXTERNAL_MARKET_REJECTION 1.1%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 39.4%, POST_SETTLEMENT_OBSERVATION 36.6%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 6384, "IDENTITY_AMBIGUOUS": 1624}; ticker orientation: {"VERIFIED": 8008}.

Checks: discipline:AMBIGUOUS 554, discipline:PASS 7454, identity_confidence:AMBIGUOUS 1422, identity_confidence:PASS 6586, level_mapping:NA 566, level_mapping:PASS 7442, market_pair:AMBIGUOUS 286, market_pair:NA 204, market_pair:PASS 7518, model_complement:NA 171, model_complement:PASS 7837, namesake:PASS 8008, physical_match_id:NA 2988, physical_match_id:PASS 5020, player_ids:PASS 8008, same_pair_other_event:PASS 8008, ticker_orientation:PASS 8008

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,430 | 2.4% | 2.1% | 0.7% | {"market_freshness": 24, "data": 13, "execution": 11, "market_freshness/coverage": 7, "model_calibration_or_unknown": 2, "coverage": 2} | 5.42 | 0.2083 / 0.2081 (287) | 15.5% | 1.8% | 4.9% | 2.4% |
| CHALLENGER | 5,638 | 17.0% | 5.8% | 12.0% | {"coverage": 584, "market_freshness/coverage": 122, "market_freshness": 112, "data": 63, "model_calibration_or_unknown": 49, "execution": 13, "model_calibration": 9, "mapping": 6} | 7.04 | 0.2171 / 0.2048 (1477) | 36.9% | 9.5% | 2.4% | 22.9% |
| DOUBLES | 1,137 | 48.7% | 48.2% | 6.9% | {"execution": 239, "mapping": 160, "market_freshness": 106, "market_freshness/coverage": 42, "coverage": 7} | 23.94 | 0.3241 / 0.2333 (331) | 20.6% | 0.0% | 100.0% | 7.9% |
| ITF_MEN | 10,658 | 24.7% | 16.9% | 32.8% | {"coverage": 1032, "execution": 529, "market_freshness": 406, "data": 357, "market_freshness/coverage": 209, "mapping": 94, "model_calibration_or_unknown": 2} | 11.13 | 0.2138 / 0.1944 (2608) | 36.4% | 61.3% | 12.5% | 22.9% |
| ITF_WOMEN | 13,221 | 26.6% | 19.1% | 43.9% | {"coverage": 1290, "market_freshness": 713, "execution": 586, "data": 522, "market_freshness/coverage": 269, "mapping": 83, "model_calibration_or_unknown": 43, "model_calibration": 10} | 12.59 | 0.2035 / 0.1913 (2759) | 39.1% | 56.6% | 10.1% | 22.7% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,930 | 5.7% | 5.1% | 1.4% | {"market_freshness": 36, "model_calibration_or_unknown": 23, "execution": 15, "data": 11, "market_freshness/coverage": 10, "model_calibration": 9, "coverage": 4, "mapping": 1} | 7.59 | 0.2355 / 0.2312 (339) | 23.7% | 1.8% | 1.9% | 3.1% |
| WTA125 | 1,366 | 12.5% | 9.8% | 2.1% | {"market_freshness/coverage": 38, "model_calibration_or_unknown": 37, "market_freshness": 37, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.2185 / 0.2069 (482) | 22.8% | 7.5% | 4.7% | 10.0% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 5 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 6 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 7 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 9 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 10 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 11 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 12 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 13 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 14 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 15 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 16 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 17 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 18 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 19 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 20 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 463 min (STALE); no external reference |
| 22 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 23 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 24 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 25 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 26 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 27 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 28 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 22.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1345 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 29 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 30 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 31 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 32 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 33 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 162 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 34 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 35 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 765 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 36 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 37 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 38 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 33 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 39 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 40 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 41 | `KXITFWMATCH-26OCT16ESTLAB-LAB` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 68 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1475.0, ratio 2.28); no external reference |
| 42 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 43 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 44 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 45 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 46 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 47 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 48 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 49 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 50 | `KXATPCHALLENGERMATCH-26OCT13GIUSEA-SEA` | CHALLENGER | fair_v1 | 76% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 757 min (STALE); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9791, "by_level_share_of_ge_25pp": {"ATP": 0.0074, "CHALLENGER": 0.1196, "DOUBLES": 0.0692, "ITF_MEN": 0.3283, "ITF_WOMEN": 0.4391, "OTHER": 0.0015, "WTA": 0.0136, "WTA125": 0.0214}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5353, "share_primary_cause_market_settled_or_in_play": 0.4533, "share_primary_cause_stale_quote_only": 0.1793}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 8008, "identity_ambiguous_share": 0.2028, "ticker_orientation": {"VERIFIED": 8008}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 5020, "with_external": 198, "coverage": 0.0394, "external_status": {"EXTERNAL_STALE": 136, "AGREES_WITH_KALSHI": 59, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 136, "MODEL_LONE_OUTLIER": 59, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.298, "share_external_supports_model": 0.0152}, "pregame_clean_ge_25pp": {"n": 2374, "with_external": 186, "coverage": 0.0783, "external_status": {"EXTERNAL_STALE": 126, "AGREES_WITH_KALSHI": 57, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 126, "MODEL_LONE_OUTLIER": 57, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3065, "share_external_supports_model": 0.0161}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 565.0, "median_sample_ratio": 2.36, "median_min_matches": 21.0, "median_max_days_since_last": 205.0, "share_severe_asymmetry": 0.2034, "data_status": {"POOR": 4254, "LIMITED": 2289, "ADEQUATE": 1465}, "comparison_lt_10pp": {"median_thinner_serve_points": 1841.0, "median_sample_ratio": 1.67, "median_min_matches": 91.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 637, "model_minus_observed": 0.0532, "kalshi_minus_observed": -0.0807, "brier_diff_model_minus_kalshi": 0.0014}, "4-10x": {"n": 424, "model_minus_observed": 0.0793, "kalshi_minus_observed": -0.0579, "brier_diff_model_minus_kalshi": 0.0082}, "<2x": {"n": 1584, "model_minus_observed": 0.0852, "kalshi_minus_observed": -0.0361, "brier_diff_model_minus_kalshi": 0.0122}, ">=10x": {"n": 515, "model_minus_observed": 0.1294, "kalshi_minus_observed": -0.0384, "brier_diff_model_minus_kalshi": 0.0178}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3160, "model": {"intercept": -0.546, "slope": 0.852, "slope_se": 0.045}, "kalshi_mid_same_rows": {"intercept": 0.223, "slope": 1.125, "slope_se": 0.051}, "mean_extremity_model": 0.1753, "mean_extremity_kalshi": 0.171, "model_brier": 0.2305, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0285, "brier_diff_se": 0.0034, "model_logloss": 0.6569, "kalshi_logloss": 0.586}, "fair_v1": {"n": 3160, "model": {"intercept": -0.412, "slope": 1.05, "slope_se": 0.05}, "kalshi_mid_same_rows": {"intercept": 0.295, "slope": 1.165, "slope_se": 0.052}, "mean_extremity_model": 0.1682, "mean_extremity_kalshi": 0.171, "model_brier": 0.2124, "kalshi_brier": 0.2019, "brier_diff_model_minus_kalshi": 0.0104, "brier_diff_se": 0.0027, "model_logloss": 0.6123, "kalshi_logloss": 0.5858}, "gen1_elo": {"n": 3160, "model": {"intercept": -0.411, "slope": 1.035, "slope_se": 0.049}, "kalshi_mid_same_rows": {"intercept": 0.28, "slope": 1.148, "slope_se": 0.051}, "mean_extremity_model": 0.1735, "mean_extremity_kalshi": 0.1714, "model_brier": 0.2113, "kalshi_brier": 0.2018, "brier_diff_model_minus_kalshi": 0.0095, "brier_diff_se": 0.0027, "model_logloss": 0.6111, "kalshi_logloss": 0.5854}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2461, "share_ge_15": 0.438, "median_abs_gap": 13.0, "n": 20398}, "gen1_elo": {"share_ge_25": 0.2393, "share_ge_15": 0.4318, "median_abs_gap": 12.51, "n": 20398}, "gen1_sr": {"share_ge_25": 0.3083, "share_ge_15": 0.5231, "median_abs_gap": 15.89, "n": 20398}, "gen2": {"share_ge_25": 0.31, "share_ge_15": 0.5091, "median_abs_gap": 15.45, "n": 20398}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1511, "share_ge_15": 0.349, "median_abs_gap": 10.65, "n": 15708}, "gen1_elo": {"share_ge_25": 0.1479, "share_ge_15": 0.3385, "median_abs_gap": 10.12, "n": 15707}, "gen1_sr": {"share_ge_25": 0.2138, "share_ge_15": 0.4441, "median_abs_gap": 13.18, "n": 15708}, "gen2": {"share_ge_25": 0.2278, "share_ge_15": 0.4406, "median_abs_gap": 13.0, "n": 15709}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.42, "share_ge_25_all": 0.0243, "share_ge_25_pregame_clean": 0.0211}, "WTA": {"median_abs_gap_pregame_clean": 7.59, "share_ge_25_all": 0.0565, "share_ge_25_pregame_clean": 0.0508}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2402, "share_within_10pp_all": 0.4397, "share_within_10pp_pregame_clean": 0.4975, "corr_model_vs_mid_pregame_clean": 0.8429}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 490, "model_brier": 0.1928, "kalshi_brier": 0.1942, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 557, "model_brier": 0.2138, "kalshi_brier": 0.2054, "brier_diff_model_minus_kalshi": 0.0085}, "15-25": {"n_settled": 689, "model_brier": 0.2299, "kalshi_brier": 0.2133, "brier_diff_model_minus_kalshi": 0.0167}, "25-40": {"n_settled": 371, "model_brier": 0.2243, "kalshi_brier": 0.2068, "brier_diff_model_minus_kalshi": 0.0175}, "3-5": {"n_settled": 308, "model_brier": 0.1953, "kalshi_brier": 0.1949, "brier_diff_model_minus_kalshi": 0.0004}, "40+": {"n_settled": 78, "model_brier": 0.3044, "kalshi_brier": 0.1729, "brier_diff_model_minus_kalshi": 0.1315}, "5-10": {"n_settled": 667, "model_brier": 0.1979, "kalshi_brier": 0.1971, "brier_diff_model_minus_kalshi": 0.0008}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.546, "slope": 0.852, "slope_se": 0.045}, "kalshi_slope": {"intercept": 0.223, "slope": 1.125, "slope_se": 0.051}, "n": 3160}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.519, "slope": 0.874, "slope_se": 0.034}, "kalshi_slope": {"intercept": 0.136, "slope": 1.075, "slope_se": 0.038}, "n": 5165}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 331, "model_brier": 0.3241, "kalshi_brier": 0.2333, "brier_diff_model_minus_kalshi": 0.0908, "brier_diff_se": 0.0172, "corr_model_outcome": 0.0152, "corr_kalshi_outcome": 0.2615}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
