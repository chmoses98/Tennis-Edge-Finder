# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-02T13:07Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 10,525): 0-3 13.5%, 3-5 9.0%, 5-10 19.5%, 10-15 14.8%, 15-25 19.6%, 25-40 14.3%, 40+ 9.3%; median gap 12.49 pp.
* **Where the extremes live**: 96.6% of >=25 pp gaps are off the ATP/WTA main tour (ITF 74.3%, Challenger 11.8%, doubles 7.3%). Main tour: ATP 3.9% and WTA 9.2% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 2,491): MARKET_ALREADY_SETTLED_WHEN_PRICED 46.0%, STALE_QUOTE 24.5%, POOR_DATA 6.5%, BOOK_QUALITY 5.9%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IN_PLAY_QUOTE 3.9%, LIMITED_DATA 3.1%, IDENTITY_AMBIGUOUS 2.6%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%. By class: coverage 46.0%, market_freshness 24.5%, data 9.6%, market_freshness/coverage 9.4%, execution 5.9%, mapping 2.6%, model_calibration_or_unknown 2.1%.
* **Stale / settled / in-play**: 69.6% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 55.4% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 2,491 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 15.1% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 0.5%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 6.8% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 783.0 points vs 1970.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.134, Gen-2 0.95, Gen-1 ledger 0.884 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 87 model 0.242 vs Kalshi 0.1797; n 23 model 0.3363 vs Kalshi 0.1395.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 33,418 model-market comparisons (57,485 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 16,302 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-02T13:03:30.725568+00:00'], shadow board 9,170 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-02T13:03:34.326747+00:00'], Model 4 2,833 rows, 8,106 settled tickers, 1,803 tickers with an external scan.
* By model: {"gen1_ledger": 9509, "gen1_elo": 4613, "fair_v1": 4613, "gen2": 4613, "gen1_sr": 4613, "model4_fundamental": 2733, "model4_conditioned": 2724}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 10,525 | 13.5 | 9.0 | 19.5 | 14.8 | 19.6 | 14.3 | 9.3 | 12.49 | 43.3% | 23.7% |
| MW fair_v1 | 4,613 | 13.8 | 8.4 | 18.8 | 14.8 | 18.6 | 15.0 | 10.6 | 12.92 | 44.1% | 25.5% |
| MW gen1_elo | 4,613 | 13.1 | 8.8 | 20.1 | 15.2 | 18.1 | 14.8 | 10.0 | 12.45 | 42.9% | 24.8% |
| MW gen1_ledger | 5,912 | 13.3 | 9.3 | 20.1 | 14.7 | 20.4 | 13.8 | 8.4 | 12.22 | 42.6% | 22.2% |
| MW gen1_sr | 4,613 | 9.8 | 7.1 | 16.9 | 13.2 | 22.3 | 18.4 | 12.3 | 16.17 | 53.0% | 30.7% |
| MW gen2 | 4,613 | 11.4 | 6.4 | 16.6 | 15.3 | 19.7 | 17.1 | 13.6 | 15.19 | 50.3% | 30.7% |
| all families model4_conditioned | 2,724 | 18.6 | 15.4 | 29.4 | 24.1 | 8.4 | 2.2 | 1.9 | 7.38 | 12.6% | 4.2% |
| all families model4_fundamental | 2,733 | 14.3 | 10.7 | 30.3 | 22.1 | 14.4 | 5.3 | 2.9 | 9.1 | 22.6% | 8.2% |

Configurable thresholds (primary): >=5pp 77.5%, >=10pp 58.0%, >=15pp 43.3%, >=20pp 32.6%, >=25pp 23.7%, >=30pp 17.4%, >=40pp 9.3%, >=50pp 4.2%
Executable gap (model outside the book, before fees): median 10.09pp; >=10pp 50.2%, >=25pp 21.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 234 | 22.6 | 17.5 | 26.9 | 13.2 | 14.5 | 1.3 | 3.9 | 6.08 | 19.7% | 5.1% |
| CHALLENGER | 800 | 15.2 | 9.0 | 16.2 | 16.0 | 15.6 | 14.9 | 13.0 | 13.08 | 43.5% | 27.9% |
| ITF_MEN | 1,470 | 11.8 | 8.4 | 19.9 | 14.6 | 18.3 | 14.9 | 12.2 | 12.99 | 45.4% | 27.1% |
| ITF_WOMEN | 1,599 | 11.0 | 6.6 | 16.0 | 14.8 | 20.9 | 19.3 | 11.4 | 15.78 | 51.7% | 30.7% |
| WTA | 426 | 23.2 | 10.6 | 26.1 | 12.9 | 18.3 | 6.8 | 2.1 | 8.09 | 27.2% | 8.9% |
| WTA125 | 84 | 14.3 | 4.8 | 17.9 | 23.8 | 20.2 | 14.3 | 4.8 | 12.4 | 39.3% | 19.1% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 234 | 23.1 | 12.8 | 25.6 | 15.8 | 16.7 | 1.7 | 4.3 | 7.06 | 22.7% | 6.0% |
| CHALLENGER | 800 | 10.9 | 5.5 | 17.9 | 17.2 | 18.4 | 17.6 | 12.5 | 14.84 | 48.5% | 30.1% |
| ITF_MEN | 1,470 | 10.0 | 6.0 | 16.9 | 16.3 | 20.1 | 16.5 | 14.2 | 15.38 | 50.8% | 30.8% |
| ITF_WOMEN | 1,599 | 9.1 | 6.5 | 14.1 | 12.9 | 19.4 | 19.9 | 17.9 | 18.22 | 57.4% | 37.9% |
| WTA | 426 | 20.9 | 5.4 | 17.1 | 15.7 | 22.5 | 16.2 | 2.1 | 12.76 | 40.8% | 18.3% |
| WTA125 | 84 | 6.0 | 6.0 | 16.7 | 20.2 | 22.6 | 15.5 | 13.1 | 15.56 | 51.2% | 28.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 234 | 28.2 | 12.8 | 29.1 | 11.1 | 9.0 | 6.0 | 3.9 | 6.53 | 18.8% | 9.8% |
| CHALLENGER | 800 | 14.9 | 7.9 | 21.1 | 14.5 | 13.9 | 14.2 | 13.5 | 11.99 | 41.6% | 27.8% |
| ITF_MEN | 1,470 | 10.3 | 9.6 | 18.6 | 16.1 | 18.2 | 15.8 | 11.4 | 13.0 | 45.4% | 27.3% |
| ITF_WOMEN | 1,599 | 9.6 | 6.8 | 16.8 | 14.3 | 23.6 | 18.5 | 10.4 | 16.52 | 52.5% | 29.0% |
| WTA | 426 | 23.7 | 13.6 | 29.8 | 15.5 | 11.7 | 4.0 | 1.6 | 6.99 | 17.4% | 5.6% |
| WTA125 | 84 | 16.7 | 6.0 | 22.6 | 29.8 | 13.1 | 10.7 | 1.2 | 10.92 | 25.0% | 11.9% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 72 | 23.6 | 22.2 | 34.7 | 12.5 | 6.9 | 0.0 | 0.0 | 6.26 | 6.9% | 0.0% |
| CHALLENGER | 791 | 21.4 | 13.7 | 26.7 | 15.9 | 13.4 | 6.5 | 2.5 | 7.45 | 22.4% | 9.0% |
| DOUBLES | 371 | 5.4 | 3.8 | 9.7 | 10.5 | 21.8 | 20.8 | 28.0 | 24.15 | 70.6% | 48.8% |
| ITF_MEN | 1,997 | 14.3 | 9.0 | 18.9 | 13.7 | 21.1 | 13.6 | 9.4 | 12.51 | 44.1% | 23.0% |
| ITF_WOMEN | 1,832 | 9.0 | 8.3 | 17.5 | 14.4 | 23.5 | 18.5 | 8.8 | 15.27 | 50.9% | 27.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 363 | 15.4 | 9.4 | 25.6 | 22.3 | 17.6 | 8.8 | 0.8 | 9.8 | 27.3% | 9.6% |
| WTA125 | 337 | 13.3 | 9.5 | 21.7 | 16.9 | 22.9 | 11.9 | 3.9 | 11.35 | 38.6% | 15.7% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 233 | 22.3 | 17.6 | 27.0 | 13.3 | 14.6 | 1.3 | 3.9 | 6.13 | 19.7% | 5.1% |
| CHALLENGER | 591 | 19.1 | 11.2 | 19.6 | 19.1 | 16.6 | 9.1 | 5.2 | 10.11 | 31.0% | 14.4% |
| ITF_MEN | 950 | 15.8 | 11.6 | 24.6 | 15.7 | 18.2 | 10.1 | 4.0 | 9.63 | 32.3% | 14.1% |
| ITF_WOMEN | 1,075 | 14.9 | 8.7 | 19.4 | 17.4 | 22.2 | 13.5 | 4.0 | 12.39 | 39.7% | 17.5% |
| WTA | 425 | 23.3 | 10.6 | 26.1 | 12.9 | 18.4 | 6.6 | 2.1 | 8.09 | 27.1% | 8.7% |
| WTA125 | 81 | 14.8 | 4.9 | 18.5 | 24.7 | 19.8 | 12.3 | 4.9 | 11.65 | 37.0% | 17.3% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 233 | 23.2 | 12.4 | 25.8 | 15.9 | 16.7 | 1.7 | 4.3 | 7.08 | 22.8% | 6.0% |
| CHALLENGER | 591 | 13.4 | 6.9 | 22.5 | 20.8 | 19.6 | 12.5 | 4.2 | 11.82 | 36.4% | 16.8% |
| ITF_MEN | 950 | 13.2 | 7.6 | 20.3 | 18.9 | 20.8 | 13.5 | 5.7 | 12.21 | 40.0% | 19.2% |
| ITF_WOMEN | 1,075 | 11.1 | 8.5 | 16.2 | 12.8 | 22.6 | 17.6 | 11.3 | 15.52 | 51.4% | 28.8% |
| WTA | 425 | 20.9 | 5.4 | 17.2 | 15.8 | 22.6 | 16.0 | 2.1 | 12.75 | 40.7% | 18.1% |
| WTA125 | 81 | 6.2 | 6.2 | 16.1 | 21.0 | 23.5 | 16.1 | 11.1 | 15.33 | 50.6% | 27.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 62 | 24.2 | 25.8 | 35.5 | 12.9 | 1.6 | 0.0 | 0.0 | 5.45 | 1.6% | 0.0% |
| CHALLENGER | 649 | 23.9 | 15.9 | 29.4 | 15.6 | 12.6 | 2.5 | 0.1 | 6.68 | 15.2% | 2.6% |
| DOUBLES | 337 | 5.6 | 3.6 | 9.8 | 10.7 | 21.7 | 21.1 | 27.6 | 24.15 | 70.3% | 48.7% |
| ITF_MEN | 1,428 | 17.5 | 10.8 | 22.2 | 14.7 | 20.9 | 10.3 | 3.6 | 9.91 | 34.8% | 13.9% |
| ITF_WOMEN | 1,244 | 11.0 | 9.7 | 21.2 | 16.5 | 24.5 | 14.9 | 2.1 | 12.15 | 41.6% | 17.0% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 334 | 15.6 | 9.9 | 26.4 | 23.1 | 18.3 | 6.9 | 0.0 | 9.55 | 25.1% | 6.9% |
| WTA125 | 259 | 15.8 | 10.4 | 25.9 | 20.1 | 21.2 | 6.2 | 0.4 | 9.54 | 27.8% | 6.6% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 371 | 5.4 | 3.8 | 9.7 | 10.5 | 21.8 | 20.8 | 28.0 | 24.15 | 70.6% | 48.8% |
| singles | 5,541 | 13.8 | 9.7 | 20.8 | 15.0 | 20.3 | 13.4 | 7.1 | 11.75 | 40.7% | 20.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 996 | 15.8 | 8.2 | 19.0 | 14.3 | 16.4 | 14.1 | 12.3 | 12.24 | 42.8% | 26.4% |
| Hard | 3,313 | 13.2 | 8.8 | 19.0 | 14.6 | 19.1 | 15.2 | 10.1 | 12.96 | 44.4% | 25.3% |
| UNKNOWN | 304 | 13.8 | 5.6 | 15.8 | 19.4 | 20.1 | 15.5 | 9.9 | 13.67 | 45.4% | 25.3% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,428 | 18.2 | 10.0 | 21.1 | 14.9 | 16.9 | 11.0 | 7.8 | 10.14 | 35.7% | 18.8% |
| B | 641 | 17.0 | 10.8 | 18.1 | 17.3 | 15.0 | 10.3 | 11.5 | 11.17 | 36.8% | 21.8% |
| C | 773 | 12.3 | 8.3 | 22.8 | 13.4 | 16.8 | 15.4 | 11.0 | 12.8 | 43.2% | 26.4% |
| D | 850 | 11.9 | 8.3 | 17.4 | 14.0 | 20.8 | 15.5 | 12.0 | 14.29 | 48.4% | 27.5% |
| F | 921 | 7.7 | 4.7 | 13.6 | 14.9 | 23.1 | 23.6 | 12.5 | 18.92 | 59.2% | 36.0% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,813 | 18.9 | 11.9 | 26.2 | 16.8 | 16.4 | 7.0 | 2.8 | 8.61 | 26.2% | 9.8% |
| B | 979 | 13.9 | 9.3 | 21.6 | 16.3 | 19.2 | 12.4 | 7.3 | 11.56 | 38.9% | 19.7% |
| C | 1,219 | 11.2 | 8.3 | 15.7 | 13.9 | 22.2 | 15.4 | 13.3 | 15.42 | 50.9% | 28.7% |
| D | 911 | 11.3 | 8.2 | 20.6 | 12.0 | 23.7 | 15.5 | 8.7 | 14.12 | 47.9% | 24.1% |
| F | 990 | 6.8 | 7.2 | 12.4 | 12.7 | 23.3 | 24.3 | 13.2 | 19.3 | 60.9% | 37.6% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 1,759 | 17.1 | 9.5 | 20.4 | 16.1 | 16.4 | 11.1 | 9.4 | 10.7 | 36.9% | 20.5% |
| LIMITED | 1,065 | 14.9 | 10.2 | 22.0 | 13.3 | 16.1 | 13.5 | 9.9 | 11.46 | 39.5% | 23.4% |
| POOR | 1,789 | 9.8 | 6.4 | 15.3 | 14.5 | 22.2 | 19.6 | 12.1 | 16.88 | 54.0% | 31.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 337 | 34.4 | 22.9 | 33.2 | 6.2 | 2.4 | 0.9 | 0.0 | 4.16 | 3.3% | 0.9% |
| GAME_SPREAD | 406 | 19.9 | 16.5 | 37.0 | 16.0 | 8.9 | 1.2 | 0.5 | 6.59 | 10.6% | 1.7% |
| MATCH_WINNER | 5,912 | 13.3 | 9.3 | 20.1 | 14.7 | 20.4 | 13.8 | 8.4 | 12.22 | 42.6% | 22.2% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 1,698 | 21.8 | 13.5 | 30.4 | 17.3 | 13.7 | 2.8 | 0.7 | 7.05 | 17.1% | 3.4% |
| TOTAL_GAMES | 1,132 | 9.9 | 9.4 | 26.5 | 24.9 | 17.0 | 8.0 | 4.4 | 10.66 | 29.3% | 12.4% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 858 | 28.8 | 32.4 | 26.9 | 0.7 | 9.0 | 1.8 | 0.5 | 4.28 | 11.2% | 2.2% |
| GAME_SPREAD | 544 | 36.8 | 14.9 | 25.0 | 18.4 | 2.6 | 1.6 | 0.7 | 4.56 | 5.0% | 2.4% |
| TOTAL_GAMES | 1,322 | 4.5 | 4.5 | 32.8 | 41.5 | 10.4 | 2.8 | 3.3 | 10.73 | 16.6% | 6.1% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 858 | 25.5 | 17.0 | 33.8 | 8.4 | 9.8 | 4.4 | 1.1 | 5.81 | 15.3% | 5.5% |
| GAME_SPREAD | 544 | 17.1 | 10.3 | 25.9 | 23.5 | 16.0 | 5.0 | 2.2 | 9.59 | 23.2% | 7.2% |
| TOTAL_GAMES | 1,331 | 5.9 | 6.8 | 29.9 | 30.4 | 16.7 | 6.0 | 4.4 | 10.84 | 27.1% | 10.4% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4,613 | 44.1% | 25.5% | 12.92 | 33.0% | 14.0% | 9.95 |
| gen1_elo | 4,613 | 42.9% | 24.8% | 12.45 | 31.3% | 13.9% | 9.51 |
| gen1_sr | 4,613 | 53.0% | 30.7% | 16.17 | 43.5% | 19.6% | 12.7 |
| gen2 | 4,613 | 50.3% | 30.7% | 15.19 | 42.2% | 21.0% | 12.77 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 1,721 | 18.0 | 12.1 | 23.2 | 15.4 | 18.2 | 9.9 | 3.1 | 9.14 | 31.3% | 13.0% |
| STALE | 2,892 | 11.3 | 6.3 | 16.2 | 14.5 | 18.8 | 18.0 | 15.0 | 16.02 | 51.8% | 33.0% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,182 | 15.3 | 10.3 | 21.9 | 15.9 | 19.8 | 12.2 | 4.6 | 10.71 | 36.6% | 16.8% |
| STALE | 2,730 | 11.0 | 8.3 | 18.0 | 13.2 | 21.0 | 15.8 | 12.8 | 14.79 | 49.5% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 10,525 | 0 | 4903 | 5622 | 31.2 | 196.7 | 1400.4 |
| ge_15pp | 4,553 | 0 | 1703 | 2850 | 38.0 | 466.8 | 1380.4 |
| ge_25pp | 2,491 | 0 | 758 | 1733 | 52.9 | 609.3 | 1380.4 |
| lt_10pp | 4,420 | 0 | 2428 | 1992 | 28.8 | 54.8 | 1130.0 |

Current slate `SL-20261002T130747Z-49f1d9b3`: 283 priced rows, quote age at build {'median': 38.7, 'max': 56.9}, freshness {'STALE': 283}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 156 | 22.4 | 12.2 | 23.1 | 20.5 | 17.9 | 3.9 | 0.0 | 7.77 | 21.8% | 3.9% |
| MARKETS_AGREE | 8 | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.96 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 12 | 0.0 | 0.0 | 16.7 | 41.7 | 41.7 | 0.0 | 0.0 | 13.48 | 41.7% | 0.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 4,613 | 177 (3.8%) | 6.8% | 0.0% | {"EXTERNAL_STALE": 156, "AGREES_WITH_KALSHI": 12, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 2,036 | 39 (1.9%) | 12.8% | 0.0% | {"EXTERNAL_STALE": 34, "AGREES_WITH_KALSHI": 5} |
| fair_v1_ge_25pp | 1,178 | 6 (0.5%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 6} |
| fair_v1_ge_25pp_pregame_clean | 470 | 6 (1.3%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 6} |
| fair_v1_lt_10pp | 1,893 | 101 (5.3%) | 2.0% | 0.0% | {"EXTERNAL_STALE": 90, "ALL_AGREE": 8, "AGREES_WITH_KALSHI": 2, "EXTERNAL_OUTLIER": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 907 | 11.9 | 7.4 | 18.6 | 15.4 | 20.4 | 15.7 | 10.6 | 13.74 | 46.6% | 26.2% |
| 4-10x | 621 | 12.2 | 9.5 | 18.7 | 14.2 | 18.0 | 16.6 | 10.8 | 13.37 | 45.4% | 27.4% |
| <2x | 2,537 | 15.4 | 9.1 | 19.6 | 15.0 | 17.7 | 13.0 | 10.2 | 11.93 | 40.9% | 23.1% |
| >=10x | 548 | 10.9 | 5.8 | 15.7 | 13.9 | 20.3 | 21.4 | 12.0 | 16.9 | 53.6% | 33.4% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 1,206 | 14.4 | 8.7 | 21.6 | 15.3 | 16.8 | 12.0 | 11.2 | 11.93 | 40.1% | 23.2% |
| 300-1000 | 1,133 | 13.3 | 7.8 | 17.0 | 15.7 | 20.0 | 16.1 | 10.1 | 13.75 | 46.2% | 26.1% |
| <300 | 1,111 | 8.7 | 6.0 | 14.8 | 13.0 | 22.0 | 22.0 | 13.5 | 18.67 | 57.4% | 35.5% |
| >=3000 | 1,163 | 18.4 | 11.2 | 21.4 | 15.3 | 15.8 | 10.3 | 7.6 | 9.95 | 33.7% | 17.9% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 185 | 0.5142 | 0.3829 | 0.4054 | +0.109 | -0.022 | 0.0175 ± 0.0107 |
| ratio 4-10x | 133 | 0.5822 | 0.4488 | 0.4887 | +0.093 | -0.040 | 0.0103 ± 0.0125 |
| ratio <2x | 366 | 0.5335 | 0.413 | 0.4617 | +0.072 | -0.049 | 0.0099 ± 0.0071 |
| ratio >=10x | 132 | 0.557 | 0.3936 | 0.4545 | +0.102 | -0.061 | 0.0204 ± 0.016 |
| thinner_sample 1000-3000 | 214 | 0.5395 | 0.4204 | 0.4579 | +0.082 | -0.037 | 0.0058 ± 0.0092 |
| thinner_sample 300-1000 | 238 | 0.5539 | 0.4278 | 0.4622 | +0.092 | -0.034 | 0.0094 ± 0.0092 |
| thinner_sample <300 | 266 | 0.5399 | 0.3796 | 0.4436 | +0.096 | -0.064 | 0.022 ± 0.0106 |
| thinner_sample >=3000 | 98 | 0.5145 | 0.4172 | 0.4388 | +0.076 | -0.021 | 0.016 ± 0.0113 |
| data_status ADEQUATE | 220 | 0.5244 | 0.4141 | 0.45 | +0.074 | -0.036 | 0.0077 ± 0.0085 |
| data_status LIMITED | 180 | 0.5592 | 0.4414 | 0.4944 | +0.065 | -0.053 | 0.0028 ± 0.0105 |
| data_status POOR | 416 | 0.5415 | 0.392 | 0.4351 | +0.106 | -0.043 | 0.021 ± 0.0079 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 135 | 0.1754 | 0.1763 | -0.0008 ± 0.0012 | 0.5233 | 0.5257 | 0.4959 | 0.4813 | 0.5037 | -0.089 ± 0.0396 | -0.01 (3) |
| 3-5 | 83 | 0.1682 | 0.1652 | +0.0031 ± 0.0037 | 0.5161 | 0.5045 | 0.5204 | 0.4794 | 0.4578 | -0.120 ± 0.0477 | 0.02 (1) |
| 5-10 | 173 | 0.198 | 0.2002 | -0.0022 ± 0.0051 | 0.5812 | 0.5856 | 0.5178 | 0.4431 | 0.4913 | -0.058 ± 0.0344 | -0.02 (2) |
| 10-15 | 139 | 0.2155 | 0.2086 | +0.0069 ± 0.0097 | 0.6142 | 0.5987 | 0.5283 | 0.4041 | 0.4388 | -0.076 ± 0.0382 | -0.0633 (3) |
| 15-25 | 176 | 0.2126 | 0.2112 | +0.0014 ± 0.0135 | 0.613 | 0.6031 | 0.5619 | 0.3657 | 0.4602 | -0.023 ± 0.0337 | -0.02 (4) |
| 25-40 | 87 | 0.242 | 0.1797 | +0.0623 ± 0.0282 | 0.6747 | 0.5304 | 0.6108 | 0.2961 | 0.3448 | -0.089 ± 0.043 | -0.01 (1) |
| 40+ | 23 | 0.3363 | 0.1395 | +0.1968 ± 0.0707 | 0.9094 | 0.4379 | 0.701 | 0.2565 | 0.2609 | -0.150 ± 0.0784 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 406 | 0.165 | 0.166 | -0.0010 ± 0.0007 | 0.4958 | 0.4984 | 0.5084 | 0.4935 | 0.5345 | -0.024 ± 0.0213 | -0.0188 (8) |
| 3-5 | 253 | 0.1717 | 0.1699 | +0.0019 ± 0.0021 | 0.5236 | 0.5127 | 0.4974 | 0.4572 | 0.4545 | -0.063 ± 0.0267 | 0.02 (1) |
| 5-10 | 578 | 0.1839 | 0.182 | +0.0018 ± 0.0026 | 0.548 | 0.5397 | 0.4734 | 0.3997 | 0.4273 | -0.033 ± 0.0179 | -0.0133 (6) |
| 10-15 | 464 | 0.1918 | 0.1763 | +0.0155 ± 0.0049 | 0.5633 | 0.517 | 0.4775 | 0.3536 | 0.3513 | -0.068 ± 0.0193 | -0.0633 (3) |
| 15-25 | 635 | 0.1916 | 0.1598 | +0.0318 ± 0.0063 | 0.5706 | 0.4732 | 0.4806 | 0.2834 | 0.2992 | -0.044 ± 0.0156 | -0.017 (10) |
| 25-40 | 574 | 0.2138 | 0.096 | +0.1178 ± 0.0081 | 0.6191 | 0.3138 | 0.5013 | 0.1858 | 0.1585 | -0.076 ± 0.0126 | -0.01 (1) |
| 40+ | 411 | 0.367 | 0.0364 | +0.3306 ± 0.0101 | 0.9552 | 0.1536 | 0.6153 | 0.1032 | 0.0462 | -0.087 ± 0.0088 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 82 | 0.1742 | 0.1765 | -0.0023 ± 0.0016 | 0.5217 | 0.5254 | 0.5205 | 0.5059 | 0.5854 | -0.015 ± 0.0449 | -0.01 (1) |
| 3-5 | 62 | 0.2111 | 0.211 | +0.0001 ± 0.0047 | 0.6018 | 0.6091 | 0.4947 | 0.4556 | 0.4677 | -0.064 ± 0.0619 | 0.02 (1) |
| 5-10 | 156 | 0.1862 | 0.1788 | +0.0074 ± 0.0052 | 0.5544 | 0.5351 | 0.5767 | 0.501 | 0.4808 | -0.131 ± 0.0341 | -0.01 (3) |
| 10-15 | 150 | 0.2165 | 0.2062 | +0.0103 ± 0.0094 | 0.6196 | 0.5979 | 0.5755 | 0.4508 | 0.48 | -0.072 ± 0.0381 | -0.0667 (3) |
| 15-25 | 194 | 0.2209 | 0.1963 | +0.0247 ± 0.0126 | 0.6266 | 0.567 | 0.5839 | 0.3869 | 0.4278 | -0.084 ± 0.0326 | -0.0167 (3) |
| 25-40 | 120 | 0.2554 | 0.1921 | +0.0633 ± 0.0246 | 0.7132 | 0.5586 | 0.654 | 0.3452 | 0.3917 | -0.106 ± 0.0409 | -0.025 (2) |
| 40+ | 52 | 0.3781 | 0.1949 | +0.1832 ± 0.0617 | 1.0423 | 0.5744 | 0.7455 | 0.2528 | 0.3269 | -0.042 ± 0.0601 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 325 | 0.1567 | 0.1585 | -0.0018 ± 0.0007 | 0.4735 | 0.4785 | 0.5527 | 0.538 | 0.5938 | +0.003 ± 0.0222 | -0.0217 (6) |
| 3-5 | 194 | 0.1745 | 0.1739 | +0.0006 ± 0.0024 | 0.5168 | 0.5222 | 0.5551 | 0.5157 | 0.5258 | -0.041 ± 0.0302 | 0.02 (1) |
| 5-10 | 514 | 0.1784 | 0.1746 | +0.0038 ± 0.0028 | 0.5332 | 0.5183 | 0.5225 | 0.447 | 0.4572 | -0.050 ± 0.0185 | -0.01 (4) |
| 10-15 | 499 | 0.1884 | 0.1762 | +0.0122 ± 0.0047 | 0.5587 | 0.5201 | 0.5194 | 0.3953 | 0.4168 | -0.038 ± 0.019 | -0.0575 (4) |
| 15-25 | 642 | 0.2024 | 0.1575 | +0.0449 ± 0.0062 | 0.591 | 0.4714 | 0.5107 | 0.3151 | 0.3037 | -0.082 ± 0.0157 | -0.0143 (7) |
| 25-40 | 614 | 0.2234 | 0.1181 | +0.1053 ± 0.0088 | 0.6467 | 0.3663 | 0.5423 | 0.2275 | 0.2199 | -0.066 ± 0.014 | -0.015 (6) |
| 40+ | 533 | 0.4018 | 0.0633 | +0.3385 ± 0.0126 | 1.0544 | 0.2269 | 0.6618 | 0.1246 | 0.0919 | -0.066 ± 0.0105 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 129 | 0.1717 | 0.1737 | -0.0020 ± 0.0013 | 0.5121 | 0.5175 | 0.5154 | 0.501 | 0.5426 | -0.046 ± 0.037 | -0.01 (5) |
| 3-5 | 89 | 0.1694 | 0.1678 | +0.0017 ± 0.0035 | 0.5119 | 0.5077 | 0.5098 | 0.4703 | 0.4719 | -0.109 ± 0.0465 | -- (0) |
| 5-10 | 167 | 0.2033 | 0.2027 | +0.0006 ± 0.0052 | 0.5974 | 0.5895 | 0.5083 | 0.436 | 0.4671 | -0.067 ± 0.0351 | -0.01 (2) |
| 10-15 | 147 | 0.2099 | 0.2049 | +0.0050 ± 0.0093 | 0.6062 | 0.591 | 0.5498 | 0.426 | 0.4762 | -0.073 ± 0.0378 | -0.044 (5) |
| 15-25 | 170 | 0.2136 | 0.2056 | +0.0080 ± 0.0134 | 0.6196 | 0.5915 | 0.5755 | 0.3822 | 0.4588 | -0.042 ± 0.0334 | -0.03 (1) |
| 25-40 | 96 | 0.2381 | 0.1897 | +0.0484 ± 0.0276 | 0.6691 | 0.5569 | 0.6037 | 0.2904 | 0.3646 | -0.070 ± 0.0414 | 0.0 (1) |
| 40+ | 18 | 0.3586 | 0.1556 | +0.2030 ± 0.0855 | 0.9645 | 0.4759 | 0.7164 | 0.2647 | 0.2778 | -0.161 ± 0.0975 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 389 | 0.1653 | 0.1654 | -0.0001 ± 0.0007 | 0.4987 | 0.4996 | 0.5073 | 0.4927 | 0.5064 | -0.048 ± 0.0208 | -0.0162 (13) |
| 3-5 | 263 | 0.1788 | 0.175 | +0.0038 ± 0.0021 | 0.5326 | 0.5217 | 0.4888 | 0.4497 | 0.4259 | -0.087 ± 0.0262 | -0.01 (2) |
| 5-10 | 572 | 0.1878 | 0.1831 | +0.0048 ± 0.0027 | 0.5584 | 0.5368 | 0.4666 | 0.3929 | 0.4003 | -0.049 ± 0.018 | -0.01 (2) |
| 10-15 | 483 | 0.1917 | 0.1754 | +0.0163 ± 0.0047 | 0.5667 | 0.5184 | 0.4911 | 0.3677 | 0.3644 | -0.070 ± 0.0191 | -0.03 (9) |
| 15-25 | 666 | 0.1832 | 0.1503 | +0.0329 ± 0.006 | 0.5533 | 0.451 | 0.4863 | 0.2875 | 0.3048 | -0.041 ± 0.0147 | -0.03 (2) |
| 25-40 | 565 | 0.2158 | 0.0984 | +0.1174 ± 0.0083 | 0.6248 | 0.3182 | 0.498 | 0.1803 | 0.1558 | -0.077 ± 0.0127 | 0.0 (1) |
| 40+ | 383 | 0.3835 | 0.0362 | +0.3473 ± 0.0106 | 1.0016 | 0.1545 | 0.6202 | 0.1028 | 0.0366 | -0.096 ± 0.009 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 414 | 0.2046 | 0.2047 | -0.0000 ± 0.0007 | 0.5918 | 0.5922 | 0.4988 | 0.4842 | 0.4855 | -0.042 ± 0.0223 | -0.0226 (46) |
| 3-5 | 296 | 0.1951 | 0.194 | +0.0011 ± 0.0021 | 0.572 | 0.5659 | 0.4657 | 0.4259 | 0.4358 | -0.040 ± 0.0254 | -0.0059 (32) |
| 5-10 | 630 | 0.1865 | 0.1812 | +0.0053 ± 0.0025 | 0.556 | 0.5417 | 0.459 | 0.3856 | 0.3873 | -0.044 ± 0.017 | -0.0049 (71) |
| 10-15 | 418 | 0.2037 | 0.1911 | +0.0126 ± 0.0054 | 0.597 | 0.5606 | 0.4583 | 0.3347 | 0.3445 | -0.042 ± 0.0213 | 0.0016 (63) |
| 15-25 | 564 | 0.2347 | 0.2092 | +0.0255 ± 0.0075 | 0.6627 | 0.6048 | 0.5292 | 0.3362 | 0.367 | -0.033 ± 0.0192 | -0.0216 (58) |
| 25-40 | 273 | 0.2696 | 0.17 | +0.0996 ± 0.0156 | 0.7445 | 0.5104 | 0.5765 | 0.2652 | 0.2601 | -0.070 ± 0.0246 | -0.0216 (25) |
| 40+ | 93 | 0.4235 | 0.1616 | +0.2619 ± 0.0447 | 1.192 | 0.4964 | 0.7363 | 0.2277 | 0.2473 | -0.056 ± 0.0433 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 762 | 0.1943 | 0.1938 | +0.0005 ± 0.0005 | 0.567 | 0.5654 | 0.4956 | 0.4811 | 0.4698 | -0.052 ± 0.0159 | -0.0155 (82) |
| 3-5 | 537 | 0.1987 | 0.1969 | +0.0017 ± 0.0016 | 0.5777 | 0.5706 | 0.4707 | 0.4309 | 0.4302 | -0.046 ± 0.0192 | -0.018 (54) |
| 5-10 | 1144 | 0.1853 | 0.1785 | +0.0068 ± 0.0019 | 0.5532 | 0.5329 | 0.4434 | 0.3694 | 0.3645 | -0.046 ± 0.0126 | -0.0089 (121) |
| 10-15 | 843 | 0.1979 | 0.1834 | +0.0145 ± 0.0037 | 0.5823 | 0.5405 | 0.4506 | 0.327 | 0.3298 | -0.043 ± 0.0146 | -0.0053 (99) |
| 15-25 | 1177 | 0.2221 | 0.1875 | +0.0346 ± 0.005 | 0.6399 | 0.55 | 0.5035 | 0.3081 | 0.3169 | -0.043 ± 0.0127 | -0.0255 (106) |
| 25-40 | 810 | 0.2458 | 0.1299 | +0.1159 ± 0.008 | 0.6934 | 0.4055 | 0.53 | 0.2149 | 0.1901 | -0.071 ± 0.0125 | -0.0206 (47) |
| 40+ | 477 | 0.3894 | 0.0808 | +0.3086 ± 0.0142 | 1.0643 | 0.2703 | 0.6543 | 0.1382 | 0.109 | -0.073 ± 0.0133 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 816 | 1.134 ± 0.1 | 1.227 | 0.1723 | 0.1854 | 0.206 | 0.1926 |
| gen2 | 816 | 0.95 ± 0.088 | 1.166 | 0.1892 | 0.1845 | 0.2231 | 0.1932 |
| gen1_elo | 816 | 1.104 ± 0.098 | 1.215 | 0.1772 | 0.1858 | 0.2055 | 0.1927 |
| gen1_sr | 816 | 1.16 ± 0.115 | 1.213 | 0.145 | 0.1869 | 0.2197 | 0.1926 |
| gen1_ledger | 2688 | 0.884 ± 0.052 | 1.056 | 0.1628 | 0.2 | 0.2197 | 0.1918 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 4,553)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,479 | 32.5% |
| STALE_QUOTE | market_freshness | 1,371 | 30.1% |
| POOR_DATA | data | 367 | 8.1% |
| BOOK_QUALITY | execution | 302 | 6.6% |
| LIMITED_DATA | data | 283 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 271 | 5.9% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 226 | 5.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 161 | 3.5% |
| IDENTITY_AMBIGUOUS | mapping | 90 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 3 | 0.1% |

Cause class: coverage 32.5%, market_freshness 30.1%, data 14.3%, market_freshness/coverage 9.5%, execution 6.6%, model_calibration_or_unknown 5.0%, mapping 2.0%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 94.2%, LOW_DATA_QUALITY 64.8%, STALE_KALSHI_QUOTE 62.6%, STALE_PLAYER_DATA 55.2%, THIN_PLAYER_HISTORY 52.4%, MODEL_INTERNAL_DISAGREEMENT 32.9%, ASYMMETRIC_SAMPLE_SIZE 28.5%, WIDE_SPREAD 15.1%, MODEL_HIGH_UNCERTAINTY 12.7%, PLAYER_IDENTITY_RISK 11.1%, LEVEL_TRANSFER_RISK 8.7%, EVENT_MAPPING_RISK 6.9%, LOW_DISPLAYED_LIQUIDITY 4.7%, MODEL_CALIBRATION_OUTLIER 2.2%, UNKNOWN 0.8%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 35.1%, POST_SETTLEMENT_OBSERVATION 32.5%, POSSIBLE_IN_PLAY_QUOTE 6.8%, CONFIRMED_IN_PLAY_QUOTE 1.3%

### >= ge_25 pp (N = 2,491)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,146 | 46.0% |
| STALE_QUOTE | market_freshness | 610 | 24.5% |
| POOR_DATA | data | 161 | 6.5% |
| BOOK_QUALITY | execution | 147 | 5.9% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 138 | 5.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 96 | 3.9% |
| LIMITED_DATA | data | 78 | 3.1% |
| IDENTITY_AMBIGUOUS | mapping | 64 | 2.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 51 | 2.1% |

Cause class: coverage 46.0%, market_freshness 24.5%, data 9.6%, market_freshness/coverage 9.4%, execution 5.9%, mapping 2.6%, model_calibration_or_unknown 2.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 96.6%, STALE_KALSHI_QUOTE 69.6%, LOW_DATA_QUALITY 68.7%, THIN_PLAYER_HISTORY 54.9%, STALE_PLAYER_DATA 53.0%, MODEL_INTERNAL_DISAGREEMENT 33.6%, ASYMMETRIC_SAMPLE_SIZE 30.9%, MODEL_HIGH_UNCERTAINTY 14.0%, PLAYER_IDENTITY_RISK 13.8%, WIDE_SPREAD 13.8%, EVENT_MAPPING_RISK 8.6%, LEVEL_TRANSFER_RISK 8.2%, LOW_DISPLAYED_LIQUIDITY 5.2%, MODEL_CALIBRATION_OUTLIER 3.2%, UNKNOWN 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 48.9%, POST_SETTLEMENT_OBSERVATION 46.0%, POSSIBLE_IN_PLAY_QUOTE 6.5%, CONFIRMED_IN_PLAY_QUOTE 1.5%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 2115, "IDENTITY_AMBIGUOUS": 376}; ticker orientation: {"VERIFIED": 2491}.

Checks: discipline:AMBIGUOUS 181, discipline:PASS 2310, identity_confidence:AMBIGUOUS 344, identity_confidence:PASS 2147, level_mapping:NA 193, level_mapping:PASS 2298, market_pair:AMBIGUOUS 62, market_pair:NA 70, market_pair:PASS 2359, model_complement:NA 42, model_complement:PASS 2449, namesake:PASS 2491, physical_match_id:NA 1313, physical_match_id:PASS 1178, player_ids:PASS 2491, same_pair_other_event:PASS 2491, ticker_orientation:PASS 2491

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 306 | 3.9% | 4.1% | 0.5% | {"market_freshness": 12} | 6.04 | 0.181 / 0.1824 (47) | 39.5% | 0.0% | 0.7% | 3.6% |
| CHALLENGER | 1,591 | 18.5% | 8.2% | 11.8% | {"coverage": 155, "market_freshness": 70, "market_freshness/coverage": 37, "data": 17, "model_calibration_or_unknown": 12, "execution": 3} | 7.68 | 0.2246 / 0.207 (523) | 53.0% | 4.2% | 0.7% | 22.1% |
| DOUBLES | 371 | 48.8% | 48.7% | 7.3% | {"market_freshness": 106, "execution": 32, "mapping": 26, "market_freshness/coverage": 11, "coverage": 6} | 24.15 | 0.3289 / 0.2278 (156) | 60.9% | 0.0% | 100.0% | 9.2% |
| ITF_MEN | 3,467 | 24.8% | 14.0% | 34.4% | {"coverage": 456, "market_freshness": 164, "data": 86, "execution": 71, "market_freshness/coverage": 70, "mapping": 10, "model_calibration_or_unknown": 1} | 9.78 | 0.2131 / 0.1867 (1268) | 55.4% | 50.0% | 5.5% | 31.4% |
| ITF_WOMEN | 3,431 | 28.9% | 17.2% | 39.8% | {"coverage": 516, "market_freshness": 213, "data": 117, "market_freshness/coverage": 76, "execution": 32, "mapping": 26, "model_calibration_or_unknown": 12} | 12.23 | 0.2053 / 0.1854 (1126) | 58.4% | 54.4% | 6.4% | 32.4% |
| OTHER | 149 | 8.1% | 7.3% | 0.5% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 789 | 9.2% | 7.9% | 2.9% | {"market_freshness": 32, "model_calibration_or_unknown": 12, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.5 | 0.2006 / 0.1964 (129) | 40.4% | 2.7% | 1.5% | 3.8% |
| WTA125 | 421 | 16.4% | 9.1% | 2.8% | {"market_freshness/coverage": 30, "model_calibration_or_unknown": 12, "market_freshness": 11, "data": 8, "coverage": 8} | 10.39 | 0.2259 / 0.2023 (213) | 34.4% | 9.0% | 0.5% | 19.2% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 3 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 4 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 5 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 6 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 7 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 8 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 9 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 10 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 11 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 12 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 13 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 14 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 15 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 16 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 17 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 18 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 19 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 20 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 21 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 22 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 23 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 24 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 114 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 25 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 26 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 27 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 66 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 28 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 29 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 30 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 31 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 32 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 33 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.9h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 671 min (STALE); no external reference |
| 34 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 183 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 35 | `KXWTAMATCH-26OCT01YASCHW-CHW` | WTA | fair_v1 | 73% / 2% | +70 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 51 min (STALE); no external reference |
| 36 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 37 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 38 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 39 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |
| 40 | `KXITFWMATCH-26SEP30KOKUEM-KOK` | ITF_WOMEN | fair_v1 | 79% / 10% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 114 min (STALE); data LIMITED (grade C, thinner serve sample 824.0, ratio 2.35); no external reference |
| 41 | `KXITFMATCH-26SEP20WILRAH-RAH` | ITF_MEN | gen1_ledger | 72% / 4% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade B, thinner serve sample 2782.0, ratio 1.84); no external reference |
| 42 | `KXITFMATCH-26SEP26NAGTHO-NAG` | ITF_MEN | gen1_ledger | 76% / 7% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 89 min (STALE); data LIMITED (grade C, thinner serve sample 1323.0, ratio 4.45); no external reference |
| 43 | `KXITFWMATCH-26SEP26PERPRE-PER` | ITF_WOMEN | gen1_ledger | 78% / 10% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 102 min (STALE); data POOR (grade D, thinner serve sample 1020.0, ratio 2.77); no external reference |
| 44 | `KXITFMATCH-26SEP22YILAGA-AGA` | ITF_MEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 203 min (STALE); data LIMITED (grade B, thinner serve sample 2786.0, ratio 2.08); no external reference |
| 45 | `KXITFMATCH-26SEP30DIMURA-URA` | ITF_MEN | fair_v1 | 71% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.5h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 220 min (STALE); data POOR (grade F, thinner serve sample 174.0, ratio 2.63); no external reference |
| 46 | `KXITFWMATCH-26OCT01TANVED-TAN` | ITF_WOMEN | fair_v1 | 76% / 8% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 8.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 492 min (STALE); no external reference |
| 47 | `KXITFWMATCH-26SEP20LLIBON-BON` | ITF_WOMEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 69 min (STALE); data POOR (grade D, thinner serve sample 1210.0, ratio 3.0); no external reference |
| 48 | `KXATPCHALLENGERDOUBLES-26SEP17ARESTEBLASCH-BLASCH` | DOUBLES | gen1_ledger | 95% / 28% | +67 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 79 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 49 | `KXITFWMATCH-26SEP24BOUKUR-BOU` | ITF_WOMEN | gen1_ledger | 76% / 8% | +67 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 113 min (STALE); data POOR (grade D, thinner serve sample 1497.0, ratio 2.48); no external reference |
| 50 | `KXATPCHALLENGERMATCH-26SEP28TABSAN-SAN` | CHALLENGER | gen1_ledger | 70% / 4% | +67 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 48 min (STALE); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9658, "by_level_share_of_ge_25pp": {"ATP": 0.0048, "CHALLENGER": 0.118, "DOUBLES": 0.0727, "ITF_MEN": 0.3444, "ITF_WOMEN": 0.3982, "OTHER": 0.0048, "WTA": 0.0293, "WTA125": 0.0277}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.6957, "share_primary_cause_market_settled_or_in_play": 0.554, "share_primary_cause_stale_quote_only": 0.2449}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 2491, "identity_ambiguous_share": 0.1509, "ticker_orientation": {"VERIFIED": 2491}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 1178, "with_external": 6, "coverage": 0.0051, "external_status": {"EXTERNAL_STALE": 6}, "triangulation": {"INSUFFICIENT_INPUTS": 6}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 470, "with_external": 6, "coverage": 0.0128, "external_status": {"EXTERNAL_STALE": 6}, "triangulation": {"INSUFFICIENT_INPUTS": 6}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 783.0, "median_sample_ratio": 2.31, "median_min_matches": 24.5, "median_max_days_since_last": 173.0, "share_severe_asymmetry": 0.1678, "data_status": {"POOR": 1171, "LIMITED": 853, "ADEQUATE": 467}, "comparison_lt_10pp": {"median_thinner_serve_points": 1970.0, "median_sample_ratio": 1.7, "median_min_matches": 78.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 185, "model_minus_observed": 0.1088, "kalshi_minus_observed": -0.0225, "brier_diff_model_minus_kalshi": 0.0175}, "4-10x": {"n": 133, "model_minus_observed": 0.0934, "kalshi_minus_observed": -0.04, "brier_diff_model_minus_kalshi": 0.0103}, "<2x": {"n": 366, "model_minus_observed": 0.0717, "kalshi_minus_observed": -0.0488, "brier_diff_model_minus_kalshi": 0.0099}, ">=10x": {"n": 132, "model_minus_observed": 0.1024, "kalshi_minus_observed": -0.061, "brier_diff_model_minus_kalshi": 0.0204}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 816, "model": {"intercept": -0.64, "slope": 0.95, "slope_se": 0.088}, "kalshi_mid_same_rows": {"intercept": 0.205, "slope": 1.166, "slope_se": 0.097}, "mean_extremity_model": 0.1892, "mean_extremity_kalshi": 0.1845, "model_brier": 0.2231, "kalshi_brier": 0.1932, "brier_diff_model_minus_kalshi": 0.03, "brier_diff_se": 0.0066, "model_logloss": 0.6383, "kalshi_logloss": 0.5648}, "fair_v1": {"n": 816, "model": {"intercept": -0.451, "slope": 1.134, "slope_se": 0.1}, "kalshi_mid_same_rows": {"intercept": 0.308, "slope": 1.227, "slope_se": 0.101}, "mean_extremity_model": 0.1723, "mean_extremity_kalshi": 0.1854, "model_brier": 0.206, "kalshi_brier": 0.1926, "brier_diff_model_minus_kalshi": 0.0134, "brier_diff_se": 0.0052, "model_logloss": 0.5967, "kalshi_logloss": 0.5634}, "gen1_elo": {"n": 816, "model": {"intercept": -0.423, "slope": 1.104, "slope_se": 0.098}, "kalshi_mid_same_rows": {"intercept": 0.319, "slope": 1.215, "slope_se": 0.099}, "mean_extremity_model": 0.1772, "mean_extremity_kalshi": 0.1858, "model_brier": 0.2055, "kalshi_brier": 0.1927, "brier_diff_model_minus_kalshi": 0.0127, "brier_diff_se": 0.0052, "model_logloss": 0.5973, "kalshi_logloss": 0.5635}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2554, "share_ge_15": 0.4414, "median_abs_gap": 12.92, "n": 4613}, "gen1_elo": {"share_ge_25": 0.2478, "share_ge_15": 0.4292, "median_abs_gap": 12.45, "n": 4613}, "gen1_sr": {"share_ge_25": 0.3074, "share_ge_15": 0.5305, "median_abs_gap": 16.17, "n": 4613}, "gen2": {"share_ge_25": 0.3067, "share_ge_15": 0.5034, "median_abs_gap": 15.19, "n": 4613}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1401, "share_ge_15": 0.3303, "median_abs_gap": 9.95, "n": 3355}, "gen1_elo": {"share_ge_25": 0.1389, "share_ge_15": 0.3127, "median_abs_gap": 9.51, "n": 3355}, "gen1_sr": {"share_ge_25": 0.1964, "share_ge_15": 0.4352, "median_abs_gap": 12.7, "n": 3355}, "gen2": {"share_ge_25": 0.2098, "share_ge_15": 0.4218, "median_abs_gap": 12.77, "n": 3355}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 6.04, "share_ge_25_all": 0.0392, "share_ge_25_pregame_clean": 0.0407}, "WTA": {"median_abs_gap_pregame_clean": 8.5, "share_ge_25_all": 0.0925, "share_ge_25_pregame_clean": 0.0791}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2247, "share_within_10pp_all": 0.42, "share_within_10pp_pregame_clean": 0.4996, "corr_model_vs_mid_pregame_clean": 0.8291}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 135, "model_brier": 0.1754, "kalshi_brier": 0.1763, "brier_diff_model_minus_kalshi": -0.0008}, "10-15": {"n_settled": 139, "model_brier": 0.2155, "kalshi_brier": 0.2086, "brier_diff_model_minus_kalshi": 0.0069}, "15-25": {"n_settled": 176, "model_brier": 0.2126, "kalshi_brier": 0.2112, "brier_diff_model_minus_kalshi": 0.0014}, "25-40": {"n_settled": 87, "model_brier": 0.242, "kalshi_brier": 0.1797, "brier_diff_model_minus_kalshi": 0.0623}, "3-5": {"n_settled": 83, "model_brier": 0.1682, "kalshi_brier": 0.1652, "brier_diff_model_minus_kalshi": 0.0031}, "40+": {"n_settled": 23, "model_brier": 0.3363, "kalshi_brier": 0.1395, "brier_diff_model_minus_kalshi": 0.1968}, "5-10": {"n_settled": 173, "model_brier": 0.198, "kalshi_brier": 0.2002, "brier_diff_model_minus_kalshi": -0.0022}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.574, "slope": 0.884, "slope_se": 0.052}, "kalshi_slope": {"intercept": 0.076, "slope": 1.056, "slope_se": 0.053}, "n": 2688}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 156, "model_brier": 0.3289, "kalshi_brier": 0.2278, "brier_diff_model_minus_kalshi": 0.101, "brier_diff_se": 0.0265, "corr_model_outcome": -0.0853, "corr_kalshi_outcome": 0.3248}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
