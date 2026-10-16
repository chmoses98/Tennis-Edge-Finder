# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-16T01:53Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 34,346): 0-3 14.4%, 3-5 9.4%, 5-10 20.1%, 10-15 15.3%, 15-25 18.9%, 25-40 13.7%, 40+ 8.2%; median gap 11.88 pp.
* **Where the extremes live**: 98.3% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.0%, Challenger 12.1%, doubles 6.8%). Main tour: ATP 1.4% and WTA 6.2% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 7,522): MARKET_ALREADY_SETTLED_WHEN_PRICED 36.8%, STALE_QUOTE 18.1%, BOOK_QUALITY 17.4%, POOR_DATA 8.3%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 4.0%, IN_PLAY_QUOTE 3.2%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.5%. By class: coverage 36.8%, market_freshness 18.1%, execution 17.4%, data 12.3%, market_freshness/coverage 8.7%, mapping 4.3%, model_calibration_or_unknown 2.0%, model_calibration 0.5%.
* **Stale / settled / in-play**: 53.9% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 45.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 7,522 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.9% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 3.8%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 21.6% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 553.0 points vs 1762.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.062, Gen-2 0.869, Gen-1 ledger 0.872 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 350 model 0.2248 vs Kalshi 0.2088; n 72 model 0.29 vs Kalshi 0.1741.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 136,132 model-market comparisons (226,990 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 47,473 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-16T01:43:43.702978+00:00'], shadow board 38,093 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-16T01:43:47.200665+00:00'], Model 4 14,351 rows, 14,710 settled tickers, 4,940 tickers with an external scan.
* By model: {"gen1_ledger": 31161, "gen1_elo": 19149, "fair_v1": 19149, "gen2": 19149, "gen1_sr": 19149, "model4_fundamental": 14192, "model4_conditioned": 14183}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 34,346 | 14.4 | 9.4 | 20.1 | 15.3 | 18.9 | 13.7 | 8.2 | 11.88 | 40.8% | 21.9% |
| MW fair_v1 | 19,149 | 13.5 | 8.4 | 18.6 | 15.8 | 19.3 | 14.6 | 9.8 | 12.96 | 43.7% | 24.4% |
| MW gen1_elo | 19,149 | 13.1 | 9.0 | 19.7 | 15.1 | 19.2 | 14.3 | 9.5 | 12.47 | 43.0% | 23.8% |
| MW gen1_ledger | 15,197 | 15.5 | 10.7 | 21.9 | 14.6 | 18.4 | 12.5 | 6.3 | 10.45 | 37.2% | 18.8% |
| MW gen1_sr | 19,149 | 9.7 | 7.5 | 16.2 | 14.2 | 21.8 | 18.7 | 11.9 | 15.9 | 52.4% | 30.6% |
| MW gen2 | 19,149 | 11.4 | 7.1 | 16.4 | 14.1 | 20.2 | 17.6 | 13.1 | 15.45 | 50.9% | 30.7% |
| all families model4_conditioned | 14,183 | 21.6 | 20.1 | 35.2 | 16.7 | 4.3 | 1.1 | 0.9 | 5.81 | 6.3% | 2.0% |
| all families model4_fundamental | 14,192 | 16.8 | 13.6 | 35.8 | 19.6 | 10.6 | 2.6 | 1.1 | 7.57 | 14.3% | 3.7% |

Configurable thresholds (primary): >=5pp 76.1%, >=10pp 56.1%, >=15pp 40.8%, >=20pp 30.3%, >=25pp 21.9%, >=30pp 15.9%, >=40pp 8.2%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.48pp; >=10pp 45.4%, >=25pp 17.4%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,340 | 30.7 | 14.5 | 25.3 | 17.4 | 10.2 | 1.1 | 0.8 | 5.69 | 12.2% | 1.9% |
| CHALLENGER | 3,201 | 15.9 | 9.9 | 20.1 | 15.8 | 14.6 | 12.2 | 11.5 | 11.51 | 38.3% | 23.7% |
| ITF_MEN | 5,490 | 11.1 | 8.2 | 17.7 | 14.8 | 19.9 | 16.2 | 12.1 | 14.24 | 48.1% | 28.3% |
| ITF_WOMEN | 7,552 | 10.3 | 6.6 | 16.3 | 15.8 | 22.2 | 18.0 | 10.8 | 15.4 | 51.0% | 28.8% |
| WTA | 955 | 21.3 | 10.9 | 24.7 | 15.6 | 20.8 | 5.5 | 1.1 | 8.16 | 27.5% | 6.7% |
| WTA125 | 611 | 13.1 | 7.7 | 22.3 | 20.9 | 20.5 | 13.6 | 2.0 | 11.33 | 36.0% | 15.6% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,340 | 24.9 | 14.5 | 24.8 | 18.7 | 14.3 | 1.9 | 1.0 | 6.55 | 17.2% | 2.8% |
| CHALLENGER | 3,201 | 14.8 | 7.8 | 19.5 | 13.4 | 18.2 | 14.2 | 12.1 | 12.73 | 44.5% | 26.3% |
| ITF_MEN | 5,490 | 9.6 | 6.9 | 15.9 | 13.6 | 20.0 | 19.2 | 14.8 | 16.63 | 54.0% | 34.0% |
| ITF_WOMEN | 7,552 | 8.6 | 5.7 | 13.6 | 13.4 | 21.6 | 20.8 | 16.2 | 18.65 | 58.6% | 37.0% |
| WTA | 955 | 17.4 | 8.3 | 19.1 | 16.0 | 22.8 | 15.3 | 1.1 | 12.08 | 39.3% | 16.4% |
| WTA125 | 611 | 6.2 | 4.8 | 16.9 | 18.0 | 25.4 | 19.6 | 9.2 | 17.24 | 54.2% | 28.8% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,340 | 28.0 | 14.3 | 28.7 | 15.2 | 10.4 | 2.5 | 0.9 | 6.03 | 13.7% | 3.4% |
| CHALLENGER | 3,201 | 15.0 | 10.2 | 20.7 | 15.1 | 15.4 | 11.7 | 11.9 | 11.01 | 39.0% | 23.6% |
| ITF_MEN | 5,490 | 10.1 | 8.2 | 18.3 | 14.1 | 20.5 | 16.5 | 12.2 | 14.75 | 49.2% | 28.8% |
| ITF_WOMEN | 7,552 | 10.0 | 6.9 | 16.4 | 15.8 | 23.0 | 18.1 | 9.8 | 15.42 | 50.9% | 28.0% |
| WTA | 955 | 22.6 | 15.3 | 32.5 | 16.2 | 10.6 | 2.1 | 0.7 | 6.17 | 13.4% | 2.8% |
| WTA125 | 611 | 22.6 | 12.8 | 29.1 | 14.9 | 14.1 | 6.2 | 0.3 | 7.52 | 20.6% | 6.6% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 730 | 31.0 | 22.9 | 35.3 | 9.2 | 1.2 | 0.4 | 0.0 | 4.69 | 1.6% | 0.4% |
| CHALLENGER | 2,191 | 22.3 | 15.5 | 27.6 | 14.7 | 12.9 | 5.1 | 2.0 | 6.94 | 20.0% | 7.1% |
| DOUBLES | 1,037 | 5.4 | 3.8 | 11.5 | 10.8 | 19.0 | 24.5 | 25.1 | 24.42 | 68.6% | 49.6% |
| ITF_MEN | 4,683 | 14.7 | 8.5 | 20.7 | 15.4 | 20.9 | 12.6 | 7.3 | 11.89 | 40.7% | 19.8% |
| ITF_WOMEN | 5,073 | 11.7 | 9.3 | 19.6 | 14.7 | 22.3 | 16.6 | 5.7 | 13.01 | 44.7% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 653 | 21.3 | 15.3 | 27.3 | 17.1 | 13.6 | 4.9 | 0.5 | 7.52 | 19.0% | 5.4% |
| WTA125 | 681 | 20.6 | 13.5 | 22.8 | 18.4 | 14.4 | 8.2 | 2.2 | 8.27 | 24.8% | 10.4% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,326 | 30.6 | 14.4 | 25.5 | 17.4 | 10.2 | 1.1 | 0.8 | 5.75 | 12.1% | 1.9% |
| CHALLENGER | 2,289 | 20.6 | 12.4 | 25.2 | 18.4 | 15.0 | 6.0 | 2.4 | 8.3 | 23.4% | 8.3% |
| ITF_MEN | 4,005 | 13.5 | 10.2 | 21.1 | 16.5 | 20.2 | 13.1 | 5.6 | 11.44 | 38.8% | 18.6% |
| ITF_WOMEN | 5,611 | 12.3 | 8.0 | 18.6 | 18.0 | 23.6 | 14.9 | 4.6 | 12.98 | 43.1% | 19.5% |
| WTA | 935 | 21.5 | 10.3 | 25.0 | 15.6 | 21.0 | 5.5 | 1.2 | 8.17 | 27.6% | 6.6% |
| WTA125 | 587 | 13.5 | 7.5 | 21.6 | 21.3 | 21.1 | 13.5 | 1.5 | 11.47 | 36.1% | 15.0% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,326 | 24.7 | 14.6 | 24.9 | 18.7 | 14.3 | 1.8 | 1.0 | 6.58 | 17.1% | 2.8% |
| CHALLENGER | 2,289 | 18.9 | 10.0 | 24.3 | 16.2 | 18.5 | 9.6 | 2.6 | 9.08 | 30.6% | 12.2% |
| ITF_MEN | 4,006 | 11.3 | 8.1 | 18.2 | 15.3 | 22.1 | 16.6 | 8.4 | 14.04 | 47.1% | 25.0% |
| ITF_WOMEN | 5,611 | 9.8 | 6.5 | 15.2 | 14.7 | 23.7 | 19.9 | 10.1 | 16.32 | 53.7% | 30.0% |
| WTA | 935 | 17.3 | 8.1 | 19.0 | 16.0 | 22.9 | 15.4 | 1.2 | 12.08 | 39.5% | 16.6% |
| WTA125 | 587 | 6.0 | 4.9 | 16.9 | 18.4 | 25.2 | 20.3 | 8.3 | 16.84 | 53.8% | 28.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 710 | 31.0 | 23.1 | 35.6 | 9.3 | 0.6 | 0.4 | 0.0 | 4.66 | 1.0% | 0.4% |
| CHALLENGER | 1,886 | 24.1 | 16.9 | 29.8 | 14.4 | 11.9 | 2.4 | 0.5 | 6.34 | 14.8% | 2.9% |
| DOUBLES | 956 | 5.5 | 3.9 | 11.8 | 10.9 | 19.0 | 24.5 | 24.4 | 24.11 | 67.9% | 48.9% |
| ITF_MEN | 3,853 | 16.2 | 9.3 | 22.6 | 16.2 | 20.8 | 10.5 | 4.4 | 10.57 | 35.7% | 14.9% |
| ITF_WOMEN | 4,141 | 12.9 | 10.1 | 21.4 | 15.5 | 22.6 | 15.0 | 2.6 | 11.56 | 40.1% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 619 | 21.8 | 16.0 | 27.5 | 17.1 | 13.9 | 3.7 | 0.0 | 7.21 | 17.6% | 3.7% |
| WTA125 | 576 | 22.6 | 14.9 | 24.3 | 20.0 | 12.8 | 5.0 | 0.3 | 7.33 | 18.2% | 5.4% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,037 | 5.4 | 3.8 | 11.5 | 10.8 | 19.0 | 24.5 | 25.1 | 24.42 | 68.6% | 49.6% |
| singles | 14,160 | 16.3 | 11.2 | 22.7 | 14.9 | 18.4 | 11.6 | 4.9 | 9.95 | 34.9% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 4,501 | 13.3 | 9.0 | 19.6 | 15.8 | 17.9 | 14.4 | 10.0 | 12.66 | 42.4% | 24.4% |
| Grass | 206 | 11.7 | 11.7 | 16.0 | 14.1 | 22.3 | 16.5 | 7.8 | 14.16 | 46.6% | 24.3% |
| Hard | 12,416 | 13.9 | 8.4 | 18.5 | 15.3 | 19.8 | 14.4 | 9.7 | 12.98 | 43.9% | 24.1% |
| UNKNOWN | 2,026 | 12.1 | 7.1 | 17.0 | 18.7 | 19.1 | 15.8 | 10.2 | 13.38 | 45.1% | 26.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,530 | 19.8 | 10.7 | 21.0 | 16.9 | 15.8 | 8.9 | 7.0 | 9.52 | 31.7% | 15.9% |
| B | 2,500 | 14.2 | 9.0 | 20.0 | 16.6 | 18.2 | 12.5 | 9.6 | 11.63 | 40.2% | 22.1% |
| C | 2,774 | 12.8 | 9.5 | 20.0 | 14.3 | 19.4 | 14.3 | 9.8 | 12.66 | 43.4% | 24.1% |
| D | 3,325 | 11.5 | 7.9 | 17.7 | 16.0 | 22.1 | 15.4 | 9.5 | 13.92 | 46.9% | 24.8% |
| F | 5,020 | 8.1 | 5.4 | 15.0 | 14.8 | 21.9 | 21.5 | 13.2 | 17.94 | 56.7% | 34.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,401 | 22.9 | 15.8 | 28.9 | 15.1 | 11.3 | 4.4 | 1.7 | 6.7 | 17.3% | 6.1% |
| B | 2,279 | 14.9 | 10.1 | 24.0 | 16.3 | 19.5 | 11.1 | 4.2 | 10.19 | 34.8% | 15.2% |
| C | 3,011 | 12.2 | 7.8 | 18.2 | 14.2 | 20.4 | 15.8 | 11.5 | 13.75 | 47.7% | 27.3% |
| D | 2,279 | 14.0 | 9.8 | 20.8 | 13.6 | 21.4 | 13.9 | 6.6 | 11.86 | 41.8% | 20.4% |
| F | 3,227 | 10.2 | 7.5 | 15.2 | 13.9 | 23.6 | 20.4 | 9.1 | 16.33 | 53.1% | 29.5% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 6,258 | 18.0 | 9.7 | 20.3 | 16.7 | 16.2 | 10.0 | 9.1 | 10.55 | 35.3% | 19.1% |
| LIMITED | 4,440 | 14.8 | 10.3 | 20.9 | 15.3 | 18.6 | 12.8 | 7.3 | 11.19 | 38.6% | 20.1% |
| POOR | 8,451 | 9.5 | 6.5 | 16.1 | 15.3 | 21.9 | 18.9 | 11.6 | 15.93 | 52.5% | 30.6% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,058 | 31.2 | 24.6 | 36.2 | 5.6 | 1.7 | 0.7 | 0.1 | 4.49 | 2.5% | 0.7% |
| GAME_SPREAD | 2,906 | 25.7 | 16.2 | 36.6 | 16.8 | 4.1 | 0.4 | 0.2 | 5.96 | 4.7% | 0.6% |
| MATCH_WINNER | 15,197 | 15.5 | 10.7 | 21.9 | 14.6 | 18.4 | 12.5 | 6.3 | 10.45 | 37.2% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 5,541 | 33.4 | 19.6 | 31.0 | 9.6 | 5.0 | 1.1 | 0.2 | 4.69 | 6.4% | 1.4% |
| TOTAL_GAMES | 4,435 | 6.7 | 9.2 | 39.4 | 29.4 | 10.4 | 2.7 | 2.3 | 9.44 | 15.4% | 5.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,953 | 25.6 | 38.3 | 31.4 | 0.3 | 3.8 | 0.4 | 0.1 | 4.29 | 4.4% | 0.5% |
| GAME_SPREAD | 3,531 | 45.4 | 16.5 | 28.6 | 7.2 | 1.1 | 0.7 | 0.4 | 3.54 | 2.2% | 1.1% |
| TOTAL_GAMES | 5,699 | 3.5 | 6.6 | 42.7 | 36.7 | 6.8 | 1.9 | 1.9 | 9.77 | 10.6% | 3.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,953 | 26.4 | 18.8 | 37.0 | 9.1 | 6.2 | 2.1 | 0.3 | 5.47 | 8.5% | 2.4% |
| GAME_SPREAD | 3,531 | 19.5 | 13.6 | 30.4 | 20.8 | 12.7 | 2.3 | 0.7 | 7.64 | 15.7% | 3.0% |
| TOTAL_GAMES | 5,708 | 6.6 | 9.1 | 38.0 | 28.0 | 13.1 | 3.2 | 2.1 | 9.61 | 18.4% | 5.3% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 19,149 | 43.7% | 24.4% | 12.96 | 34.8% | 14.9% | 10.63 |
| gen1_elo | 19,149 | 43.0% | 23.8% | 12.47 | 33.8% | 14.7% | 10.09 |
| gen1_sr | 19,149 | 52.4% | 30.6% | 15.9 | 44.5% | 21.2% | 13.29 |
| gen2 | 19,149 | 50.9% | 30.7% | 15.45 | 44.1% | 22.5% | 13.02 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 10,152 | 16.4 | 10.4 | 21.6 | 17.2 | 19.8 | 11.3 | 3.3 | 10.46 | 34.4% | 14.6% |
| STALE | 8,997 | 10.3 | 6.2 | 15.1 | 14.2 | 18.8 | 18.3 | 17.1 | 17.15 | 54.2% | 35.4% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 8,665 | 17.4 | 11.6 | 23.6 | 14.5 | 16.9 | 11.2 | 4.8 | 9.4 | 33.0% | 16.1% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 34,346 | 8665 | 13624 | 12057 | 24.4 | 156.9 | 1400.4 |
| ge_15pp | 14,022 | 2857 | 4779 | 6386 | 26.9 | 459.5 | 1380.4 |
| ge_25pp | 7,522 | 1391 | 2076 | 4055 | 34.5 | 589.9 | 1380.4 |
| lt_10pp | 15,078 | 4550 | 6543 | 3985 | 22.6 | 48.8 | 1341.5 |

Current slate `SL-20261016T015307Z-04cd0660`: 268 priced rows, quote age at build {'median': 9.6, 'max': 9.7}, freshness {'FRESH': 268}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 10 | 0.0 | 0.0 | 40.0 | 0.0 | 40.0 | 20.0 | 0.0 | 20.33 | 60.0% | 20.0% |
| EXTERNAL_LONE_OUTLIER | 11 | 72.7 | 27.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,617 | 21.0 | 10.8 | 22.9 | 18.2 | 19.2 | 7.1 | 0.7 | 8.85 | 27.0% | 7.8% |
| KALSHI_LONE_OUTLIER | 8 | 12.5 | 0.0 | 62.5 | 0.0 | 12.5 | 12.5 | 0.0 | 5.11 | 25.0% | 12.5% |
| MARKETS_AGREE | 264 | 71.6 | 28.4 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.05 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 525 | 0.0 | 3.8 | 34.5 | 28.4 | 24.2 | 8.6 | 0.6 | 11.67 | 33.3% | 9.1% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 19,149 | 2435 (12.7%) | 21.6% | 0.7% | {"EXTERNAL_STALE": 1617, "AGREES_WITH_KALSHI": 525, "ALL_AGREE": 264, "EXTERNAL_OUTLIER": 11, "SUPPORTS_MODEL_DIRECTION": 9, "AGREES_WITH_MODEL": 8, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 8,366 | 620 (7.4%) | 28.2% | 1.3% | {"EXTERNAL_STALE": 437, "AGREES_WITH_KALSHI": 175, "SUPPORTS_MODEL_DIRECTION": 6, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 4,669 | 177 (3.8%) | 27.1% | 1.7% | {"EXTERNAL_STALE": 126, "AGREES_WITH_KALSHI": 48, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,206 | 167 (7.6%) | 27.5% | 1.8% | {"EXTERNAL_STALE": 118, "AGREES_WITH_KALSHI": 46, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 7,759 | 1371 (17.7%) | 14.7% | 0.7% | {"EXTERNAL_STALE": 885, "ALL_AGREE": 264, "AGREES_WITH_KALSHI": 201, "EXTERNAL_OUTLIER": 11, "AGREES_WITH_MODEL": 6, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,720 | 11.3 | 7.7 | 19.9 | 14.9 | 21.9 | 14.3 | 10.0 | 13.57 | 46.2% | 24.3% |
| 4-10x | 2,495 | 12.5 | 8.9 | 19.6 | 15.5 | 19.2 | 15.4 | 9.0 | 12.89 | 43.6% | 24.4% |
| <2x | 9,971 | 15.4 | 9.1 | 18.8 | 16.8 | 17.8 | 13.0 | 9.1 | 11.95 | 39.9% | 22.1% |
| >=10x | 2,963 | 10.9 | 6.6 | 15.3 | 13.8 | 21.3 | 19.4 | 12.7 | 16.43 | 53.4% | 32.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 5,017 | 13.6 | 8.2 | 19.4 | 16.0 | 19.6 | 12.9 | 10.3 | 12.71 | 42.8% | 23.2% |
| 300-1000 | 4,341 | 11.9 | 8.7 | 17.4 | 16.0 | 21.1 | 15.8 | 9.2 | 13.67 | 46.1% | 25.0% |
| <300 | 5,693 | 9.0 | 6.1 | 15.7 | 14.6 | 21.6 | 20.3 | 12.7 | 16.82 | 54.6% | 33.0% |
| >=3000 | 4,098 | 21.4 | 11.6 | 22.8 | 17.0 | 13.9 | 7.4 | 5.8 | 8.39 | 27.2% | 13.3% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 607 | 0.5374 | 0.4061 | 0.4876 | +0.050 | -0.082 | -0.0 ± 0.0059 |
| ratio 4-10x | 407 | 0.5855 | 0.4466 | 0.5111 | +0.074 | -0.065 | 0.0071 ± 0.0078 |
| ratio <2x | 1470 | 0.5366 | 0.4143 | 0.4544 | +0.082 | -0.040 | 0.0111 ± 0.0037 |
| ratio >=10x | 487 | 0.5448 | 0.3782 | 0.4251 | +0.120 | -0.047 | 0.0147 ± 0.008 |
| thinner_sample 1000-3000 | 830 | 0.5425 | 0.4173 | 0.4723 | +0.070 | -0.055 | 0.0047 ± 0.005 |
| thinner_sample 300-1000 | 721 | 0.56 | 0.4227 | 0.4882 | +0.072 | -0.066 | 0.0013 ± 0.0057 |
| thinner_sample <300 | 915 | 0.5433 | 0.3831 | 0.4393 | +0.104 | -0.056 | 0.0156 ± 0.0057 |
| thinner_sample >=3000 | 505 | 0.5298 | 0.4351 | 0.4614 | +0.068 | -0.026 | 0.0144 ± 0.0052 |
| data_status ADEQUATE | 854 | 0.533 | 0.4282 | 0.459 | +0.074 | -0.031 | 0.009 ± 0.0043 |
| data_status LIMITED | 749 | 0.5513 | 0.4225 | 0.4913 | +0.060 | -0.069 | 0.0023 ± 0.0054 |
| data_status POOR | 1368 | 0.5487 | 0.3942 | 0.4525 | +0.096 | -0.058 | 0.0124 ± 0.0045 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 456 | 0.1927 | 0.1942 | -0.0015 ± 0.0007 | 0.5631 | 0.5663 | 0.4923 | 0.4773 | 0.5307 | -0.038 ± 0.0216 | -0.01 (5) |
| 3-5 | 290 | 0.1908 | 0.191 | -0.0003 ± 0.0021 | 0.5615 | 0.5607 | 0.509 | 0.4691 | 0.4897 | -0.072 ± 0.0263 | 0.02 (1) |
| 5-10 | 627 | 0.1948 | 0.195 | -0.0003 ± 0.0027 | 0.5741 | 0.5725 | 0.5092 | 0.4347 | 0.4657 | -0.081 ± 0.0183 | -0.0167 (6) |
| 10-15 | 526 | 0.2122 | 0.2039 | +0.0082 ± 0.0049 | 0.612 | 0.5897 | 0.5201 | 0.3962 | 0.424 | -0.085 ± 0.0196 | -0.048 (5) |
| 15-25 | 650 | 0.2309 | 0.2171 | +0.0138 ± 0.0071 | 0.6571 | 0.6203 | 0.5759 | 0.3807 | 0.4446 | -0.076 ± 0.0181 | -0.0075 (8) |
| 25-40 | 350 | 0.2248 | 0.2088 | +0.0160 ± 0.0145 | 0.6402 | 0.5993 | 0.6454 | 0.3367 | 0.4657 | -0.061 ± 0.0223 | -0.01 (1) |
| 40+ | 72 | 0.29 | 0.1741 | +0.1160 ± 0.0438 | 0.7878 | 0.5206 | 0.7443 | 0.2967 | 0.3889 | -0.113 ± 0.0433 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2140 | 0.1758 | 0.1769 | -0.0012 ± 0.0003 | 0.5244 | 0.5256 | 0.4766 | 0.4616 | 0.4986 | -0.018 ± 0.0092 | -0.0129 (17) |
| 3-5 | 1316 | 0.1932 | 0.1915 | +0.0017 ± 0.001 | 0.5668 | 0.5586 | 0.4802 | 0.4406 | 0.4362 | -0.063 ± 0.0123 | 0.0 (2) |
| 5-10 | 2919 | 0.1912 | 0.189 | +0.0022 ± 0.0012 | 0.5641 | 0.5557 | 0.4833 | 0.4094 | 0.4286 | -0.045 ± 0.0082 | -0.0119 (21) |
| 10-15 | 2522 | 0.2018 | 0.1827 | +0.0191 ± 0.0021 | 0.5897 | 0.5375 | 0.4794 | 0.3549 | 0.341 | -0.077 ± 0.0085 | -0.0281 (16) |
| 15-25 | 3072 | 0.2088 | 0.1726 | +0.0362 ± 0.0029 | 0.61 | 0.5087 | 0.5012 | 0.3052 | 0.3122 | -0.065 ± 0.0075 | -0.0033 (42) |
| 25-40 | 2404 | 0.22 | 0.1268 | +0.0932 ± 0.0045 | 0.6334 | 0.3901 | 0.5281 | 0.2151 | 0.2267 | -0.059 ± 0.007 | -0.01 (1) |
| 40+ | 1613 | 0.3736 | 0.0435 | +0.3301 ± 0.0058 | 0.9726 | 0.1717 | 0.6252 | 0.1049 | 0.0583 | -0.083 ± 0.0049 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 347 | 0.1976 | 0.198 | -0.0004 ± 0.0008 | 0.5766 | 0.5775 | 0.5016 | 0.4864 | 0.5072 | -0.079 ± 0.0251 | -0.01 (3) |
| 3-5 | 236 | 0.2098 | 0.2087 | +0.0011 ± 0.0024 | 0.6015 | 0.6004 | 0.5169 | 0.4769 | 0.4788 | -0.083 ± 0.0312 | 0.02 (1) |
| 5-10 | 535 | 0.1982 | 0.1974 | +0.0007 ± 0.0029 | 0.5793 | 0.5777 | 0.5521 | 0.4774 | 0.5103 | -0.072 ± 0.0199 | -0.01 (4) |
| 10-15 | 486 | 0.2126 | 0.205 | +0.0076 ± 0.0051 | 0.6113 | 0.5944 | 0.568 | 0.4436 | 0.4794 | -0.086 ± 0.0214 | -0.04 (5) |
| 15-25 | 723 | 0.2288 | 0.209 | +0.0198 ± 0.0067 | 0.6495 | 0.6003 | 0.5876 | 0.3908 | 0.4426 | -0.086 ± 0.0172 | -0.0188 (8) |
| 25-40 | 465 | 0.2649 | 0.2004 | +0.0645 ± 0.0131 | 0.7419 | 0.582 | 0.6617 | 0.3474 | 0.4043 | -0.109 ± 0.0206 | -0.0075 (4) |
| 40+ | 179 | 0.3563 | 0.1809 | +0.1755 ± 0.031 | 0.9856 | 0.5335 | 0.7393 | 0.259 | 0.3296 | -0.063 ± 0.0307 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1818 | 0.1829 | 0.1832 | -0.0004 ± 0.0003 | 0.5409 | 0.5416 | 0.4969 | 0.4822 | 0.505 | -0.034 ± 0.0104 | -0.0133 (15) |
| 3-5 | 1156 | 0.1925 | 0.1916 | +0.0009 ± 0.001 | 0.5596 | 0.5575 | 0.5156 | 0.4756 | 0.4844 | -0.042 ± 0.0131 | 0.02 (1) |
| 5-10 | 2549 | 0.1902 | 0.1874 | +0.0028 ± 0.0013 | 0.5625 | 0.552 | 0.5128 | 0.439 | 0.4586 | -0.043 ± 0.0087 | -0.0117 (6) |
| 10-15 | 2232 | 0.1946 | 0.1817 | +0.0129 ± 0.0023 | 0.574 | 0.5326 | 0.5177 | 0.3933 | 0.4068 | -0.055 ± 0.0092 | -0.02 (17) |
| 15-25 | 3241 | 0.2163 | 0.1767 | +0.0396 ± 0.0029 | 0.6282 | 0.521 | 0.5319 | 0.3355 | 0.3363 | -0.073 ± 0.0075 | -0.0095 (41) |
| 25-40 | 2814 | 0.2483 | 0.1384 | +0.1098 ± 0.0045 | 0.7038 | 0.4221 | 0.5603 | 0.244 | 0.2306 | -0.082 ± 0.007 | -0.0044 (18) |
| 40+ | 2176 | 0.3988 | 0.0681 | +0.3307 ± 0.0064 | 1.0459 | 0.2367 | 0.6633 | 0.1269 | 0.1002 | -0.066 ± 0.0055 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 451 | 0.1915 | 0.1943 | -0.0027 ± 0.0007 | 0.5615 | 0.5683 | 0.4936 | 0.4783 | 0.5565 | +0.002 ± 0.021 | -0.0137 (8) |
| 3-5 | 319 | 0.1879 | 0.1859 | +0.0020 ± 0.0019 | 0.5516 | 0.5468 | 0.4943 | 0.4549 | 0.4514 | -0.114 ± 0.0254 | 0.0067 (3) |
| 5-10 | 655 | 0.1998 | 0.1968 | +0.0029 ± 0.0026 | 0.5863 | 0.5759 | 0.5038 | 0.4301 | 0.4443 | -0.089 ± 0.0178 | -0.0071 (7) |
| 10-15 | 514 | 0.208 | 0.2082 | -0.0001 ± 0.005 | 0.6037 | 0.6 | 0.5367 | 0.4137 | 0.4786 | -0.059 ± 0.02 | -0.0317 (6) |
| 15-25 | 599 | 0.2364 | 0.2114 | +0.0250 ± 0.0073 | 0.6727 | 0.6072 | 0.5837 | 0.3903 | 0.4224 | -0.108 ± 0.0186 | -0.03 (1) |
| 25-40 | 366 | 0.2105 | 0.2129 | -0.0024 ± 0.0141 | 0.6085 | 0.609 | 0.6508 | 0.3406 | 0.4973 | -0.040 ± 0.0214 | 0.0 (1) |
| 40+ | 67 | 0.3098 | 0.1842 | +0.1256 ± 0.0472 | 0.8354 | 0.5436 | 0.749 | 0.2957 | 0.3881 | -0.101 ± 0.0493 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2055 | 0.1821 | 0.1832 | -0.0011 ± 0.0003 | 0.5382 | 0.5402 | 0.4813 | 0.4661 | 0.4993 | -0.019 ± 0.0095 | -0.0163 (35) |
| 3-5 | 1397 | 0.1857 | 0.183 | +0.0027 ± 0.0009 | 0.5478 | 0.5413 | 0.4759 | 0.4365 | 0.423 | -0.076 ± 0.0118 | -0.0094 (18) |
| 5-10 | 3099 | 0.1929 | 0.1869 | +0.0060 ± 0.0012 | 0.5695 | 0.5497 | 0.4786 | 0.4048 | 0.3995 | -0.066 ± 0.0078 | -0.01 (31) |
| 10-15 | 2385 | 0.1952 | 0.1808 | +0.0144 ± 0.0022 | 0.5747 | 0.5315 | 0.4963 | 0.3731 | 0.3765 | -0.063 ± 0.0087 | -0.015 (12) |
| 15-25 | 3136 | 0.2105 | 0.1712 | +0.0393 ± 0.0029 | 0.6157 | 0.5063 | 0.5053 | 0.3101 | 0.3084 | -0.072 ± 0.0074 | -0.03 (2) |
| 25-40 | 2355 | 0.2147 | 0.1256 | +0.0891 ± 0.0046 | 0.6212 | 0.3859 | 0.5252 | 0.2097 | 0.2301 | -0.054 ± 0.0069 | 0.0 (1) |
| 40+ | 1559 | 0.387 | 0.046 | +0.3410 ± 0.0061 | 1.0101 | 0.1781 | 0.6338 | 0.1075 | 0.0584 | -0.085 ± 0.0052 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 776 | 0.1965 | 0.1968 | -0.0003 ± 0.0006 | 0.5741 | 0.5744 | 0.5053 | 0.4902 | 0.4974 | -0.047 ± 0.0159 | -0.0224 (49) |
| 3-5 | 553 | 0.1938 | 0.1936 | +0.0002 ± 0.0015 | 0.5657 | 0.5636 | 0.4796 | 0.4398 | 0.4539 | -0.043 ± 0.0188 | -0.0194 (34) |
| 5-10 | 1164 | 0.1955 | 0.1898 | +0.0057 ± 0.0019 | 0.5766 | 0.5607 | 0.487 | 0.4135 | 0.4124 | -0.063 ± 0.013 | -0.005 (78) |
| 10-15 | 728 | 0.2072 | 0.1968 | +0.0104 ± 0.0041 | 0.6026 | 0.5754 | 0.5034 | 0.3805 | 0.3984 | -0.051 ± 0.0165 | 0.0014 (64) |
| 15-25 | 980 | 0.233 | 0.2123 | +0.0206 ± 0.0058 | 0.6643 | 0.6106 | 0.5628 | 0.3682 | 0.4133 | -0.053 ± 0.0147 | -0.0216 (58) |
| 25-40 | 568 | 0.2522 | 0.1955 | +0.0567 ± 0.0115 | 0.7107 | 0.5683 | 0.6452 | 0.3325 | 0.3961 | -0.083 ± 0.0173 | -0.0219 (26) |
| 40+ | 193 | 0.3701 | 0.1933 | +0.1769 ± 0.0321 | 1.0713 | 0.5679 | 0.793 | 0.3026 | 0.3886 | -0.075 ± 0.029 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2315 | 0.188 | 0.1881 | -0.0001 ± 0.0003 | 0.5518 | 0.5511 | 0.503 | 0.4876 | 0.4985 | -0.034 ± 0.009 | -0.0157 (88) |
| 3-5 | 1588 | 0.1878 | 0.1855 | +0.0024 ± 0.0009 | 0.5501 | 0.5445 | 0.4885 | 0.4488 | 0.4389 | -0.056 ± 0.0109 | -0.0209 (69) |
| 5-10 | 3246 | 0.1926 | 0.1851 | +0.0075 ± 0.0011 | 0.5694 | 0.5479 | 0.4806 | 0.4069 | 0.3959 | -0.063 ± 0.0077 | -0.0082 (132) |
| 10-15 | 2175 | 0.2038 | 0.1895 | +0.0143 ± 0.0023 | 0.5951 | 0.5572 | 0.5096 | 0.3865 | 0.3899 | -0.056 ± 0.0093 | -0.0053 (105) |
| 15-25 | 2742 | 0.2296 | 0.1989 | +0.0307 ± 0.0033 | 0.6624 | 0.5774 | 0.5549 | 0.3598 | 0.38 | -0.058 ± 0.0086 | -0.0255 (106) |
| 25-40 | 1870 | 0.254 | 0.1693 | +0.0846 ± 0.006 | 0.72 | 0.5004 | 0.6069 | 0.2925 | 0.3171 | -0.076 ± 0.0092 | -0.0229 (51) |
| 40+ | 910 | 0.3847 | 0.1312 | +0.2535 ± 0.0128 | 1.0915 | 0.4003 | 0.709 | 0.2021 | 0.2187 | -0.068 ± 0.0114 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2971 | 1.062 ± 0.052 | 1.173 | 0.1689 | 0.1714 | 0.2109 | 0.202 |
| gen2 | 2971 | 0.869 ± 0.047 | 1.125 | 0.177 | 0.1714 | 0.2288 | 0.2019 |
| gen1_elo | 2971 | 1.042 ± 0.05 | 1.162 | 0.1739 | 0.1719 | 0.2099 | 0.2019 |
| gen1_sr | 2971 | 1.08 ± 0.061 | 1.194 | 0.1363 | 0.1733 | 0.2248 | 0.2017 |
| gen1_ledger | 4962 | 0.872 ± 0.035 | 1.077 | 0.1772 | 0.1863 | 0.2179 | 0.1976 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 14,022)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,514 | 25.1% |
| STALE_QUOTE | market_freshness | 2,927 | 20.9% |
| BOOK_QUALITY | execution | 2,514 | 17.9% |
| POOR_DATA | data | 1,545 | 11.0% |
| LIMITED_DATA | data | 1,007 | 7.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 760 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 668 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 541 | 3.9% |
| IN_PLAY_QUOTE | market_freshness/coverage | 394 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 152 | 1.1% |

Cause class: coverage 25.1%, market_freshness 20.9%, data 18.2%, execution 17.9%, market_freshness/coverage 8.2%, model_calibration_or_unknown 4.8%, mapping 3.9%, model_calibration 1.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.1%, START_UNVERIFIABLE 96.0%, LOW_DATA_QUALITY 69.2%, THIN_PLAYER_HISTORY 58.1%, STALE_PLAYER_DATA 52.5%, STALE_KALSHI_QUOTE 45.5%, MODEL_INTERNAL_DISAGREEMENT 39.2%, ASYMMETRIC_SAMPLE_SIZE 31.9%, WIDE_SPREAD 23.8%, MODEL_HIGH_UNCERTAINTY 17.2%, PLAYER_IDENTITY_RISK 13.9%, LEVEL_TRANSFER_RISK 8.3%, EVENT_MAPPING_RISK 8.0%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 3.5%, EXTERNAL_MARKET_REJECTION 1.8%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 27.5%, POST_SETTLEMENT_OBSERVATION 25.1%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 7,522)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,771 | 36.8% |
| STALE_QUOTE | market_freshness | 1,358 | 18.1% |
| BOOK_QUALITY | execution | 1,311 | 17.4% |
| POOR_DATA | data | 625 | 8.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 410 | 5.5% |
| IDENTITY_AMBIGUOUS | mapping | 321 | 4.3% |
| LIMITED_DATA | data | 299 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 244 | 3.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 148 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 35 | 0.5% |

Cause class: coverage 36.8%, market_freshness 18.1%, execution 17.4%, data 12.3%, market_freshness/coverage 8.7%, mapping 4.3%, model_calibration_or_unknown 2.0%, model_calibration 0.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.0%, START_UNVERIFIABLE 98.3%, LOW_DATA_QUALITY 72.8%, THIN_PLAYER_HISTORY 60.3%, STALE_KALSHI_QUOTE 53.9%, STALE_PLAYER_DATA 47.6%, MODEL_INTERNAL_DISAGREEMENT 40.3%, ASYMMETRIC_SAMPLE_SIZE 33.7%, WIDE_SPREAD 23.6%, MODEL_HIGH_UNCERTAINTY 17.8%, PLAYER_IDENTITY_RISK 17.3%, EVENT_MAPPING_RISK 9.8%, LOW_DISPLAYED_LIQUIDITY 8.1%, LEVEL_TRANSFER_RISK 7.3%, MODEL_CALIBRATION_OUTLIER 4.5%, EXTERNAL_MARKET_REJECTION 0.9%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 39.6%, POST_SETTLEMENT_OBSERVATION 36.8%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 6023, "IDENTITY_AMBIGUOUS": 1499}; ticker orientation: {"VERIFIED": 7522}.

Checks: discipline:AMBIGUOUS 514, discipline:PASS 7008, identity_confidence:AMBIGUOUS 1304, identity_confidence:PASS 6218, level_mapping:NA 526, level_mapping:PASS 6996, market_pair:AMBIGUOUS 278, market_pair:NA 176, market_pair:PASS 7068, model_complement:NA 143, model_complement:PASS 7379, namesake:PASS 7522, physical_match_id:NA 2853, physical_match_id:PASS 4669, player_ids:PASS 7522, same_pair_other_event:PASS 7522, ticker_orientation:PASS 7522

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,070 | 1.4% | 1.4% | 0.4% | {"market_freshness": 20, "execution": 8, "market_freshness/coverage": 1} | 5.24 | 0.2093 / 0.2118 (255) | 16.4% | 0.5% | 5.4% | 1.6% |
| CHALLENGER | 5,392 | 16.9% | 5.9% | 12.1% | {"coverage": 554, "market_freshness/coverage": 113, "market_freshness": 111, "data": 60, "model_calibration_or_unknown": 47, "execution": 13, "model_calibration": 9, "mapping": 6} | 7.2 | 0.2168 / 0.2038 (1413) | 37.5% | 9.2% | 2.4% | 22.6% |
| DOUBLES | 1,037 | 49.6% | 48.9% | 6.8% | {"execution": 210, "mapping": 151, "market_freshness": 106, "market_freshness/coverage": 40, "coverage": 7} | 24.11 | 0.3322 / 0.234 (315) | 22.6% | 0.0% | 100.0% | 7.8% |
| ITF_MEN | 10,173 | 24.4% | 16.8% | 33.0% | {"coverage": 959, "execution": 511, "market_freshness": 386, "data": 336, "market_freshness/coverage": 202, "mapping": 85, "model_calibration_or_unknown": 2} | 11.09 | 0.2128 / 0.1948 (2500) | 36.6% | 60.4% | 11.8% | 22.8% |
| ITF_WOMEN | 12,625 | 26.2% | 18.7% | 44.0% | {"coverage": 1234, "market_freshness": 660, "execution": 548, "data": 494, "market_freshness/coverage": 252, "mapping": 73, "model_calibration_or_unknown": 37, "model_calibration": 10} | 12.49 | 0.2021 / 0.192 (2672) | 39.4% | 57.6% | 10.0% | 22.8% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,608 | 6.2% | 5.5% | 1.3% | {"market_freshness": 36, "model_calibration_or_unknown": 22, "data": 11, "market_freshness/coverage": 10, "model_calibration": 8, "execution": 7, "coverage": 4, "mapping": 1} | 7.82 | 0.2398 / 0.2312 (289) | 26.4% | 1.3% | 1.7% | 3.4% |
| WTA125 | 1,292 | 12.8% | 10.2% | 2.2% | {"model_calibration_or_unknown": 38, "market_freshness": 37, "market_freshness/coverage": 35, "data": 23, "coverage": 12, "execution": 9, "model_calibration": 8, "mapping": 4} | 9.51 | 0.2148 / 0.2048 (447) | 23.5% | 7.9% | 4.3% | 10.0% |

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
| 8 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 17.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1037 min (STALE); no external reference |
| 9 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 10 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 11 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 12 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 13 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 14 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 15 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 16 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 17 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 18 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 19 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 20 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 22 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 23 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 24 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 25 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 26 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 9.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 553 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 27 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 28 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 29 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 30 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 31 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 32 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 33 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 34 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 35 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 36 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 33 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 37 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 39 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 40 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 41 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 42 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 43 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 44 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 45 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 46 | `KXATPCHALLENGERMATCH-26OCT13GIUSEA-SEA` | CHALLENGER | fair_v1 | 76% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 757 min (STALE); no external reference |
| 47 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 64 min (STALE); no external reference |
| 48 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 49 | `KXITFWMATCH-26OCT13MAMSTR-MAM` | ITF_WOMEN | fair_v1 | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 406 min (STALE); data LIMITED (grade C, thinner serve sample 879.0, ratio 2.64); no external reference |
| 50 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.983, "by_level_share_of_ge_25pp": {"ATP": 0.0039, "CHALLENGER": 0.1214, "DOUBLES": 0.0683, "ITF_MEN": 0.3298, "ITF_WOMEN": 0.4398, "OTHER": 0.0016, "WTA": 0.0132, "WTA125": 0.0221}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5391, "share_primary_cause_market_settled_or_in_play": 0.4553, "share_primary_cause_stale_quote_only": 0.1805}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 7522, "identity_ambiguous_share": 0.1993, "ticker_orientation": {"VERIFIED": 7522}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 4669, "with_external": 177, "coverage": 0.0379, "external_status": {"EXTERNAL_STALE": 126, "AGREES_WITH_KALSHI": 48, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 126, "MODEL_LONE_OUTLIER": 48, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.2712, "share_external_supports_model": 0.0169}, "pregame_clean_ge_25pp": {"n": 2206, "with_external": 167, "coverage": 0.0757, "external_status": {"EXTERNAL_STALE": 118, "AGREES_WITH_KALSHI": 46, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 118, "MODEL_LONE_OUTLIER": 46, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.2754, "share_external_supports_model": 0.018}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 553.0, "median_sample_ratio": 2.38, "median_min_matches": 20.0, "median_max_days_since_last": 204.0, "share_severe_asymmetry": 0.2022, "data_status": {"POOR": 4017, "LIMITED": 2143, "ADEQUATE": 1362}, "comparison_lt_10pp": {"median_thinner_serve_points": 1762.0, "median_sample_ratio": 1.7, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 607, "model_minus_observed": 0.0498, "kalshi_minus_observed": -0.0816, "brier_diff_model_minus_kalshi": -0.0}, "4-10x": {"n": 407, "model_minus_observed": 0.0744, "kalshi_minus_observed": -0.0645, "brier_diff_model_minus_kalshi": 0.0071}, "<2x": {"n": 1470, "model_minus_observed": 0.0822, "kalshi_minus_observed": -0.0402, "brier_diff_model_minus_kalshi": 0.0111}, ">=10x": {"n": 487, "model_minus_observed": 0.1198, "kalshi_minus_observed": -0.0468, "brier_diff_model_minus_kalshi": 0.0147}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2971, "model": {"intercept": -0.543, "slope": 0.869, "slope_se": 0.047}, "kalshi_mid_same_rows": {"intercept": 0.235, "slope": 1.125, "slope_se": 0.053}, "mean_extremity_model": 0.177, "mean_extremity_kalshi": 0.1714, "model_brier": 0.2288, "kalshi_brier": 0.2019, "brier_diff_model_minus_kalshi": 0.0269, "brier_diff_se": 0.0035, "model_logloss": 0.653, "kalshi_logloss": 0.5857}, "fair_v1": {"n": 2971, "model": {"intercept": -0.394, "slope": 1.062, "slope_se": 0.052}, "kalshi_mid_same_rows": {"intercept": 0.322, "slope": 1.173, "slope_se": 0.054}, "mean_extremity_model": 0.1689, "mean_extremity_kalshi": 0.1714, "model_brier": 0.2109, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0089, "brier_diff_se": 0.0028, "model_logloss": 0.609, "kalshi_logloss": 0.5858}, "gen1_elo": {"n": 2971, "model": {"intercept": -0.375, "slope": 1.042, "slope_se": 0.05}, "kalshi_mid_same_rows": {"intercept": 0.324, "slope": 1.162, "slope_se": 0.053}, "mean_extremity_model": 0.1739, "mean_extremity_kalshi": 0.1719, "model_brier": 0.2099, "kalshi_brier": 0.2019, "brier_diff_model_minus_kalshi": 0.008, "brier_diff_se": 0.0028, "model_logloss": 0.6076, "kalshi_logloss": 0.5854}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2438, "share_ge_15": 0.4369, "median_abs_gap": 12.96, "n": 19149}, "gen1_elo": {"share_ge_25": 0.238, "share_ge_15": 0.4301, "median_abs_gap": 12.47, "n": 19149}, "gen1_sr": {"share_ge_25": 0.3057, "share_ge_15": 0.5236, "median_abs_gap": 15.9, "n": 19149}, "gen2": {"share_ge_25": 0.3068, "share_ge_15": 0.5092, "median_abs_gap": 15.45, "n": 19149}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1495, "share_ge_15": 0.3484, "median_abs_gap": 10.63, "n": 14753}, "gen1_elo": {"share_ge_25": 0.1471, "share_ge_15": 0.3377, "median_abs_gap": 10.09, "n": 14752}, "gen1_sr": {"share_ge_25": 0.2118, "share_ge_15": 0.4452, "median_abs_gap": 13.29, "n": 14753}, "gen2": {"share_ge_25": 0.2254, "share_ge_15": 0.4414, "median_abs_gap": 13.02, "n": 14754}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.24, "share_ge_25_all": 0.014, "share_ge_25_pregame_clean": 0.0138}, "WTA": {"median_abs_gap_pregame_clean": 7.82, "share_ge_25_all": 0.0616, "share_ge_25_pregame_clean": 0.0547}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2385, "share_within_10pp_all": 0.439, "share_within_10pp_pregame_clean": 0.497, "corr_model_vs_mid_pregame_clean": 0.8447}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 456, "model_brier": 0.1927, "kalshi_brier": 0.1942, "brier_diff_model_minus_kalshi": -0.0015}, "10-15": {"n_settled": 526, "model_brier": 0.2122, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0082}, "15-25": {"n_settled": 650, "model_brier": 0.2309, "kalshi_brier": 0.2171, "brier_diff_model_minus_kalshi": 0.0138}, "25-40": {"n_settled": 350, "model_brier": 0.2248, "kalshi_brier": 0.2088, "brier_diff_model_minus_kalshi": 0.016}, "3-5": {"n_settled": 290, "model_brier": 0.1908, "kalshi_brier": 0.191, "brier_diff_model_minus_kalshi": -0.0003}, "40+": {"n_settled": 72, "model_brier": 0.29, "kalshi_brier": 0.1741, "brier_diff_model_minus_kalshi": 0.116}, "5-10": {"n_settled": 627, "model_brier": 0.1948, "kalshi_brier": 0.195, "brier_diff_model_minus_kalshi": -0.0003}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.543, "slope": 0.869, "slope_se": 0.047}, "kalshi_slope": {"intercept": 0.235, "slope": 1.125, "slope_se": 0.053}, "n": 2971}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.509, "slope": 0.872, "slope_se": 0.035}, "kalshi_slope": {"intercept": 0.15, "slope": 1.077, "slope_se": 0.039}, "n": 4962}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 315, "model_brier": 0.3322, "kalshi_brier": 0.234, "brier_diff_model_minus_kalshi": 0.0982, "brier_diff_se": 0.0179, "corr_model_outcome": -0.0051, "corr_kalshi_outcome": 0.2496}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
