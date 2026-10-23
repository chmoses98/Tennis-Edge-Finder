# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-23T10:10Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 50,242): 0-3 13.9%, 3-5 9.4%, 5-10 19.7%, 10-15 15.3%, 15-25 19.4%, 25-40 14.1%, 40+ 8.2%; median gap 12.14 pp.
* **Where the extremes live**: 97.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.0%, Challenger 11.8%, doubles 6.7%). Main tour: ATP 4.8% and WTA 4.8% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 11,188): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.5%, STALE_QUOTE 18.7%, BOOK_QUALITY 18.1%, POOR_DATA 8.9%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.6%, LIMITED_DATA 3.6%, IN_PLAY_QUOTE 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.5%, market_freshness 18.7%, execution 18.1%, data 12.4%, market_freshness/coverage 8.9%, mapping 4.6%, model_calibration_or_unknown 2.1%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.3% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.4% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 11,188 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.1% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.6% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 479.0 points vs 1667.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.044, Gen-2 0.846, Gen-1 ledger 0.867 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 547 model 0.2243 vs Kalshi 0.2091; n 112 model 0.2783 vs Kalshi 0.1982.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 216,915 model-market comparisons (353,236 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 71,838 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-23T09:57:42.512127+00:00'], shadow board 58,017 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-23T09:57:45.775563+00:00'], Model 4 27,201 rows, 19,254 settled tickers, 6,826 tickers with an external scan.
* By model: {"gen1_ledger": 48740, "gen1_elo": 29174, "fair_v1": 29174, "gen2": 29174, "gen1_sr": 29174, "model4_fundamental": 25753, "model4_conditioned": 25726}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 50,242 | 13.9 | 9.4 | 19.7 | 15.3 | 19.4 | 14.1 | 8.2 | 12.14 | 41.6% | 22.3% |
| MW fair_v1 | 29,174 | 12.8 | 8.5 | 18.4 | 15.6 | 19.8 | 15.0 | 9.8 | 13.19 | 44.6% | 24.8% |
| MW gen1_elo | 29,174 | 12.8 | 8.5 | 18.9 | 15.3 | 20.0 | 15.0 | 9.6 | 13.02 | 44.5% | 24.6% |
| MW gen1_ledger | 21,068 | 15.4 | 10.8 | 21.5 | 14.9 | 18.7 | 12.8 | 5.9 | 10.59 | 37.4% | 18.7% |
| MW gen1_sr | 29,174 | 10.1 | 7.0 | 16.5 | 13.7 | 21.0 | 18.9 | 12.9 | 16.09 | 52.7% | 31.7% |
| MW gen2 | 29,174 | 10.9 | 7.2 | 16.2 | 14.1 | 19.5 | 18.0 | 14.0 | 15.65 | 51.5% | 32.0% |
| all families model4_conditioned | 25,726 | 21.9 | 18.9 | 34.7 | 17.7 | 4.3 | 1.4 | 1.0 | 5.96 | 6.8% | 2.5% |
| all families model4_fundamental | 25,753 | 16.6 | 13.3 | 34.1 | 20.6 | 10.6 | 3.4 | 1.3 | 7.81 | 15.3% | 4.7% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.9%, >=15pp 41.6%, >=20pp 30.9%, >=25pp 22.3%, >=30pp 16.1%, >=40pp 8.2%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.53pp; >=10pp 45.6%, >=25pp 17.4%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,493 | 28.6 | 14.2 | 24.8 | 15.0 | 11.8 | 4.9 | 0.7 | 6.14 | 17.4% | 5.6% |
| CHALLENGER | 4,563 | 15.9 | 10.0 | 20.4 | 15.6 | 14.8 | 12.3 | 11.0 | 11.02 | 38.0% | 23.2% |
| ITF_MEN | 8,087 | 10.3 | 7.4 | 16.9 | 14.7 | 21.5 | 17.2 | 12.0 | 15.21 | 50.7% | 29.2% |
| ITF_WOMEN | 11,667 | 9.4 | 6.8 | 15.9 | 15.4 | 22.5 | 18.2 | 11.7 | 15.76 | 52.3% | 29.8% |
| WTA | 1,704 | 17.1 | 13.3 | 25.6 | 19.8 | 18.8 | 4.7 | 0.7 | 8.36 | 24.2% | 5.3% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,493 | 24.0 | 15.0 | 24.9 | 17.1 | 13.1 | 4.8 | 1.0 | 6.54 | 18.9% | 5.8% |
| CHALLENGER | 4,563 | 15.1 | 8.7 | 18.6 | 14.7 | 17.3 | 13.8 | 11.9 | 12.47 | 43.0% | 25.7% |
| ITF_MEN | 8,087 | 8.3 | 5.9 | 14.5 | 13.1 | 19.7 | 20.9 | 17.6 | 18.49 | 58.2% | 38.5% |
| ITF_WOMEN | 11,667 | 8.1 | 5.6 | 13.8 | 13.5 | 20.7 | 21.0 | 17.4 | 18.96 | 59.1% | 38.4% |
| WTA | 1,704 | 14.5 | 10.1 | 21.6 | 16.1 | 23.3 | 13.6 | 0.7 | 10.94 | 37.6% | 14.3% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,493 | 24.5 | 12.9 | 23.7 | 16.0 | 14.9 | 6.9 | 1.2 | 7.3 | 23.0% | 8.1% |
| CHALLENGER | 4,563 | 14.3 | 9.2 | 20.6 | 15.6 | 16.4 | 12.7 | 11.2 | 11.47 | 40.3% | 23.9% |
| ITF_MEN | 8,087 | 9.8 | 7.5 | 16.9 | 14.1 | 22.1 | 17.6 | 12.1 | 15.61 | 51.8% | 29.7% |
| ITF_WOMEN | 11,667 | 9.5 | 6.6 | 16.2 | 15.8 | 22.9 | 18.1 | 10.8 | 15.58 | 51.9% | 29.0% |
| WTA | 1,704 | 24.2 | 16.7 | 30.5 | 16.0 | 9.9 | 2.3 | 0.4 | 6.01 | 12.6% | 2.7% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,430 | 25.4 | 19.5 | 30.9 | 11.9 | 8.9 | 3.0 | 0.3 | 5.54 | 12.2% | 3.4% |
| CHALLENGER | 3,132 | 21.4 | 14.7 | 26.4 | 14.4 | 14.7 | 6.6 | 1.9 | 7.3 | 23.1% | 8.4% |
| DOUBLES | 1,571 | 5.5 | 4.3 | 11.5 | 10.2 | 21.0 | 26.2 | 21.3 | 23.91 | 68.5% | 47.5% |
| ITF_MEN | 6,008 | 13.8 | 9.0 | 19.9 | 16.0 | 21.3 | 13.3 | 6.6 | 12.21 | 41.3% | 20.0% |
| ITF_WOMEN | 7,016 | 12.7 | 9.0 | 19.3 | 15.1 | 21.6 | 16.2 | 6.1 | 12.84 | 43.9% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,030 | 22.2 | 16.0 | 29.6 | 18.2 | 10.1 | 3.6 | 0.3 | 6.97 | 14.0% | 3.9% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,426 | 28.9 | 14.4 | 25.2 | 14.9 | 11.6 | 4.5 | 0.5 | 5.97 | 16.6% | 5.0% |
| CHALLENGER | 3,220 | 20.8 | 12.4 | 25.1 | 18.0 | 15.2 | 6.5 | 1.9 | 8.33 | 23.7% | 8.5% |
| ITF_MEN | 5,970 | 12.4 | 8.8 | 20.2 | 16.6 | 22.5 | 14.2 | 5.2 | 12.51 | 42.0% | 19.5% |
| ITF_WOMEN | 8,741 | 11.2 | 8.2 | 18.2 | 17.4 | 24.4 | 15.3 | 5.3 | 13.52 | 45.1% | 20.7% |
| WTA | 1,655 | 17.3 | 13.1 | 25.6 | 20.1 | 18.8 | 4.4 | 0.7 | 8.25 | 23.9% | 5.1% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,426 | 24.3 | 15.4 | 25.1 | 17.0 | 13.1 | 4.5 | 0.6 | 6.47 | 18.2% | 5.1% |
| CHALLENGER | 3,220 | 19.1 | 11.2 | 23.1 | 17.5 | 17.6 | 9.4 | 2.2 | 9.08 | 29.1% | 11.6% |
| ITF_MEN | 5,971 | 9.9 | 7.1 | 16.7 | 15.0 | 21.6 | 19.3 | 10.5 | 15.49 | 51.3% | 29.8% |
| ITF_WOMEN | 8,742 | 9.1 | 6.5 | 15.2 | 15.0 | 22.7 | 20.4 | 11.0 | 16.57 | 54.2% | 31.5% |
| WTA | 1,655 | 14.6 | 10.1 | 21.7 | 16.1 | 23.3 | 13.5 | 0.7 | 10.95 | 37.6% | 14.3% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,386 | 25.7 | 19.8 | 30.9 | 12.1 | 8.4 | 2.9 | 0.2 | 5.47 | 11.5% | 3.1% |
| CHALLENGER | 2,729 | 22.9 | 15.8 | 27.9 | 14.3 | 14.0 | 4.5 | 0.6 | 6.72 | 19.1% | 5.1% |
| DOUBLES | 1,459 | 5.5 | 4.5 | 11.8 | 10.4 | 20.8 | 26.2 | 20.8 | 23.85 | 67.8% | 47.0% |
| ITF_MEN | 5,034 | 15.0 | 9.7 | 21.6 | 16.8 | 21.2 | 11.7 | 4.0 | 11.18 | 36.9% | 15.7% |
| ITF_WOMEN | 5,815 | 13.6 | 9.6 | 20.7 | 15.9 | 21.8 | 15.0 | 3.4 | 11.67 | 40.2% | 18.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 980 | 22.8 | 16.5 | 29.6 | 18.2 | 10.1 | 2.9 | 0.0 | 6.81 | 13.0% | 2.9% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,571 | 5.5 | 4.3 | 11.5 | 10.2 | 21.0 | 26.2 | 21.3 | 23.91 | 68.5% | 47.5% |
| singles | 19,497 | 16.2 | 11.3 | 22.3 | 15.3 | 18.5 | 11.8 | 4.7 | 10.04 | 34.9% | 16.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 6,501 | 13.1 | 8.9 | 19.2 | 15.7 | 18.8 | 14.6 | 9.8 | 12.81 | 43.1% | 24.4% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 18,041 | 13.2 | 8.5 | 18.4 | 15.3 | 20.0 | 14.8 | 9.8 | 13.15 | 44.5% | 24.5% |
| UNKNOWN | 4,395 | 10.8 | 7.7 | 17.2 | 16.9 | 20.7 | 16.2 | 10.4 | 14.04 | 47.4% | 26.7% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,107 | 19.6 | 11.8 | 21.4 | 16.5 | 15.4 | 9.0 | 6.2 | 9.17 | 30.7% | 15.2% |
| B | 3,631 | 12.4 | 8.8 | 20.1 | 16.4 | 19.3 | 12.4 | 10.7 | 12.5 | 42.4% | 23.1% |
| C | 4,121 | 11.5 | 8.8 | 19.8 | 15.2 | 19.5 | 14.8 | 10.5 | 13.18 | 44.8% | 25.3% |
| D | 4,612 | 12.2 | 7.7 | 17.2 | 15.5 | 21.6 | 15.7 | 10.2 | 14.0 | 47.4% | 25.8% |
| F | 8,703 | 7.7 | 5.5 | 15.0 | 14.7 | 23.4 | 21.3 | 12.4 | 17.71 | 57.1% | 33.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,900 | 23.0 | 15.9 | 28.9 | 15.1 | 11.7 | 4.0 | 1.5 | 6.68 | 17.2% | 5.5% |
| B | 2,887 | 16.1 | 10.4 | 23.3 | 16.3 | 19.4 | 10.6 | 3.9 | 10.03 | 33.9% | 14.5% |
| C | 4,159 | 11.4 | 7.4 | 18.3 | 14.1 | 21.5 | 16.7 | 10.6 | 14.35 | 48.8% | 27.3% |
| D | 2,966 | 14.5 | 9.8 | 19.9 | 14.5 | 21.0 | 14.3 | 6.1 | 12.03 | 41.4% | 20.4% |
| F | 5,156 | 10.2 | 8.4 | 15.4 | 14.8 | 22.8 | 20.2 | 8.2 | 15.55 | 51.1% | 28.4% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 9,321 | 17.8 | 10.6 | 20.7 | 16.4 | 16.0 | 9.9 | 8.7 | 10.26 | 34.6% | 18.6% |
| LIMITED | 6,228 | 13.3 | 10.0 | 20.5 | 15.7 | 19.3 | 13.4 | 7.8 | 11.95 | 40.5% | 21.2% |
| POOR | 13,625 | 9.3 | 6.4 | 15.9 | 15.1 | 22.7 | 19.1 | 11.6 | 16.17 | 53.4% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,621 | 26.4 | 20.3 | 34.4 | 12.6 | 4.7 | 1.4 | 0.2 | 5.35 | 6.3% | 1.6% |
| GAME_SPREAD | 4,697 | 22.2 | 15.2 | 33.5 | 17.4 | 9.0 | 2.3 | 0.3 | 6.72 | 11.7% | 2.7% |
| MATCH_WINNER | 21,068 | 15.4 | 10.8 | 21.5 | 14.9 | 18.7 | 12.8 | 5.9 | 10.59 | 37.4% | 18.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 9,857 | 29.3 | 17.2 | 31.1 | 12.4 | 8.0 | 1.6 | 0.4 | 5.44 | 10.0% | 2.0% |
| TOTAL_GAMES | 7,473 | 8.6 | 9.7 | 36.6 | 28.9 | 10.5 | 3.2 | 2.6 | 9.45 | 16.3% | 5.8% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,993 | 25.5 | 33.6 | 32.8 | 4.5 | 2.9 | 0.5 | 0.2 | 4.48 | 3.7% | 0.8% |
| GAME_SPREAD | 6,180 | 45.5 | 16.7 | 27.0 | 7.9 | 1.7 | 0.9 | 0.3 | 3.5 | 2.9% | 1.2% |
| TOTAL_GAMES | 10,553 | 5.0 | 7.8 | 41.0 | 34.7 | 7.0 | 2.5 | 2.1 | 9.59 | 11.6% | 4.6% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,996 | 24.3 | 17.8 | 35.6 | 12.6 | 6.9 | 2.4 | 0.3 | 5.82 | 9.7% | 2.8% |
| GAME_SPREAD | 6,183 | 19.3 | 13.3 | 27.9 | 20.8 | 13.4 | 4.4 | 0.9 | 7.97 | 18.7% | 5.3% |
| TOTAL_GAMES | 10,574 | 8.5 | 9.5 | 36.4 | 27.4 | 12.2 | 3.7 | 2.3 | 9.49 | 18.2% | 6.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 29,174 | 44.6% | 24.8% | 13.19 | 36.3% | 15.6% | 10.98 |
| gen1_elo | 29,174 | 44.5% | 24.6% | 13.02 | 36.1% | 15.8% | 10.79 |
| gen1_sr | 29,174 | 52.7% | 31.7% | 16.09 | 45.0% | 22.5% | 13.29 |
| gen2 | 29,174 | 51.5% | 32.0% | 15.65 | 44.8% | 24.0% | 13.16 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 14,785 | 15.7 | 10.3 | 21.2 | 17.2 | 20.3 | 11.9 | 3.4 | 10.8 | 35.6% | 15.3% |
| STALE | 14,389 | 9.9 | 6.6 | 15.6 | 13.9 | 19.4 | 18.1 | 16.5 | 16.91 | 54.0% | 34.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 14,536 | 16.5 | 11.3 | 22.2 | 15.0 | 17.9 | 12.2 | 4.9 | 9.99 | 35.0% | 17.1% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 50,242 | 14536 | 18257 | 17449 | 24.1 | 143.0 | 1400.4 |
| ge_15pp | 20,913 | 5088 | 6547 | 9278 | 26.1 | 438.6 | 1380.4 |
| ge_25pp | 11,188 | 2487 | 2850 | 5851 | 32.3 | 577.6 | 1380.4 |
| lt_10pp | 21,637 | 7271 | 8608 | 5758 | 22.4 | 48.4 | 1341.5 |

Current slate `SL-20261023T101050Z-b08d2507`: 343 priced rows, quote age at build {'median': 13.5, 'max': 13.5}, freshness {'AGING': 343}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 22 | 0.0 | 0.0 | 22.7 | 4.5 | 40.9 | 31.8 | 0.0 | 20.48 | 72.7% | 31.8% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,729 | 19.2 | 11.1 | 24.4 | 18.8 | 18.5 | 7.4 | 0.7 | 8.98 | 26.6% | 8.1% |
| KALSHI_LONE_OUTLIER | 17 | 5.9 | 5.9 | 76.5 | 0.0 | 5.9 | 5.9 | 0.0 | 6.11 | 11.8% | 5.9% |
| MARKETS_AGREE | 538 | 65.2 | 34.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.25 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,143 | 0.0 | 2.3 | 35.1 | 26.2 | 24.9 | 10.7 | 0.8 | 12.42 | 36.4% | 11.5% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 29,174 | 4461 (15.3%) | 25.6% | 0.9% | {"EXTERNAL_STALE": 2729, "AGREES_WITH_KALSHI": 1143, "ALL_AGREE": 538, "SUPPORTS_MODEL_DIRECTION": 21, "AGREES_WITH_MODEL": 17, "EXTERNAL_OUTLIER": 12, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 13,026 | 1159 (8.9%) | 35.9% | 1.6% | {"EXTERNAL_STALE": 725, "AGREES_WITH_KALSHI": 416, "SUPPORTS_MODEL_DIRECTION": 16, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 7,239 | 359 (5.0%) | 36.5% | 2.2% | {"EXTERNAL_STALE": 220, "AGREES_WITH_KALSHI": 131, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,540 | 336 (9.5%) | 36.9% | 2.4% | {"EXTERNAL_STALE": 204, "AGREES_WITH_KALSHI": 124, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 11,597 | 2488 (21.4%) | 17.2% | 0.8% | {"EXTERNAL_STALE": 1491, "ALL_AGREE": 538, "AGREES_WITH_KALSHI": 427, "AGREES_WITH_MODEL": 15, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 4, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,557 | 10.2 | 7.5 | 19.3 | 14.4 | 22.6 | 16.0 | 10.0 | 14.28 | 48.6% | 26.0% |
| 4-10x | 3,819 | 11.0 | 8.3 | 19.2 | 15.4 | 21.1 | 14.9 | 10.1 | 13.69 | 46.1% | 25.0% |
| <2x | 14,745 | 14.9 | 9.7 | 19.0 | 16.5 | 17.8 | 13.1 | 9.1 | 11.91 | 39.9% | 22.2% |
| >=10x | 5,053 | 11.1 | 6.3 | 15.1 | 14.4 | 22.0 | 19.4 | 11.7 | 16.18 | 53.0% | 31.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 7,372 | 12.3 | 8.5 | 19.6 | 16.1 | 19.4 | 13.6 | 10.6 | 12.96 | 43.6% | 24.1% |
| 300-1000 | 6,284 | 11.7 | 8.5 | 17.3 | 15.3 | 20.7 | 16.3 | 10.2 | 13.97 | 47.2% | 26.5% |
| <300 | 9,639 | 8.7 | 5.7 | 15.5 | 14.9 | 23.0 | 20.0 | 12.2 | 16.86 | 55.2% | 32.2% |
| >=3000 | 5,879 | 21.5 | 13.0 | 23.0 | 16.5 | 14.3 | 7.0 | 4.7 | 7.96 | 26.0% | 11.7% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 834 | 0.5485 | 0.41 | 0.5012 | +0.047 | -0.091 | -0.0036 ± 0.0054 |
| ratio 4-10x | 567 | 0.586 | 0.4398 | 0.4921 | +0.094 | -0.052 | 0.0132 ± 0.0068 |
| ratio <2x | 2051 | 0.5378 | 0.4136 | 0.4466 | +0.091 | -0.033 | 0.0122 ± 0.0032 |
| ratio >=10x | 753 | 0.5686 | 0.3923 | 0.4622 | +0.106 | -0.070 | 0.0065 ± 0.0067 |
| thinner_sample 1000-3000 | 1138 | 0.5424 | 0.4147 | 0.449 | +0.093 | -0.034 | 0.0106 ± 0.0042 |
| thinner_sample 300-1000 | 968 | 0.5649 | 0.4215 | 0.4928 | +0.072 | -0.071 | 0.0006 ± 0.0052 |
| thinner_sample <300 | 1416 | 0.5583 | 0.3911 | 0.4633 | +0.095 | -0.072 | 0.0088 ± 0.0047 |
| thinner_sample >=3000 | 683 | 0.5362 | 0.4411 | 0.4641 | +0.072 | -0.023 | 0.0136 ± 0.0045 |
| data_status ADEQUATE | 1192 | 0.539 | 0.4329 | 0.4522 | +0.087 | -0.019 | 0.0126 ± 0.0036 |
| data_status LIMITED | 984 | 0.5497 | 0.4164 | 0.4797 | +0.070 | -0.063 | 0.0043 ± 0.0048 |
| data_status POOR | 2029 | 0.5606 | 0.3988 | 0.4682 | +0.092 | -0.069 | 0.0075 ± 0.0039 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 614 | 0.1993 | 0.2004 | -0.0010 ± 0.0006 | 0.5791 | 0.5814 | 0.5022 | 0.4873 | 0.5326 | -0.060 ± 0.0189 | -0.01 (5) |
| 3-5 | 391 | 0.2019 | 0.2012 | +0.0007 ± 0.0018 | 0.5869 | 0.5836 | 0.503 | 0.463 | 0.4731 | -0.099 ± 0.0234 | 0.02 (1) |
| 5-10 | 856 | 0.2012 | 0.2006 | +0.0005 ± 0.0023 | 0.5887 | 0.5842 | 0.5093 | 0.435 | 0.4638 | -0.090 ± 0.0159 | -0.0167 (6) |
| 10-15 | 726 | 0.2133 | 0.2038 | +0.0094 ± 0.0042 | 0.6172 | 0.5892 | 0.5286 | 0.4044 | 0.427 | -0.103 ± 0.0167 | -0.048 (5) |
| 15-25 | 959 | 0.2238 | 0.2132 | +0.0106 ± 0.0058 | 0.6423 | 0.6102 | 0.5764 | 0.3805 | 0.4515 | -0.089 ± 0.0147 | -0.0033 (9) |
| 25-40 | 547 | 0.2243 | 0.2091 | +0.0152 ± 0.0117 | 0.6366 | 0.6015 | 0.6557 | 0.346 | 0.4735 | -0.075 ± 0.018 | -0.01 (1) |
| 40+ | 112 | 0.2783 | 0.1982 | +0.0800 ± 0.0365 | 0.7629 | 0.5814 | 0.7564 | 0.3087 | 0.4464 | -0.077 ± 0.0358 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3151 | 0.1822 | 0.1833 | -0.0011 ± 0.0003 | 0.5391 | 0.5404 | 0.4913 | 0.4763 | 0.5148 | -0.017 ± 0.0077 | -0.0129 (17) |
| 3-5 | 2074 | 0.1966 | 0.1953 | +0.0013 ± 0.0008 | 0.5733 | 0.5672 | 0.4849 | 0.4449 | 0.4479 | -0.053 ± 0.0099 | 0.0 (2) |
| 5-10 | 4484 | 0.1966 | 0.1933 | +0.0034 ± 0.001 | 0.5772 | 0.5657 | 0.4804 | 0.4064 | 0.4199 | -0.048 ± 0.0067 | -0.0119 (21) |
| 10-15 | 3851 | 0.1974 | 0.1794 | +0.0180 ± 0.0017 | 0.5805 | 0.5294 | 0.485 | 0.3604 | 0.35 | -0.073 ± 0.0068 | -0.0281 (16) |
| 15-25 | 4861 | 0.2079 | 0.1693 | +0.0386 ± 0.0023 | 0.609 | 0.5011 | 0.5032 | 0.3069 | 0.3075 | -0.072 ± 0.0058 | -0.0025 (44) |
| 25-40 | 3770 | 0.2235 | 0.1315 | +0.0920 ± 0.0037 | 0.6412 | 0.401 | 0.5317 | 0.2189 | 0.2316 | -0.058 ± 0.0057 | -0.01 (1) |
| 40+ | 2455 | 0.3809 | 0.0456 | +0.3354 ± 0.0049 | 0.9922 | 0.1758 | 0.6333 | 0.1079 | 0.064 | -0.080 ± 0.004 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 474 | 0.204 | 0.2045 | -0.0005 ± 0.0007 | 0.5898 | 0.5907 | 0.5035 | 0.4884 | 0.5042 | -0.111 ± 0.0223 | -0.01 (3) |
| 3-5 | 343 | 0.2213 | 0.2196 | +0.0017 ± 0.002 | 0.6286 | 0.6249 | 0.5137 | 0.4737 | 0.4665 | -0.115 ± 0.027 | 0.02 (1) |
| 5-10 | 746 | 0.2049 | 0.2044 | +0.0005 ± 0.0025 | 0.596 | 0.5936 | 0.5467 | 0.4719 | 0.508 | -0.081 ± 0.0171 | -0.01 (4) |
| 10-15 | 695 | 0.2174 | 0.2092 | +0.0083 ± 0.0043 | 0.6245 | 0.6039 | 0.5655 | 0.4412 | 0.4719 | -0.111 ± 0.018 | -0.04 (5) |
| 15-25 | 985 | 0.2297 | 0.2098 | +0.0199 ± 0.0057 | 0.6523 | 0.6024 | 0.588 | 0.392 | 0.4437 | -0.100 ± 0.0149 | -0.0133 (9) |
| 25-40 | 698 | 0.2613 | 0.1987 | +0.0625 ± 0.0106 | 0.7292 | 0.5782 | 0.6531 | 0.3374 | 0.3983 | -0.110 ± 0.0165 | -0.0075 (4) |
| 40+ | 264 | 0.359 | 0.1738 | +0.1852 ± 0.0253 | 0.9879 | 0.5189 | 0.7331 | 0.2485 | 0.3144 | -0.070 ± 0.0246 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2652 | 0.1929 | 0.1931 | -0.0002 ± 0.0003 | 0.5627 | 0.563 | 0.5092 | 0.4943 | 0.5079 | -0.045 ± 0.0088 | -0.0133 (15) |
| 3-5 | 1787 | 0.1974 | 0.1969 | +0.0006 ± 0.0008 | 0.5726 | 0.5706 | 0.514 | 0.4741 | 0.4857 | -0.042 ± 0.0107 | 0.02 (1) |
| 5-10 | 3964 | 0.1936 | 0.1922 | +0.0014 ± 0.001 | 0.5712 | 0.563 | 0.5065 | 0.4324 | 0.4624 | -0.030 ± 0.007 | -0.0117 (6) |
| 10-15 | 3481 | 0.1996 | 0.1863 | +0.0133 ± 0.0018 | 0.5858 | 0.5445 | 0.5122 | 0.3882 | 0.3976 | -0.060 ± 0.0074 | -0.0189 (18) |
| 15-25 | 4839 | 0.216 | 0.1778 | +0.0382 ± 0.0024 | 0.6279 | 0.5233 | 0.5257 | 0.3297 | 0.3337 | -0.070 ± 0.0061 | -0.0086 (42) |
| 25-40 | 4431 | 0.2508 | 0.139 | +0.1118 ± 0.0036 | 0.7064 | 0.4255 | 0.5579 | 0.2412 | 0.2257 | -0.082 ± 0.0056 | -0.0044 (18) |
| 40+ | 3492 | 0.3951 | 0.0623 | +0.3328 ± 0.0048 | 1.0403 | 0.2213 | 0.6528 | 0.1205 | 0.0871 | -0.071 ± 0.0041 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 588 | 0.2003 | 0.2025 | -0.0023 ± 0.0007 | 0.5817 | 0.5872 | 0.4982 | 0.483 | 0.5493 | -0.025 ± 0.0191 | -0.0137 (8) |
| 3-5 | 421 | 0.1998 | 0.198 | +0.0018 ± 0.0018 | 0.5812 | 0.5755 | 0.505 | 0.4653 | 0.4632 | -0.117 ± 0.0225 | 0.0067 (3) |
| 5-10 | 881 | 0.1996 | 0.1963 | +0.0034 ± 0.0023 | 0.5856 | 0.5734 | 0.5068 | 0.4328 | 0.4449 | -0.100 ± 0.0153 | -0.0071 (7) |
| 10-15 | 732 | 0.2087 | 0.2052 | +0.0035 ± 0.0042 | 0.6064 | 0.5927 | 0.5387 | 0.415 | 0.4645 | -0.086 ± 0.0166 | -0.0317 (6) |
| 15-25 | 900 | 0.23 | 0.2118 | +0.0182 ± 0.006 | 0.6579 | 0.6066 | 0.5865 | 0.392 | 0.4411 | -0.110 ± 0.0152 | -0.03 (1) |
| 25-40 | 566 | 0.2137 | 0.2171 | -0.0035 ± 0.0115 | 0.615 | 0.62 | 0.667 | 0.3552 | 0.5141 | -0.052 ± 0.0176 | 0.015 (2) |
| 40+ | 117 | 0.2943 | 0.2089 | +0.0855 ± 0.037 | 0.81 | 0.6049 | 0.7643 | 0.314 | 0.453 | -0.074 ± 0.0382 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3104 | 0.1857 | 0.1863 | -0.0006 ± 0.0003 | 0.5461 | 0.5471 | 0.4909 | 0.4758 | 0.4923 | -0.036 ± 0.0078 | -0.0163 (35) |
| 3-5 | 2084 | 0.1928 | 0.1903 | +0.0025 ± 0.0008 | 0.5671 | 0.5593 | 0.4886 | 0.4489 | 0.4386 | -0.070 ± 0.0098 | -0.0094 (18) |
| 5-10 | 4559 | 0.1944 | 0.1882 | +0.0062 ± 0.001 | 0.5727 | 0.5525 | 0.4837 | 0.4097 | 0.4047 | -0.064 ± 0.0065 | -0.01 (31) |
| 10-15 | 3729 | 0.1909 | 0.1747 | +0.0162 ± 0.0017 | 0.5653 | 0.517 | 0.4961 | 0.3726 | 0.3682 | -0.069 ± 0.0068 | -0.015 (12) |
| 15-25 | 5013 | 0.2098 | 0.1713 | +0.0385 ± 0.0023 | 0.6133 | 0.5059 | 0.512 | 0.317 | 0.3154 | -0.073 ± 0.0058 | -0.03 (2) |
| 25-40 | 3766 | 0.2198 | 0.1349 | +0.0849 ± 0.0038 | 0.6339 | 0.4086 | 0.5376 | 0.2216 | 0.2469 | -0.048 ± 0.0058 | 0.01 (3) |
| 40+ | 2391 | 0.3951 | 0.0503 | +0.3448 ± 0.0052 | 1.0323 | 0.188 | 0.6451 | 0.1141 | 0.0686 | -0.082 ± 0.0044 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 970 | 0.1939 | 0.194 | -0.0002 ± 0.0005 | 0.5667 | 0.5666 | 0.506 | 0.4909 | 0.4959 | -0.058 ± 0.0143 | -0.0224 (49) |
| 3-5 | 674 | 0.1911 | 0.1905 | +0.0007 ± 0.0014 | 0.5594 | 0.5565 | 0.4874 | 0.4476 | 0.457 | -0.056 ± 0.0172 | -0.0194 (34) |
| 5-10 | 1410 | 0.2007 | 0.1944 | +0.0062 ± 0.0018 | 0.5905 | 0.5709 | 0.4962 | 0.4228 | 0.4184 | -0.074 ± 0.0119 | -0.005 (78) |
| 10-15 | 933 | 0.2096 | 0.1985 | +0.0111 ± 0.0036 | 0.6085 | 0.5791 | 0.5192 | 0.396 | 0.4105 | -0.066 ± 0.0149 | 0.0014 (64) |
| 15-25 | 1251 | 0.2306 | 0.2097 | +0.0209 ± 0.0051 | 0.6588 | 0.6043 | 0.575 | 0.38 | 0.4253 | -0.070 ± 0.013 | -0.0214 (59) |
| 25-40 | 769 | 0.2482 | 0.207 | +0.0412 ± 0.0101 | 0.7049 | 0.5951 | 0.6703 | 0.3579 | 0.4473 | -0.086 ± 0.0154 | -0.0219 (26) |
| 40+ | 257 | 0.3553 | 0.1958 | +0.1595 ± 0.0273 | 1.0249 | 0.5732 | 0.808 | 0.3255 | 0.4202 | -0.099 ± 0.0249 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3165 | 0.1824 | 0.1826 | -0.0002 ± 0.0003 | 0.5376 | 0.5372 | 0.5065 | 0.4912 | 0.5024 | -0.037 ± 0.0076 | -0.0157 (88) |
| 3-5 | 2187 | 0.1917 | 0.19 | +0.0017 ± 0.0007 | 0.561 | 0.5569 | 0.4945 | 0.4547 | 0.4531 | -0.051 ± 0.0094 | -0.0209 (69) |
| 5-10 | 4386 | 0.1973 | 0.1888 | +0.0085 ± 0.001 | 0.5804 | 0.5553 | 0.4915 | 0.418 | 0.3997 | -0.072 ± 0.0066 | -0.0082 (132) |
| 10-15 | 3039 | 0.205 | 0.1893 | +0.0157 ± 0.002 | 0.5985 | 0.5571 | 0.5254 | 0.4023 | 0.3995 | -0.065 ± 0.0079 | -0.0053 (105) |
| 15-25 | 3821 | 0.2292 | 0.1994 | +0.0298 ± 0.0029 | 0.6613 | 0.5781 | 0.5678 | 0.3722 | 0.3947 | -0.064 ± 0.0073 | -0.0253 (107) |
| 25-40 | 2648 | 0.2596 | 0.1846 | +0.0750 ± 0.0053 | 0.7355 | 0.5383 | 0.631 | 0.317 | 0.3569 | -0.078 ± 0.0081 | -0.0229 (51) |
| 40+ | 1179 | 0.3782 | 0.1436 | +0.2346 ± 0.0116 | 1.0728 | 0.4331 | 0.7292 | 0.2256 | 0.257 | -0.073 ± 0.0104 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4205 | 1.044 ± 0.043 | 1.139 | 0.1688 | 0.1653 | 0.2133 | 0.2051 |
| gen2 | 4205 | 0.846 ± 0.04 | 1.096 | 0.1694 | 0.1659 | 0.2331 | 0.2048 |
| gen1_elo | 4205 | 1.018 ± 0.042 | 1.128 | 0.1756 | 0.1655 | 0.2123 | 0.2053 |
| gen1_sr | 4205 | 1.039 ± 0.052 | 1.167 | 0.1301 | 0.1678 | 0.2292 | 0.2044 |
| gen1_ledger | 6264 | 0.867 ± 0.03 | 1.082 | 0.1832 | 0.1794 | 0.2181 | 0.1992 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 20,913)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,806 | 23.0% |
| STALE_QUOTE | market_freshness | 4,553 | 21.8% |
| BOOK_QUALITY | execution | 3,887 | 18.6% |
| POOR_DATA | data | 2,390 | 11.4% |
| LIMITED_DATA | data | 1,310 | 6.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,133 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 983 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 894 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 617 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 339 | 1.6% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 23.0%, market_freshness 21.8%, execution 18.6%, data 17.7%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.7%, mapping 4.3%, model_calibration 1.6%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.8%, START_UNVERIFIABLE 94.4%, LOW_DATA_QUALITY 71.2%, THIN_PLAYER_HISTORY 60.1%, STALE_PLAYER_DATA 49.9%, STALE_KALSHI_QUOTE 44.4%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 33.5%, WIDE_SPREAD 24.7%, MODEL_HIGH_UNCERTAINTY 17.8%, PLAYER_IDENTITY_RISK 16.3%, LEVEL_TRANSFER_RISK 11.0%, LOW_DISPLAYED_LIQUIDITY 8.1%, EVENT_MAPPING_RISK 8.0%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.1%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.5%, POST_SETTLEMENT_OBSERVATION 23.0%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 11,188)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,855 | 34.5% |
| STALE_QUOTE | market_freshness | 2,095 | 18.7% |
| BOOK_QUALITY | execution | 2,026 | 18.1% |
| POOR_DATA | data | 991 | 8.9% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 608 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 511 | 4.6% |
| LIMITED_DATA | data | 400 | 3.6% |
| IN_PLAY_QUOTE | market_freshness/coverage | 388 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 236 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 77 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.5%, market_freshness 18.7%, execution 18.1%, data 12.4%, market_freshness/coverage 8.9%, mapping 4.6%, model_calibration_or_unknown 2.1%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.2%, LOW_DATA_QUALITY 74.8%, THIN_PLAYER_HISTORY 62.4%, STALE_KALSHI_QUOTE 52.3%, STALE_PLAYER_DATA 44.8%, MODEL_INTERNAL_DISAGREEMENT 42.5%, ASYMMETRIC_SAMPLE_SIZE 34.8%, WIDE_SPREAD 24.1%, PLAYER_IDENTITY_RISK 19.6%, MODEL_HIGH_UNCERTAINTY 18.0%, LEVEL_TRANSFER_RISK 9.8%, EVENT_MAPPING_RISK 9.6%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 1.8%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.5%, POST_SETTLEMENT_OBSERVATION 34.5%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 8713, "IDENTITY_AMBIGUOUS": 2475}; ticker orientation: {"VERIFIED": 11188}.

Checks: discipline:AMBIGUOUS 746, discipline:PASS 10442, identity_confidence:AMBIGUOUS 2197, identity_confidence:PASS 8991, level_mapping:NA 758, level_mapping:PASS 10430, market_pair:AMBIGUOUS 393, market_pair:NA 280, market_pair:PASS 10515, model_complement:NA 247, model_complement:PASS 10941, namesake:PASS 11188, physical_match_id:NA 3949, physical_match_id:PASS 7239, player_ids:PASS 11188, same_pair_other_event:PASS 11188, ticker_orientation:PASS 11188

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,923 | 4.8% | 4.3% | 1.7% | {"market_freshness": 53, "model_calibration_or_unknown": 43, "data": 35, "execution": 20, "market_freshness/coverage": 13, "model_calibration": 13, "coverage": 11} | 5.86 | 0.2191 / 0.2133 (453) | 19.1% | 3.8% | 3.2% | 2.8% |
| CHALLENGER | 7,695 | 17.2% | 6.9% | 11.8% | {"coverage": 751, "market_freshness/coverage": 163, "market_freshness": 148, "data": 131, "model_calibration_or_unknown": 59, "execution": 30, "model_calibration": 27, "mapping": 15, "possible_market_error": 1} | 7.43 | 0.2197 / 0.2079 (1850) | 35.1% | 17.6% | 3.8% | 22.7% |
| DOUBLES | 1,571 | 47.5% | 47.0% | 6.7% | {"execution": 382, "mapping": 198, "market_freshness": 106, "market_freshness/coverage": 53, "coverage": 7} | 23.85 | 0.3132 / 0.2358 (413) | 14.9% | 0.0% | 100.0% | 7.1% |
| ITF_MEN | 14,095 | 25.3% | 17.8% | 31.8% | {"coverage": 1311, "execution": 685, "market_freshness": 612, "data": 477, "market_freshness/coverage": 298, "mapping": 175, "model_calibration_or_unknown": 2, "model_calibration": 2} | 11.89 | 0.2146 / 0.1969 (3149) | 37.6% | 69.5% | 19.7% | 21.9% |
| ITF_WOMEN | 18,683 | 27.0% | 19.8% | 45.1% | {"coverage": 1753, "market_freshness": 1094, "execution": 878, "data": 714, "market_freshness/coverage": 420, "mapping": 117, "model_calibration_or_unknown": 63, "model_calibration": 11} | 12.85 | 0.202 / 0.1933 (3623) | 39.8% | 56.2% | 9.9% | 22.1% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,734 | 4.8% | 4.2% | 1.2% | {"market_freshness": 42, "model_calibration_or_unknown": 28, "execution": 17, "model_calibration": 13, "data": 11, "market_freshness/coverage": 10, "coverage": 9, "mapping": 1} | 7.74 | 0.2385 / 0.2306 (451) | 24.6% | 1.2% | 1.4% | 3.6% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.6% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 311 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 17.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1037 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 15 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 16 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 17 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 18 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 19 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 20 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 21 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 22 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 23 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 24 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 271 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 25 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 26 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 27 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 28 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 29 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 30 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 213 min (STALE); no external reference |
| 31 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 32 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 33 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 34 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 36 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 37 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 38 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 39 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 40 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 41 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 42 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 43 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 468 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 44 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 45 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 46 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 47 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 48 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 49 | `KXITFWMATCH-26OCT20CHAAPI-CHA` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 1143 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 122.0, ratio 20.3); no external reference |
| 50 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 246 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9716, "by_level_share_of_ge_25pp": {"ATP": 0.0168, "CHALLENGER": 0.1184, "DOUBLES": 0.0667, "ITF_MEN": 0.3184, "ITF_WOMEN": 0.4514, "OTHER": 0.0011, "WTA": 0.0117, "WTA125": 0.0156}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.523, "share_primary_cause_market_settled_or_in_play": 0.4336, "share_primary_cause_stale_quote_only": 0.1873}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 11188, "identity_ambiguous_share": 0.2212, "ticker_orientation": {"VERIFIED": 11188}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 7239, "with_external": 359, "coverage": 0.0496, "external_status": {"EXTERNAL_STALE": 220, "AGREES_WITH_KALSHI": 131, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 220, "MODEL_LONE_OUTLIER": 131, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3649, "share_external_supports_model": 0.0223}, "pregame_clean_ge_25pp": {"n": 3540, "with_external": 336, "coverage": 0.0949, "external_status": {"EXTERNAL_STALE": 204, "AGREES_WITH_KALSHI": 124, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 204, "MODEL_LONE_OUTLIER": 124, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.369, "share_external_supports_model": 0.0238}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 479.0, "median_sample_ratio": 2.45, "median_min_matches": 20.0, "median_max_days_since_last": 226.0, "share_severe_asymmetry": 0.2146, "data_status": {"POOR": 6272, "LIMITED": 2945, "ADEQUATE": 1971}, "comparison_lt_10pp": {"median_thinner_serve_points": 1667.0, "median_sample_ratio": 1.71, "median_min_matches": 92.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 834, "model_minus_observed": 0.0473, "kalshi_minus_observed": -0.0912, "brier_diff_model_minus_kalshi": -0.0036}, "4-10x": {"n": 567, "model_minus_observed": 0.0939, "kalshi_minus_observed": -0.0523, "brier_diff_model_minus_kalshi": 0.0132}, "<2x": {"n": 2051, "model_minus_observed": 0.0911, "kalshi_minus_observed": -0.033, "brier_diff_model_minus_kalshi": 0.0122}, ">=10x": {"n": 753, "model_minus_observed": 0.1064, "kalshi_minus_observed": -0.0699, "brier_diff_model_minus_kalshi": 0.0065}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4205, "model": {"intercept": -0.549, "slope": 0.846, "slope_se": 0.04}, "kalshi_mid_same_rows": {"intercept": 0.216, "slope": 1.096, "slope_se": 0.045}, "mean_extremity_model": 0.1694, "mean_extremity_kalshi": 0.1659, "model_brier": 0.2331, "kalshi_brier": 0.2048, "brier_diff_model_minus_kalshi": 0.0282, "brier_diff_se": 0.0029, "model_logloss": 0.6626, "kalshi_logloss": 0.5923}, "fair_v1": {"n": 4205, "model": {"intercept": -0.413, "slope": 1.044, "slope_se": 0.043}, "kalshi_mid_same_rows": {"intercept": 0.31, "slope": 1.139, "slope_se": 0.045}, "mean_extremity_model": 0.1688, "mean_extremity_kalshi": 0.1653, "model_brier": 0.2133, "kalshi_brier": 0.2051, "brier_diff_model_minus_kalshi": 0.0082, "brier_diff_se": 0.0024, "model_logloss": 0.6152, "kalshi_logloss": 0.5927}, "gen1_elo": {"n": 4205, "model": {"intercept": -0.398, "slope": 1.018, "slope_se": 0.042}, "kalshi_mid_same_rows": {"intercept": 0.318, "slope": 1.128, "slope_se": 0.045}, "mean_extremity_model": 0.1756, "mean_extremity_kalshi": 0.1655, "model_brier": 0.2123, "kalshi_brier": 0.2053, "brier_diff_model_minus_kalshi": 0.007, "brier_diff_se": 0.0024, "model_logloss": 0.6139, "kalshi_logloss": 0.5932}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2481, "share_ge_15": 0.4465, "median_abs_gap": 13.19, "n": 29174}, "gen1_elo": {"share_ge_25": 0.2456, "share_ge_15": 0.4455, "median_abs_gap": 13.02, "n": 29174}, "gen1_sr": {"share_ge_25": 0.3172, "share_ge_15": 0.5272, "median_abs_gap": 16.09, "n": 29174}, "gen2": {"share_ge_25": 0.32, "share_ge_15": 0.515, "median_abs_gap": 15.65, "n": 29174}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1563, "share_ge_15": 0.3634, "median_abs_gap": 10.98, "n": 22646}, "gen1_elo": {"share_ge_25": 0.1577, "share_ge_15": 0.3607, "median_abs_gap": 10.79, "n": 22643}, "gen1_sr": {"share_ge_25": 0.2246, "share_ge_15": 0.4501, "median_abs_gap": 13.29, "n": 22647}, "gen2": {"share_ge_25": 0.2401, "share_ge_15": 0.4478, "median_abs_gap": 13.16, "n": 22648}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.86, "share_ge_25_all": 0.0479, "share_ge_25_pregame_clean": 0.043}, "WTA": {"median_abs_gap_pregame_clean": 7.74, "share_ge_25_all": 0.0479, "share_ge_25_pregame_clean": 0.0425}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2337, "share_within_10pp_all": 0.4307, "share_within_10pp_pregame_clean": 0.4835, "corr_model_vs_mid_pregame_clean": 0.8443}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 614, "model_brier": 0.1993, "kalshi_brier": 0.2004, "brier_diff_model_minus_kalshi": -0.001}, "10-15": {"n_settled": 726, "model_brier": 0.2133, "kalshi_brier": 0.2038, "brier_diff_model_minus_kalshi": 0.0094}, "15-25": {"n_settled": 959, "model_brier": 0.2238, "kalshi_brier": 0.2132, "brier_diff_model_minus_kalshi": 0.0106}, "25-40": {"n_settled": 547, "model_brier": 0.2243, "kalshi_brier": 0.2091, "brier_diff_model_minus_kalshi": 0.0152}, "3-5": {"n_settled": 391, "model_brier": 0.2019, "kalshi_brier": 0.2012, "brier_diff_model_minus_kalshi": 0.0007}, "40+": {"n_settled": 112, "model_brier": 0.2783, "kalshi_brier": 0.1982, "brier_diff_model_minus_kalshi": 0.08}, "5-10": {"n_settled": 856, "model_brier": 0.2012, "kalshi_brier": 0.2006, "brier_diff_model_minus_kalshi": 0.0005}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.549, "slope": 0.846, "slope_se": 0.04}, "kalshi_slope": {"intercept": 0.216, "slope": 1.096, "slope_se": 0.045}, "n": 4205}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.51, "slope": 0.867, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.16, "slope": 1.082, "slope_se": 0.035}, "n": 6264}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 413, "model_brier": 0.3132, "kalshi_brier": 0.2358, "brier_diff_model_minus_kalshi": 0.0773, "brier_diff_se": 0.0151, "corr_model_outcome": 0.0325, "corr_kalshi_outcome": 0.2537}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
