# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-21T16:50Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 47,537): 0-3 14.1%, 3-5 9.5%, 5-10 19.7%, 10-15 15.3%, 15-25 19.4%, 25-40 14.1%, 40+ 8.1%; median gap 12.1 pp.
* **Where the extremes live**: 97.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.2%, Challenger 12.2%, doubles 6.8%). Main tour: ATP 5.0% and WTA 4.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 10,505): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.2%, BOOK_QUALITY 18.6%, STALE_QUOTE 18.2%, POOR_DATA 9.1%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.5%, LIMITED_DATA 3.7%, IN_PLAY_QUOTE 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%. By class: coverage 34.2%, execution 18.6%, market_freshness 18.2%, data 12.8%, market_freshness/coverage 8.8%, mapping 4.5%, model_calibration_or_unknown 2.2%, model_calibration 0.7%.
* **Stale / settled / in-play**: 51.4% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.0% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 10,505 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.8% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.9% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 492.0 points vs 1696.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.045, Gen-2 0.846, Gen-1 ledger 0.87 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 506 model 0.2247 vs Kalshi 0.2106; n 102 model 0.2915 vs Kalshi 0.1869.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 203,430 model-market comparisons (330,867 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 69,187 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-21T16:41:36.717000+00:00'], shadow board 53,856 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-21T16:41:40.746415+00:00'], Model 4 25,553 rows, 18,395 settled tickers, 6,378 tickers with an external scan.
* By model: {"gen1_ledger": 46727, "gen1_elo": 27081, "fair_v1": 27081, "gen2": 27081, "gen1_sr": 27081, "model4_fundamental": 24203, "model4_conditioned": 24176}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 47,537 | 14.1 | 9.5 | 19.7 | 15.3 | 19.4 | 14.1 | 8.1 | 12.1 | 41.5% | 22.1% |
| MW fair_v1 | 27,081 | 13.0 | 8.5 | 18.3 | 15.7 | 19.9 | 14.9 | 9.6 | 13.16 | 44.5% | 24.6% |
| MW gen1_elo | 27,081 | 12.9 | 8.6 | 19.0 | 15.2 | 20.0 | 15.0 | 9.3 | 12.97 | 44.3% | 24.3% |
| MW gen1_ledger | 20,456 | 15.5 | 10.7 | 21.6 | 14.8 | 18.6 | 12.9 | 6.0 | 10.56 | 37.5% | 18.8% |
| MW gen1_sr | 27,081 | 9.9 | 7.1 | 16.6 | 13.9 | 21.3 | 18.8 | 12.5 | 15.99 | 52.5% | 31.2% |
| MW gen2 | 27,081 | 11.0 | 7.2 | 16.2 | 14.2 | 19.9 | 17.8 | 13.6 | 15.58 | 51.3% | 31.4% |
| all families model4_conditioned | 24,176 | 21.7 | 19.2 | 34.4 | 17.7 | 4.5 | 1.4 | 1.0 | 5.95 | 6.9% | 2.5% |
| all families model4_fundamental | 24,203 | 16.5 | 13.1 | 34.0 | 20.4 | 11.2 | 3.5 | 1.3 | 7.86 | 16.0% | 4.8% |

Configurable thresholds (primary): >=5pp 76.4%, >=10pp 56.8%, >=15pp 41.5%, >=20pp 30.8%, >=25pp 22.1%, >=30pp 15.9%, >=40pp 8.1%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.45pp; >=10pp 45.3%, >=25pp 17.2%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,353 | 28.8 | 13.9 | 24.2 | 14.8 | 12.5 | 5.2 | 0.7 | 6.19 | 18.4% | 5.9% |
| CHALLENGER | 4,371 | 15.7 | 10.0 | 20.3 | 15.8 | 14.8 | 12.5 | 10.9 | 11.18 | 38.3% | 23.5% |
| ITF_MEN | 7,313 | 10.6 | 7.5 | 16.9 | 14.6 | 21.3 | 17.1 | 11.9 | 15.12 | 50.3% | 29.0% |
| ITF_WOMEN | 10,764 | 9.5 | 6.9 | 15.8 | 15.6 | 22.7 | 18.2 | 11.3 | 15.76 | 52.3% | 29.5% |
| WTA | 1,620 | 17.0 | 12.7 | 25.3 | 20.1 | 19.8 | 4.4 | 0.7 | 8.57 | 24.9% | 5.1% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,353 | 23.5 | 14.8 | 24.6 | 17.2 | 13.8 | 5.1 | 0.9 | 6.76 | 19.9% | 6.0% |
| CHALLENGER | 4,371 | 14.7 | 8.4 | 18.7 | 14.7 | 17.6 | 14.1 | 11.9 | 12.68 | 43.5% | 25.9% |
| ITF_MEN | 7,313 | 8.7 | 6.2 | 14.6 | 13.2 | 19.9 | 20.3 | 17.1 | 18.12 | 57.4% | 37.4% |
| ITF_WOMEN | 10,764 | 8.2 | 5.7 | 13.7 | 13.4 | 21.1 | 21.0 | 17.0 | 18.87 | 59.0% | 37.9% |
| WTA | 1,620 | 14.4 | 9.6 | 20.9 | 16.5 | 23.9 | 13.8 | 0.7 | 11.34 | 38.5% | 14.6% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,353 | 24.2 | 12.8 | 24.1 | 15.8 | 15.0 | 7.0 | 1.1 | 7.3 | 23.1% | 8.1% |
| CHALLENGER | 4,371 | 14.1 | 9.5 | 20.8 | 15.2 | 16.4 | 12.8 | 11.2 | 11.42 | 40.4% | 24.0% |
| ITF_MEN | 7,313 | 10.1 | 7.5 | 17.1 | 14.0 | 21.9 | 17.4 | 12.0 | 15.49 | 51.3% | 29.4% |
| ITF_WOMEN | 10,764 | 9.6 | 6.7 | 16.2 | 15.6 | 23.1 | 18.4 | 10.5 | 15.65 | 52.0% | 28.9% |
| WTA | 1,620 | 24.4 | 16.7 | 29.8 | 16.2 | 10.2 | 2.3 | 0.4 | 6.04 | 13.0% | 2.7% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,351 | 26.1 | 19.3 | 30.4 | 11.9 | 8.9 | 3.1 | 0.4 | 5.49 | 12.4% | 3.5% |
| CHALLENGER | 3,034 | 21.3 | 14.9 | 26.7 | 14.0 | 14.7 | 6.6 | 1.9 | 7.27 | 23.2% | 8.5% |
| DOUBLES | 1,495 | 5.3 | 4.2 | 11.6 | 10.2 | 20.6 | 26.3 | 21.8 | 24.07 | 68.7% | 48.1% |
| ITF_MEN | 5,734 | 13.9 | 8.8 | 20.2 | 15.8 | 21.1 | 13.3 | 6.8 | 12.11 | 41.2% | 20.1% |
| ITF_WOMEN | 6,933 | 12.7 | 9.0 | 19.3 | 15.1 | 21.6 | 16.3 | 6.1 | 12.87 | 44.0% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,028 | 22.3 | 15.9 | 29.6 | 18.2 | 10.1 | 3.6 | 0.3 | 6.97 | 14.0% | 3.9% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,291 | 29.1 | 14.1 | 24.6 | 14.6 | 12.3 | 4.8 | 0.5 | 6.01 | 17.5% | 5.3% |
| CHALLENGER | 3,090 | 20.5 | 12.3 | 25.0 | 18.2 | 15.2 | 6.8 | 2.0 | 8.36 | 24.0% | 8.8% |
| ITF_MEN | 5,386 | 12.9 | 9.1 | 20.1 | 16.5 | 22.1 | 14.1 | 5.2 | 12.31 | 41.4% | 19.3% |
| ITF_WOMEN | 8,076 | 11.3 | 8.3 | 17.9 | 17.7 | 24.5 | 15.3 | 5.1 | 13.48 | 44.9% | 20.4% |
| WTA | 1,574 | 17.3 | 12.4 | 25.3 | 20.3 | 19.8 | 4.3 | 0.7 | 8.48 | 24.7% | 5.0% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,291 | 23.9 | 15.1 | 24.8 | 17.0 | 13.8 | 4.8 | 0.7 | 6.55 | 19.2% | 5.4% |
| CHALLENGER | 3,090 | 18.5 | 10.7 | 23.3 | 17.5 | 17.8 | 9.8 | 2.3 | 9.44 | 29.9% | 12.1% |
| ITF_MEN | 5,387 | 10.3 | 7.4 | 16.8 | 14.9 | 21.9 | 18.6 | 10.1 | 15.32 | 50.6% | 28.7% |
| ITF_WOMEN | 8,077 | 9.1 | 6.5 | 15.1 | 15.0 | 23.1 | 20.5 | 10.7 | 16.58 | 54.3% | 31.2% |
| WTA | 1,574 | 14.5 | 9.6 | 20.9 | 16.4 | 23.9 | 13.8 | 0.8 | 11.36 | 38.6% | 14.6% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,310 | 26.3 | 19.5 | 30.5 | 12.1 | 8.4 | 3.0 | 0.2 | 5.4 | 11.6% | 3.2% |
| CHALLENGER | 2,645 | 22.8 | 15.9 | 28.3 | 13.9 | 14.1 | 4.5 | 0.6 | 6.69 | 19.1% | 5.0% |
| DOUBLES | 1,390 | 5.2 | 4.4 | 11.9 | 10.4 | 20.6 | 26.2 | 21.3 | 23.9 | 68.1% | 47.5% |
| ITF_MEN | 4,788 | 15.1 | 9.5 | 22.0 | 16.6 | 21.0 | 11.7 | 4.2 | 11.09 | 36.8% | 15.8% |
| ITF_WOMEN | 5,782 | 13.6 | 9.5 | 20.6 | 15.9 | 21.8 | 15.1 | 3.5 | 11.75 | 40.4% | 18.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 978 | 22.8 | 16.5 | 29.6 | 18.2 | 10.1 | 2.9 | 0.0 | 6.82 | 13.0% | 2.9% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,495 | 5.3 | 4.2 | 11.6 | 10.2 | 20.6 | 26.3 | 21.8 | 24.07 | 68.7% | 48.1% |
| singles | 18,961 | 16.3 | 11.2 | 22.3 | 15.2 | 18.5 | 11.8 | 4.7 | 10.03 | 35.0% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 6,084 | 13.2 | 8.8 | 18.9 | 15.7 | 18.9 | 14.9 | 9.5 | 12.89 | 43.3% | 24.4% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 16,951 | 13.4 | 8.5 | 18.4 | 15.3 | 20.1 | 14.8 | 9.6 | 13.16 | 44.4% | 24.3% |
| UNKNOWN | 3,809 | 11.3 | 7.9 | 17.1 | 17.1 | 20.6 | 15.7 | 10.2 | 13.69 | 46.6% | 25.9% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,627 | 19.8 | 11.6 | 21.2 | 16.6 | 15.8 | 9.0 | 6.1 | 9.23 | 30.9% | 15.1% |
| B | 3,413 | 12.5 | 9.0 | 20.0 | 16.9 | 19.0 | 12.2 | 10.3 | 12.25 | 41.6% | 22.5% |
| C | 3,804 | 11.8 | 8.9 | 19.1 | 15.0 | 19.7 | 15.2 | 10.4 | 13.33 | 45.2% | 25.6% |
| D | 4,415 | 12.2 | 7.9 | 17.0 | 15.6 | 21.9 | 15.7 | 9.7 | 14.03 | 47.4% | 25.5% |
| F | 7,822 | 7.8 | 5.5 | 15.0 | 14.6 | 23.3 | 21.4 | 12.3 | 17.8 | 57.0% | 33.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,756 | 23.0 | 15.8 | 28.8 | 15.1 | 11.8 | 4.1 | 1.5 | 6.68 | 17.3% | 5.6% |
| B | 2,824 | 16.2 | 10.5 | 23.5 | 16.1 | 19.1 | 10.7 | 3.9 | 9.95 | 33.6% | 14.5% |
| C | 4,042 | 11.4 | 7.3 | 18.5 | 14.2 | 21.4 | 16.5 | 10.7 | 14.27 | 48.6% | 27.2% |
| D | 2,928 | 14.4 | 9.8 | 19.7 | 14.4 | 21.0 | 14.4 | 6.2 | 12.04 | 41.6% | 20.6% |
| F | 4,906 | 10.2 | 8.1 | 15.5 | 14.6 | 22.8 | 20.5 | 8.4 | 15.87 | 51.6% | 28.9% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 8,688 | 17.9 | 10.4 | 20.6 | 16.6 | 16.3 | 9.8 | 8.5 | 10.36 | 34.6% | 18.3% |
| LIMITED | 5,894 | 13.6 | 10.2 | 20.2 | 15.6 | 19.2 | 13.5 | 7.6 | 11.86 | 40.4% | 21.1% |
| POOR | 12,499 | 9.4 | 6.4 | 15.8 | 15.0 | 22.8 | 19.2 | 11.4 | 16.13 | 53.3% | 30.6% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,179 | 26.6 | 20.5 | 34.3 | 12.3 | 4.7 | 1.4 | 0.2 | 5.27 | 6.3% | 1.6% |
| GAME_SPREAD | 4,468 | 22.6 | 15.3 | 33.4 | 17.2 | 8.9 | 2.4 | 0.3 | 6.63 | 11.6% | 2.7% |
| MATCH_WINNER | 20,456 | 15.5 | 10.7 | 21.6 | 14.8 | 18.6 | 12.9 | 6.0 | 10.56 | 37.5% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 9,403 | 29.6 | 16.9 | 30.7 | 12.5 | 8.2 | 1.7 | 0.4 | 5.44 | 10.3% | 2.1% |
| TOTAL_GAMES | 7,197 | 8.3 | 9.4 | 36.4 | 29.1 | 10.7 | 3.3 | 2.7 | 9.53 | 16.7% | 6.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,447 | 25.3 | 34.4 | 32.4 | 4.1 | 3.0 | 0.6 | 0.2 | 4.47 | 3.8% | 0.7% |
| GAME_SPREAD | 5,789 | 45.6 | 17.1 | 26.9 | 7.7 | 1.8 | 0.7 | 0.2 | 3.46 | 2.8% | 1.0% |
| TOTAL_GAMES | 9,940 | 4.8 | 7.6 | 40.5 | 35.1 | 7.2 | 2.5 | 2.2 | 9.72 | 12.0% | 4.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,450 | 24.2 | 17.9 | 35.4 | 12.4 | 7.2 | 2.5 | 0.3 | 5.81 | 10.1% | 2.9% |
| GAME_SPREAD | 5,792 | 19.3 | 13.1 | 28.0 | 20.1 | 14.1 | 4.4 | 0.9 | 7.97 | 19.4% | 5.3% |
| TOTAL_GAMES | 9,961 | 8.2 | 9.0 | 36.4 | 27.4 | 12.8 | 3.8 | 2.4 | 9.59 | 19.0% | 6.2% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 27,081 | 44.5% | 24.6% | 13.16 | 36.2% | 15.4% | 10.98 |
| gen1_elo | 27,081 | 44.3% | 24.3% | 12.97 | 35.7% | 15.6% | 10.6 |
| gen1_sr | 27,081 | 52.5% | 31.2% | 15.99 | 44.9% | 22.1% | 13.26 |
| gen2 | 27,081 | 51.3% | 31.4% | 15.58 | 44.8% | 23.6% | 13.18 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 13,989 | 15.8 | 10.3 | 21.1 | 17.2 | 20.4 | 11.9 | 3.3 | 10.8 | 35.5% | 15.2% |
| STALE | 13,092 | 10.0 | 6.6 | 15.3 | 13.9 | 19.5 | 18.2 | 16.4 | 17.01 | 54.1% | 34.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 13,924 | 16.6 | 11.2 | 22.4 | 14.8 | 17.8 | 12.3 | 4.9 | 9.95 | 34.9% | 17.2% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 47,537 | 13924 | 17461 | 16152 | 23.9 | 131.3 | 1400.4 |
| ge_15pp | 19,712 | 4864 | 6259 | 8589 | 25.7 | 418.5 | 1380.4 |
| ge_25pp | 10,505 | 2390 | 2714 | 5401 | 31.4 | 562.2 | 1380.4 |
| lt_10pp | 20,555 | 6992 | 8239 | 5324 | 21.8 | 47.5 | 1341.5 |

Current slate `SL-20261021T165024Z-3f2029e4`: 521 priced rows, quote age at build {'median': 9.0, 'max': 9.1}, freshness {'FRESH': 521}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 22 | 0.0 | 0.0 | 22.7 | 4.5 | 40.9 | 31.8 | 0.0 | 20.48 | 72.7% | 31.8% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,512 | 19.7 | 10.8 | 23.8 | 18.8 | 19.0 | 7.3 | 0.8 | 9.12 | 27.0% | 8.0% |
| KALSHI_LONE_OUTLIER | 17 | 5.9 | 5.9 | 76.5 | 0.0 | 5.9 | 5.9 | 0.0 | 6.11 | 11.8% | 5.9% |
| MARKETS_AGREE | 475 | 65.9 | 34.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.23 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,062 | 0.0 | 2.3 | 33.8 | 26.1 | 26.1 | 10.9 | 0.8 | 12.8 | 37.9% | 11.8% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 27,081 | 4100 (15.1%) | 25.9% | 0.9% | {"EXTERNAL_STALE": 2512, "AGREES_WITH_KALSHI": 1062, "ALL_AGREE": 475, "SUPPORTS_MODEL_DIRECTION": 21, "AGREES_WITH_MODEL": 17, "EXTERNAL_OUTLIER": 12, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 12,049 | 1099 (9.1%) | 36.6% | 1.6% | {"EXTERNAL_STALE": 679, "AGREES_WITH_KALSHI": 402, "SUPPORTS_MODEL_DIRECTION": 16, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 6,653 | 335 (5.0%) | 37.3% | 2.4% | {"EXTERNAL_STALE": 202, "AGREES_WITH_KALSHI": 125, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,252 | 314 (9.7%) | 37.9% | 2.5% | {"EXTERNAL_STALE": 187, "AGREES_WITH_KALSHI": 119, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 10,794 | 2252 (20.9%) | 17.0% | 0.8% | {"EXTERNAL_STALE": 1362, "ALL_AGREE": 475, "AGREES_WITH_KALSHI": 383, "AGREES_WITH_MODEL": 15, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 4, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,173 | 10.6 | 7.7 | 19.3 | 14.5 | 22.2 | 15.8 | 9.9 | 14.02 | 47.9% | 25.7% |
| 4-10x | 3,540 | 11.2 | 8.5 | 18.8 | 15.5 | 21.1 | 14.9 | 10.1 | 13.73 | 46.1% | 25.0% |
| <2x | 13,822 | 15.0 | 9.6 | 18.8 | 16.6 | 18.1 | 13.2 | 8.7 | 11.95 | 39.9% | 21.9% |
| >=10x | 4,546 | 11.2 | 6.3 | 15.2 | 14.1 | 22.1 | 19.3 | 11.8 | 16.23 | 53.2% | 31.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 6,834 | 12.4 | 8.5 | 19.5 | 16.3 | 19.6 | 13.6 | 10.2 | 12.94 | 43.4% | 23.8% |
| 300-1000 | 5,887 | 11.7 | 8.8 | 16.9 | 15.4 | 20.9 | 16.4 | 9.9 | 13.99 | 47.2% | 26.3% |
| <300 | 8,754 | 9.0 | 5.7 | 15.4 | 14.7 | 23.0 | 20.1 | 12.1 | 16.86 | 55.2% | 32.2% |
| >=3000 | 5,606 | 21.6 | 12.8 | 22.8 | 16.6 | 14.6 | 6.9 | 4.8 | 8.03 | 26.3% | 11.7% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 784 | 0.5461 | 0.4091 | 0.5 | +0.046 | -0.091 | -0.0033 ± 0.0055 |
| ratio 4-10x | 542 | 0.5847 | 0.4392 | 0.4945 | +0.090 | -0.055 | 0.0127 ± 0.0069 |
| ratio <2x | 1942 | 0.5366 | 0.4129 | 0.447 | +0.090 | -0.034 | 0.0127 ± 0.0032 |
| ratio >=10x | 692 | 0.5662 | 0.3909 | 0.4624 | +0.104 | -0.072 | 0.0056 ± 0.007 |
| thinner_sample 1000-3000 | 1072 | 0.5412 | 0.414 | 0.4487 | +0.092 | -0.035 | 0.0105 ± 0.0044 |
| thinner_sample 300-1000 | 917 | 0.5652 | 0.4226 | 0.4962 | +0.069 | -0.074 | 0.0004 ± 0.0053 |
| thinner_sample <300 | 1315 | 0.5548 | 0.389 | 0.4608 | +0.094 | -0.072 | 0.0096 ± 0.0049 |
| thinner_sample >=3000 | 656 | 0.5349 | 0.4393 | 0.4665 | +0.068 | -0.027 | 0.013 ± 0.0046 |
| data_status ADEQUATE | 1126 | 0.537 | 0.4309 | 0.4529 | +0.084 | -0.022 | 0.0126 ± 0.0038 |
| data_status LIMITED | 943 | 0.5491 | 0.4166 | 0.4783 | +0.071 | -0.062 | 0.0045 ± 0.0049 |
| data_status POOR | 1891 | 0.5586 | 0.3983 | 0.4691 | +0.090 | -0.071 | 0.0076 ± 0.004 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 582 | 0.1978 | 0.199 | -0.0013 ± 0.0006 | 0.5742 | 0.577 | 0.4982 | 0.4834 | 0.5344 | -0.053 ± 0.0192 | -0.01 (5) |
| 3-5 | 373 | 0.2018 | 0.2011 | +0.0007 ± 0.0019 | 0.5871 | 0.5839 | 0.5014 | 0.4613 | 0.4718 | -0.096 ± 0.0239 | 0.02 (1) |
| 5-10 | 810 | 0.2028 | 0.2023 | +0.0005 ± 0.0024 | 0.5916 | 0.5883 | 0.5126 | 0.438 | 0.4679 | -0.089 ± 0.0165 | -0.0167 (6) |
| 10-15 | 686 | 0.2127 | 0.204 | +0.0088 ± 0.0043 | 0.615 | 0.5894 | 0.5243 | 0.4003 | 0.4257 | -0.099 ± 0.0172 | -0.048 (5) |
| 15-25 | 901 | 0.2233 | 0.2132 | +0.0101 ± 0.006 | 0.6413 | 0.6103 | 0.5749 | 0.3791 | 0.4517 | -0.083 ± 0.0152 | -0.0033 (9) |
| 25-40 | 506 | 0.2247 | 0.2106 | +0.0141 ± 0.0122 | 0.6374 | 0.6052 | 0.6571 | 0.3475 | 0.4763 | -0.073 ± 0.0187 | -0.01 (1) |
| 40+ | 102 | 0.2915 | 0.1869 | +0.1046 ± 0.0378 | 0.7955 | 0.5569 | 0.7502 | 0.3025 | 0.4118 | -0.100 ± 0.037 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2940 | 0.1833 | 0.1843 | -0.0010 ± 0.0003 | 0.5408 | 0.5418 | 0.484 | 0.469 | 0.5044 | -0.021 ± 0.008 | -0.0129 (17) |
| 3-5 | 1937 | 0.199 | 0.1976 | +0.0014 ± 0.0008 | 0.5792 | 0.5724 | 0.4844 | 0.4445 | 0.4455 | -0.056 ± 0.0103 | 0.0 (2) |
| 5-10 | 4120 | 0.198 | 0.1951 | +0.0028 ± 0.001 | 0.5786 | 0.5693 | 0.4822 | 0.4082 | 0.4252 | -0.045 ± 0.007 | -0.0119 (21) |
| 10-15 | 3559 | 0.2012 | 0.1836 | +0.0176 ± 0.0018 | 0.5894 | 0.5397 | 0.4853 | 0.3608 | 0.3521 | -0.072 ± 0.0072 | -0.0281 (16) |
| 15-25 | 4487 | 0.207 | 0.1701 | +0.0369 ± 0.0024 | 0.6072 | 0.5034 | 0.5007 | 0.3042 | 0.3091 | -0.068 ± 0.0061 | -0.0025 (44) |
| 25-40 | 3470 | 0.2242 | 0.131 | +0.0932 ± 0.0038 | 0.6426 | 0.4002 | 0.5326 | 0.2198 | 0.2303 | -0.061 ± 0.0059 | -0.01 (1) |
| 40+ | 2246 | 0.3799 | 0.0445 | +0.3353 ± 0.005 | 0.9891 | 0.1736 | 0.6316 | 0.1068 | 0.0619 | -0.081 ± 0.0042 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 441 | 0.2038 | 0.2043 | -0.0005 ± 0.0007 | 0.5896 | 0.5906 | 0.5042 | 0.4892 | 0.5079 | -0.101 ± 0.0231 | -0.01 (3) |
| 3-5 | 322 | 0.2214 | 0.2202 | +0.0012 ± 0.0021 | 0.6281 | 0.6258 | 0.5134 | 0.4733 | 0.472 | -0.107 ± 0.0282 | 0.02 (1) |
| 5-10 | 699 | 0.2026 | 0.2035 | -0.0009 ± 0.0026 | 0.5898 | 0.5915 | 0.5455 | 0.4707 | 0.515 | -0.071 ± 0.0175 | -0.01 (4) |
| 10-15 | 652 | 0.2167 | 0.2104 | +0.0063 ± 0.0045 | 0.6232 | 0.6067 | 0.5639 | 0.4396 | 0.4785 | -0.099 ± 0.0186 | -0.04 (5) |
| 15-25 | 942 | 0.2296 | 0.2089 | +0.0207 ± 0.0059 | 0.6522 | 0.5999 | 0.5906 | 0.3944 | 0.4437 | -0.100 ± 0.0151 | -0.0133 (9) |
| 25-40 | 661 | 0.261 | 0.201 | +0.0600 ± 0.011 | 0.7289 | 0.5839 | 0.6562 | 0.3405 | 0.4054 | -0.105 ± 0.0171 | -0.0075 (4) |
| 40+ | 243 | 0.36 | 0.1714 | +0.1886 ± 0.0263 | 0.9948 | 0.5131 | 0.7328 | 0.2498 | 0.3086 | -0.076 ± 0.0254 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2483 | 0.194 | 0.1943 | -0.0002 ± 0.0003 | 0.5657 | 0.5659 | 0.5067 | 0.4919 | 0.5091 | -0.041 ± 0.0092 | -0.0133 (15) |
| 3-5 | 1660 | 0.2018 | 0.2014 | +0.0003 ± 0.0009 | 0.5824 | 0.581 | 0.5109 | 0.4709 | 0.4855 | -0.039 ± 0.0112 | 0.02 (1) |
| 5-10 | 3654 | 0.1936 | 0.1928 | +0.0007 ± 0.0011 | 0.5699 | 0.5641 | 0.5034 | 0.4294 | 0.4631 | -0.028 ± 0.0073 | -0.0117 (6) |
| 10-15 | 3204 | 0.1989 | 0.1883 | +0.0107 ± 0.0019 | 0.5848 | 0.5491 | 0.5125 | 0.3883 | 0.4089 | -0.049 ± 0.0078 | -0.0189 (18) |
| 15-25 | 4540 | 0.2157 | 0.1776 | +0.0381 ± 0.0025 | 0.6276 | 0.5224 | 0.5273 | 0.3312 | 0.3348 | -0.071 ± 0.0063 | -0.0086 (42) |
| 25-40 | 4058 | 0.2507 | 0.1405 | +0.1102 ± 0.0037 | 0.7066 | 0.4289 | 0.5619 | 0.2453 | 0.2326 | -0.080 ± 0.0058 | -0.0044 (18) |
| 40+ | 3160 | 0.3961 | 0.0627 | +0.3334 ± 0.0051 | 1.0436 | 0.2224 | 0.6553 | 0.1211 | 0.0889 | -0.070 ± 0.0044 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 555 | 0.1969 | 0.1993 | -0.0024 ± 0.0007 | 0.5735 | 0.5793 | 0.4961 | 0.4809 | 0.555 | -0.014 ± 0.0193 | -0.0137 (8) |
| 3-5 | 403 | 0.1978 | 0.1958 | +0.0020 ± 0.0018 | 0.5744 | 0.5697 | 0.5025 | 0.4629 | 0.4591 | -0.117 ± 0.0229 | 0.0067 (3) |
| 5-10 | 840 | 0.2027 | 0.1992 | +0.0035 ± 0.0023 | 0.5926 | 0.5807 | 0.5102 | 0.4362 | 0.4476 | -0.100 ± 0.0159 | -0.0071 (7) |
| 10-15 | 692 | 0.2098 | 0.2066 | +0.0032 ± 0.0043 | 0.6071 | 0.5961 | 0.5393 | 0.416 | 0.4668 | -0.084 ± 0.0172 | -0.0317 (6) |
| 15-25 | 838 | 0.2304 | 0.2118 | +0.0187 ± 0.0062 | 0.6593 | 0.6065 | 0.5832 | 0.3893 | 0.4379 | -0.107 ± 0.0157 | -0.03 (1) |
| 25-40 | 526 | 0.2139 | 0.2171 | -0.0032 ± 0.0119 | 0.6152 | 0.62 | 0.6666 | 0.3548 | 0.5133 | -0.051 ± 0.0183 | 0.015 (2) |
| 40+ | 106 | 0.3012 | 0.2027 | +0.0985 ± 0.0386 | 0.8237 | 0.5925 | 0.7598 | 0.3095 | 0.434 | -0.081 ± 0.0399 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2862 | 0.1871 | 0.1879 | -0.0008 ± 0.0003 | 0.549 | 0.5504 | 0.491 | 0.4758 | 0.4951 | -0.033 ± 0.0081 | -0.0163 (35) |
| 3-5 | 1951 | 0.1903 | 0.1878 | +0.0026 ± 0.0008 | 0.5588 | 0.5525 | 0.4848 | 0.4453 | 0.4336 | -0.071 ± 0.01 | -0.0094 (18) |
| 5-10 | 4278 | 0.1962 | 0.1905 | +0.0057 ± 0.001 | 0.5764 | 0.5574 | 0.4851 | 0.4112 | 0.4088 | -0.062 ± 0.0067 | -0.01 (31) |
| 10-15 | 3408 | 0.1967 | 0.1803 | +0.0164 ± 0.0018 | 0.5778 | 0.5308 | 0.5007 | 0.3772 | 0.3729 | -0.070 ± 0.0072 | -0.015 (12) |
| 15-25 | 4614 | 0.2105 | 0.1726 | +0.0379 ± 0.0024 | 0.6152 | 0.5092 | 0.5088 | 0.314 | 0.314 | -0.071 ± 0.0061 | -0.03 (2) |
| 25-40 | 3468 | 0.2199 | 0.1332 | +0.0867 ± 0.0039 | 0.6337 | 0.4045 | 0.5359 | 0.2199 | 0.2428 | -0.052 ± 0.0059 | 0.01 (3) |
| 40+ | 2178 | 0.3951 | 0.0496 | +0.3456 ± 0.0054 | 1.0319 | 0.1868 | 0.6445 | 0.1136 | 0.067 | -0.084 ± 0.0045 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 922 | 0.1958 | 0.196 | -0.0002 ± 0.0005 | 0.5711 | 0.5713 | 0.5073 | 0.4922 | 0.4957 | -0.058 ± 0.0148 | -0.0224 (49) |
| 3-5 | 647 | 0.1915 | 0.1909 | +0.0005 ± 0.0014 | 0.5599 | 0.5575 | 0.485 | 0.4452 | 0.456 | -0.052 ± 0.0174 | -0.0194 (34) |
| 5-10 | 1367 | 0.2003 | 0.194 | +0.0063 ± 0.0018 | 0.5893 | 0.5699 | 0.4943 | 0.4209 | 0.4162 | -0.073 ± 0.0121 | -0.005 (78) |
| 10-15 | 898 | 0.2094 | 0.1987 | +0.0106 ± 0.0037 | 0.6068 | 0.5796 | 0.5173 | 0.394 | 0.4109 | -0.064 ± 0.0152 | 0.0014 (64) |
| 15-25 | 1191 | 0.2314 | 0.2105 | +0.0209 ± 0.0052 | 0.6606 | 0.6064 | 0.5725 | 0.3777 | 0.4232 | -0.066 ± 0.0133 | -0.0214 (59) |
| 25-40 | 728 | 0.248 | 0.2051 | +0.0429 ± 0.0103 | 0.7035 | 0.5905 | 0.666 | 0.3533 | 0.4396 | -0.083 ± 0.0157 | -0.0219 (26) |
| 40+ | 248 | 0.3521 | 0.1965 | +0.1557 ± 0.0279 | 1.0173 | 0.5747 | 0.8068 | 0.3228 | 0.4234 | -0.089 ± 0.0251 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3009 | 0.1837 | 0.1838 | -0.0001 ± 0.0003 | 0.5403 | 0.5399 | 0.507 | 0.4917 | 0.4998 | -0.038 ± 0.0079 | -0.0157 (88) |
| 3-5 | 2083 | 0.1907 | 0.1887 | +0.0020 ± 0.0008 | 0.5575 | 0.5534 | 0.4903 | 0.4506 | 0.4455 | -0.054 ± 0.0096 | -0.0209 (69) |
| 5-10 | 4204 | 0.1982 | 0.1894 | +0.0088 ± 0.001 | 0.5819 | 0.5565 | 0.4899 | 0.4164 | 0.3963 | -0.074 ± 0.0068 | -0.0082 (132) |
| 10-15 | 2902 | 0.206 | 0.1911 | +0.0149 ± 0.002 | 0.6005 | 0.561 | 0.5237 | 0.4007 | 0.4011 | -0.061 ± 0.0081 | -0.0053 (105) |
| 15-25 | 3589 | 0.2289 | 0.1981 | +0.0308 ± 0.0029 | 0.6603 | 0.5754 | 0.5653 | 0.37 | 0.3904 | -0.065 ± 0.0075 | -0.0253 (107) |
| 25-40 | 2523 | 0.2583 | 0.183 | +0.0753 ± 0.0054 | 0.7323 | 0.5344 | 0.628 | 0.3136 | 0.3535 | -0.075 ± 0.0083 | -0.0229 (51) |
| 40+ | 1142 | 0.377 | 0.1425 | +0.2344 ± 0.0118 | 1.0702 | 0.4301 | 0.7282 | 0.2243 | 0.2566 | -0.071 ± 0.0105 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3960 | 1.045 ± 0.045 | 1.148 | 0.1676 | 0.1653 | 0.2134 | 0.2052 |
| gen2 | 3960 | 0.846 ± 0.041 | 1.107 | 0.1702 | 0.1658 | 0.2324 | 0.205 |
| gen1_elo | 3960 | 1.022 ± 0.043 | 1.134 | 0.1744 | 0.1654 | 0.2126 | 0.2053 |
| gen1_sr | 3960 | 1.043 ± 0.054 | 1.178 | 0.1309 | 0.1678 | 0.2288 | 0.2046 |
| gen1_ledger | 6001 | 0.87 ± 0.031 | 1.079 | 0.1816 | 0.1801 | 0.2182 | 0.1994 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 19,712)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,493 | 22.8% |
| STALE_QUOTE | market_freshness | 4,175 | 21.2% |
| BOOK_QUALITY | execution | 3,751 | 19.0% |
| POOR_DATA | data | 2,270 | 11.5% |
| LIMITED_DATA | data | 1,278 | 6.5% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,061 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 954 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 827 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 578 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 325 | 1.7% |

Cause class: coverage 22.8%, market_freshness 21.2%, execution 19.0%, data 18.0%, market_freshness/coverage 8.3%, model_calibration_or_unknown 4.8%, mapping 4.2%, model_calibration 1.7%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 94.2%, LOW_DATA_QUALITY 71.0%, THIN_PLAYER_HISTORY 59.7%, STALE_PLAYER_DATA 51.6%, STALE_KALSHI_QUOTE 43.6%, MODEL_INTERNAL_DISAGREEMENT 42.0%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 25.1%, MODEL_HIGH_UNCERTAINTY 17.8%, PLAYER_IDENTITY_RISK 15.9%, LEVEL_TRANSFER_RISK 10.8%, EVENT_MAPPING_RISK 8.1%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 3.2%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.3%, POST_SETTLEMENT_OBSERVATION 22.8%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 10,505)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,588 | 34.2% |
| BOOK_QUALITY | execution | 1,958 | 18.6% |
| STALE_QUOTE | market_freshness | 1,911 | 18.2% |
| POOR_DATA | data | 955 | 9.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 563 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 472 | 4.5% |
| LIMITED_DATA | data | 389 | 3.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 365 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 229 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 75 | 0.7% |

Cause class: coverage 34.2%, execution 18.6%, market_freshness 18.2%, data 12.8%, market_freshness/coverage 8.8%, mapping 4.5%, model_calibration_or_unknown 2.2%, model_calibration 0.7%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.1%, LOW_DATA_QUALITY 74.8%, THIN_PLAYER_HISTORY 62.2%, STALE_KALSHI_QUOTE 51.4%, STALE_PLAYER_DATA 46.6%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 34.5%, WIDE_SPREAD 24.6%, PLAYER_IDENTITY_RISK 19.2%, MODEL_HIGH_UNCERTAINTY 18.0%, EVENT_MAPPING_RISK 9.8%, LEVEL_TRANSFER_RISK 9.7%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 5.0%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.2%, POST_SETTLEMENT_OBSERVATION 34.2%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 8216, "IDENTITY_AMBIGUOUS": 2289}; ticker orientation: {"VERIFIED": 10505}.

Checks: discipline:AMBIGUOUS 719, discipline:PASS 9786, identity_confidence:AMBIGUOUS 2022, identity_confidence:PASS 8483, level_mapping:NA 731, level_mapping:PASS 9774, market_pair:AMBIGUOUS 374, market_pair:NA 257, market_pair:PASS 9874, model_complement:NA 224, model_complement:PASS 10281, namesake:PASS 10505, physical_match_id:NA 3852, physical_match_id:PASS 6653, player_ids:PASS 10505, same_pair_other_event:PASS 10505, ticker_orientation:PASS 10505

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,704 | 5.0% | 4.5% | 1.8% | {"market_freshness": 53, "model_calibration_or_unknown": 43, "data": 35, "execution": 19, "market_freshness/coverage": 13, "model_calibration": 13, "coverage": 9} | 5.86 | 0.228 / 0.2182 (417) | 18.8% | 4.0% | 3.4% | 2.8% |
| CHALLENGER | 7,405 | 17.3% | 7.1% | 12.2% | {"coverage": 720, "market_freshness/coverage": 158, "market_freshness": 147, "data": 127, "model_calibration_or_unknown": 59, "execution": 30, "model_calibration": 27, "mapping": 15} | 7.45 | 0.2178 / 0.207 (1784) | 35.1% | 17.4% | 3.9% | 22.6% |
| DOUBLES | 1,495 | 48.1% | 47.5% | 6.8% | {"execution": 368, "mapping": 186, "market_freshness": 106, "market_freshness/coverage": 52, "coverage": 7} | 23.9 | 0.317 / 0.2354 (383) | 15.7% | 0.0% | 100.0% | 7.0% |
| ITF_MEN | 13,047 | 25.1% | 17.7% | 31.2% | {"coverage": 1204, "execution": 650, "market_freshness": 540, "data": 446, "market_freshness/coverage": 274, "mapping": 158, "model_calibration_or_unknown": 2, "model_calibration": 1} | 11.71 | 0.2138 / 0.1953 (2957) | 36.8% | 67.6% | 18.2% | 22.0% |
| ITF_WOMEN | 17,697 | 26.8% | 19.7% | 45.1% | {"coverage": 1628, "market_freshness": 987, "execution": 860, "data": 702, "market_freshness/coverage": 382, "mapping": 107, "model_calibration_or_unknown": 57, "model_calibration": 11} | 12.84 | 0.2029 / 0.1949 (3455) | 38.6% | 57.2% | 10.0% | 21.7% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,648 | 4.7% | 4.2% | 1.2% | {"market_freshness": 38, "model_calibration_or_unknown": 27, "execution": 17, "model_calibration": 12, "data": 11, "market_freshness/coverage": 10, "coverage": 7, "mapping": 1} | 7.88 | 0.2379 / 0.2309 (435) | 24.1% | 1.3% | 1.4% | 3.6% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.7% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 15 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 16 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 17 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 18 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 19 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 20 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 21 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 22 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 271 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 23 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 24 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 25 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 26 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 27 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 28 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 463 min (STALE); no external reference |
| 29 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 30 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 31 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 32 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 33 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 34 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 22.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1345 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 36 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 37 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 38 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 39 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 41 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 468 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 42 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 43 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 44 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 45 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 46 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 47 | `KXITFWMATCH-26OCT20CHAAPI-CHA` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 122.0, ratio 20.3); no external reference |
| 48 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 535 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |
| 49 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 547 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 50 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9706, "by_level_share_of_ge_25pp": {"ATP": 0.0176, "CHALLENGER": 0.1221, "DOUBLES": 0.0684, "ITF_MEN": 0.3118, "ITF_WOMEN": 0.4506, "OTHER": 0.0011, "WTA": 0.0117, "WTA125": 0.0166}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5141, "share_primary_cause_market_settled_or_in_play": 0.4299, "share_primary_cause_stale_quote_only": 0.1819}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 10505, "identity_ambiguous_share": 0.2179, "ticker_orientation": {"VERIFIED": 10505}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 6653, "with_external": 335, "coverage": 0.0504, "external_status": {"EXTERNAL_STALE": 202, "AGREES_WITH_KALSHI": 125, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 202, "MODEL_LONE_OUTLIER": 125, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3731, "share_external_supports_model": 0.0239}, "pregame_clean_ge_25pp": {"n": 3252, "with_external": 314, "coverage": 0.0966, "external_status": {"EXTERNAL_STALE": 187, "AGREES_WITH_KALSHI": 119, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 187, "MODEL_LONE_OUTLIER": 119, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.379, "share_external_supports_model": 0.0255}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 492.0, "median_sample_ratio": 2.44, "median_min_matches": 20.0, "median_max_days_since_last": 225.0, "share_severe_asymmetry": 0.2109, "data_status": {"POOR": 5854, "LIMITED": 2828, "ADEQUATE": 1823}, "comparison_lt_10pp": {"median_thinner_serve_points": 1696.0, "median_sample_ratio": 1.7, "median_min_matches": 92.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 784, "model_minus_observed": 0.0461, "kalshi_minus_observed": -0.0909, "brier_diff_model_minus_kalshi": -0.0033}, "4-10x": {"n": 542, "model_minus_observed": 0.0902, "kalshi_minus_observed": -0.0553, "brier_diff_model_minus_kalshi": 0.0127}, "<2x": {"n": 1942, "model_minus_observed": 0.0896, "kalshi_minus_observed": -0.0341, "brier_diff_model_minus_kalshi": 0.0127}, ">=10x": {"n": 692, "model_minus_observed": 0.1038, "kalshi_minus_observed": -0.0716, "brier_diff_model_minus_kalshi": 0.0056}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3960, "model": {"intercept": -0.534, "slope": 0.846, "slope_se": 0.041}, "kalshi_mid_same_rows": {"intercept": 0.235, "slope": 1.107, "slope_se": 0.046}, "mean_extremity_model": 0.1702, "mean_extremity_kalshi": 0.1658, "model_brier": 0.2324, "kalshi_brier": 0.205, "brier_diff_model_minus_kalshi": 0.0274, "brier_diff_se": 0.003, "model_logloss": 0.6613, "kalshi_logloss": 0.5926}, "fair_v1": {"n": 3960, "model": {"intercept": -0.403, "slope": 1.045, "slope_se": 0.045}, "kalshi_mid_same_rows": {"intercept": 0.317, "slope": 1.148, "slope_se": 0.047}, "mean_extremity_model": 0.1676, "mean_extremity_kalshi": 0.1653, "model_brier": 0.2134, "kalshi_brier": 0.2052, "brier_diff_model_minus_kalshi": 0.0083, "brier_diff_se": 0.0025, "model_logloss": 0.6151, "kalshi_logloss": 0.5928}, "gen1_elo": {"n": 3960, "model": {"intercept": -0.392, "slope": 1.022, "slope_se": 0.043}, "kalshi_mid_same_rows": {"intercept": 0.319, "slope": 1.134, "slope_se": 0.046}, "mean_extremity_model": 0.1744, "mean_extremity_kalshi": 0.1654, "model_brier": 0.2126, "kalshi_brier": 0.2053, "brier_diff_model_minus_kalshi": 0.0073, "brier_diff_se": 0.0025, "model_logloss": 0.6139, "kalshi_logloss": 0.5931}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2457, "share_ge_15": 0.4449, "median_abs_gap": 13.16, "n": 27081}, "gen1_elo": {"share_ge_25": 0.2432, "share_ge_15": 0.4429, "median_abs_gap": 12.97, "n": 27081}, "gen1_sr": {"share_ge_25": 0.3123, "share_ge_15": 0.5252, "median_abs_gap": 15.99, "n": 27081}, "gen2": {"share_ge_25": 0.3145, "share_ge_15": 0.5132, "median_abs_gap": 15.58, "n": 27081}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1545, "share_ge_15": 0.3616, "median_abs_gap": 10.98, "n": 21051}, "gen1_elo": {"share_ge_25": 0.1556, "share_ge_15": 0.3572, "median_abs_gap": 10.6, "n": 21048}, "gen1_sr": {"share_ge_25": 0.2209, "share_ge_15": 0.4492, "median_abs_gap": 13.26, "n": 21052}, "gen2": {"share_ge_25": 0.2362, "share_ge_15": 0.4476, "median_abs_gap": 13.18, "n": 21053}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.86, "share_ge_25_all": 0.0499, "share_ge_25_pregame_clean": 0.0453}, "WTA": {"median_abs_gap_pregame_clean": 7.88, "share_ge_25_all": 0.0465, "share_ge_25_pregame_clean": 0.0415}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2355, "share_within_10pp_all": 0.4324, "share_within_10pp_pregame_clean": 0.4844, "corr_model_vs_mid_pregame_clean": 0.8441}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 582, "model_brier": 0.1978, "kalshi_brier": 0.199, "brier_diff_model_minus_kalshi": -0.0013}, "10-15": {"n_settled": 686, "model_brier": 0.2127, "kalshi_brier": 0.204, "brier_diff_model_minus_kalshi": 0.0088}, "15-25": {"n_settled": 901, "model_brier": 0.2233, "kalshi_brier": 0.2132, "brier_diff_model_minus_kalshi": 0.0101}, "25-40": {"n_settled": 506, "model_brier": 0.2247, "kalshi_brier": 0.2106, "brier_diff_model_minus_kalshi": 0.0141}, "3-5": {"n_settled": 373, "model_brier": 0.2018, "kalshi_brier": 0.2011, "brier_diff_model_minus_kalshi": 0.0007}, "40+": {"n_settled": 102, "model_brier": 0.2915, "kalshi_brier": 0.1869, "brier_diff_model_minus_kalshi": 0.1046}, "5-10": {"n_settled": 810, "model_brier": 0.2028, "kalshi_brier": 0.2023, "brier_diff_model_minus_kalshi": 0.0005}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.534, "slope": 0.846, "slope_se": 0.041}, "kalshi_slope": {"intercept": 0.235, "slope": 1.107, "slope_se": 0.046}, "n": 3960}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.511, "slope": 0.87, "slope_se": 0.031}, "kalshi_slope": {"intercept": 0.158, "slope": 1.079, "slope_se": 0.036}, "n": 6001}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 383, "model_brier": 0.317, "kalshi_brier": 0.2354, "brier_diff_model_minus_kalshi": 0.0816, "brier_diff_se": 0.0159, "corr_model_outcome": 0.0216, "corr_kalshi_outcome": 0.2558}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
