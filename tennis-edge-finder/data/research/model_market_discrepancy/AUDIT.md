# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-11T10:30Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 28,693): 0-3 14.6%, 3-5 9.7%, 5-10 20.1%, 10-15 15.4%, 15-25 18.4%, 25-40 13.6%, 40+ 8.2%; median gap 11.7 pp.
* **Where the extremes live**: 98.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.6%, Challenger 11.9%, doubles 7.2%). Main tour: ATP 1.5% and WTA 7.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 6,230): MARKET_ALREADY_SETTLED_WHEN_PRICED 39.2%, BOOK_QUALITY 17.3%, STALE_QUOTE 16.4%, POOR_DATA 8.0%, POSSIBLY_IN_PLAY_QUOTE 5.4%, LIMITED_DATA 4.4%, IDENTITY_AMBIGUOUS 3.7%, IN_PLAY_QUOTE 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.3%. By class: coverage 39.2%, execution 17.3%, market_freshness 16.4%, data 12.4%, market_freshness/coverage 8.8%, mapping 3.7%, model_calibration_or_unknown 1.9%, model_calibration 0.3%.
* **Stale / settled / in-play**: 54.6% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 48.0% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 6,230 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 17.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 2.5%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 19.1% of the time and with the model 0.3%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 626.0 points vs 1909.5 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.073, Gen-2 0.87, Gen-1 ledger 0.873 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 261 model 0.2189 vs Kalshi 0.1998; n 57 model 0.2912 vs Kalshi 0.167.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 113,733 model-market comparisons (187,044 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 42,845 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-11T10:21:57.352463+00:00'], shadow board 30,069 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-11T10:22:01.243903+00:00'], Model 4 12,716 rows, 12,508 settled tickers, 3,526 tickers with an external scan.
* By model: {"gen1_ledger": 28168, "gen1_elo": 15109, "fair_v1": 15109, "gen2": 15109, "gen1_sr": 15109, "model4_fundamental": 12569, "model4_conditioned": 12560}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 28,693 | 14.6 | 9.7 | 20.1 | 15.4 | 18.4 | 13.6 | 8.2 | 11.7 | 40.2% | 21.7% |
| MW fair_v1 | 15,109 | 13.8 | 8.8 | 18.6 | 16.1 | 18.4 | 14.5 | 9.8 | 12.71 | 42.6% | 24.2% |
| MW gen1_elo | 15,109 | 13.4 | 9.0 | 20.2 | 15.0 | 18.7 | 14.3 | 9.3 | 12.17 | 42.3% | 23.6% |
| MW gen1_ledger | 13,584 | 15.5 | 10.7 | 21.8 | 14.5 | 18.5 | 12.6 | 6.3 | 10.49 | 37.4% | 18.9% |
| MW gen1_sr | 15,109 | 10.2 | 7.9 | 16.5 | 14.5 | 21.6 | 18.0 | 11.4 | 15.38 | 51.0% | 29.4% |
| MW gen2 | 15,109 | 12.1 | 7.3 | 16.4 | 14.3 | 20.0 | 17.0 | 12.9 | 14.97 | 49.9% | 29.9% |
| all families model4_conditioned | 12,560 | 22.1 | 20.2 | 35.9 | 15.9 | 4.2 | 0.9 | 0.9 | 5.72 | 6.0% | 1.8% |
| all families model4_fundamental | 12,569 | 16.7 | 13.4 | 35.9 | 19.8 | 10.6 | 2.5 | 1.2 | 7.59 | 14.2% | 3.6% |

Configurable thresholds (primary): >=5pp 75.7%, >=10pp 55.5%, >=15pp 40.2%, >=20pp 29.9%, >=25pp 21.7%, >=30pp 15.9%, >=40pp 8.2%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.27pp; >=10pp 44.9%, >=25pp 17.4%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,235 | 30.8 | 14.2 | 25.0 | 17.1 | 10.9 | 1.1 | 0.9 | 5.84 | 13.0% | 2.0% |
| CHALLENGER | 2,575 | 15.8 | 10.6 | 19.3 | 16.1 | 13.9 | 12.4 | 11.8 | 11.65 | 38.1% | 24.2% |
| ITF_MEN | 4,259 | 11.5 | 8.8 | 18.4 | 14.9 | 19.1 | 15.2 | 12.1 | 13.69 | 46.4% | 27.3% |
| ITF_WOMEN | 5,915 | 10.2 | 6.7 | 16.0 | 16.4 | 21.6 | 18.5 | 10.6 | 15.31 | 50.7% | 29.1% |
| WTA | 698 | 22.4 | 10.7 | 25.5 | 16.1 | 17.5 | 6.3 | 1.6 | 7.87 | 25.4% | 7.9% |
| WTA125 | 427 | 12.4 | 8.0 | 23.4 | 22.5 | 16.9 | 15.0 | 1.9 | 11.08 | 33.7% | 16.9% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,235 | 24.1 | 14.3 | 24.9 | 18.8 | 15.1 | 1.9 | 1.1 | 6.9 | 18.0% | 2.9% |
| CHALLENGER | 2,575 | 15.5 | 7.5 | 19.0 | 13.4 | 18.2 | 13.9 | 12.4 | 12.86 | 44.6% | 26.4% |
| ITF_MEN | 4,259 | 10.4 | 7.4 | 16.8 | 14.8 | 19.9 | 17.8 | 12.9 | 15.34 | 50.6% | 30.7% |
| ITF_WOMEN | 5,915 | 8.9 | 5.9 | 12.8 | 12.9 | 21.5 | 20.9 | 17.1 | 19.07 | 59.4% | 38.0% |
| WTA | 698 | 20.1 | 7.9 | 18.5 | 15.0 | 20.9 | 16.1 | 1.6 | 11.64 | 38.5% | 17.6% |
| WTA125 | 427 | 4.9 | 3.3 | 18.3 | 20.1 | 24.6 | 18.5 | 10.3 | 16.84 | 53.4% | 28.8% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,235 | 27.0 | 14.4 | 29.5 | 15.0 | 10.6 | 2.6 | 1.0 | 6.24 | 14.2% | 3.6% |
| CHALLENGER | 2,575 | 15.5 | 10.5 | 20.4 | 15.4 | 14.7 | 11.8 | 11.7 | 10.86 | 38.2% | 23.5% |
| ITF_MEN | 4,259 | 10.5 | 8.8 | 19.1 | 13.8 | 19.9 | 15.6 | 12.2 | 13.96 | 47.8% | 27.9% |
| ITF_WOMEN | 5,915 | 9.9 | 6.7 | 16.7 | 15.7 | 22.7 | 18.8 | 9.4 | 15.46 | 51.0% | 28.3% |
| WTA | 698 | 22.4 | 14.5 | 33.7 | 15.9 | 9.7 | 2.9 | 1.0 | 6.5 | 13.6% | 3.9% |
| WTA125 | 427 | 23.2 | 10.5 | 30.7 | 15.7 | 13.1 | 6.3 | 0.5 | 7.6 | 19.9% | 6.8% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 680 | 31.2 | 23.1 | 34.7 | 9.3 | 1.3 | 0.4 | 0.0 | 4.63 | 1.8% | 0.4% |
| CHALLENGER | 1,749 | 23.0 | 16.5 | 26.8 | 14.3 | 12.6 | 5.0 | 1.8 | 6.65 | 19.4% | 6.8% |
| DOUBLES | 885 | 4.4 | 3.0 | 10.8 | 11.1 | 19.7 | 25.2 | 25.8 | 25.6 | 70.6% | 51.0% |
| ITF_MEN | 4,099 | 15.0 | 8.6 | 21.2 | 15.4 | 20.4 | 12.1 | 7.4 | 11.68 | 39.9% | 19.5% |
| ITF_WOMEN | 4,843 | 11.7 | 9.3 | 19.7 | 14.5 | 22.4 | 16.7 | 5.7 | 13.05 | 44.8% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 580 | 22.1 | 14.5 | 26.0 | 17.2 | 14.1 | 5.5 | 0.5 | 7.79 | 20.2% | 6.0% |
| WTA125 | 599 | 20.0 | 13.7 | 21.9 | 18.4 | 15.0 | 8.5 | 2.5 | 8.37 | 26.0% | 11.0% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,223 | 30.7 | 14.1 | 25.2 | 17.2 | 10.9 | 1.1 | 0.9 | 5.84 | 12.9% | 2.0% |
| CHALLENGER | 1,869 | 20.4 | 13.2 | 24.3 | 18.7 | 14.6 | 6.3 | 2.5 | 8.27 | 23.3% | 8.8% |
| ITF_MEN | 3,016 | 14.4 | 11.1 | 22.1 | 16.6 | 19.0 | 11.9 | 4.9 | 10.62 | 35.9% | 16.9% |
| ITF_WOMEN | 4,203 | 12.7 | 8.4 | 18.8 | 19.1 | 23.1 | 14.6 | 3.3 | 12.59 | 41.0% | 17.9% |
| WTA | 693 | 22.2 | 10.8 | 25.7 | 16.0 | 17.5 | 6.2 | 1.6 | 7.85 | 25.2% | 7.8% |
| WTA125 | 412 | 12.9 | 8.2 | 22.6 | 22.8 | 17.2 | 15.1 | 1.2 | 11.14 | 33.5% | 16.3% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,223 | 23.9 | 14.4 | 24.9 | 18.8 | 15.0 | 1.9 | 1.1 | 6.9 | 18.0% | 2.9% |
| CHALLENGER | 1,869 | 19.9 | 9.6 | 23.7 | 16.0 | 18.7 | 9.4 | 2.6 | 9.08 | 30.8% | 12.0% |
| ITF_MEN | 3,017 | 12.5 | 9.1 | 19.5 | 16.6 | 21.6 | 14.9 | 5.9 | 12.52 | 42.3% | 20.8% |
| ITF_WOMEN | 4,203 | 10.5 | 7.1 | 14.6 | 14.1 | 24.2 | 19.5 | 10.1 | 16.27 | 53.8% | 29.6% |
| WTA | 693 | 20.1 | 7.9 | 18.5 | 15.2 | 20.8 | 16.0 | 1.6 | 11.64 | 38.4% | 17.6% |
| WTA125 | 412 | 5.1 | 3.4 | 18.2 | 20.6 | 24.3 | 18.9 | 9.5 | 16.74 | 52.7% | 28.4% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 660 | 31.2 | 23.3 | 35.0 | 9.4 | 0.6 | 0.5 | 0.0 | 4.62 | 1.1% | 0.4% |
| CHALLENGER | 1,509 | 24.8 | 18.2 | 28.8 | 14.1 | 11.9 | 2.0 | 0.1 | 6.02 | 14.1% | 2.2% |
| DOUBLES | 818 | 4.4 | 3.1 | 11.1 | 11.1 | 19.8 | 25.1 | 25.4 | 25.56 | 70.3% | 50.5% |
| ITF_MEN | 3,313 | 16.7 | 9.5 | 23.4 | 16.3 | 20.1 | 9.7 | 4.3 | 10.05 | 34.1% | 14.0% |
| ITF_WOMEN | 3,964 | 12.8 | 10.0 | 21.5 | 15.3 | 22.7 | 15.0 | 2.6 | 11.63 | 40.3% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 550 | 22.6 | 15.1 | 26.6 | 17.3 | 14.4 | 4.2 | 0.0 | 7.46 | 18.6% | 4.2% |
| WTA125 | 512 | 22.3 | 15.0 | 23.4 | 20.5 | 13.3 | 5.1 | 0.4 | 7.42 | 18.8% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 885 | 4.4 | 3.0 | 10.8 | 11.1 | 19.7 | 25.2 | 25.8 | 25.6 | 70.6% | 51.0% |
| singles | 12,699 | 16.3 | 11.3 | 22.5 | 14.8 | 18.4 | 11.7 | 5.0 | 9.96 | 35.1% | 16.7% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 3,442 | 13.6 | 9.6 | 20.4 | 15.9 | 16.7 | 13.7 | 10.0 | 12.03 | 40.4% | 23.8% |
| Grass | 40 | 10.0 | 32.5 | 15.0 | 10.0 | 17.5 | 15.0 | 0.0 | 7.15 | 32.5% | 15.0% |
| Hard | 10,140 | 14.3 | 8.4 | 18.5 | 16.0 | 18.7 | 14.4 | 9.7 | 12.73 | 42.8% | 24.1% |
| UNKNOWN | 1,487 | 11.4 | 8.3 | 15.7 | 18.0 | 20.0 | 16.5 | 10.2 | 13.98 | 46.7% | 26.7% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,662 | 20.1 | 10.7 | 21.1 | 17.1 | 14.8 | 9.0 | 7.2 | 9.45 | 31.0% | 16.2% |
| B | 2,045 | 14.6 | 9.4 | 19.4 | 17.2 | 17.3 | 12.1 | 9.9 | 11.51 | 39.3% | 22.0% |
| C | 2,267 | 12.9 | 9.8 | 19.4 | 14.9 | 19.0 | 14.8 | 9.3 | 12.69 | 43.0% | 24.1% |
| D | 2,739 | 10.9 | 8.4 | 17.8 | 16.2 | 22.0 | 14.9 | 9.8 | 13.84 | 46.7% | 24.7% |
| F | 3,396 | 7.8 | 5.3 | 14.9 | 15.0 | 20.7 | 22.9 | 13.4 | 18.31 | 57.0% | 36.3% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,999 | 22.6 | 16.1 | 28.2 | 15.2 | 11.6 | 4.6 | 1.7 | 6.73 | 17.9% | 6.3% |
| B | 2,127 | 15.2 | 9.8 | 23.9 | 16.1 | 19.3 | 11.3 | 4.3 | 10.19 | 34.9% | 15.6% |
| C | 2,722 | 12.2 | 7.6 | 17.8 | 14.2 | 20.7 | 15.9 | 11.5 | 14.05 | 48.1% | 27.4% |
| D | 2,152 | 14.2 | 9.6 | 21.2 | 13.3 | 21.6 | 13.9 | 6.1 | 11.82 | 41.6% | 20.0% |
| F | 2,584 | 9.3 | 7.5 | 14.6 | 13.5 | 23.8 | 21.2 | 10.0 | 16.92 | 55.0% | 31.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 5,140 | 18.6 | 9.8 | 20.1 | 17.1 | 15.0 | 9.9 | 9.6 | 10.43 | 34.4% | 19.5% |
| LIMITED | 3,793 | 15.0 | 10.6 | 20.6 | 15.8 | 18.3 | 12.9 | 6.8 | 11.15 | 38.0% | 19.7% |
| POOR | 6,176 | 9.2 | 6.8 | 16.2 | 15.5 | 21.3 | 19.2 | 11.8 | 15.97 | 52.3% | 31.0% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,802 | 30.8 | 24.6 | 36.5 | 5.6 | 1.8 | 0.6 | 0.1 | 4.54 | 2.4% | 0.6% |
| GAME_SPREAD | 2,715 | 25.4 | 15.7 | 36.9 | 17.0 | 4.4 | 0.4 | 0.2 | 6.07 | 5.0% | 0.6% |
| MATCH_WINNER | 13,584 | 15.5 | 10.7 | 21.8 | 14.5 | 18.5 | 12.6 | 6.3 | 10.49 | 37.4% | 18.9% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 5,010 | 33.2 | 19.4 | 30.9 | 9.7 | 5.4 | 1.2 | 0.2 | 4.75 | 6.8% | 1.4% |
| TOTAL_GAMES | 4,033 | 6.8 | 9.0 | 38.7 | 30.2 | 10.1 | 2.7 | 2.4 | 9.53 | 15.3% | 5.2% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,566 | 25.5 | 37.8 | 31.7 | 0.3 | 4.1 | 0.5 | 0.1 | 4.33 | 4.7% | 0.6% |
| GAME_SPREAD | 3,239 | 44.8 | 15.5 | 29.7 | 7.6 | 1.2 | 0.8 | 0.4 | 3.61 | 2.4% | 1.2% |
| TOTAL_GAMES | 4,755 | 3.3 | 6.6 | 44.0 | 36.4 | 6.2 | 1.4 | 2.0 | 9.61 | 9.7% | 3.5% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,566 | 25.8 | 18.7 | 36.9 | 9.5 | 6.5 | 2.2 | 0.3 | 5.54 | 9.1% | 2.5% |
| GAME_SPREAD | 3,239 | 18.9 | 13.0 | 30.3 | 20.9 | 13.7 | 2.4 | 0.7 | 7.89 | 16.9% | 3.2% |
| TOTAL_GAMES | 4,764 | 6.5 | 8.5 | 38.8 | 28.8 | 12.4 | 2.8 | 2.2 | 9.61 | 17.4% | 5.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 15,109 | 42.6% | 24.2% | 12.71 | 32.5% | 13.8% | 10.14 |
| gen1_elo | 15,109 | 42.3% | 23.6% | 12.17 | 31.9% | 13.5% | 9.58 |
| gen1_sr | 15,109 | 51.0% | 29.4% | 15.38 | 41.9% | 18.9% | 12.52 |
| gen2 | 15,109 | 49.9% | 29.9% | 14.97 | 42.2% | 20.8% | 12.43 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 7,910 | 16.8 | 11.0 | 21.7 | 17.6 | 18.5 | 11.1 | 3.2 | 10.09 | 32.8% | 14.3% |
| STALE | 7,199 | 10.6 | 6.3 | 15.3 | 14.5 | 18.2 | 18.2 | 16.9 | 16.86 | 53.3% | 35.1% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 7,052 | 17.7 | 11.8 | 23.7 | 14.3 | 16.7 | 11.1 | 4.6 | 9.19 | 32.4% | 15.7% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 28,693 | 7052 | 11382 | 10259 | 24.4 | 148.9 | 1400.4 |
| ge_15pp | 11,525 | 2287 | 3887 | 5351 | 28.1 | 453.6 | 1380.4 |
| ge_25pp | 6,230 | 1107 | 1723 | 3400 | 34.7 | 575.5 | 1380.4 |
| lt_10pp | 12,756 | 3755 | 5552 | 3449 | 22.8 | 49.5 | 1341.5 |

Current slate `SL-20261011T103001Z-6147af12`: 560 priced rows, quote age at build {'median': 8.5, 'max': 8.6}, freshness {'FRESH': 560}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 4 | 0.0 | 0.0 | 25.0 | 0.0 | 75.0 | 0.0 | 0.0 | 20.45 | 75.0% | 0.0% |
| EXTERNAL_LONE_OUTLIER | 7 | 57.1 | 42.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,035 | 23.1 | 11.7 | 22.8 | 18.8 | 17.1 | 6.2 | 0.3 | 8.2 | 23.6% | 6.5% |
| KALSHI_LONE_OUTLIER | 1 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 5.14 | 0.0% | 0.0% |
| MARKETS_AGREE | 173 | 75.7 | 24.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.95 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 288 | 0.0 | 4.5 | 36.5 | 32.3 | 18.4 | 8.0 | 0.3 | 11.03 | 26.7% | 8.3% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 15,109 | 1508 (10.0%) | 19.1% | 0.3% | {"EXTERNAL_STALE": 1035, "AGREES_WITH_KALSHI": 288, "ALL_AGREE": 173, "EXTERNAL_OUTLIER": 7, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_15pp | 6,439 | 324 (5.0%) | 23.8% | 0.9% | {"EXTERNAL_STALE": 244, "AGREES_WITH_KALSHI": 77, "SUPPORTS_MODEL_DIRECTION": 3} |
| fair_v1_ge_25pp | 3,661 | 91 (2.5%) | 26.4% | 0.0% | {"EXTERNAL_STALE": 67, "AGREES_WITH_KALSHI": 24} |
| fair_v1_ge_25pp_pregame_clean | 1,572 | 89 (5.7%) | 27.0% | 0.0% | {"EXTERNAL_STALE": 65, "AGREES_WITH_KALSHI": 24} |
| fair_v1_lt_10pp | 6,232 | 896 (14.4%) | 13.2% | 0.1% | {"EXTERNAL_STALE": 596, "ALL_AGREE": 173, "AGREES_WITH_KALSHI": 118, "EXTERNAL_OUTLIER": 7, "ALL_DISAGREE": 1, "AGREES_WITH_MODEL": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,034 | 11.7 | 8.6 | 19.7 | 15.4 | 20.9 | 13.8 | 9.9 | 13.06 | 44.7% | 23.8% |
| 4-10x | 2,059 | 11.5 | 9.1 | 19.1 | 15.2 | 19.8 | 16.1 | 9.2 | 13.15 | 45.2% | 25.4% |
| <2x | 8,121 | 15.9 | 9.3 | 18.8 | 17.2 | 16.8 | 12.8 | 9.2 | 11.75 | 38.9% | 22.1% |
| >=10x | 1,895 | 11.1 | 6.5 | 15.8 | 13.9 | 19.6 | 20.6 | 12.3 | 16.18 | 52.6% | 33.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 4,009 | 14.0 | 8.5 | 19.4 | 16.0 | 18.5 | 12.8 | 10.7 | 12.44 | 42.1% | 23.6% |
| 300-1000 | 3,598 | 11.9 | 9.0 | 17.0 | 16.1 | 20.9 | 15.9 | 9.1 | 13.67 | 45.9% | 25.0% |
| <300 | 3,912 | 8.5 | 6.2 | 15.8 | 14.9 | 20.8 | 21.0 | 12.9 | 17.09 | 54.6% | 33.9% |
| >=3000 | 3,590 | 21.5 | 11.6 | 22.5 | 17.7 | 13.1 | 7.7 | 6.0 | 8.45 | 26.8% | 13.7% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 483 | 0.5363 | 0.4047 | 0.4741 | +0.062 | -0.069 | 0.0029 ± 0.0066 |
| ratio 4-10x | 326 | 0.5795 | 0.4378 | 0.5184 | +0.061 | -0.081 | 0.0015 ± 0.0087 |
| ratio <2x | 1108 | 0.5398 | 0.4189 | 0.4531 | +0.087 | -0.034 | 0.0124 ± 0.0042 |
| ratio >=10x | 309 | 0.5468 | 0.3795 | 0.4304 | +0.116 | -0.051 | 0.0177 ± 0.0099 |
| thinner_sample 1000-3000 | 614 | 0.5447 | 0.4218 | 0.4642 | +0.081 | -0.042 | 0.0076 ± 0.0057 |
| thinner_sample 300-1000 | 586 | 0.5641 | 0.4236 | 0.4881 | +0.076 | -0.064 | 0.0024 ± 0.0065 |
| thinner_sample <300 | 631 | 0.5406 | 0.3814 | 0.4501 | +0.090 | -0.069 | 0.0134 ± 0.0067 |
| thinner_sample >=3000 | 395 | 0.529 | 0.4348 | 0.4506 | +0.078 | -0.016 | 0.0166 ± 0.0057 |
| data_status ADEQUATE | 628 | 0.531 | 0.4294 | 0.4475 | +0.084 | -0.018 | 0.0124 ± 0.0048 |
| data_status LIMITED | 598 | 0.556 | 0.4252 | 0.4833 | +0.073 | -0.058 | 0.0033 ± 0.0061 |
| data_status POOR | 1000 | 0.5491 | 0.3957 | 0.463 | +0.086 | -0.067 | 0.0114 ± 0.0052 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 347 | 0.1912 | 0.1925 | -0.0013 ± 0.0008 | 0.5595 | 0.5628 | 0.4894 | 0.4747 | 0.5187 | -0.053 ± 0.0246 | -0.01 (3) |
| 3-5 | 232 | 0.1869 | 0.188 | -0.0012 ± 0.0023 | 0.553 | 0.5541 | 0.5119 | 0.4721 | 0.5043 | -0.059 ± 0.0288 | 0.02 (1) |
| 5-10 | 457 | 0.2012 | 0.2021 | -0.0009 ± 0.0032 | 0.5884 | 0.5904 | 0.5201 | 0.446 | 0.4814 | -0.083 ± 0.0219 | -0.0125 (4) |
| 10-15 | 404 | 0.2132 | 0.2048 | +0.0084 ± 0.0056 | 0.6146 | 0.5907 | 0.5179 | 0.394 | 0.4183 | -0.098 ± 0.0225 | -0.0633 (3) |
| 15-25 | 468 | 0.2286 | 0.2141 | +0.0145 ± 0.0084 | 0.6526 | 0.6157 | 0.5731 | 0.378 | 0.438 | -0.084 ± 0.0213 | -0.0133 (6) |
| 25-40 | 261 | 0.2189 | 0.1998 | +0.0190 ± 0.0164 | 0.6269 | 0.5749 | 0.6466 | 0.3385 | 0.4598 | -0.074 ± 0.0246 | -0.01 (1) |
| 40+ | 57 | 0.2912 | 0.167 | +0.1242 ± 0.0482 | 0.7869 | 0.5063 | 0.7464 | 0.3009 | 0.386 | -0.132 ± 0.0468 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1719 | 0.1727 | 0.1735 | -0.0008 ± 0.0003 | 0.5162 | 0.5171 | 0.4748 | 0.4601 | 0.4927 | -0.025 ± 0.0102 | -0.0188 (8) |
| 3-5 | 1089 | 0.1909 | 0.1879 | +0.0030 ± 0.0011 | 0.5627 | 0.5505 | 0.4802 | 0.4406 | 0.4187 | -0.080 ± 0.0133 | 0.02 (1) |
| 5-10 | 2340 | 0.1958 | 0.1933 | +0.0025 ± 0.0014 | 0.5744 | 0.5664 | 0.488 | 0.4143 | 0.4312 | -0.050 ± 0.0092 | -0.0082 (17) |
| 10-15 | 2091 | 0.2002 | 0.1816 | +0.0186 ± 0.0023 | 0.5861 | 0.5346 | 0.475 | 0.3505 | 0.3381 | -0.079 ± 0.0093 | -0.0475 (4) |
| 15-25 | 2393 | 0.2032 | 0.1662 | +0.0370 ± 0.0033 | 0.5981 | 0.494 | 0.495 | 0.2988 | 0.3038 | -0.068 ± 0.0083 | -0.0048 (29) |
| 25-40 | 1979 | 0.2185 | 0.1221 | +0.0965 ± 0.0049 | 0.6298 | 0.3783 | 0.5264 | 0.2128 | 0.2188 | -0.062 ± 0.0076 | -0.01 (1) |
| 40+ | 1357 | 0.3722 | 0.0434 | +0.3288 ± 0.0063 | 0.9699 | 0.173 | 0.6222 | 0.1054 | 0.056 | -0.085 ± 0.0053 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 265 | 0.1947 | 0.195 | -0.0004 ± 0.0009 | 0.5711 | 0.5723 | 0.4923 | 0.4775 | 0.4868 | -0.088 ± 0.0286 | -0.01 (1) |
| 3-5 | 176 | 0.208 | 0.2084 | -0.0004 ± 0.0028 | 0.597 | 0.5997 | 0.5247 | 0.4847 | 0.5057 | -0.063 ± 0.0361 | 0.02 (1) |
| 5-10 | 393 | 0.1954 | 0.1925 | +0.0030 ± 0.0033 | 0.573 | 0.5663 | 0.5605 | 0.4856 | 0.5013 | -0.088 ± 0.0228 | -0.01 (4) |
| 10-15 | 376 | 0.2146 | 0.205 | +0.0096 ± 0.0059 | 0.6154 | 0.5956 | 0.5748 | 0.4501 | 0.4787 | -0.099 ± 0.0242 | -0.05 (4) |
| 15-25 | 539 | 0.2258 | 0.2093 | +0.0165 ± 0.0078 | 0.6409 | 0.6012 | 0.5983 | 0.4012 | 0.4638 | -0.082 ± 0.0201 | -0.01 (5) |
| 25-40 | 348 | 0.2746 | 0.2007 | +0.0739 ± 0.0152 | 0.7696 | 0.5814 | 0.6728 | 0.3589 | 0.3994 | -0.138 ± 0.0239 | -0.025 (2) |
| 40+ | 129 | 0.3472 | 0.1847 | +0.1626 ± 0.0368 | 0.9705 | 0.543 | 0.7578 | 0.28 | 0.3643 | -0.070 ± 0.0355 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1508 | 0.1765 | 0.1768 | -0.0003 ± 0.0004 | 0.5254 | 0.5263 | 0.4914 | 0.477 | 0.498 | -0.034 ± 0.0112 | -0.0217 (6) |
| 3-5 | 929 | 0.1934 | 0.1925 | +0.0009 ± 0.0012 | 0.5609 | 0.5591 | 0.5227 | 0.4828 | 0.4909 | -0.043 ± 0.0146 | 0.02 (1) |
| 5-10 | 2053 | 0.1866 | 0.1829 | +0.0038 ± 0.0014 | 0.5545 | 0.5417 | 0.5139 | 0.4405 | 0.4545 | -0.049 ± 0.0096 | -0.01 (5) |
| 10-15 | 1826 | 0.1954 | 0.1805 | +0.0150 ± 0.0025 | 0.5767 | 0.5299 | 0.5186 | 0.3942 | 0.3992 | -0.065 ± 0.0101 | -0.02 (14) |
| 15-25 | 2574 | 0.2144 | 0.1747 | +0.0397 ± 0.0033 | 0.6239 | 0.5166 | 0.5346 | 0.3389 | 0.3388 | -0.074 ± 0.0083 | -0.0026 (27) |
| 25-40 | 2285 | 0.25 | 0.1373 | +0.1128 ± 0.0049 | 0.7107 | 0.4179 | 0.5619 | 0.2457 | 0.2271 | -0.089 ± 0.0078 | -0.015 (6) |
| 40+ | 1793 | 0.405 | 0.0669 | +0.3381 ± 0.007 | 1.0609 | 0.2357 | 0.6687 | 0.1311 | 0.0993 | -0.073 ± 0.0059 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 349 | 0.192 | 0.1947 | -0.0027 ± 0.0008 | 0.5618 | 0.5689 | 0.4996 | 0.4844 | 0.5587 | -0.008 ± 0.0238 | -0.0133 (6) |
| 3-5 | 245 | 0.1876 | 0.1866 | +0.0010 ± 0.0022 | 0.5511 | 0.5486 | 0.4987 | 0.4594 | 0.4694 | -0.103 ± 0.0289 | -0.01 (1) |
| 5-10 | 497 | 0.2014 | 0.1985 | +0.0029 ± 0.003 | 0.591 | 0.5819 | 0.5113 | 0.4374 | 0.4507 | -0.095 ± 0.0207 | -0.01 (4) |
| 10-15 | 375 | 0.2146 | 0.2127 | +0.0019 ± 0.0059 | 0.6192 | 0.6089 | 0.537 | 0.4146 | 0.4693 | -0.076 ± 0.0236 | -0.044 (5) |
| 15-25 | 446 | 0.2305 | 0.2088 | +0.0217 ± 0.0084 | 0.6615 | 0.6023 | 0.5783 | 0.3852 | 0.426 | -0.104 ± 0.0213 | -0.03 (1) |
| 25-40 | 265 | 0.2017 | 0.2038 | -0.0022 ± 0.0161 | 0.5859 | 0.5859 | 0.6515 | 0.3402 | 0.4943 | -0.048 ± 0.0238 | 0.0 (1) |
| 40+ | 49 | 0.3106 | 0.1697 | +0.1409 ± 0.0534 | 0.834 | 0.5113 | 0.7427 | 0.2906 | 0.3673 | -0.138 ± 0.0533 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1631 | 0.1807 | 0.1816 | -0.0009 ± 0.0004 | 0.5338 | 0.5356 | 0.4818 | 0.4667 | 0.5009 | -0.021 ± 0.0106 | -0.0183 (23) |
| 3-5 | 1140 | 0.1837 | 0.1813 | +0.0024 ± 0.001 | 0.5425 | 0.5369 | 0.4774 | 0.4381 | 0.4281 | -0.074 ± 0.013 | -0.0243 (7) |
| 5-10 | 2509 | 0.1915 | 0.1859 | +0.0056 ± 0.0013 | 0.5672 | 0.5492 | 0.4828 | 0.409 | 0.4073 | -0.064 ± 0.0087 | -0.01 (18) |
| 10-15 | 1935 | 0.1968 | 0.1816 | +0.0152 ± 0.0024 | 0.5784 | 0.5321 | 0.4932 | 0.3701 | 0.3685 | -0.071 ± 0.0096 | -0.03 (9) |
| 15-25 | 2526 | 0.2077 | 0.1693 | +0.0383 ± 0.0032 | 0.6101 | 0.5022 | 0.4977 | 0.3024 | 0.3036 | -0.069 ± 0.0082 | -0.03 (2) |
| 25-40 | 1937 | 0.2118 | 0.1166 | +0.0952 ± 0.0049 | 0.6142 | 0.3637 | 0.5205 | 0.2035 | 0.2148 | -0.060 ± 0.0073 | 0.0 (1) |
| 40+ | 1290 | 0.3858 | 0.045 | +0.3408 ± 0.0066 | 1.008 | 0.1776 | 0.6297 | 0.1067 | 0.0535 | -0.087 ± 0.0056 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 645 | 0.2016 | 0.202 | -0.0004 ± 0.0006 | 0.5856 | 0.586 | 0.5014 | 0.4864 | 0.4961 | -0.040 ± 0.0177 | -0.0226 (46) |
| 3-5 | 476 | 0.1986 | 0.1971 | +0.0015 ± 0.0016 | 0.578 | 0.5727 | 0.4807 | 0.4411 | 0.4412 | -0.054 ± 0.0204 | -0.0058 (33) |
| 5-10 | 968 | 0.1928 | 0.1868 | +0.0060 ± 0.0021 | 0.5701 | 0.5545 | 0.4791 | 0.4056 | 0.4029 | -0.064 ± 0.0142 | -0.0049 (73) |
| 10-15 | 624 | 0.2044 | 0.1942 | +0.0103 ± 0.0044 | 0.5974 | 0.5701 | 0.49 | 0.3672 | 0.3862 | -0.047 ± 0.0176 | 0.0014 (64) |
| 15-25 | 837 | 0.2354 | 0.2094 | +0.0259 ± 0.0062 | 0.6703 | 0.6043 | 0.5528 | 0.3585 | 0.3907 | -0.059 ± 0.0159 | -0.0216 (58) |
| 25-40 | 470 | 0.2517 | 0.1879 | +0.0638 ± 0.0124 | 0.7089 | 0.5499 | 0.6354 | 0.322 | 0.3745 | -0.086 ± 0.0186 | -0.0216 (25) |
| 40+ | 159 | 0.3673 | 0.1879 | +0.1794 ± 0.0356 | 1.073 | 0.5548 | 0.7875 | 0.2915 | 0.3836 | -0.068 ± 0.0316 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2000 | 0.1912 | 0.1912 | -0.0000 ± 0.0003 | 0.559 | 0.5578 | 0.5025 | 0.4872 | 0.492 | -0.038 ± 0.0097 | -0.0155 (82) |
| 3-5 | 1394 | 0.1901 | 0.1872 | +0.0029 ± 0.0009 | 0.5551 | 0.5486 | 0.4899 | 0.4503 | 0.4354 | -0.060 ± 0.0116 | -0.0148 (63) |
| 5-10 | 2790 | 0.1905 | 0.1821 | +0.0084 ± 0.0012 | 0.5646 | 0.5415 | 0.4752 | 0.4015 | 0.3853 | -0.068 ± 0.0082 | -0.0087 (125) |
| 10-15 | 1881 | 0.2012 | 0.1866 | +0.0145 ± 0.0025 | 0.5894 | 0.5518 | 0.5034 | 0.3803 | 0.3828 | -0.057 ± 0.0099 | -0.0053 (105) |
| 15-25 | 2397 | 0.2308 | 0.1977 | +0.0331 ± 0.0036 | 0.6667 | 0.5748 | 0.5472 | 0.3522 | 0.3663 | -0.061 ± 0.0092 | -0.0255 (106) |
| 25-40 | 1647 | 0.2515 | 0.1638 | +0.0877 ± 0.0063 | 0.7147 | 0.4864 | 0.5994 | 0.2847 | 0.3048 | -0.075 ± 0.0096 | -0.0206 (47) |
| 40+ | 809 | 0.3917 | 0.1192 | +0.2725 ± 0.0132 | 1.1149 | 0.3707 | 0.7016 | 0.191 | 0.1928 | -0.077 ± 0.0116 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2226 | 1.073 ± 0.06 | 1.187 | 0.1691 | 0.1706 | 0.2105 | 0.201 |
| gen2 | 2226 | 0.87 ± 0.053 | 1.128 | 0.1854 | 0.17 | 0.2281 | 0.2011 |
| gen1_elo | 2226 | 1.066 ± 0.059 | 1.173 | 0.173 | 0.171 | 0.2089 | 0.2011 |
| gen1_sr | 2226 | 1.061 ± 0.068 | 1.207 | 0.1436 | 0.1723 | 0.2235 | 0.2009 |
| gen1_ledger | 4179 | 0.873 ± 0.039 | 1.071 | 0.1739 | 0.1889 | 0.2184 | 0.1961 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 11,525)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,104 | 26.9% |
| STALE_QUOTE | market_freshness | 2,288 | 19.9% |
| BOOK_QUALITY | execution | 2,042 | 17.7% |
| POOR_DATA | data | 1,216 | 10.5% |
| LIMITED_DATA | data | 922 | 8.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 624 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 534 | 4.6% |
| IDENTITY_AMBIGUOUS | mapping | 375 | 3.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 339 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 81 | 0.7% |

Cause class: coverage 26.9%, market_freshness 19.9%, data 18.6%, execution 17.7%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.6%, mapping 3.2%, model_calibration 0.7%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.9%, START_UNVERIFIABLE 96.0%, LOW_DATA_QUALITY 67.8%, STALE_PLAYER_DATA 57.0%, THIN_PLAYER_HISTORY 56.0%, STALE_KALSHI_QUOTE 46.4%, MODEL_INTERNAL_DISAGREEMENT 37.3%, ASYMMETRIC_SAMPLE_SIZE 30.1%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 16.3%, PLAYER_IDENTITY_RISK 11.7%, LEVEL_TRANSFER_RISK 8.8%, EVENT_MAPPING_RISK 8.1%, LOW_DISPLAYED_LIQUIDITY 7.4%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 1.1%, UNKNOWN 0.6%, EXTERNAL_MARKET_CONFIRMATION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 29.4%, POST_SETTLEMENT_OBSERVATION 26.9%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### >= ge_25 pp (N = 6,230)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,443 | 39.2% |
| BOOK_QUALITY | execution | 1,077 | 17.3% |
| STALE_QUOTE | market_freshness | 1,019 | 16.4% |
| POOR_DATA | data | 499 | 8.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 337 | 5.4% |
| LIMITED_DATA | data | 273 | 4.4% |
| IDENTITY_AMBIGUOUS | mapping | 232 | 3.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 210 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 120 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 20 | 0.3% |

Cause class: coverage 39.2%, execution 17.3%, market_freshness 16.4%, data 12.4%, market_freshness/coverage 8.8%, mapping 3.7%, model_calibration_or_unknown 1.9%, model_calibration 0.3%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.4%, START_UNVERIFIABLE 98.1%, LOW_DATA_QUALITY 71.3%, THIN_PLAYER_HISTORY 58.0%, STALE_KALSHI_QUOTE 54.6%, STALE_PLAYER_DATA 51.6%, MODEL_INTERNAL_DISAGREEMENT 38.6%, ASYMMETRIC_SAMPLE_SIZE 32.1%, WIDE_SPREAD 23.2%, MODEL_HIGH_UNCERTAINTY 17.7%, PLAYER_IDENTITY_RISK 14.9%, EVENT_MAPPING_RISK 9.9%, LEVEL_TRANSFER_RISK 7.6%, LOW_DISPLAYED_LIQUIDITY 7.6%, MODEL_CALIBRATION_OUTLIER 4.6%, EXTERNAL_MARKET_REJECTION 0.5%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 42.1%, POST_SETTLEMENT_OBSERVATION 39.2%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 5140, "IDENTITY_AMBIGUOUS": 1090}; ticker orientation: {"VERIFIED": 6230}.

Checks: discipline:AMBIGUOUS 451, discipline:PASS 5779, identity_confidence:AMBIGUOUS 926, identity_confidence:PASS 5304, level_mapping:NA 463, level_mapping:PASS 5767, market_pair:AMBIGUOUS 222, market_pair:NA 145, market_pair:PASS 5863, model_complement:NA 112, model_complement:PASS 6118, namesake:PASS 6230, physical_match_id:NA 2569, physical_match_id:PASS 3661, player_ids:PASS 6230, same_pair_other_event:PASS 6230, ticker_orientation:PASS 6230

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,915 | 1.5% | 1.5% | 0.4% | {"market_freshness": 20, "execution": 8} | 5.24 | 0.2051 / 0.2037 (213) | 16.9% | 0.1% | 5.8% | 1.7% |
| CHALLENGER | 4,324 | 17.1% | 5.8% | 11.9% | {"coverage": 457, "market_freshness": 108, "market_freshness/coverage": 87, "model_calibration_or_unknown": 44, "data": 29, "execution": 12, "model_calibration": 3, "mapping": 1} | 6.9 | 0.2224 / 0.2044 (968) | 41.0% | 5.6% | 1.9% | 21.9% |
| DOUBLES | 885 | 51.0% | 50.5% | 7.2% | {"execution": 170, "mapping": 137, "market_freshness": 106, "market_freshness/coverage": 31, "coverage": 7} | 25.56 | 0.3344 / 0.2293 (250) | 26.4% | 0.0% | 100.0% | 7.6% |
| ITF_MEN | 8,358 | 23.5% | 15.3% | 31.5% | {"coverage": 822, "execution": 406, "data": 274, "market_freshness": 271, "market_freshness/coverage": 170, "mapping": 19, "model_calibration_or_unknown": 1} | 10.36 | 0.2096 / 0.1927 (2077) | 37.6% | 53.4% | 6.4% | 24.3% |
| ITF_WOMEN | 10,758 | 26.1% | 17.7% | 45.1% | {"coverage": 1140, "execution": 463, "market_freshness": 449, "data": 435, "market_freshness/coverage": 218, "mapping": 69, "model_calibration_or_unknown": 24, "model_calibration": 9} | 12.17 | 0.2052 / 0.1922 (2333) | 38.5% | 57.3% | 9.6% | 24.1% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,278 | 7.0% | 6.2% | 1.4% | {"market_freshness": 36, "model_calibration_or_unknown": 20, "data": 11, "market_freshness/coverage": 9, "execution": 5, "model_calibration": 4, "coverage": 4, "mapping": 1} | 7.7 | 0.2208 / 0.2187 (205) | 28.2% | 1.6% | 1.4% | 2.7% |
| WTA125 | 1,026 | 13.5% | 10.3% | 2.2% | {"market_freshness/coverage": 31, "model_calibration_or_unknown": 29, "market_freshness": 27, "data": 23, "coverage": 12, "execution": 8, "mapping": 4, "model_calibration": 4} | 9.21 | 0.231 / 0.2156 (317) | 23.8% | 7.7% | 3.9% | 9.9% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 5 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 6 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 7 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 8 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 9 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 10 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 11 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 12 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 13 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 14 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 15 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 16 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 22.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1345 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 18 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 19 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 20 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 21 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 22 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 23 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 24 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 25 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 26 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 27 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 28 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 29 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 30 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 31 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 189 min (STALE); no external reference |
| 32 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 33 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 34 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 35 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 36 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 37 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 799 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 38 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 39 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 40 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 41 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 42 | `KXITFWMATCH-26OCT08ARISAV-SAV` | ITF_WOMEN | fair_v1 | 75% / 2% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.3h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 26 min (AGING); no external reference |
| 43 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 826 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 44 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 687 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 45 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 46 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 47 | `KXITFMATCH-26OCT09DELSTE-DEL` | ITF_MEN | fair_v1 | 78% / 6% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 229 min (STALE); data POOR (grade F, thinner serve sample 477.0, ratio 8.93); no external reference |
| 48 | `KXITFWMATCH-26OCT08ARAWAN-ARA` | ITF_WOMEN | fair_v1 | 77% / 6% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 21.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1321 min (STALE); data POOR (grade D, thinner serve sample 553.0, ratio 3.97); no external reference |
| 49 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 708 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 50 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9811, "by_level_share_of_ge_25pp": {"ATP": 0.0045, "CHALLENGER": 0.1189, "DOUBLES": 0.0724, "ITF_MEN": 0.3151, "ITF_WOMEN": 0.4506, "OTHER": 0.0019, "WTA": 0.0144, "WTA125": 0.0222}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5457, "share_primary_cause_market_settled_or_in_play": 0.4799, "share_primary_cause_stale_quote_only": 0.1636}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 6230, "identity_ambiguous_share": 0.175, "ticker_orientation": {"VERIFIED": 6230}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 3661, "with_external": 91, "coverage": 0.0249, "external_status": {"EXTERNAL_STALE": 67, "AGREES_WITH_KALSHI": 24}, "triangulation": {"INSUFFICIENT_INPUTS": 67, "MODEL_LONE_OUTLIER": 24}, "share_external_agrees_with_kalshi": 0.2637, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 1572, "with_external": 89, "coverage": 0.0566, "external_status": {"EXTERNAL_STALE": 65, "AGREES_WITH_KALSHI": 24}, "triangulation": {"INSUFFICIENT_INPUTS": 65, "MODEL_LONE_OUTLIER": 24}, "share_external_agrees_with_kalshi": 0.2697, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 626.0, "median_sample_ratio": 2.3, "median_min_matches": 21.0, "median_max_days_since_last": 197.0, "share_severe_asymmetry": 0.177, "data_status": {"POOR": 3165, "LIMITED": 1909, "ADEQUATE": 1156}, "comparison_lt_10pp": {"median_thinner_serve_points": 1909.5, "median_sample_ratio": 1.67, "median_min_matches": 85.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 483, "model_minus_observed": 0.0622, "kalshi_minus_observed": -0.0694, "brier_diff_model_minus_kalshi": 0.0029}, "4-10x": {"n": 326, "model_minus_observed": 0.0611, "kalshi_minus_observed": -0.0806, "brier_diff_model_minus_kalshi": 0.0015}, "<2x": {"n": 1108, "model_minus_observed": 0.0868, "kalshi_minus_observed": -0.0341, "brier_diff_model_minus_kalshi": 0.0124}, ">=10x": {"n": 309, "model_minus_observed": 0.1164, "kalshi_minus_observed": -0.0509, "brier_diff_model_minus_kalshi": 0.0177}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2226, "model": {"intercept": -0.563, "slope": 0.87, "slope_se": 0.053}, "kalshi_mid_same_rows": {"intercept": 0.21, "slope": 1.128, "slope_se": 0.061}, "mean_extremity_model": 0.1854, "mean_extremity_kalshi": 0.17, "model_brier": 0.2281, "kalshi_brier": 0.2011, "brier_diff_model_minus_kalshi": 0.027, "brier_diff_se": 0.004, "model_logloss": 0.652, "kalshi_logloss": 0.5841}, "fair_v1": {"n": 2226, "model": {"intercept": -0.41, "slope": 1.073, "slope_se": 0.06}, "kalshi_mid_same_rows": {"intercept": 0.309, "slope": 1.187, "slope_se": 0.063}, "mean_extremity_model": 0.1691, "mean_extremity_kalshi": 0.1706, "model_brier": 0.2105, "kalshi_brier": 0.201, "brier_diff_model_minus_kalshi": 0.0095, "brier_diff_se": 0.0032, "model_logloss": 0.6081, "kalshi_logloss": 0.5837}, "gen1_elo": {"n": 2226, "model": {"intercept": -0.384, "slope": 1.066, "slope_se": 0.059}, "kalshi_mid_same_rows": {"intercept": 0.313, "slope": 1.173, "slope_se": 0.062}, "mean_extremity_model": 0.173, "mean_extremity_kalshi": 0.171, "model_brier": 0.2089, "kalshi_brier": 0.2011, "brier_diff_model_minus_kalshi": 0.0078, "brier_diff_se": 0.0031, "model_logloss": 0.6056, "kalshi_logloss": 0.5838}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2423, "share_ge_15": 0.4262, "median_abs_gap": 12.71, "n": 15109}, "gen1_elo": {"share_ge_25": 0.2358, "share_ge_15": 0.4229, "median_abs_gap": 12.17, "n": 15109}, "gen1_sr": {"share_ge_25": 0.2941, "share_ge_15": 0.5098, "median_abs_gap": 15.38, "n": 15109}, "gen2": {"share_ge_25": 0.2987, "share_ge_15": 0.4989, "median_abs_gap": 14.97, "n": 15109}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1377, "share_ge_15": 0.3252, "median_abs_gap": 10.14, "n": 11416}, "gen1_elo": {"share_ge_25": 0.1346, "share_ge_15": 0.3188, "median_abs_gap": 9.58, "n": 11415}, "gen1_sr": {"share_ge_25": 0.1888, "share_ge_15": 0.4185, "median_abs_gap": 12.52, "n": 11416}, "gen2": {"share_ge_25": 0.2075, "share_ge_15": 0.4217, "median_abs_gap": 12.43, "n": 11417}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.24, "share_ge_25_all": 0.0146, "share_ge_25_pregame_clean": 0.0149}, "WTA": {"median_abs_gap_pregame_clean": 7.7, "share_ge_25_all": 0.0704, "share_ge_25_pregame_clean": 0.0619}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2434, "share_within_10pp_all": 0.4446, "share_within_10pp_pregame_clean": 0.5079, "corr_model_vs_mid_pregame_clean": 0.8524}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 347, "model_brier": 0.1912, "kalshi_brier": 0.1925, "brier_diff_model_minus_kalshi": -0.0013}, "10-15": {"n_settled": 404, "model_brier": 0.2132, "kalshi_brier": 0.2048, "brier_diff_model_minus_kalshi": 0.0084}, "15-25": {"n_settled": 468, "model_brier": 0.2286, "kalshi_brier": 0.2141, "brier_diff_model_minus_kalshi": 0.0145}, "25-40": {"n_settled": 261, "model_brier": 0.2189, "kalshi_brier": 0.1998, "brier_diff_model_minus_kalshi": 0.019}, "3-5": {"n_settled": 232, "model_brier": 0.1869, "kalshi_brier": 0.188, "brier_diff_model_minus_kalshi": -0.0012}, "40+": {"n_settled": 57, "model_brier": 0.2912, "kalshi_brier": 0.167, "brier_diff_model_minus_kalshi": 0.1242}, "5-10": {"n_settled": 457, "model_brier": 0.2012, "kalshi_brier": 0.2021, "brier_diff_model_minus_kalshi": -0.0009}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.563, "slope": 0.87, "slope_se": 0.053}, "kalshi_slope": {"intercept": 0.21, "slope": 1.128, "slope_se": 0.061}, "n": 2226}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.535, "slope": 0.873, "slope_se": 0.039}, "kalshi_slope": {"intercept": 0.123, "slope": 1.071, "slope_se": 0.043}, "n": 4179}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 250, "model_brier": 0.3344, "kalshi_brier": 0.2293, "brier_diff_model_minus_kalshi": 0.1051, "brier_diff_se": 0.0206, "corr_model_outcome": -0.0224, "corr_kalshi_outcome": 0.2891}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
