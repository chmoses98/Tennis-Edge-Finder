# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-11T06:31Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 28,382): 0-3 14.6%, 3-5 9.7%, 5-10 20.1%, 10-15 15.4%, 15-25 18.4%, 25-40 13.6%, 40+ 8.2%; median gap 11.71 pp.
* **Where the extremes live**: 98.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.6%, Challenger 11.8%, doubles 7.3%). Main tour: ATP 1.5% and WTA 7.2% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 6,170): MARKET_ALREADY_SETTLED_WHEN_PRICED 39.4%, BOOK_QUALITY 17.1%, STALE_QUOTE 16.5%, POOR_DATA 8.0%, POSSIBLY_IN_PLAY_QUOTE 5.5%, LIMITED_DATA 4.3%, IDENTITY_AMBIGUOUS 3.7%, IN_PLAY_QUOTE 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.8%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.3%. By class: coverage 39.4%, execution 17.1%, market_freshness 16.5%, data 12.3%, market_freshness/coverage 8.8%, mapping 3.7%, model_calibration_or_unknown 1.8%, model_calibration 0.3%.
* **Stale / settled / in-play**: 54.9% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 48.2% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 6,170 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 17.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 2.4%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 18.9% of the time and with the model 0.3%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 629.0 points vs 1893.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.058, Gen-2 0.857, Gen-1 ledger 0.876 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 258 model 0.2194 vs Kalshi 0.2008; n 57 model 0.2912 vs Kalshi 0.167.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 112,402 model-market comparisons (184,923 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 42,343 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-11T06:23:46.093820+00:00'], shadow board 29,743 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-11T06:23:49.713211+00:00'], Model 4 12,547 rows, 12,340 settled tickers, 3,482 tickers with an external scan.
* By model: {"gen1_ledger": 27833, "gen1_elo": 14944, "fair_v1": 14944, "gen2": 14944, "gen1_sr": 14944, "model4_fundamental": 12401, "model4_conditioned": 12392}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 28,382 | 14.6 | 9.7 | 20.1 | 15.4 | 18.4 | 13.6 | 8.2 | 11.71 | 40.2% | 21.7% |
| MW fair_v1 | 14,944 | 13.8 | 8.7 | 18.6 | 16.2 | 18.4 | 14.5 | 9.8 | 12.71 | 42.6% | 24.2% |
| MW gen1_elo | 14,944 | 13.3 | 9.1 | 20.2 | 15.1 | 18.7 | 14.3 | 9.3 | 12.18 | 42.3% | 23.6% |
| MW gen1_ledger | 13,438 | 15.5 | 10.8 | 21.7 | 14.5 | 18.5 | 12.6 | 6.4 | 10.5 | 37.5% | 19.0% |
| MW gen1_sr | 14,944 | 10.2 | 7.9 | 16.5 | 14.5 | 21.5 | 18.0 | 11.4 | 15.39 | 51.0% | 29.4% |
| MW gen2 | 14,944 | 12.1 | 7.3 | 16.4 | 14.3 | 20.0 | 17.0 | 12.9 | 14.97 | 49.9% | 29.9% |
| all families model4_conditioned | 12,392 | 22.1 | 20.2 | 35.9 | 15.8 | 4.2 | 0.9 | 0.9 | 5.71 | 5.9% | 1.8% |
| all families model4_fundamental | 12,401 | 16.7 | 13.4 | 35.9 | 19.7 | 10.6 | 2.5 | 1.2 | 7.58 | 14.3% | 3.6% |

Configurable thresholds (primary): >=5pp 75.7%, >=10pp 55.6%, >=15pp 40.2%, >=20pp 30.0%, >=25pp 21.7%, >=30pp 15.9%, >=40pp 8.2%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.3pp; >=10pp 44.9%, >=25pp 17.5%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,223 | 30.7 | 14.1 | 25.2 | 16.9 | 11.0 | 1.1 | 0.9 | 5.84 | 13.1% | 2.0% |
| CHALLENGER | 2,514 | 16.0 | 10.7 | 19.1 | 16.3 | 13.6 | 12.4 | 12.0 | 11.62 | 38.0% | 24.4% |
| ITF_MEN | 4,237 | 11.5 | 8.8 | 18.5 | 14.9 | 19.2 | 15.2 | 11.9 | 13.62 | 46.3% | 27.1% |
| ITF_WOMEN | 5,887 | 10.2 | 6.7 | 16.0 | 16.4 | 21.6 | 18.5 | 10.6 | 15.29 | 50.6% | 29.0% |
| WTA | 672 | 22.3 | 10.7 | 25.4 | 16.1 | 17.4 | 6.4 | 1.6 | 7.92 | 25.4% | 8.0% |
| WTA125 | 411 | 12.4 | 7.3 | 23.4 | 23.4 | 16.6 | 15.1 | 1.9 | 11.31 | 33.6% | 17.0% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,223 | 24.1 | 14.2 | 24.8 | 18.8 | 15.1 | 1.9 | 1.1 | 6.9 | 18.1% | 2.9% |
| CHALLENGER | 2,514 | 15.5 | 7.6 | 18.9 | 13.5 | 18.1 | 13.8 | 12.6 | 12.87 | 44.5% | 26.5% |
| ITF_MEN | 4,237 | 10.4 | 7.5 | 16.8 | 14.8 | 20.0 | 17.8 | 12.7 | 15.29 | 50.5% | 30.5% |
| ITF_WOMEN | 5,887 | 8.9 | 5.9 | 12.9 | 12.9 | 21.4 | 20.9 | 17.1 | 19.05 | 59.4% | 38.0% |
| WTA | 672 | 20.1 | 7.6 | 18.4 | 14.9 | 21.0 | 16.4 | 1.6 | 12.12 | 39.0% | 18.0% |
| WTA125 | 411 | 4.6 | 3.2 | 18.5 | 19.9 | 24.6 | 19.0 | 10.2 | 16.84 | 53.8% | 29.2% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,223 | 26.8 | 14.5 | 29.4 | 15.0 | 10.7 | 2.6 | 1.0 | 6.29 | 14.3% | 3.6% |
| CHALLENGER | 2,514 | 15.6 | 10.6 | 20.4 | 15.3 | 14.4 | 11.8 | 11.9 | 10.75 | 38.1% | 23.8% |
| ITF_MEN | 4,237 | 10.5 | 8.8 | 19.2 | 13.8 | 20.0 | 15.5 | 12.1 | 13.94 | 47.7% | 27.6% |
| ITF_WOMEN | 5,887 | 9.9 | 6.7 | 16.7 | 15.7 | 22.8 | 18.8 | 9.4 | 15.46 | 50.9% | 28.2% |
| WTA | 672 | 22.3 | 14.4 | 33.8 | 16.2 | 9.4 | 2.8 | 1.0 | 6.62 | 13.2% | 3.9% |
| WTA125 | 411 | 23.4 | 10.7 | 30.4 | 15.6 | 13.4 | 6.1 | 0.5 | 7.6 | 20.0% | 6.6% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 675 | 31.4 | 23.3 | 34.2 | 9.3 | 1.3 | 0.4 | 0.0 | 4.62 | 1.8% | 0.4% |
| CHALLENGER | 1,693 | 23.4 | 16.7 | 26.8 | 13.9 | 12.3 | 5.0 | 1.8 | 6.55 | 19.2% | 6.9% |
| DOUBLES | 874 | 4.2 | 3.1 | 10.5 | 11.1 | 19.8 | 25.4 | 25.9 | 25.71 | 71.0% | 51.3% |
| ITF_MEN | 4,084 | 15.0 | 8.6 | 21.2 | 15.4 | 20.4 | 12.1 | 7.4 | 11.68 | 39.8% | 19.5% |
| ITF_WOMEN | 4,823 | 11.7 | 9.3 | 19.7 | 14.6 | 22.4 | 16.7 | 5.6 | 13.01 | 44.7% | 22.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 557 | 22.4 | 14.0 | 25.9 | 17.4 | 14.0 | 5.8 | 0.5 | 7.91 | 20.3% | 6.3% |
| WTA125 | 583 | 19.6 | 13.9 | 21.8 | 18.5 | 15.3 | 8.4 | 2.6 | 8.61 | 26.2% | 11.0% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,212 | 30.6 | 13.9 | 25.3 | 17.0 | 11.1 | 1.2 | 0.9 | 5.86 | 13.1% | 2.1% |
| CHALLENGER | 1,813 | 20.7 | 13.5 | 24.0 | 19.0 | 14.1 | 6.1 | 2.5 | 8.15 | 22.8% | 8.7% |
| ITF_MEN | 3,006 | 14.3 | 11.1 | 22.1 | 16.6 | 19.1 | 11.9 | 4.9 | 10.63 | 35.8% | 16.8% |
| ITF_WOMEN | 4,181 | 12.7 | 8.4 | 18.8 | 19.1 | 23.1 | 14.5 | 3.2 | 12.58 | 40.9% | 17.8% |
| WTA | 667 | 22.2 | 10.8 | 25.6 | 16.0 | 17.4 | 6.3 | 1.6 | 7.89 | 25.3% | 8.0% |
| WTA125 | 396 | 12.9 | 7.6 | 22.5 | 23.7 | 16.9 | 15.2 | 1.3 | 11.31 | 33.3% | 16.4% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,212 | 23.9 | 14.3 | 24.8 | 18.8 | 15.2 | 1.9 | 1.1 | 6.9 | 18.1% | 3.0% |
| CHALLENGER | 1,813 | 20.0 | 9.8 | 23.6 | 16.3 | 18.5 | 9.2 | 2.6 | 9.02 | 30.3% | 11.8% |
| ITF_MEN | 3,007 | 12.4 | 9.1 | 19.5 | 16.6 | 21.6 | 14.9 | 5.8 | 12.49 | 42.3% | 20.7% |
| ITF_WOMEN | 4,181 | 10.5 | 7.1 | 14.7 | 14.1 | 24.0 | 19.6 | 10.0 | 16.27 | 53.6% | 29.6% |
| WTA | 667 | 20.1 | 7.7 | 18.4 | 15.0 | 20.8 | 16.3 | 1.6 | 12.12 | 38.8% | 18.0% |
| WTA125 | 396 | 4.8 | 3.3 | 18.4 | 20.4 | 24.2 | 19.4 | 9.3 | 16.74 | 53.0% | 28.8% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 655 | 31.4 | 23.5 | 34.5 | 9.5 | 0.6 | 0.5 | 0.0 | 4.61 | 1.1% | 0.5% |
| CHALLENGER | 1,456 | 25.3 | 18.5 | 29.0 | 13.6 | 11.5 | 2.0 | 0.1 | 5.89 | 13.7% | 2.1% |
| DOUBLES | 807 | 4.2 | 3.1 | 10.8 | 11.2 | 19.9 | 25.3 | 25.5 | 25.6 | 70.8% | 50.8% |
| ITF_MEN | 3,301 | 16.7 | 9.5 | 23.5 | 16.4 | 20.1 | 9.6 | 4.2 | 10.05 | 34.0% | 13.9% |
| ITF_WOMEN | 3,945 | 12.8 | 10.1 | 21.6 | 15.4 | 22.7 | 14.9 | 2.5 | 11.56 | 40.1% | 17.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 527 | 23.0 | 14.6 | 26.4 | 17.5 | 14.2 | 4.4 | 0.0 | 7.52 | 18.6% | 4.4% |
| WTA125 | 496 | 21.8 | 15.3 | 23.4 | 20.8 | 13.5 | 4.8 | 0.4 | 7.42 | 18.8% | 5.2% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 874 | 4.2 | 3.1 | 10.5 | 11.1 | 19.8 | 25.4 | 25.9 | 25.71 | 71.0% | 51.3% |
| singles | 12,564 | 16.3 | 11.3 | 22.5 | 14.8 | 18.4 | 11.7 | 5.0 | 9.96 | 35.1% | 16.7% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 3,395 | 13.7 | 9.6 | 20.3 | 16.1 | 16.5 | 13.8 | 10.2 | 12.04 | 40.4% | 24.0% |
| Grass | 33 | 12.1 | 30.3 | 12.1 | 12.1 | 18.2 | 15.2 | 0.0 | 7.35 | 33.3% | 15.2% |
| Hard | 10,038 | 14.3 | 8.5 | 18.5 | 16.0 | 18.8 | 14.4 | 9.6 | 12.75 | 42.8% | 24.0% |
| UNKNOWN | 1,478 | 11.4 | 8.2 | 15.8 | 17.9 | 20.2 | 16.4 | 10.1 | 13.98 | 46.7% | 26.5% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,590 | 20.1 | 10.6 | 21.1 | 17.1 | 14.8 | 8.9 | 7.3 | 9.45 | 31.0% | 16.2% |
| B | 2,018 | 14.8 | 9.4 | 19.4 | 17.3 | 17.1 | 12.0 | 10.0 | 11.43 | 39.1% | 22.0% |
| C | 2,253 | 12.8 | 9.8 | 19.4 | 15.0 | 18.9 | 14.9 | 9.3 | 12.69 | 43.1% | 24.1% |
| D | 2,727 | 10.8 | 8.4 | 17.8 | 16.2 | 22.0 | 14.9 | 9.9 | 13.92 | 46.8% | 24.8% |
| F | 3,356 | 7.8 | 5.3 | 15.0 | 15.1 | 20.7 | 22.9 | 13.3 | 18.26 | 56.9% | 36.2% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,937 | 22.8 | 16.1 | 28.1 | 15.1 | 11.6 | 4.6 | 1.7 | 6.72 | 17.9% | 6.3% |
| B | 2,104 | 15.3 | 9.8 | 23.9 | 16.2 | 19.1 | 11.3 | 4.3 | 10.18 | 34.8% | 15.6% |
| C | 2,700 | 12.0 | 7.7 | 17.8 | 14.2 | 20.8 | 16.0 | 11.5 | 14.14 | 48.3% | 27.5% |
| D | 2,142 | 14.2 | 9.6 | 21.3 | 13.2 | 21.7 | 13.9 | 6.1 | 11.84 | 41.7% | 20.0% |
| F | 2,555 | 9.3 | 7.6 | 14.6 | 13.6 | 23.7 | 21.3 | 9.9 | 16.91 | 54.9% | 31.2% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 5,075 | 18.6 | 9.8 | 20.1 | 17.1 | 15.0 | 9.9 | 9.6 | 10.45 | 34.5% | 19.5% |
| LIMITED | 3,745 | 15.0 | 10.6 | 20.6 | 16.0 | 18.1 | 12.9 | 6.8 | 11.16 | 37.9% | 19.7% |
| POOR | 6,124 | 9.2 | 6.8 | 16.2 | 15.6 | 21.3 | 19.2 | 11.7 | 15.94 | 52.2% | 30.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,784 | 30.8 | 24.7 | 36.5 | 5.6 | 1.8 | 0.5 | 0.1 | 4.54 | 2.4% | 0.6% |
| GAME_SPREAD | 2,698 | 25.4 | 15.8 | 36.8 | 17.0 | 4.4 | 0.4 | 0.2 | 6.08 | 5.0% | 0.6% |
| MATCH_WINNER | 13,438 | 15.5 | 10.8 | 21.7 | 14.5 | 18.5 | 12.6 | 6.4 | 10.5 | 37.5% | 19.0% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 4,914 | 33.4 | 19.4 | 30.8 | 9.6 | 5.4 | 1.2 | 0.2 | 4.72 | 6.8% | 1.4% |
| TOTAL_GAMES | 3,975 | 6.9 | 9.1 | 38.8 | 30.2 | 10.0 | 2.7 | 2.4 | 9.53 | 15.1% | 5.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,519 | 25.5 | 37.7 | 31.7 | 0.3 | 4.2 | 0.5 | 0.1 | 4.33 | 4.8% | 0.6% |
| GAME_SPREAD | 3,203 | 44.8 | 15.3 | 29.8 | 7.7 | 1.2 | 0.8 | 0.4 | 3.65 | 2.4% | 1.2% |
| TOTAL_GAMES | 4,670 | 3.3 | 6.7 | 44.1 | 36.4 | 6.2 | 1.3 | 2.0 | 9.59 | 9.5% | 3.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,519 | 25.8 | 18.7 | 36.9 | 9.4 | 6.6 | 2.2 | 0.3 | 5.55 | 9.2% | 2.6% |
| GAME_SPREAD | 3,203 | 18.9 | 13.1 | 30.2 | 20.9 | 13.8 | 2.5 | 0.8 | 7.89 | 17.0% | 3.2% |
| TOTAL_GAMES | 4,679 | 6.5 | 8.4 | 38.9 | 28.9 | 12.4 | 2.7 | 2.2 | 9.6 | 17.3% | 4.9% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 14,944 | 42.6% | 24.2% | 12.71 | 32.5% | 13.7% | 10.14 |
| gen1_elo | 14,944 | 42.3% | 23.6% | 12.18 | 31.8% | 13.4% | 9.58 |
| gen1_sr | 14,944 | 51.0% | 29.4% | 15.39 | 41.8% | 18.9% | 12.52 |
| gen2 | 14,944 | 49.9% | 29.9% | 14.97 | 42.1% | 20.8% | 12.42 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 7,767 | 16.9 | 11.0 | 21.7 | 17.7 | 18.5 | 11.0 | 3.2 | 10.09 | 32.7% | 14.2% |
| STALE | 7,177 | 10.6 | 6.3 | 15.3 | 14.6 | 18.2 | 18.2 | 16.9 | 16.86 | 53.3% | 35.1% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 6,906 | 17.8 | 11.9 | 23.6 | 14.3 | 16.7 | 11.2 | 4.6 | 9.18 | 32.4% | 15.7% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 28,382 | 6906 | 11239 | 10237 | 24.4 | 151.7 | 1400.4 |
| ge_15pp | 11,405 | 2238 | 3831 | 5336 | 28.3 | 455.5 | 1380.4 |
| ge_25pp | 6,170 | 1086 | 1697 | 3387 | 35.5 | 579.5 | 1380.4 |
| lt_10pp | 12,606 | 3682 | 5481 | 3443 | 22.8 | 49.5 | 1341.5 |

Current slate `SL-20261011T063143Z-6edb8ede`: 623 priced rows, quote age at build {'median': 8.5, 'max': 8.5}, freshness {'FRESH': 623}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 4 | 0.0 | 0.0 | 25.0 | 0.0 | 75.0 | 0.0 | 0.0 | 20.45 | 75.0% | 0.0% |
| EXTERNAL_LONE_OUTLIER | 7 | 57.1 | 42.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 978 | 24.0 | 11.6 | 22.8 | 18.9 | 16.4 | 6.0 | 0.3 | 7.89 | 22.7% | 6.3% |
| KALSHI_LONE_OUTLIER | 1 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 5.14 | 0.0% | 0.0% |
| MARKETS_AGREE | 164 | 75.0 | 25.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.94 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 269 | 0.0 | 4.5 | 35.3 | 33.1 | 18.2 | 8.6 | 0.4 | 11.28 | 27.1% | 8.9% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 14,944 | 1423 (9.5%) | 18.9% | 0.3% | {"EXTERNAL_STALE": 978, "AGREES_WITH_KALSHI": 269, "ALL_AGREE": 164, "EXTERNAL_OUTLIER": 7, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_15pp | 6,368 | 298 (4.7%) | 24.5% | 1.0% | {"EXTERNAL_STALE": 222, "AGREES_WITH_KALSHI": 73, "SUPPORTS_MODEL_DIRECTION": 3} |
| fair_v1_ge_25pp | 3,622 | 86 (2.4%) | 27.9% | 0.0% | {"EXTERNAL_STALE": 62, "AGREES_WITH_KALSHI": 24} |
| fair_v1_ge_25pp_pregame_clean | 1,547 | 84 (5.4%) | 28.6% | 0.0% | {"EXTERNAL_STALE": 60, "AGREES_WITH_KALSHI": 24} |
| fair_v1_lt_10pp | 6,155 | 851 (13.8%) | 12.6% | 0.1% | {"EXTERNAL_STALE": 571, "ALL_AGREE": 164, "AGREES_WITH_KALSHI": 107, "EXTERNAL_OUTLIER": 7, "ALL_DISAGREE": 1, "AGREES_WITH_MODEL": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,012 | 11.7 | 8.5 | 19.8 | 15.4 | 20.9 | 13.9 | 9.9 | 13.04 | 44.6% | 23.8% |
| 4-10x | 2,045 | 11.3 | 9.1 | 18.9 | 15.2 | 19.9 | 16.2 | 9.2 | 13.37 | 45.4% | 25.5% |
| <2x | 8,025 | 15.9 | 9.2 | 18.8 | 17.2 | 16.8 | 12.8 | 9.3 | 11.79 | 38.9% | 22.1% |
| >=10x | 1,862 | 11.2 | 6.6 | 15.7 | 14.1 | 19.6 | 20.6 | 12.2 | 16.13 | 52.4% | 32.8% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 3,954 | 14.1 | 8.6 | 19.4 | 16.0 | 18.5 | 12.8 | 10.8 | 12.39 | 42.0% | 23.6% |
| 300-1000 | 3,583 | 11.9 | 9.0 | 17.0 | 16.2 | 20.9 | 16.0 | 9.1 | 13.67 | 46.0% | 25.1% |
| <300 | 3,867 | 8.4 | 6.2 | 15.8 | 15.0 | 20.8 | 20.9 | 12.8 | 17.02 | 54.5% | 33.8% |
| >=3000 | 3,540 | 21.5 | 11.5 | 22.5 | 17.7 | 13.1 | 7.7 | 6.0 | 8.48 | 26.8% | 13.7% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 471 | 0.5385 | 0.406 | 0.4777 | +0.061 | -0.072 | 0.0029 ± 0.0068 |
| ratio 4-10x | 323 | 0.5814 | 0.4396 | 0.5232 | +0.058 | -0.084 | 0.0005 ± 0.0087 |
| ratio <2x | 1087 | 0.5407 | 0.4197 | 0.4535 | +0.087 | -0.034 | 0.0125 ± 0.0043 |
| ratio >=10x | 306 | 0.5496 | 0.3817 | 0.4346 | +0.115 | -0.053 | 0.0173 ± 0.01 |
| thinner_sample 1000-3000 | 602 | 0.5444 | 0.4209 | 0.4618 | +0.083 | -0.041 | 0.0082 ± 0.0058 |
| thinner_sample 300-1000 | 581 | 0.5665 | 0.4256 | 0.4923 | +0.074 | -0.067 | 0.002 ± 0.0065 |
| thinner_sample <300 | 619 | 0.5433 | 0.3834 | 0.4556 | +0.088 | -0.072 | 0.0126 ± 0.0068 |
| thinner_sample >=3000 | 385 | 0.5302 | 0.4371 | 0.4519 | +0.078 | -0.015 | 0.017 ± 0.0057 |
| data_status ADEQUATE | 616 | 0.5314 | 0.4304 | 0.4464 | +0.085 | -0.016 | 0.0131 ± 0.0048 |
| data_status LIMITED | 585 | 0.5579 | 0.426 | 0.4855 | +0.072 | -0.059 | 0.0032 ± 0.0062 |
| data_status POOR | 986 | 0.5513 | 0.3975 | 0.4675 | +0.084 | -0.070 | 0.0107 ± 0.0053 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 342 | 0.1931 | 0.1945 | -0.0014 ± 0.0008 | 0.5638 | 0.5674 | 0.4916 | 0.4768 | 0.5234 | -0.052 ± 0.0249 | -0.01 (3) |
| 3-5 | 226 | 0.1894 | 0.1905 | -0.0012 ± 0.0023 | 0.5589 | 0.5598 | 0.5124 | 0.4725 | 0.5044 | -0.059 ± 0.0294 | 0.02 (1) |
| 5-10 | 449 | 0.2014 | 0.2022 | -0.0008 ± 0.0032 | 0.5888 | 0.5907 | 0.5222 | 0.448 | 0.4833 | -0.084 ± 0.0221 | -0.0125 (4) |
| 10-15 | 397 | 0.2139 | 0.2059 | +0.0080 ± 0.0057 | 0.6159 | 0.593 | 0.5184 | 0.3946 | 0.4207 | -0.095 ± 0.0228 | -0.0633 (3) |
| 15-25 | 458 | 0.229 | 0.2149 | +0.0142 ± 0.0085 | 0.6537 | 0.6176 | 0.5755 | 0.3799 | 0.441 | -0.084 ± 0.0216 | -0.0133 (6) |
| 25-40 | 258 | 0.2194 | 0.2008 | +0.0186 ± 0.0165 | 0.6282 | 0.5769 | 0.6472 | 0.3388 | 0.4612 | -0.072 ± 0.0248 | -0.01 (1) |
| 40+ | 57 | 0.2912 | 0.167 | +0.1242 ± 0.0482 | 0.7869 | 0.5063 | 0.7464 | 0.3009 | 0.386 | -0.132 ± 0.0468 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1703 | 0.1731 | 0.174 | -0.0009 ± 0.0003 | 0.517 | 0.5181 | 0.4756 | 0.4609 | 0.4956 | -0.022 ± 0.0102 | -0.0188 (8) |
| 3-5 | 1074 | 0.1923 | 0.1891 | +0.0032 ± 0.0011 | 0.5661 | 0.5536 | 0.4797 | 0.4401 | 0.4162 | -0.081 ± 0.0135 | 0.02 (1) |
| 5-10 | 2298 | 0.1959 | 0.1932 | +0.0027 ± 0.0014 | 0.5747 | 0.5664 | 0.4897 | 0.416 | 0.4321 | -0.051 ± 0.0093 | -0.0082 (17) |
| 10-15 | 2062 | 0.2013 | 0.1826 | +0.0187 ± 0.0024 | 0.5885 | 0.5364 | 0.474 | 0.3494 | 0.3366 | -0.079 ± 0.0094 | -0.0475 (4) |
| 15-25 | 2365 | 0.2032 | 0.1659 | +0.0372 ± 0.0033 | 0.598 | 0.4933 | 0.4951 | 0.2987 | 0.3032 | -0.069 ± 0.0084 | -0.0048 (29) |
| 25-40 | 1968 | 0.2187 | 0.1225 | +0.0962 ± 0.0049 | 0.6302 | 0.3793 | 0.5267 | 0.213 | 0.2195 | -0.062 ± 0.0076 | -0.01 (1) |
| 40+ | 1348 | 0.3726 | 0.0437 | +0.3289 ± 0.0063 | 0.9705 | 0.1738 | 0.6227 | 0.1058 | 0.0564 | -0.085 ± 0.0053 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 263 | 0.1955 | 0.1959 | -0.0004 ± 0.0009 | 0.573 | 0.5744 | 0.4941 | 0.4793 | 0.4905 | -0.085 ± 0.0288 | -0.01 (1) |
| 3-5 | 174 | 0.2094 | 0.2098 | -0.0005 ± 0.0028 | 0.6001 | 0.6029 | 0.5236 | 0.4836 | 0.5057 | -0.061 ± 0.0364 | 0.02 (1) |
| 5-10 | 387 | 0.1963 | 0.1936 | +0.0027 ± 0.0034 | 0.5749 | 0.5687 | 0.5615 | 0.4867 | 0.5039 | -0.087 ± 0.0231 | -0.01 (4) |
| 10-15 | 369 | 0.2159 | 0.2065 | +0.0094 ± 0.006 | 0.6184 | 0.5992 | 0.5778 | 0.4529 | 0.4824 | -0.099 ± 0.0245 | -0.05 (4) |
| 15-25 | 528 | 0.227 | 0.2091 | +0.0178 ± 0.0079 | 0.6434 | 0.6009 | 0.5996 | 0.4025 | 0.4621 | -0.085 ± 0.0204 | -0.01 (5) |
| 25-40 | 340 | 0.2743 | 0.2021 | +0.0722 ± 0.0154 | 0.7699 | 0.5844 | 0.6733 | 0.3589 | 0.4029 | -0.135 ± 0.0243 | -0.025 (2) |
| 40+ | 126 | 0.3464 | 0.1881 | +0.1584 ± 0.0376 | 0.9703 | 0.5511 | 0.7614 | 0.2824 | 0.373 | -0.065 ± 0.0361 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1503 | 0.1768 | 0.1771 | -0.0003 ± 0.0004 | 0.526 | 0.527 | 0.4921 | 0.4777 | 0.4997 | -0.033 ± 0.0112 | -0.0217 (6) |
| 3-5 | 921 | 0.1943 | 0.1933 | +0.0010 ± 0.0012 | 0.563 | 0.5609 | 0.522 | 0.4821 | 0.4886 | -0.044 ± 0.0147 | 0.02 (1) |
| 5-10 | 2032 | 0.1868 | 0.1831 | +0.0037 ± 0.0014 | 0.5549 | 0.5422 | 0.5143 | 0.4408 | 0.4557 | -0.048 ± 0.0096 | -0.01 (5) |
| 10-15 | 1785 | 0.1963 | 0.1808 | +0.0155 ± 0.0025 | 0.5789 | 0.5305 | 0.5188 | 0.3943 | 0.3972 | -0.068 ± 0.0102 | -0.02 (14) |
| 15-25 | 2542 | 0.2152 | 0.1749 | +0.0403 ± 0.0033 | 0.6256 | 0.5169 | 0.5346 | 0.339 | 0.3375 | -0.076 ± 0.0084 | -0.0026 (27) |
| 25-40 | 2259 | 0.2497 | 0.1371 | +0.1126 ± 0.005 | 0.7102 | 0.4174 | 0.5617 | 0.2454 | 0.2271 | -0.089 ± 0.0078 | -0.015 (6) |
| 40+ | 1776 | 0.4056 | 0.0673 | +0.3383 ± 0.007 | 1.0624 | 0.2367 | 0.6695 | 0.1313 | 0.1002 | -0.072 ± 0.006 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 342 | 0.1946 | 0.1973 | -0.0028 ± 0.0009 | 0.5679 | 0.5753 | 0.4994 | 0.4842 | 0.5585 | -0.007 ± 0.0242 | -0.0133 (6) |
| 3-5 | 240 | 0.1886 | 0.1876 | +0.0010 ± 0.0022 | 0.5534 | 0.5507 | 0.4974 | 0.458 | 0.4667 | -0.104 ± 0.0294 | -0.01 (1) |
| 5-10 | 488 | 0.2007 | 0.1985 | +0.0022 ± 0.003 | 0.5893 | 0.5819 | 0.5098 | 0.4361 | 0.4529 | -0.092 ± 0.0209 | -0.01 (4) |
| 10-15 | 368 | 0.2158 | 0.2141 | +0.0017 ± 0.006 | 0.6217 | 0.6119 | 0.5373 | 0.415 | 0.4701 | -0.074 ± 0.0239 | -0.044 (5) |
| 15-25 | 438 | 0.2308 | 0.2094 | +0.0214 ± 0.0085 | 0.6624 | 0.6039 | 0.5809 | 0.3876 | 0.4292 | -0.105 ± 0.0216 | -0.03 (1) |
| 25-40 | 262 | 0.2021 | 0.2048 | -0.0027 ± 0.0163 | 0.5869 | 0.588 | 0.652 | 0.3405 | 0.4962 | -0.046 ± 0.024 | 0.0 (1) |
| 40+ | 49 | 0.3106 | 0.1697 | +0.1409 ± 0.0534 | 0.834 | 0.5113 | 0.7427 | 0.2906 | 0.3673 | -0.138 ± 0.0533 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1607 | 0.1824 | 0.1834 | -0.0010 ± 0.0004 | 0.5379 | 0.5398 | 0.4822 | 0.4671 | 0.5016 | -0.021 ± 0.0107 | -0.0183 (23) |
| 3-5 | 1122 | 0.1835 | 0.1813 | +0.0022 ± 0.001 | 0.5421 | 0.5368 | 0.475 | 0.4358 | 0.4269 | -0.072 ± 0.0132 | -0.0243 (7) |
| 5-10 | 2475 | 0.1904 | 0.1851 | +0.0053 ± 0.0013 | 0.5645 | 0.5473 | 0.481 | 0.4072 | 0.4081 | -0.061 ± 0.0087 | -0.01 (18) |
| 10-15 | 1904 | 0.1982 | 0.1826 | +0.0155 ± 0.0024 | 0.5815 | 0.5344 | 0.4926 | 0.3695 | 0.3666 | -0.072 ± 0.0097 | -0.03 (9) |
| 15-25 | 2508 | 0.2077 | 0.1691 | +0.0385 ± 0.0032 | 0.6102 | 0.5018 | 0.4977 | 0.3023 | 0.303 | -0.070 ± 0.0083 | -0.03 (2) |
| 25-40 | 1920 | 0.212 | 0.1173 | +0.0947 ± 0.0049 | 0.6145 | 0.3651 | 0.5209 | 0.2038 | 0.2161 | -0.059 ± 0.0074 | 0.0 (1) |
| 40+ | 1282 | 0.3861 | 0.0452 | +0.3408 ± 0.0067 | 1.0084 | 0.1783 | 0.63 | 0.107 | 0.0538 | -0.088 ± 0.0056 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 635 | 0.2037 | 0.204 | -0.0003 ± 0.0006 | 0.5906 | 0.5908 | 0.5008 | 0.4858 | 0.4929 | -0.042 ± 0.0179 | -0.0226 (46) |
| 3-5 | 471 | 0.1999 | 0.1985 | +0.0014 ± 0.0016 | 0.5811 | 0.5759 | 0.4799 | 0.4404 | 0.4416 | -0.053 ± 0.0205 | -0.0058 (33) |
| 5-10 | 957 | 0.1928 | 0.187 | +0.0057 ± 0.0021 | 0.5699 | 0.5551 | 0.4793 | 0.4058 | 0.4054 | -0.061 ± 0.0142 | -0.0049 (73) |
| 10-15 | 620 | 0.2045 | 0.1945 | +0.0100 ± 0.0044 | 0.5976 | 0.5707 | 0.4901 | 0.3672 | 0.3871 | -0.045 ± 0.0177 | 0.0014 (64) |
| 15-25 | 828 | 0.2355 | 0.2094 | +0.0262 ± 0.0062 | 0.6708 | 0.6042 | 0.553 | 0.3586 | 0.3901 | -0.058 ± 0.016 | -0.0216 (58) |
| 25-40 | 467 | 0.2497 | 0.187 | +0.0627 ± 0.0125 | 0.7025 | 0.5479 | 0.6339 | 0.3203 | 0.3747 | -0.083 ± 0.0187 | -0.0216 (25) |
| 40+ | 157 | 0.3608 | 0.1894 | +0.1714 ± 0.0356 | 1.0507 | 0.5579 | 0.7856 | 0.2918 | 0.3885 | -0.064 ± 0.0319 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1965 | 0.1933 | 0.1933 | -0.0000 ± 0.0004 | 0.564 | 0.5627 | 0.5018 | 0.4865 | 0.4911 | -0.038 ± 0.0099 | -0.0155 (82) |
| 3-5 | 1375 | 0.1894 | 0.1866 | +0.0029 ± 0.0009 | 0.5536 | 0.5471 | 0.4897 | 0.4502 | 0.4356 | -0.060 ± 0.0117 | -0.0148 (63) |
| 5-10 | 2757 | 0.1908 | 0.1827 | +0.0081 ± 0.0012 | 0.5653 | 0.5429 | 0.4752 | 0.4015 | 0.3874 | -0.066 ± 0.0082 | -0.0087 (125) |
| 10-15 | 1860 | 0.201 | 0.1866 | +0.0144 ± 0.0025 | 0.5891 | 0.5516 | 0.5038 | 0.3806 | 0.3833 | -0.056 ± 0.0099 | -0.0053 (105) |
| 15-25 | 2378 | 0.2313 | 0.1977 | +0.0335 ± 0.0036 | 0.6678 | 0.5749 | 0.5471 | 0.352 | 0.365 | -0.061 ± 0.0092 | -0.0255 (106) |
| 25-40 | 1637 | 0.2486 | 0.1628 | +0.0858 ± 0.0063 | 0.7062 | 0.484 | 0.5977 | 0.2828 | 0.306 | -0.072 ± 0.0096 | -0.0206 (47) |
| 40+ | 791 | 0.3809 | 0.1197 | +0.2612 ± 0.0132 | 1.0777 | 0.3708 | 0.6964 | 0.1885 | 0.1972 | -0.069 ± 0.0116 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2187 | 1.058 ± 0.06 | 1.172 | 0.1693 | 0.1699 | 0.2114 | 0.202 |
| gen2 | 2187 | 0.857 ± 0.053 | 1.114 | 0.1858 | 0.1693 | 0.2287 | 0.2021 |
| gen1_elo | 2187 | 1.053 ± 0.059 | 1.161 | 0.173 | 0.1704 | 0.2096 | 0.2021 |
| gen1_sr | 2187 | 1.047 ± 0.068 | 1.192 | 0.1439 | 0.1717 | 0.224 | 0.2019 |
| gen1_ledger | 4135 | 0.876 ± 0.039 | 1.065 | 0.1736 | 0.1888 | 0.2184 | 0.1966 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 11,405)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,090 | 27.1% |
| STALE_QUOTE | market_freshness | 2,287 | 20.1% |
| BOOK_QUALITY | execution | 2,007 | 17.6% |
| POOR_DATA | data | 1,202 | 10.5% |
| LIMITED_DATA | data | 898 | 7.9% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 622 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 522 | 4.6% |
| IDENTITY_AMBIGUOUS | mapping | 368 | 3.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 336 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 73 | 0.6% |

Cause class: coverage 27.1%, market_freshness 20.1%, data 18.4%, execution 17.6%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.6%, mapping 3.2%, model_calibration 0.6%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.0%, START_UNVERIFIABLE 96.0%, LOW_DATA_QUALITY 68.0%, STALE_PLAYER_DATA 57.0%, THIN_PLAYER_HISTORY 56.1%, STALE_KALSHI_QUOTE 46.8%, MODEL_INTERNAL_DISAGREEMENT 37.2%, ASYMMETRIC_SAMPLE_SIZE 30.1%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 16.3%, PLAYER_IDENTITY_RISK 11.6%, LEVEL_TRANSFER_RISK 8.8%, EVENT_MAPPING_RISK 8.1%, LOW_DISPLAYED_LIQUIDITY 7.4%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 1.0%, UNKNOWN 0.6%, EXTERNAL_MARKET_CONFIRMATION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 29.6%, POST_SETTLEMENT_OBSERVATION 27.1%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### >= ge_25 pp (N = 6,170)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,430 | 39.4% |
| BOOK_QUALITY | execution | 1,057 | 17.1% |
| STALE_QUOTE | market_freshness | 1,019 | 16.5% |
| POOR_DATA | data | 493 | 8.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 337 | 5.5% |
| LIMITED_DATA | data | 264 | 4.3% |
| IDENTITY_AMBIGUOUS | mapping | 229 | 3.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 209 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 112 | 1.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 20 | 0.3% |

Cause class: coverage 39.4%, execution 17.1%, market_freshness 16.5%, data 12.3%, market_freshness/coverage 8.8%, mapping 3.7%, model_calibration_or_unknown 1.8%, model_calibration 0.3%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.5%, START_UNVERIFIABLE 98.1%, LOW_DATA_QUALITY 71.4%, THIN_PLAYER_HISTORY 58.1%, STALE_KALSHI_QUOTE 54.9%, STALE_PLAYER_DATA 51.5%, MODEL_INTERNAL_DISAGREEMENT 38.5%, ASYMMETRIC_SAMPLE_SIZE 31.9%, WIDE_SPREAD 23.2%, MODEL_HIGH_UNCERTAINTY 17.7%, PLAYER_IDENTITY_RISK 14.8%, EVENT_MAPPING_RISK 10.0%, LOW_DISPLAYED_LIQUIDITY 7.5%, LEVEL_TRANSFER_RISK 7.5%, MODEL_CALIBRATION_OUTLIER 4.5%, EXTERNAL_MARKET_REJECTION 0.5%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 42.2%, POST_SETTLEMENT_OBSERVATION 39.4%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.7%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 5093, "IDENTITY_AMBIGUOUS": 1077}; ticker orientation: {"VERIFIED": 6170}.

Checks: discipline:AMBIGUOUS 448, discipline:PASS 5722, identity_confidence:AMBIGUOUS 913, identity_confidence:PASS 5257, level_mapping:NA 460, level_mapping:PASS 5710, market_pair:AMBIGUOUS 222, market_pair:NA 141, market_pair:PASS 5807, model_complement:NA 108, model_complement:PASS 6062, namesake:PASS 6170, physical_match_id:NA 2548, physical_match_id:PASS 3622, player_ids:PASS 6170, same_pair_other_event:PASS 6170, ticker_orientation:PASS 6170

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,898 | 1.5% | 1.5% | 0.4% | {"market_freshness": 20, "execution": 8} | 5.24 | 0.2059 / 0.2036 (205) | 17.1% | 0.1% | 5.9% | 1.6% |
| CHALLENGER | 4,207 | 17.3% | 5.8% | 11.8% | {"coverage": 455, "market_freshness": 108, "market_freshness/coverage": 87, "model_calibration_or_unknown": 39, "data": 26, "execution": 12, "model_calibration": 3} | 6.8 | 0.2242 / 0.2062 (948) | 42.0% | 5.2% | 1.8% | 22.3% |
| DOUBLES | 874 | 51.3% | 50.8% | 7.3% | {"execution": 168, "mapping": 136, "market_freshness": 106, "market_freshness/coverage": 31, "coverage": 7} | 25.6 | 0.3269 / 0.2291 (245) | 26.8% | 0.0% | 100.0% | 7.7% |
| ITF_MEN | 8,321 | 23.4% | 15.2% | 31.5% | {"coverage": 814, "execution": 399, "data": 272, "market_freshness": 271, "market_freshness/coverage": 169, "mapping": 19, "model_calibration_or_unknown": 1} | 10.36 | 0.2101 / 0.1936 (2055) | 37.6% | 53.4% | 6.3% | 24.2% |
| ITF_WOMEN | 10,710 | 26.0% | 17.6% | 45.1% | {"coverage": 1137, "execution": 453, "market_freshness": 449, "data": 428, "market_freshness/coverage": 218, "mapping": 68, "model_calibration_or_unknown": 22, "model_calibration": 9} | 12.14 | 0.2056 / 0.1925 (2321) | 38.6% | 57.1% | 9.5% | 24.1% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,229 | 7.2% | 6.4% | 1.4% | {"market_freshness": 36, "model_calibration_or_unknown": 20, "data": 11, "market_freshness/coverage": 9, "model_calibration": 4, "execution": 4, "coverage": 4, "mapping": 1} | 7.77 | 0.2178 / 0.2162 (197) | 29.1% | 1.7% | 1.2% | 2.9% |
| WTA125 | 994 | 13.5% | 10.2% | 2.2% | {"market_freshness/coverage": 31, "model_calibration_or_unknown": 28, "market_freshness": 27, "data": 20, "coverage": 12, "execution": 8, "mapping": 4, "model_calibration": 4} | 9.31 | 0.2353 / 0.2197 (309) | 24.6% | 7.5% | 3.8% | 10.3% |

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
| 12 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 13 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 14 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 15 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 16 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 9.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 553 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 18 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 19 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 20 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 21 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 22 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 874 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 23 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
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
| 34 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 110 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 35 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 36 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 37 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 799 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 38 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 39 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 40 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 41 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 42 | `KXITFWMATCH-26OCT08ARISAV-SAV` | ITF_WOMEN | fair_v1 | 75% / 2% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 43 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 826 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 44 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 687 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 45 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 46 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 47 | `KXITFMATCH-26OCT09DELSTE-DEL` | ITF_MEN | fair_v1 | 78% / 6% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 229 min (STALE); data POOR (grade F, thinner serve sample 477.0, ratio 8.93); no external reference |
| 48 | `KXITFWMATCH-26OCT08ARAWAN-ARA` | ITF_WOMEN | fair_v1 | 77% / 6% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 341 min (STALE); data POOR (grade D, thinner serve sample 553.0, ratio 3.97); no external reference |
| 49 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 708 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 50 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9809, "by_level_share_of_ge_25pp": {"ATP": 0.0045, "CHALLENGER": 0.1183, "DOUBLES": 0.0726, "ITF_MEN": 0.3152, "ITF_WOMEN": 0.4512, "OTHER": 0.0019, "WTA": 0.0144, "WTA125": 0.0217}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5489, "share_primary_cause_market_settled_or_in_play": 0.4823, "share_primary_cause_stale_quote_only": 0.1652}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 6170, "identity_ambiguous_share": 0.1746, "ticker_orientation": {"VERIFIED": 6170}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 3622, "with_external": 86, "coverage": 0.0237, "external_status": {"EXTERNAL_STALE": 62, "AGREES_WITH_KALSHI": 24}, "triangulation": {"INSUFFICIENT_INPUTS": 62, "MODEL_LONE_OUTLIER": 24}, "share_external_agrees_with_kalshi": 0.2791, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 1547, "with_external": 84, "coverage": 0.0543, "external_status": {"EXTERNAL_STALE": 60, "AGREES_WITH_KALSHI": 24}, "triangulation": {"INSUFFICIENT_INPUTS": 60, "MODEL_LONE_OUTLIER": 24}, "share_external_agrees_with_kalshi": 0.2857, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 629.0, "median_sample_ratio": 2.29, "median_min_matches": 21.0, "median_max_days_since_last": 197.0, "share_severe_asymmetry": 0.1746, "data_status": {"POOR": 3133, "LIMITED": 1895, "ADEQUATE": 1142}, "comparison_lt_10pp": {"median_thinner_serve_points": 1893.0, "median_sample_ratio": 1.67, "median_min_matches": 85.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 471, "model_minus_observed": 0.0608, "kalshi_minus_observed": -0.0717, "brier_diff_model_minus_kalshi": 0.0029}, "4-10x": {"n": 323, "model_minus_observed": 0.0582, "kalshi_minus_observed": -0.0836, "brier_diff_model_minus_kalshi": 0.0005}, "<2x": {"n": 1087, "model_minus_observed": 0.0871, "kalshi_minus_observed": -0.0338, "brier_diff_model_minus_kalshi": 0.0125}, ">=10x": {"n": 306, "model_minus_observed": 0.1149, "kalshi_minus_observed": -0.053, "brier_diff_model_minus_kalshi": 0.0173}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2187, "model": {"intercept": -0.551, "slope": 0.857, "slope_se": 0.053}, "kalshi_mid_same_rows": {"intercept": 0.209, "slope": 1.114, "slope_se": 0.061}, "mean_extremity_model": 0.1858, "mean_extremity_kalshi": 0.1693, "model_brier": 0.2287, "kalshi_brier": 0.2021, "brier_diff_model_minus_kalshi": 0.0267, "brier_diff_se": 0.004, "model_logloss": 0.6537, "kalshi_logloss": 0.5864}, "fair_v1": {"n": 2187, "model": {"intercept": -0.403, "slope": 1.058, "slope_se": 0.06}, "kalshi_mid_same_rows": {"intercept": 0.308, "slope": 1.172, "slope_se": 0.063}, "mean_extremity_model": 0.1693, "mean_extremity_kalshi": 0.1699, "model_brier": 0.2114, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0093, "brier_diff_se": 0.0032, "model_logloss": 0.6101, "kalshi_logloss": 0.5861}, "gen1_elo": {"n": 2187, "model": {"intercept": -0.377, "slope": 1.053, "slope_se": 0.059}, "kalshi_mid_same_rows": {"intercept": 0.315, "slope": 1.161, "slope_se": 0.062}, "mean_extremity_model": 0.173, "mean_extremity_kalshi": 0.1704, "model_brier": 0.2096, "kalshi_brier": 0.2021, "brier_diff_model_minus_kalshi": 0.0076, "brier_diff_se": 0.0031, "model_logloss": 0.6073, "kalshi_logloss": 0.5861}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2424, "share_ge_15": 0.4261, "median_abs_gap": 12.71, "n": 14944}, "gen1_elo": {"share_ge_25": 0.2357, "share_ge_15": 0.4231, "median_abs_gap": 12.18, "n": 14944}, "gen1_sr": {"share_ge_25": 0.2945, "share_ge_15": 0.5099, "median_abs_gap": 15.39, "n": 14944}, "gen2": {"share_ge_25": 0.2991, "share_ge_15": 0.4989, "median_abs_gap": 14.97, "n": 14944}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1372, "share_ge_15": 0.3246, "median_abs_gap": 10.14, "n": 11275}, "gen1_elo": {"share_ge_25": 0.134, "share_ge_15": 0.3183, "median_abs_gap": 9.58, "n": 11274}, "gen1_sr": {"share_ge_25": 0.1891, "share_ge_15": 0.4182, "median_abs_gap": 12.52, "n": 11275}, "gen2": {"share_ge_25": 0.2079, "share_ge_15": 0.4215, "median_abs_gap": 12.42, "n": 11276}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.24, "share_ge_25_all": 0.0148, "share_ge_25_pregame_clean": 0.015}, "WTA": {"median_abs_gap_pregame_clean": 7.77, "share_ge_25_all": 0.0724, "share_ge_25_pregame_clean": 0.0637}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2433, "share_within_10pp_all": 0.4442, "share_within_10pp_pregame_clean": 0.5079, "corr_model_vs_mid_pregame_clean": 0.8527}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 342, "model_brier": 0.1931, "kalshi_brier": 0.1945, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 397, "model_brier": 0.2139, "kalshi_brier": 0.2059, "brier_diff_model_minus_kalshi": 0.008}, "15-25": {"n_settled": 458, "model_brier": 0.229, "kalshi_brier": 0.2149, "brier_diff_model_minus_kalshi": 0.0142}, "25-40": {"n_settled": 258, "model_brier": 0.2194, "kalshi_brier": 0.2008, "brier_diff_model_minus_kalshi": 0.0186}, "3-5": {"n_settled": 226, "model_brier": 0.1894, "kalshi_brier": 0.1905, "brier_diff_model_minus_kalshi": -0.0012}, "40+": {"n_settled": 57, "model_brier": 0.2912, "kalshi_brier": 0.167, "brier_diff_model_minus_kalshi": 0.1242}, "5-10": {"n_settled": 449, "model_brier": 0.2014, "kalshi_brier": 0.2022, "brier_diff_model_minus_kalshi": -0.0008}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.551, "slope": 0.857, "slope_se": 0.053}, "kalshi_slope": {"intercept": 0.209, "slope": 1.114, "slope_se": 0.061}, "n": 2187}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.533, "slope": 0.876, "slope_se": 0.039}, "kalshi_slope": {"intercept": 0.124, "slope": 1.065, "slope_se": 0.043}, "n": 4135}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 245, "model_brier": 0.3269, "kalshi_brier": 0.2291, "brier_diff_model_minus_kalshi": 0.0977, "brier_diff_se": 0.0205, "corr_model_outcome": -0.0011, "corr_kalshi_outcome": 0.295}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
