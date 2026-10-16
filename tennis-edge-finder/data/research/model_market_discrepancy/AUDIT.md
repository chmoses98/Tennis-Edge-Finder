# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-16T21:59Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 35,313): 0-3 14.5%, 3-5 9.4%, 5-10 20.0%, 10-15 15.3%, 15-25 18.9%, 25-40 13.6%, 40+ 8.3%; median gap 11.88 pp.
* **Where the extremes live**: 98.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.9%, Challenger 12.3%, doubles 6.7%). Main tour: ATP 1.5% and WTA 6.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 7,760): MARKET_ALREADY_SETTLED_WHEN_PRICED 36.8%, STALE_QUOTE 18.3%, BOOK_QUALITY 17.3%, POOR_DATA 8.3%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IDENTITY_AMBIGUOUS 4.2%, LIMITED_DATA 4.0%, IN_PLAY_QUOTE 3.2%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.5%. By class: coverage 36.8%, market_freshness 18.3%, execution 17.3%, data 12.2%, market_freshness/coverage 8.7%, mapping 4.2%, model_calibration_or_unknown 2.0%, model_calibration 0.5%.
* **Stale / settled / in-play**: 54.1% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 45.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 7,760 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.9% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 3.8%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 22.1% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 562.0 points vs 1791.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.062, Gen-2 0.867, Gen-1 ledger 0.875 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 362 model 0.2244 vs Kalshi 0.2087; n 74 model 0.2888 vs Kalshi 0.1769.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 140,402 model-market comparisons (233,997 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 48,964 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-16T21:48:49.228507+00:00'], shadow board 39,308 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-16T21:48:53.393172+00:00'], Model 4 14,740 rows, 14,949 settled tickers, 5,094 tickers with an external scan.
* By model: {"gen1_ledger": 32257, "gen1_elo": 19767, "fair_v1": 19767, "gen2": 19767, "gen1_sr": 19767, "model4_fundamental": 14543, "model4_conditioned": 14534}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 35,313 | 14.5 | 9.4 | 20.0 | 15.3 | 18.9 | 13.6 | 8.3 | 11.88 | 40.8% | 22.0% |
| MW fair_v1 | 19,767 | 13.5 | 8.4 | 18.5 | 15.7 | 19.2 | 14.6 | 10.0 | 13.01 | 43.8% | 24.6% |
| MW gen1_elo | 19,767 | 13.1 | 9.0 | 19.7 | 15.1 | 19.2 | 14.3 | 9.7 | 12.49 | 43.2% | 24.0% |
| MW gen1_ledger | 15,546 | 15.6 | 10.7 | 21.9 | 14.7 | 18.4 | 12.4 | 6.2 | 10.42 | 37.0% | 18.6% |
| MW gen1_sr | 19,767 | 9.7 | 7.5 | 16.3 | 14.2 | 21.6 | 18.8 | 12.1 | 15.92 | 52.4% | 30.8% |
| MW gen2 | 19,767 | 11.4 | 7.1 | 16.5 | 14.1 | 20.0 | 17.7 | 13.2 | 15.45 | 50.9% | 30.9% |
| all families model4_conditioned | 14,534 | 21.6 | 20.0 | 34.8 | 16.8 | 4.5 | 1.3 | 1.0 | 5.83 | 6.9% | 2.3% |
| all families model4_fundamental | 14,543 | 16.7 | 13.5 | 35.5 | 19.5 | 10.8 | 2.9 | 1.2 | 7.6 | 14.8% | 4.0% |

Configurable thresholds (primary): >=5pp 76.1%, >=10pp 56.1%, >=15pp 40.8%, >=20pp 30.4%, >=25pp 22.0%, >=30pp 16.0%, >=40pp 8.3%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.52pp; >=10pp 45.5%, >=25pp 17.5%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,372 | 30.8 | 14.4 | 25.1 | 17.2 | 10.5 | 1.2 | 0.8 | 5.75 | 12.5% | 2.0% |
| CHALLENGER | 3,291 | 16.0 | 9.7 | 20.1 | 15.9 | 14.4 | 12.4 | 11.6 | 11.51 | 38.4% | 24.0% |
| ITF_MEN | 5,664 | 10.9 | 8.2 | 17.6 | 14.8 | 19.8 | 16.4 | 12.5 | 14.45 | 48.6% | 28.8% |
| ITF_WOMEN | 7,778 | 10.5 | 6.5 | 16.1 | 15.7 | 22.2 | 18.0 | 11.0 | 15.46 | 51.1% | 28.9% |
| WTA | 1,032 | 20.6 | 11.6 | 25.4 | 15.5 | 20.2 | 5.6 | 1.1 | 7.96 | 26.8% | 6.7% |
| WTA125 | 630 | 13.0 | 7.8 | 22.9 | 20.6 | 20.0 | 13.7 | 2.1 | 11.31 | 35.7% | 15.7% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,372 | 24.7 | 14.4 | 24.9 | 18.7 | 14.4 | 2.0 | 1.0 | 6.64 | 17.3% | 3.0% |
| CHALLENGER | 3,291 | 14.7 | 7.9 | 19.4 | 13.5 | 18.0 | 14.3 | 12.2 | 12.8 | 44.5% | 26.6% |
| ITF_MEN | 5,664 | 9.5 | 6.8 | 15.8 | 13.6 | 19.8 | 19.4 | 15.0 | 16.8 | 54.3% | 34.5% |
| ITF_WOMEN | 7,778 | 8.5 | 5.7 | 13.8 | 13.4 | 21.4 | 20.8 | 16.4 | 18.66 | 58.5% | 37.1% |
| WTA | 1,032 | 17.2 | 8.0 | 20.4 | 15.6 | 22.4 | 15.3 | 1.2 | 11.63 | 38.9% | 16.5% |
| WTA125 | 630 | 6.5 | 4.6 | 17.5 | 17.9 | 24.8 | 19.5 | 9.2 | 16.84 | 53.5% | 28.7% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,372 | 28.1 | 14.1 | 28.5 | 15.4 | 10.6 | 2.4 | 0.9 | 6.07 | 13.9% | 3.3% |
| CHALLENGER | 3,291 | 14.8 | 10.3 | 20.7 | 15.0 | 15.4 | 12.1 | 11.8 | 11.03 | 39.3% | 23.9% |
| ITF_MEN | 5,664 | 10.0 | 8.1 | 18.0 | 14.1 | 20.5 | 16.6 | 12.7 | 14.97 | 49.7% | 29.3% |
| ITF_WOMEN | 7,778 | 9.9 | 7.0 | 16.5 | 15.7 | 22.8 | 17.9 | 10.2 | 15.41 | 50.9% | 28.1% |
| WTA | 1,032 | 23.1 | 15.6 | 32.1 | 15.6 | 10.7 | 2.3 | 0.7 | 6.12 | 13.7% | 3.0% |
| WTA125 | 630 | 22.4 | 12.4 | 29.1 | 15.4 | 14.4 | 6.0 | 0.3 | 7.73 | 20.8% | 6.3% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 759 | 31.4 | 22.5 | 34.6 | 9.5 | 1.4 | 0.5 | 0.0 | 4.68 | 2.0% | 0.5% |
| CHALLENGER | 2,239 | 22.5 | 15.2 | 27.6 | 14.8 | 12.7 | 5.2 | 2.0 | 6.94 | 20.0% | 7.2% |
| DOUBLES | 1,060 | 5.3 | 3.7 | 11.3 | 10.8 | 20.0 | 24.4 | 24.5 | 24.16 | 69.0% | 49.0% |
| ITF_MEN | 4,772 | 14.7 | 8.6 | 20.7 | 15.5 | 20.9 | 12.5 | 7.2 | 11.88 | 40.6% | 19.7% |
| ITF_WOMEN | 5,140 | 11.8 | 9.3 | 19.6 | 14.7 | 22.3 | 16.5 | 5.8 | 13.02 | 44.6% | 22.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 727 | 21.7 | 15.5 | 28.1 | 16.9 | 12.7 | 4.7 | 0.4 | 7.18 | 17.7% | 5.1% |
| WTA125 | 700 | 20.4 | 13.9 | 22.7 | 18.4 | 14.3 | 8.1 | 2.1 | 8.29 | 24.6% | 10.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,358 | 30.7 | 14.4 | 25.3 | 17.2 | 10.5 | 1.1 | 0.8 | 5.82 | 12.4% | 1.9% |
| CHALLENGER | 2,333 | 20.9 | 12.3 | 25.3 | 18.4 | 14.9 | 5.9 | 2.4 | 8.27 | 23.2% | 8.3% |
| ITF_MEN | 4,112 | 13.3 | 10.1 | 20.9 | 16.6 | 20.2 | 13.2 | 5.7 | 11.52 | 39.1% | 18.9% |
| ITF_WOMEN | 5,808 | 12.5 | 7.9 | 18.4 | 17.8 | 23.5 | 15.0 | 5.0 | 13.04 | 43.5% | 20.0% |
| WTA | 1,012 | 20.9 | 11.1 | 25.7 | 15.5 | 20.3 | 5.5 | 1.1 | 7.98 | 26.9% | 6.6% |
| WTA125 | 604 | 13.4 | 7.6 | 22.4 | 21.0 | 20.7 | 13.2 | 1.7 | 11.31 | 35.6% | 14.9% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,358 | 24.6 | 14.4 | 25.0 | 18.6 | 14.4 | 1.9 | 1.0 | 6.71 | 17.3% | 2.9% |
| CHALLENGER | 2,333 | 18.9 | 10.2 | 24.4 | 16.2 | 18.3 | 9.4 | 2.6 | 9.07 | 30.3% | 12.0% |
| ITF_MEN | 4,113 | 11.2 | 8.1 | 18.2 | 15.3 | 21.9 | 16.8 | 8.5 | 14.07 | 47.2% | 25.3% |
| ITF_WOMEN | 5,808 | 9.7 | 6.6 | 15.4 | 14.7 | 23.3 | 20.0 | 10.4 | 16.34 | 53.7% | 30.4% |
| WTA | 1,012 | 17.2 | 7.8 | 20.4 | 15.6 | 22.4 | 15.4 | 1.2 | 11.68 | 39.0% | 16.6% |
| WTA125 | 604 | 6.3 | 4.8 | 17.6 | 18.4 | 24.7 | 20.0 | 8.3 | 16.74 | 53.0% | 28.3% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 739 | 31.4 | 22.7 | 34.9 | 9.6 | 0.8 | 0.5 | 0.0 | 4.62 | 1.4% | 0.5% |
| CHALLENGER | 1,926 | 24.4 | 16.6 | 29.8 | 14.6 | 11.8 | 2.4 | 0.5 | 6.33 | 14.8% | 3.0% |
| DOUBLES | 974 | 5.4 | 3.8 | 11.6 | 10.9 | 19.8 | 24.5 | 23.9 | 24.07 | 68.3% | 48.5% |
| ITF_MEN | 3,934 | 16.1 | 9.4 | 22.6 | 16.3 | 20.7 | 10.6 | 4.3 | 10.56 | 35.6% | 14.8% |
| ITF_WOMEN | 4,202 | 12.9 | 10.0 | 21.4 | 15.6 | 22.6 | 14.8 | 2.7 | 11.59 | 40.1% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 693 | 22.2 | 16.2 | 28.3 | 16.9 | 12.8 | 3.6 | 0.0 | 6.9 | 16.4% | 3.6% |
| WTA125 | 592 | 22.3 | 15.4 | 24.3 | 20.1 | 12.7 | 4.9 | 0.3 | 7.36 | 17.9% | 5.2% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,060 | 5.3 | 3.7 | 11.3 | 10.8 | 20.0 | 24.4 | 24.5 | 24.16 | 69.0% | 49.0% |
| singles | 14,486 | 16.4 | 11.2 | 22.7 | 15.0 | 18.3 | 11.5 | 4.9 | 9.91 | 34.7% | 16.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 4,660 | 13.4 | 8.8 | 19.2 | 15.7 | 17.9 | 14.7 | 10.3 | 12.73 | 42.9% | 25.0% |
| Grass | 222 | 10.8 | 11.7 | 17.1 | 13.5 | 23.0 | 15.8 | 8.1 | 14.16 | 46.9% | 23.9% |
| Hard | 12,782 | 13.9 | 8.4 | 18.6 | 15.2 | 19.7 | 14.4 | 9.9 | 12.99 | 44.0% | 24.3% |
| UNKNOWN | 2,103 | 12.2 | 7.1 | 16.9 | 18.8 | 19.0 | 15.8 | 10.2 | 13.38 | 45.0% | 26.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,737 | 19.8 | 10.7 | 21.1 | 16.9 | 15.7 | 9.0 | 6.9 | 9.51 | 31.6% | 15.9% |
| B | 2,588 | 14.0 | 8.9 | 19.7 | 16.4 | 18.5 | 12.4 | 10.2 | 12.01 | 41.0% | 22.5% |
| C | 2,862 | 12.7 | 9.4 | 20.0 | 14.2 | 19.2 | 14.4 | 10.1 | 12.69 | 43.7% | 24.5% |
| D | 3,406 | 11.7 | 7.8 | 17.4 | 15.9 | 22.0 | 15.4 | 9.8 | 13.95 | 47.1% | 25.1% |
| F | 5,174 | 8.1 | 5.3 | 15.0 | 14.8 | 21.7 | 21.6 | 13.5 | 17.98 | 56.8% | 35.1% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,547 | 23.1 | 15.8 | 28.9 | 15.1 | 11.1 | 4.4 | 1.6 | 6.68 | 17.1% | 6.0% |
| B | 2,319 | 14.8 | 10.1 | 24.1 | 16.4 | 19.4 | 11.0 | 4.2 | 10.19 | 34.6% | 15.3% |
| C | 3,065 | 12.1 | 7.8 | 18.1 | 14.2 | 20.8 | 15.7 | 11.3 | 13.95 | 47.8% | 27.1% |
| D | 2,317 | 14.0 | 9.8 | 20.7 | 13.7 | 21.4 | 13.8 | 6.6 | 11.86 | 41.8% | 20.4% |
| F | 3,298 | 10.4 | 7.6 | 15.2 | 13.9 | 23.6 | 20.2 | 9.0 | 16.26 | 52.8% | 29.2% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 6,499 | 18.0 | 9.6 | 20.3 | 16.6 | 16.2 | 10.0 | 9.2 | 10.55 | 35.4% | 19.2% |
| LIMITED | 4,572 | 14.7 | 10.3 | 20.8 | 15.3 | 18.6 | 12.9 | 7.5 | 11.29 | 38.9% | 20.4% |
| POOR | 8,696 | 9.6 | 6.5 | 16.0 | 15.3 | 21.8 | 19.0 | 11.9 | 15.99 | 52.7% | 30.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,172 | 30.7 | 24.2 | 35.7 | 6.2 | 2.1 | 0.8 | 0.2 | 4.56 | 3.1% | 1.0% |
| GAME_SPREAD | 2,954 | 25.7 | 16.4 | 36.5 | 16.8 | 4.1 | 0.4 | 0.2 | 5.95 | 4.7% | 0.6% |
| MATCH_WINNER | 15,546 | 15.6 | 10.7 | 21.9 | 14.7 | 18.4 | 12.4 | 6.2 | 10.42 | 37.0% | 18.6% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 5,937 | 33.0 | 19.2 | 30.5 | 10.2 | 5.6 | 1.3 | 0.2 | 4.8 | 7.1% | 1.5% |
| TOTAL_GAMES | 4,624 | 6.5 | 9.1 | 38.8 | 29.1 | 11.1 | 3.1 | 2.4 | 9.53 | 16.5% | 5.4% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,065 | 25.5 | 38.0 | 31.0 | 0.8 | 4.0 | 0.7 | 0.2 | 4.32 | 4.8% | 0.9% |
| GAME_SPREAD | 3,575 | 45.5 | 16.6 | 28.4 | 7.2 | 1.2 | 0.7 | 0.4 | 3.49 | 2.3% | 1.1% |
| TOTAL_GAMES | 5,894 | 3.6 | 6.6 | 42.1 | 36.3 | 7.1 | 2.3 | 2.0 | 9.81 | 11.4% | 4.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,065 | 26.4 | 18.6 | 36.7 | 9.2 | 6.5 | 2.3 | 0.4 | 5.5 | 9.1% | 2.6% |
| GAME_SPREAD | 3,575 | 19.7 | 13.5 | 30.3 | 20.8 | 12.8 | 2.4 | 0.7 | 7.64 | 15.8% | 3.0% |
| TOTAL_GAMES | 5,903 | 6.7 | 9.1 | 37.5 | 27.6 | 13.3 | 3.7 | 2.1 | 9.67 | 19.1% | 5.9% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 19,767 | 43.8% | 24.6% | 13.01 | 35.0% | 15.2% | 10.65 |
| gen1_elo | 19,767 | 43.2% | 24.0% | 12.49 | 33.9% | 14.9% | 10.12 |
| gen1_sr | 19,767 | 52.4% | 30.8% | 15.92 | 44.5% | 21.4% | 13.3 |
| gen2 | 19,767 | 50.9% | 30.9% | 15.45 | 44.1% | 22.8% | 13.02 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 10,500 | 16.5 | 10.4 | 21.6 | 17.2 | 19.6 | 11.3 | 3.4 | 10.43 | 34.3% | 14.7% |
| STALE | 9,267 | 10.2 | 6.1 | 15.0 | 14.0 | 18.8 | 18.4 | 17.5 | 17.35 | 54.7% | 35.9% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 9,014 | 17.4 | 11.6 | 23.5 | 14.6 | 16.9 | 11.1 | 4.8 | 9.38 | 32.8% | 15.9% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 35,313 | 9014 | 13972 | 12327 | 24.3 | 163.6 | 1400.4 |
| ge_15pp | 14,422 | 2957 | 4890 | 6575 | 26.9 | 465.8 | 1380.4 |
| ge_25pp | 7,760 | 1432 | 2131 | 4197 | 34.5 | 600.7 | 1380.4 |
| lt_10pp | 15,503 | 4739 | 6722 | 4042 | 22.3 | 48.7 | 1341.5 |

Current slate `SL-20261016T215912Z-5e413626`: 582 priced rows, quote age at build {'median': 10.8, 'max': 10.9}, freshness {'AGING': 582}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 10 | 0.0 | 0.0 | 40.0 | 0.0 | 40.0 | 20.0 | 0.0 | 20.33 | 60.0% | 20.0% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,703 | 21.3 | 10.9 | 23.1 | 18.1 | 19.0 | 7.0 | 0.6 | 8.67 | 26.6% | 7.6% |
| KALSHI_LONE_OUTLIER | 9 | 11.1 | 0.0 | 66.7 | 0.0 | 11.1 | 11.1 | 0.0 | 5.14 | 22.2% | 11.1% |
| MARKETS_AGREE | 289 | 69.9 | 30.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.1 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 573 | 0.0 | 3.7 | 35.2 | 27.6 | 23.9 | 8.7 | 0.9 | 11.66 | 33.5% | 9.6% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 19,767 | 2596 (13.1%) | 22.1% | 0.7% | {"EXTERNAL_STALE": 1703, "AGREES_WITH_KALSHI": 573, "ALL_AGREE": 289, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 9, "AGREES_WITH_MODEL": 9, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 8,666 | 653 (7.5%) | 29.4% | 1.2% | {"EXTERNAL_STALE": 453, "AGREES_WITH_KALSHI": 192, "SUPPORTS_MODEL_DIRECTION": 6, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 4,866 | 187 (3.8%) | 29.4% | 1.6% | {"EXTERNAL_STALE": 129, "AGREES_WITH_KALSHI": 55, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,311 | 176 (7.6%) | 30.1% | 1.7% | {"EXTERNAL_STALE": 120, "AGREES_WITH_KALSHI": 53, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 7,995 | 1476 (18.5%) | 15.1% | 0.7% | {"EXTERNAL_STALE": 941, "ALL_AGREE": 289, "AGREES_WITH_KALSHI": 223, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 7, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,825 | 11.1 | 7.7 | 19.5 | 14.9 | 22.0 | 14.3 | 10.4 | 13.77 | 46.8% | 24.7% |
| 4-10x | 2,554 | 12.7 | 8.9 | 19.8 | 15.5 | 18.8 | 15.2 | 9.2 | 12.66 | 43.1% | 24.3% |
| <2x | 10,320 | 15.4 | 9.1 | 18.9 | 16.7 | 17.7 | 13.2 | 9.2 | 11.95 | 40.0% | 22.3% |
| >=10x | 3,068 | 11.0 | 6.5 | 15.2 | 13.7 | 21.2 | 19.5 | 13.0 | 16.48 | 53.6% | 32.5% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 5,240 | 13.6 | 8.1 | 19.3 | 15.9 | 19.7 | 12.9 | 10.5 | 12.81 | 43.1% | 23.4% |
| 300-1000 | 4,446 | 11.9 | 8.7 | 17.3 | 15.9 | 20.9 | 15.9 | 9.5 | 13.73 | 46.2% | 25.3% |
| <300 | 5,869 | 9.1 | 6.0 | 15.6 | 14.6 | 21.4 | 20.3 | 13.0 | 16.88 | 54.7% | 33.2% |
| >=3000 | 4,212 | 21.4 | 11.7 | 22.9 | 16.9 | 13.8 | 7.6 | 5.8 | 8.38 | 27.2% | 13.4% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 620 | 0.5377 | 0.4049 | 0.4855 | +0.052 | -0.081 | -0.0001 ± 0.0059 |
| ratio 4-10x | 413 | 0.5845 | 0.4468 | 0.5109 | +0.074 | -0.064 | 0.0075 ± 0.0077 |
| ratio <2x | 1522 | 0.5367 | 0.4147 | 0.4534 | +0.083 | -0.039 | 0.0113 ± 0.0037 |
| ratio >=10x | 504 | 0.5439 | 0.3773 | 0.4187 | +0.125 | -0.041 | 0.0153 ± 0.0078 |
| thinner_sample 1000-3000 | 861 | 0.5435 | 0.4183 | 0.4715 | +0.072 | -0.053 | 0.0053 ± 0.0049 |
| thinner_sample 300-1000 | 735 | 0.5593 | 0.4212 | 0.4844 | +0.075 | -0.063 | 0.002 ± 0.0057 |
| thinner_sample <300 | 944 | 0.5425 | 0.3825 | 0.4364 | +0.106 | -0.054 | 0.0155 ± 0.0056 |
| thinner_sample >=3000 | 519 | 0.5289 | 0.4354 | 0.4605 | +0.068 | -0.025 | 0.0142 ± 0.0051 |
| data_status ADEQUATE | 890 | 0.5337 | 0.4291 | 0.4596 | +0.074 | -0.030 | 0.0093 ± 0.0042 |
| data_status LIMITED | 761 | 0.5508 | 0.422 | 0.4888 | +0.062 | -0.067 | 0.0029 ± 0.0053 |
| data_status POOR | 1408 | 0.548 | 0.3933 | 0.4489 | +0.099 | -0.056 | 0.0124 ± 0.0045 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 476 | 0.1925 | 0.1938 | -0.0014 ± 0.0007 | 0.5629 | 0.5657 | 0.4934 | 0.4786 | 0.5273 | -0.043 ± 0.0211 | -0.01 (5) |
| 3-5 | 295 | 0.1905 | 0.1909 | -0.0004 ± 0.002 | 0.5609 | 0.5605 | 0.509 | 0.4692 | 0.4915 | -0.071 ± 0.026 | 0.02 (1) |
| 5-10 | 643 | 0.1979 | 0.1973 | +0.0006 ± 0.0027 | 0.5814 | 0.5776 | 0.51 | 0.4355 | 0.4619 | -0.085 ± 0.0182 | -0.0167 (6) |
| 10-15 | 540 | 0.2124 | 0.2039 | +0.0085 ± 0.0049 | 0.6125 | 0.5892 | 0.5173 | 0.3936 | 0.4204 | -0.085 ± 0.0194 | -0.048 (5) |
| 15-25 | 669 | 0.2307 | 0.216 | +0.0146 ± 0.007 | 0.6565 | 0.6179 | 0.5758 | 0.3806 | 0.4425 | -0.079 ± 0.0178 | -0.0033 (9) |
| 25-40 | 362 | 0.2244 | 0.2087 | +0.0158 ± 0.0143 | 0.639 | 0.5994 | 0.6443 | 0.3357 | 0.4641 | -0.061 ± 0.0219 | -0.01 (1) |
| 40+ | 74 | 0.2888 | 0.1769 | +0.1119 ± 0.0433 | 0.7848 | 0.5268 | 0.7422 | 0.2957 | 0.3919 | -0.107 ± 0.043 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2218 | 0.178 | 0.1793 | -0.0013 ± 0.0003 | 0.5296 | 0.5311 | 0.4777 | 0.4627 | 0.5 | -0.018 ± 0.0091 | -0.0129 (17) |
| 3-5 | 1353 | 0.1916 | 0.19 | +0.0017 ± 0.001 | 0.5631 | 0.5548 | 0.4783 | 0.4387 | 0.4346 | -0.062 ± 0.0121 | 0.0 (2) |
| 5-10 | 2991 | 0.1924 | 0.1898 | +0.0025 ± 0.0012 | 0.567 | 0.5575 | 0.4833 | 0.4094 | 0.4263 | -0.047 ± 0.0081 | -0.0119 (21) |
| 10-15 | 2600 | 0.2013 | 0.1819 | +0.0194 ± 0.0021 | 0.5886 | 0.5353 | 0.4779 | 0.3533 | 0.3385 | -0.077 ± 0.0083 | -0.0281 (16) |
| 15-25 | 3170 | 0.2088 | 0.1712 | +0.0375 ± 0.0029 | 0.6099 | 0.5055 | 0.501 | 0.3049 | 0.3088 | -0.068 ± 0.0073 | -0.0025 (44) |
| 25-40 | 2481 | 0.22 | 0.1263 | +0.0938 ± 0.0045 | 0.6332 | 0.389 | 0.5272 | 0.2143 | 0.2245 | -0.060 ± 0.0069 | -0.01 (1) |
| 40+ | 1679 | 0.3759 | 0.043 | +0.3329 ± 0.0057 | 0.9785 | 0.1704 | 0.6261 | 0.1052 | 0.0566 | -0.085 ± 0.0047 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 354 | 0.1982 | 0.1985 | -0.0003 ± 0.0008 | 0.5777 | 0.5785 | 0.4999 | 0.4846 | 0.5056 | -0.079 ± 0.0248 | -0.01 (3) |
| 3-5 | 245 | 0.2088 | 0.208 | +0.0008 ± 0.0024 | 0.5996 | 0.599 | 0.5161 | 0.4761 | 0.4816 | -0.079 ± 0.0307 | 0.02 (1) |
| 5-10 | 558 | 0.1977 | 0.1967 | +0.0010 ± 0.0028 | 0.5784 | 0.576 | 0.5492 | 0.4742 | 0.5054 | -0.073 ± 0.0194 | -0.01 (4) |
| 10-15 | 500 | 0.2165 | 0.2083 | +0.0082 ± 0.0051 | 0.6208 | 0.6018 | 0.5677 | 0.4432 | 0.476 | -0.089 ± 0.0213 | -0.04 (5) |
| 15-25 | 739 | 0.2286 | 0.2092 | +0.0194 ± 0.0066 | 0.649 | 0.6009 | 0.5867 | 0.3901 | 0.4425 | -0.086 ± 0.0171 | -0.0133 (9) |
| 25-40 | 481 | 0.2647 | 0.2003 | +0.0644 ± 0.0129 | 0.7407 | 0.5817 | 0.6591 | 0.3442 | 0.4012 | -0.106 ± 0.0203 | -0.0075 (4) |
| 40+ | 182 | 0.3579 | 0.1786 | +0.1793 ± 0.0306 | 0.988 | 0.5282 | 0.738 | 0.2578 | 0.3242 | -0.067 ± 0.0303 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1866 | 0.1821 | 0.1824 | -0.0004 ± 0.0003 | 0.539 | 0.5398 | 0.4989 | 0.4842 | 0.507 | -0.033 ± 0.0102 | -0.0133 (15) |
| 3-5 | 1181 | 0.1921 | 0.1913 | +0.0008 ± 0.001 | 0.5589 | 0.5571 | 0.5164 | 0.4764 | 0.486 | -0.041 ± 0.013 | 0.02 (1) |
| 5-10 | 2652 | 0.1903 | 0.187 | +0.0033 ± 0.0013 | 0.5627 | 0.5511 | 0.5105 | 0.4364 | 0.4532 | -0.045 ± 0.0085 | -0.0117 (6) |
| 10-15 | 2301 | 0.197 | 0.1845 | +0.0125 ± 0.0022 | 0.5797 | 0.539 | 0.5171 | 0.3926 | 0.4072 | -0.053 ± 0.0091 | -0.0189 (18) |
| 15-25 | 3319 | 0.2159 | 0.1763 | +0.0396 ± 0.0029 | 0.6274 | 0.5202 | 0.5304 | 0.334 | 0.3347 | -0.073 ± 0.0074 | -0.0086 (42) |
| 25-40 | 2931 | 0.2477 | 0.1368 | +0.1109 ± 0.0043 | 0.702 | 0.4184 | 0.5577 | 0.2417 | 0.2262 | -0.083 ± 0.0068 | -0.0044 (18) |
| 40+ | 2242 | 0.3982 | 0.0671 | +0.3311 ± 0.0062 | 1.0442 | 0.234 | 0.6617 | 0.1257 | 0.0981 | -0.067 ± 0.0054 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 457 | 0.1924 | 0.1951 | -0.0026 ± 0.0007 | 0.5636 | 0.5702 | 0.4941 | 0.4788 | 0.5536 | -0.002 ± 0.021 | -0.0137 (8) |
| 3-5 | 333 | 0.1898 | 0.1877 | +0.0021 ± 0.0019 | 0.5561 | 0.5512 | 0.5004 | 0.4609 | 0.4565 | -0.116 ± 0.0249 | 0.0067 (3) |
| 5-10 | 675 | 0.2026 | 0.1984 | +0.0042 ± 0.0026 | 0.5925 | 0.5791 | 0.5042 | 0.4305 | 0.4356 | -0.096 ± 0.0176 | -0.0071 (7) |
| 10-15 | 527 | 0.2068 | 0.2065 | +0.0003 ± 0.0049 | 0.601 | 0.5962 | 0.5362 | 0.4132 | 0.4763 | -0.060 ± 0.0196 | -0.0317 (6) |
| 15-25 | 617 | 0.2363 | 0.21 | +0.0263 ± 0.0072 | 0.6723 | 0.604 | 0.5831 | 0.3896 | 0.4182 | -0.111 ± 0.0182 | -0.03 (1) |
| 25-40 | 380 | 0.2109 | 0.2126 | -0.0017 ± 0.0138 | 0.6092 | 0.6084 | 0.6495 | 0.34 | 0.4947 | -0.041 ± 0.0211 | 0.015 (2) |
| 40+ | 70 | 0.3064 | 0.1929 | +0.1135 ± 0.0469 | 0.8277 | 0.5631 | 0.7471 | 0.294 | 0.4 | -0.086 ± 0.0496 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2098 | 0.184 | 0.1849 | -0.0009 ± 0.0003 | 0.5426 | 0.5441 | 0.4828 | 0.4675 | 0.4957 | -0.024 ± 0.0095 | -0.0163 (35) |
| 3-5 | 1444 | 0.1875 | 0.1843 | +0.0032 ± 0.0009 | 0.552 | 0.5443 | 0.4798 | 0.4403 | 0.4204 | -0.083 ± 0.0116 | -0.0094 (18) |
| 5-10 | 3184 | 0.1942 | 0.1875 | +0.0066 ± 0.0012 | 0.5724 | 0.5511 | 0.4802 | 0.4063 | 0.3964 | -0.070 ± 0.0077 | -0.01 (31) |
| 10-15 | 2457 | 0.1941 | 0.1796 | +0.0145 ± 0.0021 | 0.5724 | 0.5284 | 0.495 | 0.3718 | 0.3748 | -0.063 ± 0.0085 | -0.015 (12) |
| 15-25 | 3250 | 0.2101 | 0.1691 | +0.0409 ± 0.0028 | 0.6147 | 0.5015 | 0.5042 | 0.3089 | 0.3031 | -0.075 ± 0.0072 | -0.03 (2) |
| 25-40 | 2435 | 0.2152 | 0.1251 | +0.0902 ± 0.0045 | 0.6223 | 0.3849 | 0.5249 | 0.2094 | 0.2279 | -0.055 ± 0.0068 | 0.01 (3) |
| 40+ | 1624 | 0.3893 | 0.0464 | +0.3429 ± 0.006 | 1.0156 | 0.1794 | 0.6354 | 0.1083 | 0.0585 | -0.085 ± 0.0051 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 793 | 0.1951 | 0.1953 | -0.0002 ± 0.0005 | 0.5705 | 0.5707 | 0.5073 | 0.4922 | 0.4994 | -0.047 ± 0.0157 | -0.0224 (49) |
| 3-5 | 566 | 0.1945 | 0.1939 | +0.0006 ± 0.0015 | 0.5672 | 0.5643 | 0.4808 | 0.441 | 0.4505 | -0.048 ± 0.0186 | -0.0194 (34) |
| 5-10 | 1185 | 0.1965 | 0.1908 | +0.0057 ± 0.0019 | 0.5792 | 0.5628 | 0.4885 | 0.4149 | 0.4135 | -0.063 ± 0.0129 | -0.005 (78) |
| 10-15 | 744 | 0.2085 | 0.197 | +0.0115 ± 0.0041 | 0.6059 | 0.5759 | 0.5057 | 0.3826 | 0.3965 | -0.055 ± 0.0164 | 0.0014 (64) |
| 15-25 | 998 | 0.2336 | 0.2117 | +0.0219 ± 0.0057 | 0.6657 | 0.6093 | 0.5634 | 0.3687 | 0.4108 | -0.056 ± 0.0146 | -0.0214 (59) |
| 25-40 | 579 | 0.2506 | 0.1962 | +0.0544 ± 0.0114 | 0.7067 | 0.5702 | 0.646 | 0.3337 | 0.4007 | -0.080 ± 0.0171 | -0.0219 (26) |
| 40+ | 193 | 0.3701 | 0.1933 | +0.1769 ± 0.0321 | 1.0713 | 0.5679 | 0.793 | 0.3026 | 0.3886 | -0.075 ± 0.029 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2361 | 0.187 | 0.187 | -0.0001 ± 0.0003 | 0.5493 | 0.5485 | 0.502 | 0.4866 | 0.4972 | -0.034 ± 0.0089 | -0.0157 (88) |
| 3-5 | 1613 | 0.1878 | 0.1854 | +0.0024 ± 0.0009 | 0.55 | 0.5443 | 0.4886 | 0.449 | 0.4389 | -0.056 ± 0.0108 | -0.0209 (69) |
| 5-10 | 3291 | 0.1931 | 0.1856 | +0.0075 ± 0.0011 | 0.5709 | 0.5491 | 0.4823 | 0.4086 | 0.3971 | -0.063 ± 0.0076 | -0.0082 (132) |
| 10-15 | 2205 | 0.2044 | 0.1899 | +0.0146 ± 0.0023 | 0.5968 | 0.5581 | 0.5107 | 0.3877 | 0.39 | -0.056 ± 0.0093 | -0.0053 (105) |
| 15-25 | 2789 | 0.2303 | 0.1982 | +0.0321 ± 0.0033 | 0.6638 | 0.5758 | 0.5551 | 0.36 | 0.3768 | -0.062 ± 0.0085 | -0.0253 (107) |
| 25-40 | 1899 | 0.2539 | 0.1699 | +0.0839 ± 0.006 | 0.7196 | 0.5021 | 0.6072 | 0.2932 | 0.3186 | -0.075 ± 0.0092 | -0.0229 (51) |
| 40+ | 913 | 0.385 | 0.1309 | +0.2541 ± 0.0128 | 1.0918 | 0.3995 | 0.7089 | 0.2019 | 0.218 | -0.068 ± 0.0114 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3059 | 1.062 ± 0.051 | 1.165 | 0.1682 | 0.1714 | 0.2114 | 0.2022 |
| gen2 | 3059 | 0.867 ± 0.046 | 1.122 | 0.1754 | 0.1714 | 0.2292 | 0.2022 |
| gen1_elo | 3059 | 1.043 ± 0.05 | 1.15 | 0.1734 | 0.1718 | 0.2106 | 0.2021 |
| gen1_sr | 3059 | 1.077 ± 0.06 | 1.189 | 0.1349 | 0.1731 | 0.2253 | 0.202 |
| gen1_ledger | 5058 | 0.875 ± 0.035 | 1.075 | 0.1772 | 0.1858 | 0.2179 | 0.1976 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 14,422)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,613 | 25.1% |
| STALE_QUOTE | market_freshness | 3,020 | 20.9% |
| BOOK_QUALITY | execution | 2,574 | 17.8% |
| POOR_DATA | data | 1,584 | 11.0% |
| LIMITED_DATA | data | 1,025 | 7.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 785 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 684 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 566 | 3.9% |
| IN_PLAY_QUOTE | market_freshness/coverage | 406 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 165 | 1.1% |

Cause class: coverage 25.1%, market_freshness 20.9%, data 18.1%, execution 17.8%, market_freshness/coverage 8.3%, model_calibration_or_unknown 4.7%, mapping 3.9%, model_calibration 1.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 95.9%, LOW_DATA_QUALITY 69.1%, THIN_PLAYER_HISTORY 57.9%, STALE_PLAYER_DATA 52.0%, STALE_KALSHI_QUOTE 45.6%, MODEL_INTERNAL_DISAGREEMENT 39.5%, ASYMMETRIC_SAMPLE_SIZE 31.7%, WIDE_SPREAD 23.6%, MODEL_HIGH_UNCERTAINTY 17.6%, PLAYER_IDENTITY_RISK 14.0%, LEVEL_TRANSFER_RISK 8.3%, EVENT_MAPPING_RISK 8.0%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 3.5%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 27.4%, POST_SETTLEMENT_OBSERVATION 25.1%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 7,760)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,855 | 36.8% |
| STALE_QUOTE | market_freshness | 1,419 | 18.3% |
| BOOK_QUALITY | execution | 1,340 | 17.3% |
| POOR_DATA | data | 641 | 8.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 423 | 5.5% |
| IDENTITY_AMBIGUOUS | mapping | 330 | 4.2% |
| LIMITED_DATA | data | 307 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 250 | 3.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 156 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 39 | 0.5% |

Cause class: coverage 36.8%, market_freshness 18.3%, execution 17.3%, data 12.2%, market_freshness/coverage 8.7%, mapping 4.2%, model_calibration_or_unknown 2.0%, model_calibration 0.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.9%, START_UNVERIFIABLE 98.2%, LOW_DATA_QUALITY 72.6%, THIN_PLAYER_HISTORY 60.1%, STALE_KALSHI_QUOTE 54.1%, STALE_PLAYER_DATA 46.9%, MODEL_INTERNAL_DISAGREEMENT 40.4%, ASYMMETRIC_SAMPLE_SIZE 33.5%, WIDE_SPREAD 23.3%, MODEL_HIGH_UNCERTAINTY 18.1%, PLAYER_IDENTITY_RISK 17.3%, EVENT_MAPPING_RISK 9.6%, LOW_DISPLAYED_LIQUIDITY 8.0%, LEVEL_TRANSFER_RISK 7.3%, MODEL_CALIBRATION_OUTLIER 4.4%, EXTERNAL_MARKET_REJECTION 1.0%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 39.5%, POST_SETTLEMENT_OBSERVATION 36.8%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 6215, "IDENTITY_AMBIGUOUS": 1545}; ticker orientation: {"VERIFIED": 7760}.

Checks: discipline:AMBIGUOUS 519, discipline:PASS 7241, identity_confidence:AMBIGUOUS 1346, identity_confidence:PASS 6414, level_mapping:NA 531, level_mapping:PASS 7229, market_pair:AMBIGUOUS 283, market_pair:NA 194, market_pair:PASS 7283, model_complement:NA 161, model_complement:PASS 7599, namesake:PASS 7760, physical_match_id:NA 2894, physical_match_id:PASS 4866, player_ids:PASS 7760, same_pair_other_event:PASS 7760, ticker_orientation:PASS 7760

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,131 | 1.5% | 1.4% | 0.4% | {"market_freshness": 20, "execution": 8, "data": 2, "market_freshness/coverage": 1} | 5.24 | 0.2088 / 0.2109 (259) | 16.2% | 0.8% | 5.3% | 1.6% |
| CHALLENGER | 5,530 | 17.2% | 5.9% | 12.3% | {"coverage": 581, "market_freshness/coverage": 120, "market_freshness": 112, "data": 63, "model_calibration_or_unknown": 47, "execution": 13, "model_calibration": 9, "mapping": 6} | 7.17 | 0.2177 / 0.2048 (1455) | 37.4% | 9.3% | 2.4% | 23.0% |
| DOUBLES | 1,060 | 49.0% | 48.5% | 6.7% | {"execution": 212, "mapping": 154, "market_freshness": 106, "market_freshness/coverage": 40, "coverage": 7} | 24.07 | 0.3273 / 0.2332 (325) | 22.1% | 0.0% | 100.0% | 8.1% |
| ITF_MEN | 10,436 | 24.6% | 16.9% | 33.1% | {"coverage": 1008, "execution": 522, "market_freshness": 403, "data": 346, "market_freshness/coverage": 204, "mapping": 87, "model_calibration_or_unknown": 2} | 11.12 | 0.2133 / 0.1945 (2570) | 36.6% | 61.0% | 12.2% | 22.9% |
| ITF_WOMEN | 12,918 | 26.3% | 18.9% | 43.8% | {"coverage": 1242, "market_freshness": 703, "execution": 559, "data": 503, "market_freshness/coverage": 259, "mapping": 77, "model_calibration_or_unknown": 45, "model_calibration": 10} | 12.53 | 0.2019 / 0.192 (2707) | 39.3% | 57.1% | 10.0% | 22.5% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,759 | 6.0% | 5.4% | 1.4% | {"market_freshness": 36, "model_calibration_or_unknown": 23, "execution": 12, "data": 11, "market_freshness/coverage": 10, "model_calibration": 9, "coverage": 4, "mapping": 1} | 7.59 | 0.2398 / 0.2312 (289) | 25.1% | 1.7% | 1.9% | 3.1% |
| WTA125 | 1,330 | 12.9% | 10.1% | 2.2% | {"market_freshness/coverage": 38, "model_calibration_or_unknown": 37, "market_freshness": 37, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.32 | 0.2167 / 0.2061 (470) | 22.9% | 7.7% | 4.5% | 10.1% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 5 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 6 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 7 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 17.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1037 min (STALE); no external reference |
| 9 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 10 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 11 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 12 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 13 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 14 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 15 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 16 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 17 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 18 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 19 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 20 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 22 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 23 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 24 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 25 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 26 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 27 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 92 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 28 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 29 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 30 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 31 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 32 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 162 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 33 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 34 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 35 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 36 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 37 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 547 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 38 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 39 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFWMATCH-26OCT16ESTLAB-LAB` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 68 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1475.0, ratio 2.28); no external reference |
| 41 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 42 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 43 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 44 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 45 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 46 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 47 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 48 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 49 | `KXATPCHALLENGERMATCH-26OCT13GIUSEA-SEA` | CHALLENGER | fair_v1 | 76% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 243 min (STALE); no external reference |
| 50 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 189 min (STALE); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9823, "by_level_share_of_ge_25pp": {"ATP": 0.004, "CHALLENGER": 0.1226, "DOUBLES": 0.0669, "ITF_MEN": 0.3314, "ITF_WOMEN": 0.4379, "OTHER": 0.0015, "WTA": 0.0137, "WTA125": 0.022}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5409, "share_primary_cause_market_settled_or_in_play": 0.4546, "share_primary_cause_stale_quote_only": 0.1829}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 7760, "identity_ambiguous_share": 0.1991, "ticker_orientation": {"VERIFIED": 7760}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 4866, "with_external": 187, "coverage": 0.0384, "external_status": {"EXTERNAL_STALE": 129, "AGREES_WITH_KALSHI": 55, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 129, "MODEL_LONE_OUTLIER": 55, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.2941, "share_external_supports_model": 0.016}, "pregame_clean_ge_25pp": {"n": 2311, "with_external": 176, "coverage": 0.0762, "external_status": {"EXTERNAL_STALE": 120, "AGREES_WITH_KALSHI": 53, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 120, "MODEL_LONE_OUTLIER": 53, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3011, "share_external_supports_model": 0.017}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 562.0, "median_sample_ratio": 2.36, "median_min_matches": 20.0, "median_max_days_since_last": 204.0, "share_severe_asymmetry": 0.2027, "data_status": {"POOR": 4138, "LIMITED": 2200, "ADEQUATE": 1422}, "comparison_lt_10pp": {"median_thinner_serve_points": 1791.0, "median_sample_ratio": 1.69, "median_min_matches": 89.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 620, "model_minus_observed": 0.0522, "kalshi_minus_observed": -0.0805, "brier_diff_model_minus_kalshi": -0.0001}, "4-10x": {"n": 413, "model_minus_observed": 0.0736, "kalshi_minus_observed": -0.0641, "brier_diff_model_minus_kalshi": 0.0075}, "<2x": {"n": 1522, "model_minus_observed": 0.0833, "kalshi_minus_observed": -0.0387, "brier_diff_model_minus_kalshi": 0.0113}, ">=10x": {"n": 504, "model_minus_observed": 0.1252, "kalshi_minus_observed": -0.0413, "brier_diff_model_minus_kalshi": 0.0153}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3059, "model": {"intercept": -0.544, "slope": 0.867, "slope_se": 0.046}, "kalshi_mid_same_rows": {"intercept": 0.231, "slope": 1.122, "slope_se": 0.052}, "mean_extremity_model": 0.1754, "mean_extremity_kalshi": 0.1714, "model_brier": 0.2292, "kalshi_brier": 0.2022, "brier_diff_model_minus_kalshi": 0.027, "brier_diff_se": 0.0034, "model_logloss": 0.6539, "kalshi_logloss": 0.5864}, "fair_v1": {"n": 3059, "model": {"intercept": -0.402, "slope": 1.062, "slope_se": 0.051}, "kalshi_mid_same_rows": {"intercept": 0.31, "slope": 1.165, "slope_se": 0.053}, "mean_extremity_model": 0.1682, "mean_extremity_kalshi": 0.1714, "model_brier": 0.2114, "kalshi_brier": 0.2022, "brier_diff_model_minus_kalshi": 0.0092, "brier_diff_se": 0.0027, "model_logloss": 0.6102, "kalshi_logloss": 0.5863}, "gen1_elo": {"n": 3059, "model": {"intercept": -0.395, "slope": 1.043, "slope_se": 0.05}, "kalshi_mid_same_rows": {"intercept": 0.301, "slope": 1.15, "slope_se": 0.052}, "mean_extremity_model": 0.1734, "mean_extremity_kalshi": 0.1718, "model_brier": 0.2106, "kalshi_brier": 0.2021, "brier_diff_model_minus_kalshi": 0.0085, "brier_diff_se": 0.0027, "model_logloss": 0.6093, "kalshi_logloss": 0.586}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2462, "share_ge_15": 0.4384, "median_abs_gap": 13.01, "n": 19767}, "gen1_elo": {"share_ge_25": 0.2401, "share_ge_15": 0.4317, "median_abs_gap": 12.49, "n": 19767}, "gen1_sr": {"share_ge_25": 0.3082, "share_ge_15": 0.5242, "median_abs_gap": 15.92, "n": 19767}, "gen2": {"share_ge_25": 0.309, "share_ge_15": 0.5093, "median_abs_gap": 15.45, "n": 19767}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1518, "share_ge_15": 0.3498, "median_abs_gap": 10.65, "n": 15227}, "gen1_elo": {"share_ge_25": 0.1491, "share_ge_15": 0.3392, "median_abs_gap": 10.12, "n": 15226}, "gen1_sr": {"share_ge_25": 0.2145, "share_ge_15": 0.4454, "median_abs_gap": 13.3, "n": 15227}, "gen2": {"share_ge_25": 0.2275, "share_ge_15": 0.4412, "median_abs_gap": 13.02, "n": 15228}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.24, "share_ge_25_all": 0.0145, "share_ge_25_pregame_clean": 0.0143}, "WTA": {"median_abs_gap_pregame_clean": 7.59, "share_ge_25_all": 0.0603, "share_ge_25_pregame_clean": 0.054}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2388, "share_within_10pp_all": 0.439, "share_within_10pp_pregame_clean": 0.4972, "corr_model_vs_mid_pregame_clean": 0.8436}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 476, "model_brier": 0.1925, "kalshi_brier": 0.1938, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 540, "model_brier": 0.2124, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0085}, "15-25": {"n_settled": 669, "model_brier": 0.2307, "kalshi_brier": 0.216, "brier_diff_model_minus_kalshi": 0.0146}, "25-40": {"n_settled": 362, "model_brier": 0.2244, "kalshi_brier": 0.2087, "brier_diff_model_minus_kalshi": 0.0158}, "3-5": {"n_settled": 295, "model_brier": 0.1905, "kalshi_brier": 0.1909, "brier_diff_model_minus_kalshi": -0.0004}, "40+": {"n_settled": 74, "model_brier": 0.2888, "kalshi_brier": 0.1769, "brier_diff_model_minus_kalshi": 0.1119}, "5-10": {"n_settled": 643, "model_brier": 0.1979, "kalshi_brier": 0.1973, "brier_diff_model_minus_kalshi": 0.0006}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.544, "slope": 0.867, "slope_se": 0.046}, "kalshi_slope": {"intercept": 0.231, "slope": 1.122, "slope_se": 0.052}, "n": 3059}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.515, "slope": 0.875, "slope_se": 0.035}, "kalshi_slope": {"intercept": 0.142, "slope": 1.075, "slope_se": 0.039}, "n": 5058}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 325, "model_brier": 0.3273, "kalshi_brier": 0.2332, "brier_diff_model_minus_kalshi": 0.0942, "brier_diff_se": 0.0175, "corr_model_outcome": 0.011, "corr_kalshi_outcome": 0.258}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
