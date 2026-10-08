# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-08T06:40Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 24,074): 0-3 13.9%, 3-5 9.6%, 5-10 19.9%, 10-15 15.4%, 15-25 18.7%, 25-40 14.2%, 40+ 8.4%; median gap 12.02 pp.
* **Where the extremes live**: 98.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.5%, Challenger 12.7%, doubles 5.5%). Main tour: ATP 1.8% and WTA 8.1% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 5,419): MARKET_ALREADY_SETTLED_WHEN_PRICED 39.7%, STALE_QUOTE 17.9%, BOOK_QUALITY 16.8%, POOR_DATA 8.2%, POSSIBLY_IN_PLAY_QUOTE 5.2%, LIMITED_DATA 4.1%, IN_PLAY_QUOTE 3.2%, IDENTITY_AMBIGUOUS 2.8%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.2%. By class: coverage 39.7%, market_freshness 17.9%, execution 16.8%, data 12.3%, market_freshness/coverage 8.4%, mapping 2.8%, model_calibration_or_unknown 2.0%, model_calibration 0.2%.
* **Stale / settled / in-play**: 56.9% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 48.1% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 5,419 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 16.3% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 1.6%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 11.4% of the time and with the model 0.3%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 605.0 points vs 1709.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.12, Gen-2 0.899, Gen-1 ledger 0.936 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 221 model 0.2183 vs Kalshi 0.2041; n 51 model 0.2726 vs Kalshi 0.1802.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%). Not implemented here.

## 1. Observations

* 89,744 model-market comparisons (150,988 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 33,963 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-08T06:35:40.351214+00:00'], shadow board 25,058 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-08T06:35:43.537600+00:00'], Model 4 9,086 rows, 10,486 settled tickers, 2,857 tickers with an external scan.
* By model: {"gen1_ledger": 21467, "gen1_elo": 12590, "fair_v1": 12590, "gen2": 12590, "gen1_sr": 12590, "model4_fundamental": 8963, "model4_conditioned": 8954}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 24,074 | 13.9 | 9.6 | 19.9 | 15.4 | 18.7 | 14.2 | 8.4 | 12.02 | 41.2% | 22.5% |
| MW fair_v1 | 12,590 | 13.1 | 8.8 | 18.4 | 16.1 | 18.5 | 15.1 | 10.1 | 13.0 | 43.6% | 25.1% |
| MW gen1_elo | 12,590 | 12.8 | 8.8 | 19.9 | 15.0 | 19.3 | 14.7 | 9.5 | 12.54 | 43.5% | 24.2% |
| MW gen1_ledger | 11,484 | 14.8 | 10.5 | 21.6 | 14.6 | 18.9 | 13.2 | 6.5 | 10.87 | 38.5% | 19.6% |
| MW gen1_sr | 12,590 | 10.2 | 7.8 | 16.0 | 14.2 | 21.5 | 18.6 | 11.8 | 15.64 | 51.9% | 30.4% |
| MW gen2 | 12,590 | 11.9 | 7.1 | 16.0 | 14.3 | 19.9 | 17.5 | 13.2 | 15.32 | 50.6% | 30.7% |
| all families model4_conditioned | 8,954 | 22.0 | 20.6 | 35.4 | 16.0 | 4.4 | 0.8 | 0.8 | 5.7 | 6.0% | 1.6% |
| all families model4_fundamental | 8,963 | 16.4 | 13.3 | 34.8 | 20.4 | 10.9 | 3.0 | 1.1 | 7.79 | 15.0% | 4.1% |

Configurable thresholds (primary): >=5pp 76.5%, >=10pp 56.6%, >=15pp 41.2%, >=20pp 30.8%, >=25pp 22.5%, >=30pp 16.4%, >=40pp 8.4%, >=50pp 3.6%
Executable gap (model outside the book, before fees): median 8.48pp; >=10pp 45.6%, >=25pp 18.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 895 | 25.9 | 16.2 | 24.1 | 17.9 | 13.3 | 1.3 | 1.2 | 6.01 | 15.9% | 2.6% |
| CHALLENGER | 2,183 | 14.8 | 11.0 | 18.5 | 16.1 | 13.1 | 13.4 | 13.1 | 11.98 | 39.6% | 26.5% |
| ITF_MEN | 3,630 | 11.1 | 8.6 | 18.8 | 14.7 | 19.4 | 15.0 | 12.4 | 13.79 | 46.9% | 27.4% |
| ITF_WOMEN | 5,036 | 10.5 | 6.8 | 16.1 | 16.1 | 21.5 | 19.1 | 9.9 | 15.23 | 50.5% | 29.0% |
| WTA | 534 | 23.6 | 9.6 | 25.1 | 16.3 | 17.2 | 6.2 | 2.1 | 8.12 | 25.5% | 8.2% |
| WTA125 | 312 | 12.2 | 6.7 | 21.1 | 26.0 | 14.7 | 16.7 | 2.6 | 11.33 | 34.0% | 19.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 895 | 21.7 | 14.3 | 24.0 | 18.9 | 17.3 | 2.4 | 1.4 | 6.9 | 21.1% | 3.8% |
| CHALLENGER | 2,183 | 15.0 | 7.5 | 17.7 | 13.4 | 18.3 | 14.6 | 13.5 | 13.3 | 46.4% | 28.0% |
| ITF_MEN | 3,630 | 10.7 | 7.4 | 16.7 | 14.7 | 19.8 | 17.6 | 13.1 | 15.33 | 50.5% | 30.7% |
| ITF_WOMEN | 5,036 | 9.1 | 6.0 | 12.9 | 13.2 | 20.9 | 21.3 | 16.6 | 18.87 | 58.8% | 37.9% |
| WTA | 534 | 22.1 | 5.1 | 18.2 | 15.2 | 21.2 | 16.3 | 2.1 | 12.38 | 39.5% | 18.4% |
| WTA125 | 312 | 4.8 | 2.9 | 17.0 | 22.4 | 20.5 | 20.2 | 12.2 | 16.79 | 52.9% | 32.4% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 895 | 26.3 | 11.4 | 29.8 | 16.6 | 11.2 | 3.4 | 1.3 | 6.85 | 15.9% | 4.7% |
| CHALLENGER | 2,183 | 15.7 | 10.9 | 19.6 | 14.1 | 14.1 | 12.5 | 13.1 | 10.98 | 39.6% | 25.6% |
| ITF_MEN | 3,630 | 10.0 | 8.9 | 18.6 | 14.2 | 20.5 | 15.4 | 12.5 | 14.18 | 48.4% | 27.9% |
| ITF_WOMEN | 5,036 | 9.7 | 6.7 | 17.0 | 15.6 | 23.5 | 18.9 | 8.6 | 15.46 | 51.0% | 27.5% |
| WTA | 534 | 22.9 | 13.1 | 35.2 | 14.6 | 9.4 | 3.6 | 1.3 | 6.99 | 14.2% | 4.9% |
| WTA125 | 312 | 21.1 | 11.9 | 28.9 | 17.3 | 15.1 | 5.1 | 0.6 | 7.84 | 20.8% | 5.8% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 433 | 28.4 | 21.2 | 37.2 | 11.3 | 1.6 | 0.2 | 0.0 | 5.03 | 1.8% | 0.2% |
| CHALLENGER | 1,407 | 23.0 | 16.8 | 26.1 | 14.1 | 12.3 | 5.5 | 2.1 | 6.71 | 19.9% | 7.6% |
| DOUBLES | 642 | 4.2 | 3.6 | 12.3 | 11.5 | 21.8 | 23.7 | 22.9 | 23.58 | 68.4% | 46.6% |
| ITF_MEN | 3,655 | 14.3 | 8.8 | 20.6 | 15.1 | 20.3 | 12.8 | 8.1 | 11.92 | 41.2% | 20.9% |
| ITF_WOMEN | 4,277 | 11.8 | 9.4 | 19.9 | 14.2 | 21.8 | 17.0 | 5.8 | 12.95 | 44.7% | 22.9% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 439 | 20.3 | 11.6 | 25.7 | 18.9 | 15.5 | 7.3 | 0.7 | 8.46 | 23.5% | 8.0% |
| WTA125 | 482 | 16.2 | 12.7 | 22.2 | 19.7 | 17.2 | 9.1 | 2.9 | 9.64 | 29.2% | 12.0% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 891 | 25.9 | 16.1 | 24.1 | 18.0 | 13.4 | 1.4 | 1.2 | 6.04 | 15.9% | 2.6% |
| CHALLENGER | 1,545 | 19.6 | 14.1 | 24.0 | 18.8 | 13.8 | 6.9 | 3.0 | 8.27 | 23.6% | 9.8% |
| ITF_MEN | 2,646 | 13.5 | 10.8 | 22.1 | 16.4 | 19.5 | 12.1 | 5.5 | 10.98 | 37.1% | 17.6% |
| ITF_WOMEN | 3,661 | 12.9 | 8.4 | 19.0 | 18.6 | 23.1 | 15.2 | 2.9 | 12.61 | 41.1% | 18.1% |
| WTA | 531 | 23.5 | 9.6 | 25.2 | 16.2 | 17.3 | 6.0 | 2.1 | 8.09 | 25.4% | 8.1% |
| WTA125 | 301 | 12.6 | 7.0 | 20.9 | 26.2 | 14.9 | 16.6 | 1.7 | 11.31 | 33.2% | 18.3% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 891 | 21.6 | 14.2 | 24.1 | 18.9 | 17.4 | 2.4 | 1.5 | 6.91 | 21.2% | 3.8% |
| CHALLENGER | 1,545 | 19.8 | 9.8 | 22.5 | 16.4 | 18.7 | 10.0 | 2.9 | 9.5 | 31.5% | 12.8% |
| ITF_MEN | 2,647 | 12.7 | 8.8 | 19.4 | 16.7 | 21.0 | 15.2 | 6.3 | 12.56 | 42.4% | 21.4% |
| ITF_WOMEN | 3,661 | 10.6 | 7.2 | 14.9 | 14.4 | 22.9 | 19.9 | 10.1 | 16.08 | 52.9% | 30.0% |
| WTA | 531 | 22.0 | 5.1 | 18.3 | 15.2 | 21.1 | 16.2 | 2.1 | 12.38 | 39.4% | 18.3% |
| WTA125 | 301 | 5.0 | 3.0 | 17.3 | 23.3 | 19.6 | 20.9 | 11.0 | 16.14 | 51.5% | 31.9% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 418 | 28.7 | 21.5 | 37.3 | 11.5 | 0.7 | 0.2 | 0.0 | 4.99 | 1.0% | 0.2% |
| CHALLENGER | 1,189 | 24.9 | 19.1 | 28.4 | 13.8 | 11.6 | 2.1 | 0.1 | 6.01 | 13.8% | 2.2% |
| DOUBLES | 588 | 4.2 | 3.6 | 12.6 | 11.4 | 22.1 | 23.5 | 22.6 | 23.51 | 68.2% | 46.1% |
| ITF_MEN | 2,949 | 16.1 | 9.8 | 23.0 | 16.1 | 20.0 | 10.4 | 4.7 | 10.26 | 35.1% | 15.1% |
| ITF_WOMEN | 3,478 | 13.2 | 10.2 | 21.8 | 15.1 | 22.0 | 15.3 | 2.4 | 11.34 | 39.7% | 17.7% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 409 | 20.8 | 12.2 | 26.4 | 19.1 | 15.9 | 5.6 | 0.0 | 8.4 | 21.5% | 5.6% |
| WTA125 | 399 | 18.3 | 14.0 | 24.8 | 22.6 | 15.3 | 4.8 | 0.2 | 8.3 | 20.3% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 642 | 4.2 | 3.6 | 12.3 | 11.5 | 21.8 | 23.7 | 22.9 | 23.58 | 68.4% | 46.6% |
| singles | 10,842 | 15.4 | 10.9 | 22.2 | 14.8 | 18.7 | 12.5 | 5.5 | 10.39 | 36.7% | 18.1% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 2,939 | 13.2 | 9.7 | 20.4 | 15.5 | 15.9 | 14.7 | 10.7 | 12.19 | 41.2% | 25.3% |
| Hard | 8,452 | 13.2 | 8.6 | 18.2 | 16.0 | 19.2 | 14.9 | 9.9 | 13.11 | 44.0% | 24.8% |
| UNKNOWN | 1,199 | 12.1 | 8.5 | 14.5 | 18.1 | 20.1 | 17.3 | 9.4 | 13.98 | 46.8% | 26.7% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,607 | 18.2 | 11.2 | 20.4 | 17.0 | 15.0 | 9.9 | 8.2 | 10.03 | 33.2% | 18.2% |
| B | 1,605 | 15.3 | 9.9 | 19.8 | 17.2 | 16.2 | 11.8 | 9.8 | 11.12 | 37.8% | 21.6% |
| C | 1,967 | 12.8 | 9.9 | 20.3 | 15.2 | 18.4 | 14.2 | 9.2 | 12.54 | 41.9% | 23.5% |
| D | 2,407 | 11.3 | 8.6 | 17.1 | 16.2 | 22.5 | 15.1 | 9.2 | 13.98 | 46.8% | 24.3% |
| F | 3,004 | 7.4 | 4.9 | 15.0 | 14.8 | 20.8 | 23.4 | 13.7 | 18.45 | 57.9% | 37.0% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,109 | 21.3 | 15.2 | 27.4 | 15.8 | 12.8 | 5.3 | 2.1 | 7.19 | 20.2% | 7.4% |
| B | 1,798 | 14.7 | 10.0 | 24.7 | 16.2 | 17.8 | 11.6 | 5.0 | 10.15 | 34.4% | 16.6% |
| C | 2,301 | 12.3 | 8.4 | 19.2 | 14.2 | 20.8 | 15.2 | 9.9 | 13.18 | 45.9% | 25.1% |
| D | 1,953 | 13.7 | 9.1 | 21.2 | 13.1 | 22.1 | 14.5 | 6.2 | 12.14 | 42.9% | 20.8% |
| F | 2,323 | 9.3 | 7.9 | 14.2 | 13.5 | 23.1 | 21.6 | 10.4 | 16.91 | 55.1% | 32.0% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 4,077 | 17.2 | 10.4 | 19.6 | 17.2 | 15.2 | 10.3 | 10.1 | 10.8 | 35.6% | 20.4% |
| LIMITED | 3,063 | 14.6 | 10.7 | 21.2 | 15.6 | 17.4 | 13.2 | 7.2 | 11.02 | 37.9% | 20.4% |
| POOR | 5,450 | 9.2 | 6.6 | 15.9 | 15.5 | 21.6 | 19.6 | 11.6 | 16.07 | 52.8% | 31.3% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,801 | 29.8 | 26.0 | 36.8 | 5.5 | 1.7 | 0.3 | 0.0 | 4.47 | 1.9% | 0.3% |
| GAME_SPREAD | 1,877 | 24.4 | 15.3 | 36.9 | 18.5 | 4.5 | 0.3 | 0.2 | 6.18 | 4.9% | 0.4% |
| MATCH_WINNER | 11,484 | 14.8 | 10.5 | 21.6 | 14.6 | 18.9 | 13.2 | 6.5 | 10.87 | 38.5% | 19.6% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 3,466 | 29.6 | 19.1 | 31.2 | 11.2 | 7.2 | 1.4 | 0.3 | 5.14 | 8.9% | 1.7% |
| TOTAL_GAMES | 2,815 | 7.4 | 9.2 | 38.3 | 29.8 | 9.7 | 3.3 | 2.3 | 9.45 | 15.2% | 5.5% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,292 | 24.0 | 39.7 | 29.8 | 0.3 | 5.4 | 0.5 | 0.2 | 4.34 | 6.1% | 0.7% |
| GAME_SPREAD | 2,292 | 46.3 | 14.3 | 29.3 | 8.3 | 1.1 | 0.5 | 0.2 | 3.47 | 1.8% | 0.7% |
| TOTAL_GAMES | 3,370 | 3.4 | 6.3 | 44.9 | 36.6 | 5.7 | 1.4 | 1.7 | 9.59 | 8.8% | 3.1% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,292 | 25.3 | 18.3 | 35.7 | 10.1 | 7.2 | 2.9 | 0.5 | 5.63 | 10.6% | 3.4% |
| GAME_SPREAD | 2,292 | 19.1 | 13.1 | 26.5 | 23.1 | 14.6 | 2.9 | 0.7 | 8.39 | 18.1% | 3.5% |
| TOTAL_GAMES | 3,379 | 5.8 | 8.6 | 39.5 | 28.8 | 12.1 | 3.1 | 2.0 | 9.58 | 17.2% | 5.2% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 12,590 | 43.6% | 25.1% | 13.0 | 33.7% | 14.6% | 10.45 |
| gen1_elo | 12,590 | 43.5% | 24.2% | 12.54 | 33.3% | 14.1% | 10.01 |
| gen1_sr | 12,590 | 51.9% | 30.4% | 15.64 | 43.0% | 20.1% | 12.81 |
| gen2 | 12,590 | 50.6% | 30.7% | 15.32 | 42.8% | 21.8% | 12.67 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 6,230 | 15.9 | 11.2 | 21.5 | 17.5 | 18.7 | 11.9 | 3.4 | 10.36 | 34.0% | 15.3% |
| STALE | 6,360 | 10.4 | 6.5 | 15.3 | 14.7 | 18.3 | 18.2 | 16.6 | 16.7 | 53.1% | 34.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 4,952 | 16.9 | 11.8 | 24.1 | 14.4 | 16.7 | 11.8 | 4.2 | 9.24 | 32.8% | 16.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 24,074 | 4952 | 9702 | 9420 | 25.5 | 164.2 | 1400.4 |
| ge_15pp | 9,915 | 1623 | 3404 | 4888 | 29.4 | 453.4 | 1380.4 |
| ge_25pp | 5,419 | 794 | 1542 | 3083 | 39.2 | 570.4 | 1380.4 |
| lt_10pp | 10,456 | 2614 | 4658 | 3184 | 24.0 | 51.7 | 1230.8 |

Current slate `SL-20261008T064050Z-13bf9c90`: 657 priced rows, quote age at build {'median': 5.5, 'max': 5.6}, freshness {'FRESH': 657}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 2 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.87 | 100.0% | 0.0% |
| EXTERNAL_LONE_OUTLIER | 3 | 33.3 | 66.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 3.05 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 563 | 21.7 | 11.9 | 21.5 | 20.6 | 16.9 | 7.1 | 0.4 | 8.38 | 24.3% | 7.5% |
| MARKETS_AGREE | 44 | 77.3 | 22.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.12 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 79 | 0.0 | 2.5 | 29.1 | 32.9 | 24.1 | 11.4 | 0.0 | 11.66 | 35.4% | 11.4% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 12,590 | 691 (5.5%) | 11.4% | 0.3% | {"EXTERNAL_STALE": 563, "AGREES_WITH_KALSHI": 79, "ALL_AGREE": 44, "EXTERNAL_OUTLIER": 3, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_ge_15pp | 5,493 | 167 (3.0%) | 16.8% | 1.2% | {"EXTERNAL_STALE": 137, "AGREES_WITH_KALSHI": 28, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_ge_25pp | 3,163 | 51 (1.6%) | 17.6% | 0.0% | {"EXTERNAL_STALE": 42, "AGREES_WITH_KALSHI": 9} |
| fair_v1_ge_25pp_pregame_clean | 1,401 | 50 (3.6%) | 18.0% | 0.0% | {"EXTERNAL_STALE": 41, "AGREES_WITH_KALSHI": 9} |
| fair_v1_lt_10pp | 5,073 | 382 (7.5%) | 6.5% | 0.0% | {"EXTERNAL_STALE": 310, "ALL_AGREE": 44, "AGREES_WITH_KALSHI": 25, "EXTERNAL_OUTLIER": 3} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 2,554 | 11.5 | 8.6 | 20.2 | 15.7 | 20.9 | 14.0 | 9.1 | 12.75 | 44.0% | 23.1% |
| 4-10x | 1,838 | 11.4 | 9.3 | 17.9 | 14.5 | 20.6 | 17.1 | 9.1 | 14.04 | 46.8% | 26.3% |
| <2x | 6,563 | 14.9 | 9.4 | 18.4 | 17.0 | 16.9 | 13.4 | 10.0 | 12.17 | 40.4% | 23.4% |
| >=10x | 1,635 | 10.3 | 6.2 | 16.0 | 14.7 | 18.8 | 21.0 | 12.8 | 16.17 | 52.7% | 33.8% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 3,216 | 14.1 | 8.8 | 20.1 | 15.8 | 17.5 | 12.9 | 10.8 | 12.07 | 41.2% | 23.7% |
| 300-1000 | 3,102 | 12.2 | 9.3 | 16.7 | 16.0 | 21.2 | 16.0 | 8.5 | 13.67 | 45.7% | 24.5% |
| <300 | 3,488 | 8.0 | 6.0 | 15.7 | 15.0 | 20.8 | 21.4 | 13.2 | 17.2 | 55.3% | 34.6% |
| >=3000 | 2,784 | 19.2 | 11.9 | 21.6 | 17.8 | 13.8 | 8.7 | 7.0 | 9.31 | 29.4% | 15.6% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 386 | 0.5408 | 0.4085 | 0.4715 | +0.069 | -0.063 | 0.0045 ± 0.0074 |
| ratio 4-10x | 279 | 0.5892 | 0.4466 | 0.5376 | +0.051 | -0.091 | -0.0069 ± 0.0093 |
| ratio <2x | 802 | 0.5434 | 0.4157 | 0.4601 | +0.083 | -0.044 | 0.0099 ± 0.0052 |
| ratio >=10x | 261 | 0.5635 | 0.3876 | 0.4636 | +0.100 | -0.076 | 0.0115 ± 0.0114 |
| thinner_sample 1000-3000 | 454 | 0.5471 | 0.4202 | 0.4604 | +0.087 | -0.040 | 0.0064 ± 0.0068 |
| thinner_sample 300-1000 | 480 | 0.575 | 0.4337 | 0.5042 | +0.071 | -0.070 | -0.001 ± 0.0072 |
| thinner_sample <300 | 548 | 0.5523 | 0.3894 | 0.4799 | +0.072 | -0.090 | 0.0074 ± 0.0074 |
| thinner_sample >=3000 | 246 | 0.5242 | 0.4248 | 0.439 | +0.085 | -0.014 | 0.0175 ± 0.0075 |
| data_status ADEQUATE | 455 | 0.529 | 0.4221 | 0.4396 | +0.089 | -0.018 | 0.012 ± 0.0059 |
| data_status LIMITED | 419 | 0.5679 | 0.4319 | 0.4964 | +0.071 | -0.065 | 0.0004 ± 0.0075 |
| data_status POOR | 854 | 0.559 | 0.4026 | 0.4848 | +0.074 | -0.082 | 0.0061 ± 0.0058 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 249 | 0.1803 | 0.1813 | -0.0011 ± 0.0009 | 0.5343 | 0.537 | 0.4935 | 0.4791 | 0.51 | -0.086 ± 0.0285 | -0.01 (3) |
| 3-5 | 173 | 0.1872 | 0.1881 | -0.0009 ± 0.0027 | 0.5541 | 0.5535 | 0.5072 | 0.4673 | 0.4913 | -0.079 ± 0.0337 | 0.02 (1) |
| 5-10 | 356 | 0.2004 | 0.2026 | -0.0022 ± 0.0036 | 0.587 | 0.5931 | 0.5201 | 0.4463 | 0.4888 | -0.093 ± 0.0249 | -0.0125 (4) |
| 10-15 | 301 | 0.2199 | 0.2179 | +0.0019 ± 0.0067 | 0.6284 | 0.62 | 0.5334 | 0.4093 | 0.4618 | -0.091 ± 0.027 | -0.0633 (3) |
| 15-25 | 377 | 0.2201 | 0.2105 | +0.0095 ± 0.0092 | 0.6309 | 0.6087 | 0.5746 | 0.3789 | 0.4509 | -0.085 ± 0.0237 | -0.018 (5) |
| 25-40 | 221 | 0.2183 | 0.2041 | +0.0141 ± 0.0181 | 0.6267 | 0.5847 | 0.6535 | 0.3436 | 0.4751 | -0.075 ± 0.0271 | -0.01 (1) |
| 40+ | 51 | 0.2726 | 0.1802 | +0.0924 ± 0.0517 | 0.742 | 0.5366 | 0.757 | 0.311 | 0.4314 | -0.112 ± 0.051 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1149 | 0.1638 | 0.1642 | -0.0004 ± 0.0004 | 0.4938 | 0.494 | 0.4781 | 0.4633 | 0.497 | -0.035 ± 0.0122 | -0.0188 (8) |
| 3-5 | 828 | 0.192 | 0.1871 | +0.0049 ± 0.0012 | 0.5666 | 0.5494 | 0.4781 | 0.4386 | 0.3925 | -0.110 ± 0.0152 | 0.02 (1) |
| 5-10 | 1770 | 0.192 | 0.1909 | +0.0011 ± 0.0016 | 0.5669 | 0.563 | 0.4899 | 0.4161 | 0.4418 | -0.049 ± 0.0105 | -0.0082 (17) |
| 10-15 | 1546 | 0.2044 | 0.1894 | +0.0150 ± 0.0028 | 0.5951 | 0.5531 | 0.4774 | 0.3526 | 0.3558 | -0.072 ± 0.0111 | -0.0633 (3) |
| 15-25 | 1896 | 0.1976 | 0.1629 | +0.0347 ± 0.0036 | 0.5839 | 0.4864 | 0.4897 | 0.2932 | 0.3038 | -0.070 ± 0.0093 | -0.0115 (20) |
| 25-40 | 1678 | 0.2156 | 0.1266 | +0.0890 ± 0.0054 | 0.6232 | 0.3898 | 0.5295 | 0.216 | 0.233 | -0.056 ± 0.0084 | -0.01 (1) |
| 40+ | 1158 | 0.3654 | 0.0471 | +0.3184 ± 0.0071 | 0.9536 | 0.1822 | 0.6209 | 0.1063 | 0.0648 | -0.077 ± 0.0059 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 194 | 0.1952 | 0.1954 | -0.0003 ± 0.0011 | 0.5738 | 0.5741 | 0.4941 | 0.4791 | 0.4742 | -0.119 ± 0.0333 | -0.01 (1) |
| 3-5 | 128 | 0.2106 | 0.2102 | +0.0004 ± 0.0033 | 0.6021 | 0.6039 | 0.5097 | 0.4698 | 0.4766 | -0.085 ± 0.0432 | 0.02 (1) |
| 5-10 | 300 | 0.1923 | 0.1902 | +0.0021 ± 0.0038 | 0.5676 | 0.5626 | 0.5632 | 0.4878 | 0.5067 | -0.098 ± 0.0261 | -0.01 (4) |
| 10-15 | 295 | 0.2195 | 0.2096 | +0.0099 ± 0.0067 | 0.6258 | 0.6064 | 0.5869 | 0.4624 | 0.4915 | -0.115 ± 0.0278 | -0.05 (4) |
| 15-25 | 418 | 0.2211 | 0.2055 | +0.0156 ± 0.0088 | 0.6289 | 0.5919 | 0.6014 | 0.4036 | 0.4689 | -0.102 ± 0.0229 | -0.015 (4) |
| 25-40 | 285 | 0.2653 | 0.2052 | +0.0602 ± 0.0168 | 0.7423 | 0.5922 | 0.6735 | 0.3605 | 0.4211 | -0.135 ± 0.027 | -0.025 (2) |
| 40+ | 108 | 0.339 | 0.1934 | +0.1456 ± 0.041 | 0.9582 | 0.5631 | 0.7658 | 0.284 | 0.3889 | -0.059 ± 0.0391 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1088 | 0.175 | 0.1758 | -0.0008 ± 0.0004 | 0.5223 | 0.5245 | 0.4965 | 0.4823 | 0.5101 | -0.036 ± 0.0133 | -0.0217 (6) |
| 3-5 | 677 | 0.1901 | 0.1863 | +0.0038 ± 0.0013 | 0.5517 | 0.5437 | 0.5198 | 0.4798 | 0.4535 | -0.081 ± 0.0168 | 0.02 (1) |
| 5-10 | 1515 | 0.1823 | 0.1799 | +0.0024 ± 0.0016 | 0.5475 | 0.5369 | 0.5132 | 0.4392 | 0.4587 | -0.050 ± 0.0111 | -0.01 (5) |
| 10-15 | 1374 | 0.1966 | 0.1832 | +0.0134 ± 0.0029 | 0.5813 | 0.5366 | 0.5231 | 0.399 | 0.4105 | -0.068 ± 0.0118 | -0.02 (14) |
| 15-25 | 2001 | 0.209 | 0.1702 | +0.0388 ± 0.0036 | 0.6115 | 0.505 | 0.5277 | 0.3325 | 0.3338 | -0.083 ± 0.0094 | -0.0094 (17) |
| 25-40 | 1874 | 0.2464 | 0.1391 | +0.1074 ± 0.0055 | 0.6978 | 0.4231 | 0.5626 | 0.2457 | 0.2359 | -0.087 ± 0.0087 | -0.015 (6) |
| 40+ | 1496 | 0.3992 | 0.0722 | +0.3270 ± 0.0079 | 1.046 | 0.2485 | 0.6704 | 0.1322 | 0.1116 | -0.062 ± 0.0067 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 259 | 0.1892 | 0.1915 | -0.0023 ± 0.001 | 0.5556 | 0.5621 | 0.5042 | 0.4891 | 0.5444 | -0.041 ± 0.0275 | -0.0133 (6) |
| 3-5 | 188 | 0.1842 | 0.1822 | +0.0020 ± 0.0025 | 0.5435 | 0.5387 | 0.4909 | 0.4515 | 0.4468 | -0.134 ± 0.0331 | -0.01 (1) |
| 5-10 | 360 | 0.1966 | 0.1981 | -0.0016 ± 0.0035 | 0.5788 | 0.5815 | 0.5156 | 0.442 | 0.4833 | -0.085 ± 0.0243 | -0.01 (3) |
| 10-15 | 283 | 0.2168 | 0.2159 | +0.0008 ± 0.0069 | 0.6243 | 0.6173 | 0.5434 | 0.4202 | 0.4806 | -0.091 ± 0.0272 | -0.044 (5) |
| 15-25 | 373 | 0.2255 | 0.2104 | +0.0150 ± 0.0093 | 0.6478 | 0.606 | 0.5843 | 0.3906 | 0.4477 | -0.101 ± 0.0236 | -0.03 (1) |
| 25-40 | 220 | 0.2037 | 0.2099 | -0.0061 ± 0.0179 | 0.592 | 0.6001 | 0.6586 | 0.3471 | 0.5091 | -0.055 ± 0.0263 | 0.0 (1) |
| 40+ | 45 | 0.2966 | 0.1799 | +0.1167 ± 0.0563 | 0.7985 | 0.5355 | 0.7496 | 0.2982 | 0.4 | -0.122 ± 0.0568 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1149 | 0.1777 | 0.1789 | -0.0012 ± 0.0004 | 0.5269 | 0.5298 | 0.4902 | 0.475 | 0.5135 | -0.026 ± 0.0125 | -0.0183 (23) |
| 3-5 | 853 | 0.1862 | 0.1831 | +0.0032 ± 0.0012 | 0.549 | 0.5422 | 0.4726 | 0.4332 | 0.4127 | -0.093 ± 0.0152 | -0.01 (3) |
| 5-10 | 1806 | 0.1826 | 0.1799 | +0.0026 ± 0.0015 | 0.5462 | 0.5356 | 0.4829 | 0.409 | 0.4252 | -0.055 ± 0.01 | -0.0067 (12) |
| 10-15 | 1445 | 0.1995 | 0.1829 | +0.0166 ± 0.0028 | 0.5844 | 0.5352 | 0.4913 | 0.368 | 0.3619 | -0.084 ± 0.0111 | -0.03 (9) |
| 15-25 | 2066 | 0.2063 | 0.1684 | +0.0379 ± 0.0036 | 0.6057 | 0.5008 | 0.4959 | 0.2993 | 0.302 | -0.073 ± 0.0091 | -0.03 (2) |
| 25-40 | 1616 | 0.2137 | 0.1224 | +0.0913 ± 0.0055 | 0.6184 | 0.3778 | 0.5241 | 0.2067 | 0.2252 | -0.058 ± 0.0082 | 0.0 (1) |
| 40+ | 1090 | 0.3788 | 0.048 | +0.3308 ± 0.0075 | 0.9913 | 0.1853 | 0.6274 | 0.1059 | 0.0615 | -0.079 ± 0.0062 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 538 | 0.2016 | 0.2016 | -0.0000 ± 0.0007 | 0.5867 | 0.5863 | 0.5001 | 0.4853 | 0.487 | -0.048 ± 0.0193 | -0.0226 (46) |
| 3-5 | 404 | 0.1956 | 0.1948 | +0.0008 ± 0.0018 | 0.5728 | 0.5694 | 0.481 | 0.4414 | 0.4554 | -0.043 ± 0.0219 | -0.0059 (32) |
| 5-10 | 830 | 0.1916 | 0.1863 | +0.0053 ± 0.0023 | 0.5672 | 0.5536 | 0.4716 | 0.3981 | 0.4 | -0.060 ± 0.0153 | -0.0049 (73) |
| 10-15 | 546 | 0.2026 | 0.1917 | +0.0109 ± 0.0047 | 0.5942 | 0.5642 | 0.4778 | 0.3548 | 0.3718 | -0.048 ± 0.0187 | 0.0014 (64) |
| 15-25 | 749 | 0.2346 | 0.2101 | +0.0245 ± 0.0066 | 0.6641 | 0.606 | 0.5445 | 0.35 | 0.3858 | -0.054 ± 0.0169 | -0.0216 (58) |
| 25-40 | 417 | 0.2437 | 0.1828 | +0.0609 ± 0.013 | 0.6848 | 0.5385 | 0.6183 | 0.3051 | 0.3621 | -0.072 ± 0.0196 | -0.0216 (25) |
| 40+ | 141 | 0.3412 | 0.1844 | +0.1568 ± 0.0368 | 0.9694 | 0.5461 | 0.7707 | 0.2776 | 0.3901 | -0.041 ± 0.0325 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1503 | 0.1883 | 0.1882 | +0.0001 ± 0.0004 | 0.554 | 0.5526 | 0.4979 | 0.4826 | 0.4837 | -0.045 ± 0.0111 | -0.0155 (82) |
| 3-5 | 1068 | 0.1852 | 0.1834 | +0.0018 ± 0.0011 | 0.5452 | 0.5411 | 0.4894 | 0.4498 | 0.4513 | -0.049 ± 0.0131 | -0.017 (57) |
| 5-10 | 2221 | 0.1881 | 0.1805 | +0.0077 ± 0.0014 | 0.5594 | 0.5382 | 0.4721 | 0.3982 | 0.3868 | -0.067 ± 0.0092 | -0.0087 (125) |
| 10-15 | 1537 | 0.1981 | 0.1834 | +0.0146 ± 0.0027 | 0.583 | 0.5439 | 0.4877 | 0.3648 | 0.3663 | -0.060 ± 0.0108 | -0.0053 (105) |
| 15-25 | 2047 | 0.2277 | 0.1984 | +0.0293 ± 0.0039 | 0.6546 | 0.577 | 0.5381 | 0.3428 | 0.3659 | -0.055 ± 0.01 | -0.0255 (106) |
| 25-40 | 1427 | 0.2366 | 0.1578 | +0.0789 ± 0.0066 | 0.67 | 0.4719 | 0.5802 | 0.2651 | 0.2992 | -0.059 ± 0.0102 | -0.0206 (47) |
| 40+ | 696 | 0.3537 | 0.1067 | +0.2470 ± 0.0132 | 0.9676 | 0.3368 | 0.6739 | 0.1686 | 0.1897 | -0.054 ± 0.0114 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 1728 | 1.12 ± 0.07 | 1.214 | 0.1697 | 0.1659 | 0.2083 | 0.202 |
| gen2 | 1728 | 0.899 ± 0.061 | 1.138 | 0.1866 | 0.1654 | 0.2268 | 0.202 |
| gen1_elo | 1728 | 1.101 ± 0.068 | 1.197 | 0.1736 | 0.1664 | 0.2072 | 0.202 |
| gen1_sr | 1728 | 1.117 ± 0.079 | 1.221 | 0.1433 | 0.1679 | 0.2223 | 0.2018 |
| gen1_ledger | 3625 | 0.936 ± 0.044 | 1.087 | 0.1697 | 0.1915 | 0.2159 | 0.1948 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 9,915)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,721 | 27.4% |
| STALE_QUOTE | market_freshness | 2,179 | 22.0% |
| BOOK_QUALITY | execution | 1,738 | 17.5% |
| POOR_DATA | data | 1,064 | 10.7% |
| LIMITED_DATA | data | 699 | 7.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 507 | 5.1% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 449 | 4.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 275 | 2.8% |
| IDENTITY_AMBIGUOUS | mapping | 256 | 2.6% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 27 | 0.3% |

Cause class: coverage 27.4%, market_freshness 22.0%, data 17.8%, execution 17.5%, market_freshness/coverage 7.9%, model_calibration_or_unknown 4.5%, mapping 2.6%, model_calibration 0.3%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.6%, START_UNVERIFIABLE 96.1%, LOW_DATA_QUALITY 69.2%, THIN_PLAYER_HISTORY 58.4%, STALE_PLAYER_DATA 58.4%, STALE_KALSHI_QUOTE 49.3%, MODEL_INTERNAL_DISAGREEMENT 37.4%, ASYMMETRIC_SAMPLE_SIZE 31.5%, WIDE_SPREAD 23.8%, MODEL_HIGH_UNCERTAINTY 15.9%, PLAYER_IDENTITY_RISK 10.8%, LEVEL_TRANSFER_RISK 8.8%, EVENT_MAPPING_RISK 7.2%, LOW_DISPLAYED_LIQUIDITY 7.2%, MODEL_CALIBRATION_OUTLIER 3.0%, UNKNOWN 0.5%, EXTERNAL_MARKET_REJECTION 0.4%, EXTERNAL_MARKET_CONFIRMATION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 29.8%, POST_SETTLEMENT_OBSERVATION 27.4%, POSSIBLE_IN_PLAY_QUOTE 5.5%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### >= ge_25 pp (N = 5,419)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,151 | 39.7% |
| STALE_QUOTE | market_freshness | 971 | 17.9% |
| BOOK_QUALITY | execution | 908 | 16.8% |
| POOR_DATA | data | 445 | 8.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 280 | 5.2% |
| LIMITED_DATA | data | 223 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 174 | 3.2% |
| IDENTITY_AMBIGUOUS | mapping | 149 | 2.8% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 108 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 10 | 0.2% |

Cause class: coverage 39.7%, market_freshness 17.9%, execution 16.8%, data 12.3%, market_freshness/coverage 8.4%, mapping 2.8%, model_calibration_or_unknown 2.0%, model_calibration 0.2%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.7%, START_UNVERIFIABLE 98.1%, LOW_DATA_QUALITY 71.8%, THIN_PLAYER_HISTORY 60.2%, STALE_KALSHI_QUOTE 56.9%, STALE_PLAYER_DATA 53.7%, MODEL_INTERNAL_DISAGREEMENT 39.2%, ASYMMETRIC_SAMPLE_SIZE 33.7%, WIDE_SPREAD 23.0%, MODEL_HIGH_UNCERTAINTY 17.1%, PLAYER_IDENTITY_RISK 13.4%, EVENT_MAPPING_RISK 8.4%, LOW_DISPLAYED_LIQUIDITY 7.6%, LEVEL_TRANSFER_RISK 7.5%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 0.3%, UNKNOWN 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 42.4%, POST_SETTLEMENT_OBSERVATION 39.7%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.7%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 4538, "IDENTITY_AMBIGUOUS": 881}; ticker orientation: {"VERIFIED": 5419}.

Checks: discipline:AMBIGUOUS 299, discipline:PASS 5120, identity_confidence:AMBIGUOUS 728, identity_confidence:PASS 4691, level_mapping:NA 311, level_mapping:PASS 5108, market_pair:AMBIGUOUS 193, market_pair:NA 126, market_pair:PASS 5100, model_complement:NA 93, model_complement:PASS 5326, namesake:PASS 5419, physical_match_id:NA 2256, physical_match_id:PASS 3163, player_ids:PASS 5419, same_pair_other_event:PASS 5419, ticker_orientation:PASS 5419

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,328 | 1.8% | 1.8% | 0.4% | {"market_freshness": 20, "execution": 4} | 5.67 | 0.2032 / 0.2006 (111) | 21.2% | 0.1% | 6.2% | 1.4% |
| CHALLENGER | 3,590 | 19.1% | 6.5% | 12.7% | {"coverage": 427, "market_freshness": 107, "market_freshness/coverage": 81, "model_calibration_or_unknown": 39, "data": 25, "execution": 4, "model_calibration": 3} | 6.88 | 0.223 / 0.2044 (846) | 47.2% | 5.0% | 1.6% | 23.8% |
| DOUBLES | 642 | 46.6% | 46.1% | 5.5% | {"market_freshness": 106, "execution": 101, "mapping": 64, "market_freshness/coverage": 21, "coverage": 7} | 23.51 | 0.3105 / 0.2241 (194) | 36.4% | 0.0% | 100.0% | 8.4% |
| ITF_MEN | 7,285 | 24.2% | 16.3% | 32.5% | {"coverage": 711, "execution": 378, "market_freshness": 261, "data": 252, "market_freshness/coverage": 139, "mapping": 19, "model_calibration_or_unknown": 1} | 10.63 | 0.2127 / 0.193 (1779) | 39.2% | 55.4% | 6.3% | 23.2% |
| ITF_WOMEN | 9,313 | 26.2% | 17.9% | 45.0% | {"coverage": 989, "market_freshness": 420, "execution": 404, "data": 367, "market_freshness/coverage": 172, "mapping": 60, "model_calibration_or_unknown": 22, "model_calibration": 6} | 12.05 | 0.2019 / 0.1938 (1963) | 40.4% | 59.0% | 10.1% | 23.3% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 973 | 8.1% | 7.0% | 1.5% | {"market_freshness": 34, "model_calibration_or_unknown": 16, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.27 | 0.2008 / 0.1978 (145) | 34.2% | 2.2% | 1.2% | 3.4% |
| WTA125 | 794 | 14.9% | 10.7% | 2.2% | {"market_freshness/coverage": 31, "model_calibration_or_unknown": 28, "market_freshness": 21, "data": 13, "coverage": 12, "execution": 8, "mapping": 4, "model_calibration": 1} | 9.98 | 0.2248 / 0.211 (273) | 27.0% | 5.9% | 4.3% | 11.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 5 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 17.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1037 min (STALE); no external reference |
| 6 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 7 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 8 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 9 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 10 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 11 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 12 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 92 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 14 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 15 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 16 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 17 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 18 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 19 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 20 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 21 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 22 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 23 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 24 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 25 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 26 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 27 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 64 min (STALE); no external reference |
| 28 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 29 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 22% | +74 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 30 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 31 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 32 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 33 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 34 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 253 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 35 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 36 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 22 min (AGING); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 37 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 38 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 39 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 40 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.2h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 141 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 41 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 42 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 43 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 66 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 44 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 46 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 47 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 48 | `KXATPCHALLENGERMATCH-26OCT06BARSAM-SAM` | CHALLENGER | fair_v1 | 84% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 710 min (STALE); no external reference |
| 49 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.9h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 671 min (STALE); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9811, "by_level_share_of_ge_25pp": {"ATP": 0.0044, "CHALLENGER": 0.1266, "DOUBLES": 0.0552, "ITF_MEN": 0.325, "ITF_WOMEN": 0.4503, "OTHER": 0.0022, "WTA": 0.0146, "WTA125": 0.0218}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5689, "share_primary_cause_market_settled_or_in_play": 0.4807, "share_primary_cause_stale_quote_only": 0.1792}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 5419, "identity_ambiguous_share": 0.1626, "ticker_orientation": {"VERIFIED": 5419}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 3163, "with_external": 51, "coverage": 0.0161, "external_status": {"EXTERNAL_STALE": 42, "AGREES_WITH_KALSHI": 9}, "triangulation": {"INSUFFICIENT_INPUTS": 42, "MODEL_LONE_OUTLIER": 9}, "share_external_agrees_with_kalshi": 0.1765, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 1401, "with_external": 50, "coverage": 0.0357, "external_status": {"EXTERNAL_STALE": 41, "AGREES_WITH_KALSHI": 9}, "triangulation": {"INSUFFICIENT_INPUTS": 41, "MODEL_LONE_OUTLIER": 9}, "share_external_agrees_with_kalshi": 0.18, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 605.0, "median_sample_ratio": 2.35, "median_min_matches": 20.0, "median_max_days_since_last": 197.0, "share_severe_asymmetry": 0.1808, "data_status": {"POOR": 2865, "LIMITED": 1583, "ADEQUATE": 971}, "comparison_lt_10pp": {"median_thinner_serve_points": 1709.0, "median_sample_ratio": 1.77, "median_min_matches": 71.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 386, "model_minus_observed": 0.0693, "kalshi_minus_observed": -0.063, "brier_diff_model_minus_kalshi": 0.0045}, "4-10x": {"n": 279, "model_minus_observed": 0.0515, "kalshi_minus_observed": -0.0911, "brier_diff_model_minus_kalshi": -0.0069}, "<2x": {"n": 802, "model_minus_observed": 0.0833, "kalshi_minus_observed": -0.0444, "brier_diff_model_minus_kalshi": 0.0099}, ">=10x": {"n": 261, "model_minus_observed": 0.0999, "kalshi_minus_observed": -0.076, "brier_diff_model_minus_kalshi": 0.0115}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 1728, "model": {"intercept": -0.576, "slope": 0.899, "slope_se": 0.061}, "kalshi_mid_same_rows": {"intercept": 0.234, "slope": 1.138, "slope_se": 0.07}, "mean_extremity_model": 0.1866, "mean_extremity_kalshi": 0.1654, "model_brier": 0.2268, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0249, "brier_diff_se": 0.0046, "model_logloss": 0.6488, "kalshi_logloss": 0.5864}, "fair_v1": {"n": 1728, "model": {"intercept": -0.404, "slope": 1.12, "slope_se": 0.07}, "kalshi_mid_same_rows": {"intercept": 0.365, "slope": 1.214, "slope_se": 0.073}, "mean_extremity_model": 0.1697, "mean_extremity_kalshi": 0.1659, "model_brier": 0.2083, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0063, "brier_diff_se": 0.0037, "model_logloss": 0.6026, "kalshi_logloss": 0.5864}, "gen1_elo": {"n": 1728, "model": {"intercept": -0.378, "slope": 1.101, "slope_se": 0.068}, "kalshi_mid_same_rows": {"intercept": 0.364, "slope": 1.197, "slope_se": 0.071}, "mean_extremity_model": 0.1736, "mean_extremity_kalshi": 0.1664, "model_brier": 0.2072, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0052, "brier_diff_se": 0.0037, "model_logloss": 0.6012, "kalshi_logloss": 0.5863}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2512, "share_ge_15": 0.4363, "median_abs_gap": 13.0, "n": 12590}, "gen1_elo": {"share_ge_25": 0.2416, "share_ge_15": 0.4347, "median_abs_gap": 12.54, "n": 12590}, "gen1_sr": {"share_ge_25": 0.3036, "share_ge_15": 0.5187, "median_abs_gap": 15.64, "n": 12590}, "gen2": {"share_ge_25": 0.3073, "share_ge_15": 0.506, "median_abs_gap": 15.32, "n": 12590}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1463, "share_ge_15": 0.3373, "median_abs_gap": 10.45, "n": 9575}, "gen1_elo": {"share_ge_25": 0.1411, "share_ge_15": 0.3329, "median_abs_gap": 10.01, "n": 9574}, "gen1_sr": {"share_ge_25": 0.2005, "share_ge_15": 0.4299, "median_abs_gap": 12.81, "n": 9575}, "gen2": {"share_ge_25": 0.2183, "share_ge_15": 0.4283, "median_abs_gap": 12.67, "n": 9576}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.67, "share_ge_25_all": 0.0181, "share_ge_25_pregame_clean": 0.0183}, "WTA": {"median_abs_gap_pregame_clean": 8.27, "share_ge_25_all": 0.0812, "share_ge_25_pregame_clean": 0.0702}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2351, "share_within_10pp_all": 0.4343, "share_within_10pp_pregame_clean": 0.4981, "corr_model_vs_mid_pregame_clean": 0.8526}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 249, "model_brier": 0.1803, "kalshi_brier": 0.1813, "brier_diff_model_minus_kalshi": -0.0011}, "10-15": {"n_settled": 301, "model_brier": 0.2199, "kalshi_brier": 0.2179, "brier_diff_model_minus_kalshi": 0.0019}, "15-25": {"n_settled": 377, "model_brier": 0.2201, "kalshi_brier": 0.2105, "brier_diff_model_minus_kalshi": 0.0095}, "25-40": {"n_settled": 221, "model_brier": 0.2183, "kalshi_brier": 0.2041, "brier_diff_model_minus_kalshi": 0.0141}, "3-5": {"n_settled": 173, "model_brier": 0.1872, "kalshi_brier": 0.1881, "brier_diff_model_minus_kalshi": -0.0009}, "40+": {"n_settled": 51, "model_brier": 0.2726, "kalshi_brier": 0.1802, "brier_diff_model_minus_kalshi": 0.0924}, "5-10": {"n_settled": 356, "model_brier": 0.2004, "kalshi_brier": 0.2026, "brier_diff_model_minus_kalshi": -0.0022}}}`

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
