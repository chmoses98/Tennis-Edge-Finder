# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-06T05:58Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 17,447): 0-3 13.4%, 3-5 9.5%, 5-10 19.5%, 10-15 15.2%, 15-25 18.8%, 25-40 14.7%, 40+ 8.8%; median gap 12.27 pp.
* **Where the extremes live**: 97.5% of >=25 pp gaps are off the ATP/WTA main tour (ITF 75.9%, Challenger 14.0%, doubles 4.8%). Main tour: ATP 2.6% and WTA 8.8% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 4,096): MARKET_ALREADY_SETTLED_WHEN_PRICED 41.0%, STALE_QUOTE 21.0%, BOOK_QUALITY 13.8%, POOR_DATA 8.3%, POSSIBLY_IN_PLAY_QUOTE 4.6%, IN_PLAY_QUOTE 3.1%, LIMITED_DATA 3.0%, IDENTITY_AMBIGUOUS 2.8%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.1%. By class: coverage 41.0%, market_freshness 21.0%, execution 13.8%, data 11.4%, market_freshness/coverage 7.7%, mapping 2.8%, model_calibration_or_unknown 2.2%, model_calibration 0.1%.
* **Stale / settled / in-play**: 61.4% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 48.6% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 4,096 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 16.1% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 1.7%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 7.6% of the time and with the model 0.2%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 600.0 points vs 1856.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.12, Gen-2 0.913, Gen-1 ledger 0.9 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 135 model 0.2265 vs Kalshi 0.1774; n 30 model 0.3354 vs Kalshi 0.1357.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 62,637 model-market comparisons (106,105 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 25,608 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-06T05:54:24.497528+00:00'], shadow board 17,545 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-06T05:54:27.251266+00:00'], Model 4 5,821 rows, 8,818 settled tickers, 2,140 tickers with an external scan.
* By model: {"gen1_ledger": 16000, "gen1_elo": 8810, "fair_v1": 8810, "gen2": 8810, "gen1_sr": 8810, "model4_fundamental": 5703, "model4_conditioned": 5694}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 17,447 | 13.4 | 9.5 | 19.5 | 15.2 | 18.8 | 14.7 | 8.8 | 12.27 | 42.2% | 23.5% |
| MW fair_v1 | 8,810 | 12.9 | 9.2 | 18.4 | 15.6 | 18.1 | 15.5 | 10.3 | 13.0 | 44.0% | 25.9% |
| MW gen1_elo | 8,810 | 12.8 | 8.8 | 19.9 | 14.7 | 19.0 | 15.0 | 9.7 | 12.57 | 43.7% | 24.7% |
| MW gen1_ledger | 8,637 | 14.0 | 9.9 | 20.7 | 14.9 | 19.4 | 13.9 | 7.1 | 11.63 | 40.4% | 21.0% |
| MW gen1_sr | 8,810 | 9.7 | 7.7 | 16.1 | 14.1 | 21.8 | 18.5 | 12.1 | 15.92 | 52.4% | 30.6% |
| MW gen2 | 8,810 | 11.1 | 7.0 | 16.5 | 14.4 | 19.9 | 17.4 | 13.8 | 15.48 | 51.1% | 31.1% |
| all families model4_conditioned | 5,694 | 21.4 | 19.6 | 32.5 | 17.5 | 6.7 | 1.3 | 1.2 | 6.04 | 9.1% | 2.4% |
| all families model4_fundamental | 5,703 | 16.2 | 12.8 | 32.8 | 20.2 | 12.0 | 4.2 | 1.7 | 7.96 | 17.9% | 5.9% |

Configurable thresholds (primary): >=5pp 77.0%, >=10pp 57.5%, >=15pp 42.2%, >=20pp 32.0%, >=25pp 23.5%, >=30pp 17.2%, >=40pp 8.8%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.99pp; >=10pp 47.0%, >=25pp 19.4%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 578 | 23.7 | 19.0 | 25.4 | 15.7 | 12.1 | 2.1 | 1.9 | 5.88 | 16.1% | 4.0% |
| CHALLENGER | 1,778 | 14.5 | 11.0 | 18.0 | 16.2 | 13.8 | 13.4 | 13.1 | 12.07 | 40.3% | 26.4% |
| ITF_MEN | 2,436 | 10.9 | 8.6 | 18.7 | 14.3 | 18.1 | 16.4 | 12.9 | 13.77 | 47.4% | 29.3% |
| ITF_WOMEN | 3,305 | 10.1 | 6.8 | 16.2 | 15.4 | 21.7 | 19.7 | 10.1 | 15.77 | 51.6% | 29.8% |
| WTA | 484 | 22.3 | 10.3 | 24.6 | 14.9 | 18.8 | 6.8 | 2.3 | 8.38 | 27.9% | 9.1% |
| WTA125 | 229 | 14.4 | 7.9 | 17.9 | 26.6 | 14.0 | 15.7 | 3.5 | 11.31 | 33.2% | 19.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 578 | 18.9 | 15.7 | 27.3 | 17.1 | 15.1 | 3.6 | 2.2 | 6.92 | 20.9% | 5.9% |
| CHALLENGER | 1,778 | 14.3 | 6.8 | 18.0 | 13.9 | 18.9 | 15.3 | 12.8 | 13.76 | 47.0% | 28.1% |
| ITF_MEN | 2,436 | 9.6 | 7.0 | 16.5 | 15.0 | 19.5 | 17.9 | 14.4 | 15.59 | 51.8% | 32.3% |
| ITF_WOMEN | 3,305 | 8.1 | 6.2 | 13.7 | 12.8 | 21.4 | 20.4 | 17.5 | 18.89 | 59.3% | 37.9% |
| WTA | 484 | 20.7 | 5.2 | 16.5 | 15.7 | 21.9 | 17.8 | 2.3 | 13.18 | 41.9% | 20.0% |
| WTA125 | 229 | 6.1 | 2.2 | 17.5 | 23.1 | 20.5 | 17.5 | 13.1 | 15.79 | 51.1% | 30.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 578 | 24.6 | 12.6 | 30.3 | 15.9 | 9.3 | 5.2 | 2.1 | 7.34 | 16.6% | 7.3% |
| CHALLENGER | 1,778 | 16.0 | 10.6 | 21.3 | 13.4 | 13.5 | 12.1 | 13.1 | 10.53 | 38.7% | 25.2% |
| ITF_MEN | 2,436 | 9.4 | 8.7 | 18.4 | 14.5 | 19.8 | 16.4 | 12.8 | 14.48 | 49.1% | 29.2% |
| ITF_WOMEN | 3,305 | 9.7 | 6.5 | 16.2 | 15.2 | 24.2 | 19.5 | 8.8 | 16.32 | 52.5% | 28.3% |
| WTA | 484 | 22.3 | 13.4 | 33.7 | 14.9 | 10.3 | 3.9 | 1.4 | 7.04 | 15.7% | 5.4% |
| WTA125 | 229 | 21.4 | 10.5 | 24.9 | 17.9 | 19.2 | 5.2 | 0.9 | 8.06 | 25.3% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 315 | 29.2 | 20.3 | 37.8 | 11.1 | 1.6 | 0.0 | 0.0 | 5.11 | 1.6% | 0.0% |
| CHALLENGER | 1,238 | 21.6 | 15.5 | 26.7 | 14.9 | 12.9 | 6.1 | 2.3 | 7.06 | 21.3% | 8.4% |
| DOUBLES | 446 | 4.9 | 3.4 | 12.3 | 11.4 | 23.8 | 20.4 | 23.8 | 22.7 | 67.9% | 44.2% |
| ITF_MEN | 2,683 | 13.8 | 8.4 | 18.5 | 15.1 | 20.5 | 14.5 | 9.3 | 12.76 | 44.2% | 23.7% |
| ITF_WOMEN | 2,968 | 9.9 | 8.6 | 17.9 | 14.4 | 23.1 | 19.0 | 7.1 | 14.6 | 49.2% | 26.0% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 412 | 18.7 | 9.7 | 26.5 | 20.1 | 16.5 | 7.8 | 0.7 | 9.03 | 25.0% | 8.5% |
| WTA125 | 426 | 14.3 | 11.0 | 22.1 | 19.9 | 19.2 | 10.3 | 3.0 | 10.39 | 32.6% | 13.4% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 577 | 23.6 | 19.1 | 25.5 | 15.8 | 12.1 | 2.1 | 1.9 | 5.88 | 16.1% | 4.0% |
| CHALLENGER | 1,276 | 18.5 | 13.6 | 22.7 | 19.0 | 15.1 | 7.7 | 3.5 | 8.77 | 26.2% | 11.1% |
| ITF_MEN | 1,738 | 13.3 | 11.2 | 22.1 | 15.5 | 18.2 | 13.1 | 6.7 | 10.83 | 37.9% | 19.7% |
| ITF_WOMEN | 2,408 | 12.5 | 8.6 | 18.9 | 17.2 | 23.2 | 15.9 | 3.6 | 12.94 | 42.8% | 19.6% |
| WTA | 483 | 22.4 | 10.3 | 24.6 | 14.9 | 18.8 | 6.6 | 2.3 | 8.36 | 27.7% | 8.9% |
| WTA125 | 223 | 14.8 | 8.1 | 18.4 | 27.4 | 13.9 | 15.2 | 2.2 | 11.31 | 31.4% | 17.5% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 577 | 18.9 | 15.6 | 27.4 | 17.2 | 15.1 | 3.6 | 2.2 | 6.93 | 21.0% | 5.9% |
| CHALLENGER | 1,276 | 18.3 | 8.6 | 22.3 | 17.0 | 20.0 | 10.9 | 3.0 | 10.09 | 33.9% | 13.9% |
| ITF_MEN | 1,738 | 12.1 | 8.3 | 19.3 | 16.8 | 20.2 | 15.0 | 8.3 | 12.87 | 43.5% | 23.2% |
| ITF_WOMEN | 2,408 | 9.5 | 7.4 | 15.3 | 13.3 | 23.6 | 19.2 | 11.6 | 16.81 | 54.5% | 30.9% |
| WTA | 483 | 20.7 | 5.2 | 16.6 | 15.7 | 21.9 | 17.6 | 2.3 | 13.18 | 41.8% | 19.9% |
| WTA125 | 223 | 6.3 | 2.2 | 17.5 | 23.8 | 21.1 | 17.9 | 11.2 | 15.33 | 50.2% | 29.1% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 305 | 29.5 | 21.0 | 38.0 | 11.2 | 0.3 | 0.0 | 0.0 | 4.98 | 0.3% | 0.0% |
| CHALLENGER | 1,040 | 23.6 | 17.6 | 29.3 | 14.5 | 12.4 | 2.5 | 0.1 | 6.37 | 15.0% | 2.6% |
| DOUBLES | 403 | 5.0 | 3.2 | 12.7 | 11.4 | 24.1 | 20.6 | 23.1 | 22.7 | 67.7% | 43.7% |
| ITF_MEN | 2,066 | 16.0 | 9.6 | 20.8 | 16.3 | 20.4 | 11.9 | 5.0 | 11.21 | 37.3% | 16.9% |
| ITF_WOMEN | 2,280 | 11.4 | 9.8 | 20.4 | 15.7 | 23.6 | 16.8 | 2.4 | 12.27 | 42.8% | 19.2% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 382 | 19.1 | 10.2 | 27.2 | 20.4 | 17.0 | 6.0 | 0.0 | 8.75 | 23.0% | 6.0% |
| WTA125 | 346 | 16.5 | 12.1 | 25.1 | 23.1 | 17.3 | 5.5 | 0.3 | 9.13 | 23.1% | 5.8% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 446 | 4.9 | 3.4 | 12.3 | 11.4 | 23.8 | 20.4 | 23.8 | 22.7 | 67.9% | 44.2% |
| singles | 8,191 | 14.5 | 10.3 | 21.2 | 15.1 | 19.2 | 13.6 | 6.2 | 11.19 | 38.9% | 19.8% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 2,063 | 13.7 | 9.7 | 19.1 | 15.8 | 15.8 | 14.4 | 11.4 | 12.37 | 41.7% | 25.9% |
| Hard | 6,003 | 12.6 | 9.2 | 18.4 | 15.3 | 19.0 | 15.6 | 9.9 | 13.11 | 44.5% | 25.4% |
| UNKNOWN | 744 | 12.8 | 7.8 | 15.7 | 16.8 | 17.3 | 18.3 | 11.3 | 13.67 | 46.9% | 29.6% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 2,624 | 17.3 | 11.6 | 20.3 | 16.4 | 14.9 | 10.7 | 8.8 | 10.29 | 34.4% | 19.5% |
| B | 1,168 | 15.8 | 10.0 | 20.2 | 17.7 | 15.9 | 10.4 | 9.8 | 10.91 | 36.2% | 20.3% |
| C | 1,310 | 12.8 | 10.8 | 20.8 | 13.9 | 17.2 | 14.9 | 9.5 | 12.24 | 41.7% | 24.4% |
| D | 1,590 | 11.1 | 8.8 | 16.4 | 15.0 | 22.6 | 15.8 | 10.1 | 14.17 | 48.6% | 26.0% |
| F | 2,118 | 7.2 | 4.9 | 14.9 | 14.7 | 20.5 | 24.6 | 13.2 | 18.87 | 58.3% | 37.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 2,575 | 20.5 | 13.6 | 27.1 | 16.5 | 13.9 | 5.9 | 2.5 | 7.69 | 22.2% | 8.4% |
| B | 1,280 | 14.4 | 9.5 | 22.7 | 16.1 | 19.0 | 11.8 | 6.6 | 11.11 | 37.3% | 18.4% |
| C | 1,629 | 11.4 | 8.1 | 17.9 | 14.6 | 22.5 | 14.9 | 10.6 | 14.15 | 48.0% | 25.5% |
| D | 1,378 | 12.1 | 8.3 | 21.1 | 13.1 | 22.1 | 16.6 | 6.8 | 13.04 | 45.4% | 23.4% |
| F | 1,775 | 8.2 | 7.7 | 12.3 | 13.6 | 22.9 | 24.0 | 11.3 | 18.11 | 58.2% | 35.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 3,094 | 16.5 | 10.8 | 19.5 | 17.1 | 15.3 | 10.8 | 10.1 | 10.91 | 36.1% | 20.8% |
| LIMITED | 1,982 | 14.6 | 11.4 | 22.1 | 14.5 | 16.1 | 13.2 | 8.0 | 10.7 | 37.4% | 21.2% |
| POOR | 3,734 | 9.0 | 6.6 | 15.4 | 14.8 | 21.6 | 20.7 | 11.8 | 16.9 | 54.1% | 32.6% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,325 | 30.5 | 26.9 | 35.9 | 5.0 | 1.5 | 0.2 | 0.0 | 4.35 | 1.7% | 0.2% |
| GAME_SPREAD | 1,133 | 23.2 | 15.9 | 37.2 | 17.7 | 5.3 | 0.4 | 0.3 | 6.18 | 6.0% | 0.7% |
| MATCH_WINNER | 8,637 | 14.0 | 9.9 | 20.7 | 14.9 | 19.4 | 13.9 | 7.1 | 11.63 | 40.4% | 21.0% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 2,882 | 27.9 | 18.5 | 31.1 | 12.0 | 8.5 | 1.6 | 0.4 | 5.47 | 10.5% | 2.0% |
| TOTAL_GAMES | 1,999 | 8.4 | 9.7 | 34.4 | 27.4 | 12.6 | 4.5 | 3.1 | 9.65 | 20.2% | 7.6% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,052 | 26.6 | 37.7 | 25.6 | 0.3 | 8.7 | 0.8 | 0.3 | 4.29 | 9.8% | 1.1% |
| GAME_SPREAD | 1,351 | 42.9 | 14.9 | 28.2 | 11.3 | 1.5 | 0.9 | 0.3 | 3.85 | 2.7% | 1.2% |
| TOTAL_GAMES | 2,291 | 4.1 | 6.1 | 41.1 | 36.5 | 7.9 | 1.9 | 2.4 | 9.88 | 12.3% | 4.4% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,052 | 25.9 | 17.8 | 33.8 | 8.9 | 8.6 | 4.2 | 0.7 | 5.62 | 13.6% | 4.9% |
| GAME_SPREAD | 1,351 | 18.1 | 13.1 | 27.7 | 23.3 | 12.7 | 4.0 | 1.1 | 8.44 | 17.8% | 5.1% |
| TOTAL_GAMES | 2,300 | 6.3 | 8.3 | 35.0 | 28.4 | 14.6 | 4.4 | 2.9 | 10.04 | 22.0% | 7.3% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 8,810 | 44.0% | 25.9% | 13.0 | 34.6% | 15.8% | 10.47 |
| gen1_elo | 8,810 | 43.7% | 24.7% | 12.57 | 33.9% | 15.2% | 10.07 |
| gen1_sr | 8,810 | 52.4% | 30.6% | 15.92 | 44.0% | 20.5% | 13.14 |
| gen2 | 8,810 | 51.1% | 31.1% | 15.48 | 43.8% | 22.7% | 12.85 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 4,036 | 15.5 | 12.4 | 21.9 | 16.1 | 18.2 | 12.0 | 3.8 | 10.0 | 34.0% | 15.8% |
| STALE | 4,774 | 10.7 | 6.4 | 15.3 | 15.1 | 18.1 | 18.5 | 15.9 | 16.48 | 52.5% | 34.4% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 2,105 | 16.8 | 11.0 | 23.8 | 15.5 | 16.1 | 13.2 | 3.6 | 9.71 | 32.9% | 16.8% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 17,447 | 2105 | 7508 | 7834 | 28.1 | 173.9 | 1400.4 |
| ge_15pp | 7,371 | 693 | 2660 | 4018 | 33.0 | 430.2 | 1380.4 |
| ge_25pp | 4,096 | 353 | 1229 | 2514 | 43.5 | 545.7 | 1380.4 |
| lt_10pp | 7,415 | 1085 | 3646 | 2684 | 25.6 | 54.4 | 1201.9 |

Current slate `SL-20261006T055836Z-6ebae9e2`: 1047 priced rows, quote age at build {'median': 4.6, 'max': 4.7}, freshness {'FRESH': 1047}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 400 | 18.2 | 12.8 | 27.5 | 21.0 | 12.2 | 8.0 | 0.2 | 7.79 | 20.5% | 8.2% |
| KALSHI_LONE_OUTLIER | 1 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 7.99 | 0.0% | 0.0% |
| MARKETS_AGREE | 22 | 59.1 | 40.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.35 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 35 | 0.0 | 2.9 | 31.4 | 37.1 | 14.3 | 14.3 | 0.0 | 11.9 | 28.6% | 14.3% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 8,810 | 459 (5.2%) | 7.6% | 0.2% | {"EXTERNAL_STALE": 400, "AGREES_WITH_KALSHI": 35, "ALL_AGREE": 22, "EXTERNAL_OUTLIER": 1, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_15pp | 3,879 | 92 (2.4%) | 10.9% | 0.0% | {"EXTERNAL_STALE": 82, "AGREES_WITH_KALSHI": 10} |
| fair_v1_ge_25pp | 2,281 | 38 (1.7%) | 13.2% | 0.0% | {"EXTERNAL_STALE": 33, "AGREES_WITH_KALSHI": 5} |
| fair_v1_ge_25pp_pregame_clean | 1,061 | 38 (3.6%) | 13.2% | 0.0% | {"EXTERNAL_STALE": 33, "AGREES_WITH_KALSHI": 5} |
| fair_v1_lt_10pp | 3,561 | 270 (7.6%) | 4.4% | 0.4% | {"EXTERNAL_STALE": 234, "ALL_AGREE": 22, "AGREES_WITH_KALSHI": 12, "EXTERNAL_OUTLIER": 1, "AGREES_WITH_MODEL": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 1,763 | 10.6 | 8.9 | 20.8 | 15.0 | 21.0 | 14.5 | 9.2 | 12.82 | 44.8% | 23.7% |
| 4-10x | 1,259 | 12.2 | 10.9 | 17.4 | 14.1 | 18.6 | 17.6 | 9.4 | 13.25 | 45.5% | 26.9% |
| <2x | 4,699 | 14.6 | 9.8 | 18.6 | 16.3 | 16.8 | 13.8 | 10.2 | 12.14 | 40.7% | 24.0% |
| >=10x | 1,089 | 10.1 | 5.0 | 14.7 | 14.9 | 18.9 | 22.6 | 13.9 | 17.69 | 55.4% | 36.5% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 2,242 | 14.0 | 9.0 | 20.9 | 15.9 | 16.5 | 12.3 | 11.4 | 11.77 | 40.2% | 23.7% |
| 300-1000 | 2,047 | 12.2 | 10.0 | 16.9 | 15.0 | 20.8 | 16.1 | 8.9 | 13.58 | 45.8% | 25.0% |
| <300 | 2,466 | 8.3 | 6.0 | 14.8 | 14.4 | 20.7 | 22.7 | 13.1 | 18.15 | 56.5% | 35.8% |
| >=3000 | 2,055 | 17.9 | 12.4 | 21.3 | 17.1 | 14.2 | 9.9 | 7.3 | 9.65 | 31.4% | 17.2% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 258 | 0.5202 | 0.39 | 0.438 | +0.082 | -0.048 | 0.0067 ± 0.0087 |
| ratio 4-10x | 179 | 0.578 | 0.4416 | 0.4804 | +0.098 | -0.039 | 0.0162 ± 0.011 |
| ratio <2x | 518 | 0.5346 | 0.4107 | 0.4633 | +0.071 | -0.053 | 0.0129 ± 0.0062 |
| ratio >=10x | 178 | 0.5544 | 0.3821 | 0.4607 | +0.094 | -0.079 | 0.0145 ± 0.014 |
| thinner_sample 1000-3000 | 297 | 0.5411 | 0.4217 | 0.4579 | +0.083 | -0.036 | 0.0092 ± 0.008 |
| thinner_sample 300-1000 | 305 | 0.5559 | 0.4245 | 0.4787 | +0.077 | -0.054 | 0.0052 ± 0.0083 |
| thinner_sample <300 | 378 | 0.5404 | 0.3756 | 0.4497 | +0.091 | -0.074 | 0.0193 ± 0.009 |
| thinner_sample >=3000 | 153 | 0.5148 | 0.4164 | 0.451 | +0.064 | -0.035 | 0.0148 ± 0.009 |
| data_status ADEQUATE | 330 | 0.5276 | 0.4195 | 0.4545 | +0.073 | -0.035 | 0.0079 ± 0.0068 |
| data_status LIMITED | 233 | 0.5531 | 0.4283 | 0.4936 | +0.059 | -0.065 | 0.0037 ± 0.0095 |
| data_status POOR | 570 | 0.5444 | 0.3898 | 0.4491 | +0.095 | -0.059 | 0.0183 ± 0.0069 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 177 | 0.1816 | 0.1825 | -0.0009 ± 0.0011 | 0.5382 | 0.5406 | 0.4955 | 0.4812 | 0.4915 | -0.094 ± 0.0346 | -0.01 (3) |
| 3-5 | 113 | 0.1755 | 0.1765 | -0.0010 ± 0.0033 | 0.5301 | 0.5289 | 0.5149 | 0.4742 | 0.5044 | -0.067 ± 0.041 | 0.02 (1) |
| 5-10 | 232 | 0.1957 | 0.2021 | -0.0064 ± 0.0044 | 0.5768 | 0.5922 | 0.5177 | 0.4439 | 0.5172 | -0.041 ± 0.0297 | -0.0167 (3) |
| 10-15 | 197 | 0.2187 | 0.2146 | +0.0041 ± 0.0082 | 0.6238 | 0.6119 | 0.5198 | 0.396 | 0.4416 | -0.071 ± 0.0328 | -0.0633 (3) |
| 15-25 | 249 | 0.2178 | 0.209 | +0.0088 ± 0.0114 | 0.6236 | 0.6026 | 0.5601 | 0.3642 | 0.4418 | -0.046 ± 0.0289 | -0.02 (4) |
| 25-40 | 135 | 0.2265 | 0.1774 | +0.0492 ± 0.0223 | 0.6416 | 0.5242 | 0.6231 | 0.3107 | 0.3852 | -0.079 ± 0.0332 | -0.01 (1) |
| 40+ | 30 | 0.3354 | 0.1357 | +0.1998 ± 0.0606 | 0.9067 | 0.4279 | 0.7106 | 0.2678 | 0.2667 | -0.167 ± 0.0655 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 597 | 0.1651 | 0.1663 | -0.0012 ± 0.0006 | 0.4977 | 0.5001 | 0.4977 | 0.483 | 0.526 | -0.019 ± 0.0173 | -0.0188 (8) |
| 3-5 | 391 | 0.1692 | 0.1688 | +0.0003 ± 0.0017 | 0.514 | 0.5087 | 0.4739 | 0.4339 | 0.4527 | -0.039 ± 0.021 | 0.02 (1) |
| 5-10 | 883 | 0.1827 | 0.1847 | -0.0020 ± 0.0022 | 0.5459 | 0.5507 | 0.4828 | 0.409 | 0.4564 | -0.014 ± 0.0145 | -0.0129 (7) |
| 10-15 | 781 | 0.1902 | 0.1763 | +0.0140 ± 0.0037 | 0.5619 | 0.5186 | 0.4701 | 0.3463 | 0.3521 | -0.056 ± 0.015 | -0.0633 (3) |
| 15-25 | 985 | 0.1981 | 0.1604 | +0.0377 ± 0.0051 | 0.585 | 0.4783 | 0.4754 | 0.2769 | 0.2812 | -0.055 ± 0.0127 | -0.017 (10) |
| 25-40 | 987 | 0.2107 | 0.0973 | +0.1134 ± 0.0063 | 0.6133 | 0.3172 | 0.5044 | 0.1883 | 0.1692 | -0.070 ± 0.0096 | -0.01 (1) |
| 40+ | 730 | 0.3729 | 0.036 | +0.3369 ± 0.0076 | 0.9701 | 0.1562 | 0.6153 | 0.1027 | 0.0397 | -0.091 ± 0.0066 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 121 | 0.1794 | 0.1804 | -0.0010 ± 0.0013 | 0.5327 | 0.533 | 0.5032 | 0.4883 | 0.5124 | -0.070 ± 0.039 | -0.01 (1) |
| 3-5 | 88 | 0.2026 | 0.2014 | +0.0012 ± 0.0038 | 0.583 | 0.5857 | 0.4948 | 0.4555 | 0.4545 | -0.088 ± 0.0518 | 0.02 (1) |
| 5-10 | 208 | 0.183 | 0.1833 | -0.0004 ± 0.0045 | 0.5465 | 0.5464 | 0.571 | 0.4957 | 0.5288 | -0.071 ± 0.0306 | -0.01 (4) |
| 10-15 | 189 | 0.2292 | 0.2191 | +0.0102 ± 0.0086 | 0.6484 | 0.6293 | 0.578 | 0.454 | 0.4815 | -0.090 ± 0.0356 | -0.0667 (3) |
| 15-25 | 281 | 0.2245 | 0.1997 | +0.0248 ± 0.0107 | 0.636 | 0.5777 | 0.5855 | 0.3882 | 0.4306 | -0.090 ± 0.0277 | -0.0167 (3) |
| 25-40 | 170 | 0.2612 | 0.1959 | +0.0653 ± 0.0212 | 0.7253 | 0.5714 | 0.651 | 0.3386 | 0.3882 | -0.102 ± 0.0351 | -0.025 (2) |
| 40+ | 76 | 0.3836 | 0.166 | +0.2176 ± 0.0475 | 1.0482 | 0.501 | 0.7414 | 0.2476 | 0.2895 | -0.079 ± 0.0448 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 481 | 0.1549 | 0.1559 | -0.0010 ± 0.0006 | 0.4709 | 0.4729 | 0.5245 | 0.5098 | 0.5343 | -0.026 ± 0.0183 | -0.0217 (6) |
| 3-5 | 340 | 0.1799 | 0.1785 | +0.0014 ± 0.0018 | 0.5284 | 0.5277 | 0.5126 | 0.4728 | 0.4765 | -0.051 ± 0.0236 | 0.02 (1) |
| 5-10 | 791 | 0.1701 | 0.1709 | -0.0008 ± 0.0022 | 0.5132 | 0.5122 | 0.5195 | 0.4448 | 0.4804 | -0.021 ± 0.0148 | -0.01 (5) |
| 10-15 | 692 | 0.1896 | 0.1787 | +0.0109 ± 0.004 | 0.5619 | 0.5253 | 0.5061 | 0.3824 | 0.4061 | -0.042 ± 0.0163 | -0.0575 (4) |
| 15-25 | 1088 | 0.2058 | 0.1646 | +0.0412 ± 0.0049 | 0.6009 | 0.4921 | 0.5112 | 0.3149 | 0.3143 | -0.067 ± 0.0124 | -0.0143 (7) |
| 25-40 | 1012 | 0.2314 | 0.119 | +0.1124 ± 0.0069 | 0.6646 | 0.3728 | 0.5366 | 0.2194 | 0.2036 | -0.070 ± 0.011 | -0.015 (6) |
| 40+ | 950 | 0.4103 | 0.0555 | +0.3548 ± 0.0088 | 1.0695 | 0.2099 | 0.6612 | 0.1221 | 0.0716 | -0.084 ± 0.0073 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 182 | 0.1937 | 0.1955 | -0.0018 ± 0.0011 | 0.5671 | 0.5729 | 0.5155 | 0.5007 | 0.5275 | -0.061 ± 0.033 | -0.01 (5) |
| 3-5 | 120 | 0.1665 | 0.1636 | +0.0030 ± 0.003 | 0.5046 | 0.4979 | 0.5061 | 0.4666 | 0.45 | -0.129 ± 0.0396 | -- (0) |
| 5-10 | 232 | 0.1957 | 0.1946 | +0.0011 ± 0.0043 | 0.5796 | 0.5717 | 0.5017 | 0.4288 | 0.4526 | -0.080 ± 0.0288 | -0.01 (3) |
| 10-15 | 189 | 0.2153 | 0.2159 | -0.0006 ± 0.0084 | 0.6195 | 0.618 | 0.5414 | 0.4178 | 0.4868 | -0.055 ± 0.0338 | -0.044 (5) |
| 15-25 | 245 | 0.2132 | 0.203 | +0.0102 ± 0.0112 | 0.6171 | 0.5865 | 0.5734 | 0.3793 | 0.449 | -0.058 ± 0.0281 | -0.03 (1) |
| 25-40 | 140 | 0.2231 | 0.1922 | +0.0309 ± 0.0226 | 0.6374 | 0.5603 | 0.6242 | 0.3122 | 0.4143 | -0.058 ± 0.0337 | 0.0 (1) |
| 40+ | 25 | 0.3648 | 0.1373 | +0.2275 ± 0.0667 | 0.9712 | 0.4311 | 0.711 | 0.2606 | 0.24 | -0.185 ± 0.0761 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 611 | 0.1724 | 0.1725 | -0.0001 ± 0.0006 | 0.5174 | 0.5179 | 0.4976 | 0.4829 | 0.4926 | -0.050 ± 0.0168 | -0.0162 (13) |
| 3-5 | 409 | 0.174 | 0.1717 | +0.0024 ± 0.0017 | 0.5257 | 0.5243 | 0.4865 | 0.4471 | 0.4401 | -0.069 ± 0.021 | -0.01 (2) |
| 5-10 | 897 | 0.1824 | 0.1738 | +0.0086 ± 0.0021 | 0.5459 | 0.5179 | 0.4678 | 0.3944 | 0.3724 | -0.080 ± 0.0139 | -0.01 (3) |
| 10-15 | 718 | 0.1915 | 0.183 | +0.0085 ± 0.004 | 0.5653 | 0.537 | 0.4804 | 0.3566 | 0.3844 | -0.035 ± 0.016 | -0.03 (9) |
| 15-25 | 1089 | 0.1875 | 0.151 | +0.0365 ± 0.0047 | 0.5635 | 0.4553 | 0.4832 | 0.2842 | 0.2938 | -0.049 ± 0.0116 | -0.03 (2) |
| 25-40 | 949 | 0.2103 | 0.0981 | +0.1122 ± 0.0065 | 0.6131 | 0.3161 | 0.5012 | 0.1811 | 0.1675 | -0.067 ± 0.0098 | 0.0 (1) |
| 40+ | 681 | 0.3906 | 0.0378 | +0.3528 ± 0.0084 | 1.0194 | 0.1612 | 0.6249 | 0.1029 | 0.0382 | -0.092 ± 0.0071 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 454 | 0.2029 | 0.2029 | +0.0000 ± 0.0007 | 0.5876 | 0.588 | 0.4966 | 0.482 | 0.4846 | -0.041 ± 0.0212 | -0.0226 (46) |
| 3-5 | 336 | 0.1962 | 0.1954 | +0.0008 ± 0.0019 | 0.5755 | 0.5717 | 0.469 | 0.4293 | 0.4435 | -0.035 ± 0.0239 | -0.0059 (32) |
| 5-10 | 697 | 0.1868 | 0.1826 | +0.0042 ± 0.0024 | 0.5568 | 0.5449 | 0.4593 | 0.3859 | 0.3945 | -0.038 ± 0.0162 | -0.005 (72) |
| 10-15 | 467 | 0.2023 | 0.1916 | +0.0108 ± 0.0051 | 0.5936 | 0.5633 | 0.4606 | 0.3373 | 0.3555 | -0.032 ± 0.0201 | 0.0016 (63) |
| 15-25 | 631 | 0.2324 | 0.2085 | +0.0239 ± 0.0071 | 0.6584 | 0.6023 | 0.5278 | 0.3347 | 0.3708 | -0.028 ± 0.0181 | -0.0216 (58) |
| 25-40 | 318 | 0.2646 | 0.1664 | +0.0982 ± 0.0143 | 0.7343 | 0.5008 | 0.5726 | 0.2615 | 0.2579 | -0.071 ± 0.0225 | -0.0216 (25) |
| 40+ | 98 | 0.424 | 0.155 | +0.2689 ± 0.0426 | 1.187 | 0.48 | 0.7319 | 0.2239 | 0.2347 | -0.063 ± 0.0412 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 870 | 0.1969 | 0.1964 | +0.0005 ± 0.0005 | 0.5755 | 0.5739 | 0.4926 | 0.4781 | 0.4667 | -0.052 ± 0.015 | -0.0155 (82) |
| 3-5 | 636 | 0.1936 | 0.1924 | +0.0012 ± 0.0014 | 0.5687 | 0.5649 | 0.4702 | 0.4304 | 0.4371 | -0.037 ± 0.0174 | -0.018 (54) |
| 5-10 | 1319 | 0.1854 | 0.1806 | +0.0048 ± 0.0018 | 0.5528 | 0.5373 | 0.4456 | 0.3716 | 0.3791 | -0.034 ± 0.0118 | -0.0089 (122) |
| 10-15 | 978 | 0.195 | 0.1831 | +0.0119 ± 0.0034 | 0.5753 | 0.5414 | 0.453 | 0.3298 | 0.3436 | -0.030 ± 0.0136 | -0.0053 (99) |
| 15-25 | 1358 | 0.2218 | 0.1855 | +0.0363 ± 0.0046 | 0.6403 | 0.5443 | 0.5032 | 0.3075 | 0.313 | -0.045 ± 0.0117 | -0.0255 (106) |
| 25-40 | 958 | 0.2425 | 0.1277 | +0.1148 ± 0.0073 | 0.687 | 0.3986 | 0.5278 | 0.2128 | 0.1889 | -0.071 ± 0.0114 | -0.0206 (47) |
| 40+ | 526 | 0.3867 | 0.0786 | +0.3081 ± 0.0134 | 1.0539 | 0.2663 | 0.6498 | 0.1345 | 0.1046 | -0.072 ± 0.0124 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 1133 | 1.12 ± 0.086 | 1.237 | 0.1685 | 0.1796 | 0.2077 | 0.1955 |
| gen2 | 1133 | 0.913 ± 0.076 | 1.158 | 0.1847 | 0.1797 | 0.2273 | 0.1952 |
| gen1_elo | 1133 | 1.113 ± 0.084 | 1.198 | 0.1737 | 0.1802 | 0.2065 | 0.1953 |
| gen1_sr | 1133 | 1.138 ± 0.099 | 1.208 | 0.1418 | 0.1817 | 0.2222 | 0.1952 |
| gen1_ledger | 3001 | 0.9 ± 0.049 | 1.072 | 0.1623 | 0.201 | 0.2183 | 0.1913 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 7,371)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,123 | 28.8% |
| STALE_QUOTE | market_freshness | 1,891 | 25.7% |
| BOOK_QUALITY | execution | 1,090 | 14.8% |
| POOR_DATA | data | 738 | 10.0% |
| LIMITED_DATA | data | 435 | 5.9% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 350 | 4.8% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 349 | 4.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 207 | 2.8% |
| IDENTITY_AMBIGUOUS | mapping | 180 | 2.4% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 8 | 0.1% |

Cause class: coverage 28.8%, market_freshness 25.7%, data 15.9%, execution 14.8%, market_freshness/coverage 7.6%, model_calibration_or_unknown 4.7%, mapping 2.4%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 95.4%, LOW_DATA_QUALITY 67.8%, THIN_PLAYER_HISTORY 57.5%, STALE_PLAYER_DATA 57.1%, STALE_KALSHI_QUOTE 54.5%, MODEL_INTERNAL_DISAGREEMENT 36.5%, ASYMMETRIC_SAMPLE_SIZE 30.9%, WIDE_SPREAD 22.2%, MODEL_HIGH_UNCERTAINTY 14.6%, PLAYER_IDENTITY_RISK 11.0%, LEVEL_TRANSFER_RISK 8.1%, EVENT_MAPPING_RISK 6.7%, LOW_DISPLAYED_LIQUIDITY 6.4%, MODEL_CALIBRATION_OUTLIER 2.3%, UNKNOWN 0.6%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 31.0%, POST_SETTLEMENT_OBSERVATION 28.8%, POSSIBLE_IN_PLAY_QUOTE 5.3%, CONFIRMED_IN_PLAY_QUOTE 0.8%

### >= ge_25 pp (N = 4,096)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,678 | 41.0% |
| STALE_QUOTE | market_freshness | 861 | 21.0% |
| BOOK_QUALITY | execution | 567 | 13.8% |
| POOR_DATA | data | 342 | 8.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 188 | 4.6% |
| IN_PLAY_QUOTE | market_freshness/coverage | 126 | 3.1% |
| LIMITED_DATA | data | 125 | 3.0% |
| IDENTITY_AMBIGUOUS | mapping | 113 | 2.8% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 91 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 5 | 0.1% |

Cause class: coverage 41.0%, market_freshness 21.0%, execution 13.8%, data 11.4%, market_freshness/coverage 7.7%, mapping 2.8%, model_calibration_or_unknown 2.2%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 97.5%, LOW_DATA_QUALITY 70.7%, STALE_KALSHI_QUOTE 61.4%, THIN_PLAYER_HISTORY 59.9%, STALE_PLAYER_DATA 54.3%, MODEL_INTERNAL_DISAGREEMENT 38.7%, ASYMMETRIC_SAMPLE_SIZE 33.6%, WIDE_SPREAD 21.0%, MODEL_HIGH_UNCERTAINTY 15.8%, PLAYER_IDENTITY_RISK 13.6%, LEVEL_TRANSFER_RISK 7.6%, EVENT_MAPPING_RISK 7.4%, LOW_DISPLAYED_LIQUIDITY 6.9%, MODEL_CALIBRATION_OUTLIER 3.0%, UNKNOWN 0.1%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 43.4%, POST_SETTLEMENT_OBSERVATION 41.0%, POSSIBLE_IN_PLAY_QUOTE 5.2%, CONFIRMED_IN_PLAY_QUOTE 0.9%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 3436, "IDENTITY_AMBIGUOUS": 660}; ticker orientation: {"VERIFIED": 4096}.

Checks: discipline:AMBIGUOUS 197, discipline:PASS 3899, identity_confidence:AMBIGUOUS 555, identity_confidence:PASS 3541, level_mapping:NA 209, level_mapping:PASS 3887, market_pair:AMBIGUOUS 137, market_pair:NA 94, market_pair:PASS 3865, model_complement:NA 63, model_complement:PASS 4033, namesake:PASS 4096, physical_match_id:NA 1815, physical_match_id:PASS 2281, player_ids:PASS 4096, same_pair_other_event:PASS 4096, ticker_orientation:PASS 4096

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 893 | 2.6% | 2.6% | 0.6% | {"market_freshness": 20, "execution": 3} | 5.54 | 0.1735 / 0.1763 (51) | 24.4% | 0.2% | 6.0% | 1.2% |
| CHALLENGER | 3,016 | 19.0% | 7.3% | 14.0% | {"coverage": 338, "market_freshness": 105, "market_freshness/coverage": 67, "model_calibration_or_unknown": 32, "data": 25, "execution": 4, "model_calibration": 3} | 7.32 | 0.2214 / 0.2064 (710) | 49.7% | 5.6% | 1.4% | 23.2% |
| DOUBLES | 446 | 44.2% | 43.7% | 4.8% | {"market_freshness": 106, "mapping": 35, "execution": 35, "market_freshness/coverage": 14, "coverage": 7} | 22.7 | 0.3201 / 0.2285 (165) | 52.5% | 0.0% | 100.0% | 9.6% |
| ITF_MEN | 5,119 | 26.4% | 18.2% | 33.0% | {"coverage": 578, "execution": 255, "market_freshness": 222, "data": 192, "market_freshness/coverage": 81, "mapping": 22, "model_calibration_or_unknown": 1} | 11.09 | 0.2149 / 0.1884 (1399) | 46.0% | 55.7% | 6.8% | 25.7% |
| ITF_WOMEN | 6,273 | 28.0% | 19.4% | 42.9% | {"coverage": 738, "market_freshness": 359, "execution": 253, "data": 226, "market_freshness/coverage": 112, "mapping": 50, "model_calibration_or_unknown": 21} | 12.69 | 0.2041 / 0.185 (1413) | 47.5% | 61.3% | 10.9% | 25.3% |
| OTHER | 149 | 8.1% | 7.3% | 0.3% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 896 | 8.8% | 7.6% | 1.9% | {"market_freshness": 34, "model_calibration_or_unknown": 16, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.45 | 0.1994 / 0.1937 (131) | 36.2% | 2.3% | 1.3% | 3.5% |
| WTA125 | 655 | 15.4% | 10.4% | 2.5% | {"market_freshness/coverage": 30, "model_calibration_or_unknown": 19, "market_freshness": 13, "data": 13, "coverage": 12, "execution": 8, "mapping": 4, "model_calibration": 2} | 10.12 | 0.2266 / 0.2043 (223) | 27.8% | 6.4% | 3.8% | 13.1% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 3 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 4 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 5 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 6 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 7 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 8 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 9 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 10 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 12 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 13 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 14 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 15 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 16 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 17 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 18 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 19 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 20 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 21 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 22 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 23 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 24 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 799 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 25 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 26 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 27 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 28 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 29 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 826 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 30 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 687 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 31 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 32 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 33 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 708 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 34 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 36 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 37 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 38 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 39 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 114 min (STALE); data LIMITED (grade B, thinner serve sample 2163.0, ratio 2.0); no external reference |
| 40 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 183 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 41 | `KXWTAMATCH-26OCT01YASCHW-CHW` | WTA | fair_v1 | 73% / 2% | +70 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 51 min (STALE); no external reference |
| 42 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 43 | `KXATPCHALLENGERMATCH-26OCT05CASMUN-CAS` | CHALLENGER | fair_v1 | 83% / 14% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 192 min (STALE); data POOR (grade D, thinner serve sample 814.0, ratio 3.76); no external reference |
| 44 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 45 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 46 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |
| 47 | `KXITFWMATCH-26SEP30KOKUEM-KOK` | ITF_WOMEN | fair_v1 | 79% / 10% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 114 min (STALE); data LIMITED (grade C, thinner serve sample 824.0, ratio 2.35); no external reference |
| 48 | `KXITFMATCH-26SEP20WILRAH-RAH` | ITF_MEN | gen1_ledger | 72% / 4% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade B, thinner serve sample 2782.0, ratio 1.84); no external reference |
| 49 | `KXITFMATCH-26SEP26NAGTHO-NAG` | ITF_MEN | gen1_ledger | 76% / 7% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 89 min (STALE); data LIMITED (grade C, thinner serve sample 1323.0, ratio 4.45); no external reference |
| 50 | `KXITFWMATCH-26SEP26PERPRE-PER` | ITF_WOMEN | gen1_ledger | 78% / 10% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 102 min (STALE); data POOR (grade D, thinner serve sample 1020.0, ratio 2.77); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.975, "by_level_share_of_ge_25pp": {"ATP": 0.0056, "CHALLENGER": 0.1401, "DOUBLES": 0.0481, "ITF_MEN": 0.3298, "ITF_WOMEN": 0.4294, "OTHER": 0.0029, "WTA": 0.0193, "WTA125": 0.0247}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.6138, "share_primary_cause_market_settled_or_in_play": 0.4864, "share_primary_cause_stale_quote_only": 0.2102}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 4096, "identity_ambiguous_share": 0.1611, "ticker_orientation": {"VERIFIED": 4096}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 2281, "with_external": 38, "coverage": 0.0167, "external_status": {"EXTERNAL_STALE": 33, "AGREES_WITH_KALSHI": 5}, "triangulation": {"INSUFFICIENT_INPUTS": 33, "MODEL_LONE_OUTLIER": 5}, "share_external_agrees_with_kalshi": 0.1316, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 1061, "with_external": 38, "coverage": 0.0358, "external_status": {"EXTERNAL_STALE": 33, "AGREES_WITH_KALSHI": 5}, "triangulation": {"INSUFFICIENT_INPUTS": 33, "MODEL_LONE_OUTLIER": 5}, "share_external_agrees_with_kalshi": 0.1316, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 600.0, "median_sample_ratio": 2.35, "median_min_matches": 20.0, "median_max_days_since_last": 196.0, "share_severe_asymmetry": 0.1829, "data_status": {"POOR": 2176, "LIMITED": 1147, "ADEQUATE": 773}, "comparison_lt_10pp": {"median_thinner_serve_points": 1856.0, "median_sample_ratio": 1.73, "median_min_matches": 80.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 258, "model_minus_observed": 0.0823, "kalshi_minus_observed": -0.048, "brier_diff_model_minus_kalshi": 0.0067}, "4-10x": {"n": 179, "model_minus_observed": 0.0976, "kalshi_minus_observed": -0.0389, "brier_diff_model_minus_kalshi": 0.0162}, "<2x": {"n": 518, "model_minus_observed": 0.0713, "kalshi_minus_observed": -0.0526, "brier_diff_model_minus_kalshi": 0.0129}, ">=10x": {"n": 178, "model_minus_observed": 0.0937, "kalshi_minus_observed": -0.0785, "brier_diff_model_minus_kalshi": 0.0145}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 1133, "model": {"intercept": -0.618, "slope": 0.913, "slope_se": 0.076}, "kalshi_mid_same_rows": {"intercept": 0.216, "slope": 1.158, "slope_se": 0.084}, "mean_extremity_model": 0.1847, "mean_extremity_kalshi": 0.1797, "model_brier": 0.2273, "kalshi_brier": 0.1952, "brier_diff_model_minus_kalshi": 0.0322, "brier_diff_se": 0.0057, "model_logloss": 0.6475, "kalshi_logloss": 0.5703}, "fair_v1": {"n": 1133, "model": {"intercept": -0.41, "slope": 1.12, "slope_se": 0.086}, "kalshi_mid_same_rows": {"intercept": 0.361, "slope": 1.237, "slope_se": 0.087}, "mean_extremity_model": 0.1685, "mean_extremity_kalshi": 0.1796, "model_brier": 0.2077, "kalshi_brier": 0.1955, "brier_diff_model_minus_kalshi": 0.0122, "brier_diff_se": 0.0044, "model_logloss": 0.601, "kalshi_logloss": 0.5711}, "gen1_elo": {"n": 1133, "model": {"intercept": -0.44, "slope": 1.113, "slope_se": 0.084}, "kalshi_mid_same_rows": {"intercept": 0.304, "slope": 1.198, "slope_se": 0.085}, "mean_extremity_model": 0.1737, "mean_extremity_kalshi": 0.1802, "model_brier": 0.2065, "kalshi_brier": 0.1953, "brier_diff_model_minus_kalshi": 0.0112, "brier_diff_se": 0.0044, "model_logloss": 0.6002, "kalshi_logloss": 0.5705}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2589, "share_ge_15": 0.4403, "median_abs_gap": 13.0, "n": 8810}, "gen1_elo": {"share_ge_25": 0.2472, "share_ge_15": 0.4369, "median_abs_gap": 12.57, "n": 8810}, "gen1_sr": {"share_ge_25": 0.3061, "share_ge_15": 0.5242, "median_abs_gap": 15.92, "n": 8810}, "gen2": {"share_ge_25": 0.3112, "share_ge_15": 0.5107, "median_abs_gap": 15.48, "n": 8810}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1582, "share_ge_15": 0.346, "median_abs_gap": 10.47, "n": 6705}, "gen1_elo": {"share_ge_25": 0.1517, "share_ge_15": 0.3391, "median_abs_gap": 10.07, "n": 6705}, "gen1_sr": {"share_ge_25": 0.2054, "share_ge_15": 0.4403, "median_abs_gap": 13.14, "n": 6705}, "gen2": {"share_ge_25": 0.2265, "share_ge_15": 0.4377, "median_abs_gap": 12.85, "n": 6705}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.54, "share_ge_25_all": 0.0258, "share_ge_25_pregame_clean": 0.0261}, "WTA": {"median_abs_gap_pregame_clean": 8.45, "share_ge_25_all": 0.0882, "share_ge_25_pregame_clean": 0.0763}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2297, "share_within_10pp_all": 0.425, "share_within_10pp_pregame_clean": 0.4918, "corr_model_vs_mid_pregame_clean": 0.8341}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 177, "model_brier": 0.1816, "kalshi_brier": 0.1825, "brier_diff_model_minus_kalshi": -0.0009}, "10-15": {"n_settled": 197, "model_brier": 0.2187, "kalshi_brier": 0.2146, "brier_diff_model_minus_kalshi": 0.0041}, "15-25": {"n_settled": 249, "model_brier": 0.2178, "kalshi_brier": 0.209, "brier_diff_model_minus_kalshi": 0.0088}, "25-40": {"n_settled": 135, "model_brier": 0.2265, "kalshi_brier": 0.1774, "brier_diff_model_minus_kalshi": 0.0492}, "3-5": {"n_settled": 113, "model_brier": 0.1755, "kalshi_brier": 0.1765, "brier_diff_model_minus_kalshi": -0.001}, "40+": {"n_settled": 30, "model_brier": 0.3354, "kalshi_brier": 0.1357, "brier_diff_model_minus_kalshi": 0.1998}, "5-10": {"n_settled": 232, "model_brier": 0.1957, "kalshi_brier": 0.2021, "brier_diff_model_minus_kalshi": -0.0064}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.552, "slope": 0.9, "slope_se": 0.049}, "kalshi_slope": {"intercept": 0.11, "slope": 1.072, "slope_se": 0.05}, "n": 3001}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 165, "model_brier": 0.3201, "kalshi_brier": 0.2285, "brier_diff_model_minus_kalshi": 0.0915, "brier_diff_se": 0.0255, "corr_model_outcome": -0.0908, "corr_kalshi_outcome": 0.3347}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
