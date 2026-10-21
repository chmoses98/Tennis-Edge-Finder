# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-21T01:41Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 45,344): 0-3 14.1%, 3-5 9.5%, 5-10 19.7%, 10-15 15.4%, 15-25 19.3%, 25-40 14.0%, 40+ 8.0%; median gap 12.04 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 75.8%, Challenger 12.5%, doubles 6.8%). Main tour: ATP 5.0% and WTA 4.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 9,957): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.4%, BOOK_QUALITY 18.9%, STALE_QUOTE 18.0%, POOR_DATA 8.9%, POSSIBLY_IN_PLAY_QUOTE 5.3%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 3.8%, IN_PLAY_QUOTE 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%. By class: coverage 34.4%, execution 18.9%, market_freshness 18.0%, data 12.7%, market_freshness/coverage 8.7%, mapping 4.3%, model_calibration_or_unknown 2.2%, model_calibration 0.8%.
* **Stale / settled / in-play**: 51.5% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.1% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 9,957 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.4% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.8%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.3% of the time and with the model 0.8%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 502.0 points vs 1753.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.045, Gen-2 0.844, Gen-1 ledger 0.874 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 476 model 0.2261 vs Kalshi 0.2106; n 95 model 0.3 vs Kalshi 0.1766.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 194,558 model-market comparisons (315,994 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 66,438 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-21T01:28:48.239206+00:00'], shadow board 51,284 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-21T01:28:51.763971+00:00'], Model 4 24,456 rows, 17,809 settled tickers, 6,142 tickers with an external scan.
* By model: {"gen1_ledger": 44933, "gen1_elo": 25785, "fair_v1": 25785, "gen2": 25785, "gen1_sr": 25785, "model4_fundamental": 23256, "model4_conditioned": 23229}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 45,344 | 14.1 | 9.5 | 19.7 | 15.4 | 19.3 | 14.0 | 8.0 | 12.04 | 41.3% | 22.0% |
| MW fair_v1 | 25,785 | 13.2 | 8.5 | 18.2 | 15.7 | 20.0 | 14.9 | 9.5 | 13.12 | 44.3% | 24.4% |
| MW gen1_elo | 25,785 | 12.9 | 8.7 | 19.2 | 15.2 | 19.9 | 14.9 | 9.2 | 12.84 | 44.0% | 24.1% |
| MW gen1_ledger | 19,559 | 15.4 | 10.7 | 21.7 | 14.9 | 18.5 | 12.8 | 6.0 | 10.53 | 37.3% | 18.8% |
| MW gen1_sr | 25,785 | 9.9 | 7.2 | 16.6 | 14.0 | 21.4 | 18.7 | 12.1 | 15.88 | 52.2% | 30.8% |
| MW gen2 | 25,785 | 11.1 | 7.3 | 16.2 | 14.2 | 20.1 | 17.8 | 13.3 | 15.52 | 51.1% | 31.1% |
| all families model4_conditioned | 23,229 | 21.8 | 19.2 | 34.3 | 17.8 | 4.5 | 1.4 | 1.1 | 5.95 | 7.0% | 2.4% |
| all families model4_fundamental | 23,256 | 16.3 | 13.0 | 34.0 | 20.4 | 11.4 | 3.5 | 1.4 | 7.91 | 16.2% | 4.8% |

Configurable thresholds (primary): >=5pp 76.4%, >=10pp 56.7%, >=15pp 41.3%, >=20pp 30.6%, >=25pp 22.0%, >=30pp 15.8%, >=40pp 8.0%, >=50pp 3.6%
Executable gap (model outside the book, before fees): median 8.41pp; >=10pp 45.1%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,264 | 28.5 | 13.9 | 24.4 | 15.1 | 12.4 | 5.2 | 0.6 | 6.22 | 18.1% | 5.7% |
| CHALLENGER | 4,278 | 15.5 | 10.1 | 20.1 | 15.8 | 15.0 | 12.6 | 10.9 | 11.32 | 38.4% | 23.4% |
| ITF_MEN | 6,856 | 10.8 | 7.7 | 17.0 | 14.5 | 21.0 | 17.1 | 11.9 | 14.98 | 49.9% | 28.9% |
| ITF_WOMEN | 10,158 | 9.7 | 6.8 | 15.5 | 15.6 | 23.1 | 18.3 | 11.1 | 15.8 | 52.4% | 29.3% |
| WTA | 1,569 | 17.3 | 12.2 | 24.7 | 20.3 | 20.3 | 4.4 | 0.7 | 8.85 | 25.4% | 5.1% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,264 | 23.3 | 15.0 | 24.4 | 17.2 | 14.1 | 5.2 | 0.8 | 6.85 | 20.1% | 6.0% |
| CHALLENGER | 4,278 | 14.5 | 8.5 | 18.7 | 14.6 | 17.8 | 14.0 | 11.9 | 12.7 | 43.8% | 25.9% |
| ITF_MEN | 6,856 | 8.9 | 6.4 | 14.8 | 13.3 | 19.8 | 20.3 | 16.4 | 17.85 | 56.5% | 36.8% |
| ITF_WOMEN | 10,158 | 8.2 | 5.6 | 13.5 | 13.5 | 21.5 | 20.9 | 16.7 | 18.91 | 59.2% | 37.7% |
| WTA | 1,569 | 14.6 | 9.4 | 20.1 | 16.7 | 24.3 | 14.1 | 0.8 | 11.64 | 39.1% | 14.8% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,264 | 24.0 | 13.0 | 24.2 | 16.0 | 15.1 | 6.6 | 1.1 | 7.26 | 22.8% | 7.7% |
| CHALLENGER | 4,278 | 14.2 | 9.6 | 20.9 | 15.2 | 16.2 | 12.9 | 11.1 | 11.41 | 40.2% | 24.0% |
| ITF_MEN | 6,856 | 10.1 | 7.8 | 17.3 | 13.9 | 21.6 | 17.4 | 12.0 | 15.39 | 51.0% | 29.3% |
| ITF_WOMEN | 10,158 | 9.4 | 6.7 | 16.3 | 15.7 | 23.2 | 18.5 | 10.2 | 15.68 | 51.9% | 28.7% |
| WTA | 1,569 | 24.4 | 16.6 | 30.2 | 16.0 | 10.3 | 2.2 | 0.5 | 6.01 | 12.9% | 2.6% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,293 | 26.5 | 19.9 | 29.5 | 11.9 | 8.7 | 3.2 | 0.4 | 5.4 | 12.2% | 3.6% |
| CHALLENGER | 2,973 | 21.2 | 14.7 | 26.8 | 14.2 | 14.9 | 6.4 | 1.9 | 7.29 | 23.2% | 8.3% |
| DOUBLES | 1,408 | 4.8 | 4.1 | 11.7 | 10.4 | 20.7 | 25.8 | 22.4 | 24.09 | 69.0% | 48.2% |
| ITF_MEN | 5,431 | 14.1 | 8.8 | 20.6 | 15.9 | 20.4 | 13.3 | 6.8 | 11.97 | 40.6% | 20.2% |
| ITF_WOMEN | 6,562 | 12.2 | 8.9 | 19.2 | 15.2 | 21.8 | 16.6 | 6.1 | 13.04 | 44.5% | 22.6% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,011 | 22.1 | 15.7 | 29.8 | 18.2 | 10.3 | 3.7 | 0.3 | 7.04 | 14.2% | 4.0% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,207 | 28.9 | 14.1 | 24.7 | 14.9 | 12.1 | 4.8 | 0.5 | 6.14 | 17.4% | 5.3% |
| CHALLENGER | 3,016 | 20.3 | 12.4 | 24.8 | 18.3 | 15.4 | 6.7 | 2.1 | 8.44 | 24.2% | 8.8% |
| ITF_MEN | 5,061 | 13.1 | 9.3 | 20.2 | 16.4 | 21.7 | 13.9 | 5.3 | 12.09 | 40.9% | 19.2% |
| ITF_WOMEN | 7,626 | 11.4 | 8.1 | 17.7 | 17.8 | 24.8 | 15.3 | 4.9 | 13.51 | 45.0% | 20.2% |
| WTA | 1,528 | 17.5 | 12.0 | 24.7 | 20.5 | 20.3 | 4.4 | 0.7 | 8.85 | 25.4% | 5.1% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,207 | 23.6 | 15.3 | 24.6 | 17.0 | 14.0 | 4.9 | 0.7 | 6.63 | 19.6% | 5.6% |
| CHALLENGER | 3,016 | 18.2 | 10.8 | 23.4 | 17.4 | 18.0 | 9.8 | 2.4 | 9.44 | 30.2% | 12.2% |
| ITF_MEN | 5,062 | 10.5 | 7.6 | 17.0 | 15.1 | 21.8 | 18.4 | 9.6 | 14.95 | 49.8% | 28.0% |
| ITF_WOMEN | 7,626 | 9.2 | 6.4 | 14.9 | 15.0 | 23.6 | 20.3 | 10.6 | 16.62 | 54.5% | 30.9% |
| WTA | 1,528 | 14.6 | 9.4 | 20.1 | 16.6 | 24.3 | 14.3 | 0.8 | 11.67 | 39.3% | 15.0% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,253 | 26.7 | 20.1 | 29.5 | 12.1 | 8.2 | 3.0 | 0.2 | 5.34 | 11.5% | 3.3% |
| CHALLENGER | 2,586 | 22.7 | 15.7 | 28.4 | 14.1 | 14.3 | 4.2 | 0.6 | 6.72 | 19.1% | 4.8% |
| DOUBLES | 1,309 | 4.8 | 4.3 | 11.8 | 10.6 | 20.7 | 25.9 | 21.9 | 23.92 | 68.5% | 47.8% |
| ITF_MEN | 4,520 | 15.4 | 9.5 | 22.5 | 16.7 | 20.1 | 11.7 | 4.1 | 10.77 | 35.9% | 15.8% |
| ITF_WOMEN | 5,457 | 13.1 | 9.5 | 20.6 | 16.0 | 22.1 | 15.3 | 3.5 | 11.84 | 40.8% | 18.8% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 964 | 22.5 | 16.2 | 29.9 | 18.3 | 10.3 | 2.9 | 0.0 | 6.86 | 13.2% | 2.9% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,408 | 4.8 | 4.1 | 11.7 | 10.4 | 20.7 | 25.8 | 22.4 | 24.09 | 69.0% | 48.2% |
| singles | 18,151 | 16.3 | 11.2 | 22.4 | 15.3 | 18.3 | 11.8 | 4.7 | 10.02 | 34.8% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 5,813 | 13.3 | 8.8 | 19.0 | 15.7 | 18.9 | 14.8 | 9.5 | 12.8 | 43.1% | 24.3% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 16,286 | 13.5 | 8.5 | 18.3 | 15.4 | 20.2 | 14.7 | 9.4 | 13.1 | 44.2% | 24.1% |
| UNKNOWN | 3,449 | 11.3 | 7.9 | 16.7 | 17.3 | 20.8 | 15.9 | 10.1 | 13.75 | 46.7% | 25.9% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,395 | 19.7 | 11.4 | 21.1 | 16.8 | 16.0 | 9.0 | 6.0 | 9.34 | 30.9% | 15.0% |
| B | 3,285 | 12.4 | 9.1 | 19.9 | 17.2 | 18.9 | 12.1 | 10.3 | 12.18 | 41.3% | 22.4% |
| C | 3,616 | 12.1 | 8.9 | 18.9 | 14.8 | 19.8 | 15.4 | 10.1 | 13.24 | 45.2% | 25.5% |
| D | 4,219 | 12.2 | 7.7 | 16.9 | 15.6 | 22.2 | 16.0 | 9.4 | 14.08 | 47.6% | 25.4% |
| F | 7,270 | 7.9 | 5.7 | 15.0 | 14.4 | 23.4 | 21.2 | 12.4 | 17.71 | 57.0% | 33.6% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,612 | 23.2 | 15.8 | 28.5 | 15.1 | 11.8 | 4.1 | 1.5 | 6.68 | 17.4% | 5.5% |
| B | 2,729 | 15.9 | 10.5 | 24.0 | 16.1 | 18.8 | 10.8 | 3.9 | 9.92 | 33.5% | 14.7% |
| C | 3,862 | 10.9 | 7.2 | 18.4 | 14.4 | 21.8 | 16.3 | 10.9 | 14.43 | 49.0% | 27.2% |
| D | 2,803 | 13.9 | 9.7 | 19.7 | 14.7 | 21.1 | 14.7 | 6.2 | 12.11 | 41.9% | 20.9% |
| F | 4,553 | 10.3 | 8.0 | 15.7 | 14.6 | 22.2 | 20.7 | 8.5 | 15.76 | 51.4% | 29.2% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 8,426 | 17.9 | 10.3 | 20.4 | 16.8 | 16.5 | 9.8 | 8.3 | 10.42 | 34.6% | 18.1% |
| LIMITED | 5,635 | 13.8 | 10.2 | 20.1 | 15.6 | 19.2 | 13.6 | 7.5 | 11.77 | 40.3% | 21.1% |
| POOR | 11,724 | 9.5 | 6.5 | 15.8 | 14.9 | 22.9 | 19.1 | 11.2 | 16.1 | 53.3% | 30.4% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,966 | 26.7 | 20.9 | 34.3 | 12.0 | 4.5 | 1.5 | 0.2 | 5.2 | 6.2% | 1.7% |
| GAME_SPREAD | 4,306 | 22.9 | 15.4 | 33.3 | 17.1 | 8.7 | 2.4 | 0.3 | 6.54 | 11.4% | 2.6% |
| MATCH_WINNER | 19,559 | 15.4 | 10.7 | 21.7 | 14.9 | 18.5 | 12.8 | 6.0 | 10.53 | 37.3% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 9,106 | 29.9 | 16.8 | 30.3 | 12.7 | 8.2 | 1.7 | 0.4 | 5.42 | 10.2% | 2.1% |
| TOTAL_GAMES | 6,972 | 8.0 | 9.3 | 36.5 | 29.2 | 10.9 | 3.4 | 2.8 | 9.59 | 17.1% | 6.2% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,118 | 25.3 | 34.7 | 32.1 | 4.0 | 3.1 | 0.6 | 0.1 | 4.45 | 3.9% | 0.7% |
| GAME_SPREAD | 5,552 | 45.8 | 17.0 | 27.0 | 7.6 | 1.8 | 0.6 | 0.2 | 3.41 | 2.6% | 0.8% |
| TOTAL_GAMES | 9,559 | 4.8 | 7.3 | 40.5 | 35.3 | 7.3 | 2.5 | 2.3 | 9.74 | 12.1% | 4.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,121 | 24.2 | 17.9 | 35.3 | 12.3 | 7.3 | 2.6 | 0.3 | 5.81 | 10.2% | 2.9% |
| GAME_SPREAD | 5,555 | 19.1 | 13.2 | 28.1 | 19.9 | 14.4 | 4.3 | 0.9 | 7.99 | 19.6% | 5.2% |
| TOTAL_GAMES | 9,580 | 7.9 | 8.8 | 36.4 | 27.6 | 13.0 | 3.7 | 2.5 | 9.66 | 19.3% | 6.2% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 25,785 | 44.3% | 24.4% | 13.12 | 36.0% | 15.3% | 10.95 |
| gen1_elo | 25,785 | 44.0% | 24.1% | 12.84 | 35.4% | 15.4% | 10.53 |
| gen1_sr | 25,785 | 52.2% | 30.8% | 15.88 | 44.6% | 21.7% | 13.17 |
| gen2 | 25,785 | 51.1% | 31.1% | 15.52 | 44.6% | 23.3% | 13.14 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 13,479 | 15.9 | 10.3 | 21.0 | 17.4 | 20.4 | 11.8 | 3.3 | 10.8 | 35.4% | 15.0% |
| STALE | 12,306 | 10.2 | 6.6 | 15.2 | 13.9 | 19.5 | 18.3 | 16.3 | 17.02 | 54.1% | 34.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 13,027 | 16.6 | 11.3 | 22.6 | 15.0 | 17.5 | 12.2 | 4.8 | 9.86 | 34.5% | 17.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 45,344 | 13027 | 16951 | 15366 | 23.9 | 131.1 | 1400.4 |
| ge_15pp | 18,727 | 4495 | 6066 | 8166 | 25.7 | 430.3 | 1380.4 |
| ge_25pp | 9,957 | 2215 | 2616 | 5126 | 31.4 | 573.1 | 1380.4 |
| lt_10pp | 19,647 | 6578 | 7996 | 5073 | 21.7 | 47.4 | 1341.5 |

Current slate `SL-20261021T014119Z-14cce745`: 800 priced rows, quote age at build {'median': 12.8, 'max': 12.9}, freshness {'AGING': 800}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 16 | 0.0 | 0.0 | 25.0 | 0.0 | 43.8 | 31.2 | 0.0 | 20.49 | 75.0% | 31.2% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,390 | 19.8 | 11.1 | 23.3 | 18.7 | 19.3 | 7.2 | 0.7 | 9.1 | 27.1% | 7.8% |
| KALSHI_LONE_OUTLIER | 15 | 6.7 | 6.7 | 73.3 | 0.0 | 6.7 | 6.7 | 0.0 | 5.49 | 13.3% | 6.7% |
| MARKETS_AGREE | 435 | 68.3 | 31.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.11 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 971 | 0.0 | 2.5 | 33.6 | 26.7 | 26.1 | 10.4 | 0.8 | 12.72 | 37.3% | 11.2% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 25,785 | 3839 (14.9%) | 25.3% | 0.8% | {"EXTERNAL_STALE": 2390, "AGREES_WITH_KALSHI": 971, "ALL_AGREE": 435, "SUPPORTS_MODEL_DIRECTION": 15, "AGREES_WITH_MODEL": 15, "EXTERNAL_OUTLIER": 12, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 11,433 | 1024 (9.0%) | 35.4% | 1.4% | {"EXTERNAL_STALE": 648, "AGREES_WITH_KALSHI": 362, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 6,280 | 302 (4.8%) | 36.1% | 2.0% | {"EXTERNAL_STALE": 187, "AGREES_WITH_KALSHI": 109, "SUPPORTS_MODEL_DIRECTION": 5, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,067 | 285 (9.3%) | 36.8% | 2.1% | {"EXTERNAL_STALE": 174, "AGREES_WITH_KALSHI": 105, "SUPPORTS_MODEL_DIRECTION": 5, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 10,300 | 2108 (20.5%) | 16.6% | 0.8% | {"EXTERNAL_STALE": 1294, "ALL_AGREE": 435, "AGREES_WITH_KALSHI": 350, "AGREES_WITH_MODEL": 13, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 4,971 | 10.6 | 7.7 | 19.2 | 14.7 | 22.2 | 15.7 | 9.9 | 14.0 | 47.8% | 25.6% |
| 4-10x | 3,359 | 11.5 | 8.4 | 18.7 | 15.5 | 21.2 | 14.8 | 9.9 | 13.64 | 45.9% | 24.7% |
| <2x | 13,234 | 15.2 | 9.6 | 18.7 | 16.7 | 18.2 | 13.2 | 8.4 | 11.91 | 39.8% | 21.6% |
| >=10x | 4,221 | 11.2 | 6.5 | 15.1 | 13.9 | 21.9 | 19.4 | 11.9 | 16.23 | 53.3% | 31.3% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 6,542 | 12.5 | 8.5 | 19.4 | 16.3 | 19.7 | 13.6 | 10.0 | 12.88 | 43.3% | 23.6% |
| 300-1000 | 5,614 | 11.8 | 8.6 | 16.8 | 15.5 | 21.1 | 16.3 | 9.8 | 14.02 | 47.2% | 26.2% |
| <300 | 8,173 | 9.0 | 5.8 | 15.4 | 14.6 | 23.0 | 20.2 | 11.9 | 16.85 | 55.2% | 32.1% |
| >=3000 | 5,456 | 21.5 | 12.6 | 22.6 | 16.8 | 14.7 | 6.9 | 4.8 | 8.1 | 26.4% | 11.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 761 | 0.5447 | 0.4089 | 0.4941 | +0.051 | -0.085 | -0.0006 ± 0.0055 |
| ratio 4-10x | 519 | 0.5899 | 0.4447 | 0.501 | +0.089 | -0.056 | 0.0126 ± 0.0071 |
| ratio <2x | 1856 | 0.537 | 0.4146 | 0.451 | +0.086 | -0.036 | 0.0122 ± 0.0033 |
| ratio >=10x | 644 | 0.5641 | 0.3902 | 0.4581 | +0.106 | -0.068 | 0.0076 ± 0.0072 |
| thinner_sample 1000-3000 | 1037 | 0.5423 | 0.4158 | 0.4542 | +0.088 | -0.038 | 0.0101 ± 0.0044 |
| thinner_sample 300-1000 | 885 | 0.5659 | 0.4241 | 0.4983 | +0.068 | -0.074 | -0.0001 ± 0.0054 |
| thinner_sample <300 | 1223 | 0.5547 | 0.39 | 0.4546 | +0.100 | -0.065 | 0.0125 ± 0.005 |
| thinner_sample >=3000 | 635 | 0.534 | 0.4397 | 0.4724 | +0.062 | -0.033 | 0.0126 ± 0.0046 |
| data_status ADEQUATE | 1084 | 0.5371 | 0.4325 | 0.4613 | +0.076 | -0.029 | 0.0112 ± 0.0038 |
| data_status LIMITED | 919 | 0.5514 | 0.4193 | 0.481 | +0.070 | -0.062 | 0.0045 ± 0.0049 |
| data_status POOR | 1777 | 0.5581 | 0.3987 | 0.4648 | +0.093 | -0.066 | 0.0097 ± 0.0041 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 563 | 0.1969 | 0.1982 | -0.0014 ± 0.0007 | 0.5723 | 0.5753 | 0.4991 | 0.4842 | 0.5364 | -0.049 ± 0.0196 | -0.01 (5) |
| 3-5 | 358 | 0.1999 | 0.1996 | +0.0003 ± 0.0019 | 0.5826 | 0.5804 | 0.5029 | 0.4628 | 0.4777 | -0.089 ± 0.0243 | 0.02 (1) |
| 5-10 | 784 | 0.2011 | 0.2013 | -0.0002 ± 0.0024 | 0.5881 | 0.5865 | 0.5134 | 0.4389 | 0.4732 | -0.084 ± 0.0166 | -0.0167 (6) |
| 10-15 | 656 | 0.2132 | 0.2038 | +0.0094 ± 0.0044 | 0.616 | 0.5889 | 0.524 | 0.3998 | 0.4238 | -0.099 ± 0.0176 | -0.048 (5) |
| 15-25 | 848 | 0.2255 | 0.2147 | +0.0107 ± 0.0062 | 0.6461 | 0.614 | 0.5782 | 0.3824 | 0.4528 | -0.085 ± 0.0157 | -0.0033 (9) |
| 25-40 | 476 | 0.2261 | 0.2106 | +0.0156 ± 0.0125 | 0.6409 | 0.605 | 0.6552 | 0.3469 | 0.4727 | -0.074 ± 0.0193 | -0.01 (1) |
| 40+ | 95 | 0.3 | 0.1766 | +0.1234 ± 0.0386 | 0.818 | 0.5257 | 0.7498 | 0.3018 | 0.3895 | -0.119 ± 0.0373 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2779 | 0.1826 | 0.1837 | -0.0011 ± 0.0003 | 0.5402 | 0.5415 | 0.4799 | 0.4648 | 0.5027 | -0.018 ± 0.0082 | -0.0129 (17) |
| 3-5 | 1829 | 0.1953 | 0.1941 | +0.0012 ± 0.0008 | 0.5714 | 0.5651 | 0.483 | 0.443 | 0.4472 | -0.053 ± 0.0105 | 0.0 (2) |
| 5-10 | 3875 | 0.1961 | 0.1929 | +0.0032 ± 0.0011 | 0.5747 | 0.5645 | 0.4856 | 0.4117 | 0.4258 | -0.049 ± 0.0072 | -0.0119 (21) |
| 10-15 | 3381 | 0.2032 | 0.1849 | +0.0182 ± 0.0019 | 0.5941 | 0.5432 | 0.4853 | 0.3609 | 0.3499 | -0.075 ± 0.0074 | -0.0281 (16) |
| 15-25 | 4249 | 0.2094 | 0.1718 | +0.0376 ± 0.0025 | 0.6125 | 0.5077 | 0.5017 | 0.3054 | 0.3081 | -0.070 ± 0.0063 | -0.0025 (44) |
| 25-40 | 3263 | 0.2238 | 0.13 | +0.0938 ± 0.0039 | 0.6421 | 0.3976 | 0.5312 | 0.2186 | 0.2283 | -0.062 ± 0.0061 | -0.01 (1) |
| 40+ | 2115 | 0.3796 | 0.0445 | +0.3351 ± 0.0052 | 0.9887 | 0.173 | 0.6316 | 0.107 | 0.0619 | -0.082 ± 0.0043 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 419 | 0.2005 | 0.2011 | -0.0006 ± 0.0008 | 0.5827 | 0.5839 | 0.501 | 0.4861 | 0.5107 | -0.088 ± 0.0235 | -0.01 (3) |
| 3-5 | 314 | 0.2202 | 0.219 | +0.0012 ± 0.0021 | 0.6259 | 0.6236 | 0.5129 | 0.4728 | 0.4713 | -0.107 ± 0.0285 | 0.02 (1) |
| 5-10 | 666 | 0.1995 | 0.2005 | -0.0010 ± 0.0026 | 0.5824 | 0.5843 | 0.5473 | 0.4724 | 0.5165 | -0.070 ± 0.0179 | -0.01 (4) |
| 10-15 | 628 | 0.2177 | 0.2121 | +0.0056 ± 0.0046 | 0.6255 | 0.6108 | 0.5643 | 0.4399 | 0.4825 | -0.094 ± 0.019 | -0.04 (5) |
| 15-25 | 905 | 0.2312 | 0.2111 | +0.0201 ± 0.006 | 0.656 | 0.605 | 0.5917 | 0.3953 | 0.4464 | -0.098 ± 0.0155 | -0.0133 (9) |
| 25-40 | 624 | 0.2628 | 0.1998 | +0.0630 ± 0.0113 | 0.7335 | 0.5806 | 0.6579 | 0.3422 | 0.4022 | -0.111 ± 0.0175 | -0.0075 (4) |
| 40+ | 224 | 0.3659 | 0.1664 | +0.1995 ± 0.027 | 1.0106 | 0.4988 | 0.7375 | 0.2547 | 0.3036 | -0.088 ± 0.0261 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2318 | 0.1891 | 0.1895 | -0.0004 ± 0.0003 | 0.5556 | 0.5563 | 0.5017 | 0.4868 | 0.5078 | -0.037 ± 0.0094 | -0.0133 (15) |
| 3-5 | 1585 | 0.1979 | 0.1981 | -0.0001 ± 0.0009 | 0.5739 | 0.574 | 0.5111 | 0.4711 | 0.4915 | -0.033 ± 0.0114 | 0.02 (1) |
| 5-10 | 3437 | 0.1925 | 0.1917 | +0.0008 ± 0.0011 | 0.5678 | 0.5621 | 0.5052 | 0.4312 | 0.4644 | -0.028 ± 0.0076 | -0.0117 (6) |
| 10-15 | 3057 | 0.2 | 0.1896 | +0.0104 ± 0.002 | 0.5876 | 0.5521 | 0.5135 | 0.3894 | 0.4112 | -0.048 ± 0.008 | -0.0189 (18) |
| 15-25 | 4334 | 0.2173 | 0.1801 | +0.0372 ± 0.0025 | 0.6317 | 0.5281 | 0.5293 | 0.333 | 0.3394 | -0.068 ± 0.0065 | -0.0086 (42) |
| 25-40 | 3831 | 0.2508 | 0.1389 | +0.1118 ± 0.0038 | 0.7064 | 0.4254 | 0.5618 | 0.2454 | 0.2297 | -0.084 ± 0.006 | -0.0044 (18) |
| 40+ | 2929 | 0.3993 | 0.0622 | +0.3371 ± 0.0053 | 1.0517 | 0.2206 | 0.6585 | 0.1223 | 0.0888 | -0.072 ± 0.0045 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 537 | 0.1977 | 0.2001 | -0.0024 ± 0.0007 | 0.5755 | 0.5812 | 0.4952 | 0.4798 | 0.5531 | -0.013 ± 0.0197 | -0.0137 (8) |
| 3-5 | 391 | 0.194 | 0.1919 | +0.0021 ± 0.0018 | 0.5654 | 0.5605 | 0.5042 | 0.4647 | 0.4604 | -0.117 ± 0.0231 | 0.0067 (3) |
| 5-10 | 810 | 0.2016 | 0.1986 | +0.0030 ± 0.0024 | 0.5903 | 0.5797 | 0.5108 | 0.4368 | 0.4506 | -0.097 ± 0.0161 | -0.0071 (7) |
| 10-15 | 656 | 0.2093 | 0.2052 | +0.0041 ± 0.0044 | 0.6063 | 0.5925 | 0.539 | 0.4157 | 0.4634 | -0.085 ± 0.0176 | -0.0317 (6) |
| 15-25 | 797 | 0.2336 | 0.2125 | +0.0211 ± 0.0064 | 0.6664 | 0.6085 | 0.5854 | 0.3915 | 0.4341 | -0.113 ± 0.0162 | -0.03 (1) |
| 25-40 | 491 | 0.2146 | 0.2184 | -0.0038 ± 0.0124 | 0.6165 | 0.6234 | 0.6648 | 0.354 | 0.5132 | -0.049 ± 0.019 | 0.015 (2) |
| 40+ | 98 | 0.3093 | 0.1956 | +0.1137 ± 0.0399 | 0.8461 | 0.5688 | 0.7622 | 0.3107 | 0.4184 | -0.098 ± 0.0411 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2698 | 0.1857 | 0.1864 | -0.0007 ± 0.0003 | 0.547 | 0.5483 | 0.4865 | 0.4711 | 0.4885 | -0.035 ± 0.0084 | -0.0163 (35) |
| 3-5 | 1850 | 0.1864 | 0.1835 | +0.0028 ± 0.0008 | 0.5501 | 0.5431 | 0.4834 | 0.4438 | 0.4292 | -0.075 ± 0.0102 | -0.0094 (18) |
| 5-10 | 4059 | 0.1966 | 0.191 | +0.0057 ± 0.001 | 0.5776 | 0.5586 | 0.4871 | 0.4133 | 0.4102 | -0.062 ± 0.0069 | -0.01 (31) |
| 10-15 | 3225 | 0.197 | 0.1799 | +0.0170 ± 0.0019 | 0.5788 | 0.5301 | 0.5011 | 0.3775 | 0.3705 | -0.073 ± 0.0074 | -0.015 (12) |
| 15-25 | 4362 | 0.2139 | 0.1739 | +0.0399 ± 0.0025 | 0.6227 | 0.5128 | 0.5091 | 0.3146 | 0.309 | -0.077 ± 0.0063 | -0.03 (2) |
| 25-40 | 3249 | 0.2203 | 0.1316 | +0.0887 ± 0.004 | 0.6345 | 0.4007 | 0.534 | 0.218 | 0.2379 | -0.055 ± 0.0061 | 0.01 (3) |
| 40+ | 2048 | 0.3947 | 0.0495 | +0.3452 ± 0.0056 | 1.0317 | 0.186 | 0.6444 | 0.1139 | 0.0669 | -0.084 ± 0.0047 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 901 | 0.1956 | 0.1958 | -0.0002 ± 0.0005 | 0.571 | 0.5712 | 0.5061 | 0.491 | 0.4939 | -0.059 ± 0.015 | -0.0224 (49) |
| 3-5 | 626 | 0.1926 | 0.1921 | +0.0005 ± 0.0014 | 0.5626 | 0.5604 | 0.4836 | 0.4438 | 0.4553 | -0.052 ± 0.0177 | -0.0194 (34) |
| 5-10 | 1326 | 0.2001 | 0.1937 | +0.0064 ± 0.0018 | 0.588 | 0.569 | 0.491 | 0.4177 | 0.4125 | -0.071 ± 0.0123 | -0.005 (78) |
| 10-15 | 863 | 0.209 | 0.1982 | +0.0109 ± 0.0038 | 0.6064 | 0.578 | 0.5161 | 0.393 | 0.409 | -0.065 ± 0.0154 | 0.0014 (64) |
| 15-25 | 1152 | 0.2313 | 0.2113 | +0.0199 ± 0.0053 | 0.6601 | 0.6087 | 0.5724 | 0.3776 | 0.4253 | -0.065 ± 0.0136 | -0.0214 (59) |
| 25-40 | 702 | 0.2495 | 0.2045 | +0.0450 ± 0.0105 | 0.7076 | 0.5891 | 0.6639 | 0.3512 | 0.4345 | -0.086 ± 0.0159 | -0.0219 (26) |
| 40+ | 241 | 0.3517 | 0.1964 | +0.1553 ± 0.0284 | 1.0155 | 0.5747 | 0.8055 | 0.3208 | 0.4232 | -0.085 ± 0.0255 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2950 | 0.1833 | 0.1835 | -0.0002 ± 0.0003 | 0.5398 | 0.5394 | 0.5064 | 0.4911 | 0.4997 | -0.038 ± 0.0079 | -0.0157 (88) |
| 3-5 | 2025 | 0.1909 | 0.1889 | +0.0020 ± 0.0008 | 0.5583 | 0.5541 | 0.4898 | 0.4501 | 0.4444 | -0.054 ± 0.0097 | -0.0209 (69) |
| 5-10 | 4065 | 0.197 | 0.1881 | +0.0089 ± 0.001 | 0.579 | 0.5537 | 0.4869 | 0.4135 | 0.3926 | -0.073 ± 0.0069 | -0.0082 (132) |
| 10-15 | 2822 | 0.2053 | 0.1904 | +0.0148 ± 0.002 | 0.5988 | 0.5594 | 0.5227 | 0.3996 | 0.4004 | -0.061 ± 0.0082 | -0.0053 (105) |
| 15-25 | 3482 | 0.2294 | 0.1986 | +0.0308 ± 0.003 | 0.6615 | 0.5768 | 0.5648 | 0.3696 | 0.39 | -0.064 ± 0.0076 | -0.0253 (107) |
| 25-40 | 2427 | 0.2597 | 0.1825 | +0.0772 ± 0.0055 | 0.7357 | 0.5331 | 0.6246 | 0.3102 | 0.3473 | -0.074 ± 0.0085 | -0.0229 (51) |
| 40+ | 1098 | 0.3766 | 0.1398 | +0.2368 ± 0.0119 | 1.0665 | 0.4236 | 0.725 | 0.2217 | 0.2514 | -0.073 ± 0.0105 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3780 | 1.045 ± 0.046 | 1.167 | 0.1669 | 0.1647 | 0.2136 | 0.2047 |
| gen2 | 3780 | 0.844 ± 0.042 | 1.129 | 0.1706 | 0.1652 | 0.2322 | 0.2044 |
| gen1_elo | 3780 | 1.023 ± 0.045 | 1.149 | 0.1736 | 0.165 | 0.2128 | 0.2047 |
| gen1_sr | 3780 | 1.045 ± 0.055 | 1.205 | 0.1313 | 0.167 | 0.2285 | 0.204 |
| gen1_ledger | 5811 | 0.874 ± 0.032 | 1.085 | 0.1802 | 0.1796 | 0.2184 | 0.1994 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 18,727)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,301 | 23.0% |
| STALE_QUOTE | market_freshness | 3,936 | 21.0% |
| BOOK_QUALITY | execution | 3,603 | 19.2% |
| POOR_DATA | data | 2,118 | 11.3% |
| LIMITED_DATA | data | 1,232 | 6.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,008 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 933 | 5.0% |
| IDENTITY_AMBIGUOUS | mapping | 744 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 541 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 311 | 1.7% |

Cause class: coverage 23.0%, market_freshness 21.0%, execution 19.2%, data 17.9%, market_freshness/coverage 8.3%, model_calibration_or_unknown 5.0%, mapping 4.0%, model_calibration 1.7%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.9%, START_UNVERIFIABLE 94.1%, LOW_DATA_QUALITY 70.5%, THIN_PLAYER_HISTORY 59.2%, STALE_PLAYER_DATA 51.4%, STALE_KALSHI_QUOTE 43.6%, MODEL_INTERNAL_DISAGREEMENT 41.8%, ASYMMETRIC_SAMPLE_SIZE 32.7%, WIDE_SPREAD 25.4%, MODEL_HIGH_UNCERTAINTY 18.0%, PLAYER_IDENTITY_RISK 15.4%, LEVEL_TRANSFER_RISK 10.3%, EVENT_MAPPING_RISK 8.2%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 3.0%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.4%, POST_SETTLEMENT_OBSERVATION 23.0%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 9,957)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,424 | 34.4% |
| BOOK_QUALITY | execution | 1,886 | 18.9% |
| STALE_QUOTE | market_freshness | 1,794 | 18.0% |
| POOR_DATA | data | 886 | 8.9% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 531 | 5.3% |
| IDENTITY_AMBIGUOUS | mapping | 432 | 4.3% |
| LIMITED_DATA | data | 375 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 338 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 216 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 75 | 0.8% |

Cause class: coverage 34.4%, execution 18.9%, market_freshness 18.0%, data 12.7%, market_freshness/coverage 8.7%, mapping 4.3%, model_calibration_or_unknown 2.2%, model_calibration 0.8%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.2%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 74.4%, THIN_PLAYER_HISTORY 61.8%, STALE_KALSHI_QUOTE 51.5%, STALE_PLAYER_DATA 46.8%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 25.0%, PLAYER_IDENTITY_RISK 18.7%, MODEL_HIGH_UNCERTAINTY 18.3%, EVENT_MAPPING_RISK 9.9%, LEVEL_TRANSFER_RISK 9.4%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 5.0%, EXTERNAL_MARKET_REJECTION 1.7%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.3%, POST_SETTLEMENT_OBSERVATION 34.4%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 7827, "IDENTITY_AMBIGUOUS": 2130}; ticker orientation: {"VERIFIED": 9957}.

Checks: discipline:AMBIGUOUS 679, discipline:PASS 9278, identity_confidence:AMBIGUOUS 1865, identity_confidence:PASS 8092, level_mapping:NA 691, level_mapping:PASS 9266, market_pair:AMBIGUOUS 368, market_pair:NA 240, market_pair:PASS 9349, model_complement:NA 207, model_complement:PASS 9750, namesake:PASS 9957, physical_match_id:NA 3677, physical_match_id:PASS 6280, player_ids:PASS 9957, same_pair_other_event:PASS 9957, ticker_orientation:PASS 9957

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,557 | 5.0% | 4.6% | 1.8% | {"market_freshness": 53, "model_calibration_or_unknown": 39, "data": 34, "execution": 19, "model_calibration": 13, "market_freshness/coverage": 11, "coverage": 7} | 5.87 | 0.2252 / 0.2154 (397) | 18.8% | 3.9% | 3.5% | 2.7% |
| CHALLENGER | 7,251 | 17.2% | 6.9% | 12.5% | {"coverage": 705, "market_freshness/coverage": 155, "market_freshness": 148, "data": 112, "model_calibration_or_unknown": 58, "execution": 30, "model_calibration": 27, "mapping": 14} | 7.49 | 0.2176 / 0.2076 (1762) | 35.2% | 17.2% | 3.9% | 22.7% |
| DOUBLES | 1,408 | 48.2% | 47.8% | 6.8% | {"execution": 342, "mapping": 177, "market_freshness": 106, "market_freshness/coverage": 47, "coverage": 7} | 23.92 | 0.322 / 0.2344 (362) | 16.6% | 0.0% | 100.0% | 7.0% |
| ITF_MEN | 12,287 | 25.1% | 17.6% | 30.9% | {"coverage": 1144, "execution": 627, "market_freshness": 502, "data": 417, "market_freshness/coverage": 251, "mapping": 137, "model_calibration_or_unknown": 2, "model_calibration": 1} | 11.5 | 0.2142 / 0.1948 (2822) | 36.7% | 65.7% | 16.8% | 22.0% |
| ITF_WOMEN | 16,720 | 26.7% | 19.6% | 44.9% | {"coverage": 1544, "market_freshness": 907, "execution": 837, "data": 664, "market_freshness/coverage": 356, "mapping": 98, "model_calibration_or_unknown": 49, "model_calibration": 11} | 12.9 | 0.2032 / 0.1949 (3299) | 38.4% | 57.8% | 10.2% | 21.8% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,580 | 4.7% | 4.2% | 1.2% | {"market_freshness": 38, "model_calibration_or_unknown": 27, "execution": 17, "model_calibration": 12, "data": 11, "market_freshness/coverage": 10, "coverage": 4, "mapping": 1} | 7.96 | 0.2365 / 0.2304 (419) | 24.0% | 1.3% | 1.4% | 3.4% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.8% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 15 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 16 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 17 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 18 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 19 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 20 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 21 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 22 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 23 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 24 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 25 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 26 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 27 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 28 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 463 min (STALE); no external reference |
| 29 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 30 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 31 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 32 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 33 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 34 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 92 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 36 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 37 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 38 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 39 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 41 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 162 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 42 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 43 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 44 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 45 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 46 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 535 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |
| 47 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 33 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 48 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 49 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFWMATCH-26OCT16ESTLAB-LAB` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 68 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1475.0, ratio 2.28); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9702, "by_level_share_of_ge_25pp": {"ATP": 0.0177, "CHALLENGER": 0.1254, "DOUBLES": 0.0682, "ITF_MEN": 0.3094, "ITF_WOMEN": 0.4485, "OTHER": 0.0012, "WTA": 0.0121, "WTA125": 0.0175}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5148, "share_primary_cause_market_settled_or_in_play": 0.4311, "share_primary_cause_stale_quote_only": 0.1802}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 9957, "identity_ambiguous_share": 0.2139, "ticker_orientation": {"VERIFIED": 9957}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 6280, "with_external": 302, "coverage": 0.0481, "external_status": {"EXTERNAL_STALE": 187, "AGREES_WITH_KALSHI": 109, "SUPPORTS_MODEL_DIRECTION": 5, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 187, "MODEL_LONE_OUTLIER": 109, "ALL_THREE_DISAGREE": 5, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3609, "share_external_supports_model": 0.0199}, "pregame_clean_ge_25pp": {"n": 3067, "with_external": 285, "coverage": 0.0929, "external_status": {"EXTERNAL_STALE": 174, "AGREES_WITH_KALSHI": 105, "SUPPORTS_MODEL_DIRECTION": 5, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 174, "MODEL_LONE_OUTLIER": 105, "ALL_THREE_DISAGREE": 5, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3684, "share_external_supports_model": 0.0211}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 502.0, "median_sample_ratio": 2.43, "median_min_matches": 20.0, "median_max_days_since_last": 223.0, "share_severe_asymmetry": 0.2089, "data_status": {"POOR": 5495, "LIMITED": 2712, "ADEQUATE": 1750}, "comparison_lt_10pp": {"median_thinner_serve_points": 1753.0, "median_sample_ratio": 1.69, "median_min_matches": 93.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 761, "model_minus_observed": 0.0507, "kalshi_minus_observed": -0.0852, "brier_diff_model_minus_kalshi": -0.0006}, "4-10x": {"n": 519, "model_minus_observed": 0.089, "kalshi_minus_observed": -0.0563, "brier_diff_model_minus_kalshi": 0.0126}, "<2x": {"n": 1856, "model_minus_observed": 0.086, "kalshi_minus_observed": -0.0364, "brier_diff_model_minus_kalshi": 0.0122}, ">=10x": {"n": 644, "model_minus_observed": 0.106, "kalshi_minus_observed": -0.0679, "brier_diff_model_minus_kalshi": 0.0076}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3780, "model": {"intercept": -0.528, "slope": 0.844, "slope_se": 0.042}, "kalshi_mid_same_rows": {"intercept": 0.242, "slope": 1.129, "slope_se": 0.048}, "mean_extremity_model": 0.1706, "mean_extremity_kalshi": 0.1652, "model_brier": 0.2322, "kalshi_brier": 0.2044, "brier_diff_model_minus_kalshi": 0.0278, "brier_diff_se": 0.0031, "model_logloss": 0.6611, "kalshi_logloss": 0.5912}, "fair_v1": {"n": 3780, "model": {"intercept": -0.398, "slope": 1.045, "slope_se": 0.046}, "kalshi_mid_same_rows": {"intercept": 0.32, "slope": 1.167, "slope_se": 0.049}, "mean_extremity_model": 0.1669, "mean_extremity_kalshi": 0.1647, "model_brier": 0.2136, "kalshi_brier": 0.2047, "brier_diff_model_minus_kalshi": 0.0089, "brier_diff_se": 0.0025, "model_logloss": 0.6155, "kalshi_logloss": 0.5916}, "gen1_elo": {"n": 3780, "model": {"intercept": -0.396, "slope": 1.023, "slope_se": 0.045}, "kalshi_mid_same_rows": {"intercept": 0.311, "slope": 1.149, "slope_se": 0.048}, "mean_extremity_model": 0.1736, "mean_extremity_kalshi": 0.165, "model_brier": 0.2128, "kalshi_brier": 0.2047, "brier_diff_model_minus_kalshi": 0.0081, "brier_diff_se": 0.0025, "model_logloss": 0.6145, "kalshi_logloss": 0.5916}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2436, "share_ge_15": 0.4434, "median_abs_gap": 13.12, "n": 25785}, "gen1_elo": {"share_ge_25": 0.2408, "share_ge_15": 0.4397, "median_abs_gap": 12.84, "n": 25785}, "gen1_sr": {"share_ge_25": 0.3084, "share_ge_15": 0.5222, "median_abs_gap": 15.88, "n": 25785}, "gen2": {"share_ge_25": 0.3107, "share_ge_15": 0.5114, "median_abs_gap": 15.52, "n": 25785}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1528, "share_ge_15": 0.3601, "median_abs_gap": 10.95, "n": 20072}, "gen1_elo": {"share_ge_25": 0.1537, "share_ge_15": 0.3538, "median_abs_gap": 10.53, "n": 20070}, "gen1_sr": {"share_ge_25": 0.2173, "share_ge_15": 0.4463, "median_abs_gap": 13.17, "n": 20073}, "gen2": {"share_ge_25": 0.2327, "share_ge_15": 0.4463, "median_abs_gap": 13.14, "n": 20073}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.87, "share_ge_25_all": 0.0495, "share_ge_25_pregame_clean": 0.0457}, "WTA": {"median_abs_gap_pregame_clean": 7.96, "share_ge_25_all": 0.0465, "share_ge_25_pregame_clean": 0.0425}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2361, "share_within_10pp_all": 0.4333, "share_within_10pp_pregame_clean": 0.4856, "corr_model_vs_mid_pregame_clean": 0.8441}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 563, "model_brier": 0.1969, "kalshi_brier": 0.1982, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 656, "model_brier": 0.2132, "kalshi_brier": 0.2038, "brier_diff_model_minus_kalshi": 0.0094}, "15-25": {"n_settled": 848, "model_brier": 0.2255, "kalshi_brier": 0.2147, "brier_diff_model_minus_kalshi": 0.0107}, "25-40": {"n_settled": 476, "model_brier": 0.2261, "kalshi_brier": 0.2106, "brier_diff_model_minus_kalshi": 0.0156}, "3-5": {"n_settled": 358, "model_brier": 0.1999, "kalshi_brier": 0.1996, "brier_diff_model_minus_kalshi": 0.0003}, "40+": {"n_settled": 95, "model_brier": 0.3, "kalshi_brier": 0.1766, "brier_diff_model_minus_kalshi": 0.1234}, "5-10": {"n_settled": 784, "model_brier": 0.2011, "kalshi_brier": 0.2013, "brier_diff_model_minus_kalshi": -0.0002}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.528, "slope": 0.844, "slope_se": 0.042}, "kalshi_slope": {"intercept": 0.242, "slope": 1.129, "slope_se": 0.048}, "n": 3780}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.511, "slope": 0.874, "slope_se": 0.032}, "kalshi_slope": {"intercept": 0.159, "slope": 1.085, "slope_se": 0.037}, "n": 5811}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 362, "model_brier": 0.322, "kalshi_brier": 0.2344, "brier_diff_model_minus_kalshi": 0.0876, "brier_diff_se": 0.0164, "corr_model_outcome": 0.0109, "corr_kalshi_outcome": 0.2581}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
