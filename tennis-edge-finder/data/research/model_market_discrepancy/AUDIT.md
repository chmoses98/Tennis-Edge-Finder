# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-12T01:52Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 29,596): 0-3 14.6%, 3-5 9.7%, 5-10 20.2%, 10-15 15.4%, 15-25 18.5%, 25-40 13.5%, 40+ 8.1%; median gap 11.66 pp.
* **Where the extremes live**: 98.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.3%, Challenger 12.2%, doubles 7.1%). Main tour: ATP 1.4% and WTA 6.4% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 6,395): MARKET_ALREADY_SETTLED_WHEN_PRICED 39.2%, BOOK_QUALITY 17.5%, STALE_QUOTE 16.2%, POOR_DATA 7.9%, POSSIBLY_IN_PLAY_QUOTE 5.7%, LIMITED_DATA 4.2%, IDENTITY_AMBIGUOUS 3.7%, IN_PLAY_QUOTE 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 1.8%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.4%. By class: coverage 39.2%, execution 17.5%, market_freshness 16.2%, data 12.1%, market_freshness/coverage 9.2%, mapping 3.7%, model_calibration_or_unknown 1.8%, model_calibration 0.4%.
* **Stale / settled / in-play**: 54.2% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 48.3% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 6,395 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 17.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 2.8%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 21.3% of the time and with the model 0.6%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 619.0 points vs 1923.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.078, Gen-2 0.873, Gen-1 ledger 0.88 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 273 model 0.218 vs Kalshi 0.2006; n 59 model 0.2961 vs Kalshi 0.17.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 118,206 model-market comparisons (194,071 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 44,147 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-12T01:44:43.144849+00:00'], shadow board 31,183 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-12T01:44:46.740207+00:00'], Model 4 13,363 rows, 12,789 settled tickers, 3,655 tickers with an external scan.
* By model: {"gen1_ledger": 29111, "gen1_elo": 15670, "fair_v1": 15670, "gen2": 15670, "gen1_sr": 15670, "model4_fundamental": 13212, "model4_conditioned": 13203}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 29,596 | 14.6 | 9.7 | 20.2 | 15.4 | 18.5 | 13.5 | 8.1 | 11.66 | 40.1% | 21.6% |
| MW fair_v1 | 15,670 | 13.9 | 8.7 | 18.7 | 16.1 | 18.5 | 14.4 | 9.7 | 12.69 | 42.6% | 24.1% |
| MW gen1_elo | 15,670 | 13.4 | 9.1 | 20.3 | 15.0 | 18.6 | 14.3 | 9.2 | 12.12 | 42.2% | 23.5% |
| MW gen1_ledger | 13,926 | 15.5 | 10.7 | 22.0 | 14.6 | 18.5 | 12.4 | 6.3 | 10.45 | 37.2% | 18.8% |
| MW gen1_sr | 15,670 | 10.1 | 7.9 | 16.6 | 14.5 | 21.6 | 17.9 | 11.4 | 15.35 | 50.9% | 29.3% |
| MW gen2 | 15,670 | 12.1 | 7.4 | 16.4 | 14.3 | 20.1 | 16.9 | 12.8 | 14.95 | 49.8% | 29.7% |
| all families model4_conditioned | 13,203 | 21.9 | 20.1 | 35.8 | 16.0 | 4.3 | 1.0 | 0.9 | 5.78 | 6.2% | 1.9% |
| all families model4_fundamental | 13,212 | 16.7 | 13.3 | 36.0 | 19.8 | 10.6 | 2.6 | 1.1 | 7.63 | 14.3% | 3.7% |

Configurable thresholds (primary): >=5pp 75.7%, >=10pp 55.5%, >=15pp 40.1%, >=20pp 29.8%, >=25pp 21.6%, >=30pp 15.8%, >=40pp 8.1%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.24pp; >=10pp 44.7%, >=25pp 17.3%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,279 | 30.5 | 14.5 | 24.6 | 17.8 | 10.7 | 1.1 | 0.9 | 5.84 | 12.7% | 1.9% |
| CHALLENGER | 2,745 | 15.8 | 10.1 | 20.0 | 16.0 | 14.4 | 12.2 | 11.5 | 11.52 | 38.1% | 23.7% |
| ITF_MEN | 4,356 | 11.5 | 8.8 | 18.3 | 14.8 | 19.1 | 15.3 | 12.1 | 13.75 | 46.6% | 27.5% |
| ITF_WOMEN | 6,021 | 10.2 | 6.6 | 15.9 | 16.2 | 21.5 | 18.7 | 10.8 | 15.46 | 51.0% | 29.5% |
| WTA | 796 | 21.9 | 10.9 | 25.4 | 16.3 | 18.5 | 5.7 | 1.4 | 7.87 | 25.5% | 7.0% |
| WTA125 | 473 | 12.9 | 8.2 | 23.7 | 20.3 | 18.2 | 14.6 | 2.1 | 11.08 | 34.9% | 16.7% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,279 | 24.1 | 14.5 | 24.4 | 19.1 | 15.0 | 1.9 | 1.0 | 6.9 | 17.9% | 2.9% |
| CHALLENGER | 2,745 | 15.4 | 7.5 | 19.3 | 13.3 | 18.2 | 14.1 | 12.2 | 12.78 | 44.5% | 26.3% |
| ITF_MEN | 4,356 | 10.3 | 7.4 | 16.7 | 14.7 | 19.8 | 17.9 | 13.2 | 15.43 | 50.8% | 31.0% |
| ITF_WOMEN | 6,021 | 8.9 | 5.9 | 12.8 | 12.9 | 21.6 | 20.9 | 17.1 | 19.1 | 59.6% | 38.0% |
| WTA | 796 | 19.4 | 8.7 | 18.1 | 15.4 | 22.4 | 14.7 | 1.4 | 11.59 | 38.4% | 16.1% |
| WTA125 | 473 | 4.9 | 4.0 | 18.6 | 19.7 | 24.5 | 18.4 | 9.9 | 16.84 | 52.8% | 28.3% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,279 | 27.3 | 14.3 | 29.4 | 15.0 | 10.6 | 2.5 | 0.9 | 6.1 | 14.0% | 3.4% |
| CHALLENGER | 2,745 | 15.3 | 10.3 | 20.8 | 15.5 | 14.9 | 11.8 | 11.4 | 10.85 | 38.2% | 23.2% |
| ITF_MEN | 4,356 | 10.5 | 8.9 | 19.0 | 13.7 | 19.9 | 15.7 | 12.3 | 14.02 | 48.0% | 28.0% |
| ITF_WOMEN | 6,021 | 9.8 | 6.7 | 16.6 | 15.6 | 22.6 | 19.0 | 9.6 | 15.52 | 51.2% | 28.6% |
| WTA | 796 | 22.5 | 14.6 | 33.8 | 15.6 | 10.2 | 2.5 | 0.9 | 6.23 | 13.6% | 3.4% |
| WTA125 | 473 | 22.8 | 10.8 | 30.2 | 14.8 | 13.9 | 7.0 | 0.4 | 7.6 | 21.3% | 7.4% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 703 | 30.7 | 22.5 | 36.0 | 9.1 | 1.3 | 0.4 | 0.0 | 4.73 | 1.7% | 0.4% |
| CHALLENGER | 1,895 | 22.3 | 15.8 | 27.2 | 14.8 | 13.0 | 4.9 | 1.9 | 6.88 | 19.8% | 6.9% |
| DOUBLES | 909 | 4.5 | 3.2 | 11.4 | 11.2 | 19.4 | 24.8 | 25.5 | 25.37 | 69.6% | 50.3% |
| ITF_MEN | 4,158 | 15.0 | 8.6 | 21.1 | 15.4 | 20.4 | 12.2 | 7.4 | 11.71 | 40.0% | 19.6% |
| ITF_WOMEN | 4,872 | 11.6 | 9.3 | 19.6 | 14.5 | 22.5 | 16.7 | 5.8 | 13.09 | 45.0% | 22.5% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 625 | 21.1 | 14.9 | 27.0 | 17.3 | 14.1 | 5.1 | 0.5 | 7.78 | 19.7% | 5.6% |
| WTA125 | 615 | 20.3 | 13.7 | 21.8 | 18.4 | 15.0 | 8.5 | 2.4 | 8.37 | 25.9% | 10.9% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,267 | 30.4 | 14.4 | 24.7 | 17.9 | 10.7 | 1.1 | 0.9 | 5.84 | 12.6% | 2.0% |
| CHALLENGER | 1,991 | 20.2 | 12.5 | 25.2 | 18.6 | 15.0 | 6.1 | 2.4 | 8.31 | 23.5% | 8.5% |
| ITF_MEN | 3,080 | 14.4 | 11.1 | 21.9 | 16.6 | 19.1 | 11.9 | 4.9 | 10.62 | 35.9% | 16.8% |
| ITF_WOMEN | 4,267 | 12.7 | 8.3 | 18.7 | 18.9 | 23.2 | 14.9 | 3.3 | 12.64 | 41.4% | 18.2% |
| WTA | 791 | 21.7 | 11.0 | 25.5 | 16.3 | 18.5 | 5.6 | 1.4 | 7.85 | 25.4% | 7.0% |
| WTA125 | 452 | 13.5 | 8.0 | 23.0 | 20.8 | 18.8 | 14.4 | 1.6 | 11.08 | 34.7% | 15.9% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,267 | 23.9 | 14.6 | 24.5 | 19.1 | 15.0 | 1.9 | 1.0 | 6.9 | 17.9% | 2.9% |
| CHALLENGER | 1,991 | 19.7 | 9.4 | 24.0 | 16.0 | 18.6 | 9.5 | 2.7 | 9.13 | 30.8% | 12.2% |
| ITF_MEN | 3,081 | 12.5 | 9.0 | 19.5 | 16.6 | 21.6 | 15.0 | 5.9 | 12.52 | 42.5% | 20.9% |
| ITF_WOMEN | 4,267 | 10.4 | 7.0 | 14.6 | 14.1 | 24.4 | 19.5 | 10.0 | 16.37 | 53.9% | 29.5% |
| WTA | 791 | 19.3 | 8.7 | 18.1 | 15.6 | 22.2 | 14.7 | 1.4 | 11.55 | 38.3% | 16.1% |
| WTA125 | 452 | 4.9 | 4.2 | 18.8 | 20.1 | 24.1 | 19.0 | 8.8 | 16.39 | 52.0% | 27.9% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 683 | 30.8 | 22.7 | 36.3 | 9.2 | 0.6 | 0.4 | 0.0 | 4.7 | 1.0% | 0.4% |
| CHALLENGER | 1,624 | 24.3 | 17.4 | 29.4 | 14.7 | 12.0 | 1.9 | 0.3 | 6.23 | 14.2% | 2.2% |
| DOUBLES | 842 | 4.5 | 3.2 | 11.8 | 11.3 | 19.5 | 24.6 | 25.2 | 24.68 | 69.2% | 49.8% |
| ITF_MEN | 3,358 | 16.7 | 9.4 | 23.3 | 16.4 | 20.2 | 9.8 | 4.2 | 10.08 | 34.2% | 14.0% |
| ITF_WOMEN | 3,982 | 12.8 | 10.0 | 21.5 | 15.4 | 22.8 | 15.0 | 2.6 | 11.64 | 40.4% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 595 | 21.5 | 15.5 | 27.6 | 17.3 | 14.3 | 3.9 | 0.0 | 7.33 | 18.1% | 3.9% |
| WTA125 | 517 | 22.4 | 15.3 | 23.4 | 20.3 | 13.2 | 5.0 | 0.4 | 7.42 | 18.6% | 5.4% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 909 | 4.5 | 3.2 | 11.4 | 11.2 | 19.4 | 24.8 | 25.5 | 25.37 | 69.6% | 50.3% |
| singles | 13,017 | 16.2 | 11.2 | 22.7 | 14.9 | 18.4 | 11.6 | 5.0 | 9.95 | 35.0% | 16.6% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 3,577 | 13.4 | 9.4 | 20.7 | 15.9 | 16.9 | 13.7 | 9.9 | 12.03 | 40.5% | 23.7% |
| Grass | 69 | 11.6 | 24.6 | 14.5 | 7.2 | 23.2 | 18.8 | 0.0 | 9.51 | 42.0% | 18.8% |
| Hard | 10,473 | 14.4 | 8.5 | 18.5 | 15.9 | 18.8 | 14.2 | 9.6 | 12.69 | 42.6% | 23.9% |
| UNKNOWN | 1,551 | 11.6 | 8.1 | 15.5 | 17.7 | 19.9 | 16.9 | 10.3 | 14.09 | 47.1% | 27.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,883 | 20.1 | 10.7 | 21.1 | 17.1 | 15.1 | 8.7 | 7.2 | 9.45 | 31.0% | 15.9% |
| B | 2,117 | 14.4 | 9.3 | 19.9 | 17.3 | 17.3 | 12.0 | 9.9 | 11.45 | 39.2% | 21.9% |
| C | 2,315 | 13.3 | 9.7 | 19.4 | 14.6 | 19.0 | 14.7 | 9.2 | 12.62 | 43.0% | 24.0% |
| D | 2,794 | 10.8 | 8.3 | 18.1 | 16.0 | 22.0 | 14.8 | 9.8 | 13.84 | 46.7% | 24.7% |
| F | 3,561 | 7.9 | 5.3 | 14.8 | 14.8 | 20.7 | 23.1 | 13.4 | 18.38 | 57.2% | 36.4% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,118 | 22.4 | 15.9 | 28.6 | 15.2 | 11.6 | 4.5 | 1.7 | 6.8 | 17.8% | 6.2% |
| B | 2,166 | 15.2 | 9.8 | 24.1 | 16.2 | 19.2 | 11.2 | 4.3 | 10.18 | 34.7% | 15.5% |
| C | 2,775 | 12.2 | 7.6 | 18.1 | 14.4 | 20.5 | 15.8 | 11.4 | 13.71 | 47.7% | 27.2% |
| D | 2,177 | 14.2 | 9.7 | 21.2 | 13.2 | 21.7 | 13.8 | 6.3 | 11.83 | 41.8% | 20.1% |
| F | 2,690 | 9.4 | 7.5 | 14.8 | 13.8 | 23.7 | 21.0 | 9.8 | 16.8 | 54.5% | 30.8% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 5,370 | 18.5 | 9.8 | 20.3 | 17.1 | 15.2 | 9.6 | 9.5 | 10.42 | 34.3% | 19.1% |
| LIMITED | 3,898 | 15.3 | 10.5 | 20.6 | 15.7 | 18.4 | 12.8 | 6.7 | 11.07 | 37.9% | 19.6% |
| POOR | 6,402 | 9.2 | 6.7 | 16.3 | 15.4 | 21.3 | 19.4 | 11.8 | 15.99 | 52.4% | 31.1% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,894 | 31.2 | 24.1 | 36.5 | 5.6 | 1.8 | 0.7 | 0.1 | 4.54 | 2.6% | 0.8% |
| GAME_SPREAD | 2,799 | 25.5 | 15.8 | 36.9 | 17.0 | 4.2 | 0.4 | 0.2 | 6.05 | 4.9% | 0.6% |
| MATCH_WINNER | 13,926 | 15.5 | 10.7 | 22.0 | 14.6 | 18.5 | 12.4 | 6.3 | 10.45 | 37.2% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 5,265 | 32.9 | 19.4 | 31.1 | 9.9 | 5.3 | 1.2 | 0.2 | 4.78 | 6.7% | 1.4% |
| TOTAL_GAMES | 4,203 | 6.7 | 8.9 | 39.1 | 29.8 | 10.3 | 2.8 | 2.4 | 9.5 | 15.5% | 5.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,734 | 25.6 | 37.9 | 31.7 | 0.3 | 4.0 | 0.4 | 0.1 | 4.32 | 4.6% | 0.6% |
| GAME_SPREAD | 3,362 | 44.9 | 16.0 | 29.3 | 7.5 | 1.2 | 0.7 | 0.4 | 3.59 | 2.3% | 1.1% |
| TOTAL_GAMES | 5,107 | 3.3 | 6.4 | 43.8 | 36.2 | 6.5 | 1.7 | 2.0 | 9.66 | 10.3% | 3.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,734 | 26.1 | 18.6 | 37.2 | 9.4 | 6.4 | 2.1 | 0.3 | 5.54 | 8.9% | 2.5% |
| GAME_SPREAD | 3,362 | 18.9 | 12.9 | 30.4 | 21.3 | 13.4 | 2.4 | 0.7 | 7.9 | 16.4% | 3.1% |
| TOTAL_GAMES | 5,116 | 6.5 | 8.6 | 38.5 | 28.5 | 12.6 | 3.1 | 2.2 | 9.65 | 17.9% | 5.3% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 15,670 | 42.6% | 24.1% | 12.69 | 32.5% | 13.6% | 10.12 |
| gen1_elo | 15,670 | 42.2% | 23.5% | 12.12 | 31.8% | 13.4% | 9.56 |
| gen1_sr | 15,670 | 50.9% | 29.3% | 15.35 | 41.8% | 18.8% | 12.48 |
| gen2 | 15,670 | 49.8% | 29.7% | 14.95 | 42.1% | 20.6% | 12.39 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 8,259 | 16.8 | 11.0 | 21.7 | 17.5 | 18.6 | 11.1 | 3.3 | 10.11 | 33.0% | 14.3% |
| STALE | 7,411 | 10.6 | 6.2 | 15.4 | 14.4 | 18.3 | 18.1 | 17.0 | 16.86 | 53.3% | 35.1% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 7,394 | 17.5 | 11.7 | 24.0 | 14.5 | 16.7 | 10.9 | 4.6 | 9.22 | 32.3% | 15.6% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 29,596 | 7394 | 11731 | 10471 | 24.4 | 145.5 | 1400.4 |
| ge_15pp | 11,862 | 2387 | 4012 | 5463 | 27.8 | 451.6 | 1380.4 |
| ge_25pp | 6,395 | 1151 | 1775 | 3469 | 34.6 | 578.0 | 1380.4 |
| lt_10pp | 13,181 | 3933 | 5721 | 3527 | 22.6 | 49.2 | 1341.5 |

Current slate `SL-20261012T015241Z-feab5b57`: 590 priced rows, quote age at build {'median': 8.2, 'max': 8.3}, freshness {'FRESH': 590}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 8 | 0.0 | 0.0 | 37.5 | 0.0 | 37.5 | 25.0 | 0.0 | 20.45 | 62.5% | 25.0% |
| EXTERNAL_LONE_OUTLIER | 8 | 62.5 | 37.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.43 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,118 | 22.5 | 10.9 | 23.3 | 19.1 | 17.8 | 6.1 | 0.4 | 8.45 | 24.2% | 6.4% |
| KALSHI_LONE_OUTLIER | 3 | 0.0 | 0.0 | 66.7 | 0.0 | 33.3 | 0.0 | 0.0 | 5.14 | 33.3% | 0.0% |
| MARKETS_AGREE | 200 | 72.5 | 27.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.99 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 361 | 0.0 | 4.2 | 36.8 | 30.5 | 20.2 | 7.8 | 0.6 | 11.24 | 28.5% | 8.3% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 15,670 | 1698 (10.8%) | 21.3% | 0.6% | {"EXTERNAL_STALE": 1118, "AGREES_WITH_KALSHI": 361, "ALL_AGREE": 200, "EXTERNAL_OUTLIER": 8, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 3, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 6,676 | 380 (5.7%) | 27.1% | 1.6% | {"EXTERNAL_STALE": 271, "AGREES_WITH_KALSHI": 103, "SUPPORTS_MODEL_DIRECTION": 5, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp | 3,782 | 104 (2.8%) | 28.8% | 1.9% | {"EXTERNAL_STALE": 72, "AGREES_WITH_KALSHI": 30, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_ge_25pp_pregame_clean | 1,614 | 99 (6.1%) | 28.3% | 2.0% | {"EXTERNAL_STALE": 69, "AGREES_WITH_KALSHI": 28, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_lt_10pp | 6,479 | 995 (15.4%) | 14.9% | 0.4% | {"EXTERNAL_STALE": 634, "ALL_AGREE": 200, "AGREES_WITH_KALSHI": 148, "EXTERNAL_OUTLIER": 8, "AGREES_WITH_MODEL": 2, "SUPPORTS_MODEL_DIRECTION": 2, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,113 | 11.7 | 8.4 | 19.7 | 15.2 | 21.1 | 13.9 | 10.0 | 13.24 | 45.1% | 23.9% |
| 4-10x | 2,108 | 11.8 | 9.0 | 19.4 | 15.2 | 19.6 | 15.9 | 9.2 | 13.09 | 44.7% | 25.1% |
| <2x | 8,441 | 16.0 | 9.3 | 18.9 | 17.2 | 16.9 | 12.6 | 9.1 | 11.67 | 38.6% | 21.7% |
| >=10x | 2,008 | 10.9 | 6.5 | 16.0 | 13.4 | 19.7 | 21.0 | 12.5 | 16.51 | 53.2% | 33.5% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 4,155 | 14.1 | 8.3 | 19.4 | 16.0 | 18.6 | 12.7 | 10.8 | 12.44 | 42.1% | 23.5% |
| 300-1000 | 3,677 | 12.1 | 8.9 | 17.2 | 16.0 | 21.0 | 15.8 | 9.1 | 13.66 | 45.8% | 24.8% |
| <300 | 4,090 | 8.5 | 6.2 | 15.9 | 14.6 | 20.7 | 21.3 | 12.8 | 17.12 | 54.8% | 34.1% |
| >=3000 | 3,748 | 21.4 | 11.8 | 22.4 | 17.7 | 13.4 | 7.4 | 5.8 | 8.45 | 26.7% | 13.3% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 499 | 0.5377 | 0.4067 | 0.479 | +0.059 | -0.072 | 0.0021 ± 0.0065 |
| ratio 4-10x | 339 | 0.5803 | 0.4396 | 0.5162 | +0.064 | -0.077 | 0.0027 ± 0.0086 |
| ratio <2x | 1167 | 0.539 | 0.4181 | 0.4584 | +0.081 | -0.040 | 0.0109 ± 0.0041 |
| ratio >=10x | 337 | 0.5477 | 0.3803 | 0.4362 | +0.112 | -0.056 | 0.0145 ± 0.0095 |
| thinner_sample 1000-3000 | 660 | 0.5451 | 0.422 | 0.4773 | +0.068 | -0.055 | 0.0048 ± 0.0055 |
| thinner_sample 300-1000 | 601 | 0.5637 | 0.4244 | 0.4859 | +0.078 | -0.061 | 0.0026 ± 0.0063 |
| thinner_sample <300 | 668 | 0.5428 | 0.3829 | 0.4521 | +0.091 | -0.069 | 0.0125 ± 0.0066 |
| thinner_sample >=3000 | 413 | 0.5264 | 0.4326 | 0.4528 | +0.074 | -0.020 | 0.0159 ± 0.0056 |
| data_status ADEQUATE | 654 | 0.5305 | 0.4288 | 0.4511 | +0.080 | -0.022 | 0.0113 ± 0.0047 |
| data_status LIMITED | 644 | 0.5544 | 0.4247 | 0.4922 | +0.062 | -0.068 | 0.0014 ± 0.0058 |
| data_status POOR | 1044 | 0.5504 | 0.3967 | 0.4636 | +0.087 | -0.067 | 0.0108 ± 0.0051 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 363 | 0.1904 | 0.1917 | -0.0014 ± 0.0008 | 0.5569 | 0.5602 | 0.4909 | 0.4761 | 0.5207 | -0.051 ± 0.0241 | -0.01 (3) |
| 3-5 | 241 | 0.1899 | 0.1912 | -0.0012 ± 0.0022 | 0.5596 | 0.5608 | 0.5097 | 0.47 | 0.5021 | -0.060 ± 0.0285 | 0.02 (1) |
| 5-10 | 488 | 0.2006 | 0.2022 | -0.0016 ± 0.0031 | 0.586 | 0.5894 | 0.5171 | 0.4431 | 0.4816 | -0.085 ± 0.0212 | -0.0125 (4) |
| 10-15 | 421 | 0.2111 | 0.2047 | +0.0064 ± 0.0055 | 0.61 | 0.5904 | 0.5172 | 0.3933 | 0.4252 | -0.090 ± 0.022 | -0.0633 (3) |
| 15-25 | 497 | 0.2257 | 0.2131 | +0.0126 ± 0.0081 | 0.6458 | 0.6133 | 0.5754 | 0.3806 | 0.4467 | -0.079 ± 0.0205 | -0.0133 (6) |
| 25-40 | 273 | 0.218 | 0.2006 | +0.0175 ± 0.0161 | 0.6257 | 0.5766 | 0.6486 | 0.3402 | 0.4652 | -0.075 ± 0.024 | -0.01 (1) |
| 40+ | 59 | 0.2961 | 0.17 | +0.1261 ± 0.0478 | 0.8068 | 0.513 | 0.7522 | 0.3075 | 0.3898 | -0.142 ± 0.0474 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1816 | 0.1734 | 0.1744 | -0.0010 ± 0.0003 | 0.5174 | 0.5186 | 0.4763 | 0.4614 | 0.4945 | -0.023 ± 0.0099 | -0.0188 (8) |
| 3-5 | 1131 | 0.1921 | 0.1895 | +0.0026 ± 0.001 | 0.5651 | 0.554 | 0.4797 | 0.4402 | 0.4235 | -0.076 ± 0.0131 | 0.02 (1) |
| 5-10 | 2468 | 0.1941 | 0.1916 | +0.0025 ± 0.0013 | 0.5702 | 0.5619 | 0.4862 | 0.4125 | 0.4287 | -0.052 ± 0.009 | -0.0082 (17) |
| 10-15 | 2153 | 0.1997 | 0.1817 | +0.0179 ± 0.0023 | 0.585 | 0.5347 | 0.4765 | 0.352 | 0.3418 | -0.077 ± 0.0091 | -0.0475 (4) |
| 15-25 | 2512 | 0.2028 | 0.1675 | +0.0353 ± 0.0032 | 0.5973 | 0.497 | 0.4965 | 0.3005 | 0.3105 | -0.064 ± 0.0082 | -0.0048 (29) |
| 25-40 | 2069 | 0.2188 | 0.1228 | +0.0961 ± 0.0048 | 0.6307 | 0.3801 | 0.5276 | 0.214 | 0.2209 | -0.064 ± 0.0074 | -0.01 (1) |
| 40+ | 1412 | 0.3715 | 0.0432 | +0.3284 ± 0.0061 | 0.969 | 0.1719 | 0.6224 | 0.1059 | 0.0567 | -0.086 ± 0.0052 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 276 | 0.1946 | 0.1949 | -0.0003 ± 0.0009 | 0.5695 | 0.5707 | 0.4929 | 0.478 | 0.4891 | -0.088 ± 0.0282 | -0.01 (1) |
| 3-5 | 184 | 0.2082 | 0.2086 | -0.0003 ± 0.0027 | 0.5969 | 0.5994 | 0.5252 | 0.4852 | 0.5054 | -0.064 ± 0.0352 | 0.02 (1) |
| 5-10 | 426 | 0.1963 | 0.1945 | +0.0019 ± 0.0032 | 0.5743 | 0.5703 | 0.5565 | 0.4814 | 0.5047 | -0.085 ± 0.0221 | -0.01 (4) |
| 10-15 | 392 | 0.2132 | 0.2043 | +0.0089 ± 0.0058 | 0.6124 | 0.5943 | 0.5767 | 0.4519 | 0.4821 | -0.099 ± 0.0235 | -0.05 (4) |
| 15-25 | 572 | 0.2238 | 0.2088 | +0.0150 ± 0.0075 | 0.6362 | 0.5999 | 0.5977 | 0.4007 | 0.4668 | -0.081 ± 0.0194 | -0.01 (5) |
| 25-40 | 357 | 0.2735 | 0.1989 | +0.0746 ± 0.0149 | 0.7667 | 0.5774 | 0.672 | 0.3582 | 0.3978 | -0.140 ± 0.0235 | -0.025 (2) |
| 40+ | 135 | 0.3489 | 0.1865 | +0.1624 ± 0.0361 | 0.9805 | 0.5461 | 0.7554 | 0.2786 | 0.363 | -0.069 ± 0.0353 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1571 | 0.1774 | 0.1778 | -0.0004 ± 0.0004 | 0.5264 | 0.5275 | 0.491 | 0.4765 | 0.5003 | -0.031 ± 0.011 | -0.0217 (6) |
| 3-5 | 978 | 0.1922 | 0.1914 | +0.0009 ± 0.0011 | 0.5584 | 0.5563 | 0.5193 | 0.4794 | 0.4877 | -0.042 ± 0.0142 | 0.02 (1) |
| 5-10 | 2172 | 0.1884 | 0.1849 | +0.0035 ± 0.0014 | 0.5584 | 0.5461 | 0.5133 | 0.4396 | 0.4553 | -0.048 ± 0.0094 | -0.01 (5) |
| 10-15 | 1884 | 0.1949 | 0.1801 | +0.0148 ± 0.0025 | 0.5754 | 0.5292 | 0.5202 | 0.3958 | 0.4013 | -0.066 ± 0.0099 | -0.02 (14) |
| 15-25 | 2728 | 0.2136 | 0.1743 | +0.0392 ± 0.0032 | 0.6228 | 0.5157 | 0.5347 | 0.3389 | 0.3402 | -0.076 ± 0.0081 | -0.0026 (27) |
| 25-40 | 2368 | 0.249 | 0.1364 | +0.1127 ± 0.0048 | 0.708 | 0.4158 | 0.5613 | 0.2452 | 0.2268 | -0.089 ± 0.0076 | -0.015 (6) |
| 40+ | 1860 | 0.4033 | 0.0667 | +0.3366 ± 0.0068 | 1.0568 | 0.2344 | 0.6668 | 0.1298 | 0.0989 | -0.072 ± 0.0058 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 360 | 0.1927 | 0.1955 | -0.0027 ± 0.0008 | 0.563 | 0.5702 | 0.4988 | 0.4836 | 0.5639 | -0.001 ± 0.0234 | -0.0133 (6) |
| 3-5 | 253 | 0.1866 | 0.1853 | +0.0013 ± 0.0022 | 0.5489 | 0.5459 | 0.5003 | 0.4609 | 0.4664 | -0.108 ± 0.0284 | -0.01 (1) |
| 5-10 | 525 | 0.2007 | 0.1987 | +0.0021 ± 0.0029 | 0.5885 | 0.581 | 0.5075 | 0.4336 | 0.4514 | -0.093 ± 0.0202 | -0.01 (4) |
| 10-15 | 404 | 0.2125 | 0.213 | -0.0004 ± 0.0057 | 0.614 | 0.6091 | 0.5363 | 0.4137 | 0.4777 | -0.069 ± 0.0229 | -0.044 (5) |
| 15-25 | 469 | 0.2289 | 0.2073 | +0.0216 ± 0.0082 | 0.6572 | 0.5988 | 0.5796 | 0.3866 | 0.4286 | -0.104 ± 0.0207 | -0.03 (1) |
| 25-40 | 280 | 0.2007 | 0.2058 | -0.0051 ± 0.0157 | 0.5843 | 0.5905 | 0.655 | 0.3435 | 0.5036 | -0.047 ± 0.0232 | 0.0 (1) |
| 40+ | 51 | 0.3152 | 0.173 | +0.1422 ± 0.0527 | 0.8532 | 0.5189 | 0.7494 | 0.2986 | 0.3725 | -0.150 ± 0.0537 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1697 | 0.1815 | 0.1825 | -0.0010 ± 0.0004 | 0.5352 | 0.5371 | 0.4848 | 0.4697 | 0.505 | -0.020 ± 0.0104 | -0.0183 (23) |
| 3-5 | 1182 | 0.1839 | 0.1813 | +0.0026 ± 0.001 | 0.5433 | 0.537 | 0.4794 | 0.4401 | 0.4281 | -0.076 ± 0.0128 | -0.0243 (7) |
| 5-10 | 2637 | 0.1905 | 0.1852 | +0.0052 ± 0.0013 | 0.564 | 0.5467 | 0.481 | 0.4072 | 0.4073 | -0.063 ± 0.0085 | -0.01 (18) |
| 10-15 | 2034 | 0.1955 | 0.1816 | +0.0139 ± 0.0023 | 0.5754 | 0.532 | 0.4929 | 0.3698 | 0.3741 | -0.065 ± 0.0094 | -0.03 (9) |
| 15-25 | 2629 | 0.2076 | 0.1689 | +0.0387 ± 0.0031 | 0.61 | 0.5017 | 0.5001 | 0.3049 | 0.3054 | -0.071 ± 0.008 | -0.03 (2) |
| 25-40 | 2040 | 0.2125 | 0.1192 | +0.0933 ± 0.0048 | 0.6158 | 0.3697 | 0.5228 | 0.2061 | 0.2206 | -0.060 ± 0.0072 | 0.0 (1) |
| 40+ | 1342 | 0.3852 | 0.0453 | +0.3399 ± 0.0065 | 1.0072 | 0.1778 | 0.6301 | 0.1074 | 0.0551 | -0.088 ± 0.0055 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 667 | 0.2008 | 0.2014 | -0.0006 ± 0.0006 | 0.5831 | 0.584 | 0.5017 | 0.4867 | 0.5022 | -0.035 ± 0.0174 | -0.0226 (46) |
| 3-5 | 486 | 0.1984 | 0.1973 | +0.0011 ± 0.0016 | 0.577 | 0.5725 | 0.4798 | 0.4401 | 0.4444 | -0.051 ± 0.0201 | -0.0058 (33) |
| 5-10 | 998 | 0.1918 | 0.1864 | +0.0055 ± 0.0021 | 0.5675 | 0.5533 | 0.4799 | 0.4063 | 0.4068 | -0.062 ± 0.0139 | -0.0049 (73) |
| 10-15 | 636 | 0.2038 | 0.1932 | +0.0106 ± 0.0044 | 0.5957 | 0.5679 | 0.4921 | 0.3693 | 0.3868 | -0.050 ± 0.0175 | 0.0014 (64) |
| 15-25 | 858 | 0.2344 | 0.2101 | +0.0243 ± 0.0061 | 0.668 | 0.6057 | 0.5533 | 0.3591 | 0.3951 | -0.057 ± 0.0157 | -0.0216 (58) |
| 25-40 | 484 | 0.2508 | 0.1889 | +0.0619 ± 0.0123 | 0.7076 | 0.5523 | 0.6403 | 0.3268 | 0.3822 | -0.087 ± 0.0183 | -0.0216 (25) |
| 40+ | 166 | 0.3602 | 0.1898 | +0.1703 ± 0.0347 | 1.0519 | 0.5591 | 0.7926 | 0.2989 | 0.3976 | -0.071 ± 0.0308 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2087 | 0.1903 | 0.1905 | -0.0002 ± 0.0003 | 0.5559 | 0.555 | 0.5021 | 0.4868 | 0.4964 | -0.034 ± 0.0095 | -0.0155 (82) |
| 3-5 | 1440 | 0.1898 | 0.1872 | +0.0026 ± 0.0009 | 0.5545 | 0.548 | 0.4866 | 0.4471 | 0.4347 | -0.058 ± 0.0114 | -0.0148 (63) |
| 5-10 | 2896 | 0.1895 | 0.1815 | +0.0080 ± 0.0012 | 0.5622 | 0.5398 | 0.4747 | 0.4009 | 0.3874 | -0.066 ± 0.008 | -0.0087 (125) |
| 10-15 | 1964 | 0.1994 | 0.1851 | +0.0143 ± 0.0024 | 0.5854 | 0.5478 | 0.5027 | 0.3797 | 0.3829 | -0.056 ± 0.0097 | -0.0053 (105) |
| 15-25 | 2500 | 0.2291 | 0.1974 | +0.0317 ± 0.0035 | 0.6622 | 0.5742 | 0.5499 | 0.355 | 0.3724 | -0.059 ± 0.009 | -0.0255 (106) |
| 25-40 | 1698 | 0.2514 | 0.1642 | +0.0872 ± 0.0062 | 0.7146 | 0.4872 | 0.6018 | 0.2869 | 0.308 | -0.077 ± 0.0095 | -0.0206 (47) |
| 40+ | 839 | 0.3857 | 0.1235 | +0.2622 ± 0.0131 | 1.0979 | 0.3813 | 0.7065 | 0.1974 | 0.2086 | -0.075 ± 0.0115 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2342 | 1.078 ± 0.058 | 1.197 | 0.1694 | 0.1699 | 0.2096 | 0.2012 |
| gen2 | 2342 | 0.873 ± 0.052 | 1.139 | 0.1847 | 0.1693 | 0.2271 | 0.201 |
| gen1_elo | 2342 | 1.07 ± 0.057 | 1.185 | 0.1734 | 0.1703 | 0.2081 | 0.2012 |
| gen1_sr | 2342 | 1.074 ± 0.066 | 1.222 | 0.1433 | 0.1715 | 0.2228 | 0.2008 |
| gen1_ledger | 4295 | 0.88 ± 0.038 | 1.084 | 0.1749 | 0.1881 | 0.2174 | 0.1961 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 11,862)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,170 | 26.7% |
| STALE_QUOTE | market_freshness | 2,341 | 19.7% |
| BOOK_QUALITY | execution | 2,131 | 18.0% |
| POOR_DATA | data | 1,233 | 10.4% |
| LIMITED_DATA | data | 926 | 7.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 671 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 549 | 4.6% |
| IDENTITY_AMBIGUOUS | mapping | 385 | 3.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 358 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 98 | 0.8% |

Cause class: coverage 26.7%, market_freshness 19.7%, data 18.2%, execution 18.0%, market_freshness/coverage 8.7%, model_calibration_or_unknown 4.6%, mapping 3.2%, model_calibration 0.8%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.6%, START_UNVERIFIABLE 95.8%, LOW_DATA_QUALITY 67.7%, STALE_PLAYER_DATA 56.7%, THIN_PLAYER_HISTORY 56.1%, STALE_KALSHI_QUOTE 46.1%, MODEL_INTERNAL_DISAGREEMENT 37.6%, ASYMMETRIC_SAMPLE_SIZE 30.3%, WIDE_SPREAD 23.8%, MODEL_HIGH_UNCERTAINTY 16.4%, PLAYER_IDENTITY_RISK 11.8%, LEVEL_TRANSFER_RISK 8.9%, EVENT_MAPPING_RISK 8.0%, LOW_DISPLAYED_LIQUIDITY 7.4%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 1.4%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 29.3%, POST_SETTLEMENT_OBSERVATION 26.7%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### >= ge_25 pp (N = 6,395)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,505 | 39.2% |
| BOOK_QUALITY | execution | 1,120 | 17.5% |
| STALE_QUOTE | market_freshness | 1,033 | 16.2% |
| POOR_DATA | data | 503 | 7.9% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 364 | 5.7% |
| LIMITED_DATA | data | 270 | 4.2% |
| IDENTITY_AMBIGUOUS | mapping | 237 | 3.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 222 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 118 | 1.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 23 | 0.4% |

Cause class: coverage 39.2%, execution 17.5%, market_freshness 16.2%, data 12.1%, market_freshness/coverage 9.2%, mapping 3.7%, model_calibration_or_unknown 1.8%, model_calibration 0.4%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.2%, START_UNVERIFIABLE 98.1%, LOW_DATA_QUALITY 71.4%, THIN_PLAYER_HISTORY 58.3%, STALE_KALSHI_QUOTE 54.2%, STALE_PLAYER_DATA 51.3%, MODEL_INTERNAL_DISAGREEMENT 38.9%, ASYMMETRIC_SAMPLE_SIZE 32.5%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 17.5%, PLAYER_IDENTITY_RISK 15.0%, EVENT_MAPPING_RISK 9.8%, LEVEL_TRANSFER_RISK 7.8%, LOW_DISPLAYED_LIQUIDITY 7.6%, MODEL_CALIBRATION_OUTLIER 4.7%, EXTERNAL_MARKET_REJECTION 0.7%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 42.1%, POST_SETTLEMENT_OBSERVATION 39.2%, POSSIBLE_IN_PLAY_QUOTE 6.2%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 5267, "IDENTITY_AMBIGUOUS": 1128}; ticker orientation: {"VERIFIED": 6395}.

Checks: discipline:AMBIGUOUS 457, discipline:PASS 5938, identity_confidence:AMBIGUOUS 962, identity_confidence:PASS 5433, level_mapping:NA 469, level_mapping:PASS 5926, market_pair:AMBIGUOUS 226, market_pair:NA 153, market_pair:PASS 6016, model_complement:NA 120, model_complement:PASS 6275, namesake:PASS 6395, physical_match_id:NA 2613, physical_match_id:PASS 3782, player_ids:PASS 6395, same_pair_other_event:PASS 6395, ticker_orientation:PASS 6395

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,982 | 1.4% | 1.4% | 0.4% | {"market_freshness": 20, "execution": 8} | 5.29 | 0.2052 / 0.2035 (219) | 16.7% | 0.4% | 5.6% | 1.6% |
| CHALLENGER | 4,640 | 16.8% | 5.7% | 12.2% | {"coverage": 473, "market_freshness": 109, "market_freshness/coverage": 102, "model_calibration_or_unknown": 40, "data": 36, "execution": 12, "model_calibration": 4, "mapping": 4} | 7.13 | 0.2167 / 0.2017 (1082) | 39.4% | 7.5% | 2.2% | 22.1% |
| DOUBLES | 909 | 50.3% | 49.8% | 7.1% | {"execution": 176, "mapping": 137, "market_freshness": 106, "market_freshness/coverage": 31, "coverage": 7} | 24.68 | 0.3344 / 0.2293 (250) | 25.7% | 0.0% | 100.0% | 7.4% |
| ITF_MEN | 8,514 | 23.6% | 15.3% | 31.4% | {"coverage": 841, "execution": 417, "market_freshness": 275, "data": 272, "market_freshness/coverage": 182, "mapping": 22, "model_calibration_or_unknown": 2} | 10.41 | 0.2102 / 0.1933 (2101) | 37.4% | 53.9% | 6.8% | 24.4% |
| ITF_WOMEN | 10,893 | 26.4% | 17.9% | 44.9% | {"coverage": 1167, "execution": 487, "market_freshness": 456, "data": 432, "market_freshness/coverage": 227, "mapping": 68, "model_calibration_or_unknown": 24, "model_calibration": 9} | 12.21 | 0.205 / 0.1935 (2379) | 38.6% | 57.6% | 9.6% | 24.3% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,421 | 6.4% | 5.6% | 1.4% | {"market_freshness": 36, "model_calibration_or_unknown": 20, "data": 11, "market_freshness/coverage": 9, "execution": 6, "model_calibration": 4, "coverage": 4, "mapping": 1} | 7.7 | 0.2224 / 0.2198 (207) | 27.5% | 1.5% | 1.7% | 2.5% |
| WTA125 | 1,088 | 13.4% | 10.3% | 2.3% | {"market_freshness/coverage": 34, "model_calibration_or_unknown": 30, "market_freshness": 29, "data": 22, "coverage": 12, "execution": 9, "model_calibration": 6, "mapping": 4} | 9.17 | 0.2245 / 0.2104 (357) | 24.3% | 8.0% | 4.1% | 10.9% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 5 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 6 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 7 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 8 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 9 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 10 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 11 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 12 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 13 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 14 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 15 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 16 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 18 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 12.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 768 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 19 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 20 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 21 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 22 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 23 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 24 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 25 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 26 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 27 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 28 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 29 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 30 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 31 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 32 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 33 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 189 min (STALE); no external reference |
| 34 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 35 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 36 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 37 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 39 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 253 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 40 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 41 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 22 min (AGING); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 42 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 43 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 44 | `KXITFWMATCH-26OCT08ARISAV-SAV` | ITF_WOMEN | fair_v1 | 75% / 2% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 45 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 230 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 46 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.2h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 141 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 47 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 48 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 49 | `KXITFMATCH-26OCT09DELSTE-DEL` | ITF_MEN | fair_v1 | 78% / 6% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 229 min (STALE); data POOR (grade F, thinner serve sample 477.0, ratio 8.93); no external reference |
| 50 | `KXITFWMATCH-26OCT08ARAWAN-ARA` | ITF_WOMEN | fair_v1 | 77% / 6% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 21.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1321 min (STALE); data POOR (grade D, thinner serve sample 553.0, ratio 3.97); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9815, "by_level_share_of_ge_25pp": {"ATP": 0.0044, "CHALLENGER": 0.122, "DOUBLES": 0.0715, "ITF_MEN": 0.3145, "ITF_WOMEN": 0.4488, "OTHER": 0.0019, "WTA": 0.0142, "WTA125": 0.0228}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5425, "share_primary_cause_market_settled_or_in_play": 0.4833, "share_primary_cause_stale_quote_only": 0.1615}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 6395, "identity_ambiguous_share": 0.1764, "ticker_orientation": {"VERIFIED": 6395}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 3782, "with_external": 104, "coverage": 0.0275, "external_status": {"EXTERNAL_STALE": 72, "AGREES_WITH_KALSHI": 30, "SUPPORTS_MODEL_DIRECTION": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 72, "MODEL_LONE_OUTLIER": 30, "ALL_THREE_DISAGREE": 2}, "share_external_agrees_with_kalshi": 0.2885, "share_external_supports_model": 0.0192}, "pregame_clean_ge_25pp": {"n": 1614, "with_external": 99, "coverage": 0.0613, "external_status": {"EXTERNAL_STALE": 69, "AGREES_WITH_KALSHI": 28, "SUPPORTS_MODEL_DIRECTION": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 69, "MODEL_LONE_OUTLIER": 28, "ALL_THREE_DISAGREE": 2}, "share_external_agrees_with_kalshi": 0.2828, "share_external_supports_model": 0.0202}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 619.0, "median_sample_ratio": 2.31, "median_min_matches": 21.0, "median_max_days_since_last": 197.0, "share_severe_asymmetry": 0.1834, "data_status": {"POOR": 3272, "LIMITED": 1936, "ADEQUATE": 1187}, "comparison_lt_10pp": {"median_thinner_serve_points": 1923.0, "median_sample_ratio": 1.66, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 499, "model_minus_observed": 0.0588, "kalshi_minus_observed": -0.0723, "brier_diff_model_minus_kalshi": 0.0021}, "4-10x": {"n": 339, "model_minus_observed": 0.0641, "kalshi_minus_observed": -0.0767, "brier_diff_model_minus_kalshi": 0.0027}, "<2x": {"n": 1167, "model_minus_observed": 0.0805, "kalshi_minus_observed": -0.0403, "brier_diff_model_minus_kalshi": 0.0109}, ">=10x": {"n": 337, "model_minus_observed": 0.1115, "kalshi_minus_observed": -0.0559, "brier_diff_model_minus_kalshi": 0.0145}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2342, "model": {"intercept": -0.549, "slope": 0.873, "slope_se": 0.052}, "kalshi_mid_same_rows": {"intercept": 0.226, "slope": 1.139, "slope_se": 0.06}, "mean_extremity_model": 0.1847, "mean_extremity_kalshi": 0.1693, "model_brier": 0.2271, "kalshi_brier": 0.201, "brier_diff_model_minus_kalshi": 0.0262, "brier_diff_se": 0.0039, "model_logloss": 0.6498, "kalshi_logloss": 0.5836}, "fair_v1": {"n": 2342, "model": {"intercept": -0.393, "slope": 1.078, "slope_se": 0.058}, "kalshi_mid_same_rows": {"intercept": 0.331, "slope": 1.197, "slope_se": 0.062}, "mean_extremity_model": 0.1694, "mean_extremity_kalshi": 0.1699, "model_brier": 0.2096, "kalshi_brier": 0.2012, "brier_diff_model_minus_kalshi": 0.0084, "brier_diff_se": 0.0031, "model_logloss": 0.606, "kalshi_logloss": 0.5838}, "gen1_elo": {"n": 2342, "model": {"intercept": -0.368, "slope": 1.07, "slope_se": 0.057}, "kalshi_mid_same_rows": {"intercept": 0.337, "slope": 1.185, "slope_se": 0.061}, "mean_extremity_model": 0.1734, "mean_extremity_kalshi": 0.1703, "model_brier": 0.2081, "kalshi_brier": 0.2012, "brier_diff_model_minus_kalshi": 0.0069, "brier_diff_se": 0.003, "model_logloss": 0.6037, "kalshi_logloss": 0.5838}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2414, "share_ge_15": 0.426, "median_abs_gap": 12.69, "n": 15670}, "gen1_elo": {"share_ge_25": 0.2353, "share_ge_15": 0.4218, "median_abs_gap": 12.12, "n": 15670}, "gen1_sr": {"share_ge_25": 0.2931, "share_ge_15": 0.5089, "median_abs_gap": 15.35, "n": 15670}, "gen2": {"share_ge_25": 0.2973, "share_ge_15": 0.4984, "median_abs_gap": 14.95, "n": 15670}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1362, "share_ge_15": 0.3254, "median_abs_gap": 10.12, "n": 11848}, "gen1_elo": {"share_ge_25": 0.134, "share_ge_15": 0.3181, "median_abs_gap": 9.56, "n": 11847}, "gen1_sr": {"share_ge_25": 0.1875, "share_ge_15": 0.4177, "median_abs_gap": 12.48, "n": 11848}, "gen2": {"share_ge_25": 0.2056, "share_ge_15": 0.421, "median_abs_gap": 12.39, "n": 11849}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.29, "share_ge_25_all": 0.0141, "share_ge_25_pregame_clean": 0.0144}, "WTA": {"median_abs_gap_pregame_clean": 7.7, "share_ge_25_all": 0.064, "share_ge_25_pregame_clean": 0.0563}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2428, "share_within_10pp_all": 0.4454, "share_within_10pp_pregame_clean": 0.5086, "corr_model_vs_mid_pregame_clean": 0.8529}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 363, "model_brier": 0.1904, "kalshi_brier": 0.1917, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 421, "model_brier": 0.2111, "kalshi_brier": 0.2047, "brier_diff_model_minus_kalshi": 0.0064}, "15-25": {"n_settled": 497, "model_brier": 0.2257, "kalshi_brier": 0.2131, "brier_diff_model_minus_kalshi": 0.0126}, "25-40": {"n_settled": 273, "model_brier": 0.218, "kalshi_brier": 0.2006, "brier_diff_model_minus_kalshi": 0.0175}, "3-5": {"n_settled": 241, "model_brier": 0.1899, "kalshi_brier": 0.1912, "brier_diff_model_minus_kalshi": -0.0012}, "40+": {"n_settled": 59, "model_brier": 0.2961, "kalshi_brier": 0.17, "brier_diff_model_minus_kalshi": 0.1261}, "5-10": {"n_settled": 488, "model_brier": 0.2006, "kalshi_brier": 0.2022, "brier_diff_model_minus_kalshi": -0.0016}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.549, "slope": 0.873, "slope_se": 0.052}, "kalshi_slope": {"intercept": 0.226, "slope": 1.139, "slope_se": 0.06}, "n": 2342}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.522, "slope": 0.88, "slope_se": 0.038}, "kalshi_slope": {"intercept": 0.144, "slope": 1.084, "slope_se": 0.042}, "n": 4295}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 250, "model_brier": 0.3344, "kalshi_brier": 0.2293, "brier_diff_model_minus_kalshi": 0.1051, "brier_diff_se": 0.0206, "corr_model_outcome": -0.0224, "corr_kalshi_outcome": 0.2891}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
