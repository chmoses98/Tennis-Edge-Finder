# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-07T23:29Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 23,162): 0-3 13.6%, 3-5 9.6%, 5-10 19.8%, 10-15 15.3%, 15-25 18.8%, 25-40 14.3%, 40+ 8.6%; median gap 12.15 pp.
* **Where the extremes live**: 98.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.7%, Challenger 12.9%, doubles 5.0%). Main tour: ATP 1.8% and WTA 8.2% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 5,299): MARKET_ALREADY_SETTLED_WHEN_PRICED 40.4%, STALE_QUOTE 18.1%, BOOK_QUALITY 16.6%, POOR_DATA 8.1%, POSSIBLY_IN_PLAY_QUOTE 5.2%, LIMITED_DATA 3.7%, IN_PLAY_QUOTE 3.2%, IDENTITY_AMBIGUOUS 2.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.2%. By class: coverage 40.4%, market_freshness 18.1%, execution 16.6%, data 11.8%, market_freshness/coverage 8.4%, mapping 2.5%, model_calibration_or_unknown 2.0%, model_calibration 0.2%.
* **Stale / settled / in-play**: 57.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 48.8% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 5,299 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 15.9% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 1.4%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 12.3% of the time and with the model 0.2%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 604.0 points vs 1702.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.14, Gen-2 0.918, Gen-1 ledger 0.942 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 216 model 0.215 vs Kalshi 0.2038; n 49 model 0.2835 vs Kalshi 0.1763.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%). Not implemented here.

## 1. Observations

* 86,306 model-market comparisons (145,270 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 32,764 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-07T23:23:48.480048+00:00'], shadow board 24,142 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-07T23:23:52.393666+00:00'], Model 4 8,655 rows, 10,390 settled tickers, 2,605 tickers with an external scan.
* By model: {"gen1_ledger": 20725, "gen1_elo": 12131, "fair_v1": 12131, "gen2": 12131, "gen1_sr": 12131, "model4_fundamental": 8533, "model4_conditioned": 8524}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 23,162 | 13.6 | 9.6 | 19.8 | 15.3 | 18.8 | 14.3 | 8.6 | 12.15 | 41.7% | 22.9% |
| MW fair_v1 | 12,131 | 12.8 | 8.8 | 18.3 | 15.9 | 18.5 | 15.2 | 10.4 | 13.12 | 44.2% | 25.6% |
| MW gen1_elo | 12,131 | 12.6 | 8.8 | 19.6 | 14.9 | 19.4 | 14.9 | 9.7 | 12.74 | 44.0% | 24.6% |
| MW gen1_ledger | 11,031 | 14.4 | 10.4 | 21.5 | 14.6 | 19.2 | 13.2 | 6.6 | 11.08 | 39.0% | 19.9% |
| MW gen1_sr | 12,131 | 10.0 | 7.7 | 15.8 | 14.1 | 21.6 | 18.7 | 12.0 | 15.87 | 52.3% | 30.8% |
| MW gen2 | 12,131 | 11.7 | 7.1 | 15.8 | 14.3 | 19.9 | 17.6 | 13.5 | 15.46 | 51.0% | 31.1% |
| all families model4_conditioned | 8,524 | 21.9 | 20.4 | 35.3 | 16.1 | 4.6 | 0.9 | 0.8 | 5.75 | 6.3% | 1.7% |
| all families model4_fundamental | 8,533 | 16.4 | 13.3 | 34.5 | 20.4 | 11.1 | 3.1 | 1.2 | 7.81 | 15.4% | 4.3% |

Configurable thresholds (primary): >=5pp 76.8%, >=10pp 57.0%, >=15pp 41.7%, >=20pp 31.3%, >=25pp 22.9%, >=30pp 16.8%, >=40pp 8.6%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.54pp; >=10pp 45.9%, >=25pp 18.4%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 851 | 25.9 | 16.6 | 24.2 | 17.3 | 13.4 | 1.4 | 1.3 | 6.01 | 16.1% | 2.7% |
| CHALLENGER | 2,139 | 14.2 | 11.2 | 18.4 | 16.1 | 13.1 | 13.7 | 13.3 | 12.06 | 40.1% | 27.0% |
| ITF_MEN | 3,475 | 10.6 | 8.4 | 18.8 | 14.5 | 19.5 | 15.2 | 13.0 | 14.08 | 47.7% | 28.2% |
| ITF_WOMEN | 4,837 | 10.3 | 6.8 | 16.0 | 16.0 | 21.5 | 19.3 | 10.2 | 15.41 | 51.0% | 29.5% |
| WTA | 527 | 23.3 | 9.7 | 24.7 | 16.5 | 17.5 | 6.3 | 2.1 | 8.17 | 25.8% | 8.3% |
| WTA125 | 302 | 12.6 | 7.0 | 20.9 | 25.2 | 14.6 | 17.2 | 2.6 | 11.32 | 34.4% | 19.9% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 851 | 21.5 | 14.9 | 23.7 | 18.6 | 17.3 | 2.5 | 1.5 | 6.9 | 21.3% | 4.0% |
| CHALLENGER | 2,139 | 14.8 | 7.2 | 17.6 | 13.4 | 18.6 | 14.7 | 13.7 | 13.56 | 47.0% | 28.4% |
| ITF_MEN | 3,475 | 10.3 | 7.2 | 16.6 | 14.7 | 19.7 | 17.7 | 13.7 | 15.48 | 51.2% | 31.4% |
| ITF_WOMEN | 4,837 | 9.0 | 6.0 | 12.9 | 13.0 | 20.9 | 21.5 | 16.7 | 18.93 | 59.1% | 38.2% |
| WTA | 527 | 21.8 | 5.1 | 17.6 | 15.4 | 21.4 | 16.5 | 2.1 | 12.72 | 40.0% | 18.6% |
| WTA125 | 302 | 5.0 | 3.0 | 16.9 | 23.2 | 19.5 | 19.9 | 12.6 | 16.69 | 52.0% | 32.5% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 851 | 26.2 | 11.4 | 29.5 | 16.9 | 11.1 | 3.5 | 1.4 | 6.85 | 16.0% | 4.9% |
| CHALLENGER | 2,139 | 15.3 | 11.1 | 19.4 | 14.1 | 14.1 | 12.7 | 13.3 | 11.11 | 40.1% | 26.0% |
| ITF_MEN | 3,475 | 9.6 | 8.8 | 18.3 | 13.9 | 20.9 | 15.6 | 13.0 | 14.88 | 49.5% | 28.6% |
| ITF_WOMEN | 4,837 | 9.6 | 6.8 | 16.6 | 15.6 | 23.5 | 19.1 | 8.8 | 15.57 | 51.4% | 27.9% |
| WTA | 527 | 23.0 | 13.3 | 34.9 | 14.4 | 9.5 | 3.6 | 1.3 | 6.99 | 14.4% | 4.9% |
| WTA125 | 302 | 21.2 | 12.2 | 27.8 | 17.6 | 15.2 | 5.3 | 0.7 | 7.73 | 21.2% | 6.0% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 413 | 28.1 | 21.1 | 38.0 | 11.6 | 1.2 | 0.0 | 0.0 | 5.11 | 1.2% | 0.0% |
| CHALLENGER | 1,364 | 22.8 | 16.3 | 26.5 | 14.2 | 12.5 | 5.6 | 2.2 | 6.77 | 20.2% | 7.8% |
| DOUBLES | 595 | 4.0 | 3.2 | 13.1 | 12.3 | 22.7 | 21.7 | 23.0 | 23.06 | 67.4% | 44.7% |
| ITF_MEN | 3,502 | 13.8 | 8.6 | 20.1 | 15.2 | 20.6 | 13.2 | 8.4 | 12.16 | 42.3% | 21.6% |
| ITF_WOMEN | 4,101 | 11.6 | 9.6 | 19.4 | 14.0 | 22.2 | 17.3 | 6.0 | 13.17 | 45.5% | 23.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 435 | 19.8 | 11.7 | 25.8 | 19.1 | 15.6 | 7.4 | 0.7 | 8.5 | 23.7% | 8.1% |
| WTA125 | 472 | 15.5 | 12.9 | 22.2 | 19.5 | 17.6 | 9.3 | 3.0 | 9.86 | 29.9% | 12.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 847 | 25.9 | 16.4 | 24.2 | 17.4 | 13.5 | 1.4 | 1.3 | 6.01 | 16.2% | 2.7% |
| CHALLENGER | 1,502 | 18.8 | 14.4 | 24.0 | 18.9 | 13.9 | 7.0 | 3.0 | 8.35 | 23.9% | 10.0% |
| ITF_MEN | 2,495 | 13.0 | 10.8 | 22.3 | 16.2 | 19.7 | 12.2 | 5.8 | 11.08 | 37.7% | 18.0% |
| ITF_WOMEN | 3,481 | 12.8 | 8.5 | 18.9 | 18.5 | 23.0 | 15.2 | 3.0 | 12.65 | 41.3% | 18.3% |
| WTA | 524 | 23.3 | 9.7 | 24.8 | 16.4 | 17.6 | 6.1 | 2.1 | 8.16 | 25.8% | 8.2% |
| WTA125 | 291 | 13.1 | 7.2 | 20.6 | 25.4 | 14.8 | 17.2 | 1.7 | 11.31 | 33.7% | 18.9% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 847 | 21.4 | 14.9 | 23.9 | 18.5 | 17.4 | 2.5 | 1.5 | 6.9 | 21.4% | 4.0% |
| CHALLENGER | 1,502 | 19.6 | 9.6 | 22.4 | 16.4 | 19.1 | 10.1 | 2.9 | 9.61 | 32.0% | 12.9% |
| ITF_MEN | 2,496 | 12.3 | 8.7 | 19.4 | 16.8 | 21.0 | 15.1 | 6.7 | 12.7 | 42.8% | 21.8% |
| ITF_WOMEN | 3,481 | 10.5 | 7.2 | 14.9 | 14.3 | 22.9 | 20.0 | 10.2 | 16.17 | 53.1% | 30.2% |
| WTA | 524 | 21.8 | 5.2 | 17.8 | 15.5 | 21.4 | 16.4 | 2.1 | 12.71 | 39.9% | 18.5% |
| WTA125 | 291 | 5.2 | 3.1 | 17.2 | 24.1 | 18.6 | 20.6 | 11.3 | 15.35 | 50.5% | 32.0% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 398 | 28.4 | 21.4 | 38.2 | 11.8 | 0.2 | 0.0 | 0.0 | 5.06 | 0.2% | 0.0% |
| CHALLENGER | 1,146 | 24.8 | 18.5 | 29.0 | 13.8 | 11.8 | 2.1 | 0.1 | 6.16 | 14.0% | 2.2% |
| DOUBLES | 541 | 4.1 | 3.1 | 13.5 | 12.2 | 23.1 | 21.3 | 22.7 | 22.7 | 67.1% | 44.0% |
| ITF_MEN | 2,800 | 15.5 | 9.6 | 22.5 | 16.3 | 20.4 | 10.8 | 4.9 | 10.7 | 36.1% | 15.7% |
| ITF_WOMEN | 3,314 | 13.0 | 10.4 | 21.3 | 14.8 | 22.4 | 15.6 | 2.5 | 11.45 | 40.5% | 18.0% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 405 | 20.2 | 12.3 | 26.4 | 19.3 | 16.1 | 5.7 | 0.0 | 8.4 | 21.7% | 5.7% |
| WTA125 | 389 | 17.5 | 14.4 | 24.9 | 22.4 | 15.7 | 4.9 | 0.3 | 8.61 | 20.8% | 5.1% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 595 | 4.0 | 3.2 | 13.1 | 12.3 | 22.7 | 21.7 | 23.0 | 23.06 | 67.4% | 44.7% |
| singles | 10,436 | 15.0 | 10.8 | 21.9 | 14.8 | 18.9 | 12.8 | 5.7 | 10.55 | 37.4% | 18.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 2,836 | 12.9 | 9.6 | 20.1 | 15.5 | 16.0 | 14.9 | 11.0 | 12.48 | 42.0% | 25.9% |
| Hard | 8,168 | 12.9 | 8.6 | 18.2 | 15.8 | 19.2 | 15.1 | 10.2 | 13.25 | 44.5% | 25.3% |
| UNKNOWN | 1,127 | 11.9 | 8.5 | 14.0 | 18.3 | 20.1 | 17.2 | 10.0 | 14.11 | 47.3% | 27.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,483 | 17.7 | 11.3 | 20.2 | 16.9 | 15.1 | 10.3 | 8.5 | 10.19 | 33.8% | 18.8% |
| B | 1,518 | 14.8 | 9.9 | 19.7 | 17.1 | 16.2 | 11.9 | 10.3 | 11.19 | 38.4% | 22.2% |
| C | 1,892 | 12.5 | 9.6 | 20.8 | 15.0 | 18.3 | 14.3 | 9.5 | 12.57 | 42.1% | 23.8% |
| D | 2,322 | 11.2 | 8.7 | 16.6 | 16.1 | 22.7 | 15.2 | 9.4 | 14.1 | 47.3% | 24.6% |
| F | 2,916 | 7.1 | 4.9 | 15.0 | 14.6 | 20.7 | 23.6 | 14.0 | 18.59 | 58.3% | 37.6% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,001 | 21.1 | 15.0 | 27.2 | 15.9 | 13.1 | 5.4 | 2.2 | 7.28 | 20.7% | 7.6% |
| B | 1,695 | 14.4 | 10.0 | 24.5 | 15.6 | 18.4 | 11.9 | 5.2 | 10.28 | 35.5% | 17.1% |
| C | 2,193 | 12.1 | 8.2 | 19.5 | 14.6 | 21.1 | 14.6 | 9.8 | 13.11 | 45.6% | 24.4% |
| D | 1,883 | 13.1 | 9.1 | 21.1 | 13.2 | 22.3 | 14.8 | 6.4 | 12.38 | 43.5% | 21.2% |
| F | 2,259 | 9.1 | 7.9 | 13.8 | 13.4 | 23.2 | 22.1 | 10.6 | 17.11 | 55.9% | 32.7% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 3,961 | 16.8 | 10.5 | 19.4 | 17.1 | 15.2 | 10.6 | 10.4 | 10.92 | 36.2% | 20.9% |
| LIMITED | 2,895 | 14.2 | 10.6 | 21.4 | 15.5 | 17.4 | 13.4 | 7.5 | 11.1 | 38.3% | 20.9% |
| POOR | 5,275 | 9.0 | 6.7 | 15.7 | 15.3 | 21.6 | 19.8 | 11.9 | 16.36 | 53.3% | 31.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,729 | 29.7 | 26.3 | 36.7 | 5.4 | 1.7 | 0.2 | 0.0 | 4.47 | 1.8% | 0.2% |
| GAME_SPREAD | 1,817 | 24.1 | 15.2 | 36.9 | 18.8 | 4.6 | 0.3 | 0.2 | 6.19 | 5.0% | 0.4% |
| MATCH_WINNER | 11,031 | 14.4 | 10.4 | 21.5 | 14.6 | 19.2 | 13.2 | 6.6 | 11.08 | 39.0% | 19.9% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 3,378 | 29.2 | 18.9 | 31.4 | 11.5 | 7.4 | 1.4 | 0.3 | 5.21 | 9.1% | 1.7% |
| TOTAL_GAMES | 2,746 | 7.6 | 9.3 | 38.1 | 29.5 | 9.9 | 3.3 | 2.3 | 9.45 | 15.6% | 5.6% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,128 | 24.4 | 39.4 | 29.5 | 0.3 | 5.7 | 0.5 | 0.2 | 4.34 | 6.5% | 0.7% |
| GAME_SPREAD | 2,166 | 45.8 | 14.1 | 29.6 | 8.6 | 1.1 | 0.6 | 0.2 | 3.57 | 1.8% | 0.7% |
| TOTAL_GAMES | 3,230 | 3.4 | 6.2 | 44.6 | 36.6 | 5.9 | 1.5 | 1.7 | 9.64 | 9.1% | 3.2% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,128 | 25.3 | 18.4 | 35.5 | 10.1 | 7.3 | 3.0 | 0.5 | 5.62 | 10.8% | 3.5% |
| GAME_SPREAD | 2,166 | 19.3 | 13.2 | 26.2 | 23.0 | 14.6 | 3.0 | 0.7 | 8.35 | 18.3% | 3.7% |
| TOTAL_GAMES | 3,239 | 5.8 | 8.6 | 39.1 | 28.7 | 12.4 | 3.2 | 2.1 | 9.61 | 17.8% | 5.4% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 12,131 | 44.2% | 25.6% | 13.12 | 34.0% | 14.9% | 10.48 |
| gen1_elo | 12,131 | 44.0% | 24.6% | 12.74 | 33.6% | 14.3% | 10.05 |
| gen1_sr | 12,131 | 52.3% | 30.8% | 15.87 | 43.3% | 20.2% | 12.92 |
| gen2 | 12,131 | 51.0% | 31.1% | 15.46 | 43.0% | 22.0% | 12.74 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 5,894 | 15.5 | 11.5 | 21.6 | 17.3 | 18.7 | 12.0 | 3.5 | 10.39 | 34.2% | 15.5% |
| STALE | 6,237 | 10.2 | 6.3 | 15.2 | 14.6 | 18.4 | 18.4 | 16.8 | 16.97 | 53.6% | 35.2% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 4,499 | 16.4 | 11.7 | 24.0 | 14.5 | 17.2 | 12.0 | 4.2 | 9.42 | 33.5% | 16.2% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 23,162 | 4499 | 9366 | 9297 | 25.6 | 176.5 | 1400.4 |
| ge_15pp | 9,661 | 1505 | 3304 | 4852 | 30.2 | 459.5 | 1380.4 |
| ge_25pp | 5,299 | 729 | 1505 | 3065 | 40.0 | 574.8 | 1380.4 |
| lt_10pp | 9,952 | 2343 | 4490 | 3119 | 24.4 | 52.9 | 1230.8 |

Current slate `SL-20261007T232911Z-2d892952`: 522 priced rows, quote age at build {'median': 5.7, 'max': 5.7}, freshness {'FRESH': 522}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 1 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 20.71 | 100.0% | 0.0% |
| EXTERNAL_LONE_OUTLIER | 2 | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.98 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 454 | 20.3 | 12.8 | 21.4 | 20.0 | 18.1 | 7.0 | 0.4 | 8.64 | 25.6% | 7.5% |
| MARKETS_AGREE | 35 | 71.4 | 28.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 69 | 0.0 | 2.9 | 27.5 | 34.8 | 21.7 | 13.0 | 0.0 | 11.66 | 34.8% | 13.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 12,131 | 561 (4.6%) | 12.3% | 0.2% | {"EXTERNAL_STALE": 454, "AGREES_WITH_KALSHI": 69, "ALL_AGREE": 35, "EXTERNAL_OUTLIER": 2, "SUPPORTS_MODEL_DIRECTION": 1} |
| fair_v1_ge_15pp | 5,357 | 141 (2.6%) | 17.0% | 0.7% | {"EXTERNAL_STALE": 116, "AGREES_WITH_KALSHI": 24, "SUPPORTS_MODEL_DIRECTION": 1} |
| fair_v1_ge_25pp | 3,108 | 43 (1.4%) | 20.9% | 0.0% | {"EXTERNAL_STALE": 34, "AGREES_WITH_KALSHI": 9} |
| fair_v1_ge_25pp_pregame_clean | 1,358 | 42 (3.1%) | 21.4% | 0.0% | {"EXTERNAL_STALE": 33, "AGREES_WITH_KALSHI": 9} |
| fair_v1_lt_10pp | 4,840 | 305 (6.3%) | 6.9% | 0.0% | {"EXTERNAL_STALE": 247, "ALL_AGREE": 35, "AGREES_WITH_KALSHI": 21, "EXTERNAL_OUTLIER": 2} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 2,454 | 11.0 | 8.6 | 20.3 | 15.7 | 20.9 | 14.1 | 9.3 | 12.89 | 44.3% | 23.5% |
| 4-10x | 1,785 | 11.1 | 9.3 | 18.0 | 14.3 | 20.7 | 17.3 | 9.3 | 14.1 | 47.3% | 26.6% |
| <2x | 6,321 | 14.6 | 9.5 | 18.2 | 16.8 | 17.0 | 13.6 | 10.4 | 12.4 | 40.9% | 24.0% |
| >=10x | 1,571 | 10.2 | 6.1 | 15.7 | 14.8 | 18.8 | 21.3 | 13.2 | 16.49 | 53.2% | 34.4% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 3,071 | 13.6 | 8.6 | 20.2 | 15.8 | 17.4 | 13.0 | 11.3 | 12.22 | 41.8% | 24.3% |
| 300-1000 | 2,981 | 12.1 | 9.3 | 16.6 | 15.8 | 21.3 | 16.1 | 8.7 | 13.74 | 46.2% | 24.9% |
| <300 | 3,393 | 7.9 | 6.0 | 15.5 | 14.8 | 20.7 | 21.5 | 13.5 | 17.47 | 55.7% | 35.0% |
| >=3000 | 2,686 | 18.7 | 12.1 | 21.4 | 17.7 | 13.9 | 9.0 | 7.2 | 9.46 | 30.1% | 16.2% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 374 | 0.5403 | 0.408 | 0.4706 | +0.070 | -0.063 | 0.0019 ± 0.0075 |
| ratio 4-10x | 277 | 0.5871 | 0.446 | 0.5343 | +0.053 | -0.088 | -0.0054 ± 0.0093 |
| ratio <2x | 791 | 0.544 | 0.4165 | 0.4589 | +0.085 | -0.042 | 0.0106 ± 0.0052 |
| ratio >=10x | 256 | 0.5631 | 0.388 | 0.4648 | +0.098 | -0.077 | 0.0115 ± 0.0115 |
| thinner_sample 1000-3000 | 445 | 0.5467 | 0.4208 | 0.4629 | +0.084 | -0.042 | 0.0051 ± 0.0068 |
| thinner_sample 300-1000 | 468 | 0.5735 | 0.4336 | 0.4979 | +0.076 | -0.064 | 0.0003 ± 0.0072 |
| thinner_sample <300 | 543 | 0.553 | 0.3898 | 0.4807 | +0.072 | -0.091 | 0.0069 ± 0.0074 |
| thinner_sample >=3000 | 242 | 0.5256 | 0.4259 | 0.438 | +0.088 | -0.012 | 0.0182 ± 0.0076 |
| data_status ADEQUATE | 448 | 0.5294 | 0.4226 | 0.4375 | +0.092 | -0.015 | 0.0121 ± 0.0059 |
| data_status LIMITED | 407 | 0.5677 | 0.4332 | 0.4988 | +0.069 | -0.066 | -0.0006 ± 0.0075 |
| data_status POOR | 843 | 0.5586 | 0.4024 | 0.4828 | +0.076 | -0.080 | 0.0064 ± 0.0058 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 247 | 0.1792 | 0.1803 | -0.0011 ± 0.0009 | 0.532 | 0.5348 | 0.4937 | 0.4793 | 0.5101 | -0.086 ± 0.0286 | -0.01 (3) |
| 3-5 | 169 | 0.1834 | 0.1835 | -0.0001 ± 0.0027 | 0.5454 | 0.5429 | 0.5123 | 0.4723 | 0.4852 | -0.091 ± 0.0335 | 0.02 (1) |
| 5-10 | 351 | 0.2014 | 0.2031 | -0.0017 ± 0.0036 | 0.5895 | 0.5947 | 0.5218 | 0.4481 | 0.4872 | -0.096 ± 0.0251 | -0.0167 (3) |
| 10-15 | 297 | 0.2203 | 0.2182 | +0.0021 ± 0.0068 | 0.6292 | 0.6206 | 0.5337 | 0.4093 | 0.4613 | -0.092 ± 0.0272 | -0.0633 (3) |
| 15-25 | 369 | 0.2197 | 0.2112 | +0.0085 ± 0.0094 | 0.6302 | 0.6103 | 0.5737 | 0.3777 | 0.4526 | -0.081 ± 0.0238 | -0.02 (4) |
| 25-40 | 216 | 0.215 | 0.2038 | +0.0112 ± 0.0182 | 0.6179 | 0.5838 | 0.6507 | 0.3406 | 0.4769 | -0.070 ± 0.0271 | -0.01 (1) |
| 40+ | 49 | 0.2835 | 0.1763 | +0.1072 ± 0.0527 | 0.7693 | 0.5281 | 0.75 | 0.3043 | 0.4082 | -0.120 ± 0.0527 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1141 | 0.1627 | 0.1631 | -0.0004 ± 0.0004 | 0.4912 | 0.4912 | 0.4783 | 0.4634 | 0.4952 | -0.037 ± 0.0122 | -0.0188 (8) |
| 3-5 | 813 | 0.1906 | 0.1854 | +0.0052 ± 0.0012 | 0.5637 | 0.5457 | 0.4795 | 0.44 | 0.3899 | -0.114 ± 0.0153 | 0.02 (1) |
| 5-10 | 1733 | 0.1904 | 0.1887 | +0.0017 ± 0.0016 | 0.5634 | 0.5587 | 0.4914 | 0.4177 | 0.4403 | -0.053 ± 0.0106 | -0.0129 (7) |
| 10-15 | 1513 | 0.2052 | 0.1909 | +0.0143 ± 0.0028 | 0.5966 | 0.5563 | 0.4789 | 0.3542 | 0.3596 | -0.071 ± 0.0112 | -0.0633 (3) |
| 15-25 | 1869 | 0.1979 | 0.1635 | +0.0344 ± 0.0037 | 0.5846 | 0.4878 | 0.4899 | 0.2933 | 0.305 | -0.068 ± 0.0093 | -0.017 (10) |
| 25-40 | 1658 | 0.2151 | 0.126 | +0.0892 ± 0.0055 | 0.6221 | 0.3884 | 0.5284 | 0.2149 | 0.2316 | -0.056 ± 0.0084 | -0.01 (1) |
| 40+ | 1149 | 0.3655 | 0.0463 | +0.3192 ± 0.007 | 0.9539 | 0.1802 | 0.6199 | 0.1056 | 0.0627 | -0.078 ± 0.0059 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 194 | 0.1952 | 0.1954 | -0.0003 ± 0.0011 | 0.5738 | 0.5741 | 0.4941 | 0.4791 | 0.4742 | -0.119 ± 0.0333 | -0.01 (1) |
| 3-5 | 124 | 0.2044 | 0.2038 | +0.0006 ± 0.0033 | 0.5872 | 0.5894 | 0.5078 | 0.4679 | 0.4758 | -0.085 ± 0.0434 | 0.02 (1) |
| 5-10 | 296 | 0.192 | 0.1907 | +0.0013 ± 0.0038 | 0.5672 | 0.5638 | 0.5649 | 0.4896 | 0.5135 | -0.092 ± 0.0262 | -0.01 (4) |
| 10-15 | 291 | 0.2187 | 0.2079 | +0.0108 ± 0.0067 | 0.6242 | 0.6027 | 0.5871 | 0.4627 | 0.488 | -0.120 ± 0.0279 | -0.0667 (3) |
| 15-25 | 410 | 0.2228 | 0.2069 | +0.0160 ± 0.0089 | 0.6329 | 0.5952 | 0.6012 | 0.4037 | 0.4683 | -0.102 ± 0.0232 | -0.0167 (3) |
| 25-40 | 278 | 0.2637 | 0.2062 | +0.0575 ± 0.017 | 0.7367 | 0.5946 | 0.6727 | 0.36 | 0.4245 | -0.132 ± 0.0274 | -0.025 (2) |
| 40+ | 105 | 0.3393 | 0.1907 | +0.1486 ± 0.0416 | 0.9415 | 0.5571 | 0.7604 | 0.2777 | 0.381 | -0.054 ± 0.0393 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1076 | 0.1747 | 0.1755 | -0.0008 ± 0.0004 | 0.5217 | 0.5239 | 0.4966 | 0.4824 | 0.5093 | -0.037 ± 0.0134 | -0.0217 (6) |
| 3-5 | 665 | 0.1868 | 0.1833 | +0.0035 ± 0.0013 | 0.5441 | 0.5371 | 0.516 | 0.476 | 0.4541 | -0.077 ± 0.0169 | 0.02 (1) |
| 5-10 | 1499 | 0.1819 | 0.1798 | +0.0021 ± 0.0016 | 0.5454 | 0.5366 | 0.514 | 0.4398 | 0.461 | -0.048 ± 0.0112 | -0.01 (5) |
| 10-15 | 1353 | 0.1957 | 0.1807 | +0.0150 ± 0.0029 | 0.5797 | 0.5314 | 0.5241 | 0.3999 | 0.405 | -0.075 ± 0.0118 | -0.0575 (4) |
| 15-25 | 1950 | 0.2087 | 0.1707 | +0.0380 ± 0.0037 | 0.608 | 0.5061 | 0.5283 | 0.3332 | 0.3364 | -0.082 ± 0.0095 | -0.0143 (7) |
| 25-40 | 1849 | 0.246 | 0.1388 | +0.1072 ± 0.0055 | 0.6964 | 0.4222 | 0.562 | 0.2451 | 0.2353 | -0.086 ± 0.0087 | -0.015 (6) |
| 40+ | 1484 | 0.3992 | 0.0721 | +0.3270 ± 0.008 | 1.0442 | 0.2484 | 0.67 | 0.1317 | 0.1112 | -0.061 ± 0.0067 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 255 | 0.1876 | 0.1899 | -0.0023 ± 0.001 | 0.5521 | 0.5587 | 0.5046 | 0.4894 | 0.549 | -0.036 ± 0.0276 | -0.01 (5) |
| 3-5 | 183 | 0.1851 | 0.1829 | +0.0021 ± 0.0025 | 0.5458 | 0.541 | 0.4933 | 0.454 | 0.4481 | -0.136 ± 0.0337 | -- (0) |
| 5-10 | 355 | 0.1959 | 0.1976 | -0.0017 ± 0.0036 | 0.5775 | 0.5805 | 0.5189 | 0.445 | 0.4873 | -0.085 ± 0.0245 | -0.01 (3) |
| 10-15 | 280 | 0.2168 | 0.216 | +0.0007 ± 0.0069 | 0.6243 | 0.6175 | 0.5443 | 0.421 | 0.4821 | -0.091 ± 0.0273 | -0.044 (5) |
| 15-25 | 366 | 0.2255 | 0.2103 | +0.0151 ± 0.0093 | 0.6478 | 0.6058 | 0.5821 | 0.3886 | 0.4454 | -0.099 ± 0.0238 | -0.03 (1) |
| 25-40 | 216 | 0.201 | 0.2095 | -0.0084 ± 0.018 | 0.5855 | 0.5991 | 0.6556 | 0.3441 | 0.5093 | -0.050 ± 0.0262 | 0.0 (1) |
| 40+ | 43 | 0.3101 | 0.1754 | +0.1346 ± 0.0575 | 0.8319 | 0.5258 | 0.7415 | 0.29 | 0.3721 | -0.132 ± 0.059 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1109 | 0.1765 | 0.1778 | -0.0012 ± 0.0004 | 0.5243 | 0.5272 | 0.4844 | 0.4692 | 0.5113 | -0.024 ± 0.0127 | -0.0162 (13) |
| 3-5 | 840 | 0.1856 | 0.1823 | +0.0033 ± 0.0012 | 0.5476 | 0.5406 | 0.4717 | 0.4323 | 0.4107 | -0.094 ± 0.0153 | -0.01 (2) |
| 5-10 | 1773 | 0.1819 | 0.1793 | +0.0026 ± 0.0015 | 0.5448 | 0.5344 | 0.4857 | 0.4117 | 0.4281 | -0.055 ± 0.0101 | -0.01 (3) |
| 10-15 | 1427 | 0.2 | 0.1834 | +0.0166 ± 0.0028 | 0.5856 | 0.5366 | 0.4932 | 0.3699 | 0.3637 | -0.085 ± 0.0112 | -0.03 (9) |
| 15-25 | 2048 | 0.2066 | 0.1681 | +0.0384 ± 0.0036 | 0.6063 | 0.5003 | 0.4953 | 0.2987 | 0.3003 | -0.073 ± 0.0091 | -0.03 (2) |
| 25-40 | 1599 | 0.2133 | 0.1215 | +0.0918 ± 0.0055 | 0.6174 | 0.3757 | 0.5228 | 0.2053 | 0.2233 | -0.058 ± 0.0082 | 0.0 (1) |
| 40+ | 1080 | 0.3788 | 0.0471 | +0.3317 ± 0.0075 | 0.9914 | 0.183 | 0.6263 | 0.105 | 0.0593 | -0.080 ± 0.0062 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 536 | 0.2023 | 0.2024 | -0.0000 ± 0.0007 | 0.5887 | 0.5882 | 0.4984 | 0.4836 | 0.4851 | -0.049 ± 0.0194 | -0.0226 (46) |
| 3-5 | 399 | 0.1954 | 0.1945 | +0.0008 ± 0.0018 | 0.5724 | 0.5689 | 0.4801 | 0.4406 | 0.4536 | -0.044 ± 0.022 | -0.0059 (32) |
| 5-10 | 823 | 0.1903 | 0.1851 | +0.0051 ± 0.0023 | 0.5639 | 0.551 | 0.4705 | 0.3969 | 0.3998 | -0.059 ± 0.0153 | -0.005 (72) |
| 10-15 | 541 | 0.2022 | 0.1917 | +0.0105 ± 0.0047 | 0.5923 | 0.5641 | 0.4761 | 0.3531 | 0.3715 | -0.046 ± 0.0188 | 0.0016 (63) |
| 15-25 | 744 | 0.2349 | 0.2102 | +0.0248 ± 0.0066 | 0.665 | 0.606 | 0.5436 | 0.3492 | 0.3844 | -0.054 ± 0.0169 | -0.0216 (58) |
| 25-40 | 414 | 0.244 | 0.1825 | +0.0616 ± 0.0131 | 0.6856 | 0.5377 | 0.6171 | 0.3036 | 0.3599 | -0.071 ± 0.0196 | -0.0216 (25) |
| 40+ | 138 | 0.3427 | 0.1826 | +0.1601 ± 0.0373 | 0.9731 | 0.5422 | 0.7671 | 0.2731 | 0.3841 | -0.037 ± 0.0327 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1487 | 0.1881 | 0.1879 | +0.0002 ± 0.0004 | 0.5542 | 0.5526 | 0.4986 | 0.4833 | 0.4822 | -0.048 ± 0.0112 | -0.0155 (82) |
| 3-5 | 1048 | 0.1855 | 0.1834 | +0.0020 ± 0.0011 | 0.5464 | 0.5416 | 0.4876 | 0.448 | 0.4466 | -0.051 ± 0.0133 | -0.018 (54) |
| 5-10 | 2189 | 0.1873 | 0.1798 | +0.0075 ± 0.0014 | 0.557 | 0.5366 | 0.4718 | 0.3979 | 0.3869 | -0.067 ± 0.0092 | -0.0089 (122) |
| 10-15 | 1521 | 0.1981 | 0.1836 | +0.0145 ± 0.0027 | 0.5826 | 0.5445 | 0.4875 | 0.3646 | 0.3669 | -0.059 ± 0.0109 | -0.0053 (99) |
| 15-25 | 2028 | 0.2268 | 0.198 | +0.0288 ± 0.0039 | 0.6517 | 0.5762 | 0.537 | 0.3416 | 0.3664 | -0.053 ± 0.01 | -0.0255 (106) |
| 25-40 | 1418 | 0.2367 | 0.1564 | +0.0803 ± 0.0066 | 0.6702 | 0.4686 | 0.5796 | 0.2644 | 0.2962 | -0.061 ± 0.0102 | -0.0206 (47) |
| 40+ | 690 | 0.3533 | 0.1061 | +0.2472 ± 0.0133 | 0.966 | 0.3353 | 0.6727 | 0.167 | 0.1884 | -0.052 ± 0.0115 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 1698 | 1.14 ± 0.071 | 1.217 | 0.1689 | 0.1661 | 0.2077 | 0.2015 |
| gen2 | 1698 | 0.918 ± 0.062 | 1.144 | 0.1862 | 0.1656 | 0.2261 | 0.2016 |
| gen1_elo | 1698 | 1.113 ± 0.069 | 1.203 | 0.1727 | 0.1666 | 0.2068 | 0.2016 |
| gen1_sr | 1698 | 1.142 ± 0.081 | 1.229 | 0.1429 | 0.1681 | 0.2216 | 0.2015 |
| gen1_ledger | 3595 | 0.942 ± 0.044 | 1.091 | 0.169 | 0.1917 | 0.2157 | 0.1945 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 9,661)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,711 | 28.1% |
| STALE_QUOTE | market_freshness | 2,153 | 22.3% |
| BOOK_QUALITY | execution | 1,695 | 17.5% |
| POOR_DATA | data | 1,005 | 10.4% |
| LIMITED_DATA | data | 636 | 6.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 501 | 5.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 440 | 4.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 269 | 2.8% |
| IDENTITY_AMBIGUOUS | mapping | 231 | 2.4% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 20 | 0.2% |

Cause class: coverage 28.1%, market_freshness 22.3%, execution 17.5%, data 17.0%, market_freshness/coverage 8.0%, model_calibration_or_unknown 4.5%, mapping 2.4%, model_calibration 0.2%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.6%, START_UNVERIFIABLE 96.1%, LOW_DATA_QUALITY 69.1%, THIN_PLAYER_HISTORY 58.6%, STALE_PLAYER_DATA 58.1%, STALE_KALSHI_QUOTE 50.2%, MODEL_INTERNAL_DISAGREEMENT 37.4%, ASYMMETRIC_SAMPLE_SIZE 31.6%, WIDE_SPREAD 24.0%, MODEL_HIGH_UNCERTAINTY 15.8%, PLAYER_IDENTITY_RISK 10.5%, LEVEL_TRANSFER_RISK 8.5%, LOW_DISPLAYED_LIQUIDITY 7.3%, EVENT_MAPPING_RISK 7.0%, MODEL_CALIBRATION_OUTLIER 2.9%, UNKNOWN 0.5%, EXTERNAL_MARKET_REJECTION 0.4%, EXTERNAL_MARKET_CONFIRMATION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 30.4%, POST_SETTLEMENT_OBSERVATION 28.1%, POSSIBLE_IN_PLAY_QUOTE 5.6%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### >= ge_25 pp (N = 5,299)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,142 | 40.4% |
| STALE_QUOTE | market_freshness | 962 | 18.1% |
| BOOK_QUALITY | execution | 878 | 16.6% |
| POOR_DATA | data | 428 | 8.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 277 | 5.2% |
| LIMITED_DATA | data | 195 | 3.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 169 | 3.2% |
| IDENTITY_AMBIGUOUS | mapping | 133 | 2.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 106 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 9 | 0.2% |

Cause class: coverage 40.4%, market_freshness 18.1%, execution 16.6%, data 11.8%, market_freshness/coverage 8.4%, mapping 2.5%, model_calibration_or_unknown 2.0%, model_calibration 0.2%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.8%, START_UNVERIFIABLE 98.1%, LOW_DATA_QUALITY 71.5%, THIN_PLAYER_HISTORY 60.5%, STALE_KALSHI_QUOTE 57.8%, STALE_PLAYER_DATA 53.5%, MODEL_INTERNAL_DISAGREEMENT 39.5%, ASYMMETRIC_SAMPLE_SIZE 33.8%, WIDE_SPREAD 23.0%, MODEL_HIGH_UNCERTAINTY 17.1%, PLAYER_IDENTITY_RISK 13.0%, EVENT_MAPPING_RISK 7.9%, LOW_DISPLAYED_LIQUIDITY 7.7%, LEVEL_TRANSFER_RISK 7.3%, MODEL_CALIBRATION_OUTLIER 3.5%, EXTERNAL_MARKET_REJECTION 0.2%, UNKNOWN 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 43.1%, POST_SETTLEMENT_OBSERVATION 40.4%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.7%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 4455, "IDENTITY_AMBIGUOUS": 844}; ticker orientation: {"VERIFIED": 5299}.

Checks: discipline:AMBIGUOUS 266, discipline:PASS 5033, identity_confidence:AMBIGUOUS 691, identity_confidence:PASS 4608, level_mapping:NA 278, level_mapping:PASS 5021, market_pair:AMBIGUOUS 192, market_pair:NA 123, market_pair:PASS 4984, model_complement:NA 91, model_complement:PASS 5208, namesake:PASS 5299, physical_match_id:NA 2191, physical_match_id:PASS 3108, player_ids:PASS 5299, same_pair_other_event:PASS 5299, ticker_orientation:PASS 5299

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,264 | 1.8% | 1.8% | 0.4% | {"market_freshness": 20, "execution": 3} | 5.67 | 0.2039 / 0.2 (105) | 22.1% | 0.2% | 6.2% | 1.5% |
| CHALLENGER | 3,503 | 19.5% | 6.6% | 12.9% | {"coverage": 427, "market_freshness": 107, "market_freshness/coverage": 81, "model_calibration_or_unknown": 37, "data": 25, "execution": 4, "model_calibration": 2} | 6.92 | 0.223 / 0.2047 (844) | 48.0% | 5.1% | 1.5% | 24.4% |
| DOUBLES | 595 | 44.7% | 44.0% | 5.0% | {"market_freshness": 106, "execution": 81, "mapping": 51, "market_freshness/coverage": 21, "coverage": 7} | 22.7 | 0.3105 / 0.2241 (194) | 39.3% | 0.0% | 100.0% | 9.1% |
| ITF_MEN | 6,977 | 24.9% | 16.8% | 32.8% | {"coverage": 710, "execution": 378, "market_freshness": 257, "data": 234, "market_freshness/coverage": 138, "mapping": 19, "model_calibration_or_unknown": 1} | 10.89 | 0.2127 / 0.1926 (1769) | 40.2% | 55.9% | 6.4% | 24.1% |
| ITF_WOMEN | 8,938 | 26.6% | 18.2% | 44.9% | {"coverage": 981, "market_freshness": 415, "execution": 395, "data": 340, "market_freshness/coverage": 165, "mapping": 57, "model_calibration_or_unknown": 22, "model_calibration": 6} | 12.15 | 0.2009 / 0.1932 (1925) | 41.5% | 59.6% | 10.3% | 24.0% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 962 | 8.2% | 7.1% | 1.5% | {"market_freshness": 34, "model_calibration_or_unknown": 16, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.33 | 0.2008 / 0.1978 (145) | 34.6% | 2.2% | 1.2% | 3.4% |
| WTA125 | 774 | 15.2% | 11.0% | 2.2% | {"market_freshness/coverage": 31, "model_calibration_or_unknown": 28, "market_freshness": 21, "data": 13, "coverage": 12, "execution": 8, "mapping": 4, "model_calibration": 1} | 9.98 | 0.2242 / 0.2098 (269) | 27.5% | 5.6% | 4.1% | 12.1% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 5 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 207 min (STALE); no external reference |
| 6 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 7 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 8 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 9 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 10 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 11 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 12 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 14 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 16 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 17 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 874 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 18 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 19 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 20 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 21 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 22 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 23 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 24 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 25 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 26 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 189 min (STALE); no external reference |
| 27 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 28 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 29 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 110 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 30 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 31 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 32 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 253 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 33 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 34 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 22 min (AGING); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 35 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 36 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 37 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 230 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 38 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 114 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 39 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 40 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 41 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 42 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 708 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 43 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 44 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 45 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 46 | `KXATPCHALLENGERMATCH-26OCT06BARSAM-SAM` | CHALLENGER | fair_v1 | 84% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 710 min (STALE); no external reference |
| 47 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.9h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 671 min (STALE); no external reference |
| 49 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 407 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 50 | `KXWTAMATCH-26OCT01YASCHW-CHW` | WTA | fair_v1 | 73% / 2% | +70 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 51 min (STALE); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9808, "by_level_share_of_ge_25pp": {"ATP": 0.0043, "CHALLENGER": 0.1289, "DOUBLES": 0.0502, "ITF_MEN": 0.3278, "ITF_WOMEN": 0.4493, "OTHER": 0.0023, "WTA": 0.0149, "WTA125": 0.0223}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5784, "share_primary_cause_market_settled_or_in_play": 0.4884, "share_primary_cause_stale_quote_only": 0.1815}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 5299, "identity_ambiguous_share": 0.1593, "ticker_orientation": {"VERIFIED": 5299}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 3108, "with_external": 43, "coverage": 0.0138, "external_status": {"EXTERNAL_STALE": 34, "AGREES_WITH_KALSHI": 9}, "triangulation": {"INSUFFICIENT_INPUTS": 34, "MODEL_LONE_OUTLIER": 9}, "share_external_agrees_with_kalshi": 0.2093, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 1358, "with_external": 42, "coverage": 0.0309, "external_status": {"EXTERNAL_STALE": 33, "AGREES_WITH_KALSHI": 9}, "triangulation": {"INSUFFICIENT_INPUTS": 33, "MODEL_LONE_OUTLIER": 9}, "share_external_agrees_with_kalshi": 0.2143, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 604.0, "median_sample_ratio": 2.35, "median_min_matches": 19.0, "median_max_days_since_last": 197.0, "share_severe_asymmetry": 0.1817, "data_status": {"POOR": 2822, "LIMITED": 1510, "ADEQUATE": 967}, "comparison_lt_10pp": {"median_thinner_serve_points": 1702.0, "median_sample_ratio": 1.77, "median_min_matches": 71.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 374, "model_minus_observed": 0.0697, "kalshi_minus_observed": -0.0626, "brier_diff_model_minus_kalshi": 0.0019}, "4-10x": {"n": 277, "model_minus_observed": 0.0528, "kalshi_minus_observed": -0.0883, "brier_diff_model_minus_kalshi": -0.0054}, "<2x": {"n": 791, "model_minus_observed": 0.0851, "kalshi_minus_observed": -0.0424, "brier_diff_model_minus_kalshi": 0.0106}, ">=10x": {"n": 256, "model_minus_observed": 0.0983, "kalshi_minus_observed": -0.0768, "brier_diff_model_minus_kalshi": 0.0115}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 1698, "model": {"intercept": -0.578, "slope": 0.918, "slope_se": 0.062}, "kalshi_mid_same_rows": {"intercept": 0.238, "slope": 1.144, "slope_se": 0.071}, "mean_extremity_model": 0.1862, "mean_extremity_kalshi": 0.1656, "model_brier": 0.2261, "kalshi_brier": 0.2016, "brier_diff_model_minus_kalshi": 0.0246, "brier_diff_se": 0.0046, "model_logloss": 0.6459, "kalshi_logloss": 0.5857}, "fair_v1": {"n": 1698, "model": {"intercept": -0.413, "slope": 1.14, "slope_se": 0.071}, "kalshi_mid_same_rows": {"intercept": 0.359, "slope": 1.217, "slope_se": 0.074}, "mean_extremity_model": 0.1689, "mean_extremity_kalshi": 0.1661, "model_brier": 0.2077, "kalshi_brier": 0.2015, "brier_diff_model_minus_kalshi": 0.0062, "brier_diff_se": 0.0037, "model_logloss": 0.6013, "kalshi_logloss": 0.5854}, "gen1_elo": {"n": 1698, "model": {"intercept": -0.379, "slope": 1.113, "slope_se": 0.069}, "kalshi_mid_same_rows": {"intercept": 0.367, "slope": 1.203, "slope_se": 0.072}, "mean_extremity_model": 0.1727, "mean_extremity_kalshi": 0.1666, "model_brier": 0.2068, "kalshi_brier": 0.2016, "brier_diff_model_minus_kalshi": 0.0052, "brier_diff_se": 0.0037, "model_logloss": 0.6006, "kalshi_logloss": 0.5855}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2562, "share_ge_15": 0.4416, "median_abs_gap": 13.12, "n": 12131}, "gen1_elo": {"share_ge_25": 0.246, "share_ge_15": 0.4401, "median_abs_gap": 12.74, "n": 12131}, "gen1_sr": {"share_ge_25": 0.3075, "share_ge_15": 0.5235, "median_abs_gap": 15.87, "n": 12131}, "gen2": {"share_ge_25": 0.3114, "share_ge_15": 0.5102, "median_abs_gap": 15.46, "n": 12131}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1486, "share_ge_15": 0.3401, "median_abs_gap": 10.48, "n": 9140}, "gen1_elo": {"share_ge_25": 0.1428, "share_ge_15": 0.3357, "median_abs_gap": 10.05, "n": 9139}, "gen1_sr": {"share_ge_25": 0.2015, "share_ge_15": 0.4328, "median_abs_gap": 12.92, "n": 9140}, "gen2": {"share_ge_25": 0.22, "share_ge_15": 0.4304, "median_abs_gap": 12.74, "n": 9141}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.67, "share_ge_25_all": 0.0182, "share_ge_25_pregame_clean": 0.0185}, "WTA": {"median_abs_gap_pregame_clean": 8.33, "share_ge_25_all": 0.0821, "share_ge_25_pregame_clean": 0.071}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2317, "share_within_10pp_all": 0.4297, "share_within_10pp_pregame_clean": 0.4952, "corr_model_vs_mid_pregame_clean": 0.85}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 247, "model_brier": 0.1792, "kalshi_brier": 0.1803, "brier_diff_model_minus_kalshi": -0.0011}, "10-15": {"n_settled": 297, "model_brier": 0.2203, "kalshi_brier": 0.2182, "brier_diff_model_minus_kalshi": 0.0021}, "15-25": {"n_settled": 369, "model_brier": 0.2197, "kalshi_brier": 0.2112, "brier_diff_model_minus_kalshi": 0.0085}, "25-40": {"n_settled": 216, "model_brier": 0.215, "kalshi_brier": 0.2038, "brier_diff_model_minus_kalshi": 0.0112}, "3-5": {"n_settled": 169, "model_brier": 0.1834, "kalshi_brier": 0.1835, "brier_diff_model_minus_kalshi": -0.0001}, "40+": {"n_settled": 49, "model_brier": 0.2835, "kalshi_brier": 0.1763, "brier_diff_model_minus_kalshi": 0.1072}, "5-10": {"n_settled": 351, "model_brier": 0.2014, "kalshi_brier": 0.2031, "brier_diff_model_minus_kalshi": -0.0017}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%)
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap).
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 194, "model_brier": 0.3105, "kalshi_brier": 0.2241, "brier_diff_model_minus_kalshi": 0.0864, "brier_diff_se": 0.0227, "corr_model_outcome": 0.0137, "corr_kalshi_outcome": 0.3509}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
