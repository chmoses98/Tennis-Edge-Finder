# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-16T05:12Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 34,535): 0-3 14.4%, 3-5 9.4%, 5-10 20.1%, 10-15 15.3%, 15-25 18.9%, 25-40 13.6%, 40+ 8.2%; median gap 11.87 pp.
* **Where the extremes live**: 98.3% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.0%, Challenger 12.1%, doubles 6.8%). Main tour: ATP 1.4% and WTA 6.2% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 7,546): MARKET_ALREADY_SETTLED_WHEN_PRICED 36.8%, STALE_QUOTE 18.0%, BOOK_QUALITY 17.4%, POOR_DATA 8.4%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 4.0%, IN_PLAY_QUOTE 3.2%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.5%. By class: coverage 36.8%, market_freshness 18.0%, execution 17.4%, data 12.4%, market_freshness/coverage 8.7%, mapping 4.3%, model_calibration_or_unknown 2.0%, model_calibration 0.5%.
* **Stale / settled / in-play**: 53.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 45.4% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 7,546 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.9% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 3.9%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 21.4% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 553.0 points vs 1761.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.062, Gen-2 0.868, Gen-1 ledger 0.872 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 350 model 0.2248 vs Kalshi 0.2088; n 72 model 0.29 vs Kalshi 0.1741.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 136,800 model-market comparisons (228,239 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 47,604 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-16T05:03:13.374223+00:00'], shadow board 38,356 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-16T05:03:16.849492+00:00'], Model 4 14,384 rows, 14,714 settled tickers, 4,966 tickers with an external scan.
* By model: {"gen1_ledger": 31235, "gen1_elo": 19281, "fair_v1": 19281, "gen2": 19281, "gen1_sr": 19281, "model4_fundamental": 14225, "model4_conditioned": 14216}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 34,535 | 14.4 | 9.4 | 20.1 | 15.3 | 18.9 | 13.6 | 8.2 | 11.87 | 40.8% | 21.9% |
| MW fair_v1 | 19,281 | 13.6 | 8.4 | 18.6 | 15.8 | 19.3 | 14.6 | 9.8 | 12.95 | 43.6% | 24.3% |
| MW gen1_elo | 19,281 | 13.2 | 9.0 | 19.8 | 15.1 | 19.2 | 14.3 | 9.5 | 12.46 | 43.0% | 23.7% |
| MW gen1_ledger | 15,254 | 15.6 | 10.7 | 21.9 | 14.6 | 18.4 | 12.5 | 6.3 | 10.45 | 37.2% | 18.7% |
| MW gen1_sr | 19,281 | 9.7 | 7.5 | 16.3 | 14.2 | 21.8 | 18.7 | 11.8 | 15.87 | 52.3% | 30.5% |
| MW gen2 | 19,281 | 11.4 | 7.1 | 16.5 | 14.2 | 20.2 | 17.6 | 13.0 | 15.41 | 50.8% | 30.6% |
| all families model4_conditioned | 14,216 | 21.7 | 20.1 | 35.2 | 16.7 | 4.3 | 1.1 | 0.9 | 5.81 | 6.3% | 2.0% |
| all families model4_fundamental | 14,225 | 16.8 | 13.6 | 35.8 | 19.6 | 10.6 | 2.6 | 1.1 | 7.57 | 14.2% | 3.7% |

Configurable thresholds (primary): >=5pp 76.1%, >=10pp 56.0%, >=15pp 40.8%, >=20pp 30.2%, >=25pp 21.9%, >=30pp 15.8%, >=40pp 8.2%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.48pp; >=10pp 45.4%, >=25pp 17.4%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,343 | 30.7 | 14.5 | 25.3 | 17.4 | 10.2 | 1.1 | 0.8 | 5.67 | 12.1% | 1.9% |
| CHALLENGER | 3,221 | 16.0 | 9.9 | 20.1 | 15.8 | 14.6 | 12.1 | 11.5 | 11.49 | 38.2% | 23.6% |
| ITF_MEN | 5,532 | 11.1 | 8.3 | 17.7 | 14.8 | 20.0 | 16.2 | 12.0 | 14.25 | 48.1% | 28.2% |
| ITF_WOMEN | 7,607 | 10.4 | 6.6 | 16.3 | 15.8 | 22.2 | 18.0 | 10.7 | 15.36 | 50.9% | 28.7% |
| WTA | 958 | 21.3 | 10.9 | 24.7 | 15.6 | 20.9 | 5.5 | 1.1 | 8.16 | 27.6% | 6.7% |
| WTA125 | 620 | 13.1 | 7.7 | 22.6 | 20.8 | 20.2 | 13.6 | 2.1 | 11.32 | 35.8% | 15.7% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,343 | 24.9 | 14.4 | 24.9 | 18.7 | 14.3 | 1.9 | 1.0 | 6.54 | 17.1% | 2.8% |
| CHALLENGER | 3,221 | 14.8 | 7.8 | 19.6 | 13.4 | 18.2 | 14.2 | 12.1 | 12.69 | 44.4% | 26.2% |
| ITF_MEN | 5,532 | 9.6 | 6.8 | 15.9 | 13.6 | 20.0 | 19.2 | 14.8 | 16.61 | 54.0% | 34.0% |
| ITF_WOMEN | 7,607 | 8.6 | 5.7 | 13.7 | 13.5 | 21.5 | 20.8 | 16.2 | 18.55 | 58.4% | 36.9% |
| WTA | 958 | 17.3 | 8.2 | 19.2 | 16.0 | 22.8 | 15.3 | 1.1 | 12.08 | 39.2% | 16.5% |
| WTA125 | 620 | 6.3 | 4.7 | 16.9 | 18.2 | 25.2 | 19.5 | 9.2 | 17.0 | 53.9% | 28.7% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,343 | 28.1 | 14.3 | 28.7 | 15.2 | 10.3 | 2.5 | 0.9 | 6.03 | 13.7% | 3.4% |
| CHALLENGER | 3,221 | 15.0 | 10.2 | 20.8 | 15.1 | 15.4 | 11.7 | 11.8 | 10.98 | 38.9% | 23.5% |
| ITF_MEN | 5,532 | 10.1 | 8.2 | 18.3 | 14.2 | 20.5 | 16.5 | 12.2 | 14.66 | 49.2% | 28.7% |
| ITF_WOMEN | 7,607 | 10.0 | 6.9 | 16.5 | 15.8 | 23.0 | 18.0 | 9.8 | 15.33 | 50.8% | 27.8% |
| WTA | 958 | 22.6 | 15.2 | 32.5 | 16.3 | 10.5 | 2.1 | 0.7 | 6.17 | 13.4% | 2.8% |
| WTA125 | 620 | 22.6 | 12.6 | 29.2 | 15.0 | 14.2 | 6.1 | 0.3 | 7.57 | 20.6% | 6.5% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 730 | 31.0 | 22.9 | 35.3 | 9.2 | 1.2 | 0.4 | 0.0 | 4.69 | 1.6% | 0.4% |
| CHALLENGER | 2,209 | 22.3 | 15.4 | 27.7 | 14.7 | 12.8 | 5.1 | 2.0 | 6.94 | 19.9% | 7.1% |
| DOUBLES | 1,041 | 5.4 | 3.8 | 11.4 | 10.8 | 19.2 | 24.5 | 25.0 | 24.38 | 68.7% | 49.5% |
| ITF_MEN | 4,710 | 14.8 | 8.6 | 20.6 | 15.4 | 20.9 | 12.6 | 7.2 | 11.89 | 40.7% | 19.8% |
| ITF_WOMEN | 5,073 | 11.7 | 9.3 | 19.6 | 14.7 | 22.3 | 16.6 | 5.7 | 13.01 | 44.7% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 653 | 21.3 | 15.3 | 27.3 | 17.1 | 13.6 | 4.9 | 0.5 | 7.52 | 19.0% | 5.4% |
| WTA125 | 689 | 20.5 | 13.6 | 22.8 | 18.4 | 14.4 | 8.1 | 2.2 | 8.27 | 24.7% | 10.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,329 | 30.6 | 14.4 | 25.5 | 17.4 | 10.2 | 1.1 | 0.8 | 5.71 | 12.0% | 1.9% |
| CHALLENGER | 2,307 | 20.8 | 12.4 | 25.2 | 18.4 | 14.9 | 5.9 | 2.3 | 8.27 | 23.2% | 8.3% |
| ITF_MEN | 4,046 | 13.4 | 10.2 | 21.0 | 16.5 | 20.3 | 13.0 | 5.6 | 11.46 | 38.9% | 18.6% |
| ITF_WOMEN | 5,666 | 12.4 | 8.0 | 18.6 | 17.9 | 23.6 | 14.9 | 4.5 | 12.95 | 43.1% | 19.4% |
| WTA | 938 | 21.5 | 10.2 | 25.1 | 15.6 | 21.0 | 5.4 | 1.2 | 8.16 | 27.6% | 6.6% |
| WTA125 | 596 | 13.4 | 7.5 | 22.0 | 21.1 | 20.8 | 13.4 | 1.7 | 11.33 | 35.9% | 15.1% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,329 | 24.8 | 14.5 | 25.0 | 18.7 | 14.3 | 1.8 | 1.0 | 6.57 | 17.1% | 2.8% |
| CHALLENGER | 2,307 | 18.9 | 10.0 | 24.4 | 16.2 | 18.5 | 9.5 | 2.6 | 9.08 | 30.5% | 12.0% |
| ITF_MEN | 4,047 | 11.3 | 8.1 | 18.3 | 15.3 | 22.1 | 16.6 | 8.4 | 14.03 | 47.1% | 25.0% |
| ITF_WOMEN | 5,666 | 9.8 | 6.6 | 15.3 | 14.7 | 23.6 | 19.9 | 10.1 | 16.27 | 53.6% | 30.0% |
| WTA | 938 | 17.3 | 8.1 | 19.2 | 16.0 | 22.8 | 15.5 | 1.2 | 12.08 | 39.5% | 16.6% |
| WTA125 | 596 | 6.0 | 4.9 | 16.9 | 18.6 | 25.0 | 20.1 | 8.4 | 16.84 | 53.5% | 28.5% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 710 | 31.0 | 23.1 | 35.6 | 9.3 | 0.6 | 0.4 | 0.0 | 4.66 | 1.0% | 0.4% |
| CHALLENGER | 1,904 | 24.1 | 16.8 | 29.9 | 14.4 | 11.9 | 2.4 | 0.5 | 6.34 | 14.8% | 2.9% |
| DOUBLES | 959 | 5.5 | 3.9 | 11.8 | 10.8 | 19.2 | 24.5 | 24.3 | 24.1 | 68.0% | 48.8% |
| ITF_MEN | 3,880 | 16.2 | 9.4 | 22.5 | 16.2 | 20.8 | 10.6 | 4.3 | 10.57 | 35.6% | 14.9% |
| ITF_WOMEN | 4,141 | 12.9 | 10.1 | 21.4 | 15.5 | 22.6 | 15.0 | 2.6 | 11.56 | 40.1% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 619 | 21.8 | 16.0 | 27.5 | 17.1 | 13.9 | 3.7 | 0.0 | 7.21 | 17.6% | 3.7% |
| WTA125 | 584 | 22.4 | 15.1 | 24.3 | 20.0 | 12.8 | 5.0 | 0.3 | 7.36 | 18.1% | 5.3% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,041 | 5.4 | 3.8 | 11.4 | 10.8 | 19.2 | 24.5 | 25.0 | 24.38 | 68.7% | 49.5% |
| singles | 14,213 | 16.3 | 11.2 | 22.7 | 14.9 | 18.4 | 11.6 | 4.9 | 9.95 | 34.9% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 4,541 | 13.4 | 8.9 | 19.5 | 15.8 | 18.0 | 14.4 | 9.9 | 12.65 | 42.3% | 24.4% |
| Grass | 211 | 11.4 | 11.8 | 17.1 | 13.7 | 22.3 | 16.1 | 7.6 | 14.16 | 46.0% | 23.7% |
| Hard | 12,478 | 13.9 | 8.4 | 18.5 | 15.3 | 19.8 | 14.4 | 9.7 | 12.96 | 43.9% | 24.1% |
| UNKNOWN | 2,051 | 12.1 | 7.2 | 17.1 | 18.8 | 19.0 | 15.8 | 10.1 | 13.35 | 44.9% | 25.8% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,567 | 19.8 | 10.7 | 21.0 | 16.9 | 15.8 | 8.9 | 7.0 | 9.52 | 31.6% | 15.8% |
| B | 2,517 | 14.2 | 8.9 | 20.0 | 16.6 | 18.2 | 12.6 | 9.5 | 11.63 | 40.3% | 22.1% |
| C | 2,794 | 12.8 | 9.6 | 20.1 | 14.2 | 19.3 | 14.3 | 9.8 | 12.62 | 43.3% | 24.1% |
| D | 3,344 | 11.6 | 7.9 | 17.6 | 16.1 | 22.1 | 15.3 | 9.4 | 13.84 | 46.8% | 24.7% |
| F | 5,059 | 8.1 | 5.4 | 15.1 | 14.9 | 21.9 | 21.4 | 13.2 | 17.86 | 56.5% | 34.6% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,420 | 22.9 | 15.8 | 28.9 | 15.1 | 11.2 | 4.4 | 1.6 | 6.7 | 17.3% | 6.0% |
| B | 2,284 | 14.9 | 10.1 | 24.0 | 16.3 | 19.5 | 11.1 | 4.2 | 10.18 | 34.8% | 15.2% |
| C | 3,016 | 12.2 | 7.8 | 18.2 | 14.2 | 20.5 | 15.8 | 11.5 | 13.8 | 47.8% | 27.3% |
| D | 2,286 | 14.0 | 9.8 | 20.7 | 13.6 | 21.4 | 13.9 | 6.6 | 11.86 | 41.8% | 20.4% |
| F | 3,248 | 10.3 | 7.6 | 15.2 | 14.0 | 23.5 | 20.4 | 9.0 | 16.28 | 52.9% | 29.4% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 6,306 | 18.1 | 9.6 | 20.3 | 16.7 | 16.2 | 10.0 | 9.1 | 10.54 | 35.3% | 19.0% |
| LIMITED | 4,464 | 14.8 | 10.3 | 20.9 | 15.3 | 18.5 | 12.8 | 7.3 | 11.16 | 38.6% | 20.1% |
| POOR | 8,511 | 9.6 | 6.5 | 16.1 | 15.4 | 22.0 | 18.9 | 11.6 | 15.89 | 52.4% | 30.4% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,062 | 31.2 | 24.6 | 36.2 | 5.6 | 1.7 | 0.7 | 0.1 | 4.49 | 2.5% | 0.7% |
| GAME_SPREAD | 2,906 | 25.7 | 16.2 | 36.6 | 16.8 | 4.1 | 0.4 | 0.2 | 5.96 | 4.7% | 0.6% |
| MATCH_WINNER | 15,254 | 15.6 | 10.7 | 21.9 | 14.6 | 18.4 | 12.5 | 6.3 | 10.45 | 37.2% | 18.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 5,545 | 33.4 | 19.6 | 31.1 | 9.6 | 5.0 | 1.1 | 0.2 | 4.71 | 6.4% | 1.4% |
| TOTAL_GAMES | 4,444 | 6.7 | 9.2 | 39.4 | 29.4 | 10.3 | 2.7 | 2.3 | 9.44 | 15.3% | 5.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,965 | 25.6 | 38.3 | 31.3 | 0.3 | 3.8 | 0.4 | 0.1 | 4.29 | 4.4% | 0.5% |
| GAME_SPREAD | 3,537 | 45.5 | 16.5 | 28.6 | 7.2 | 1.1 | 0.7 | 0.4 | 3.53 | 2.2% | 1.1% |
| TOTAL_GAMES | 5,714 | 3.5 | 6.6 | 42.7 | 36.8 | 6.8 | 1.9 | 1.9 | 9.77 | 10.5% | 3.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,965 | 26.5 | 18.9 | 37.0 | 9.1 | 6.2 | 2.0 | 0.3 | 5.47 | 8.5% | 2.4% |
| GAME_SPREAD | 3,537 | 19.6 | 13.6 | 30.4 | 20.8 | 12.7 | 2.3 | 0.7 | 7.64 | 15.7% | 3.0% |
| TOTAL_GAMES | 5,723 | 6.6 | 9.1 | 38.0 | 28.0 | 13.0 | 3.2 | 2.1 | 9.6 | 18.3% | 5.3% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 19,281 | 43.6% | 24.3% | 12.95 | 34.8% | 14.9% | 10.62 |
| gen1_elo | 19,281 | 43.0% | 23.7% | 12.46 | 33.8% | 14.7% | 10.09 |
| gen1_sr | 19,281 | 52.3% | 30.5% | 15.87 | 44.5% | 21.2% | 13.28 |
| gen2 | 19,281 | 50.8% | 30.6% | 15.41 | 44.1% | 22.5% | 13.01 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 10,279 | 16.4 | 10.4 | 21.6 | 17.2 | 19.8 | 11.3 | 3.3 | 10.43 | 34.3% | 14.6% |
| STALE | 9,002 | 10.3 | 6.2 | 15.1 | 14.1 | 18.8 | 18.3 | 17.1 | 17.16 | 54.2% | 35.4% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 8,722 | 17.4 | 11.6 | 23.6 | 14.5 | 16.9 | 11.2 | 4.8 | 9.39 | 32.9% | 16.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 34,535 | 8722 | 13751 | 12062 | 24.4 | 155.4 | 1400.4 |
| ge_15pp | 14,082 | 2873 | 4819 | 6390 | 26.9 | 457.0 | 1380.4 |
| ge_25pp | 7,546 | 1397 | 2091 | 4058 | 34.5 | 589.4 | 1380.4 |
| lt_10pp | 15,178 | 4581 | 6611 | 3986 | 22.6 | 48.8 | 1341.5 |

Current slate `SL-20261016T051243Z-1b439f3c`: 261 priced rows, quote age at build {'median': 9.7, 'max': 9.8}, freshness {'FRESH': 261}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 10 | 0.0 | 0.0 | 40.0 | 0.0 | 40.0 | 20.0 | 0.0 | 20.33 | 60.0% | 20.0% |
| EXTERNAL_LONE_OUTLIER | 11 | 72.7 | 27.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,652 | 21.1 | 10.7 | 23.0 | 18.2 | 19.2 | 7.1 | 0.7 | 8.82 | 27.0% | 7.8% |
| KALSHI_LONE_OUTLIER | 8 | 12.5 | 0.0 | 62.5 | 0.0 | 12.5 | 12.5 | 0.0 | 5.11 | 25.0% | 12.5% |
| MARKETS_AGREE | 267 | 70.8 | 29.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.08 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 531 | 0.0 | 3.8 | 34.8 | 28.1 | 23.9 | 8.7 | 0.8 | 11.66 | 33.3% | 9.4% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 19,281 | 2479 (12.9%) | 21.4% | 0.7% | {"EXTERNAL_STALE": 1652, "AGREES_WITH_KALSHI": 531, "ALL_AGREE": 267, "EXTERNAL_OUTLIER": 11, "SUPPORTS_MODEL_DIRECTION": 9, "AGREES_WITH_MODEL": 8, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 8,410 | 631 (7.5%) | 28.1% | 1.3% | {"EXTERNAL_STALE": 446, "AGREES_WITH_KALSHI": 177, "SUPPORTS_MODEL_DIRECTION": 6, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 4,687 | 182 (3.9%) | 27.5% | 1.7% | {"EXTERNAL_STALE": 129, "AGREES_WITH_KALSHI": 50, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,221 | 172 (7.7%) | 27.9% | 1.7% | {"EXTERNAL_STALE": 121, "AGREES_WITH_KALSHI": 48, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 7,828 | 1399 (17.9%) | 14.6% | 0.6% | {"EXTERNAL_STALE": 906, "ALL_AGREE": 267, "AGREES_WITH_KALSHI": 205, "EXTERNAL_OUTLIER": 11, "AGREES_WITH_MODEL": 6, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,741 | 11.2 | 7.7 | 19.8 | 15.0 | 21.9 | 14.3 | 10.0 | 13.58 | 46.2% | 24.3% |
| 4-10x | 2,507 | 12.7 | 8.9 | 19.6 | 15.4 | 19.1 | 15.4 | 8.9 | 12.74 | 43.4% | 24.3% |
| <2x | 10,043 | 15.4 | 9.1 | 18.9 | 16.8 | 17.8 | 13.0 | 9.0 | 11.91 | 39.8% | 22.1% |
| >=10x | 2,990 | 10.9 | 6.6 | 15.3 | 13.8 | 21.4 | 19.3 | 12.6 | 16.38 | 53.3% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 5,063 | 13.6 | 8.2 | 19.4 | 16.0 | 19.6 | 12.9 | 10.2 | 12.69 | 42.7% | 23.1% |
| 300-1000 | 4,365 | 12.0 | 8.7 | 17.4 | 15.9 | 21.1 | 15.8 | 9.2 | 13.67 | 46.0% | 25.0% |
| <300 | 5,737 | 9.1 | 6.1 | 15.7 | 14.7 | 21.6 | 20.2 | 12.6 | 16.73 | 54.4% | 32.8% |
| >=3000 | 4,116 | 21.5 | 11.6 | 22.9 | 16.9 | 13.9 | 7.4 | 5.8 | 8.38 | 27.1% | 13.2% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 607 | 0.5374 | 0.4061 | 0.4876 | +0.050 | -0.082 | -0.0 ± 0.0059 |
| ratio 4-10x | 407 | 0.5855 | 0.4466 | 0.5111 | +0.074 | -0.065 | 0.0071 ± 0.0078 |
| ratio <2x | 1471 | 0.5366 | 0.4143 | 0.4548 | +0.082 | -0.041 | 0.011 ± 0.0037 |
| ratio >=10x | 487 | 0.5448 | 0.3782 | 0.4251 | +0.120 | -0.047 | 0.0147 ± 0.008 |
| thinner_sample 1000-3000 | 830 | 0.5425 | 0.4173 | 0.4723 | +0.070 | -0.055 | 0.0047 ± 0.005 |
| thinner_sample 300-1000 | 721 | 0.56 | 0.4227 | 0.4882 | +0.072 | -0.066 | 0.0013 ± 0.0057 |
| thinner_sample <300 | 915 | 0.5433 | 0.3831 | 0.4393 | +0.104 | -0.056 | 0.0156 ± 0.0057 |
| thinner_sample >=3000 | 506 | 0.5297 | 0.4351 | 0.4625 | +0.067 | -0.027 | 0.0142 ± 0.0052 |
| data_status ADEQUATE | 855 | 0.5329 | 0.4282 | 0.4596 | +0.073 | -0.031 | 0.0089 ± 0.0043 |
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
| 5-10 | 628 | 0.1949 | 0.1953 | -0.0004 ± 0.0027 | 0.5743 | 0.573 | 0.5091 | 0.4347 | 0.4666 | -0.080 ± 0.0183 | -0.0167 (6) |
| 10-15 | 526 | 0.2122 | 0.2039 | +0.0082 ± 0.0049 | 0.612 | 0.5897 | 0.5201 | 0.3962 | 0.424 | -0.085 ± 0.0196 | -0.048 (5) |
| 15-25 | 650 | 0.2309 | 0.2171 | +0.0138 ± 0.0071 | 0.6571 | 0.6203 | 0.5759 | 0.3807 | 0.4446 | -0.076 ± 0.0181 | -0.0075 (8) |
| 25-40 | 350 | 0.2248 | 0.2088 | +0.0160 ± 0.0145 | 0.6402 | 0.5993 | 0.6454 | 0.3367 | 0.4657 | -0.061 ± 0.0223 | -0.01 (1) |
| 40+ | 72 | 0.29 | 0.1741 | +0.1160 ± 0.0438 | 0.7878 | 0.5206 | 0.7443 | 0.2967 | 0.3889 | -0.113 ± 0.0433 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2140 | 0.1758 | 0.1769 | -0.0012 ± 0.0003 | 0.5244 | 0.5256 | 0.4766 | 0.4616 | 0.4986 | -0.018 ± 0.0092 | -0.0129 (17) |
| 3-5 | 1316 | 0.1932 | 0.1915 | +0.0017 ± 0.001 | 0.5668 | 0.5586 | 0.4802 | 0.4406 | 0.4362 | -0.063 ± 0.0123 | 0.0 (2) |
| 5-10 | 2922 | 0.1912 | 0.1892 | +0.0021 ± 0.0012 | 0.5643 | 0.5561 | 0.4833 | 0.4094 | 0.4292 | -0.044 ± 0.0082 | -0.0119 (21) |
| 10-15 | 2522 | 0.2018 | 0.1827 | +0.0191 ± 0.0021 | 0.5897 | 0.5375 | 0.4794 | 0.3549 | 0.341 | -0.077 ± 0.0085 | -0.0281 (16) |
| 15-25 | 3072 | 0.2088 | 0.1726 | +0.0362 ± 0.0029 | 0.61 | 0.5087 | 0.5012 | 0.3052 | 0.3122 | -0.065 ± 0.0075 | -0.0033 (42) |
| 25-40 | 2407 | 0.2201 | 0.1267 | +0.0934 ± 0.0045 | 0.6335 | 0.3899 | 0.5281 | 0.2151 | 0.2264 | -0.059 ± 0.007 | -0.01 (1) |
| 40+ | 1613 | 0.3736 | 0.0435 | +0.3301 ± 0.0058 | 0.9726 | 0.1717 | 0.6252 | 0.1049 | 0.0583 | -0.083 ± 0.0049 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 347 | 0.1976 | 0.198 | -0.0004 ± 0.0008 | 0.5766 | 0.5775 | 0.5016 | 0.4864 | 0.5072 | -0.079 ± 0.0251 | -0.01 (3) |
| 3-5 | 236 | 0.2098 | 0.2087 | +0.0011 ± 0.0024 | 0.6015 | 0.6004 | 0.5169 | 0.4769 | 0.4788 | -0.083 ± 0.0312 | 0.02 (1) |
| 5-10 | 536 | 0.1983 | 0.1977 | +0.0006 ± 0.0029 | 0.5796 | 0.5783 | 0.552 | 0.4773 | 0.5112 | -0.071 ± 0.0199 | -0.01 (4) |
| 10-15 | 486 | 0.2126 | 0.205 | +0.0076 ± 0.0051 | 0.6113 | 0.5944 | 0.568 | 0.4436 | 0.4794 | -0.086 ± 0.0214 | -0.04 (5) |
| 15-25 | 723 | 0.2288 | 0.209 | +0.0198 ± 0.0067 | 0.6495 | 0.6003 | 0.5876 | 0.3908 | 0.4426 | -0.086 ± 0.0172 | -0.0188 (8) |
| 25-40 | 465 | 0.2649 | 0.2004 | +0.0645 ± 0.0131 | 0.7419 | 0.582 | 0.6617 | 0.3474 | 0.4043 | -0.109 ± 0.0206 | -0.0075 (4) |
| 40+ | 179 | 0.3563 | 0.1809 | +0.1755 ± 0.031 | 0.9856 | 0.5335 | 0.7393 | 0.259 | 0.3296 | -0.063 ± 0.0307 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1818 | 0.1829 | 0.1832 | -0.0004 ± 0.0003 | 0.5409 | 0.5416 | 0.4969 | 0.4822 | 0.505 | -0.034 ± 0.0104 | -0.0133 (15) |
| 3-5 | 1156 | 0.1925 | 0.1916 | +0.0009 ± 0.001 | 0.5596 | 0.5575 | 0.5156 | 0.4756 | 0.4844 | -0.042 ± 0.0131 | 0.02 (1) |
| 5-10 | 2552 | 0.1903 | 0.1876 | +0.0027 ± 0.0013 | 0.5627 | 0.5524 | 0.5128 | 0.439 | 0.4592 | -0.042 ± 0.0087 | -0.0117 (6) |
| 10-15 | 2232 | 0.1946 | 0.1817 | +0.0129 ± 0.0023 | 0.574 | 0.5326 | 0.5177 | 0.3933 | 0.4068 | -0.055 ± 0.0092 | -0.02 (17) |
| 15-25 | 3241 | 0.2163 | 0.1767 | +0.0396 ± 0.0029 | 0.6282 | 0.521 | 0.5319 | 0.3355 | 0.3363 | -0.073 ± 0.0075 | -0.0095 (41) |
| 25-40 | 2817 | 0.2483 | 0.1383 | +0.1100 ± 0.0045 | 0.7039 | 0.4219 | 0.5603 | 0.244 | 0.2304 | -0.082 ± 0.007 | -0.0044 (18) |
| 40+ | 2176 | 0.3988 | 0.0681 | +0.3307 ± 0.0064 | 1.0459 | 0.2367 | 0.6633 | 0.1269 | 0.1002 | -0.066 ± 0.0055 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 451 | 0.1915 | 0.1943 | -0.0027 ± 0.0007 | 0.5615 | 0.5683 | 0.4936 | 0.4783 | 0.5565 | +0.002 ± 0.021 | -0.0137 (8) |
| 3-5 | 319 | 0.1879 | 0.1859 | +0.0020 ± 0.0019 | 0.5516 | 0.5468 | 0.4943 | 0.4549 | 0.4514 | -0.114 ± 0.0254 | 0.0067 (3) |
| 5-10 | 656 | 0.1999 | 0.1971 | +0.0028 ± 0.0026 | 0.5865 | 0.5764 | 0.5038 | 0.43 | 0.4451 | -0.088 ± 0.0178 | -0.0071 (7) |
| 10-15 | 514 | 0.208 | 0.2082 | -0.0001 ± 0.005 | 0.6037 | 0.6 | 0.5367 | 0.4137 | 0.4786 | -0.059 ± 0.02 | -0.0317 (6) |
| 15-25 | 599 | 0.2364 | 0.2114 | +0.0250 ± 0.0073 | 0.6727 | 0.6072 | 0.5837 | 0.3903 | 0.4224 | -0.108 ± 0.0186 | -0.03 (1) |
| 25-40 | 366 | 0.2105 | 0.2129 | -0.0024 ± 0.0141 | 0.6085 | 0.609 | 0.6508 | 0.3406 | 0.4973 | -0.040 ± 0.0214 | 0.0 (1) |
| 40+ | 67 | 0.3098 | 0.1842 | +0.1256 ± 0.0472 | 0.8354 | 0.5436 | 0.749 | 0.2957 | 0.3881 | -0.101 ± 0.0493 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2055 | 0.1821 | 0.1832 | -0.0011 ± 0.0003 | 0.5382 | 0.5402 | 0.4813 | 0.4661 | 0.4993 | -0.019 ± 0.0095 | -0.0163 (35) |
| 3-5 | 1397 | 0.1857 | 0.183 | +0.0027 ± 0.0009 | 0.5478 | 0.5413 | 0.4759 | 0.4365 | 0.423 | -0.076 ± 0.0118 | -0.0094 (18) |
| 5-10 | 3102 | 0.1929 | 0.1871 | +0.0059 ± 0.0012 | 0.5696 | 0.5501 | 0.4786 | 0.4048 | 0.4001 | -0.065 ± 0.0078 | -0.01 (31) |
| 10-15 | 2385 | 0.1952 | 0.1808 | +0.0144 ± 0.0022 | 0.5747 | 0.5315 | 0.4963 | 0.3731 | 0.3765 | -0.063 ± 0.0087 | -0.015 (12) |
| 15-25 | 3136 | 0.2105 | 0.1712 | +0.0393 ± 0.0029 | 0.6157 | 0.5063 | 0.5053 | 0.3101 | 0.3084 | -0.072 ± 0.0074 | -0.03 (2) |
| 25-40 | 2357 | 0.2147 | 0.1255 | +0.0892 ± 0.0046 | 0.6213 | 0.3858 | 0.5252 | 0.2098 | 0.23 | -0.054 ± 0.0069 | 0.0 (1) |
| 40+ | 1560 | 0.3869 | 0.046 | +0.3409 ± 0.0061 | 1.01 | 0.1781 | 0.6338 | 0.1075 | 0.0583 | -0.085 ± 0.0052 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 776 | 0.1965 | 0.1968 | -0.0003 ± 0.0006 | 0.5741 | 0.5744 | 0.5053 | 0.4902 | 0.4974 | -0.047 ± 0.0159 | -0.0224 (49) |
| 3-5 | 553 | 0.1938 | 0.1936 | +0.0002 ± 0.0015 | 0.5657 | 0.5636 | 0.4796 | 0.4398 | 0.4539 | -0.043 ± 0.0188 | -0.0194 (34) |
| 5-10 | 1165 | 0.1955 | 0.19 | +0.0056 ± 0.0019 | 0.5767 | 0.561 | 0.487 | 0.4134 | 0.4129 | -0.063 ± 0.013 | -0.005 (78) |
| 10-15 | 729 | 0.2071 | 0.1966 | +0.0105 ± 0.0041 | 0.6023 | 0.575 | 0.5032 | 0.3803 | 0.3978 | -0.051 ± 0.0165 | 0.0014 (64) |
| 15-25 | 980 | 0.233 | 0.2123 | +0.0206 ± 0.0058 | 0.6643 | 0.6106 | 0.5628 | 0.3682 | 0.4133 | -0.053 ± 0.0147 | -0.0216 (58) |
| 25-40 | 568 | 0.2522 | 0.1955 | +0.0567 ± 0.0115 | 0.7107 | 0.5683 | 0.6452 | 0.3325 | 0.3961 | -0.083 ± 0.0173 | -0.0219 (26) |
| 40+ | 193 | 0.3701 | 0.1933 | +0.1769 ± 0.0321 | 1.0713 | 0.5679 | 0.793 | 0.3026 | 0.3886 | -0.075 ± 0.029 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2315 | 0.188 | 0.1881 | -0.0001 ± 0.0003 | 0.5518 | 0.5511 | 0.503 | 0.4876 | 0.4985 | -0.034 ± 0.009 | -0.0157 (88) |
| 3-5 | 1588 | 0.1878 | 0.1855 | +0.0024 ± 0.0009 | 0.5501 | 0.5445 | 0.4885 | 0.4488 | 0.4389 | -0.056 ± 0.0109 | -0.0209 (69) |
| 5-10 | 3247 | 0.1926 | 0.1851 | +0.0075 ± 0.0011 | 0.5694 | 0.548 | 0.4806 | 0.4069 | 0.3961 | -0.063 ± 0.0077 | -0.0082 (132) |
| 10-15 | 2176 | 0.2037 | 0.1894 | +0.0143 ± 0.0023 | 0.595 | 0.5571 | 0.5095 | 0.3865 | 0.3897 | -0.056 ± 0.0093 | -0.0053 (105) |
| 15-25 | 2743 | 0.2295 | 0.1989 | +0.0307 ± 0.0033 | 0.6623 | 0.5773 | 0.5548 | 0.3597 | 0.3799 | -0.058 ± 0.0086 | -0.0255 (106) |
| 25-40 | 1870 | 0.254 | 0.1693 | +0.0846 ± 0.006 | 0.72 | 0.5004 | 0.6069 | 0.2925 | 0.3171 | -0.076 ± 0.0092 | -0.0229 (51) |
| 40+ | 910 | 0.3847 | 0.1312 | +0.2535 ± 0.0128 | 1.0915 | 0.4003 | 0.709 | 0.2021 | 0.2187 | -0.068 ± 0.0114 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2972 | 1.062 ± 0.052 | 1.173 | 0.1689 | 0.1714 | 0.2109 | 0.2021 |
| gen2 | 2972 | 0.868 ± 0.047 | 1.125 | 0.1769 | 0.1714 | 0.2288 | 0.202 |
| gen1_elo | 2972 | 1.042 ± 0.05 | 1.162 | 0.1739 | 0.1718 | 0.2099 | 0.2019 |
| gen1_sr | 2972 | 1.08 ± 0.061 | 1.194 | 0.1363 | 0.1732 | 0.2248 | 0.2017 |
| gen1_ledger | 4964 | 0.872 ± 0.035 | 1.077 | 0.1772 | 0.1863 | 0.2178 | 0.1976 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 14,082)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,517 | 25.0% |
| STALE_QUOTE | market_freshness | 2,929 | 20.8% |
| BOOK_QUALITY | execution | 2,523 | 17.9% |
| POOR_DATA | data | 1,560 | 11.1% |
| LIMITED_DATA | data | 1,015 | 7.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 760 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 676 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 552 | 3.9% |
| IN_PLAY_QUOTE | market_freshness/coverage | 395 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 155 | 1.1% |

Cause class: coverage 25.0%, market_freshness 20.8%, data 18.3%, execution 17.9%, market_freshness/coverage 8.2%, model_calibration_or_unknown 4.8%, mapping 3.9%, model_calibration 1.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.1%, START_UNVERIFIABLE 96.0%, LOW_DATA_QUALITY 69.2%, THIN_PLAYER_HISTORY 58.1%, STALE_PLAYER_DATA 52.5%, STALE_KALSHI_QUOTE 45.4%, MODEL_INTERNAL_DISAGREEMENT 39.3%, ASYMMETRIC_SAMPLE_SIZE 31.8%, WIDE_SPREAD 23.8%, MODEL_HIGH_UNCERTAINTY 17.3%, PLAYER_IDENTITY_RISK 13.9%, LEVEL_TRANSFER_RISK 8.3%, EVENT_MAPPING_RISK 8.0%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 3.5%, EXTERNAL_MARKET_REJECTION 1.8%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 27.4%, POST_SETTLEMENT_OBSERVATION 25.0%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 7,546)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,774 | 36.8% |
| STALE_QUOTE | market_freshness | 1,359 | 18.0% |
| BOOK_QUALITY | execution | 1,313 | 17.4% |
| POOR_DATA | data | 632 | 8.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 410 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 323 | 4.3% |
| LIMITED_DATA | data | 304 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 244 | 3.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 150 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 37 | 0.5% |

Cause class: coverage 36.8%, market_freshness 18.0%, execution 17.4%, data 12.4%, market_freshness/coverage 8.7%, mapping 4.3%, model_calibration_or_unknown 2.0%, model_calibration 0.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.0%, START_UNVERIFIABLE 98.3%, LOW_DATA_QUALITY 72.8%, THIN_PLAYER_HISTORY 60.3%, STALE_KALSHI_QUOTE 53.8%, STALE_PLAYER_DATA 47.6%, MODEL_INTERNAL_DISAGREEMENT 40.2%, ASYMMETRIC_SAMPLE_SIZE 33.7%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 17.8%, PLAYER_IDENTITY_RISK 17.3%, EVENT_MAPPING_RISK 9.8%, LOW_DISPLAYED_LIQUIDITY 8.0%, LEVEL_TRANSFER_RISK 7.3%, MODEL_CALIBRATION_OUTLIER 4.5%, EXTERNAL_MARKET_REJECTION 0.9%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 39.5%, POST_SETTLEMENT_OBSERVATION 36.8%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 6045, "IDENTITY_AMBIGUOUS": 1501}; ticker orientation: {"VERIFIED": 7546}.

Checks: discipline:AMBIGUOUS 515, discipline:PASS 7031, identity_confidence:AMBIGUOUS 1306, identity_confidence:PASS 6240, level_mapping:NA 527, level_mapping:PASS 7019, market_pair:AMBIGUOUS 278, market_pair:NA 177, market_pair:PASS 7091, model_complement:NA 144, model_complement:PASS 7402, namesake:PASS 7546, physical_match_id:NA 2859, physical_match_id:PASS 4687, player_ids:PASS 7546, same_pair_other_event:PASS 7546, ticker_orientation:PASS 7546

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,073 | 1.4% | 1.4% | 0.4% | {"market_freshness": 20, "execution": 8, "market_freshness/coverage": 1} | 5.24 | 0.2093 / 0.2118 (255) | 16.4% | 0.5% | 5.3% | 1.6% |
| CHALLENGER | 5,430 | 16.9% | 5.9% | 12.1% | {"coverage": 556, "market_freshness/coverage": 113, "market_freshness": 111, "data": 62, "model_calibration_or_unknown": 46, "execution": 13, "model_calibration": 9, "mapping": 6} | 7.18 | 0.2169 / 0.2041 (1415) | 37.2% | 9.3% | 2.4% | 22.4% |
| DOUBLES | 1,041 | 49.5% | 48.8% | 6.8% | {"execution": 210, "mapping": 152, "market_freshness": 106, "market_freshness/coverage": 40, "coverage": 7} | 24.1 | 0.3315 / 0.2334 (316) | 22.5% | 0.0% | 100.0% | 7.9% |
| ITF_MEN | 10,242 | 24.3% | 16.8% | 33.0% | {"coverage": 960, "execution": 512, "market_freshness": 387, "data": 343, "market_freshness/coverage": 202, "mapping": 85, "model_calibration_or_unknown": 2} | 11.1 | 0.2128 / 0.1948 (2500) | 36.4% | 60.6% | 11.9% | 22.6% |
| ITF_WOMEN | 12,680 | 26.2% | 18.7% | 43.9% | {"coverage": 1234, "market_freshness": 660, "execution": 549, "data": 497, "market_freshness/coverage": 252, "mapping": 74, "model_calibration_or_unknown": 40, "model_calibration": 10} | 12.46 | 0.2021 / 0.192 (2672) | 39.2% | 57.5% | 10.0% | 22.7% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,611 | 6.2% | 5.5% | 1.3% | {"market_freshness": 36, "model_calibration_or_unknown": 22, "data": 11, "market_freshness/coverage": 10, "model_calibration": 8, "execution": 7, "coverage": 4, "mapping": 1} | 7.82 | 0.2398 / 0.2312 (289) | 26.3% | 1.3% | 1.7% | 3.4% |
| WTA125 | 1,309 | 12.8% | 10.2% | 2.2% | {"model_calibration_or_unknown": 38, "market_freshness": 37, "market_freshness/coverage": 35, "data": 23, "coverage": 12, "model_calibration": 10, "execution": 9, "mapping": 4} | 9.39 | 0.2148 / 0.2048 (447) | 23.2% | 7.8% | 4.4% | 9.8% |

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
| 11 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 12 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 13 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 14 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 15 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 16 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 17 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 18 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 19 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 20 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 22 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 23 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 24 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 25 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 26 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 321 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 27 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 28 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 29 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 30 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 31 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 32 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 33 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 34 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 35 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 33 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 36 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 37 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 39 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 40 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 41 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 42 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 43 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 44 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 45 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 46 | `KXATPCHALLENGERMATCH-26OCT13GIUSEA-SEA` | CHALLENGER | fair_v1 | 76% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 757 min (STALE); no external reference |
| 47 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 64 min (STALE); no external reference |
| 48 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 49 | `KXITFWMATCH-26OCT13MAMSTR-MAM` | ITF_WOMEN | fair_v1 | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 406 min (STALE); data LIMITED (grade C, thinner serve sample 879.0, ratio 2.64); no external reference |
| 50 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.983, "by_level_share_of_ge_25pp": {"ATP": 0.0038, "CHALLENGER": 0.1214, "DOUBLES": 0.0682, "ITF_MEN": 0.3301, "ITF_WOMEN": 0.4394, "OTHER": 0.0016, "WTA": 0.0131, "WTA125": 0.0223}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5378, "share_primary_cause_market_settled_or_in_play": 0.4542, "share_primary_cause_stale_quote_only": 0.1801}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 7546, "identity_ambiguous_share": 0.1989, "ticker_orientation": {"VERIFIED": 7546}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 4687, "with_external": 182, "coverage": 0.0388, "external_status": {"EXTERNAL_STALE": 129, "AGREES_WITH_KALSHI": 50, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 129, "MODEL_LONE_OUTLIER": 50, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.2747, "share_external_supports_model": 0.0165}, "pregame_clean_ge_25pp": {"n": 2221, "with_external": 172, "coverage": 0.0774, "external_status": {"EXTERNAL_STALE": 121, "AGREES_WITH_KALSHI": 48, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 121, "MODEL_LONE_OUTLIER": 48, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.2791, "share_external_supports_model": 0.0174}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 553.0, "median_sample_ratio": 2.38, "median_min_matches": 20.0, "median_max_days_since_last": 204.0, "share_severe_asymmetry": 0.2024, "data_status": {"POOR": 4027, "LIMITED": 2150, "ADEQUATE": 1369}, "comparison_lt_10pp": {"median_thinner_serve_points": 1761.0, "median_sample_ratio": 1.7, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 607, "model_minus_observed": 0.0498, "kalshi_minus_observed": -0.0816, "brier_diff_model_minus_kalshi": -0.0}, "4-10x": {"n": 407, "model_minus_observed": 0.0744, "kalshi_minus_observed": -0.0645, "brier_diff_model_minus_kalshi": 0.0071}, "<2x": {"n": 1471, "model_minus_observed": 0.0818, "kalshi_minus_observed": -0.0405, "brier_diff_model_minus_kalshi": 0.011}, ">=10x": {"n": 487, "model_minus_observed": 0.1198, "kalshi_minus_observed": -0.0468, "brier_diff_model_minus_kalshi": 0.0147}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2972, "model": {"intercept": -0.542, "slope": 0.868, "slope_se": 0.047}, "kalshi_mid_same_rows": {"intercept": 0.236, "slope": 1.125, "slope_se": 0.053}, "mean_extremity_model": 0.1769, "mean_extremity_kalshi": 0.1714, "model_brier": 0.2288, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0269, "brier_diff_se": 0.0035, "model_logloss": 0.653, "kalshi_logloss": 0.5858}, "fair_v1": {"n": 2972, "model": {"intercept": -0.393, "slope": 1.062, "slope_se": 0.052}, "kalshi_mid_same_rows": {"intercept": 0.323, "slope": 1.173, "slope_se": 0.054}, "mean_extremity_model": 0.1689, "mean_extremity_kalshi": 0.1714, "model_brier": 0.2109, "kalshi_brier": 0.2021, "brier_diff_model_minus_kalshi": 0.0088, "brier_diff_se": 0.0028, "model_logloss": 0.6091, "kalshi_logloss": 0.5859}, "gen1_elo": {"n": 2972, "model": {"intercept": -0.374, "slope": 1.042, "slope_se": 0.05}, "kalshi_mid_same_rows": {"intercept": 0.325, "slope": 1.162, "slope_se": 0.053}, "mean_extremity_model": 0.1739, "mean_extremity_kalshi": 0.1718, "model_brier": 0.2099, "kalshi_brier": 0.2019, "brier_diff_model_minus_kalshi": 0.008, "brier_diff_se": 0.0028, "model_logloss": 0.6076, "kalshi_logloss": 0.5855}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2431, "share_ge_15": 0.4362, "median_abs_gap": 12.95, "n": 19281}, "gen1_elo": {"share_ge_25": 0.2372, "share_ge_15": 0.4295, "median_abs_gap": 12.46, "n": 19281}, "gen1_sr": {"share_ge_25": 0.3052, "share_ge_15": 0.523, "median_abs_gap": 15.87, "n": 19281}, "gen2": {"share_ge_25": 0.3063, "share_ge_15": 0.5083, "median_abs_gap": 15.41, "n": 19281}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1492, "share_ge_15": 0.3482, "median_abs_gap": 10.62, "n": 14882}, "gen1_elo": {"share_ge_25": 0.1467, "share_ge_15": 0.3376, "median_abs_gap": 10.09, "n": 14881}, "gen1_sr": {"share_ge_25": 0.2118, "share_ge_15": 0.4449, "median_abs_gap": 13.28, "n": 14882}, "gen2": {"share_ge_25": 0.2253, "share_ge_15": 0.4408, "median_abs_gap": 13.01, "n": 14883}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.24, "share_ge_25_all": 0.014, "share_ge_25_pregame_clean": 0.0137}, "WTA": {"median_abs_gap_pregame_clean": 7.82, "share_ge_25_all": 0.0615, "share_ge_25_pregame_clean": 0.0546}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2388, "share_within_10pp_all": 0.4395, "share_within_10pp_pregame_clean": 0.4973, "corr_model_vs_mid_pregame_clean": 0.8448}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 456, "model_brier": 0.1927, "kalshi_brier": 0.1942, "brier_diff_model_minus_kalshi": -0.0015}, "10-15": {"n_settled": 526, "model_brier": 0.2122, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0082}, "15-25": {"n_settled": 650, "model_brier": 0.2309, "kalshi_brier": 0.2171, "brier_diff_model_minus_kalshi": 0.0138}, "25-40": {"n_settled": 350, "model_brier": 0.2248, "kalshi_brier": 0.2088, "brier_diff_model_minus_kalshi": 0.016}, "3-5": {"n_settled": 290, "model_brier": 0.1908, "kalshi_brier": 0.191, "brier_diff_model_minus_kalshi": -0.0003}, "40+": {"n_settled": 72, "model_brier": 0.29, "kalshi_brier": 0.1741, "brier_diff_model_minus_kalshi": 0.116}, "5-10": {"n_settled": 628, "model_brier": 0.1949, "kalshi_brier": 0.1953, "brier_diff_model_minus_kalshi": -0.0004}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.542, "slope": 0.868, "slope_se": 0.047}, "kalshi_slope": {"intercept": 0.236, "slope": 1.125, "slope_se": 0.053}, "n": 2972}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.509, "slope": 0.872, "slope_se": 0.035}, "kalshi_slope": {"intercept": 0.151, "slope": 1.077, "slope_se": 0.039}, "n": 4964}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 316, "model_brier": 0.3315, "kalshi_brier": 0.2334, "brier_diff_model_minus_kalshi": 0.0981, "brier_diff_se": 0.0179, "corr_model_outcome": 0.0012, "corr_kalshi_outcome": 0.2529}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
