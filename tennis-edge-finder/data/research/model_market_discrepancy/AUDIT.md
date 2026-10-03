# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-03T12:20Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 11,060): 0-3 13.3%, 3-5 9.0%, 5-10 19.4%, 10-15 14.9%, 15-25 19.6%, 25-40 14.3%, 40+ 9.6%; median gap 12.59 pp.
* **Where the extremes live**: 96.7% of >=25 pp gaps are off the ATP/WTA main tour (ITF 74.6%, Challenger 12.0%, doubles 6.9%). Main tour: ATP 4.1% and WTA 9.4% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 2,639): MARKET_ALREADY_SETTLED_WHEN_PRICED 47.4%, STALE_QUOTE 23.6%, POOR_DATA 6.2%, BOOK_QUALITY 5.7%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IN_PLAY_QUOTE 3.8%, LIMITED_DATA 3.1%, IDENTITY_AMBIGUOUS 2.6%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%. By class: coverage 47.4%, market_freshness 23.6%, data 9.4%, market_freshness/coverage 9.2%, execution 5.7%, mapping 2.6%, model_calibration_or_unknown 2.1%.
* **Stale / settled / in-play**: 70.1% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 56.6% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 2,639 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 14.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 0.5%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 9.2% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 824.0 points vs 2005.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.108, Gen-2 0.942, Gen-1 ledger 0.885 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 90 model 0.2352 vs Kalshi 0.181; n 26 model 0.3509 vs Kalshi 0.1453.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 35,324 model-market comparisons (61,080 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 16,630 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-03T12:16:28.474381+00:00'], shadow board 9,951 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-03T12:16:32.036545+00:00'], Model 4 2,930 rows, 8,254 settled tickers, 1,807 tickers with an external scan.
* By model: {"gen1_ledger": 9659, "gen1_elo": 5006, "fair_v1": 5006, "gen2": 5006, "gen1_sr": 5006, "model4_fundamental": 2825, "model4_conditioned": 2816}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 11,060 | 13.3 | 9.0 | 19.4 | 14.9 | 19.6 | 14.3 | 9.6 | 12.59 | 43.5% | 23.9% |
| MW fair_v1 | 5,006 | 13.4 | 8.3 | 18.6 | 15.2 | 18.7 | 14.9 | 10.9 | 13.05 | 44.5% | 25.9% |
| MW gen1_elo | 5,006 | 13.0 | 8.8 | 19.9 | 15.0 | 18.2 | 14.9 | 10.3 | 12.51 | 43.3% | 25.2% |
| MW gen1_ledger | 6,054 | 13.2 | 9.5 | 20.1 | 14.7 | 20.4 | 13.8 | 8.4 | 12.22 | 42.6% | 22.2% |
| MW gen1_sr | 5,006 | 9.6 | 7.0 | 16.7 | 13.4 | 22.4 | 18.6 | 12.4 | 16.39 | 53.4% | 31.0% |
| MW gen2 | 5,006 | 11.2 | 6.2 | 16.6 | 14.8 | 20.3 | 17.2 | 13.7 | 15.54 | 51.2% | 30.9% |
| all families model4_conditioned | 2,816 | 18.6 | 15.4 | 29.6 | 23.8 | 8.4 | 2.4 | 1.9 | 7.37 | 12.6% | 4.3% |
| all families model4_fundamental | 2,825 | 14.6 | 10.7 | 29.9 | 21.7 | 14.6 | 5.5 | 3.0 | 9.1 | 23.1% | 8.5% |

Configurable thresholds (primary): >=5pp 77.8%, >=10pp 58.4%, >=15pp 43.5%, >=20pp 32.9%, >=25pp 23.9%, >=30pp 17.6%, >=40pp 9.6%, >=50pp 4.3%
Executable gap (model outside the book, before fees): median 10.28pp; >=10pp 50.7%, >=25pp 21.2%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 242 | 22.3 | 17.4 | 27.3 | 12.8 | 14.9 | 1.6 | 3.7 | 6.19 | 20.2% | 5.4% |
| CHALLENGER | 867 | 14.7 | 9.2 | 16.0 | 16.4 | 15.6 | 15.2 | 12.9 | 13.33 | 43.7% | 28.1% |
| ITF_MEN | 1,621 | 11.8 | 8.4 | 19.8 | 15.1 | 17.6 | 14.7 | 12.6 | 12.81 | 44.9% | 27.3% |
| ITF_WOMEN | 1,757 | 10.5 | 6.3 | 15.7 | 15.2 | 21.6 | 18.8 | 11.8 | 15.96 | 52.3% | 30.7% |
| WTA | 435 | 23.0 | 10.6 | 25.8 | 12.6 | 18.9 | 6.7 | 2.5 | 8.16 | 28.1% | 9.2% |
| WTA125 | 84 | 14.3 | 4.8 | 17.9 | 23.8 | 20.2 | 14.3 | 4.8 | 12.4 | 39.3% | 19.1% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 242 | 23.1 | 12.8 | 24.8 | 16.1 | 17.4 | 1.6 | 4.1 | 7.29 | 23.1% | 5.8% |
| CHALLENGER | 867 | 11.1 | 5.1 | 17.8 | 16.4 | 19.1 | 17.9 | 12.7 | 14.94 | 49.7% | 30.6% |
| ITF_MEN | 1,621 | 9.9 | 6.2 | 17.5 | 15.5 | 20.3 | 16.5 | 14.1 | 15.41 | 50.8% | 30.5% |
| ITF_WOMEN | 1,757 | 8.8 | 6.1 | 14.0 | 12.6 | 20.6 | 19.9 | 18.1 | 18.65 | 58.5% | 38.0% |
| WTA | 435 | 20.5 | 5.5 | 16.8 | 15.6 | 22.3 | 16.8 | 2.5 | 12.98 | 41.6% | 19.3% |
| WTA125 | 84 | 6.0 | 6.0 | 16.7 | 20.2 | 22.6 | 15.5 | 13.1 | 15.56 | 51.2% | 28.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 242 | 28.1 | 12.8 | 28.5 | 10.7 | 9.1 | 7.0 | 3.7 | 6.53 | 19.8% | 10.7% |
| CHALLENGER | 867 | 15.1 | 8.2 | 21.6 | 13.8 | 13.4 | 14.2 | 13.7 | 11.49 | 41.3% | 27.9% |
| ITF_MEN | 1,621 | 10.1 | 9.6 | 18.7 | 16.0 | 18.0 | 15.6 | 12.0 | 13.08 | 45.6% | 27.6% |
| ITF_WOMEN | 1,757 | 9.7 | 6.6 | 16.6 | 14.4 | 23.8 | 18.6 | 10.4 | 16.52 | 52.8% | 29.0% |
| WTA | 435 | 23.4 | 14.0 | 29.4 | 15.6 | 11.5 | 4.4 | 1.6 | 6.99 | 17.5% | 6.0% |
| WTA125 | 84 | 16.7 | 6.0 | 22.6 | 29.8 | 13.1 | 10.7 | 1.2 | 10.92 | 25.0% | 11.9% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 72 | 23.6 | 22.2 | 34.7 | 12.5 | 6.9 | 0.0 | 0.0 | 6.26 | 6.9% | 0.0% |
| CHALLENGER | 813 | 21.2 | 13.9 | 26.6 | 16.0 | 13.3 | 6.5 | 2.6 | 7.45 | 22.4% | 9.1% |
| DOUBLES | 382 | 5.8 | 3.9 | 9.9 | 10.5 | 22.0 | 20.7 | 27.2 | 23.99 | 69.9% | 47.9% |
| ITF_MEN | 2,054 | 14.2 | 9.2 | 18.9 | 14.0 | 20.7 | 13.5 | 9.5 | 12.41 | 43.7% | 23.0% |
| ITF_WOMEN | 1,884 | 8.9 | 8.3 | 17.4 | 14.1 | 23.9 | 18.4 | 9.0 | 15.54 | 51.3% | 27.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 363 | 15.4 | 9.4 | 25.6 | 22.3 | 17.6 | 8.8 | 0.8 | 9.8 | 27.3% | 9.6% |
| WTA125 | 337 | 13.3 | 9.5 | 21.7 | 16.9 | 22.9 | 11.9 | 3.9 | 11.35 | 38.6% | 15.7% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 241 | 22.0 | 17.4 | 27.4 | 12.9 | 14.9 | 1.7 | 3.7 | 6.21 | 20.3% | 5.4% |
| CHALLENGER | 637 | 18.5 | 11.5 | 19.6 | 19.6 | 16.8 | 8.9 | 5.0 | 10.19 | 30.8% | 14.0% |
| ITF_MEN | 1,024 | 15.6 | 11.8 | 25.0 | 16.9 | 17.3 | 9.5 | 3.9 | 9.5 | 30.7% | 13.4% |
| ITF_WOMEN | 1,173 | 14.4 | 8.3 | 18.9 | 17.6 | 22.9 | 13.2 | 4.6 | 12.62 | 40.8% | 17.8% |
| WTA | 434 | 23.0 | 10.6 | 25.8 | 12.7 | 18.9 | 6.5 | 2.5 | 8.16 | 27.9% | 9.0% |
| WTA125 | 81 | 14.8 | 4.9 | 18.5 | 24.7 | 19.8 | 12.3 | 4.9 | 11.65 | 37.0% | 17.3% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 241 | 23.2 | 12.4 | 24.9 | 16.2 | 17.4 | 1.7 | 4.2 | 7.5 | 23.2% | 5.8% |
| CHALLENGER | 637 | 13.8 | 6.4 | 22.4 | 19.9 | 20.6 | 12.7 | 4.1 | 11.92 | 37.4% | 16.8% |
| ITF_MEN | 1,024 | 13.4 | 7.6 | 21.8 | 17.9 | 21.4 | 12.6 | 5.4 | 11.83 | 39.4% | 18.0% |
| ITF_WOMEN | 1,173 | 10.7 | 8.0 | 16.0 | 12.4 | 23.8 | 17.5 | 11.6 | 16.06 | 52.9% | 29.1% |
| WTA | 434 | 20.5 | 5.5 | 16.8 | 15.7 | 22.4 | 16.6 | 2.5 | 12.96 | 41.5% | 19.1% |
| WTA125 | 81 | 6.2 | 6.2 | 16.1 | 21.0 | 23.5 | 16.1 | 11.1 | 15.33 | 50.6% | 27.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 62 | 24.2 | 25.8 | 35.5 | 12.9 | 1.6 | 0.0 | 0.0 | 5.45 | 1.6% | 0.0% |
| CHALLENGER | 664 | 23.6 | 16.3 | 29.4 | 15.7 | 12.5 | 2.4 | 0.1 | 6.68 | 15.1% | 2.6% |
| DOUBLES | 345 | 6.1 | 3.8 | 10.1 | 10.4 | 21.7 | 20.9 | 27.0 | 23.94 | 69.6% | 47.8% |
| ITF_MEN | 1,460 | 17.3 | 11.2 | 22.1 | 15.2 | 20.8 | 9.9 | 3.6 | 9.87 | 34.2% | 13.5% |
| ITF_WOMEN | 1,276 | 11.0 | 9.9 | 21.2 | 16.2 | 24.9 | 14.7 | 2.1 | 12.17 | 41.8% | 16.9% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 334 | 15.6 | 9.9 | 26.4 | 23.1 | 18.3 | 6.9 | 0.0 | 9.55 | 25.1% | 6.9% |
| WTA125 | 259 | 15.8 | 10.4 | 25.9 | 20.1 | 21.2 | 6.2 | 0.4 | 9.54 | 27.8% | 6.6% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 382 | 5.8 | 3.9 | 9.9 | 10.5 | 22.0 | 20.7 | 27.2 | 23.99 | 69.9% | 47.9% |
| singles | 5,672 | 13.7 | 9.8 | 20.7 | 15.0 | 20.3 | 13.3 | 7.2 | 11.79 | 40.7% | 20.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 1,086 | 15.4 | 8.6 | 19.0 | 14.6 | 15.9 | 13.9 | 12.7 | 12.33 | 42.5% | 26.6% |
| Hard | 3,583 | 12.7 | 8.5 | 18.8 | 15.0 | 19.4 | 15.2 | 10.4 | 13.25 | 45.0% | 25.6% |
| UNKNOWN | 337 | 14.2 | 5.9 | 14.5 | 19.3 | 19.9 | 14.8 | 11.3 | 13.67 | 46.0% | 26.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,562 | 17.2 | 10.2 | 20.8 | 14.8 | 17.3 | 11.3 | 8.4 | 10.42 | 37.0% | 19.7% |
| B | 721 | 17.2 | 10.7 | 17.1 | 16.8 | 16.1 | 10.4 | 11.8 | 11.28 | 38.3% | 22.2% |
| C | 826 | 12.1 | 8.1 | 22.4 | 13.4 | 16.8 | 15.7 | 11.4 | 12.95 | 44.0% | 27.1% |
| D | 930 | 11.1 | 7.6 | 17.6 | 14.6 | 20.8 | 15.6 | 12.7 | 14.48 | 49.0% | 28.3% |
| F | 967 | 7.7 | 4.5 | 13.7 | 16.6 | 22.4 | 22.9 | 12.3 | 18.42 | 57.6% | 35.2% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,869 | 18.7 | 12.0 | 26.1 | 16.7 | 16.4 | 7.0 | 3.2 | 8.65 | 26.5% | 10.1% |
| B | 1,000 | 13.7 | 9.6 | 21.4 | 16.0 | 19.4 | 12.5 | 7.4 | 11.6 | 39.3% | 19.9% |
| C | 1,248 | 11.2 | 8.4 | 15.9 | 13.8 | 22.2 | 15.4 | 13.1 | 15.3 | 50.7% | 28.5% |
| D | 929 | 11.1 | 8.1 | 20.6 | 11.9 | 24.1 | 15.4 | 8.8 | 14.28 | 48.3% | 24.2% |
| F | 1,008 | 6.9 | 7.1 | 12.2 | 13.4 | 23.1 | 24.2 | 13.0 | 18.94 | 60.3% | 37.2% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 1,935 | 16.6 | 9.6 | 19.8 | 15.8 | 16.9 | 11.4 | 9.9 | 10.98 | 38.2% | 21.3% |
| LIMITED | 1,156 | 14.5 | 10.2 | 21.4 | 13.4 | 16.4 | 13.8 | 10.3 | 11.67 | 40.4% | 24.1% |
| POOR | 1,915 | 9.4 | 6.0 | 15.5 | 15.6 | 21.8 | 19.2 | 12.4 | 16.53 | 53.4% | 31.6% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 341 | 34.3 | 22.9 | 33.1 | 6.5 | 2.4 | 0.9 | 0.0 | 4.16 | 3.2% | 0.9% |
| GAME_SPREAD | 406 | 19.9 | 16.5 | 37.0 | 16.0 | 8.9 | 1.2 | 0.5 | 6.59 | 10.6% | 1.7% |
| MATCH_WINNER | 6,054 | 13.2 | 9.5 | 20.1 | 14.7 | 20.4 | 13.8 | 8.4 | 12.22 | 42.6% | 22.2% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 1,702 | 21.7 | 13.4 | 30.6 | 17.2 | 13.6 | 2.8 | 0.7 | 7.04 | 17.0% | 3.4% |
| TOTAL_GAMES | 1,132 | 9.9 | 9.4 | 26.5 | 24.9 | 17.0 | 8.0 | 4.4 | 10.66 | 29.3% | 12.4% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 887 | 28.6 | 32.6 | 26.8 | 0.7 | 9.1 | 1.7 | 0.5 | 4.28 | 11.3% | 2.1% |
| GAME_SPREAD | 565 | 36.6 | 15.0 | 25.3 | 17.9 | 2.5 | 1.9 | 0.7 | 4.55 | 5.1% | 2.6% |
| TOTAL_GAMES | 1,364 | 4.5 | 4.5 | 33.1 | 41.3 | 10.3 | 3.1 | 3.2 | 10.72 | 16.6% | 6.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 887 | 26.2 | 16.7 | 33.6 | 8.1 | 9.9 | 4.5 | 1.0 | 5.79 | 15.4% | 5.5% |
| GAME_SPREAD | 565 | 17.5 | 10.3 | 25.5 | 23.2 | 15.9 | 5.1 | 2.5 | 9.56 | 23.5% | 7.6% |
| TOTAL_GAMES | 1,373 | 5.8 | 7.0 | 29.4 | 29.9 | 17.0 | 6.3 | 4.4 | 10.91 | 27.8% | 10.8% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5,006 | 44.5% | 25.9% | 13.05 | 33.1% | 14.0% | 10.02 |
| gen1_elo | 5,006 | 43.3% | 25.2% | 12.51 | 31.2% | 14.0% | 9.51 |
| gen1_sr | 5,006 | 53.4% | 31.0% | 16.39 | 43.4% | 19.6% | 12.73 |
| gen2 | 5,006 | 51.2% | 30.9% | 15.54 | 42.8% | 20.9% | 12.85 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 1,892 | 17.6 | 12.1 | 23.3 | 15.9 | 18.3 | 9.7 | 3.2 | 9.37 | 31.2% | 12.8% |
| STALE | 3,114 | 10.8 | 6.1 | 15.7 | 14.7 | 18.9 | 18.1 | 15.7 | 16.48 | 52.7% | 33.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,277 | 15.2 | 10.4 | 22.0 | 16.0 | 19.8 | 12.0 | 4.6 | 10.66 | 36.4% | 16.7% |
| STALE | 2,777 | 10.9 | 8.3 | 17.8 | 13.2 | 21.1 | 15.8 | 12.9 | 14.87 | 49.8% | 28.7% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 11,060 | 0 | 5169 | 5891 | 31.2 | 216.1 | 1400.4 |
| ge_15pp | 4,808 | 0 | 1784 | 3024 | 39.7 | 507.5 | 1380.4 |
| ge_25pp | 2,639 | 0 | 789 | 1850 | 54.1 | 637.8 | 1380.4 |
| lt_10pp | 4,603 | 0 | 2562 | 2041 | 28.4 | 54.8 | 1201.9 |

Current slate `SL-20261003T122045Z-42895fa6`: 74 priced rows, quote age at build {'median': 22.3, 'max': 39.1}, freshness {'AGING': 62, 'STALE': 12}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 140 | 20.7 | 10.7 | 22.9 | 22.9 | 18.6 | 4.3 | 0.0 | 7.95 | 22.9% | 4.3% |
| MARKETS_AGREE | 8 | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.96 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 15 | 0.0 | 0.0 | 13.3 | 40.0 | 46.7 | 0.0 | 0.0 | 14.99 | 46.7% | 0.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 5,006 | 164 (3.3%) | 9.2% | 0.0% | {"EXTERNAL_STALE": 140, "AGREES_WITH_KALSHI": 15, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 2,230 | 39 (1.8%) | 17.9% | 0.0% | {"EXTERNAL_STALE": 32, "AGREES_WITH_KALSHI": 7} |
| fair_v1_ge_25pp | 1,295 | 6 (0.5%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 6} |
| fair_v1_ge_25pp_pregame_clean | 501 | 6 (1.2%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 6} |
| fair_v1_lt_10pp | 2,017 | 87 (4.3%) | 2.3% | 0.0% | {"EXTERNAL_STALE": 76, "ALL_AGREE": 8, "AGREES_WITH_KALSHI": 2, "EXTERNAL_OUTLIER": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 986 | 12.0 | 7.2 | 18.7 | 15.5 | 20.0 | 16.2 | 10.4 | 13.71 | 46.7% | 26.7% |
| 4-10x | 668 | 12.0 | 8.8 | 18.3 | 15.4 | 17.8 | 16.3 | 11.4 | 13.67 | 45.5% | 27.7% |
| <2x | 2,766 | 14.8 | 9.2 | 19.2 | 14.9 | 18.2 | 13.0 | 10.7 | 12.11 | 41.9% | 23.7% |
| >=10x | 586 | 10.8 | 5.6 | 15.7 | 15.5 | 19.8 | 20.3 | 12.3 | 16.17 | 52.4% | 32.6% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 1,355 | 14.2 | 8.7 | 20.4 | 15.3 | 17.4 | 12.1 | 11.8 | 12.01 | 41.3% | 23.9% |
| 300-1000 | 1,217 | 12.9 | 7.4 | 16.8 | 15.9 | 20.0 | 16.4 | 10.6 | 14.12 | 46.9% | 27.0% |
| <300 | 1,170 | 8.6 | 5.8 | 15.1 | 14.4 | 21.3 | 21.4 | 13.3 | 18.03 | 56.1% | 34.8% |
| >=3000 | 1,264 | 17.4 | 11.2 | 21.4 | 14.9 | 16.4 | 10.5 | 8.2 | 9.98 | 35.0% | 18.7% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 195 | 0.5161 | 0.383 | 0.4154 | +0.101 | -0.032 | 0.0135 ± 0.0105 |
| ratio 4-10x | 140 | 0.5855 | 0.4495 | 0.4857 | +0.100 | -0.036 | 0.0121 ± 0.0125 |
| ratio <2x | 401 | 0.534 | 0.4152 | 0.4613 | +0.073 | -0.046 | 0.0117 ± 0.0068 |
| ratio >=10x | 136 | 0.5529 | 0.3918 | 0.4559 | +0.097 | -0.064 | 0.0197 ± 0.0156 |
| thinner_sample 1000-3000 | 231 | 0.537 | 0.4168 | 0.4545 | +0.082 | -0.038 | 0.0095 ± 0.0092 |
| thinner_sample 300-1000 | 250 | 0.5566 | 0.4279 | 0.468 | +0.089 | -0.040 | 0.0065 ± 0.0092 |
| thinner_sample <300 | 272 | 0.5392 | 0.3807 | 0.4485 | +0.091 | -0.068 | 0.0212 ± 0.0104 |
| thinner_sample >=3000 | 119 | 0.5217 | 0.425 | 0.437 | +0.085 | -0.012 | 0.0179 ± 0.0101 |
| data_status ADEQUATE | 251 | 0.5258 | 0.4173 | 0.4462 | +0.080 | -0.029 | 0.0097 ± 0.0078 |
| data_status LIMITED | 192 | 0.559 | 0.4373 | 0.5 | +0.059 | -0.063 | 0.0023 ± 0.0107 |
| data_status POOR | 429 | 0.5423 | 0.3932 | 0.4382 | +0.104 | -0.045 | 0.0206 ± 0.0078 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 145 | 0.1764 | 0.1771 | -0.0007 ± 0.0012 | 0.5257 | 0.5277 | 0.4963 | 0.4817 | 0.4966 | -0.092 ± 0.0381 | -0.01 (3) |
| 3-5 | 91 | 0.1761 | 0.1748 | +0.0012 ± 0.0036 | 0.5331 | 0.5256 | 0.5201 | 0.4792 | 0.4835 | -0.089 ± 0.0468 | 0.02 (1) |
| 5-10 | 185 | 0.201 | 0.2036 | -0.0026 ± 0.005 | 0.5876 | 0.5933 | 0.5172 | 0.4425 | 0.4919 | -0.052 ± 0.0336 | -0.0167 (3) |
| 10-15 | 147 | 0.216 | 0.2088 | +0.0072 ± 0.0094 | 0.6153 | 0.5998 | 0.5248 | 0.4006 | 0.4354 | -0.074 ± 0.0371 | -0.0633 (3) |
| 15-25 | 188 | 0.2145 | 0.2097 | +0.0048 ± 0.0131 | 0.6166 | 0.6005 | 0.5615 | 0.3651 | 0.4521 | -0.027 ± 0.0325 | -0.02 (4) |
| 25-40 | 90 | 0.2352 | 0.181 | +0.0542 ± 0.0277 | 0.6592 | 0.5337 | 0.6174 | 0.3041 | 0.3667 | -0.077 ± 0.0423 | -0.01 (1) |
| 40+ | 26 | 0.3509 | 0.1453 | +0.2057 ± 0.0675 | 0.9495 | 0.453 | 0.7195 | 0.2762 | 0.2692 | -0.176 ± 0.0753 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 440 | 0.1655 | 0.1665 | -0.0011 ± 0.0007 | 0.4973 | 0.5 | 0.5082 | 0.4934 | 0.5318 | -0.024 ± 0.0204 | -0.0188 (8) |
| 3-5 | 274 | 0.1776 | 0.1773 | +0.0003 ± 0.0021 | 0.5365 | 0.5292 | 0.497 | 0.4568 | 0.4745 | -0.041 ± 0.0262 | 0.02 (1) |
| 5-10 | 630 | 0.1838 | 0.1819 | +0.0019 ± 0.0025 | 0.5474 | 0.5396 | 0.4748 | 0.4011 | 0.427 | -0.033 ± 0.0171 | -0.0129 (7) |
| 10-15 | 513 | 0.1952 | 0.1772 | +0.0180 ± 0.0046 | 0.5722 | 0.5189 | 0.478 | 0.3539 | 0.3431 | -0.073 ± 0.0184 | -0.0633 (3) |
| 15-25 | 694 | 0.1937 | 0.1583 | +0.0354 ± 0.006 | 0.5751 | 0.4699 | 0.4806 | 0.283 | 0.2896 | -0.051 ± 0.0148 | -0.017 (10) |
| 25-40 | 623 | 0.2128 | 0.0955 | +0.1173 ± 0.0077 | 0.6181 | 0.3123 | 0.5037 | 0.1893 | 0.1621 | -0.074 ± 0.0121 | -0.01 (1) |
| 40+ | 461 | 0.3718 | 0.0353 | +0.3365 ± 0.0095 | 0.9689 | 0.1508 | 0.6179 | 0.104 | 0.0434 | -0.092 ± 0.0081 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 88 | 0.1784 | 0.1802 | -0.0018 ± 0.0015 | 0.5303 | 0.533 | 0.5325 | 0.5177 | 0.5795 | -0.029 ± 0.044 | -0.01 (1) |
| 3-5 | 67 | 0.2138 | 0.2119 | +0.0019 ± 0.0045 | 0.609 | 0.6116 | 0.4989 | 0.4598 | 0.4478 | -0.085 ± 0.0591 | 0.02 (1) |
| 5-10 | 173 | 0.1851 | 0.1808 | +0.0043 ± 0.005 | 0.5518 | 0.5394 | 0.5729 | 0.4969 | 0.4971 | -0.104 ± 0.0328 | -0.01 (4) |
| 10-15 | 155 | 0.2236 | 0.2113 | +0.0123 ± 0.0094 | 0.6363 | 0.6093 | 0.5757 | 0.451 | 0.471 | -0.080 ± 0.0379 | -0.0667 (3) |
| 15-25 | 209 | 0.2231 | 0.1937 | +0.0294 ± 0.0121 | 0.631 | 0.5624 | 0.5825 | 0.3853 | 0.4163 | -0.091 ± 0.031 | -0.0167 (3) |
| 25-40 | 126 | 0.253 | 0.1958 | +0.0573 ± 0.0243 | 0.7065 | 0.5672 | 0.6571 | 0.3465 | 0.4048 | -0.089 ± 0.0404 | -0.025 (2) |
| 40+ | 54 | 0.3802 | 0.1959 | +0.1843 ± 0.0606 | 1.0546 | 0.5767 | 0.7524 | 0.2608 | 0.3333 | -0.055 ± 0.0597 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 348 | 0.1601 | 0.1621 | -0.0020 ± 0.0007 | 0.4816 | 0.487 | 0.5556 | 0.5409 | 0.5948 | +0.002 ± 0.0217 | -0.0217 (6) |
| 3-5 | 218 | 0.1783 | 0.1752 | +0.0032 ± 0.0022 | 0.5272 | 0.5253 | 0.547 | 0.5076 | 0.4862 | -0.070 ± 0.0284 | 0.02 (1) |
| 5-10 | 570 | 0.1771 | 0.1753 | +0.0018 ± 0.0027 | 0.5302 | 0.5198 | 0.5196 | 0.4442 | 0.4667 | -0.035 ± 0.0176 | -0.01 (5) |
| 10-15 | 526 | 0.19 | 0.1756 | +0.0144 ± 0.0046 | 0.5636 | 0.5184 | 0.5151 | 0.3909 | 0.403 | -0.046 ± 0.0185 | -0.0575 (4) |
| 15-25 | 719 | 0.2074 | 0.1565 | +0.0509 ± 0.0059 | 0.6031 | 0.4694 | 0.5126 | 0.3162 | 0.2907 | -0.092 ± 0.0147 | -0.0143 (7) |
| 25-40 | 675 | 0.2227 | 0.118 | +0.1048 ± 0.0084 | 0.6472 | 0.3655 | 0.5448 | 0.2293 | 0.2222 | -0.062 ± 0.0134 | -0.015 (6) |
| 40+ | 579 | 0.403 | 0.0606 | +0.3423 ± 0.0119 | 1.0581 | 0.2198 | 0.6617 | 0.1239 | 0.0881 | -0.069 ± 0.0098 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 137 | 0.1811 | 0.1829 | -0.0018 ± 0.0013 | 0.5332 | 0.538 | 0.5199 | 0.5055 | 0.5401 | -0.050 ± 0.0369 | -0.01 (5) |
| 3-5 | 100 | 0.1705 | 0.168 | +0.0026 ± 0.0033 | 0.5146 | 0.5084 | 0.5 | 0.4606 | 0.45 | -0.113 ± 0.0434 | -- (0) |
| 5-10 | 178 | 0.2062 | 0.205 | +0.0012 ± 0.0051 | 0.6039 | 0.5947 | 0.5064 | 0.4338 | 0.4607 | -0.068 ± 0.0342 | -0.01 (3) |
| 10-15 | 153 | 0.2111 | 0.2077 | +0.0034 ± 0.0092 | 0.6083 | 0.5972 | 0.5511 | 0.4273 | 0.4837 | -0.065 ± 0.0371 | -0.044 (5) |
| 15-25 | 185 | 0.2115 | 0.2016 | +0.0099 ± 0.0128 | 0.6139 | 0.5837 | 0.5767 | 0.3837 | 0.4541 | -0.044 ± 0.0317 | -0.03 (1) |
| 25-40 | 98 | 0.234 | 0.1909 | +0.0431 ± 0.0273 | 0.6598 | 0.5596 | 0.6078 | 0.2947 | 0.3776 | -0.064 ± 0.0409 | 0.0 (1) |
| 40+ | 21 | 0.3707 | 0.1604 | +0.2102 ± 0.0791 | 0.9917 | 0.4892 | 0.7365 | 0.2879 | 0.2857 | -0.191 ± 0.0908 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 414 | 0.1717 | 0.172 | -0.0002 ± 0.0007 | 0.5128 | 0.5139 | 0.5103 | 0.4958 | 0.5097 | -0.046 ± 0.0205 | -0.0162 (13) |
| 3-5 | 298 | 0.1787 | 0.1737 | +0.0050 ± 0.0019 | 0.533 | 0.5193 | 0.487 | 0.4477 | 0.4094 | -0.098 ± 0.0244 | -0.01 (2) |
| 5-10 | 622 | 0.1927 | 0.1861 | +0.0066 ± 0.0026 | 0.5699 | 0.5441 | 0.4685 | 0.3947 | 0.3891 | -0.060 ± 0.0174 | -0.01 (3) |
| 10-15 | 530 | 0.1892 | 0.1728 | +0.0164 ± 0.0045 | 0.5602 | 0.5119 | 0.4889 | 0.3651 | 0.3623 | -0.067 ± 0.018 | -0.03 (9) |
| 15-25 | 734 | 0.1851 | 0.1497 | +0.0354 ± 0.0057 | 0.5578 | 0.4507 | 0.4906 | 0.2919 | 0.3025 | -0.046 ± 0.014 | -0.03 (2) |
| 25-40 | 601 | 0.2139 | 0.0963 | +0.1176 ± 0.008 | 0.6204 | 0.3123 | 0.4971 | 0.1798 | 0.1547 | -0.076 ± 0.0122 | 0.0 (1) |
| 40+ | 436 | 0.3889 | 0.035 | +0.3539 ± 0.0098 | 1.0153 | 0.1517 | 0.6242 | 0.1043 | 0.0344 | -0.101 ± 0.0083 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 423 | 0.205 | 0.2051 | -0.0001 ± 0.0007 | 0.5926 | 0.5931 | 0.5006 | 0.4859 | 0.4894 | -0.040 ± 0.0221 | -0.0226 (46) |
| 3-5 | 306 | 0.1937 | 0.1923 | +0.0015 ± 0.002 | 0.5691 | 0.562 | 0.4624 | 0.4226 | 0.4281 | -0.044 ± 0.0249 | -0.0059 (32) |
| 5-10 | 646 | 0.1889 | 0.1841 | +0.0048 ± 0.0025 | 0.5614 | 0.5483 | 0.4606 | 0.3871 | 0.3932 | -0.039 ± 0.0169 | -0.005 (72) |
| 10-15 | 428 | 0.2037 | 0.1914 | +0.0124 ± 0.0053 | 0.5968 | 0.5614 | 0.4603 | 0.3366 | 0.3481 | -0.039 ± 0.021 | 0.0016 (63) |
| 15-25 | 575 | 0.2337 | 0.2088 | +0.0249 ± 0.0074 | 0.6604 | 0.604 | 0.5298 | 0.3367 | 0.3687 | -0.031 ± 0.019 | -0.0216 (58) |
| 25-40 | 274 | 0.2689 | 0.1707 | +0.0982 ± 0.0156 | 0.7429 | 0.5118 | 0.577 | 0.2657 | 0.2628 | -0.068 ± 0.0246 | -0.0216 (25) |
| 40+ | 94 | 0.4254 | 0.1611 | +0.2643 ± 0.0443 | 1.1952 | 0.4956 | 0.7368 | 0.2289 | 0.2447 | -0.060 ± 0.0429 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 779 | 0.1944 | 0.1939 | +0.0005 ± 0.0005 | 0.5672 | 0.5658 | 0.4952 | 0.4807 | 0.4698 | -0.052 ± 0.0158 | -0.0155 (82) |
| 3-5 | 549 | 0.1972 | 0.1952 | +0.0020 ± 0.0015 | 0.5743 | 0.5666 | 0.4675 | 0.4277 | 0.4244 | -0.048 ± 0.0189 | -0.018 (54) |
| 5-10 | 1175 | 0.1875 | 0.1808 | +0.0067 ± 0.0019 | 0.5581 | 0.5382 | 0.4457 | 0.3717 | 0.3677 | -0.045 ± 0.0125 | -0.0089 (122) |
| 10-15 | 862 | 0.1981 | 0.1838 | +0.0143 ± 0.0037 | 0.5826 | 0.5416 | 0.4512 | 0.3276 | 0.3318 | -0.041 ± 0.0145 | -0.0053 (99) |
| 15-25 | 1202 | 0.2214 | 0.1863 | +0.0351 ± 0.0049 | 0.638 | 0.5473 | 0.5039 | 0.3084 | 0.3161 | -0.043 ± 0.0125 | -0.0255 (106) |
| 25-40 | 826 | 0.2448 | 0.1283 | +0.1165 ± 0.0079 | 0.691 | 0.401 | 0.5285 | 0.2132 | 0.1877 | -0.071 ± 0.0123 | -0.0206 (47) |
| 40+ | 491 | 0.389 | 0.0789 | +0.3101 ± 0.0139 | 1.0628 | 0.2654 | 0.6527 | 0.1368 | 0.1059 | -0.074 ± 0.0129 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 872 | 1.108 ± 0.096 | 1.219 | 0.1715 | 0.1836 | 0.2078 | 0.1943 |
| gen2 | 872 | 0.942 ± 0.086 | 1.151 | 0.188 | 0.1828 | 0.2245 | 0.1947 |
| gen1_elo | 872 | 1.086 ± 0.094 | 1.199 | 0.1767 | 0.184 | 0.2072 | 0.1944 |
| gen1_sr | 872 | 1.142 ± 0.111 | 1.212 | 0.144 | 0.1852 | 0.2202 | 0.1942 |
| gen1_ledger | 2746 | 0.885 ± 0.051 | 1.058 | 0.1625 | 0.1994 | 0.2197 | 0.1924 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 4,808)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,615 | 33.6% |
| STALE_QUOTE | market_freshness | 1,409 | 29.3% |
| POOR_DATA | data | 380 | 7.9% |
| BOOK_QUALITY | execution | 314 | 6.5% |
| LIMITED_DATA | data | 302 | 6.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 281 | 5.8% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 240 | 5.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 167 | 3.5% |
| IDENTITY_AMBIGUOUS | mapping | 95 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 5 | 0.1% |

Cause class: coverage 33.6%, market_freshness 29.3%, data 14.2%, market_freshness/coverage 9.3%, execution 6.5%, model_calibration_or_unknown 5.0%, mapping 2.0%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 94.3%, LOW_DATA_QUALITY 63.8%, STALE_KALSHI_QUOTE 62.9%, STALE_PLAYER_DATA 54.0%, THIN_PLAYER_HISTORY 51.5%, MODEL_INTERNAL_DISAGREEMENT 32.9%, ASYMMETRIC_SAMPLE_SIZE 27.9%, WIDE_SPREAD 14.6%, MODEL_HIGH_UNCERTAINTY 13.8%, PLAYER_IDENTITY_RISK 10.7%, LEVEL_TRANSFER_RISK 8.3%, EVENT_MAPPING_RISK 6.7%, LOW_DISPLAYED_LIQUIDITY 4.9%, MODEL_CALIBRATION_OUTLIER 2.2%, UNKNOWN 0.8%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.2%, POST_SETTLEMENT_OBSERVATION 33.6%, POSSIBLE_IN_PLAY_QUOTE 6.7%, CONFIRMED_IN_PLAY_QUOTE 1.2%

### >= ge_25 pp (N = 2,639)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,252 | 47.4% |
| STALE_QUOTE | market_freshness | 624 | 23.6% |
| POOR_DATA | data | 165 | 6.2% |
| BOOK_QUALITY | execution | 150 | 5.7% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 142 | 5.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 100 | 3.8% |
| LIMITED_DATA | data | 83 | 3.1% |
| IDENTITY_AMBIGUOUS | mapping | 69 | 2.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 54 | 2.1% |

Cause class: coverage 47.4%, market_freshness 23.6%, data 9.4%, market_freshness/coverage 9.2%, execution 5.7%, mapping 2.6%, model_calibration_or_unknown 2.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 96.7%, STALE_KALSHI_QUOTE 70.1%, LOW_DATA_QUALITY 67.6%, THIN_PLAYER_HISTORY 53.9%, STALE_PLAYER_DATA 51.8%, MODEL_INTERNAL_DISAGREEMENT 33.7%, ASYMMETRIC_SAMPLE_SIZE 30.2%, MODEL_HIGH_UNCERTAINTY 15.0%, PLAYER_IDENTITY_RISK 13.3%, WIDE_SPREAD 13.2%, EVENT_MAPPING_RISK 8.2%, LEVEL_TRANSFER_RISK 7.8%, LOW_DISPLAYED_LIQUIDITY 5.4%, MODEL_CALIBRATION_OUTLIER 3.2%, UNKNOWN 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 50.2%, POST_SETTLEMENT_OBSERVATION 47.4%, POSSIBLE_IN_PLAY_QUOTE 6.3%, CONFIRMED_IN_PLAY_QUOTE 1.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 2255, "IDENTITY_AMBIGUOUS": 384}; ticker orientation: {"VERIFIED": 2639}.

Checks: discipline:AMBIGUOUS 183, discipline:PASS 2456, identity_confidence:AMBIGUOUS 352, identity_confidence:PASS 2287, level_mapping:NA 195, level_mapping:PASS 2444, market_pair:AMBIGUOUS 62, market_pair:NA 75, market_pair:PASS 2502, model_complement:NA 46, model_complement:PASS 2593, namesake:PASS 2639, physical_match_id:NA 1344, physical_match_id:PASS 1295, player_ids:PASS 2639, same_pair_other_event:PASS 2639, ticker_orientation:PASS 2639

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 314 | 4.1% | 4.3% | 0.5% | {"market_freshness": 12, "execution": 1} | 6.16 | 0.1791 / 0.1823 (49) | 39.2% | 0.0% | 0.6% | 3.5% |
| CHALLENGER | 1,680 | 18.9% | 8.2% | 12.0% | {"coverage": 173, "market_freshness": 74, "market_freshness/coverage": 39, "data": 17, "model_calibration_or_unknown": 12, "execution": 3} | 7.84 | 0.2253 / 0.2076 (540) | 52.1% | 3.9% | 0.7% | 22.6% |
| DOUBLES | 382 | 47.9% | 47.8% | 6.9% | {"market_freshness": 106, "execution": 32, "mapping": 27, "market_freshness/coverage": 12, "coverage": 6} | 23.94 | 0.3237 / 0.228 (160) | 61.0% | 0.0% | 100.0% | 9.7% |
| ITF_MEN | 3,675 | 24.9% | 13.5% | 34.7% | {"coverage": 511, "market_freshness": 163, "data": 89, "execution": 71, "market_freshness/coverage": 70, "mapping": 10, "model_calibration_or_unknown": 1} | 9.73 | 0.213 / 0.1875 (1315) | 55.3% | 49.1% | 5.2% | 32.4% |
| ITF_WOMEN | 3,641 | 28.9% | 17.3% | 39.9% | {"coverage": 549, "market_freshness": 222, "data": 123, "market_freshness/coverage": 81, "execution": 34, "mapping": 30, "model_calibration_or_unknown": 15} | 12.36 | 0.2068 / 0.1868 (1164) | 58.2% | 53.8% | 6.2% | 32.7% |
| OTHER | 149 | 8.1% | 7.3% | 0.4% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 798 | 9.4% | 8.1% | 2.8% | {"market_freshness": 34, "model_calibration_or_unknown": 12, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.66 | 0.2006 / 0.1964 (129) | 40.5% | 2.6% | 1.5% | 3.8% |
| WTA125 | 421 | 16.4% | 9.1% | 2.6% | {"market_freshness/coverage": 30, "model_calibration_or_unknown": 12, "market_freshness": 11, "data": 8, "coverage": 8} | 10.39 | 0.2261 / 0.2035 (219) | 34.4% | 9.0% | 0.5% | 19.2% |

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
| 8 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
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
| 25 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 230 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 26 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.2h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 141 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 27 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 28 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 29 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 156 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 30 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 31 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 32 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 33 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 34 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 114 min (STALE); data LIMITED (grade B, thinner serve sample 2163.0, ratio 2.0); no external reference |
| 36 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 183 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 37 | `KXWTAMATCH-26OCT01YASCHW-CHW` | WTA | fair_v1 | 73% / 2% | +70 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 51 min (STALE); no external reference |
| 38 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 39 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 40 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 41 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |
| 42 | `KXITFWMATCH-26SEP30KOKUEM-KOK` | ITF_WOMEN | fair_v1 | 79% / 10% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 776 min (STALE); data LIMITED (grade C, thinner serve sample 824.0, ratio 2.35); no external reference |
| 43 | `KXITFMATCH-26SEP20WILRAH-RAH` | ITF_MEN | gen1_ledger | 72% / 4% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade B, thinner serve sample 2782.0, ratio 1.84); no external reference |
| 44 | `KXITFMATCH-26SEP26NAGTHO-NAG` | ITF_MEN | gen1_ledger | 76% / 7% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 89 min (STALE); data LIMITED (grade C, thinner serve sample 1323.0, ratio 4.45); no external reference |
| 45 | `KXITFWMATCH-26SEP26PERPRE-PER` | ITF_WOMEN | gen1_ledger | 78% / 10% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 102 min (STALE); data POOR (grade D, thinner serve sample 1020.0, ratio 2.77); no external reference |
| 46 | `KXITFMATCH-26SEP22YILAGA-AGA` | ITF_MEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 203 min (STALE); data LIMITED (grade B, thinner serve sample 2786.0, ratio 2.08); no external reference |
| 47 | `KXITFMATCH-26SEP30DIMURA-URA` | ITF_MEN | fair_v1 | 71% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.5h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 819 min (STALE); data POOR (grade F, thinner serve sample 174.0, ratio 2.63); no external reference |
| 48 | `KXITFWMATCH-26OCT01TANVED-TAN` | ITF_WOMEN | fair_v1 | 76% / 8% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 8.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 492 min (STALE); no external reference |
| 49 | `KXITFWMATCH-26SEP20LLIBON-BON` | ITF_WOMEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 69 min (STALE); data POOR (grade D, thinner serve sample 1210.0, ratio 3.0); no external reference |
| 50 | `KXATPCHALLENGERDOUBLES-26SEP17ARESTEBLASCH-BLASCH` | DOUBLES | gen1_ledger | 95% / 28% | +67 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 79 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9665, "by_level_share_of_ge_25pp": {"ATP": 0.0049, "CHALLENGER": 0.1205, "DOUBLES": 0.0693, "ITF_MEN": 0.3467, "ITF_WOMEN": 0.3994, "OTHER": 0.0045, "WTA": 0.0284, "WTA125": 0.0261}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.701, "share_primary_cause_market_settled_or_in_play": 0.5661, "share_primary_cause_stale_quote_only": 0.2365}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 2639, "identity_ambiguous_share": 0.1455, "ticker_orientation": {"VERIFIED": 2639}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 1295, "with_external": 6, "coverage": 0.0046, "external_status": {"EXTERNAL_STALE": 6}, "triangulation": {"INSUFFICIENT_INPUTS": 6}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 501, "with_external": 6, "coverage": 0.012, "external_status": {"EXTERNAL_STALE": 6}, "triangulation": {"INSUFFICIENT_INPUTS": 6}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 824.0, "median_sample_ratio": 2.25, "median_min_matches": 28.0, "median_max_days_since_last": 172.0, "share_severe_asymmetry": 0.1637, "data_status": {"POOR": 1216, "LIMITED": 900, "ADEQUATE": 523}, "comparison_lt_10pp": {"median_thinner_serve_points": 2005.0, "median_sample_ratio": 1.71, "median_min_matches": 80.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 195, "model_minus_observed": 0.1007, "kalshi_minus_observed": -0.0324, "brier_diff_model_minus_kalshi": 0.0135}, "4-10x": {"n": 140, "model_minus_observed": 0.0998, "kalshi_minus_observed": -0.0362, "brier_diff_model_minus_kalshi": 0.0121}, "<2x": {"n": 401, "model_minus_observed": 0.0727, "kalshi_minus_observed": -0.0462, "brier_diff_model_minus_kalshi": 0.0117}, ">=10x": {"n": 136, "model_minus_observed": 0.097, "kalshi_minus_observed": -0.0641, "brier_diff_model_minus_kalshi": 0.0197}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 872, "model": {"intercept": -0.641, "slope": 0.942, "slope_se": 0.086}, "kalshi_mid_same_rows": {"intercept": 0.187, "slope": 1.151, "slope_se": 0.094}, "mean_extremity_model": 0.188, "mean_extremity_kalshi": 0.1828, "model_brier": 0.2245, "kalshi_brier": 0.1947, "brier_diff_model_minus_kalshi": 0.0297, "brier_diff_se": 0.0064, "model_logloss": 0.6415, "kalshi_logloss": 0.5686}, "fair_v1": {"n": 872, "model": {"intercept": -0.437, "slope": 1.108, "slope_se": 0.096}, "kalshi_mid_same_rows": {"intercept": 0.307, "slope": 1.219, "slope_se": 0.098}, "mean_extremity_model": 0.1715, "mean_extremity_kalshi": 0.1836, "model_brier": 0.2078, "kalshi_brier": 0.1943, "brier_diff_model_minus_kalshi": 0.0134, "brier_diff_se": 0.005, "model_logloss": 0.6007, "kalshi_logloss": 0.5676}, "gen1_elo": {"n": 872, "model": {"intercept": -0.433, "slope": 1.086, "slope_se": 0.094}, "kalshi_mid_same_rows": {"intercept": 0.293, "slope": 1.199, "slope_se": 0.096}, "mean_extremity_model": 0.1767, "mean_extremity_kalshi": 0.184, "model_brier": 0.2072, "kalshi_brier": 0.1944, "brier_diff_model_minus_kalshi": 0.0129, "brier_diff_se": 0.005, "model_logloss": 0.6011, "kalshi_logloss": 0.5675}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2587, "share_ge_15": 0.4455, "median_abs_gap": 13.05, "n": 5006}, "gen1_elo": {"share_ge_25": 0.2517, "share_ge_15": 0.4333, "median_abs_gap": 12.51, "n": 5006}, "gen1_sr": {"share_ge_25": 0.31, "share_ge_15": 0.5336, "median_abs_gap": 16.39, "n": 5006}, "gen2": {"share_ge_25": 0.3094, "share_ge_15": 0.512, "median_abs_gap": 15.54, "n": 5006}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1396, "share_ge_15": 0.3309, "median_abs_gap": 10.02, "n": 3590}, "gen1_elo": {"share_ge_25": 0.1404, "share_ge_15": 0.3125, "median_abs_gap": 9.51, "n": 3590}, "gen1_sr": {"share_ge_25": 0.1958, "share_ge_15": 0.4343, "median_abs_gap": 12.73, "n": 3590}, "gen2": {"share_ge_25": 0.2092, "share_ge_15": 0.4284, "median_abs_gap": 12.85, "n": 3590}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 6.16, "share_ge_25_all": 0.0414, "share_ge_25_pregame_clean": 0.0429}, "WTA": {"median_abs_gap_pregame_clean": 8.66, "share_ge_25_all": 0.094, "share_ge_25_pregame_clean": 0.0807}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2224, "share_within_10pp_all": 0.4162, "share_within_10pp_pregame_clean": 0.4977, "corr_model_vs_mid_pregame_clean": 0.8283}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 145, "model_brier": 0.1764, "kalshi_brier": 0.1771, "brier_diff_model_minus_kalshi": -0.0007}, "10-15": {"n_settled": 147, "model_brier": 0.216, "kalshi_brier": 0.2088, "brier_diff_model_minus_kalshi": 0.0072}, "15-25": {"n_settled": 188, "model_brier": 0.2145, "kalshi_brier": 0.2097, "brier_diff_model_minus_kalshi": 0.0048}, "25-40": {"n_settled": 90, "model_brier": 0.2352, "kalshi_brier": 0.181, "brier_diff_model_minus_kalshi": 0.0542}, "3-5": {"n_settled": 91, "model_brier": 0.1761, "kalshi_brier": 0.1748, "brier_diff_model_minus_kalshi": 0.0012}, "40+": {"n_settled": 26, "model_brier": 0.3509, "kalshi_brier": 0.1453, "brier_diff_model_minus_kalshi": 0.2057}, "5-10": {"n_settled": 185, "model_brier": 0.201, "kalshi_brier": 0.2036, "brier_diff_model_minus_kalshi": -0.0026}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.562, "slope": 0.885, "slope_se": 0.051}, "kalshi_slope": {"intercept": 0.085, "slope": 1.058, "slope_se": 0.053}, "n": 2746}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 160, "model_brier": 0.3237, "kalshi_brier": 0.228, "brier_diff_model_minus_kalshi": 0.0957, "brier_diff_se": 0.026, "corr_model_outcome": -0.0918, "corr_kalshi_outcome": 0.3335}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
