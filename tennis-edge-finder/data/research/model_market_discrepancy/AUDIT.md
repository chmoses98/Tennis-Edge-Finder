# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-19T05:27Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 39,856): 0-3 14.4%, 3-5 9.5%, 5-10 19.9%, 10-15 15.4%, 15-25 19.0%, 25-40 13.7%, 40+ 8.1%; median gap 11.87 pp.
* **Where the extremes live**: 97.5% of >=25 pp gaps are off the ATP/WTA main tour (ITF 75.5%, Challenger 12.4%, doubles 7.4%). Main tour: ATP 3.6% and WTA 4.9% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 8,672): MARKET_ALREADY_SETTLED_WHEN_PRICED 35.2%, BOOK_QUALITY 19.2%, STALE_QUOTE 17.8%, POOR_DATA 8.6%, POSSIBLY_IN_PLAY_QUOTE 5.2%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 3.8%, IN_PLAY_QUOTE 3.2%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.5%. By class: coverage 35.2%, execution 19.2%, market_freshness 17.8%, data 12.4%, market_freshness/coverage 8.5%, mapping 4.3%, model_calibration_or_unknown 2.0%, model_calibration 0.5%.
* **Stale / settled / in-play**: 52.0% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.7% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 8,672 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.9% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.1%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 23.2% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 533.0 points vs 1827.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.058, Gen-2 0.842, Gen-1 ledger 0.884 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 415 model 0.2202 vs Kalshi 0.2107; n 84 model 0.2967 vs Kalshi 0.1739.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 168,044 model-market comparisons (273,546 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 59,782 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-19T05:18:13.884978+00:00'], shadow board 44,267 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-19T05:18:16.922290+00:00'], Model 4 20,160 rows, 16,316 settled tickers, 5,537 tickers with an external scan.
* By model: {"gen1_ledger": 40416, "gen1_elo": 22261, "fair_v1": 22261, "gen2": 22261, "gen1_sr": 22261, "model4_fundamental": 19301, "model4_conditioned": 19283}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 39,856 | 14.4 | 9.5 | 19.9 | 15.4 | 19.0 | 13.7 | 8.1 | 11.87 | 40.7% | 21.8% |
| MW fair_v1 | 22,261 | 13.5 | 8.6 | 18.5 | 15.9 | 19.4 | 14.5 | 9.7 | 12.95 | 43.5% | 24.2% |
| MW gen1_elo | 22,261 | 13.1 | 9.1 | 19.5 | 15.2 | 19.5 | 14.4 | 9.3 | 12.54 | 43.1% | 23.7% |
| MW gen1_ledger | 17,595 | 15.5 | 10.8 | 21.7 | 14.8 | 18.5 | 12.6 | 6.1 | 10.48 | 37.2% | 18.7% |
| MW gen1_sr | 22,261 | 9.8 | 7.3 | 16.8 | 14.3 | 21.4 | 18.4 | 12.0 | 15.62 | 51.7% | 30.4% |
| MW gen2 | 22,261 | 11.4 | 7.2 | 16.4 | 14.3 | 19.9 | 17.5 | 13.2 | 15.33 | 50.6% | 30.7% |
| all families model4_conditioned | 19,283 | 21.7 | 18.9 | 34.5 | 17.5 | 4.8 | 1.5 | 1.1 | 5.98 | 7.4% | 2.6% |
| all families model4_fundamental | 19,301 | 16.1 | 12.9 | 34.6 | 20.4 | 11.2 | 3.4 | 1.4 | 7.91 | 16.0% | 4.8% |

Configurable thresholds (primary): >=5pp 76.0%, >=10pp 56.1%, >=15pp 40.7%, >=20pp 30.2%, >=25pp 21.8%, >=30pp 15.7%, >=40pp 8.1%, >=50pp 3.6%
Executable gap (model outside the book, before fees): median 8.18pp; >=10pp 44.5%, >=25pp 16.9%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,894 | 29.5 | 13.1 | 24.6 | 16.9 | 11.7 | 3.6 | 0.6 | 6.33 | 16.0% | 4.2% |
| CHALLENGER | 3,718 | 15.7 | 10.2 | 20.2 | 16.0 | 14.6 | 12.3 | 11.1 | 11.31 | 37.9% | 23.4% |
| ITF_MEN | 5,974 | 11.0 | 7.9 | 17.3 | 14.9 | 20.1 | 16.3 | 12.5 | 14.64 | 48.9% | 28.9% |
| ITF_WOMEN | 8,687 | 10.2 | 6.8 | 15.8 | 15.5 | 22.5 | 18.2 | 11.0 | 15.61 | 51.7% | 29.2% |
| WTA | 1,328 | 18.6 | 12.3 | 25.1 | 19.4 | 19.4 | 4.4 | 0.8 | 8.34 | 24.6% | 5.3% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,894 | 23.8 | 14.8 | 24.0 | 17.9 | 14.2 | 4.4 | 0.9 | 6.86 | 19.5% | 5.3% |
| CHALLENGER | 3,718 | 14.8 | 8.2 | 18.9 | 13.8 | 18.0 | 14.2 | 12.1 | 12.77 | 44.3% | 26.3% |
| ITF_MEN | 5,974 | 9.3 | 6.7 | 15.6 | 13.5 | 19.8 | 19.4 | 15.7 | 17.04 | 54.9% | 35.1% |
| ITF_WOMEN | 8,687 | 8.4 | 5.6 | 13.7 | 13.6 | 21.1 | 20.9 | 16.8 | 18.87 | 58.8% | 37.7% |
| WTA | 1,328 | 16.3 | 8.5 | 20.3 | 16.6 | 22.7 | 14.6 | 0.9 | 11.46 | 38.2% | 15.5% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,894 | 24.8 | 13.6 | 25.8 | 16.7 | 13.9 | 4.5 | 0.7 | 6.82 | 19.1% | 5.2% |
| CHALLENGER | 3,718 | 14.6 | 10.1 | 20.9 | 15.1 | 15.8 | 12.1 | 11.3 | 11.16 | 39.2% | 23.4% |
| ITF_MEN | 5,974 | 10.0 | 8.0 | 17.7 | 14.1 | 20.9 | 16.8 | 12.5 | 15.02 | 50.2% | 29.3% |
| ITF_WOMEN | 8,687 | 9.5 | 7.0 | 16.4 | 15.6 | 23.0 | 18.3 | 10.2 | 15.58 | 51.6% | 28.5% |
| WTA | 1,328 | 23.8 | 17.5 | 30.3 | 15.1 | 10.7 | 2.1 | 0.5 | 6.0 | 13.3% | 2.6% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,137 | 27.5 | 20.3 | 31.3 | 11.5 | 6.8 | 2.5 | 0.1 | 5.23 | 9.3% | 2.5% |
| CHALLENGER | 2,598 | 21.9 | 14.9 | 27.1 | 14.2 | 14.1 | 6.0 | 1.9 | 7.08 | 21.9% | 7.8% |
| DOUBLES | 1,324 | 4.6 | 4.2 | 10.4 | 10.8 | 21.1 | 25.8 | 23.0 | 24.16 | 69.9% | 48.8% |
| ITF_MEN | 4,980 | 14.5 | 8.7 | 20.7 | 15.8 | 20.9 | 12.4 | 7.0 | 11.86 | 40.4% | 19.5% |
| ITF_WOMEN | 5,736 | 11.7 | 9.1 | 19.3 | 14.8 | 22.1 | 16.9 | 6.2 | 13.17 | 45.1% | 23.0% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 939 | 22.6 | 15.9 | 29.5 | 17.2 | 10.5 | 3.9 | 0.3 | 6.82 | 14.8% | 4.3% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,855 | 29.7 | 13.2 | 24.9 | 16.8 | 11.5 | 3.3 | 0.7 | 6.17 | 15.5% | 3.9% |
| CHALLENGER | 2,660 | 20.3 | 12.7 | 25.2 | 18.6 | 14.8 | 6.3 | 2.1 | 8.25 | 23.2% | 8.4% |
| ITF_MEN | 4,329 | 13.6 | 9.9 | 20.6 | 16.8 | 20.4 | 13.1 | 5.6 | 11.64 | 39.1% | 18.7% |
| ITF_WOMEN | 6,509 | 11.9 | 8.1 | 17.9 | 17.6 | 24.1 | 15.4 | 4.9 | 13.34 | 44.4% | 20.3% |
| WTA | 1,302 | 18.7 | 11.9 | 25.2 | 19.4 | 19.5 | 4.4 | 0.8 | 8.36 | 24.7% | 5.2% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,855 | 23.9 | 15.0 | 24.1 | 17.9 | 14.0 | 4.2 | 0.8 | 6.73 | 19.0% | 5.0% |
| CHALLENGER | 2,660 | 18.8 | 10.4 | 23.6 | 16.6 | 18.5 | 9.5 | 2.6 | 9.25 | 30.6% | 12.1% |
| ITF_MEN | 4,330 | 11.0 | 8.0 | 18.1 | 15.4 | 22.0 | 17.0 | 8.6 | 14.14 | 47.5% | 25.6% |
| ITF_WOMEN | 6,509 | 9.3 | 6.3 | 15.1 | 14.9 | 23.2 | 20.4 | 10.7 | 16.65 | 54.3% | 31.1% |
| WTA | 1,302 | 16.2 | 8.4 | 20.4 | 16.6 | 22.7 | 14.8 | 0.9 | 11.5 | 38.4% | 15.7% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,104 | 27.7 | 20.5 | 31.5 | 11.7 | 6.2 | 2.3 | 0.1 | 5.11 | 8.6% | 2.4% |
| CHALLENGER | 2,255 | 23.5 | 16.2 | 28.9 | 14.0 | 13.3 | 3.5 | 0.6 | 6.5 | 17.4% | 4.1% |
| DOUBLES | 1,231 | 4.6 | 4.4 | 10.6 | 11.0 | 21.0 | 26.0 | 22.4 | 24.07 | 69.5% | 48.4% |
| ITF_MEN | 4,121 | 15.9 | 9.4 | 22.6 | 16.7 | 20.7 | 10.6 | 4.2 | 10.61 | 35.4% | 14.8% |
| ITF_WOMEN | 4,743 | 12.5 | 9.7 | 20.9 | 15.6 | 22.3 | 15.6 | 3.5 | 11.9 | 41.3% | 19.0% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 900 | 22.9 | 16.3 | 29.8 | 17.2 | 10.7 | 3.1 | 0.0 | 6.7 | 13.8% | 3.1% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,324 | 4.6 | 4.2 | 10.4 | 10.8 | 21.1 | 25.8 | 23.0 | 24.16 | 69.9% | 48.8% |
| singles | 16,271 | 16.4 | 11.3 | 22.6 | 15.1 | 18.3 | 11.5 | 4.8 | 9.9 | 34.5% | 16.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 5,084 | 13.6 | 8.9 | 19.3 | 15.9 | 18.1 | 14.4 | 9.7 | 12.65 | 42.3% | 24.1% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 14,356 | 13.9 | 8.5 | 18.4 | 15.6 | 19.7 | 14.3 | 9.6 | 12.95 | 43.6% | 23.9% |
| UNKNOWN | 2,584 | 11.8 | 7.8 | 17.0 | 18.3 | 19.5 | 15.7 | 9.9 | 13.3 | 45.2% | 25.7% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,547 | 19.9 | 10.9 | 21.3 | 17.4 | 15.8 | 8.6 | 6.1 | 9.34 | 30.5% | 14.7% |
| B | 2,882 | 13.2 | 9.2 | 19.9 | 16.9 | 18.4 | 11.9 | 10.6 | 12.08 | 40.9% | 22.5% |
| C | 3,218 | 12.7 | 9.3 | 19.4 | 14.6 | 19.3 | 14.8 | 9.9 | 12.8 | 44.0% | 24.7% |
| D | 3,733 | 12.4 | 8.0 | 17.2 | 15.5 | 21.9 | 15.5 | 9.5 | 13.85 | 46.9% | 25.0% |
| F | 5,881 | 7.8 | 5.6 | 14.9 | 14.8 | 22.2 | 21.5 | 13.2 | 17.85 | 56.9% | 34.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,190 | 23.3 | 15.9 | 28.8 | 15.1 | 11.3 | 4.0 | 1.4 | 6.61 | 16.8% | 5.5% |
| B | 2,500 | 15.3 | 10.1 | 24.0 | 16.4 | 19.3 | 11.0 | 4.0 | 10.12 | 34.3% | 15.0% |
| C | 3,558 | 11.2 | 7.5 | 17.8 | 14.2 | 21.6 | 16.4 | 11.2 | 14.61 | 49.2% | 27.6% |
| D | 2,556 | 14.0 | 9.9 | 20.5 | 13.8 | 20.9 | 14.5 | 6.6 | 12.04 | 41.9% | 21.1% |
| F | 3,791 | 10.1 | 7.9 | 15.0 | 14.3 | 23.3 | 20.4 | 8.9 | 16.19 | 52.6% | 29.4% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 7,443 | 18.1 | 9.9 | 20.6 | 17.2 | 16.2 | 9.5 | 8.5 | 10.42 | 34.2% | 18.0% |
| LIMITED | 5,009 | 14.5 | 10.4 | 20.4 | 15.4 | 18.8 | 13.2 | 7.4 | 11.46 | 39.4% | 20.6% |
| POOR | 9,809 | 9.6 | 6.6 | 15.8 | 15.2 | 22.0 | 19.0 | 11.7 | 15.96 | 52.7% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,382 | 26.9 | 21.8 | 34.9 | 11.2 | 3.8 | 1.2 | 0.2 | 5.09 | 5.2% | 1.4% |
| GAME_SPREAD | 3,893 | 23.7 | 15.4 | 34.3 | 17.4 | 7.2 | 1.8 | 0.2 | 6.39 | 9.2% | 2.0% |
| MATCH_WINNER | 17,595 | 15.5 | 10.8 | 21.7 | 14.8 | 18.5 | 12.6 | 6.1 | 10.48 | 37.2% | 18.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 8,229 | 30.5 | 17.7 | 30.4 | 12.2 | 7.6 | 1.2 | 0.4 | 5.21 | 9.3% | 1.6% |
| TOTAL_GAMES | 6,293 | 7.2 | 8.8 | 37.1 | 29.1 | 11.2 | 3.5 | 3.0 | 9.65 | 17.8% | 6.6% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,752 | 25.1 | 34.4 | 32.6 | 3.7 | 3.5 | 0.6 | 0.2 | 4.48 | 4.3% | 0.8% |
| GAME_SPREAD | 4,630 | 45.9 | 16.9 | 27.4 | 7.1 | 1.8 | 0.6 | 0.3 | 3.42 | 2.7% | 0.9% |
| TOTAL_GAMES | 7,901 | 4.6 | 6.8 | 40.4 | 35.5 | 7.7 | 2.7 | 2.4 | 9.83 | 12.8% | 5.1% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,755 | 24.4 | 17.6 | 36.0 | 12.0 | 7.1 | 2.6 | 0.4 | 5.84 | 10.0% | 2.9% |
| GAME_SPREAD | 4,633 | 19.3 | 13.5 | 28.7 | 20.0 | 13.8 | 3.8 | 0.9 | 7.89 | 18.5% | 4.7% |
| TOTAL_GAMES | 7,913 | 7.3 | 8.5 | 36.8 | 27.7 | 13.2 | 3.9 | 2.6 | 9.72 | 19.8% | 6.5% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 22,261 | 43.5% | 24.2% | 12.95 | 34.9% | 15.0% | 10.7 |
| gen1_elo | 22,261 | 43.1% | 23.7% | 12.54 | 34.2% | 14.9% | 10.21 |
| gen1_sr | 22,261 | 51.7% | 30.4% | 15.62 | 44.0% | 21.1% | 13.03 |
| gen2 | 22,261 | 50.6% | 30.7% | 15.33 | 44.0% | 22.7% | 12.99 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 11,887 | 16.3 | 10.4 | 21.4 | 17.5 | 19.7 | 11.4 | 3.3 | 10.51 | 34.4% | 14.6% |
| STALE | 10,374 | 10.3 | 6.5 | 15.0 | 14.2 | 18.9 | 18.1 | 17.0 | 17.08 | 54.0% | 35.1% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 11,063 | 17.0 | 11.5 | 22.9 | 14.7 | 17.3 | 11.7 | 4.9 | 9.66 | 33.9% | 16.6% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 39,856 | 11063 | 15359 | 13434 | 23.7 | 139.0 | 1400.4 |
| ge_15pp | 16,232 | 3747 | 5372 | 7113 | 25.8 | 440.2 | 1380.4 |
| ge_25pp | 8,672 | 1831 | 2330 | 4511 | 32.7 | 582.1 | 1380.4 |
| lt_10pp | 17,482 | 5685 | 7359 | 4438 | 21.7 | 47.7 | 1341.5 |

Current slate `SL-20261019T052657Z-db65eecb`: 866 priced rows, quote age at build {'median': 9.1, 'max': 9.2}, freshness {'FRESH': 866}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 11 | 0.0 | 0.0 | 36.4 | 0.0 | 45.5 | 18.2 | 0.0 | 20.19 | 63.6% | 18.2% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,071 | 21.1 | 10.7 | 23.5 | 19.4 | 18.4 | 6.5 | 0.5 | 8.67 | 25.4% | 7.0% |
| KALSHI_LONE_OUTLIER | 11 | 9.1 | 0.0 | 72.7 | 0.0 | 9.1 | 9.1 | 0.0 | 5.2 | 18.2% | 9.1% |
| MARKETS_AGREE | 360 | 70.0 | 30.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.09 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 743 | 0.0 | 2.8 | 35.5 | 28.5 | 23.1 | 9.3 | 0.7 | 11.98 | 33.1% | 10.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 22,261 | 3208 (14.4%) | 23.2% | 0.7% | {"EXTERNAL_STALE": 2071, "AGREES_WITH_KALSHI": 743, "ALL_AGREE": 360, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 11, "SUPPORTS_MODEL_DIRECTION": 10, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 9,686 | 780 (8.1%) | 31.5% | 1.1% | {"EXTERNAL_STALE": 525, "AGREES_WITH_KALSHI": 246, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 5,379 | 222 (4.1%) | 33.3% | 1.4% | {"EXTERNAL_STALE": 145, "AGREES_WITH_KALSHI": 74, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,590 | 210 (8.1%) | 34.3% | 1.4% | {"EXTERNAL_STALE": 135, "AGREES_WITH_KALSHI": 72, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 9,028 | 1815 (20.1%) | 15.7% | 0.7% | {"EXTERNAL_STALE": 1145, "ALL_AGREE": 360, "AGREES_WITH_KALSHI": 285, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 9, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 4,275 | 11.2 | 7.9 | 19.3 | 15.1 | 21.5 | 15.1 | 9.9 | 13.77 | 46.5% | 25.0% |
| 4-10x | 2,896 | 12.3 | 8.9 | 19.0 | 15.8 | 19.5 | 15.2 | 9.5 | 13.02 | 44.1% | 24.6% |
| <2x | 11,573 | 15.6 | 9.4 | 19.0 | 16.9 | 17.8 | 12.6 | 8.7 | 11.7 | 39.1% | 21.3% |
| >=10x | 3,517 | 10.8 | 6.4 | 15.2 | 13.7 | 21.8 | 19.5 | 12.6 | 16.44 | 53.8% | 32.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 5,743 | 13.1 | 8.5 | 19.5 | 16.1 | 19.6 | 13.1 | 10.2 | 12.78 | 42.8% | 23.3% |
| 300-1000 | 4,932 | 12.2 | 8.7 | 17.1 | 15.8 | 20.7 | 16.1 | 9.4 | 13.72 | 46.2% | 25.5% |
| <300 | 6,700 | 9.0 | 6.0 | 15.4 | 14.8 | 22.0 | 20.1 | 12.7 | 16.86 | 54.9% | 32.9% |
| >=3000 | 4,886 | 21.7 | 12.0 | 22.8 | 17.4 | 14.1 | 6.9 | 5.1 | 8.16 | 26.1% | 11.9% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 675 | 0.5419 | 0.4075 | 0.4904 | +0.052 | -0.083 | -0.0007 ± 0.0058 |
| ratio 4-10x | 460 | 0.5908 | 0.449 | 0.5152 | +0.076 | -0.066 | 0.0081 ± 0.0074 |
| ratio <2x | 1673 | 0.5381 | 0.4169 | 0.4519 | +0.086 | -0.035 | 0.0119 ± 0.0035 |
| ratio >=10x | 563 | 0.5601 | 0.3879 | 0.4458 | +0.114 | -0.058 | 0.0105 ± 0.0076 |
| thinner_sample 1000-3000 | 937 | 0.5436 | 0.4175 | 0.4632 | +0.080 | -0.046 | 0.0078 ± 0.0047 |
| thinner_sample 300-1000 | 803 | 0.5656 | 0.4249 | 0.4969 | +0.069 | -0.072 | 0.0 ± 0.0056 |
| thinner_sample <300 | 1052 | 0.5533 | 0.3911 | 0.4515 | +0.102 | -0.060 | 0.013 ± 0.0054 |
| thinner_sample >=3000 | 579 | 0.5313 | 0.4382 | 0.4611 | +0.070 | -0.023 | 0.0141 ± 0.0048 |
| data_status ADEQUATE | 981 | 0.5341 | 0.4297 | 0.4557 | +0.079 | -0.026 | 0.0113 ± 0.004 |
| data_status LIMITED | 835 | 0.5544 | 0.4241 | 0.491 | +0.063 | -0.067 | 0.0027 ± 0.0051 |
| data_status POOR | 1555 | 0.5571 | 0.3999 | 0.4617 | +0.095 | -0.062 | 0.0102 ± 0.0043 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 517 | 0.1965 | 0.1978 | -0.0013 ± 0.0007 | 0.5718 | 0.5744 | 0.4958 | 0.4809 | 0.53 | -0.051 ± 0.0205 | -0.01 (5) |
| 3-5 | 323 | 0.1973 | 0.1966 | +0.0007 ± 0.002 | 0.5764 | 0.5734 | 0.5057 | 0.4658 | 0.4768 | -0.084 ± 0.0252 | 0.02 (1) |
| 5-10 | 704 | 0.1986 | 0.1984 | +0.0001 ± 0.0025 | 0.5826 | 0.5803 | 0.5133 | 0.4389 | 0.4702 | -0.084 ± 0.0175 | -0.0167 (6) |
| 10-15 | 596 | 0.2152 | 0.2065 | +0.0087 ± 0.0047 | 0.6206 | 0.5952 | 0.523 | 0.3989 | 0.4245 | -0.092 ± 0.0186 | -0.048 (5) |
| 15-25 | 732 | 0.2269 | 0.2133 | +0.0137 ± 0.0067 | 0.6478 | 0.6118 | 0.5805 | 0.3853 | 0.4481 | -0.087 ± 0.0169 | -0.0033 (9) |
| 25-40 | 415 | 0.2202 | 0.2107 | +0.0095 ± 0.0133 | 0.6284 | 0.6043 | 0.6561 | 0.3475 | 0.4867 | -0.065 ± 0.0203 | -0.01 (1) |
| 40+ | 84 | 0.2967 | 0.1739 | +0.1228 ± 0.0408 | 0.801 | 0.521 | 0.7529 | 0.3035 | 0.3929 | -0.119 ± 0.0388 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2450 | 0.1824 | 0.1836 | -0.0013 ± 0.0003 | 0.5398 | 0.5412 | 0.4799 | 0.4648 | 0.5041 | -0.018 ± 0.0088 | -0.0129 (17) |
| 3-5 | 1539 | 0.1942 | 0.1921 | +0.0021 ± 0.0009 | 0.5691 | 0.5601 | 0.478 | 0.4382 | 0.4301 | -0.065 ± 0.0114 | 0.0 (2) |
| 5-10 | 3315 | 0.1931 | 0.1902 | +0.0029 ± 0.0011 | 0.5682 | 0.5588 | 0.4854 | 0.4117 | 0.4268 | -0.049 ± 0.0077 | -0.0119 (21) |
| 10-15 | 2932 | 0.2028 | 0.1845 | +0.0182 ± 0.002 | 0.5933 | 0.5419 | 0.4841 | 0.3594 | 0.3489 | -0.075 ± 0.0079 | -0.0281 (16) |
| 15-25 | 3532 | 0.2079 | 0.1716 | +0.0363 ± 0.0027 | 0.6072 | 0.5074 | 0.5029 | 0.3067 | 0.3131 | -0.068 ± 0.0069 | -0.0025 (44) |
| 25-40 | 2770 | 0.2211 | 0.1276 | +0.0935 ± 0.0042 | 0.6356 | 0.3922 | 0.533 | 0.2198 | 0.231 | -0.064 ± 0.0065 | -0.01 (1) |
| 40+ | 1843 | 0.3779 | 0.0425 | +0.3354 ± 0.0054 | 0.9832 | 0.169 | 0.6281 | 0.1061 | 0.0564 | -0.086 ± 0.0044 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 383 | 0.2011 | 0.2016 | -0.0006 ± 0.0008 | 0.5843 | 0.5855 | 0.5031 | 0.488 | 0.5117 | -0.082 ± 0.0243 | -0.01 (3) |
| 3-5 | 276 | 0.2148 | 0.2146 | +0.0001 ± 0.0023 | 0.6128 | 0.6132 | 0.5154 | 0.4755 | 0.4891 | -0.082 ± 0.0294 | 0.02 (1) |
| 5-10 | 606 | 0.199 | 0.1983 | +0.0007 ± 0.0027 | 0.5815 | 0.5797 | 0.5452 | 0.4703 | 0.5033 | -0.076 ± 0.0187 | -0.01 (4) |
| 10-15 | 557 | 0.2185 | 0.2131 | +0.0053 ± 0.0049 | 0.6274 | 0.6127 | 0.5686 | 0.4443 | 0.4883 | -0.091 ± 0.0203 | -0.04 (5) |
| 15-25 | 809 | 0.2291 | 0.209 | +0.0201 ± 0.0063 | 0.6498 | 0.6004 | 0.5902 | 0.3941 | 0.445 | -0.092 ± 0.0163 | -0.0133 (9) |
| 25-40 | 543 | 0.2653 | 0.1976 | +0.0676 ± 0.012 | 0.7401 | 0.5762 | 0.6658 | 0.3505 | 0.4015 | -0.123 ± 0.0188 | -0.0075 (4) |
| 40+ | 197 | 0.363 | 0.1769 | +0.1861 ± 0.0297 | 1.0109 | 0.5248 | 0.744 | 0.2609 | 0.3249 | -0.074 ± 0.0287 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2068 | 0.1851 | 0.1856 | -0.0005 ± 0.0003 | 0.5463 | 0.5474 | 0.5027 | 0.488 | 0.5106 | -0.034 ± 0.0098 | -0.0133 (15) |
| 3-5 | 1305 | 0.1952 | 0.1944 | +0.0008 ± 0.001 | 0.5662 | 0.564 | 0.5168 | 0.4769 | 0.4866 | -0.044 ± 0.0124 | 0.02 (1) |
| 5-10 | 2942 | 0.1911 | 0.1887 | +0.0025 ± 0.0012 | 0.5646 | 0.5556 | 0.5067 | 0.4328 | 0.4545 | -0.041 ± 0.0081 | -0.0117 (6) |
| 10-15 | 2581 | 0.1998 | 0.1902 | +0.0096 ± 0.0022 | 0.5882 | 0.5533 | 0.5205 | 0.3959 | 0.4219 | -0.046 ± 0.0087 | -0.0189 (18) |
| 15-25 | 3687 | 0.2174 | 0.1789 | +0.0385 ± 0.0027 | 0.6297 | 0.5263 | 0.532 | 0.3359 | 0.3393 | -0.072 ± 0.007 | -0.0086 (42) |
| 25-40 | 3260 | 0.2495 | 0.1368 | +0.1128 ± 0.0041 | 0.705 | 0.4196 | 0.5629 | 0.2468 | 0.2279 | -0.090 ± 0.0064 | -0.0044 (18) |
| 40+ | 2538 | 0.4005 | 0.0659 | +0.3346 ± 0.0059 | 1.0575 | 0.2301 | 0.6625 | 0.1252 | 0.0961 | -0.069 ± 0.005 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 501 | 0.1975 | 0.2001 | -0.0025 ± 0.0007 | 0.5758 | 0.5817 | 0.4995 | 0.4843 | 0.5569 | -0.013 ± 0.0203 | -0.0137 (8) |
| 3-5 | 364 | 0.1929 | 0.1905 | +0.0024 ± 0.0018 | 0.5632 | 0.5576 | 0.4991 | 0.4594 | 0.4505 | -0.120 ± 0.024 | 0.0067 (3) |
| 5-10 | 730 | 0.2013 | 0.1982 | +0.0031 ± 0.0025 | 0.5895 | 0.5786 | 0.5071 | 0.4333 | 0.4466 | -0.094 ± 0.0169 | -0.0071 (7) |
| 10-15 | 583 | 0.2094 | 0.2066 | +0.0028 ± 0.0047 | 0.6069 | 0.5964 | 0.5399 | 0.4169 | 0.47 | -0.076 ± 0.0186 | -0.0317 (6) |
| 15-25 | 683 | 0.2351 | 0.2108 | +0.0243 ± 0.0069 | 0.6695 | 0.6058 | 0.589 | 0.3955 | 0.429 | -0.115 ± 0.0175 | -0.03 (1) |
| 25-40 | 426 | 0.2041 | 0.2159 | -0.0118 ± 0.013 | 0.5928 | 0.616 | 0.6617 | 0.3519 | 0.5235 | -0.040 ± 0.0197 | 0.015 (2) |
| 40+ | 84 | 0.3176 | 0.1877 | +0.1299 ± 0.0426 | 0.8542 | 0.5524 | 0.7573 | 0.3043 | 0.3929 | -0.113 ± 0.0438 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2344 | 0.1882 | 0.1892 | -0.0010 ± 0.0003 | 0.5533 | 0.5551 | 0.4884 | 0.4731 | 0.4996 | -0.028 ± 0.009 | -0.0163 (35) |
| 3-5 | 1610 | 0.1886 | 0.1851 | +0.0035 ± 0.0009 | 0.5551 | 0.5467 | 0.4771 | 0.4377 | 0.4143 | -0.086 ± 0.011 | -0.0094 (18) |
| 5-10 | 3517 | 0.1946 | 0.188 | +0.0066 ± 0.0011 | 0.5736 | 0.5521 | 0.4842 | 0.4103 | 0.4006 | -0.070 ± 0.0073 | -0.01 (31) |
| 10-15 | 2755 | 0.1974 | 0.1809 | +0.0165 ± 0.002 | 0.58 | 0.5315 | 0.4996 | 0.3761 | 0.3717 | -0.072 ± 0.008 | -0.015 (12) |
| 15-25 | 3668 | 0.2093 | 0.1714 | +0.0379 ± 0.0027 | 0.6122 | 0.5072 | 0.507 | 0.3121 | 0.313 | -0.071 ± 0.0068 | -0.03 (2) |
| 25-40 | 2713 | 0.215 | 0.1256 | +0.0895 ± 0.0043 | 0.6219 | 0.3859 | 0.5302 | 0.2142 | 0.2344 | -0.059 ± 0.0064 | 0.01 (3) |
| 40+ | 1774 | 0.3929 | 0.0472 | +0.3458 ± 0.0058 | 1.0245 | 0.1814 | 0.6395 | 0.1113 | 0.0598 | -0.089 ± 0.0049 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 842 | 0.1963 | 0.1964 | -0.0001 ± 0.0005 | 0.5732 | 0.5731 | 0.5074 | 0.4924 | 0.4941 | -0.057 ± 0.0154 | -0.0224 (49) |
| 3-5 | 593 | 0.1945 | 0.1938 | +0.0007 ± 0.0015 | 0.5674 | 0.5646 | 0.4811 | 0.4413 | 0.4503 | -0.052 ± 0.0182 | -0.0194 (34) |
| 5-10 | 1240 | 0.1992 | 0.1929 | +0.0063 ± 0.0019 | 0.5859 | 0.5679 | 0.4896 | 0.4162 | 0.4105 | -0.070 ± 0.0127 | -0.005 (78) |
| 10-15 | 792 | 0.2074 | 0.1966 | +0.0108 ± 0.0039 | 0.6029 | 0.575 | 0.5107 | 0.3875 | 0.404 | -0.059 ± 0.0159 | 0.0014 (64) |
| 15-25 | 1063 | 0.2333 | 0.2125 | +0.0208 ± 0.0056 | 0.6648 | 0.6112 | 0.5693 | 0.3743 | 0.4196 | -0.061 ± 0.0142 | -0.0214 (59) |
| 25-40 | 632 | 0.2445 | 0.2003 | +0.0442 ± 0.0109 | 0.6926 | 0.5795 | 0.6574 | 0.3448 | 0.4288 | -0.080 ± 0.0165 | -0.0219 (26) |
| 40+ | 219 | 0.3522 | 0.1941 | +0.1581 ± 0.0299 | 1.0177 | 0.5694 | 0.8035 | 0.3161 | 0.4201 | -0.079 ± 0.0262 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2617 | 0.1876 | 0.1877 | -0.0001 ± 0.0003 | 0.5503 | 0.5495 | 0.5049 | 0.4897 | 0.4975 | -0.039 ± 0.0085 | -0.0157 (88) |
| 3-5 | 1807 | 0.1909 | 0.1883 | +0.0026 ± 0.0008 | 0.5582 | 0.552 | 0.4881 | 0.4484 | 0.4361 | -0.059 ± 0.0103 | -0.0209 (69) |
| 5-10 | 3602 | 0.1955 | 0.1867 | +0.0087 ± 0.0011 | 0.5759 | 0.5517 | 0.4873 | 0.4138 | 0.3931 | -0.073 ± 0.0073 | -0.0082 (132) |
| 10-15 | 2458 | 0.2033 | 0.1888 | +0.0145 ± 0.0022 | 0.5937 | 0.5557 | 0.5178 | 0.3948 | 0.3967 | -0.059 ± 0.0088 | -0.0053 (105) |
| 15-25 | 3073 | 0.2293 | 0.1984 | +0.0309 ± 0.0032 | 0.6606 | 0.5767 | 0.5619 | 0.3664 | 0.3863 | -0.063 ± 0.0081 | -0.0253 (107) |
| 25-40 | 2097 | 0.25 | 0.1738 | +0.0762 ± 0.0057 | 0.7097 | 0.5115 | 0.6165 | 0.3028 | 0.3414 | -0.072 ± 0.0088 | -0.0229 (51) |
| 40+ | 984 | 0.3789 | 0.1335 | +0.2455 ± 0.0124 | 1.0741 | 0.4069 | 0.7178 | 0.2136 | 0.2368 | -0.073 ± 0.0108 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3371 | 1.058 ± 0.049 | 1.177 | 0.168 | 0.1658 | 0.2123 | 0.2037 |
| gen2 | 3371 | 0.842 ± 0.044 | 1.136 | 0.174 | 0.1658 | 0.2312 | 0.2037 |
| gen1_elo | 3371 | 1.039 ± 0.047 | 1.161 | 0.1737 | 0.1662 | 0.2113 | 0.2036 |
| gen1_sr | 3371 | 1.045 ± 0.057 | 1.207 | 0.134 | 0.1675 | 0.2274 | 0.2034 |
| gen1_ledger | 5381 | 0.884 ± 0.034 | 1.083 | 0.1784 | 0.1813 | 0.2177 | 0.1989 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 16,232)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,862 | 23.8% |
| STALE_QUOTE | market_freshness | 3,327 | 20.5% |
| BOOK_QUALITY | execution | 3,177 | 19.6% |
| POOR_DATA | data | 1,772 | 10.9% |
| LIMITED_DATA | data | 1,106 | 6.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 858 | 5.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 801 | 4.9% |
| IDENTITY_AMBIGUOUS | mapping | 657 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 456 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 216 | 1.3% |

Cause class: coverage 23.8%, market_freshness 20.5%, execution 19.6%, data 17.7%, market_freshness/coverage 8.1%, model_calibration_or_unknown 4.9%, mapping 4.0%, model_calibration 1.3%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.6%, START_UNVERIFIABLE 94.6%, LOW_DATA_QUALITY 69.8%, THIN_PLAYER_HISTORY 58.1%, STALE_PLAYER_DATA 51.6%, STALE_KALSHI_QUOTE 43.8%, MODEL_INTERNAL_DISAGREEMENT 40.3%, ASYMMETRIC_SAMPLE_SIZE 32.3%, WIDE_SPREAD 25.6%, MODEL_HIGH_UNCERTAINTY 17.8%, PLAYER_IDENTITY_RISK 15.0%, LEVEL_TRANSFER_RISK 8.9%, EVENT_MAPPING_RISK 8.6%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 2.3%, UNKNOWN 1.0%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 26.2%, POST_SETTLEMENT_OBSERVATION 23.8%, POSSIBLE_IN_PLAY_QUOTE 5.6%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 8,672)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,054 | 35.2% |
| BOOK_QUALITY | execution | 1,669 | 19.2% |
| STALE_QUOTE | market_freshness | 1,547 | 17.8% |
| POOR_DATA | data | 747 | 8.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 453 | 5.2% |
| IDENTITY_AMBIGUOUS | mapping | 374 | 4.3% |
| LIMITED_DATA | data | 327 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 281 | 3.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 173 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 47 | 0.5% |

Cause class: coverage 35.2%, execution 19.2%, market_freshness 17.8%, data 12.4%, market_freshness/coverage 8.5%, mapping 4.3%, model_calibration_or_unknown 2.0%, model_calibration 0.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.7%, START_UNVERIFIABLE 97.5%, LOW_DATA_QUALITY 73.8%, THIN_PLAYER_HISTORY 60.6%, STALE_KALSHI_QUOTE 52.0%, STALE_PLAYER_DATA 47.1%, MODEL_INTERNAL_DISAGREEMENT 41.1%, ASYMMETRIC_SAMPLE_SIZE 34.1%, WIDE_SPREAD 25.5%, PLAYER_IDENTITY_RISK 18.3%, MODEL_HIGH_UNCERTAINTY 18.1%, EVENT_MAPPING_RISK 10.4%, LEVEL_TRANSFER_RISK 7.9%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 5.2%, EXTERNAL_MARKET_REJECTION 1.3%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 38.0%, POST_SETTLEMENT_OBSERVATION 35.2%, POSSIBLE_IN_PLAY_QUOTE 5.6%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 6856, "IDENTITY_AMBIGUOUS": 1816}; ticker orientation: {"VERIFIED": 8672}.

Checks: discipline:AMBIGUOUS 646, discipline:PASS 8026, identity_confidence:AMBIGUOUS 1590, identity_confidence:PASS 7082, level_mapping:NA 658, level_mapping:PASS 8014, market_pair:AMBIGUOUS 314, market_pair:NA 213, market_pair:PASS 8145, model_complement:NA 180, model_complement:PASS 8492, namesake:PASS 8672, physical_match_id:NA 3293, physical_match_id:PASS 5379, player_ids:PASS 8672, same_pair_other_event:PASS 8672, ticker_orientation:PASS 8672

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,031 | 3.6% | 3.4% | 1.3% | {"market_freshness": 36, "data": 27, "model_calibration_or_unknown": 15, "execution": 14, "market_freshness/coverage": 8, "model_calibration": 7, "coverage": 2} | 5.67 | 0.2142 / 0.2101 (329) | 17.5% | 3.2% | 4.1% | 2.4% |
| CHALLENGER | 6,316 | 17.0% | 6.5% | 12.4% | {"coverage": 621, "market_freshness/coverage": 134, "market_freshness": 131, "data": 92, "model_calibration_or_unknown": 49, "execution": 25, "model_calibration": 10, "mapping": 10} | 7.26 | 0.2165 / 0.2063 (1580) | 35.8% | 14.8% | 3.2% | 22.2% |
| DOUBLES | 1,324 | 48.8% | 48.4% | 7.4% | {"execution": 319, "mapping": 171, "market_freshness": 106, "market_freshness/coverage": 43, "coverage": 7} | 24.07 | 0.324 / 0.2339 (337) | 17.7% | 0.0% | 100.0% | 7.0% |
| ITF_MEN | 10,954 | 24.6% | 16.8% | 31.1% | {"coverage": 1061, "execution": 547, "market_freshness": 414, "data": 359, "market_freshness/coverage": 214, "mapping": 96, "model_calibration_or_unknown": 2} | 11.18 | 0.214 / 0.1949 (2662) | 36.4% | 62.1% | 13.5% | 22.9% |
| ITF_WOMEN | 14,423 | 26.7% | 19.8% | 44.5% | {"coverage": 1346, "market_freshness": 784, "execution": 734, "data": 562, "market_freshness/coverage": 286, "mapping": 91, "model_calibration_or_unknown": 43, "model_calibration": 10} | 12.81 | 0.2019 / 0.1939 (2943) | 38.4% | 57.8% | 10.3% | 22.0% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,267 | 4.9% | 4.4% | 1.3% | {"market_freshness": 36, "model_calibration_or_unknown": 23, "execution": 16, "data": 11, "market_freshness/coverage": 10, "model_calibration": 9, "coverage": 4, "mapping": 1} | 7.67 | 0.2401 / 0.2332 (371) | 23.2% | 1.5% | 1.6% | 2.9% |
| WTA125 | 1,392 | 12.5% | 9.9% | 2.0% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

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
| 8 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 9 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 10 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 11 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 12 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 13 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 14 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 15 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 16 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 17 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 18 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 19 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 20 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 213 min (STALE); no external reference |
| 22 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 23 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 24 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 25 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 26 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 27 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 28 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 22.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1345 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 29 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 30 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 31 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 32 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 33 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 468 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 34 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 35 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 874 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 36 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 37 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 38 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.2h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 196 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |
| 39 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 33 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 40 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 41 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 42 | `KXITFWMATCH-26OCT16ESTLAB-LAB` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 68 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1475.0, ratio 2.28); no external reference |
| 43 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 44 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 45 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 46 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 47 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 48 | `KXATPDOUBLES-26OCT18COLGOFPOLZIE-COLGOF` | DOUBLES | gen1_ledger | 90% / 15% | +75 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 49 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 50 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9747, "by_level_share_of_ge_25pp": {"ATP": 0.0126, "CHALLENGER": 0.1236, "DOUBLES": 0.0745, "ITF_MEN": 0.3105, "ITF_WOMEN": 0.4446, "OTHER": 0.0014, "WTA": 0.0127, "WTA125": 0.0201}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5202, "share_primary_cause_market_settled_or_in_play": 0.4368, "share_primary_cause_stale_quote_only": 0.1784}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 8672, "identity_ambiguous_share": 0.2094, "ticker_orientation": {"VERIFIED": 8672}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 5379, "with_external": 222, "coverage": 0.0413, "external_status": {"EXTERNAL_STALE": 145, "AGREES_WITH_KALSHI": 74, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 145, "MODEL_LONE_OUTLIER": 74, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3333, "share_external_supports_model": 0.0135}, "pregame_clean_ge_25pp": {"n": 2590, "with_external": 210, "coverage": 0.0811, "external_status": {"EXTERNAL_STALE": 135, "AGREES_WITH_KALSHI": 72, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 135, "MODEL_LONE_OUTLIER": 72, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3429, "share_external_supports_model": 0.0143}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 533.0, "median_sample_ratio": 2.44, "median_min_matches": 21.0, "median_max_days_since_last": 216.0, "share_severe_asymmetry": 0.2066, "data_status": {"POOR": 4676, "LIMITED": 2468, "ADEQUATE": 1528}, "comparison_lt_10pp": {"median_thinner_serve_points": 1827.0, "median_sample_ratio": 1.67, "median_min_matches": 94.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 675, "model_minus_observed": 0.0516, "kalshi_minus_observed": -0.0828, "brier_diff_model_minus_kalshi": -0.0007}, "4-10x": {"n": 460, "model_minus_observed": 0.0756, "kalshi_minus_observed": -0.0662, "brier_diff_model_minus_kalshi": 0.0081}, "<2x": {"n": 1673, "model_minus_observed": 0.0862, "kalshi_minus_observed": -0.0349, "brier_diff_model_minus_kalshi": 0.0119}, ">=10x": {"n": 563, "model_minus_observed": 0.1143, "kalshi_minus_observed": -0.058, "brier_diff_model_minus_kalshi": 0.0105}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3371, "model": {"intercept": -0.525, "slope": 0.842, "slope_se": 0.044}, "kalshi_mid_same_rows": {"intercept": 0.241, "slope": 1.136, "slope_se": 0.051}, "mean_extremity_model": 0.174, "mean_extremity_kalshi": 0.1658, "model_brier": 0.2312, "kalshi_brier": 0.2037, "brier_diff_model_minus_kalshi": 0.0276, "brier_diff_se": 0.0033, "model_logloss": 0.659, "kalshi_logloss": 0.5898}, "fair_v1": {"n": 3371, "model": {"intercept": -0.399, "slope": 1.058, "slope_se": 0.049}, "kalshi_mid_same_rows": {"intercept": 0.319, "slope": 1.177, "slope_se": 0.052}, "mean_extremity_model": 0.168, "mean_extremity_kalshi": 0.1658, "model_brier": 0.2123, "kalshi_brier": 0.2037, "brier_diff_model_minus_kalshi": 0.0086, "brier_diff_se": 0.0026, "model_logloss": 0.6123, "kalshi_logloss": 0.5897}, "gen1_elo": {"n": 3371, "model": {"intercept": -0.39, "slope": 1.039, "slope_se": 0.047}, "kalshi_mid_same_rows": {"intercept": 0.312, "slope": 1.161, "slope_se": 0.051}, "mean_extremity_model": 0.1737, "mean_extremity_kalshi": 0.1662, "model_brier": 0.2113, "kalshi_brier": 0.2036, "brier_diff_model_minus_kalshi": 0.0077, "brier_diff_se": 0.0026, "model_logloss": 0.6109, "kalshi_logloss": 0.5895}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2416, "share_ge_15": 0.4351, "median_abs_gap": 12.95, "n": 22261}, "gen1_elo": {"share_ge_25": 0.2369, "share_ge_15": 0.4315, "median_abs_gap": 12.54, "n": 22261}, "gen1_sr": {"share_ge_25": 0.3037, "share_ge_15": 0.5175, "median_abs_gap": 15.62, "n": 22261}, "gen2": {"share_ge_25": 0.3073, "share_ge_15": 0.5062, "median_abs_gap": 15.33, "n": 22261}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1498, "share_ge_15": 0.349, "median_abs_gap": 10.7, "n": 17289}, "gen1_elo": {"share_ge_25": 0.1488, "share_ge_15": 0.3422, "median_abs_gap": 10.21, "n": 17288}, "gen1_sr": {"share_ge_25": 0.2113, "share_ge_15": 0.4399, "median_abs_gap": 13.03, "n": 17289}, "gen2": {"share_ge_25": 0.227, "share_ge_15": 0.4396, "median_abs_gap": 12.99, "n": 17290}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.67, "share_ge_25_all": 0.036, "share_ge_25_pregame_clean": 0.0335}, "WTA": {"median_abs_gap_pregame_clean": 7.67, "share_ge_25_all": 0.0485, "share_ge_25_pregame_clean": 0.0436}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2397, "share_within_10pp_all": 0.4386, "share_within_10pp_pregame_clean": 0.493, "corr_model_vs_mid_pregame_clean": 0.8418}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 517, "model_brier": 0.1965, "kalshi_brier": 0.1978, "brier_diff_model_minus_kalshi": -0.0013}, "10-15": {"n_settled": 596, "model_brier": 0.2152, "kalshi_brier": 0.2065, "brier_diff_model_minus_kalshi": 0.0087}, "15-25": {"n_settled": 732, "model_brier": 0.2269, "kalshi_brier": 0.2133, "brier_diff_model_minus_kalshi": 0.0137}, "25-40": {"n_settled": 415, "model_brier": 0.2202, "kalshi_brier": 0.2107, "brier_diff_model_minus_kalshi": 0.0095}, "3-5": {"n_settled": 323, "model_brier": 0.1973, "kalshi_brier": 0.1966, "brier_diff_model_minus_kalshi": 0.0007}, "40+": {"n_settled": 84, "model_brier": 0.2967, "kalshi_brier": 0.1739, "brier_diff_model_minus_kalshi": 0.1228}, "5-10": {"n_settled": 704, "model_brier": 0.1986, "kalshi_brier": 0.1984, "brier_diff_model_minus_kalshi": 0.0001}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.525, "slope": 0.842, "slope_se": 0.044}, "kalshi_slope": {"intercept": 0.241, "slope": 1.136, "slope_se": 0.051}, "n": 3371}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.514, "slope": 0.884, "slope_se": 0.034}, "kalshi_slope": {"intercept": 0.153, "slope": 1.083, "slope_se": 0.038}, "n": 5381}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 337, "model_brier": 0.324, "kalshi_brier": 0.2339, "brier_diff_model_minus_kalshi": 0.0902, "brier_diff_se": 0.0171, "corr_model_outcome": 0.0142, "corr_kalshi_outcome": 0.2577}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
