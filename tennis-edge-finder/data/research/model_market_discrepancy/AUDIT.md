# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-22T18:28Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 49,450): 0-3 13.9%, 3-5 9.4%, 5-10 19.7%, 10-15 15.3%, 15-25 19.4%, 25-40 14.1%, 40+ 8.2%; median gap 12.16 pp.
* **Where the extremes live**: 97.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.8%, Challenger 11.9%, doubles 6.7%). Main tour: ATP 4.9% and WTA 4.8% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 11,011): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.6%, STALE_QUOTE 18.6%, BOOK_QUALITY 18.2%, POOR_DATA 8.8%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IDENTITY_AMBIGUOUS 4.5%, LIMITED_DATA 3.6%, IN_PLAY_QUOTE 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%. By class: coverage 34.6%, market_freshness 18.6%, execution 18.2%, data 12.4%, market_freshness/coverage 8.9%, mapping 4.5%, model_calibration_or_unknown 2.1%, model_calibration 0.7%.
* **Stale / settled / in-play**: 52.3% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 11,011 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.0% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.9%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.8% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 480.0 points vs 1667.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.038, Gen-2 0.845, Gen-1 ledger 0.864 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 539 model 0.2247 vs Kalshi 0.2098; n 109 model 0.2803 vs Kalshi 0.1965.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 212,715 model-market comparisons (346,474 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 70,895 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-22T18:17:25.880039+00:00'], shadow board 56,832 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-22T18:17:29.975475+00:00'], Model 4 26,659 rows, 19,106 settled tickers, 6,674 tickers with an external scan.
* By model: {"gen1_ledger": 48000, "gen1_elo": 28580, "fair_v1": 28580, "gen2": 28580, "gen1_sr": 28580, "model4_fundamental": 25211, "model4_conditioned": 25184}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 49,450 | 13.9 | 9.4 | 19.7 | 15.3 | 19.4 | 14.1 | 8.2 | 12.16 | 41.7% | 22.3% |
| MW fair_v1 | 28,580 | 12.9 | 8.5 | 18.3 | 15.6 | 19.9 | 15.0 | 9.8 | 13.24 | 44.7% | 24.8% |
| MW gen1_elo | 28,580 | 12.8 | 8.5 | 18.9 | 15.2 | 20.0 | 15.0 | 9.6 | 13.02 | 44.6% | 24.6% |
| MW gen1_ledger | 20,870 | 15.4 | 10.7 | 21.5 | 14.8 | 18.7 | 12.8 | 5.9 | 10.58 | 37.5% | 18.8% |
| MW gen1_sr | 28,580 | 9.9 | 7.0 | 16.5 | 13.7 | 21.1 | 18.9 | 12.8 | 16.15 | 52.9% | 31.7% |
| MW gen2 | 28,580 | 10.8 | 7.2 | 16.2 | 14.1 | 19.6 | 18.0 | 14.0 | 15.7 | 51.6% | 32.0% |
| all families model4_conditioned | 25,184 | 21.8 | 19.0 | 34.6 | 17.8 | 4.4 | 1.4 | 1.0 | 5.97 | 6.9% | 2.5% |
| all families model4_fundamental | 25,211 | 16.6 | 13.2 | 34.0 | 20.6 | 10.8 | 3.5 | 1.3 | 7.83 | 15.6% | 4.8% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 57.0%, >=15pp 41.7%, >=20pp 31.0%, >=25pp 22.3%, >=30pp 16.1%, >=40pp 8.2%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.52pp; >=10pp 45.6%, >=25pp 17.4%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,445 | 28.9 | 13.9 | 24.6 | 14.8 | 12.0 | 5.0 | 0.7 | 6.17 | 17.8% | 5.7% |
| CHALLENGER | 4,496 | 15.9 | 9.9 | 20.4 | 15.7 | 14.8 | 12.4 | 11.0 | 11.09 | 38.1% | 23.4% |
| ITF_MEN | 7,871 | 10.3 | 7.5 | 16.9 | 14.7 | 21.6 | 17.2 | 12.0 | 15.22 | 50.8% | 29.2% |
| ITF_WOMEN | 11,428 | 9.3 | 6.9 | 15.8 | 15.4 | 22.6 | 18.2 | 11.7 | 15.82 | 52.5% | 29.9% |
| WTA | 1,680 | 17.3 | 13.0 | 25.4 | 20.0 | 19.1 | 4.6 | 0.7 | 8.41 | 24.4% | 5.3% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,445 | 23.6 | 15.0 | 25.1 | 17.1 | 13.3 | 4.9 | 1.0 | 6.58 | 19.2% | 5.9% |
| CHALLENGER | 4,496 | 14.8 | 8.7 | 18.6 | 14.8 | 17.3 | 13.9 | 11.9 | 12.5 | 43.1% | 25.8% |
| ITF_MEN | 7,871 | 8.4 | 6.0 | 14.4 | 13.1 | 19.7 | 20.8 | 17.7 | 18.57 | 58.2% | 38.5% |
| ITF_WOMEN | 11,428 | 8.0 | 5.6 | 13.7 | 13.5 | 20.9 | 21.1 | 17.3 | 19.01 | 59.3% | 38.4% |
| WTA | 1,680 | 14.5 | 10.1 | 21.1 | 16.4 | 23.5 | 13.7 | 0.7 | 11.08 | 37.9% | 14.4% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,445 | 24.5 | 12.8 | 24.0 | 15.9 | 14.7 | 6.9 | 1.2 | 7.26 | 22.8% | 8.1% |
| CHALLENGER | 4,496 | 14.4 | 9.3 | 20.7 | 15.4 | 16.2 | 12.8 | 11.2 | 11.45 | 40.3% | 24.0% |
| ITF_MEN | 7,871 | 9.8 | 7.5 | 17.0 | 14.0 | 22.1 | 17.6 | 12.1 | 15.59 | 51.8% | 29.6% |
| ITF_WOMEN | 11,428 | 9.6 | 6.6 | 16.2 | 15.7 | 23.0 | 18.2 | 10.8 | 15.65 | 52.0% | 29.0% |
| WTA | 1,680 | 24.2 | 16.9 | 30.1 | 16.0 | 10.1 | 2.3 | 0.4 | 6.01 | 12.8% | 2.7% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,408 | 25.4 | 19.6 | 30.8 | 11.8 | 9.0 | 3.0 | 0.4 | 5.54 | 12.4% | 3.4% |
| CHALLENGER | 3,091 | 21.4 | 14.8 | 26.5 | 14.0 | 14.8 | 6.5 | 1.9 | 7.27 | 23.2% | 8.4% |
| DOUBLES | 1,552 | 5.5 | 4.1 | 11.5 | 10.2 | 20.9 | 26.4 | 21.4 | 23.99 | 68.6% | 47.7% |
| ITF_MEN | 5,922 | 13.8 | 8.9 | 20.1 | 16.0 | 21.3 | 13.3 | 6.6 | 12.16 | 41.2% | 20.0% |
| ITF_WOMEN | 6,988 | 12.7 | 9.1 | 19.3 | 15.1 | 21.6 | 16.3 | 6.1 | 12.86 | 44.0% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,028 | 22.3 | 15.9 | 29.6 | 18.2 | 10.1 | 3.6 | 0.3 | 6.97 | 14.0% | 3.9% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,378 | 29.2 | 14.1 | 25.0 | 14.8 | 11.8 | 4.6 | 0.5 | 6.0 | 16.9% | 5.1% |
| CHALLENGER | 3,173 | 20.8 | 12.3 | 25.1 | 18.1 | 15.2 | 6.6 | 2.0 | 8.34 | 23.8% | 8.6% |
| ITF_MEN | 5,788 | 12.4 | 9.0 | 20.2 | 16.5 | 22.6 | 14.2 | 5.1 | 12.49 | 41.9% | 19.3% |
| ITF_WOMEN | 8,538 | 11.1 | 8.2 | 18.0 | 17.5 | 24.6 | 15.4 | 5.2 | 13.55 | 45.2% | 20.6% |
| WTA | 1,631 | 17.5 | 12.8 | 25.4 | 20.2 | 19.1 | 4.3 | 0.7 | 8.39 | 24.1% | 5.0% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,378 | 23.9 | 15.3 | 25.3 | 16.9 | 13.3 | 4.6 | 0.6 | 6.48 | 18.5% | 5.2% |
| CHALLENGER | 3,173 | 18.7 | 11.1 | 23.1 | 17.7 | 17.6 | 9.6 | 2.2 | 9.2 | 29.4% | 11.8% |
| ITF_MEN | 5,789 | 10.0 | 7.1 | 16.7 | 14.9 | 21.5 | 19.3 | 10.5 | 15.49 | 51.3% | 29.8% |
| ITF_WOMEN | 8,539 | 9.0 | 6.4 | 15.2 | 15.0 | 22.9 | 20.6 | 10.9 | 16.62 | 54.4% | 31.5% |
| WTA | 1,631 | 14.6 | 10.1 | 21.1 | 16.3 | 23.5 | 13.6 | 0.7 | 11.09 | 37.9% | 14.3% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,364 | 25.7 | 19.9 | 30.8 | 12.0 | 8.5 | 2.9 | 0.2 | 5.44 | 11.7% | 3.1% |
| CHALLENGER | 2,694 | 22.9 | 15.9 | 28.1 | 14.0 | 14.1 | 4.4 | 0.6 | 6.68 | 19.1% | 5.0% |
| DOUBLES | 1,442 | 5.5 | 4.3 | 11.8 | 10.5 | 20.7 | 26.3 | 20.9 | 23.85 | 68.0% | 47.2% |
| ITF_MEN | 4,953 | 15.0 | 9.6 | 21.8 | 16.8 | 21.1 | 11.7 | 4.0 | 11.13 | 36.9% | 15.7% |
| ITF_WOMEN | 5,792 | 13.6 | 9.6 | 20.7 | 15.9 | 21.8 | 15.0 | 3.4 | 11.68 | 40.2% | 18.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 978 | 22.8 | 16.5 | 29.6 | 18.2 | 10.1 | 2.9 | 0.0 | 6.82 | 13.0% | 2.9% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,552 | 5.5 | 4.1 | 11.5 | 10.2 | 20.9 | 26.4 | 21.4 | 23.99 | 68.6% | 47.7% |
| singles | 19,318 | 16.2 | 11.3 | 22.3 | 15.2 | 18.5 | 11.8 | 4.7 | 10.03 | 35.0% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 6,371 | 13.2 | 8.8 | 19.0 | 15.6 | 18.9 | 14.8 | 9.7 | 12.92 | 43.4% | 24.5% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 17,751 | 13.2 | 8.5 | 18.4 | 15.3 | 20.0 | 14.8 | 9.8 | 13.21 | 44.6% | 24.5% |
| UNKNOWN | 4,221 | 10.8 | 7.8 | 17.1 | 16.9 | 20.8 | 16.1 | 10.5 | 13.98 | 47.4% | 26.6% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,934 | 19.7 | 11.6 | 21.3 | 16.5 | 15.6 | 9.0 | 6.2 | 9.23 | 30.9% | 15.3% |
| B | 3,560 | 12.5 | 8.9 | 19.8 | 16.5 | 19.3 | 12.4 | 10.6 | 12.48 | 42.3% | 23.0% |
| C | 4,040 | 11.6 | 8.8 | 19.6 | 15.2 | 19.5 | 14.9 | 10.5 | 13.16 | 44.9% | 25.4% |
| D | 4,576 | 12.1 | 7.8 | 17.2 | 15.5 | 21.6 | 15.7 | 10.1 | 14.03 | 47.4% | 25.9% |
| F | 8,470 | 7.6 | 5.6 | 14.9 | 14.6 | 23.5 | 21.3 | 12.4 | 17.79 | 57.2% | 33.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,846 | 23.0 | 15.9 | 28.8 | 15.0 | 11.8 | 4.0 | 1.5 | 6.66 | 17.3% | 5.5% |
| B | 2,861 | 16.2 | 10.4 | 23.4 | 16.0 | 19.3 | 10.7 | 4.0 | 9.99 | 33.9% | 14.6% |
| C | 4,123 | 11.4 | 7.3 | 18.3 | 14.2 | 21.4 | 16.7 | 10.7 | 14.32 | 48.8% | 27.3% |
| D | 2,959 | 14.5 | 9.8 | 19.9 | 14.4 | 20.9 | 14.3 | 6.1 | 11.9 | 41.3% | 20.4% |
| F | 5,081 | 10.2 | 8.2 | 15.5 | 14.8 | 22.8 | 20.3 | 8.2 | 15.68 | 51.3% | 28.5% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 9,105 | 17.8 | 10.4 | 20.6 | 16.4 | 16.2 | 9.9 | 8.7 | 10.37 | 34.8% | 18.6% |
| LIMITED | 6,139 | 13.4 | 10.1 | 20.4 | 15.7 | 19.2 | 13.5 | 7.7 | 11.92 | 40.5% | 21.2% |
| POOR | 13,336 | 9.2 | 6.4 | 15.8 | 15.0 | 22.8 | 19.1 | 11.6 | 16.18 | 53.5% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,438 | 26.4 | 20.4 | 34.2 | 12.6 | 4.8 | 1.4 | 0.2 | 5.33 | 6.4% | 1.6% |
| GAME_SPREAD | 4,634 | 22.3 | 15.1 | 33.5 | 17.4 | 9.0 | 2.4 | 0.3 | 6.71 | 11.7% | 2.7% |
| MATCH_WINNER | 20,870 | 15.4 | 10.7 | 21.5 | 14.8 | 18.7 | 12.8 | 5.9 | 10.58 | 37.5% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 9,661 | 29.2 | 17.0 | 31.2 | 12.5 | 8.1 | 1.7 | 0.4 | 5.48 | 10.2% | 2.1% |
| TOTAL_GAMES | 7,373 | 8.5 | 9.6 | 36.5 | 28.9 | 10.6 | 3.2 | 2.7 | 9.49 | 16.5% | 5.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,801 | 25.4 | 33.8 | 32.6 | 4.5 | 3.0 | 0.6 | 0.2 | 4.48 | 3.8% | 0.8% |
| GAME_SPREAD | 6,039 | 45.4 | 16.8 | 27.0 | 7.8 | 1.8 | 0.9 | 0.3 | 3.51 | 3.0% | 1.2% |
| TOTAL_GAMES | 10,344 | 4.9 | 7.7 | 40.7 | 34.9 | 7.1 | 2.5 | 2.2 | 9.66 | 11.8% | 4.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,804 | 24.2 | 17.8 | 35.4 | 12.7 | 7.0 | 2.5 | 0.3 | 5.82 | 9.9% | 2.8% |
| GAME_SPREAD | 6,042 | 19.3 | 13.3 | 28.0 | 20.4 | 13.7 | 4.5 | 0.9 | 7.97 | 19.1% | 5.4% |
| TOTAL_GAMES | 10,365 | 8.5 | 9.3 | 36.3 | 27.4 | 12.4 | 3.8 | 2.3 | 9.51 | 18.5% | 6.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 28,580 | 44.7% | 24.8% | 13.24 | 36.4% | 15.6% | 11.0 |
| gen1_elo | 28,580 | 44.6% | 24.6% | 13.02 | 36.0% | 15.7% | 10.73 |
| gen1_sr | 28,580 | 52.9% | 31.7% | 16.15 | 45.1% | 22.4% | 13.35 |
| gen2 | 28,580 | 51.6% | 32.0% | 15.7 | 44.9% | 24.0% | 13.21 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 14,438 | 15.8 | 10.3 | 21.1 | 17.2 | 20.4 | 11.9 | 3.3 | 10.81 | 35.6% | 15.2% |
| STALE | 14,142 | 9.9 | 6.7 | 15.5 | 13.9 | 19.4 | 18.1 | 16.5 | 16.91 | 54.0% | 34.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 14,338 | 16.5 | 11.3 | 22.3 | 14.9 | 17.9 | 12.3 | 4.9 | 9.98 | 35.0% | 17.1% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 49,450 | 14338 | 17910 | 17202 | 24.1 | 141.7 | 1400.4 |
| ge_15pp | 20,610 | 5024 | 6436 | 9150 | 26.0 | 435.0 | 1380.4 |
| ge_25pp | 11,011 | 2458 | 2792 | 5761 | 32.3 | 574.8 | 1380.4 |
| lt_10pp | 21,285 | 7180 | 8437 | 5668 | 22.1 | 48.0 | 1341.5 |

Current slate `SL-20261022T182832Z-b256534e`: 362 priced rows, quote age at build {'median': 11.4, 'max': 11.4}, freshness {'AGING': 362}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 22 | 0.0 | 0.0 | 22.7 | 4.5 | 40.9 | 31.8 | 0.0 | 20.48 | 72.7% | 31.8% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,637 | 19.5 | 10.8 | 23.9 | 18.9 | 18.9 | 7.4 | 0.7 | 9.1 | 26.9% | 8.1% |
| KALSHI_LONE_OUTLIER | 17 | 5.9 | 5.9 | 76.5 | 0.0 | 5.9 | 5.9 | 0.0 | 6.11 | 11.8% | 5.9% |
| MARKETS_AGREE | 515 | 66.6 | 33.4 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.2 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,114 | 0.0 | 2.2 | 34.9 | 25.9 | 25.3 | 10.8 | 0.8 | 12.54 | 36.9% | 11.6% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 28,580 | 4317 (15.1%) | 25.8% | 0.9% | {"EXTERNAL_STALE": 2637, "AGREES_WITH_KALSHI": 1114, "ALL_AGREE": 515, "SUPPORTS_MODEL_DIRECTION": 21, "AGREES_WITH_MODEL": 17, "EXTERNAL_OUTLIER": 12, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 12,787 | 1139 (8.9%) | 36.1% | 1.6% | {"EXTERNAL_STALE": 710, "AGREES_WITH_KALSHI": 411, "SUPPORTS_MODEL_DIRECTION": 16, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 7,091 | 350 (4.9%) | 36.9% | 2.3% | {"EXTERNAL_STALE": 213, "AGREES_WITH_KALSHI": 129, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,443 | 327 (9.5%) | 37.3% | 2.5% | {"EXTERNAL_STALE": 197, "AGREES_WITH_KALSHI": 122, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 11,336 | 2391 (21.1%) | 17.3% | 0.8% | {"EXTERNAL_STALE": 1430, "ALL_AGREE": 515, "AGREES_WITH_KALSHI": 414, "AGREES_WITH_MODEL": 15, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 4, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,448 | 10.4 | 7.5 | 19.2 | 14.4 | 22.5 | 15.9 | 10.0 | 14.26 | 48.5% | 26.0% |
| 4-10x | 3,737 | 10.9 | 8.4 | 19.1 | 15.4 | 21.2 | 14.9 | 10.2 | 13.75 | 46.2% | 25.1% |
| <2x | 14,477 | 14.9 | 9.6 | 18.9 | 16.6 | 17.9 | 13.1 | 9.0 | 11.98 | 40.1% | 22.2% |
| >=10x | 4,918 | 11.1 | 6.4 | 15.1 | 14.3 | 22.0 | 19.4 | 11.7 | 16.18 | 53.1% | 31.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 7,202 | 12.3 | 8.4 | 19.5 | 16.2 | 19.6 | 13.6 | 10.5 | 13.0 | 43.7% | 24.1% |
| 300-1000 | 6,175 | 11.6 | 8.7 | 17.2 | 15.3 | 20.7 | 16.3 | 10.3 | 14.0 | 47.3% | 26.5% |
| <300 | 9,420 | 8.7 | 5.7 | 15.4 | 14.8 | 23.1 | 20.1 | 12.2 | 16.87 | 55.3% | 32.2% |
| >=3000 | 5,783 | 21.6 | 12.8 | 22.9 | 16.5 | 14.4 | 7.0 | 4.8 | 8.01 | 26.2% | 11.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 826 | 0.5478 | 0.41 | 0.5012 | +0.047 | -0.091 | -0.0039 ± 0.0054 |
| ratio 4-10x | 564 | 0.5857 | 0.4398 | 0.4911 | +0.095 | -0.051 | 0.0136 ± 0.0068 |
| ratio <2x | 2032 | 0.5374 | 0.4137 | 0.4469 | +0.091 | -0.033 | 0.0122 ± 0.0032 |
| ratio >=10x | 746 | 0.5674 | 0.3919 | 0.4611 | +0.106 | -0.069 | 0.0067 ± 0.0067 |
| thinner_sample 1000-3000 | 1125 | 0.5426 | 0.4152 | 0.4507 | +0.092 | -0.035 | 0.0102 ± 0.0043 |
| thinner_sample 300-1000 | 962 | 0.5644 | 0.4214 | 0.4917 | +0.073 | -0.070 | 0.0009 ± 0.0052 |
| thinner_sample <300 | 1403 | 0.5572 | 0.391 | 0.4626 | +0.095 | -0.072 | 0.009 ± 0.0047 |
| thinner_sample >=3000 | 678 | 0.5354 | 0.4405 | 0.4631 | +0.072 | -0.023 | 0.0137 ± 0.0045 |
| data_status ADEQUATE | 1181 | 0.5384 | 0.4326 | 0.4505 | +0.088 | -0.018 | 0.0131 ± 0.0037 |
| data_status LIMITED | 977 | 0.5496 | 0.4169 | 0.4811 | +0.069 | -0.064 | 0.004 ± 0.0048 |
| data_status POOR | 2010 | 0.5599 | 0.3988 | 0.4682 | +0.092 | -0.069 | 0.0074 ± 0.0039 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 613 | 0.1995 | 0.2005 | -0.0010 ± 0.0006 | 0.5793 | 0.5815 | 0.502 | 0.4871 | 0.5318 | -0.060 ± 0.019 | -0.01 (5) |
| 3-5 | 389 | 0.2023 | 0.2017 | +0.0007 ± 0.0018 | 0.5878 | 0.5845 | 0.5027 | 0.4626 | 0.473 | -0.099 ± 0.0235 | 0.02 (1) |
| 5-10 | 852 | 0.2012 | 0.2007 | +0.0005 ± 0.0023 | 0.5889 | 0.5845 | 0.5096 | 0.4353 | 0.4648 | -0.089 ± 0.016 | -0.0167 (6) |
| 10-15 | 722 | 0.213 | 0.2037 | +0.0093 ± 0.0042 | 0.6164 | 0.5888 | 0.5274 | 0.4032 | 0.4266 | -0.103 ± 0.0167 | -0.048 (5) |
| 15-25 | 944 | 0.2244 | 0.2135 | +0.0109 ± 0.0059 | 0.6436 | 0.6109 | 0.5767 | 0.3808 | 0.4513 | -0.089 ± 0.0149 | -0.0033 (9) |
| 25-40 | 539 | 0.2247 | 0.2098 | +0.0150 ± 0.0118 | 0.6379 | 0.603 | 0.6552 | 0.3456 | 0.4731 | -0.074 ± 0.0181 | -0.01 (1) |
| 40+ | 109 | 0.2803 | 0.1965 | +0.0839 ± 0.037 | 0.7681 | 0.5777 | 0.7552 | 0.3067 | 0.4404 | -0.080 ± 0.0363 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3137 | 0.1826 | 0.1836 | -0.0011 ± 0.0003 | 0.5399 | 0.5411 | 0.4914 | 0.4763 | 0.5151 | -0.017 ± 0.0077 | -0.0129 (17) |
| 3-5 | 2063 | 0.1969 | 0.1957 | +0.0012 ± 0.0008 | 0.5739 | 0.5679 | 0.4848 | 0.4449 | 0.4489 | -0.053 ± 0.0099 | 0.0 (2) |
| 5-10 | 4435 | 0.1978 | 0.1945 | +0.0033 ± 0.001 | 0.5798 | 0.5688 | 0.4818 | 0.4078 | 0.4221 | -0.047 ± 0.0067 | -0.0119 (21) |
| 10-15 | 3785 | 0.1986 | 0.1809 | +0.0177 ± 0.0017 | 0.5833 | 0.5332 | 0.4859 | 0.3613 | 0.3522 | -0.073 ± 0.0069 | -0.0281 (16) |
| 15-25 | 4766 | 0.2083 | 0.1697 | +0.0386 ± 0.0023 | 0.61 | 0.5021 | 0.5035 | 0.3071 | 0.3078 | -0.072 ± 0.0059 | -0.0025 (44) |
| 25-40 | 3711 | 0.2238 | 0.1321 | +0.0917 ± 0.0037 | 0.642 | 0.4025 | 0.5316 | 0.2189 | 0.232 | -0.058 ± 0.0058 | -0.01 (1) |
| 40+ | 2420 | 0.3807 | 0.0453 | +0.3354 ± 0.0049 | 0.9915 | 0.175 | 0.6327 | 0.1073 | 0.0632 | -0.080 ± 0.0041 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 472 | 0.2038 | 0.2042 | -0.0005 ± 0.0007 | 0.5893 | 0.5902 | 0.5033 | 0.4883 | 0.5042 | -0.110 ± 0.0223 | -0.01 (3) |
| 3-5 | 342 | 0.2214 | 0.2198 | +0.0017 ± 0.002 | 0.6288 | 0.6252 | 0.5139 | 0.4739 | 0.4678 | -0.114 ± 0.0271 | 0.02 (1) |
| 5-10 | 735 | 0.2044 | 0.2042 | +0.0002 ± 0.0025 | 0.595 | 0.5931 | 0.5462 | 0.4714 | 0.5088 | -0.079 ± 0.0171 | -0.01 (4) |
| 10-15 | 690 | 0.2172 | 0.209 | +0.0082 ± 0.0044 | 0.624 | 0.6037 | 0.5657 | 0.4414 | 0.4725 | -0.111 ± 0.0181 | -0.04 (5) |
| 15-25 | 977 | 0.2297 | 0.21 | +0.0197 ± 0.0058 | 0.6523 | 0.6028 | 0.5884 | 0.3925 | 0.4442 | -0.100 ± 0.0149 | -0.0133 (9) |
| 25-40 | 691 | 0.2618 | 0.1991 | +0.0627 ± 0.0107 | 0.7306 | 0.579 | 0.653 | 0.3374 | 0.398 | -0.109 ± 0.0166 | -0.0075 (4) |
| 40+ | 261 | 0.3577 | 0.1752 | +0.1825 ± 0.0256 | 0.9859 | 0.5222 | 0.7337 | 0.249 | 0.318 | -0.067 ± 0.0248 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2644 | 0.1929 | 0.1932 | -0.0002 ± 0.0003 | 0.5627 | 0.563 | 0.5091 | 0.4942 | 0.5083 | -0.045 ± 0.0089 | -0.0133 (15) |
| 3-5 | 1769 | 0.1984 | 0.198 | +0.0005 ± 0.0009 | 0.5747 | 0.5731 | 0.5151 | 0.4752 | 0.4884 | -0.041 ± 0.0108 | 0.02 (1) |
| 5-10 | 3898 | 0.194 | 0.1926 | +0.0014 ± 0.0011 | 0.5721 | 0.564 | 0.5065 | 0.4326 | 0.4623 | -0.030 ± 0.0071 | -0.0117 (6) |
| 10-15 | 3429 | 0.2001 | 0.1873 | +0.0128 ± 0.0019 | 0.5871 | 0.5473 | 0.514 | 0.3899 | 0.4016 | -0.058 ± 0.0075 | -0.0189 (18) |
| 15-25 | 4796 | 0.2159 | 0.178 | +0.0379 ± 0.0024 | 0.6277 | 0.5238 | 0.5259 | 0.3299 | 0.3349 | -0.069 ± 0.0061 | -0.0086 (42) |
| 25-40 | 4352 | 0.251 | 0.1401 | +0.1109 ± 0.0036 | 0.707 | 0.4281 | 0.5587 | 0.242 | 0.2279 | -0.080 ± 0.0056 | -0.0044 (18) |
| 40+ | 3429 | 0.3952 | 0.063 | +0.3321 ± 0.0049 | 1.041 | 0.2231 | 0.6534 | 0.1207 | 0.0887 | -0.070 ± 0.0042 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 586 | 0.2001 | 0.2024 | -0.0023 ± 0.0007 | 0.5813 | 0.587 | 0.4976 | 0.4823 | 0.5495 | -0.024 ± 0.0192 | -0.0137 (8) |
| 3-5 | 417 | 0.2003 | 0.1984 | +0.0020 ± 0.0018 | 0.5825 | 0.5765 | 0.5063 | 0.4667 | 0.4628 | -0.119 ± 0.0227 | 0.0067 (3) |
| 5-10 | 878 | 0.1997 | 0.1963 | +0.0035 ± 0.0023 | 0.5859 | 0.5735 | 0.5071 | 0.4331 | 0.4442 | -0.101 ± 0.0154 | -0.0071 (7) |
| 10-15 | 728 | 0.2085 | 0.205 | +0.0035 ± 0.0042 | 0.6059 | 0.5924 | 0.5383 | 0.4146 | 0.4643 | -0.085 ± 0.0167 | -0.0317 (6) |
| 15-25 | 887 | 0.2311 | 0.2119 | +0.0193 ± 0.006 | 0.6605 | 0.6069 | 0.5859 | 0.3916 | 0.4386 | -0.112 ± 0.0154 | -0.03 (1) |
| 25-40 | 558 | 0.2131 | 0.2181 | -0.0050 ± 0.0116 | 0.6138 | 0.6222 | 0.6666 | 0.3548 | 0.5161 | -0.049 ± 0.0178 | 0.015 (2) |
| 40+ | 114 | 0.2963 | 0.2074 | +0.0889 ± 0.0375 | 0.8151 | 0.6019 | 0.7631 | 0.3122 | 0.4474 | -0.077 ± 0.0389 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3073 | 0.1868 | 0.1874 | -0.0006 ± 0.0003 | 0.5487 | 0.5497 | 0.4914 | 0.4763 | 0.4924 | -0.036 ± 0.0079 | -0.0163 (35) |
| 3-5 | 2064 | 0.1938 | 0.1912 | +0.0026 ± 0.0008 | 0.5694 | 0.5614 | 0.4888 | 0.4491 | 0.437 | -0.072 ± 0.0098 | -0.0094 (18) |
| 5-10 | 4519 | 0.1948 | 0.1887 | +0.0061 ± 0.001 | 0.5736 | 0.5538 | 0.4847 | 0.4107 | 0.4063 | -0.064 ± 0.0065 | -0.01 (31) |
| 10-15 | 3673 | 0.1921 | 0.176 | +0.0160 ± 0.0017 | 0.5679 | 0.5206 | 0.4979 | 0.3744 | 0.3708 | -0.069 ± 0.0069 | -0.015 (12) |
| 15-25 | 4930 | 0.2109 | 0.1719 | +0.0390 ± 0.0023 | 0.6159 | 0.5075 | 0.512 | 0.317 | 0.3144 | -0.074 ± 0.0059 | -0.03 (2) |
| 25-40 | 3702 | 0.2188 | 0.1353 | +0.0834 ± 0.0038 | 0.6315 | 0.4094 | 0.5367 | 0.2209 | 0.2482 | -0.046 ± 0.0058 | 0.01 (3) |
| 40+ | 2356 | 0.3947 | 0.05 | +0.3447 ± 0.0052 | 1.0316 | 0.1873 | 0.6445 | 0.1135 | 0.0679 | -0.082 ± 0.0044 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 963 | 0.1946 | 0.1947 | -0.0002 ± 0.0005 | 0.5683 | 0.5682 | 0.5074 | 0.4923 | 0.4974 | -0.057 ± 0.0144 | -0.0224 (49) |
| 3-5 | 669 | 0.1922 | 0.1914 | +0.0007 ± 0.0014 | 0.5617 | 0.5587 | 0.4873 | 0.4475 | 0.4559 | -0.057 ± 0.0173 | -0.0194 (34) |
| 5-10 | 1407 | 0.2007 | 0.1943 | +0.0063 ± 0.0018 | 0.5906 | 0.5707 | 0.4963 | 0.4229 | 0.4179 | -0.074 ± 0.0119 | -0.005 (78) |
| 10-15 | 921 | 0.2095 | 0.1987 | +0.0108 ± 0.0037 | 0.6083 | 0.5795 | 0.5179 | 0.3947 | 0.4104 | -0.065 ± 0.015 | 0.0014 (64) |
| 15-25 | 1243 | 0.2302 | 0.2099 | +0.0203 ± 0.0051 | 0.6577 | 0.6047 | 0.5747 | 0.3798 | 0.4264 | -0.069 ± 0.013 | -0.0214 (59) |
| 25-40 | 760 | 0.2489 | 0.2072 | +0.0417 ± 0.0101 | 0.7068 | 0.5956 | 0.6691 | 0.3568 | 0.4461 | -0.085 ± 0.0155 | -0.0219 (26) |
| 40+ | 256 | 0.3542 | 0.1961 | +0.1581 ± 0.0274 | 1.0227 | 0.5738 | 0.8081 | 0.3254 | 0.4219 | -0.098 ± 0.0249 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3147 | 0.183 | 0.1832 | -0.0002 ± 0.0003 | 0.539 | 0.5385 | 0.5072 | 0.4918 | 0.5027 | -0.037 ± 0.0077 | -0.0157 (88) |
| 3-5 | 2173 | 0.1924 | 0.1906 | +0.0018 ± 0.0008 | 0.5627 | 0.5583 | 0.4938 | 0.454 | 0.451 | -0.052 ± 0.0095 | -0.0209 (69) |
| 5-10 | 4356 | 0.1978 | 0.1892 | +0.0086 ± 0.001 | 0.5816 | 0.5564 | 0.4915 | 0.418 | 0.399 | -0.073 ± 0.0067 | -0.0082 (132) |
| 10-15 | 3012 | 0.2051 | 0.1897 | +0.0155 ± 0.002 | 0.5989 | 0.5577 | 0.5249 | 0.4017 | 0.3997 | -0.064 ± 0.0079 | -0.0053 (105) |
| 15-25 | 3794 | 0.2288 | 0.1996 | +0.0292 ± 0.0029 | 0.6603 | 0.5786 | 0.5678 | 0.3721 | 0.3962 | -0.062 ± 0.0073 | -0.0253 (107) |
| 25-40 | 2615 | 0.2598 | 0.1847 | +0.0750 ± 0.0053 | 0.7364 | 0.5384 | 0.6302 | 0.3161 | 0.3564 | -0.076 ± 0.0082 | -0.0229 (51) |
| 40+ | 1174 | 0.3782 | 0.143 | +0.2352 ± 0.0116 | 1.073 | 0.4316 | 0.7292 | 0.2255 | 0.2564 | -0.074 ± 0.0104 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4168 | 1.038 ± 0.043 | 1.135 | 0.1687 | 0.1654 | 0.2135 | 0.2052 |
| gen2 | 4168 | 0.845 ± 0.04 | 1.094 | 0.1696 | 0.166 | 0.2329 | 0.205 |
| gen1_elo | 4168 | 1.016 ± 0.042 | 1.124 | 0.1754 | 0.1655 | 0.2125 | 0.2054 |
| gen1_sr | 4168 | 1.038 ± 0.053 | 1.163 | 0.1303 | 0.168 | 0.2291 | 0.2045 |
| gen1_ledger | 6219 | 0.864 ± 0.03 | 1.078 | 0.1829 | 0.1795 | 0.2182 | 0.1995 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 20,610)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,749 | 23.0% |
| STALE_QUOTE | market_freshness | 4,484 | 21.8% |
| BOOK_QUALITY | execution | 3,844 | 18.6% |
| POOR_DATA | data | 2,342 | 11.4% |
| LIMITED_DATA | data | 1,290 | 6.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,120 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 973 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 863 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 611 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 334 | 1.6% |

Cause class: coverage 23.0%, market_freshness 21.8%, execution 18.6%, data 17.6%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.7%, mapping 4.2%, model_calibration 1.6%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 94.4%, LOW_DATA_QUALITY 71.2%, THIN_PLAYER_HISTORY 60.0%, STALE_PLAYER_DATA 50.2%, STALE_KALSHI_QUOTE 44.4%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 33.4%, WIDE_SPREAD 24.9%, MODEL_HIGH_UNCERTAINTY 17.8%, PLAYER_IDENTITY_RISK 16.2%, LEVEL_TRANSFER_RISK 10.9%, LOW_DISPLAYED_LIQUIDITY 8.0%, EVENT_MAPPING_RISK 8.0%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.1%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.6%, POST_SETTLEMENT_OBSERVATION 23.0%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 11,011)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,809 | 34.6% |
| STALE_QUOTE | market_freshness | 2,052 | 18.6% |
| BOOK_QUALITY | execution | 2,004 | 18.2% |
| POOR_DATA | data | 970 | 8.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 600 | 5.5% |
| IDENTITY_AMBIGUOUS | mapping | 493 | 4.5% |
| LIMITED_DATA | data | 395 | 3.6% |
| IN_PLAY_QUOTE | market_freshness/coverage | 383 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 230 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 75 | 0.7% |

Cause class: coverage 34.6%, market_freshness 18.6%, execution 18.2%, data 12.4%, market_freshness/coverage 8.9%, mapping 4.5%, model_calibration_or_unknown 2.1%, model_calibration 0.7%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.1%, LOW_DATA_QUALITY 74.8%, THIN_PLAYER_HISTORY 62.4%, STALE_KALSHI_QUOTE 52.3%, STALE_PLAYER_DATA 45.1%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 34.6%, WIDE_SPREAD 24.2%, PLAYER_IDENTITY_RISK 19.5%, MODEL_HIGH_UNCERTAINTY 17.9%, LEVEL_TRANSFER_RISK 9.7%, EVENT_MAPPING_RISK 9.7%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 1.8%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.7%, POST_SETTLEMENT_OBSERVATION 34.6%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 8584, "IDENTITY_AMBIGUOUS": 2427}; ticker orientation: {"VERIFIED": 11011}.

Checks: discipline:AMBIGUOUS 741, discipline:PASS 10270, identity_confidence:AMBIGUOUS 2150, identity_confidence:PASS 8861, level_mapping:NA 753, level_mapping:PASS 10258, market_pair:AMBIGUOUS 391, market_pair:NA 277, market_pair:PASS 10343, model_complement:NA 244, model_complement:PASS 10767, namesake:PASS 11011, physical_match_id:NA 3920, physical_match_id:PASS 7091, player_ids:PASS 11011, same_pair_other_event:PASS 11011, ticker_orientation:PASS 11011

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,853 | 4.9% | 4.4% | 1.7% | {"market_freshness": 53, "model_calibration_or_unknown": 43, "data": 35, "execution": 20, "market_freshness/coverage": 13, "model_calibration": 13, "coverage": 11} | 5.86 | 0.22 / 0.2142 (447) | 19.2% | 3.9% | 3.3% | 2.9% |
| CHALLENGER | 7,587 | 17.3% | 6.9% | 11.9% | {"coverage": 742, "market_freshness/coverage": 161, "market_freshness": 147, "data": 130, "model_calibration_or_unknown": 58, "execution": 30, "model_calibration": 27, "mapping": 15} | 7.44 | 0.219 / 0.2077 (1834) | 35.2% | 17.5% | 3.9% | 22.7% |
| DOUBLES | 1,552 | 47.7% | 47.2% | 6.7% | {"execution": 380, "mapping": 195, "market_freshness": 106, "market_freshness/coverage": 53, "coverage": 7} | 23.85 | 0.3148 / 0.2366 (405) | 15.1% | 0.0% | 100.0% | 7.1% |
| ITF_MEN | 13,793 | 25.2% | 17.6% | 31.6% | {"coverage": 1291, "execution": 673, "market_freshness": 593, "data": 460, "market_freshness/coverage": 293, "mapping": 166, "model_calibration_or_unknown": 2, "model_calibration": 1} | 11.86 | 0.2146 / 0.1971 (3125) | 37.7% | 69.1% | 19.3% | 22.1% |
| ITF_WOMEN | 18,416 | 27.0% | 19.7% | 45.2% | {"coverage": 1736, "market_freshness": 1072, "execution": 870, "data": 706, "market_freshness/coverage": 414, "mapping": 111, "model_calibration_or_unknown": 58, "model_calibration": 11} | 12.88 | 0.2026 / 0.1937 (3595) | 39.8% | 56.6% | 9.9% | 22.2% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,708 | 4.8% | 4.2% | 1.2% | {"market_freshness": 41, "model_calibration_or_unknown": 28, "execution": 17, "model_calibration": 12, "data": 11, "market_freshness/coverage": 10, "coverage": 9, "mapping": 1} | 7.81 | 0.2385 / 0.2306 (451) | 24.7% | 1.3% | 1.4% | 3.7% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.6% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 17.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1037 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 15 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 16 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 17 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 18 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 19 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 20 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 21 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 22 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 23 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 24 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 25 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 26 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 27 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 28 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 29 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 30 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 31 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 32 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 33 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 34 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 36 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 37 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 22.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1345 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 38 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 39 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 40 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 41 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 42 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 43 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 468 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 44 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 45 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 46 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 874 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 47 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 48 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 49 | `KXITFWMATCH-26OCT20CHAAPI-CHA` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 555 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 122.0, ratio 20.3); no external reference |
| 50 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 770 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9713, "by_level_share_of_ge_25pp": {"ATP": 0.0171, "CHALLENGER": 0.119, "DOUBLES": 0.0673, "ITF_MEN": 0.316, "ITF_WOMEN": 0.4521, "OTHER": 0.0011, "WTA": 0.0117, "WTA125": 0.0158}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5232, "share_primary_cause_market_settled_or_in_play": 0.4352, "share_primary_cause_stale_quote_only": 0.1864}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 11011, "identity_ambiguous_share": 0.2204, "ticker_orientation": {"VERIFIED": 11011}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 7091, "with_external": 350, "coverage": 0.0494, "external_status": {"EXTERNAL_STALE": 213, "AGREES_WITH_KALSHI": 129, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 213, "MODEL_LONE_OUTLIER": 129, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3686, "share_external_supports_model": 0.0229}, "pregame_clean_ge_25pp": {"n": 3443, "with_external": 327, "coverage": 0.095, "external_status": {"EXTERNAL_STALE": 197, "AGREES_WITH_KALSHI": 122, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 197, "MODEL_LONE_OUTLIER": 122, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3731, "share_external_supports_model": 0.0245}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 480.0, "median_sample_ratio": 2.44, "median_min_matches": 20.0, "median_max_days_since_last": 225.0, "share_severe_asymmetry": 0.2135, "data_status": {"POOR": 6163, "LIMITED": 2917, "ADEQUATE": 1931}, "comparison_lt_10pp": {"median_thinner_serve_points": 1667.0, "median_sample_ratio": 1.71, "median_min_matches": 92.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 826, "model_minus_observed": 0.0466, "kalshi_minus_observed": -0.0912, "brier_diff_model_minus_kalshi": -0.0039}, "4-10x": {"n": 564, "model_minus_observed": 0.0946, "kalshi_minus_observed": -0.0513, "brier_diff_model_minus_kalshi": 0.0136}, "<2x": {"n": 2032, "model_minus_observed": 0.0906, "kalshi_minus_observed": -0.0332, "brier_diff_model_minus_kalshi": 0.0122}, ">=10x": {"n": 746, "model_minus_observed": 0.1063, "kalshi_minus_observed": -0.0692, "brier_diff_model_minus_kalshi": 0.0067}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4168, "model": {"intercept": -0.546, "slope": 0.845, "slope_se": 0.04}, "kalshi_mid_same_rows": {"intercept": 0.217, "slope": 1.094, "slope_se": 0.045}, "mean_extremity_model": 0.1696, "mean_extremity_kalshi": 0.166, "model_brier": 0.2329, "kalshi_brier": 0.205, "brier_diff_model_minus_kalshi": 0.0279, "brier_diff_se": 0.003, "model_logloss": 0.6623, "kalshi_logloss": 0.5927}, "fair_v1": {"n": 4168, "model": {"intercept": -0.41, "slope": 1.038, "slope_se": 0.043}, "kalshi_mid_same_rows": {"intercept": 0.308, "slope": 1.135, "slope_se": 0.045}, "mean_extremity_model": 0.1687, "mean_extremity_kalshi": 0.1654, "model_brier": 0.2135, "kalshi_brier": 0.2052, "brier_diff_model_minus_kalshi": 0.0082, "brier_diff_se": 0.0024, "model_logloss": 0.6156, "kalshi_logloss": 0.593}, "gen1_elo": {"n": 4168, "model": {"intercept": -0.398, "slope": 1.016, "slope_se": 0.042}, "kalshi_mid_same_rows": {"intercept": 0.313, "slope": 1.124, "slope_se": 0.045}, "mean_extremity_model": 0.1754, "mean_extremity_kalshi": 0.1655, "model_brier": 0.2125, "kalshi_brier": 0.2054, "brier_diff_model_minus_kalshi": 0.0071, "brier_diff_se": 0.0024, "model_logloss": 0.6143, "kalshi_logloss": 0.5934}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2481, "share_ge_15": 0.4474, "median_abs_gap": 13.24, "n": 28580}, "gen1_elo": {"share_ge_25": 0.2455, "share_ge_15": 0.4456, "median_abs_gap": 13.02, "n": 28580}, "gen1_sr": {"share_ge_25": 0.3172, "share_ge_15": 0.5286, "median_abs_gap": 16.15, "n": 28580}, "gen2": {"share_ge_25": 0.3202, "share_ge_15": 0.5163, "median_abs_gap": 15.7, "n": 28580}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1555, "share_ge_15": 0.3638, "median_abs_gap": 11.0, "n": 22142}, "gen1_elo": {"share_ge_25": 0.1568, "share_ge_15": 0.3598, "median_abs_gap": 10.73, "n": 22139}, "gen1_sr": {"share_ge_25": 0.2243, "share_ge_15": 0.4514, "median_abs_gap": 13.35, "n": 22143}, "gen2": {"share_ge_25": 0.2402, "share_ge_15": 0.4491, "median_abs_gap": 13.21, "n": 22144}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.86, "share_ge_25_all": 0.0488, "share_ge_25_pregame_clean": 0.0438}, "WTA": {"median_abs_gap_pregame_clean": 7.81, "share_ge_25_all": 0.0476, "share_ge_25_pregame_clean": 0.0422}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2338, "share_within_10pp_all": 0.4304, "share_within_10pp_pregame_clean": 0.4834, "corr_model_vs_mid_pregame_clean": 0.8448}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 613, "model_brier": 0.1995, "kalshi_brier": 0.2005, "brier_diff_model_minus_kalshi": -0.001}, "10-15": {"n_settled": 722, "model_brier": 0.213, "kalshi_brier": 0.2037, "brier_diff_model_minus_kalshi": 0.0093}, "15-25": {"n_settled": 944, "model_brier": 0.2244, "kalshi_brier": 0.2135, "brier_diff_model_minus_kalshi": 0.0109}, "25-40": {"n_settled": 539, "model_brier": 0.2247, "kalshi_brier": 0.2098, "brier_diff_model_minus_kalshi": 0.015}, "3-5": {"n_settled": 389, "model_brier": 0.2023, "kalshi_brier": 0.2017, "brier_diff_model_minus_kalshi": 0.0007}, "40+": {"n_settled": 109, "model_brier": 0.2803, "kalshi_brier": 0.1965, "brier_diff_model_minus_kalshi": 0.0839}, "5-10": {"n_settled": 852, "model_brier": 0.2012, "kalshi_brier": 0.2007, "brier_diff_model_minus_kalshi": 0.0005}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.546, "slope": 0.845, "slope_se": 0.04}, "kalshi_slope": {"intercept": 0.217, "slope": 1.094, "slope_se": 0.045}, "n": 4168}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.507, "slope": 0.864, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.16, "slope": 1.078, "slope_se": 0.035}, "n": 6219}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 405, "model_brier": 0.3148, "kalshi_brier": 0.2366, "brier_diff_model_minus_kalshi": 0.0782, "brier_diff_se": 0.0153, "corr_model_outcome": 0.0162, "corr_kalshi_outcome": 0.2501}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
