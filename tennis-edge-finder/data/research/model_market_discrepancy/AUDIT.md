# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-03T02:18Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 10,812): 0-3 13.4%, 3-5 8.9%, 5-10 19.4%, 10-15 14.8%, 15-25 19.6%, 25-40 14.4%, 40+ 9.6%; median gap 12.59 pp.
* **Where the extremes live**: 96.6% of >=25 pp gaps are off the ATP/WTA main tour (ITF 74.4%, Challenger 12.1%, doubles 7.0%). Main tour: ATP 3.8% and WTA 9.4% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 2,587): MARKET_ALREADY_SETTLED_WHEN_PRICED 47.2%, STALE_QUOTE 23.9%, POOR_DATA 6.3%, BOOK_QUALITY 5.7%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IN_PLAY_QUOTE 3.9%, LIMITED_DATA 3.0%, IDENTITY_AMBIGUOUS 2.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%. By class: coverage 47.2%, market_freshness 23.9%, data 9.3%, market_freshness/coverage 9.3%, execution 5.7%, mapping 2.5%, model_calibration_or_unknown 2.0%.
* **Stale / settled / in-play**: 70.3% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 56.6% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 2,587 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 14.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 0.5%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 7.5% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 824.0 points vs 1969.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.112, Gen-2 0.941, Gen-1 ledger 0.883 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 89 model 0.2374 vs Kalshi 0.1802; n 25 model 0.3417 vs Kalshi 0.1463.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|CHALLENGER. Not implemented here.

## 1. Observations

* 34,645 model-market comparisons (59,732 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 16,390 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-02T13:30:06.576336+00:00'], shadow board 9,669 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-03T02:14:22.919064+00:00'], Model 4 2,926 rows, 8,186 settled tickers, 1,791 tickers with an external scan.
* By model: {"gen1_ledger": 9552, "gen1_elo": 4865, "fair_v1": 4865, "gen2": 4865, "gen1_sr": 4865, "model4_fundamental": 2821, "model4_conditioned": 2812}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 10,812 | 13.4 | 8.9 | 19.4 | 14.8 | 19.6 | 14.4 | 9.6 | 12.59 | 43.5% | 23.9% |
| MW fair_v1 | 4,865 | 13.6 | 8.4 | 18.6 | 14.9 | 18.6 | 15.0 | 11.0 | 13.02 | 44.5% | 25.9% |
| MW gen1_elo | 4,865 | 12.9 | 8.8 | 19.9 | 15.0 | 18.1 | 14.9 | 10.3 | 12.51 | 43.4% | 25.2% |
| MW gen1_ledger | 5,947 | 13.3 | 9.3 | 20.1 | 14.7 | 20.4 | 13.9 | 8.4 | 12.23 | 42.6% | 22.3% |
| MW gen1_sr | 4,865 | 9.7 | 7.0 | 16.7 | 13.2 | 22.4 | 18.5 | 12.5 | 16.43 | 53.4% | 31.0% |
| MW gen2 | 4,865 | 11.3 | 6.3 | 16.5 | 15.1 | 19.9 | 17.2 | 13.7 | 15.43 | 50.9% | 31.0% |
| all families model4_conditioned | 2,812 | 18.6 | 15.5 | 29.6 | 23.8 | 8.2 | 2.4 | 1.9 | 7.37 | 12.5% | 4.3% |
| all families model4_fundamental | 2,821 | 14.5 | 10.7 | 30.0 | 21.8 | 14.6 | 5.5 | 3.0 | 9.09 | 23.0% | 8.4% |

Configurable thresholds (primary): >=5pp 77.7%, >=10pp 58.3%, >=15pp 43.5%, >=20pp 32.9%, >=25pp 23.9%, >=30pp 17.6%, >=40pp 9.6%, >=50pp 4.3%
Executable gap (model outside the book, before fees): median 10.23pp; >=10pp 50.6%, >=25pp 21.2%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 241 | 22.4 | 17.4 | 27.4 | 12.9 | 14.9 | 1.2 | 3.7 | 6.16 | 19.9% | 5.0% |
| CHALLENGER | 840 | 15.0 | 9.1 | 15.8 | 16.1 | 15.5 | 15.2 | 13.3 | 13.29 | 44.0% | 28.6% |
| ITF_MEN | 1,571 | 12.0 | 8.3 | 19.5 | 14.8 | 17.8 | 15.0 | 12.7 | 13.06 | 45.4% | 27.6% |
| ITF_WOMEN | 1,694 | 10.6 | 6.4 | 16.0 | 14.9 | 21.4 | 18.9 | 11.7 | 15.78 | 52.0% | 30.6% |
| WTA | 435 | 23.0 | 10.6 | 25.8 | 12.6 | 18.9 | 6.7 | 2.5 | 8.16 | 28.1% | 9.2% |
| WTA125 | 84 | 14.3 | 4.8 | 17.9 | 23.8 | 20.2 | 14.3 | 4.8 | 12.4 | 39.3% | 19.1% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 241 | 23.2 | 12.9 | 24.9 | 16.2 | 17.0 | 1.7 | 4.2 | 7.08 | 22.8% | 5.8% |
| CHALLENGER | 840 | 10.9 | 5.2 | 17.6 | 16.7 | 18.3 | 18.3 | 12.9 | 14.92 | 49.5% | 31.2% |
| ITF_MEN | 1,571 | 9.7 | 6.1 | 17.2 | 15.8 | 20.4 | 16.6 | 14.2 | 15.45 | 51.1% | 30.7% |
| ITF_WOMEN | 1,694 | 9.0 | 6.3 | 14.1 | 12.9 | 19.9 | 19.8 | 17.9 | 18.3 | 57.7% | 37.7% |
| WTA | 435 | 20.5 | 5.5 | 16.8 | 15.6 | 22.3 | 16.8 | 2.5 | 12.98 | 41.6% | 19.3% |
| WTA125 | 84 | 6.0 | 6.0 | 16.7 | 20.2 | 22.6 | 15.5 | 13.1 | 15.56 | 51.2% | 28.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 241 | 28.2 | 12.9 | 28.6 | 10.8 | 9.1 | 6.6 | 3.7 | 6.53 | 19.5% | 10.4% |
| CHALLENGER | 840 | 14.9 | 8.1 | 20.8 | 14.2 | 13.7 | 14.2 | 14.2 | 11.99 | 42.0% | 28.3% |
| ITF_MEN | 1,571 | 10.1 | 9.6 | 18.7 | 15.8 | 18.0 | 15.7 | 12.0 | 13.09 | 45.8% | 27.8% |
| ITF_WOMEN | 1,694 | 9.4 | 6.7 | 16.7 | 14.4 | 23.7 | 18.5 | 10.5 | 16.54 | 52.7% | 29.0% |
| WTA | 435 | 23.4 | 14.0 | 29.4 | 15.6 | 11.5 | 4.4 | 1.6 | 6.99 | 17.5% | 6.0% |
| WTA125 | 84 | 16.7 | 6.0 | 22.6 | 29.8 | 13.1 | 10.7 | 1.2 | 10.92 | 25.0% | 11.9% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 72 | 23.6 | 22.2 | 34.7 | 12.5 | 6.9 | 0.0 | 0.0 | 6.26 | 6.9% | 0.0% |
| CHALLENGER | 794 | 21.4 | 13.6 | 26.6 | 15.9 | 13.5 | 6.4 | 2.6 | 7.45 | 22.5% | 9.1% |
| DOUBLES | 373 | 5.4 | 3.8 | 9.7 | 10.5 | 22.0 | 20.9 | 27.9 | 24.15 | 70.8% | 48.8% |
| ITF_MEN | 2,013 | 14.4 | 8.9 | 19.0 | 13.7 | 21.0 | 13.7 | 9.4 | 12.51 | 44.0% | 23.1% |
| ITF_WOMEN | 1,846 | 8.9 | 8.3 | 17.5 | 14.2 | 23.5 | 18.5 | 9.0 | 15.32 | 51.0% | 27.5% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 363 | 15.4 | 9.4 | 25.6 | 22.3 | 17.6 | 8.8 | 0.8 | 9.8 | 27.3% | 9.6% |
| WTA125 | 337 | 13.3 | 9.5 | 21.7 | 16.9 | 22.9 | 11.9 | 3.9 | 11.35 | 38.6% | 15.7% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 240 | 22.1 | 17.5 | 27.5 | 12.9 | 15.0 | 1.2 | 3.8 | 6.19 | 20.0% | 5.0% |
| CHALLENGER | 614 | 19.1 | 11.2 | 19.4 | 19.2 | 16.6 | 9.3 | 5.2 | 10.18 | 31.1% | 14.5% |
| ITF_MEN | 987 | 15.9 | 11.7 | 24.8 | 16.3 | 17.5 | 9.8 | 4.0 | 9.53 | 31.3% | 13.8% |
| ITF_WOMEN | 1,126 | 14.6 | 8.5 | 19.4 | 17.5 | 22.5 | 13.1 | 4.4 | 12.45 | 40.0% | 17.5% |
| WTA | 434 | 23.0 | 10.6 | 25.8 | 12.7 | 18.9 | 6.5 | 2.5 | 8.16 | 27.9% | 9.0% |
| WTA125 | 81 | 14.8 | 4.9 | 18.5 | 24.7 | 19.8 | 12.3 | 4.9 | 11.65 | 37.0% | 17.3% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 240 | 23.3 | 12.5 | 25.0 | 16.2 | 17.1 | 1.7 | 4.2 | 7.29 | 22.9% | 5.8% |
| CHALLENGER | 614 | 13.7 | 6.7 | 22.3 | 20.4 | 19.7 | 13.0 | 4.2 | 11.87 | 37.0% | 17.3% |
| ITF_MEN | 987 | 13.1 | 7.7 | 21.2 | 18.3 | 21.3 | 13.0 | 5.5 | 12.05 | 39.7% | 18.4% |
| ITF_WOMEN | 1,126 | 11.1 | 8.3 | 16.2 | 12.8 | 23.1 | 17.1 | 11.4 | 15.57 | 51.6% | 28.5% |
| WTA | 434 | 20.5 | 5.5 | 16.8 | 15.7 | 22.4 | 16.6 | 2.5 | 12.96 | 41.5% | 19.1% |
| WTA125 | 81 | 6.2 | 6.2 | 16.1 | 21.0 | 23.5 | 16.1 | 11.1 | 15.33 | 50.6% | 27.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 62 | 24.2 | 25.8 | 35.5 | 12.9 | 1.6 | 0.0 | 0.0 | 5.45 | 1.6% | 0.0% |
| CHALLENGER | 647 | 24.0 | 15.9 | 29.4 | 15.5 | 12.7 | 2.5 | 0.1 | 6.68 | 15.3% | 2.6% |
| DOUBLES | 337 | 5.6 | 3.6 | 9.8 | 10.4 | 22.0 | 21.1 | 27.6 | 24.15 | 70.6% | 48.7% |
| ITF_MEN | 1,427 | 17.5 | 10.8 | 22.2 | 14.8 | 20.9 | 10.2 | 3.6 | 9.9 | 34.7% | 13.7% |
| ITF_WOMEN | 1,242 | 11.0 | 9.8 | 21.3 | 16.5 | 24.4 | 14.8 | 2.1 | 12.07 | 41.3% | 16.9% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 334 | 15.6 | 9.9 | 26.4 | 23.1 | 18.3 | 6.9 | 0.0 | 9.55 | 25.1% | 6.9% |
| WTA125 | 259 | 15.8 | 10.4 | 25.9 | 20.1 | 21.2 | 6.2 | 0.4 | 9.54 | 27.8% | 6.6% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 373 | 5.4 | 3.8 | 9.7 | 10.5 | 22.0 | 20.9 | 27.9 | 24.15 | 70.8% | 48.8% |
| singles | 5,574 | 13.8 | 9.7 | 20.8 | 14.9 | 20.2 | 13.4 | 7.1 | 11.79 | 40.8% | 20.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 1,058 | 15.6 | 8.2 | 18.7 | 14.6 | 16.0 | 14.3 | 12.7 | 12.56 | 42.9% | 26.9% |
| Hard | 3,485 | 13.0 | 8.7 | 18.9 | 14.6 | 19.3 | 15.1 | 10.4 | 13.14 | 44.9% | 25.6% |
| UNKNOWN | 322 | 13.7 | 5.6 | 15.2 | 19.2 | 19.9 | 15.5 | 10.9 | 13.77 | 46.3% | 26.4% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,519 | 17.6 | 10.1 | 20.7 | 14.8 | 17.2 | 11.1 | 8.6 | 10.39 | 36.9% | 19.7% |
| B | 685 | 17.5 | 10.7 | 17.5 | 16.8 | 15.2 | 10.2 | 12.1 | 11.17 | 37.5% | 22.3% |
| C | 810 | 12.2 | 8.2 | 22.4 | 13.6 | 16.9 | 15.8 | 11.0 | 12.91 | 43.7% | 26.8% |
| D | 905 | 11.4 | 7.8 | 17.7 | 14.0 | 20.9 | 15.8 | 12.4 | 14.53 | 49.1% | 28.2% |
| F | 946 | 7.5 | 4.7 | 13.6 | 15.9 | 22.7 | 23.0 | 12.6 | 18.69 | 58.4% | 35.6% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,828 | 18.9 | 11.8 | 26.2 | 16.7 | 16.4 | 7.0 | 3.0 | 8.66 | 26.4% | 10.0% |
| B | 985 | 13.8 | 9.3 | 21.4 | 16.2 | 19.3 | 12.6 | 7.3 | 11.64 | 39.2% | 19.9% |
| C | 1,227 | 11.2 | 8.2 | 15.7 | 13.8 | 22.2 | 15.6 | 13.2 | 15.42 | 51.0% | 28.8% |
| D | 915 | 11.3 | 8.2 | 20.8 | 11.9 | 23.6 | 15.4 | 8.8 | 14.12 | 47.9% | 24.3% |
| F | 992 | 6.8 | 7.2 | 12.4 | 12.9 | 23.3 | 24.3 | 13.2 | 19.19 | 60.8% | 37.5% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 1,885 | 17.0 | 9.6 | 19.8 | 15.8 | 16.6 | 11.2 | 10.1 | 10.92 | 37.8% | 21.3% |
| LIMITED | 1,111 | 14.7 | 10.1 | 21.6 | 13.3 | 16.4 | 13.9 | 10.1 | 11.76 | 40.3% | 23.9% |
| POOR | 1,869 | 9.5 | 6.2 | 15.5 | 15.0 | 22.0 | 19.4 | 12.4 | 16.64 | 53.8% | 31.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 341 | 34.3 | 22.9 | 33.1 | 6.5 | 2.4 | 0.9 | 0.0 | 4.16 | 3.2% | 0.9% |
| GAME_SPREAD | 406 | 19.9 | 16.5 | 37.0 | 16.0 | 8.9 | 1.2 | 0.5 | 6.59 | 10.6% | 1.7% |
| MATCH_WINNER | 5,947 | 13.3 | 9.3 | 20.1 | 14.7 | 20.4 | 13.9 | 8.4 | 12.23 | 42.6% | 22.3% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 1,702 | 21.7 | 13.4 | 30.6 | 17.2 | 13.6 | 2.8 | 0.7 | 7.04 | 17.0% | 3.4% |
| TOTAL_GAMES | 1,132 | 9.9 | 9.4 | 26.5 | 24.9 | 17.0 | 8.0 | 4.4 | 10.66 | 29.3% | 12.4% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 883 | 28.8 | 32.7 | 26.9 | 0.7 | 8.7 | 1.7 | 0.5 | 4.27 | 10.9% | 2.1% |
| GAME_SPREAD | 565 | 36.6 | 15.0 | 25.3 | 17.9 | 2.5 | 1.9 | 0.7 | 4.55 | 5.1% | 2.6% |
| TOTAL_GAMES | 1,364 | 4.5 | 4.5 | 33.1 | 41.3 | 10.3 | 3.1 | 3.2 | 10.72 | 16.6% | 6.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 883 | 26.2 | 16.8 | 33.8 | 8.2 | 9.8 | 4.3 | 1.0 | 5.79 | 15.2% | 5.3% |
| GAME_SPREAD | 565 | 17.5 | 10.3 | 25.5 | 23.2 | 15.9 | 5.1 | 2.5 | 9.56 | 23.5% | 7.6% |
| TOTAL_GAMES | 1,373 | 5.8 | 7.0 | 29.4 | 29.9 | 17.0 | 6.3 | 4.4 | 10.91 | 27.8% | 10.8% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4,865 | 44.5% | 25.9% | 13.02 | 33.0% | 14.0% | 9.98 |
| gen1_elo | 4,865 | 43.4% | 25.2% | 12.51 | 31.2% | 14.0% | 9.51 |
| gen1_sr | 4,865 | 53.4% | 31.0% | 16.43 | 43.5% | 19.6% | 12.69 |
| gen2 | 4,865 | 50.9% | 31.0% | 15.43 | 42.4% | 20.9% | 12.77 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 1,809 | 18.0 | 12.2 | 23.4 | 15.4 | 18.4 | 9.7 | 3.1 | 9.14 | 31.1% | 12.8% |
| STALE | 3,056 | 11.0 | 6.1 | 15.7 | 14.7 | 18.8 | 18.1 | 15.6 | 16.44 | 52.5% | 33.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,201 | 15.3 | 10.2 | 22.0 | 15.9 | 19.8 | 12.2 | 4.6 | 10.71 | 36.6% | 16.8% |
| STALE | 2,746 | 11.0 | 8.2 | 17.9 | 13.2 | 21.0 | 15.9 | 12.9 | 14.82 | 49.7% | 28.7% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 10,812 | 0 | 5010 | 5802 | 31.3 | 217.5 | 1400.4 |
| ge_15pp | 4,703 | 0 | 1734 | 2969 | 39.8 | 518.9 | 1380.4 |
| ge_25pp | 2,587 | 0 | 768 | 1819 | 54.4 | 637.8 | 1380.4 |
| lt_10pp | 4,512 | 0 | 2489 | 2023 | 28.8 | 55.0 | 1201.9 |

Current slate `SL-20261003T021827Z-7f3afd1f`: 254 priced rows, quote age at build {'median': 38.4, 'max': 38.4}, freshness {'STALE': 254}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 138 | 21.0 | 10.9 | 21.0 | 23.2 | 19.6 | 4.3 | 0.0 | 8.04 | 23.9% | 4.3% |
| MARKETS_AGREE | 8 | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.96 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 12 | 0.0 | 0.0 | 8.3 | 50.0 | 41.7 | 0.0 | 0.0 | 14.32 | 41.7% | 0.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 4,865 | 159 (3.3%) | 7.5% | 0.0% | {"EXTERNAL_STALE": 138, "AGREES_WITH_KALSHI": 12, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 2,167 | 38 (1.8%) | 13.2% | 0.0% | {"EXTERNAL_STALE": 33, "AGREES_WITH_KALSHI": 5} |
| fair_v1_ge_25pp | 1,261 | 6 (0.5%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 6} |
| fair_v1_ge_25pp_pregame_clean | 487 | 6 (1.2%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 6} |
| fair_v1_lt_10pp | 1,972 | 83 (4.2%) | 1.2% | 0.0% | {"EXTERNAL_STALE": 73, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1, "AGREES_WITH_KALSHI": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 956 | 12.1 | 7.1 | 18.5 | 15.5 | 19.8 | 16.5 | 10.5 | 13.75 | 46.8% | 27.0% |
| 4-10x | 652 | 12.3 | 9.1 | 18.6 | 14.4 | 18.2 | 16.3 | 11.2 | 13.62 | 45.7% | 27.5% |
| <2x | 2,683 | 15.1 | 9.2 | 19.2 | 14.8 | 18.0 | 12.9 | 10.7 | 12.09 | 41.7% | 23.7% |
| >=10x | 574 | 10.4 | 5.8 | 15.8 | 15.2 | 19.9 | 20.4 | 12.5 | 16.24 | 52.8% | 32.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 1,294 | 14.6 | 8.6 | 20.9 | 15.2 | 16.9 | 12.0 | 11.8 | 11.95 | 40.7% | 23.8% |
| 300-1000 | 1,192 | 13.1 | 7.5 | 16.6 | 15.8 | 20.0 | 16.7 | 10.3 | 14.1 | 47.0% | 27.0% |
| <300 | 1,146 | 8.5 | 5.9 | 15.3 | 13.7 | 21.6 | 21.5 | 13.6 | 18.33 | 56.6% | 35.1% |
| >=3000 | 1,233 | 17.8 | 11.2 | 21.1 | 15.0 | 16.4 | 10.4 | 8.2 | 9.98 | 35.0% | 18.6% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 192 | 0.5149 | 0.383 | 0.4115 | +0.103 | -0.029 | 0.0142 ± 0.0105 |
| ratio 4-10x | 136 | 0.5831 | 0.449 | 0.4853 | +0.098 | -0.036 | 0.0087 ± 0.0123 |
| ratio <2x | 386 | 0.5342 | 0.4149 | 0.4585 | +0.076 | -0.044 | 0.0114 ± 0.007 |
| ratio >=10x | 134 | 0.5538 | 0.3918 | 0.4627 | +0.091 | -0.071 | 0.0186 ± 0.0158 |
| thinner_sample 1000-3000 | 224 | 0.5388 | 0.4188 | 0.4509 | +0.088 | -0.032 | 0.0086 ± 0.0093 |
| thinner_sample 300-1000 | 244 | 0.5542 | 0.427 | 0.4631 | +0.091 | -0.036 | 0.0069 ± 0.0091 |
| thinner_sample <300 | 269 | 0.5394 | 0.38 | 0.4498 | +0.090 | -0.070 | 0.0209 ± 0.0106 |
| thinner_sample >=3000 | 111 | 0.5185 | 0.4236 | 0.4414 | +0.077 | -0.018 | 0.0145 ± 0.0105 |
| data_status ADEQUATE | 239 | 0.5248 | 0.4164 | 0.4435 | +0.081 | -0.027 | 0.0076 ± 0.008 |
| data_status LIMITED | 187 | 0.5591 | 0.4379 | 0.4973 | +0.062 | -0.059 | 0.0031 ± 0.0108 |
| data_status POOR | 422 | 0.5417 | 0.393 | 0.4384 | +0.103 | -0.045 | 0.0199 ± 0.0078 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 144 | 0.1771 | 0.1778 | -0.0006 ± 0.0012 | 0.5272 | 0.529 | 0.4947 | 0.4801 | 0.4931 | -0.094 ± 0.0383 | -0.01 (3) |
| 3-5 | 86 | 0.1747 | 0.1713 | +0.0034 ± 0.0037 | 0.5299 | 0.5174 | 0.5171 | 0.476 | 0.4535 | -0.118 ± 0.0475 | 0.02 (1) |
| 5-10 | 179 | 0.2002 | 0.2022 | -0.0020 ± 0.0051 | 0.586 | 0.5899 | 0.5186 | 0.4439 | 0.4916 | -0.056 ± 0.034 | -0.0167 (3) |
| 10-15 | 145 | 0.2162 | 0.2103 | +0.0059 ± 0.0095 | 0.6156 | 0.603 | 0.526 | 0.4021 | 0.4414 | -0.070 ± 0.0375 | -0.0633 (3) |
| 15-25 | 180 | 0.2119 | 0.2111 | +0.0008 ± 0.0133 | 0.6114 | 0.6027 | 0.5615 | 0.3651 | 0.4611 | -0.021 ± 0.0333 | -0.02 (4) |
| 25-40 | 89 | 0.2374 | 0.1802 | +0.0572 ± 0.0278 | 0.6642 | 0.5319 | 0.6153 | 0.3019 | 0.3596 | -0.083 ± 0.0424 | -0.01 (1) |
| 40+ | 25 | 0.3417 | 0.1463 | +0.1954 ± 0.0695 | 0.93 | 0.4542 | 0.7178 | 0.2734 | 0.28 | -0.168 ± 0.0779 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 436 | 0.1663 | 0.1672 | -0.0010 ± 0.0007 | 0.4989 | 0.5013 | 0.5063 | 0.4915 | 0.5275 | -0.027 ± 0.0206 | -0.0188 (8) |
| 3-5 | 261 | 0.1742 | 0.172 | +0.0023 ± 0.0021 | 0.529 | 0.517 | 0.4955 | 0.4552 | 0.4483 | -0.067 ± 0.0264 | 0.02 (1) |
| 5-10 | 607 | 0.1841 | 0.1823 | +0.0018 ± 0.0026 | 0.548 | 0.5401 | 0.4744 | 0.4006 | 0.4283 | -0.032 ± 0.0175 | -0.0129 (7) |
| 10-15 | 499 | 0.196 | 0.1795 | +0.0165 ± 0.0047 | 0.5741 | 0.5238 | 0.4781 | 0.3544 | 0.3487 | -0.069 ± 0.0188 | -0.0633 (3) |
| 15-25 | 669 | 0.1906 | 0.1575 | +0.0331 ± 0.0061 | 0.5689 | 0.4666 | 0.4784 | 0.2808 | 0.293 | -0.046 ± 0.0151 | -0.017 (10) |
| 25-40 | 609 | 0.214 | 0.0955 | +0.1185 ± 0.0078 | 0.6211 | 0.3125 | 0.5027 | 0.1884 | 0.1593 | -0.077 ± 0.0122 | -0.01 (1) |
| 40+ | 448 | 0.3697 | 0.0354 | +0.3343 ± 0.0097 | 0.9645 | 0.151 | 0.6168 | 0.1034 | 0.0446 | -0.090 ± 0.0083 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 87 | 0.1797 | 0.1813 | -0.0016 ± 0.0016 | 0.5329 | 0.5352 | 0.5301 | 0.5155 | 0.5747 | -0.033 ± 0.0444 | -0.01 (1) |
| 3-5 | 67 | 0.2138 | 0.2119 | +0.0019 ± 0.0045 | 0.609 | 0.6116 | 0.4989 | 0.4598 | 0.4478 | -0.085 ± 0.0591 | 0.02 (1) |
| 5-10 | 165 | 0.1861 | 0.1789 | +0.0071 ± 0.005 | 0.5538 | 0.5349 | 0.572 | 0.4961 | 0.4788 | -0.124 ± 0.0332 | -0.01 (4) |
| 10-15 | 153 | 0.2221 | 0.209 | +0.0131 ± 0.0094 | 0.6331 | 0.6039 | 0.5776 | 0.453 | 0.4706 | -0.083 ± 0.0379 | -0.0667 (3) |
| 15-25 | 200 | 0.2204 | 0.1969 | +0.0235 ± 0.0124 | 0.6257 | 0.5685 | 0.5823 | 0.3856 | 0.43 | -0.081 ± 0.032 | -0.0167 (3) |
| 25-40 | 122 | 0.252 | 0.1939 | +0.0580 ± 0.0246 | 0.705 | 0.5627 | 0.6566 | 0.3471 | 0.4016 | -0.097 ± 0.0408 | -0.025 (2) |
| 40+ | 54 | 0.3802 | 0.1959 | +0.1843 ± 0.0606 | 1.0546 | 0.5767 | 0.7524 | 0.2608 | 0.3333 | -0.055 ± 0.0597 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 345 | 0.1609 | 0.1628 | -0.0019 ± 0.0007 | 0.4832 | 0.4883 | 0.554 | 0.5394 | 0.5913 | -0.000 ± 0.0219 | -0.0217 (6) |
| 3-5 | 212 | 0.1801 | 0.1776 | +0.0025 ± 0.0023 | 0.5305 | 0.5302 | 0.553 | 0.5137 | 0.5 | -0.063 ± 0.0291 | 0.02 (1) |
| 5-10 | 544 | 0.1772 | 0.174 | +0.0033 ± 0.0027 | 0.5302 | 0.5161 | 0.5179 | 0.4425 | 0.4559 | -0.045 ± 0.018 | -0.01 (5) |
| 10-15 | 519 | 0.1895 | 0.1746 | +0.0149 ± 0.0046 | 0.5628 | 0.5155 | 0.5145 | 0.3904 | 0.4008 | -0.048 ± 0.0185 | -0.0575 (4) |
| 15-25 | 687 | 0.2051 | 0.1567 | +0.0484 ± 0.006 | 0.5987 | 0.4691 | 0.5115 | 0.3156 | 0.2955 | -0.088 ± 0.015 | -0.0143 (7) |
| 25-40 | 656 | 0.2216 | 0.1177 | +0.1039 ± 0.0085 | 0.6455 | 0.3641 | 0.5425 | 0.2275 | 0.221 | -0.063 ± 0.0136 | -0.015 (6) |
| 40+ | 566 | 0.4042 | 0.0614 | +0.3429 ± 0.0121 | 1.0619 | 0.222 | 0.6624 | 0.1245 | 0.0883 | -0.070 ± 0.01 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 132 | 0.1796 | 0.1811 | -0.0015 ± 0.0013 | 0.5297 | 0.5338 | 0.5177 | 0.5033 | 0.5379 | -0.052 ± 0.0374 | -0.01 (5) |
| 3-5 | 97 | 0.1704 | 0.168 | +0.0024 ± 0.0034 | 0.5137 | 0.508 | 0.501 | 0.4616 | 0.4536 | -0.112 ± 0.0443 | -- (0) |
| 5-10 | 172 | 0.2054 | 0.2055 | -0.0001 ± 0.0051 | 0.6018 | 0.5957 | 0.5066 | 0.434 | 0.4709 | -0.059 ± 0.0349 | -0.01 (3) |
| 10-15 | 153 | 0.2111 | 0.2077 | +0.0034 ± 0.0092 | 0.6083 | 0.5972 | 0.5511 | 0.4273 | 0.4837 | -0.065 ± 0.0371 | -0.044 (5) |
| 15-25 | 177 | 0.2103 | 0.2024 | +0.0079 ± 0.013 | 0.6123 | 0.5845 | 0.5751 | 0.382 | 0.4576 | -0.042 ± 0.0324 | -0.03 (1) |
| 25-40 | 97 | 0.2359 | 0.1903 | +0.0456 ± 0.0275 | 0.6638 | 0.5582 | 0.6062 | 0.2926 | 0.3711 | -0.069 ± 0.0409 | 0.0 (1) |
| 40+ | 20 | 0.3594 | 0.1625 | +0.1969 ± 0.082 | 0.9675 | 0.4925 | 0.7348 | 0.285 | 0.3 | -0.182 ± 0.0949 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 400 | 0.1698 | 0.1698 | +0.0000 ± 0.0007 | 0.5084 | 0.509 | 0.508 | 0.4934 | 0.5075 | -0.047 ± 0.0207 | -0.0162 (13) |
| 3-5 | 290 | 0.1793 | 0.1747 | +0.0046 ± 0.002 | 0.534 | 0.521 | 0.4871 | 0.4479 | 0.4138 | -0.094 ± 0.0248 | -0.01 (2) |
| 5-10 | 600 | 0.1919 | 0.1866 | +0.0053 ± 0.0027 | 0.5678 | 0.5448 | 0.4682 | 0.3943 | 0.3983 | -0.051 ± 0.0177 | -0.01 (3) |
| 10-15 | 516 | 0.1894 | 0.1747 | +0.0147 ± 0.0046 | 0.5609 | 0.5158 | 0.4888 | 0.3653 | 0.3682 | -0.062 ± 0.0184 | -0.03 (9) |
| 15-25 | 711 | 0.184 | 0.1489 | +0.0351 ± 0.0058 | 0.5559 | 0.4475 | 0.4881 | 0.2891 | 0.301 | -0.045 ± 0.0141 | -0.03 (2) |
| 25-40 | 589 | 0.215 | 0.0959 | +0.1191 ± 0.008 | 0.6229 | 0.3115 | 0.4961 | 0.1783 | 0.1511 | -0.079 ± 0.0122 | 0.0 (1) |
| 40+ | 423 | 0.3857 | 0.0351 | +0.3507 ± 0.01 | 1.0085 | 0.1519 | 0.6222 | 0.1036 | 0.0355 | -0.099 ± 0.0084 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 422 | 0.2051 | 0.2051 | -0.0000 ± 0.0007 | 0.5926 | 0.5931 | 0.5004 | 0.4858 | 0.4882 | -0.041 ± 0.0221 | -0.0226 (46) |
| 3-5 | 299 | 0.1936 | 0.1923 | +0.0012 ± 0.002 | 0.5685 | 0.5618 | 0.4629 | 0.4231 | 0.4314 | -0.042 ± 0.0252 | -0.0059 (32) |
| 5-10 | 641 | 0.1886 | 0.1837 | +0.0049 ± 0.0025 | 0.5608 | 0.5473 | 0.4603 | 0.3868 | 0.3916 | -0.040 ± 0.017 | -0.005 (72) |
| 10-15 | 424 | 0.2039 | 0.1919 | +0.0120 ± 0.0054 | 0.5972 | 0.5625 | 0.4597 | 0.336 | 0.3491 | -0.038 ± 0.0212 | 0.0016 (63) |
| 15-25 | 569 | 0.2338 | 0.2086 | +0.0252 ± 0.0075 | 0.6608 | 0.6033 | 0.5288 | 0.3357 | 0.3673 | -0.032 ± 0.0191 | -0.0216 (58) |
| 25-40 | 273 | 0.2696 | 0.17 | +0.0996 ± 0.0156 | 0.7445 | 0.5104 | 0.5765 | 0.2652 | 0.2601 | -0.070 ± 0.0246 | -0.0216 (25) |
| 40+ | 93 | 0.4235 | 0.1616 | +0.2619 ± 0.0447 | 1.192 | 0.4964 | 0.7363 | 0.2277 | 0.2473 | -0.056 ± 0.0433 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 778 | 0.1944 | 0.1939 | +0.0005 ± 0.0005 | 0.5672 | 0.5657 | 0.4951 | 0.4806 | 0.4692 | -0.052 ± 0.0158 | -0.0155 (82) |
| 3-5 | 542 | 0.1971 | 0.1953 | +0.0018 ± 0.0015 | 0.5741 | 0.5665 | 0.4679 | 0.4281 | 0.4262 | -0.047 ± 0.019 | -0.018 (54) |
| 5-10 | 1170 | 0.1874 | 0.1806 | +0.0068 ± 0.0019 | 0.5577 | 0.5376 | 0.4454 | 0.3714 | 0.3667 | -0.046 ± 0.0125 | -0.0089 (122) |
| 10-15 | 857 | 0.1982 | 0.1842 | +0.0140 ± 0.0037 | 0.5829 | 0.5423 | 0.451 | 0.3274 | 0.3326 | -0.040 ± 0.0145 | -0.0053 (99) |
| 15-25 | 1192 | 0.2212 | 0.1864 | +0.0348 ± 0.0049 | 0.6378 | 0.5473 | 0.5033 | 0.3078 | 0.3163 | -0.043 ± 0.0125 | -0.0255 (106) |
| 25-40 | 821 | 0.2452 | 0.1285 | +0.1166 ± 0.0079 | 0.6919 | 0.4018 | 0.5287 | 0.2136 | 0.1876 | -0.072 ± 0.0124 | -0.0206 (47) |
| 40+ | 483 | 0.3894 | 0.0799 | +0.3095 ± 0.0141 | 1.065 | 0.2678 | 0.6537 | 0.1373 | 0.1077 | -0.074 ± 0.0131 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 848 | 1.112 ± 0.097 | 1.209 | 0.1725 | 0.1843 | 0.207 | 0.1942 |
| gen2 | 848 | 0.941 ± 0.086 | 1.141 | 0.1893 | 0.1835 | 0.2241 | 0.1947 |
| gen1_elo | 848 | 1.085 ± 0.095 | 1.199 | 0.1772 | 0.1847 | 0.2065 | 0.1944 |
| gen1_sr | 848 | 1.134 ± 0.111 | 1.213 | 0.1452 | 0.1859 | 0.2199 | 0.1942 |
| gen1_ledger | 2721 | 0.883 ± 0.051 | 1.054 | 0.1628 | 0.1999 | 0.2197 | 0.1923 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 4,703)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,577 | 33.5% |
| STALE_QUOTE | market_freshness | 1,386 | 29.5% |
| POOR_DATA | data | 374 | 8.0% |
| BOOK_QUALITY | execution | 306 | 6.5% |
| LIMITED_DATA | data | 287 | 6.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 281 | 6.0% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 232 | 4.9% |
| IN_PLAY_QUOTE | market_freshness/coverage | 167 | 3.5% |
| IDENTITY_AMBIGUOUS | mapping | 90 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 3 | 0.1% |

Cause class: coverage 33.5%, market_freshness 29.5%, data 14.1%, market_freshness/coverage 9.5%, execution 6.5%, model_calibration_or_unknown 4.9%, mapping 1.9%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 94.2%, LOW_DATA_QUALITY 64.1%, STALE_KALSHI_QUOTE 63.1%, STALE_PLAYER_DATA 54.0%, THIN_PLAYER_HISTORY 51.9%, MODEL_INTERNAL_DISAGREEMENT 32.8%, ASYMMETRIC_SAMPLE_SIZE 28.1%, WIDE_SPREAD 14.7%, MODEL_HIGH_UNCERTAINTY 13.3%, PLAYER_IDENTITY_RISK 10.8%, LEVEL_TRANSFER_RISK 8.4%, EVENT_MAPPING_RISK 6.8%, LOW_DISPLAYED_LIQUIDITY 4.9%, MODEL_CALIBRATION_OUTLIER 2.2%, UNKNOWN 0.8%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.2%, POST_SETTLEMENT_OBSERVATION 33.5%, POSSIBLE_IN_PLAY_QUOTE 6.8%, CONFIRMED_IN_PLAY_QUOTE 1.2%

### >= ge_25 pp (N = 2,587)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,221 | 47.2% |
| STALE_QUOTE | market_freshness | 618 | 23.9% |
| POOR_DATA | data | 163 | 6.3% |
| BOOK_QUALITY | execution | 148 | 5.7% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 142 | 5.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 100 | 3.9% |
| LIMITED_DATA | data | 79 | 3.0% |
| IDENTITY_AMBIGUOUS | mapping | 64 | 2.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 52 | 2.0% |

Cause class: coverage 47.2%, market_freshness 23.9%, data 9.3%, market_freshness/coverage 9.3%, execution 5.7%, mapping 2.5%, model_calibration_or_unknown 2.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 96.6%, STALE_KALSHI_QUOTE 70.3%, LOW_DATA_QUALITY 67.9%, THIN_PLAYER_HISTORY 54.3%, STALE_PLAYER_DATA 51.8%, MODEL_INTERNAL_DISAGREEMENT 33.5%, ASYMMETRIC_SAMPLE_SIZE 30.3%, MODEL_HIGH_UNCERTAINTY 14.5%, PLAYER_IDENTITY_RISK 13.3%, WIDE_SPREAD 13.3%, EVENT_MAPPING_RISK 8.3%, LEVEL_TRANSFER_RISK 7.9%, LOW_DISPLAYED_LIQUIDITY 5.4%, MODEL_CALIBRATION_OUTLIER 3.2%, UNKNOWN 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 50.0%, POST_SETTLEMENT_OBSERVATION 47.2%, POSSIBLE_IN_PLAY_QUOTE 6.5%, CONFIRMED_IN_PLAY_QUOTE 1.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 2210, "IDENTITY_AMBIGUOUS": 377}; ticker orientation: {"VERIFIED": 2587}.

Checks: discipline:AMBIGUOUS 182, discipline:PASS 2405, identity_confidence:AMBIGUOUS 345, identity_confidence:PASS 2242, level_mapping:NA 194, level_mapping:PASS 2393, market_pair:AMBIGUOUS 62, market_pair:NA 75, market_pair:PASS 2450, model_complement:NA 46, model_complement:PASS 2541, namesake:PASS 2587, physical_match_id:NA 1326, physical_match_id:PASS 1261, player_ids:PASS 2587, same_pair_other_event:PASS 2587, ticker_orientation:PASS 2587

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 313 | 3.8% | 4.0% | 0.5% | {"market_freshness": 12} | 6.14 | 0.1791 / 0.1823 (49) | 39.3% | 0.0% | 0.6% | 3.5% |
| CHALLENGER | 1,634 | 19.1% | 8.4% | 12.1% | {"coverage": 167, "market_freshness": 74, "market_freshness/coverage": 39, "data": 17, "model_calibration_or_unknown": 12, "execution": 3} | 7.81 | 0.2262 / 0.209 (535) | 53.1% | 4.0% | 0.7% | 22.8% |
| DOUBLES | 373 | 48.8% | 48.7% | 7.0% | {"market_freshness": 106, "execution": 32, "mapping": 26, "market_freshness/coverage": 12, "coverage": 6} | 24.15 | 0.3278 / 0.2277 (157) | 60.9% | 0.0% | 100.0% | 9.7% |
| ITF_MEN | 3,584 | 25.1% | 13.8% | 34.7% | {"coverage": 496, "market_freshness": 163, "data": 87, "execution": 71, "market_freshness/coverage": 70, "mapping": 10, "model_calibration_or_unknown": 1} | 9.74 | 0.2126 / 0.1868 (1298) | 55.8% | 49.4% | 5.3% | 32.6% |
| ITF_WOMEN | 3,540 | 29.0% | 17.2% | 39.7% | {"coverage": 539, "market_freshness": 216, "data": 119, "market_freshness/coverage": 81, "execution": 33, "mapping": 26, "model_calibration_or_unknown": 13} | 12.22 | 0.2059 / 0.1866 (1140) | 58.6% | 54.1% | 6.2% | 33.1% |
| OTHER | 149 | 8.1% | 7.3% | 0.5% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 798 | 9.4% | 8.1% | 2.9% | {"market_freshness": 34, "model_calibration_or_unknown": 12, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.66 | 0.2006 / 0.1964 (129) | 40.5% | 2.6% | 1.5% | 3.8% |
| WTA125 | 421 | 16.4% | 9.1% | 2.7% | {"market_freshness/coverage": 30, "model_calibration_or_unknown": 12, "market_freshness": 11, "data": 8, "coverage": 8} | 10.39 | 0.2261 / 0.2035 (219) | 34.4% | 9.0% | 0.5% | 19.2% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 3 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 4 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 5 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 6 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 7 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 8 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 9 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 10 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 11 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 12 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 14 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 15 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 16 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 17 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 18 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 19 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 20 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 21 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 22 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 22 min (AGING); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 23 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 24 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 25 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 114 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 26 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 27 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 28 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 29 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 708 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 30 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 31 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 32 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 33 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 34 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 114 min (STALE); data LIMITED (grade B, thinner serve sample 2163.0, ratio 2.0); no external reference |
| 35 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 407 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 36 | `KXWTAMATCH-26OCT01YASCHW-CHW` | WTA | fair_v1 | 73% / 2% | +70 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 51 min (STALE); no external reference |
| 37 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 38 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 39 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |
| 41 | `KXITFWMATCH-26SEP30KOKUEM-KOK` | ITF_WOMEN | fair_v1 | 79% / 10% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 776 min (STALE); data LIMITED (grade C, thinner serve sample 824.0, ratio 2.35); no external reference |
| 42 | `KXITFMATCH-26SEP20WILRAH-RAH` | ITF_MEN | gen1_ledger | 72% / 4% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade B, thinner serve sample 2782.0, ratio 1.84); no external reference |
| 43 | `KXITFMATCH-26SEP26NAGTHO-NAG` | ITF_MEN | gen1_ledger | 76% / 7% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 89 min (STALE); data LIMITED (grade C, thinner serve sample 1323.0, ratio 4.45); no external reference |
| 44 | `KXITFWMATCH-26SEP26PERPRE-PER` | ITF_WOMEN | gen1_ledger | 78% / 10% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 102 min (STALE); data POOR (grade D, thinner serve sample 1020.0, ratio 2.77); no external reference |
| 45 | `KXITFMATCH-26SEP22YILAGA-AGA` | ITF_MEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 203 min (STALE); data LIMITED (grade B, thinner serve sample 2786.0, ratio 2.08); no external reference |
| 46 | `KXITFMATCH-26SEP30DIMURA-URA` | ITF_MEN | fair_v1 | 71% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.5h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 819 min (STALE); data POOR (grade F, thinner serve sample 174.0, ratio 2.63); no external reference |
| 47 | `KXITFWMATCH-26OCT01TANVED-TAN` | ITF_WOMEN | fair_v1 | 76% / 8% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 167 min (STALE); no external reference |
| 48 | `KXITFWMATCH-26SEP20LLIBON-BON` | ITF_WOMEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 69 min (STALE); data POOR (grade D, thinner serve sample 1210.0, ratio 3.0); no external reference |
| 49 | `KXATPCHALLENGERDOUBLES-26SEP17ARESTEBLASCH-BLASCH` | DOUBLES | gen1_ledger | 95% / 28% | +67 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 79 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFWMATCH-26SEP24BOUKUR-BOU` | ITF_WOMEN | gen1_ledger | 76% / 8% | +67 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 113 min (STALE); data POOR (grade D, thinner serve sample 1497.0, ratio 2.48); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9664, "by_level_share_of_ge_25pp": {"ATP": 0.0046, "CHALLENGER": 0.1206, "DOUBLES": 0.0704, "ITF_MEN": 0.3471, "ITF_WOMEN": 0.397, "OTHER": 0.0046, "WTA": 0.029, "WTA125": 0.0267}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.7031, "share_primary_cause_market_settled_or_in_play": 0.5656, "share_primary_cause_stale_quote_only": 0.2389}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 2587, "identity_ambiguous_share": 0.1457, "ticker_orientation": {"VERIFIED": 2587}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 1261, "with_external": 6, "coverage": 0.0048, "external_status": {"EXTERNAL_STALE": 6}, "triangulation": {"INSUFFICIENT_INPUTS": 6}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 487, "with_external": 6, "coverage": 0.0123, "external_status": {"EXTERNAL_STALE": 6}, "triangulation": {"INSUFFICIENT_INPUTS": 6}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 824.0, "median_sample_ratio": 2.27, "median_min_matches": 26.0, "median_max_days_since_last": 172.0, "share_severe_asymmetry": 0.1643, "data_status": {"POOR": 1199, "LIMITED": 880, "ADEQUATE": 508}, "comparison_lt_10pp": {"median_thinner_serve_points": 1969.0, "median_sample_ratio": 1.71, "median_min_matches": 79.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 192, "model_minus_observed": 0.1034, "kalshi_minus_observed": -0.0285, "brier_diff_model_minus_kalshi": 0.0142}, "4-10x": {"n": 136, "model_minus_observed": 0.0978, "kalshi_minus_observed": -0.0362, "brier_diff_model_minus_kalshi": 0.0087}, "<2x": {"n": 386, "model_minus_observed": 0.0757, "kalshi_minus_observed": -0.0436, "brier_diff_model_minus_kalshi": 0.0114}, ">=10x": {"n": 134, "model_minus_observed": 0.0911, "kalshi_minus_observed": -0.0709, "brier_diff_model_minus_kalshi": 0.0186}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 848, "model": {"intercept": -0.648, "slope": 0.941, "slope_se": 0.086}, "kalshi_mid_same_rows": {"intercept": 0.177, "slope": 1.141, "slope_se": 0.095}, "mean_extremity_model": 0.1893, "mean_extremity_kalshi": 0.1835, "model_brier": 0.2241, "kalshi_brier": 0.1947, "brier_diff_model_minus_kalshi": 0.0294, "brier_diff_se": 0.0065, "model_logloss": 0.6409, "kalshi_logloss": 0.568}, "fair_v1": {"n": 848, "model": {"intercept": -0.443, "slope": 1.112, "slope_se": 0.097}, "kalshi_mid_same_rows": {"intercept": 0.299, "slope": 1.209, "slope_se": 0.098}, "mean_extremity_model": 0.1725, "mean_extremity_kalshi": 0.1843, "model_brier": 0.207, "kalshi_brier": 0.1942, "brier_diff_model_minus_kalshi": 0.0128, "brier_diff_se": 0.0051, "model_logloss": 0.5991, "kalshi_logloss": 0.5671}, "gen1_elo": {"n": 848, "model": {"intercept": -0.417, "slope": 1.085, "slope_se": 0.095}, "kalshi_mid_same_rows": {"intercept": 0.313, "slope": 1.199, "slope_se": 0.097}, "mean_extremity_model": 0.1772, "mean_extremity_kalshi": 0.1847, "model_brier": 0.2065, "kalshi_brier": 0.1944, "brier_diff_model_minus_kalshi": 0.0122, "brier_diff_se": 0.0051, "model_logloss": 0.5996, "kalshi_logloss": 0.5672}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2592, "share_ge_15": 0.4454, "median_abs_gap": 13.02, "n": 4865}, "gen1_elo": {"share_ge_25": 0.252, "share_ge_15": 0.4335, "median_abs_gap": 12.51, "n": 4865}, "gen1_sr": {"share_ge_25": 0.31, "share_ge_15": 0.5342, "median_abs_gap": 16.43, "n": 4865}, "gen2": {"share_ge_25": 0.3096, "share_ge_15": 0.5087, "median_abs_gap": 15.43, "n": 4865}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1399, "share_ge_15": 0.33, "median_abs_gap": 9.98, "n": 3482}, "gen1_elo": {"share_ge_25": 0.1401, "share_ge_15": 0.3122, "median_abs_gap": 9.51, "n": 3482}, "gen1_sr": {"share_ge_25": 0.1956, "share_ge_15": 0.4345, "median_abs_gap": 12.69, "n": 3482}, "gen2": {"share_ge_25": 0.2091, "share_ge_15": 0.4239, "median_abs_gap": 12.77, "n": 3482}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 6.14, "share_ge_25_all": 0.0383, "share_ge_25_pregame_clean": 0.0397}, "WTA": {"median_abs_gap_pregame_clean": 8.66, "share_ge_25_all": 0.094, "share_ge_25_pregame_clean": 0.0807}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2231, "share_within_10pp_all": 0.4173, "share_within_10pp_pregame_clean": 0.4994, "corr_model_vs_mid_pregame_clean": 0.8284}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 144, "model_brier": 0.1771, "kalshi_brier": 0.1778, "brier_diff_model_minus_kalshi": -0.0006}, "10-15": {"n_settled": 145, "model_brier": 0.2162, "kalshi_brier": 0.2103, "brier_diff_model_minus_kalshi": 0.0059}, "15-25": {"n_settled": 180, "model_brier": 0.2119, "kalshi_brier": 0.2111, "brier_diff_model_minus_kalshi": 0.0008}, "25-40": {"n_settled": 89, "model_brier": 0.2374, "kalshi_brier": 0.1802, "brier_diff_model_minus_kalshi": 0.0572}, "3-5": {"n_settled": 86, "model_brier": 0.1747, "kalshi_brier": 0.1713, "brier_diff_model_minus_kalshi": 0.0034}, "40+": {"n_settled": 25, "model_brier": 0.3417, "kalshi_brier": 0.1463, "brier_diff_model_minus_kalshi": 0.1954}, "5-10": {"n_settled": 179, "model_brier": 0.2002, "kalshi_brier": 0.2022, "brier_diff_model_minus_kalshi": -0.002}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|CHALLENGER
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'NO_SKILL:gen2|CHALLENGER', 'TOO_EXTREME:gen1_ledger']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.565, "slope": 0.883, "slope_se": 0.051}, "kalshi_slope": {"intercept": 0.082, "slope": 1.054, "slope_se": 0.053}, "n": 2721}, "NO_SKILL:gen2|CHALLENGER": {"n_settled": 117, "model_brier": 0.2501, "kalshi_brier": 0.2215, "brier_diff_model_minus_kalshi": 0.0287, "brier_diff_se": 0.0134, "corr_model_outcome": 0.2086, "corr_kalshi_outcome": 0.2237}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 157, "model_brier": 0.3278, "kalshi_brier": 0.2277, "brier_diff_model_minus_kalshi": 0.1001, "brier_diff_se": 0.0263, "corr_model_outcome": -0.0891, "corr_kalshi_outcome": 0.3284}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
