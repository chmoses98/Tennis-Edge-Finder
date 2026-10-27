# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-27T18:09Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 60,456): 0-3 14.0%, 3-5 9.5%, 5-10 19.9%, 10-15 15.4%, 15-25 19.1%, 25-40 14.0%, 40+ 8.0%; median gap 11.97 pp.
* **Where the extremes live**: 96.8% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.6%, Challenger 11.7%, doubles 6.6%). Main tour: ATP 4.4% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 13,278): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.2%, STALE_QUOTE 19.1%, BOOK_QUALITY 19.0%, POOR_DATA 9.0%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 3.5%, IN_PLAY_QUOTE 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.2%, market_freshness 19.1%, execution 19.0%, data 12.5%, market_freshness/coverage 8.9%, mapping 4.3%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 51.4% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.1% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 13,278 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.7% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.1%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.9% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 459.0 points vs 1761.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.024, Gen-2 0.814, Gen-1 ledger 0.858 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 634 model 0.2235 vs Kalshi 0.2089; n 133 model 0.2706 vs Kalshi 0.202.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 263,949 model-market comparisons (427,453 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 88,233 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-27T17:51:42.319014+00:00'], shadow board 69,430 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-27T17:51:47.669044+00:00'], Model 4 34,125 rows, 21,857 settled tickers, 7,845 tickers with an external scan.
* By model: {"gen1_ledger": 60065, "gen1_elo": 34909, "fair_v1": 34909, "gen2": 34909, "gen1_sr": 34909, "model4_fundamental": 32146, "model4_conditioned": 32102}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 60,456 | 14.0 | 9.5 | 19.9 | 15.4 | 19.1 | 14.0 | 8.0 | 11.97 | 41.1% | 22.0% |
| MW fair_v1 | 34,909 | 12.9 | 8.7 | 18.5 | 15.6 | 19.7 | 14.9 | 9.7 | 13.06 | 44.2% | 24.6% |
| MW gen1_elo | 34,909 | 12.8 | 8.5 | 19.3 | 15.4 | 19.7 | 14.8 | 9.5 | 12.86 | 44.0% | 24.3% |
| MW gen1_ledger | 25,547 | 15.5 | 10.7 | 21.8 | 15.2 | 18.4 | 12.7 | 5.7 | 10.49 | 36.8% | 18.4% |
| MW gen1_sr | 34,909 | 10.2 | 7.2 | 16.9 | 13.6 | 20.8 | 18.6 | 12.7 | 15.92 | 52.1% | 31.4% |
| MW gen2 | 34,909 | 11.1 | 7.5 | 16.3 | 13.9 | 19.5 | 17.9 | 13.8 | 15.52 | 51.3% | 31.8% |
| all families model4_conditioned | 32,102 | 22.1 | 18.3 | 34.5 | 17.4 | 4.9 | 1.8 | 1.1 | 6.04 | 7.8% | 2.9% |
| all families model4_fundamental | 32,146 | 17.0 | 13.2 | 34.1 | 20.4 | 10.2 | 3.7 | 1.4 | 7.75 | 15.3% | 5.1% |

Configurable thresholds (primary): >=5pp 76.4%, >=10pp 56.5%, >=15pp 41.1%, >=20pp 30.5%, >=25pp 22.0%, >=30pp 15.8%, >=40pp 8.0%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.35pp; >=10pp 45.0%, >=25pp 17.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,198 | 27.1 | 15.5 | 26.9 | 14.0 | 11.5 | 4.2 | 0.6 | 5.93 | 16.4% | 4.9% |
| CHALLENGER | 5,527 | 15.9 | 9.9 | 20.2 | 15.8 | 15.5 | 12.1 | 10.6 | 11.06 | 38.1% | 22.7% |
| ITF_MEN | 9,333 | 9.9 | 7.2 | 16.5 | 14.9 | 21.6 | 17.7 | 12.2 | 15.52 | 51.5% | 29.9% |
| ITF_WOMEN | 13,601 | 9.6 | 6.9 | 15.9 | 15.3 | 22.3 | 18.3 | 11.7 | 15.69 | 52.4% | 30.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,280 | 17.0 | 13.9 | 25.0 | 20.4 | 16.6 | 6.5 | 0.6 | 8.39 | 23.7% | 7.1% |
| WTA125 | 964 | 14.9 | 7.2 | 23.2 | 19.9 | 20.8 | 12.2 | 1.8 | 11.03 | 34.8% | 14.0% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,198 | 25.4 | 15.4 | 25.3 | 16.9 | 11.9 | 4.3 | 0.8 | 6.33 | 17.0% | 5.1% |
| CHALLENGER | 5,527 | 15.1 | 8.8 | 18.0 | 14.7 | 18.1 | 13.9 | 11.5 | 12.73 | 43.5% | 25.4% |
| ITF_MEN | 9,333 | 8.0 | 6.0 | 14.2 | 12.9 | 20.0 | 21.2 | 17.8 | 18.82 | 59.0% | 39.0% |
| ITF_WOMEN | 13,601 | 8.0 | 5.6 | 13.9 | 12.9 | 20.7 | 21.4 | 17.6 | 19.3 | 59.6% | 39.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,280 | 14.4 | 10.7 | 22.3 | 15.8 | 22.4 | 12.8 | 1.4 | 10.78 | 36.7% | 14.3% |
| WTA125 | 964 | 8.3 | 6.1 | 16.9 | 17.2 | 24.5 | 18.1 | 8.8 | 15.68 | 51.4% | 27.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,198 | 22.7 | 12.5 | 24.7 | 16.1 | 16.1 | 6.5 | 1.4 | 7.58 | 24.0% | 7.9% |
| CHALLENGER | 5,527 | 14.6 | 9.2 | 21.3 | 16.0 | 15.8 | 12.3 | 10.9 | 11.34 | 39.0% | 23.2% |
| ITF_MEN | 9,333 | 9.6 | 7.1 | 16.6 | 14.1 | 22.1 | 18.0 | 12.4 | 15.99 | 52.6% | 30.4% |
| ITF_WOMEN | 13,601 | 9.3 | 6.7 | 16.4 | 15.9 | 22.5 | 18.1 | 11.0 | 15.52 | 51.6% | 29.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,280 | 23.7 | 16.4 | 31.6 | 15.1 | 9.7 | 2.5 | 1.1 | 6.08 | 13.2% | 3.6% |
| WTA125 | 964 | 22.4 | 12.0 | 27.0 | 16.5 | 15.3 | 6.3 | 0.4 | 7.99 | 22.1% | 6.7% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,868 | 24.6 | 19.1 | 30.7 | 12.8 | 9.1 | 3.2 | 0.5 | 5.74 | 12.8% | 3.7% |
| CHALLENGER | 3,801 | 21.9 | 14.4 | 27.0 | 14.9 | 14.1 | 6.2 | 1.6 | 7.27 | 21.9% | 7.8% |
| DOUBLES | 1,856 | 5.2 | 4.5 | 12.1 | 10.4 | 20.5 | 25.3 | 21.9 | 23.86 | 67.8% | 47.2% |
| ITF_MEN | 7,038 | 12.9 | 9.0 | 20.2 | 16.0 | 21.7 | 13.8 | 6.4 | 12.27 | 41.9% | 20.2% |
| ITF_WOMEN | 8,509 | 12.9 | 8.8 | 19.5 | 15.4 | 21.3 | 16.2 | 5.8 | 12.63 | 43.4% | 22.1% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,346 | 23.7 | 15.6 | 30.1 | 17.8 | 9.6 | 3.0 | 0.3 | 6.79 | 12.8% | 3.3% |
| WTA125 | 980 | 23.4 | 13.2 | 21.0 | 18.7 | 14.0 | 8.0 | 1.8 | 8.16 | 23.8% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,114 | 27.4 | 15.7 | 27.4 | 13.9 | 11.3 | 3.9 | 0.4 | 5.92 | 15.6% | 4.3% |
| CHALLENGER | 3,915 | 20.7 | 12.4 | 25.1 | 18.2 | 15.5 | 6.5 | 1.6 | 8.32 | 23.6% | 8.1% |
| ITF_MEN | 6,895 | 12.0 | 8.6 | 19.7 | 16.9 | 22.8 | 14.5 | 5.5 | 12.84 | 42.8% | 20.0% |
| ITF_WOMEN | 10,261 | 11.3 | 8.2 | 18.1 | 17.3 | 24.2 | 15.4 | 5.4 | 13.54 | 45.0% | 20.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,213 | 17.2 | 13.8 | 25.1 | 20.6 | 16.6 | 6.1 | 0.6 | 8.34 | 23.3% | 6.7% |
| WTA125 | 932 | 15.2 | 7.0 | 23.0 | 20.2 | 21.2 | 11.9 | 1.5 | 11.03 | 34.7% | 13.4% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,114 | 25.6 | 15.7 | 25.5 | 16.9 | 11.8 | 4.0 | 0.5 | 6.23 | 16.3% | 4.5% |
| CHALLENGER | 3,915 | 19.3 | 11.1 | 22.4 | 17.2 | 18.5 | 9.6 | 2.0 | 9.21 | 30.0% | 11.6% |
| ITF_MEN | 6,896 | 9.4 | 7.1 | 16.5 | 14.9 | 21.9 | 19.3 | 10.9 | 15.66 | 52.1% | 30.2% |
| ITF_WOMEN | 10,262 | 9.0 | 6.4 | 15.4 | 14.3 | 22.7 | 20.9 | 11.2 | 16.89 | 54.8% | 32.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,213 | 14.5 | 10.7 | 22.4 | 15.9 | 22.5 | 12.7 | 1.3 | 10.77 | 36.5% | 14.0% |
| WTA125 | 932 | 8.3 | 6.1 | 17.1 | 17.5 | 24.5 | 18.4 | 8.2 | 15.44 | 51.1% | 26.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,815 | 24.7 | 19.3 | 30.7 | 12.9 | 8.8 | 3.0 | 0.4 | 5.67 | 12.2% | 3.5% |
| CHALLENGER | 3,352 | 23.3 | 15.3 | 28.2 | 15.0 | 13.5 | 4.3 | 0.5 | 6.72 | 18.2% | 4.7% |
| DOUBLES | 1,736 | 5.1 | 4.5 | 12.4 | 10.6 | 20.4 | 25.2 | 21.7 | 23.82 | 67.3% | 46.9% |
| ITF_MEN | 5,959 | 13.9 | 9.6 | 21.8 | 16.8 | 21.7 | 12.2 | 4.0 | 11.43 | 37.9% | 16.3% |
| ITF_WOMEN | 7,183 | 13.6 | 9.3 | 20.8 | 16.1 | 21.4 | 15.2 | 3.6 | 11.75 | 40.2% | 18.8% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,292 | 24.1 | 16.0 | 30.1 | 17.8 | 9.6 | 2.3 | 0.1 | 6.68 | 12.0% | 2.4% |
| WTA125 | 862 | 25.1 | 14.0 | 22.2 | 19.8 | 12.8 | 5.6 | 0.6 | 7.36 | 18.9% | 6.2% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,856 | 5.2 | 4.5 | 12.1 | 10.4 | 20.5 | 25.3 | 21.9 | 23.86 | 67.8% | 47.2% |
| singles | 23,691 | 16.3 | 11.2 | 22.6 | 15.6 | 18.3 | 11.7 | 4.4 | 9.98 | 34.4% | 16.1% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,451 | 12.8 | 9.2 | 20.0 | 15.8 | 19.0 | 13.9 | 9.3 | 12.52 | 42.1% | 23.2% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 22,297 | 13.4 | 8.8 | 18.4 | 15.3 | 19.6 | 15.0 | 9.5 | 13.01 | 44.1% | 24.5% |
| UNKNOWN | 4,912 | 10.8 | 7.3 | 17.1 | 16.9 | 20.9 | 16.0 | 11.1 | 14.12 | 48.0% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 10,055 | 19.7 | 12.4 | 22.1 | 16.1 | 14.7 | 9.1 | 5.8 | 8.73 | 29.7% | 15.0% |
| B | 4,296 | 12.6 | 8.6 | 19.1 | 16.5 | 19.5 | 12.9 | 10.8 | 12.75 | 43.2% | 23.6% |
| C | 4,814 | 11.8 | 8.8 | 19.5 | 16.0 | 19.3 | 14.4 | 10.0 | 13.0 | 43.8% | 24.5% |
| D | 5,323 | 12.2 | 8.1 | 17.5 | 15.4 | 21.4 | 15.7 | 9.6 | 13.83 | 46.8% | 25.4% |
| F | 10,421 | 7.3 | 5.5 | 14.9 | 14.6 | 23.7 | 21.2 | 12.8 | 17.89 | 57.6% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,190 | 23.8 | 15.9 | 28.8 | 15.1 | 11.2 | 3.9 | 1.4 | 6.54 | 16.4% | 5.2% |
| B | 3,474 | 16.6 | 10.1 | 24.1 | 16.2 | 19.4 | 10.2 | 3.4 | 9.82 | 33.0% | 13.6% |
| C | 4,883 | 11.0 | 7.3 | 19.1 | 14.5 | 21.2 | 16.1 | 10.7 | 14.09 | 48.1% | 26.9% |
| D | 3,563 | 14.2 | 9.8 | 20.7 | 15.6 | 20.6 | 13.4 | 5.7 | 11.6 | 39.7% | 19.1% |
| F | 6,437 | 9.8 | 8.1 | 15.5 | 15.1 | 22.7 | 20.9 | 7.9 | 15.81 | 51.5% | 28.8% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 11,405 | 18.0 | 11.2 | 21.3 | 15.9 | 15.2 | 10.0 | 8.4 | 9.9 | 33.7% | 18.4% |
| LIMITED | 7,409 | 13.7 | 9.9 | 20.0 | 16.5 | 19.5 | 13.2 | 7.2 | 11.91 | 39.9% | 20.4% |
| POOR | 16,095 | 9.0 | 6.4 | 15.9 | 15.0 | 22.9 | 19.2 | 11.7 | 16.24 | 53.7% | 30.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,058 | 24.4 | 18.5 | 33.3 | 14.6 | 6.3 | 2.6 | 0.3 | 5.75 | 9.2% | 2.9% |
| GAME_SPREAD | 5,567 | 22.3 | 15.4 | 33.2 | 16.8 | 9.1 | 2.8 | 0.5 | 6.71 | 12.4% | 3.3% |
| MATCH_WINNER | 25,547 | 15.5 | 10.7 | 21.8 | 15.2 | 18.4 | 12.7 | 5.7 | 10.49 | 36.8% | 18.4% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 12,734 | 27.7 | 16.5 | 31.1 | 12.6 | 9.3 | 2.5 | 0.3 | 5.68 | 12.1% | 2.8% |
| TOTAL_GAMES | 9,135 | 9.2 | 10.2 | 36.2 | 27.1 | 10.5 | 4.0 | 2.8 | 9.35 | 17.4% | 6.8% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,439 | 24.5 | 30.7 | 32.9 | 6.9 | 4.0 | 0.8 | 0.2 | 4.67 | 4.9% | 1.0% |
| GAME_SPREAD | 7,522 | 46.8 | 16.4 | 25.7 | 7.4 | 1.9 | 1.2 | 0.6 | 3.31 | 3.6% | 1.7% |
| TOTAL_GAMES | 13,141 | 5.8 | 8.5 | 40.9 | 32.2 | 7.3 | 3.1 | 2.2 | 9.44 | 12.7% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,450 | 23.8 | 16.9 | 35.0 | 14.3 | 7.2 | 2.5 | 0.3 | 6.03 | 10.1% | 2.9% |
| GAME_SPREAD | 7,525 | 19.8 | 13.4 | 28.4 | 20.7 | 12.3 | 4.4 | 1.1 | 7.84 | 17.8% | 5.5% |
| TOTAL_GAMES | 13,171 | 9.4 | 9.9 | 36.5 | 25.7 | 11.7 | 4.3 | 2.4 | 9.28 | 18.4% | 6.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 34,909 | 44.2% | 24.6% | 13.06 | 35.9% | 15.5% | 10.87 |
| gen1_elo | 34,909 | 44.0% | 24.3% | 12.86 | 35.6% | 15.5% | 10.67 |
| gen1_sr | 34,909 | 52.1% | 31.4% | 15.92 | 44.5% | 22.3% | 13.03 |
| gen2 | 34,909 | 51.3% | 31.8% | 15.52 | 44.6% | 23.9% | 13.06 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 17,268 | 15.5 | 10.5 | 21.3 | 17.3 | 20.1 | 11.9 | 3.3 | 10.72 | 35.3% | 15.2% |
| STALE | 17,641 | 10.4 | 6.9 | 15.8 | 13.9 | 19.2 | 17.9 | 15.9 | 16.34 | 53.0% | 33.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 19,015 | 16.4 | 11.1 | 22.5 | 15.3 | 17.7 | 12.2 | 4.8 | 10.02 | 34.7% | 17.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 60,456 | 19015 | 20740 | 20701 | 24.1 | 118.4 | 1400.4 |
| ge_15pp | 24,850 | 6606 | 7389 | 10855 | 26.3 | 418.5 | 1399.2 |
| ge_25pp | 13,278 | 3233 | 3217 | 6828 | 31.3 | 565.6 | 1380.4 |
| lt_10pp | 26,282 | 9493 | 9806 | 6983 | 22.4 | 47.3 | 1341.5 |

Current slate `SL-20261027T180939Z-93a8f15f`: 697 priced rows, quote age at build {'median': 18.5, 'max': 18.6}, freshness {'AGING': 697}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 38 | 0.0 | 0.0 | 31.6 | 7.9 | 39.5 | 21.1 | 0.0 | 20.05 | 60.5% | 21.1% |
| EXTERNAL_LONE_OUTLIER | 18 | 77.8 | 22.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,451 | 19.8 | 11.1 | 24.9 | 18.5 | 17.9 | 7.1 | 0.7 | 8.77 | 25.7% | 7.8% |
| KALSHI_LONE_OUTLIER | 22 | 4.5 | 4.5 | 77.3 | 4.5 | 4.5 | 4.5 | 0.0 | 6.16 | 9.1% | 4.5% |
| MARKETS_AGREE | 674 | 65.1 | 34.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.21 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,465 | 0.0 | 2.5 | 35.1 | 26.8 | 24.7 | 10.2 | 0.7 | 12.12 | 35.6% | 10.8% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 34,909 | 5668 (16.2%) | 25.9% | 1.0% | {"EXTERNAL_STALE": 3451, "AGREES_WITH_KALSHI": 1465, "ALL_AGREE": 674, "SUPPORTS_MODEL_DIRECTION": 37, "AGREES_WITH_MODEL": 22, "EXTERNAL_OUTLIER": 18, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 15,445 | 1433 (9.3%) | 36.4% | 1.7% | {"EXTERNAL_STALE": 887, "AGREES_WITH_KALSHI": 521, "SUPPORTS_MODEL_DIRECTION": 23, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 8,583 | 437 (5.1%) | 36.4% | 2.1% | {"EXTERNAL_STALE": 269, "AGREES_WITH_KALSHI": 159, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,238 | 413 (9.8%) | 36.8% | 2.2% | {"EXTERNAL_STALE": 252, "AGREES_WITH_KALSHI": 152, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 14,020 | 3201 (22.8%) | 17.2% | 0.9% | {"EXTERNAL_STALE": 1927, "ALL_AGREE": 674, "AGREES_WITH_KALSHI": 551, "AGREES_WITH_MODEL": 19, "EXTERNAL_OUTLIER": 18, "SUPPORTS_MODEL_DIRECTION": 11, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 6,720 | 10.4 | 7.5 | 19.3 | 14.8 | 22.1 | 16.2 | 9.8 | 14.09 | 48.0% | 25.9% |
| 4-10x | 4,564 | 11.0 | 8.5 | 18.6 | 15.3 | 22.0 | 14.7 | 9.8 | 13.76 | 46.5% | 24.5% |
| <2x | 17,849 | 15.1 | 10.1 | 19.3 | 16.4 | 17.4 | 13.1 | 8.7 | 11.63 | 39.1% | 21.7% |
| >=10x | 5,776 | 10.5 | 6.1 | 15.2 | 14.2 | 22.0 | 19.4 | 12.5 | 16.49 | 53.9% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 8,835 | 12.8 | 8.5 | 19.2 | 16.3 | 19.2 | 13.5 | 10.4 | 12.84 | 43.1% | 23.9% |
| 300-1000 | 7,302 | 11.9 | 8.8 | 17.4 | 15.3 | 20.6 | 16.4 | 9.6 | 13.79 | 46.7% | 26.1% |
| <300 | 11,386 | 8.3 | 5.7 | 15.4 | 14.8 | 23.2 | 20.1 | 12.5 | 17.05 | 55.8% | 32.6% |
| >=3000 | 7,386 | 21.2 | 13.6 | 23.8 | 16.1 | 13.7 | 7.1 | 4.5 | 7.67 | 25.4% | 11.6% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 984 | 0.5499 | 0.4123 | 0.503 | +0.047 | -0.091 | -0.0038 ± 0.0049 |
| ratio 4-10x | 667 | 0.5846 | 0.4372 | 0.4933 | +0.091 | -0.056 | 0.0096 ± 0.0062 |
| ratio <2x | 2415 | 0.538 | 0.4149 | 0.448 | +0.090 | -0.033 | 0.011 ± 0.0029 |
| ratio >=10x | 879 | 0.5696 | 0.3932 | 0.4539 | +0.116 | -0.061 | 0.0116 ± 0.0062 |
| thinner_sample 1000-3000 | 1337 | 0.5386 | 0.4122 | 0.4503 | +0.088 | -0.038 | 0.0084 ± 0.0039 |
| thinner_sample 300-1000 | 1093 | 0.5682 | 0.4254 | 0.4922 | +0.076 | -0.067 | 0.0011 ± 0.0049 |
| thinner_sample <300 | 1682 | 0.5606 | 0.3929 | 0.462 | +0.099 | -0.069 | 0.0096 ± 0.0043 |
| thinner_sample >=3000 | 833 | 0.5366 | 0.4418 | 0.4658 | +0.071 | -0.024 | 0.013 ± 0.004 |
| data_status ADEQUATE | 1412 | 0.5372 | 0.4335 | 0.4511 | +0.086 | -0.018 | 0.0123 ± 0.0033 |
| data_status LIMITED | 1147 | 0.5487 | 0.4151 | 0.4847 | +0.064 | -0.070 | 0.0024 ± 0.0044 |
| data_status POOR | 2386 | 0.563 | 0.401 | 0.4661 | +0.097 | -0.065 | 0.0081 ± 0.0036 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 724 | 0.2008 | 0.2014 | -0.0005 ± 0.0006 | 0.582 | 0.5831 | 0.501 | 0.4861 | 0.5124 | -0.084 ± 0.0177 | -0.01 (5) |
| 3-5 | 447 | 0.2047 | 0.2046 | +0.0000 ± 0.0017 | 0.5925 | 0.5911 | 0.5054 | 0.4654 | 0.4832 | -0.099 ± 0.022 | 0.02 (1) |
| 5-10 | 1021 | 0.2041 | 0.2044 | -0.0003 ± 0.0021 | 0.5949 | 0.5932 | 0.5139 | 0.4401 | 0.475 | -0.090 ± 0.0146 | -0.0167 (6) |
| 10-15 | 872 | 0.22 | 0.2108 | +0.0093 ± 0.0039 | 0.6324 | 0.6047 | 0.5296 | 0.4057 | 0.4289 | -0.108 ± 0.0156 | -0.048 (5) |
| 15-25 | 1114 | 0.2242 | 0.212 | +0.0122 ± 0.0054 | 0.6439 | 0.6075 | 0.5759 | 0.3802 | 0.447 | -0.096 ± 0.0138 | -0.0033 (9) |
| 25-40 | 634 | 0.2235 | 0.2089 | +0.0146 ± 0.0108 | 0.6368 | 0.6006 | 0.6546 | 0.3449 | 0.4748 | -0.073 ± 0.0167 | -0.01 (1) |
| 40+ | 133 | 0.2706 | 0.202 | +0.0686 ± 0.0335 | 0.7413 | 0.5884 | 0.7469 | 0.2975 | 0.4511 | -0.054 ± 0.0332 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3772 | 0.1851 | 0.1859 | -0.0008 ± 0.0002 | 0.5461 | 0.5468 | 0.4877 | 0.4726 | 0.5 | -0.028 ± 0.0071 | -0.0129 (17) |
| 3-5 | 2523 | 0.1984 | 0.1968 | +0.0016 ± 0.0007 | 0.5774 | 0.5713 | 0.4838 | 0.4439 | 0.4423 | -0.058 ± 0.009 | 0.0 (2) |
| 5-10 | 5359 | 0.2003 | 0.1966 | +0.0037 ± 0.0009 | 0.5859 | 0.5731 | 0.4854 | 0.4115 | 0.4228 | -0.050 ± 0.0061 | -0.0119 (21) |
| 10-15 | 4597 | 0.2016 | 0.1841 | +0.0175 ± 0.0016 | 0.5898 | 0.5404 | 0.4897 | 0.3654 | 0.3565 | -0.073 ± 0.0063 | -0.0281 (16) |
| 15-25 | 5734 | 0.2074 | 0.1686 | +0.0388 ± 0.0021 | 0.6081 | 0.499 | 0.5021 | 0.3059 | 0.3061 | -0.072 ± 0.0054 | -0.0025 (44) |
| 25-40 | 4481 | 0.2227 | 0.1269 | +0.0959 ± 0.0033 | 0.6396 | 0.3891 | 0.5289 | 0.2153 | 0.2234 | -0.061 ± 0.0052 | -0.01 (1) |
| 40+ | 2902 | 0.3777 | 0.0479 | +0.3298 ± 0.0046 | 0.9835 | 0.1818 | 0.6307 | 0.1057 | 0.0672 | -0.074 ± 0.0038 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 569 | 0.2058 | 0.2065 | -0.0007 ± 0.0007 | 0.5931 | 0.5948 | 0.5097 | 0.4945 | 0.5149 | -0.110 ± 0.0206 | -0.01 (3) |
| 3-5 | 402 | 0.2269 | 0.2237 | +0.0033 ± 0.0019 | 0.6406 | 0.634 | 0.5116 | 0.4719 | 0.4453 | -0.140 ± 0.0252 | 0.02 (1) |
| 5-10 | 886 | 0.2084 | 0.208 | +0.0003 ± 0.0023 | 0.6031 | 0.6021 | 0.5482 | 0.4734 | 0.5113 | -0.086 ± 0.0159 | -0.01 (4) |
| 10-15 | 807 | 0.2201 | 0.2127 | +0.0074 ± 0.0041 | 0.6317 | 0.6116 | 0.5679 | 0.4436 | 0.4783 | -0.109 ± 0.017 | -0.04 (5) |
| 15-25 | 1160 | 0.2301 | 0.2133 | +0.0168 ± 0.0053 | 0.6545 | 0.6096 | 0.5853 | 0.3901 | 0.4483 | -0.098 ± 0.0138 | -0.0133 (9) |
| 25-40 | 815 | 0.2655 | 0.1977 | +0.0678 ± 0.0098 | 0.7418 | 0.5763 | 0.6522 | 0.338 | 0.3902 | -0.121 ± 0.0154 | -0.0075 (4) |
| 40+ | 306 | 0.3588 | 0.1714 | +0.1875 ± 0.0234 | 0.9838 | 0.5118 | 0.7348 | 0.2487 | 0.3137 | -0.072 ± 0.0227 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3207 | 0.1937 | 0.1939 | -0.0002 ± 0.0003 | 0.5648 | 0.5648 | 0.5124 | 0.4974 | 0.5067 | -0.049 ± 0.0081 | -0.0133 (15) |
| 3-5 | 2152 | 0.1986 | 0.1972 | +0.0014 ± 0.0008 | 0.5755 | 0.5715 | 0.5136 | 0.4738 | 0.4749 | -0.053 ± 0.0098 | 0.02 (1) |
| 5-10 | 4758 | 0.1982 | 0.1955 | +0.0027 ± 0.001 | 0.5823 | 0.5709 | 0.5137 | 0.4397 | 0.4617 | -0.038 ± 0.0065 | -0.0117 (6) |
| 10-15 | 4110 | 0.205 | 0.1924 | +0.0126 ± 0.0017 | 0.5995 | 0.5589 | 0.5168 | 0.3929 | 0.4046 | -0.057 ± 0.0069 | -0.0189 (18) |
| 15-25 | 5726 | 0.2157 | 0.1794 | +0.0363 ± 0.0022 | 0.6274 | 0.5261 | 0.5246 | 0.3293 | 0.3381 | -0.064 ± 0.0056 | -0.0086 (42) |
| 25-40 | 5249 | 0.2514 | 0.137 | +0.1144 ± 0.0032 | 0.7076 | 0.4203 | 0.5573 | 0.2406 | 0.221 | -0.086 ± 0.0051 | -0.0044 (18) |
| 40+ | 4166 | 0.3945 | 0.0616 | +0.3329 ± 0.0044 | 1.0374 | 0.2193 | 0.6518 | 0.1193 | 0.0864 | -0.070 ± 0.0038 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 706 | 0.1977 | 0.1997 | -0.0020 ± 0.0006 | 0.5747 | 0.5797 | 0.5016 | 0.4863 | 0.5467 | -0.037 ± 0.0176 | -0.0137 (8) |
| 3-5 | 486 | 0.203 | 0.2016 | +0.0014 ± 0.0017 | 0.5891 | 0.584 | 0.5043 | 0.4646 | 0.4691 | -0.117 ± 0.0212 | 0.0067 (3) |
| 5-10 | 1044 | 0.2047 | 0.2024 | +0.0023 ± 0.0021 | 0.5961 | 0.5877 | 0.5116 | 0.4374 | 0.4579 | -0.098 ± 0.0143 | -0.0071 (7) |
| 10-15 | 864 | 0.2108 | 0.206 | +0.0048 ± 0.0038 | 0.6113 | 0.5947 | 0.5395 | 0.4161 | 0.4595 | -0.096 ± 0.0155 | -0.0317 (6) |
| 15-25 | 1052 | 0.232 | 0.2162 | +0.0158 ± 0.0056 | 0.6623 | 0.6169 | 0.5869 | 0.3924 | 0.4487 | -0.106 ± 0.0143 | -0.03 (1) |
| 25-40 | 651 | 0.2149 | 0.2158 | -0.0009 ± 0.0107 | 0.6193 | 0.6165 | 0.6644 | 0.3539 | 0.5084 | -0.057 ± 0.0165 | 0.015 (2) |
| 40+ | 142 | 0.2873 | 0.2079 | +0.0794 ± 0.0333 | 0.7902 | 0.6008 | 0.7562 | 0.3052 | 0.4507 | -0.060 ± 0.035 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3727 | 0.185 | 0.1856 | -0.0006 ± 0.0002 | 0.5448 | 0.5456 | 0.4863 | 0.4712 | 0.4889 | -0.035 ± 0.0071 | -0.0163 (35) |
| 3-5 | 2475 | 0.1983 | 0.1965 | +0.0018 ± 0.0007 | 0.5796 | 0.5732 | 0.4847 | 0.4451 | 0.4424 | -0.062 ± 0.0091 | -0.0094 (18) |
| 5-10 | 5497 | 0.1956 | 0.191 | +0.0046 ± 0.0009 | 0.5749 | 0.5587 | 0.4883 | 0.4141 | 0.4204 | -0.053 ± 0.0059 | -0.01 (31) |
| 10-15 | 4462 | 0.1936 | 0.1781 | +0.0155 ± 0.0016 | 0.5713 | 0.5256 | 0.4991 | 0.3758 | 0.3743 | -0.067 ± 0.0063 | -0.015 (12) |
| 15-25 | 5885 | 0.2127 | 0.1733 | +0.0394 ± 0.0021 | 0.6196 | 0.5102 | 0.5131 | 0.3181 | 0.3155 | -0.074 ± 0.0054 | -0.03 (2) |
| 25-40 | 4458 | 0.2192 | 0.13 | +0.0892 ± 0.0034 | 0.6325 | 0.3957 | 0.5329 | 0.2169 | 0.2358 | -0.052 ± 0.0052 | 0.01 (3) |
| 40+ | 2864 | 0.3909 | 0.0528 | +0.3381 ± 0.0048 | 1.0211 | 0.1947 | 0.6424 | 0.1133 | 0.0723 | -0.077 ± 0.0041 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1092 | 0.1959 | 0.196 | -0.0001 ± 0.0005 | 0.5708 | 0.5706 | 0.5025 | 0.4875 | 0.4918 | -0.066 ± 0.0136 | -0.0224 (49) |
| 3-5 | 752 | 0.1919 | 0.1914 | +0.0006 ± 0.0013 | 0.5607 | 0.5585 | 0.4948 | 0.455 | 0.4654 | -0.062 ± 0.0163 | -0.0194 (34) |
| 5-10 | 1573 | 0.2025 | 0.1967 | +0.0058 ± 0.0017 | 0.5951 | 0.5759 | 0.4968 | 0.4233 | 0.4215 | -0.077 ± 0.0114 | -0.005 (78) |
| 10-15 | 1065 | 0.2144 | 0.2025 | +0.0120 ± 0.0034 | 0.6206 | 0.588 | 0.5285 | 0.4057 | 0.4169 | -0.077 ± 0.0141 | 0.0014 (64) |
| 15-25 | 1400 | 0.2317 | 0.2108 | +0.0209 ± 0.0048 | 0.6607 | 0.6064 | 0.5799 | 0.385 | 0.4307 | -0.078 ± 0.0123 | -0.0214 (59) |
| 25-40 | 867 | 0.2435 | 0.2097 | +0.0339 ± 0.0095 | 0.6955 | 0.6013 | 0.6778 | 0.3658 | 0.4671 | -0.086 ± 0.0145 | -0.0219 (26) |
| 40+ | 283 | 0.3432 | 0.1994 | +0.1438 ± 0.026 | 0.9915 | 0.5839 | 0.8067 | 0.3263 | 0.4346 | -0.094 ± 0.024 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3737 | 0.1807 | 0.1809 | -0.0002 ± 0.0002 | 0.5327 | 0.5324 | 0.5055 | 0.4903 | 0.4993 | -0.041 ± 0.007 | -0.0157 (88) |
| 3-5 | 2570 | 0.1948 | 0.1928 | +0.0020 ± 0.0007 | 0.567 | 0.5627 | 0.5034 | 0.4636 | 0.4584 | -0.056 ± 0.0088 | -0.0209 (69) |
| 5-10 | 5167 | 0.1983 | 0.1903 | +0.0079 ± 0.0009 | 0.5841 | 0.5591 | 0.4936 | 0.42 | 0.4051 | -0.071 ± 0.0061 | -0.0082 (132) |
| 10-15 | 3611 | 0.2109 | 0.1955 | +0.0154 ± 0.0018 | 0.6129 | 0.5715 | 0.5293 | 0.4065 | 0.4046 | -0.066 ± 0.0074 | -0.0053 (105) |
| 15-25 | 4430 | 0.2307 | 0.2004 | +0.0303 ± 0.0027 | 0.6642 | 0.5798 | 0.5681 | 0.3724 | 0.3937 | -0.067 ± 0.0068 | -0.0253 (107) |
| 25-40 | 3044 | 0.2592 | 0.1852 | +0.0740 ± 0.0049 | 0.7349 | 0.5407 | 0.6333 | 0.3201 | 0.361 | -0.078 ± 0.0076 | -0.0229 (51) |
| 40+ | 1313 | 0.3746 | 0.1476 | +0.2270 ± 0.0111 | 1.0604 | 0.4447 | 0.7291 | 0.2279 | 0.265 | -0.071 ± 0.01 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4945 | 1.024 ± 0.04 | 1.092 | 0.1676 | 0.1642 | 0.2153 | 0.2073 |
| gen2 | 4945 | 0.814 ± 0.037 | 1.053 | 0.1688 | 0.1647 | 0.2353 | 0.2071 |
| gen1_elo | 4945 | 1.0 ± 0.039 | 1.091 | 0.174 | 0.1644 | 0.2141 | 0.2074 |
| gen1_sr | 4945 | 0.991 ± 0.048 | 1.116 | 0.1294 | 0.1666 | 0.2313 | 0.2068 |
| gen1_ledger | 7032 | 0.858 ± 0.028 | 1.058 | 0.1841 | 0.1768 | 0.2187 | 0.2014 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 24,850)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 5,479 | 22.1% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,468 | 22.0% |
| BOOK_QUALITY | execution | 4,795 | 19.3% |
| POOR_DATA | data | 2,859 | 11.5% |
| LIMITED_DATA | data | 1,540 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,351 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,161 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 1,044 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 712 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 440 | 1.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 22.1%, coverage 22.0%, execution 19.3%, data 17.7%, market_freshness/coverage 8.3%, model_calibration_or_unknown 4.7%, mapping 4.2%, model_calibration 1.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.1%, LOW_DATA_QUALITY 71.2%, THIN_PLAYER_HISTORY 60.3%, STALE_PLAYER_DATA 51.5%, STALE_KALSHI_QUOTE 43.7%, MODEL_INTERNAL_DISAGREEMENT 42.5%, ASYMMETRIC_SAMPLE_SIZE 33.5%, WIDE_SPREAD 25.4%, MODEL_HIGH_UNCERTAINTY 17.7%, PLAYER_IDENTITY_RISK 16.2%, LEVEL_TRANSFER_RISK 10.5%, LOW_DISPLAYED_LIQUIDITY 8.0%, EVENT_MAPPING_RISK 7.7%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.5%, POST_SETTLEMENT_OBSERVATION 22.0%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 13,278)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,410 | 33.2% |
| STALE_QUOTE | market_freshness | 2,529 | 19.1% |
| BOOK_QUALITY | execution | 2,517 | 19.0% |
| POOR_DATA | data | 1,200 | 9.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 727 | 5.5% |
| IDENTITY_AMBIGUOUS | mapping | 571 | 4.3% |
| LIMITED_DATA | data | 459 | 3.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 456 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 297 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 111 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.2%, market_freshness 19.1%, execution 19.0%, data 12.5%, market_freshness/coverage 8.9%, mapping 4.3%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.8%, LOW_DATA_QUALITY 74.6%, THIN_PLAYER_HISTORY 62.6%, STALE_KALSHI_QUOTE 51.4%, STALE_PLAYER_DATA 46.1%, MODEL_INTERNAL_DISAGREEMENT 42.6%, ASYMMETRIC_SAMPLE_SIZE 34.8%, WIDE_SPREAD 25.0%, PLAYER_IDENTITY_RISK 19.3%, MODEL_HIGH_UNCERTAINTY 18.1%, LEVEL_TRANSFER_RISK 9.3%, EVENT_MAPPING_RISK 9.3%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.2%, POST_SETTLEMENT_OBSERVATION 33.2%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 10401, "IDENTITY_AMBIGUOUS": 2877}; ticker orientation: {"VERIFIED": 13278}.

Checks: discipline:AMBIGUOUS 877, discipline:PASS 12401, identity_confidence:AMBIGUOUS 2566, identity_confidence:PASS 10712, level_mapping:NA 889, level_mapping:PASS 12389, market_pair:AMBIGUOUS 469, market_pair:NA 318, market_pair:PASS 12491, model_complement:NA 283, model_complement:PASS 12995, namesake:AMBIGUOUS 6, namesake:PASS 13272, physical_match_id:NA 4695, physical_match_id:PASS 8583, player_ids:PASS 13278, same_pair_other_event:PASS 13278, ticker_orientation:PASS 13278

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,066 | 4.4% | 4.0% | 1.7% | {"market_freshness": 56, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "market_freshness/coverage": 15, "coverage": 13} | 5.85 | 0.221 / 0.2171 (575) | 20.9% | 3.1% | 3.3% | 2.7% |
| CHALLENGER | 9,328 | 16.6% | 6.5% | 11.7% | {"coverage": 885, "market_freshness/coverage": 189, "market_freshness": 168, "data": 144, "model_calibration_or_unknown": 74, "execution": 36, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.44 | 0.2189 / 0.2092 (2145) | 34.7% | 16.4% | 4.1% | 22.1% |
| DOUBLES | 1,856 | 47.2% | 46.9% | 6.6% | {"execution": 490, "mapping": 219, "market_freshness": 106, "market_freshness/coverage": 55, "coverage": 7} | 23.82 | 0.3112 / 0.2362 (445) | 12.6% | 0.0% | 100.0% | 6.5% |
| ITF_MEN | 16,371 | 25.7% | 18.3% | 31.7% | {"coverage": 1482, "execution": 811, "market_freshness": 757, "data": 591, "market_freshness/coverage": 379, "mapping": 181, "model_calibration": 6, "model_calibration_or_unknown": 2} | 12.09 | 0.217 / 0.199 (3503) | 37.0% | 70.4% | 18.7% | 21.5% |
| ITF_WOMEN | 22,110 | 27.0% | 20.0% | 45.0% | {"coverage": 1994, "market_freshness": 1311, "execution": 1103, "data": 835, "market_freshness/coverage": 492, "mapping": 148, "model_calibration_or_unknown": 74, "model_calibration": 12} | 12.84 | 0.2051 / 0.1979 (4124) | 39.1% | 58.0% | 10.3% | 21.1% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,626 | 5.7% | 5.1% | 1.6% | {"market_freshness": 73, "model_calibration_or_unknown": 43, "execution": 27, "data": 19, "model_calibration": 16, "coverage": 16, "market_freshness/coverage": 11, "mapping": 1} | 7.65 | 0.2336 / 0.2276 (575) | 25.4% | 1.2% | 1.5% | 3.3% |
| WTA125 | 1,944 | 11.9% | 9.9% | 1.7% | {"market_freshness": 56, "model_calibration_or_unknown": 49, "market_freshness/coverage": 41, "data": 34, "execution": 21, "model_calibration": 14, "coverage": 12, "mapping": 4} | 9.38 | 0.2134 / 0.1977 (568) | 25.1% | 11.8% | 5.5% | 7.7% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
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
| 14 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 15 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 16 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 17 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 18 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 19 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | LIMITED_DATA | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 20 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 21 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 22 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 23 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 24 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 25 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 271 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 26 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 27 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 28 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 29 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 30 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 31 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 32 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 33 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 34 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 35 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 36 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 37 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 77 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 38 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 39 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 41 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 42 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 43 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 44 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 45 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 46 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 47 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 48 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 468 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 49 | `KXITFMATCH-26OCT27GHESAD-GHE` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 130 min (STALE); data POOR (grade F, thinner serve sample 276.0, ratio 6.69); no external reference |
| 50 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9675, "by_level_share_of_ge_25pp": {"ATP": 0.0169, "CHALLENGER": 0.1167, "DOUBLES": 0.066, "ITF_MEN": 0.317, "ITF_WOMEN": 0.4495, "OTHER": 0.0009, "WTA": 0.0155, "WTA125": 0.0174}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5142, "share_primary_cause_market_settled_or_in_play": 0.4212, "share_primary_cause_stale_quote_only": 0.1905}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 13278, "identity_ambiguous_share": 0.2167, "ticker_orientation": {"VERIFIED": 13278}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 8583, "with_external": 437, "coverage": 0.0509, "external_status": {"EXTERNAL_STALE": 269, "AGREES_WITH_KALSHI": 159, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 269, "MODEL_LONE_OUTLIER": 159, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3638, "share_external_supports_model": 0.0206}, "pregame_clean_ge_25pp": {"n": 4238, "with_external": 413, "coverage": 0.0975, "external_status": {"EXTERNAL_STALE": 252, "AGREES_WITH_KALSHI": 152, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 252, "MODEL_LONE_OUTLIER": 152, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.368, "share_external_supports_model": 0.0218}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 459.0, "median_sample_ratio": 2.47, "median_min_matches": 19.0, "median_max_days_since_last": 238.0, "share_severe_asymmetry": 0.2145, "data_status": {"POOR": 7522, "LIMITED": 3369, "ADEQUATE": 2387}, "comparison_lt_10pp": {"median_thinner_serve_points": 1761.0, "median_sample_ratio": 1.67, "median_min_matches": 95.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 984, "model_minus_observed": 0.0469, "kalshi_minus_observed": -0.0908, "brier_diff_model_minus_kalshi": -0.0038}, "4-10x": {"n": 667, "model_minus_observed": 0.0913, "kalshi_minus_observed": -0.0561, "brier_diff_model_minus_kalshi": 0.0096}, "<2x": {"n": 2415, "model_minus_observed": 0.09, "kalshi_minus_observed": -0.0331, "brier_diff_model_minus_kalshi": 0.011}, ">=10x": {"n": 879, "model_minus_observed": 0.1157, "kalshi_minus_observed": -0.0607, "brier_diff_model_minus_kalshi": 0.0116}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4945, "model": {"intercept": -0.538, "slope": 0.814, "slope_se": 0.037}, "kalshi_mid_same_rows": {"intercept": 0.191, "slope": 1.053, "slope_se": 0.041}, "mean_extremity_model": 0.1688, "mean_extremity_kalshi": 0.1647, "model_brier": 0.2353, "kalshi_brier": 0.2071, "brier_diff_model_minus_kalshi": 0.0282, "brier_diff_se": 0.0027, "model_logloss": 0.6682, "kalshi_logloss": 0.5973}, "fair_v1": {"n": 4945, "model": {"intercept": -0.414, "slope": 1.024, "slope_se": 0.04}, "kalshi_mid_same_rows": {"intercept": 0.281, "slope": 1.092, "slope_se": 0.041}, "mean_extremity_model": 0.1676, "mean_extremity_kalshi": 0.1642, "model_brier": 0.2153, "kalshi_brier": 0.2073, "brier_diff_model_minus_kalshi": 0.008, "brier_diff_se": 0.0022, "model_logloss": 0.6198, "kalshi_logloss": 0.5976}, "gen1_elo": {"n": 4945, "model": {"intercept": -0.388, "slope": 1.0, "slope_se": 0.039}, "kalshi_mid_same_rows": {"intercept": 0.303, "slope": 1.091, "slope_se": 0.041}, "mean_extremity_model": 0.174, "mean_extremity_kalshi": 0.1644, "model_brier": 0.2141, "kalshi_brier": 0.2074, "brier_diff_model_minus_kalshi": 0.0067, "brier_diff_se": 0.0022, "model_logloss": 0.6177, "kalshi_logloss": 0.5978}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2459, "share_ge_15": 0.4424, "median_abs_gap": 13.06, "n": 34909}, "gen1_elo": {"share_ge_25": 0.243, "share_ge_15": 0.4402, "median_abs_gap": 12.86, "n": 34909}, "gen1_sr": {"share_ge_25": 0.3138, "share_ge_15": 0.5213, "median_abs_gap": 15.92, "n": 34909}, "gen2": {"share_ge_25": 0.3178, "share_ge_15": 0.5126, "median_abs_gap": 15.52, "n": 34909}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.155, "share_ge_15": 0.3594, "median_abs_gap": 10.87, "n": 27336}, "gen1_elo": {"share_ge_25": 0.1548, "share_ge_15": 0.356, "median_abs_gap": 10.67, "n": 27334}, "gen1_sr": {"share_ge_25": 0.2226, "share_ge_15": 0.4452, "median_abs_gap": 13.03, "n": 27337}, "gen2": {"share_ge_25": 0.239, "share_ge_15": 0.4458, "median_abs_gap": 13.06, "n": 27338}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.85, "share_ge_25_all": 0.0444, "share_ge_25_pregame_clean": 0.04}, "WTA": {"median_abs_gap_pregame_clean": 7.65, "share_ge_25_all": 0.0568, "share_ge_25_pregame_clean": 0.0511}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2356, "share_within_10pp_all": 0.4347, "share_within_10pp_pregame_clean": 0.4855, "corr_model_vs_mid_pregame_clean": 0.8448}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 724, "model_brier": 0.2008, "kalshi_brier": 0.2014, "brier_diff_model_minus_kalshi": -0.0005}, "10-15": {"n_settled": 872, "model_brier": 0.22, "kalshi_brier": 0.2108, "brier_diff_model_minus_kalshi": 0.0093}, "15-25": {"n_settled": 1114, "model_brier": 0.2242, "kalshi_brier": 0.212, "brier_diff_model_minus_kalshi": 0.0122}, "25-40": {"n_settled": 634, "model_brier": 0.2235, "kalshi_brier": 0.2089, "brier_diff_model_minus_kalshi": 0.0146}, "3-5": {"n_settled": 447, "model_brier": 0.2047, "kalshi_brier": 0.2046, "brier_diff_model_minus_kalshi": 0.0}, "40+": {"n_settled": 133, "model_brier": 0.2706, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0686}, "5-10": {"n_settled": 1021, "model_brier": 0.2041, "kalshi_brier": 0.2044, "brier_diff_model_minus_kalshi": -0.0003}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.538, "slope": 0.814, "slope_se": 0.037}, "kalshi_slope": {"intercept": 0.191, "slope": 1.053, "slope_se": 0.041}, "n": 4945}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.495, "slope": 0.858, "slope_se": 0.028}, "kalshi_slope": {"intercept": 0.158, "slope": 1.058, "slope_se": 0.033}, "n": 7032}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 445, "model_brier": 0.3112, "kalshi_brier": 0.2362, "brier_diff_model_minus_kalshi": 0.0749, "brier_diff_se": 0.0143, "corr_model_outcome": 0.0359, "corr_kalshi_outcome": 0.2487}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
