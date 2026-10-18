# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-18T21:39Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 39,315): 0-3 14.5%, 3-5 9.5%, 5-10 19.9%, 10-15 15.4%, 15-25 18.9%, 25-40 13.7%, 40+ 8.2%; median gap 11.88 pp.
* **Where the extremes live**: 97.6% of >=25 pp gaps are off the ATP/WTA main tour (ITF 75.6%, Challenger 12.4%, doubles 7.4%). Main tour: ATP 3.4% and WTA 5.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 8,590): MARKET_ALREADY_SETTLED_WHEN_PRICED 35.5%, BOOK_QUALITY 19.1%, STALE_QUOTE 17.8%, POOR_DATA 8.5%, POSSIBLY_IN_PLAY_QUOTE 5.2%, IDENTITY_AMBIGUOUS 4.2%, LIMITED_DATA 3.8%, IN_PLAY_QUOTE 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.5%. By class: coverage 35.5%, execution 19.1%, market_freshness 17.8%, data 12.3%, market_freshness/coverage 8.5%, mapping 4.2%, model_calibration_or_unknown 1.9%, model_calibration 0.5%.
* **Stale / settled / in-play**: 52.3% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 44.0% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 8,590 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.8% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.1%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 23.3% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 535.0 points vs 1833.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.058, Gen-2 0.841, Gen-1 ledger 0.883 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 409 model 0.2195 vs Kalshi 0.2107; n 84 model 0.2967 vs Kalshi 0.1739.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 164,691 model-market comparisons (268,638 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 58,876 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-18T21:27:18.216273+00:00'], shadow board 43,591 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-18T21:27:23.721626+00:00'], Model 4 19,466 rows, 16,239 settled tickers, 5,468 tickers with an external scan.
* By model: {"gen1_ledger": 39737, "gen1_elo": 21923, "fair_v1": 21923, "gen2": 21923, "gen1_sr": 21923, "model4_fundamental": 18640, "model4_conditioned": 18622}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 39,315 | 14.5 | 9.5 | 19.9 | 15.4 | 18.9 | 13.7 | 8.2 | 11.88 | 40.8% | 21.9% |
| MW fair_v1 | 21,923 | 13.5 | 8.5 | 18.5 | 15.9 | 19.2 | 14.6 | 9.8 | 12.96 | 43.6% | 24.3% |
| MW gen1_elo | 21,923 | 13.1 | 9.1 | 19.4 | 15.2 | 19.4 | 14.4 | 9.4 | 12.54 | 43.2% | 23.8% |
| MW gen1_ledger | 17,392 | 15.6 | 10.8 | 21.6 | 14.8 | 18.5 | 12.6 | 6.2 | 10.48 | 37.2% | 18.7% |
| MW gen1_sr | 21,923 | 9.7 | 7.3 | 16.7 | 14.2 | 21.4 | 18.4 | 12.1 | 15.68 | 51.9% | 30.5% |
| MW gen2 | 21,923 | 11.4 | 7.1 | 16.5 | 14.2 | 19.9 | 17.5 | 13.3 | 15.38 | 50.7% | 30.8% |
| all families model4_conditioned | 18,622 | 21.7 | 19.0 | 34.5 | 17.4 | 4.8 | 1.5 | 1.2 | 5.96 | 7.4% | 2.7% |
| all families model4_fundamental | 18,640 | 16.2 | 12.9 | 34.7 | 20.1 | 11.2 | 3.4 | 1.4 | 7.89 | 16.0% | 4.9% |

Configurable thresholds (primary): >=5pp 76.0%, >=10pp 56.1%, >=15pp 40.8%, >=20pp 30.3%, >=25pp 21.9%, >=30pp 15.8%, >=40pp 8.2%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.18pp; >=10pp 44.5%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,832 | 29.5 | 13.3 | 24.4 | 17.0 | 11.7 | 3.4 | 0.7 | 6.21 | 15.7% | 4.0% |
| CHALLENGER | 3,648 | 15.8 | 10.0 | 20.2 | 15.7 | 14.6 | 12.5 | 11.2 | 11.32 | 38.3% | 23.7% |
| ITF_MEN | 5,946 | 11.0 | 8.0 | 17.3 | 14.9 | 19.9 | 16.3 | 12.5 | 14.54 | 48.8% | 28.8% |
| ITF_WOMEN | 8,558 | 10.2 | 6.8 | 15.8 | 15.6 | 22.4 | 18.2 | 11.1 | 15.64 | 51.7% | 29.3% |
| WTA | 1,279 | 18.8 | 12.2 | 25.3 | 19.1 | 19.1 | 4.6 | 0.9 | 8.22 | 24.6% | 5.5% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,832 | 23.9 | 14.4 | 24.3 | 18.1 | 14.1 | 4.3 | 1.0 | 6.9 | 19.4% | 5.2% |
| CHALLENGER | 3,648 | 14.7 | 8.1 | 18.9 | 13.6 | 18.0 | 14.4 | 12.3 | 12.87 | 44.7% | 26.7% |
| ITF_MEN | 5,946 | 9.3 | 6.7 | 15.7 | 13.6 | 19.8 | 19.3 | 15.7 | 17.02 | 54.8% | 35.0% |
| ITF_WOMEN | 8,558 | 8.4 | 5.5 | 13.7 | 13.6 | 21.1 | 20.7 | 16.9 | 18.86 | 58.8% | 37.7% |
| WTA | 1,279 | 16.9 | 8.1 | 20.3 | 16.4 | 22.6 | 14.7 | 0.9 | 11.5 | 38.2% | 15.6% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,832 | 25.2 | 13.6 | 25.7 | 17.0 | 13.7 | 4.2 | 0.7 | 6.75 | 18.6% | 4.9% |
| CHALLENGER | 3,648 | 14.8 | 10.1 | 20.7 | 14.9 | 15.8 | 12.2 | 11.5 | 11.17 | 39.5% | 23.7% |
| ITF_MEN | 5,946 | 10.0 | 8.1 | 17.8 | 14.1 | 20.8 | 16.8 | 12.5 | 15.0 | 50.0% | 29.2% |
| ITF_WOMEN | 8,558 | 9.6 | 7.0 | 16.3 | 15.6 | 23.0 | 18.3 | 10.3 | 15.59 | 51.6% | 28.6% |
| WTA | 1,279 | 23.8 | 17.2 | 30.6 | 15.1 | 10.9 | 1.9 | 0.6 | 6.0 | 13.4% | 2.5% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,121 | 27.6 | 20.2 | 31.7 | 11.6 | 6.4 | 2.3 | 0.1 | 5.23 | 8.8% | 2.4% |
| CHALLENGER | 2,531 | 22.1 | 15.2 | 26.6 | 14.3 | 14.0 | 5.9 | 1.9 | 7.07 | 21.9% | 7.8% |
| DOUBLES | 1,297 | 4.7 | 4.3 | 10.2 | 10.9 | 21.1 | 25.7 | 23.1 | 24.15 | 69.8% | 48.8% |
| ITF_MEN | 4,964 | 14.5 | 8.7 | 20.7 | 15.8 | 21.0 | 12.4 | 7.0 | 11.86 | 40.4% | 19.4% |
| ITF_WOMEN | 5,678 | 11.8 | 9.1 | 19.1 | 14.8 | 22.1 | 16.9 | 6.2 | 13.17 | 45.1% | 23.1% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 920 | 22.6 | 15.8 | 29.4 | 17.5 | 10.4 | 4.0 | 0.3 | 6.81 | 14.8% | 4.3% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,793 | 29.7 | 13.4 | 24.8 | 16.9 | 11.5 | 3.1 | 0.7 | 6.13 | 15.2% | 3.7% |
| CHALLENGER | 2,601 | 20.5 | 12.6 | 25.4 | 18.1 | 14.8 | 6.5 | 2.2 | 8.23 | 23.4% | 8.6% |
| ITF_MEN | 4,301 | 13.6 | 9.9 | 20.8 | 16.8 | 20.2 | 13.1 | 5.5 | 11.56 | 38.9% | 18.6% |
| ITF_WOMEN | 6,389 | 12.0 | 8.1 | 18.0 | 17.7 | 23.9 | 15.4 | 4.9 | 13.33 | 44.2% | 20.3% |
| WTA | 1,253 | 19.0 | 11.7 | 25.5 | 19.1 | 19.2 | 4.5 | 0.9 | 8.24 | 24.7% | 5.4% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,793 | 24.0 | 14.6 | 24.4 | 18.1 | 14.0 | 4.1 | 0.8 | 6.76 | 18.9% | 4.9% |
| CHALLENGER | 2,601 | 18.8 | 10.3 | 23.6 | 16.4 | 18.6 | 9.5 | 2.7 | 9.26 | 30.8% | 12.3% |
| ITF_MEN | 4,302 | 11.0 | 8.0 | 18.1 | 15.4 | 22.0 | 17.0 | 8.5 | 14.12 | 47.4% | 25.4% |
| ITF_WOMEN | 6,389 | 9.4 | 6.3 | 15.2 | 15.0 | 23.2 | 20.2 | 10.7 | 16.58 | 54.2% | 31.0% |
| WTA | 1,253 | 16.8 | 8.1 | 20.4 | 16.4 | 22.6 | 14.8 | 1.0 | 11.62 | 38.4% | 15.8% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,088 | 27.9 | 20.4 | 31.9 | 11.8 | 5.9 | 2.1 | 0.1 | 5.11 | 8.1% | 2.2% |
| CHALLENGER | 2,189 | 23.8 | 16.5 | 28.4 | 14.1 | 13.3 | 3.4 | 0.6 | 6.45 | 17.3% | 4.0% |
| DOUBLES | 1,204 | 4.7 | 4.5 | 10.4 | 11.1 | 20.9 | 25.8 | 22.6 | 24.07 | 69.3% | 48.4% |
| ITF_MEN | 4,105 | 15.9 | 9.4 | 22.6 | 16.7 | 20.7 | 10.6 | 4.1 | 10.6 | 35.4% | 14.7% |
| ITF_WOMEN | 4,686 | 12.6 | 9.8 | 20.7 | 15.6 | 22.3 | 15.6 | 3.4 | 11.9 | 41.3% | 19.0% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 881 | 22.9 | 16.2 | 29.6 | 17.5 | 10.6 | 3.2 | 0.0 | 6.68 | 13.7% | 3.2% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,297 | 4.7 | 4.3 | 10.2 | 10.9 | 21.1 | 25.7 | 23.1 | 24.15 | 69.8% | 48.8% |
| singles | 16,095 | 16.5 | 11.3 | 22.5 | 15.1 | 18.3 | 11.5 | 4.8 | 9.9 | 34.5% | 16.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 5,029 | 13.5 | 8.9 | 19.3 | 15.9 | 18.1 | 14.5 | 9.8 | 12.67 | 42.5% | 24.4% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 14,141 | 13.9 | 8.5 | 18.4 | 15.5 | 19.6 | 14.4 | 9.7 | 12.98 | 43.7% | 24.1% |
| UNKNOWN | 2,516 | 12.0 | 7.8 | 17.2 | 18.1 | 19.2 | 15.8 | 10.1 | 13.18 | 45.0% | 25.8% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,436 | 19.9 | 10.8 | 21.4 | 17.3 | 15.7 | 8.7 | 6.2 | 9.37 | 30.6% | 14.9% |
| B | 2,828 | 13.2 | 9.2 | 19.9 | 16.6 | 18.3 | 12.1 | 10.8 | 12.12 | 41.1% | 22.8% |
| C | 3,186 | 12.7 | 9.3 | 19.4 | 14.5 | 19.2 | 14.9 | 10.0 | 12.8 | 44.1% | 24.9% |
| D | 3,682 | 12.4 | 7.9 | 17.2 | 15.6 | 21.8 | 15.6 | 9.6 | 13.91 | 47.0% | 25.1% |
| F | 5,791 | 7.9 | 5.5 | 14.9 | 14.9 | 22.0 | 21.6 | 13.2 | 17.85 | 56.8% | 34.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,127 | 23.3 | 15.9 | 28.8 | 15.2 | 11.2 | 4.1 | 1.5 | 6.61 | 16.7% | 5.5% |
| B | 2,479 | 15.4 | 10.1 | 23.8 | 16.4 | 19.3 | 11.0 | 4.1 | 10.14 | 34.3% | 15.0% |
| C | 3,510 | 11.3 | 7.6 | 17.6 | 14.2 | 21.6 | 16.4 | 11.2 | 14.61 | 49.2% | 27.6% |
| D | 2,533 | 14.1 | 9.9 | 20.3 | 13.7 | 20.8 | 14.5 | 6.6 | 12.04 | 41.9% | 21.1% |
| F | 3,743 | 10.2 | 7.9 | 14.8 | 14.4 | 23.4 | 20.3 | 8.9 | 16.15 | 52.6% | 29.2% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 7,306 | 18.0 | 9.8 | 20.6 | 17.1 | 16.2 | 9.6 | 8.7 | 10.46 | 34.4% | 18.3% |
| LIMITED | 4,953 | 14.5 | 10.4 | 20.4 | 15.3 | 18.7 | 13.2 | 7.5 | 11.41 | 39.4% | 20.7% |
| POOR | 9,664 | 9.7 | 6.6 | 15.9 | 15.2 | 21.9 | 19.1 | 11.8 | 15.97 | 52.7% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,317 | 27.1 | 21.9 | 35.0 | 11.0 | 3.6 | 1.2 | 0.2 | 5.06 | 4.9% | 1.3% |
| GAME_SPREAD | 3,787 | 23.9 | 15.5 | 34.5 | 17.4 | 6.9 | 1.6 | 0.2 | 6.34 | 8.6% | 1.8% |
| MATCH_WINNER | 17,392 | 15.6 | 10.8 | 21.6 | 14.8 | 18.5 | 12.6 | 6.2 | 10.48 | 37.2% | 18.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 8,087 | 30.5 | 17.9 | 30.5 | 12.2 | 7.3 | 1.2 | 0.4 | 5.18 | 9.0% | 1.6% |
| TOTAL_GAMES | 6,130 | 7.2 | 8.8 | 37.1 | 28.8 | 11.4 | 3.6 | 3.1 | 9.65 | 18.1% | 6.7% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,533 | 25.1 | 34.7 | 32.3 | 3.5 | 3.5 | 0.6 | 0.2 | 4.47 | 4.4% | 0.8% |
| GAME_SPREAD | 4,480 | 45.9 | 16.9 | 27.5 | 7.1 | 1.7 | 0.7 | 0.3 | 3.44 | 2.7% | 0.9% |
| TOTAL_GAMES | 7,609 | 4.5 | 6.7 | 40.6 | 35.3 | 7.6 | 2.7 | 2.5 | 9.83 | 12.8% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,536 | 24.5 | 17.6 | 36.0 | 11.8 | 7.0 | 2.6 | 0.4 | 5.82 | 10.0% | 2.9% |
| GAME_SPREAD | 4,483 | 19.3 | 13.6 | 28.8 | 19.9 | 13.7 | 3.7 | 0.9 | 7.85 | 18.3% | 4.7% |
| TOTAL_GAMES | 7,621 | 7.2 | 8.6 | 37.0 | 27.4 | 13.2 | 4.0 | 2.7 | 9.7 | 19.9% | 6.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 21,923 | 43.6% | 24.3% | 12.96 | 34.8% | 15.0% | 10.66 |
| gen1_elo | 21,923 | 43.2% | 23.8% | 12.54 | 34.1% | 14.8% | 10.18 |
| gen1_sr | 21,923 | 51.9% | 30.5% | 15.68 | 44.1% | 21.2% | 13.04 |
| gen2 | 21,923 | 50.7% | 30.8% | 15.38 | 44.0% | 22.7% | 13.0 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 11,686 | 16.4 | 10.4 | 21.5 | 17.4 | 19.6 | 11.4 | 3.3 | 10.5 | 34.3% | 14.7% |
| STALE | 10,237 | 10.3 | 6.4 | 15.1 | 14.1 | 18.8 | 18.2 | 17.2 | 17.15 | 54.1% | 35.4% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 10,860 | 17.1 | 11.6 | 22.7 | 14.8 | 17.3 | 11.6 | 4.9 | 9.65 | 33.8% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 39,315 | 10860 | 15158 | 13297 | 23.7 | 143.1 | 1400.4 |
| ge_15pp | 16,023 | 3668 | 5302 | 7053 | 25.8 | 449.2 | 1380.4 |
| ge_25pp | 8,590 | 1792 | 2308 | 4490 | 32.9 | 584.3 | 1380.4 |
| lt_10pp | 17,241 | 5585 | 7270 | 4386 | 21.8 | 47.9 | 1341.5 |

Current slate `SL-20261018T213937Z-a0540083`: 814 priced rows, quote age at build {'median': 12.6, 'max': 12.7}, freshness {'AGING': 814}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 11 | 0.0 | 0.0 | 36.4 | 0.0 | 45.5 | 18.2 | 0.0 | 20.19 | 63.6% | 18.2% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,013 | 21.3 | 10.6 | 23.5 | 19.1 | 18.4 | 6.6 | 0.5 | 8.65 | 25.5% | 7.1% |
| KALSHI_LONE_OUTLIER | 11 | 9.1 | 0.0 | 72.7 | 0.0 | 9.1 | 9.1 | 0.0 | 5.2 | 18.2% | 9.1% |
| MARKETS_AGREE | 355 | 70.1 | 29.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.1 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 731 | 0.0 | 2.9 | 35.6 | 28.4 | 23.1 | 9.3 | 0.7 | 11.92 | 33.1% | 10.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 21,923 | 3133 (14.3%) | 23.3% | 0.7% | {"EXTERNAL_STALE": 2013, "AGREES_WITH_KALSHI": 731, "ALL_AGREE": 355, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 11, "SUPPORTS_MODEL_DIRECTION": 10, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 9,556 | 765 (8.0%) | 31.6% | 1.2% | {"EXTERNAL_STALE": 514, "AGREES_WITH_KALSHI": 242, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 5,336 | 219 (4.1%) | 33.3% | 1.4% | {"EXTERNAL_STALE": 143, "AGREES_WITH_KALSHI": 73, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,552 | 207 (8.1%) | 34.3% | 1.5% | {"EXTERNAL_STALE": 133, "AGREES_WITH_KALSHI": 71, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 8,887 | 1776 (20.0%) | 15.8% | 0.7% | {"EXTERNAL_STALE": 1115, "ALL_AGREE": 355, "AGREES_WITH_KALSHI": 281, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 9, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 4,215 | 11.2 | 7.8 | 19.3 | 15.0 | 21.4 | 15.2 | 10.1 | 13.77 | 46.6% | 25.2% |
| 4-10x | 2,845 | 12.3 | 8.9 | 19.0 | 15.6 | 19.4 | 15.3 | 9.5 | 13.01 | 44.1% | 24.8% |
| <2x | 11,398 | 15.6 | 9.3 | 19.0 | 16.9 | 17.7 | 12.7 | 8.8 | 11.75 | 39.2% | 21.5% |
| >=10x | 3,465 | 10.7 | 6.4 | 15.3 | 13.8 | 21.6 | 19.5 | 12.6 | 16.44 | 53.7% | 32.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 5,673 | 13.1 | 8.5 | 19.4 | 16.0 | 19.6 | 13.2 | 10.3 | 12.81 | 43.0% | 23.5% |
| 300-1000 | 4,864 | 12.2 | 8.7 | 17.0 | 15.7 | 20.6 | 16.2 | 9.5 | 13.72 | 46.3% | 25.7% |
| <300 | 6,595 | 9.0 | 6.0 | 15.5 | 14.8 | 21.8 | 20.2 | 12.8 | 16.92 | 54.8% | 33.0% |
| >=3000 | 4,791 | 21.7 | 11.9 | 22.9 | 17.4 | 14.0 | 6.9 | 5.2 | 8.18 | 26.1% | 12.1% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 670 | 0.5413 | 0.4066 | 0.4881 | +0.053 | -0.081 | -0.0002 ± 0.0058 |
| ratio 4-10x | 453 | 0.5887 | 0.4476 | 0.5143 | +0.074 | -0.067 | 0.0071 ± 0.0074 |
| ratio <2x | 1663 | 0.5379 | 0.4166 | 0.4504 | +0.087 | -0.034 | 0.0124 ± 0.0035 |
| ratio >=10x | 557 | 0.5593 | 0.3875 | 0.4434 | +0.116 | -0.056 | 0.0115 ± 0.0076 |
| thinner_sample 1000-3000 | 933 | 0.5431 | 0.4171 | 0.4609 | +0.082 | -0.044 | 0.0083 ± 0.0047 |
| thinner_sample 300-1000 | 795 | 0.5643 | 0.4243 | 0.4943 | +0.070 | -0.070 | 0.0005 ± 0.0056 |
| thinner_sample <300 | 1039 | 0.5524 | 0.3898 | 0.4495 | +0.103 | -0.060 | 0.0133 ± 0.0054 |
| thinner_sample >=3000 | 576 | 0.5314 | 0.4383 | 0.4618 | +0.070 | -0.024 | 0.0142 ± 0.0048 |
| data_status ADEQUATE | 977 | 0.5343 | 0.4297 | 0.4555 | +0.079 | -0.026 | 0.0114 ± 0.004 |
| data_status LIMITED | 830 | 0.5536 | 0.4237 | 0.4892 | +0.064 | -0.066 | 0.0036 ± 0.0051 |
| data_status POOR | 1536 | 0.5559 | 0.3987 | 0.459 | +0.097 | -0.060 | 0.0104 ± 0.0044 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 513 | 0.1954 | 0.1967 | -0.0013 ± 0.0007 | 0.5695 | 0.5721 | 0.4955 | 0.4806 | 0.5302 | -0.049 ± 0.0205 | -0.01 (5) |
| 3-5 | 321 | 0.1972 | 0.1966 | +0.0005 ± 0.002 | 0.576 | 0.5734 | 0.5059 | 0.466 | 0.4798 | -0.081 ± 0.0253 | 0.02 (1) |
| 5-10 | 697 | 0.199 | 0.1984 | +0.0006 ± 0.0026 | 0.5834 | 0.5801 | 0.5128 | 0.4383 | 0.4663 | -0.088 ± 0.0175 | -0.0167 (6) |
| 10-15 | 593 | 0.2151 | 0.2063 | +0.0088 ± 0.0047 | 0.6203 | 0.5947 | 0.5222 | 0.398 | 0.4233 | -0.092 ± 0.0187 | -0.048 (5) |
| 15-25 | 726 | 0.2279 | 0.2127 | +0.0152 ± 0.0067 | 0.6498 | 0.6106 | 0.5797 | 0.3845 | 0.4435 | -0.089 ± 0.017 | -0.0033 (9) |
| 25-40 | 409 | 0.2195 | 0.2107 | +0.0088 ± 0.0134 | 0.6269 | 0.6044 | 0.6543 | 0.3461 | 0.4866 | -0.061 ± 0.0204 | -0.01 (1) |
| 40+ | 84 | 0.2967 | 0.1739 | +0.1228 ± 0.0408 | 0.801 | 0.521 | 0.7529 | 0.3035 | 0.3929 | -0.119 ± 0.0388 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2429 | 0.1815 | 0.1828 | -0.0013 ± 0.0003 | 0.538 | 0.5394 | 0.4796 | 0.4645 | 0.5035 | -0.018 ± 0.0088 | -0.0129 (17) |
| 3-5 | 1521 | 0.194 | 0.1921 | +0.0019 ± 0.0009 | 0.5687 | 0.56 | 0.4781 | 0.4384 | 0.4326 | -0.063 ± 0.0114 | 0.0 (2) |
| 5-10 | 3280 | 0.1931 | 0.19 | +0.0031 ± 0.0011 | 0.568 | 0.5582 | 0.4848 | 0.411 | 0.4247 | -0.051 ± 0.0077 | -0.0119 (21) |
| 10-15 | 2906 | 0.2024 | 0.1839 | +0.0184 ± 0.002 | 0.5925 | 0.5404 | 0.4832 | 0.3585 | 0.3472 | -0.075 ± 0.0079 | -0.0281 (16) |
| 15-25 | 3506 | 0.2081 | 0.171 | +0.0371 ± 0.0027 | 0.6077 | 0.5058 | 0.5026 | 0.3065 | 0.3109 | -0.069 ± 0.0069 | -0.0025 (44) |
| 25-40 | 2746 | 0.2212 | 0.1268 | +0.0944 ± 0.0042 | 0.636 | 0.3903 | 0.5315 | 0.2184 | 0.2283 | -0.064 ± 0.0065 | -0.01 (1) |
| 40+ | 1841 | 0.3777 | 0.0425 | +0.3352 ± 0.0054 | 0.9826 | 0.1689 | 0.628 | 0.106 | 0.0565 | -0.086 ± 0.0044 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 381 | 0.2015 | 0.202 | -0.0005 ± 0.0008 | 0.5852 | 0.5864 | 0.5022 | 0.4872 | 0.5092 | -0.084 ± 0.0244 | -0.01 (3) |
| 3-5 | 274 | 0.2147 | 0.2142 | +0.0004 ± 0.0023 | 0.6125 | 0.6123 | 0.5154 | 0.4755 | 0.4854 | -0.086 ± 0.0295 | 0.02 (1) |
| 5-10 | 603 | 0.1987 | 0.1981 | +0.0006 ± 0.0027 | 0.5809 | 0.5793 | 0.5456 | 0.4708 | 0.5041 | -0.076 ± 0.0187 | -0.01 (4) |
| 10-15 | 551 | 0.2184 | 0.2121 | +0.0063 ± 0.0049 | 0.6272 | 0.6105 | 0.5685 | 0.4443 | 0.4846 | -0.093 ± 0.0204 | -0.04 (5) |
| 15-25 | 801 | 0.2293 | 0.2084 | +0.0209 ± 0.0064 | 0.6504 | 0.5992 | 0.5895 | 0.3932 | 0.4419 | -0.093 ± 0.0164 | -0.0133 (9) |
| 25-40 | 538 | 0.2669 | 0.1974 | +0.0695 ± 0.0121 | 0.7439 | 0.5757 | 0.6647 | 0.3494 | 0.3978 | -0.123 ± 0.019 | -0.0075 (4) |
| 40+ | 195 | 0.3643 | 0.1773 | +0.1870 ± 0.0299 | 1.0151 | 0.5257 | 0.7432 | 0.2602 | 0.3231 | -0.073 ± 0.0289 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2056 | 0.1852 | 0.1857 | -0.0005 ± 0.0003 | 0.5464 | 0.5475 | 0.5026 | 0.4878 | 0.5102 | -0.034 ± 0.0098 | -0.0133 (15) |
| 3-5 | 1296 | 0.1951 | 0.1941 | +0.0010 ± 0.001 | 0.5658 | 0.5634 | 0.5169 | 0.477 | 0.4846 | -0.046 ± 0.0124 | 0.02 (1) |
| 5-10 | 2918 | 0.1914 | 0.189 | +0.0025 ± 0.0012 | 0.5653 | 0.5564 | 0.5071 | 0.4332 | 0.4548 | -0.041 ± 0.0082 | -0.0117 (6) |
| 10-15 | 2545 | 0.1998 | 0.1892 | +0.0107 ± 0.0022 | 0.5884 | 0.551 | 0.5202 | 0.3957 | 0.4177 | -0.050 ± 0.0087 | -0.0189 (18) |
| 15-25 | 3646 | 0.2175 | 0.1779 | +0.0396 ± 0.0028 | 0.63 | 0.5239 | 0.5316 | 0.3354 | 0.336 | -0.074 ± 0.007 | -0.0086 (42) |
| 25-40 | 3240 | 0.2501 | 0.1358 | +0.1142 ± 0.0041 | 0.7063 | 0.417 | 0.5619 | 0.2458 | 0.2247 | -0.091 ± 0.0065 | -0.0044 (18) |
| 40+ | 2528 | 0.4013 | 0.0654 | +0.3359 ± 0.0059 | 1.0595 | 0.2289 | 0.6623 | 0.1247 | 0.0945 | -0.069 ± 0.005 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 497 | 0.1975 | 0.2 | -0.0025 ± 0.0007 | 0.5757 | 0.5815 | 0.4989 | 0.4837 | 0.5533 | -0.016 ± 0.0204 | -0.0137 (8) |
| 3-5 | 362 | 0.1918 | 0.1896 | +0.0022 ± 0.0018 | 0.5607 | 0.5557 | 0.4984 | 0.4588 | 0.453 | -0.118 ± 0.024 | 0.0067 (3) |
| 5-10 | 724 | 0.2012 | 0.1978 | +0.0035 ± 0.0025 | 0.5894 | 0.5777 | 0.5062 | 0.4324 | 0.4434 | -0.096 ± 0.017 | -0.0071 (7) |
| 10-15 | 579 | 0.209 | 0.2064 | +0.0026 ± 0.0047 | 0.6059 | 0.5958 | 0.5389 | 0.4158 | 0.4698 | -0.074 ± 0.0186 | -0.0317 (6) |
| 15-25 | 678 | 0.2357 | 0.2104 | +0.0253 ± 0.0069 | 0.6708 | 0.605 | 0.5887 | 0.3952 | 0.4263 | -0.116 ± 0.0176 | -0.03 (1) |
| 25-40 | 420 | 0.2047 | 0.2159 | -0.0112 ± 0.0131 | 0.5943 | 0.6161 | 0.6601 | 0.3506 | 0.5214 | -0.038 ± 0.0199 | 0.015 (2) |
| 40+ | 83 | 0.3118 | 0.1871 | +0.1247 ± 0.0428 | 0.8371 | 0.5509 | 0.7556 | 0.302 | 0.3976 | -0.102 ± 0.0431 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2320 | 0.1884 | 0.1893 | -0.0009 ± 0.0003 | 0.5537 | 0.5554 | 0.4876 | 0.4723 | 0.4957 | -0.031 ± 0.0091 | -0.0163 (35) |
| 3-5 | 1597 | 0.1879 | 0.1846 | +0.0034 ± 0.0009 | 0.5536 | 0.5455 | 0.4758 | 0.4363 | 0.4145 | -0.084 ± 0.0111 | -0.0094 (18) |
| 5-10 | 3483 | 0.1941 | 0.1873 | +0.0068 ± 0.0011 | 0.5725 | 0.5505 | 0.483 | 0.4091 | 0.3982 | -0.071 ± 0.0074 | -0.01 (31) |
| 10-15 | 2732 | 0.1965 | 0.1802 | +0.0163 ± 0.002 | 0.5777 | 0.5297 | 0.499 | 0.3756 | 0.3719 | -0.070 ± 0.0081 | -0.015 (12) |
| 15-25 | 3640 | 0.209 | 0.1708 | +0.0382 ± 0.0027 | 0.6114 | 0.5056 | 0.5069 | 0.312 | 0.3121 | -0.071 ± 0.0069 | -0.03 (2) |
| 25-40 | 2687 | 0.2153 | 0.1248 | +0.0904 ± 0.0043 | 0.6224 | 0.3841 | 0.5285 | 0.2125 | 0.2315 | -0.058 ± 0.0065 | 0.01 (3) |
| 40+ | 1770 | 0.3921 | 0.047 | +0.3452 ± 0.0058 | 1.0222 | 0.1808 | 0.639 | 0.1108 | 0.0599 | -0.087 ± 0.0048 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 839 | 0.1962 | 0.1962 | -0.0001 ± 0.0005 | 0.5728 | 0.5727 | 0.5074 | 0.4923 | 0.4934 | -0.058 ± 0.0154 | -0.0224 (49) |
| 3-5 | 588 | 0.1947 | 0.1938 | +0.0009 ± 0.0015 | 0.5677 | 0.5644 | 0.4804 | 0.4406 | 0.4473 | -0.053 ± 0.0183 | -0.0194 (34) |
| 5-10 | 1237 | 0.1989 | 0.1928 | +0.0062 ± 0.0019 | 0.5853 | 0.5676 | 0.4895 | 0.4161 | 0.4115 | -0.069 ± 0.0127 | -0.005 (78) |
| 10-15 | 788 | 0.2074 | 0.1963 | +0.0111 ± 0.0039 | 0.6029 | 0.5742 | 0.5102 | 0.387 | 0.4023 | -0.059 ± 0.0159 | 0.0014 (64) |
| 15-25 | 1059 | 0.2335 | 0.2123 | +0.0211 ± 0.0056 | 0.6652 | 0.6109 | 0.5688 | 0.3738 | 0.4183 | -0.061 ± 0.0142 | -0.0214 (59) |
| 25-40 | 625 | 0.2445 | 0.1995 | +0.0449 ± 0.011 | 0.6922 | 0.5777 | 0.6557 | 0.3434 | 0.4256 | -0.079 ± 0.0165 | -0.0219 (26) |
| 40+ | 217 | 0.3554 | 0.1936 | +0.1619 ± 0.0301 | 1.0264 | 0.5683 | 0.8023 | 0.3144 | 0.4147 | -0.080 ± 0.0264 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2600 | 0.1874 | 0.1875 | -0.0000 ± 0.0003 | 0.5499 | 0.5491 | 0.5047 | 0.4894 | 0.4973 | -0.039 ± 0.0085 | -0.0157 (88) |
| 3-5 | 1792 | 0.1905 | 0.1878 | +0.0027 ± 0.0008 | 0.5572 | 0.5507 | 0.4874 | 0.4477 | 0.4336 | -0.061 ± 0.0103 | -0.0209 (69) |
| 5-10 | 3580 | 0.1948 | 0.1864 | +0.0084 ± 0.0011 | 0.5743 | 0.5509 | 0.4869 | 0.4133 | 0.395 | -0.070 ± 0.0073 | -0.0082 (132) |
| 10-15 | 2443 | 0.2035 | 0.1885 | +0.0149 ± 0.0022 | 0.5942 | 0.5552 | 0.5171 | 0.3942 | 0.3942 | -0.060 ± 0.0088 | -0.0053 (105) |
| 15-25 | 3057 | 0.2293 | 0.198 | +0.0313 ± 0.0032 | 0.6604 | 0.5759 | 0.5612 | 0.3658 | 0.3847 | -0.063 ± 0.0081 | -0.0253 (107) |
| 25-40 | 2078 | 0.2497 | 0.173 | +0.0767 ± 0.0057 | 0.7088 | 0.5096 | 0.615 | 0.3014 | 0.3388 | -0.071 ± 0.0088 | -0.0229 (51) |
| 40+ | 977 | 0.3816 | 0.1326 | +0.2490 ± 0.0124 | 1.0813 | 0.4049 | 0.7163 | 0.2115 | 0.2313 | -0.074 ± 0.0109 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3343 | 1.058 ± 0.049 | 1.175 | 0.1681 | 0.1666 | 0.2124 | 0.2034 |
| gen2 | 3343 | 0.841 ± 0.044 | 1.132 | 0.1741 | 0.1666 | 0.2315 | 0.2033 |
| gen1_elo | 3343 | 1.042 ± 0.048 | 1.161 | 0.1737 | 0.167 | 0.2112 | 0.2033 |
| gen1_sr | 3343 | 1.04 ± 0.058 | 1.2 | 0.1341 | 0.1683 | 0.2276 | 0.2031 |
| gen1_ledger | 5353 | 0.883 ± 0.034 | 1.081 | 0.1783 | 0.182 | 0.2178 | 0.1986 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 16,023)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,857 | 24.1% |
| STALE_QUOTE | market_freshness | 3,269 | 20.4% |
| BOOK_QUALITY | execution | 3,123 | 19.5% |
| POOR_DATA | data | 1,743 | 10.9% |
| LIMITED_DATA | data | 1,093 | 6.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 853 | 5.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 779 | 4.9% |
| IDENTITY_AMBIGUOUS | mapping | 639 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 455 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 212 | 1.3% |

Cause class: coverage 24.1%, market_freshness 20.4%, execution 19.5%, data 17.7%, market_freshness/coverage 8.2%, model_calibration_or_unknown 4.9%, mapping 4.0%, model_calibration 1.3%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.6%, START_UNVERIFIABLE 94.8%, LOW_DATA_QUALITY 69.8%, THIN_PLAYER_HISTORY 58.1%, STALE_PLAYER_DATA 51.7%, STALE_KALSHI_QUOTE 44.0%, MODEL_INTERNAL_DISAGREEMENT 40.2%, ASYMMETRIC_SAMPLE_SIZE 32.2%, WIDE_SPREAD 25.5%, MODEL_HIGH_UNCERTAINTY 17.8%, PLAYER_IDENTITY_RISK 14.9%, LEVEL_TRANSFER_RISK 8.9%, EVENT_MAPPING_RISK 8.6%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 2.3%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 26.5%, POST_SETTLEMENT_OBSERVATION 24.1%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 8,590)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,051 | 35.5% |
| BOOK_QUALITY | execution | 1,644 | 19.1% |
| STALE_QUOTE | market_freshness | 1,527 | 17.8% |
| POOR_DATA | data | 734 | 8.5% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 451 | 5.2% |
| IDENTITY_AMBIGUOUS | mapping | 365 | 4.2% |
| LIMITED_DATA | data | 323 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 281 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 167 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 47 | 0.5% |

Cause class: coverage 35.5%, execution 19.1%, market_freshness 17.8%, data 12.3%, market_freshness/coverage 8.5%, mapping 4.2%, model_calibration_or_unknown 1.9%, model_calibration 0.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.7%, START_UNVERIFIABLE 97.5%, LOW_DATA_QUALITY 73.7%, THIN_PLAYER_HISTORY 60.5%, STALE_KALSHI_QUOTE 52.3%, STALE_PLAYER_DATA 47.1%, MODEL_INTERNAL_DISAGREEMENT 41.1%, ASYMMETRIC_SAMPLE_SIZE 34.0%, WIDE_SPREAD 25.3%, PLAYER_IDENTITY_RISK 18.2%, MODEL_HIGH_UNCERTAINTY 18.2%, EVENT_MAPPING_RISK 10.3%, LEVEL_TRANSFER_RISK 7.8%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 5.1%, EXTERNAL_MARKET_REJECTION 1.2%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 38.3%, POST_SETTLEMENT_OBSERVATION 35.5%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 6806, "IDENTITY_AMBIGUOUS": 1784}; ticker orientation: {"VERIFIED": 8590}.

Checks: discipline:AMBIGUOUS 633, discipline:PASS 7957, identity_confidence:AMBIGUOUS 1562, identity_confidence:PASS 7028, level_mapping:NA 645, level_mapping:PASS 7945, market_pair:AMBIGUOUS 308, market_pair:NA 213, market_pair:PASS 8069, model_complement:NA 180, model_complement:PASS 8410, namesake:PASS 8590, physical_match_id:NA 3254, physical_match_id:PASS 5336, player_ids:PASS 8590, same_pair_other_event:PASS 8590, ticker_orientation:PASS 8590

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,953 | 3.4% | 3.2% | 1.2% | {"market_freshness": 35, "data": 24, "execution": 13, "model_calibration_or_unknown": 12, "market_freshness/coverage": 8, "model_calibration": 7, "coverage": 2} | 5.64 | 0.2142 / 0.2101 (329) | 17.4% | 3.0% | 4.2% | 2.4% |
| CHALLENGER | 6,179 | 17.2% | 6.5% | 12.4% | {"coverage": 619, "market_freshness/coverage": 133, "market_freshness": 131, "data": 90, "model_calibration_or_unknown": 46, "execution": 25, "model_calibration": 10, "mapping": 10} | 7.24 | 0.2162 / 0.2054 (1558) | 36.1% | 14.3% | 3.1% | 22.5% |
| DOUBLES | 1,297 | 48.8% | 48.4% | 7.4% | {"execution": 309, "mapping": 168, "market_freshness": 106, "market_freshness/coverage": 43, "coverage": 7} | 24.07 | 0.324 / 0.2339 (337) | 18.0% | 0.0% | 100.0% | 7.2% |
| ITF_MEN | 10,910 | 24.6% | 16.7% | 31.2% | {"coverage": 1061, "execution": 539, "market_freshness": 411, "data": 357, "market_freshness/coverage": 214, "mapping": 94, "model_calibration_or_unknown": 2} | 11.13 | 0.214 / 0.1949 (2662) | 36.4% | 61.9% | 13.3% | 22.9% |
| ITF_WOMEN | 14,236 | 26.8% | 19.8% | 44.5% | {"coverage": 1345, "market_freshness": 768, "execution": 728, "data": 552, "market_freshness/coverage": 285, "mapping": 87, "model_calibration_or_unknown": 43, "model_calibration": 10} | 12.78 | 0.202 / 0.1934 (2915) | 38.5% | 57.7% | 10.2% | 22.2% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,199 | 5.0% | 4.5% | 1.3% | {"market_freshness": 36, "model_calibration_or_unknown": 23, "execution": 16, "data": 11, "market_freshness/coverage": 10, "model_calibration": 9, "coverage": 4, "mapping": 1} | 7.59 | 0.2413 / 0.234 (365) | 23.3% | 1.6% | 1.6% | 3.0% |
| WTA125 | 1,392 | 12.5% | 9.9% | 2.0% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 5 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 6 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 7 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 151 min (STALE); no external reference |
| 9 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 10 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 11 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 12 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 13 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 14 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 15 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 16 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 17 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 18 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 19 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 20 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 22 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 23 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 24 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 25 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 26 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 27 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 28 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 22.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1345 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 29 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 30 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 31 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 32 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 33 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 468 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 34 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 35 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 874 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 36 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 37 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 38 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 547 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 39 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 40 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 41 | `KXITFWMATCH-26OCT16ESTLAB-LAB` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 68 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1475.0, ratio 2.28); no external reference |
| 42 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 43 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 44 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 45 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.8h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 359 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 46 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 47 | `KXATPDOUBLES-26OCT18COLGOFPOLZIE-COLGOF` | DOUBLES | gen1_ledger | 90% / 15% | +75 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 49 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 50 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9756, "by_level_share_of_ge_25pp": {"ATP": 0.0118, "CHALLENGER": 0.1239, "DOUBLES": 0.0737, "ITF_MEN": 0.3118, "ITF_WOMEN": 0.4445, "OTHER": 0.0014, "WTA": 0.0128, "WTA125": 0.0203}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5227, "share_primary_cause_market_settled_or_in_play": 0.4404, "share_primary_cause_stale_quote_only": 0.1778}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 8590, "identity_ambiguous_share": 0.2077, "ticker_orientation": {"VERIFIED": 8590}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 5336, "with_external": 219, "coverage": 0.041, "external_status": {"EXTERNAL_STALE": 143, "AGREES_WITH_KALSHI": 73, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 143, "MODEL_LONE_OUTLIER": 73, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3333, "share_external_supports_model": 0.0137}, "pregame_clean_ge_25pp": {"n": 2552, "with_external": 207, "coverage": 0.0811, "external_status": {"EXTERNAL_STALE": 133, "AGREES_WITH_KALSHI": 71, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 133, "MODEL_LONE_OUTLIER": 71, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.343, "share_external_supports_model": 0.0145}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 535.0, "median_sample_ratio": 2.43, "median_min_matches": 21.0, "median_max_days_since_last": 213.0, "share_severe_asymmetry": 0.2057, "data_status": {"POOR": 4623, "LIMITED": 2447, "ADEQUATE": 1520}, "comparison_lt_10pp": {"median_thinner_serve_points": 1833.0, "median_sample_ratio": 1.67, "median_min_matches": 94.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 670, "model_minus_observed": 0.0533, "kalshi_minus_observed": -0.0814, "brier_diff_model_minus_kalshi": -0.0002}, "4-10x": {"n": 453, "model_minus_observed": 0.0743, "kalshi_minus_observed": -0.0667, "brier_diff_model_minus_kalshi": 0.0071}, "<2x": {"n": 1663, "model_minus_observed": 0.0875, "kalshi_minus_observed": -0.0338, "brier_diff_model_minus_kalshi": 0.0124}, ">=10x": {"n": 557, "model_minus_observed": 0.1159, "kalshi_minus_observed": -0.0559, "brier_diff_model_minus_kalshi": 0.0115}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3343, "model": {"intercept": -0.533, "slope": 0.841, "slope_se": 0.044}, "kalshi_mid_same_rows": {"intercept": 0.23, "slope": 1.132, "slope_se": 0.051}, "mean_extremity_model": 0.1741, "mean_extremity_kalshi": 0.1666, "model_brier": 0.2315, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.0282, "brier_diff_se": 0.0033, "model_logloss": 0.6598, "kalshi_logloss": 0.589}, "fair_v1": {"n": 3343, "model": {"intercept": -0.404, "slope": 1.058, "slope_se": 0.049}, "kalshi_mid_same_rows": {"intercept": 0.313, "slope": 1.175, "slope_se": 0.052}, "mean_extremity_model": 0.1681, "mean_extremity_kalshi": 0.1666, "model_brier": 0.2124, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": 0.009, "brier_diff_se": 0.0026, "model_logloss": 0.6123, "kalshi_logloss": 0.5889}, "gen1_elo": {"n": 3343, "model": {"intercept": -0.394, "slope": 1.042, "slope_se": 0.048}, "kalshi_mid_same_rows": {"intercept": 0.308, "slope": 1.161, "slope_se": 0.051}, "mean_extremity_model": 0.1737, "mean_extremity_kalshi": 0.167, "model_brier": 0.2112, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.0079, "brier_diff_se": 0.0026, "model_logloss": 0.6104, "kalshi_logloss": 0.5887}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2434, "share_ge_15": 0.4359, "median_abs_gap": 12.96, "n": 21923}, "gen1_elo": {"share_ge_25": 0.2378, "share_ge_15": 0.4321, "median_abs_gap": 12.54, "n": 21923}, "gen1_sr": {"share_ge_25": 0.3053, "share_ge_15": 0.5193, "median_abs_gap": 15.68, "n": 21923}, "gen2": {"share_ge_25": 0.3084, "share_ge_15": 0.5073, "median_abs_gap": 15.38, "n": 21923}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1504, "share_ge_15": 0.3485, "median_abs_gap": 10.66, "n": 16971}, "gen1_elo": {"share_ge_25": 0.1484, "share_ge_15": 0.3414, "median_abs_gap": 10.18, "n": 16970}, "gen1_sr": {"share_ge_25": 0.2116, "share_ge_15": 0.4407, "median_abs_gap": 13.04, "n": 16971}, "gen2": {"share_ge_25": 0.227, "share_ge_15": 0.4397, "median_abs_gap": 13.0, "n": 16972}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.64, "share_ge_25_all": 0.0342, "share_ge_25_pregame_clean": 0.0316}, "WTA": {"median_abs_gap_pregame_clean": 7.59, "share_ge_25_all": 0.05, "share_ge_25_pregame_clean": 0.045}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.24, "share_within_10pp_all": 0.4385, "share_within_10pp_pregame_clean": 0.4938, "corr_model_vs_mid_pregame_clean": 0.8421}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 513, "model_brier": 0.1954, "kalshi_brier": 0.1967, "brier_diff_model_minus_kalshi": -0.0013}, "10-15": {"n_settled": 593, "model_brier": 0.2151, "kalshi_brier": 0.2063, "brier_diff_model_minus_kalshi": 0.0088}, "15-25": {"n_settled": 726, "model_brier": 0.2279, "kalshi_brier": 0.2127, "brier_diff_model_minus_kalshi": 0.0152}, "25-40": {"n_settled": 409, "model_brier": 0.2195, "kalshi_brier": 0.2107, "brier_diff_model_minus_kalshi": 0.0088}, "3-5": {"n_settled": 321, "model_brier": 0.1972, "kalshi_brier": 0.1966, "brier_diff_model_minus_kalshi": 0.0005}, "40+": {"n_settled": 84, "model_brier": 0.2967, "kalshi_brier": 0.1739, "brier_diff_model_minus_kalshi": 0.1228}, "5-10": {"n_settled": 697, "model_brier": 0.199, "kalshi_brier": 0.1984, "brier_diff_model_minus_kalshi": 0.0006}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.533, "slope": 0.841, "slope_se": 0.044}, "kalshi_slope": {"intercept": 0.23, "slope": 1.132, "slope_se": 0.051}, "n": 3343}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.518, "slope": 0.883, "slope_se": 0.034}, "kalshi_slope": {"intercept": 0.149, "slope": 1.081, "slope_se": 0.038}, "n": 5353}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 337, "model_brier": 0.324, "kalshi_brier": 0.2339, "brier_diff_model_minus_kalshi": 0.0902, "brier_diff_se": 0.0171, "corr_model_outcome": 0.0142, "corr_kalshi_outcome": 0.2577}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
