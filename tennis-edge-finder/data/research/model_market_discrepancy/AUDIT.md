# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-09T23:05Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 26,901): 0-3 14.3%, 3-5 9.6%, 5-10 19.9%, 10-15 15.5%, 15-25 18.5%, 25-40 13.8%, 40+ 8.4%; median gap 11.9 pp.
* **Where the extremes live**: 98.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.9%, Challenger 12.0%, doubles 7.0%). Main tour: ATP 1.6% and WTA 7.8% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 5,986): MARKET_ALREADY_SETTLED_WHEN_PRICED 39.8%, STALE_QUOTE 16.7%, BOOK_QUALITY 16.6%, POOR_DATA 7.9%, POSSIBLY_IN_PLAY_QUOTE 5.5%, LIMITED_DATA 4.3%, IDENTITY_AMBIGUOUS 3.6%, IN_PLAY_QUOTE 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.2%. By class: coverage 39.8%, market_freshness 16.7%, execution 16.6%, data 12.2%, market_freshness/coverage 8.9%, mapping 3.6%, model_calibration_or_unknown 1.9%, model_calibration 0.2%.
* **Stale / settled / in-play**: 55.5% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 48.8% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 5,986 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 17.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 2.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 16.4% of the time and with the model 0.3%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 638.0 points vs 1841.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.06, Gen-2 0.855, Gen-1 ledger 0.9 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 252 model 0.2211 vs Kalshi 0.2018; n 55 model 0.2888 vs Kalshi 0.1716.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 104,548 model-market comparisons (173,264 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 39,419 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-09T22:59:11.000965+00:00'], shadow board 28,182 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-09T22:59:14.690318+00:00'], Model 4 11,298 rows, 11,707 settled tickers, 3,222 tickers with an external scan.
* By model: {"gen1_ledger": 25609, "gen1_elo": 14160, "fair_v1": 14160, "gen2": 14160, "gen1_sr": 14160, "model4_fundamental": 11154, "model4_conditioned": 11145}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 26,901 | 14.3 | 9.6 | 19.9 | 15.5 | 18.5 | 13.8 | 8.4 | 11.9 | 40.7% | 22.2% |
| MW fair_v1 | 14,160 | 13.6 | 8.6 | 18.3 | 16.3 | 18.3 | 14.8 | 10.1 | 12.89 | 43.2% | 24.9% |
| MW gen1_elo | 14,160 | 13.1 | 8.9 | 20.1 | 14.9 | 18.9 | 14.5 | 9.5 | 12.43 | 43.0% | 24.1% |
| MW gen1_ledger | 12,741 | 15.1 | 10.7 | 21.7 | 14.6 | 18.6 | 12.8 | 6.5 | 10.72 | 38.0% | 19.4% |
| MW gen1_sr | 14,160 | 10.2 | 7.9 | 16.2 | 14.2 | 21.4 | 18.3 | 11.8 | 15.51 | 51.5% | 30.1% |
| MW gen2 | 14,160 | 12.2 | 7.2 | 16.1 | 14.3 | 19.8 | 17.2 | 13.2 | 15.14 | 50.2% | 30.5% |
| all families model4_conditioned | 11,145 | 22.2 | 20.3 | 36.0 | 15.7 | 4.1 | 0.8 | 0.8 | 5.7 | 5.8% | 1.7% |
| all families model4_fundamental | 11,154 | 16.8 | 13.3 | 35.7 | 19.8 | 10.7 | 2.5 | 1.1 | 7.58 | 14.3% | 3.7% |

Configurable thresholds (primary): >=5pp 76.1%, >=10pp 56.2%, >=15pp 40.7%, >=20pp 30.5%, >=25pp 22.2%, >=30pp 16.3%, >=40pp 8.4%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.52pp; >=10pp 45.6%, >=25pp 18.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,118 | 29.5 | 14.5 | 24.8 | 17.4 | 11.5 | 1.2 | 1.0 | 5.93 | 13.8% | 2.2% |
| CHALLENGER | 2,343 | 15.7 | 10.8 | 18.6 | 16.3 | 12.8 | 13.0 | 12.8 | 11.84 | 38.7% | 25.9% |
| ITF_MEN | 4,078 | 11.5 | 8.7 | 18.4 | 15.1 | 19.1 | 15.1 | 12.2 | 13.66 | 46.4% | 27.2% |
| ITF_WOMEN | 5,688 | 10.3 | 6.6 | 15.8 | 16.4 | 21.7 | 18.7 | 10.6 | 15.43 | 51.0% | 29.3% |
| WTA | 587 | 23.3 | 10.1 | 25.6 | 16.4 | 16.4 | 6.5 | 1.9 | 7.85 | 24.7% | 8.3% |
| WTA125 | 346 | 11.6 | 6.1 | 22.2 | 25.7 | 16.2 | 15.9 | 2.3 | 11.47 | 34.4% | 18.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,118 | 24.1 | 13.7 | 24.7 | 18.5 | 15.7 | 2.1 | 1.2 | 6.9 | 19.0% | 3.2% |
| CHALLENGER | 2,343 | 15.3 | 7.4 | 18.1 | 13.4 | 18.1 | 14.3 | 13.4 | 13.12 | 45.7% | 27.6% |
| ITF_MEN | 4,078 | 10.5 | 7.5 | 16.9 | 15.0 | 19.9 | 17.4 | 12.8 | 15.21 | 50.1% | 30.3% |
| ITF_WOMEN | 5,688 | 9.1 | 6.0 | 12.8 | 12.9 | 20.9 | 21.2 | 17.2 | 19.08 | 59.3% | 38.4% |
| WTA | 587 | 22.0 | 5.6 | 18.7 | 15.2 | 20.9 | 15.7 | 1.9 | 11.75 | 38.5% | 17.5% |
| WTA125 | 346 | 4.3 | 2.9 | 17.6 | 20.5 | 22.5 | 21.1 | 11.0 | 17.24 | 54.6% | 32.1% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,118 | 26.6 | 13.9 | 28.8 | 15.4 | 11.3 | 2.9 | 1.1 | 6.47 | 15.2% | 3.9% |
| CHALLENGER | 2,343 | 15.8 | 10.6 | 20.3 | 14.5 | 13.9 | 12.2 | 12.7 | 10.84 | 38.8% | 24.9% |
| ITF_MEN | 4,078 | 10.4 | 8.8 | 19.2 | 13.8 | 20.1 | 15.4 | 12.2 | 13.95 | 47.7% | 27.7% |
| ITF_WOMEN | 5,688 | 9.7 | 6.7 | 16.7 | 15.6 | 23.0 | 18.9 | 9.4 | 15.57 | 51.3% | 28.2% |
| WTA | 587 | 23.2 | 13.3 | 35.4 | 14.7 | 9.0 | 3.2 | 1.2 | 6.68 | 13.5% | 4.4% |
| WTA125 | 346 | 22.0 | 11.6 | 31.2 | 16.5 | 13.6 | 4.6 | 0.6 | 7.99 | 18.8% | 5.2% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 613 | 29.9 | 23.6 | 35.2 | 9.5 | 1.5 | 0.3 | 0.0 | 4.72 | 1.8% | 0.3% |
| CHALLENGER | 1,524 | 23.6 | 17.5 | 26.1 | 13.7 | 11.9 | 5.4 | 2.0 | 6.47 | 19.2% | 7.3% |
| DOUBLES | 825 | 4.0 | 3.3 | 10.6 | 11.6 | 19.4 | 24.5 | 26.7 | 25.63 | 70.5% | 51.1% |
| ITF_MEN | 3,955 | 14.9 | 8.5 | 21.2 | 15.2 | 20.3 | 12.3 | 7.6 | 11.73 | 40.2% | 19.9% |
| ITF_WOMEN | 4,676 | 11.5 | 9.3 | 19.9 | 14.6 | 22.4 | 16.6 | 5.6 | 12.98 | 44.6% | 22.2% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 483 | 21.5 | 12.4 | 26.1 | 18.0 | 14.7 | 6.6 | 0.6 | 8.26 | 21.9% | 7.2% |
| WTA125 | 516 | 16.7 | 13.4 | 22.5 | 20.2 | 16.1 | 8.5 | 2.7 | 9.18 | 27.3% | 11.2% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,109 | 29.5 | 14.3 | 24.9 | 17.5 | 11.5 | 1.3 | 1.0 | 5.94 | 13.8% | 2.2% |
| CHALLENGER | 1,646 | 20.7 | 14.0 | 23.8 | 19.3 | 13.1 | 6.4 | 2.7 | 7.97 | 22.2% | 9.2% |
| ITF_MEN | 2,887 | 14.4 | 10.9 | 22.0 | 16.8 | 19.0 | 11.9 | 5.1 | 10.73 | 35.9% | 16.9% |
| ITF_WOMEN | 4,027 | 12.8 | 8.3 | 18.6 | 19.0 | 23.3 | 14.7 | 3.2 | 12.62 | 41.2% | 17.9% |
| WTA | 584 | 23.3 | 10.1 | 25.7 | 16.3 | 16.4 | 6.3 | 1.9 | 7.81 | 24.7% | 8.2% |
| WTA125 | 333 | 12.0 | 6.3 | 21.6 | 26.1 | 16.5 | 15.9 | 1.5 | 11.47 | 33.9% | 17.4% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,109 | 24.1 | 13.7 | 24.7 | 18.5 | 15.8 | 2.1 | 1.2 | 6.9 | 19.0% | 3.2% |
| CHALLENGER | 1,646 | 20.2 | 9.8 | 23.0 | 16.3 | 18.6 | 9.4 | 2.6 | 9.08 | 30.6% | 12.0% |
| ITF_MEN | 2,888 | 12.6 | 9.2 | 19.6 | 16.8 | 21.4 | 14.7 | 5.8 | 12.44 | 41.9% | 20.6% |
| ITF_WOMEN | 4,027 | 10.7 | 7.2 | 14.4 | 14.1 | 23.4 | 20.1 | 10.1 | 16.26 | 53.5% | 30.1% |
| WTA | 584 | 21.9 | 5.7 | 18.8 | 15.2 | 20.9 | 15.6 | 1.9 | 11.74 | 38.4% | 17.5% |
| WTA125 | 333 | 4.5 | 3.0 | 17.7 | 21.3 | 21.9 | 21.6 | 9.9 | 16.84 | 53.4% | 31.5% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 593 | 29.9 | 23.9 | 35.6 | 9.6 | 0.7 | 0.3 | 0.0 | 4.69 | 1.0% | 0.3% |
| CHALLENGER | 1,290 | 25.7 | 19.8 | 28.3 | 13.3 | 10.9 | 2.0 | 0.1 | 5.76 | 13.0% | 2.1% |
| DOUBLES | 761 | 3.9 | 3.3 | 10.8 | 11.7 | 19.6 | 24.2 | 26.5 | 25.57 | 70.3% | 50.7% |
| ITF_MEN | 3,182 | 16.6 | 9.5 | 23.4 | 16.2 | 20.1 | 9.9 | 4.4 | 10.06 | 34.3% | 14.2% |
| ITF_WOMEN | 3,808 | 12.8 | 10.1 | 21.8 | 15.5 | 22.7 | 14.8 | 2.3 | 11.44 | 39.9% | 17.2% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 453 | 22.1 | 13.0 | 26.7 | 18.1 | 15.0 | 5.1 | 0.0 | 7.98 | 20.1% | 5.1% |
| WTA125 | 431 | 18.6 | 14.8 | 24.8 | 23.0 | 14.2 | 4.4 | 0.2 | 8.14 | 18.8% | 4.6% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 825 | 4.0 | 3.3 | 10.6 | 11.6 | 19.4 | 24.5 | 26.7 | 25.63 | 70.5% | 51.1% |
| singles | 11,916 | 15.8 | 11.2 | 22.4 | 14.8 | 18.6 | 12.0 | 5.2 | 10.12 | 35.8% | 17.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 3,251 | 13.6 | 9.6 | 20.1 | 16.0 | 16.1 | 14.2 | 10.4 | 12.15 | 40.7% | 24.6% |
| Hard | 9,504 | 13.9 | 8.4 | 18.1 | 16.1 | 18.8 | 14.7 | 10.0 | 12.93 | 43.5% | 24.6% |
| UNKNOWN | 1,405 | 11.5 | 8.3 | 15.2 | 18.1 | 20.0 | 16.8 | 10.1 | 14.04 | 46.9% | 26.9% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,205 | 19.9 | 10.5 | 20.5 | 17.4 | 14.5 | 9.3 | 7.8 | 9.7 | 31.7% | 17.2% |
| B | 1,905 | 15.1 | 9.5 | 19.2 | 17.2 | 16.6 | 12.3 | 10.1 | 11.4 | 39.0% | 22.4% |
| C | 2,181 | 12.4 | 9.8 | 19.4 | 15.3 | 18.7 | 14.9 | 9.5 | 12.72 | 43.0% | 24.4% |
| D | 2,659 | 10.8 | 8.4 | 17.3 | 16.4 | 22.1 | 15.0 | 10.0 | 14.02 | 47.1% | 25.1% |
| F | 3,210 | 7.7 | 5.1 | 14.8 | 14.9 | 21.0 | 23.0 | 13.6 | 18.41 | 57.5% | 36.5% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,604 | 22.3 | 16.0 | 28.0 | 15.2 | 11.7 | 4.9 | 1.8 | 6.84 | 18.4% | 6.7% |
| B | 1,998 | 14.7 | 9.8 | 24.4 | 16.1 | 18.9 | 11.6 | 4.5 | 10.34 | 35.0% | 16.1% |
| C | 2,621 | 11.8 | 7.8 | 18.0 | 14.5 | 20.7 | 15.7 | 11.6 | 14.01 | 48.0% | 27.2% |
| D | 2,094 | 14.0 | 9.3 | 21.3 | 13.2 | 22.0 | 14.0 | 6.2 | 12.04 | 42.2% | 20.2% |
| F | 2,424 | 9.1 | 7.8 | 14.3 | 13.7 | 23.6 | 21.5 | 10.1 | 16.92 | 55.2% | 31.6% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 4,732 | 18.4 | 9.7 | 19.6 | 17.2 | 14.8 | 10.2 | 10.0 | 10.59 | 35.0% | 20.2% |
| LIMITED | 3,518 | 14.7 | 10.5 | 20.4 | 16.2 | 17.7 | 13.3 | 7.2 | 11.32 | 38.2% | 20.5% |
| POOR | 5,910 | 9.1 | 6.7 | 15.9 | 15.6 | 21.5 | 19.3 | 11.9 | 16.05 | 52.7% | 31.2% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,540 | 30.2 | 24.8 | 36.9 | 5.5 | 1.9 | 0.6 | 0.1 | 4.56 | 2.6% | 0.7% |
| GAME_SPREAD | 2,423 | 24.9 | 15.7 | 36.9 | 17.5 | 4.7 | 0.2 | 0.2 | 6.14 | 5.1% | 0.4% |
| MATCH_WINNER | 12,741 | 15.1 | 10.7 | 21.7 | 14.6 | 18.6 | 12.8 | 6.5 | 10.72 | 38.0% | 19.4% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 4,382 | 32.3 | 19.7 | 30.5 | 9.9 | 6.1 | 1.3 | 0.3 | 4.82 | 7.6% | 1.6% |
| TOTAL_GAMES | 3,499 | 7.1 | 9.2 | 38.5 | 30.4 | 9.7 | 2.7 | 2.3 | 9.45 | 14.8% | 5.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,123 | 25.0 | 37.9 | 31.7 | 0.2 | 4.6 | 0.5 | 0.1 | 4.33 | 5.2% | 0.7% |
| GAME_SPREAD | 2,893 | 45.1 | 14.8 | 29.8 | 8.0 | 1.2 | 0.8 | 0.3 | 3.59 | 2.3% | 1.0% |
| TOTAL_GAMES | 4,129 | 3.4 | 6.5 | 44.7 | 36.6 | 5.7 | 1.2 | 2.0 | 9.56 | 8.8% | 3.1% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,123 | 25.6 | 18.5 | 36.6 | 9.7 | 6.9 | 2.5 | 0.4 | 5.59 | 9.7% | 2.8% |
| GAME_SPREAD | 2,893 | 18.9 | 13.1 | 29.0 | 21.4 | 14.3 | 2.6 | 0.7 | 7.97 | 17.6% | 3.3% |
| TOTAL_GAMES | 4,138 | 6.5 | 8.3 | 39.6 | 28.8 | 11.9 | 2.6 | 2.2 | 9.51 | 16.8% | 4.9% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 14,160 | 43.2% | 24.9% | 12.89 | 32.8% | 14.1% | 10.29 |
| gen1_elo | 14,160 | 43.0% | 24.1% | 12.43 | 32.3% | 13.7% | 9.67 |
| gen1_sr | 14,160 | 51.5% | 30.1% | 15.51 | 42.2% | 19.5% | 12.61 |
| gen2 | 14,160 | 50.2% | 30.5% | 15.14 | 42.3% | 21.2% | 12.51 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 7,221 | 16.7 | 11.0 | 21.4 | 17.8 | 18.4 | 11.4 | 3.4 | 10.28 | 33.2% | 14.8% |
| STALE | 6,939 | 10.4 | 6.2 | 15.1 | 14.7 | 18.2 | 18.3 | 17.1 | 17.02 | 53.5% | 35.4% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 6,209 | 17.1 | 11.8 | 23.7 | 14.4 | 16.7 | 11.4 | 4.8 | 9.32 | 32.9% | 16.2% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 26,901 | 6209 | 10693 | 9999 | 24.9 | 165.2 | 1400.4 |
| ge_15pp | 10,957 | 2044 | 3687 | 5226 | 28.7 | 459.9 | 1380.4 |
| ge_25pp | 5,986 | 1005 | 1657 | 3324 | 37.8 | 582.4 | 1380.4 |
| lt_10pp | 11,780 | 3271 | 5172 | 3337 | 23.2 | 49.5 | 1341.5 |

Current slate `SL-20261009T230457Z-02c10727`: 565 priced rows, quote age at build {'median': 6.1, 'max': 6.1}, freshness {'FRESH': 565}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 4 | 0.0 | 0.0 | 25.0 | 0.0 | 75.0 | 0.0 | 0.0 | 20.45 | 75.0% | 0.0% |
| EXTERNAL_LONE_OUTLIER | 4 | 25.0 | 75.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 3.22 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 843 | 23.6 | 11.4 | 21.9 | 20.4 | 15.4 | 6.9 | 0.4 | 8.01 | 22.7% | 7.2% |
| MARKETS_AGREE | 120 | 77.5 | 22.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.65 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 190 | 0.0 | 3.7 | 33.7 | 35.3 | 18.4 | 8.4 | 0.5 | 11.66 | 27.4% | 8.9% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 14,160 | 1161 (8.2%) | 16.4% | 0.3% | {"EXTERNAL_STALE": 843, "AGREES_WITH_KALSHI": 190, "ALL_AGREE": 120, "EXTERNAL_OUTLIER": 4, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 6,114 | 246 (4.0%) | 21.1% | 1.2% | {"EXTERNAL_STALE": 191, "AGREES_WITH_KALSHI": 52, "SUPPORTS_MODEL_DIRECTION": 3} |
| fair_v1_ge_25pp | 3,519 | 78 (2.2%) | 21.8% | 0.0% | {"EXTERNAL_STALE": 61, "AGREES_WITH_KALSHI": 17} |
| fair_v1_ge_25pp_pregame_clean | 1,492 | 76 (5.1%) | 22.4% | 0.0% | {"EXTERNAL_STALE": 59, "AGREES_WITH_KALSHI": 17} |
| fair_v1_lt_10pp | 5,740 | 676 (11.8%) | 10.5% | 0.0% | {"EXTERNAL_STALE": 480, "ALL_AGREE": 120, "AGREES_WITH_KALSHI": 71, "EXTERNAL_OUTLIER": 4, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 2,875 | 11.7 | 8.3 | 19.7 | 15.4 | 20.7 | 13.8 | 10.3 | 13.06 | 44.8% | 24.2% |
| 4-10x | 1,988 | 11.2 | 9.2 | 18.3 | 15.4 | 20.1 | 16.4 | 9.3 | 13.57 | 45.9% | 25.8% |
| <2x | 7,537 | 15.6 | 9.2 | 18.4 | 17.3 | 16.6 | 13.3 | 9.7 | 11.96 | 39.5% | 22.9% |
| >=10x | 1,760 | 10.8 | 6.4 | 15.6 | 14.3 | 19.9 | 20.6 | 12.4 | 16.48 | 53.0% | 33.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 3,710 | 14.2 | 8.5 | 19.0 | 15.9 | 18.1 | 13.2 | 11.1 | 12.48 | 42.4% | 24.3% |
| 300-1000 | 3,486 | 11.8 | 9.1 | 16.6 | 16.4 | 20.9 | 16.0 | 9.3 | 13.75 | 46.2% | 25.3% |
| <300 | 3,699 | 8.2 | 6.0 | 15.7 | 15.0 | 21.0 | 21.0 | 13.1 | 17.18 | 55.1% | 34.1% |
| >=3000 | 3,265 | 21.1 | 11.4 | 22.1 | 18.1 | 12.8 | 8.1 | 6.5 | 8.73 | 27.3% | 14.5% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 456 | 0.5392 | 0.4068 | 0.4781 | +0.061 | -0.071 | 0.0039 ± 0.0069 |
| ratio 4-10x | 318 | 0.5804 | 0.4392 | 0.522 | +0.058 | -0.083 | -0.0013 ± 0.0087 |
| ratio <2x | 1006 | 0.54 | 0.4166 | 0.4493 | +0.091 | -0.033 | 0.0135 ± 0.0045 |
| ratio >=10x | 299 | 0.55 | 0.3805 | 0.4381 | +0.112 | -0.058 | 0.0163 ± 0.0102 |
| thinner_sample 1000-3000 | 572 | 0.5429 | 0.418 | 0.4615 | +0.081 | -0.043 | 0.008 ± 0.006 |
| thinner_sample 300-1000 | 567 | 0.5671 | 0.4264 | 0.4938 | +0.073 | -0.068 | 0.0025 ± 0.0066 |
| thinner_sample <300 | 607 | 0.5439 | 0.3836 | 0.4596 | +0.084 | -0.076 | 0.0111 ± 0.0069 |
| thinner_sample >=3000 | 333 | 0.5282 | 0.4335 | 0.4324 | +0.096 | +0.001 | 0.0215 ± 0.0062 |
| data_status ADEQUATE | 554 | 0.5293 | 0.4262 | 0.435 | +0.094 | -0.009 | 0.0152 ± 0.0052 |
| data_status LIMITED | 557 | 0.5577 | 0.425 | 0.4847 | +0.073 | -0.060 | 0.004 ± 0.0064 |
| data_status POOR | 968 | 0.552 | 0.3979 | 0.4711 | +0.081 | -0.073 | 0.0095 ± 0.0053 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 318 | 0.1932 | 0.1944 | -0.0011 ± 0.0009 | 0.5642 | 0.5671 | 0.4917 | 0.4772 | 0.5157 | -0.064 ± 0.0258 | -0.01 (3) |
| 3-5 | 213 | 0.1879 | 0.1893 | -0.0015 ± 0.0024 | 0.5556 | 0.5571 | 0.5093 | 0.4695 | 0.507 | -0.056 ± 0.0302 | 0.02 (1) |
| 5-10 | 421 | 0.2009 | 0.2028 | -0.0018 ± 0.0033 | 0.5881 | 0.5923 | 0.5226 | 0.4485 | 0.4893 | -0.083 ± 0.0229 | -0.0125 (4) |
| 10-15 | 377 | 0.2142 | 0.2066 | +0.0076 ± 0.0059 | 0.6161 | 0.5946 | 0.517 | 0.3932 | 0.4218 | -0.096 ± 0.0234 | -0.0633 (3) |
| 15-25 | 443 | 0.2273 | 0.2112 | +0.0161 ± 0.0086 | 0.6498 | 0.6097 | 0.5734 | 0.3775 | 0.4334 | -0.091 ± 0.0218 | -0.0133 (6) |
| 25-40 | 252 | 0.2211 | 0.2018 | +0.0193 ± 0.0168 | 0.6321 | 0.5793 | 0.6468 | 0.3382 | 0.4603 | -0.073 ± 0.0252 | -0.01 (1) |
| 40+ | 55 | 0.2888 | 0.1716 | +0.1171 ± 0.0497 | 0.7822 | 0.5171 | 0.752 | 0.305 | 0.4 | -0.128 ± 0.0484 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1595 | 0.1731 | 0.1741 | -0.0010 ± 0.0004 | 0.5171 | 0.5184 | 0.475 | 0.4604 | 0.5003 | -0.019 ± 0.0106 | -0.0188 (8) |
| 3-5 | 1017 | 0.1924 | 0.1893 | +0.0031 ± 0.0011 | 0.5661 | 0.5535 | 0.4786 | 0.439 | 0.4169 | -0.081 ± 0.0139 | 0.02 (1) |
| 5-10 | 2155 | 0.1965 | 0.1941 | +0.0025 ± 0.0014 | 0.5764 | 0.5686 | 0.4902 | 0.4165 | 0.4329 | -0.053 ± 0.0096 | -0.0082 (17) |
| 10-15 | 1981 | 0.2008 | 0.1827 | +0.0182 ± 0.0024 | 0.587 | 0.5364 | 0.471 | 0.3465 | 0.3362 | -0.078 ± 0.0096 | -0.0475 (4) |
| 15-25 | 2290 | 0.2042 | 0.1642 | +0.0400 ± 0.0033 | 0.6006 | 0.4895 | 0.4922 | 0.2958 | 0.293 | -0.077 ± 0.0084 | -0.0048 (29) |
| 25-40 | 1920 | 0.2181 | 0.1229 | +0.0952 ± 0.005 | 0.6288 | 0.3805 | 0.5262 | 0.2125 | 0.2203 | -0.061 ± 0.0077 | -0.01 (1) |
| 40+ | 1317 | 0.3714 | 0.0442 | +0.3272 ± 0.0064 | 0.9681 | 0.1749 | 0.6223 | 0.1056 | 0.0577 | -0.083 ± 0.0055 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 246 | 0.199 | 0.1992 | -0.0003 ± 0.001 | 0.5814 | 0.5826 | 0.4933 | 0.4783 | 0.4837 | -0.095 ± 0.03 | -0.01 (1) |
| 3-5 | 164 | 0.2099 | 0.2108 | -0.0009 ± 0.0029 | 0.6011 | 0.6055 | 0.5265 | 0.4865 | 0.5122 | -0.059 ± 0.0376 | 0.02 (1) |
| 5-10 | 360 | 0.1935 | 0.1907 | +0.0028 ± 0.0035 | 0.569 | 0.5627 | 0.5661 | 0.4913 | 0.5083 | -0.092 ± 0.0238 | -0.01 (4) |
| 10-15 | 351 | 0.2175 | 0.2089 | +0.0086 ± 0.0062 | 0.6223 | 0.6041 | 0.5789 | 0.454 | 0.4872 | -0.101 ± 0.0253 | -0.05 (4) |
| 15-25 | 501 | 0.2262 | 0.2057 | +0.0205 ± 0.008 | 0.6412 | 0.5935 | 0.5955 | 0.3983 | 0.4511 | -0.096 ± 0.0207 | -0.01 (5) |
| 25-40 | 334 | 0.2761 | 0.2014 | +0.0747 ± 0.0155 | 0.7744 | 0.5828 | 0.6724 | 0.3583 | 0.3982 | -0.139 ± 0.0245 | -0.025 (2) |
| 40+ | 123 | 0.341 | 0.1909 | +0.1501 ± 0.0381 | 0.9583 | 0.5575 | 0.7617 | 0.2833 | 0.3821 | -0.059 ± 0.0368 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1418 | 0.1794 | 0.18 | -0.0006 ± 0.0004 | 0.5322 | 0.5339 | 0.494 | 0.4797 | 0.5078 | -0.028 ± 0.0117 | -0.0217 (6) |
| 3-5 | 870 | 0.1933 | 0.1919 | +0.0014 ± 0.0012 | 0.5608 | 0.558 | 0.5251 | 0.4852 | 0.4874 | -0.050 ± 0.0151 | 0.02 (1) |
| 5-10 | 1910 | 0.1859 | 0.1822 | +0.0036 ± 0.0014 | 0.5531 | 0.5404 | 0.5171 | 0.4439 | 0.4597 | -0.049 ± 0.0099 | -0.01 (5) |
| 10-15 | 1711 | 0.1977 | 0.1823 | +0.0154 ± 0.0026 | 0.5823 | 0.5334 | 0.5179 | 0.3933 | 0.3974 | -0.069 ± 0.0105 | -0.02 (14) |
| 15-25 | 2422 | 0.2155 | 0.1726 | +0.0429 ± 0.0033 | 0.6266 | 0.5115 | 0.5285 | 0.333 | 0.3249 | -0.084 ± 0.0085 | -0.0026 (27) |
| 25-40 | 2209 | 0.2513 | 0.1371 | +0.1142 ± 0.005 | 0.714 | 0.4179 | 0.5623 | 0.2458 | 0.225 | -0.092 ± 0.0079 | -0.015 (6) |
| 40+ | 1735 | 0.4029 | 0.068 | +0.3348 ± 0.0072 | 1.0558 | 0.238 | 0.6686 | 0.1306 | 0.1026 | -0.069 ± 0.0061 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 326 | 0.1936 | 0.1962 | -0.0026 ± 0.0009 | 0.566 | 0.5731 | 0.5014 | 0.486 | 0.5521 | -0.018 ± 0.0248 | -0.0133 (6) |
| 3-5 | 220 | 0.1896 | 0.1884 | +0.0011 ± 0.0023 | 0.5556 | 0.5528 | 0.4985 | 0.4592 | 0.4682 | -0.110 ± 0.0309 | -0.01 (1) |
| 5-10 | 455 | 0.1992 | 0.1987 | +0.0005 ± 0.0032 | 0.5851 | 0.582 | 0.5078 | 0.4339 | 0.4637 | -0.084 ± 0.0218 | -0.01 (4) |
| 10-15 | 349 | 0.2143 | 0.2119 | +0.0024 ± 0.0061 | 0.6186 | 0.6075 | 0.5367 | 0.4143 | 0.467 | -0.081 ± 0.0244 | -0.044 (5) |
| 15-25 | 425 | 0.2292 | 0.2084 | +0.0208 ± 0.0087 | 0.6583 | 0.6016 | 0.5788 | 0.3852 | 0.4282 | -0.106 ± 0.0219 | -0.03 (1) |
| 25-40 | 256 | 0.2029 | 0.2051 | -0.0022 ± 0.0165 | 0.5889 | 0.5888 | 0.6526 | 0.3415 | 0.4961 | -0.048 ± 0.0243 | 0.0 (1) |
| 40+ | 48 | 0.3114 | 0.1729 | +0.1385 ± 0.0545 | 0.836 | 0.5193 | 0.7473 | 0.2942 | 0.375 | -0.138 ± 0.0544 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1500 | 0.1822 | 0.1832 | -0.0010 ± 0.0004 | 0.5379 | 0.54 | 0.4851 | 0.4699 | 0.5007 | -0.026 ± 0.0111 | -0.0183 (23) |
| 3-5 | 1032 | 0.1872 | 0.1847 | +0.0025 ± 0.0011 | 0.55 | 0.5442 | 0.4722 | 0.433 | 0.4205 | -0.079 ± 0.0139 | -0.0243 (7) |
| 5-10 | 2364 | 0.1895 | 0.1852 | +0.0043 ± 0.0013 | 0.562 | 0.547 | 0.4793 | 0.4053 | 0.4141 | -0.055 ± 0.0089 | -0.01 (18) |
| 10-15 | 1810 | 0.1967 | 0.18 | +0.0168 ± 0.0025 | 0.5783 | 0.5282 | 0.4908 | 0.3676 | 0.3597 | -0.079 ± 0.0099 | -0.03 (9) |
| 15-25 | 2445 | 0.2079 | 0.1687 | +0.0392 ± 0.0033 | 0.6106 | 0.5008 | 0.4949 | 0.2994 | 0.2982 | -0.072 ± 0.0083 | -0.03 (2) |
| 25-40 | 1876 | 0.2121 | 0.1179 | +0.0942 ± 0.005 | 0.6148 | 0.3668 | 0.5219 | 0.2043 | 0.218 | -0.058 ± 0.0075 | 0.0 (1) |
| 40+ | 1248 | 0.3849 | 0.0457 | +0.3392 ± 0.0068 | 1.0053 | 0.1795 | 0.6296 | 0.1067 | 0.0553 | -0.086 ± 0.0058 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 609 | 0.2042 | 0.2042 | -0.0000 ± 0.0006 | 0.5922 | 0.5917 | 0.4996 | 0.4847 | 0.4844 | -0.050 ± 0.0182 | -0.0226 (46) |
| 3-5 | 453 | 0.1973 | 0.1956 | +0.0017 ± 0.0017 | 0.5756 | 0.5698 | 0.4778 | 0.4383 | 0.4371 | -0.057 ± 0.0208 | -0.0058 (33) |
| 5-10 | 925 | 0.1927 | 0.1874 | +0.0053 ± 0.0022 | 0.5699 | 0.5558 | 0.4782 | 0.4047 | 0.4065 | -0.059 ± 0.0145 | -0.0049 (73) |
| 10-15 | 605 | 0.2029 | 0.1931 | +0.0098 ± 0.0045 | 0.5942 | 0.5678 | 0.4876 | 0.3648 | 0.3851 | -0.044 ± 0.0178 | 0.0014 (64) |
| 15-25 | 810 | 0.2361 | 0.2091 | +0.0269 ± 0.0063 | 0.6713 | 0.6037 | 0.55 | 0.3556 | 0.3852 | -0.060 ± 0.0161 | -0.0216 (58) |
| 25-40 | 456 | 0.2435 | 0.1862 | +0.0573 ± 0.0125 | 0.6861 | 0.546 | 0.6301 | 0.317 | 0.3794 | -0.075 ± 0.0188 | -0.0216 (25) |
| 40+ | 152 | 0.3536 | 0.1875 | +0.1661 ± 0.0358 | 1.0093 | 0.5536 | 0.781 | 0.2877 | 0.3882 | -0.061 ± 0.0323 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1860 | 0.1927 | 0.1925 | +0.0002 ± 0.0004 | 0.5626 | 0.5609 | 0.5012 | 0.486 | 0.4849 | -0.045 ± 0.0101 | -0.0155 (82) |
| 3-5 | 1292 | 0.1892 | 0.1861 | +0.0031 ± 0.001 | 0.5531 | 0.546 | 0.4887 | 0.4493 | 0.4319 | -0.064 ± 0.012 | -0.0148 (63) |
| 5-10 | 2652 | 0.1912 | 0.1831 | +0.0080 ± 0.0013 | 0.5663 | 0.5439 | 0.4749 | 0.4011 | 0.3876 | -0.066 ± 0.0084 | -0.0087 (125) |
| 10-15 | 1794 | 0.1991 | 0.1845 | +0.0146 ± 0.0025 | 0.5852 | 0.547 | 0.5014 | 0.3783 | 0.3802 | -0.058 ± 0.0101 | -0.0053 (105) |
| 15-25 | 2320 | 0.2305 | 0.1968 | +0.0338 ± 0.0036 | 0.6656 | 0.5727 | 0.5443 | 0.3492 | 0.3616 | -0.062 ± 0.0093 | -0.0255 (106) |
| 25-40 | 1589 | 0.2416 | 0.161 | +0.0806 ± 0.0063 | 0.6877 | 0.4797 | 0.5922 | 0.278 | 0.3084 | -0.064 ± 0.0097 | -0.0206 (47) |
| 40+ | 759 | 0.3665 | 0.1164 | +0.2502 ± 0.0132 | 1.0075 | 0.3619 | 0.6868 | 0.1807 | 0.1963 | -0.062 ± 0.0116 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2079 | 1.06 ± 0.061 | 1.17 | 0.1699 | 0.1707 | 0.2112 | 0.2017 |
| gen2 | 2079 | 0.855 ± 0.054 | 1.107 | 0.1864 | 0.17 | 0.2294 | 0.2017 |
| gen1_elo | 2079 | 1.058 ± 0.061 | 1.165 | 0.1741 | 0.1712 | 0.209 | 0.2016 |
| gen1_sr | 2079 | 1.045 ± 0.069 | 1.178 | 0.1444 | 0.1725 | 0.2243 | 0.2015 |
| gen1_ledger | 4010 | 0.9 ± 0.04 | 1.064 | 0.1733 | 0.1903 | 0.2172 | 0.196 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 10,957)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,033 | 27.7% |
| STALE_QUOTE | market_freshness | 2,230 | 20.3% |
| BOOK_QUALITY | execution | 1,879 | 17.2% |
| POOR_DATA | data | 1,165 | 10.6% |
| LIMITED_DATA | data | 837 | 7.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 599 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 488 | 4.5% |
| IDENTITY_AMBIGUOUS | mapping | 341 | 3.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 333 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 52 | 0.5% |

Cause class: coverage 27.7%, market_freshness 20.3%, data 18.3%, execution 17.2%, market_freshness/coverage 8.5%, model_calibration_or_unknown 4.5%, mapping 3.1%, model_calibration 0.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.2%, START_UNVERIFIABLE 96.2%, LOW_DATA_QUALITY 68.6%, STALE_PLAYER_DATA 57.1%, THIN_PLAYER_HISTORY 56.7%, STALE_KALSHI_QUOTE 47.7%, MODEL_INTERNAL_DISAGREEMENT 37.2%, ASYMMETRIC_SAMPLE_SIZE 30.3%, WIDE_SPREAD 23.1%, MODEL_HIGH_UNCERTAINTY 16.3%, PLAYER_IDENTITY_RISK 11.3%, LEVEL_TRANSFER_RISK 8.9%, EVENT_MAPPING_RISK 8.0%, LOW_DISPLAYED_LIQUIDITY 7.3%, MODEL_CALIBRATION_OUTLIER 3.4%, EXTERNAL_MARKET_REJECTION 0.8%, UNKNOWN 0.5%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 30.3%, POST_SETTLEMENT_OBSERVATION 27.7%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### >= ge_25 pp (N = 5,986)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,385 | 39.8% |
| STALE_QUOTE | market_freshness | 997 | 16.7% |
| BOOK_QUALITY | execution | 994 | 16.6% |
| POOR_DATA | data | 471 | 7.9% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 327 | 5.5% |
| LIMITED_DATA | data | 258 | 4.3% |
| IDENTITY_AMBIGUOUS | mapping | 218 | 3.6% |
| IN_PLAY_QUOTE | market_freshness/coverage | 208 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 113 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 15 | 0.2% |

Cause class: coverage 39.8%, market_freshness 16.7%, execution 16.6%, data 12.2%, market_freshness/coverage 8.9%, mapping 3.6%, model_calibration_or_unknown 1.9%, model_calibration 0.2%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.6%, START_UNVERIFIABLE 98.2%, LOW_DATA_QUALITY 71.4%, THIN_PLAYER_HISTORY 58.2%, STALE_KALSHI_QUOTE 55.5%, STALE_PLAYER_DATA 51.6%, MODEL_INTERNAL_DISAGREEMENT 38.5%, ASYMMETRIC_SAMPLE_SIZE 31.8%, WIDE_SPREAD 22.6%, MODEL_HIGH_UNCERTAINTY 17.7%, PLAYER_IDENTITY_RISK 14.4%, EVENT_MAPPING_RISK 9.8%, LOW_DISPLAYED_LIQUIDITY 7.5%, LEVEL_TRANSFER_RISK 7.5%, MODEL_CALIBRATION_OUTLIER 4.2%, EXTERNAL_MARKET_REJECTION 0.4%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 42.8%, POST_SETTLEMENT_OBSERVATION 39.8%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.7%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 4958, "IDENTITY_AMBIGUOUS": 1028}; ticker orientation: {"VERIFIED": 5986}.

Checks: discipline:AMBIGUOUS 422, discipline:PASS 5564, identity_confidence:AMBIGUOUS 865, identity_confidence:PASS 5121, level_mapping:NA 434, level_mapping:PASS 5552, market_pair:AMBIGUOUS 220, market_pair:NA 134, market_pair:PASS 5632, model_complement:NA 101, model_complement:PASS 5885, namesake:PASS 5986, physical_match_id:NA 2467, physical_match_id:PASS 3519, player_ids:PASS 5986, same_pair_other_event:PASS 5986, ticker_orientation:PASS 5986

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,731 | 1.6% | 1.6% | 0.4% | {"market_freshness": 20, "execution": 7} | 5.37 | 0.2233 / 0.2136 (171) | 18.0% | 0.1% | 5.8% | 1.7% |
| CHALLENGER | 3,867 | 18.6% | 6.1% | 12.0% | {"coverage": 453, "market_freshness": 107, "market_freshness/coverage": 87, "model_calibration_or_unknown": 39, "data": 25, "execution": 4, "model_calibration": 3} | 6.69 | 0.2251 / 0.2062 (930) | 45.1% | 4.6% | 1.7% | 24.1% |
| DOUBLES | 825 | 51.1% | 50.7% | 7.0% | {"execution": 153, "mapping": 127, "market_freshness": 106, "market_freshness/coverage": 29, "coverage": 7} | 25.57 | 0.3171 / 0.2282 (228) | 28.4% | 0.0% | 100.0% | 7.8% |
| ITF_MEN | 8,033 | 23.6% | 15.5% | 31.7% | {"coverage": 791, "execution": 385, "data": 270, "market_freshness": 267, "market_freshness/coverage": 164, "mapping": 19, "model_calibration_or_unknown": 1} | 10.42 | 0.2096 / 0.1933 (2009) | 38.2% | 53.6% | 6.3% | 24.4% |
| ITF_WOMEN | 10,364 | 26.1% | 17.5% | 45.2% | {"coverage": 1117, "market_freshness": 439, "execution": 428, "data": 410, "market_freshness/coverage": 214, "mapping": 66, "model_calibration_or_unknown": 22, "model_calibration": 9} | 12.15 | 0.2044 / 0.1923 (2255) | 39.1% | 57.1% | 9.6% | 24.4% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,070 | 7.8% | 6.9% | 1.4% | {"market_freshness": 34, "model_calibration_or_unknown": 21, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 7.96 | 0.21 / 0.2073 (153) | 31.2% | 2.0% | 1.1% | 3.1% |
| WTA125 | 862 | 14.0% | 10.2% | 2.0% | {"market_freshness/coverage": 31, "model_calibration_or_unknown": 28, "market_freshness": 22, "data": 13, "coverage": 12, "execution": 8, "mapping": 4, "model_calibration": 3} | 9.91 | 0.2321 / 0.2152 (301) | 25.3% | 6.2% | 3.9% | 11.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 5 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 6 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 7 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 8 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 9 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 10 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 11 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 12 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 14 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 15 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 16 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 321 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 18 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 19 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 20 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 21 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 22 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 23 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 24 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 25 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 26 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 27 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 28 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 29 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 30 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 31 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 760 min (STALE); no external reference |
| 32 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 33 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 34 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 35 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 36 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 37 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 153 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 38 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 39 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 22 min (AGING); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 40 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 41 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 42 | `KXITFWMATCH-26OCT08ARISAV-SAV` | ITF_WOMEN | fair_v1 | 75% / 2% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.3h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 26 min (AGING); no external reference |
| 43 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 256 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 44 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.2h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 141 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 45 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 46 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 47 | `KXITFMATCH-26OCT09DELSTE-DEL` | ITF_MEN | fair_v1 | 78% / 6% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 229 min (STALE); data POOR (grade F, thinner serve sample 477.0, ratio 8.93); no external reference |
| 48 | `KXITFWMATCH-26OCT08ARAWAN-ARA` | ITF_WOMEN | fair_v1 | 77% / 6% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 341 min (STALE); data POOR (grade D, thinner serve sample 553.0, ratio 3.97); no external reference |
| 49 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 156 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 50 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9814, "by_level_share_of_ge_25pp": {"ATP": 0.0045, "CHALLENGER": 0.1199, "DOUBLES": 0.0705, "ITF_MEN": 0.3169, "ITF_WOMEN": 0.4519, "OTHER": 0.002, "WTA": 0.014, "WTA125": 0.0202}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5553, "share_primary_cause_market_settled_or_in_play": 0.4877, "share_primary_cause_stale_quote_only": 0.1666}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 5986, "identity_ambiguous_share": 0.1717, "ticker_orientation": {"VERIFIED": 5986}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 3519, "with_external": 78, "coverage": 0.0222, "external_status": {"EXTERNAL_STALE": 61, "AGREES_WITH_KALSHI": 17}, "triangulation": {"INSUFFICIENT_INPUTS": 61, "MODEL_LONE_OUTLIER": 17}, "share_external_agrees_with_kalshi": 0.2179, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 1492, "with_external": 76, "coverage": 0.0509, "external_status": {"EXTERNAL_STALE": 59, "AGREES_WITH_KALSHI": 17}, "triangulation": {"INSUFFICIENT_INPUTS": 59, "MODEL_LONE_OUTLIER": 17}, "share_external_agrees_with_kalshi": 0.2237, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 638.0, "median_sample_ratio": 2.28, "median_min_matches": 21.0, "median_max_days_since_last": 196.0, "share_severe_asymmetry": 0.1714, "data_status": {"POOR": 3044, "LIMITED": 1838, "ADEQUATE": 1104}, "comparison_lt_10pp": {"median_thinner_serve_points": 1841.0, "median_sample_ratio": 1.7, "median_min_matches": 81.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 456, "model_minus_observed": 0.0612, "kalshi_minus_observed": -0.0712, "brier_diff_model_minus_kalshi": 0.0039}, "4-10x": {"n": 318, "model_minus_observed": 0.0584, "kalshi_minus_observed": -0.0828, "brier_diff_model_minus_kalshi": -0.0013}, "<2x": {"n": 1006, "model_minus_observed": 0.0907, "kalshi_minus_observed": -0.0327, "brier_diff_model_minus_kalshi": 0.0135}, ">=10x": {"n": 299, "model_minus_observed": 0.1119, "kalshi_minus_observed": -0.0577, "brier_diff_model_minus_kalshi": 0.0163}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2079, "model": {"intercept": -0.568, "slope": 0.855, "slope_se": 0.054}, "kalshi_mid_same_rows": {"intercept": 0.199, "slope": 1.107, "slope_se": 0.062}, "mean_extremity_model": 0.1864, "mean_extremity_kalshi": 0.17, "model_brier": 0.2294, "kalshi_brier": 0.2017, "brier_diff_model_minus_kalshi": 0.0277, "brier_diff_se": 0.0042, "model_logloss": 0.6554, "kalshi_logloss": 0.5858}, "fair_v1": {"n": 2079, "model": {"intercept": -0.412, "slope": 1.06, "slope_se": 0.061}, "kalshi_mid_same_rows": {"intercept": 0.31, "slope": 1.17, "slope_se": 0.064}, "mean_extremity_model": 0.1699, "mean_extremity_kalshi": 0.1707, "model_brier": 0.2112, "kalshi_brier": 0.2017, "brier_diff_model_minus_kalshi": 0.0095, "brier_diff_se": 0.0033, "model_logloss": 0.6098, "kalshi_logloss": 0.5854}, "gen1_elo": {"n": 2079, "model": {"intercept": -0.377, "slope": 1.058, "slope_se": 0.061}, "kalshi_mid_same_rows": {"intercept": 0.328, "slope": 1.165, "slope_se": 0.063}, "mean_extremity_model": 0.1741, "mean_extremity_kalshi": 0.1712, "model_brier": 0.209, "kalshi_brier": 0.2016, "brier_diff_model_minus_kalshi": 0.0074, "brier_diff_se": 0.0033, "model_logloss": 0.6058, "kalshi_logloss": 0.5852}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2485, "share_ge_15": 0.4318, "median_abs_gap": 12.89, "n": 14160}, "gen1_elo": {"share_ge_25": 0.2405, "share_ge_15": 0.4299, "median_abs_gap": 12.43, "n": 14160}, "gen1_sr": {"share_ge_25": 0.3012, "share_ge_15": 0.5149, "median_abs_gap": 15.51, "n": 14160}, "gen2": {"share_ge_25": 0.3048, "share_ge_15": 0.5025, "median_abs_gap": 15.14, "n": 14160}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1409, "share_ge_15": 0.3282, "median_abs_gap": 10.29, "n": 10586}, "gen1_elo": {"share_ge_25": 0.1368, "share_ge_15": 0.3232, "median_abs_gap": 9.67, "n": 10585}, "gen1_sr": {"share_ge_25": 0.1946, "share_ge_15": 0.422, "median_abs_gap": 12.61, "n": 10586}, "gen2": {"share_ge_25": 0.2123, "share_ge_15": 0.4234, "median_abs_gap": 12.51, "n": 10587}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.37, "share_ge_25_all": 0.0156, "share_ge_25_pregame_clean": 0.0159}, "WTA": {"median_abs_gap_pregame_clean": 7.96, "share_ge_25_all": 0.0785, "share_ge_25_pregame_clean": 0.0685}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2391, "share_within_10pp_all": 0.4379, "share_within_10pp_pregame_clean": 0.503, "corr_model_vs_mid_pregame_clean": 0.8505}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 318, "model_brier": 0.1932, "kalshi_brier": 0.1944, "brier_diff_model_minus_kalshi": -0.0011}, "10-15": {"n_settled": 377, "model_brier": 0.2142, "kalshi_brier": 0.2066, "brier_diff_model_minus_kalshi": 0.0076}, "15-25": {"n_settled": 443, "model_brier": 0.2273, "kalshi_brier": 0.2112, "brier_diff_model_minus_kalshi": 0.0161}, "25-40": {"n_settled": 252, "model_brier": 0.2211, "kalshi_brier": 0.2018, "brier_diff_model_minus_kalshi": 0.0193}, "3-5": {"n_settled": 213, "model_brier": 0.1879, "kalshi_brier": 0.1893, "brier_diff_model_minus_kalshi": -0.0015}, "40+": {"n_settled": 55, "model_brier": 0.2888, "kalshi_brier": 0.1716, "brier_diff_model_minus_kalshi": 0.1171}, "5-10": {"n_settled": 421, "model_brier": 0.2009, "kalshi_brier": 0.2028, "brier_diff_model_minus_kalshi": -0.0018}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.568, "slope": 0.855, "slope_se": 0.054}, "kalshi_slope": {"intercept": 0.199, "slope": 1.107, "slope_se": 0.062}, "n": 2079}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.542, "slope": 0.9, "slope_se": 0.04}, "kalshi_slope": {"intercept": 0.125, "slope": 1.064, "slope_se": 0.043}, "n": 4010}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 228, "model_brier": 0.3171, "kalshi_brier": 0.2282, "brier_diff_model_minus_kalshi": 0.0889, "brier_diff_se": 0.021, "corr_model_outcome": 0.0177, "corr_kalshi_outcome": 0.31}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
