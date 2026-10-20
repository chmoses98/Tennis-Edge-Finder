# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-20T05:41Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 43,035): 0-3 14.3%, 3-5 9.6%, 5-10 19.9%, 10-15 15.4%, 15-25 19.2%, 25-40 13.8%, 40+ 7.9%; median gap 11.91 pp.
* **Where the extremes live**: 97.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 75.5%, Challenger 12.5%, doubles 7.1%). Main tour: ATP 4.5% and WTA 4.6% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 9,321): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.0%, BOOK_QUALITY 19.5%, STALE_QUOTE 17.9%, POOR_DATA 9.1%, POSSIBLY_IN_PLAY_QUOTE 5.2%, IDENTITY_AMBIGUOUS 4.5%, LIMITED_DATA 3.8%, IN_PLAY_QUOTE 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.6%. By class: coverage 34.0%, execution 19.5%, market_freshness 17.9%, data 12.9%, market_freshness/coverage 8.4%, mapping 4.5%, model_calibration_or_unknown 2.2%, model_calibration 0.6%.
* **Stale / settled / in-play**: 50.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.4% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 9,321 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.5%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 24.2% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 510.0 points vs 1765.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.059, Gen-2 0.853, Gen-1 ledger 0.882 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 438 model 0.2236 vs Kalshi 0.2081; n 87 model 0.297 vs Kalshi 0.1766.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 182,889 model-market comparisons (296,925 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 64,098 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-20T05:29:41.026356+00:00'], shadow board 47,851 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-20T05:29:44.398774+00:00'], Model 4 22,670 rows, 16,941 settled tickers, 5,850 tickers with an external scan.
* By model: {"gen1_ledger": 43259, "gen1_elo": 24057, "fair_v1": 24057, "gen2": 24057, "gen1_sr": 24057, "model4_fundamental": 21710, "model4_conditioned": 21692}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 43,035 | 14.3 | 9.6 | 19.9 | 15.4 | 19.2 | 13.8 | 7.9 | 11.91 | 40.9% | 21.7% |
| MW fair_v1 | 24,057 | 13.3 | 8.7 | 18.4 | 15.8 | 19.8 | 14.6 | 9.4 | 12.99 | 43.8% | 24.0% |
| MW gen1_elo | 24,057 | 13.1 | 8.9 | 19.4 | 15.2 | 19.7 | 14.5 | 9.1 | 12.66 | 43.4% | 23.6% |
| MW gen1_ledger | 18,978 | 15.5 | 10.7 | 21.6 | 14.9 | 18.5 | 12.8 | 6.0 | 10.53 | 37.2% | 18.7% |
| MW gen1_sr | 24,057 | 10.0 | 7.3 | 16.8 | 14.2 | 21.4 | 18.4 | 11.8 | 15.6 | 51.7% | 30.2% |
| MW gen2 | 24,057 | 11.3 | 7.4 | 16.4 | 14.3 | 20.1 | 17.6 | 13.0 | 15.37 | 50.7% | 30.6% |
| all families model4_conditioned | 21,692 | 21.9 | 19.1 | 34.4 | 17.5 | 4.6 | 1.4 | 1.0 | 5.93 | 7.0% | 2.4% |
| all families model4_fundamental | 21,710 | 16.2 | 13.0 | 34.2 | 20.5 | 11.3 | 3.4 | 1.3 | 7.9 | 16.0% | 4.7% |

Configurable thresholds (primary): >=5pp 76.2%, >=10pp 56.3%, >=15pp 40.9%, >=20pp 30.2%, >=25pp 21.7%, >=30pp 15.5%, >=40pp 7.9%, >=50pp 3.5%
Executable gap (model outside the book, before fees): median 8.3pp; >=10pp 44.7%, >=25pp 16.7%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,117 | 28.5 | 13.9 | 25.0 | 15.8 | 11.5 | 4.7 | 0.6 | 6.21 | 16.8% | 5.3% |
| CHALLENGER | 4,052 | 15.5 | 10.2 | 20.3 | 16.1 | 14.7 | 12.3 | 10.8 | 11.17 | 37.9% | 23.1% |
| ITF_MEN | 6,329 | 10.9 | 7.8 | 17.1 | 14.7 | 20.6 | 16.6 | 12.2 | 14.84 | 49.5% | 28.8% |
| ITF_WOMEN | 9,421 | 9.9 | 6.9 | 15.8 | 15.6 | 23.1 | 18.1 | 10.8 | 15.61 | 51.9% | 28.8% |
| WTA | 1,478 | 17.7 | 12.5 | 24.0 | 19.8 | 21.0 | 4.3 | 0.7 | 8.65 | 26.0% | 5.0% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,117 | 23.4 | 15.3 | 24.6 | 17.1 | 13.8 | 5.0 | 0.8 | 6.72 | 19.7% | 5.9% |
| CHALLENGER | 4,052 | 14.7 | 8.4 | 18.8 | 14.4 | 18.0 | 14.0 | 11.8 | 12.7 | 43.8% | 25.8% |
| ITF_MEN | 6,329 | 9.2 | 6.5 | 15.3 | 13.4 | 19.7 | 20.0 | 15.9 | 17.5 | 55.5% | 35.9% |
| ITF_WOMEN | 9,421 | 8.3 | 5.6 | 13.6 | 13.7 | 21.6 | 20.8 | 16.5 | 18.8 | 58.8% | 37.3% |
| WTA | 1,478 | 14.8 | 9.5 | 19.9 | 16.0 | 24.4 | 14.6 | 0.8 | 11.71 | 39.8% | 15.4% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,117 | 23.8 | 13.5 | 25.0 | 16.2 | 14.8 | 5.7 | 0.9 | 7.05 | 21.4% | 6.6% |
| CHALLENGER | 4,052 | 14.4 | 9.8 | 21.3 | 15.2 | 15.9 | 12.3 | 11.2 | 11.19 | 39.4% | 23.5% |
| ITF_MEN | 6,329 | 10.1 | 7.9 | 17.4 | 14.0 | 21.4 | 17.0 | 12.2 | 15.16 | 50.6% | 29.2% |
| ITF_WOMEN | 9,421 | 9.5 | 6.9 | 16.3 | 15.8 | 23.3 | 18.3 | 9.9 | 15.57 | 51.6% | 28.3% |
| WTA | 1,478 | 24.7 | 16.6 | 30.0 | 15.6 | 10.3 | 2.3 | 0.5 | 6.0 | 13.1% | 2.8% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,216 | 26.9 | 20.1 | 29.9 | 11.9 | 8.0 | 2.9 | 0.2 | 5.31 | 11.1% | 3.1% |
| CHALLENGER | 2,844 | 21.5 | 14.7 | 27.1 | 14.0 | 14.6 | 6.2 | 1.9 | 7.2 | 22.7% | 8.1% |
| DOUBLES | 1,361 | 4.5 | 4.1 | 11.3 | 10.6 | 20.9 | 26.2 | 22.5 | 24.11 | 69.5% | 48.6% |
| ITF_MEN | 5,307 | 14.2 | 8.7 | 20.7 | 15.9 | 20.6 | 13.1 | 6.8 | 11.91 | 40.5% | 19.9% |
| ITF_WOMEN | 6,370 | 12.1 | 8.9 | 19.1 | 15.3 | 21.9 | 16.6 | 6.1 | 13.11 | 44.6% | 22.7% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 999 | 22.3 | 15.9 | 29.1 | 18.2 | 10.4 | 3.7 | 0.3 | 6.94 | 14.4% | 4.0% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,075 | 28.7 | 14.0 | 25.3 | 15.6 | 11.4 | 4.5 | 0.6 | 6.17 | 16.4% | 5.1% |
| CHALLENGER | 2,889 | 20.2 | 12.6 | 25.1 | 18.5 | 15.1 | 6.5 | 1.9 | 8.36 | 23.5% | 8.4% |
| ITF_MEN | 4,657 | 13.4 | 9.6 | 20.3 | 16.5 | 21.1 | 13.7 | 5.5 | 11.94 | 40.3% | 19.2% |
| ITF_WOMEN | 7,115 | 11.6 | 8.2 | 17.8 | 17.6 | 24.7 | 15.3 | 4.8 | 13.43 | 44.9% | 20.2% |
| WTA | 1,439 | 17.9 | 12.2 | 23.9 | 19.9 | 21.1 | 4.2 | 0.8 | 8.74 | 26.1% | 5.0% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,075 | 23.5 | 15.5 | 24.6 | 17.1 | 13.7 | 4.9 | 0.7 | 6.63 | 19.3% | 5.6% |
| CHALLENGER | 2,889 | 18.4 | 10.7 | 23.4 | 17.3 | 18.4 | 9.5 | 2.4 | 9.46 | 30.2% | 11.9% |
| ITF_MEN | 4,658 | 10.8 | 7.8 | 17.6 | 15.1 | 21.7 | 17.9 | 9.1 | 14.52 | 48.8% | 27.1% |
| ITF_WOMEN | 7,115 | 9.2 | 6.4 | 14.8 | 15.1 | 23.6 | 20.3 | 10.6 | 16.7 | 54.5% | 30.9% |
| WTA | 1,439 | 14.7 | 9.5 | 19.8 | 15.9 | 24.5 | 14.7 | 0.8 | 11.75 | 40.0% | 15.6% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,178 | 27.1 | 20.4 | 30.1 | 12.1 | 7.5 | 2.7 | 0.1 | 5.27 | 10.3% | 2.8% |
| CHALLENGER | 2,481 | 23.0 | 15.8 | 28.9 | 13.8 | 14.0 | 4.0 | 0.6 | 6.6 | 18.5% | 4.5% |
| DOUBLES | 1,265 | 4.5 | 4.3 | 11.5 | 10.8 | 20.8 | 26.3 | 21.9 | 24.05 | 69.0% | 48.2% |
| ITF_MEN | 4,437 | 15.5 | 9.5 | 22.5 | 16.7 | 20.3 | 11.4 | 4.2 | 10.77 | 35.9% | 15.6% |
| ITF_WOMEN | 5,329 | 12.9 | 9.4 | 20.6 | 16.1 | 22.1 | 15.4 | 3.5 | 11.9 | 41.0% | 18.9% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 953 | 22.8 | 16.4 | 29.2 | 18.3 | 10.5 | 2.9 | 0.0 | 6.8 | 13.4% | 2.9% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,361 | 4.5 | 4.1 | 11.3 | 10.6 | 20.9 | 26.2 | 22.5 | 24.11 | 69.5% | 48.6% |
| singles | 17,617 | 16.3 | 11.2 | 22.4 | 15.3 | 18.3 | 11.7 | 4.7 | 10.01 | 34.8% | 16.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 5,443 | 13.4 | 9.0 | 19.5 | 15.8 | 18.4 | 14.6 | 9.3 | 12.6 | 42.2% | 23.8% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 15,380 | 13.7 | 8.6 | 18.4 | 15.5 | 20.1 | 14.3 | 9.4 | 13.0 | 43.8% | 23.7% |
| UNKNOWN | 2,997 | 11.5 | 7.9 | 16.8 | 17.6 | 20.4 | 15.9 | 9.9 | 13.53 | 46.2% | 25.8% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,023 | 19.6 | 11.4 | 21.4 | 17.1 | 16.0 | 8.8 | 5.7 | 9.3 | 30.5% | 14.5% |
| B | 3,103 | 12.9 | 9.2 | 20.2 | 17.1 | 18.5 | 11.8 | 10.4 | 12.01 | 40.7% | 22.2% |
| C | 3,389 | 12.7 | 9.1 | 18.9 | 14.7 | 19.9 | 14.9 | 9.8 | 12.99 | 44.6% | 24.7% |
| D | 3,992 | 12.3 | 8.0 | 17.0 | 15.8 | 22.0 | 15.5 | 9.5 | 13.92 | 46.9% | 24.9% |
| F | 6,550 | 7.8 | 5.6 | 15.1 | 14.5 | 23.1 | 21.3 | 12.6 | 17.82 | 57.0% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,468 | 23.3 | 15.9 | 28.5 | 15.2 | 11.6 | 4.1 | 1.4 | 6.62 | 17.1% | 5.5% |
| B | 2,657 | 15.8 | 10.3 | 24.1 | 16.3 | 19.1 | 10.6 | 3.8 | 9.99 | 33.5% | 14.4% |
| C | 3,755 | 10.9 | 7.3 | 18.1 | 14.5 | 21.9 | 16.4 | 10.9 | 14.53 | 49.1% | 27.2% |
| D | 2,753 | 14.0 | 9.7 | 19.9 | 14.5 | 21.0 | 14.6 | 6.2 | 12.08 | 41.9% | 20.9% |
| F | 4,345 | 10.3 | 7.9 | 15.7 | 14.4 | 22.4 | 20.7 | 8.7 | 15.91 | 51.8% | 29.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 7,960 | 17.9 | 10.3 | 20.7 | 17.0 | 16.4 | 9.5 | 8.1 | 10.28 | 34.0% | 17.6% |
| LIMITED | 5,336 | 14.2 | 10.3 | 20.2 | 15.5 | 19.2 | 13.3 | 7.2 | 11.59 | 39.8% | 20.5% |
| POOR | 10,761 | 9.5 | 6.6 | 15.9 | 15.1 | 22.6 | 18.9 | 11.4 | 16.0 | 52.9% | 30.3% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,688 | 26.8 | 21.2 | 34.8 | 11.6 | 4.1 | 1.4 | 0.2 | 5.17 | 5.7% | 1.6% |
| GAME_SPREAD | 4,115 | 23.3 | 15.5 | 33.5 | 17.1 | 8.2 | 2.3 | 0.3 | 6.49 | 10.7% | 2.5% |
| MATCH_WINNER | 18,978 | 15.5 | 10.7 | 21.6 | 14.9 | 18.5 | 12.8 | 6.0 | 10.53 | 37.2% | 18.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 8,758 | 30.2 | 17.1 | 30.4 | 12.5 | 8.1 | 1.4 | 0.4 | 5.33 | 9.9% | 1.8% |
| TOTAL_GAMES | 6,696 | 7.7 | 9.1 | 36.6 | 29.1 | 11.1 | 3.5 | 2.9 | 9.62 | 17.4% | 6.4% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,589 | 25.4 | 34.7 | 32.3 | 3.7 | 3.2 | 0.6 | 0.2 | 4.45 | 3.9% | 0.7% |
| GAME_SPREAD | 5,196 | 46.1 | 16.9 | 27.0 | 7.4 | 1.7 | 0.6 | 0.2 | 3.4 | 2.6% | 0.9% |
| TOTAL_GAMES | 8,907 | 4.8 | 7.2 | 40.5 | 35.2 | 7.5 | 2.5 | 2.2 | 9.74 | 12.2% | 4.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,592 | 24.4 | 17.9 | 35.7 | 12.1 | 7.2 | 2.5 | 0.3 | 5.79 | 10.0% | 2.8% |
| GAME_SPREAD | 5,199 | 19.2 | 13.3 | 28.5 | 19.9 | 14.2 | 4.0 | 0.9 | 7.95 | 19.1% | 4.9% |
| TOTAL_GAMES | 8,919 | 7.6 | 8.7 | 36.4 | 27.9 | 13.2 | 3.8 | 2.4 | 9.7 | 19.4% | 6.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 24,057 | 43.8% | 24.0% | 12.99 | 35.6% | 15.1% | 10.83 |
| gen1_elo | 24,057 | 43.4% | 23.6% | 12.66 | 34.8% | 15.1% | 10.47 |
| gen1_sr | 24,057 | 51.7% | 30.2% | 15.6 | 44.2% | 21.3% | 13.07 |
| gen2 | 24,057 | 50.7% | 30.6% | 15.37 | 44.3% | 22.9% | 13.07 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 12,842 | 16.0 | 10.5 | 21.2 | 17.4 | 20.2 | 11.5 | 3.2 | 10.65 | 35.0% | 14.8% |
| STALE | 11,215 | 10.3 | 6.6 | 15.2 | 14.1 | 19.3 | 18.0 | 16.4 | 16.96 | 53.8% | 34.5% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 12,446 | 16.7 | 11.3 | 22.7 | 15.1 | 17.5 | 12.0 | 4.8 | 9.82 | 34.3% | 16.8% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 43,035 | 12446 | 16314 | 14275 | 23.6 | 126.0 | 1400.4 |
| ge_15pp | 17,595 | 4271 | 5780 | 7544 | 25.7 | 425.8 | 1380.4 |
| ge_25pp | 9,321 | 2095 | 2487 | 4739 | 31.1 | 571.0 | 1380.4 |
| lt_10pp | 18,795 | 6301 | 7755 | 4739 | 21.7 | 47.5 | 1341.5 |

Current slate `SL-20261020T054148Z-fb05e711`: 673 priced rows, quote age at build {'median': 12.6, 'max': 12.7}, freshness {'AGING': 673}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 12 | 0.0 | 0.0 | 33.3 | 0.0 | 50.0 | 16.7 | 0.0 | 20.33 | 66.7% | 16.7% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,251 | 20.1 | 10.7 | 23.6 | 18.8 | 19.1 | 7.0 | 0.6 | 9.01 | 26.7% | 7.6% |
| KALSHI_LONE_OUTLIER | 14 | 7.1 | 7.1 | 71.4 | 0.0 | 7.1 | 7.1 | 0.0 | 5.35 | 14.3% | 7.1% |
| MARKETS_AGREE | 396 | 68.4 | 31.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.1 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 857 | 0.0 | 2.8 | 34.8 | 28.0 | 24.3 | 9.6 | 0.6 | 12.22 | 34.4% | 10.2% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 24,057 | 3542 (14.7%) | 24.2% | 0.7% | {"EXTERNAL_STALE": 2251, "AGREES_WITH_KALSHI": 857, "ALL_AGREE": 396, "AGREES_WITH_MODEL": 14, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 11, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 10,525 | 906 (8.6%) | 32.6% | 1.1% | {"EXTERNAL_STALE": 601, "AGREES_WITH_KALSHI": 295, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 5,764 | 261 (4.5%) | 33.3% | 1.1% | {"EXTERNAL_STALE": 171, "AGREES_WITH_KALSHI": 87, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,842 | 247 (8.7%) | 34.4% | 1.2% | {"EXTERNAL_STALE": 159, "AGREES_WITH_KALSHI": 85, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 9,725 | 1972 (20.3%) | 16.3% | 0.8% | {"EXTERNAL_STALE": 1226, "ALL_AGREE": 396, "AGREES_WITH_KALSHI": 322, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 12, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 4,625 | 10.8 | 7.9 | 19.5 | 14.8 | 22.0 | 15.3 | 9.6 | 13.82 | 46.9% | 24.9% |
| 4-10x | 3,147 | 11.7 | 8.6 | 18.7 | 15.7 | 20.5 | 15.1 | 9.9 | 13.47 | 45.4% | 24.9% |
| <2x | 12,444 | 15.3 | 9.7 | 18.9 | 16.9 | 18.2 | 12.6 | 8.3 | 11.71 | 39.1% | 20.9% |
| >=10x | 3,841 | 11.2 | 6.5 | 15.3 | 13.5 | 21.7 | 19.5 | 12.2 | 16.35 | 53.5% | 31.8% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 6,134 | 12.7 | 8.5 | 19.8 | 16.3 | 19.7 | 13.2 | 9.8 | 12.69 | 42.7% | 23.0% |
| 300-1000 | 5,270 | 12.0 | 8.9 | 16.8 | 15.7 | 20.9 | 16.1 | 9.6 | 13.82 | 46.6% | 25.6% |
| <300 | 7,424 | 9.0 | 5.9 | 15.5 | 14.6 | 22.8 | 20.1 | 12.1 | 16.89 | 55.0% | 32.2% |
| >=3000 | 5,229 | 21.5 | 12.6 | 22.7 | 17.1 | 14.6 | 6.8 | 4.8 | 8.09 | 26.2% | 11.6% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 711 | 0.5442 | 0.4096 | 0.4951 | +0.049 | -0.086 | 0.0001 ± 0.0056 |
| ratio 4-10x | 487 | 0.5926 | 0.4504 | 0.5154 | +0.077 | -0.065 | 0.0079 ± 0.0072 |
| ratio <2x | 1741 | 0.5378 | 0.4167 | 0.4503 | +0.087 | -0.034 | 0.0121 ± 0.0034 |
| ratio >=10x | 594 | 0.5638 | 0.3895 | 0.4478 | +0.116 | -0.058 | 0.0123 ± 0.0075 |
| thinner_sample 1000-3000 | 977 | 0.5442 | 0.418 | 0.4585 | +0.086 | -0.041 | 0.0095 ± 0.0046 |
| thinner_sample 300-1000 | 844 | 0.5664 | 0.4256 | 0.4988 | +0.068 | -0.073 | 0.0 ± 0.0054 |
| thinner_sample <300 | 1111 | 0.5554 | 0.3924 | 0.4536 | +0.102 | -0.061 | 0.0135 ± 0.0052 |
| thinner_sample >=3000 | 601 | 0.5323 | 0.4391 | 0.4659 | +0.066 | -0.027 | 0.0132 ± 0.0047 |
| data_status ADEQUATE | 1028 | 0.5355 | 0.4313 | 0.4582 | +0.077 | -0.027 | 0.0114 ± 0.0039 |
| data_status LIMITED | 867 | 0.5537 | 0.4226 | 0.4867 | +0.067 | -0.064 | 0.0034 ± 0.005 |
| data_status POOR | 1638 | 0.5593 | 0.4015 | 0.464 | +0.095 | -0.062 | 0.0107 ± 0.0042 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 534 | 0.1957 | 0.197 | -0.0013 ± 0.0007 | 0.5699 | 0.5726 | 0.4974 | 0.4824 | 0.5337 | -0.051 ± 0.0201 | -0.01 (5) |
| 3-5 | 342 | 0.1988 | 0.1981 | +0.0007 ± 0.0019 | 0.58 | 0.5769 | 0.5058 | 0.4657 | 0.4766 | -0.091 ± 0.0247 | 0.02 (1) |
| 5-10 | 730 | 0.199 | 0.1991 | -0.0001 ± 0.0025 | 0.5834 | 0.5817 | 0.5125 | 0.4381 | 0.4712 | -0.084 ± 0.0172 | -0.0167 (6) |
| 10-15 | 626 | 0.2143 | 0.2055 | +0.0088 ± 0.0045 | 0.6184 | 0.5932 | 0.5264 | 0.4022 | 0.4281 | -0.097 ± 0.018 | -0.048 (5) |
| 15-25 | 776 | 0.2277 | 0.2148 | +0.0129 ± 0.0065 | 0.6493 | 0.6147 | 0.5817 | 0.3863 | 0.451 | -0.090 ± 0.0166 | -0.0033 (9) |
| 25-40 | 438 | 0.2236 | 0.2081 | +0.0155 ± 0.0129 | 0.6354 | 0.5987 | 0.6553 | 0.3474 | 0.4749 | -0.076 ± 0.0198 | -0.01 (1) |
| 40+ | 87 | 0.297 | 0.1766 | +0.1204 ± 0.0404 | 0.8103 | 0.527 | 0.7594 | 0.3102 | 0.4023 | -0.126 ± 0.0388 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2542 | 0.1804 | 0.1816 | -0.0013 ± 0.0003 | 0.5355 | 0.537 | 0.4791 | 0.464 | 0.5031 | -0.019 ± 0.0086 | -0.0129 (17) |
| 3-5 | 1640 | 0.194 | 0.1922 | +0.0019 ± 0.0009 | 0.5687 | 0.5605 | 0.4821 | 0.4422 | 0.4378 | -0.063 ± 0.011 | 0.0 (2) |
| 5-10 | 3494 | 0.1947 | 0.1914 | +0.0033 ± 0.0011 | 0.5716 | 0.5611 | 0.4851 | 0.4113 | 0.4239 | -0.052 ± 0.0075 | -0.0119 (21) |
| 10-15 | 3141 | 0.2049 | 0.1869 | +0.0180 ± 0.0019 | 0.5974 | 0.547 | 0.4884 | 0.3638 | 0.354 | -0.074 ± 0.0077 | -0.0281 (16) |
| 15-25 | 3792 | 0.2092 | 0.1726 | +0.0366 ± 0.0026 | 0.6097 | 0.5096 | 0.5027 | 0.3066 | 0.3125 | -0.069 ± 0.0067 | -0.0025 (44) |
| 25-40 | 2910 | 0.2222 | 0.1267 | +0.0954 ± 0.0041 | 0.6385 | 0.39 | 0.5317 | 0.2191 | 0.2265 | -0.067 ± 0.0064 | -0.01 (1) |
| 40+ | 1934 | 0.3796 | 0.0427 | +0.3369 ± 0.0053 | 0.9879 | 0.1695 | 0.6297 | 0.1069 | 0.0569 | -0.087 ± 0.0044 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 402 | 0.1998 | 0.2003 | -0.0005 ± 0.0008 | 0.5815 | 0.5826 | 0.504 | 0.489 | 0.5075 | -0.092 ± 0.0239 | -0.01 (3) |
| 3-5 | 289 | 0.216 | 0.2151 | +0.0010 ± 0.0022 | 0.6154 | 0.6141 | 0.5153 | 0.4754 | 0.4775 | -0.098 ± 0.0291 | 0.02 (1) |
| 5-10 | 626 | 0.1988 | 0.1991 | -0.0004 ± 0.0027 | 0.5809 | 0.5814 | 0.5462 | 0.4712 | 0.5112 | -0.073 ± 0.0184 | -0.01 (4) |
| 10-15 | 590 | 0.2167 | 0.2105 | +0.0061 ± 0.0047 | 0.6233 | 0.607 | 0.5669 | 0.4426 | 0.4831 | -0.096 ± 0.0196 | -0.04 (5) |
| 15-25 | 845 | 0.2313 | 0.2101 | +0.0212 ± 0.0062 | 0.6546 | 0.6032 | 0.5925 | 0.3962 | 0.445 | -0.098 ± 0.0161 | -0.0133 (9) |
| 25-40 | 577 | 0.2629 | 0.1991 | +0.0638 ± 0.0117 | 0.7342 | 0.579 | 0.6645 | 0.3494 | 0.4073 | -0.118 ± 0.0182 | -0.0075 (4) |
| 40+ | 204 | 0.3678 | 0.1756 | +0.1922 ± 0.0291 | 1.0227 | 0.5218 | 0.7445 | 0.2622 | 0.3186 | -0.084 ± 0.0283 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2174 | 0.1854 | 0.1861 | -0.0006 ± 0.0003 | 0.5473 | 0.5485 | 0.5024 | 0.4875 | 0.5124 | -0.033 ± 0.0096 | -0.0133 (15) |
| 3-5 | 1388 | 0.1966 | 0.1961 | +0.0006 ± 0.001 | 0.5696 | 0.568 | 0.5153 | 0.4754 | 0.4863 | -0.043 ± 0.0121 | 0.02 (1) |
| 5-10 | 3121 | 0.191 | 0.1896 | +0.0014 ± 0.0012 | 0.564 | 0.5573 | 0.5071 | 0.4331 | 0.4624 | -0.033 ± 0.0079 | -0.0117 (6) |
| 10-15 | 2754 | 0.1995 | 0.1882 | +0.0114 ± 0.0021 | 0.5871 | 0.5486 | 0.5187 | 0.3941 | 0.4129 | -0.053 ± 0.0084 | -0.0189 (18) |
| 15-25 | 3929 | 0.2175 | 0.1795 | +0.0380 ± 0.0027 | 0.6295 | 0.5273 | 0.5311 | 0.3347 | 0.3398 | -0.070 ± 0.0068 | -0.0086 (42) |
| 25-40 | 3436 | 0.2505 | 0.138 | +0.1124 ± 0.004 | 0.7068 | 0.4225 | 0.5632 | 0.2471 | 0.2293 | -0.089 ± 0.0063 | -0.0044 (18) |
| 40+ | 2651 | 0.4009 | 0.0654 | +0.3356 ± 0.0057 | 1.0579 | 0.2288 | 0.6618 | 0.1251 | 0.0939 | -0.071 ± 0.0049 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 512 | 0.1979 | 0.2005 | -0.0025 ± 0.0007 | 0.5765 | 0.5825 | 0.4985 | 0.4832 | 0.5566 | -0.014 ± 0.0202 | -0.0137 (8) |
| 3-5 | 374 | 0.1943 | 0.1921 | +0.0021 ± 0.0018 | 0.5663 | 0.5612 | 0.5 | 0.4604 | 0.4545 | -0.119 ± 0.0236 | 0.0067 (3) |
| 5-10 | 766 | 0.2006 | 0.1973 | +0.0032 ± 0.0024 | 0.5879 | 0.5768 | 0.5083 | 0.4345 | 0.4465 | -0.098 ± 0.0165 | -0.0071 (7) |
| 10-15 | 614 | 0.2096 | 0.2071 | +0.0026 ± 0.0046 | 0.6071 | 0.5973 | 0.5412 | 0.418 | 0.4723 | -0.078 ± 0.0182 | -0.0317 (6) |
| 15-25 | 726 | 0.2339 | 0.2114 | +0.0225 ± 0.0066 | 0.6663 | 0.6068 | 0.5904 | 0.397 | 0.4353 | -0.116 ± 0.017 | -0.03 (1) |
| 25-40 | 452 | 0.2115 | 0.2143 | -0.0028 ± 0.0127 | 0.6094 | 0.6126 | 0.6633 | 0.3535 | 0.5111 | -0.054 ± 0.0194 | 0.015 (2) |
| 40+ | 89 | 0.3108 | 0.1932 | +0.1177 ± 0.0416 | 0.8465 | 0.5643 | 0.7657 | 0.3136 | 0.4157 | -0.111 ± 0.043 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2431 | 0.1874 | 0.1883 | -0.0010 ± 0.0003 | 0.5515 | 0.5533 | 0.4876 | 0.4723 | 0.4986 | -0.028 ± 0.0089 | -0.0163 (35) |
| 3-5 | 1703 | 0.1894 | 0.1864 | +0.0029 ± 0.0008 | 0.5565 | 0.5494 | 0.4817 | 0.4421 | 0.4251 | -0.079 ± 0.0107 | -0.0094 (18) |
| 5-10 | 3742 | 0.1949 | 0.1887 | +0.0061 ± 0.0011 | 0.5738 | 0.5537 | 0.4843 | 0.4104 | 0.4035 | -0.068 ± 0.0071 | -0.01 (31) |
| 10-15 | 2925 | 0.1976 | 0.1812 | +0.0164 ± 0.002 | 0.5804 | 0.5325 | 0.5004 | 0.3768 | 0.3723 | -0.072 ± 0.0078 | -0.015 (12) |
| 15-25 | 3888 | 0.2117 | 0.1726 | +0.0391 ± 0.0026 | 0.6173 | 0.5098 | 0.5106 | 0.316 | 0.3135 | -0.075 ± 0.0067 | -0.03 (2) |
| 25-40 | 2894 | 0.2182 | 0.1266 | +0.0916 ± 0.0042 | 0.6297 | 0.3884 | 0.5317 | 0.2162 | 0.2322 | -0.062 ± 0.0063 | 0.01 (3) |
| 40+ | 1870 | 0.3943 | 0.0475 | +0.3468 ± 0.0057 | 1.0289 | 0.1821 | 0.6412 | 0.1123 | 0.061 | -0.089 ± 0.0048 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 860 | 0.1958 | 0.1961 | -0.0002 ± 0.0005 | 0.5719 | 0.5722 | 0.5069 | 0.4919 | 0.4977 | -0.054 ± 0.0153 | -0.0224 (49) |
| 3-5 | 604 | 0.1937 | 0.1929 | +0.0007 ± 0.0014 | 0.5655 | 0.5626 | 0.4821 | 0.4423 | 0.4503 | -0.054 ± 0.0181 | -0.0194 (34) |
| 5-10 | 1284 | 0.2 | 0.1938 | +0.0062 ± 0.0019 | 0.5875 | 0.5696 | 0.4905 | 0.4172 | 0.4128 | -0.069 ± 0.0125 | -0.005 (78) |
| 10-15 | 820 | 0.2086 | 0.1974 | +0.0111 ± 0.0039 | 0.6051 | 0.5768 | 0.5146 | 0.3915 | 0.4061 | -0.064 ± 0.0157 | 0.0014 (64) |
| 15-25 | 1103 | 0.232 | 0.2111 | +0.0209 ± 0.0054 | 0.6614 | 0.6083 | 0.572 | 0.3771 | 0.4225 | -0.065 ± 0.0139 | -0.0214 (59) |
| 25-40 | 654 | 0.2479 | 0.2014 | +0.0465 ± 0.0108 | 0.7021 | 0.5818 | 0.659 | 0.3467 | 0.4266 | -0.086 ± 0.0164 | -0.0219 (26) |
| 40+ | 229 | 0.3492 | 0.194 | +0.1552 ± 0.0291 | 1.0088 | 0.5691 | 0.8045 | 0.3186 | 0.4236 | -0.081 ± 0.0256 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2715 | 0.1868 | 0.1868 | -0.0001 ± 0.0003 | 0.5483 | 0.5476 | 0.506 | 0.4907 | 0.4991 | -0.039 ± 0.0083 | -0.0157 (88) |
| 3-5 | 1862 | 0.1907 | 0.188 | +0.0027 ± 0.0008 | 0.558 | 0.5516 | 0.4884 | 0.4487 | 0.435 | -0.062 ± 0.0101 | -0.0209 (69) |
| 5-10 | 3778 | 0.1965 | 0.188 | +0.0085 ± 0.0011 | 0.5779 | 0.554 | 0.4886 | 0.4152 | 0.396 | -0.072 ± 0.0071 | -0.0082 (132) |
| 10-15 | 2571 | 0.2048 | 0.1899 | +0.0149 ± 0.0021 | 0.5969 | 0.5581 | 0.5213 | 0.3983 | 0.3983 | -0.062 ± 0.0086 | -0.0053 (105) |
| 15-25 | 3236 | 0.2285 | 0.1976 | +0.0308 ± 0.0031 | 0.6579 | 0.5751 | 0.5636 | 0.3684 | 0.3888 | -0.064 ± 0.0079 | -0.0253 (107) |
| 25-40 | 2201 | 0.2544 | 0.1759 | +0.0785 ± 0.0056 | 0.7204 | 0.5166 | 0.6195 | 0.3059 | 0.3408 | -0.078 ± 0.0087 | -0.0229 (51) |
| 40+ | 1038 | 0.3747 | 0.137 | +0.2376 ± 0.0122 | 1.063 | 0.416 | 0.7225 | 0.2186 | 0.2486 | -0.072 ± 0.0106 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3533 | 1.059 ± 0.048 | 1.191 | 0.167 | 0.1637 | 0.213 | 0.2038 |
| gen2 | 3533 | 0.853 ± 0.044 | 1.148 | 0.1725 | 0.1641 | 0.2313 | 0.2037 |
| gen1_elo | 3533 | 1.036 ± 0.046 | 1.173 | 0.1733 | 0.164 | 0.2121 | 0.2039 |
| gen1_sr | 3533 | 1.059 ± 0.057 | 1.224 | 0.1328 | 0.1659 | 0.2273 | 0.2035 |
| gen1_ledger | 5554 | 0.882 ± 0.033 | 1.091 | 0.1787 | 0.18 | 0.2181 | 0.1989 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 17,595)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,007 | 22.8% |
| STALE_QUOTE | market_freshness | 3,620 | 20.6% |
| BOOK_QUALITY | execution | 3,465 | 19.7% |
| POOR_DATA | data | 2,023 | 11.5% |
| LIMITED_DATA | data | 1,202 | 6.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 909 | 5.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 890 | 5.1% |
| IDENTITY_AMBIGUOUS | mapping | 720 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 495 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 264 | 1.5% |

Cause class: coverage 22.8%, market_freshness 20.6%, execution 19.7%, data 18.3%, market_freshness/coverage 8.0%, model_calibration_or_unknown 5.1%, mapping 4.1%, model_calibration 1.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.3%, START_UNVERIFIABLE 94.2%, LOW_DATA_QUALITY 70.3%, THIN_PLAYER_HISTORY 58.9%, STALE_PLAYER_DATA 52.9%, STALE_KALSHI_QUOTE 42.9%, MODEL_INTERNAL_DISAGREEMENT 41.3%, ASYMMETRIC_SAMPLE_SIZE 32.7%, WIDE_SPREAD 25.6%, MODEL_HIGH_UNCERTAINTY 17.9%, PLAYER_IDENTITY_RISK 15.2%, LEVEL_TRANSFER_RISK 10.1%, EVENT_MAPPING_RISK 8.3%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 2.6%, UNKNOWN 1.0%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.2%, POST_SETTLEMENT_OBSERVATION 22.8%, POSSIBLE_IN_PLAY_QUOTE 5.5%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 9,321)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,168 | 34.0% |
| BOOK_QUALITY | execution | 1,819 | 19.5% |
| STALE_QUOTE | market_freshness | 1,666 | 17.9% |
| POOR_DATA | data | 850 | 9.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 481 | 5.2% |
| IDENTITY_AMBIGUOUS | mapping | 415 | 4.5% |
| LIMITED_DATA | data | 353 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 306 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 205 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 58 | 0.6% |

Cause class: coverage 34.0%, execution 19.5%, market_freshness 17.9%, data 12.9%, market_freshness/coverage 8.4%, mapping 4.5%, model_calibration_or_unknown 2.2%, model_calibration 0.6%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.5%, START_UNVERIFIABLE 97.2%, LOW_DATA_QUALITY 74.3%, THIN_PLAYER_HISTORY 61.6%, STALE_KALSHI_QUOTE 50.8%, STALE_PLAYER_DATA 48.3%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 34.7%, WIDE_SPREAD 25.5%, PLAYER_IDENTITY_RISK 18.6%, MODEL_HIGH_UNCERTAINTY 18.2%, EVENT_MAPPING_RISK 10.2%, LEVEL_TRANSFER_RISK 9.2%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 5.1%, EXTERNAL_MARKET_REJECTION 1.4%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.8%, POST_SETTLEMENT_OBSERVATION 34.0%, POSSIBLE_IN_PLAY_QUOTE 5.5%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 7340, "IDENTITY_AMBIGUOUS": 1981}; ticker orientation: {"VERIFIED": 9321}.

Checks: discipline:AMBIGUOUS 662, discipline:PASS 8659, identity_confidence:AMBIGUOUS 1734, identity_confidence:PASS 7587, level_mapping:NA 674, level_mapping:PASS 8647, market_pair:AMBIGUOUS 345, market_pair:NA 220, market_pair:PASS 8756, model_complement:NA 187, model_complement:PASS 9134, namesake:PASS 9321, physical_match_id:NA 3557, physical_match_id:PASS 5764, player_ids:PASS 9321, same_pair_other_event:PASS 9321, ticker_orientation:PASS 9321

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,333 | 4.5% | 4.2% | 1.6% | {"market_freshness": 47, "model_calibration_or_unknown": 35, "data": 29, "execution": 17, "market_freshness/coverage": 10, "model_calibration": 10, "coverage": 2} | 5.84 | 0.2198 / 0.2114 (357) | 18.2% | 3.5% | 3.8% | 2.4% |
| CHALLENGER | 6,896 | 16.9% | 6.6% | 12.5% | {"coverage": 667, "market_freshness/coverage": 145, "market_freshness": 136, "data": 104, "model_calibration_or_unknown": 55, "execution": 30, "model_calibration": 17, "mapping": 14} | 7.37 | 0.2173 / 0.2062 (1676) | 35.0% | 16.4% | 3.6% | 22.1% |
| DOUBLES | 1,361 | 48.6% | 48.2% | 7.1% | {"execution": 328, "mapping": 176, "market_freshness": 106, "market_freshness/coverage": 45, "coverage": 7} | 24.05 | 0.3206 / 0.2346 (352) | 17.2% | 0.0% | 100.0% | 7.0% |
| ITF_MEN | 11,636 | 24.8% | 17.4% | 30.9% | {"coverage": 1077, "execution": 602, "market_freshness": 457, "data": 397, "market_freshness/coverage": 222, "mapping": 125, "model_calibration_or_unknown": 2} | 11.41 | 0.2153 / 0.1951 (2688) | 35.8% | 64.0% | 15.4% | 21.9% |
| ITF_WOMEN | 15,791 | 26.3% | 19.7% | 44.6% | {"coverage": 1398, "market_freshness": 844, "execution": 811, "data": 639, "market_freshness/coverage": 316, "mapping": 94, "model_calibration_or_unknown": 47, "model_calibration": 10} | 12.87 | 0.2016 / 0.1938 (3093) | 37.5% | 58.2% | 10.3% | 21.2% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,477 | 4.6% | 4.2% | 1.2% | {"market_freshness": 36, "model_calibration_or_unknown": 25, "execution": 17, "data": 11, "market_freshness/coverage": 10, "model_calibration": 10, "coverage": 4, "mapping": 1} | 7.86 | 0.2376 / 0.2309 (391) | 23.5% | 1.4% | 1.5% | 3.4% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.9% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 5 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 6 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 7 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 8 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 9 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 10 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 15.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 928 min (STALE); no external reference |
| 11 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 12 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 13 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 14 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 15 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | POOR_DATA | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 16 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 17 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 18 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 19 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 20 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 21 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 22 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 23 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 24 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 25 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 26 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 27 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 28 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 29 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 30 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 31 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 92 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 32 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 33 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 34 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 36 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 162 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 37 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 38 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 39 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 40 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 41 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 20.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 1255 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |
| 42 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 33 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 43 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 44 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFWMATCH-26OCT16ESTLAB-LAB` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 68 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1475.0, ratio 2.28); no external reference |
| 46 | `KXITFWMATCH-26OCT19VLABOU-VLA` | ITF_WOMEN | fair_v1 | 77% / 2% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 3.13); no external reference |
| 47 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 49 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 50 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 624 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9717, "by_level_share_of_ge_25pp": {"ATP": 0.0161, "CHALLENGER": 0.1253, "DOUBLES": 0.071, "ITF_MEN": 0.3092, "ITF_WOMEN": 0.4462, "OTHER": 0.0013, "WTA": 0.0122, "WTA125": 0.0187}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5084, "share_primary_cause_market_settled_or_in_play": 0.4243, "share_primary_cause_stale_quote_only": 0.1787}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 9321, "identity_ambiguous_share": 0.2125, "ticker_orientation": {"VERIFIED": 9321}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 5764, "with_external": 261, "coverage": 0.0453, "external_status": {"EXTERNAL_STALE": 171, "AGREES_WITH_KALSHI": 87, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 171, "MODEL_LONE_OUTLIER": 87, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3333, "share_external_supports_model": 0.0115}, "pregame_clean_ge_25pp": {"n": 2842, "with_external": 247, "coverage": 0.0869, "external_status": {"EXTERNAL_STALE": 159, "AGREES_WITH_KALSHI": 85, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 159, "MODEL_LONE_OUTLIER": 85, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3441, "share_external_supports_model": 0.0121}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 510.0, "median_sample_ratio": 2.47, "median_min_matches": 20.0, "median_max_days_since_last": 223.0, "share_severe_asymmetry": 0.2103, "data_status": {"POOR": 5129, "LIMITED": 2578, "ADEQUATE": 1614}, "comparison_lt_10pp": {"median_thinner_serve_points": 1765.0, "median_sample_ratio": 1.68, "median_min_matches": 93.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 711, "model_minus_observed": 0.0491, "kalshi_minus_observed": -0.0855, "brier_diff_model_minus_kalshi": 0.0001}, "4-10x": {"n": 487, "model_minus_observed": 0.0772, "kalshi_minus_observed": -0.065, "brier_diff_model_minus_kalshi": 0.0079}, "<2x": {"n": 1741, "model_minus_observed": 0.0875, "kalshi_minus_observed": -0.0336, "brier_diff_model_minus_kalshi": 0.0121}, ">=10x": {"n": 594, "model_minus_observed": 0.116, "kalshi_minus_observed": -0.0583, "brier_diff_model_minus_kalshi": 0.0123}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3533, "model": {"intercept": -0.531, "slope": 0.853, "slope_se": 0.044}, "kalshi_mid_same_rows": {"intercept": 0.241, "slope": 1.148, "slope_se": 0.05}, "mean_extremity_model": 0.1725, "mean_extremity_kalshi": 0.1641, "model_brier": 0.2313, "kalshi_brier": 0.2037, "brier_diff_model_minus_kalshi": 0.0276, "brier_diff_se": 0.0032, "model_logloss": 0.6591, "kalshi_logloss": 0.5899}, "fair_v1": {"n": 3533, "model": {"intercept": -0.401, "slope": 1.059, "slope_se": 0.048}, "kalshi_mid_same_rows": {"intercept": 0.321, "slope": 1.191, "slope_se": 0.051}, "mean_extremity_model": 0.167, "mean_extremity_kalshi": 0.1637, "model_brier": 0.213, "kalshi_brier": 0.2038, "brier_diff_model_minus_kalshi": 0.0091, "brier_diff_se": 0.0026, "model_logloss": 0.6137, "kalshi_logloss": 0.5899}, "gen1_elo": {"n": 3533, "model": {"intercept": -0.393, "slope": 1.036, "slope_se": 0.046}, "kalshi_mid_same_rows": {"intercept": 0.315, "slope": 1.173, "slope_se": 0.05}, "mean_extremity_model": 0.1733, "mean_extremity_kalshi": 0.164, "model_brier": 0.2121, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0082, "brier_diff_se": 0.0026, "model_logloss": 0.6127, "kalshi_logloss": 0.59}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2396, "share_ge_15": 0.4375, "median_abs_gap": 12.99, "n": 24057}, "gen1_elo": {"share_ge_25": 0.2363, "share_ge_15": 0.4337, "median_abs_gap": 12.66, "n": 24057}, "gen1_sr": {"share_ge_25": 0.3024, "share_ge_15": 0.5169, "median_abs_gap": 15.6, "n": 24057}, "gen2": {"share_ge_25": 0.306, "share_ge_15": 0.5069, "median_abs_gap": 15.37, "n": 24057}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1511, "share_ge_15": 0.3556, "median_abs_gap": 10.83, "n": 18809}, "gen1_elo": {"share_ge_25": 0.151, "share_ge_15": 0.3485, "median_abs_gap": 10.47, "n": 18807}, "gen1_sr": {"share_ge_25": 0.2135, "share_ge_15": 0.4424, "median_abs_gap": 13.07, "n": 18809}, "gen2": {"share_ge_25": 0.2295, "share_ge_15": 0.4434, "median_abs_gap": 13.07, "n": 18810}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.84, "share_ge_25_all": 0.045, "share_ge_25_pregame_clean": 0.0424}, "WTA": {"median_abs_gap_pregame_clean": 7.86, "share_ge_25_all": 0.046, "share_ge_25_pregame_clean": 0.0418}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2383, "share_within_10pp_all": 0.4367, "share_within_10pp_pregame_clean": 0.4883, "corr_model_vs_mid_pregame_clean": 0.8431}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 534, "model_brier": 0.1957, "kalshi_brier": 0.197, "brier_diff_model_minus_kalshi": -0.0013}, "10-15": {"n_settled": 626, "model_brier": 0.2143, "kalshi_brier": 0.2055, "brier_diff_model_minus_kalshi": 0.0088}, "15-25": {"n_settled": 776, "model_brier": 0.2277, "kalshi_brier": 0.2148, "brier_diff_model_minus_kalshi": 0.0129}, "25-40": {"n_settled": 438, "model_brier": 0.2236, "kalshi_brier": 0.2081, "brier_diff_model_minus_kalshi": 0.0155}, "3-5": {"n_settled": 342, "model_brier": 0.1988, "kalshi_brier": 0.1981, "brier_diff_model_minus_kalshi": 0.0007}, "40+": {"n_settled": 87, "model_brier": 0.297, "kalshi_brier": 0.1766, "brier_diff_model_minus_kalshi": 0.1204}, "5-10": {"n_settled": 730, "model_brier": 0.199, "kalshi_brier": 0.1991, "brier_diff_model_minus_kalshi": -0.0001}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.531, "slope": 0.853, "slope_se": 0.044}, "kalshi_slope": {"intercept": 0.241, "slope": 1.148, "slope_se": 0.05}, "n": 3533}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.513, "slope": 0.882, "slope_se": 0.033}, "kalshi_slope": {"intercept": 0.157, "slope": 1.091, "slope_se": 0.038}, "n": 5554}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 352, "model_brier": 0.3206, "kalshi_brier": 0.2346, "brier_diff_model_minus_kalshi": 0.0861, "brier_diff_se": 0.0167, "corr_model_outcome": 0.0143, "corr_kalshi_outcome": 0.2592}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
