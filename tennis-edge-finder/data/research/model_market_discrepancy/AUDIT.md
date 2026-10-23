# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-23T03:13Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 49,862): 0-3 13.9%, 3-5 9.4%, 5-10 19.7%, 10-15 15.3%, 15-25 19.4%, 25-40 14.1%, 40+ 8.2%; median gap 12.16 pp.
* **Where the extremes live**: 97.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.9%, Challenger 11.9%, doubles 6.7%). Main tour: ATP 4.8% and WTA 4.8% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 11,107): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.7%, STALE_QUOTE 18.7%, BOOK_QUALITY 18.1%, POOR_DATA 8.8%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IDENTITY_AMBIGUOUS 4.5%, LIMITED_DATA 3.5%, IN_PLAY_QUOTE 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%. By class: coverage 34.7%, market_freshness 18.7%, execution 18.1%, data 12.3%, market_freshness/coverage 8.9%, mapping 4.5%, model_calibration_or_unknown 2.1%, model_calibration 0.7%.
* **Stale / settled / in-play**: 52.4% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.6% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 11,107 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.1% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.9%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.5% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 480.0 points vs 1667.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.042, Gen-2 0.845, Gen-1 ledger 0.866 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 542 model 0.225 vs Kalshi 0.2095; n 110 model 0.2782 vs Kalshi 0.1983.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 215,043 model-market comparisons (350,241 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 71,310 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-23T03:00:18.318416+00:00'], shadow board 57,520 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-23T03:00:21.780640+00:00'], Model 4 26,959 rows, 19,194 settled tickers, 6,776 tickers with an external scan.
* By model: {"gen1_ledger": 48348, "gen1_elo": 28925, "fair_v1": 28925, "gen2": 28925, "gen1_sr": 28925, "model4_fundamental": 25511, "model4_conditioned": 25484}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 49,862 | 13.9 | 9.4 | 19.7 | 15.3 | 19.4 | 14.1 | 8.2 | 12.16 | 41.7% | 22.3% |
| MW fair_v1 | 28,925 | 12.8 | 8.5 | 18.4 | 15.6 | 19.9 | 15.0 | 9.8 | 13.23 | 44.7% | 24.8% |
| MW gen1_elo | 28,925 | 12.8 | 8.5 | 18.9 | 15.3 | 20.0 | 15.0 | 9.6 | 13.02 | 44.5% | 24.6% |
| MW gen1_ledger | 20,937 | 15.5 | 10.7 | 21.5 | 14.9 | 18.7 | 12.8 | 5.9 | 10.58 | 37.5% | 18.8% |
| MW gen1_sr | 28,925 | 10.0 | 7.0 | 16.5 | 13.7 | 21.1 | 18.9 | 12.9 | 16.14 | 52.8% | 31.8% |
| MW gen2 | 28,925 | 10.9 | 7.2 | 16.2 | 14.1 | 19.5 | 18.1 | 14.0 | 15.68 | 51.6% | 32.1% |
| all families model4_conditioned | 25,484 | 21.8 | 19.0 | 34.7 | 17.8 | 4.3 | 1.4 | 1.0 | 5.97 | 6.8% | 2.5% |
| all families model4_fundamental | 25,511 | 16.6 | 13.3 | 34.0 | 20.6 | 10.7 | 3.5 | 1.3 | 7.83 | 15.5% | 4.8% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 57.0%, >=15pp 41.7%, >=20pp 31.0%, >=25pp 22.3%, >=30pp 16.1%, >=40pp 8.2%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.53pp; >=10pp 45.6%, >=25pp 17.4%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,471 | 28.8 | 14.0 | 24.7 | 14.9 | 11.9 | 4.9 | 0.7 | 6.15 | 17.6% | 5.7% |
| CHALLENGER | 4,532 | 15.9 | 9.9 | 20.4 | 15.6 | 14.8 | 12.3 | 11.0 | 11.08 | 38.1% | 23.3% |
| ITF_MEN | 7,995 | 10.2 | 7.4 | 17.0 | 14.7 | 21.5 | 17.2 | 12.0 | 15.21 | 50.8% | 29.2% |
| ITF_WOMEN | 11,571 | 9.3 | 6.9 | 15.9 | 15.4 | 22.6 | 18.2 | 11.7 | 15.78 | 52.4% | 29.9% |
| WTA | 1,696 | 17.2 | 13.1 | 25.5 | 19.9 | 18.9 | 4.7 | 0.7 | 8.39 | 24.3% | 5.4% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,471 | 23.8 | 15.0 | 25.1 | 17.1 | 13.2 | 4.9 | 1.0 | 6.57 | 19.0% | 5.8% |
| CHALLENGER | 4,532 | 14.8 | 8.7 | 18.6 | 14.7 | 17.3 | 13.9 | 11.9 | 12.49 | 43.1% | 25.8% |
| ITF_MEN | 7,995 | 8.3 | 5.9 | 14.5 | 13.1 | 19.6 | 20.9 | 17.6 | 18.58 | 58.2% | 38.6% |
| ITF_WOMEN | 11,571 | 8.0 | 5.6 | 13.7 | 13.5 | 20.7 | 21.1 | 17.4 | 18.99 | 59.2% | 38.5% |
| WTA | 1,696 | 14.5 | 10.1 | 21.4 | 16.2 | 23.4 | 13.7 | 0.7 | 11.03 | 37.8% | 14.4% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,471 | 24.5 | 12.8 | 23.9 | 15.9 | 14.8 | 6.9 | 1.2 | 7.3 | 22.9% | 8.1% |
| CHALLENGER | 4,532 | 14.3 | 9.3 | 20.6 | 15.5 | 16.3 | 12.8 | 11.2 | 11.47 | 40.3% | 24.0% |
| ITF_MEN | 7,995 | 9.7 | 7.5 | 17.0 | 14.0 | 22.1 | 17.6 | 12.1 | 15.61 | 51.8% | 29.7% |
| ITF_WOMEN | 11,571 | 9.5 | 6.6 | 16.2 | 15.8 | 22.9 | 18.2 | 10.8 | 15.6 | 51.9% | 29.0% |
| WTA | 1,696 | 24.2 | 16.8 | 30.4 | 16.0 | 10.0 | 2.3 | 0.4 | 6.01 | 12.7% | 2.7% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,420 | 25.5 | 19.5 | 30.9 | 11.8 | 8.9 | 3.0 | 0.3 | 5.54 | 12.3% | 3.4% |
| CHALLENGER | 3,109 | 21.5 | 14.7 | 26.4 | 14.2 | 14.8 | 6.5 | 1.9 | 7.29 | 23.1% | 8.4% |
| DOUBLES | 1,560 | 5.5 | 4.2 | 11.5 | 10.3 | 20.9 | 26.3 | 21.4 | 23.92 | 68.5% | 47.6% |
| ITF_MEN | 5,951 | 13.8 | 8.9 | 20.1 | 16.0 | 21.3 | 13.3 | 6.6 | 12.16 | 41.2% | 20.0% |
| ITF_WOMEN | 6,988 | 12.7 | 9.1 | 19.3 | 15.1 | 21.6 | 16.3 | 6.1 | 12.86 | 44.0% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,028 | 22.3 | 15.9 | 29.6 | 18.2 | 10.1 | 3.6 | 0.3 | 6.97 | 14.0% | 3.9% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,404 | 29.1 | 14.3 | 25.1 | 14.8 | 11.7 | 4.5 | 0.5 | 5.99 | 16.7% | 5.0% |
| CHALLENGER | 3,191 | 20.9 | 12.3 | 25.1 | 18.0 | 15.2 | 6.5 | 1.9 | 8.34 | 23.7% | 8.5% |
| ITF_MEN | 5,883 | 12.3 | 8.9 | 20.3 | 16.5 | 22.6 | 14.2 | 5.2 | 12.49 | 41.9% | 19.4% |
| ITF_WOMEN | 8,645 | 11.1 | 8.2 | 18.2 | 17.4 | 24.5 | 15.3 | 5.3 | 13.53 | 45.1% | 20.6% |
| WTA | 1,647 | 17.4 | 12.9 | 25.5 | 20.2 | 18.9 | 4.4 | 0.7 | 8.36 | 24.0% | 5.1% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,404 | 24.1 | 15.3 | 25.2 | 16.9 | 13.2 | 4.5 | 0.6 | 6.48 | 18.3% | 5.2% |
| CHALLENGER | 3,191 | 18.8 | 11.2 | 23.1 | 17.6 | 17.6 | 9.5 | 2.2 | 9.13 | 29.2% | 11.7% |
| ITF_MEN | 5,884 | 9.9 | 7.1 | 16.8 | 15.0 | 21.5 | 19.4 | 10.4 | 15.49 | 51.3% | 29.8% |
| ITF_WOMEN | 8,646 | 9.1 | 6.5 | 15.2 | 15.0 | 22.8 | 20.5 | 11.0 | 16.58 | 54.3% | 31.5% |
| WTA | 1,647 | 14.6 | 10.1 | 21.4 | 16.1 | 23.4 | 13.6 | 0.7 | 11.03 | 37.8% | 14.3% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,376 | 25.7 | 19.8 | 30.9 | 12.1 | 8.4 | 2.9 | 0.2 | 5.46 | 11.6% | 3.1% |
| CHALLENGER | 2,708 | 23.0 | 15.8 | 27.9 | 14.2 | 14.1 | 4.4 | 0.6 | 6.69 | 19.1% | 5.0% |
| DOUBLES | 1,449 | 5.5 | 4.4 | 11.7 | 10.4 | 20.8 | 26.2 | 20.9 | 23.85 | 67.9% | 47.1% |
| ITF_MEN | 4,978 | 15.0 | 9.6 | 21.8 | 16.8 | 21.2 | 11.6 | 4.0 | 11.14 | 36.9% | 15.7% |
| ITF_WOMEN | 5,787 | 13.6 | 9.6 | 20.7 | 15.9 | 21.8 | 15.0 | 3.4 | 11.67 | 40.2% | 18.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 978 | 22.8 | 16.5 | 29.6 | 18.2 | 10.1 | 2.9 | 0.0 | 6.82 | 13.0% | 2.9% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,560 | 5.5 | 4.2 | 11.5 | 10.3 | 20.9 | 26.3 | 21.4 | 23.92 | 68.5% | 47.6% |
| singles | 19,377 | 16.3 | 11.3 | 22.3 | 15.2 | 18.5 | 11.8 | 4.7 | 10.03 | 34.9% | 16.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 6,440 | 13.1 | 8.8 | 19.1 | 15.7 | 18.8 | 14.7 | 9.8 | 12.89 | 43.3% | 24.5% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 17,932 | 13.2 | 8.5 | 18.4 | 15.3 | 20.0 | 14.8 | 9.8 | 13.16 | 44.5% | 24.5% |
| UNKNOWN | 4,316 | 10.7 | 7.8 | 17.2 | 16.9 | 20.8 | 16.2 | 10.5 | 14.06 | 47.5% | 26.7% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,033 | 19.7 | 11.7 | 21.4 | 16.5 | 15.5 | 9.0 | 6.2 | 9.19 | 30.8% | 15.3% |
| B | 3,600 | 12.4 | 8.8 | 19.9 | 16.4 | 19.3 | 12.5 | 10.7 | 12.51 | 42.4% | 23.2% |
| C | 4,087 | 11.5 | 8.8 | 19.7 | 15.2 | 19.5 | 14.8 | 10.5 | 13.18 | 44.8% | 25.3% |
| D | 4,598 | 12.1 | 7.8 | 17.2 | 15.4 | 21.6 | 15.7 | 10.2 | 14.02 | 47.4% | 25.9% |
| F | 8,607 | 7.6 | 5.6 | 15.0 | 14.7 | 23.5 | 21.3 | 12.4 | 17.73 | 57.1% | 33.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,867 | 23.0 | 15.9 | 28.8 | 15.1 | 11.7 | 4.0 | 1.5 | 6.67 | 17.2% | 5.5% |
| B | 2,868 | 16.2 | 10.4 | 23.3 | 16.1 | 19.4 | 10.6 | 3.9 | 10.02 | 33.9% | 14.6% |
| C | 4,136 | 11.4 | 7.4 | 18.3 | 14.1 | 21.5 | 16.6 | 10.6 | 14.32 | 48.7% | 27.3% |
| D | 2,960 | 14.5 | 9.8 | 19.9 | 14.4 | 20.9 | 14.3 | 6.1 | 11.93 | 41.3% | 20.4% |
| F | 5,106 | 10.2 | 8.3 | 15.5 | 14.8 | 22.8 | 20.2 | 8.2 | 15.67 | 51.2% | 28.5% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 9,237 | 17.8 | 10.5 | 20.7 | 16.4 | 16.1 | 9.9 | 8.7 | 10.32 | 34.7% | 18.6% |
| LIMITED | 6,185 | 13.4 | 10.1 | 20.4 | 15.6 | 19.3 | 13.5 | 7.7 | 11.95 | 40.5% | 21.2% |
| POOR | 13,503 | 9.2 | 6.4 | 15.9 | 15.0 | 22.8 | 19.1 | 11.6 | 16.17 | 53.4% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,534 | 26.4 | 20.3 | 34.4 | 12.6 | 4.8 | 1.4 | 0.2 | 5.35 | 6.4% | 1.6% |
| GAME_SPREAD | 4,667 | 22.2 | 15.2 | 33.5 | 17.4 | 9.0 | 2.4 | 0.3 | 6.72 | 11.7% | 2.7% |
| MATCH_WINNER | 20,937 | 15.5 | 10.7 | 21.5 | 14.9 | 18.7 | 12.8 | 5.9 | 10.58 | 37.5% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 9,757 | 29.2 | 17.1 | 31.2 | 12.4 | 8.1 | 1.7 | 0.4 | 5.47 | 10.1% | 2.0% |
| TOTAL_GAMES | 7,429 | 8.5 | 9.6 | 36.5 | 28.9 | 10.5 | 3.2 | 2.6 | 9.47 | 16.4% | 5.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,905 | 25.4 | 33.7 | 32.7 | 4.5 | 2.9 | 0.6 | 0.2 | 4.48 | 3.7% | 0.8% |
| GAME_SPREAD | 6,114 | 45.4 | 16.7 | 27.1 | 7.9 | 1.8 | 0.9 | 0.3 | 3.52 | 3.0% | 1.2% |
| TOTAL_GAMES | 10,465 | 4.9 | 7.7 | 40.8 | 34.8 | 7.0 | 2.5 | 2.1 | 9.62 | 11.7% | 4.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,908 | 24.3 | 17.8 | 35.6 | 12.7 | 7.0 | 2.5 | 0.3 | 5.82 | 9.8% | 2.8% |
| GAME_SPREAD | 6,117 | 19.2 | 13.3 | 27.9 | 20.6 | 13.5 | 4.4 | 0.9 | 7.99 | 18.9% | 5.4% |
| TOTAL_GAMES | 10,486 | 8.5 | 9.4 | 36.3 | 27.5 | 12.3 | 3.7 | 2.3 | 9.5 | 18.3% | 6.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 28,925 | 44.7% | 24.8% | 13.23 | 36.3% | 15.6% | 11.0 |
| gen1_elo | 28,925 | 44.5% | 24.6% | 13.02 | 36.0% | 15.7% | 10.76 |
| gen1_sr | 28,925 | 52.8% | 31.8% | 16.14 | 45.1% | 22.4% | 13.31 |
| gen2 | 28,925 | 51.6% | 32.1% | 15.68 | 44.8% | 24.0% | 13.18 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 14,583 | 15.7 | 10.3 | 21.1 | 17.2 | 20.4 | 11.9 | 3.3 | 10.8 | 35.6% | 15.3% |
| STALE | 14,342 | 9.9 | 6.7 | 15.6 | 13.9 | 19.4 | 18.1 | 16.5 | 16.87 | 53.9% | 34.5% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 14,405 | 16.5 | 11.3 | 22.3 | 14.9 | 17.9 | 12.2 | 4.9 | 9.99 | 35.0% | 17.1% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 49,862 | 14405 | 18055 | 17402 | 24.1 | 145.1 | 1400.4 |
| ge_15pp | 20,772 | 5042 | 6482 | 9248 | 26.3 | 440.0 | 1380.4 |
| ge_25pp | 11,107 | 2464 | 2817 | 5826 | 32.5 | 580.7 | 1380.4 |
| lt_10pp | 21,467 | 7213 | 8510 | 5744 | 22.3 | 48.5 | 1341.5 |

Current slate `SL-20261023T031326Z-76f59b37`: 429 priced rows, quote age at build {'median': 13.4, 'max': 13.5}, freshness {'AGING': 429}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 22 | 0.0 | 0.0 | 22.7 | 4.5 | 40.9 | 31.8 | 0.0 | 20.48 | 72.7% | 31.8% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,699 | 19.3 | 11.0 | 24.1 | 18.9 | 18.6 | 7.4 | 0.7 | 9.05 | 26.7% | 8.1% |
| KALSHI_LONE_OUTLIER | 17 | 5.9 | 5.9 | 76.5 | 0.0 | 5.9 | 5.9 | 0.0 | 6.11 | 11.8% | 5.9% |
| MARKETS_AGREE | 521 | 66.4 | 33.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.2 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,122 | 0.0 | 2.2 | 35.1 | 26.0 | 25.1 | 10.7 | 0.8 | 12.49 | 36.6% | 11.5% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 28,925 | 4393 (15.2%) | 25.5% | 0.9% | {"EXTERNAL_STALE": 2699, "AGREES_WITH_KALSHI": 1122, "ALL_AGREE": 521, "SUPPORTS_MODEL_DIRECTION": 21, "AGREES_WITH_MODEL": 17, "EXTERNAL_OUTLIER": 12, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 12,931 | 1150 (8.9%) | 35.7% | 1.6% | {"EXTERNAL_STALE": 721, "AGREES_WITH_KALSHI": 411, "SUPPORTS_MODEL_DIRECTION": 16, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 7,181 | 355 (4.9%) | 36.3% | 2.2% | {"EXTERNAL_STALE": 218, "AGREES_WITH_KALSHI": 129, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,488 | 332 (9.5%) | 36.8% | 2.4% | {"EXTERNAL_STALE": 202, "AGREES_WITH_KALSHI": 122, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 11,485 | 2440 (21.2%) | 17.2% | 0.8% | {"EXTERNAL_STALE": 1468, "ALL_AGREE": 521, "AGREES_WITH_KALSHI": 419, "AGREES_WITH_MODEL": 15, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 4, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,511 | 10.3 | 7.5 | 19.2 | 14.4 | 22.6 | 16.0 | 10.0 | 14.28 | 48.6% | 26.0% |
| 4-10x | 3,783 | 10.9 | 8.4 | 19.3 | 15.4 | 21.0 | 14.9 | 10.1 | 13.67 | 46.0% | 25.0% |
| <2x | 14,637 | 14.9 | 9.6 | 18.9 | 16.5 | 17.9 | 13.1 | 9.1 | 11.95 | 40.1% | 22.2% |
| >=10x | 4,994 | 11.1 | 6.3 | 15.2 | 14.4 | 22.0 | 19.3 | 11.7 | 16.17 | 53.0% | 31.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 7,302 | 12.3 | 8.5 | 19.5 | 16.1 | 19.5 | 13.6 | 10.5 | 13.0 | 43.7% | 24.1% |
| 300-1000 | 6,237 | 11.6 | 8.6 | 17.3 | 15.3 | 20.7 | 16.2 | 10.3 | 13.99 | 47.2% | 26.5% |
| <300 | 9,548 | 8.7 | 5.7 | 15.5 | 14.9 | 23.0 | 20.0 | 12.2 | 16.86 | 55.2% | 32.2% |
| >=3000 | 5,838 | 21.6 | 12.9 | 23.0 | 16.5 | 14.3 | 7.0 | 4.8 | 7.99 | 26.1% | 11.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 831 | 0.5481 | 0.4102 | 0.5018 | +0.046 | -0.092 | -0.004 ± 0.0054 |
| ratio 4-10x | 567 | 0.586 | 0.4398 | 0.4921 | +0.094 | -0.052 | 0.0132 ± 0.0068 |
| ratio <2x | 2045 | 0.5375 | 0.4135 | 0.4469 | +0.091 | -0.033 | 0.012 ± 0.0032 |
| ratio >=10x | 750 | 0.5679 | 0.392 | 0.46 | +0.108 | -0.068 | 0.0074 ± 0.0067 |
| thinner_sample 1000-3000 | 1134 | 0.5423 | 0.4147 | 0.4497 | +0.093 | -0.035 | 0.0102 ± 0.0042 |
| thinner_sample 300-1000 | 965 | 0.5644 | 0.4216 | 0.4922 | +0.072 | -0.071 | 0.0008 ± 0.0052 |
| thinner_sample <300 | 1412 | 0.5578 | 0.391 | 0.4625 | +0.095 | -0.071 | 0.009 ± 0.0047 |
| thinner_sample >=3000 | 682 | 0.5361 | 0.4411 | 0.4648 | +0.071 | -0.024 | 0.0135 ± 0.0045 |
| data_status ADEQUATE | 1188 | 0.539 | 0.4328 | 0.4529 | +0.086 | -0.020 | 0.0124 ± 0.0036 |
| data_status LIMITED | 981 | 0.5492 | 0.4164 | 0.4791 | +0.070 | -0.063 | 0.0045 ± 0.0048 |
| data_status POOR | 2024 | 0.5602 | 0.3988 | 0.4679 | +0.092 | -0.069 | 0.0074 ± 0.0039 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 613 | 0.1995 | 0.2005 | -0.0010 ± 0.0006 | 0.5793 | 0.5815 | 0.502 | 0.4871 | 0.5318 | -0.060 ± 0.019 | -0.01 (5) |
| 3-5 | 390 | 0.202 | 0.2014 | +0.0006 ± 0.0018 | 0.587 | 0.5839 | 0.5033 | 0.4632 | 0.4744 | -0.098 ± 0.0235 | 0.02 (1) |
| 5-10 | 856 | 0.2012 | 0.2006 | +0.0005 ± 0.0023 | 0.5887 | 0.5842 | 0.5093 | 0.435 | 0.4638 | -0.090 ± 0.0159 | -0.0167 (6) |
| 10-15 | 725 | 0.2131 | 0.2038 | +0.0093 ± 0.0042 | 0.6169 | 0.5892 | 0.5285 | 0.4043 | 0.4276 | -0.103 ± 0.0167 | -0.048 (5) |
| 15-25 | 957 | 0.2237 | 0.2131 | +0.0107 ± 0.0058 | 0.6422 | 0.6098 | 0.5765 | 0.3807 | 0.4514 | -0.089 ± 0.0147 | -0.0033 (9) |
| 25-40 | 542 | 0.225 | 0.2095 | +0.0154 ± 0.0117 | 0.6383 | 0.6023 | 0.6549 | 0.3452 | 0.4723 | -0.075 ± 0.0181 | -0.01 (1) |
| 40+ | 110 | 0.2782 | 0.1983 | +0.0798 ± 0.0369 | 0.7633 | 0.5816 | 0.7555 | 0.3072 | 0.4455 | -0.076 ± 0.0362 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3147 | 0.1823 | 0.1833 | -0.0011 ± 0.0003 | 0.5392 | 0.5405 | 0.4912 | 0.4761 | 0.5145 | -0.017 ± 0.0077 | -0.0129 (17) |
| 3-5 | 2071 | 0.1967 | 0.1954 | +0.0013 ± 0.0008 | 0.5733 | 0.5673 | 0.485 | 0.445 | 0.4486 | -0.053 ± 0.0099 | 0.0 (2) |
| 5-10 | 4474 | 0.197 | 0.1936 | +0.0034 ± 0.001 | 0.5779 | 0.5666 | 0.481 | 0.407 | 0.4207 | -0.047 ± 0.0067 | -0.0119 (21) |
| 10-15 | 3829 | 0.1979 | 0.1801 | +0.0178 ± 0.0017 | 0.5818 | 0.5314 | 0.4861 | 0.3615 | 0.3521 | -0.073 ± 0.0068 | -0.0281 (16) |
| 15-25 | 4842 | 0.2083 | 0.1694 | +0.0389 ± 0.0023 | 0.6099 | 0.5013 | 0.5033 | 0.3069 | 0.3069 | -0.073 ± 0.0059 | -0.0025 (44) |
| 25-40 | 3749 | 0.2235 | 0.1315 | +0.0920 ± 0.0037 | 0.6414 | 0.4008 | 0.5308 | 0.218 | 0.2307 | -0.058 ± 0.0058 | -0.01 (1) |
| 40+ | 2446 | 0.3807 | 0.0453 | +0.3354 ± 0.0049 | 0.9918 | 0.175 | 0.6328 | 0.1074 | 0.0634 | -0.080 ± 0.004 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 473 | 0.2038 | 0.2043 | -0.0005 ± 0.0007 | 0.5894 | 0.5904 | 0.5034 | 0.4883 | 0.5053 | -0.110 ± 0.0223 | -0.01 (3) |
| 3-5 | 342 | 0.2214 | 0.2198 | +0.0017 ± 0.002 | 0.6288 | 0.6252 | 0.5139 | 0.4739 | 0.4678 | -0.114 ± 0.0271 | 0.02 (1) |
| 5-10 | 743 | 0.2045 | 0.2041 | +0.0004 ± 0.0025 | 0.5953 | 0.593 | 0.547 | 0.4722 | 0.5087 | -0.081 ± 0.0171 | -0.01 (4) |
| 10-15 | 694 | 0.2174 | 0.2093 | +0.0081 ± 0.0044 | 0.6245 | 0.6043 | 0.5657 | 0.4414 | 0.4726 | -0.110 ± 0.0181 | -0.04 (5) |
| 15-25 | 984 | 0.2296 | 0.2099 | +0.0197 ± 0.0057 | 0.6522 | 0.6025 | 0.588 | 0.392 | 0.4441 | -0.100 ± 0.0149 | -0.0133 (9) |
| 25-40 | 693 | 0.2614 | 0.199 | +0.0624 ± 0.0107 | 0.7298 | 0.5788 | 0.6526 | 0.3371 | 0.3983 | -0.109 ± 0.0166 | -0.0075 (4) |
| 40+ | 264 | 0.359 | 0.1738 | +0.1852 ± 0.0253 | 0.9879 | 0.5189 | 0.7331 | 0.2485 | 0.3144 | -0.070 ± 0.0246 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2650 | 0.1928 | 0.193 | -0.0002 ± 0.0003 | 0.5625 | 0.5628 | 0.5091 | 0.4942 | 0.5083 | -0.045 ± 0.0088 | -0.0133 (15) |
| 3-5 | 1779 | 0.198 | 0.1975 | +0.0005 ± 0.0008 | 0.5738 | 0.5721 | 0.5152 | 0.4752 | 0.4879 | -0.041 ± 0.0108 | 0.02 (1) |
| 5-10 | 3940 | 0.1936 | 0.1923 | +0.0013 ± 0.001 | 0.5713 | 0.5635 | 0.5074 | 0.4334 | 0.464 | -0.030 ± 0.0071 | -0.0117 (6) |
| 10-15 | 3457 | 0.2004 | 0.1873 | +0.0131 ± 0.0018 | 0.5878 | 0.5473 | 0.5141 | 0.3901 | 0.4003 | -0.059 ± 0.0075 | -0.0189 (18) |
| 15-25 | 4832 | 0.216 | 0.1779 | +0.0381 ± 0.0024 | 0.6278 | 0.5235 | 0.5256 | 0.3296 | 0.334 | -0.069 ± 0.0061 | -0.0086 (42) |
| 25-40 | 4411 | 0.2505 | 0.1392 | +0.1113 ± 0.0036 | 0.7058 | 0.4256 | 0.5575 | 0.2408 | 0.226 | -0.081 ± 0.0056 | -0.0044 (18) |
| 40+ | 3489 | 0.3949 | 0.0623 | +0.3326 ± 0.0048 | 1.04 | 0.2214 | 0.6527 | 0.1206 | 0.0871 | -0.071 ± 0.0041 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 588 | 0.2003 | 0.2025 | -0.0023 ± 0.0007 | 0.5817 | 0.5872 | 0.4982 | 0.483 | 0.5493 | -0.025 ± 0.0191 | -0.0137 (8) |
| 3-5 | 420 | 0.2 | 0.198 | +0.0019 ± 0.0018 | 0.5816 | 0.5757 | 0.5047 | 0.465 | 0.4619 | -0.118 ± 0.0225 | 0.0067 (3) |
| 5-10 | 881 | 0.1996 | 0.1963 | +0.0034 ± 0.0023 | 0.5856 | 0.5734 | 0.5068 | 0.4328 | 0.4449 | -0.100 ± 0.0153 | -0.0071 (7) |
| 10-15 | 731 | 0.2089 | 0.2053 | +0.0036 ± 0.0042 | 0.6068 | 0.5928 | 0.5384 | 0.4148 | 0.4637 | -0.086 ± 0.0166 | -0.0317 (6) |
| 15-25 | 897 | 0.2298 | 0.2116 | +0.0182 ± 0.006 | 0.6575 | 0.6062 | 0.5867 | 0.3921 | 0.4415 | -0.110 ± 0.0153 | -0.03 (1) |
| 25-40 | 561 | 0.2143 | 0.2176 | -0.0033 ± 0.0116 | 0.6167 | 0.621 | 0.6665 | 0.3546 | 0.5134 | -0.052 ± 0.0178 | 0.015 (2) |
| 40+ | 115 | 0.2941 | 0.2091 | +0.0849 ± 0.0373 | 0.81 | 0.6055 | 0.7633 | 0.3127 | 0.4522 | -0.073 ± 0.0387 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3104 | 0.1857 | 0.1863 | -0.0006 ± 0.0003 | 0.5461 | 0.5471 | 0.4909 | 0.4758 | 0.4923 | -0.036 ± 0.0078 | -0.0163 (35) |
| 3-5 | 2080 | 0.1929 | 0.1903 | +0.0025 ± 0.0008 | 0.5673 | 0.5594 | 0.4883 | 0.4486 | 0.4375 | -0.071 ± 0.0098 | -0.0094 (18) |
| 5-10 | 4554 | 0.1946 | 0.1884 | +0.0062 ± 0.001 | 0.5731 | 0.553 | 0.484 | 0.4101 | 0.4051 | -0.064 ± 0.0065 | -0.01 (31) |
| 10-15 | 3705 | 0.1918 | 0.1755 | +0.0162 ± 0.0017 | 0.5673 | 0.5193 | 0.4975 | 0.374 | 0.3695 | -0.070 ± 0.0069 | -0.015 (12) |
| 15-25 | 4987 | 0.21 | 0.1713 | +0.0387 ± 0.0023 | 0.6139 | 0.5061 | 0.512 | 0.3169 | 0.3152 | -0.073 ± 0.0058 | -0.03 (2) |
| 25-40 | 3747 | 0.22 | 0.135 | +0.0850 ± 0.0038 | 0.6343 | 0.4085 | 0.5369 | 0.2208 | 0.2461 | -0.048 ± 0.0058 | 0.01 (3) |
| 40+ | 2381 | 0.3947 | 0.05 | +0.3448 ± 0.0052 | 1.0316 | 0.1871 | 0.6446 | 0.1135 | 0.068 | -0.082 ± 0.0044 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 967 | 0.1942 | 0.1944 | -0.0002 ± 0.0005 | 0.5675 | 0.5674 | 0.5066 | 0.4914 | 0.4964 | -0.058 ± 0.0144 | -0.0224 (49) |
| 3-5 | 673 | 0.1914 | 0.1907 | +0.0006 ± 0.0014 | 0.5601 | 0.5573 | 0.488 | 0.4482 | 0.4577 | -0.056 ± 0.0172 | -0.0194 (34) |
| 5-10 | 1410 | 0.2007 | 0.1944 | +0.0062 ± 0.0018 | 0.5905 | 0.5709 | 0.4962 | 0.4228 | 0.4184 | -0.074 ± 0.0119 | -0.005 (78) |
| 10-15 | 928 | 0.2098 | 0.1985 | +0.0113 ± 0.0036 | 0.6089 | 0.5791 | 0.5186 | 0.3954 | 0.4095 | -0.067 ± 0.0149 | 0.0014 (64) |
| 15-25 | 1250 | 0.2307 | 0.2098 | +0.0208 ± 0.0051 | 0.6589 | 0.6045 | 0.5751 | 0.3801 | 0.4256 | -0.070 ± 0.013 | -0.0214 (59) |
| 25-40 | 765 | 0.2482 | 0.2072 | +0.0411 ± 0.0101 | 0.7051 | 0.5954 | 0.6696 | 0.3572 | 0.4471 | -0.085 ± 0.0154 | -0.0219 (26) |
| 40+ | 256 | 0.3542 | 0.1961 | +0.1581 ± 0.0274 | 1.0227 | 0.5738 | 0.8081 | 0.3254 | 0.4219 | -0.098 ± 0.0249 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3158 | 0.1826 | 0.1827 | -0.0002 ± 0.0003 | 0.5379 | 0.5374 | 0.5066 | 0.4912 | 0.5019 | -0.037 ± 0.0077 | -0.0157 (88) |
| 3-5 | 2185 | 0.1918 | 0.1901 | +0.0017 ± 0.0007 | 0.5614 | 0.5573 | 0.4945 | 0.4548 | 0.4531 | -0.051 ± 0.0094 | -0.0209 (69) |
| 5-10 | 4380 | 0.1975 | 0.189 | +0.0085 ± 0.001 | 0.581 | 0.5558 | 0.4917 | 0.4182 | 0.3998 | -0.073 ± 0.0066 | -0.0082 (132) |
| 10-15 | 3026 | 0.2051 | 0.1894 | +0.0157 ± 0.002 | 0.5986 | 0.5571 | 0.5251 | 0.4019 | 0.3992 | -0.065 ± 0.0079 | -0.0053 (105) |
| 15-25 | 3819 | 0.2292 | 0.1994 | +0.0298 ± 0.0029 | 0.6614 | 0.5781 | 0.5679 | 0.3722 | 0.3946 | -0.064 ± 0.0073 | -0.0253 (107) |
| 25-40 | 2642 | 0.2597 | 0.1845 | +0.0752 ± 0.0053 | 0.7359 | 0.5379 | 0.6306 | 0.3166 | 0.3562 | -0.078 ± 0.0081 | -0.0229 (51) |
| 40+ | 1177 | 0.3778 | 0.1437 | +0.2342 ± 0.0116 | 1.0719 | 0.4332 | 0.7291 | 0.2254 | 0.2574 | -0.072 ± 0.0104 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4193 | 1.042 ± 0.043 | 1.137 | 0.1688 | 0.1655 | 0.2133 | 0.2052 |
| gen2 | 4193 | 0.845 ± 0.04 | 1.095 | 0.1695 | 0.166 | 0.233 | 0.2049 |
| gen1_elo | 4193 | 1.017 ± 0.042 | 1.126 | 0.1756 | 0.1656 | 0.2124 | 0.2054 |
| gen1_sr | 4193 | 1.038 ± 0.053 | 1.166 | 0.1302 | 0.168 | 0.2292 | 0.2045 |
| gen1_ledger | 6249 | 0.866 ± 0.03 | 1.08 | 0.1831 | 0.1794 | 0.2181 | 0.1993 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 20,772)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,801 | 23.1% |
| STALE_QUOTE | market_freshness | 4,528 | 21.8% |
| BOOK_QUALITY | execution | 3,864 | 18.6% |
| POOR_DATA | data | 2,354 | 11.3% |
| LIMITED_DATA | data | 1,293 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,130 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 977 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 874 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 617 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 334 | 1.6% |

Cause class: coverage 23.1%, market_freshness 21.8%, execution 18.6%, data 17.6%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.7%, mapping 4.2%, model_calibration 1.6%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.8%, START_UNVERIFIABLE 94.4%, LOW_DATA_QUALITY 71.2%, THIN_PLAYER_HISTORY 60.0%, STALE_PLAYER_DATA 50.0%, STALE_KALSHI_QUOTE 44.5%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 33.4%, WIDE_SPREAD 24.8%, MODEL_HIGH_UNCERTAINTY 17.8%, PLAYER_IDENTITY_RISK 16.2%, LEVEL_TRANSFER_RISK 10.9%, LOW_DISPLAYED_LIQUIDITY 8.1%, EVENT_MAPPING_RISK 8.0%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.1%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.7%, POST_SETTLEMENT_OBSERVATION 23.1%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 11,107)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,850 | 34.7% |
| STALE_QUOTE | market_freshness | 2,075 | 18.7% |
| BOOK_QUALITY | execution | 2,015 | 18.1% |
| POOR_DATA | data | 974 | 8.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 606 | 5.5% |
| IDENTITY_AMBIGUOUS | mapping | 498 | 4.5% |
| LIMITED_DATA | data | 393 | 3.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 388 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 233 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 75 | 0.7% |

Cause class: coverage 34.7%, market_freshness 18.7%, execution 18.1%, data 12.3%, market_freshness/coverage 8.9%, mapping 4.5%, model_calibration_or_unknown 2.1%, model_calibration 0.7%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.1%, LOW_DATA_QUALITY 74.8%, THIN_PLAYER_HISTORY 62.4%, STALE_KALSHI_QUOTE 52.4%, STALE_PLAYER_DATA 44.8%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 34.6%, WIDE_SPREAD 24.1%, PLAYER_IDENTITY_RISK 19.6%, MODEL_HIGH_UNCERTAINTY 18.0%, LEVEL_TRANSFER_RISK 9.7%, EVENT_MAPPING_RISK 9.6%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 1.8%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.8%, POST_SETTLEMENT_OBSERVATION 34.7%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 8653, "IDENTITY_AMBIGUOUS": 2454}; ticker orientation: {"VERIFIED": 11107}.

Checks: discipline:AMBIGUOUS 743, discipline:PASS 10364, identity_confidence:AMBIGUOUS 2177, identity_confidence:PASS 8930, level_mapping:NA 755, level_mapping:PASS 10352, market_pair:AMBIGUOUS 391, market_pair:NA 279, market_pair:PASS 10437, model_complement:NA 246, model_complement:PASS 10861, namesake:PASS 11107, physical_match_id:NA 3926, physical_match_id:PASS 7181, player_ids:PASS 11107, same_pair_other_event:PASS 11107, ticker_orientation:PASS 11107

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,891 | 4.8% | 4.3% | 1.7% | {"market_freshness": 53, "model_calibration_or_unknown": 43, "data": 35, "execution": 20, "market_freshness/coverage": 13, "model_calibration": 13, "coverage": 11} | 5.86 | 0.2187 / 0.2133 (451) | 19.2% | 3.8% | 3.2% | 2.9% |
| CHALLENGER | 7,641 | 17.2% | 6.9% | 11.9% | {"coverage": 749, "market_freshness/coverage": 163, "market_freshness": 147, "data": 128, "model_calibration_or_unknown": 58, "execution": 30, "model_calibration": 27, "mapping": 15} | 7.42 | 0.2198 / 0.2081 (1844) | 35.3% | 17.6% | 3.9% | 22.8% |
| DOUBLES | 1,560 | 47.6% | 47.1% | 6.7% | {"execution": 381, "mapping": 196, "market_freshness": 106, "market_freshness/coverage": 53, "coverage": 7} | 23.85 | 0.3137 / 0.2366 (410) | 15.0% | 0.0% | 100.0% | 7.1% |
| ITF_MEN | 13,946 | 25.3% | 17.7% | 31.7% | {"coverage": 1308, "execution": 680, "market_freshness": 605, "data": 465, "market_freshness/coverage": 296, "mapping": 166, "model_calibration_or_unknown": 2, "model_calibration": 1} | 11.86 | 0.2145 / 0.1969 (3137) | 37.9% | 69.3% | 19.5% | 22.1% |
| ITF_WOMEN | 18,559 | 27.0% | 19.7% | 45.2% | {"coverage": 1753, "market_freshness": 1082, "execution": 873, "data": 705, "market_freshness/coverage": 420, "mapping": 115, "model_calibration_or_unknown": 60, "model_calibration": 11} | 12.87 | 0.2022 / 0.1934 (3619) | 39.9% | 56.4% | 9.9% | 22.2% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,724 | 4.8% | 4.3% | 1.2% | {"market_freshness": 42, "model_calibration_or_unknown": 29, "execution": 17, "model_calibration": 12, "data": 11, "market_freshness/coverage": 10, "coverage": 9, "mapping": 1} | 7.78 | 0.2385 / 0.2306 (451) | 24.7% | 1.2% | 1.4% | 3.6% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.6% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 15.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 928 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 15 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 16 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 17 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 18 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 19 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 20 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 21 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 22 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 23 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 365 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 24 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 25 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 26 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 27 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 28 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 29 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 30 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 31 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 32 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 33 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 34 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 36 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 37 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 321 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 38 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 39 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 40 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 41 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 42 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 43 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 162 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 44 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 45 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 46 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 874 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 47 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 48 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 49 | `KXITFWMATCH-26OCT20CHAAPI-CHA` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 122.0, ratio 20.3); no external reference |
| 50 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.2h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 196 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9714, "by_level_share_of_ge_25pp": {"ATP": 0.0169, "CHALLENGER": 0.1186, "DOUBLES": 0.0669, "ITF_MEN": 0.3172, "ITF_WOMEN": 0.4519, "OTHER": 0.0011, "WTA": 0.0118, "WTA125": 0.0157}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5245, "share_primary_cause_market_settled_or_in_play": 0.4361, "share_primary_cause_stale_quote_only": 0.1868}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 11107, "identity_ambiguous_share": 0.2209, "ticker_orientation": {"VERIFIED": 11107}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 7181, "with_external": 355, "coverage": 0.0494, "external_status": {"EXTERNAL_STALE": 218, "AGREES_WITH_KALSHI": 129, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 218, "MODEL_LONE_OUTLIER": 129, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3634, "share_external_supports_model": 0.0225}, "pregame_clean_ge_25pp": {"n": 3488, "with_external": 332, "coverage": 0.0952, "external_status": {"EXTERNAL_STALE": 202, "AGREES_WITH_KALSHI": 122, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 202, "MODEL_LONE_OUTLIER": 122, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3675, "share_external_supports_model": 0.0241}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 480.0, "median_sample_ratio": 2.44, "median_min_matches": 20.0, "median_max_days_since_last": 225.0, "share_severe_asymmetry": 0.2136, "data_status": {"POOR": 6219, "LIMITED": 2929, "ADEQUATE": 1959}, "comparison_lt_10pp": {"median_thinner_serve_points": 1667.0, "median_sample_ratio": 1.71, "median_min_matches": 92.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 831, "model_minus_observed": 0.0463, "kalshi_minus_observed": -0.0916, "brier_diff_model_minus_kalshi": -0.004}, "4-10x": {"n": 567, "model_minus_observed": 0.0939, "kalshi_minus_observed": -0.0523, "brier_diff_model_minus_kalshi": 0.0132}, "<2x": {"n": 2045, "model_minus_observed": 0.0906, "kalshi_minus_observed": -0.0334, "brier_diff_model_minus_kalshi": 0.012}, ">=10x": {"n": 750, "model_minus_observed": 0.1079, "kalshi_minus_observed": -0.068, "brier_diff_model_minus_kalshi": 0.0074}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4193, "model": {"intercept": -0.546, "slope": 0.845, "slope_se": 0.04}, "kalshi_mid_same_rows": {"intercept": 0.218, "slope": 1.095, "slope_se": 0.045}, "mean_extremity_model": 0.1695, "mean_extremity_kalshi": 0.166, "model_brier": 0.233, "kalshi_brier": 0.2049, "brier_diff_model_minus_kalshi": 0.0281, "brier_diff_se": 0.003, "model_logloss": 0.6625, "kalshi_logloss": 0.5924}, "fair_v1": {"n": 4193, "model": {"intercept": -0.412, "slope": 1.042, "slope_se": 0.043}, "kalshi_mid_same_rows": {"intercept": 0.309, "slope": 1.137, "slope_se": 0.045}, "mean_extremity_model": 0.1688, "mean_extremity_kalshi": 0.1655, "model_brier": 0.2133, "kalshi_brier": 0.2052, "brier_diff_model_minus_kalshi": 0.0082, "brier_diff_se": 0.0024, "model_logloss": 0.6152, "kalshi_logloss": 0.5928}, "gen1_elo": {"n": 4193, "model": {"intercept": -0.397, "slope": 1.017, "slope_se": 0.042}, "kalshi_mid_same_rows": {"intercept": 0.316, "slope": 1.126, "slope_se": 0.045}, "mean_extremity_model": 0.1756, "mean_extremity_kalshi": 0.1656, "model_brier": 0.2124, "kalshi_brier": 0.2054, "brier_diff_model_minus_kalshi": 0.007, "brier_diff_se": 0.0024, "model_logloss": 0.614, "kalshi_logloss": 0.5932}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2483, "share_ge_15": 0.4471, "median_abs_gap": 13.23, "n": 28925}, "gen1_elo": {"share_ge_25": 0.2456, "share_ge_15": 0.4455, "median_abs_gap": 13.02, "n": 28925}, "gen1_sr": {"share_ge_25": 0.3177, "share_ge_15": 0.5282, "median_abs_gap": 16.14, "n": 28925}, "gen2": {"share_ge_25": 0.3207, "share_ge_15": 0.5159, "median_abs_gap": 15.68, "n": 28925}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1557, "share_ge_15": 0.3633, "median_abs_gap": 11.0, "n": 22404}, "gen1_elo": {"share_ge_25": 0.157, "share_ge_15": 0.3599, "median_abs_gap": 10.76, "n": 22401}, "gen1_sr": {"share_ge_25": 0.2245, "share_ge_15": 0.4507, "median_abs_gap": 13.31, "n": 22405}, "gen2": {"share_ge_25": 0.2402, "share_ge_15": 0.4483, "median_abs_gap": 13.18, "n": 22406}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.86, "share_ge_25_all": 0.0483, "share_ge_25_pregame_clean": 0.0434}, "WTA": {"median_abs_gap_pregame_clean": 7.78, "share_ge_25_all": 0.0481, "share_ge_25_pregame_clean": 0.0427}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2336, "share_within_10pp_all": 0.4305, "share_within_10pp_pregame_clean": 0.4838, "corr_model_vs_mid_pregame_clean": 0.8447}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 613, "model_brier": 0.1995, "kalshi_brier": 0.2005, "brier_diff_model_minus_kalshi": -0.001}, "10-15": {"n_settled": 725, "model_brier": 0.2131, "kalshi_brier": 0.2038, "brier_diff_model_minus_kalshi": 0.0093}, "15-25": {"n_settled": 957, "model_brier": 0.2237, "kalshi_brier": 0.2131, "brier_diff_model_minus_kalshi": 0.0107}, "25-40": {"n_settled": 542, "model_brier": 0.225, "kalshi_brier": 0.2095, "brier_diff_model_minus_kalshi": 0.0154}, "3-5": {"n_settled": 390, "model_brier": 0.202, "kalshi_brier": 0.2014, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 110, "model_brier": 0.2782, "kalshi_brier": 0.1983, "brier_diff_model_minus_kalshi": 0.0798}, "5-10": {"n_settled": 856, "model_brier": 0.2012, "kalshi_brier": 0.2006, "brier_diff_model_minus_kalshi": 0.0005}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.546, "slope": 0.845, "slope_se": 0.04}, "kalshi_slope": {"intercept": 0.218, "slope": 1.095, "slope_se": 0.045}, "n": 4193}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.509, "slope": 0.866, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.159, "slope": 1.08, "slope_se": 0.035}, "n": 6249}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 410, "model_brier": 0.3137, "kalshi_brier": 0.2366, "brier_diff_model_minus_kalshi": 0.0771, "brier_diff_se": 0.0152, "corr_model_outcome": 0.0255, "corr_kalshi_outcome": 0.2486}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
