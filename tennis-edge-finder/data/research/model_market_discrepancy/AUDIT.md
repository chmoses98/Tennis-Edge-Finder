# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-23T18:28Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 50,881): 0-3 13.9%, 3-5 9.5%, 5-10 19.7%, 10-15 15.3%, 15-25 19.3%, 25-40 14.1%, 40+ 8.3%; median gap 12.15 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.9%, Challenger 11.9%, doubles 6.6%). Main tour: ATP 4.7% and WTA 5.2% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 11,387): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.6%, STALE_QUOTE 18.7%, BOOK_QUALITY 18.0%, POOR_DATA 8.8%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.5%, IN_PLAY_QUOTE 3.6%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.6%, market_freshness 18.7%, execution 18.0%, data 12.3%, market_freshness/coverage 9.0%, mapping 4.5%, model_calibration_or_unknown 2.2%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.4% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.6% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 11,387 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.1% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.9% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 490.0 points vs 1669.5 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.036, Gen-2 0.839, Gen-1 ledger 0.861 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 554 model 0.2237 vs Kalshi 0.209; n 112 model 0.2783 vs Kalshi 0.1982.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 219,855 model-market comparisons (358,027 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 72,847 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-23T18:14:33.174474+00:00'], shadow board 58,840 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-23T18:14:37.576509+00:00'], Model 4 27,447 rows, 19,537 settled tickers, 6,886 tickers with an external scan.
* By model: {"gen1_ledger": 49524, "gen1_elo": 29590, "fair_v1": 29590, "gen2": 29590, "gen1_sr": 29590, "model4_fundamental": 25999, "model4_conditioned": 25972}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 50,881 | 13.9 | 9.5 | 19.7 | 15.3 | 19.3 | 14.1 | 8.3 | 12.15 | 41.7% | 22.4% |
| MW fair_v1 | 29,590 | 12.8 | 8.5 | 18.4 | 15.6 | 19.7 | 15.0 | 10.0 | 13.23 | 44.8% | 25.0% |
| MW gen1_elo | 29,590 | 12.7 | 8.5 | 18.9 | 15.3 | 19.9 | 15.1 | 9.7 | 13.05 | 44.7% | 24.7% |
| MW gen1_ledger | 21,291 | 15.4 | 10.8 | 21.4 | 15.0 | 18.7 | 12.8 | 5.9 | 10.58 | 37.4% | 18.7% |
| MW gen1_sr | 29,590 | 10.2 | 7.0 | 16.5 | 13.6 | 20.9 | 18.9 | 13.0 | 16.09 | 52.7% | 31.9% |
| MW gen2 | 29,590 | 10.9 | 7.3 | 16.2 | 14.0 | 19.5 | 18.0 | 14.2 | 15.67 | 51.6% | 32.1% |
| all families model4_conditioned | 25,972 | 21.9 | 18.9 | 34.7 | 17.6 | 4.4 | 1.5 | 1.0 | 5.96 | 6.9% | 2.5% |
| all families model4_fundamental | 25,999 | 16.6 | 13.4 | 34.1 | 20.6 | 10.6 | 3.5 | 1.3 | 7.78 | 15.3% | 4.7% |

Configurable thresholds (primary): >=5pp 76.7%, >=10pp 57.0%, >=15pp 41.7%, >=20pp 31.0%, >=25pp 22.4%, >=30pp 16.2%, >=40pp 8.3%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.53pp; >=10pp 45.6%, >=25pp 17.5%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,522 | 28.4 | 14.3 | 25.0 | 15.0 | 11.8 | 4.8 | 0.7 | 6.07 | 17.4% | 5.5% |
| CHALLENGER | 4,609 | 15.8 | 10.0 | 20.5 | 15.5 | 14.8 | 12.4 | 11.2 | 11.07 | 38.3% | 23.5% |
| ITF_MEN | 8,203 | 10.2 | 7.3 | 16.8 | 14.7 | 21.5 | 17.4 | 12.1 | 15.35 | 50.9% | 29.5% |
| ITF_WOMEN | 11,814 | 9.3 | 6.8 | 16.0 | 15.4 | 22.4 | 18.2 | 11.9 | 15.79 | 52.4% | 30.1% |
| WTA | 1,782 | 17.1 | 13.4 | 25.6 | 19.6 | 18.4 | 5.2 | 0.7 | 8.25 | 24.3% | 5.9% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,522 | 24.2 | 15.1 | 24.9 | 17.2 | 13.0 | 4.8 | 0.9 | 6.5 | 18.7% | 5.7% |
| CHALLENGER | 4,609 | 15.1 | 8.8 | 18.5 | 14.5 | 17.3 | 13.8 | 12.0 | 12.48 | 43.1% | 25.8% |
| ITF_MEN | 8,203 | 8.2 | 5.9 | 14.5 | 13.0 | 19.7 | 20.9 | 17.8 | 18.63 | 58.5% | 38.7% |
| ITF_WOMEN | 11,814 | 8.1 | 5.7 | 13.7 | 13.4 | 20.6 | 21.0 | 17.6 | 19.03 | 59.1% | 38.5% |
| WTA | 1,782 | 14.0 | 10.2 | 21.9 | 16.2 | 23.2 | 13.4 | 1.1 | 10.97 | 37.6% | 14.5% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,522 | 24.4 | 12.8 | 23.6 | 16.2 | 14.9 | 7.0 | 1.1 | 7.33 | 23.0% | 8.1% |
| CHALLENGER | 4,609 | 14.3 | 9.1 | 20.5 | 15.6 | 16.2 | 12.9 | 11.3 | 11.49 | 40.5% | 24.2% |
| ITF_MEN | 8,203 | 9.7 | 7.4 | 16.9 | 14.0 | 22.0 | 17.7 | 12.3 | 15.67 | 52.0% | 30.0% |
| ITF_WOMEN | 11,814 | 9.4 | 6.6 | 16.2 | 15.8 | 22.8 | 18.1 | 11.0 | 15.62 | 52.0% | 29.2% |
| WTA | 1,782 | 24.1 | 16.8 | 30.5 | 15.5 | 10.0 | 2.6 | 0.5 | 6.04 | 13.1% | 3.1% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,475 | 25.4 | 19.4 | 30.9 | 12.0 | 8.9 | 3.0 | 0.3 | 5.58 | 12.3% | 3.3% |
| CHALLENGER | 3,159 | 21.4 | 14.7 | 26.4 | 14.4 | 14.6 | 6.7 | 1.9 | 7.3 | 23.2% | 8.6% |
| DOUBLES | 1,591 | 5.5 | 4.4 | 11.5 | 10.4 | 21.1 | 26.1 | 21.1 | 23.85 | 68.3% | 47.1% |
| ITF_MEN | 6,075 | 13.8 | 9.1 | 19.9 | 16.1 | 21.3 | 13.3 | 6.6 | 12.21 | 41.2% | 19.9% |
| ITF_WOMEN | 7,055 | 12.7 | 9.0 | 19.3 | 15.1 | 21.6 | 16.3 | 6.1 | 12.84 | 43.9% | 22.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,055 | 22.3 | 16.0 | 29.6 | 18.1 | 10.1 | 3.6 | 0.4 | 6.86 | 14.0% | 4.0% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,452 | 28.6 | 14.5 | 25.4 | 15.0 | 11.6 | 4.5 | 0.5 | 5.94 | 16.5% | 4.9% |
| CHALLENGER | 3,247 | 20.7 | 12.4 | 25.2 | 17.9 | 15.2 | 6.7 | 1.9 | 8.33 | 23.8% | 8.6% |
| ITF_MEN | 6,027 | 12.3 | 8.8 | 20.2 | 16.6 | 22.6 | 14.3 | 5.2 | 12.53 | 42.1% | 19.5% |
| ITF_WOMEN | 8,830 | 11.1 | 8.2 | 18.2 | 17.4 | 24.3 | 15.3 | 5.5 | 13.52 | 45.1% | 20.8% |
| WTA | 1,732 | 17.3 | 13.2 | 25.6 | 19.9 | 18.3 | 5.0 | 0.8 | 8.25 | 24.0% | 5.7% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,452 | 24.5 | 15.4 | 25.0 | 17.1 | 13.0 | 4.5 | 0.6 | 6.41 | 18.0% | 5.1% |
| CHALLENGER | 3,247 | 19.1 | 11.3 | 23.0 | 17.4 | 17.6 | 9.4 | 2.2 | 9.08 | 29.2% | 11.6% |
| ITF_MEN | 6,028 | 9.8 | 7.1 | 16.8 | 14.9 | 21.7 | 19.2 | 10.6 | 15.5 | 51.5% | 29.8% |
| ITF_WOMEN | 8,831 | 9.2 | 6.5 | 15.2 | 14.9 | 22.6 | 20.4 | 11.1 | 16.57 | 54.1% | 31.5% |
| WTA | 1,732 | 14.1 | 10.2 | 21.9 | 16.1 | 23.2 | 13.3 | 1.1 | 11.0 | 37.6% | 14.4% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,428 | 25.6 | 19.7 | 30.9 | 12.2 | 8.5 | 2.9 | 0.2 | 5.5 | 11.6% | 3.1% |
| CHALLENGER | 2,753 | 22.9 | 15.8 | 27.9 | 14.3 | 13.9 | 4.7 | 0.6 | 6.72 | 19.2% | 5.2% |
| DOUBLES | 1,476 | 5.5 | 4.5 | 11.7 | 10.6 | 21.0 | 26.0 | 20.7 | 23.62 | 67.7% | 46.7% |
| ITF_MEN | 5,086 | 14.9 | 9.7 | 21.5 | 16.9 | 21.2 | 11.7 | 4.0 | 11.2 | 36.9% | 15.7% |
| ITF_WOMEN | 5,840 | 13.6 | 9.6 | 20.7 | 16.0 | 21.8 | 15.0 | 3.4 | 11.67 | 40.1% | 18.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,005 | 22.8 | 16.5 | 29.6 | 18.1 | 10.1 | 2.9 | 0.1 | 6.79 | 13.0% | 3.0% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,591 | 5.5 | 4.4 | 11.5 | 10.4 | 21.1 | 26.1 | 21.1 | 23.85 | 68.3% | 47.1% |
| singles | 19,700 | 16.2 | 11.3 | 22.2 | 15.3 | 18.5 | 11.8 | 4.7 | 10.04 | 34.9% | 16.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 6,574 | 13.0 | 8.9 | 19.2 | 15.6 | 18.7 | 14.7 | 10.0 | 12.88 | 43.3% | 24.6% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 18,274 | 13.2 | 8.6 | 18.5 | 15.2 | 19.8 | 14.9 | 9.8 | 13.15 | 44.6% | 24.7% |
| UNKNOWN | 4,505 | 10.7 | 7.6 | 17.2 | 16.9 | 20.6 | 16.2 | 10.8 | 14.09 | 47.6% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,263 | 19.4 | 11.9 | 21.4 | 16.5 | 15.3 | 9.1 | 6.4 | 9.17 | 30.8% | 15.5% |
| B | 3,678 | 12.3 | 8.7 | 19.9 | 16.2 | 19.2 | 12.7 | 10.9 | 12.59 | 42.8% | 23.6% |
| C | 4,184 | 11.4 | 8.7 | 19.8 | 15.1 | 19.5 | 14.8 | 10.7 | 13.23 | 45.0% | 25.5% |
| D | 4,644 | 12.1 | 7.7 | 17.3 | 15.5 | 21.5 | 15.7 | 10.2 | 13.98 | 47.4% | 25.9% |
| F | 8,821 | 7.6 | 5.5 | 15.0 | 14.6 | 23.4 | 21.3 | 12.5 | 17.8 | 57.2% | 33.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,982 | 23.0 | 15.9 | 28.9 | 15.1 | 11.6 | 4.1 | 1.5 | 6.68 | 17.2% | 5.6% |
| B | 2,913 | 16.2 | 10.4 | 23.2 | 16.3 | 19.3 | 10.7 | 4.0 | 10.04 | 33.9% | 14.7% |
| C | 4,198 | 11.3 | 7.4 | 18.1 | 14.3 | 21.6 | 16.7 | 10.6 | 14.38 | 48.8% | 27.3% |
| D | 2,984 | 14.4 | 9.8 | 19.8 | 14.5 | 21.0 | 14.3 | 6.1 | 12.04 | 41.4% | 20.4% |
| F | 5,214 | 10.2 | 8.5 | 15.5 | 14.9 | 22.8 | 20.1 | 8.1 | 15.49 | 50.9% | 28.2% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 9,499 | 17.6 | 10.7 | 20.7 | 16.3 | 15.8 | 10.0 | 8.9 | 10.28 | 34.7% | 18.9% |
| LIMITED | 6,295 | 13.2 | 10.0 | 20.5 | 15.6 | 19.3 | 13.5 | 7.9 | 11.98 | 40.7% | 21.4% |
| POOR | 13,796 | 9.2 | 6.3 | 15.9 | 15.0 | 22.6 | 19.2 | 11.7 | 16.21 | 53.5% | 30.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,797 | 26.1 | 19.9 | 33.9 | 12.4 | 5.4 | 2.1 | 0.2 | 5.42 | 7.8% | 2.4% |
| GAME_SPREAD | 4,745 | 22.3 | 15.2 | 33.6 | 17.3 | 9.0 | 2.3 | 0.3 | 6.73 | 11.6% | 2.6% |
| MATCH_WINNER | 21,291 | 15.4 | 10.8 | 21.4 | 15.0 | 18.7 | 12.8 | 5.9 | 10.58 | 37.4% | 18.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 10,137 | 29.3 | 17.1 | 31.0 | 12.4 | 8.0 | 1.9 | 0.4 | 5.45 | 10.2% | 2.2% |
| TOTAL_GAMES | 7,530 | 8.8 | 9.7 | 36.5 | 28.8 | 10.4 | 3.2 | 2.6 | 9.43 | 16.2% | 5.8% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,105 | 25.4 | 33.4 | 32.6 | 4.5 | 3.1 | 0.7 | 0.2 | 4.49 | 4.1% | 0.9% |
| GAME_SPREAD | 6,231 | 45.6 | 16.7 | 26.9 | 7.9 | 1.7 | 0.9 | 0.3 | 3.48 | 2.9% | 1.2% |
| TOTAL_GAMES | 10,636 | 5.0 | 7.8 | 41.1 | 34.5 | 6.9 | 2.5 | 2.1 | 9.58 | 11.6% | 4.6% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,108 | 24.2 | 17.7 | 35.5 | 12.6 | 7.0 | 2.6 | 0.3 | 5.84 | 10.0% | 2.9% |
| GAME_SPREAD | 6,234 | 19.4 | 13.4 | 27.8 | 20.8 | 13.3 | 4.3 | 0.9 | 7.96 | 18.6% | 5.3% |
| TOTAL_GAMES | 10,657 | 8.5 | 9.6 | 36.6 | 27.2 | 12.1 | 3.7 | 2.3 | 9.45 | 18.0% | 5.9% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 29,590 | 44.8% | 25.0% | 13.23 | 36.4% | 15.7% | 10.98 |
| gen1_elo | 29,590 | 44.7% | 24.7% | 13.05 | 36.1% | 15.8% | 10.81 |
| gen1_sr | 29,590 | 52.7% | 31.9% | 16.09 | 44.9% | 22.4% | 13.23 |
| gen2 | 29,590 | 51.6% | 32.1% | 15.67 | 44.8% | 24.0% | 13.14 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 15,009 | 15.6 | 10.4 | 21.2 | 17.2 | 20.2 | 12.0 | 3.4 | 10.79 | 35.6% | 15.4% |
| STALE | 14,581 | 9.8 | 6.6 | 15.6 | 13.8 | 19.3 | 18.1 | 16.8 | 17.02 | 54.2% | 34.9% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 14,759 | 16.5 | 11.3 | 22.2 | 15.1 | 17.9 | 12.2 | 4.8 | 10.0 | 34.9% | 17.1% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 50,881 | 14759 | 18481 | 17641 | 24.2 | 146.4 | 1400.4 |
| ge_15pp | 21,201 | 5159 | 6629 | 9413 | 26.2 | 440.0 | 1380.4 |
| ge_25pp | 11,387 | 2521 | 2901 | 5965 | 32.5 | 579.9 | 1380.4 |
| lt_10pp | 21,892 | 7378 | 8718 | 5796 | 22.4 | 48.3 | 1341.5 |

Current slate `SL-20261023T182814Z-050c3eda`: 486 priced rows, quote age at build {'median': 14.0, 'max': 14.1}, freshness {'AGING': 486}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 23 | 0.0 | 0.0 | 21.7 | 4.3 | 39.1 | 34.8 | 0.0 | 20.49 | 73.9% | 34.8% |
| EXTERNAL_LONE_OUTLIER | 14 | 71.4 | 28.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.4 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,771 | 19.1 | 11.2 | 24.6 | 18.8 | 18.4 | 7.3 | 0.7 | 8.96 | 26.4% | 8.0% |
| KALSHI_LONE_OUTLIER | 17 | 5.9 | 5.9 | 76.5 | 0.0 | 5.9 | 5.9 | 0.0 | 6.11 | 11.8% | 5.9% |
| MARKETS_AGREE | 554 | 63.9 | 36.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.34 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,179 | 0.0 | 2.2 | 35.7 | 25.9 | 24.7 | 10.8 | 0.8 | 12.27 | 36.2% | 11.5% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 29,590 | 4558 (15.4%) | 25.9% | 0.9% | {"EXTERNAL_STALE": 2771, "AGREES_WITH_KALSHI": 1179, "ALL_AGREE": 554, "SUPPORTS_MODEL_DIRECTION": 22, "AGREES_WITH_MODEL": 17, "EXTERNAL_OUTLIER": 14, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 13,243 | 1177 (8.9%) | 36.3% | 1.6% | {"EXTERNAL_STALE": 731, "AGREES_WITH_KALSHI": 427, "SUPPORTS_MODEL_DIRECTION": 17, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 7,404 | 367 (5.0%) | 37.1% | 2.5% | {"EXTERNAL_STALE": 222, "AGREES_WITH_KALSHI": 136, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,605 | 344 (9.5%) | 37.5% | 2.6% | {"EXTERNAL_STALE": 206, "AGREES_WITH_KALSHI": 129, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 11,745 | 2555 (21.8%) | 17.5% | 0.7% | {"EXTERNAL_STALE": 1520, "ALL_AGREE": 554, "AGREES_WITH_KALSHI": 447, "AGREES_WITH_MODEL": 15, "EXTERNAL_OUTLIER": 14, "SUPPORTS_MODEL_DIRECTION": 4, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,648 | 10.1 | 7.5 | 19.5 | 14.3 | 22.4 | 16.0 | 10.2 | 14.29 | 48.6% | 26.2% |
| 4-10x | 3,876 | 11.0 | 8.2 | 19.1 | 15.3 | 21.2 | 15.0 | 10.2 | 13.77 | 46.4% | 25.2% |
| <2x | 14,944 | 14.8 | 9.7 | 19.0 | 16.5 | 17.6 | 13.1 | 9.2 | 11.91 | 40.0% | 22.4% |
| >=10x | 5,122 | 10.9 | 6.3 | 15.2 | 14.4 | 21.9 | 19.5 | 11.8 | 16.29 | 53.2% | 31.3% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 7,508 | 12.2 | 8.5 | 19.6 | 16.0 | 19.2 | 13.7 | 10.8 | 12.98 | 43.7% | 24.5% |
| 300-1000 | 6,362 | 11.6 | 8.5 | 17.2 | 15.4 | 20.6 | 16.4 | 10.3 | 14.0 | 47.3% | 26.6% |
| <300 | 9,755 | 8.6 | 5.7 | 15.5 | 14.8 | 22.9 | 20.1 | 12.3 | 16.95 | 55.4% | 32.4% |
| >=3000 | 5,965 | 21.3 | 13.1 | 23.1 | 16.4 | 14.2 | 7.0 | 4.8 | 7.96 | 26.1% | 11.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 844 | 0.5483 | 0.4096 | 0.4988 | +0.050 | -0.089 | -0.003 ± 0.0053 |
| ratio 4-10x | 579 | 0.5876 | 0.4416 | 0.4957 | +0.092 | -0.054 | 0.0128 ± 0.0067 |
| ratio <2x | 2083 | 0.538 | 0.4144 | 0.4455 | +0.092 | -0.031 | 0.0128 ± 0.0032 |
| ratio >=10x | 774 | 0.5697 | 0.3946 | 0.4664 | +0.103 | -0.072 | 0.0054 ± 0.0065 |
| thinner_sample 1000-3000 | 1153 | 0.5423 | 0.4149 | 0.4449 | +0.097 | -0.030 | 0.0113 ± 0.0042 |
| thinner_sample 300-1000 | 984 | 0.5664 | 0.4229 | 0.4919 | +0.074 | -0.069 | 0.0013 ± 0.0052 |
| thinner_sample <300 | 1447 | 0.5595 | 0.3932 | 0.4665 | +0.093 | -0.073 | 0.0083 ± 0.0047 |
| thinner_sample >=3000 | 696 | 0.5351 | 0.4405 | 0.467 | +0.068 | -0.026 | 0.0135 ± 0.0044 |
| data_status ADEQUATE | 1218 | 0.5383 | 0.4329 | 0.4507 | +0.088 | -0.018 | 0.013 ± 0.0036 |
| data_status LIMITED | 991 | 0.5501 | 0.4165 | 0.4793 | +0.071 | -0.063 | 0.0046 ± 0.0048 |
| data_status POOR | 2071 | 0.5619 | 0.4007 | 0.4698 | +0.092 | -0.069 | 0.0074 ± 0.0038 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 623 | 0.2008 | 0.2019 | -0.0011 ± 0.0006 | 0.5823 | 0.5846 | 0.5033 | 0.4884 | 0.5329 | -0.060 ± 0.0189 | -0.01 (5) |
| 3-5 | 396 | 0.2028 | 0.2024 | +0.0005 ± 0.0018 | 0.5888 | 0.5861 | 0.5021 | 0.462 | 0.4747 | -0.097 ± 0.0233 | 0.02 (1) |
| 5-10 | 885 | 0.2017 | 0.2015 | +0.0003 ± 0.0023 | 0.5898 | 0.5859 | 0.511 | 0.4369 | 0.4678 | -0.089 ± 0.0156 | -0.0167 (6) |
| 10-15 | 735 | 0.2141 | 0.2036 | +0.0105 ± 0.0042 | 0.619 | 0.5887 | 0.5287 | 0.4046 | 0.4231 | -0.107 ± 0.0166 | -0.048 (5) |
| 15-25 | 975 | 0.2246 | 0.2132 | +0.0114 ± 0.0058 | 0.6439 | 0.6102 | 0.5775 | 0.3817 | 0.4503 | -0.092 ± 0.0147 | -0.0033 (9) |
| 25-40 | 554 | 0.2237 | 0.209 | +0.0148 ± 0.0116 | 0.6356 | 0.601 | 0.6562 | 0.3467 | 0.4747 | -0.075 ± 0.0179 | -0.01 (1) |
| 40+ | 112 | 0.2783 | 0.1982 | +0.0800 ± 0.0365 | 0.7629 | 0.5814 | 0.7564 | 0.3087 | 0.4464 | -0.077 ± 0.0358 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3220 | 0.184 | 0.1851 | -0.0010 ± 0.0003 | 0.5434 | 0.5446 | 0.4928 | 0.4777 | 0.5146 | -0.018 ± 0.0077 | -0.0129 (17) |
| 3-5 | 2113 | 0.1977 | 0.1966 | +0.0011 ± 0.0008 | 0.5757 | 0.57 | 0.485 | 0.4451 | 0.4501 | -0.052 ± 0.0098 | 0.0 (2) |
| 5-10 | 4609 | 0.198 | 0.1949 | +0.0031 ± 0.001 | 0.5801 | 0.5694 | 0.4806 | 0.4067 | 0.4227 | -0.046 ± 0.0066 | -0.0119 (21) |
| 10-15 | 3932 | 0.1974 | 0.1788 | +0.0185 ± 0.0017 | 0.5804 | 0.5282 | 0.4855 | 0.3611 | 0.3484 | -0.075 ± 0.0067 | -0.0281 (16) |
| 15-25 | 4959 | 0.2081 | 0.1691 | +0.0390 ± 0.0023 | 0.6093 | 0.5008 | 0.5051 | 0.3087 | 0.3085 | -0.074 ± 0.0058 | -0.0025 (44) |
| 25-40 | 3871 | 0.223 | 0.1299 | +0.0931 ± 0.0036 | 0.6401 | 0.3969 | 0.531 | 0.2179 | 0.2291 | -0.059 ± 0.0056 | -0.01 (1) |
| 40+ | 2527 | 0.3801 | 0.046 | +0.3340 ± 0.0048 | 0.99 | 0.1764 | 0.6331 | 0.1076 | 0.0653 | -0.078 ± 0.004 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 488 | 0.2064 | 0.207 | -0.0006 ± 0.0007 | 0.5949 | 0.596 | 0.5052 | 0.4901 | 0.5102 | -0.107 ± 0.0221 | -0.01 (3) |
| 3-5 | 353 | 0.2234 | 0.2213 | +0.0021 ± 0.002 | 0.633 | 0.6286 | 0.5135 | 0.4736 | 0.4618 | -0.120 ± 0.0267 | 0.02 (1) |
| 5-10 | 762 | 0.2052 | 0.2048 | +0.0004 ± 0.0025 | 0.5967 | 0.5945 | 0.5469 | 0.4721 | 0.5092 | -0.081 ± 0.0169 | -0.01 (4) |
| 10-15 | 709 | 0.2172 | 0.2087 | +0.0085 ± 0.0043 | 0.6241 | 0.6029 | 0.5657 | 0.4415 | 0.4711 | -0.113 ± 0.0178 | -0.04 (5) |
| 15-25 | 996 | 0.2301 | 0.2103 | +0.0198 ± 0.0057 | 0.6533 | 0.6033 | 0.5878 | 0.392 | 0.4438 | -0.101 ± 0.0148 | -0.0133 (9) |
| 25-40 | 705 | 0.2622 | 0.198 | +0.0642 ± 0.0106 | 0.7317 | 0.5766 | 0.6532 | 0.3376 | 0.3957 | -0.112 ± 0.0164 | -0.0075 (4) |
| 40+ | 267 | 0.3591 | 0.1721 | +0.1870 ± 0.0251 | 0.9875 | 0.5146 | 0.7316 | 0.2471 | 0.3109 | -0.071 ± 0.0244 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2736 | 0.194 | 0.1942 | -0.0002 ± 0.0003 | 0.5648 | 0.5652 | 0.5094 | 0.4945 | 0.5091 | -0.044 ± 0.0087 | -0.0133 (15) |
| 3-5 | 1815 | 0.1986 | 0.1982 | +0.0004 ± 0.0008 | 0.5753 | 0.5738 | 0.5142 | 0.4743 | 0.4887 | -0.040 ± 0.0107 | 0.02 (1) |
| 5-10 | 4060 | 0.1953 | 0.1937 | +0.0016 ± 0.001 | 0.5756 | 0.5666 | 0.5083 | 0.4342 | 0.4631 | -0.032 ± 0.007 | -0.0117 (6) |
| 10-15 | 3568 | 0.2011 | 0.1885 | +0.0126 ± 0.0018 | 0.589 | 0.5495 | 0.5125 | 0.3885 | 0.4005 | -0.057 ± 0.0074 | -0.0189 (18) |
| 15-25 | 4904 | 0.2161 | 0.1778 | +0.0383 ± 0.0024 | 0.6278 | 0.5231 | 0.5252 | 0.3293 | 0.3332 | -0.070 ± 0.0061 | -0.0086 (42) |
| 25-40 | 4549 | 0.2521 | 0.1377 | +0.1144 ± 0.0035 | 0.709 | 0.4224 | 0.5583 | 0.2415 | 0.222 | -0.085 ± 0.0055 | -0.0044 (18) |
| 40+ | 3599 | 0.394 | 0.0608 | +0.3331 ± 0.0047 | 1.0373 | 0.2173 | 0.6509 | 0.1191 | 0.0847 | -0.072 ± 0.004 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 597 | 0.2001 | 0.2022 | -0.0021 ± 0.0007 | 0.581 | 0.5863 | 0.5004 | 0.4851 | 0.5494 | -0.027 ± 0.0189 | -0.0137 (8) |
| 3-5 | 426 | 0.2003 | 0.1985 | +0.0018 ± 0.0017 | 0.5825 | 0.5768 | 0.506 | 0.4663 | 0.4648 | -0.118 ± 0.0223 | 0.0067 (3) |
| 5-10 | 901 | 0.2009 | 0.1977 | +0.0032 ± 0.0022 | 0.5882 | 0.5766 | 0.5075 | 0.4334 | 0.4462 | -0.101 ± 0.0152 | -0.0071 (7) |
| 10-15 | 746 | 0.209 | 0.2057 | +0.0034 ± 0.0041 | 0.6073 | 0.5937 | 0.5389 | 0.4153 | 0.4651 | -0.084 ± 0.0165 | -0.0317 (6) |
| 15-25 | 918 | 0.2312 | 0.212 | +0.0192 ± 0.0059 | 0.6602 | 0.6071 | 0.5879 | 0.3935 | 0.4401 | -0.113 ± 0.0152 | -0.03 (1) |
| 25-40 | 574 | 0.2138 | 0.2174 | -0.0036 ± 0.0114 | 0.6158 | 0.6205 | 0.6679 | 0.3567 | 0.5157 | -0.053 ± 0.0176 | 0.015 (2) |
| 40+ | 118 | 0.2919 | 0.209 | +0.0829 ± 0.0368 | 0.8038 | 0.6052 | 0.7657 | 0.3158 | 0.4576 | -0.070 ± 0.0381 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3152 | 0.1852 | 0.1857 | -0.0005 ± 0.0003 | 0.545 | 0.5458 | 0.4912 | 0.476 | 0.4902 | -0.038 ± 0.0077 | -0.0163 (35) |
| 3-5 | 2130 | 0.1944 | 0.1921 | +0.0023 ± 0.0008 | 0.571 | 0.5636 | 0.4879 | 0.4482 | 0.4399 | -0.068 ± 0.0097 | -0.0094 (18) |
| 5-10 | 4660 | 0.1959 | 0.1903 | +0.0056 ± 0.001 | 0.5759 | 0.5571 | 0.4826 | 0.4086 | 0.4075 | -0.061 ± 0.0064 | -0.01 (31) |
| 10-15 | 3836 | 0.191 | 0.1749 | +0.0161 ± 0.0017 | 0.5654 | 0.5178 | 0.498 | 0.3745 | 0.3707 | -0.068 ± 0.0067 | -0.015 (12) |
| 15-25 | 5122 | 0.2104 | 0.1715 | +0.0390 ± 0.0023 | 0.6147 | 0.5064 | 0.5137 | 0.3187 | 0.3163 | -0.074 ± 0.0058 | -0.03 (2) |
| 25-40 | 3880 | 0.2192 | 0.1333 | +0.0859 ± 0.0037 | 0.6325 | 0.4042 | 0.537 | 0.2206 | 0.2448 | -0.049 ± 0.0056 | 0.01 (3) |
| 40+ | 2451 | 0.3946 | 0.0506 | +0.3440 ± 0.0051 | 1.031 | 0.1884 | 0.6453 | 0.114 | 0.0698 | -0.081 ± 0.0043 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 981 | 0.1953 | 0.1955 | -0.0002 ± 0.0005 | 0.5701 | 0.5701 | 0.5045 | 0.4893 | 0.4964 | -0.056 ± 0.0143 | -0.0224 (49) |
| 3-5 | 686 | 0.1918 | 0.1911 | +0.0006 ± 0.0013 | 0.5607 | 0.5579 | 0.4893 | 0.4494 | 0.4592 | -0.056 ± 0.0171 | -0.0194 (34) |
| 5-10 | 1422 | 0.2009 | 0.1948 | +0.0060 ± 0.0018 | 0.5908 | 0.5719 | 0.4963 | 0.4229 | 0.4198 | -0.072 ± 0.0119 | -0.005 (78) |
| 10-15 | 946 | 0.21 | 0.1983 | +0.0117 ± 0.0036 | 0.6096 | 0.5786 | 0.5205 | 0.3973 | 0.4091 | -0.068 ± 0.0147 | 0.0014 (64) |
| 15-25 | 1272 | 0.2311 | 0.21 | +0.0212 ± 0.005 | 0.66 | 0.6046 | 0.5761 | 0.3812 | 0.4253 | -0.071 ± 0.0129 | -0.0214 (59) |
| 25-40 | 775 | 0.2481 | 0.2069 | +0.0413 ± 0.01 | 0.7047 | 0.595 | 0.6716 | 0.3593 | 0.449 | -0.086 ± 0.0153 | -0.0219 (26) |
| 40+ | 258 | 0.354 | 0.1967 | +0.1573 ± 0.0273 | 1.0218 | 0.5751 | 0.808 | 0.3255 | 0.4225 | -0.096 ± 0.0249 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3197 | 0.1829 | 0.1831 | -0.0002 ± 0.0003 | 0.5387 | 0.5383 | 0.5052 | 0.4899 | 0.5023 | -0.036 ± 0.0076 | -0.0157 (88) |
| 3-5 | 2219 | 0.1924 | 0.1907 | +0.0017 ± 0.0007 | 0.5624 | 0.5582 | 0.4948 | 0.4551 | 0.4529 | -0.052 ± 0.0094 | -0.0209 (69) |
| 5-10 | 4426 | 0.1972 | 0.1887 | +0.0085 ± 0.001 | 0.5801 | 0.5552 | 0.4916 | 0.4181 | 0.4001 | -0.072 ± 0.0066 | -0.0082 (132) |
| 10-15 | 3088 | 0.2053 | 0.1892 | +0.0160 ± 0.0019 | 0.599 | 0.5568 | 0.5271 | 0.404 | 0.3996 | -0.066 ± 0.0078 | -0.0053 (105) |
| 15-25 | 3867 | 0.2296 | 0.1995 | +0.0300 ± 0.0028 | 0.662 | 0.5783 | 0.5685 | 0.373 | 0.3946 | -0.065 ± 0.0072 | -0.0253 (107) |
| 25-40 | 2674 | 0.2595 | 0.1842 | +0.0753 ± 0.0052 | 0.7352 | 0.5374 | 0.6315 | 0.3176 | 0.3571 | -0.078 ± 0.0081 | -0.0229 (51) |
| 40+ | 1189 | 0.3774 | 0.1448 | +0.2326 ± 0.0116 | 1.0701 | 0.4357 | 0.7292 | 0.2257 | 0.259 | -0.070 ± 0.0104 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4280 | 1.036 ± 0.043 | 1.132 | 0.1689 | 0.1648 | 0.2139 | 0.2055 |
| gen2 | 4280 | 0.839 ± 0.04 | 1.092 | 0.1689 | 0.1654 | 0.2336 | 0.2052 |
| gen1_elo | 4280 | 1.012 ± 0.041 | 1.122 | 0.1758 | 0.1648 | 0.2129 | 0.2058 |
| gen1_sr | 4280 | 1.027 ± 0.052 | 1.168 | 0.1297 | 0.1674 | 0.2296 | 0.2048 |
| gen1_ledger | 6340 | 0.861 ± 0.03 | 1.075 | 0.1837 | 0.1793 | 0.2185 | 0.1996 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 21,201)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,898 | 23.1% |
| STALE_QUOTE | market_freshness | 4,605 | 21.7% |
| BOOK_QUALITY | execution | 3,940 | 18.6% |
| POOR_DATA | data | 2,412 | 11.4% |
| LIMITED_DATA | data | 1,315 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,151 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 997 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 897 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 639 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 346 | 1.6% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 23.1%, market_freshness 21.7%, execution 18.6%, data 17.6%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.7%, mapping 4.2%, model_calibration 1.6%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 94.3%, LOW_DATA_QUALITY 71.1%, THIN_PLAYER_HISTORY 60.0%, STALE_PLAYER_DATA 49.6%, STALE_KALSHI_QUOTE 44.4%, MODEL_INTERNAL_DISAGREEMENT 42.6%, ASYMMETRIC_SAMPLE_SIZE 33.6%, WIDE_SPREAD 24.7%, MODEL_HIGH_UNCERTAINTY 17.9%, PLAYER_IDENTITY_RISK 16.3%, LEVEL_TRANSFER_RISK 11.1%, LOW_DISPLAYED_LIQUIDITY 8.1%, EVENT_MAPPING_RISK 7.9%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.1%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.7%, POST_SETTLEMENT_OBSERVATION 23.1%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 11,387)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,943 | 34.6% |
| STALE_QUOTE | market_freshness | 2,130 | 18.7% |
| BOOK_QUALITY | execution | 2,048 | 18.0% |
| POOR_DATA | data | 1,002 | 8.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 616 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 511 | 4.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 407 | 3.6% |
| LIMITED_DATA | data | 403 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 248 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 78 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.6%, market_freshness 18.7%, execution 18.0%, data 12.3%, market_freshness/coverage 9.0%, mapping 4.5%, model_calibration_or_unknown 2.2%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 74.5%, THIN_PLAYER_HISTORY 62.3%, STALE_KALSHI_QUOTE 52.4%, STALE_PLAYER_DATA 44.4%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 34.8%, WIDE_SPREAD 23.8%, PLAYER_IDENTITY_RISK 19.6%, MODEL_HIGH_UNCERTAINTY 18.2%, LEVEL_TRANSFER_RISK 9.8%, EVENT_MAPPING_RISK 9.5%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.8%, POST_SETTLEMENT_OBSERVATION 34.6%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 8872, "IDENTITY_AMBIGUOUS": 2515}; ticker orientation: {"VERIFIED": 11387}.

Checks: discipline:AMBIGUOUS 750, discipline:PASS 10637, identity_confidence:AMBIGUOUS 2235, identity_confidence:PASS 9152, level_mapping:NA 762, level_mapping:PASS 10625, market_pair:AMBIGUOUS 395, market_pair:NA 287, market_pair:PASS 10705, model_complement:NA 254, model_complement:PASS 11133, namesake:PASS 11387, physical_match_id:NA 3983, physical_match_id:PASS 7404, player_ids:PASS 11387, same_pair_other_event:PASS 11387, ticker_orientation:PASS 11387

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,997 | 4.7% | 4.2% | 1.7% | {"market_freshness": 53, "model_calibration_or_unknown": 43, "data": 35, "execution": 21, "market_freshness/coverage": 13, "model_calibration": 13, "coverage": 11} | 5.86 | 0.2175 / 0.2114 (467) | 18.7% | 3.8% | 3.1% | 2.9% |
| CHALLENGER | 7,768 | 17.5% | 7.1% | 11.9% | {"coverage": 766, "market_freshness/coverage": 165, "market_freshness": 148, "data": 141, "model_calibration_or_unknown": 61, "execution": 31, "model_calibration": 28, "mapping": 15, "possible_market_error": 1} | 7.44 | 0.2204 / 0.2085 (1866) | 35.0% | 17.8% | 3.8% | 22.8% |
| DOUBLES | 1,591 | 47.1% | 46.7% | 6.6% | {"execution": 385, "mapping": 198, "market_freshness": 106, "market_freshness/coverage": 54, "coverage": 7} | 23.62 | 0.3097 / 0.2354 (421) | 14.7% | 0.0% | 100.0% | 7.2% |
| ITF_MEN | 14,278 | 25.4% | 17.7% | 31.9% | {"coverage": 1344, "execution": 691, "market_freshness": 621, "data": 481, "market_freshness/coverage": 312, "mapping": 175, "model_calibration_or_unknown": 2, "model_calibration": 2} | 11.91 | 0.2151 / 0.1973 (3217) | 37.6% | 69.8% | 19.8% | 22.2% |
| ITF_WOMEN | 18,869 | 27.2% | 19.8% | 45.1% | {"coverage": 1793, "market_freshness": 1114, "execution": 882, "data": 714, "market_freshness/coverage": 430, "mapping": 117, "model_calibration_or_unknown": 69, "model_calibration": 11} | 12.84 | 0.2031 / 0.1942 (3668) | 39.8% | 56.0% | 9.9% | 22.2% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,837 | 5.2% | 4.7% | 1.3% | {"market_freshness": 48, "model_calibration_or_unknown": 32, "execution": 24, "model_calibration": 13, "data": 11, "market_freshness/coverage": 10, "coverage": 9, "mapping": 1} | 7.7 | 0.2385 / 0.2306 (451) | 24.5% | 1.3% | 1.5% | 3.5% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.5% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 311 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 15.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 928 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 15 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 16 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 17 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 18 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 19 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 20 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 21 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 22 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 23 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 24 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 25 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 26 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 27 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 28 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 29 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 30 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 31 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 32 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 33 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 34 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 35 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 36 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 37 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 38 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 39 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 9.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 553 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 40 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 41 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 42 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 43 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 44 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 45 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 468 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 46 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 47 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 48 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 765 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 49 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 50 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9705, "by_level_share_of_ge_25pp": {"ATP": 0.0166, "CHALLENGER": 0.1191, "DOUBLES": 0.0659, "ITF_MEN": 0.3186, "ITF_WOMEN": 0.4505, "OTHER": 0.0011, "WTA": 0.013, "WTA125": 0.0153}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5238, "share_primary_cause_market_settled_or_in_play": 0.4361, "share_primary_cause_stale_quote_only": 0.1871}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 11387, "identity_ambiguous_share": 0.2209, "ticker_orientation": {"VERIFIED": 11387}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 7404, "with_external": 367, "coverage": 0.0496, "external_status": {"EXTERNAL_STALE": 222, "AGREES_WITH_KALSHI": 136, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 222, "MODEL_LONE_OUTLIER": 136, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3706, "share_external_supports_model": 0.0245}, "pregame_clean_ge_25pp": {"n": 3605, "with_external": 344, "coverage": 0.0954, "external_status": {"EXTERNAL_STALE": 206, "AGREES_WITH_KALSHI": 129, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 206, "MODEL_LONE_OUTLIER": 129, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.375, "share_external_supports_model": 0.0262}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 490.0, "median_sample_ratio": 2.44, "median_min_matches": 21.0, "median_max_days_since_last": 225.0, "share_severe_asymmetry": 0.2147, "data_status": {"POOR": 6363, "LIMITED": 2985, "ADEQUATE": 2039}, "comparison_lt_10pp": {"median_thinner_serve_points": 1669.5, "median_sample_ratio": 1.71, "median_min_matches": 93.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 844, "model_minus_observed": 0.0495, "kalshi_minus_observed": -0.0892, "brier_diff_model_minus_kalshi": -0.003}, "4-10x": {"n": 579, "model_minus_observed": 0.0919, "kalshi_minus_observed": -0.0541, "brier_diff_model_minus_kalshi": 0.0128}, "<2x": {"n": 2083, "model_minus_observed": 0.0925, "kalshi_minus_observed": -0.0311, "brier_diff_model_minus_kalshi": 0.0128}, ">=10x": {"n": 774, "model_minus_observed": 0.1033, "kalshi_minus_observed": -0.0718, "brier_diff_model_minus_kalshi": 0.0054}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4280, "model": {"intercept": -0.545, "slope": 0.839, "slope_se": 0.04}, "kalshi_mid_same_rows": {"intercept": 0.211, "slope": 1.092, "slope_se": 0.044}, "mean_extremity_model": 0.1689, "mean_extremity_kalshi": 0.1654, "model_brier": 0.2336, "kalshi_brier": 0.2052, "brier_diff_model_minus_kalshi": 0.0285, "brier_diff_se": 0.0029, "model_logloss": 0.6638, "kalshi_logloss": 0.593}, "fair_v1": {"n": 4280, "model": {"intercept": -0.412, "slope": 1.036, "slope_se": 0.043}, "kalshi_mid_same_rows": {"intercept": 0.304, "slope": 1.132, "slope_se": 0.045}, "mean_extremity_model": 0.1689, "mean_extremity_kalshi": 0.1648, "model_brier": 0.2139, "kalshi_brier": 0.2055, "brier_diff_model_minus_kalshi": 0.0084, "brier_diff_se": 0.0024, "model_logloss": 0.6164, "kalshi_logloss": 0.5936}, "gen1_elo": {"n": 4280, "model": {"intercept": -0.397, "slope": 1.012, "slope_se": 0.041}, "kalshi_mid_same_rows": {"intercept": 0.313, "slope": 1.122, "slope_se": 0.044}, "mean_extremity_model": 0.1758, "mean_extremity_kalshi": 0.1648, "model_brier": 0.2129, "kalshi_brier": 0.2058, "brier_diff_model_minus_kalshi": 0.0071, "brier_diff_se": 0.0024, "model_logloss": 0.6151, "kalshi_logloss": 0.5942}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2502, "share_ge_15": 0.4475, "median_abs_gap": 13.23, "n": 29590}, "gen1_elo": {"share_ge_25": 0.2474, "share_ge_15": 0.4467, "median_abs_gap": 13.05, "n": 29590}, "gen1_sr": {"share_ge_25": 0.3185, "share_ge_15": 0.5274, "median_abs_gap": 16.09, "n": 29590}, "gen2": {"share_ge_25": 0.3213, "share_ge_15": 0.516, "median_abs_gap": 15.67, "n": 29590}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1573, "share_ge_15": 0.3635, "median_abs_gap": 10.98, "n": 22922}, "gen1_elo": {"share_ge_25": 0.1583, "share_ge_15": 0.3612, "median_abs_gap": 10.81, "n": 22919}, "gen1_sr": {"share_ge_25": 0.2245, "share_ge_15": 0.4493, "median_abs_gap": 13.23, "n": 22923}, "gen2": {"share_ge_25": 0.2401, "share_ge_15": 0.4478, "median_abs_gap": 13.14, "n": 22924}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.86, "share_ge_25_all": 0.0473, "share_ge_25_pregame_clean": 0.0425}, "WTA": {"median_abs_gap_pregame_clean": 7.7, "share_ge_25_all": 0.0522, "share_ge_25_pregame_clean": 0.0471}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2333, "share_within_10pp_all": 0.4303, "share_within_10pp_pregame_clean": 0.4835, "corr_model_vs_mid_pregame_clean": 0.8436}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 623, "model_brier": 0.2008, "kalshi_brier": 0.2019, "brier_diff_model_minus_kalshi": -0.0011}, "10-15": {"n_settled": 735, "model_brier": 0.2141, "kalshi_brier": 0.2036, "brier_diff_model_minus_kalshi": 0.0105}, "15-25": {"n_settled": 975, "model_brier": 0.2246, "kalshi_brier": 0.2132, "brier_diff_model_minus_kalshi": 0.0114}, "25-40": {"n_settled": 554, "model_brier": 0.2237, "kalshi_brier": 0.209, "brier_diff_model_minus_kalshi": 0.0148}, "3-5": {"n_settled": 396, "model_brier": 0.2028, "kalshi_brier": 0.2024, "brier_diff_model_minus_kalshi": 0.0005}, "40+": {"n_settled": 112, "model_brier": 0.2783, "kalshi_brier": 0.1982, "brier_diff_model_minus_kalshi": 0.08}, "5-10": {"n_settled": 885, "model_brier": 0.2017, "kalshi_brier": 0.2015, "brier_diff_model_minus_kalshi": 0.0003}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.545, "slope": 0.839, "slope_se": 0.04}, "kalshi_slope": {"intercept": 0.211, "slope": 1.092, "slope_se": 0.044}, "n": 4280}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.507, "slope": 0.861, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.158, "slope": 1.075, "slope_se": 0.035}, "n": 6340}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 421, "model_brier": 0.3097, "kalshi_brier": 0.2354, "brier_diff_model_minus_kalshi": 0.0742, "brier_diff_se": 0.0149, "corr_model_outcome": 0.0449, "corr_kalshi_outcome": 0.2582}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
