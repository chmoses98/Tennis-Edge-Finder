# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-16T17:14Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 35,031): 0-3 14.5%, 3-5 9.4%, 5-10 20.1%, 10-15 15.3%, 15-25 18.9%, 25-40 13.6%, 40+ 8.3%; median gap 11.88 pp.
* **Where the extremes live**: 98.3% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.9%, Challenger 12.2%, doubles 6.7%). Main tour: ATP 1.4% and WTA 6.1% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 7,679): MARKET_ALREADY_SETTLED_WHEN_PRICED 36.7%, STALE_QUOTE 18.2%, BOOK_QUALITY 17.3%, POOR_DATA 8.3%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 4.0%, IN_PLAY_QUOTE 3.2%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.5%. By class: coverage 36.7%, market_freshness 18.2%, execution 17.3%, data 12.3%, market_freshness/coverage 8.6%, mapping 4.3%, model_calibration_or_unknown 2.0%, model_calibration 0.5%.
* **Stale / settled / in-play**: 53.9% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 45.3% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 7,679 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.9% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 3.9%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 21.4% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 561.0 points vs 1786.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.059, Gen-2 0.87, Gen-1 ledger 0.874 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 358 model 0.2252 vs Kalshi 0.2084; n 74 model 0.2888 vs Kalshi 0.1769.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 138,801 model-market comparisons (231,599 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 48,356 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-16T17:04:51.644092+00:00'], shadow board 38,953 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-16T17:04:55.254687+00:00'], Model 4 14,508 rows, 14,891 settled tickers, 5,061 tickers with an external scan.
* By model: {"gen1_ledger": 31770, "gen1_elo": 19586, "fair_v1": 19586, "gen2": 19586, "gen1_sr": 19586, "model4_fundamental": 14348, "model4_conditioned": 14339}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 35,031 | 14.5 | 9.4 | 20.1 | 15.3 | 18.9 | 13.6 | 8.3 | 11.88 | 40.8% | 21.9% |
| MW fair_v1 | 19,586 | 13.6 | 8.4 | 18.6 | 15.8 | 19.2 | 14.6 | 9.9 | 12.99 | 43.7% | 24.5% |
| MW gen1_elo | 19,586 | 13.1 | 9.0 | 19.7 | 15.1 | 19.2 | 14.3 | 9.6 | 12.48 | 43.1% | 23.9% |
| MW gen1_ledger | 15,445 | 15.6 | 10.7 | 21.9 | 14.7 | 18.4 | 12.4 | 6.2 | 10.43 | 37.1% | 18.7% |
| MW gen1_sr | 19,586 | 9.7 | 7.5 | 16.3 | 14.2 | 21.6 | 18.7 | 11.9 | 15.89 | 52.3% | 30.7% |
| MW gen2 | 19,586 | 11.4 | 7.1 | 16.6 | 14.1 | 20.1 | 17.6 | 13.1 | 15.41 | 50.8% | 30.8% |
| all families model4_conditioned | 14,339 | 21.6 | 20.1 | 35.0 | 16.7 | 4.4 | 1.3 | 0.9 | 5.83 | 6.6% | 2.2% |
| all families model4_fundamental | 14,348 | 16.8 | 13.6 | 35.6 | 19.5 | 10.6 | 2.8 | 1.1 | 7.58 | 14.5% | 3.9% |

Configurable thresholds (primary): >=5pp 76.1%, >=10pp 56.1%, >=15pp 40.8%, >=20pp 30.3%, >=25pp 21.9%, >=30pp 15.9%, >=40pp 8.3%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.5pp; >=10pp 45.4%, >=25pp 17.5%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,354 | 30.6 | 14.6 | 25.3 | 17.3 | 10.3 | 1.1 | 0.8 | 5.69 | 12.3% | 1.9% |
| CHALLENGER | 3,268 | 16.1 | 9.8 | 20.0 | 15.9 | 14.4 | 12.3 | 11.5 | 11.5 | 38.2% | 23.8% |
| ITF_MEN | 5,615 | 11.0 | 8.2 | 17.6 | 14.8 | 19.8 | 16.2 | 12.3 | 14.34 | 48.4% | 28.5% |
| ITF_WOMEN | 7,714 | 10.5 | 6.5 | 16.2 | 15.7 | 22.2 | 18.0 | 10.8 | 15.42 | 51.0% | 28.8% |
| WTA | 1,007 | 20.9 | 11.3 | 25.1 | 15.5 | 20.5 | 5.7 | 1.1 | 8.09 | 27.2% | 6.8% |
| WTA125 | 628 | 13.1 | 7.6 | 22.8 | 20.7 | 20.1 | 13.7 | 2.1 | 11.31 | 35.8% | 15.8% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,354 | 24.7 | 14.4 | 25.0 | 18.5 | 14.4 | 1.9 | 1.0 | 6.58 | 17.3% | 2.9% |
| CHALLENGER | 3,268 | 14.8 | 7.9 | 19.5 | 13.4 | 18.0 | 14.3 | 12.1 | 12.7 | 44.4% | 26.4% |
| ITF_MEN | 5,615 | 9.6 | 6.8 | 15.8 | 13.7 | 19.8 | 19.3 | 14.9 | 16.65 | 54.1% | 34.2% |
| ITF_WOMEN | 7,714 | 8.6 | 5.7 | 13.8 | 13.4 | 21.4 | 20.7 | 16.3 | 18.58 | 58.4% | 37.0% |
| WTA | 1,007 | 17.2 | 7.9 | 20.0 | 15.8 | 22.5 | 15.4 | 1.2 | 11.71 | 39.1% | 16.6% |
| WTA125 | 628 | 6.4 | 4.6 | 17.4 | 18.0 | 24.8 | 19.6 | 9.2 | 16.92 | 53.7% | 28.8% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,354 | 28.1 | 14.2 | 28.7 | 15.3 | 10.4 | 2.4 | 0.9 | 6.03 | 13.7% | 3.3% |
| CHALLENGER | 3,268 | 14.8 | 10.3 | 20.8 | 15.0 | 15.4 | 11.9 | 11.8 | 11.02 | 39.1% | 23.7% |
| ITF_MEN | 5,615 | 10.1 | 8.2 | 18.1 | 14.1 | 20.5 | 16.5 | 12.5 | 14.88 | 49.5% | 29.0% |
| ITF_WOMEN | 7,714 | 9.9 | 7.0 | 16.5 | 15.7 | 22.9 | 18.0 | 10.1 | 15.39 | 50.9% | 28.0% |
| WTA | 1,007 | 22.8 | 15.4 | 32.2 | 15.9 | 10.6 | 2.4 | 0.7 | 6.12 | 13.7% | 3.1% |
| WTA125 | 628 | 22.4 | 12.4 | 29.0 | 15.3 | 14.5 | 6.0 | 0.3 | 7.72 | 20.9% | 6.4% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 741 | 31.3 | 22.7 | 35.1 | 9.2 | 1.4 | 0.4 | 0.0 | 4.68 | 1.8% | 0.4% |
| CHALLENGER | 2,234 | 22.4 | 15.2 | 27.6 | 14.8 | 12.8 | 5.2 | 2.0 | 6.94 | 20.0% | 7.2% |
| DOUBLES | 1,054 | 5.3 | 3.7 | 11.4 | 10.8 | 19.7 | 24.4 | 24.7 | 24.16 | 68.8% | 49.0% |
| ITF_MEN | 4,751 | 14.7 | 8.7 | 20.6 | 15.4 | 20.9 | 12.5 | 7.2 | 11.89 | 40.6% | 19.7% |
| ITF_WOMEN | 5,116 | 11.8 | 9.3 | 19.6 | 14.7 | 22.3 | 16.6 | 5.8 | 13.02 | 44.7% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 702 | 21.5 | 15.2 | 27.8 | 17.2 | 13.0 | 4.8 | 0.4 | 7.29 | 18.2% | 5.3% |
| WTA125 | 698 | 20.3 | 13.8 | 22.8 | 18.5 | 14.3 | 8.2 | 2.1 | 8.3 | 24.6% | 10.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,340 | 30.5 | 14.6 | 25.4 | 17.3 | 10.3 | 1.0 | 0.8 | 5.75 | 12.2% | 1.9% |
| CHALLENGER | 2,331 | 20.9 | 12.3 | 25.2 | 18.4 | 14.9 | 6.0 | 2.3 | 8.27 | 23.2% | 8.3% |
| ITF_MEN | 4,090 | 13.4 | 10.1 | 21.0 | 16.6 | 20.2 | 13.0 | 5.7 | 11.49 | 38.9% | 18.7% |
| ITF_WOMEN | 5,765 | 12.4 | 7.9 | 18.4 | 17.8 | 23.6 | 14.9 | 4.9 | 13.01 | 43.4% | 19.8% |
| WTA | 987 | 21.1 | 10.7 | 25.4 | 15.5 | 20.6 | 5.6 | 1.1 | 8.09 | 27.3% | 6.7% |
| WTA125 | 602 | 13.5 | 7.5 | 22.3 | 21.1 | 20.8 | 13.3 | 1.7 | 11.32 | 35.7% | 14.9% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,340 | 24.6 | 14.5 | 25.1 | 18.5 | 14.4 | 1.9 | 1.0 | 6.64 | 17.2% | 2.8% |
| CHALLENGER | 2,331 | 18.9 | 10.2 | 24.4 | 16.2 | 18.3 | 9.5 | 2.6 | 9.07 | 30.3% | 12.0% |
| ITF_MEN | 4,091 | 11.3 | 8.1 | 18.2 | 15.4 | 21.9 | 16.7 | 8.4 | 14.03 | 47.0% | 25.1% |
| ITF_WOMEN | 5,765 | 9.7 | 6.6 | 15.4 | 14.7 | 23.4 | 19.9 | 10.3 | 16.32 | 53.6% | 30.2% |
| WTA | 987 | 17.1 | 7.8 | 20.0 | 15.8 | 22.6 | 15.5 | 1.2 | 11.74 | 39.3% | 16.7% |
| WTA125 | 602 | 6.2 | 4.8 | 17.4 | 18.4 | 24.8 | 20.1 | 8.3 | 16.74 | 53.2% | 28.4% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 721 | 31.4 | 22.9 | 35.4 | 9.3 | 0.7 | 0.4 | 0.0 | 4.62 | 1.1% | 0.4% |
| CHALLENGER | 1,923 | 24.2 | 16.6 | 29.8 | 14.6 | 11.8 | 2.5 | 0.5 | 6.34 | 14.9% | 3.1% |
| DOUBLES | 968 | 5.5 | 3.8 | 11.7 | 10.9 | 19.5 | 24.5 | 24.1 | 24.07 | 68.1% | 48.5% |
| ITF_MEN | 3,917 | 16.1 | 9.5 | 22.5 | 16.2 | 20.8 | 10.5 | 4.3 | 10.58 | 35.6% | 14.8% |
| ITF_WOMEN | 4,182 | 12.9 | 10.0 | 21.4 | 15.5 | 22.5 | 14.9 | 2.7 | 11.57 | 40.2% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 668 | 22.0 | 15.9 | 28.0 | 17.2 | 13.2 | 3.7 | 0.0 | 7.08 | 16.9% | 3.7% |
| WTA125 | 590 | 22.2 | 15.2 | 24.4 | 20.2 | 12.7 | 4.9 | 0.3 | 7.38 | 18.0% | 5.2% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,054 | 5.3 | 3.7 | 11.4 | 10.8 | 19.7 | 24.4 | 24.7 | 24.16 | 68.8% | 49.0% |
| singles | 14,391 | 16.3 | 11.2 | 22.7 | 14.9 | 18.3 | 11.6 | 4.9 | 9.92 | 34.8% | 16.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 4,615 | 13.5 | 8.8 | 19.3 | 15.8 | 17.9 | 14.6 | 10.2 | 12.71 | 42.6% | 24.7% |
| Grass | 217 | 11.1 | 11.5 | 17.1 | 13.4 | 23.0 | 16.1 | 7.8 | 14.16 | 47.0% | 24.0% |
| Hard | 12,668 | 13.9 | 8.4 | 18.6 | 15.3 | 19.7 | 14.4 | 9.8 | 12.99 | 43.9% | 24.2% |
| UNKNOWN | 2,086 | 12.2 | 7.2 | 16.9 | 18.8 | 19.0 | 15.7 | 10.1 | 13.35 | 44.9% | 25.8% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,674 | 19.8 | 10.7 | 21.1 | 16.9 | 15.7 | 8.9 | 6.9 | 9.5 | 31.6% | 15.8% |
| B | 2,561 | 14.1 | 8.9 | 19.8 | 16.4 | 18.5 | 12.5 | 9.9 | 11.98 | 40.8% | 22.4% |
| C | 2,834 | 12.7 | 9.5 | 20.0 | 14.3 | 19.2 | 14.4 | 10.0 | 12.68 | 43.5% | 24.4% |
| D | 3,385 | 11.6 | 7.9 | 17.5 | 16.0 | 22.1 | 15.3 | 9.6 | 13.92 | 47.0% | 24.9% |
| F | 5,132 | 8.1 | 5.3 | 15.0 | 14.9 | 21.8 | 21.5 | 13.4 | 17.94 | 56.6% | 34.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,502 | 23.0 | 15.7 | 28.9 | 15.2 | 11.1 | 4.4 | 1.7 | 6.69 | 17.2% | 6.1% |
| B | 2,305 | 14.8 | 10.0 | 24.0 | 16.4 | 19.4 | 11.1 | 4.2 | 10.21 | 34.8% | 15.3% |
| C | 3,048 | 12.1 | 7.8 | 18.2 | 14.1 | 20.7 | 15.8 | 11.4 | 13.9 | 47.8% | 27.1% |
| D | 2,309 | 13.9 | 9.8 | 20.7 | 13.7 | 21.4 | 13.8 | 6.6 | 11.86 | 41.8% | 20.4% |
| F | 3,281 | 10.3 | 7.7 | 15.2 | 13.9 | 23.6 | 20.3 | 9.0 | 16.28 | 52.8% | 29.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 6,426 | 18.1 | 9.6 | 20.3 | 16.6 | 16.2 | 10.0 | 9.1 | 10.54 | 35.4% | 19.1% |
| LIMITED | 4,531 | 14.7 | 10.3 | 20.8 | 15.3 | 18.5 | 12.9 | 7.4 | 11.24 | 38.8% | 20.3% |
| POOR | 8,629 | 9.6 | 6.5 | 16.0 | 15.3 | 21.9 | 18.9 | 11.8 | 15.93 | 52.5% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,106 | 31.0 | 24.3 | 36.0 | 5.8 | 1.9 | 0.8 | 0.2 | 4.52 | 2.9% | 1.0% |
| GAME_SPREAD | 2,914 | 25.7 | 16.3 | 36.6 | 16.7 | 4.1 | 0.4 | 0.2 | 5.96 | 4.7% | 0.6% |
| MATCH_WINNER | 15,445 | 15.6 | 10.7 | 21.9 | 14.7 | 18.4 | 12.4 | 6.2 | 10.43 | 37.1% | 18.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 5,766 | 33.0 | 19.3 | 30.7 | 9.9 | 5.6 | 1.3 | 0.2 | 4.79 | 7.1% | 1.5% |
| TOTAL_GAMES | 4,515 | 6.6 | 9.1 | 39.2 | 29.3 | 10.7 | 2.8 | 2.3 | 9.46 | 15.8% | 5.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,009 | 25.5 | 38.1 | 31.1 | 0.4 | 4.0 | 0.7 | 0.2 | 4.31 | 4.9% | 0.9% |
| GAME_SPREAD | 3,545 | 45.5 | 16.6 | 28.5 | 7.2 | 1.1 | 0.7 | 0.4 | 3.53 | 2.2% | 1.1% |
| TOTAL_GAMES | 5,785 | 3.6 | 6.6 | 42.4 | 36.5 | 6.8 | 2.1 | 1.9 | 9.78 | 10.9% | 4.0% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,009 | 26.4 | 18.8 | 36.8 | 9.1 | 6.3 | 2.3 | 0.4 | 5.48 | 9.0% | 2.7% |
| GAME_SPREAD | 3,545 | 19.7 | 13.5 | 30.4 | 20.7 | 12.7 | 2.3 | 0.7 | 7.64 | 15.7% | 3.0% |
| TOTAL_GAMES | 5,794 | 6.7 | 9.1 | 37.8 | 27.8 | 13.1 | 3.5 | 2.1 | 9.61 | 18.6% | 5.5% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 19,586 | 43.7% | 24.5% | 12.99 | 34.9% | 15.1% | 10.65 |
| gen1_elo | 19,586 | 43.1% | 23.9% | 12.48 | 33.9% | 14.9% | 10.12 |
| gen1_sr | 19,586 | 52.3% | 30.7% | 15.89 | 44.5% | 21.4% | 13.29 |
| gen2 | 19,586 | 50.8% | 30.8% | 15.41 | 44.1% | 22.7% | 13.0 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 10,424 | 16.4 | 10.4 | 21.6 | 17.2 | 19.7 | 11.3 | 3.4 | 10.43 | 34.3% | 14.6% |
| STALE | 9,162 | 10.3 | 6.1 | 15.0 | 14.1 | 18.8 | 18.3 | 17.3 | 17.3 | 54.4% | 35.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 8,913 | 17.4 | 11.6 | 23.6 | 14.6 | 16.9 | 11.2 | 4.8 | 9.4 | 32.9% | 16.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 35,031 | 8913 | 13896 | 12222 | 24.4 | 159.0 | 1400.4 |
| ge_15pp | 14,297 | 2932 | 4866 | 6499 | 26.9 | 458.0 | 1380.4 |
| ge_25pp | 7,679 | 1422 | 2117 | 4140 | 34.5 | 586.0 | 1380.4 |
| lt_10pp | 15,385 | 4681 | 6684 | 4020 | 22.4 | 48.8 | 1341.5 |

Current slate `SL-20261016T171448Z-ccb61f5a`: 435 priced rows, quote age at build {'median': 10.3, 'max': 10.4}, freshness {'AGING': 435}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 10 | 0.0 | 0.0 | 40.0 | 0.0 | 40.0 | 20.0 | 0.0 | 20.33 | 60.0% | 20.0% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,697 | 21.3 | 11.0 | 22.9 | 18.2 | 19.0 | 7.0 | 0.6 | 8.71 | 26.6% | 7.6% |
| KALSHI_LONE_OUTLIER | 8 | 12.5 | 0.0 | 62.5 | 0.0 | 12.5 | 12.5 | 0.0 | 5.11 | 25.0% | 12.5% |
| MARKETS_AGREE | 272 | 71.0 | 29.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.07 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 546 | 0.0 | 3.7 | 35.4 | 27.7 | 23.6 | 8.8 | 0.9 | 11.66 | 33.3% | 9.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 19,586 | 2545 (13.0%) | 21.4% | 0.7% | {"EXTERNAL_STALE": 1697, "AGREES_WITH_KALSHI": 546, "ALL_AGREE": 272, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 9, "AGREES_WITH_MODEL": 8, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 8,566 | 642 (7.5%) | 28.3% | 1.2% | {"EXTERNAL_STALE": 452, "AGREES_WITH_KALSHI": 182, "SUPPORTS_MODEL_DIRECTION": 6, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 4,795 | 185 (3.9%) | 28.6% | 1.6% | {"EXTERNAL_STALE": 129, "AGREES_WITH_KALSHI": 53, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,282 | 174 (7.6%) | 29.3% | 1.7% | {"EXTERNAL_STALE": 120, "AGREES_WITH_KALSHI": 51, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 7,935 | 1443 (18.2%) | 14.8% | 0.6% | {"EXTERNAL_STALE": 936, "ALL_AGREE": 272, "AGREES_WITH_KALSHI": 213, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 6, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,792 | 11.2 | 7.8 | 19.6 | 15.0 | 22.0 | 14.3 | 10.2 | 13.73 | 46.5% | 24.5% |
| 4-10x | 2,535 | 12.7 | 8.9 | 19.7 | 15.5 | 18.9 | 15.3 | 9.0 | 12.72 | 43.2% | 24.3% |
| <2x | 10,219 | 15.4 | 9.1 | 18.9 | 16.7 | 17.7 | 13.1 | 9.1 | 11.93 | 39.9% | 22.2% |
| >=10x | 3,040 | 11.0 | 6.5 | 15.3 | 13.8 | 21.2 | 19.4 | 12.9 | 16.44 | 53.5% | 32.3% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 5,174 | 13.7 | 8.2 | 19.3 | 15.9 | 19.7 | 12.9 | 10.4 | 12.79 | 43.0% | 23.3% |
| 300-1000 | 4,417 | 11.9 | 8.7 | 17.3 | 16.0 | 20.9 | 15.8 | 9.3 | 13.69 | 46.1% | 25.2% |
| <300 | 5,820 | 9.1 | 6.0 | 15.7 | 14.7 | 21.5 | 20.2 | 12.8 | 16.81 | 54.5% | 33.0% |
| >=3000 | 4,175 | 21.4 | 11.7 | 22.9 | 16.9 | 13.8 | 7.5 | 5.8 | 8.38 | 27.1% | 13.3% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 614 | 0.5378 | 0.406 | 0.487 | +0.051 | -0.081 | 0.0001 ± 0.0059 |
| ratio 4-10x | 409 | 0.5841 | 0.4458 | 0.5086 | +0.075 | -0.063 | 0.0072 ± 0.0077 |
| ratio <2x | 1508 | 0.5366 | 0.4142 | 0.4536 | +0.083 | -0.039 | 0.0116 ± 0.0037 |
| ratio >=10x | 500 | 0.5442 | 0.3773 | 0.418 | +0.126 | -0.041 | 0.0155 ± 0.0079 |
| thinner_sample 1000-3000 | 850 | 0.5431 | 0.4178 | 0.4706 | +0.073 | -0.053 | 0.0057 ± 0.0049 |
| thinner_sample 300-1000 | 728 | 0.5589 | 0.4213 | 0.4849 | +0.074 | -0.064 | 0.0019 ± 0.0057 |
| thinner_sample <300 | 937 | 0.5429 | 0.3824 | 0.4354 | +0.107 | -0.053 | 0.0157 ± 0.0056 |
| thinner_sample >=3000 | 516 | 0.5294 | 0.4355 | 0.4632 | +0.066 | -0.028 | 0.0141 ± 0.0051 |
| data_status ADEQUATE | 879 | 0.5334 | 0.4287 | 0.4596 | +0.074 | -0.031 | 0.0095 ± 0.0042 |
| data_status LIMITED | 757 | 0.5508 | 0.4218 | 0.4888 | +0.062 | -0.067 | 0.0031 ± 0.0053 |
| data_status POOR | 1395 | 0.5481 | 0.3933 | 0.4487 | +0.099 | -0.055 | 0.0126 ± 0.0045 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 467 | 0.1928 | 0.1942 | -0.0014 ± 0.0007 | 0.5635 | 0.5664 | 0.4917 | 0.4769 | 0.5289 | -0.040 ± 0.0213 | -0.01 (5) |
| 3-5 | 294 | 0.1904 | 0.1907 | -0.0003 ± 0.002 | 0.5608 | 0.5601 | 0.5089 | 0.4691 | 0.4898 | -0.071 ± 0.0261 | 0.02 (1) |
| 5-10 | 639 | 0.1972 | 0.1966 | +0.0006 ± 0.0027 | 0.5798 | 0.576 | 0.5101 | 0.4356 | 0.4617 | -0.085 ± 0.0182 | -0.0167 (6) |
| 10-15 | 536 | 0.2121 | 0.2038 | +0.0083 ± 0.0049 | 0.6118 | 0.5892 | 0.5176 | 0.3938 | 0.4216 | -0.084 ± 0.0194 | -0.048 (5) |
| 15-25 | 663 | 0.231 | 0.216 | +0.0150 ± 0.007 | 0.6571 | 0.618 | 0.5762 | 0.3809 | 0.4419 | -0.079 ± 0.0179 | -0.0033 (9) |
| 25-40 | 358 | 0.2252 | 0.2084 | +0.0168 ± 0.0144 | 0.6408 | 0.5988 | 0.6449 | 0.3362 | 0.4637 | -0.062 ± 0.022 | -0.01 (1) |
| 40+ | 74 | 0.2888 | 0.1769 | +0.1119 ± 0.0433 | 0.7848 | 0.5268 | 0.7422 | 0.2957 | 0.3919 | -0.107 ± 0.043 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2183 | 0.1767 | 0.1779 | -0.0011 ± 0.0003 | 0.5268 | 0.5279 | 0.4778 | 0.4628 | 0.4984 | -0.020 ± 0.0091 | -0.0129 (17) |
| 3-5 | 1335 | 0.1925 | 0.1909 | +0.0017 ± 0.001 | 0.5652 | 0.5571 | 0.4807 | 0.441 | 0.4367 | -0.062 ± 0.0122 | 0.0 (2) |
| 5-10 | 2965 | 0.1926 | 0.1902 | +0.0024 ± 0.0012 | 0.5674 | 0.5583 | 0.4839 | 0.41 | 0.428 | -0.046 ± 0.0081 | -0.0119 (21) |
| 10-15 | 2559 | 0.2015 | 0.1826 | +0.0190 ± 0.0021 | 0.589 | 0.5369 | 0.4784 | 0.3539 | 0.3408 | -0.076 ± 0.0084 | -0.0281 (16) |
| 15-25 | 3140 | 0.2093 | 0.1719 | +0.0374 ± 0.0029 | 0.6111 | 0.5073 | 0.502 | 0.3059 | 0.3099 | -0.068 ± 0.0074 | -0.0025 (44) |
| 25-40 | 2455 | 0.2204 | 0.1267 | +0.0938 ± 0.0045 | 0.6341 | 0.3901 | 0.5278 | 0.215 | 0.2253 | -0.060 ± 0.0069 | -0.01 (1) |
| 40+ | 1656 | 0.3754 | 0.0433 | +0.3321 ± 0.0057 | 0.9773 | 0.1712 | 0.6261 | 0.1053 | 0.0574 | -0.084 ± 0.0048 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 352 | 0.198 | 0.1984 | -0.0004 ± 0.0008 | 0.5774 | 0.5783 | 0.5001 | 0.4849 | 0.5057 | -0.079 ± 0.0249 | -0.01 (3) |
| 3-5 | 242 | 0.2087 | 0.2075 | +0.0013 ± 0.0024 | 0.5995 | 0.598 | 0.5156 | 0.4756 | 0.4752 | -0.086 ± 0.0308 | 0.02 (1) |
| 5-10 | 549 | 0.1979 | 0.1966 | +0.0013 ± 0.0029 | 0.5789 | 0.5758 | 0.5499 | 0.4751 | 0.5046 | -0.076 ± 0.0196 | -0.01 (4) |
| 10-15 | 494 | 0.2149 | 0.2063 | +0.0086 ± 0.0051 | 0.6171 | 0.5974 | 0.5685 | 0.444 | 0.4757 | -0.090 ± 0.0213 | -0.04 (5) |
| 15-25 | 734 | 0.2286 | 0.2097 | +0.0189 ± 0.0067 | 0.6489 | 0.6019 | 0.587 | 0.3903 | 0.4441 | -0.083 ± 0.0171 | -0.0133 (9) |
| 25-40 | 479 | 0.2653 | 0.2006 | +0.0648 ± 0.0129 | 0.7423 | 0.5825 | 0.6591 | 0.3444 | 0.4008 | -0.106 ± 0.0203 | -0.0075 (4) |
| 40+ | 181 | 0.3567 | 0.1792 | +0.1776 ± 0.0307 | 0.9858 | 0.5294 | 0.738 | 0.2577 | 0.326 | -0.065 ± 0.0303 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1842 | 0.1829 | 0.1833 | -0.0004 ± 0.0003 | 0.5411 | 0.5418 | 0.497 | 0.4823 | 0.5049 | -0.034 ± 0.0103 | -0.0133 (15) |
| 3-5 | 1170 | 0.192 | 0.1911 | +0.0009 ± 0.001 | 0.5587 | 0.5566 | 0.5151 | 0.4751 | 0.4838 | -0.042 ± 0.013 | 0.02 (1) |
| 5-10 | 2611 | 0.1905 | 0.1872 | +0.0033 ± 0.0013 | 0.5633 | 0.5518 | 0.5117 | 0.4377 | 0.4546 | -0.045 ± 0.0086 | -0.0117 (6) |
| 10-15 | 2269 | 0.1955 | 0.1824 | +0.0131 ± 0.0022 | 0.5763 | 0.5342 | 0.5177 | 0.3933 | 0.4059 | -0.056 ± 0.0091 | -0.0189 (18) |
| 15-25 | 3285 | 0.2163 | 0.1773 | +0.0390 ± 0.0029 | 0.6282 | 0.5223 | 0.5315 | 0.3351 | 0.3373 | -0.072 ± 0.0074 | -0.0086 (42) |
| 25-40 | 2902 | 0.2484 | 0.1379 | +0.1105 ± 0.0044 | 0.7036 | 0.4211 | 0.5589 | 0.2428 | 0.2281 | -0.082 ± 0.0069 | -0.0044 (18) |
| 40+ | 2214 | 0.3981 | 0.0678 | +0.3303 ± 0.0063 | 1.0441 | 0.2358 | 0.6621 | 0.1263 | 0.0994 | -0.066 ± 0.0054 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 457 | 0.1924 | 0.1951 | -0.0026 ± 0.0007 | 0.5636 | 0.5702 | 0.4941 | 0.4788 | 0.5536 | -0.002 ± 0.021 | -0.0137 (8) |
| 3-5 | 327 | 0.1887 | 0.1864 | +0.0023 ± 0.0019 | 0.5537 | 0.5481 | 0.4985 | 0.4591 | 0.4526 | -0.117 ± 0.0252 | 0.0067 (3) |
| 5-10 | 669 | 0.202 | 0.1983 | +0.0038 ± 0.0026 | 0.5914 | 0.5788 | 0.5039 | 0.4302 | 0.438 | -0.094 ± 0.0177 | -0.0071 (7) |
| 10-15 | 523 | 0.2069 | 0.2067 | +0.0002 ± 0.0049 | 0.601 | 0.5965 | 0.5354 | 0.4124 | 0.4761 | -0.060 ± 0.0197 | -0.0317 (6) |
| 15-25 | 611 | 0.2375 | 0.2105 | +0.0270 ± 0.0072 | 0.675 | 0.6054 | 0.5837 | 0.3903 | 0.4173 | -0.112 ± 0.0183 | -0.03 (1) |
| 25-40 | 375 | 0.2102 | 0.2126 | -0.0024 ± 0.0139 | 0.6076 | 0.6085 | 0.6498 | 0.34 | 0.496 | -0.040 ± 0.0211 | 0.015 (2) |
| 40+ | 69 | 0.3095 | 0.1871 | +0.1224 ± 0.0467 | 0.8346 | 0.55 | 0.7478 | 0.2949 | 0.3913 | -0.098 ± 0.0489 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2088 | 0.1835 | 0.1845 | -0.0010 ± 0.0003 | 0.5415 | 0.5433 | 0.4821 | 0.4669 | 0.4966 | -0.022 ± 0.0095 | -0.0163 (35) |
| 3-5 | 1421 | 0.1855 | 0.1825 | +0.0030 ± 0.0009 | 0.5474 | 0.5403 | 0.4767 | 0.4373 | 0.4208 | -0.079 ± 0.0117 | -0.0094 (18) |
| 5-10 | 3151 | 0.1941 | 0.1878 | +0.0063 ± 0.0012 | 0.5723 | 0.5517 | 0.4799 | 0.4061 | 0.398 | -0.068 ± 0.0078 | -0.01 (31) |
| 10-15 | 2421 | 0.1948 | 0.1804 | +0.0144 ± 0.0021 | 0.5737 | 0.5303 | 0.4957 | 0.3724 | 0.3763 | -0.063 ± 0.0086 | -0.015 (12) |
| 15-25 | 3207 | 0.2113 | 0.1704 | +0.0409 ± 0.0029 | 0.6174 | 0.5046 | 0.5056 | 0.3104 | 0.3046 | -0.075 ± 0.0073 | -0.03 (2) |
| 25-40 | 2405 | 0.2151 | 0.1257 | +0.0894 ± 0.0045 | 0.622 | 0.3865 | 0.5254 | 0.21 | 0.2295 | -0.054 ± 0.0069 | 0.01 (3) |
| 40+ | 1600 | 0.389 | 0.0458 | +0.3433 ± 0.0061 | 1.0151 | 0.1779 | 0.6349 | 0.108 | 0.0575 | -0.086 ± 0.0051 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 787 | 0.1959 | 0.1961 | -0.0002 ± 0.0006 | 0.5725 | 0.5728 | 0.5076 | 0.4925 | 0.4994 | -0.048 ± 0.0158 | -0.0224 (49) |
| 3-5 | 563 | 0.1943 | 0.1939 | +0.0004 ± 0.0015 | 0.5668 | 0.5643 | 0.4809 | 0.4412 | 0.4529 | -0.045 ± 0.0186 | -0.0194 (34) |
| 5-10 | 1176 | 0.1965 | 0.1908 | +0.0057 ± 0.0019 | 0.5791 | 0.5629 | 0.4881 | 0.4145 | 0.4133 | -0.064 ± 0.013 | -0.005 (78) |
| 10-15 | 740 | 0.2077 | 0.1963 | +0.0114 ± 0.0041 | 0.604 | 0.5745 | 0.5048 | 0.3818 | 0.3959 | -0.055 ± 0.0164 | 0.0014 (64) |
| 15-25 | 993 | 0.2331 | 0.2116 | +0.0215 ± 0.0057 | 0.6646 | 0.6091 | 0.5634 | 0.3687 | 0.4119 | -0.054 ± 0.0146 | -0.0214 (59) |
| 25-40 | 577 | 0.2513 | 0.196 | +0.0553 ± 0.0114 | 0.7082 | 0.5697 | 0.6456 | 0.3331 | 0.3986 | -0.081 ± 0.0171 | -0.0219 (26) |
| 40+ | 193 | 0.3701 | 0.1933 | +0.1769 ± 0.0321 | 1.0713 | 0.5679 | 0.793 | 0.3026 | 0.3886 | -0.075 ± 0.029 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2348 | 0.1876 | 0.1877 | -0.0001 ± 0.0003 | 0.5508 | 0.5501 | 0.5029 | 0.4876 | 0.4987 | -0.034 ± 0.0089 | -0.0157 (88) |
| 3-5 | 1603 | 0.188 | 0.1856 | +0.0024 ± 0.0009 | 0.5504 | 0.5447 | 0.4889 | 0.4493 | 0.4392 | -0.056 ± 0.0108 | -0.0209 (69) |
| 5-10 | 3273 | 0.193 | 0.1855 | +0.0075 ± 0.0011 | 0.5704 | 0.5488 | 0.4819 | 0.4082 | 0.3969 | -0.063 ± 0.0076 | -0.0082 (132) |
| 10-15 | 2194 | 0.2043 | 0.1896 | +0.0147 ± 0.0023 | 0.5965 | 0.5575 | 0.51 | 0.387 | 0.3888 | -0.057 ± 0.0093 | -0.0053 (105) |
| 15-25 | 2776 | 0.2298 | 0.198 | +0.0318 ± 0.0033 | 0.6628 | 0.5755 | 0.555 | 0.3598 | 0.3775 | -0.061 ± 0.0085 | -0.0253 (107) |
| 25-40 | 1893 | 0.2542 | 0.1699 | +0.0842 ± 0.006 | 0.7203 | 0.5021 | 0.6072 | 0.2931 | 0.318 | -0.076 ± 0.0092 | -0.0229 (51) |
| 40+ | 911 | 0.3846 | 0.1311 | +0.2535 ± 0.0128 | 1.0911 | 0.4 | 0.7088 | 0.202 | 0.2184 | -0.068 ± 0.0114 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3031 | 1.059 ± 0.051 | 1.167 | 0.1684 | 0.1715 | 0.2114 | 0.2021 |
| gen2 | 3031 | 0.87 ± 0.046 | 1.122 | 0.1757 | 0.1715 | 0.2291 | 0.202 |
| gen1_elo | 3031 | 1.04 ± 0.05 | 1.152 | 0.1736 | 0.1719 | 0.2106 | 0.2019 |
| gen1_sr | 3031 | 1.079 ± 0.061 | 1.188 | 0.1353 | 0.1733 | 0.2252 | 0.2018 |
| gen1_ledger | 5029 | 0.874 ± 0.035 | 1.075 | 0.1772 | 0.1859 | 0.218 | 0.1976 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 14,297)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,567 | 24.9% |
| STALE_QUOTE | market_freshness | 2,989 | 20.9% |
| BOOK_QUALITY | execution | 2,561 | 17.9% |
| POOR_DATA | data | 1,580 | 11.1% |
| LIMITED_DATA | data | 1,022 | 7.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 772 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 683 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 560 | 3.9% |
| IN_PLAY_QUOTE | market_freshness/coverage | 405 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 158 | 1.1% |

Cause class: coverage 24.9%, market_freshness 20.9%, data 18.2%, execution 17.9%, market_freshness/coverage 8.2%, model_calibration_or_unknown 4.8%, mapping 3.9%, model_calibration 1.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 95.9%, LOW_DATA_QUALITY 69.2%, THIN_PLAYER_HISTORY 57.9%, STALE_PLAYER_DATA 52.2%, STALE_KALSHI_QUOTE 45.5%, MODEL_INTERNAL_DISAGREEMENT 39.4%, ASYMMETRIC_SAMPLE_SIZE 31.8%, WIDE_SPREAD 23.7%, MODEL_HIGH_UNCERTAINTY 17.5%, PLAYER_IDENTITY_RISK 14.0%, LEVEL_TRANSFER_RISK 8.3%, EVENT_MAPPING_RISK 8.0%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 3.5%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 27.3%, POST_SETTLEMENT_OBSERVATION 24.9%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 7,679)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,817 | 36.7% |
| STALE_QUOTE | market_freshness | 1,399 | 18.2% |
| BOOK_QUALITY | execution | 1,332 | 17.3% |
| POOR_DATA | data | 638 | 8.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 415 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 327 | 4.3% |
| LIMITED_DATA | data | 309 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 249 | 3.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 155 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 38 | 0.5% |

Cause class: coverage 36.7%, market_freshness 18.2%, execution 17.3%, data 12.3%, market_freshness/coverage 8.6%, mapping 4.3%, model_calibration_or_unknown 2.0%, model_calibration 0.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.9%, START_UNVERIFIABLE 98.2%, LOW_DATA_QUALITY 72.7%, THIN_PLAYER_HISTORY 60.2%, STALE_KALSHI_QUOTE 53.9%, STALE_PLAYER_DATA 47.2%, MODEL_INTERNAL_DISAGREEMENT 40.3%, ASYMMETRIC_SAMPLE_SIZE 33.6%, WIDE_SPREAD 23.4%, MODEL_HIGH_UNCERTAINTY 18.0%, PLAYER_IDENTITY_RISK 17.3%, EVENT_MAPPING_RISK 9.7%, LOW_DISPLAYED_LIQUIDITY 8.1%, LEVEL_TRANSFER_RISK 7.4%, MODEL_CALIBRATION_OUTLIER 4.5%, EXTERNAL_MARKET_REJECTION 1.0%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 39.4%, POST_SETTLEMENT_OBSERVATION 36.7%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 6150, "IDENTITY_AMBIGUOUS": 1529}; ticker orientation: {"VERIFIED": 7679}.

Checks: discipline:AMBIGUOUS 517, discipline:PASS 7162, identity_confidence:AMBIGUOUS 1330, identity_confidence:PASS 6349, level_mapping:NA 529, level_mapping:PASS 7150, market_pair:AMBIGUOUS 283, market_pair:NA 188, market_pair:PASS 7208, model_complement:NA 155, model_complement:PASS 7524, namesake:PASS 7679, physical_match_id:NA 2884, physical_match_id:PASS 4795, player_ids:PASS 7679, same_pair_other_event:PASS 7679, ticker_orientation:PASS 7679

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,095 | 1.4% | 1.4% | 0.4% | {"market_freshness": 20, "execution": 8, "market_freshness/coverage": 1} | 5.24 | 0.2088 / 0.2109 (259) | 16.4% | 0.6% | 5.3% | 1.6% |
| CHALLENGER | 5,502 | 17.1% | 5.9% | 12.2% | {"coverage": 569, "market_freshness/coverage": 117, "market_freshness": 112, "data": 65, "model_calibration_or_unknown": 48, "execution": 13, "model_calibration": 9, "mapping": 6} | 7.17 | 0.2177 / 0.2043 (1441) | 37.2% | 9.3% | 2.4% | 22.7% |
| DOUBLES | 1,054 | 49.0% | 48.5% | 6.7% | {"execution": 211, "mapping": 153, "market_freshness": 106, "market_freshness/coverage": 40, "coverage": 7} | 24.07 | 0.3273 / 0.2332 (325) | 22.2% | 0.0% | 100.0% | 8.2% |
| ITF_MEN | 10,366 | 24.5% | 16.8% | 33.1% | {"coverage": 989, "execution": 516, "market_freshness": 398, "data": 345, "market_freshness/coverage": 204, "mapping": 85, "model_calibration_or_unknown": 2} | 11.11 | 0.2134 / 0.1947 (2554) | 36.4% | 60.9% | 12.1% | 22.8% |
| ITF_WOMEN | 12,830 | 26.2% | 18.9% | 43.9% | {"coverage": 1235, "market_freshness": 688, "execution": 558, "data": 503, "market_freshness/coverage": 253, "mapping": 77, "model_calibration_or_unknown": 43, "model_calibration": 10} | 12.51 | 0.2018 / 0.1918 (2685) | 39.2% | 57.3% | 10.0% | 22.5% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,709 | 6.1% | 5.5% | 1.4% | {"market_freshness": 36, "model_calibration_or_unknown": 23, "execution": 12, "data": 11, "market_freshness/coverage": 10, "model_calibration": 8, "coverage": 4, "mapping": 1} | 7.73 | 0.2398 / 0.2312 (289) | 25.6% | 1.6% | 1.8% | 3.2% |
| WTA125 | 1,326 | 12.9% | 10.2% | 2.2% | {"market_freshness/coverage": 38, "model_calibration_or_unknown": 37, "market_freshness": 37, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.38 | 0.217 / 0.2063 (465) | 22.9% | 7.7% | 4.4% | 10.1% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 5 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 6 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 7 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 207 min (STALE); no external reference |
| 9 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 10 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 11 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 12 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 13 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 14 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 15 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 16 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 17 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 18 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 19 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 20 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 22 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 23 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 24 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 25 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 26 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 27 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 12.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 768 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 28 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 29 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 30 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 31 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 32 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 162 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 33 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 34 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 35 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 36 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 37 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 33 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 38 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 39 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFWMATCH-26OCT16ESTLAB-LAB` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | POOR_DATA | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1475.0, ratio 2.28); no external reference |
| 41 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 42 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 43 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 44 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.8h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 359 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 45 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 46 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 47 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 48 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 49 | `KXATPCHALLENGERMATCH-26OCT13GIUSEA-SEA` | CHALLENGER | fair_v1 | 76% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 243 min (STALE); no external reference |
| 50 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 760 min (STALE); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9826, "by_level_share_of_ge_25pp": {"ATP": 0.0038, "CHALLENGER": 0.1223, "DOUBLES": 0.0673, "ITF_MEN": 0.3306, "ITF_WOMEN": 0.4385, "OTHER": 0.0016, "WTA": 0.0137, "WTA125": 0.0223}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5391, "share_primary_cause_market_settled_or_in_play": 0.4532, "share_primary_cause_stale_quote_only": 0.1822}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 7679, "identity_ambiguous_share": 0.1991, "ticker_orientation": {"VERIFIED": 7679}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 4795, "with_external": 185, "coverage": 0.0386, "external_status": {"EXTERNAL_STALE": 129, "AGREES_WITH_KALSHI": 53, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 129, "MODEL_LONE_OUTLIER": 53, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.2865, "share_external_supports_model": 0.0162}, "pregame_clean_ge_25pp": {"n": 2282, "with_external": 174, "coverage": 0.0762, "external_status": {"EXTERNAL_STALE": 120, "AGREES_WITH_KALSHI": 51, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 120, "MODEL_LONE_OUTLIER": 51, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.2931, "share_external_supports_model": 0.0172}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 561.0, "median_sample_ratio": 2.37, "median_min_matches": 20.0, "median_max_days_since_last": 204.0, "share_severe_asymmetry": 0.2028, "data_status": {"POOR": 4093, "LIMITED": 2185, "ADEQUATE": 1401}, "comparison_lt_10pp": {"median_thinner_serve_points": 1786.0, "median_sample_ratio": 1.69, "median_min_matches": 87.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 614, "model_minus_observed": 0.0509, "kalshi_minus_observed": -0.081, "brier_diff_model_minus_kalshi": 0.0001}, "4-10x": {"n": 409, "model_minus_observed": 0.0755, "kalshi_minus_observed": -0.0628, "brier_diff_model_minus_kalshi": 0.0072}, "<2x": {"n": 1508, "model_minus_observed": 0.083, "kalshi_minus_observed": -0.0394, "brier_diff_model_minus_kalshi": 0.0116}, ">=10x": {"n": 500, "model_minus_observed": 0.1262, "kalshi_minus_observed": -0.0407, "brier_diff_model_minus_kalshi": 0.0155}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3031, "model": {"intercept": -0.549, "slope": 0.87, "slope_se": 0.046}, "kalshi_mid_same_rows": {"intercept": 0.229, "slope": 1.122, "slope_se": 0.052}, "mean_extremity_model": 0.1757, "mean_extremity_kalshi": 0.1715, "model_brier": 0.2291, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0271, "brier_diff_se": 0.0034, "model_logloss": 0.6537, "kalshi_logloss": 0.586}, "fair_v1": {"n": 3031, "model": {"intercept": -0.402, "slope": 1.059, "slope_se": 0.051}, "kalshi_mid_same_rows": {"intercept": 0.311, "slope": 1.167, "slope_se": 0.054}, "mean_extremity_model": 0.1684, "mean_extremity_kalshi": 0.1715, "model_brier": 0.2114, "kalshi_brier": 0.2021, "brier_diff_model_minus_kalshi": 0.0093, "brier_diff_se": 0.0028, "model_logloss": 0.6102, "kalshi_logloss": 0.586}, "gen1_elo": {"n": 3031, "model": {"intercept": -0.393, "slope": 1.04, "slope_se": 0.05}, "kalshi_mid_same_rows": {"intercept": 0.303, "slope": 1.152, "slope_se": 0.053}, "mean_extremity_model": 0.1736, "mean_extremity_kalshi": 0.1719, "model_brier": 0.2106, "kalshi_brier": 0.2019, "brier_diff_model_minus_kalshi": 0.0087, "brier_diff_se": 0.0027, "model_logloss": 0.6092, "kalshi_logloss": 0.5856}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2448, "share_ge_15": 0.4374, "median_abs_gap": 12.99, "n": 19586}, "gen1_elo": {"share_ge_25": 0.2389, "share_ge_15": 0.4309, "median_abs_gap": 12.48, "n": 19586}, "gen1_sr": {"share_ge_25": 0.3069, "share_ge_15": 0.5233, "median_abs_gap": 15.89, "n": 19586}, "gen2": {"share_ge_25": 0.3077, "share_ge_15": 0.5085, "median_abs_gap": 15.41, "n": 19586}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.151, "share_ge_15": 0.3492, "median_abs_gap": 10.65, "n": 15115}, "gen1_elo": {"share_ge_25": 0.1487, "share_ge_15": 0.339, "median_abs_gap": 10.12, "n": 15114}, "gen1_sr": {"share_ge_25": 0.2136, "share_ge_15": 0.4452, "median_abs_gap": 13.29, "n": 15115}, "gen2": {"share_ge_25": 0.2266, "share_ge_15": 0.4408, "median_abs_gap": 13.0, "n": 15116}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.24, "share_ge_25_all": 0.0138, "share_ge_25_pregame_clean": 0.0136}, "WTA": {"median_abs_gap_pregame_clean": 7.73, "share_ge_25_all": 0.0614, "share_ge_25_pregame_clean": 0.055}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2387, "share_within_10pp_all": 0.4392, "share_within_10pp_pregame_clean": 0.497, "corr_model_vs_mid_pregame_clean": 0.8437}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 467, "model_brier": 0.1928, "kalshi_brier": 0.1942, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 536, "model_brier": 0.2121, "kalshi_brier": 0.2038, "brier_diff_model_minus_kalshi": 0.0083}, "15-25": {"n_settled": 663, "model_brier": 0.231, "kalshi_brier": 0.216, "brier_diff_model_minus_kalshi": 0.015}, "25-40": {"n_settled": 358, "model_brier": 0.2252, "kalshi_brier": 0.2084, "brier_diff_model_minus_kalshi": 0.0168}, "3-5": {"n_settled": 294, "model_brier": 0.1904, "kalshi_brier": 0.1907, "brier_diff_model_minus_kalshi": -0.0003}, "40+": {"n_settled": 74, "model_brier": 0.2888, "kalshi_brier": 0.1769, "brier_diff_model_minus_kalshi": 0.1119}, "5-10": {"n_settled": 639, "model_brier": 0.1972, "kalshi_brier": 0.1966, "brier_diff_model_minus_kalshi": 0.0006}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.549, "slope": 0.87, "slope_se": 0.046}, "kalshi_slope": {"intercept": 0.229, "slope": 1.122, "slope_se": 0.052}, "n": 3031}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.514, "slope": 0.874, "slope_se": 0.035}, "kalshi_slope": {"intercept": 0.144, "slope": 1.075, "slope_se": 0.039}, "n": 5029}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 325, "model_brier": 0.3273, "kalshi_brier": 0.2332, "brier_diff_model_minus_kalshi": 0.0942, "brier_diff_se": 0.0175, "corr_model_outcome": 0.011, "corr_kalshi_outcome": 0.258}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
