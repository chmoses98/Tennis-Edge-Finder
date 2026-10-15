# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-15T22:10Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 34,178): 0-3 14.4%, 3-5 9.4%, 5-10 20.1%, 10-15 15.3%, 15-25 18.9%, 25-40 13.7%, 40+ 8.3%; median gap 11.89 pp.
* **Where the extremes live**: 98.3% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.0%, Challenger 12.1%, doubles 6.8%). Main tour: ATP 1.4% and WTA 6.2% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 7,495): MARKET_ALREADY_SETTLED_WHEN_PRICED 37.0%, STALE_QUOTE 18.1%, BOOK_QUALITY 17.4%, POOR_DATA 8.3%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 3.9%, IN_PLAY_QUOTE 3.2%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.4%. By class: coverage 37.0%, market_freshness 18.1%, execution 17.4%, data 12.2%, market_freshness/coverage 8.7%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.4%.
* **Stale / settled / in-play**: 54.1% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 45.6% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 7,495 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.0% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 3.7%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 21.9% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 553.0 points vs 1766.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.064, Gen-2 0.868, Gen-1 ledger 0.871 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 349 model 0.2254 vs Kalshi 0.2087; n 72 model 0.29 vs Kalshi 0.1741.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 135,508 model-market comparisons (225,826 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 47,365 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-15T22:00:39.646976+00:00'], shadow board 37,845 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-15T22:00:44.304615+00:00'], Model 4 14,319 rows, 14,690 settled tickers, 4,884 tickers with an external scan.
* By model: {"gen1_ledger": 31097, "gen1_elo": 19025, "fair_v1": 19025, "gen2": 19025, "gen1_sr": 19025, "model4_fundamental": 14160, "model4_conditioned": 14151}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 34,178 | 14.4 | 9.4 | 20.1 | 15.3 | 18.9 | 13.7 | 8.3 | 11.89 | 40.8% | 21.9% |
| MW fair_v1 | 19,025 | 13.5 | 8.4 | 18.5 | 15.8 | 19.3 | 14.6 | 9.8 | 12.99 | 43.7% | 24.4% |
| MW gen1_elo | 19,025 | 13.2 | 8.9 | 19.7 | 15.2 | 19.2 | 14.3 | 9.5 | 12.47 | 43.1% | 23.9% |
| MW gen1_ledger | 15,153 | 15.5 | 10.7 | 21.9 | 14.6 | 18.4 | 12.5 | 6.3 | 10.45 | 37.2% | 18.8% |
| MW gen1_sr | 19,025 | 9.7 | 7.5 | 16.2 | 14.2 | 21.8 | 18.7 | 11.9 | 15.91 | 52.4% | 30.6% |
| MW gen2 | 19,025 | 11.5 | 7.1 | 16.4 | 14.1 | 20.3 | 17.5 | 13.2 | 15.47 | 51.0% | 30.7% |
| all families model4_conditioned | 14,151 | 21.6 | 20.1 | 35.2 | 16.7 | 4.3 | 1.1 | 0.9 | 5.81 | 6.3% | 2.0% |
| all families model4_fundamental | 14,160 | 16.8 | 13.6 | 35.7 | 19.6 | 10.6 | 2.6 | 1.1 | 7.58 | 14.3% | 3.7% |

Configurable thresholds (primary): >=5pp 76.2%, >=10pp 56.1%, >=15pp 40.8%, >=20pp 30.3%, >=25pp 21.9%, >=30pp 15.9%, >=40pp 8.3%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.5pp; >=10pp 45.4%, >=25pp 17.5%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,338 | 30.6 | 14.5 | 25.3 | 17.4 | 10.2 | 1.1 | 0.8 | 5.69 | 12.2% | 1.9% |
| CHALLENGER | 3,187 | 15.8 | 9.9 | 20.1 | 15.9 | 14.7 | 12.1 | 11.6 | 11.53 | 38.4% | 23.7% |
| ITF_MEN | 5,448 | 11.1 | 8.2 | 17.8 | 14.8 | 19.8 | 16.2 | 12.1 | 14.24 | 48.1% | 28.4% |
| ITF_WOMEN | 7,498 | 10.3 | 6.6 | 16.2 | 15.9 | 22.2 | 18.1 | 10.8 | 15.45 | 51.1% | 28.9% |
| WTA | 951 | 21.4 | 10.7 | 24.7 | 15.7 | 20.8 | 5.6 | 1.2 | 8.17 | 27.6% | 6.7% |
| WTA125 | 603 | 13.3 | 7.6 | 21.9 | 21.1 | 20.7 | 13.6 | 1.8 | 11.33 | 36.1% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,338 | 24.8 | 14.5 | 24.7 | 18.8 | 14.3 | 1.9 | 1.0 | 6.55 | 17.2% | 2.8% |
| CHALLENGER | 3,187 | 14.8 | 7.8 | 19.5 | 13.4 | 18.2 | 14.2 | 12.2 | 12.73 | 44.6% | 26.4% |
| ITF_MEN | 5,448 | 9.6 | 6.9 | 15.8 | 13.6 | 20.0 | 19.1 | 14.9 | 16.64 | 54.0% | 34.0% |
| ITF_WOMEN | 7,498 | 8.7 | 5.6 | 13.6 | 13.4 | 21.7 | 20.7 | 16.3 | 18.68 | 58.7% | 37.0% |
| WTA | 951 | 17.5 | 8.2 | 18.9 | 16.1 | 22.9 | 15.2 | 1.2 | 12.08 | 39.3% | 16.4% |
| WTA125 | 603 | 6.3 | 4.6 | 16.9 | 17.7 | 25.5 | 19.7 | 9.1 | 17.24 | 54.4% | 28.9% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,338 | 27.9 | 14.3 | 28.7 | 15.2 | 10.4 | 2.5 | 0.9 | 6.03 | 13.8% | 3.4% |
| CHALLENGER | 3,187 | 15.1 | 10.2 | 20.6 | 15.1 | 15.4 | 11.7 | 11.9 | 11.01 | 39.0% | 23.6% |
| ITF_MEN | 5,448 | 10.1 | 8.2 | 18.3 | 14.1 | 20.4 | 16.6 | 12.3 | 14.77 | 49.3% | 28.8% |
| ITF_WOMEN | 7,498 | 9.9 | 6.9 | 16.3 | 15.8 | 23.0 | 18.2 | 9.9 | 15.46 | 51.1% | 28.1% |
| WTA | 951 | 22.6 | 15.3 | 32.5 | 16.1 | 10.6 | 2.1 | 0.7 | 6.17 | 13.5% | 2.8% |
| WTA125 | 603 | 22.6 | 12.9 | 29.0 | 15.1 | 13.8 | 6.3 | 0.3 | 7.5 | 20.4% | 6.6% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 729 | 31.0 | 22.9 | 35.2 | 9.2 | 1.2 | 0.4 | 0.0 | 4.69 | 1.7% | 0.4% |
| CHALLENGER | 2,178 | 22.2 | 15.5 | 27.6 | 14.7 | 12.9 | 5.0 | 2.0 | 6.98 | 20.0% | 7.1% |
| DOUBLES | 1,029 | 5.3 | 3.8 | 11.5 | 10.8 | 18.9 | 24.5 | 25.3 | 24.5 | 68.6% | 49.8% |
| ITF_MEN | 4,661 | 14.7 | 8.5 | 20.7 | 15.4 | 20.8 | 12.6 | 7.3 | 11.88 | 40.6% | 19.9% |
| ITF_WOMEN | 5,073 | 11.7 | 9.3 | 19.6 | 14.7 | 22.3 | 16.6 | 5.7 | 13.01 | 44.7% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 653 | 21.3 | 15.3 | 27.3 | 17.1 | 13.6 | 4.9 | 0.5 | 7.52 | 19.0% | 5.4% |
| WTA125 | 681 | 20.6 | 13.5 | 22.8 | 18.4 | 14.4 | 8.2 | 2.2 | 8.27 | 24.8% | 10.4% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,324 | 30.6 | 14.4 | 25.4 | 17.4 | 10.2 | 1.1 | 0.8 | 5.75 | 12.1% | 1.9% |
| CHALLENGER | 2,276 | 20.5 | 12.5 | 25.2 | 18.5 | 15.1 | 5.9 | 2.4 | 8.31 | 23.4% | 8.3% |
| ITF_MEN | 3,966 | 13.5 | 10.1 | 21.1 | 16.5 | 20.1 | 13.1 | 5.6 | 11.38 | 38.7% | 18.7% |
| ITF_WOMEN | 5,561 | 12.2 | 8.0 | 18.5 | 18.1 | 23.7 | 14.9 | 4.6 | 13.0 | 43.2% | 19.5% |
| WTA | 931 | 21.6 | 10.1 | 25.0 | 15.7 | 20.9 | 5.5 | 1.2 | 8.18 | 27.6% | 6.7% |
| WTA125 | 579 | 13.6 | 7.4 | 21.2 | 21.4 | 21.4 | 13.5 | 1.4 | 11.47 | 36.3% | 14.8% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,324 | 24.7 | 14.6 | 24.9 | 18.7 | 14.3 | 1.8 | 1.0 | 6.58 | 17.2% | 2.8% |
| CHALLENGER | 2,276 | 19.0 | 9.9 | 24.4 | 16.2 | 18.4 | 9.5 | 2.6 | 9.08 | 30.6% | 12.1% |
| ITF_MEN | 3,967 | 11.3 | 8.1 | 18.1 | 15.3 | 22.1 | 16.5 | 8.5 | 14.04 | 47.0% | 25.0% |
| ITF_WOMEN | 5,561 | 9.8 | 6.5 | 15.2 | 14.7 | 23.8 | 19.9 | 10.1 | 16.34 | 53.8% | 30.0% |
| WTA | 931 | 17.4 | 8.1 | 18.9 | 16.1 | 23.0 | 15.4 | 1.2 | 12.12 | 39.5% | 16.5% |
| WTA125 | 579 | 6.0 | 4.8 | 16.9 | 18.1 | 25.4 | 20.4 | 8.3 | 17.19 | 54.1% | 28.7% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 709 | 31.0 | 23.1 | 35.5 | 9.3 | 0.6 | 0.4 | 0.0 | 4.64 | 1.0% | 0.4% |
| CHALLENGER | 1,874 | 24.0 | 16.9 | 29.8 | 14.5 | 12.0 | 2.4 | 0.5 | 6.36 | 14.9% | 2.9% |
| DOUBLES | 950 | 5.5 | 3.9 | 11.8 | 10.8 | 18.9 | 24.4 | 24.6 | 24.2 | 68.0% | 49.0% |
| ITF_MEN | 3,833 | 16.2 | 9.3 | 22.7 | 16.2 | 20.6 | 10.5 | 4.4 | 10.54 | 35.5% | 14.9% |
| ITF_WOMEN | 4,143 | 12.9 | 10.0 | 21.5 | 15.5 | 22.5 | 15.0 | 2.6 | 11.56 | 40.1% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 619 | 21.8 | 16.0 | 27.5 | 17.1 | 13.9 | 3.7 | 0.0 | 7.21 | 17.6% | 3.7% |
| WTA125 | 576 | 22.6 | 14.9 | 24.3 | 20.0 | 12.8 | 5.0 | 0.3 | 7.33 | 18.2% | 5.4% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,029 | 5.3 | 3.8 | 11.5 | 10.8 | 18.9 | 24.5 | 25.3 | 24.5 | 68.6% | 49.8% |
| singles | 14,124 | 16.3 | 11.2 | 22.7 | 14.9 | 18.4 | 11.6 | 4.9 | 9.95 | 34.9% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 4,464 | 13.2 | 9.0 | 19.6 | 15.9 | 18.0 | 14.4 | 10.0 | 12.66 | 42.4% | 24.4% |
| Grass | 201 | 11.9 | 11.4 | 14.9 | 14.4 | 22.4 | 16.9 | 8.0 | 14.16 | 47.3% | 24.9% |
| Hard | 12,358 | 13.8 | 8.4 | 18.5 | 15.4 | 19.7 | 14.4 | 9.7 | 12.99 | 43.9% | 24.2% |
| UNKNOWN | 2,002 | 12.1 | 7.0 | 17.0 | 18.7 | 19.1 | 15.7 | 10.3 | 13.38 | 45.2% | 26.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,500 | 19.7 | 10.7 | 20.9 | 16.9 | 15.8 | 8.9 | 7.0 | 9.54 | 31.7% | 15.9% |
| B | 2,482 | 14.2 | 9.0 | 19.9 | 16.6 | 18.1 | 12.5 | 9.6 | 11.63 | 40.2% | 22.1% |
| C | 2,755 | 12.8 | 9.4 | 20.0 | 14.3 | 19.4 | 14.3 | 9.8 | 12.66 | 43.5% | 24.1% |
| D | 3,306 | 11.4 | 7.9 | 17.7 | 16.1 | 22.0 | 15.4 | 9.5 | 13.92 | 46.9% | 24.9% |
| F | 4,982 | 8.1 | 5.3 | 15.0 | 14.9 | 21.9 | 21.6 | 13.3 | 17.95 | 56.8% | 34.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,389 | 22.8 | 15.9 | 28.9 | 15.1 | 11.3 | 4.4 | 1.7 | 6.7 | 17.4% | 6.1% |
| B | 2,277 | 14.9 | 10.0 | 24.0 | 16.3 | 19.5 | 11.1 | 4.2 | 10.19 | 34.7% | 15.2% |
| C | 3,000 | 12.2 | 7.8 | 18.2 | 14.2 | 20.3 | 15.8 | 11.6 | 13.7 | 47.6% | 27.3% |
| D | 2,277 | 14.1 | 9.8 | 20.8 | 13.6 | 21.3 | 13.9 | 6.6 | 11.85 | 41.8% | 20.5% |
| F | 3,210 | 10.2 | 7.5 | 15.2 | 14.0 | 23.6 | 20.4 | 9.1 | 16.36 | 53.1% | 29.5% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 6,216 | 18.0 | 9.7 | 20.2 | 16.8 | 16.3 | 9.9 | 9.2 | 10.59 | 35.4% | 19.1% |
| LIMITED | 4,417 | 14.8 | 10.3 | 20.8 | 15.3 | 18.6 | 12.8 | 7.3 | 11.21 | 38.7% | 20.1% |
| POOR | 8,392 | 9.5 | 6.5 | 16.1 | 15.4 | 21.9 | 19.0 | 11.7 | 15.97 | 52.6% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,054 | 31.2 | 24.6 | 36.2 | 5.5 | 1.7 | 0.7 | 0.1 | 4.49 | 2.5% | 0.7% |
| GAME_SPREAD | 2,900 | 25.8 | 16.2 | 36.6 | 16.8 | 4.1 | 0.4 | 0.2 | 5.96 | 4.7% | 0.6% |
| MATCH_WINNER | 15,153 | 15.5 | 10.7 | 21.9 | 14.6 | 18.4 | 12.5 | 6.3 | 10.45 | 37.2% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 5,537 | 33.5 | 19.6 | 31.0 | 9.6 | 5.1 | 1.1 | 0.2 | 4.69 | 6.4% | 1.4% |
| TOTAL_GAMES | 4,429 | 6.7 | 9.2 | 39.3 | 29.4 | 10.4 | 2.7 | 2.3 | 9.44 | 15.4% | 5.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,945 | 25.6 | 38.3 | 31.4 | 0.3 | 3.8 | 0.4 | 0.1 | 4.29 | 4.4% | 0.5% |
| GAME_SPREAD | 3,525 | 45.4 | 16.5 | 28.6 | 7.3 | 1.1 | 0.7 | 0.4 | 3.54 | 2.2% | 1.1% |
| TOTAL_GAMES | 5,681 | 3.5 | 6.6 | 42.7 | 36.7 | 6.8 | 1.9 | 1.9 | 9.77 | 10.6% | 3.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,945 | 26.4 | 18.9 | 37.0 | 9.1 | 6.2 | 2.1 | 0.3 | 5.47 | 8.6% | 2.4% |
| GAME_SPREAD | 3,525 | 19.6 | 13.6 | 30.4 | 20.8 | 12.8 | 2.3 | 0.7 | 7.65 | 15.7% | 3.0% |
| TOTAL_GAMES | 5,690 | 6.6 | 9.1 | 37.9 | 28.0 | 13.1 | 3.2 | 2.1 | 9.61 | 18.4% | 5.3% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 19,025 | 43.7% | 24.4% | 12.99 | 34.8% | 14.9% | 10.64 |
| gen1_elo | 19,025 | 43.1% | 23.9% | 12.47 | 33.8% | 14.7% | 10.11 |
| gen1_sr | 19,025 | 52.4% | 30.6% | 15.91 | 44.5% | 21.1% | 13.3 |
| gen2 | 19,025 | 51.0% | 30.7% | 15.47 | 44.1% | 22.5% | 13.02 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 10,029 | 16.3 | 10.4 | 21.6 | 17.3 | 19.7 | 11.3 | 3.3 | 10.46 | 34.3% | 14.6% |
| STALE | 8,996 | 10.3 | 6.2 | 15.1 | 14.2 | 18.8 | 18.3 | 17.1 | 17.15 | 54.2% | 35.4% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 8,621 | 17.4 | 11.6 | 23.6 | 14.5 | 16.9 | 11.2 | 4.9 | 9.38 | 32.9% | 16.1% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 34,178 | 8621 | 13501 | 12056 | 24.4 | 159.1 | 1400.4 |
| ge_15pp | 13,957 | 2839 | 4733 | 6385 | 26.9 | 459.7 | 1380.4 |
| ge_25pp | 7,495 | 1385 | 2056 | 4054 | 34.5 | 592.1 | 1380.4 |
| lt_10pp | 14,993 | 4530 | 6478 | 3985 | 22.6 | 48.9 | 1341.5 |

Current slate `SL-20261015T221052Z-5a66cedc`: 232 priced rows, quote age at build {'median': 10.4, 'max': 10.5}, freshness {'AGING': 232}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 10 | 0.0 | 0.0 | 40.0 | 0.0 | 40.0 | 20.0 | 0.0 | 20.33 | 60.0% | 20.0% |
| EXTERNAL_LONE_OUTLIER | 11 | 72.7 | 27.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,574 | 21.1 | 10.7 | 22.8 | 18.4 | 19.2 | 7.1 | 0.6 | 8.86 | 27.0% | 7.8% |
| KALSHI_LONE_OUTLIER | 8 | 12.5 | 0.0 | 62.5 | 0.0 | 12.5 | 12.5 | 0.0 | 5.11 | 25.0% | 12.5% |
| MARKETS_AGREE | 264 | 71.6 | 28.4 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.05 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 523 | 0.0 | 3.8 | 34.4 | 28.5 | 24.3 | 8.4 | 0.6 | 11.67 | 33.3% | 9.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 19,025 | 2390 (12.6%) | 21.9% | 0.7% | {"EXTERNAL_STALE": 1574, "AGREES_WITH_KALSHI": 523, "ALL_AGREE": 264, "EXTERNAL_OUTLIER": 11, "SUPPORTS_MODEL_DIRECTION": 9, "AGREES_WITH_MODEL": 8, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 8,319 | 607 (7.3%) | 28.7% | 1.3% | {"EXTERNAL_STALE": 425, "AGREES_WITH_KALSHI": 174, "SUPPORTS_MODEL_DIRECTION": 6, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 4,648 | 172 (3.7%) | 27.3% | 1.7% | {"EXTERNAL_STALE": 122, "AGREES_WITH_KALSHI": 47, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,187 | 162 (7.4%) | 27.8% | 1.8% | {"EXTERNAL_STALE": 114, "AGREES_WITH_KALSHI": 45, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 7,694 | 1344 (17.5%) | 14.9% | 0.7% | {"EXTERNAL_STALE": 859, "ALL_AGREE": 264, "AGREES_WITH_KALSHI": 200, "EXTERNAL_OUTLIER": 11, "AGREES_WITH_MODEL": 6, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,700 | 11.3 | 7.8 | 19.9 | 14.9 | 21.9 | 14.2 | 10.0 | 13.56 | 46.2% | 24.2% |
| 4-10x | 2,483 | 12.4 | 8.8 | 19.5 | 15.6 | 19.2 | 15.5 | 9.0 | 12.89 | 43.7% | 24.5% |
| <2x | 9,906 | 15.4 | 9.1 | 18.8 | 16.8 | 17.7 | 13.0 | 9.2 | 11.96 | 39.9% | 22.2% |
| >=10x | 2,936 | 11.0 | 6.5 | 15.2 | 13.9 | 21.2 | 19.6 | 12.7 | 16.44 | 53.5% | 32.2% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 4,976 | 13.6 | 8.3 | 19.3 | 16.0 | 19.6 | 12.9 | 10.3 | 12.78 | 42.9% | 23.2% |
| 300-1000 | 4,317 | 11.9 | 8.7 | 17.4 | 16.0 | 21.1 | 15.7 | 9.3 | 13.67 | 46.0% | 24.9% |
| <300 | 5,649 | 9.0 | 6.0 | 15.7 | 14.7 | 21.5 | 20.4 | 12.7 | 16.86 | 54.7% | 33.2% |
| >=3000 | 4,083 | 21.3 | 11.6 | 22.8 | 17.0 | 13.9 | 7.5 | 5.8 | 8.41 | 27.2% | 13.3% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 607 | 0.5374 | 0.4061 | 0.4876 | +0.050 | -0.082 | -0.0 ± 0.0059 |
| ratio 4-10x | 405 | 0.5843 | 0.4462 | 0.5111 | +0.073 | -0.065 | 0.007 ± 0.0077 |
| ratio <2x | 1468 | 0.5367 | 0.4143 | 0.4544 | +0.082 | -0.040 | 0.0112 ± 0.0037 |
| ratio >=10x | 484 | 0.5459 | 0.3787 | 0.4277 | +0.118 | -0.049 | 0.0144 ± 0.008 |
| thinner_sample 1000-3000 | 828 | 0.5426 | 0.4173 | 0.4722 | +0.070 | -0.055 | 0.0048 ± 0.005 |
| thinner_sample 300-1000 | 720 | 0.5595 | 0.4226 | 0.4875 | +0.072 | -0.065 | 0.0016 ± 0.0057 |
| thinner_sample <300 | 911 | 0.5436 | 0.3832 | 0.4413 | +0.102 | -0.058 | 0.0151 ± 0.0057 |
| thinner_sample >=3000 | 505 | 0.5298 | 0.4351 | 0.4614 | +0.068 | -0.026 | 0.0144 ± 0.0052 |
| data_status ADEQUATE | 852 | 0.5331 | 0.4283 | 0.4589 | +0.074 | -0.031 | 0.0092 ± 0.0043 |
| data_status LIMITED | 749 | 0.5513 | 0.4225 | 0.4913 | +0.060 | -0.069 | 0.0023 ± 0.0054 |
| data_status POOR | 1363 | 0.5487 | 0.3942 | 0.4534 | +0.095 | -0.059 | 0.0122 ± 0.0045 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 455 | 0.1931 | 0.1946 | -0.0015 ± 0.0007 | 0.5643 | 0.5675 | 0.4932 | 0.4783 | 0.5319 | -0.038 ± 0.0216 | -0.01 (5) |
| 3-5 | 289 | 0.1904 | 0.1908 | -0.0004 ± 0.0021 | 0.5607 | 0.5602 | 0.5089 | 0.469 | 0.4913 | -0.069 ± 0.0262 | 0.02 (1) |
| 5-10 | 626 | 0.1946 | 0.1949 | -0.0003 ± 0.0027 | 0.5737 | 0.5723 | 0.5091 | 0.4346 | 0.4665 | -0.081 ± 0.0183 | -0.0167 (6) |
| 10-15 | 525 | 0.2119 | 0.2033 | +0.0086 ± 0.0049 | 0.6115 | 0.5884 | 0.5203 | 0.3964 | 0.4229 | -0.086 ± 0.0196 | -0.048 (5) |
| 15-25 | 648 | 0.2303 | 0.2171 | +0.0132 ± 0.0071 | 0.6556 | 0.6203 | 0.5756 | 0.3805 | 0.446 | -0.075 ± 0.0182 | -0.0075 (8) |
| 25-40 | 349 | 0.2254 | 0.2087 | +0.0167 ± 0.0146 | 0.6416 | 0.5991 | 0.6448 | 0.3363 | 0.4642 | -0.061 ± 0.0224 | -0.01 (1) |
| 40+ | 72 | 0.29 | 0.1741 | +0.1160 ± 0.0438 | 0.7878 | 0.5206 | 0.7443 | 0.2967 | 0.3889 | -0.113 ± 0.0433 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2131 | 0.1764 | 0.1776 | -0.0012 ± 0.0003 | 0.5262 | 0.5275 | 0.4783 | 0.4632 | 0.5007 | -0.018 ± 0.0093 | -0.0129 (17) |
| 3-5 | 1310 | 0.1936 | 0.192 | +0.0016 ± 0.001 | 0.5679 | 0.5599 | 0.4808 | 0.4412 | 0.4374 | -0.062 ± 0.0123 | 0.0 (2) |
| 5-10 | 2914 | 0.1912 | 0.1891 | +0.0021 ± 0.0012 | 0.5642 | 0.5559 | 0.4835 | 0.4095 | 0.4293 | -0.045 ± 0.0082 | -0.0119 (21) |
| 10-15 | 2518 | 0.2016 | 0.1824 | +0.0192 ± 0.0021 | 0.5893 | 0.5369 | 0.4794 | 0.3549 | 0.3407 | -0.078 ± 0.0085 | -0.0281 (16) |
| 15-25 | 3059 | 0.2082 | 0.1726 | +0.0356 ± 0.0029 | 0.6087 | 0.5086 | 0.5008 | 0.3048 | 0.3135 | -0.064 ± 0.0075 | -0.0033 (42) |
| 25-40 | 2398 | 0.2198 | 0.1268 | +0.0930 ± 0.0045 | 0.633 | 0.3901 | 0.5278 | 0.2149 | 0.2269 | -0.059 ± 0.007 | -0.01 (1) |
| 40+ | 1613 | 0.3736 | 0.0435 | +0.3301 ± 0.0058 | 0.9726 | 0.1717 | 0.6252 | 0.1049 | 0.0583 | -0.083 ± 0.0049 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 347 | 0.1976 | 0.198 | -0.0004 ± 0.0008 | 0.5766 | 0.5775 | 0.5016 | 0.4864 | 0.5072 | -0.079 ± 0.0251 | -0.01 (3) |
| 3-5 | 235 | 0.2095 | 0.2085 | +0.0010 ± 0.0024 | 0.6008 | 0.5999 | 0.5168 | 0.4767 | 0.4809 | -0.081 ± 0.0313 | 0.02 (1) |
| 5-10 | 534 | 0.1985 | 0.1978 | +0.0007 ± 0.0029 | 0.5802 | 0.5787 | 0.553 | 0.4782 | 0.5112 | -0.072 ± 0.02 | -0.01 (4) |
| 10-15 | 485 | 0.2122 | 0.2049 | +0.0073 ± 0.0051 | 0.6105 | 0.5942 | 0.5679 | 0.4435 | 0.4804 | -0.084 ± 0.0213 | -0.04 (5) |
| 15-25 | 721 | 0.2288 | 0.2084 | +0.0204 ± 0.0067 | 0.6495 | 0.5991 | 0.5878 | 0.3909 | 0.4411 | -0.088 ± 0.0172 | -0.0188 (8) |
| 25-40 | 463 | 0.2652 | 0.2005 | +0.0647 ± 0.0131 | 0.7426 | 0.5821 | 0.6613 | 0.347 | 0.4039 | -0.108 ± 0.0207 | -0.0075 (4) |
| 40+ | 179 | 0.3563 | 0.1809 | +0.1755 ± 0.031 | 0.9856 | 0.5335 | 0.7393 | 0.259 | 0.3296 | -0.063 ± 0.0307 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1816 | 0.1828 | 0.1832 | -0.0004 ± 0.0003 | 0.5409 | 0.5415 | 0.4968 | 0.4821 | 0.505 | -0.034 ± 0.0104 | -0.0133 (15) |
| 3-5 | 1153 | 0.1924 | 0.1916 | +0.0008 ± 0.001 | 0.5596 | 0.5576 | 0.5152 | 0.4752 | 0.4848 | -0.041 ± 0.0131 | 0.02 (1) |
| 5-10 | 2534 | 0.1911 | 0.1883 | +0.0028 ± 0.0013 | 0.5647 | 0.5546 | 0.5148 | 0.4411 | 0.4609 | -0.043 ± 0.0088 | -0.0117 (6) |
| 10-15 | 2230 | 0.1944 | 0.1816 | +0.0128 ± 0.0023 | 0.5737 | 0.5325 | 0.5176 | 0.3933 | 0.4072 | -0.054 ± 0.0092 | -0.02 (17) |
| 15-25 | 3235 | 0.2162 | 0.1763 | +0.0399 ± 0.0029 | 0.6281 | 0.5202 | 0.5319 | 0.3354 | 0.3354 | -0.074 ± 0.0075 | -0.0095 (41) |
| 25-40 | 2801 | 0.2477 | 0.1385 | +0.1092 ± 0.0045 | 0.7028 | 0.422 | 0.5599 | 0.2435 | 0.2313 | -0.081 ± 0.0071 | -0.0044 (18) |
| 40+ | 2174 | 0.3988 | 0.0681 | +0.3307 ± 0.0064 | 1.046 | 0.2367 | 0.6634 | 0.1268 | 0.1003 | -0.066 ± 0.0055 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 450 | 0.1919 | 0.1947 | -0.0027 ± 0.0007 | 0.5626 | 0.5694 | 0.4926 | 0.4773 | 0.5556 | +0.002 ± 0.021 | -0.0137 (8) |
| 3-5 | 318 | 0.1875 | 0.1857 | +0.0018 ± 0.0019 | 0.5509 | 0.5463 | 0.4942 | 0.4548 | 0.4528 | -0.112 ± 0.0253 | 0.0067 (3) |
| 5-10 | 653 | 0.1992 | 0.1963 | +0.0029 ± 0.0026 | 0.5851 | 0.5746 | 0.504 | 0.4302 | 0.4441 | -0.089 ± 0.0178 | -0.0071 (7) |
| 10-15 | 514 | 0.208 | 0.2082 | -0.0001 ± 0.005 | 0.6037 | 0.6 | 0.5367 | 0.4137 | 0.4786 | -0.059 ± 0.02 | -0.0317 (6) |
| 15-25 | 597 | 0.2357 | 0.2114 | +0.0243 ± 0.0073 | 0.6709 | 0.6071 | 0.5834 | 0.3901 | 0.4238 | -0.106 ± 0.0186 | -0.03 (1) |
| 25-40 | 365 | 0.2111 | 0.2128 | -0.0017 ± 0.0141 | 0.6098 | 0.6087 | 0.6502 | 0.3402 | 0.4959 | -0.040 ± 0.0215 | 0.0 (1) |
| 40+ | 67 | 0.3098 | 0.1842 | +0.1256 ± 0.0472 | 0.8354 | 0.5436 | 0.749 | 0.2957 | 0.3881 | -0.101 ± 0.0493 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2045 | 0.183 | 0.1841 | -0.0012 ± 0.0003 | 0.5405 | 0.5427 | 0.483 | 0.4678 | 0.5012 | -0.019 ± 0.0095 | -0.0163 (35) |
| 3-5 | 1393 | 0.1859 | 0.1832 | +0.0027 ± 0.0009 | 0.5483 | 0.5419 | 0.4759 | 0.4365 | 0.4235 | -0.075 ± 0.0118 | -0.0094 (18) |
| 5-10 | 3091 | 0.1926 | 0.1867 | +0.0059 ± 0.0012 | 0.569 | 0.5494 | 0.4788 | 0.4049 | 0.3999 | -0.066 ± 0.0078 | -0.01 (31) |
| 10-15 | 2384 | 0.1951 | 0.1808 | +0.0143 ± 0.0022 | 0.5746 | 0.5315 | 0.4963 | 0.373 | 0.3767 | -0.063 ± 0.0087 | -0.015 (12) |
| 15-25 | 3122 | 0.2098 | 0.1712 | +0.0386 ± 0.0029 | 0.6142 | 0.5061 | 0.5048 | 0.3096 | 0.3097 | -0.070 ± 0.0074 | -0.03 (2) |
| 25-40 | 2350 | 0.2145 | 0.1256 | +0.0889 ± 0.0046 | 0.6208 | 0.3858 | 0.5249 | 0.2095 | 0.2302 | -0.053 ± 0.007 | 0.0 (1) |
| 40+ | 1558 | 0.387 | 0.046 | +0.3410 ± 0.0061 | 1.0101 | 0.1781 | 0.6338 | 0.1074 | 0.0584 | -0.084 ± 0.0052 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 774 | 0.1966 | 0.1969 | -0.0003 ± 0.0006 | 0.5744 | 0.5749 | 0.5046 | 0.4895 | 0.4974 | -0.047 ± 0.016 | -0.0224 (49) |
| 3-5 | 552 | 0.1938 | 0.1937 | +0.0002 ± 0.0015 | 0.5658 | 0.5638 | 0.4798 | 0.44 | 0.4547 | -0.043 ± 0.0188 | -0.0194 (34) |
| 5-10 | 1164 | 0.1955 | 0.1898 | +0.0057 ± 0.0019 | 0.5766 | 0.5607 | 0.487 | 0.4135 | 0.4124 | -0.063 ± 0.013 | -0.005 (78) |
| 10-15 | 728 | 0.2072 | 0.1968 | +0.0104 ± 0.0041 | 0.6026 | 0.5754 | 0.5034 | 0.3805 | 0.3984 | -0.051 ± 0.0165 | 0.0014 (64) |
| 15-25 | 980 | 0.233 | 0.2123 | +0.0206 ± 0.0058 | 0.6643 | 0.6106 | 0.5628 | 0.3682 | 0.4133 | -0.053 ± 0.0147 | -0.0216 (58) |
| 25-40 | 567 | 0.2522 | 0.1958 | +0.0564 ± 0.0115 | 0.7108 | 0.5688 | 0.6455 | 0.3327 | 0.3968 | -0.082 ± 0.0173 | -0.0219 (26) |
| 40+ | 193 | 0.3701 | 0.1933 | +0.1769 ± 0.0321 | 1.0713 | 0.5679 | 0.793 | 0.3026 | 0.3886 | -0.075 ± 0.029 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2312 | 0.188 | 0.1881 | -0.0001 ± 0.0003 | 0.5519 | 0.5512 | 0.5028 | 0.4874 | 0.4987 | -0.034 ± 0.009 | -0.0157 (88) |
| 3-5 | 1586 | 0.1879 | 0.1855 | +0.0024 ± 0.0009 | 0.5502 | 0.5446 | 0.4886 | 0.449 | 0.4395 | -0.056 ± 0.0109 | -0.0209 (69) |
| 5-10 | 3245 | 0.1926 | 0.1851 | +0.0075 ± 0.0011 | 0.5695 | 0.548 | 0.4804 | 0.4068 | 0.3957 | -0.063 ± 0.0077 | -0.0082 (132) |
| 10-15 | 2174 | 0.2037 | 0.1895 | +0.0142 ± 0.0023 | 0.5948 | 0.5571 | 0.5095 | 0.3865 | 0.3901 | -0.055 ± 0.0093 | -0.0053 (105) |
| 15-25 | 2741 | 0.2296 | 0.1989 | +0.0307 ± 0.0033 | 0.6625 | 0.5774 | 0.5548 | 0.3598 | 0.3798 | -0.059 ± 0.0086 | -0.0255 (106) |
| 25-40 | 1868 | 0.254 | 0.1695 | +0.0845 ± 0.006 | 0.7201 | 0.5007 | 0.6071 | 0.2926 | 0.3175 | -0.076 ± 0.0092 | -0.0229 (51) |
| 40+ | 908 | 0.3842 | 0.1314 | +0.2528 ± 0.0128 | 1.0905 | 0.4006 | 0.7088 | 0.202 | 0.2192 | -0.068 ± 0.0115 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2964 | 1.064 ± 0.052 | 1.175 | 0.1689 | 0.1715 | 0.2108 | 0.2019 |
| gen2 | 2964 | 0.868 ± 0.047 | 1.126 | 0.177 | 0.1715 | 0.2288 | 0.2018 |
| gen1_elo | 2964 | 1.045 ± 0.05 | 1.164 | 0.1738 | 0.172 | 0.2097 | 0.2018 |
| gen1_sr | 2964 | 1.08 ± 0.061 | 1.194 | 0.1363 | 0.1734 | 0.2248 | 0.2016 |
| gen1_ledger | 4958 | 0.871 ± 0.035 | 1.077 | 0.1773 | 0.1862 | 0.2179 | 0.1976 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 13,957)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,513 | 25.2% |
| STALE_QUOTE | market_freshness | 2,927 | 21.0% |
| BOOK_QUALITY | execution | 2,494 | 17.9% |
| POOR_DATA | data | 1,531 | 11.0% |
| LIMITED_DATA | data | 997 | 7.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 759 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 658 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 536 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 391 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 151 | 1.1% |

Cause class: coverage 25.2%, market_freshness 21.0%, data 18.1%, execution 17.9%, market_freshness/coverage 8.2%, model_calibration_or_unknown 4.7%, mapping 3.8%, model_calibration 1.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.1%, START_UNVERIFIABLE 96.0%, LOW_DATA_QUALITY 69.2%, THIN_PLAYER_HISTORY 58.1%, STALE_PLAYER_DATA 52.6%, STALE_KALSHI_QUOTE 45.8%, MODEL_INTERNAL_DISAGREEMENT 39.2%, ASYMMETRIC_SAMPLE_SIZE 31.9%, WIDE_SPREAD 23.8%, MODEL_HIGH_UNCERTAINTY 17.2%, PLAYER_IDENTITY_RISK 13.8%, LEVEL_TRANSFER_RISK 8.3%, EVENT_MAPPING_RISK 8.0%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 3.5%, EXTERNAL_MARKET_REJECTION 1.8%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 27.6%, POST_SETTLEMENT_OBSERVATION 25.2%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 7,495)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,770 | 37.0% |
| STALE_QUOTE | market_freshness | 1,358 | 18.1% |
| BOOK_QUALITY | execution | 1,301 | 17.4% |
| POOR_DATA | data | 620 | 8.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 410 | 5.5% |
| IDENTITY_AMBIGUOUS | mapping | 322 | 4.3% |
| LIMITED_DATA | data | 295 | 3.9% |
| IN_PLAY_QUOTE | market_freshness/coverage | 241 | 3.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 144 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 34 | 0.4% |

Cause class: coverage 37.0%, market_freshness 18.1%, execution 17.4%, data 12.2%, market_freshness/coverage 8.7%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.4%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.0%, START_UNVERIFIABLE 98.3%, LOW_DATA_QUALITY 72.8%, THIN_PLAYER_HISTORY 60.3%, STALE_KALSHI_QUOTE 54.1%, STALE_PLAYER_DATA 47.7%, MODEL_INTERNAL_DISAGREEMENT 40.2%, ASYMMETRIC_SAMPLE_SIZE 33.7%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 17.7%, PLAYER_IDENTITY_RISK 17.3%, EVENT_MAPPING_RISK 9.8%, LOW_DISPLAYED_LIQUIDITY 8.1%, LEVEL_TRANSFER_RISK 7.3%, MODEL_CALIBRATION_OUTLIER 4.5%, EXTERNAL_MARKET_REJECTION 0.9%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 39.7%, POST_SETTLEMENT_OBSERVATION 37.0%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 6000, "IDENTITY_AMBIGUOUS": 1495}; ticker orientation: {"VERIFIED": 7495}.

Checks: discipline:AMBIGUOUS 512, discipline:PASS 6983, identity_confidence:AMBIGUOUS 1300, identity_confidence:PASS 6195, level_mapping:NA 524, level_mapping:PASS 6971, market_pair:AMBIGUOUS 277, market_pair:NA 176, market_pair:PASS 7042, model_complement:NA 143, model_complement:PASS 7352, namesake:PASS 7495, physical_match_id:NA 2847, physical_match_id:PASS 4648, player_ids:PASS 7495, same_pair_other_event:PASS 7495, ticker_orientation:PASS 7495

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,067 | 1.4% | 1.4% | 0.4% | {"market_freshness": 20, "execution": 8, "market_freshness/coverage": 1} | 5.24 | 0.2093 / 0.2118 (255) | 16.4% | 0.5% | 5.4% | 1.6% |
| CHALLENGER | 5,365 | 17.0% | 5.9% | 12.1% | {"coverage": 554, "market_freshness/coverage": 113, "market_freshness": 111, "data": 58, "model_calibration_or_unknown": 46, "execution": 13, "model_calibration": 9, "mapping": 6} | 7.2 | 0.2167 / 0.2036 (1412) | 37.6% | 9.2% | 2.4% | 22.7% |
| DOUBLES | 1,029 | 49.8% | 49.0% | 6.8% | {"execution": 208, "mapping": 152, "market_freshness": 106, "market_freshness/coverage": 39, "coverage": 7} | 24.2 | 0.3322 / 0.234 (315) | 22.7% | 0.0% | 100.0% | 7.7% |
| ITF_MEN | 10,109 | 24.4% | 16.8% | 33.0% | {"coverage": 958, "execution": 508, "market_freshness": 386, "data": 330, "market_freshness/coverage": 202, "mapping": 85, "model_calibration_or_unknown": 2} | 11.04 | 0.2127 / 0.1948 (2496) | 36.8% | 60.2% | 11.6% | 22.9% |
| ITF_WOMEN | 12,571 | 26.2% | 18.7% | 44.0% | {"coverage": 1234, "market_freshness": 660, "execution": 543, "data": 493, "market_freshness/coverage": 250, "mapping": 73, "model_calibration_or_unknown": 35, "model_calibration": 10} | 12.5 | 0.2021 / 0.1921 (2666) | 39.5% | 57.7% | 10.0% | 22.8% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,604 | 6.2% | 5.5% | 1.3% | {"market_freshness": 36, "model_calibration_or_unknown": 22, "data": 11, "market_freshness/coverage": 10, "model_calibration": 8, "execution": 7, "coverage": 4, "mapping": 1} | 7.83 | 0.2398 / 0.2312 (289) | 26.4% | 1.3% | 1.7% | 3.4% |
| WTA125 | 1,284 | 12.8% | 10.1% | 2.2% | {"model_calibration_or_unknown": 37, "market_freshness": 37, "market_freshness/coverage": 35, "data": 23, "coverage": 12, "execution": 9, "model_calibration": 7, "mapping": 4} | 9.51 | 0.2148 / 0.2048 (447) | 23.7% | 7.9% | 4.3% | 10.1% |

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
| 8 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 9 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 10 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 11 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 12 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 13 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 14 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 15 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 16 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 17 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 18 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 19 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 20 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 22 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 23 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 24 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 25 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 26 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 92 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 27 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 28 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 29 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 30 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 31 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 32 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 33 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 34 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 35 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 36 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 547 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 37 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 39 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 40 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 41 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.8h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 359 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 42 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 43 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 44 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 45 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 46 | `KXATPCHALLENGERMATCH-26OCT13GIUSEA-SEA` | CHALLENGER | fair_v1 | 76% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 757 min (STALE); no external reference |
| 47 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 189 min (STALE); no external reference |
| 48 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 49 | `KXITFWMATCH-26OCT13MAMSTR-MAM` | ITF_WOMEN | fair_v1 | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 406 min (STALE); data LIMITED (grade C, thinner serve sample 879.0, ratio 2.64); no external reference |
| 50 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9829, "by_level_share_of_ge_25pp": {"ATP": 0.0039, "CHALLENGER": 0.1214, "DOUBLES": 0.0683, "ITF_MEN": 0.3297, "ITF_WOMEN": 0.44, "OTHER": 0.0016, "WTA": 0.0132, "WTA125": 0.0219}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5409, "share_primary_cause_market_settled_or_in_play": 0.4565, "share_primary_cause_stale_quote_only": 0.1812}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 7495, "identity_ambiguous_share": 0.1995, "ticker_orientation": {"VERIFIED": 7495}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 4648, "with_external": 172, "coverage": 0.037, "external_status": {"EXTERNAL_STALE": 122, "AGREES_WITH_KALSHI": 47, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 122, "MODEL_LONE_OUTLIER": 47, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.2733, "share_external_supports_model": 0.0174}, "pregame_clean_ge_25pp": {"n": 2187, "with_external": 162, "coverage": 0.0741, "external_status": {"EXTERNAL_STALE": 114, "AGREES_WITH_KALSHI": 45, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 114, "MODEL_LONE_OUTLIER": 45, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.2778, "share_external_supports_model": 0.0185}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 553.0, "median_sample_ratio": 2.38, "median_min_matches": 20.0, "median_max_days_since_last": 204.0, "share_severe_asymmetry": 0.2019, "data_status": {"POOR": 4003, "LIMITED": 2136, "ADEQUATE": 1356}, "comparison_lt_10pp": {"median_thinner_serve_points": 1766.0, "median_sample_ratio": 1.7, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 607, "model_minus_observed": 0.0498, "kalshi_minus_observed": -0.0816, "brier_diff_model_minus_kalshi": -0.0}, "4-10x": {"n": 405, "model_minus_observed": 0.0732, "kalshi_minus_observed": -0.0649, "brier_diff_model_minus_kalshi": 0.007}, "<2x": {"n": 1468, "model_minus_observed": 0.0823, "kalshi_minus_observed": -0.0401, "brier_diff_model_minus_kalshi": 0.0112}, ">=10x": {"n": 484, "model_minus_observed": 0.1182, "kalshi_minus_observed": -0.049, "brier_diff_model_minus_kalshi": 0.0144}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2964, "model": {"intercept": -0.543, "slope": 0.868, "slope_se": 0.047}, "kalshi_mid_same_rows": {"intercept": 0.235, "slope": 1.126, "slope_se": 0.053}, "mean_extremity_model": 0.177, "mean_extremity_kalshi": 0.1715, "model_brier": 0.2288, "kalshi_brier": 0.2018, "brier_diff_model_minus_kalshi": 0.027, "brier_diff_se": 0.0035, "model_logloss": 0.6531, "kalshi_logloss": 0.5855}, "fair_v1": {"n": 2964, "model": {"intercept": -0.392, "slope": 1.064, "slope_se": 0.052}, "kalshi_mid_same_rows": {"intercept": 0.325, "slope": 1.175, "slope_se": 0.054}, "mean_extremity_model": 0.1689, "mean_extremity_kalshi": 0.1715, "model_brier": 0.2108, "kalshi_brier": 0.2019, "brier_diff_model_minus_kalshi": 0.0088, "brier_diff_se": 0.0028, "model_logloss": 0.6088, "kalshi_logloss": 0.5856}, "gen1_elo": {"n": 2964, "model": {"intercept": -0.374, "slope": 1.045, "slope_se": 0.05}, "kalshi_mid_same_rows": {"intercept": 0.326, "slope": 1.164, "slope_se": 0.053}, "mean_extremity_model": 0.1738, "mean_extremity_kalshi": 0.172, "model_brier": 0.2097, "kalshi_brier": 0.2018, "brier_diff_model_minus_kalshi": 0.0079, "brier_diff_se": 0.0028, "model_logloss": 0.6072, "kalshi_logloss": 0.5852}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2443, "share_ge_15": 0.4373, "median_abs_gap": 12.99, "n": 19025}, "gen1_elo": {"share_ge_25": 0.2387, "share_ge_15": 0.4306, "median_abs_gap": 12.47, "n": 19025}, "gen1_sr": {"share_ge_25": 0.3061, "share_ge_15": 0.5242, "median_abs_gap": 15.91, "n": 19025}, "gen2": {"share_ge_25": 0.3069, "share_ge_15": 0.5097, "median_abs_gap": 15.47, "n": 19025}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1494, "share_ge_15": 0.3481, "median_abs_gap": 10.64, "n": 14637}, "gen1_elo": {"share_ge_25": 0.1473, "share_ge_15": 0.3375, "median_abs_gap": 10.11, "n": 14636}, "gen1_sr": {"share_ge_25": 0.2115, "share_ge_15": 0.4452, "median_abs_gap": 13.3, "n": 14637}, "gen2": {"share_ge_25": 0.2248, "share_ge_15": 0.4415, "median_abs_gap": 13.02, "n": 14638}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.24, "share_ge_25_all": 0.014, "share_ge_25_pregame_clean": 0.0138}, "WTA": {"median_abs_gap_pregame_clean": 7.83, "share_ge_25_all": 0.0617, "share_ge_25_pregame_clean": 0.0548}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2382, "share_within_10pp_all": 0.4387, "share_within_10pp_pregame_clean": 0.4969, "corr_model_vs_mid_pregame_clean": 0.8447}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 455, "model_brier": 0.1931, "kalshi_brier": 0.1946, "brier_diff_model_minus_kalshi": -0.0015}, "10-15": {"n_settled": 525, "model_brier": 0.2119, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.0086}, "15-25": {"n_settled": 648, "model_brier": 0.2303, "kalshi_brier": 0.2171, "brier_diff_model_minus_kalshi": 0.0132}, "25-40": {"n_settled": 349, "model_brier": 0.2254, "kalshi_brier": 0.2087, "brier_diff_model_minus_kalshi": 0.0167}, "3-5": {"n_settled": 289, "model_brier": 0.1904, "kalshi_brier": 0.1908, "brier_diff_model_minus_kalshi": -0.0004}, "40+": {"n_settled": 72, "model_brier": 0.29, "kalshi_brier": 0.1741, "brier_diff_model_minus_kalshi": 0.116}, "5-10": {"n_settled": 626, "model_brier": 0.1946, "kalshi_brier": 0.1949, "brier_diff_model_minus_kalshi": -0.0003}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.543, "slope": 0.868, "slope_se": 0.047}, "kalshi_slope": {"intercept": 0.235, "slope": 1.126, "slope_se": 0.053}, "n": 2964}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.508, "slope": 0.871, "slope_se": 0.035}, "kalshi_slope": {"intercept": 0.152, "slope": 1.077, "slope_se": 0.039}, "n": 4958}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 315, "model_brier": 0.3322, "kalshi_brier": 0.234, "brier_diff_model_minus_kalshi": 0.0982, "brier_diff_se": 0.0179, "corr_model_outcome": -0.0051, "corr_kalshi_outcome": 0.2496}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
