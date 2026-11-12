# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-12T18:42Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 90,936): 0-3 13.9%, 3-5 9.5%, 5-10 20.1%, 10-15 15.2%, 15-25 19.2%, 25-40 13.7%, 40+ 8.3%; median gap 11.93 pp.
* **Where the extremes live**: 97.3% of >=25 pp gaps are off the ATP/WTA main tour (ITF 78.4%, Challenger 11.0%, doubles 6.4%). Main tour: ATP 3.7% and WTA 5.9% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 20,073): MARKET_ALREADY_SETTLED_WHEN_PRICED 35.2%, STALE_QUOTE 20.2%, BOOK_QUALITY 16.3%, POOR_DATA 9.0%, POSSIBLY_IN_PLAY_QUOTE 5.9%, IDENTITY_AMBIGUOUS 4.2%, IN_PLAY_QUOTE 3.4%, LIMITED_DATA 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 1.7%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 35.2%, market_freshness 20.2%, execution 16.3%, data 12.3%, market_freshness/coverage 9.3%, mapping 4.2%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 55.7% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 44.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 20,073 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.8%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.9% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 479.0 points vs 1667.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.027, Gen-2 0.824, Gen-1 ledger 0.869 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 1026 model 0.2251 vs Kalshi 0.2038; n 212 model 0.3052 vs Kalshi 0.1675.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA. Not implemented here.

## 1. Observations

* 377,673 model-market comparisons (625,150 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 124,310 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-12T18:23:20.638301+00:00'], shadow board 105,334 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-12T18:23:24.277467+00:00'], Model 4 44,171 rows, 31,253 settled tickers, 11,756 tickers with an external scan.
* By model: {"gen1_ledger": 83099, "gen1_elo": 52931, "fair_v1": 52931, "gen2": 52931, "gen1_sr": 52931, "model4_fundamental": 41467, "model4_conditioned": 41383}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 90,936 | 13.9 | 9.5 | 20.1 | 15.2 | 19.2 | 13.7 | 8.3 | 11.93 | 41.3% | 22.1% |
| MW fair_v1 | 52,931 | 12.6 | 8.6 | 18.7 | 15.2 | 19.6 | 15.0 | 10.3 | 13.2 | 45.0% | 25.4% |
| MW gen1_elo | 52,931 | 12.3 | 8.8 | 19.1 | 15.3 | 19.4 | 15.0 | 10.2 | 13.0 | 44.5% | 25.1% |
| MW gen1_ledger | 38,005 | 15.8 | 10.8 | 22.1 | 15.2 | 18.6 | 11.9 | 5.5 | 10.29 | 36.1% | 17.5% |
| MW gen1_sr | 52,931 | 9.9 | 7.1 | 16.5 | 13.9 | 20.9 | 18.8 | 12.8 | 16.0 | 52.5% | 31.6% |
| MW gen2 | 52,931 | 10.8 | 7.5 | 16.7 | 13.7 | 19.7 | 17.7 | 13.9 | 15.53 | 51.3% | 31.6% |
| all families model4_conditioned | 41,383 | 22.2 | 17.9 | 34.6 | 16.9 | 5.0 | 2.2 | 1.2 | 6.07 | 8.4% | 3.4% |
| all families model4_fundamental | 41,467 | 17.3 | 13.5 | 34.0 | 19.9 | 9.9 | 3.8 | 1.5 | 7.61 | 15.2% | 5.3% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.5%, >=15pp 41.3%, >=20pp 30.5%, >=25pp 22.1%, >=30pp 16.0%, >=40pp 8.3%, >=50pp 3.9%
Executable gap (model outside the book, before fees): median 8.58pp; >=10pp 45.7%, >=25pp 17.6%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,122 | 27.9 | 15.9 | 28.0 | 13.3 | 10.8 | 3.5 | 0.6 | 5.81 | 14.9% | 4.2% |
| CHALLENGER | 8,309 | 16.3 | 9.6 | 20.6 | 15.3 | 15.8 | 11.3 | 11.1 | 10.93 | 38.2% | 22.5% |
| ITF_MEN | 15,559 | 9.6 | 7.3 | 17.1 | 14.8 | 21.1 | 17.2 | 12.8 | 15.45 | 51.1% | 30.0% |
| ITF_WOMEN | 20,506 | 9.3 | 7.0 | 16.1 | 14.7 | 22.2 | 18.7 | 12.0 | 16.03 | 52.9% | 30.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,102 | 16.6 | 13.3 | 24.9 | 20.7 | 16.7 | 6.7 | 1.1 | 8.64 | 24.5% | 7.8% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,122 | 26.3 | 15.7 | 26.3 | 15.8 | 11.3 | 3.9 | 0.8 | 6.1 | 16.0% | 4.7% |
| CHALLENGER | 8,309 | 14.4 | 9.1 | 19.0 | 13.8 | 18.4 | 13.6 | 11.6 | 12.54 | 43.6% | 25.2% |
| ITF_MEN | 15,559 | 8.1 | 6.2 | 15.2 | 13.8 | 20.4 | 19.9 | 16.3 | 17.84 | 56.6% | 36.2% |
| ITF_WOMEN | 20,506 | 7.8 | 5.8 | 14.1 | 12.7 | 20.7 | 21.2 | 17.7 | 19.17 | 59.6% | 38.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,102 | 14.1 | 10.3 | 21.6 | 16.1 | 22.5 | 12.8 | 2.5 | 11.21 | 37.8% | 15.3% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,122 | 23.4 | 14.1 | 25.6 | 15.5 | 14.3 | 5.9 | 1.1 | 7.04 | 21.4% | 7.1% |
| CHALLENGER | 8,309 | 15.1 | 9.6 | 20.8 | 15.6 | 16.1 | 11.9 | 10.9 | 11.2 | 38.9% | 22.9% |
| ITF_MEN | 15,559 | 9.3 | 7.3 | 17.2 | 14.2 | 21.4 | 17.3 | 13.2 | 15.75 | 51.9% | 30.5% |
| ITF_WOMEN | 20,506 | 9.2 | 6.8 | 16.2 | 15.6 | 22.1 | 18.7 | 11.4 | 15.78 | 52.1% | 30.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,102 | 22.5 | 17.2 | 31.8 | 15.3 | 8.9 | 3.3 | 1.0 | 6.12 | 13.2% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,492 | 28.1 | 19.5 | 29.2 | 12.2 | 8.1 | 2.5 | 0.4 | 5.24 | 11.1% | 3.0% |
| CHALLENGER | 5,032 | 22.9 | 14.6 | 27.8 | 14.8 | 13.0 | 5.5 | 1.5 | 7.02 | 20.0% | 7.0% |
| DOUBLES | 2,787 | 4.8 | 4.4 | 12.8 | 11.1 | 20.6 | 24.6 | 21.6 | 23.2 | 66.8% | 46.2% |
| ITF_MEN | 11,263 | 12.8 | 9.5 | 21.4 | 15.7 | 21.6 | 12.9 | 6.0 | 11.8 | 40.5% | 18.9% |
| ITF_WOMEN | 13,201 | 13.4 | 9.3 | 19.9 | 15.7 | 21.7 | 14.6 | 5.4 | 12.18 | 41.7% | 20.0% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,825 | 23.9 | 15.9 | 31.7 | 16.8 | 8.9 | 2.5 | 0.2 | 6.56 | 11.6% | 2.7% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,993 | 28.4 | 16.1 | 28.5 | 13.2 | 10.5 | 3.1 | 0.3 | 5.64 | 13.9% | 3.4% |
| CHALLENGER | 5,843 | 21.1 | 12.0 | 25.7 | 18.1 | 15.8 | 5.6 | 1.8 | 8.22 | 23.2% | 7.4% |
| ITF_MEN | 11,285 | 11.8 | 8.7 | 20.6 | 17.2 | 22.1 | 14.0 | 5.5 | 12.45 | 41.6% | 19.5% |
| ITF_WOMEN | 14,917 | 11.3 | 8.6 | 19.1 | 17.0 | 24.1 | 15.3 | 4.6 | 13.14 | 44.0% | 19.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,988 | 16.9 | 13.3 | 25.3 | 21.1 | 16.7 | 6.2 | 0.6 | 8.45 | 23.5% | 6.8% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,993 | 26.6 | 16.0 | 26.6 | 15.7 | 11.2 | 3.4 | 0.4 | 6.02 | 15.0% | 3.8% |
| CHALLENGER | 5,843 | 18.1 | 11.7 | 23.8 | 16.3 | 19.0 | 9.0 | 2.1 | 8.99 | 30.0% | 11.0% |
| ITF_MEN | 11,287 | 9.6 | 7.3 | 17.8 | 16.0 | 22.3 | 17.9 | 9.0 | 14.74 | 49.3% | 27.0% |
| ITF_WOMEN | 14,919 | 8.9 | 7.0 | 16.1 | 14.2 | 22.5 | 20.6 | 10.7 | 16.52 | 53.8% | 31.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,988 | 14.4 | 10.5 | 21.8 | 16.3 | 22.7 | 12.5 | 1.9 | 11.03 | 37.0% | 14.4% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,422 | 28.3 | 19.7 | 29.2 | 12.3 | 7.8 | 2.3 | 0.3 | 5.21 | 10.4% | 2.6% |
| CHALLENGER | 4,455 | 24.2 | 15.4 | 28.9 | 14.9 | 12.3 | 3.8 | 0.4 | 6.56 | 16.5% | 4.2% |
| DOUBLES | 2,608 | 4.7 | 4.5 | 13.1 | 11.2 | 20.4 | 24.5 | 21.7 | 23.14 | 66.6% | 46.2% |
| ITF_MEN | 9,729 | 13.6 | 10.0 | 22.9 | 16.2 | 21.7 | 11.4 | 4.2 | 10.94 | 37.2% | 15.5% |
| ITF_WOMEN | 11,364 | 14.1 | 9.9 | 20.9 | 16.2 | 21.9 | 13.5 | 3.6 | 11.42 | 38.9% | 17.1% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,762 | 24.3 | 16.4 | 31.7 | 16.8 | 8.8 | 2.0 | 0.1 | 6.43 | 10.9% | 2.0% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,787 | 4.8 | 4.4 | 12.8 | 11.1 | 20.6 | 24.6 | 21.6 | 23.2 | 66.8% | 46.2% |
| singles | 35,218 | 16.6 | 11.4 | 22.9 | 15.5 | 18.4 | 10.9 | 4.3 | 9.76 | 33.7% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 11,447 | 12.7 | 9.0 | 19.3 | 15.0 | 19.6 | 14.4 | 10.0 | 12.95 | 44.0% | 24.4% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 34,441 | 13.0 | 8.6 | 18.9 | 15.0 | 19.2 | 15.0 | 10.3 | 13.02 | 44.5% | 25.3% |
| UNKNOWN | 6,630 | 10.4 | 7.5 | 17.1 | 16.6 | 21.6 | 15.8 | 11.1 | 14.32 | 48.5% | 26.9% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 14,689 | 19.1 | 11.8 | 22.4 | 15.8 | 14.8 | 9.5 | 6.5 | 9.03 | 30.9% | 16.1% |
| B | 6,310 | 13.0 | 8.6 | 19.5 | 15.3 | 19.7 | 12.4 | 11.5 | 12.77 | 43.6% | 23.9% |
| C | 7,508 | 11.9 | 8.5 | 19.4 | 16.0 | 19.2 | 14.6 | 10.4 | 12.98 | 44.1% | 25.0% |
| D | 8,736 | 11.3 | 8.4 | 17.8 | 15.1 | 21.8 | 15.7 | 9.9 | 14.08 | 47.4% | 25.7% |
| F | 15,688 | 7.3 | 5.7 | 15.0 | 14.3 | 23.0 | 21.1 | 13.6 | 18.05 | 57.7% | 34.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,954 | 24.9 | 15.9 | 28.9 | 14.9 | 10.6 | 3.5 | 1.3 | 6.36 | 15.3% | 4.7% |
| B | 5,167 | 16.7 | 11.0 | 24.2 | 17.0 | 18.9 | 9.3 | 2.9 | 9.6 | 31.2% | 12.3% |
| C | 7,494 | 11.0 | 7.8 | 19.5 | 15.0 | 21.0 | 15.6 | 10.1 | 13.48 | 46.7% | 25.7% |
| D | 5,809 | 14.4 | 10.0 | 21.1 | 15.4 | 21.0 | 12.7 | 5.4 | 11.36 | 39.1% | 18.1% |
| F | 9,581 | 10.2 | 8.4 | 16.7 | 14.4 | 23.4 | 18.8 | 8.0 | 15.11 | 50.2% | 26.8% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 16,649 | 17.5 | 10.9 | 21.4 | 15.5 | 15.2 | 10.2 | 9.3 | 10.02 | 34.7% | 19.5% |
| LIMITED | 11,461 | 13.5 | 9.4 | 20.4 | 15.9 | 19.8 | 13.3 | 7.6 | 11.94 | 40.7% | 20.9% |
| POOR | 24,821 | 8.8 | 6.7 | 16.1 | 14.6 | 22.5 | 19.0 | 12.3 | 16.36 | 53.9% | 31.4% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,318 | 23.8 | 18.0 | 33.0 | 15.4 | 6.4 | 3.0 | 0.4 | 5.9 | 9.8% | 3.4% |
| GAME_SPREAD | 6,960 | 22.8 | 15.3 | 32.0 | 16.9 | 9.1 | 3.3 | 0.7 | 6.7 | 13.1% | 4.0% |
| MATCH_WINNER | 38,005 | 15.8 | 10.8 | 22.1 | 15.2 | 18.6 | 11.9 | 5.5 | 10.29 | 36.1% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 17,131 | 28.3 | 16.8 | 30.7 | 12.7 | 8.8 | 2.3 | 0.3 | 5.58 | 11.4% | 2.6% |
| TOTAL_GAMES | 11,661 | 9.7 | 10.8 | 36.3 | 25.7 | 10.4 | 4.2 | 2.9 | 9.14 | 17.5% | 7.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,718 | 24.5 | 28.8 | 33.3 | 8.0 | 4.0 | 1.2 | 0.3 | 4.79 | 5.4% | 1.5% |
| GAME_SPREAD | 9,573 | 46.7 | 15.8 | 25.2 | 7.4 | 2.4 | 1.9 | 0.6 | 3.33 | 4.9% | 2.5% |
| TOTAL_GAMES | 17,092 | 6.5 | 9.8 | 40.9 | 29.8 | 7.3 | 3.3 | 2.4 | 9.15 | 12.9% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,754 | 23.8 | 16.6 | 34.7 | 14.8 | 6.9 | 2.7 | 0.5 | 6.05 | 10.1% | 3.2% |
| GAME_SPREAD | 9,582 | 20.3 | 13.4 | 28.4 | 20.2 | 12.2 | 4.3 | 1.1 | 7.71 | 17.7% | 5.5% |
| TOTAL_GAMES | 17,131 | 10.0 | 10.9 | 36.5 | 24.3 | 11.3 | 4.4 | 2.6 | 9.01 | 18.3% | 7.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 52,931 | 45.0% | 25.4% | 13.2 | 35.5% | 15.2% | 10.72 |
| gen1_elo | 52,931 | 44.5% | 25.1% | 13.0 | 34.9% | 15.0% | 10.51 |
| gen1_sr | 52,931 | 52.5% | 31.6% | 16.0 | 44.0% | 21.5% | 13.0 |
| gen2 | 52,931 | 51.3% | 31.6% | 15.53 | 43.9% | 23.0% | 12.84 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,313 | 15.5 | 10.5 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.72 | 35.4% | 15.3% |
| STALE | 32,618 | 10.7 | 7.4 | 17.0 | 13.9 | 19.3 | 17.0 | 14.6 | 15.39 | 50.9% | 31.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 31,473 | 16.3 | 11.1 | 22.6 | 15.2 | 18.2 | 11.5 | 5.0 | 9.97 | 34.7% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 90,936 | 31473 | 23785 | 35678 | 25.3 | 145.7 | 1451.1 |
| ge_15pp | 37,526 | 10919 | 8483 | 18124 | 29.1 | 449.6 | 1451.1 |
| ge_25pp | 20,073 | 5183 | 3709 | 11181 | 34.8 | 592.5 | 1431.1 |
| lt_10pp | 39,607 | 15757 | 11243 | 12607 | 22.8 | 49.7 | 1421.7 |

Current slate `SL-20261112T184225Z-f54625b4`: 282 priced rows, quote age at build {'median': 19.4, 'max': 19.5}, freshness {'AGING': 282}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 52 | 0.0 | 0.0 | 34.6 | 9.6 | 32.7 | 19.2 | 3.9 | 18.34 | 55.8% | 23.1% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 5,083 | 19.1 | 11.1 | 25.7 | 18.3 | 17.7 | 7.1 | 1.0 | 8.78 | 25.8% | 8.1% |
| KALSHI_LONE_OUTLIER | 32 | 6.2 | 6.2 | 75.0 | 6.2 | 3.1 | 3.1 | 0.0 | 6.16 | 6.2% | 3.1% |
| MARKETS_AGREE | 1,083 | 66.3 | 33.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,313 | 0.0 | 2.2 | 38.4 | 26.0 | 23.7 | 8.8 | 0.9 | 11.66 | 33.4% | 9.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 52,931 | 8592 (16.2%) | 26.9% | 0.9% | {"EXTERNAL_STALE": 5083, "AGREES_WITH_KALSHI": 2313, "ALL_AGREE": 1083, "SUPPORTS_MODEL_DIRECTION": 50, "AGREES_WITH_MODEL": 32, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 23,808 | 2113 (8.9%) | 36.5% | 1.5% | {"EXTERNAL_STALE": 1310, "AGREES_WITH_KALSHI": 772, "SUPPORTS_MODEL_DIRECTION": 29, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 13,428 | 647 (4.8%) | 34.6% | 2.0% | {"EXTERNAL_STALE": 410, "AGREES_WITH_KALSHI": 224, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 6,117 | 615 (10.1%) | 35.3% | 2.1% | {"EXTERNAL_STALE": 385, "AGREES_WITH_KALSHI": 217, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 21,081 | 4939 (23.4%) | 19.0% | 0.9% | {"EXTERNAL_STALE": 2842, "ALL_AGREE": 1083, "AGREES_WITH_KALSHI": 939, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 28, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 10,379 | 10.7 | 7.6 | 18.9 | 14.3 | 21.8 | 16.4 | 10.3 | 14.38 | 48.5% | 26.7% |
| 4-10x | 7,157 | 10.9 | 8.7 | 18.0 | 14.8 | 21.6 | 14.7 | 11.3 | 14.1 | 47.6% | 26.0% |
| <2x | 26,887 | 14.5 | 9.6 | 19.9 | 16.0 | 17.5 | 13.3 | 9.2 | 11.7 | 40.1% | 22.5% |
| >=10x | 8,508 | 10.1 | 6.5 | 15.2 | 14.2 | 21.8 | 18.9 | 13.2 | 16.52 | 54.0% | 32.2% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 13,890 | 12.4 | 8.6 | 19.6 | 16.1 | 19.2 | 13.7 | 10.5 | 12.84 | 43.4% | 24.2% |
| 300-1000 | 11,527 | 11.5 | 8.7 | 17.8 | 15.1 | 20.6 | 16.4 | 9.9 | 13.91 | 46.9% | 26.4% |
| <300 | 16,821 | 8.1 | 5.9 | 15.1 | 14.4 | 22.9 | 20.0 | 13.6 | 17.47 | 56.5% | 33.6% |
| >=3000 | 10,693 | 20.9 | 12.8 | 24.0 | 15.5 | 14.0 | 7.4 | 5.4 | 7.9 | 26.8% | 12.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1632 | 0.5472 | 0.4077 | 0.4755 | +0.072 | -0.068 | 0.0039 ± 0.0038 |
| ratio 4-10x | 1115 | 0.5717 | 0.4275 | 0.4843 | +0.087 | -0.057 | 0.0101 ± 0.0048 |
| ratio <2x | 3979 | 0.5345 | 0.4117 | 0.4308 | +0.104 | -0.019 | 0.0152 ± 0.0023 |
| ratio >=10x | 1381 | 0.5588 | 0.3871 | 0.4323 | +0.127 | -0.045 | 0.0184 ± 0.0048 |
| thinner_sample 1000-3000 | 2230 | 0.5397 | 0.4127 | 0.4413 | +0.098 | -0.029 | 0.0134 ± 0.0031 |
| thinner_sample 300-1000 | 1845 | 0.5595 | 0.4195 | 0.4667 | +0.093 | -0.047 | 0.0064 ± 0.0036 |
| thinner_sample <300 | 2658 | 0.5525 | 0.3853 | 0.4413 | +0.111 | -0.056 | 0.0159 ± 0.0034 |
| thinner_sample >=3000 | 1374 | 0.5275 | 0.4341 | 0.4432 | +0.084 | -0.009 | 0.0143 ± 0.0031 |
| data_status ADEQUATE | 2190 | 0.5312 | 0.4288 | 0.4379 | +0.093 | -0.009 | 0.0154 ± 0.0026 |
| data_status LIMITED | 1972 | 0.5469 | 0.4142 | 0.461 | +0.086 | -0.047 | 0.0082 ± 0.0034 |
| data_status POOR | 3945 | 0.5544 | 0.3951 | 0.4459 | +0.109 | -0.051 | 0.0136 ± 0.0027 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1168 | 0.1961 | 0.1961 | -0.0000 ± 0.0004 | 0.5715 | 0.5717 | 0.5018 | 0.4866 | 0.4932 | -0.098 ± 0.0137 | -0.0087 (8) |
| 3-5 | 749 | 0.2079 | 0.2072 | +0.0007 ± 0.0013 | 0.6013 | 0.5978 | 0.5012 | 0.4613 | 0.4726 | -0.101 ± 0.0171 | 0.01 (3) |
| 5-10 | 1751 | 0.2024 | 0.2006 | +0.0018 ± 0.0016 | 0.5913 | 0.5846 | 0.509 | 0.4351 | 0.4586 | -0.091 ± 0.011 | -0.0143 (7) |
| 10-15 | 1406 | 0.2192 | 0.2093 | +0.0099 ± 0.003 | 0.6302 | 0.6021 | 0.5245 | 0.4011 | 0.4218 | -0.106 ± 0.0124 | -0.055 (6) |
| 15-25 | 1795 | 0.2256 | 0.2061 | +0.0195 ± 0.0042 | 0.6463 | 0.595 | 0.5709 | 0.3764 | 0.4234 | -0.103 ± 0.0108 | -0.0045 (11) |
| 25-40 | 1026 | 0.2251 | 0.2038 | +0.0212 ± 0.0084 | 0.6403 | 0.5882 | 0.6439 | 0.3341 | 0.4542 | -0.065 ± 0.0131 | -0.06 (2) |
| 40+ | 212 | 0.3052 | 0.1675 | +0.1377 ± 0.0255 | 0.8164 | 0.5038 | 0.7246 | 0.2672 | 0.3538 | -0.087 ± 0.0246 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5909 | 0.1869 | 0.1877 | -0.0009 ± 0.0002 | 0.5502 | 0.5512 | 0.4912 | 0.4759 | 0.5075 | -0.021 ± 0.0057 | -0.01 (28) |
| 3-5 | 4006 | 0.1988 | 0.1967 | +0.0020 ± 0.0006 | 0.5783 | 0.5713 | 0.4804 | 0.4406 | 0.4348 | -0.060 ± 0.0071 | 0.005 (6) |
| 5-10 | 8791 | 0.2009 | 0.1966 | +0.0044 ± 0.0007 | 0.5876 | 0.5735 | 0.4822 | 0.4084 | 0.4161 | -0.050 ± 0.0048 | -0.0114 (22) |
| 10-15 | 7143 | 0.2015 | 0.1856 | +0.0160 ± 0.0013 | 0.5896 | 0.5449 | 0.4845 | 0.3606 | 0.3585 | -0.063 ± 0.0051 | -0.0379 (19) |
| 15-25 | 9204 | 0.2059 | 0.1659 | +0.0400 ± 0.0017 | 0.6037 | 0.4938 | 0.4974 | 0.3018 | 0.2982 | -0.069 ± 0.0042 | -0.0043 (51) |
| 25-40 | 7217 | 0.2227 | 0.1238 | +0.0990 ± 0.0026 | 0.6395 | 0.3817 | 0.5236 | 0.2096 | 0.213 | -0.059 ± 0.004 | -0.0733 (3) |
| 40+ | 4950 | 0.38 | 0.0439 | +0.3360 ± 0.0034 | 0.99 | 0.1704 | 0.6281 | 0.1018 | 0.0574 | -0.076 ± 0.0028 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 935 | 0.2014 | 0.2018 | -0.0004 ± 0.0005 | 0.5823 | 0.5836 | 0.5095 | 0.4945 | 0.5209 | -0.094 ± 0.0157 | -0.0117 (6) |
| 3-5 | 675 | 0.2124 | 0.2096 | +0.0028 ± 0.0014 | 0.6085 | 0.6022 | 0.5189 | 0.4793 | 0.4607 | -0.126 ± 0.0189 | 0.01 (3) |
| 5-10 | 1503 | 0.2041 | 0.2024 | +0.0017 ± 0.0018 | 0.5936 | 0.589 | 0.5379 | 0.4635 | 0.4904 | -0.085 ± 0.012 | -0.01 (4) |
| 10-15 | 1313 | 0.2152 | 0.2074 | +0.0078 ± 0.0032 | 0.6232 | 0.6005 | 0.557 | 0.4326 | 0.4661 | -0.102 ± 0.0131 | -0.04 (5) |
| 15-25 | 1888 | 0.2327 | 0.2108 | +0.0218 ± 0.0042 | 0.6619 | 0.6054 | 0.5839 | 0.3883 | 0.4322 | -0.101 ± 0.0108 | -0.0183 (12) |
| 25-40 | 1313 | 0.2662 | 0.2 | +0.0661 ± 0.0077 | 0.7425 | 0.5808 | 0.6588 | 0.3449 | 0.3983 | -0.109 ± 0.0124 | -0.008 (5) |
| 40+ | 480 | 0.3736 | 0.1597 | +0.2139 ± 0.0183 | 1.0152 | 0.4842 | 0.7315 | 0.2427 | 0.2812 | -0.088 ± 0.0176 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5086 | 0.19 | 0.1902 | -0.0002 ± 0.0002 | 0.5549 | 0.5551 | 0.5073 | 0.4922 | 0.5065 | -0.040 ± 0.0063 | -0.0154 (26) |
| 3-5 | 3503 | 0.1941 | 0.1931 | +0.0009 ± 0.0006 | 0.5654 | 0.5626 | 0.5115 | 0.4718 | 0.479 | -0.044 ± 0.0076 | 0.01 (5) |
| 5-10 | 7835 | 0.1953 | 0.192 | +0.0033 ± 0.0007 | 0.5749 | 0.5622 | 0.5062 | 0.432 | 0.449 | -0.039 ± 0.005 | -0.0117 (6) |
| 10-15 | 6507 | 0.2024 | 0.1902 | +0.0122 ± 0.0014 | 0.5944 | 0.5569 | 0.5063 | 0.3824 | 0.396 | -0.050 ± 0.0055 | -0.0189 (18) |
| 15-25 | 9284 | 0.2155 | 0.1787 | +0.0369 ± 0.0017 | 0.6278 | 0.5252 | 0.5231 | 0.3276 | 0.3335 | -0.061 ± 0.0044 | -0.014 (52) |
| 25-40 | 8358 | 0.2502 | 0.1375 | +0.1128 ± 0.0026 | 0.7068 | 0.4197 | 0.5591 | 0.2418 | 0.2263 | -0.077 ± 0.0041 | -0.0095 (20) |
| 40+ | 6647 | 0.4016 | 0.0595 | +0.3421 ± 0.0034 | 1.0581 | 0.2137 | 0.6546 | 0.1191 | 0.0809 | -0.073 ± 0.0029 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1143 | 0.1958 | 0.1968 | -0.0011 ± 0.0005 | 0.5711 | 0.5736 | 0.5006 | 0.4851 | 0.5214 | -0.061 ± 0.0137 | -0.0191 (11) |
| 3-5 | 817 | 0.209 | 0.2075 | +0.0015 ± 0.0013 | 0.6047 | 0.5997 | 0.4981 | 0.4585 | 0.4614 | -0.108 ± 0.0167 | 0.002 (5) |
| 5-10 | 1753 | 0.2025 | 0.198 | +0.0045 ± 0.0016 | 0.5905 | 0.578 | 0.5105 | 0.4367 | 0.4427 | -0.107 ± 0.0109 | -0.01 (10) |
| 10-15 | 1451 | 0.2117 | 0.202 | +0.0097 ± 0.0029 | 0.6137 | 0.586 | 0.5384 | 0.4151 | 0.4397 | -0.105 ± 0.0119 | -0.0286 (7) |
| 15-25 | 1707 | 0.2312 | 0.2116 | +0.0196 ± 0.0043 | 0.6598 | 0.6072 | 0.5796 | 0.3856 | 0.4318 | -0.105 ± 0.0112 | -0.03 (1) |
| 25-40 | 1010 | 0.217 | 0.2067 | +0.0103 ± 0.0085 | 0.6239 | 0.5945 | 0.6519 | 0.342 | 0.4782 | -0.058 ± 0.0132 | -0.0267 (3) |
| 40+ | 226 | 0.3101 | 0.1782 | +0.1318 ± 0.0253 | 0.8355 | 0.5275 | 0.7367 | 0.28 | 0.3761 | -0.079 ± 0.0258 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5727 | 0.1865 | 0.1869 | -0.0005 ± 0.0002 | 0.5489 | 0.5492 | 0.4865 | 0.4711 | 0.4845 | -0.038 ± 0.0058 | -0.0189 (44) |
| 3-5 | 4101 | 0.2048 | 0.203 | +0.0018 ± 0.0006 | 0.5947 | 0.5885 | 0.4816 | 0.4421 | 0.4392 | -0.057 ± 0.0071 | -0.0073 (22) |
| 5-10 | 8911 | 0.1955 | 0.19 | +0.0055 ± 0.0007 | 0.5744 | 0.5572 | 0.485 | 0.4111 | 0.4106 | -0.057 ± 0.0047 | -0.0117 (42) |
| 10-15 | 7164 | 0.1948 | 0.1792 | +0.0156 ± 0.0012 | 0.5748 | 0.5304 | 0.496 | 0.3727 | 0.3713 | -0.063 ± 0.005 | -0.0136 (14) |
| 15-25 | 9240 | 0.2109 | 0.1716 | +0.0393 ± 0.0017 | 0.6153 | 0.5066 | 0.5092 | 0.3145 | 0.3118 | -0.068 ± 0.0043 | -0.0533 (3) |
| 25-40 | 7203 | 0.2169 | 0.1235 | +0.0934 ± 0.0026 | 0.627 | 0.3802 | 0.5252 | 0.2097 | 0.221 | -0.052 ± 0.004 | -0.02 (4) |
| 40+ | 4874 | 0.3883 | 0.048 | +0.3404 ± 0.0035 | 1.0123 | 0.1807 | 0.6368 | 0.1072 | 0.0634 | -0.076 ± 0.003 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1616 | 0.1955 | 0.1951 | +0.0004 ± 0.0004 | 0.5687 | 0.5675 | 0.508 | 0.4929 | 0.4882 | -0.077 ± 0.0112 | -0.0221 (56) |
| 3-5 | 1137 | 0.1881 | 0.1881 | +0.0000 ± 0.001 | 0.5538 | 0.5522 | 0.4986 | 0.4587 | 0.4767 | -0.055 ± 0.0132 | -0.0194 (34) |
| 5-10 | 2310 | 0.1992 | 0.1941 | +0.0051 ± 0.0014 | 0.5877 | 0.5713 | 0.5086 | 0.435 | 0.4381 | -0.077 ± 0.0094 | -0.005 (78) |
| 10-15 | 1594 | 0.215 | 0.202 | +0.0129 ± 0.0028 | 0.6236 | 0.5874 | 0.5445 | 0.4217 | 0.4291 | -0.091 ± 0.0116 | 0.0012 (66) |
| 15-25 | 2081 | 0.2326 | 0.2079 | +0.0247 ± 0.0039 | 0.6637 | 0.5996 | 0.592 | 0.397 | 0.4325 | -0.090 ± 0.0101 | -0.0214 (59) |
| 25-40 | 1215 | 0.2418 | 0.2118 | +0.0299 ± 0.008 | 0.69 | 0.6068 | 0.6881 | 0.3764 | 0.4848 | -0.082 ± 0.0125 | -0.0252 (27) |
| 40+ | 449 | 0.3284 | 0.1972 | +0.1312 ± 0.0201 | 0.9384 | 0.576 | 0.808 | 0.3309 | 0.4477 | -0.093 ± 0.0188 | -0.1137 (8) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5831 | 0.1763 | 0.1763 | +0.0001 ± 0.0002 | 0.5224 | 0.5218 | 0.5096 | 0.4944 | 0.4999 | -0.043 ± 0.0055 | -0.0154 (103) |
| 3-5 | 3997 | 0.1932 | 0.1923 | +0.0009 ± 0.0006 | 0.5646 | 0.5619 | 0.502 | 0.4623 | 0.4706 | -0.041 ± 0.007 | -0.0212 (73) |
| 5-10 | 8164 | 0.1967 | 0.1902 | +0.0065 ± 0.0007 | 0.5806 | 0.5608 | 0.5026 | 0.429 | 0.4227 | -0.061 ± 0.0049 | -0.0084 (134) |
| 10-15 | 5598 | 0.2111 | 0.1941 | +0.0170 ± 0.0015 | 0.6141 | 0.569 | 0.5372 | 0.4144 | 0.4055 | -0.074 ± 0.006 | -0.0057 (111) |
| 15-25 | 6882 | 0.232 | 0.1993 | +0.0327 ± 0.0021 | 0.6669 | 0.5779 | 0.5763 | 0.3809 | 0.3952 | -0.069 ± 0.0054 | -0.026 (108) |
| 25-40 | 4439 | 0.2578 | 0.1906 | +0.0673 ± 0.0041 | 0.7289 | 0.5546 | 0.6401 | 0.3279 | 0.3794 | -0.062 ± 0.0064 | -0.0277 (53) |
| 40+ | 1997 | 0.369 | 0.1592 | +0.2098 ± 0.0092 | 1.0371 | 0.4746 | 0.7406 | 0.241 | 0.2909 | -0.058 ± 0.0085 | -0.054 (15) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 8107 | 1.027 ± 0.031 | 1.091 | 0.1679 | 0.1708 | 0.2156 | 0.2028 |
| gen2 | 8107 | 0.824 ± 0.028 | 1.069 | 0.174 | 0.1711 | 0.233 | 0.2028 |
| gen1_elo | 8107 | 1.011 ± 0.03 | 1.081 | 0.1744 | 0.171 | 0.2147 | 0.2029 |
| gen1_sr | 8107 | 1.01 ± 0.037 | 1.117 | 0.1335 | 0.1726 | 0.2292 | 0.2025 |
| gen1_ledger | 10402 | 0.869 ± 0.023 | 1.067 | 0.1903 | 0.1772 | 0.217 | 0.1998 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 37,526)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 9,122 | 24.3% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 8,778 | 23.4% |
| BOOK_QUALITY | execution | 6,332 | 16.9% |
| POOR_DATA | data | 4,280 | 11.4% |
| LIMITED_DATA | data | 2,242 | 6.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 2,196 | 5.9% |
| IDENTITY_AMBIGUOUS | mapping | 1,534 | 4.1% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,420 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 1,046 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 575 | 1.5% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 24.3%, coverage 23.4%, data 17.4%, execution 16.9%, market_freshness/coverage 8.6%, mapping 4.1%, model_calibration_or_unknown 3.8%, model_calibration 1.5%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 95.0%, LOW_DATA_QUALITY 72.2%, THIN_PLAYER_HISTORY 60.3%, STALE_PLAYER_DATA 52.1%, STALE_KALSHI_QUOTE 48.3%, MODEL_INTERNAL_DISAGREEMENT 41.8%, ASYMMETRIC_SAMPLE_SIZE 33.3%, WIDE_SPREAD 23.4%, MODEL_HIGH_UNCERTAINTY 18.7%, PLAYER_IDENTITY_RISK 15.0%, LEVEL_TRANSFER_RISK 9.3%, LOW_DISPLAYED_LIQUIDITY 8.6%, EVENT_MAPPING_RISK 7.0%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.2%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.7%, POST_SETTLEMENT_OBSERVATION 23.4%, POSSIBLE_IN_PLAY_QUOTE 6.3%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 20,073)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,069 | 35.2% |
| STALE_QUOTE | market_freshness | 4,055 | 20.2% |
| BOOK_QUALITY | execution | 3,266 | 16.3% |
| POOR_DATA | data | 1,812 | 9.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,185 | 5.9% |
| IDENTITY_AMBIGUOUS | mapping | 851 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 688 | 3.4% |
| LIMITED_DATA | data | 660 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 347 | 1.7% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 139 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 35.2%, market_freshness 20.2%, execution 16.3%, data 12.3%, market_freshness/coverage 9.3%, mapping 4.2%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.1%, START_UNVERIFIABLE 97.3%, LOW_DATA_QUALITY 75.2%, THIN_PLAYER_HISTORY 62.4%, STALE_KALSHI_QUOTE 55.7%, STALE_PLAYER_DATA 45.4%, MODEL_INTERNAL_DISAGREEMENT 41.9%, ASYMMETRIC_SAMPLE_SIZE 34.4%, WIDE_SPREAD 22.5%, MODEL_HIGH_UNCERTAINTY 19.3%, PLAYER_IDENTITY_RISK 17.8%, LOW_DISPLAYED_LIQUIDITY 8.5%, EVENT_MAPPING_RISK 8.4%, LEVEL_TRANSFER_RISK 8.2%, MODEL_CALIBRATION_OUTLIER 4.6%, EXTERNAL_MARKET_REJECTION 1.7%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 38.1%, POST_SETTLEMENT_OBSERVATION 35.2%, POSSIBLE_IN_PLAY_QUOTE 6.4%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 16142, "IDENTITY_AMBIGUOUS": 3931}; ticker orientation: {"VERIFIED": 20073}.

Checks: discipline:AMBIGUOUS 1288, discipline:PASS 18785, identity_confidence:AMBIGUOUS 3581, identity_confidence:PASS 16492, level_mapping:NA 1300, level_mapping:PASS 18773, market_pair:AMBIGUOUS 514, market_pair:NA 427, market_pair:PASS 19132, model_complement:NA 389, model_complement:PASS 19684, namesake:AMBIGUOUS 6, namesake:PASS 20067, physical_match_id:NA 6645, physical_match_id:PASS 13428, player_ids:PASS 20073, same_pair_other_event:PASS 20073, ticker_orientation:PASS 20073

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,614 | 3.7% | 3.1% | 1.2% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 24, "market_freshness/coverage": 22} | 5.47 | 0.2224 / 0.2183 (865) | 25.7% | 2.4% | 3.2% | 3.0% |
| CHALLENGER | 13,341 | 16.6% | 6.0% | 11.0% | {"coverage": 1357, "market_freshness": 274, "market_freshness/coverage": 240, "data": 164, "model_calibration_or_unknown": 82, "execution": 41, "model_calibration": 40, "mapping": 17, "possible_market_error": 1} | 7.34 | 0.2213 / 0.2109 (3094) | 41.8% | 13.7% | 4.0% | 22.8% |
| DOUBLES | 2,787 | 46.2% | 46.2% | 6.4% | {"execution": 711, "mapping": 389, "market_freshness": 106, "market_freshness/coverage": 75, "coverage": 7} | 23.14 | 0.2991 / 0.2325 (698) | 8.4% | 0.0% | 100.0% | 6.4% |
| ITF_MEN | 26,822 | 25.3% | 17.7% | 33.9% | {"coverage": 2394, "market_freshness": 1429, "execution": 1045, "data": 996, "market_freshness/coverage": 693, "mapping": 230, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.75 | 0.218 / 0.1978 (5665) | 42.4% | 70.1% | 14.5% | 21.6% |
| ITF_WOMEN | 33,707 | 26.5% | 18.7% | 44.5% | {"coverage": 3232, "market_freshness": 1985, "execution": 1386, "data": 1211, "market_freshness/coverage": 786, "mapping": 209, "model_calibration_or_unknown": 98, "model_calibration": 23} | 12.46 | 0.2029 / 0.1931 (6563) | 43.0% | 57.4% | 10.1% | 22.0% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,927 | 5.9% | 5.0% | 1.5% | {"market_freshness": 111, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.65 | 0.2315 / 0.221 (812) | 30.4% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.5% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 113 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 286 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFMATCH-26NOV12VALRAT-RAT` | ITF_MEN | gen1_ledger | 92% / 4% | +88 | POOR_DATA | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1333.0, ratio 3.64); no external reference |
| 6 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 7 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 8 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 311 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 9 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 773 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 10 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 11 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.5h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 517 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 12 | `KXITFMATCH-26NOV10KOUPOR-POR` | ITF_MEN | fair_v1 | 87% / 2% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.9h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 305 min (STALE); data POOR (grade D, thinner serve sample 1554.0, ratio 1.02); no external reference |
| 13 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 14 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 113 min (STALE); no external reference |
| 17 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 18 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 19 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 20 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 22 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 23 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 24 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 25 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 26 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 27 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 573 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 28 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 29 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 30 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 31 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 32 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 33 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 34 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 35 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 36 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 37 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 38 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 39 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 40 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 41 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 42 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 43 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 44 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 768 min (STALE); no external reference |
| 45 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 46 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 47 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 48 | `KXITFWMATCH-26NOV11CORROJ-ROJ` | ITF_WOMEN | fair_v1 | 87% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade D, thinner serve sample 531.0, ratio 1.04); no external reference |
| 49 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 50 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9734, "by_level_share_of_ge_25pp": {"ATP": 0.0122, "CHALLENGER": 0.1104, "DOUBLES": 0.0642, "ITF_MEN": 0.3387, "ITF_WOMEN": 0.4449, "OTHER": 0.0006, "WTA": 0.0145, "WTA125": 0.0146}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.557, "share_primary_cause_market_settled_or_in_play": 0.4455, "share_primary_cause_stale_quote_only": 0.202}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 20073, "identity_ambiguous_share": 0.1958, "ticker_orientation": {"VERIFIED": 20073}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 13428, "with_external": 647, "coverage": 0.0482, "external_status": {"EXTERNAL_STALE": 410, "AGREES_WITH_KALSHI": 224, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 410, "MODEL_LONE_OUTLIER": 224, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3462, "share_external_supports_model": 0.0201}, "pregame_clean_ge_25pp": {"n": 6117, "with_external": 615, "coverage": 0.1005, "external_status": {"EXTERNAL_STALE": 385, "AGREES_WITH_KALSHI": 217, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 385, "MODEL_LONE_OUTLIER": 217, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3528, "share_external_supports_model": 0.0211}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 479.0, "median_sample_ratio": 2.46, "median_min_matches": 18.0, "median_max_days_since_last": 246.5, "share_severe_asymmetry": 0.2071, "data_status": {"POOR": 11443, "LIMITED": 5030, "ADEQUATE": 3600}, "comparison_lt_10pp": {"median_thinner_serve_points": 1667.0, "median_sample_ratio": 1.71, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1632, "model_minus_observed": 0.0717, "kalshi_minus_observed": -0.0678, "brier_diff_model_minus_kalshi": 0.0039}, "4-10x": {"n": 1115, "model_minus_observed": 0.0874, "kalshi_minus_observed": -0.0568, "brier_diff_model_minus_kalshi": 0.0101}, "<2x": {"n": 3979, "model_minus_observed": 0.1038, "kalshi_minus_observed": -0.019, "brier_diff_model_minus_kalshi": 0.0152}, ">=10x": {"n": 1381, "model_minus_observed": 0.1265, "kalshi_minus_observed": -0.0452, "brier_diff_model_minus_kalshi": 0.0184}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 8107, "model": {"intercept": -0.565, "slope": 0.824, "slope_se": 0.028}, "kalshi_mid_same_rows": {"intercept": 0.168, "slope": 1.069, "slope_se": 0.031}, "mean_extremity_model": 0.174, "mean_extremity_kalshi": 0.1711, "model_brier": 0.233, "kalshi_brier": 0.2028, "brier_diff_model_minus_kalshi": 0.0302, "brier_diff_se": 0.0021, "model_logloss": 0.6633, "kalshi_logloss": 0.5876}, "fair_v1": {"n": 8107, "model": {"intercept": -0.474, "slope": 1.027, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.214, "slope": 1.091, "slope_se": 0.032}, "mean_extremity_model": 0.1679, "mean_extremity_kalshi": 0.1708, "model_brier": 0.2156, "kalshi_brier": 0.2028, "brier_diff_model_minus_kalshi": 0.0128, "brier_diff_se": 0.0017, "model_logloss": 0.6204, "kalshi_logloss": 0.5876}, "gen1_elo": {"n": 8107, "model": {"intercept": -0.464, "slope": 1.011, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.215, "slope": 1.081, "slope_se": 0.031}, "mean_extremity_model": 0.1744, "mean_extremity_kalshi": 0.171, "model_brier": 0.2147, "kalshi_brier": 0.2029, "brier_diff_model_minus_kalshi": 0.0118, "brier_diff_se": 0.0017, "model_logloss": 0.6189, "kalshi_logloss": 0.5878}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2537, "share_ge_15": 0.4498, "median_abs_gap": 13.2, "n": 52931}, "gen1_elo": {"share_ge_25": 0.2514, "share_ge_15": 0.4454, "median_abs_gap": 13.0, "n": 52931}, "gen1_sr": {"share_ge_25": 0.3163, "share_ge_15": 0.5252, "median_abs_gap": 16.0, "n": 52931}, "gen2": {"share_ge_25": 0.3162, "share_ge_15": 0.5133, "median_abs_gap": 15.53, "n": 52931}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1517, "share_ge_15": 0.3551, "median_abs_gap": 10.72, "n": 40310}, "gen1_elo": {"share_ge_25": 0.1501, "share_ge_15": 0.3494, "median_abs_gap": 10.51, "n": 40310}, "gen1_sr": {"share_ge_25": 0.2152, "share_ge_15": 0.4403, "median_abs_gap": 13.0, "n": 40313}, "gen2": {"share_ge_25": 0.2302, "share_ge_15": 0.4392, "median_abs_gap": 12.84, "n": 40314}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.47, "share_ge_25_all": 0.037, "share_ge_25_pregame_clean": 0.031}, "WTA": {"median_abs_gap_pregame_clean": 7.65, "share_ge_25_all": 0.0591, "share_ge_25_pregame_clean": 0.0501}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2342, "share_within_10pp_all": 0.4355, "share_within_10pp_pregame_clean": 0.4902, "corr_model_vs_mid_pregame_clean": 0.8499}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1168, "model_brier": 0.1961, "kalshi_brier": 0.1961, "brier_diff_model_minus_kalshi": -0.0}, "10-15": {"n_settled": 1406, "model_brier": 0.2192, "kalshi_brier": 0.2093, "brier_diff_model_minus_kalshi": 0.0099}, "15-25": {"n_settled": 1795, "model_brier": 0.2256, "kalshi_brier": 0.2061, "brier_diff_model_minus_kalshi": 0.0195}, "25-40": {"n_settled": 1026, "model_brier": 0.2251, "kalshi_brier": 0.2038, "brier_diff_model_minus_kalshi": 0.0212}, "3-5": {"n_settled": 749, "model_brier": 0.2079, "kalshi_brier": 0.2072, "brier_diff_model_minus_kalshi": 0.0007}, "40+": {"n_settled": 212, "model_brier": 0.3052, "kalshi_brier": 0.1675, "brier_diff_model_minus_kalshi": 0.1377}, "5-10": {"n_settled": 1751, "model_brier": 0.2024, "kalshi_brier": 0.2006, "brier_diff_model_minus_kalshi": 0.0018}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'NO_SKILL:gen2|WTA', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.565, "slope": 0.824, "slope_se": 0.028}, "kalshi_slope": {"intercept": 0.168, "slope": 1.069, "slope_se": 0.031}, "n": 8107}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.504, "slope": 0.869, "slope_se": 0.023}, "kalshi_slope": {"intercept": 0.15, "slope": 1.067, "slope_se": 0.027}, "n": 10402}, "NO_SKILL:gen2|WTA": {"n_settled": 346, "model_brier": 0.25, "kalshi_brier": 0.2262, "brier_diff_model_minus_kalshi": 0.0238, "brier_diff_se": 0.0089, "corr_model_outcome": 0.2572, "corr_kalshi_outcome": 0.3102}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 698, "model_brier": 0.2991, "kalshi_brier": 0.2325, "brier_diff_model_minus_kalshi": 0.0665, "brier_diff_se": 0.0111, "corr_model_outcome": 0.1068, "corr_kalshi_outcome": 0.2752}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
