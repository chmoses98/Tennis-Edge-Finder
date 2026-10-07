# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-07T06:30Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 21,260): 0-3 13.5%, 3-5 9.5%, 5-10 19.8%, 10-15 15.4%, 15-25 18.9%, 25-40 14.4%, 40+ 8.5%; median gap 12.17 pp.
* **Where the extremes live**: 97.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.5%, Challenger 13.2%, doubles 4.7%). Main tour: ATP 2.0% and WTA 8.5% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 4,874): MARKET_ALREADY_SETTLED_WHEN_PRICED 40.1%, STALE_QUOTE 19.4%, BOOK_QUALITY 16.7%, POOR_DATA 8.3%, POSSIBLY_IN_PLAY_QUOTE 4.6%, LIMITED_DATA 3.5%, IN_PLAY_QUOTE 2.8%, IDENTITY_AMBIGUOUS 2.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.0%. By class: coverage 40.1%, market_freshness 19.4%, execution 16.7%, data 11.8%, market_freshness/coverage 7.4%, mapping 2.5%, model_calibration_or_unknown 2.1%, model_calibration 0.0%.
* **Stale / settled / in-play**: 58.9% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 47.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 4,874 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 16.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 0.9%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 6.4% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 596.0 points vs 1754.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.149, Gen-2 0.935, Gen-1 ledger 0.934 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 175 model 0.2106 vs Kalshi 0.1996; n 39 model 0.3105 vs Kalshi 0.1436.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%). Not implemented here.

## 1. Observations

* 78,782 model-market comparisons (132,540 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 30,718 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-07T06:26:13.676156+00:00'], shadow board 21,922 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-07T06:26:16.638670+00:00'], Model 4 7,740 rows, 9,601 settled tickers, 2,415 tickers with an external scan.
* By model: {"gen1_ledger": 19487, "gen1_elo": 11016, "fair_v1": 11016, "gen2": 11016, "gen1_sr": 11016, "model4_fundamental": 7620, "model4_conditioned": 7611}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 21,260 | 13.5 | 9.5 | 19.8 | 15.4 | 18.9 | 14.4 | 8.5 | 12.17 | 41.8% | 22.9% |
| MW fair_v1 | 11,016 | 12.9 | 8.9 | 18.4 | 15.9 | 18.6 | 15.3 | 10.2 | 13.04 | 44.0% | 25.4% |
| MW gen1_elo | 11,016 | 12.8 | 8.8 | 19.7 | 14.9 | 19.4 | 14.8 | 9.6 | 12.66 | 43.8% | 24.4% |
| MW gen1_ledger | 10,244 | 14.2 | 10.3 | 21.3 | 14.8 | 19.2 | 13.5 | 6.8 | 11.27 | 39.5% | 20.2% |
| MW gen1_sr | 11,016 | 9.8 | 7.8 | 16.0 | 14.2 | 21.8 | 18.5 | 11.9 | 15.8 | 52.2% | 30.4% |
| MW gen2 | 11,016 | 11.5 | 7.1 | 16.0 | 14.5 | 19.9 | 17.5 | 13.4 | 15.41 | 50.9% | 30.9% |
| all families model4_conditioned | 7,611 | 21.7 | 20.3 | 34.4 | 16.5 | 5.2 | 1.0 | 0.9 | 5.82 | 7.0% | 1.8% |
| all families model4_fundamental | 7,620 | 16.5 | 13.2 | 34.2 | 20.3 | 11.2 | 3.4 | 1.3 | 7.81 | 15.8% | 4.6% |

Configurable thresholds (primary): >=5pp 77.0%, >=10pp 57.2%, >=15pp 41.8%, >=20pp 31.4%, >=25pp 22.9%, >=30pp 16.8%, >=40pp 8.5%, >=50pp 3.6%
Executable gap (model outside the book, before fees): median 8.54pp; >=10pp 45.9%, >=25pp 18.4%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 763 | 25.4 | 17.3 | 24.9 | 16.9 | 12.4 | 1.6 | 1.4 | 5.93 | 15.5% | 3.0% |
| CHALLENGER | 2,030 | 14.5 | 11.2 | 18.4 | 16.2 | 13.3 | 13.3 | 13.2 | 12.03 | 39.8% | 26.5% |
| ITF_MEN | 3,116 | 10.5 | 8.5 | 18.6 | 14.6 | 19.6 | 15.2 | 13.1 | 14.09 | 47.9% | 28.2% |
| ITF_WOMEN | 4,309 | 10.4 | 6.6 | 16.1 | 15.9 | 21.7 | 19.6 | 9.7 | 15.41 | 50.9% | 29.2% |
| WTA | 511 | 22.7 | 9.8 | 24.7 | 16.2 | 18.0 | 6.5 | 2.1 | 8.36 | 26.6% | 8.6% |
| WTA125 | 287 | 12.9 | 6.6 | 20.6 | 25.4 | 14.3 | 17.4 | 2.8 | 11.47 | 34.5% | 20.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 763 | 21.0 | 15.1 | 25.3 | 18.0 | 16.2 | 2.8 | 1.7 | 6.9 | 20.7% | 4.5% |
| CHALLENGER | 2,030 | 14.7 | 7.2 | 17.7 | 13.7 | 18.7 | 14.5 | 13.6 | 13.46 | 46.8% | 28.1% |
| ITF_MEN | 3,116 | 10.1 | 7.1 | 16.3 | 15.0 | 20.0 | 17.8 | 13.7 | 15.55 | 51.5% | 31.5% |
| ITF_WOMEN | 4,309 | 8.6 | 6.2 | 13.1 | 13.2 | 20.9 | 21.2 | 16.6 | 18.71 | 58.7% | 37.9% |
| WTA | 511 | 21.1 | 4.9 | 17.0 | 15.8 | 21.9 | 17.0 | 2.1 | 13.18 | 41.1% | 19.2% |
| WTA125 | 287 | 5.2 | 2.1 | 16.4 | 23.7 | 19.9 | 19.9 | 12.9 | 16.74 | 52.6% | 32.8% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 763 | 25.0 | 12.1 | 30.0 | 16.9 | 10.5 | 3.9 | 1.6 | 6.9 | 16.0% | 5.5% |
| CHALLENGER | 2,030 | 15.8 | 11.0 | 19.9 | 14.1 | 13.7 | 12.3 | 13.1 | 10.75 | 39.2% | 25.4% |
| ITF_MEN | 3,116 | 9.5 | 8.7 | 18.3 | 13.9 | 21.0 | 15.5 | 13.1 | 14.97 | 49.7% | 28.7% |
| ITF_WOMEN | 4,309 | 9.8 | 6.7 | 16.4 | 15.5 | 23.8 | 19.3 | 8.4 | 15.62 | 51.5% | 27.7% |
| WTA | 511 | 23.3 | 12.9 | 34.6 | 14.3 | 9.8 | 3.7 | 1.4 | 6.99 | 14.9% | 5.1% |
| WTA125 | 287 | 21.2 | 11.5 | 27.2 | 18.1 | 15.7 | 5.6 | 0.7 | 7.99 | 21.9% | 6.3% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 398 | 28.4 | 20.9 | 37.7 | 11.8 | 1.3 | 0.0 | 0.0 | 5.17 | 1.3% | 0.0% |
| CHALLENGER | 1,332 | 22.6 | 16.1 | 26.8 | 14.3 | 12.3 | 5.7 | 2.2 | 6.8 | 20.2% | 7.9% |
| DOUBLES | 518 | 4.2 | 3.1 | 13.7 | 11.4 | 23.8 | 20.9 | 23.0 | 22.7 | 67.6% | 43.8% |
| ITF_MEN | 3,236 | 13.4 | 8.4 | 19.6 | 15.5 | 20.6 | 13.7 | 8.8 | 12.46 | 43.1% | 22.5% |
| ITF_WOMEN | 3,728 | 10.9 | 9.2 | 18.9 | 14.1 | 22.6 | 18.0 | 6.3 | 13.67 | 46.9% | 24.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 424 | 19.1 | 11.3 | 25.7 | 19.6 | 16.0 | 7.5 | 0.7 | 8.71 | 24.3% | 8.2% |
| WTA125 | 459 | 15.0 | 12.6 | 22.0 | 19.6 | 18.1 | 9.6 | 3.0 | 10.09 | 30.7% | 12.6% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 759 | 25.4 | 17.1 | 24.9 | 17.0 | 12.5 | 1.6 | 1.4 | 5.93 | 15.6% | 3.0% |
| CHALLENGER | 1,443 | 18.9 | 14.3 | 23.6 | 18.7 | 14.3 | 7.1 | 3.0 | 8.46 | 24.5% | 10.2% |
| ITF_MEN | 2,271 | 12.7 | 10.7 | 22.1 | 16.2 | 19.6 | 12.6 | 6.2 | 11.18 | 38.3% | 18.7% |
| ITF_WOMEN | 3,142 | 12.9 | 8.2 | 18.8 | 18.1 | 23.1 | 15.6 | 3.2 | 12.79 | 42.0% | 18.9% |
| WTA | 509 | 22.8 | 9.8 | 24.8 | 16.1 | 18.1 | 6.3 | 2.2 | 8.36 | 26.5% | 8.5% |
| WTA125 | 276 | 13.4 | 6.9 | 20.3 | 25.7 | 14.5 | 17.4 | 1.8 | 11.39 | 33.7% | 19.2% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 759 | 20.8 | 15.0 | 25.4 | 17.9 | 16.3 | 2.8 | 1.7 | 6.9 | 20.8% | 4.5% |
| CHALLENGER | 1,443 | 19.3 | 9.4 | 22.3 | 16.5 | 19.5 | 10.1 | 2.9 | 9.77 | 32.5% | 13.0% |
| ITF_MEN | 2,271 | 12.2 | 8.4 | 18.9 | 16.9 | 21.0 | 15.4 | 7.1 | 12.85 | 43.5% | 22.5% |
| ITF_WOMEN | 3,142 | 10.2 | 7.3 | 14.9 | 14.2 | 22.9 | 19.9 | 10.7 | 16.27 | 53.4% | 30.5% |
| WTA | 509 | 21.2 | 4.9 | 17.1 | 15.9 | 21.8 | 16.9 | 2.2 | 13.07 | 40.9% | 19.1% |
| WTA125 | 276 | 5.4 | 2.2 | 16.7 | 24.6 | 18.8 | 20.6 | 11.6 | 15.82 | 51.1% | 32.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 385 | 28.6 | 21.0 | 38.2 | 11.9 | 0.3 | 0.0 | 0.0 | 5.11 | 0.3% | 0.0% |
| CHALLENGER | 1,118 | 24.7 | 18.2 | 29.2 | 13.9 | 11.6 | 2.1 | 0.1 | 6.17 | 13.9% | 2.2% |
| DOUBLES | 475 | 4.2 | 3.0 | 14.1 | 11.4 | 24.0 | 21.1 | 22.3 | 22.7 | 67.4% | 43.4% |
| ITF_MEN | 2,590 | 15.2 | 9.3 | 21.9 | 16.6 | 20.5 | 11.3 | 5.1 | 11.16 | 37.0% | 16.4% |
| ITF_WOMEN | 3,008 | 12.3 | 10.2 | 20.9 | 15.0 | 22.9 | 16.2 | 2.6 | 11.84 | 41.7% | 18.8% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 394 | 19.5 | 11.9 | 26.4 | 19.8 | 16.5 | 5.8 | 0.0 | 8.48 | 22.3% | 5.8% |
| WTA125 | 376 | 17.0 | 14.1 | 24.7 | 22.6 | 16.2 | 5.0 | 0.3 | 8.91 | 21.5% | 5.3% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 518 | 4.2 | 3.1 | 13.7 | 11.4 | 23.8 | 20.9 | 23.0 | 22.7 | 67.6% | 43.8% |
| singles | 9,726 | 14.7 | 10.6 | 21.7 | 15.0 | 19.0 | 13.1 | 5.9 | 10.82 | 38.0% | 19.0% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 2,591 | 13.3 | 9.5 | 19.9 | 15.4 | 16.1 | 14.6 | 11.0 | 12.3 | 41.8% | 25.6% |
| Hard | 7,439 | 12.8 | 8.8 | 18.4 | 15.8 | 19.4 | 15.1 | 9.8 | 13.21 | 44.3% | 24.9% |
| UNKNOWN | 986 | 12.4 | 8.0 | 14.1 | 18.1 | 18.9 | 18.1 | 10.4 | 14.13 | 47.4% | 28.5% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,192 | 17.8 | 11.3 | 20.4 | 16.9 | 14.9 | 10.2 | 8.4 | 10.1 | 33.5% | 18.6% |
| B | 1,389 | 15.3 | 9.9 | 19.6 | 17.4 | 16.3 | 11.4 | 10.0 | 11.08 | 37.8% | 21.4% |
| C | 1,691 | 12.4 | 9.8 | 21.4 | 15.0 | 18.1 | 14.3 | 9.0 | 12.24 | 41.4% | 23.3% |
| D | 2,057 | 11.6 | 8.8 | 16.3 | 15.9 | 22.9 | 15.7 | 8.8 | 14.1 | 47.4% | 24.5% |
| F | 2,687 | 7.0 | 4.9 | 14.9 | 14.6 | 21.0 | 23.5 | 14.1 | 18.74 | 58.6% | 37.6% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 2,880 | 21.0 | 14.7 | 27.1 | 16.1 | 13.3 | 5.5 | 2.2 | 7.33 | 21.0% | 7.7% |
| B | 1,546 | 14.2 | 9.8 | 23.7 | 15.7 | 18.9 | 12.1 | 5.6 | 10.68 | 36.6% | 17.7% |
| C | 1,967 | 11.7 | 8.0 | 19.5 | 14.9 | 21.3 | 14.7 | 9.8 | 13.2 | 45.8% | 24.5% |
| D | 1,729 | 12.5 | 9.0 | 20.8 | 13.2 | 22.2 | 15.6 | 6.7 | 12.87 | 44.4% | 22.2% |
| F | 2,122 | 8.6 | 7.6 | 13.5 | 13.5 | 23.2 | 22.6 | 11.0 | 17.52 | 56.8% | 33.6% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 3,661 | 16.9 | 10.5 | 19.7 | 17.2 | 15.2 | 10.5 | 10.0 | 10.83 | 35.8% | 20.5% |
| LIMITED | 2,576 | 14.3 | 10.7 | 21.8 | 15.4 | 17.2 | 13.2 | 7.3 | 10.97 | 37.7% | 20.5% |
| POOR | 4,779 | 9.0 | 6.6 | 15.5 | 15.2 | 21.9 | 20.0 | 11.8 | 16.49 | 53.7% | 31.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,669 | 29.8 | 26.2 | 36.8 | 5.3 | 1.7 | 0.2 | 0.0 | 4.46 | 1.9% | 0.2% |
| GAME_SPREAD | 1,686 | 23.7 | 15.4 | 37.0 | 18.7 | 4.7 | 0.3 | 0.2 | 6.2 | 5.2% | 0.5% |
| MATCH_WINNER | 10,244 | 14.2 | 10.3 | 21.3 | 14.8 | 19.2 | 13.5 | 6.8 | 11.27 | 39.5% | 20.2% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 3,274 | 29.0 | 18.6 | 31.6 | 11.4 | 7.6 | 1.4 | 0.3 | 5.3 | 9.3% | 1.8% |
| TOTAL_GAMES | 2,590 | 7.9 | 9.5 | 37.1 | 29.3 | 10.4 | 3.5 | 2.4 | 9.51 | 16.3% | 5.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,780 | 24.8 | 39.2 | 28.4 | 0.3 | 6.4 | 0.6 | 0.2 | 4.32 | 7.3% | 0.8% |
| GAME_SPREAD | 1,904 | 45.0 | 14.5 | 29.5 | 9.0 | 1.2 | 0.6 | 0.2 | 3.59 | 2.0% | 0.8% |
| TOTAL_GAMES | 2,927 | 3.7 | 6.2 | 43.4 | 36.8 | 6.5 | 1.5 | 1.9 | 9.75 | 10.0% | 3.5% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,780 | 25.6 | 18.1 | 35.4 | 9.5 | 7.5 | 3.3 | 0.5 | 5.6 | 11.3% | 3.8% |
| GAME_SPREAD | 1,904 | 19.2 | 13.5 | 26.8 | 22.8 | 13.7 | 3.2 | 0.8 | 8.31 | 17.6% | 4.0% |
| TOTAL_GAMES | 2,936 | 6.1 | 8.3 | 37.9 | 28.8 | 13.0 | 3.5 | 2.3 | 9.74 | 18.8% | 5.8% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 11,016 | 44.0% | 25.4% | 13.04 | 34.4% | 15.3% | 10.54 |
| gen1_elo | 11,016 | 43.8% | 24.4% | 12.66 | 33.9% | 14.7% | 10.12 |
| gen1_sr | 11,016 | 52.2% | 30.4% | 15.8 | 43.5% | 20.2% | 12.97 |
| gen2 | 11,016 | 50.9% | 30.9% | 15.41 | 43.4% | 22.4% | 12.79 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 5,222 | 15.5 | 11.5 | 21.7 | 17.2 | 18.7 | 11.8 | 3.6 | 10.34 | 34.1% | 15.4% |
| STALE | 5,794 | 10.5 | 6.5 | 15.3 | 14.8 | 18.4 | 18.4 | 16.1 | 16.55 | 52.9% | 34.5% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 3,712 | 16.1 | 11.5 | 24.0 | 14.9 | 17.1 | 12.3 | 4.1 | 9.66 | 33.5% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 21,260 | 3712 | 8694 | 8854 | 26.1 | 178.3 | 1400.4 |
| ge_15pp | 8,890 | 1245 | 3069 | 4576 | 31.0 | 455.5 | 1380.4 |
| ge_25pp | 4,874 | 611 | 1394 | 2869 | 40.7 | 564.5 | 1380.4 |
| lt_10pp | 9,100 | 1915 | 4176 | 3009 | 24.4 | 53.6 | 1201.9 |

Current slate `SL-20261007T063011Z-761949d0`: 1023 priced rows, quote age at build {'median': 4.3, 'max': 4.4}, freshness {'FRESH': 1023}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 329 | 21.9 | 12.2 | 21.9 | 20.7 | 16.4 | 6.4 | 0.6 | 7.89 | 23.4% | 7.0% |
| MARKETS_AGREE | 22 | 68.2 | 31.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.35 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 24 | 0.0 | 0.0 | 29.2 | 41.7 | 25.0 | 4.2 | 0.0 | 12.11 | 29.2% | 4.2% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 11,016 | 376 (3.4%) | 6.4% | 0.0% | {"EXTERNAL_STALE": 329, "AGREES_WITH_KALSHI": 24, "ALL_AGREE": 22, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 4,846 | 84 (1.7%) | 8.3% | 0.0% | {"EXTERNAL_STALE": 77, "AGREES_WITH_KALSHI": 7} |
| fair_v1_ge_25pp | 2,801 | 24 (0.9%) | 4.2% | 0.0% | {"EXTERNAL_STALE": 23, "AGREES_WITH_KALSHI": 1} |
| fair_v1_ge_25pp_pregame_clean | 1,284 | 24 (1.9%) | 4.2% | 0.0% | {"EXTERNAL_STALE": 23, "AGREES_WITH_KALSHI": 1} |
| fair_v1_lt_10pp | 4,416 | 214 (4.9%) | 3.3% | 0.0% | {"EXTERNAL_STALE": 184, "ALL_AGREE": 22, "AGREES_WITH_KALSHI": 7, "EXTERNAL_OUTLIER": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 2,193 | 11.0 | 8.5 | 20.6 | 15.3 | 21.2 | 14.0 | 9.3 | 12.9 | 44.5% | 23.4% |
| 4-10x | 1,630 | 11.2 | 9.8 | 17.9 | 14.6 | 20.6 | 17.3 | 8.7 | 13.76 | 46.6% | 26.0% |
| <2x | 5,772 | 14.7 | 9.5 | 18.4 | 16.8 | 17.0 | 13.6 | 10.0 | 12.24 | 40.6% | 23.6% |
| >=10x | 1,421 | 10.3 | 5.8 | 15.1 | 14.8 | 18.7 | 21.5 | 13.7 | 16.86 | 53.9% | 35.2% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 2,772 | 13.9 | 8.4 | 20.7 | 15.9 | 17.1 | 12.9 | 11.1 | 12.06 | 41.1% | 23.9% |
| 300-1000 | 2,633 | 12.2 | 9.5 | 16.5 | 15.8 | 22.0 | 15.9 | 8.1 | 13.68 | 46.0% | 24.0% |
| <300 | 3,131 | 8.0 | 6.1 | 15.4 | 14.7 | 20.7 | 21.8 | 13.5 | 17.75 | 55.9% | 35.3% |
| >=3000 | 2,480 | 18.6 | 12.3 | 21.4 | 17.7 | 13.8 | 9.0 | 7.1 | 9.47 | 30.0% | 16.2% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 318 | 0.5363 | 0.4034 | 0.4591 | +0.077 | -0.056 | 0.002 ± 0.0079 |
| ratio 4-10x | 231 | 0.589 | 0.4503 | 0.5368 | +0.052 | -0.086 | 0.0007 ± 0.0099 |
| ratio <2x | 660 | 0.5389 | 0.4143 | 0.4591 | +0.080 | -0.045 | 0.0109 ± 0.0056 |
| ratio >=10x | 214 | 0.5574 | 0.3842 | 0.4579 | +0.100 | -0.074 | 0.012 ± 0.0126 |
| thinner_sample 1000-3000 | 369 | 0.542 | 0.4204 | 0.4634 | +0.079 | -0.043 | 0.0042 ± 0.0073 |
| thinner_sample 300-1000 | 383 | 0.5708 | 0.4337 | 0.4987 | +0.072 | -0.065 | -0.0001 ± 0.0077 |
| thinner_sample <300 | 472 | 0.5505 | 0.3889 | 0.4767 | +0.074 | -0.088 | 0.0113 ± 0.0079 |
| thinner_sample >=3000 | 199 | 0.5181 | 0.4178 | 0.4221 | +0.096 | -0.004 | 0.0187 ± 0.0082 |
| data_status ADEQUATE | 390 | 0.5254 | 0.4189 | 0.4385 | +0.087 | -0.019 | 0.0105 ± 0.0062 |
| data_status LIMITED | 318 | 0.5642 | 0.4327 | 0.5031 | +0.061 | -0.070 | -0.0041 ± 0.0083 |
| data_status POOR | 715 | 0.5556 | 0.4013 | 0.4755 | +0.080 | -0.074 | 0.0109 ± 0.0062 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 212 | 0.1833 | 0.184 | -0.0008 ± 0.001 | 0.5418 | 0.5438 | 0.4929 | 0.4787 | 0.4953 | -0.101 ± 0.0314 | -0.01 (3) |
| 3-5 | 143 | 0.1817 | 0.1835 | -0.0018 ± 0.0029 | 0.5422 | 0.5435 | 0.5147 | 0.4741 | 0.5105 | -0.070 ± 0.037 | 0.02 (1) |
| 5-10 | 300 | 0.2 | 0.2024 | -0.0024 ± 0.0039 | 0.5863 | 0.5914 | 0.5208 | 0.4468 | 0.4933 | -0.089 ± 0.0271 | -0.0167 (3) |
| 10-15 | 244 | 0.2209 | 0.2175 | +0.0034 ± 0.0075 | 0.6301 | 0.6189 | 0.5276 | 0.4035 | 0.4508 | -0.094 ± 0.03 | -0.0633 (3) |
| 15-25 | 310 | 0.2177 | 0.2098 | +0.0079 ± 0.0102 | 0.6244 | 0.6041 | 0.5716 | 0.3762 | 0.4516 | -0.076 ± 0.026 | -0.02 (4) |
| 25-40 | 175 | 0.2106 | 0.1996 | +0.0110 ± 0.02 | 0.6077 | 0.5735 | 0.643 | 0.3314 | 0.4686 | -0.051 ± 0.0297 | -0.01 (1) |
| 40+ | 39 | 0.3105 | 0.1436 | +0.1669 ± 0.0543 | 0.8355 | 0.4493 | 0.7382 | 0.2969 | 0.3333 | -0.170 ± 0.0539 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 868 | 0.1682 | 0.169 | -0.0009 ± 0.0005 | 0.5037 | 0.5049 | 0.491 | 0.4763 | 0.5196 | -0.031 ± 0.0143 | -0.0188 (8) |
| 3-5 | 637 | 0.1871 | 0.1852 | +0.0019 ± 0.0014 | 0.5533 | 0.5442 | 0.4779 | 0.4381 | 0.4286 | -0.079 ± 0.0176 | 0.02 (1) |
| 5-10 | 1333 | 0.1854 | 0.1853 | +0.0000 ± 0.0018 | 0.5516 | 0.5497 | 0.4809 | 0.4072 | 0.4426 | -0.043 ± 0.0119 | -0.0129 (7) |
| 10-15 | 1139 | 0.1965 | 0.1821 | +0.0144 ± 0.0032 | 0.5773 | 0.5343 | 0.4736 | 0.3491 | 0.3547 | -0.074 ± 0.0126 | -0.0633 (3) |
| 15-25 | 1467 | 0.1995 | 0.1601 | +0.0393 ± 0.0041 | 0.5882 | 0.4779 | 0.4887 | 0.2916 | 0.2897 | -0.083 ± 0.0104 | -0.017 (10) |
| 25-40 | 1385 | 0.2122 | 0.1203 | +0.0919 ± 0.0059 | 0.6161 | 0.3728 | 0.5208 | 0.2068 | 0.2202 | -0.053 ± 0.009 | -0.01 (1) |
| 40+ | 981 | 0.3683 | 0.0399 | +0.3284 ± 0.0071 | 0.9589 | 0.1648 | 0.6181 | 0.1032 | 0.051 | -0.086 ± 0.006 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 156 | 0.187 | 0.1864 | +0.0005 ± 0.0012 | 0.5503 | 0.5474 | 0.494 | 0.4793 | 0.4551 | -0.144 ± 0.0369 | -0.01 (1) |
| 3-5 | 103 | 0.1975 | 0.1972 | +0.0003 ± 0.0035 | 0.5712 | 0.5755 | 0.4925 | 0.4527 | 0.466 | -0.078 ± 0.0471 | 0.02 (1) |
| 5-10 | 256 | 0.1956 | 0.1951 | +0.0005 ± 0.0041 | 0.5747 | 0.5725 | 0.568 | 0.493 | 0.5195 | -0.092 ± 0.0286 | -0.01 (4) |
| 10-15 | 243 | 0.2303 | 0.2176 | +0.0127 ± 0.0075 | 0.6506 | 0.6249 | 0.5812 | 0.4571 | 0.4733 | -0.126 ± 0.0317 | -0.0667 (3) |
| 15-25 | 347 | 0.2205 | 0.2034 | +0.0171 ± 0.0096 | 0.6274 | 0.5867 | 0.5943 | 0.3969 | 0.4582 | -0.095 ± 0.0248 | -0.0167 (3) |
| 25-40 | 226 | 0.2578 | 0.1989 | +0.0589 ± 0.0184 | 0.7173 | 0.5782 | 0.664 | 0.3531 | 0.4115 | -0.128 ± 0.0301 | -0.025 (2) |
| 40+ | 92 | 0.3507 | 0.1819 | +0.1687 ± 0.0441 | 0.9751 | 0.5349 | 0.7556 | 0.2692 | 0.3587 | -0.061 ± 0.0415 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 746 | 0.1685 | 0.1688 | -0.0003 ± 0.0005 | 0.5038 | 0.5045 | 0.5091 | 0.4949 | 0.5067 | -0.060 ± 0.0161 | -0.0217 (6) |
| 3-5 | 514 | 0.1802 | 0.1769 | +0.0033 ± 0.0015 | 0.5304 | 0.5252 | 0.511 | 0.4712 | 0.4494 | -0.076 ± 0.0189 | 0.02 (1) |
| 5-10 | 1174 | 0.1821 | 0.1818 | +0.0003 ± 0.0019 | 0.5411 | 0.5372 | 0.5131 | 0.4385 | 0.471 | -0.041 ± 0.0127 | -0.01 (5) |
| 10-15 | 1058 | 0.1961 | 0.1808 | +0.0154 ± 0.0033 | 0.58 | 0.531 | 0.5126 | 0.3888 | 0.3922 | -0.080 ± 0.0134 | -0.0575 (4) |
| 15-25 | 1548 | 0.2077 | 0.1676 | +0.0401 ± 0.0041 | 0.6067 | 0.4981 | 0.5253 | 0.33 | 0.3282 | -0.087 ± 0.0105 | -0.0143 (7) |
| 25-40 | 1480 | 0.2404 | 0.1295 | +0.1109 ± 0.006 | 0.6829 | 0.3995 | 0.5542 | 0.237 | 0.2196 | -0.089 ± 0.0095 | -0.015 (6) |
| 40+ | 1290 | 0.3966 | 0.068 | +0.3286 ± 0.0083 | 1.0356 | 0.238 | 0.6646 | 0.1266 | 0.1031 | -0.064 ± 0.007 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 219 | 0.1908 | 0.1928 | -0.0021 ± 0.0011 | 0.5603 | 0.5664 | 0.5111 | 0.4962 | 0.5434 | -0.050 ± 0.0299 | -0.01 (5) |
| 3-5 | 153 | 0.1789 | 0.1774 | +0.0015 ± 0.0027 | 0.5319 | 0.5283 | 0.5032 | 0.4641 | 0.4641 | -0.130 ± 0.0365 | -- (0) |
| 5-10 | 303 | 0.1977 | 0.198 | -0.0003 ± 0.0039 | 0.5819 | 0.5786 | 0.5173 | 0.4436 | 0.4785 | -0.091 ± 0.0262 | -0.01 (3) |
| 10-15 | 234 | 0.214 | 0.2169 | -0.0029 ± 0.0075 | 0.6176 | 0.6196 | 0.5435 | 0.4201 | 0.4957 | -0.075 ± 0.0302 | -0.044 (5) |
| 15-25 | 303 | 0.221 | 0.2067 | +0.0144 ± 0.0102 | 0.6381 | 0.5952 | 0.5829 | 0.3886 | 0.4488 | -0.093 ± 0.026 | -0.03 (1) |
| 25-40 | 178 | 0.2026 | 0.2089 | -0.0062 ± 0.02 | 0.5898 | 0.5972 | 0.6503 | 0.3375 | 0.5 | -0.036 ± 0.0292 | 0.0 (1) |
| 40+ | 33 | 0.3471 | 0.1356 | +0.2115 ± 0.058 | 0.918 | 0.43 | 0.7266 | 0.2779 | 0.2727 | -0.196 ± 0.0611 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 875 | 0.1682 | 0.1691 | -0.0009 ± 0.0005 | 0.5057 | 0.5077 | 0.4916 | 0.4768 | 0.5086 | -0.038 ± 0.014 | -0.0162 (13) |
| 3-5 | 618 | 0.1865 | 0.1819 | +0.0046 ± 0.0014 | 0.5497 | 0.5408 | 0.4762 | 0.4371 | 0.3964 | -0.121 ± 0.0179 | -0.01 (2) |
| 5-10 | 1391 | 0.185 | 0.1808 | +0.0042 ± 0.0017 | 0.5523 | 0.5352 | 0.4821 | 0.4084 | 0.4148 | -0.067 ± 0.0114 | -0.01 (3) |
| 10-15 | 1070 | 0.1889 | 0.1805 | +0.0084 ± 0.0032 | 0.5594 | 0.5291 | 0.4828 | 0.3595 | 0.3869 | -0.056 ± 0.0128 | -0.03 (9) |
| 15-25 | 1603 | 0.2017 | 0.1615 | +0.0402 ± 0.004 | 0.5969 | 0.4828 | 0.4933 | 0.2951 | 0.2951 | -0.075 ± 0.0101 | -0.03 (2) |
| 25-40 | 1325 | 0.2132 | 0.1183 | +0.0949 ± 0.006 | 0.6179 | 0.3656 | 0.5195 | 0.2011 | 0.2151 | -0.057 ± 0.009 | 0.0 (1) |
| 40+ | 928 | 0.3829 | 0.0408 | +0.3421 ± 0.0076 | 1.0022 | 0.1677 | 0.6246 | 0.1024 | 0.0474 | -0.087 ± 0.0063 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 495 | 0.2026 | 0.2028 | -0.0002 ± 0.0007 | 0.5863 | 0.5872 | 0.4992 | 0.4843 | 0.4909 | -0.043 ± 0.0202 | -0.0226 (46) |
| 3-5 | 372 | 0.1927 | 0.1929 | -0.0001 ± 0.0018 | 0.567 | 0.5658 | 0.4785 | 0.4388 | 0.4624 | -0.034 ± 0.0225 | -0.0059 (32) |
| 5-10 | 760 | 0.1888 | 0.1841 | +0.0048 ± 0.0024 | 0.5612 | 0.548 | 0.4673 | 0.3936 | 0.3987 | -0.052 ± 0.0158 | -0.005 (72) |
| 10-15 | 505 | 0.2018 | 0.1917 | +0.0100 ± 0.0049 | 0.5921 | 0.5638 | 0.467 | 0.344 | 0.3644 | -0.041 ± 0.0194 | 0.0016 (63) |
| 15-25 | 680 | 0.2364 | 0.212 | +0.0244 ± 0.0069 | 0.6689 | 0.6098 | 0.5362 | 0.3427 | 0.3779 | -0.044 ± 0.0178 | -0.0216 (58) |
| 25-40 | 369 | 0.2496 | 0.1772 | +0.0724 ± 0.0136 | 0.6996 | 0.5255 | 0.5994 | 0.2872 | 0.3252 | -0.066 ± 0.0208 | -0.0216 (25) |
| 40+ | 117 | 0.3747 | 0.1653 | +0.2094 ± 0.0395 | 1.0503 | 0.5022 | 0.7517 | 0.2526 | 0.3162 | -0.051 ± 0.0354 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1182 | 0.1918 | 0.1919 | -0.0001 ± 0.0004 | 0.559 | 0.5593 | 0.4972 | 0.482 | 0.4932 | -0.037 ± 0.0126 | -0.0155 (82) |
| 3-5 | 841 | 0.1845 | 0.1838 | +0.0007 ± 0.0012 | 0.5459 | 0.5441 | 0.49 | 0.4504 | 0.4614 | -0.040 ± 0.0148 | -0.018 (54) |
| 5-10 | 1749 | 0.1838 | 0.1781 | +0.0058 ± 0.0015 | 0.5483 | 0.5311 | 0.4652 | 0.3908 | 0.3922 | -0.054 ± 0.0102 | -0.0089 (122) |
| 10-15 | 1306 | 0.1968 | 0.1852 | +0.0115 ± 0.003 | 0.581 | 0.5475 | 0.4766 | 0.3535 | 0.3675 | -0.046 ± 0.0118 | -0.0053 (99) |
| 15-25 | 1705 | 0.2267 | 0.1939 | +0.0328 ± 0.0042 | 0.6528 | 0.5655 | 0.5265 | 0.331 | 0.3449 | -0.058 ± 0.0108 | -0.0255 (106) |
| 25-40 | 1243 | 0.2388 | 0.1502 | +0.0886 ± 0.0069 | 0.6757 | 0.4533 | 0.564 | 0.249 | 0.2671 | -0.062 ± 0.0107 | -0.0206 (47) |
| 40+ | 612 | 0.3697 | 0.0878 | +0.2819 ± 0.0129 | 1.004 | 0.2908 | 0.6612 | 0.1528 | 0.1405 | -0.070 ± 0.0115 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 1423 | 1.149 ± 0.079 | 1.25 | 0.167 | 0.1667 | 0.2074 | 0.2 |
| gen2 | 1423 | 0.935 ± 0.069 | 1.168 | 0.1826 | 0.1665 | 0.2267 | 0.1999 |
| gen1_elo | 1423 | 1.123 ± 0.077 | 1.229 | 0.1721 | 0.1669 | 0.2063 | 0.1999 |
| gen1_sr | 1423 | 1.172 ± 0.09 | 1.241 | 0.1405 | 0.1685 | 0.222 | 0.2 |
| gen1_ledger | 3298 | 0.934 ± 0.047 | 1.096 | 0.1653 | 0.1942 | 0.2165 | 0.1934 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 8,890)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,490 | 28.0% |
| STALE_QUOTE | market_freshness | 2,087 | 23.5% |
| BOOK_QUALITY | execution | 1,573 | 17.7% |
| POOR_DATA | data | 920 | 10.3% |
| LIMITED_DATA | data | 563 | 6.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 414 | 4.7% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 404 | 4.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 225 | 2.5% |
| IDENTITY_AMBIGUOUS | mapping | 207 | 2.3% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 7 | 0.1% |

Cause class: coverage 28.0%, market_freshness 23.5%, execution 17.7%, data 16.7%, market_freshness/coverage 7.1%, model_calibration_or_unknown 4.7%, mapping 2.3%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 95.9%, LOW_DATA_QUALITY 68.9%, THIN_PLAYER_HISTORY 58.7%, STALE_PLAYER_DATA 58.3%, STALE_KALSHI_QUOTE 51.5%, MODEL_INTERNAL_DISAGREEMENT 37.4%, ASYMMETRIC_SAMPLE_SIZE 31.8%, WIDE_SPREAD 24.4%, MODEL_HIGH_UNCERTAINTY 15.3%, PLAYER_IDENTITY_RISK 10.6%, LEVEL_TRANSFER_RISK 8.4%, LOW_DISPLAYED_LIQUIDITY 7.1%, EVENT_MAPPING_RISK 6.9%, MODEL_CALIBRATION_OUTLIER 2.7%, UNKNOWN 0.5%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 30.0%, POST_SETTLEMENT_OBSERVATION 28.0%, POSSIBLE_IN_PLAY_QUOTE 5.0%, CONFIRMED_IN_PLAY_QUOTE 0.7%

### >= ge_25 pp (N = 4,874)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,955 | 40.1% |
| STALE_QUOTE | market_freshness | 943 | 19.4% |
| BOOK_QUALITY | execution | 815 | 16.7% |
| POOR_DATA | data | 403 | 8.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 223 | 4.6% |
| LIMITED_DATA | data | 170 | 3.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 138 | 2.8% |
| IDENTITY_AMBIGUOUS | mapping | 120 | 2.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 105 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 2 | 0.0% |

Cause class: coverage 40.1%, market_freshness 19.4%, execution 16.7%, data 11.8%, market_freshness/coverage 7.4%, mapping 2.5%, model_calibration_or_unknown 2.1%, model_calibration 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 97.9%, LOW_DATA_QUALITY 71.5%, THIN_PLAYER_HISTORY 60.8%, STALE_KALSHI_QUOTE 58.9%, STALE_PLAYER_DATA 54.5%, MODEL_INTERNAL_DISAGREEMENT 39.8%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 23.4%, MODEL_HIGH_UNCERTAINTY 16.6%, PLAYER_IDENTITY_RISK 13.2%, EVENT_MAPPING_RISK 7.7%, LEVEL_TRANSFER_RISK 7.6%, LOW_DISPLAYED_LIQUIDITY 7.4%, MODEL_CALIBRATION_OUTLIER 3.4%, UNKNOWN 0.1%, EXTERNAL_MARKET_REJECTION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 42.4%, POST_SETTLEMENT_OBSERVATION 40.1%, POSSIBLE_IN_PLAY_QUOTE 5.1%, CONFIRMED_IN_PLAY_QUOTE 0.8%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 4083, "IDENTITY_AMBIGUOUS": 791}; ticker orientation: {"VERIFIED": 4874}.

Checks: discipline:AMBIGUOUS 227, discipline:PASS 4647, identity_confidence:AMBIGUOUS 643, identity_confidence:PASS 4231, level_mapping:NA 239, level_mapping:PASS 4635, market_pair:AMBIGUOUS 181, market_pair:NA 119, market_pair:PASS 4574, model_complement:NA 88, model_complement:PASS 4786, namesake:PASS 4874, physical_match_id:NA 2073, physical_match_id:PASS 2801, player_ids:PASS 4874, same_pair_other_event:PASS 4874, ticker_orientation:PASS 4874

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,161 | 2.0% | 2.0% | 0.5% | {"market_freshness": 20, "execution": 3} | 5.62 | 0.1932 / 0.1842 (79) | 22.0% | 0.2% | 6.1% | 1.5% |
| CHALLENGER | 3,362 | 19.1% | 6.7% | 13.2% | {"coverage": 397, "market_freshness": 106, "market_freshness/coverage": 73, "model_calibration_or_unknown": 37, "data": 25, "execution": 4} | 6.94 | 0.2204 / 0.2034 (792) | 48.6% | 5.3% | 1.4% | 23.8% |
| DOUBLES | 518 | 43.8% | 43.4% | 4.7% | {"market_freshness": 106, "execution": 58, "mapping": 42, "market_freshness/coverage": 14, "coverage": 7} | 22.7 | 0.3152 / 0.2262 (172) | 45.2% | 0.0% | 100.0% | 8.3% |
| ITF_MEN | 6,352 | 25.3% | 17.5% | 33.0% | {"coverage": 652, "execution": 358, "market_freshness": 252, "data": 221, "market_freshness/coverage": 104, "mapping": 19, "model_calibration_or_unknown": 1} | 11.17 | 0.2156 / 0.1927 (1563) | 42.0% | 56.4% | 6.6% | 23.5% |
| ITF_WOMEN | 8,037 | 27.0% | 18.8% | 44.5% | {"coverage": 882, "market_freshness": 402, "execution": 375, "data": 303, "market_freshness/coverage": 129, "mapping": 53, "model_calibration_or_unknown": 22, "model_calibration": 2} | 12.41 | 0.2012 / 0.1908 (1683) | 43.3% | 60.4% | 10.9% | 23.5% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 935 | 8.5% | 7.3% | 1.6% | {"market_freshness": 34, "model_calibration_or_unknown": 16, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.39 | 0.2026 / 0.197 (137) | 35.4% | 2.2% | 1.3% | 3.4% |
| WTA125 | 746 | 15.6% | 11.2% | 2.4% | {"market_freshness/coverage": 31, "model_calibration_or_unknown": 27, "market_freshness": 21, "data": 13, "coverage": 12, "execution": 8, "mapping": 4} | 10.08 | 0.2208 / 0.2064 (253) | 28.4% | 5.8% | 4.0% | 12.6% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 3 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 4 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 17.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1037 min (STALE); no external reference |
| 5 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 6 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 7 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 8 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 9 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 10 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 11 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 12 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 13 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 14% | +77 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 14 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 15 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 16 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 17 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 18 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 19 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 20 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 21 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 22 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 23 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 24 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 25 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 26 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 27 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 28 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 253 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 29 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 30 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 31 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 32 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 33 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 34 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.2h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 141 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 35 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 36 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 37 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 66 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 38 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 39 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 40 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 41 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 42 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 43 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.9h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 671 min (STALE); no external reference |
| 44 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 732 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 45 | `KXWTAMATCH-26OCT01YASCHW-CHW` | WTA | fair_v1 | 73% / 2% | +70 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 51 min (STALE); no external reference |
| 46 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 47 | `KXATPCHALLENGERMATCH-26OCT05CASMUN-CAS` | CHALLENGER | fair_v1 | 83% / 14% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 192 min (STALE); data POOR (grade D, thinner serve sample 814.0, ratio 3.76); no external reference |
| 48 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 49 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9791, "by_level_share_of_ge_25pp": {"ATP": 0.0047, "CHALLENGER": 0.1317, "DOUBLES": 0.0466, "ITF_MEN": 0.3297, "ITF_WOMEN": 0.4448, "OTHER": 0.0025, "WTA": 0.0162, "WTA125": 0.0238}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5886, "share_primary_cause_market_settled_or_in_play": 0.4752, "share_primary_cause_stale_quote_only": 0.1935}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 4874, "identity_ambiguous_share": 0.1623, "ticker_orientation": {"VERIFIED": 4874}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 2801, "with_external": 24, "coverage": 0.0086, "external_status": {"EXTERNAL_STALE": 23, "AGREES_WITH_KALSHI": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 23, "MODEL_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.0417, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 1284, "with_external": 24, "coverage": 0.0187, "external_status": {"EXTERNAL_STALE": 23, "AGREES_WITH_KALSHI": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 23, "MODEL_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.0417, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 596.0, "median_sample_ratio": 2.38, "median_min_matches": 19.0, "median_max_days_since_last": 197.0, "share_severe_asymmetry": 0.1859, "data_status": {"POOR": 2627, "LIMITED": 1361, "ADEQUATE": 886}, "comparison_lt_10pp": {"median_thinner_serve_points": 1754.0, "median_sample_ratio": 1.76, "median_min_matches": 74.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 318, "model_minus_observed": 0.0772, "kalshi_minus_observed": -0.0557, "brier_diff_model_minus_kalshi": 0.002}, "4-10x": {"n": 231, "model_minus_observed": 0.0522, "kalshi_minus_observed": -0.0865, "brier_diff_model_minus_kalshi": 0.0007}, "<2x": {"n": 660, "model_minus_observed": 0.0798, "kalshi_minus_observed": -0.0448, "brier_diff_model_minus_kalshi": 0.0109}, ">=10x": {"n": 214, "model_minus_observed": 0.0995, "kalshi_minus_observed": -0.0737, "brier_diff_model_minus_kalshi": 0.012}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 1423, "model": {"intercept": -0.607, "slope": 0.935, "slope_se": 0.069}, "kalshi_mid_same_rows": {"intercept": 0.227, "slope": 1.168, "slope_se": 0.078}, "mean_extremity_model": 0.1826, "mean_extremity_kalshi": 0.1665, "model_brier": 0.2267, "kalshi_brier": 0.1999, "brier_diff_model_minus_kalshi": 0.0268, "brier_diff_se": 0.0051, "model_logloss": 0.6461, "kalshi_logloss": 0.5809}, "fair_v1": {"n": 1423, "model": {"intercept": -0.403, "slope": 1.149, "slope_se": 0.079}, "kalshi_mid_same_rows": {"intercept": 0.372, "slope": 1.25, "slope_se": 0.081}, "mean_extremity_model": 0.167, "mean_extremity_kalshi": 0.1667, "model_brier": 0.2074, "kalshi_brier": 0.2, "brier_diff_model_minus_kalshi": 0.0074, "brier_diff_se": 0.004, "model_logloss": 0.6005, "kalshi_logloss": 0.5809}, "gen1_elo": {"n": 1423, "model": {"intercept": -0.38, "slope": 1.123, "slope_se": 0.077}, "kalshi_mid_same_rows": {"intercept": 0.367, "slope": 1.229, "slope_se": 0.08}, "mean_extremity_model": 0.1721, "mean_extremity_kalshi": 0.1669, "model_brier": 0.2063, "kalshi_brier": 0.1999, "brier_diff_model_minus_kalshi": 0.0065, "brier_diff_se": 0.004, "model_logloss": 0.5998, "kalshi_logloss": 0.5805}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2543, "share_ge_15": 0.4399, "median_abs_gap": 13.04, "n": 11016}, "gen1_elo": {"share_ge_25": 0.2441, "share_ge_15": 0.4379, "median_abs_gap": 12.66, "n": 11016}, "gen1_sr": {"share_ge_25": 0.3036, "share_ge_15": 0.5216, "median_abs_gap": 15.8, "n": 11016}, "gen2": {"share_ge_25": 0.3095, "share_ge_15": 0.5088, "median_abs_gap": 15.41, "n": 11016}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1529, "share_ge_15": 0.3439, "median_abs_gap": 10.54, "n": 8400}, "gen1_elo": {"share_ge_25": 0.1467, "share_ge_15": 0.3394, "median_abs_gap": 10.12, "n": 8400}, "gen1_sr": {"share_ge_25": 0.2025, "share_ge_15": 0.4354, "median_abs_gap": 12.97, "n": 8400}, "gen2": {"share_ge_25": 0.2236, "share_ge_15": 0.4335, "median_abs_gap": 12.79, "n": 8400}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.62, "share_ge_25_all": 0.0198, "share_ge_25_pregame_clean": 0.0201}, "WTA": {"median_abs_gap_pregame_clean": 8.39, "share_ge_25_all": 0.0845, "share_ge_25_pregame_clean": 0.0731}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2304, "share_within_10pp_all": 0.428, "share_within_10pp_pregame_clean": 0.4919, "corr_model_vs_mid_pregame_clean": 0.8449}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 212, "model_brier": 0.1833, "kalshi_brier": 0.184, "brier_diff_model_minus_kalshi": -0.0008}, "10-15": {"n_settled": 244, "model_brier": 0.2209, "kalshi_brier": 0.2175, "brier_diff_model_minus_kalshi": 0.0034}, "15-25": {"n_settled": 310, "model_brier": 0.2177, "kalshi_brier": 0.2098, "brier_diff_model_minus_kalshi": 0.0079}, "25-40": {"n_settled": 175, "model_brier": 0.2106, "kalshi_brier": 0.1996, "brier_diff_model_minus_kalshi": 0.011}, "3-5": {"n_settled": 143, "model_brier": 0.1817, "kalshi_brier": 0.1835, "brier_diff_model_minus_kalshi": -0.0018}, "40+": {"n_settled": 39, "model_brier": 0.3105, "kalshi_brier": 0.1436, "brier_diff_model_minus_kalshi": 0.1669}, "5-10": {"n_settled": 300, "model_brier": 0.2, "kalshi_brier": 0.2024, "brier_diff_model_minus_kalshi": -0.0024}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%)
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap).
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 172, "model_brier": 0.3152, "kalshi_brier": 0.2262, "brier_diff_model_minus_kalshi": 0.0891, "brier_diff_se": 0.0246, "corr_model_outcome": -0.0687, "corr_kalshi_outcome": 0.3509}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
