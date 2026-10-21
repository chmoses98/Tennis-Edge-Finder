# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-21T10:12Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 46,403): 0-3 14.1%, 3-5 9.5%, 5-10 19.8%, 10-15 15.4%, 15-25 19.4%, 25-40 14.0%, 40+ 7.9%; median gap 12.04 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 75.9%, Challenger 12.4%, doubles 6.9%). Main tour: ATP 5.0% and WTA 4.6% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 10,163): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.9%, BOOK_QUALITY 19.0%, STALE_QUOTE 18.1%, POOR_DATA 9.2%, POSSIBLY_IN_PLAY_QUOTE 5.3%, IDENTITY_AMBIGUOUS 4.5%, LIMITED_DATA 3.8%, IN_PLAY_QUOTE 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%. By class: coverage 33.9%, execution 19.0%, market_freshness 18.1%, data 13.0%, market_freshness/coverage 8.6%, mapping 4.5%, model_calibration_or_unknown 2.2%, model_calibration 0.7%.
* **Stale / settled / in-play**: 51.1% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 10,163 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.1%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.5% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 494.0 points vs 1716.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.045, Gen-2 0.845, Gen-1 ledger 0.873 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 485 model 0.2265 vs Kalshi 0.2097; n 97 model 0.2967 vs Kalshi 0.1848.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 198,564 model-market comparisons (322,702 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 67,920 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-21T09:59:09.967451+00:00'], shadow board 52,386 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-21T09:59:13.630431+00:00'], Model 4 24,900 rows, 17,979 settled tickers, 6,315 tickers with an external scan.
* By model: {"gen1_ledger": 45881, "gen1_elo": 26338, "fair_v1": 26338, "gen2": 26338, "gen1_sr": 26338, "model4_fundamental": 23679, "model4_conditioned": 23652}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 46,403 | 14.1 | 9.5 | 19.8 | 15.4 | 19.4 | 14.0 | 7.9 | 12.04 | 41.3% | 21.9% |
| MW fair_v1 | 26,338 | 13.1 | 8.6 | 18.3 | 15.7 | 20.0 | 14.9 | 9.4 | 13.1 | 44.3% | 24.3% |
| MW gen1_elo | 26,338 | 12.9 | 8.7 | 19.2 | 15.2 | 19.9 | 14.9 | 9.1 | 12.82 | 44.0% | 24.0% |
| MW gen1_ledger | 20,065 | 15.5 | 10.7 | 21.6 | 14.9 | 18.5 | 12.8 | 6.0 | 10.54 | 37.3% | 18.8% |
| MW gen1_sr | 26,338 | 9.9 | 7.2 | 16.6 | 14.0 | 21.4 | 18.7 | 12.1 | 15.91 | 52.3% | 30.9% |
| MW gen2 | 26,338 | 11.1 | 7.3 | 16.3 | 14.2 | 20.0 | 17.8 | 13.3 | 15.51 | 51.1% | 31.1% |
| all families model4_conditioned | 23,652 | 21.7 | 19.2 | 34.4 | 17.7 | 4.5 | 1.4 | 1.0 | 5.94 | 6.9% | 2.4% |
| all families model4_fundamental | 23,679 | 16.4 | 13.1 | 34.0 | 20.4 | 11.3 | 3.5 | 1.3 | 7.9 | 16.1% | 4.9% |

Configurable thresholds (primary): >=5pp 76.4%, >=10pp 56.6%, >=15pp 41.3%, >=20pp 30.6%, >=25pp 21.9%, >=30pp 15.7%, >=40pp 7.9%, >=50pp 3.6%
Executable gap (model outside the book, before fees): median 8.41pp; >=10pp 45.1%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,302 | 28.6 | 13.9 | 24.3 | 14.9 | 12.6 | 5.2 | 0.6 | 6.21 | 18.3% | 5.8% |
| CHALLENGER | 4,316 | 15.6 | 10.1 | 20.2 | 15.8 | 14.9 | 12.5 | 10.9 | 11.23 | 38.3% | 23.4% |
| ITF_MEN | 7,050 | 10.7 | 7.7 | 17.1 | 14.5 | 21.1 | 17.1 | 11.7 | 15.0 | 50.0% | 28.8% |
| ITF_WOMEN | 10,418 | 9.6 | 6.9 | 15.7 | 15.7 | 23.0 | 18.1 | 11.0 | 15.69 | 52.1% | 29.1% |
| WTA | 1,592 | 17.1 | 12.5 | 24.9 | 20.2 | 20.2 | 4.3 | 0.7 | 8.65 | 25.2% | 5.0% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,302 | 23.4 | 14.9 | 24.4 | 17.2 | 14.0 | 5.2 | 0.8 | 6.85 | 20.1% | 6.0% |
| CHALLENGER | 4,316 | 14.6 | 8.5 | 18.7 | 14.6 | 17.7 | 14.0 | 11.9 | 12.68 | 43.6% | 25.9% |
| ITF_MEN | 7,050 | 8.8 | 6.3 | 14.8 | 13.2 | 19.9 | 20.4 | 16.6 | 17.99 | 56.9% | 37.0% |
| ITF_WOMEN | 10,418 | 8.3 | 5.6 | 13.8 | 13.4 | 21.4 | 20.8 | 16.7 | 18.71 | 58.9% | 37.5% |
| WTA | 1,592 | 14.5 | 9.6 | 20.5 | 16.6 | 24.2 | 13.9 | 0.8 | 11.46 | 38.8% | 14.6% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,302 | 24.2 | 12.8 | 24.2 | 15.9 | 15.0 | 6.8 | 1.0 | 7.29 | 22.9% | 7.8% |
| CHALLENGER | 4,316 | 14.1 | 9.6 | 20.8 | 15.2 | 16.3 | 12.8 | 11.1 | 11.41 | 40.3% | 23.9% |
| ITF_MEN | 7,050 | 10.1 | 7.7 | 17.4 | 13.9 | 21.8 | 17.4 | 11.8 | 15.44 | 51.0% | 29.2% |
| ITF_WOMEN | 10,418 | 9.5 | 6.7 | 16.4 | 15.7 | 23.1 | 18.4 | 10.2 | 15.57 | 51.7% | 28.6% |
| WTA | 1,592 | 24.4 | 16.6 | 30.0 | 16.1 | 10.2 | 2.1 | 0.4 | 6.02 | 12.8% | 2.6% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,319 | 26.4 | 19.6 | 29.7 | 11.9 | 8.8 | 3.2 | 0.4 | 5.4 | 12.4% | 3.6% |
| CHALLENGER | 3,004 | 21.3 | 14.8 | 26.7 | 14.2 | 14.8 | 6.4 | 1.9 | 7.29 | 23.1% | 8.3% |
| DOUBLES | 1,449 | 5.0 | 4.2 | 11.7 | 10.3 | 20.4 | 26.1 | 22.2 | 24.1 | 68.7% | 48.3% |
| ITF_MEN | 5,596 | 14.0 | 8.8 | 20.4 | 15.9 | 20.8 | 13.4 | 6.7 | 12.05 | 40.9% | 20.1% |
| ITF_WOMEN | 6,790 | 12.5 | 8.9 | 19.4 | 15.2 | 21.6 | 16.4 | 6.0 | 12.91 | 44.1% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,026 | 22.3 | 15.9 | 29.6 | 18.1 | 10.1 | 3.6 | 0.3 | 6.97 | 14.0% | 3.9% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,245 | 28.9 | 14.1 | 24.6 | 14.7 | 12.3 | 4.8 | 0.5 | 6.13 | 17.6% | 5.3% |
| CHALLENGER | 3,047 | 20.4 | 12.4 | 24.8 | 18.4 | 15.3 | 6.7 | 2.0 | 8.43 | 24.1% | 8.8% |
| ITF_MEN | 5,239 | 13.0 | 9.1 | 20.2 | 16.4 | 21.9 | 14.1 | 5.2 | 12.23 | 41.3% | 19.3% |
| ITF_WOMEN | 7,873 | 11.3 | 8.2 | 17.9 | 17.8 | 24.6 | 15.3 | 4.9 | 13.47 | 44.8% | 20.2% |
| WTA | 1,551 | 17.3 | 12.2 | 24.9 | 20.4 | 20.1 | 4.3 | 0.7 | 8.73 | 25.1% | 5.0% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,245 | 23.7 | 15.2 | 24.5 | 17.1 | 14.0 | 4.9 | 0.7 | 6.63 | 19.6% | 5.6% |
| CHALLENGER | 3,047 | 18.4 | 10.8 | 23.4 | 17.4 | 17.9 | 9.8 | 2.3 | 9.42 | 30.1% | 12.1% |
| ITF_MEN | 5,240 | 10.3 | 7.5 | 16.9 | 14.8 | 21.9 | 18.5 | 9.9 | 15.25 | 50.4% | 28.4% |
| ITF_WOMEN | 7,873 | 9.3 | 6.5 | 15.2 | 14.9 | 23.3 | 20.2 | 10.7 | 16.51 | 54.2% | 30.9% |
| WTA | 1,551 | 14.5 | 9.5 | 20.4 | 16.5 | 24.2 | 14.1 | 0.8 | 11.5 | 39.0% | 14.8% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,279 | 26.6 | 19.9 | 29.8 | 12.1 | 8.4 | 3.0 | 0.2 | 5.37 | 11.7% | 3.3% |
| CHALLENGER | 2,617 | 22.7 | 15.8 | 28.4 | 14.1 | 14.2 | 4.3 | 0.6 | 6.72 | 19.0% | 4.9% |
| DOUBLES | 1,348 | 4.9 | 4.4 | 11.9 | 10.5 | 20.4 | 26.2 | 21.7 | 23.99 | 68.2% | 47.9% |
| ITF_MEN | 4,680 | 15.3 | 9.5 | 22.1 | 16.6 | 20.6 | 11.7 | 4.1 | 10.89 | 36.5% | 15.8% |
| ITF_WOMEN | 5,679 | 13.4 | 9.5 | 20.7 | 15.9 | 21.8 | 15.2 | 3.5 | 11.81 | 40.5% | 18.7% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 977 | 22.8 | 16.4 | 29.6 | 18.2 | 10.1 | 2.9 | 0.0 | 6.82 | 13.0% | 2.9% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,449 | 5.0 | 4.2 | 11.7 | 10.3 | 20.4 | 26.1 | 22.2 | 24.1 | 68.7% | 48.3% |
| singles | 18,616 | 16.3 | 11.2 | 22.4 | 15.3 | 18.4 | 11.8 | 4.7 | 10.02 | 34.9% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 5,947 | 13.2 | 8.9 | 19.1 | 15.7 | 18.9 | 14.8 | 9.4 | 12.8 | 43.1% | 24.2% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 16,551 | 13.5 | 8.6 | 18.4 | 15.4 | 20.1 | 14.7 | 9.3 | 13.09 | 44.2% | 24.0% |
| UNKNOWN | 3,603 | 11.3 | 7.9 | 17.0 | 17.2 | 20.9 | 15.7 | 9.9 | 13.69 | 46.5% | 25.7% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,499 | 19.7 | 11.6 | 21.1 | 16.8 | 16.0 | 8.9 | 5.9 | 9.3 | 30.9% | 14.9% |
| B | 3,335 | 12.5 | 9.1 | 20.0 | 17.2 | 18.9 | 12.1 | 10.3 | 12.17 | 41.3% | 22.4% |
| C | 3,690 | 11.9 | 9.1 | 19.1 | 15.0 | 19.6 | 15.2 | 10.1 | 13.18 | 44.9% | 25.3% |
| D | 4,308 | 12.2 | 7.8 | 17.0 | 15.5 | 22.2 | 15.8 | 9.4 | 14.03 | 47.4% | 25.2% |
| F | 7,506 | 7.9 | 5.6 | 15.2 | 14.5 | 23.4 | 21.3 | 12.2 | 17.64 | 56.9% | 33.5% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,696 | 23.2 | 15.8 | 28.6 | 15.1 | 11.8 | 4.1 | 1.5 | 6.68 | 17.3% | 5.5% |
| B | 2,782 | 16.0 | 10.5 | 23.8 | 16.2 | 19.0 | 10.7 | 3.9 | 9.92 | 33.5% | 14.5% |
| C | 3,961 | 11.2 | 7.4 | 18.5 | 14.3 | 21.4 | 16.4 | 10.8 | 14.28 | 48.6% | 27.2% |
| D | 2,877 | 14.2 | 9.7 | 19.8 | 14.6 | 21.0 | 14.5 | 6.2 | 12.08 | 41.7% | 20.7% |
| F | 4,749 | 10.3 | 8.0 | 15.7 | 14.6 | 22.5 | 20.6 | 8.4 | 15.81 | 51.4% | 28.9% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 8,526 | 17.9 | 10.3 | 20.5 | 16.8 | 16.5 | 9.8 | 8.3 | 10.39 | 34.5% | 18.1% |
| LIMITED | 5,753 | 13.7 | 10.3 | 20.2 | 15.7 | 19.1 | 13.4 | 7.4 | 11.73 | 40.0% | 20.9% |
| POOR | 12,059 | 9.5 | 6.5 | 15.9 | 14.9 | 22.9 | 19.1 | 11.2 | 16.08 | 53.2% | 30.3% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,058 | 26.7 | 20.8 | 34.2 | 12.0 | 4.5 | 1.5 | 0.2 | 5.21 | 6.2% | 1.7% |
| GAME_SPREAD | 4,377 | 22.8 | 15.4 | 33.3 | 17.0 | 8.8 | 2.4 | 0.3 | 6.56 | 11.5% | 2.7% |
| MATCH_WINNER | 20,065 | 15.5 | 10.7 | 21.6 | 14.9 | 18.5 | 12.8 | 6.0 | 10.54 | 37.3% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 9,267 | 29.9 | 16.8 | 30.4 | 12.6 | 8.1 | 1.7 | 0.4 | 5.43 | 10.2% | 2.1% |
| TOTAL_GAMES | 7,090 | 8.2 | 9.3 | 36.4 | 29.1 | 10.8 | 3.3 | 2.8 | 9.56 | 16.9% | 6.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,262 | 25.3 | 34.6 | 32.3 | 4.0 | 3.1 | 0.6 | 0.1 | 4.45 | 3.8% | 0.7% |
| GAME_SPREAD | 5,658 | 45.7 | 17.0 | 27.0 | 7.6 | 1.8 | 0.7 | 0.2 | 3.44 | 2.7% | 0.9% |
| TOTAL_GAMES | 9,732 | 4.8 | 7.4 | 40.5 | 35.2 | 7.3 | 2.5 | 2.3 | 9.73 | 12.1% | 4.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,265 | 24.2 | 18.0 | 35.3 | 12.3 | 7.3 | 2.6 | 0.3 | 5.8 | 10.2% | 2.9% |
| GAME_SPREAD | 5,661 | 19.2 | 13.1 | 28.1 | 19.9 | 14.3 | 4.4 | 0.9 | 8.0 | 19.6% | 5.3% |
| TOTAL_GAMES | 9,753 | 8.0 | 8.9 | 36.4 | 27.5 | 12.9 | 3.8 | 2.5 | 9.63 | 19.2% | 6.2% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 26,338 | 44.3% | 24.3% | 13.1 | 36.1% | 15.3% | 10.96 |
| gen1_elo | 26,338 | 44.0% | 24.0% | 12.82 | 35.5% | 15.5% | 10.55 |
| gen1_sr | 26,338 | 52.3% | 30.9% | 15.91 | 44.8% | 21.9% | 13.25 |
| gen2 | 26,338 | 51.1% | 31.1% | 15.51 | 44.7% | 23.4% | 13.16 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 13,771 | 15.8 | 10.3 | 21.1 | 17.3 | 20.4 | 11.8 | 3.3 | 10.8 | 35.5% | 15.1% |
| STALE | 12,567 | 10.1 | 6.7 | 15.3 | 14.0 | 19.5 | 18.2 | 16.1 | 16.9 | 53.9% | 34.4% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 13,533 | 16.6 | 11.2 | 22.5 | 15.0 | 17.6 | 12.2 | 4.8 | 9.9 | 34.6% | 17.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 46,403 | 13533 | 17243 | 15627 | 23.9 | 124.9 | 1400.4 |
| ge_15pp | 19,151 | 4688 | 6178 | 8285 | 25.7 | 418.1 | 1380.4 |
| ge_25pp | 10,163 | 2306 | 2667 | 5190 | 31.1 | 563.9 | 1380.4 |
| lt_10pp | 20,126 | 6819 | 8135 | 5172 | 21.7 | 47.3 | 1341.5 |

Current slate `SL-20261021T101215Z-904e78bb`: 718 priced rows, quote age at build {'median': 13.6, 'max': 13.7}, freshness {'AGING': 718}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 20 | 0.0 | 0.0 | 25.0 | 0.0 | 40.0 | 35.0 | 0.0 | 20.49 | 75.0% | 35.0% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,467 | 19.5 | 10.9 | 23.6 | 18.6 | 19.3 | 7.3 | 0.7 | 9.16 | 27.4% | 8.1% |
| KALSHI_LONE_OUTLIER | 17 | 5.9 | 5.9 | 76.5 | 0.0 | 5.9 | 5.9 | 0.0 | 6.11 | 11.8% | 5.9% |
| MARKETS_AGREE | 453 | 67.1 | 32.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.2 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,014 | 0.0 | 2.4 | 33.3 | 26.4 | 26.3 | 10.8 | 0.8 | 12.8 | 37.9% | 11.5% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 26,338 | 3983 (15.1%) | 25.5% | 0.9% | {"EXTERNAL_STALE": 2467, "AGREES_WITH_KALSHI": 1014, "ALL_AGREE": 453, "SUPPORTS_MODEL_DIRECTION": 19, "AGREES_WITH_MODEL": 17, "EXTERNAL_OUTLIER": 12, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 11,664 | 1076 (9.2%) | 35.7% | 1.6% | {"EXTERNAL_STALE": 675, "AGREES_WITH_KALSHI": 384, "SUPPORTS_MODEL_DIRECTION": 15, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 6,395 | 324 (5.1%) | 36.1% | 2.5% | {"EXTERNAL_STALE": 199, "AGREES_WITH_KALSHI": 117, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,160 | 306 (9.7%) | 36.9% | 2.6% | {"EXTERNAL_STALE": 185, "AGREES_WITH_KALSHI": 113, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 10,538 | 2179 (20.7%) | 16.6% | 0.9% | {"EXTERNAL_STALE": 1332, "ALL_AGREE": 453, "AGREES_WITH_KALSHI": 362, "AGREES_WITH_MODEL": 15, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 4, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,053 | 10.6 | 7.7 | 19.3 | 14.6 | 22.3 | 15.7 | 9.8 | 13.98 | 47.8% | 25.5% |
| 4-10x | 3,433 | 11.3 | 8.5 | 19.0 | 15.5 | 21.1 | 14.8 | 9.8 | 13.57 | 45.8% | 24.6% |
| <2x | 13,491 | 15.1 | 9.6 | 18.8 | 16.7 | 18.2 | 13.1 | 8.4 | 11.91 | 39.8% | 21.5% |
| >=10x | 4,361 | 11.2 | 6.5 | 15.3 | 13.9 | 22.0 | 19.4 | 11.8 | 16.18 | 53.1% | 31.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 6,664 | 12.4 | 8.5 | 19.5 | 16.4 | 19.7 | 13.5 | 9.9 | 12.85 | 43.2% | 23.5% |
| 300-1000 | 5,726 | 11.8 | 8.7 | 17.0 | 15.5 | 21.0 | 16.2 | 9.8 | 13.92 | 47.0% | 26.0% |
| <300 | 8,424 | 9.0 | 5.8 | 15.5 | 14.6 | 23.1 | 20.2 | 11.8 | 16.81 | 55.1% | 32.0% |
| >=3000 | 5,524 | 21.5 | 12.7 | 22.7 | 16.8 | 14.7 | 6.9 | 4.8 | 8.08 | 26.4% | 11.7% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 769 | 0.5457 | 0.4093 | 0.498 | +0.048 | -0.089 | -0.0023 ± 0.0056 |
| ratio 4-10x | 522 | 0.588 | 0.4434 | 0.5 | +0.088 | -0.057 | 0.0124 ± 0.0071 |
| ratio <2x | 1882 | 0.5368 | 0.414 | 0.4506 | +0.086 | -0.037 | 0.0128 ± 0.0033 |
| ratio >=10x | 655 | 0.5657 | 0.3912 | 0.4626 | +0.103 | -0.071 | 0.0062 ± 0.0072 |
| thinner_sample 1000-3000 | 1046 | 0.5427 | 0.4156 | 0.4522 | +0.090 | -0.037 | 0.0106 ± 0.0044 |
| thinner_sample 300-1000 | 894 | 0.5651 | 0.4234 | 0.4989 | +0.066 | -0.075 | -0.0001 ± 0.0054 |
| thinner_sample <300 | 1247 | 0.5549 | 0.3902 | 0.4587 | +0.096 | -0.069 | 0.0111 ± 0.005 |
| thinner_sample >=3000 | 641 | 0.5344 | 0.4395 | 0.4743 | +0.060 | -0.035 | 0.0125 ± 0.0046 |
| data_status ADEQUATE | 1098 | 0.5377 | 0.4321 | 0.4608 | +0.077 | -0.029 | 0.0117 ± 0.0038 |
| data_status LIMITED | 924 | 0.5506 | 0.4184 | 0.4794 | +0.071 | -0.061 | 0.005 ± 0.0049 |
| data_status POOR | 1806 | 0.5582 | 0.399 | 0.4684 | +0.090 | -0.070 | 0.0086 ± 0.0041 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 570 | 0.1969 | 0.1983 | -0.0014 ± 0.0006 | 0.5724 | 0.5753 | 0.4981 | 0.4833 | 0.5368 | -0.050 ± 0.0194 | -0.01 (5) |
| 3-5 | 360 | 0.1998 | 0.1997 | +0.0001 ± 0.0019 | 0.5824 | 0.5808 | 0.5034 | 0.4632 | 0.4806 | -0.088 ± 0.0242 | 0.02 (1) |
| 5-10 | 790 | 0.2018 | 0.2024 | -0.0006 ± 0.0024 | 0.5896 | 0.589 | 0.5134 | 0.4389 | 0.4759 | -0.082 ± 0.0166 | -0.0167 (6) |
| 10-15 | 666 | 0.2129 | 0.2034 | +0.0095 ± 0.0044 | 0.6153 | 0.588 | 0.5243 | 0.4002 | 0.4234 | -0.100 ± 0.0174 | -0.048 (5) |
| 15-25 | 860 | 0.2249 | 0.2148 | +0.0101 ± 0.0062 | 0.6449 | 0.6144 | 0.5781 | 0.3824 | 0.4547 | -0.085 ± 0.0156 | -0.0033 (9) |
| 25-40 | 485 | 0.2265 | 0.2097 | +0.0168 ± 0.0124 | 0.6417 | 0.6029 | 0.6548 | 0.3463 | 0.4701 | -0.075 ± 0.019 | -0.01 (1) |
| 40+ | 97 | 0.2967 | 0.1848 | +0.1119 ± 0.0387 | 0.8097 | 0.5528 | 0.7487 | 0.3013 | 0.4021 | -0.107 ± 0.0381 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2835 | 0.1829 | 0.184 | -0.0011 ± 0.0003 | 0.5407 | 0.542 | 0.48 | 0.465 | 0.5041 | -0.018 ± 0.0081 | -0.0129 (17) |
| 3-5 | 1854 | 0.196 | 0.1951 | +0.0009 ± 0.0008 | 0.5727 | 0.5672 | 0.4834 | 0.4434 | 0.452 | -0.049 ± 0.0105 | 0.0 (2) |
| 5-10 | 3930 | 0.1967 | 0.1939 | +0.0028 ± 0.0011 | 0.576 | 0.5668 | 0.4854 | 0.4114 | 0.4282 | -0.046 ± 0.0071 | -0.0119 (21) |
| 10-15 | 3437 | 0.2027 | 0.1844 | +0.0183 ± 0.0018 | 0.5931 | 0.5421 | 0.4866 | 0.3621 | 0.3506 | -0.075 ± 0.0073 | -0.0281 (16) |
| 15-25 | 4306 | 0.2088 | 0.1717 | +0.0371 ± 0.0025 | 0.6111 | 0.5074 | 0.5017 | 0.3054 | 0.3096 | -0.069 ± 0.0063 | -0.0025 (44) |
| 25-40 | 3320 | 0.2248 | 0.131 | +0.0938 ± 0.0039 | 0.644 | 0.4004 | 0.5324 | 0.2198 | 0.2295 | -0.062 ± 0.0061 | -0.01 (1) |
| 40+ | 2136 | 0.3791 | 0.0451 | +0.3340 ± 0.0052 | 0.9875 | 0.175 | 0.6312 | 0.1068 | 0.0627 | -0.081 ± 0.0043 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 427 | 0.2024 | 0.203 | -0.0006 ± 0.0008 | 0.5871 | 0.5884 | 0.502 | 0.487 | 0.5105 | -0.094 ± 0.0234 | -0.01 (3) |
| 3-5 | 318 | 0.2214 | 0.2203 | +0.0012 ± 0.0021 | 0.6286 | 0.6264 | 0.5129 | 0.4728 | 0.4717 | -0.107 ± 0.0284 | 0.02 (1) |
| 5-10 | 673 | 0.1995 | 0.2003 | -0.0008 ± 0.0026 | 0.5823 | 0.5839 | 0.5471 | 0.4722 | 0.5156 | -0.073 ± 0.0178 | -0.01 (4) |
| 10-15 | 633 | 0.2177 | 0.2116 | +0.0061 ± 0.0046 | 0.6255 | 0.6097 | 0.5643 | 0.4399 | 0.4803 | -0.096 ± 0.0189 | -0.04 (5) |
| 15-25 | 916 | 0.2308 | 0.2106 | +0.0203 ± 0.006 | 0.6552 | 0.6038 | 0.5914 | 0.3953 | 0.4454 | -0.099 ± 0.0154 | -0.0133 (9) |
| 25-40 | 634 | 0.2628 | 0.2 | +0.0627 ± 0.0112 | 0.7333 | 0.5815 | 0.6572 | 0.3414 | 0.4022 | -0.109 ± 0.0174 | -0.0075 (4) |
| 40+ | 227 | 0.3637 | 0.1693 | +0.1945 ± 0.0271 | 1.0044 | 0.5087 | 0.7377 | 0.2541 | 0.3084 | -0.083 ± 0.0261 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2368 | 0.1912 | 0.1916 | -0.0004 ± 0.0003 | 0.5604 | 0.561 | 0.5028 | 0.4879 | 0.5076 | -0.038 ± 0.0093 | -0.0133 (15) |
| 3-5 | 1608 | 0.1989 | 0.1992 | -0.0004 ± 0.0009 | 0.576 | 0.5765 | 0.5111 | 0.4711 | 0.4944 | -0.030 ± 0.0114 | 0.02 (1) |
| 5-10 | 3473 | 0.1928 | 0.1919 | +0.0008 ± 0.0011 | 0.5684 | 0.5626 | 0.5053 | 0.4313 | 0.4642 | -0.029 ± 0.0075 | -0.0117 (6) |
| 10-15 | 3120 | 0.1992 | 0.189 | +0.0102 ± 0.002 | 0.5855 | 0.5507 | 0.5144 | 0.3902 | 0.4128 | -0.047 ± 0.0079 | -0.0189 (18) |
| 15-25 | 4389 | 0.2173 | 0.1797 | +0.0376 ± 0.0025 | 0.6316 | 0.5273 | 0.5294 | 0.3332 | 0.3383 | -0.069 ± 0.0064 | -0.0086 (42) |
| 25-40 | 3892 | 0.2512 | 0.1396 | +0.1116 ± 0.0038 | 0.7074 | 0.4271 | 0.5624 | 0.246 | 0.231 | -0.083 ± 0.0059 | -0.0044 (18) |
| 40+ | 2968 | 0.3985 | 0.063 | +0.3354 ± 0.0053 | 1.0494 | 0.2237 | 0.6579 | 0.1221 | 0.0896 | -0.071 ± 0.0045 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 541 | 0.1975 | 0.2 | -0.0025 ± 0.0007 | 0.5751 | 0.5809 | 0.4945 | 0.4792 | 0.5545 | -0.013 ± 0.0196 | -0.0137 (8) |
| 3-5 | 394 | 0.195 | 0.1928 | +0.0022 ± 0.0018 | 0.5676 | 0.5625 | 0.5045 | 0.4649 | 0.4594 | -0.119 ± 0.023 | 0.0067 (3) |
| 5-10 | 819 | 0.2015 | 0.1989 | +0.0026 ± 0.0024 | 0.5901 | 0.5804 | 0.5104 | 0.4365 | 0.453 | -0.094 ± 0.016 | -0.0071 (7) |
| 10-15 | 669 | 0.2099 | 0.2061 | +0.0038 ± 0.0044 | 0.6075 | 0.5951 | 0.5392 | 0.416 | 0.4649 | -0.085 ± 0.0175 | -0.0317 (6) |
| 15-25 | 805 | 0.2327 | 0.2123 | +0.0205 ± 0.0063 | 0.6646 | 0.6079 | 0.5857 | 0.3919 | 0.436 | -0.113 ± 0.0161 | -0.03 (1) |
| 25-40 | 501 | 0.2141 | 0.2176 | -0.0035 ± 0.0122 | 0.615 | 0.6216 | 0.6653 | 0.354 | 0.513 | -0.049 ± 0.0187 | 0.015 (2) |
| 40+ | 99 | 0.3091 | 0.2028 | +0.1063 ± 0.0402 | 0.8452 | 0.5933 | 0.7593 | 0.308 | 0.4242 | -0.088 ± 0.042 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2729 | 0.1854 | 0.1862 | -0.0008 ± 0.0003 | 0.5461 | 0.5476 | 0.4863 | 0.471 | 0.4903 | -0.034 ± 0.0083 | -0.0163 (35) |
| 3-5 | 1895 | 0.1872 | 0.1848 | +0.0024 ± 0.0008 | 0.552 | 0.5461 | 0.4843 | 0.4448 | 0.4359 | -0.069 ± 0.0101 | -0.0094 (18) |
| 5-10 | 4131 | 0.1968 | 0.1914 | +0.0054 ± 0.001 | 0.5779 | 0.5596 | 0.487 | 0.4131 | 0.4122 | -0.060 ± 0.0069 | -0.01 (31) |
| 10-15 | 3278 | 0.1971 | 0.1806 | +0.0166 ± 0.0018 | 0.579 | 0.5318 | 0.5023 | 0.3787 | 0.3737 | -0.071 ± 0.0074 | -0.015 (12) |
| 15-25 | 4414 | 0.2133 | 0.174 | +0.0393 ± 0.0024 | 0.6215 | 0.5129 | 0.5094 | 0.3149 | 0.3108 | -0.076 ± 0.0063 | -0.03 (2) |
| 25-40 | 3303 | 0.2202 | 0.1322 | +0.0880 ± 0.004 | 0.6341 | 0.4027 | 0.5346 | 0.2185 | 0.2395 | -0.054 ± 0.0061 | 0.01 (3) |
| 40+ | 2068 | 0.3946 | 0.05 | +0.3446 ± 0.0056 | 1.0312 | 0.1879 | 0.644 | 0.1136 | 0.0672 | -0.084 ± 0.0047 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 902 | 0.1956 | 0.1958 | -0.0002 ± 0.0005 | 0.571 | 0.5713 | 0.5062 | 0.491 | 0.4945 | -0.059 ± 0.0149 | -0.0224 (49) |
| 3-5 | 628 | 0.1923 | 0.1919 | +0.0004 ± 0.0014 | 0.562 | 0.56 | 0.4843 | 0.4444 | 0.457 | -0.051 ± 0.0176 | -0.0194 (34) |
| 5-10 | 1334 | 0.1999 | 0.1935 | +0.0063 ± 0.0018 | 0.5874 | 0.5686 | 0.492 | 0.4187 | 0.4138 | -0.072 ± 0.0123 | -0.005 (78) |
| 10-15 | 872 | 0.2098 | 0.1996 | +0.0102 ± 0.0038 | 0.6081 | 0.582 | 0.516 | 0.3929 | 0.4117 | -0.062 ± 0.0154 | 0.0014 (64) |
| 15-25 | 1166 | 0.2306 | 0.2111 | +0.0195 ± 0.0053 | 0.6585 | 0.6081 | 0.5729 | 0.3781 | 0.4271 | -0.064 ± 0.0135 | -0.0214 (59) |
| 25-40 | 710 | 0.2506 | 0.2047 | +0.0460 ± 0.0105 | 0.7102 | 0.5894 | 0.6647 | 0.3521 | 0.4338 | -0.087 ± 0.0159 | -0.0219 (26) |
| 40+ | 242 | 0.3503 | 0.197 | +0.1533 ± 0.0284 | 1.0119 | 0.576 | 0.8058 | 0.3211 | 0.4256 | -0.084 ± 0.0254 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2953 | 0.1833 | 0.1834 | -0.0002 ± 0.0003 | 0.5397 | 0.5393 | 0.5066 | 0.4912 | 0.4998 | -0.038 ± 0.0079 | -0.0157 (88) |
| 3-5 | 2035 | 0.1911 | 0.1891 | +0.0020 ± 0.0008 | 0.5586 | 0.5546 | 0.49 | 0.4503 | 0.4452 | -0.054 ± 0.0097 | -0.0209 (69) |
| 5-10 | 4103 | 0.197 | 0.1884 | +0.0086 ± 0.001 | 0.5791 | 0.5544 | 0.4874 | 0.4139 | 0.3948 | -0.072 ± 0.0069 | -0.0082 (132) |
| 10-15 | 2846 | 0.2055 | 0.1911 | +0.0143 ± 0.002 | 0.5991 | 0.5612 | 0.5231 | 0.4001 | 0.4027 | -0.059 ± 0.0082 | -0.0053 (105) |
| 15-25 | 3518 | 0.229 | 0.1986 | +0.0304 ± 0.003 | 0.6606 | 0.5768 | 0.5654 | 0.3701 | 0.3914 | -0.064 ± 0.0075 | -0.0253 (107) |
| 25-40 | 2449 | 0.2611 | 0.1826 | +0.0785 ± 0.0055 | 0.7393 | 0.5336 | 0.6257 | 0.3112 | 0.3467 | -0.077 ± 0.0084 | -0.0229 (51) |
| 40+ | 1105 | 0.3758 | 0.14 | +0.2358 ± 0.0119 | 1.0641 | 0.4242 | 0.7252 | 0.2221 | 0.2525 | -0.073 ± 0.0105 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3828 | 1.045 ± 0.046 | 1.164 | 0.1668 | 0.1645 | 0.2136 | 0.205 |
| gen2 | 3828 | 0.845 ± 0.042 | 1.121 | 0.1702 | 0.1649 | 0.2324 | 0.2047 |
| gen1_elo | 3828 | 1.024 ± 0.044 | 1.146 | 0.1734 | 0.1647 | 0.2127 | 0.205 |
| gen1_sr | 3828 | 1.044 ± 0.055 | 1.196 | 0.1309 | 0.1668 | 0.2286 | 0.2043 |
| gen1_ledger | 5854 | 0.873 ± 0.032 | 1.085 | 0.1803 | 0.1794 | 0.2184 | 0.1996 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 19,151)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,322 | 22.6% |
| STALE_QUOTE | market_freshness | 4,034 | 21.1% |
| BOOK_QUALITY | execution | 3,684 | 19.2% |
| POOR_DATA | data | 2,228 | 11.6% |
| LIMITED_DATA | data | 1,262 | 6.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,015 | 5.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 950 | 5.0% |
| IDENTITY_AMBIGUOUS | mapping | 795 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 543 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 318 | 1.7% |

Cause class: coverage 22.6%, market_freshness 21.1%, execution 19.2%, data 18.2%, market_freshness/coverage 8.1%, model_calibration_or_unknown 5.0%, mapping 4.2%, model_calibration 1.7%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.8%, START_UNVERIFIABLE 94.1%, LOW_DATA_QUALITY 70.7%, THIN_PLAYER_HISTORY 59.5%, STALE_PLAYER_DATA 51.8%, STALE_KALSHI_QUOTE 43.3%, MODEL_INTERNAL_DISAGREEMENT 41.9%, ASYMMETRIC_SAMPLE_SIZE 32.9%, WIDE_SPREAD 25.3%, MODEL_HIGH_UNCERTAINTY 17.9%, PLAYER_IDENTITY_RISK 15.6%, LEVEL_TRANSFER_RISK 10.6%, EVENT_MAPPING_RISK 8.2%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 3.1%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.0%, POST_SETTLEMENT_OBSERVATION 22.6%, POSSIBLE_IN_PLAY_QUOTE 5.6%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 10,163)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,443 | 33.9% |
| BOOK_QUALITY | execution | 1,932 | 19.0% |
| STALE_QUOTE | market_freshness | 1,839 | 18.1% |
| POOR_DATA | data | 938 | 9.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 535 | 5.3% |
| IDENTITY_AMBIGUOUS | mapping | 452 | 4.5% |
| LIMITED_DATA | data | 386 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 340 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 223 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 75 | 0.7% |

Cause class: coverage 33.9%, execution 19.0%, market_freshness 18.1%, data 13.0%, market_freshness/coverage 8.6%, mapping 4.5%, model_calibration_or_unknown 2.2%, model_calibration 0.7%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.1%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 74.6%, THIN_PLAYER_HISTORY 62.0%, STALE_KALSHI_QUOTE 51.1%, STALE_PLAYER_DATA 47.1%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 34.4%, WIDE_SPREAD 25.0%, PLAYER_IDENTITY_RISK 19.0%, MODEL_HIGH_UNCERTAINTY 18.1%, EVENT_MAPPING_RISK 10.0%, LEVEL_TRANSFER_RISK 9.6%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 5.1%, EXTERNAL_MARKET_REJECTION 1.8%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.8%, POST_SETTLEMENT_OBSERVATION 33.9%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 7965, "IDENTITY_AMBIGUOUS": 2198}; ticker orientation: {"VERIFIED": 10163}.

Checks: discipline:AMBIGUOUS 700, discipline:PASS 9463, identity_confidence:AMBIGUOUS 1931, identity_confidence:PASS 8232, level_mapping:NA 712, level_mapping:PASS 9451, market_pair:AMBIGUOUS 372, market_pair:NA 243, market_pair:PASS 9548, model_complement:NA 210, model_complement:PASS 9953, namesake:PASS 10163, physical_match_id:NA 3768, physical_match_id:PASS 6395, player_ids:PASS 10163, same_pair_other_event:PASS 10163, ticker_orientation:PASS 10163

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,621 | 5.0% | 4.6% | 1.8% | {"market_freshness": 53, "model_calibration_or_unknown": 41, "data": 36, "execution": 19, "model_calibration": 13, "market_freshness/coverage": 11, "coverage": 7} | 5.87 | 0.2256 / 0.2158 (401) | 18.7% | 4.1% | 3.5% | 2.7% |
| CHALLENGER | 7,320 | 17.2% | 7.0% | 12.4% | {"coverage": 709, "market_freshness/coverage": 157, "market_freshness": 146, "data": 118, "model_calibration_or_unknown": 59, "execution": 30, "model_calibration": 27, "mapping": 14} | 7.48 | 0.2177 / 0.2071 (1774) | 35.0% | 17.2% | 3.9% | 22.6% |
| DOUBLES | 1,449 | 48.3% | 47.9% | 6.9% | {"execution": 360, "mapping": 179, "market_freshness": 106, "market_freshness/coverage": 48, "coverage": 7} | 23.99 | 0.3198 / 0.2347 (368) | 16.2% | 0.0% | 100.0% | 7.0% |
| ITF_MEN | 12,646 | 25.0% | 17.7% | 31.1% | {"coverage": 1153, "execution": 638, "market_freshness": 518, "data": 443, "market_freshness/coverage": 252, "mapping": 152, "model_calibration_or_unknown": 2, "model_calibration": 1} | 11.62 | 0.2143 / 0.1953 (2857) | 36.4% | 66.6% | 17.4% | 21.6% |
| ITF_WOMEN | 17,208 | 26.5% | 19.6% | 44.9% | {"coverage": 1550, "market_freshness": 938, "execution": 854, "data": 693, "market_freshness/coverage": 358, "mapping": 101, "model_calibration_or_unknown": 53, "model_calibration": 11} | 12.84 | 0.2031 / 0.1953 (3323) | 38.2% | 57.5% | 10.1% | 21.2% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,618 | 4.6% | 4.2% | 1.2% | {"market_freshness": 38, "model_calibration_or_unknown": 27, "execution": 17, "model_calibration": 12, "data": 11, "market_freshness/coverage": 10, "coverage": 4, "mapping": 1} | 7.91 | 0.2363 / 0.2302 (429) | 23.8% | 1.3% | 1.4% | 3.4% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.7% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 207 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 15 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 16 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 17 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 18 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 19 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 20 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 21 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 22 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 23 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 24 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 25 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 26 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 27 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 28 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 463 min (STALE); no external reference |
| 29 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 30 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 31 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 32 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 33 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 34 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 22.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1345 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 36 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 37 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 38 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 39 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 41 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 162 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 42 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 43 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 765 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 44 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 45 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 46 | `KXITFWMATCH-26OCT20CHAAPI-CHA` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 122.0, ratio 20.3); no external reference |
| 47 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.2h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 196 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |
| 48 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 547 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 49 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 50 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9705, "by_level_share_of_ge_25pp": {"ATP": 0.0177, "CHALLENGER": 0.124, "DOUBLES": 0.0689, "ITF_MEN": 0.3108, "ITF_WOMEN": 0.4485, "OTHER": 0.0012, "WTA": 0.0118, "WTA125": 0.0171}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5107, "share_primary_cause_market_settled_or_in_play": 0.4249, "share_primary_cause_stale_quote_only": 0.181}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 10163, "identity_ambiguous_share": 0.2163, "ticker_orientation": {"VERIFIED": 10163}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 6395, "with_external": 324, "coverage": 0.0507, "external_status": {"EXTERNAL_STALE": 199, "AGREES_WITH_KALSHI": 117, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 199, "MODEL_LONE_OUTLIER": 117, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3611, "share_external_supports_model": 0.0247}, "pregame_clean_ge_25pp": {"n": 3160, "with_external": 306, "coverage": 0.0968, "external_status": {"EXTERNAL_STALE": 185, "AGREES_WITH_KALSHI": 113, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 185, "MODEL_LONE_OUTLIER": 113, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3693, "share_external_supports_model": 0.0261}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 494.0, "median_sample_ratio": 2.44, "median_min_matches": 20.0, "median_max_days_since_last": 223.0, "share_severe_asymmetry": 0.2104, "data_status": {"POOR": 5640, "LIMITED": 2753, "ADEQUATE": 1770}, "comparison_lt_10pp": {"median_thinner_serve_points": 1716.0, "median_sample_ratio": 1.7, "median_min_matches": 92.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 769, "model_minus_observed": 0.0476, "kalshi_minus_observed": -0.0887, "brier_diff_model_minus_kalshi": -0.0023}, "4-10x": {"n": 522, "model_minus_observed": 0.088, "kalshi_minus_observed": -0.0566, "brier_diff_model_minus_kalshi": 0.0124}, "<2x": {"n": 1882, "model_minus_observed": 0.0862, "kalshi_minus_observed": -0.0366, "brier_diff_model_minus_kalshi": 0.0128}, ">=10x": {"n": 655, "model_minus_observed": 0.1032, "kalshi_minus_observed": -0.0714, "brier_diff_model_minus_kalshi": 0.0062}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3828, "model": {"intercept": -0.53, "slope": 0.845, "slope_se": 0.042}, "kalshi_mid_same_rows": {"intercept": 0.237, "slope": 1.121, "slope_se": 0.048}, "mean_extremity_model": 0.1702, "mean_extremity_kalshi": 0.1649, "model_brier": 0.2324, "kalshi_brier": 0.2047, "brier_diff_model_minus_kalshi": 0.0277, "brier_diff_se": 0.0031, "model_logloss": 0.6613, "kalshi_logloss": 0.5921}, "fair_v1": {"n": 3828, "model": {"intercept": -0.393, "slope": 1.045, "slope_se": 0.046}, "kalshi_mid_same_rows": {"intercept": 0.326, "slope": 1.164, "slope_se": 0.048}, "mean_extremity_model": 0.1668, "mean_extremity_kalshi": 0.1645, "model_brier": 0.2136, "kalshi_brier": 0.205, "brier_diff_model_minus_kalshi": 0.0086, "brier_diff_se": 0.0025, "model_logloss": 0.6154, "kalshi_logloss": 0.5926}, "gen1_elo": {"n": 3828, "model": {"intercept": -0.39, "slope": 1.024, "slope_se": 0.044}, "kalshi_mid_same_rows": {"intercept": 0.318, "slope": 1.146, "slope_se": 0.047}, "mean_extremity_model": 0.1734, "mean_extremity_kalshi": 0.1647, "model_brier": 0.2127, "kalshi_brier": 0.205, "brier_diff_model_minus_kalshi": 0.0077, "brier_diff_se": 0.0025, "model_logloss": 0.6142, "kalshi_logloss": 0.5927}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2428, "share_ge_15": 0.4429, "median_abs_gap": 13.1, "n": 26338}, "gen1_elo": {"share_ge_25": 0.2403, "share_ge_15": 0.4397, "median_abs_gap": 12.82, "n": 26338}, "gen1_sr": {"share_ge_25": 0.3088, "share_ge_15": 0.5228, "median_abs_gap": 15.91, "n": 26338}, "gen2": {"share_ge_25": 0.3109, "share_ge_15": 0.5112, "median_abs_gap": 15.51, "n": 26338}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1535, "share_ge_15": 0.361, "median_abs_gap": 10.96, "n": 20589}, "gen1_elo": {"share_ge_25": 0.1546, "share_ge_15": 0.3554, "median_abs_gap": 10.55, "n": 20587}, "gen1_sr": {"share_ge_25": 0.2193, "share_ge_15": 0.4484, "median_abs_gap": 13.25, "n": 20590}, "gen2": {"share_ge_25": 0.2343, "share_ge_15": 0.4473, "median_abs_gap": 13.16, "n": 20590}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.87, "share_ge_25_all": 0.0497, "share_ge_25_pregame_clean": 0.046}, "WTA": {"median_abs_gap_pregame_clean": 7.91, "share_ge_25_all": 0.0458, "share_ge_25_pregame_clean": 0.0419}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2362, "share_within_10pp_all": 0.4337, "share_within_10pp_pregame_clean": 0.4849, "corr_model_vs_mid_pregame_clean": 0.8449}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 570, "model_brier": 0.1969, "kalshi_brier": 0.1983, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 666, "model_brier": 0.2129, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": 0.0095}, "15-25": {"n_settled": 860, "model_brier": 0.2249, "kalshi_brier": 0.2148, "brier_diff_model_minus_kalshi": 0.0101}, "25-40": {"n_settled": 485, "model_brier": 0.2265, "kalshi_brier": 0.2097, "brier_diff_model_minus_kalshi": 0.0168}, "3-5": {"n_settled": 360, "model_brier": 0.1998, "kalshi_brier": 0.1997, "brier_diff_model_minus_kalshi": 0.0001}, "40+": {"n_settled": 97, "model_brier": 0.2967, "kalshi_brier": 0.1848, "brier_diff_model_minus_kalshi": 0.1119}, "5-10": {"n_settled": 790, "model_brier": 0.2018, "kalshi_brier": 0.2024, "brier_diff_model_minus_kalshi": -0.0006}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.53, "slope": 0.845, "slope_se": 0.042}, "kalshi_slope": {"intercept": 0.237, "slope": 1.121, "slope_se": 0.048}, "n": 3828}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.508, "slope": 0.873, "slope_se": 0.032}, "kalshi_slope": {"intercept": 0.163, "slope": 1.085, "slope_se": 0.037}, "n": 5854}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 368, "model_brier": 0.3198, "kalshi_brier": 0.2347, "brier_diff_model_minus_kalshi": 0.085, "brier_diff_se": 0.0163, "corr_model_outcome": 0.015, "corr_kalshi_outcome": 0.2592}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
