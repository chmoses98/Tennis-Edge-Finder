# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-14T05:30Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 32,040): 0-3 14.5%, 3-5 9.5%, 5-10 20.2%, 10-15 15.4%, 15-25 18.7%, 25-40 13.5%, 40+ 8.1%; median gap 11.73 pp.
* **Where the extremes live**: 98.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.2%, Challenger 12.5%, doubles 7.0%). Main tour: ATP 1.4% and WTA 6.3% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 6,928): MARKET_ALREADY_SETTLED_WHEN_PRICED 37.8%, BOOK_QUALITY 17.8%, STALE_QUOTE 16.4%, POOR_DATA 8.3%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IDENTITY_AMBIGUOUS 4.4%, LIMITED_DATA 4.1%, IN_PLAY_QUOTE 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.4%. By class: coverage 37.8%, execution 17.8%, market_freshness 16.4%, data 12.4%, market_freshness/coverage 8.8%, mapping 4.4%, model_calibration_or_unknown 2.0%, model_calibration 0.4%.
* **Stale / settled / in-play**: 53.1% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 46.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 6,928 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 3.4%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 21.3% of the time and with the model 0.6%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 578.0 points vs 1856.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.068, Gen-2 0.875, Gen-1 ledger 0.881 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 312 model 0.2229 vs Kalshi 0.2077; n 68 model 0.2909 vs Kalshi 0.1768.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 127,363 model-market comparisons (210,606 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 46,168 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-14T05:20:44.388339+00:00'], shadow board 34,507 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-14T05:20:48.121326+00:00'], Model 4 13,972 rows, 13,850 settled tickers, 4,368 tickers with an external scan.
* By model: {"gen1_ledger": 30362, "gen1_elo": 17342, "fair_v1": 17342, "gen2": 17342, "gen1_sr": 17342, "model4_fundamental": 13821, "model4_conditioned": 13812}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 32,040 | 14.5 | 9.5 | 20.2 | 15.4 | 18.7 | 13.5 | 8.1 | 11.73 | 40.3% | 21.6% |
| MW fair_v1 | 17,342 | 13.7 | 8.6 | 18.8 | 16.0 | 18.9 | 14.4 | 9.7 | 12.77 | 43.0% | 24.1% |
| MW gen1_elo | 17,342 | 13.3 | 9.1 | 20.1 | 15.2 | 18.8 | 14.3 | 9.2 | 12.25 | 42.3% | 23.5% |
| MW gen1_ledger | 14,698 | 15.5 | 10.7 | 22.0 | 14.7 | 18.4 | 12.4 | 6.3 | 10.47 | 37.2% | 18.7% |
| MW gen1_sr | 17,342 | 9.9 | 7.8 | 16.5 | 14.3 | 21.8 | 18.1 | 11.6 | 15.52 | 51.5% | 29.7% |
| MW gen2 | 17,342 | 11.8 | 7.3 | 16.4 | 14.2 | 20.3 | 17.1 | 13.0 | 15.21 | 50.4% | 30.0% |
| all families model4_conditioned | 13,812 | 21.7 | 20.1 | 35.4 | 16.5 | 4.3 | 1.1 | 0.9 | 5.81 | 6.3% | 2.0% |
| all families model4_fundamental | 13,821 | 16.7 | 13.4 | 35.8 | 19.8 | 10.6 | 2.6 | 1.1 | 7.6 | 14.3% | 3.7% |

Configurable thresholds (primary): >=5pp 76.0%, >=10pp 55.7%, >=15pp 40.3%, >=20pp 29.8%, >=25pp 21.6%, >=30pp 15.7%, >=40pp 8.1%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.38pp; >=10pp 45.0%, >=25pp 17.3%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,316 | 30.2 | 14.7 | 25.1 | 17.7 | 10.4 | 1.1 | 0.8 | 5.84 | 12.4% | 2.0% |
| CHALLENGER | 3,043 | 15.6 | 10.0 | 20.2 | 15.7 | 14.8 | 11.9 | 11.7 | 11.51 | 38.5% | 23.6% |
| ITF_MEN | 4,845 | 11.3 | 8.4 | 18.1 | 15.1 | 19.3 | 15.5 | 12.2 | 13.92 | 47.1% | 27.7% |
| ITF_WOMEN | 6,673 | 10.3 | 6.5 | 16.2 | 16.1 | 21.9 | 18.6 | 10.4 | 15.38 | 50.9% | 28.9% |
| WTA | 902 | 21.9 | 10.9 | 24.7 | 15.7 | 19.7 | 5.8 | 1.2 | 8.02 | 26.7% | 7.0% |
| WTA125 | 563 | 13.0 | 7.8 | 22.6 | 21.0 | 19.7 | 14.0 | 1.9 | 11.31 | 35.7% | 16.0% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,316 | 24.1 | 14.5 | 24.9 | 19.1 | 14.6 | 1.9 | 1.0 | 6.81 | 17.5% | 2.9% |
| CHALLENGER | 3,043 | 15.1 | 7.6 | 19.4 | 13.4 | 18.2 | 14.0 | 12.4 | 12.74 | 44.6% | 26.4% |
| ITF_MEN | 4,845 | 9.8 | 7.2 | 16.2 | 14.2 | 20.0 | 18.2 | 14.3 | 15.95 | 52.5% | 32.5% |
| ITF_WOMEN | 6,673 | 8.8 | 5.9 | 13.0 | 13.1 | 21.9 | 20.7 | 16.6 | 18.87 | 59.2% | 37.3% |
| WTA | 902 | 18.3 | 8.1 | 19.1 | 16.0 | 22.6 | 14.8 | 1.2 | 11.68 | 38.6% | 16.0% |
| WTA125 | 563 | 5.9 | 4.3 | 17.9 | 17.8 | 25.4 | 19.2 | 9.6 | 17.24 | 54.2% | 28.8% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,316 | 27.6 | 14.4 | 28.9 | 15.3 | 10.3 | 2.5 | 0.9 | 6.06 | 13.8% | 3.4% |
| CHALLENGER | 3,043 | 14.8 | 10.3 | 20.6 | 15.3 | 15.4 | 11.8 | 11.7 | 11.02 | 39.0% | 23.5% |
| ITF_MEN | 4,845 | 10.4 | 8.3 | 18.9 | 14.1 | 19.9 | 16.0 | 12.3 | 14.19 | 48.3% | 28.3% |
| ITF_WOMEN | 6,673 | 9.9 | 6.9 | 16.5 | 15.8 | 22.6 | 18.9 | 9.3 | 15.38 | 50.8% | 28.2% |
| WTA | 902 | 22.3 | 15.4 | 32.9 | 16.0 | 10.4 | 2.2 | 0.8 | 6.15 | 13.4% | 3.0% |
| WTA125 | 563 | 22.9 | 11.9 | 28.8 | 15.4 | 14.2 | 6.4 | 0.4 | 7.52 | 21.0% | 6.8% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 713 | 30.9 | 22.9 | 35.6 | 9.0 | 1.3 | 0.4 | 0.0 | 4.7 | 1.7% | 0.4% |
| CHALLENGER | 2,081 | 22.0 | 15.4 | 27.6 | 15.1 | 12.9 | 5.0 | 2.0 | 6.99 | 19.9% | 7.0% |
| DOUBLES | 960 | 4.5 | 3.4 | 11.6 | 11.0 | 18.9 | 24.7 | 25.9 | 25.48 | 69.5% | 50.6% |
| ITF_MEN | 4,516 | 14.8 | 8.4 | 20.9 | 15.4 | 20.7 | 12.5 | 7.3 | 11.86 | 40.5% | 19.8% |
| ITF_WOMEN | 4,960 | 11.7 | 9.3 | 19.5 | 14.7 | 22.5 | 16.6 | 5.8 | 13.07 | 44.9% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 648 | 21.4 | 15.1 | 27.3 | 17.1 | 13.6 | 4.9 | 0.5 | 7.61 | 19.0% | 5.4% |
| WTA125 | 671 | 20.6 | 13.7 | 22.6 | 18.5 | 14.2 | 8.2 | 2.2 | 8.22 | 24.6% | 10.4% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,302 | 30.1 | 14.6 | 25.3 | 17.7 | 10.4 | 1.1 | 0.8 | 5.84 | 12.3% | 1.9% |
| CHALLENGER | 2,186 | 20.1 | 12.4 | 25.4 | 18.4 | 15.3 | 5.9 | 2.5 | 8.34 | 23.6% | 8.4% |
| ITF_MEN | 3,506 | 14.0 | 10.4 | 21.4 | 16.8 | 19.5 | 12.4 | 5.5 | 11.11 | 37.3% | 17.8% |
| ITF_WOMEN | 4,869 | 12.6 | 8.1 | 18.6 | 18.6 | 23.5 | 15.0 | 3.6 | 12.76 | 42.1% | 18.6% |
| WTA | 888 | 22.1 | 10.2 | 25.1 | 15.9 | 19.8 | 5.6 | 1.2 | 8.09 | 26.7% | 6.9% |
| WTA125 | 540 | 13.3 | 7.6 | 22.0 | 21.3 | 20.4 | 13.9 | 1.5 | 11.31 | 35.7% | 15.4% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,302 | 24.0 | 14.6 | 25.0 | 19.1 | 14.6 | 1.8 | 1.0 | 6.81 | 17.4% | 2.8% |
| CHALLENGER | 2,186 | 19.4 | 9.6 | 24.1 | 16.1 | 18.5 | 9.7 | 2.6 | 9.09 | 30.8% | 12.3% |
| ITF_MEN | 3,507 | 11.7 | 8.6 | 18.5 | 15.9 | 21.8 | 15.8 | 7.7 | 13.38 | 45.3% | 23.5% |
| ITF_WOMEN | 4,869 | 10.1 | 6.9 | 14.7 | 14.2 | 24.5 | 19.5 | 10.0 | 16.41 | 54.0% | 29.5% |
| WTA | 888 | 18.1 | 7.9 | 19.1 | 16.2 | 22.6 | 14.8 | 1.2 | 11.72 | 38.6% | 16.0% |
| WTA125 | 540 | 5.7 | 4.4 | 18.0 | 18.1 | 25.2 | 19.8 | 8.7 | 16.84 | 53.7% | 28.5% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 693 | 30.9 | 23.1 | 35.9 | 9.1 | 0.6 | 0.4 | 0.0 | 4.69 | 1.0% | 0.4% |
| CHALLENGER | 1,797 | 23.8 | 16.8 | 29.7 | 14.9 | 12.0 | 2.2 | 0.6 | 6.36 | 14.8% | 2.8% |
| DOUBLES | 890 | 4.5 | 3.5 | 11.9 | 11.0 | 19.0 | 24.4 | 25.7 | 25.22 | 69.1% | 50.1% |
| ITF_MEN | 3,708 | 16.3 | 9.2 | 22.8 | 16.3 | 20.6 | 10.4 | 4.3 | 10.46 | 35.4% | 14.7% |
| ITF_WOMEN | 4,054 | 12.8 | 10.0 | 21.3 | 15.5 | 22.8 | 14.9 | 2.6 | 11.65 | 40.4% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 614 | 22.0 | 15.8 | 27.5 | 17.1 | 13.8 | 3.8 | 0.0 | 7.21 | 17.6% | 3.8% |
| WTA125 | 568 | 22.5 | 15.1 | 24.1 | 20.2 | 12.5 | 5.1 | 0.3 | 7.33 | 18.0% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 960 | 4.5 | 3.4 | 11.6 | 11.0 | 18.9 | 24.7 | 25.9 | 25.48 | 69.5% | 50.6% |
| singles | 13,738 | 16.2 | 11.2 | 22.7 | 15.0 | 18.4 | 11.6 | 5.0 | 9.96 | 34.9% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 4,041 | 13.3 | 9.0 | 20.0 | 16.1 | 17.6 | 14.1 | 9.8 | 12.44 | 41.5% | 23.9% |
| Grass | 156 | 10.9 | 14.1 | 16.7 | 14.7 | 21.1 | 17.3 | 5.1 | 13.12 | 43.6% | 22.4% |
| Hard | 11,391 | 14.2 | 8.5 | 18.7 | 15.7 | 19.2 | 14.2 | 9.5 | 12.71 | 43.0% | 23.7% |
| UNKNOWN | 1,754 | 11.8 | 7.5 | 16.6 | 18.1 | 19.3 | 16.2 | 10.5 | 13.68 | 46.0% | 26.7% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,240 | 19.9 | 10.7 | 21.1 | 16.9 | 15.6 | 8.7 | 7.1 | 9.49 | 31.4% | 15.8% |
| B | 2,293 | 14.6 | 9.1 | 20.1 | 16.8 | 17.8 | 12.1 | 9.6 | 11.42 | 39.4% | 21.6% |
| C | 2,499 | 13.0 | 9.5 | 19.9 | 14.9 | 19.1 | 14.4 | 9.2 | 12.57 | 42.7% | 23.6% |
| D | 3,046 | 10.9 | 8.1 | 18.1 | 16.1 | 22.1 | 15.1 | 9.5 | 13.75 | 46.7% | 24.6% |
| F | 4,264 | 8.0 | 5.3 | 15.1 | 15.1 | 21.1 | 22.1 | 13.3 | 17.94 | 56.5% | 35.4% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,286 | 22.6 | 15.8 | 28.8 | 15.3 | 11.4 | 4.4 | 1.6 | 6.72 | 17.4% | 6.1% |
| B | 2,235 | 15.0 | 9.9 | 24.0 | 16.5 | 19.1 | 11.1 | 4.2 | 10.19 | 34.5% | 15.4% |
| C | 2,892 | 12.1 | 7.6 | 18.3 | 14.3 | 20.4 | 15.7 | 11.6 | 13.76 | 47.7% | 27.3% |
| D | 2,229 | 14.0 | 9.8 | 20.8 | 13.6 | 21.5 | 13.8 | 6.5 | 11.86 | 41.8% | 20.3% |
| F | 3,056 | 10.0 | 7.4 | 15.2 | 13.8 | 23.8 | 20.4 | 9.3 | 16.45 | 53.5% | 29.7% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 5,826 | 18.3 | 9.8 | 20.3 | 16.8 | 15.9 | 9.8 | 9.3 | 10.45 | 34.9% | 19.0% |
| LIMITED | 4,135 | 15.2 | 10.3 | 20.9 | 15.8 | 18.4 | 12.7 | 6.7 | 11.05 | 37.8% | 19.3% |
| POOR | 7,381 | 9.2 | 6.6 | 16.4 | 15.6 | 21.5 | 19.1 | 11.7 | 15.86 | 52.2% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,982 | 31.4 | 24.3 | 36.4 | 5.4 | 1.8 | 0.7 | 0.1 | 4.49 | 2.5% | 0.7% |
| GAME_SPREAD | 2,850 | 25.8 | 15.9 | 36.8 | 16.7 | 4.2 | 0.4 | 0.2 | 6.0 | 4.8% | 0.6% |
| MATCH_WINNER | 14,698 | 15.5 | 10.7 | 22.0 | 14.7 | 18.4 | 12.4 | 6.3 | 10.47 | 37.2% | 18.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 5,445 | 33.5 | 19.4 | 31.0 | 9.6 | 5.1 | 1.2 | 0.2 | 4.72 | 6.5% | 1.4% |
| TOTAL_GAMES | 4,363 | 6.7 | 9.1 | 39.0 | 29.7 | 10.4 | 2.7 | 2.3 | 9.46 | 15.5% | 5.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,857 | 25.6 | 38.0 | 31.6 | 0.3 | 3.9 | 0.4 | 0.1 | 4.31 | 4.5% | 0.6% |
| GAME_SPREAD | 3,464 | 45.1 | 16.5 | 28.9 | 7.3 | 1.1 | 0.7 | 0.4 | 3.58 | 2.2% | 1.1% |
| TOTAL_GAMES | 5,491 | 3.4 | 6.5 | 42.9 | 36.7 | 6.6 | 1.9 | 1.9 | 9.76 | 10.5% | 3.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,857 | 26.3 | 18.6 | 37.2 | 9.2 | 6.3 | 2.1 | 0.3 | 5.52 | 8.7% | 2.4% |
| GAME_SPREAD | 3,464 | 19.1 | 13.3 | 30.4 | 21.1 | 13.0 | 2.3 | 0.7 | 7.82 | 16.0% | 3.0% |
| TOTAL_GAMES | 5,500 | 6.7 | 8.9 | 37.9 | 28.3 | 12.9 | 3.2 | 2.1 | 9.66 | 18.3% | 5.3% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 17,342 | 43.0% | 24.1% | 12.77 | 33.6% | 14.2% | 10.39 |
| gen1_elo | 17,342 | 42.3% | 23.5% | 12.25 | 32.6% | 14.0% | 9.85 |
| gen1_sr | 17,342 | 51.5% | 29.7% | 15.52 | 43.1% | 19.9% | 12.83 |
| gen2 | 17,342 | 50.4% | 30.0% | 15.21 | 43.3% | 21.5% | 12.76 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 9,430 | 16.6 | 10.6 | 21.7 | 17.4 | 19.2 | 11.2 | 3.3 | 10.35 | 33.7% | 14.5% |
| STALE | 7,912 | 10.3 | 6.1 | 15.3 | 14.3 | 18.5 | 18.2 | 17.2 | 17.1 | 53.9% | 35.5% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 8,166 | 17.3 | 11.5 | 23.8 | 14.7 | 16.8 | 11.1 | 4.8 | 9.35 | 32.7% | 15.8% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 32,040 | 8166 | 12902 | 10972 | 24.1 | 140.7 | 1400.4 |
| ge_15pp | 12,916 | 2668 | 4470 | 5778 | 26.3 | 443.0 | 1380.4 |
| ge_25pp | 6,928 | 1293 | 1957 | 3678 | 33.5 | 574.8 | 1380.4 |
| lt_10pp | 14,184 | 4299 | 6236 | 3649 | 22.4 | 48.1 | 1341.5 |

Current slate `SL-20261014T053006Z-8e7d74ad`: 650 priced rows, quote age at build {'median': 9.7, 'max': 9.7}, freshness {'FRESH': 650}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 8 | 0.0 | 0.0 | 37.5 | 0.0 | 37.5 | 25.0 | 0.0 | 20.45 | 62.5% | 25.0% |
| EXTERNAL_LONE_OUTLIER | 11 | 72.7 | 27.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,367 | 21.3 | 10.7 | 23.0 | 18.9 | 18.8 | 6.7 | 0.7 | 8.85 | 26.1% | 7.3% |
| KALSHI_LONE_OUTLIER | 5 | 20.0 | 0.0 | 60.0 | 0.0 | 20.0 | 0.0 | 0.0 | 5.14 | 20.0% | 0.0% |
| MARKETS_AGREE | 241 | 71.8 | 28.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.03 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 442 | 0.0 | 3.9 | 34.6 | 30.3 | 22.2 | 8.4 | 0.7 | 11.57 | 31.2% | 9.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 17,342 | 2074 (12.0%) | 21.3% | 0.6% | {"EXTERNAL_STALE": 1367, "AGREES_WITH_KALSHI": 442, "ALL_AGREE": 241, "EXTERNAL_OUTLIER": 11, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 5, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 7,449 | 501 (6.7%) | 27.5% | 1.2% | {"EXTERNAL_STALE": 357, "AGREES_WITH_KALSHI": 138, "SUPPORTS_MODEL_DIRECTION": 5, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp | 4,173 | 142 (3.4%) | 28.2% | 1.4% | {"EXTERNAL_STALE": 100, "AGREES_WITH_KALSHI": 40, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_ge_25pp_pregame_clean | 1,884 | 134 (7.1%) | 28.4% | 1.5% | {"EXTERNAL_STALE": 94, "AGREES_WITH_KALSHI": 38, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_lt_10pp | 7,116 | 1181 (16.6%) | 14.4% | 0.5% | {"EXTERNAL_STALE": 752, "ALL_AGREE": 241, "AGREES_WITH_KALSHI": 170, "EXTERNAL_OUTLIER": 11, "AGREES_WITH_MODEL": 4, "SUPPORTS_MODEL_DIRECTION": 2, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,413 | 11.6 | 8.1 | 20.0 | 14.9 | 21.4 | 14.2 | 9.8 | 13.27 | 45.4% | 24.1% |
| 4-10x | 2,298 | 11.9 | 8.8 | 19.4 | 15.6 | 19.8 | 15.5 | 9.0 | 13.02 | 44.3% | 24.5% |
| <2x | 9,180 | 15.7 | 9.2 | 18.9 | 16.9 | 17.4 | 12.7 | 9.1 | 11.77 | 39.2% | 21.8% |
| >=10x | 2,451 | 10.8 | 6.7 | 15.8 | 14.4 | 20.2 | 19.9 | 12.2 | 16.01 | 52.3% | 32.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 4,529 | 14.1 | 8.2 | 19.5 | 16.0 | 19.1 | 12.7 | 10.4 | 12.46 | 42.1% | 23.0% |
| 300-1000 | 3,999 | 11.9 | 8.6 | 17.6 | 16.2 | 21.2 | 15.7 | 8.8 | 13.55 | 45.7% | 24.5% |
| <300 | 4,849 | 8.7 | 6.2 | 15.9 | 14.9 | 20.9 | 20.6 | 12.8 | 16.81 | 54.3% | 33.4% |
| >=3000 | 3,965 | 21.1 | 11.8 | 22.6 | 17.2 | 13.9 | 7.5 | 5.9 | 8.5 | 27.3% | 13.4% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 563 | 0.5367 | 0.4055 | 0.4813 | +0.055 | -0.076 | 0.0017 ± 0.0061 |
| ratio 4-10x | 376 | 0.5863 | 0.4459 | 0.5213 | +0.065 | -0.075 | 0.0045 ± 0.0081 |
| ratio <2x | 1330 | 0.5378 | 0.4162 | 0.4564 | +0.081 | -0.040 | 0.0104 ± 0.0039 |
| ratio >=10x | 408 | 0.5466 | 0.3792 | 0.4338 | +0.113 | -0.055 | 0.012 ± 0.0088 |
| thinner_sample 1000-3000 | 756 | 0.5441 | 0.4191 | 0.4735 | +0.071 | -0.054 | 0.0042 ± 0.0052 |
| thinner_sample 300-1000 | 672 | 0.5617 | 0.4236 | 0.4821 | +0.080 | -0.059 | 0.0046 ± 0.0059 |
| thinner_sample <300 | 783 | 0.5447 | 0.3845 | 0.4559 | +0.089 | -0.071 | 0.0101 ± 0.0062 |
| thinner_sample >=3000 | 466 | 0.5271 | 0.4326 | 0.4549 | +0.072 | -0.022 | 0.0154 ± 0.0053 |
| data_status ADEQUATE | 767 | 0.5315 | 0.4278 | 0.455 | +0.076 | -0.027 | 0.0091 ± 0.0045 |
| data_status LIMITED | 713 | 0.553 | 0.4238 | 0.4881 | +0.065 | -0.064 | 0.0031 ± 0.0055 |
| data_status POOR | 1197 | 0.5505 | 0.3959 | 0.4628 | +0.088 | -0.067 | 0.0101 ± 0.0049 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 410 | 0.1925 | 0.1939 | -0.0014 ± 0.0008 | 0.5624 | 0.5654 | 0.492 | 0.477 | 0.5195 | -0.053 ± 0.0228 | -0.01 (3) |
| 3-5 | 273 | 0.1905 | 0.1914 | -0.0009 ± 0.0021 | 0.5609 | 0.5616 | 0.5067 | 0.4669 | 0.4945 | -0.066 ± 0.027 | 0.02 (1) |
| 5-10 | 560 | 0.1979 | 0.1992 | -0.0013 ± 0.0028 | 0.5804 | 0.5826 | 0.5114 | 0.4372 | 0.475 | -0.081 ± 0.0196 | -0.0125 (4) |
| 10-15 | 480 | 0.2113 | 0.2041 | +0.0072 ± 0.0052 | 0.6099 | 0.5893 | 0.5224 | 0.3988 | 0.4292 | -0.087 ± 0.0205 | -0.0633 (3) |
| 15-25 | 574 | 0.2267 | 0.2146 | +0.0121 ± 0.0075 | 0.6478 | 0.6157 | 0.5742 | 0.3795 | 0.4477 | -0.076 ± 0.0193 | -0.0133 (6) |
| 25-40 | 312 | 0.2229 | 0.2077 | +0.0151 ± 0.0154 | 0.6368 | 0.5959 | 0.651 | 0.3412 | 0.4712 | -0.065 ± 0.0233 | -0.01 (1) |
| 40+ | 68 | 0.2909 | 0.1768 | +0.1141 ± 0.0454 | 0.7906 | 0.5286 | 0.7508 | 0.3033 | 0.3971 | -0.121 ± 0.0447 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1944 | 0.1769 | 0.1781 | -0.0011 ± 0.0003 | 0.5277 | 0.5288 | 0.4783 | 0.4633 | 0.4979 | -0.022 ± 0.0097 | -0.0188 (8) |
| 3-5 | 1231 | 0.1954 | 0.1939 | +0.0014 ± 0.001 | 0.5721 | 0.5643 | 0.4796 | 0.44 | 0.4379 | -0.061 ± 0.0128 | 0.02 (1) |
| 5-10 | 2670 | 0.193 | 0.1914 | +0.0016 ± 0.0013 | 0.5677 | 0.5619 | 0.4852 | 0.4114 | 0.4341 | -0.044 ± 0.0086 | -0.0082 (17) |
| 10-15 | 2306 | 0.2012 | 0.1833 | +0.0179 ± 0.0022 | 0.5881 | 0.5385 | 0.4798 | 0.3555 | 0.3461 | -0.075 ± 0.0089 | -0.0475 (4) |
| 15-25 | 2733 | 0.2054 | 0.1699 | +0.0355 ± 0.0031 | 0.6026 | 0.5026 | 0.4986 | 0.3028 | 0.3125 | -0.064 ± 0.0079 | -0.0048 (29) |
| 25-40 | 2188 | 0.2191 | 0.1241 | +0.0950 ± 0.0047 | 0.6314 | 0.3835 | 0.529 | 0.2152 | 0.2239 | -0.063 ± 0.0073 | -0.01 (1) |
| 40+ | 1498 | 0.3722 | 0.0437 | +0.3285 ± 0.006 | 0.9702 | 0.1728 | 0.6243 | 0.106 | 0.0587 | -0.084 ± 0.005 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 315 | 0.1961 | 0.1965 | -0.0003 ± 0.0009 | 0.5737 | 0.5746 | 0.4999 | 0.4848 | 0.5016 | -0.088 ± 0.0264 | -0.01 (1) |
| 3-5 | 214 | 0.212 | 0.2109 | +0.0011 ± 0.0026 | 0.6062 | 0.6053 | 0.5187 | 0.4787 | 0.4813 | -0.084 ± 0.0331 | 0.02 (1) |
| 5-10 | 489 | 0.1972 | 0.197 | +0.0002 ± 0.003 | 0.576 | 0.5762 | 0.5554 | 0.4803 | 0.5153 | -0.070 ± 0.0209 | -0.01 (4) |
| 10-15 | 442 | 0.2182 | 0.2067 | +0.0115 ± 0.0054 | 0.6235 | 0.599 | 0.5751 | 0.4507 | 0.4706 | -0.106 ± 0.0225 | -0.05 (4) |
| 15-25 | 643 | 0.2243 | 0.2076 | +0.0166 ± 0.0071 | 0.6386 | 0.5978 | 0.5913 | 0.3939 | 0.4541 | -0.083 ± 0.0183 | -0.01 (5) |
| 25-40 | 419 | 0.2692 | 0.198 | +0.0712 ± 0.0137 | 0.7537 | 0.5757 | 0.6672 | 0.3532 | 0.3986 | -0.128 ± 0.0215 | -0.025 (2) |
| 40+ | 155 | 0.3451 | 0.19 | +0.1551 ± 0.0338 | 0.9621 | 0.5558 | 0.7492 | 0.272 | 0.3613 | -0.056 ± 0.0333 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1678 | 0.182 | 0.1824 | -0.0004 ± 0.0004 | 0.5393 | 0.54 | 0.4952 | 0.4805 | 0.5048 | -0.033 ± 0.0108 | -0.0217 (6) |
| 3-5 | 1072 | 0.1954 | 0.1947 | +0.0008 ± 0.0011 | 0.5662 | 0.5645 | 0.5166 | 0.4767 | 0.486 | -0.042 ± 0.0137 | 0.02 (1) |
| 5-10 | 2333 | 0.1897 | 0.1876 | +0.0021 ± 0.0013 | 0.561 | 0.5529 | 0.5144 | 0.4406 | 0.4646 | -0.039 ± 0.0091 | -0.01 (5) |
| 10-15 | 2034 | 0.1977 | 0.1822 | +0.0156 ± 0.0024 | 0.5811 | 0.534 | 0.5239 | 0.3996 | 0.4022 | -0.068 ± 0.0096 | -0.02 (14) |
| 15-25 | 2930 | 0.2147 | 0.1752 | +0.0395 ± 0.0031 | 0.6248 | 0.5179 | 0.5342 | 0.3379 | 0.3386 | -0.076 ± 0.0078 | -0.0026 (27) |
| 25-40 | 2536 | 0.248 | 0.1369 | +0.1111 ± 0.0047 | 0.7047 | 0.4177 | 0.5619 | 0.2459 | 0.2299 | -0.087 ± 0.0074 | -0.015 (6) |
| 40+ | 1987 | 0.3998 | 0.0681 | +0.3317 ± 0.0067 | 1.0472 | 0.237 | 0.666 | 0.129 | 0.1022 | -0.068 ± 0.0057 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 406 | 0.1934 | 0.1961 | -0.0027 ± 0.0008 | 0.5657 | 0.5727 | 0.4929 | 0.4778 | 0.5542 | -0.003 ± 0.0222 | -0.0133 (6) |
| 3-5 | 291 | 0.1869 | 0.1852 | +0.0016 ± 0.002 | 0.5494 | 0.5454 | 0.4929 | 0.4535 | 0.4536 | -0.115 ± 0.0265 | -0.01 (1) |
| 5-10 | 602 | 0.1994 | 0.1972 | +0.0022 ± 0.0027 | 0.5852 | 0.5772 | 0.5052 | 0.4315 | 0.4502 | -0.089 ± 0.0186 | -0.01 (4) |
| 10-15 | 454 | 0.2096 | 0.2118 | -0.0022 ± 0.0053 | 0.6069 | 0.607 | 0.5392 | 0.4165 | 0.489 | -0.058 ± 0.0213 | -0.044 (5) |
| 15-25 | 540 | 0.2309 | 0.209 | +0.0219 ± 0.0077 | 0.6613 | 0.6021 | 0.5797 | 0.3864 | 0.4278 | -0.102 ± 0.0195 | -0.03 (1) |
| 25-40 | 323 | 0.2087 | 0.2146 | -0.0059 ± 0.0151 | 0.6054 | 0.6126 | 0.6573 | 0.3451 | 0.5077 | -0.038 ± 0.0226 | 0.0 (1) |
| 40+ | 61 | 0.3195 | 0.1777 | +0.1418 ± 0.0492 | 0.8584 | 0.5313 | 0.7574 | 0.3028 | 0.377 | -0.134 ± 0.0497 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1853 | 0.1862 | 0.1874 | -0.0012 ± 0.0004 | 0.5484 | 0.5508 | 0.4847 | 0.4696 | 0.504 | -0.019 ± 0.0101 | -0.0183 (23) |
| 3-5 | 1291 | 0.1868 | 0.1847 | +0.0021 ± 0.001 | 0.5505 | 0.5454 | 0.4766 | 0.4372 | 0.4307 | -0.071 ± 0.0124 | -0.0243 (7) |
| 5-10 | 2861 | 0.1924 | 0.1872 | +0.0053 ± 0.0012 | 0.5682 | 0.551 | 0.4813 | 0.4076 | 0.4075 | -0.062 ± 0.0081 | -0.01 (18) |
| 10-15 | 2161 | 0.1945 | 0.1808 | +0.0137 ± 0.0023 | 0.5732 | 0.5306 | 0.4942 | 0.371 | 0.3767 | -0.064 ± 0.0091 | -0.03 (9) |
| 15-25 | 2810 | 0.2081 | 0.1703 | +0.0379 ± 0.003 | 0.611 | 0.5045 | 0.5026 | 0.3073 | 0.3103 | -0.069 ± 0.0078 | -0.03 (2) |
| 25-40 | 2167 | 0.2135 | 0.1219 | +0.0916 ± 0.0047 | 0.6186 | 0.3763 | 0.5241 | 0.2077 | 0.2247 | -0.057 ± 0.0071 | 0.0 (1) |
| 40+ | 1427 | 0.3864 | 0.0455 | +0.3409 ± 0.0064 | 1.01 | 0.178 | 0.6325 | 0.108 | 0.0568 | -0.087 ± 0.0053 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 721 | 0.1996 | 0.2003 | -0.0007 ± 0.0006 | 0.58 | 0.5816 | 0.5058 | 0.4908 | 0.509 | -0.036 ± 0.0166 | -0.0226 (46) |
| 3-5 | 522 | 0.1964 | 0.1958 | +0.0006 ± 0.0016 | 0.5721 | 0.569 | 0.48 | 0.4402 | 0.4502 | -0.047 ± 0.0195 | -0.0058 (33) |
| 5-10 | 1081 | 0.1921 | 0.1864 | +0.0057 ± 0.002 | 0.5682 | 0.5535 | 0.4817 | 0.4082 | 0.407 | -0.064 ± 0.0134 | -0.0049 (73) |
| 10-15 | 691 | 0.2046 | 0.1952 | +0.0093 ± 0.0042 | 0.5973 | 0.5719 | 0.4973 | 0.3743 | 0.3965 | -0.046 ± 0.0168 | 0.0014 (64) |
| 15-25 | 922 | 0.2327 | 0.2123 | +0.0203 ± 0.0059 | 0.6639 | 0.611 | 0.5594 | 0.3652 | 0.4111 | -0.051 ± 0.0152 | -0.0216 (58) |
| 25-40 | 525 | 0.2534 | 0.1923 | +0.0611 ± 0.0119 | 0.7143 | 0.5602 | 0.6446 | 0.3313 | 0.3886 | -0.087 ± 0.0178 | -0.0216 (25) |
| 40+ | 178 | 0.3628 | 0.1934 | +0.1693 ± 0.0336 | 1.0535 | 0.568 | 0.7956 | 0.3023 | 0.3989 | -0.070 ± 0.0301 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2184 | 0.1904 | 0.1907 | -0.0003 ± 0.0003 | 0.5563 | 0.5559 | 0.5042 | 0.4888 | 0.5027 | -0.031 ± 0.0093 | -0.0155 (82) |
| 3-5 | 1510 | 0.1891 | 0.1865 | +0.0025 ± 0.0009 | 0.553 | 0.5468 | 0.4867 | 0.4471 | 0.4358 | -0.058 ± 0.0112 | -0.0148 (63) |
| 5-10 | 3079 | 0.1906 | 0.1828 | +0.0078 ± 0.0012 | 0.5648 | 0.543 | 0.4767 | 0.4031 | 0.3901 | -0.066 ± 0.0078 | -0.0087 (125) |
| 10-15 | 2072 | 0.1998 | 0.1871 | +0.0126 ± 0.0024 | 0.586 | 0.5521 | 0.5055 | 0.3825 | 0.3924 | -0.049 ± 0.0095 | -0.0053 (105) |
| 15-25 | 2605 | 0.23 | 0.1989 | +0.0311 ± 0.0034 | 0.664 | 0.5777 | 0.5531 | 0.3582 | 0.3774 | -0.059 ± 0.0088 | -0.0255 (106) |
| 25-40 | 1762 | 0.2536 | 0.1674 | +0.0862 ± 0.0062 | 0.7201 | 0.495 | 0.6053 | 0.2904 | 0.3133 | -0.077 ± 0.0095 | -0.0206 (47) |
| 40+ | 861 | 0.3855 | 0.1269 | +0.2587 ± 0.0131 | 1.0958 | 0.3898 | 0.7094 | 0.2002 | 0.2137 | -0.072 ± 0.0115 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2677 | 1.068 ± 0.054 | 1.185 | 0.1691 | 0.1699 | 0.2102 | 0.2022 |
| gen2 | 2677 | 0.875 ± 0.049 | 1.124 | 0.1805 | 0.1697 | 0.2281 | 0.202 |
| gen1_elo | 2677 | 1.047 ± 0.053 | 1.177 | 0.1734 | 0.1702 | 0.2091 | 0.2022 |
| gen1_sr | 2677 | 1.076 ± 0.063 | 1.2 | 0.1394 | 0.1717 | 0.2241 | 0.2018 |
| gen1_ledger | 4640 | 0.881 ± 0.036 | 1.091 | 0.1758 | 0.1864 | 0.2171 | 0.197 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 12,916)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,314 | 25.7% |
| STALE_QUOTE | market_freshness | 2,518 | 19.5% |
| BOOK_QUALITY | execution | 2,374 | 18.4% |
| POOR_DATA | data | 1,427 | 11.1% |
| LIMITED_DATA | data | 974 | 7.5% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 699 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 630 | 4.9% |
| IDENTITY_AMBIGUOUS | mapping | 491 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 365 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 124 | 1.0% |

Cause class: coverage 25.7%, market_freshness 19.5%, data 18.6%, execution 18.4%, market_freshness/coverage 8.2%, model_calibration_or_unknown 4.9%, mapping 3.8%, model_calibration 1.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.3%, START_UNVERIFIABLE 95.8%, LOW_DATA_QUALITY 68.5%, THIN_PLAYER_HISTORY 57.2%, STALE_PLAYER_DATA 55.2%, STALE_KALSHI_QUOTE 44.7%, MODEL_INTERNAL_DISAGREEMENT 38.5%, ASYMMETRIC_SAMPLE_SIZE 31.2%, WIDE_SPREAD 23.9%, MODEL_HIGH_UNCERTAINTY 16.6%, PLAYER_IDENTITY_RISK 13.0%, LEVEL_TRANSFER_RISK 8.8%, EVENT_MAPPING_RISK 7.8%, LOW_DISPLAYED_LIQUIDITY 7.4%, MODEL_CALIBRATION_OUTLIER 3.5%, EXTERNAL_MARKET_REJECTION 1.6%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 28.0%, POST_SETTLEMENT_OBSERVATION 25.7%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 6,928)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,616 | 37.8% |
| BOOK_QUALITY | execution | 1,235 | 17.8% |
| STALE_QUOTE | market_freshness | 1,135 | 16.4% |
| POOR_DATA | data | 575 | 8.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 380 | 5.5% |
| IDENTITY_AMBIGUOUS | mapping | 307 | 4.4% |
| LIMITED_DATA | data | 286 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 226 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 140 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 28 | 0.4% |

Cause class: coverage 37.8%, execution 17.8%, market_freshness 16.4%, data 12.4%, market_freshness/coverage 8.8%, mapping 4.4%, model_calibration_or_unknown 2.0%, model_calibration 0.4%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.1%, START_UNVERIFIABLE 98.2%, LOW_DATA_QUALITY 72.1%, THIN_PLAYER_HISTORY 59.4%, STALE_KALSHI_QUOTE 53.1%, STALE_PLAYER_DATA 50.2%, MODEL_INTERNAL_DISAGREEMENT 39.6%, ASYMMETRIC_SAMPLE_SIZE 33.0%, WIDE_SPREAD 23.7%, MODEL_HIGH_UNCERTAINTY 17.4%, PLAYER_IDENTITY_RISK 16.7%, EVENT_MAPPING_RISK 9.7%, LEVEL_TRANSFER_RISK 7.7%, LOW_DISPLAYED_LIQUIDITY 7.6%, MODEL_CALIBRATION_OUTLIER 4.5%, EXTERNAL_MARKET_REJECTION 0.8%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 40.5%, POST_SETTLEMENT_OBSERVATION 37.8%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 5597, "IDENTITY_AMBIGUOUS": 1331}; ticker orientation: {"VERIFIED": 6928}.

Checks: discipline:AMBIGUOUS 486, discipline:PASS 6442, identity_confidence:AMBIGUOUS 1158, identity_confidence:PASS 5770, level_mapping:NA 498, level_mapping:PASS 6430, market_pair:AMBIGUOUS 239, market_pair:NA 171, market_pair:PASS 6518, model_complement:NA 138, model_complement:PASS 6790, namesake:PASS 6928, physical_match_id:NA 2755, physical_match_id:PASS 4173, player_ids:PASS 6928, same_pair_other_event:PASS 6928, ticker_orientation:PASS 6928

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,029 | 1.4% | 1.4% | 0.4% | {"market_freshness": 20, "execution": 8, "market_freshness/coverage": 1} | 5.27 | 0.2124 / 0.2138 (243) | 16.3% | 0.5% | 5.5% | 1.7% |
| CHALLENGER | 5,124 | 16.9% | 5.9% | 12.5% | {"coverage": 526, "market_freshness": 109, "market_freshness/coverage": 105, "data": 57, "model_calibration_or_unknown": 45, "execution": 12, "mapping": 6, "model_calibration": 4} | 7.24 | 0.2174 / 0.2032 (1308) | 37.7% | 8.8% | 2.4% | 22.3% |
| DOUBLES | 960 | 50.6% | 50.1% | 7.0% | {"execution": 191, "mapping": 149, "market_freshness": 106, "market_freshness/coverage": 33, "coverage": 7} | 25.22 | 0.3357 / 0.2324 (268) | 24.4% | 0.0% | 100.0% | 7.3% |
| ITF_MEN | 9,361 | 23.9% | 16.2% | 32.3% | {"coverage": 878, "execution": 481, "market_freshness": 312, "data": 305, "market_freshness/coverage": 188, "mapping": 71, "model_calibration_or_unknown": 2} | 10.82 | 0.2097 / 0.1938 (2276) | 35.6% | 57.7% | 9.7% | 22.9% |
| ITF_WOMEN | 11,633 | 26.2% | 18.2% | 43.9% | {"coverage": 1188, "execution": 522, "market_freshness": 516, "data": 465, "market_freshness/coverage": 234, "mapping": 75, "model_calibration_or_unknown": 32, "model_calibration": 10} | 12.33 | 0.2034 / 0.1925 (2513) | 37.9% | 58.1% | 9.8% | 23.3% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,550 | 6.3% | 5.6% | 1.4% | {"market_freshness": 36, "model_calibration_or_unknown": 22, "data": 11, "market_freshness/coverage": 10, "model_calibration": 7, "execution": 7, "coverage": 4, "mapping": 1} | 7.77 | 0.2344 / 0.2267 (253) | 26.1% | 1.4% | 1.7% | 3.1% |
| WTA125 | 1,234 | 13.0% | 10.3% | 2.3% | {"model_calibration_or_unknown": 37, "market_freshness": 34, "market_freshness/coverage": 34, "data": 23, "coverage": 12, "execution": 9, "model_calibration": 7, "mapping": 4} | 9.38 | 0.2188 / 0.2098 (414) | 22.9% | 8.3% | 4.3% | 10.2% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 5 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 6 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 7 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 8 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 9 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 10 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 11 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 12 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 13 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 14 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 15 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 16 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 17 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 18 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 19 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 20 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 21 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 321 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 22 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 23 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 24 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 25 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 26 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 27 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 874 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 28 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 29 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 30 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 547 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 31 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 32 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 33 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 34 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 35 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 36 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 37 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 38 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 39 | `KXATPCHALLENGERMATCH-26OCT13GIUSEA-SEA` | CHALLENGER | fair_v1 | 76% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 757 min (STALE); no external reference |
| 40 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 64 min (STALE); no external reference |
| 41 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 42 | `KXITFWMATCH-26OCT13MAMSTR-MAM` | ITF_WOMEN | fair_v1 | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 406 min (STALE); data LIMITED (grade C, thinner serve sample 879.0, ratio 2.64); no external reference |
| 43 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 44 | `KXITFMATCH-26OCT13VISMUE-MUE` | ITF_MEN | fair_v1 | 25% / 98% | -74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 617 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 0.0); no external reference |
| 45 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 46 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 47 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 48 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 253 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 49 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 50 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 22 min (AGING); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9817, "by_level_share_of_ge_25pp": {"ATP": 0.0042, "CHALLENGER": 0.1247, "DOUBLES": 0.0702, "ITF_MEN": 0.3229, "ITF_WOMEN": 0.4391, "OTHER": 0.0017, "WTA": 0.0141, "WTA125": 0.0231}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5309, "share_primary_cause_market_settled_or_in_play": 0.465, "share_primary_cause_stale_quote_only": 0.1638}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 6928, "identity_ambiguous_share": 0.1921, "ticker_orientation": {"VERIFIED": 6928}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 4173, "with_external": 142, "coverage": 0.034, "external_status": {"EXTERNAL_STALE": 100, "AGREES_WITH_KALSHI": 40, "SUPPORTS_MODEL_DIRECTION": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 100, "MODEL_LONE_OUTLIER": 40, "ALL_THREE_DISAGREE": 2}, "share_external_agrees_with_kalshi": 0.2817, "share_external_supports_model": 0.0141}, "pregame_clean_ge_25pp": {"n": 1884, "with_external": 134, "coverage": 0.0711, "external_status": {"EXTERNAL_STALE": 94, "AGREES_WITH_KALSHI": 38, "SUPPORTS_MODEL_DIRECTION": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 94, "MODEL_LONE_OUTLIER": 38, "ALL_THREE_DISAGREE": 2}, "share_external_agrees_with_kalshi": 0.2836, "share_external_supports_model": 0.0149}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 578.0, "median_sample_ratio": 2.35, "median_min_matches": 20.0, "median_max_days_since_last": 204.0, "share_severe_asymmetry": 0.1924, "data_status": {"POOR": 3642, "LIMITED": 2015, "ADEQUATE": 1271}, "comparison_lt_10pp": {"median_thinner_serve_points": 1856.0, "median_sample_ratio": 1.67, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 563, "model_minus_observed": 0.0553, "kalshi_minus_observed": -0.0759, "brier_diff_model_minus_kalshi": 0.0017}, "4-10x": {"n": 376, "model_minus_observed": 0.065, "kalshi_minus_observed": -0.0754, "brier_diff_model_minus_kalshi": 0.0045}, "<2x": {"n": 1330, "model_minus_observed": 0.0814, "kalshi_minus_observed": -0.0402, "brier_diff_model_minus_kalshi": 0.0104}, ">=10x": {"n": 408, "model_minus_observed": 0.1128, "kalshi_minus_observed": -0.0546, "brier_diff_model_minus_kalshi": 0.012}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2677, "model": {"intercept": -0.55, "slope": 0.875, "slope_se": 0.049}, "kalshi_mid_same_rows": {"intercept": 0.224, "slope": 1.124, "slope_se": 0.056}, "mean_extremity_model": 0.1805, "mean_extremity_kalshi": 0.1697, "model_brier": 0.2281, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0261, "brier_diff_se": 0.0036, "model_logloss": 0.6512, "kalshi_logloss": 0.586}, "fair_v1": {"n": 2677, "model": {"intercept": -0.385, "slope": 1.068, "slope_se": 0.054}, "kalshi_mid_same_rows": {"intercept": 0.335, "slope": 1.185, "slope_se": 0.058}, "mean_extremity_model": 0.1691, "mean_extremity_kalshi": 0.1699, "model_brier": 0.2102, "kalshi_brier": 0.2022, "brier_diff_model_minus_kalshi": 0.008, "brier_diff_se": 0.0029, "model_logloss": 0.6073, "kalshi_logloss": 0.5863}, "gen1_elo": {"n": 2677, "model": {"intercept": -0.355, "slope": 1.047, "slope_se": 0.053}, "kalshi_mid_same_rows": {"intercept": 0.348, "slope": 1.177, "slope_se": 0.057}, "mean_extremity_model": 0.1734, "mean_extremity_kalshi": 0.1702, "model_brier": 0.2091, "kalshi_brier": 0.2022, "brier_diff_model_minus_kalshi": 0.0068, "brier_diff_se": 0.0029, "model_logloss": 0.6061, "kalshi_logloss": 0.5864}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2406, "share_ge_15": 0.4295, "median_abs_gap": 12.77, "n": 17342}, "gen1_elo": {"share_ge_25": 0.2353, "share_ge_15": 0.4231, "median_abs_gap": 12.25, "n": 17342}, "gen1_sr": {"share_ge_25": 0.2973, "share_ge_15": 0.5151, "median_abs_gap": 15.52, "n": 17342}, "gen2": {"share_ge_25": 0.3004, "share_ge_15": 0.5037, "median_abs_gap": 15.21, "n": 17342}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1417, "share_ge_15": 0.336, "median_abs_gap": 10.39, "n": 13291}, "gen1_elo": {"share_ge_25": 0.1396, "share_ge_15": 0.3258, "median_abs_gap": 9.85, "n": 13290}, "gen1_sr": {"share_ge_25": 0.1988, "share_ge_15": 0.4312, "median_abs_gap": 12.83, "n": 13291}, "gen2": {"share_ge_25": 0.2152, "share_ge_15": 0.4326, "median_abs_gap": 12.76, "n": 13292}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.27, "share_ge_25_all": 0.0143, "share_ge_25_pregame_clean": 0.014}, "WTA": {"median_abs_gap_pregame_clean": 7.77, "share_ge_25_all": 0.0632, "share_ge_25_pregame_clean": 0.0559}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2403, "share_within_10pp_all": 0.4427, "share_within_10pp_pregame_clean": 0.502, "corr_model_vs_mid_pregame_clean": 0.8497}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 410, "model_brier": 0.1925, "kalshi_brier": 0.1939, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 480, "model_brier": 0.2113, "kalshi_brier": 0.2041, "brier_diff_model_minus_kalshi": 0.0072}, "15-25": {"n_settled": 574, "model_brier": 0.2267, "kalshi_brier": 0.2146, "brier_diff_model_minus_kalshi": 0.0121}, "25-40": {"n_settled": 312, "model_brier": 0.2229, "kalshi_brier": 0.2077, "brier_diff_model_minus_kalshi": 0.0151}, "3-5": {"n_settled": 273, "model_brier": 0.1905, "kalshi_brier": 0.1914, "brier_diff_model_minus_kalshi": -0.0009}, "40+": {"n_settled": 68, "model_brier": 0.2909, "kalshi_brier": 0.1768, "brier_diff_model_minus_kalshi": 0.1141}, "5-10": {"n_settled": 560, "model_brier": 0.1979, "kalshi_brier": 0.1992, "brier_diff_model_minus_kalshi": -0.0013}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.55, "slope": 0.875, "slope_se": 0.049}, "kalshi_slope": {"intercept": 0.224, "slope": 1.124, "slope_se": 0.056}, "n": 2677}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.502, "slope": 0.881, "slope_se": 0.036}, "kalshi_slope": {"intercept": 0.166, "slope": 1.091, "slope_se": 0.041}, "n": 4640}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 268, "model_brier": 0.3357, "kalshi_brier": 0.2324, "brier_diff_model_minus_kalshi": 0.1033, "brier_diff_se": 0.0199, "corr_model_outcome": -0.0413, "corr_kalshi_outcome": 0.2681}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
