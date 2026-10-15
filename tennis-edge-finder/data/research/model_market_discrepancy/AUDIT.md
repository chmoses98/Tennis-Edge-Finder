# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-15T12:14Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 33,764): 0-3 14.4%, 3-5 9.5%, 5-10 20.1%, 10-15 15.3%, 15-25 18.9%, 25-40 13.6%, 40+ 8.2%; median gap 11.85 pp.
* **Where the extremes live**: 98.3% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.6%, Challenger 12.3%, doubles 7.0%). Main tour: ATP 1.4% and WTA 6.2% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 7,354): MARKET_ALREADY_SETTLED_WHEN_PRICED 37.3%, BOOK_QUALITY 17.5%, STALE_QUOTE 17.3%, POOR_DATA 8.3%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 4.0%, IN_PLAY_QUOTE 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.4%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 37.3%, execution 17.5%, market_freshness 17.3%, data 12.4%, market_freshness/coverage 8.8%, mapping 4.3%, model_calibration_or_unknown 2.0%, model_calibration 0.4%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 53.6% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 46.1% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 7,354 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.9% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 3.7%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 21.7% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 553.0 points vs 1791.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.064, Gen-2 0.869, Gen-1 ledger 0.873 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 348 model 0.2258 vs Kalshi 0.2082; n 72 model 0.29 vs Kalshi 0.1741.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 133,810 model-market comparisons (222,628 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 47,265 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-15T12:04:24.771818+00:00'], shadow board 37,101 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-15T12:04:28.772061+00:00'], Model 4 14,258 rows, 14,587 settled tickers, 4,788 tickers with an external scan.
* By model: {"gen1_ledger": 31033, "gen1_elo": 18647, "fair_v1": 18647, "gen2": 18647, "gen1_sr": 18647, "model4_fundamental": 14099, "model4_conditioned": 14090}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 33,764 | 14.4 | 9.5 | 20.1 | 15.3 | 18.9 | 13.6 | 8.2 | 11.85 | 40.7% | 21.8% |
| MW fair_v1 | 18,647 | 13.6 | 8.4 | 18.6 | 15.9 | 19.3 | 14.5 | 9.7 | 12.93 | 43.5% | 24.2% |
| MW gen1_elo | 18,647 | 13.2 | 8.9 | 19.8 | 15.2 | 19.1 | 14.3 | 9.3 | 12.42 | 42.8% | 23.6% |
| MW gen1_ledger | 15,117 | 15.5 | 10.7 | 22.0 | 14.6 | 18.4 | 12.5 | 6.3 | 10.45 | 37.2% | 18.8% |
| MW gen1_sr | 18,647 | 9.8 | 7.5 | 16.2 | 14.2 | 21.9 | 18.5 | 11.8 | 15.82 | 52.2% | 30.3% |
| MW gen2 | 18,647 | 11.5 | 7.1 | 16.4 | 14.2 | 20.4 | 17.3 | 13.1 | 15.39 | 50.8% | 30.4% |
| all families model4_conditioned | 14,090 | 21.6 | 20.1 | 35.3 | 16.6 | 4.4 | 1.1 | 0.9 | 5.82 | 6.3% | 2.0% |
| all families model4_fundamental | 14,099 | 16.8 | 13.5 | 35.7 | 19.6 | 10.6 | 2.6 | 1.1 | 7.58 | 14.3% | 3.7% |

Configurable thresholds (primary): >=5pp 76.1%, >=10pp 56.0%, >=15pp 40.7%, >=20pp 30.1%, >=25pp 21.8%, >=30pp 15.8%, >=40pp 8.2%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.47pp; >=10pp 45.3%, >=25pp 17.4%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,334 | 30.6 | 14.5 | 25.2 | 17.5 | 10.3 | 1.1 | 0.8 | 5.69 | 12.2% | 1.9% |
| CHALLENGER | 3,161 | 15.7 | 10.0 | 20.1 | 15.8 | 14.7 | 12.2 | 11.6 | 11.53 | 38.4% | 23.7% |
| ITF_MEN | 5,316 | 11.1 | 8.2 | 17.9 | 14.9 | 19.6 | 16.2 | 12.0 | 14.16 | 47.8% | 28.2% |
| ITF_WOMEN | 7,291 | 10.4 | 6.6 | 16.2 | 16.0 | 22.3 | 18.0 | 10.5 | 15.35 | 50.9% | 28.5% |
| WTA | 943 | 21.4 | 10.7 | 24.5 | 15.8 | 20.8 | 5.6 | 1.2 | 8.18 | 27.6% | 6.8% |
| WTA125 | 602 | 13.3 | 7.5 | 21.9 | 21.1 | 20.8 | 13.6 | 1.8 | 11.4 | 36.2% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,334 | 24.8 | 14.5 | 24.7 | 18.8 | 14.4 | 1.9 | 1.0 | 6.55 | 17.2% | 2.9% |
| CHALLENGER | 3,161 | 14.9 | 7.6 | 19.5 | 13.5 | 18.2 | 14.1 | 12.2 | 12.73 | 44.5% | 26.3% |
| ITF_MEN | 5,316 | 9.6 | 6.9 | 15.9 | 13.9 | 20.0 | 18.7 | 14.9 | 16.5 | 53.7% | 33.7% |
| ITF_WOMEN | 7,291 | 8.7 | 5.8 | 13.4 | 13.5 | 21.8 | 20.6 | 16.2 | 18.59 | 58.7% | 36.8% |
| WTA | 943 | 17.6 | 8.1 | 18.7 | 16.2 | 23.1 | 15.2 | 1.2 | 12.12 | 39.5% | 16.3% |
| WTA125 | 602 | 6.3 | 4.7 | 16.9 | 17.6 | 25.6 | 19.8 | 9.1 | 17.24 | 54.5% | 28.9% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,334 | 27.9 | 14.4 | 28.6 | 15.3 | 10.4 | 2.5 | 0.9 | 6.03 | 13.8% | 3.4% |
| CHALLENGER | 3,161 | 15.1 | 10.2 | 20.5 | 15.2 | 15.4 | 11.7 | 11.9 | 11.02 | 39.0% | 23.6% |
| ITF_MEN | 5,316 | 10.2 | 8.1 | 18.5 | 14.2 | 20.3 | 16.5 | 12.2 | 14.53 | 49.0% | 28.7% |
| ITF_WOMEN | 7,291 | 10.0 | 6.8 | 16.5 | 15.9 | 23.1 | 18.2 | 9.5 | 15.35 | 50.8% | 27.8% |
| WTA | 943 | 22.6 | 15.5 | 32.6 | 15.8 | 10.7 | 2.1 | 0.7 | 6.17 | 13.6% | 2.9% |
| WTA125 | 602 | 22.6 | 13.0 | 28.9 | 15.1 | 13.8 | 6.3 | 0.3 | 7.5 | 20.4% | 6.6% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 728 | 31.0 | 22.8 | 35.3 | 9.2 | 1.2 | 0.4 | 0.0 | 4.69 | 1.7% | 0.4% |
| CHALLENGER | 2,169 | 22.2 | 15.4 | 27.6 | 14.7 | 13.0 | 5.0 | 2.0 | 6.98 | 20.1% | 7.0% |
| DOUBLES | 1,025 | 5.3 | 3.8 | 11.5 | 10.7 | 18.8 | 24.6 | 25.3 | 24.85 | 68.7% | 49.9% |
| ITF_MEN | 4,641 | 14.7 | 8.5 | 20.8 | 15.4 | 20.8 | 12.5 | 7.3 | 11.87 | 40.6% | 19.9% |
| ITF_WOMEN | 5,071 | 11.7 | 9.3 | 19.6 | 14.7 | 22.3 | 16.6 | 5.7 | 13.01 | 44.7% | 22.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 653 | 21.3 | 15.3 | 27.3 | 17.1 | 13.6 | 4.9 | 0.5 | 7.52 | 19.0% | 5.4% |
| WTA125 | 681 | 20.6 | 13.5 | 22.8 | 18.4 | 14.4 | 8.2 | 2.2 | 8.27 | 24.8% | 10.4% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,320 | 30.5 | 14.5 | 25.4 | 17.5 | 10.2 | 1.1 | 0.8 | 5.75 | 12.1% | 1.9% |
| CHALLENGER | 2,265 | 20.3 | 12.4 | 25.2 | 18.4 | 15.2 | 6.0 | 2.4 | 8.32 | 23.6% | 8.4% |
| ITF_MEN | 3,859 | 13.7 | 10.2 | 21.3 | 16.7 | 19.9 | 13.0 | 5.3 | 11.24 | 38.2% | 18.3% |
| ITF_WOMEN | 5,379 | 12.4 | 8.1 | 18.5 | 18.3 | 23.8 | 14.8 | 4.0 | 12.9 | 42.6% | 18.8% |
| WTA | 923 | 21.7 | 10.1 | 24.8 | 15.8 | 20.9 | 5.5 | 1.2 | 8.22 | 27.6% | 6.7% |
| WTA125 | 578 | 13.7 | 7.3 | 21.3 | 21.4 | 21.4 | 13.5 | 1.4 | 11.49 | 36.3% | 14.9% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,320 | 24.7 | 14.6 | 24.8 | 18.8 | 14.4 | 1.8 | 1.0 | 6.58 | 17.2% | 2.8% |
| CHALLENGER | 2,265 | 19.1 | 9.7 | 24.2 | 16.2 | 18.5 | 9.6 | 2.6 | 9.1 | 30.7% | 12.2% |
| ITF_MEN | 3,860 | 11.4 | 8.3 | 18.2 | 15.6 | 22.1 | 16.1 | 8.3 | 13.88 | 46.5% | 24.4% |
| ITF_WOMEN | 5,379 | 9.9 | 6.6 | 15.1 | 14.8 | 24.0 | 19.5 | 10.0 | 16.25 | 53.5% | 29.5% |
| WTA | 923 | 17.6 | 7.9 | 18.6 | 16.2 | 23.2 | 15.3 | 1.2 | 12.25 | 39.6% | 16.5% |
| WTA125 | 578 | 6.1 | 4.8 | 17.0 | 18.0 | 25.4 | 20.4 | 8.3 | 17.21 | 54.1% | 28.7% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 708 | 31.1 | 23.0 | 35.6 | 9.3 | 0.6 | 0.4 | 0.0 | 4.66 | 1.0% | 0.4% |
| CHALLENGER | 1,873 | 24.0 | 16.8 | 29.7 | 14.4 | 12.1 | 2.4 | 0.6 | 6.36 | 15.1% | 3.0% |
| DOUBLES | 946 | 5.4 | 3.9 | 11.8 | 10.8 | 18.9 | 24.5 | 24.6 | 24.2 | 68.1% | 49.1% |
| ITF_MEN | 3,813 | 16.2 | 9.3 | 22.8 | 16.2 | 20.6 | 10.5 | 4.4 | 10.53 | 35.5% | 14.9% |
| ITF_WOMEN | 4,141 | 12.9 | 10.1 | 21.4 | 15.5 | 22.6 | 15.0 | 2.6 | 11.56 | 40.1% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 619 | 21.8 | 16.0 | 27.5 | 17.1 | 13.9 | 3.7 | 0.0 | 7.21 | 17.6% | 3.7% |
| WTA125 | 577 | 22.5 | 14.9 | 24.3 | 19.9 | 12.8 | 5.2 | 0.3 | 7.35 | 18.4% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,025 | 5.3 | 3.8 | 11.5 | 10.7 | 18.8 | 24.6 | 25.3 | 24.85 | 68.7% | 49.9% |
| singles | 14,092 | 16.3 | 11.2 | 22.7 | 14.9 | 18.4 | 11.6 | 5.0 | 9.95 | 34.9% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 4,374 | 13.2 | 9.1 | 19.6 | 16.0 | 18.1 | 14.3 | 9.7 | 12.64 | 42.1% | 24.1% |
| Grass | 194 | 12.4 | 11.3 | 14.9 | 14.9 | 22.7 | 17.5 | 6.2 | 14.16 | 46.4% | 23.7% |
| Hard | 12,136 | 14.0 | 8.4 | 18.5 | 15.5 | 19.7 | 14.3 | 9.6 | 12.91 | 43.6% | 24.0% |
| UNKNOWN | 1,943 | 12.2 | 7.2 | 16.9 | 18.7 | 19.1 | 15.9 | 10.1 | 13.38 | 45.1% | 26.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,453 | 19.7 | 10.7 | 20.9 | 17.0 | 15.9 | 8.9 | 7.0 | 9.56 | 31.7% | 15.8% |
| B | 2,428 | 14.4 | 9.1 | 20.1 | 16.6 | 18.1 | 12.1 | 9.5 | 11.51 | 39.7% | 21.6% |
| C | 2,682 | 12.9 | 9.5 | 19.9 | 14.5 | 19.5 | 14.2 | 9.4 | 12.61 | 43.1% | 23.6% |
| D | 3,249 | 11.4 | 8.0 | 17.7 | 16.1 | 21.9 | 15.5 | 9.3 | 13.83 | 46.7% | 24.8% |
| F | 4,835 | 8.0 | 5.3 | 15.1 | 15.0 | 21.7 | 21.7 | 13.2 | 17.85 | 56.6% | 34.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,379 | 22.8 | 15.8 | 28.9 | 15.1 | 11.3 | 4.4 | 1.7 | 6.7 | 17.4% | 6.1% |
| B | 2,275 | 14.9 | 10.0 | 24.0 | 16.3 | 19.5 | 11.1 | 4.2 | 10.19 | 34.7% | 15.2% |
| C | 2,993 | 12.2 | 7.8 | 18.3 | 14.1 | 20.2 | 15.8 | 11.6 | 13.64 | 47.6% | 27.4% |
| D | 2,276 | 14.1 | 9.8 | 20.7 | 13.6 | 21.3 | 13.9 | 6.6 | 11.86 | 41.8% | 20.5% |
| F | 3,194 | 10.1 | 7.5 | 15.2 | 13.9 | 23.7 | 20.4 | 9.1 | 16.38 | 53.2% | 29.5% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 6,125 | 18.0 | 9.7 | 20.3 | 16.8 | 16.3 | 9.8 | 9.1 | 10.53 | 35.2% | 18.9% |
| LIMITED | 4,338 | 15.0 | 10.4 | 20.8 | 15.5 | 18.7 | 12.6 | 7.0 | 11.12 | 38.3% | 19.6% |
| POOR | 8,184 | 9.5 | 6.5 | 16.1 | 15.5 | 21.8 | 19.1 | 11.6 | 15.89 | 52.4% | 30.6% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,046 | 31.2 | 24.5 | 36.3 | 5.5 | 1.7 | 0.7 | 0.1 | 4.49 | 2.5% | 0.7% |
| GAME_SPREAD | 2,894 | 25.8 | 16.1 | 36.6 | 16.8 | 4.1 | 0.4 | 0.2 | 5.97 | 4.7% | 0.6% |
| MATCH_WINNER | 15,117 | 15.5 | 10.7 | 22.0 | 14.6 | 18.4 | 12.5 | 6.3 | 10.45 | 37.2% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 5,529 | 33.4 | 19.5 | 31.0 | 9.6 | 5.1 | 1.1 | 0.2 | 4.71 | 6.4% | 1.4% |
| TOTAL_GAMES | 4,423 | 6.7 | 9.2 | 39.2 | 29.4 | 10.4 | 2.7 | 2.3 | 9.44 | 15.4% | 5.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,929 | 25.6 | 38.2 | 31.4 | 0.3 | 3.9 | 0.4 | 0.1 | 4.3 | 4.4% | 0.5% |
| GAME_SPREAD | 3,513 | 45.3 | 16.5 | 28.7 | 7.3 | 1.1 | 0.7 | 0.4 | 3.55 | 2.2% | 1.1% |
| TOTAL_GAMES | 5,648 | 3.5 | 6.5 | 42.7 | 36.7 | 6.8 | 1.9 | 1.9 | 9.77 | 10.6% | 3.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,929 | 26.4 | 18.8 | 37.1 | 9.1 | 6.2 | 2.1 | 0.3 | 5.47 | 8.6% | 2.4% |
| GAME_SPREAD | 3,513 | 19.5 | 13.6 | 30.3 | 20.9 | 12.8 | 2.3 | 0.7 | 7.7 | 15.8% | 3.0% |
| TOTAL_GAMES | 5,657 | 6.7 | 8.9 | 37.9 | 28.1 | 13.1 | 3.3 | 2.1 | 9.64 | 18.4% | 5.4% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 18,647 | 43.5% | 24.2% | 12.93 | 34.4% | 14.5% | 10.56 |
| gen1_elo | 18,647 | 42.8% | 23.6% | 12.42 | 33.3% | 14.3% | 10.03 |
| gen1_sr | 18,647 | 52.2% | 30.3% | 15.82 | 44.1% | 20.7% | 13.14 |
| gen2 | 18,647 | 50.8% | 30.4% | 15.39 | 43.8% | 22.1% | 12.91 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 9,885 | 16.4 | 10.4 | 21.5 | 17.4 | 19.7 | 11.3 | 3.3 | 10.46 | 34.3% | 14.6% |
| STALE | 8,762 | 10.4 | 6.2 | 15.3 | 14.2 | 18.8 | 18.2 | 16.9 | 17.02 | 53.8% | 35.0% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 8,585 | 17.3 | 11.6 | 23.7 | 14.5 | 16.9 | 11.2 | 4.9 | 9.38 | 32.9% | 16.1% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 33,764 | 8585 | 13357 | 11822 | 24.4 | 145.1 | 1400.4 |
| ge_15pp | 13,731 | 2827 | 4679 | 6225 | 26.8 | 443.3 | 1380.4 |
| ge_25pp | 7,354 | 1379 | 2035 | 3940 | 34.3 | 578.1 | 1380.4 |
| lt_10pp | 14,856 | 4513 | 6408 | 3935 | 22.6 | 48.8 | 1341.5 |

Current slate `SL-20261015T121409Z-bca1079b`: 276 priced rows, quote age at build {'median': 9.9, 'max': 10.0}, freshness {'FRESH': 240, 'AGING': 36}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 10 | 0.0 | 0.0 | 40.0 | 0.0 | 40.0 | 20.0 | 0.0 | 20.33 | 60.0% | 20.0% |
| EXTERNAL_LONE_OUTLIER | 11 | 72.7 | 27.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,531 | 21.1 | 10.8 | 22.6 | 18.7 | 19.1 | 7.2 | 0.6 | 8.94 | 26.9% | 7.8% |
| KALSHI_LONE_OUTLIER | 7 | 14.3 | 0.0 | 57.1 | 0.0 | 14.3 | 14.3 | 0.0 | 5.14 | 28.6% | 14.3% |
| MARKETS_AGREE | 258 | 72.1 | 27.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.04 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 504 | 0.0 | 3.8 | 34.5 | 29.0 | 24.2 | 7.9 | 0.6 | 11.66 | 32.7% | 8.5% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 18,647 | 2321 (12.4%) | 21.7% | 0.7% | {"EXTERNAL_STALE": 1531, "AGREES_WITH_KALSHI": 504, "ALL_AGREE": 258, "EXTERNAL_OUTLIER": 11, "SUPPORTS_MODEL_DIRECTION": 9, "AGREES_WITH_MODEL": 7, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 8,105 | 584 (7.2%) | 28.2% | 1.4% | {"EXTERNAL_STALE": 411, "AGREES_WITH_KALSHI": 165, "SUPPORTS_MODEL_DIRECTION": 6, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 4,513 | 165 (3.7%) | 26.1% | 1.8% | {"EXTERNAL_STALE": 119, "AGREES_WITH_KALSHI": 43, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,081 | 156 (7.5%) | 26.3% | 1.9% | {"EXTERNAL_STALE": 112, "AGREES_WITH_KALSHI": 41, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 7,574 | 1305 (17.2%) | 14.8% | 0.6% | {"EXTERNAL_STALE": 834, "ALL_AGREE": 258, "AGREES_WITH_KALSHI": 193, "EXTERNAL_OUTLIER": 11, "AGREES_WITH_MODEL": 5, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,639 | 11.4 | 7.9 | 19.9 | 14.9 | 21.8 | 14.2 | 9.8 | 13.43 | 45.8% | 24.0% |
| 4-10x | 2,444 | 12.2 | 8.9 | 19.5 | 15.6 | 19.4 | 15.4 | 8.9 | 12.89 | 43.8% | 24.3% |
| <2x | 9,730 | 15.5 | 9.1 | 18.8 | 16.9 | 17.8 | 12.9 | 9.0 | 11.91 | 39.7% | 21.9% |
| >=10x | 2,834 | 11.0 | 6.5 | 15.3 | 14.0 | 21.0 | 19.6 | 12.6 | 16.28 | 53.1% | 32.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 4,863 | 13.7 | 8.2 | 19.4 | 16.1 | 19.8 | 12.7 | 10.2 | 12.67 | 42.6% | 22.9% |
| 300-1000 | 4,240 | 12.1 | 8.8 | 17.4 | 16.2 | 21.0 | 15.6 | 8.9 | 13.56 | 45.6% | 24.6% |
| <300 | 5,485 | 8.9 | 6.0 | 15.8 | 14.7 | 21.4 | 20.5 | 12.6 | 16.81 | 54.5% | 33.1% |
| >=3000 | 4,059 | 21.3 | 11.7 | 22.7 | 17.1 | 13.9 | 7.5 | 5.8 | 8.42 | 27.3% | 13.3% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 604 | 0.5377 | 0.4063 | 0.4868 | +0.051 | -0.081 | 0.0 ± 0.006 |
| ratio 4-10x | 405 | 0.5843 | 0.4462 | 0.5111 | +0.073 | -0.065 | 0.007 ± 0.0077 |
| ratio <2x | 1447 | 0.5371 | 0.4145 | 0.4554 | +0.082 | -0.041 | 0.011 ± 0.0038 |
| ratio >=10x | 478 | 0.5463 | 0.3784 | 0.4268 | +0.119 | -0.048 | 0.0148 ± 0.0081 |
| thinner_sample 1000-3000 | 816 | 0.5427 | 0.4177 | 0.473 | +0.070 | -0.055 | 0.0044 ± 0.005 |
| thinner_sample 300-1000 | 716 | 0.56 | 0.4228 | 0.4874 | +0.073 | -0.065 | 0.0016 ± 0.0058 |
| thinner_sample <300 | 904 | 0.5441 | 0.3832 | 0.4414 | +0.103 | -0.058 | 0.0153 ± 0.0057 |
| thinner_sample >=3000 | 498 | 0.5303 | 0.4351 | 0.4618 | +0.069 | -0.027 | 0.0145 ± 0.0053 |
| data_status ADEQUATE | 835 | 0.5337 | 0.4289 | 0.4611 | +0.073 | -0.032 | 0.0085 ± 0.0043 |
| data_status LIMITED | 747 | 0.551 | 0.4223 | 0.49 | +0.061 | -0.068 | 0.0027 ± 0.0054 |
| data_status POOR | 1352 | 0.5492 | 0.3943 | 0.4534 | +0.096 | -0.059 | 0.0124 ± 0.0046 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 447 | 0.1929 | 0.1944 | -0.0014 ± 0.0007 | 0.5638 | 0.5667 | 0.4916 | 0.4766 | 0.528 | -0.042 ± 0.0218 | -0.01 (3) |
| 3-5 | 288 | 0.1905 | 0.1907 | -0.0003 ± 0.0021 | 0.5608 | 0.56 | 0.5087 | 0.4688 | 0.4896 | -0.071 ± 0.0262 | 0.02 (1) |
| 5-10 | 620 | 0.1943 | 0.1952 | -0.0009 ± 0.0027 | 0.5731 | 0.573 | 0.5097 | 0.4352 | 0.471 | -0.077 ± 0.0184 | -0.02 (5) |
| 10-15 | 518 | 0.2111 | 0.2018 | +0.0093 ± 0.0049 | 0.6096 | 0.584 | 0.5213 | 0.3976 | 0.4208 | -0.091 ± 0.0196 | -0.0633 (3) |
| 15-25 | 641 | 0.2306 | 0.2183 | +0.0123 ± 0.0072 | 0.6563 | 0.6231 | 0.5765 | 0.3815 | 0.4493 | -0.073 ± 0.0183 | -0.0133 (6) |
| 25-40 | 348 | 0.2258 | 0.2082 | +0.0176 ± 0.0146 | 0.6423 | 0.598 | 0.6447 | 0.3362 | 0.4626 | -0.063 ± 0.0224 | -0.01 (1) |
| 40+ | 72 | 0.29 | 0.1741 | +0.1160 ± 0.0438 | 0.7878 | 0.5206 | 0.7443 | 0.2967 | 0.3889 | -0.113 ± 0.0433 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2097 | 0.1762 | 0.1774 | -0.0012 ± 0.0003 | 0.5256 | 0.5269 | 0.4775 | 0.4624 | 0.5002 | -0.018 ± 0.0093 | -0.0188 (8) |
| 3-5 | 1306 | 0.1934 | 0.1917 | +0.0017 ± 0.001 | 0.5675 | 0.5592 | 0.4811 | 0.4414 | 0.4364 | -0.063 ± 0.0123 | 0.02 (1) |
| 5-10 | 2893 | 0.1912 | 0.1895 | +0.0018 ± 0.0012 | 0.5642 | 0.5568 | 0.4841 | 0.4101 | 0.4321 | -0.043 ± 0.0082 | -0.0132 (19) |
| 10-15 | 2479 | 0.2017 | 0.1826 | +0.0191 ± 0.0021 | 0.5893 | 0.5368 | 0.4808 | 0.3564 | 0.3425 | -0.078 ± 0.0086 | -0.0371 (7) |
| 15-25 | 3006 | 0.2076 | 0.1725 | +0.0350 ± 0.003 | 0.6074 | 0.5084 | 0.5009 | 0.3049 | 0.3154 | -0.062 ± 0.0076 | -0.0048 (29) |
| 25-40 | 2372 | 0.2197 | 0.1265 | +0.0932 ± 0.0046 | 0.6328 | 0.3893 | 0.5281 | 0.215 | 0.2268 | -0.059 ± 0.0071 | -0.01 (1) |
| 40+ | 1597 | 0.3737 | 0.0439 | +0.3298 ± 0.0059 | 0.9729 | 0.1727 | 0.6255 | 0.1053 | 0.0589 | -0.083 ± 0.0049 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 342 | 0.1976 | 0.1978 | -0.0002 ± 0.0008 | 0.5763 | 0.5769 | 0.501 | 0.4859 | 0.5029 | -0.084 ± 0.0253 | -0.01 (1) |
| 3-5 | 233 | 0.2098 | 0.2088 | +0.0010 ± 0.0024 | 0.6014 | 0.6006 | 0.5162 | 0.4761 | 0.4807 | -0.081 ± 0.0314 | 0.02 (1) |
| 5-10 | 530 | 0.1983 | 0.1979 | +0.0005 ± 0.0029 | 0.5798 | 0.5788 | 0.5533 | 0.4786 | 0.5132 | -0.070 ± 0.0201 | -0.01 (4) |
| 10-15 | 479 | 0.2126 | 0.2045 | +0.0081 ± 0.0052 | 0.6113 | 0.5934 | 0.5686 | 0.4441 | 0.4781 | -0.088 ± 0.0214 | -0.05 (4) |
| 15-25 | 715 | 0.2287 | 0.2085 | +0.0202 ± 0.0068 | 0.6492 | 0.5995 | 0.5885 | 0.3916 | 0.442 | -0.088 ± 0.0173 | -0.0167 (6) |
| 25-40 | 458 | 0.2651 | 0.1993 | +0.0657 ± 0.0131 | 0.7426 | 0.5782 | 0.663 | 0.3487 | 0.4039 | -0.111 ± 0.0207 | -0.025 (2) |
| 40+ | 177 | 0.3554 | 0.1823 | +0.1731 ± 0.0313 | 0.9838 | 0.5371 | 0.7404 | 0.2599 | 0.3333 | -0.062 ± 0.031 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1790 | 0.1828 | 0.1831 | -0.0003 ± 0.0003 | 0.5406 | 0.5412 | 0.4967 | 0.4821 | 0.5034 | -0.035 ± 0.0104 | -0.0217 (6) |
| 3-5 | 1146 | 0.1925 | 0.1919 | +0.0007 ± 0.001 | 0.5597 | 0.558 | 0.5152 | 0.4752 | 0.486 | -0.040 ± 0.0132 | 0.02 (1) |
| 5-10 | 2519 | 0.1913 | 0.1886 | +0.0027 ± 0.0013 | 0.5651 | 0.5553 | 0.5155 | 0.4418 | 0.4625 | -0.042 ± 0.0088 | -0.01 (5) |
| 10-15 | 2204 | 0.1946 | 0.181 | +0.0136 ± 0.0023 | 0.574 | 0.531 | 0.5178 | 0.3934 | 0.4038 | -0.058 ± 0.0092 | -0.0227 (15) |
| 15-25 | 3192 | 0.2164 | 0.1768 | +0.0395 ± 0.0029 | 0.6285 | 0.5213 | 0.533 | 0.3366 | 0.3371 | -0.074 ± 0.0075 | -0.0061 (31) |
| 25-40 | 2748 | 0.2475 | 0.1377 | +0.1099 ± 0.0045 | 0.7026 | 0.4192 | 0.5611 | 0.2447 | 0.2314 | -0.082 ± 0.0071 | -0.015 (6) |
| 40+ | 2151 | 0.3992 | 0.0683 | +0.3309 ± 0.0064 | 1.0471 | 0.2373 | 0.664 | 0.1271 | 0.1009 | -0.066 ± 0.0055 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 441 | 0.1921 | 0.1947 | -0.0026 ± 0.0007 | 0.5629 | 0.5695 | 0.4905 | 0.4753 | 0.551 | -0.002 ± 0.0213 | -0.0133 (6) |
| 3-5 | 314 | 0.1864 | 0.1845 | +0.0019 ± 0.0019 | 0.5484 | 0.5437 | 0.4945 | 0.4551 | 0.4522 | -0.114 ± 0.0254 | -0.01 (1) |
| 5-10 | 647 | 0.1992 | 0.1964 | +0.0028 ± 0.0026 | 0.5851 | 0.5749 | 0.5043 | 0.4306 | 0.4451 | -0.089 ± 0.0179 | -0.004 (5) |
| 10-15 | 508 | 0.2082 | 0.2079 | +0.0003 ± 0.005 | 0.604 | 0.5983 | 0.5384 | 0.4154 | 0.4783 | -0.062 ± 0.0201 | -0.044 (5) |
| 15-25 | 593 | 0.2361 | 0.212 | +0.0242 ± 0.0074 | 0.6719 | 0.6085 | 0.5839 | 0.3905 | 0.425 | -0.106 ± 0.0188 | -0.03 (1) |
| 25-40 | 365 | 0.2111 | 0.2128 | -0.0017 ± 0.0141 | 0.6098 | 0.6087 | 0.6502 | 0.3402 | 0.4959 | -0.040 ± 0.0215 | 0.0 (1) |
| 40+ | 66 | 0.3138 | 0.1811 | +0.1326 ± 0.0474 | 0.8443 | 0.537 | 0.7485 | 0.2945 | 0.3788 | -0.112 ± 0.0489 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2007 | 0.1834 | 0.1845 | -0.0011 ± 0.0003 | 0.5414 | 0.5435 | 0.4818 | 0.4665 | 0.5002 | -0.019 ± 0.0096 | -0.0179 (24) |
| 3-5 | 1376 | 0.1848 | 0.1823 | +0.0026 ± 0.0009 | 0.546 | 0.5398 | 0.476 | 0.4367 | 0.4251 | -0.074 ± 0.0119 | -0.0167 (9) |
| 5-10 | 3061 | 0.1931 | 0.1874 | +0.0057 ± 0.0012 | 0.5701 | 0.551 | 0.4798 | 0.406 | 0.4022 | -0.065 ± 0.0079 | -0.0065 (20) |
| 10-15 | 2354 | 0.1951 | 0.1809 | +0.0142 ± 0.0022 | 0.5745 | 0.5313 | 0.4976 | 0.3743 | 0.3785 | -0.063 ± 0.0087 | -0.03 (9) |
| 15-25 | 3080 | 0.21 | 0.1712 | +0.0388 ± 0.0029 | 0.6145 | 0.5062 | 0.5055 | 0.3102 | 0.3104 | -0.070 ± 0.0075 | -0.03 (2) |
| 25-40 | 2333 | 0.2139 | 0.1253 | +0.0887 ± 0.0046 | 0.6196 | 0.3848 | 0.525 | 0.2094 | 0.2306 | -0.053 ± 0.007 | 0.0 (1) |
| 40+ | 1539 | 0.3873 | 0.0457 | +0.3416 ± 0.0062 | 1.0112 | 0.1777 | 0.6335 | 0.1074 | 0.0572 | -0.086 ± 0.0052 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 764 | 0.1963 | 0.1968 | -0.0004 ± 0.0006 | 0.5731 | 0.5739 | 0.504 | 0.4889 | 0.5 | -0.043 ± 0.016 | -0.0226 (46) |
| 3-5 | 549 | 0.1934 | 0.1931 | +0.0002 ± 0.0015 | 0.5647 | 0.5626 | 0.4792 | 0.4394 | 0.4536 | -0.042 ± 0.0189 | -0.0058 (33) |
| 5-10 | 1148 | 0.1951 | 0.1897 | +0.0054 ± 0.0019 | 0.5758 | 0.5607 | 0.4874 | 0.414 | 0.4146 | -0.062 ± 0.0131 | -0.0054 (74) |
| 10-15 | 725 | 0.2066 | 0.1963 | +0.0103 ± 0.0041 | 0.6014 | 0.5743 | 0.5032 | 0.3802 | 0.3986 | -0.050 ± 0.0165 | 0.0014 (64) |
| 15-25 | 975 | 0.2321 | 0.2121 | +0.0200 ± 0.0058 | 0.6624 | 0.61 | 0.5623 | 0.3678 | 0.4144 | -0.050 ± 0.0147 | -0.0216 (58) |
| 25-40 | 561 | 0.2531 | 0.1948 | +0.0584 ± 0.0115 | 0.7129 | 0.5667 | 0.644 | 0.3312 | 0.3922 | -0.083 ± 0.0174 | -0.0219 (26) |
| 40+ | 193 | 0.3701 | 0.1933 | +0.1769 ± 0.0321 | 1.0713 | 0.5679 | 0.793 | 0.3026 | 0.3886 | -0.075 ± 0.029 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2289 | 0.1879 | 0.1881 | -0.0002 ± 0.0003 | 0.551 | 0.5503 | 0.5028 | 0.4874 | 0.4993 | -0.033 ± 0.009 | -0.0155 (82) |
| 3-5 | 1575 | 0.1875 | 0.1852 | +0.0023 ± 0.0009 | 0.5494 | 0.5439 | 0.4885 | 0.4488 | 0.44 | -0.055 ± 0.0109 | -0.0148 (63) |
| 5-10 | 3215 | 0.1922 | 0.1848 | +0.0074 ± 0.0011 | 0.5685 | 0.5473 | 0.4804 | 0.4068 | 0.3963 | -0.063 ± 0.0077 | -0.009 (126) |
| 10-15 | 2166 | 0.2033 | 0.189 | +0.0143 ± 0.0023 | 0.594 | 0.5562 | 0.5091 | 0.3861 | 0.3897 | -0.055 ± 0.0093 | -0.0053 (105) |
| 15-25 | 2726 | 0.2291 | 0.1984 | +0.0308 ± 0.0033 | 0.6615 | 0.5763 | 0.5546 | 0.3596 | 0.3797 | -0.058 ± 0.0086 | -0.0255 (106) |
| 25-40 | 1851 | 0.2544 | 0.1683 | +0.0861 ± 0.006 | 0.7211 | 0.4981 | 0.6061 | 0.2916 | 0.3139 | -0.077 ± 0.0093 | -0.0229 (51) |
| 40+ | 907 | 0.3845 | 0.1309 | +0.2537 ± 0.0128 | 1.0913 | 0.3994 | 0.7089 | 0.202 | 0.2183 | -0.069 ± 0.0114 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2934 | 1.064 ± 0.052 | 1.179 | 0.1691 | 0.1715 | 0.2107 | 0.2019 |
| gen2 | 2934 | 0.869 ± 0.047 | 1.128 | 0.1776 | 0.1715 | 0.2288 | 0.2017 |
| gen1_elo | 2934 | 1.044 ± 0.051 | 1.166 | 0.1739 | 0.172 | 0.2098 | 0.2017 |
| gen1_sr | 2934 | 1.078 ± 0.061 | 1.197 | 0.1369 | 0.1733 | 0.2247 | 0.2015 |
| gen1_ledger | 4915 | 0.873 ± 0.035 | 1.083 | 0.1772 | 0.1867 | 0.2176 | 0.1973 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 13,731)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,473 | 25.3% |
| STALE_QUOTE | market_freshness | 2,806 | 20.4% |
| BOOK_QUALITY | execution | 2,470 | 18.0% |
| POOR_DATA | data | 1,516 | 11.0% |
| LIMITED_DATA | data | 994 | 7.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 752 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 657 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 526 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 390 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 145 | 1.1% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 2 | 0.0% |

Cause class: coverage 25.3%, market_freshness 20.4%, data 18.3%, execution 18.0%, market_freshness/coverage 8.3%, model_calibration_or_unknown 4.8%, mapping 3.8%, model_calibration 1.1%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.1%, START_UNVERIFIABLE 95.9%, LOW_DATA_QUALITY 69.1%, THIN_PLAYER_HISTORY 57.9%, STALE_PLAYER_DATA 53.3%, STALE_KALSHI_QUOTE 45.3%, MODEL_INTERNAL_DISAGREEMENT 39.1%, ASYMMETRIC_SAMPLE_SIZE 31.8%, WIDE_SPREAD 23.7%, MODEL_HIGH_UNCERTAINTY 17.0%, PLAYER_IDENTITY_RISK 13.8%, LEVEL_TRANSFER_RISK 8.5%, EVENT_MAPPING_RISK 7.9%, LOW_DISPLAYED_LIQUIDITY 7.6%, MODEL_CALIBRATION_OUTLIER 3.5%, EXTERNAL_MARKET_REJECTION 1.8%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 27.7%, POST_SETTLEMENT_OBSERVATION 25.3%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 7,354)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,743 | 37.3% |
| BOOK_QUALITY | execution | 1,289 | 17.5% |
| STALE_QUOTE | market_freshness | 1,271 | 17.3% |
| POOR_DATA | data | 613 | 8.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 405 | 5.5% |
| IDENTITY_AMBIGUOUS | mapping | 319 | 4.3% |
| LIMITED_DATA | data | 297 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 240 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 145 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 31 | 0.4% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 37.3%, execution 17.5%, market_freshness 17.3%, data 12.4%, market_freshness/coverage 8.8%, mapping 4.3%, model_calibration_or_unknown 2.0%, model_calibration 0.4%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.1%, START_UNVERIFIABLE 98.3%, LOW_DATA_QUALITY 72.8%, THIN_PLAYER_HISTORY 60.2%, STALE_KALSHI_QUOTE 53.6%, STALE_PLAYER_DATA 48.5%, MODEL_INTERNAL_DISAGREEMENT 40.1%, ASYMMETRIC_SAMPLE_SIZE 33.6%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 17.5%, PLAYER_IDENTITY_RISK 17.4%, EVENT_MAPPING_RISK 9.7%, LOW_DISPLAYED_LIQUIDITY 7.8%, LEVEL_TRANSFER_RISK 7.4%, MODEL_CALIBRATION_OUTLIER 4.5%, EXTERNAL_MARKET_REJECTION 0.8%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 40.1%, POST_SETTLEMENT_OBSERVATION 37.3%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 5892, "IDENTITY_AMBIGUOUS": 1462}; ticker orientation: {"VERIFIED": 7354}.

Checks: discipline:AMBIGUOUS 511, discipline:PASS 6843, identity_confidence:AMBIGUOUS 1278, identity_confidence:PASS 6076, level_mapping:NA 523, level_mapping:PASS 6831, market_pair:AMBIGUOUS 262, market_pair:NA 174, market_pair:PASS 6918, model_complement:NA 141, model_complement:PASS 7213, namesake:PASS 7354, physical_match_id:NA 2841, physical_match_id:PASS 4513, player_ids:PASS 7354, same_pair_other_event:PASS 7354, ticker_orientation:PASS 7354

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,062 | 1.4% | 1.4% | 0.4% | {"market_freshness": 20, "execution": 8, "market_freshness/coverage": 1} | 5.24 | 0.2099 / 0.2126 (253) | 16.4% | 0.5% | 5.4% | 1.7% |
| CHALLENGER | 5,330 | 16.9% | 5.9% | 12.3% | {"coverage": 548, "market_freshness": 110, "market_freshness/coverage": 108, "data": 62, "model_calibration_or_unknown": 48, "execution": 13, "model_calibration": 7, "mapping": 6} | 7.24 | 0.2171 / 0.2031 (1384) | 37.6% | 9.2% | 2.4% | 22.4% |
| DOUBLES | 1,025 | 49.9% | 49.1% | 7.0% | {"execution": 208, "mapping": 151, "market_freshness": 106, "market_freshness/coverage": 39, "coverage": 7} | 24.2 | 0.3319 / 0.2309 (301) | 22.8% | 0.0% | 100.0% | 7.7% |
| ITF_MEN | 9,957 | 24.3% | 16.6% | 33.0% | {"coverage": 948, "execution": 503, "market_freshness": 362, "data": 324, "market_freshness/coverage": 202, "mapping": 83, "model_calibration_or_unknown": 2} | 10.98 | 0.2124 / 0.1943 (2484) | 36.6% | 59.9% | 11.3% | 22.9% |
| ITF_WOMEN | 12,362 | 26.0% | 18.3% | 43.7% | {"coverage": 1223, "market_freshness": 598, "execution": 536, "data": 490, "market_freshness/coverage": 250, "mapping": 73, "model_calibration_or_unknown": 33, "model_calibration": 10} | 12.41 | 0.2021 / 0.1923 (2660) | 39.1% | 57.9% | 9.9% | 23.0% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,596 | 6.2% | 5.5% | 1.4% | {"market_freshness": 36, "model_calibration_or_unknown": 23, "data": 11, "market_freshness/coverage": 10, "model_calibration": 7, "execution": 7, "coverage": 4, "mapping": 1} | 7.85 | 0.2398 / 0.2312 (289) | 26.5% | 1.3% | 1.7% | 3.4% |
| WTA125 | 1,283 | 12.8% | 10.2% | 2.2% | {"model_calibration_or_unknown": 37, "market_freshness": 37, "market_freshness/coverage": 34, "data": 23, "coverage": 12, "execution": 9, "model_calibration": 7, "mapping": 4, "possible_market_error": 1} | 9.53 | 0.2156 / 0.207 (436) | 23.6% | 8.0% | 4.2% | 10.0% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 5 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 6 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 7 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 8 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 9 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 10 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 11 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 12 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 13 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 14 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 15 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 16 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 17 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 18 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 19 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 20 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 21 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 22 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 23 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 24 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 25 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 92 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 26 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 27 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 28 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 29 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 30 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 31 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 32 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 33 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 34 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 35 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 33 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 36 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 37 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 39 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 40 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.8h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 359 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 41 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 42 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 43 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 44 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 45 | `KXATPCHALLENGERMATCH-26OCT13GIUSEA-SEA` | CHALLENGER | fair_v1 | 76% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 243 min (STALE); no external reference |
| 46 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 189 min (STALE); no external reference |
| 47 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 48 | `KXITFWMATCH-26OCT13MAMSTR-MAM` | ITF_WOMEN | fair_v1 | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 406 min (STALE); data LIMITED (grade C, thinner serve sample 879.0, ratio 2.64); no external reference |
| 49 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 50 | `KXITFMATCH-26OCT13VISMUE-MUE` | ITF_MEN | fair_v1 | 25% / 98% | -74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 617 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 0.0); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9826, "by_level_share_of_ge_25pp": {"ATP": 0.0039, "CHALLENGER": 0.1227, "DOUBLES": 0.0695, "ITF_MEN": 0.3296, "ITF_WOMEN": 0.4369, "OTHER": 0.0016, "WTA": 0.0135, "WTA125": 0.0223}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5358, "share_primary_cause_market_settled_or_in_play": 0.4607, "share_primary_cause_stale_quote_only": 0.1728}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 7354, "identity_ambiguous_share": 0.1988, "ticker_orientation": {"VERIFIED": 7354}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 4513, "with_external": 165, "coverage": 0.0366, "external_status": {"EXTERNAL_STALE": 119, "AGREES_WITH_KALSHI": 43, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 119, "MODEL_LONE_OUTLIER": 43, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.2606, "share_external_supports_model": 0.0182}, "pregame_clean_ge_25pp": {"n": 2081, "with_external": 156, "coverage": 0.075, "external_status": {"EXTERNAL_STALE": 112, "AGREES_WITH_KALSHI": 41, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 112, "MODEL_LONE_OUTLIER": 41, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.2628, "share_external_supports_model": 0.0192}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 553.0, "median_sample_ratio": 2.38, "median_min_matches": 20.0, "median_max_days_since_last": 204.0, "share_severe_asymmetry": 0.2004, "data_status": {"POOR": 3931, "LIMITED": 2097, "ADEQUATE": 1326}, "comparison_lt_10pp": {"median_thinner_serve_points": 1791.0, "median_sample_ratio": 1.69, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 604, "model_minus_observed": 0.0509, "kalshi_minus_observed": -0.0805, "brier_diff_model_minus_kalshi": 0.0}, "4-10x": {"n": 405, "model_minus_observed": 0.0732, "kalshi_minus_observed": -0.0649, "brier_diff_model_minus_kalshi": 0.007}, "<2x": {"n": 1447, "model_minus_observed": 0.0817, "kalshi_minus_observed": -0.0409, "brier_diff_model_minus_kalshi": 0.011}, ">=10x": {"n": 478, "model_minus_observed": 0.1195, "kalshi_minus_observed": -0.0484, "brier_diff_model_minus_kalshi": 0.0148}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2934, "model": {"intercept": -0.547, "slope": 0.869, "slope_se": 0.047}, "kalshi_mid_same_rows": {"intercept": 0.232, "slope": 1.128, "slope_se": 0.053}, "mean_extremity_model": 0.1776, "mean_extremity_kalshi": 0.1715, "model_brier": 0.2288, "kalshi_brier": 0.2017, "brier_diff_model_minus_kalshi": 0.0271, "brier_diff_se": 0.0035, "model_logloss": 0.6529, "kalshi_logloss": 0.5851}, "fair_v1": {"n": 2934, "model": {"intercept": -0.393, "slope": 1.064, "slope_se": 0.052}, "kalshi_mid_same_rows": {"intercept": 0.327, "slope": 1.179, "slope_se": 0.055}, "mean_extremity_model": 0.1691, "mean_extremity_kalshi": 0.1715, "model_brier": 0.2107, "kalshi_brier": 0.2019, "brier_diff_model_minus_kalshi": 0.0088, "brier_diff_se": 0.0028, "model_logloss": 0.6086, "kalshi_logloss": 0.5853}, "gen1_elo": {"n": 2934, "model": {"intercept": -0.379, "slope": 1.044, "slope_se": 0.051}, "kalshi_mid_same_rows": {"intercept": 0.324, "slope": 1.166, "slope_se": 0.054}, "mean_extremity_model": 0.1739, "mean_extremity_kalshi": 0.172, "model_brier": 0.2098, "kalshi_brier": 0.2017, "brier_diff_model_minus_kalshi": 0.0081, "brier_diff_se": 0.0028, "model_logloss": 0.6076, "kalshi_logloss": 0.5849}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.242, "share_ge_15": 0.4347, "median_abs_gap": 12.93, "n": 18647}, "gen1_elo": {"share_ge_25": 0.2363, "share_ge_15": 0.4278, "median_abs_gap": 12.42, "n": 18647}, "gen1_sr": {"share_ge_25": 0.3034, "share_ge_15": 0.522, "median_abs_gap": 15.82, "n": 18647}, "gen2": {"share_ge_25": 0.3041, "share_ge_15": 0.5077, "median_abs_gap": 15.39, "n": 18647}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1453, "share_ge_15": 0.3438, "median_abs_gap": 10.56, "n": 14324}, "gen1_elo": {"share_ge_25": 0.1428, "share_ge_15": 0.3329, "median_abs_gap": 10.03, "n": 14323}, "gen1_sr": {"share_ge_25": 0.2073, "share_ge_15": 0.4413, "median_abs_gap": 13.14, "n": 14324}, "gen2": {"share_ge_25": 0.2207, "share_ge_15": 0.438, "median_abs_gap": 12.91, "n": 14325}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.24, "share_ge_25_all": 0.0141, "share_ge_25_pregame_clean": 0.0138}, "WTA": {"median_abs_gap_pregame_clean": 7.85, "share_ge_25_all": 0.062, "share_ge_25_pregame_clean": 0.0551}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.239, "share_within_10pp_all": 0.44, "share_within_10pp_pregame_clean": 0.4988, "corr_model_vs_mid_pregame_clean": 0.8477}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 447, "model_brier": 0.1929, "kalshi_brier": 0.1944, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 518, "model_brier": 0.2111, "kalshi_brier": 0.2018, "brier_diff_model_minus_kalshi": 0.0093}, "15-25": {"n_settled": 641, "model_brier": 0.2306, "kalshi_brier": 0.2183, "brier_diff_model_minus_kalshi": 0.0123}, "25-40": {"n_settled": 348, "model_brier": 0.2258, "kalshi_brier": 0.2082, "brier_diff_model_minus_kalshi": 0.0176}, "3-5": {"n_settled": 288, "model_brier": 0.1905, "kalshi_brier": 0.1907, "brier_diff_model_minus_kalshi": -0.0003}, "40+": {"n_settled": 72, "model_brier": 0.29, "kalshi_brier": 0.1741, "brier_diff_model_minus_kalshi": 0.116}, "5-10": {"n_settled": 620, "model_brier": 0.1943, "kalshi_brier": 0.1952, "brier_diff_model_minus_kalshi": -0.0009}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.547, "slope": 0.869, "slope_se": 0.047}, "kalshi_slope": {"intercept": 0.232, "slope": 1.128, "slope_se": 0.053}, "n": 2934}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.505, "slope": 0.873, "slope_se": 0.035}, "kalshi_slope": {"intercept": 0.159, "slope": 1.083, "slope_se": 0.039}, "n": 4915}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 301, "model_brier": 0.3319, "kalshi_brier": 0.2309, "brier_diff_model_minus_kalshi": 0.101, "brier_diff_se": 0.0185, "corr_model_outcome": -0.0098, "corr_kalshi_outcome": 0.2765}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
