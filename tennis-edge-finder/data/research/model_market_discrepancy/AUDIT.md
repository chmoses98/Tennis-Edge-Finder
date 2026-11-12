# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-12T08:08Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 89,873): 0-3 13.9%, 3-5 9.5%, 5-10 20.1%, 10-15 15.2%, 15-25 19.2%, 25-40 13.7%, 40+ 8.3%; median gap 11.91 pp.
* **Where the extremes live**: 97.3% of >=25 pp gaps are off the ATP/WTA main tour (ITF 78.3%, Challenger 11.1%, doubles 6.4%). Main tour: ATP 3.7% and WTA 5.9% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 19,822): MARKET_ALREADY_SETTLED_WHEN_PRICED 35.1%, STALE_QUOTE 20.2%, BOOK_QUALITY 16.4%, POOR_DATA 9.0%, POSSIBLY_IN_PLAY_QUOTE 5.9%, IDENTITY_AMBIGUOUS 4.2%, IN_PLAY_QUOTE 3.4%, LIMITED_DATA 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 1.7%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 35.1%, market_freshness 20.2%, execution 16.4%, data 12.3%, market_freshness/coverage 9.3%, mapping 4.2%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 55.6% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 44.4% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 19,822 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.9%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.9% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 476.0 points vs 1670.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.022, Gen-2 0.819, Gen-1 ledger 0.867 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 1009 model 0.225 vs Kalshi 0.2034; n 211 model 0.3067 vs Kalshi 0.1672.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA. Not implemented here.

## 1. Observations

* 374,339 model-market comparisons (618,862 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 123,278 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-12T07:54:23.373934+00:00'], shadow board 104,070 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-12T07:54:26.763575+00:00'], Model 4 44,059 rows, 30,999 settled tickers, 11,696 tickers with an external scan.
* By model: {"gen1_ledger": 82509, "gen1_elo": 52298, "fair_v1": 52298, "gen2": 52298, "gen1_sr": 52298, "model4_fundamental": 41361, "model4_conditioned": 41277}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 89,873 | 13.9 | 9.5 | 20.1 | 15.2 | 19.2 | 13.7 | 8.3 | 11.91 | 41.2% | 22.1% |
| MW fair_v1 | 52,298 | 12.6 | 8.6 | 18.7 | 15.2 | 19.6 | 15.0 | 10.3 | 13.17 | 44.9% | 25.3% |
| MW gen1_elo | 52,298 | 12.4 | 8.7 | 19.1 | 15.3 | 19.4 | 15.0 | 10.1 | 13.0 | 44.5% | 25.1% |
| MW gen1_ledger | 37,575 | 15.8 | 10.8 | 22.2 | 15.1 | 18.6 | 11.9 | 5.6 | 10.29 | 36.1% | 17.5% |
| MW gen1_sr | 52,298 | 9.9 | 7.1 | 16.6 | 13.9 | 20.9 | 18.8 | 12.8 | 15.98 | 52.5% | 31.6% |
| MW gen2 | 52,298 | 10.8 | 7.5 | 16.6 | 13.8 | 19.7 | 17.7 | 13.9 | 15.5 | 51.2% | 31.6% |
| all families model4_conditioned | 41,277 | 22.2 | 17.9 | 34.5 | 16.9 | 5.0 | 2.2 | 1.2 | 6.07 | 8.4% | 3.4% |
| all families model4_fundamental | 41,361 | 17.3 | 13.5 | 34.0 | 20.0 | 9.9 | 3.8 | 1.5 | 7.61 | 15.2% | 5.3% |

Configurable thresholds (primary): >=5pp 76.5%, >=10pp 56.4%, >=15pp 41.2%, >=20pp 30.5%, >=25pp 22.1%, >=30pp 16.0%, >=40pp 8.3%, >=50pp 3.9%
Executable gap (model outside the book, before fees): median 8.56pp; >=10pp 45.6%, >=25pp 17.5%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,112 | 28.0 | 15.9 | 28.0 | 13.3 | 10.7 | 3.5 | 0.6 | 5.79 | 14.9% | 4.2% |
| CHALLENGER | 8,244 | 16.4 | 9.6 | 20.6 | 15.2 | 15.8 | 11.4 | 11.1 | 10.93 | 38.3% | 22.5% |
| ITF_MEN | 15,264 | 9.6 | 7.3 | 17.1 | 14.8 | 21.1 | 17.2 | 12.8 | 15.48 | 51.2% | 30.1% |
| ITF_WOMEN | 20,249 | 9.4 | 7.1 | 16.1 | 14.7 | 22.1 | 18.6 | 12.0 | 16.0 | 52.8% | 30.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,096 | 16.6 | 13.3 | 25.0 | 20.7 | 16.6 | 6.7 | 1.1 | 8.61 | 24.4% | 7.8% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,112 | 26.3 | 15.7 | 26.3 | 15.7 | 11.3 | 3.9 | 0.8 | 6.09 | 16.0% | 4.7% |
| CHALLENGER | 8,244 | 14.4 | 9.1 | 19.0 | 13.9 | 18.4 | 13.7 | 11.6 | 12.54 | 43.6% | 25.2% |
| ITF_MEN | 15,264 | 8.1 | 6.1 | 15.1 | 13.9 | 20.3 | 20.0 | 16.4 | 17.86 | 56.7% | 36.4% |
| ITF_WOMEN | 20,249 | 7.8 | 5.9 | 14.1 | 12.7 | 20.7 | 21.1 | 17.6 | 19.11 | 59.5% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,096 | 14.2 | 10.4 | 21.6 | 16.2 | 22.4 | 12.7 | 2.5 | 11.2 | 37.7% | 15.2% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,112 | 23.4 | 14.1 | 25.6 | 15.5 | 14.3 | 6.0 | 1.1 | 7.04 | 21.4% | 7.1% |
| CHALLENGER | 8,244 | 15.1 | 9.6 | 20.8 | 15.6 | 16.1 | 12.0 | 10.9 | 11.29 | 39.0% | 22.9% |
| ITF_MEN | 15,264 | 9.3 | 7.3 | 17.2 | 14.2 | 21.5 | 17.4 | 13.2 | 15.82 | 52.0% | 30.6% |
| ITF_WOMEN | 20,249 | 9.2 | 6.8 | 16.3 | 15.6 | 22.1 | 18.7 | 11.3 | 15.71 | 52.1% | 30.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,096 | 22.5 | 17.2 | 31.8 | 15.2 | 8.9 | 3.3 | 1.0 | 6.12 | 13.2% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,483 | 28.1 | 19.5 | 29.1 | 12.1 | 8.1 | 2.5 | 0.4 | 5.24 | 11.1% | 3.0% |
| CHALLENGER | 4,988 | 22.8 | 14.5 | 27.9 | 14.8 | 13.1 | 5.4 | 1.5 | 7.02 | 20.0% | 6.9% |
| DOUBLES | 2,748 | 4.9 | 4.5 | 13.0 | 11.0 | 20.6 | 24.4 | 21.6 | 23.05 | 66.6% | 46.0% |
| ITF_MEN | 11,074 | 12.7 | 9.5 | 21.4 | 15.6 | 21.7 | 12.9 | 6.1 | 11.83 | 40.7% | 19.0% |
| ITF_WOMEN | 13,058 | 13.5 | 9.3 | 19.8 | 15.7 | 21.6 | 14.6 | 5.4 | 12.2 | 41.6% | 20.0% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,819 | 24.0 | 16.0 | 31.5 | 16.8 | 8.9 | 2.5 | 0.2 | 6.46 | 11.7% | 2.8% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,983 | 28.4 | 16.1 | 28.4 | 13.2 | 10.4 | 3.1 | 0.3 | 5.64 | 13.8% | 3.4% |
| CHALLENGER | 5,800 | 21.1 | 11.9 | 25.7 | 18.0 | 15.8 | 5.6 | 1.8 | 8.21 | 23.2% | 7.5% |
| ITF_MEN | 11,100 | 11.8 | 8.7 | 20.6 | 17.2 | 22.2 | 14.0 | 5.5 | 12.47 | 41.7% | 19.5% |
| ITF_WOMEN | 14,781 | 11.3 | 8.6 | 19.1 | 17.0 | 24.0 | 15.3 | 4.6 | 13.13 | 44.0% | 20.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,982 | 16.9 | 13.3 | 25.3 | 21.0 | 16.6 | 6.2 | 0.6 | 8.44 | 23.4% | 6.8% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,983 | 26.7 | 16.0 | 26.6 | 15.7 | 11.2 | 3.4 | 0.4 | 6.02 | 15.0% | 3.8% |
| CHALLENGER | 5,800 | 18.2 | 11.6 | 23.8 | 16.4 | 18.9 | 9.0 | 2.1 | 9.0 | 30.0% | 11.1% |
| ITF_MEN | 11,102 | 9.6 | 7.3 | 17.6 | 16.1 | 22.2 | 18.1 | 9.1 | 14.8 | 49.4% | 27.2% |
| ITF_WOMEN | 14,782 | 8.9 | 7.0 | 16.1 | 14.2 | 22.6 | 20.6 | 10.7 | 16.51 | 53.8% | 31.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,982 | 14.4 | 10.5 | 21.9 | 16.4 | 22.6 | 12.4 | 1.9 | 11.03 | 36.9% | 14.3% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,413 | 28.4 | 19.7 | 29.1 | 12.3 | 7.8 | 2.3 | 0.3 | 5.2 | 10.4% | 2.6% |
| CHALLENGER | 4,414 | 24.1 | 15.4 | 29.1 | 14.9 | 12.4 | 3.8 | 0.4 | 6.58 | 16.5% | 4.2% |
| DOUBLES | 2,575 | 4.7 | 4.5 | 13.2 | 11.0 | 20.5 | 24.3 | 21.7 | 23.02 | 66.5% | 46.0% |
| ITF_MEN | 9,560 | 13.5 | 10.0 | 22.9 | 16.1 | 21.8 | 11.4 | 4.2 | 11.0 | 37.5% | 15.6% |
| ITF_WOMEN | 11,242 | 14.1 | 9.9 | 20.9 | 16.2 | 21.8 | 13.5 | 3.6 | 11.42 | 38.9% | 17.1% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,756 | 24.4 | 16.4 | 31.5 | 16.8 | 8.9 | 2.0 | 0.1 | 6.42 | 10.9% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,748 | 4.9 | 4.5 | 13.0 | 11.0 | 20.6 | 24.4 | 21.6 | 23.05 | 66.6% | 46.0% |
| singles | 34,827 | 16.6 | 11.3 | 22.9 | 15.4 | 18.5 | 10.9 | 4.3 | 9.76 | 33.7% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 11,216 | 12.7 | 8.9 | 19.4 | 15.1 | 19.6 | 14.4 | 9.8 | 12.93 | 43.9% | 24.3% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 34,069 | 13.0 | 8.7 | 18.9 | 15.0 | 19.1 | 15.0 | 10.3 | 12.99 | 44.4% | 25.3% |
| UNKNOWN | 6,600 | 10.4 | 7.5 | 17.1 | 16.5 | 21.6 | 15.9 | 11.2 | 14.36 | 48.6% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 14,569 | 19.1 | 11.8 | 22.4 | 15.8 | 14.8 | 9.5 | 6.5 | 9.01 | 30.8% | 16.0% |
| B | 6,252 | 13.0 | 8.6 | 19.6 | 15.3 | 19.7 | 12.4 | 11.5 | 12.73 | 43.6% | 23.9% |
| C | 7,394 | 12.0 | 8.6 | 19.5 | 16.1 | 19.0 | 14.6 | 10.4 | 12.9 | 43.9% | 24.9% |
| D | 8,577 | 11.4 | 8.3 | 17.9 | 15.0 | 21.9 | 15.8 | 9.8 | 14.07 | 47.4% | 25.6% |
| F | 15,506 | 7.3 | 5.7 | 15.0 | 14.3 | 23.1 | 21.1 | 13.6 | 18.05 | 57.8% | 34.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,868 | 24.9 | 15.9 | 28.9 | 14.9 | 10.6 | 3.4 | 1.3 | 6.35 | 15.3% | 4.7% |
| B | 5,112 | 16.7 | 10.9 | 24.2 | 16.9 | 19.0 | 9.3 | 3.0 | 9.6 | 31.3% | 12.3% |
| C | 7,390 | 11.0 | 7.9 | 19.6 | 14.9 | 21.0 | 15.5 | 10.1 | 13.46 | 46.6% | 25.6% |
| D | 5,727 | 14.5 | 10.0 | 21.1 | 15.4 | 21.0 | 12.7 | 5.4 | 11.35 | 39.1% | 18.1% |
| F | 9,478 | 10.2 | 8.4 | 16.6 | 14.5 | 23.4 | 18.9 | 8.0 | 15.18 | 50.3% | 26.9% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 16,516 | 17.6 | 10.9 | 21.4 | 15.5 | 15.1 | 10.2 | 9.2 | 10.01 | 34.6% | 19.4% |
| LIMITED | 11,302 | 13.5 | 9.4 | 20.5 | 16.0 | 19.6 | 13.3 | 7.6 | 11.91 | 40.5% | 20.9% |
| POOR | 24,480 | 8.8 | 6.6 | 16.1 | 14.6 | 22.6 | 19.1 | 12.3 | 16.38 | 53.9% | 31.4% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,282 | 23.7 | 18.0 | 33.0 | 15.4 | 6.4 | 3.0 | 0.4 | 5.9 | 9.8% | 3.4% |
| GAME_SPREAD | 6,938 | 22.8 | 15.3 | 32.1 | 16.8 | 9.1 | 3.3 | 0.7 | 6.69 | 13.1% | 4.0% |
| MATCH_WINNER | 37,575 | 15.8 | 10.8 | 22.2 | 15.1 | 18.6 | 11.9 | 5.6 | 10.29 | 36.1% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 17,071 | 28.3 | 16.8 | 30.7 | 12.7 | 8.8 | 2.3 | 0.3 | 5.58 | 11.5% | 2.6% |
| TOTAL_GAMES | 11,619 | 9.7 | 10.8 | 36.3 | 25.7 | 10.4 | 4.2 | 2.9 | 9.14 | 17.5% | 7.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,682 | 24.5 | 28.7 | 33.3 | 8.1 | 4.0 | 1.2 | 0.3 | 4.79 | 5.4% | 1.5% |
| GAME_SPREAD | 9,548 | 46.7 | 15.8 | 25.2 | 7.4 | 2.4 | 1.9 | 0.6 | 3.33 | 4.9% | 2.5% |
| TOTAL_GAMES | 17,047 | 6.6 | 9.8 | 40.9 | 29.9 | 7.3 | 3.3 | 2.4 | 9.16 | 12.9% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,718 | 23.8 | 16.6 | 34.6 | 14.8 | 6.9 | 2.7 | 0.5 | 6.05 | 10.1% | 3.2% |
| GAME_SPREAD | 9,557 | 20.3 | 13.4 | 28.4 | 20.2 | 12.1 | 4.3 | 1.1 | 7.7 | 17.6% | 5.5% |
| TOTAL_GAMES | 17,086 | 10.0 | 10.9 | 36.5 | 24.3 | 11.3 | 4.4 | 2.6 | 9.02 | 18.3% | 7.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 52,298 | 44.9% | 25.3% | 13.17 | 35.5% | 15.2% | 10.71 |
| gen1_elo | 52,298 | 44.5% | 25.1% | 13.0 | 35.0% | 15.0% | 10.51 |
| gen1_sr | 52,298 | 52.5% | 31.6% | 15.98 | 44.0% | 21.5% | 13.0 |
| gen2 | 52,298 | 51.2% | 31.6% | 15.5 | 43.9% | 23.0% | 12.84 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,229 | 15.5 | 10.5 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 32,069 | 10.8 | 7.4 | 17.0 | 13.9 | 19.3 | 17.0 | 14.6 | 15.38 | 50.9% | 31.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 31,043 | 16.3 | 11.1 | 22.7 | 15.2 | 18.2 | 11.5 | 5.0 | 9.96 | 34.7% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 89,873 | 31043 | 23701 | 35129 | 25.2 | 142.3 | 1451.1 |
| ge_15pp | 37,056 | 10768 | 8447 | 17841 | 29.1 | 445.6 | 1451.1 |
| ge_25pp | 19,822 | 5109 | 3694 | 11019 | 34.6 | 593.3 | 1431.1 |
| lt_10pp | 39,185 | 15557 | 11206 | 12422 | 22.8 | 49.7 | 1421.7 |

Current slate `SL-20261112T080849Z-c7e0d27b`: 425 priced rows, quote age at build {'median': 14.7, 'max': 14.8}, freshness {'AGING': 425}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 52 | 0.0 | 0.0 | 34.6 | 9.6 | 32.7 | 19.2 | 3.9 | 18.34 | 55.8% | 23.1% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 5,053 | 19.1 | 11.1 | 25.7 | 18.3 | 17.7 | 7.1 | 1.0 | 8.78 | 25.8% | 8.1% |
| KALSHI_LONE_OUTLIER | 32 | 6.2 | 6.2 | 75.0 | 6.2 | 3.1 | 3.1 | 0.0 | 6.16 | 6.2% | 3.1% |
| MARKETS_AGREE | 1,077 | 66.4 | 33.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,295 | 0.0 | 2.2 | 38.5 | 25.8 | 23.8 | 8.8 | 0.9 | 11.65 | 33.5% | 9.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 52,298 | 8538 (16.3%) | 26.9% | 1.0% | {"EXTERNAL_STALE": 5053, "AGREES_WITH_KALSHI": 2295, "ALL_AGREE": 1077, "SUPPORTS_MODEL_DIRECTION": 50, "AGREES_WITH_MODEL": 32, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 23,489 | 2103 (8.9%) | 36.5% | 1.5% | {"EXTERNAL_STALE": 1304, "AGREES_WITH_KALSHI": 768, "SUPPORTS_MODEL_DIRECTION": 29, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 13,251 | 645 (4.9%) | 34.6% | 2.0% | {"EXTERNAL_STALE": 409, "AGREES_WITH_KALSHI": 223, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 6,062 | 613 (10.1%) | 35.2% | 2.1% | {"EXTERNAL_STALE": 384, "AGREES_WITH_KALSHI": 216, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 20,859 | 4911 (23.5%) | 19.0% | 0.9% | {"EXTERNAL_STALE": 2825, "ALL_AGREE": 1077, "AGREES_WITH_KALSHI": 934, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 28, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 10,255 | 10.7 | 7.5 | 19.0 | 14.3 | 21.8 | 16.5 | 10.2 | 14.38 | 48.5% | 26.7% |
| 4-10x | 7,051 | 11.0 | 8.7 | 17.9 | 14.8 | 21.7 | 14.8 | 11.2 | 14.12 | 47.6% | 26.0% |
| <2x | 26,605 | 14.5 | 9.6 | 19.9 | 16.0 | 17.5 | 13.3 | 9.1 | 11.65 | 39.9% | 22.5% |
| >=10x | 8,387 | 10.2 | 6.5 | 15.1 | 14.3 | 21.8 | 18.9 | 13.3 | 16.52 | 54.0% | 32.2% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 13,707 | 12.4 | 8.6 | 19.8 | 16.1 | 19.1 | 13.7 | 10.5 | 12.79 | 43.2% | 24.2% |
| 300-1000 | 11,360 | 11.6 | 8.6 | 17.8 | 15.1 | 20.6 | 16.4 | 9.9 | 13.88 | 46.9% | 26.2% |
| <300 | 16,620 | 8.1 | 5.9 | 15.1 | 14.4 | 22.9 | 20.1 | 13.6 | 17.47 | 56.6% | 33.7% |
| >=3000 | 10,611 | 21.0 | 12.8 | 24.0 | 15.5 | 13.9 | 7.4 | 5.4 | 7.87 | 26.7% | 12.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1614 | 0.5466 | 0.4075 | 0.4771 | +0.070 | -0.070 | 0.0036 ± 0.0038 |
| ratio 4-10x | 1095 | 0.5735 | 0.4287 | 0.4849 | +0.089 | -0.056 | 0.0099 ± 0.0048 |
| ratio <2x | 3929 | 0.5346 | 0.4121 | 0.4314 | +0.103 | -0.019 | 0.0152 ± 0.0023 |
| ratio >=10x | 1358 | 0.5611 | 0.3885 | 0.4352 | +0.126 | -0.047 | 0.0184 ± 0.0048 |
| thinner_sample 1000-3000 | 2199 | 0.5392 | 0.4123 | 0.4416 | +0.098 | -0.029 | 0.0135 ± 0.0031 |
| thinner_sample 300-1000 | 1810 | 0.5605 | 0.4206 | 0.4691 | +0.091 | -0.048 | 0.0061 ± 0.0036 |
| thinner_sample <300 | 2623 | 0.5541 | 0.3865 | 0.4438 | +0.110 | -0.057 | 0.0155 ± 0.0035 |
| thinner_sample >=3000 | 1364 | 0.5272 | 0.4339 | 0.4421 | +0.085 | -0.008 | 0.0149 ± 0.0031 |
| data_status ADEQUATE | 2178 | 0.531 | 0.4287 | 0.4366 | +0.094 | -0.008 | 0.0159 ± 0.0026 |
| data_status LIMITED | 1937 | 0.5469 | 0.4142 | 0.4621 | +0.085 | -0.048 | 0.0085 ± 0.0034 |
| data_status POOR | 3881 | 0.5558 | 0.3962 | 0.4486 | +0.107 | -0.052 | 0.013 ± 0.0027 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1154 | 0.1968 | 0.1969 | -0.0001 ± 0.0005 | 0.5733 | 0.5737 | 0.5038 | 0.4886 | 0.4965 | -0.097 ± 0.0138 | -0.0087 (8) |
| 3-5 | 741 | 0.2089 | 0.2083 | +0.0006 ± 0.0014 | 0.6039 | 0.6007 | 0.503 | 0.4632 | 0.475 | -0.101 ± 0.0172 | 0.01 (3) |
| 5-10 | 1717 | 0.203 | 0.2014 | +0.0016 ± 0.0016 | 0.5927 | 0.5864 | 0.5082 | 0.4343 | 0.4589 | -0.091 ± 0.0112 | -0.0143 (7) |
| 10-15 | 1395 | 0.2193 | 0.2093 | +0.0099 ± 0.003 | 0.6305 | 0.6021 | 0.5245 | 0.4011 | 0.4215 | -0.107 ± 0.0125 | -0.055 (6) |
| 15-25 | 1769 | 0.2254 | 0.2065 | +0.0189 ± 0.0042 | 0.6457 | 0.5962 | 0.5715 | 0.3769 | 0.4257 | -0.103 ± 0.0109 | -0.0045 (11) |
| 25-40 | 1009 | 0.225 | 0.2034 | +0.0215 ± 0.0085 | 0.6403 | 0.5873 | 0.645 | 0.3354 | 0.4549 | -0.067 ± 0.0132 | -0.06 (2) |
| 40+ | 211 | 0.3067 | 0.1672 | +0.1395 ± 0.0255 | 0.82 | 0.5029 | 0.7236 | 0.266 | 0.3507 | -0.087 ± 0.0247 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5870 | 0.1873 | 0.1882 | -0.0009 ± 0.0002 | 0.5511 | 0.5523 | 0.492 | 0.4767 | 0.5099 | -0.019 ± 0.0058 | -0.01 (28) |
| 3-5 | 3969 | 0.1996 | 0.1976 | +0.0020 ± 0.0006 | 0.5805 | 0.5737 | 0.4819 | 0.4421 | 0.4369 | -0.059 ± 0.0071 | 0.005 (6) |
| 5-10 | 8680 | 0.2013 | 0.197 | +0.0043 ± 0.0007 | 0.5885 | 0.5747 | 0.4822 | 0.4084 | 0.4167 | -0.049 ± 0.0048 | -0.0114 (22) |
| 10-15 | 7088 | 0.2017 | 0.1857 | +0.0160 ± 0.0013 | 0.59 | 0.5452 | 0.4852 | 0.3613 | 0.3589 | -0.064 ± 0.0051 | -0.0379 (19) |
| 15-25 | 9092 | 0.206 | 0.1663 | +0.0397 ± 0.0017 | 0.6037 | 0.4946 | 0.497 | 0.3014 | 0.2985 | -0.069 ± 0.0043 | -0.0043 (51) |
| 25-40 | 7125 | 0.223 | 0.1237 | +0.0993 ± 0.0026 | 0.6401 | 0.3817 | 0.5238 | 0.2098 | 0.2126 | -0.060 ± 0.0041 | -0.0733 (3) |
| 40+ | 4874 | 0.3808 | 0.0436 | +0.3372 ± 0.0034 | 0.9919 | 0.1696 | 0.6284 | 0.1013 | 0.0566 | -0.076 ± 0.0028 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 920 | 0.2029 | 0.2033 | -0.0004 ± 0.0005 | 0.586 | 0.5873 | 0.5085 | 0.4935 | 0.5207 | -0.094 ± 0.0159 | -0.0117 (6) |
| 3-5 | 667 | 0.213 | 0.2099 | +0.0031 ± 0.0014 | 0.6098 | 0.6029 | 0.5172 | 0.4776 | 0.4558 | -0.130 ± 0.019 | 0.01 (3) |
| 5-10 | 1481 | 0.2052 | 0.2034 | +0.0018 ± 0.0018 | 0.5962 | 0.5914 | 0.5376 | 0.4632 | 0.4902 | -0.086 ± 0.0121 | -0.01 (4) |
| 10-15 | 1292 | 0.2143 | 0.2071 | +0.0072 ± 0.0032 | 0.6214 | 0.6 | 0.5573 | 0.4329 | 0.469 | -0.101 ± 0.0132 | -0.04 (5) |
| 15-25 | 1870 | 0.2329 | 0.2111 | +0.0218 ± 0.0042 | 0.6622 | 0.6061 | 0.5844 | 0.3888 | 0.4326 | -0.102 ± 0.0109 | -0.0183 (12) |
| 25-40 | 1294 | 0.2657 | 0.201 | +0.0647 ± 0.0078 | 0.7414 | 0.5829 | 0.6591 | 0.3451 | 0.4011 | -0.107 ± 0.0125 | -0.008 (5) |
| 40+ | 472 | 0.3746 | 0.1573 | +0.2172 ± 0.0183 | 1.0176 | 0.4786 | 0.7309 | 0.2426 | 0.2775 | -0.091 ± 0.0176 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5040 | 0.1904 | 0.1905 | -0.0002 ± 0.0002 | 0.5559 | 0.5561 | 0.5075 | 0.4924 | 0.5065 | -0.041 ± 0.0063 | -0.0154 (26) |
| 3-5 | 3471 | 0.1944 | 0.1934 | +0.0010 ± 0.0006 | 0.5661 | 0.5631 | 0.511 | 0.4713 | 0.4777 | -0.045 ± 0.0077 | 0.01 (5) |
| 5-10 | 7748 | 0.1958 | 0.1925 | +0.0034 ± 0.0008 | 0.5762 | 0.5635 | 0.5061 | 0.4319 | 0.4489 | -0.039 ± 0.005 | -0.0117 (6) |
| 10-15 | 6450 | 0.2022 | 0.1902 | +0.0120 ± 0.0014 | 0.594 | 0.557 | 0.5067 | 0.3828 | 0.3974 | -0.049 ± 0.0055 | -0.0189 (18) |
| 15-25 | 9192 | 0.2158 | 0.179 | +0.0369 ± 0.0017 | 0.6284 | 0.526 | 0.5233 | 0.3279 | 0.3337 | -0.061 ± 0.0044 | -0.014 (52) |
| 25-40 | 8248 | 0.2505 | 0.138 | +0.1124 ± 0.0026 | 0.7074 | 0.421 | 0.5592 | 0.2418 | 0.227 | -0.076 ± 0.0041 | -0.0095 (20) |
| 40+ | 6549 | 0.4022 | 0.0589 | +0.3434 ± 0.0035 | 1.0597 | 0.2121 | 0.6545 | 0.1187 | 0.0797 | -0.074 ± 0.0029 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1130 | 0.1962 | 0.1973 | -0.0011 ± 0.0005 | 0.5721 | 0.5747 | 0.5021 | 0.4866 | 0.523 | -0.061 ± 0.0138 | -0.0191 (11) |
| 3-5 | 804 | 0.2095 | 0.2082 | +0.0013 ± 0.0013 | 0.606 | 0.6013 | 0.4979 | 0.4584 | 0.4627 | -0.108 ± 0.0168 | 0.002 (5) |
| 5-10 | 1725 | 0.2031 | 0.1987 | +0.0044 ± 0.0016 | 0.5918 | 0.5795 | 0.5105 | 0.4368 | 0.4435 | -0.107 ± 0.011 | -0.01 (10) |
| 10-15 | 1435 | 0.2121 | 0.2022 | +0.0099 ± 0.0029 | 0.6147 | 0.5863 | 0.5381 | 0.4149 | 0.4383 | -0.107 ± 0.012 | -0.0286 (7) |
| 15-25 | 1683 | 0.231 | 0.2122 | +0.0188 ± 0.0044 | 0.6592 | 0.6088 | 0.5808 | 0.3867 | 0.4349 | -0.104 ± 0.0113 | -0.03 (1) |
| 25-40 | 997 | 0.2171 | 0.2074 | +0.0097 ± 0.0085 | 0.6241 | 0.5962 | 0.6533 | 0.3432 | 0.4804 | -0.058 ± 0.0133 | -0.0267 (3) |
| 40+ | 222 | 0.3135 | 0.1759 | +0.1376 ± 0.0255 | 0.8438 | 0.5218 | 0.7369 | 0.2794 | 0.3694 | -0.084 ± 0.0259 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5681 | 0.1866 | 0.1871 | -0.0005 ± 0.0002 | 0.5493 | 0.5496 | 0.4872 | 0.4718 | 0.4855 | -0.038 ± 0.0058 | -0.0189 (44) |
| 3-5 | 4062 | 0.2053 | 0.2035 | +0.0018 ± 0.0006 | 0.5959 | 0.5899 | 0.4819 | 0.4424 | 0.4404 | -0.057 ± 0.0072 | -0.0073 (22) |
| 5-10 | 8819 | 0.196 | 0.1905 | +0.0054 ± 0.0007 | 0.5755 | 0.5584 | 0.4857 | 0.4118 | 0.4117 | -0.056 ± 0.0047 | -0.0117 (42) |
| 10-15 | 7099 | 0.195 | 0.1795 | +0.0155 ± 0.0012 | 0.5751 | 0.531 | 0.4963 | 0.3729 | 0.3719 | -0.063 ± 0.0051 | -0.0136 (14) |
| 15-25 | 9123 | 0.211 | 0.1718 | +0.0391 ± 0.0017 | 0.6154 | 0.5072 | 0.5091 | 0.3145 | 0.312 | -0.068 ± 0.0043 | -0.0533 (3) |
| 25-40 | 7120 | 0.2175 | 0.1238 | +0.0937 ± 0.0026 | 0.6283 | 0.3811 | 0.5256 | 0.21 | 0.2211 | -0.052 ± 0.004 | -0.02 (4) |
| 40+ | 4794 | 0.3894 | 0.0476 | +0.3417 ± 0.0036 | 1.0145 | 0.1798 | 0.6374 | 0.1068 | 0.0628 | -0.076 ± 0.003 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1604 | 0.1962 | 0.1958 | +0.0004 ± 0.0004 | 0.5705 | 0.5694 | 0.5088 | 0.4938 | 0.49 | -0.076 ± 0.0113 | -0.0221 (56) |
| 3-5 | 1118 | 0.1894 | 0.1895 | -0.0001 ± 0.001 | 0.5569 | 0.5555 | 0.4985 | 0.4586 | 0.4776 | -0.054 ± 0.0133 | -0.0194 (34) |
| 5-10 | 2283 | 0.1996 | 0.1946 | +0.0050 ± 0.0014 | 0.5886 | 0.5725 | 0.5078 | 0.4342 | 0.438 | -0.076 ± 0.0095 | -0.005 (78) |
| 10-15 | 1575 | 0.2156 | 0.2023 | +0.0133 ± 0.0028 | 0.6252 | 0.5879 | 0.544 | 0.4213 | 0.4273 | -0.092 ± 0.0117 | 0.0012 (66) |
| 15-25 | 2054 | 0.232 | 0.2075 | +0.0244 ± 0.004 | 0.6619 | 0.5989 | 0.5917 | 0.3967 | 0.4328 | -0.090 ± 0.0101 | -0.0214 (59) |
| 25-40 | 1204 | 0.2414 | 0.2112 | +0.0301 ± 0.0081 | 0.6893 | 0.6055 | 0.6882 | 0.3766 | 0.4842 | -0.084 ± 0.0125 | -0.0252 (27) |
| 40+ | 446 | 0.3276 | 0.1963 | +0.1313 ± 0.0201 | 0.9364 | 0.5732 | 0.8082 | 0.3316 | 0.4484 | -0.093 ± 0.0188 | -0.1137 (8) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5793 | 0.1768 | 0.1768 | +0.0001 ± 0.0002 | 0.5237 | 0.523 | 0.5098 | 0.4945 | 0.5001 | -0.043 ± 0.0056 | -0.0154 (103) |
| 3-5 | 3956 | 0.1944 | 0.1935 | +0.0009 ± 0.0006 | 0.5674 | 0.5648 | 0.5018 | 0.462 | 0.4707 | -0.041 ± 0.0071 | -0.0212 (73) |
| 5-10 | 8096 | 0.197 | 0.1905 | +0.0065 ± 0.0007 | 0.5812 | 0.5616 | 0.5026 | 0.429 | 0.423 | -0.061 ± 0.0049 | -0.0084 (134) |
| 10-15 | 5547 | 0.2111 | 0.194 | +0.0171 ± 0.0015 | 0.6141 | 0.5689 | 0.5372 | 0.4143 | 0.4051 | -0.075 ± 0.006 | -0.0057 (111) |
| 15-25 | 6824 | 0.2317 | 0.1991 | +0.0326 ± 0.0021 | 0.6659 | 0.5775 | 0.5762 | 0.3807 | 0.3952 | -0.069 ± 0.0054 | -0.026 (108) |
| 25-40 | 4397 | 0.2578 | 0.1905 | +0.0673 ± 0.0041 | 0.7289 | 0.5544 | 0.6397 | 0.3275 | 0.3789 | -0.063 ± 0.0065 | -0.0277 (53) |
| 40+ | 1988 | 0.369 | 0.1588 | +0.2102 ± 0.0092 | 1.0374 | 0.4734 | 0.7406 | 0.2413 | 0.2907 | -0.059 ± 0.0085 | -0.054 (15) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 7996 | 1.022 ± 0.031 | 1.089 | 0.1676 | 0.1702 | 0.216 | 0.2033 |
| gen2 | 7996 | 0.819 ± 0.028 | 1.067 | 0.1736 | 0.1705 | 0.2333 | 0.2032 |
| gen1_elo | 7996 | 1.007 ± 0.03 | 1.078 | 0.1741 | 0.1704 | 0.2151 | 0.2034 |
| gen1_sr | 7996 | 1.005 ± 0.037 | 1.115 | 0.1333 | 0.172 | 0.2295 | 0.2029 |
| gen1_ledger | 10284 | 0.867 ± 0.023 | 1.067 | 0.1899 | 0.1767 | 0.2173 | 0.2 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 37,056)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 9,003 | 24.3% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 8,624 | 23.3% |
| BOOK_QUALITY | execution | 6,291 | 17.0% |
| POOR_DATA | data | 4,229 | 11.4% |
| LIMITED_DATA | data | 2,220 | 6.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 2,160 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 1,509 | 4.1% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,412 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 1,034 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 573 | 1.6% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 24.3%, coverage 23.3%, data 17.4%, execution 17.0%, market_freshness/coverage 8.6%, mapping 4.1%, model_calibration_or_unknown 3.8%, model_calibration 1.6%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 95.0%, LOW_DATA_QUALITY 72.1%, THIN_PLAYER_HISTORY 60.3%, STALE_PLAYER_DATA 52.2%, STALE_KALSHI_QUOTE 48.1%, MODEL_INTERNAL_DISAGREEMENT 41.8%, ASYMMETRIC_SAMPLE_SIZE 33.2%, WIDE_SPREAD 23.4%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 15.0%, LEVEL_TRANSFER_RISK 9.4%, LOW_DISPLAYED_LIQUIDITY 8.6%, EVENT_MAPPING_RISK 6.9%, MODEL_CALIBRATION_OUTLIER 3.5%, EXTERNAL_MARKET_REJECTION 3.2%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.7%, POST_SETTLEMENT_OBSERVATION 23.3%, POSSIBLE_IN_PLAY_QUOTE 6.2%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 19,822)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,955 | 35.1% |
| STALE_QUOTE | market_freshness | 4,011 | 20.2% |
| BOOK_QUALITY | execution | 3,240 | 16.4% |
| POOR_DATA | data | 1,793 | 9.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,170 | 5.9% |
| IDENTITY_AMBIGUOUS | mapping | 836 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 677 | 3.4% |
| LIMITED_DATA | data | 655 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 345 | 1.7% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 139 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 35.1%, market_freshness 20.2%, execution 16.4%, data 12.3%, market_freshness/coverage 9.3%, mapping 4.2%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.1%, START_UNVERIFIABLE 97.3%, LOW_DATA_QUALITY 75.2%, THIN_PLAYER_HISTORY 62.4%, STALE_KALSHI_QUOTE 55.6%, STALE_PLAYER_DATA 45.5%, MODEL_INTERNAL_DISAGREEMENT 41.9%, ASYMMETRIC_SAMPLE_SIZE 34.4%, WIDE_SPREAD 22.6%, MODEL_HIGH_UNCERTAINTY 19.2%, PLAYER_IDENTITY_RISK 17.9%, LOW_DISPLAYED_LIQUIDITY 8.4%, EVENT_MAPPING_RISK 8.4%, LEVEL_TRANSFER_RISK 8.3%, MODEL_CALIBRATION_OUTLIER 4.6%, EXTERNAL_MARKET_REJECTION 1.8%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 38.0%, POST_SETTLEMENT_OBSERVATION 35.1%, POSSIBLE_IN_PLAY_QUOTE 6.3%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 15938, "IDENTITY_AMBIGUOUS": 3884}; ticker orientation: {"VERIFIED": 19822}.

Checks: discipline:AMBIGUOUS 1264, discipline:PASS 18558, identity_confidence:AMBIGUOUS 3544, identity_confidence:PASS 16278, level_mapping:NA 1276, level_mapping:PASS 18546, market_pair:AMBIGUOUS 504, market_pair:NA 427, market_pair:PASS 18891, model_complement:NA 389, model_complement:PASS 19433, namesake:AMBIGUOUS 6, namesake:PASS 19816, physical_match_id:NA 6571, physical_match_id:PASS 13251, player_ids:PASS 19822, same_pair_other_event:PASS 19822, ticker_orientation:PASS 19822

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,595 | 3.7% | 3.1% | 1.2% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 24, "market_freshness/coverage": 22} | 5.47 | 0.2218 / 0.2178 (863) | 25.7% | 2.4% | 3.2% | 3.0% |
| CHALLENGER | 13,232 | 16.6% | 6.0% | 11.1% | {"coverage": 1345, "market_freshness": 274, "market_freshness/coverage": 238, "data": 164, "model_calibration_or_unknown": 80, "execution": 41, "model_calibration": 40, "mapping": 17, "possible_market_error": 1} | 7.35 | 0.2213 / 0.2107 (3074) | 41.8% | 13.8% | 4.0% | 22.8% |
| DOUBLES | 2,748 | 46.0% | 46.0% | 6.4% | {"execution": 699, "mapping": 379, "market_freshness": 106, "market_freshness/coverage": 73, "coverage": 7} | 23.02 | 0.2986 / 0.2326 (691) | 8.5% | 0.0% | 100.0% | 6.3% |
| ITF_MEN | 26,338 | 25.4% | 17.7% | 33.8% | {"coverage": 2355, "market_freshness": 1403, "execution": 1038, "data": 982, "market_freshness/coverage": 683, "mapping": 226, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.76 | 0.2189 / 0.1985 (5559) | 42.2% | 70.1% | 14.6% | 21.6% |
| ITF_WOMEN | 33,307 | 26.5% | 18.7% | 44.5% | {"coverage": 3169, "market_freshness": 1967, "execution": 1379, "data": 1201, "market_freshness/coverage": 774, "mapping": 208, "model_calibration_or_unknown": 98, "model_calibration": 23} | 12.46 | 0.2031 / 0.1934 (6469) | 42.8% | 57.5% | 10.0% | 21.9% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,915 | 5.9% | 5.0% | 1.5% | {"market_freshness": 111, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.65 | 0.2315 / 0.221 (812) | 30.3% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.5% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 113 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 519 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 286 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 20.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 1252 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFMATCH-26NOV10KOUPOR-POR` | ITF_MEN | fair_v1 | 87% / 2% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 80 min (STALE); data POOR (grade D, thinner serve sample 1554.0, ratio 1.02); no external reference |
| 12 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 13 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 15 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 113 min (STALE); no external reference |
| 16 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 17 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 18 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 19 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 20 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 21 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 22 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 23 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 24 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 25 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 26 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 163 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 27 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 28 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 29 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 30 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 31 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 32 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 33 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 34 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 35 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 36 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 37 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 38 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 39 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 40 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 41 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 43 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 44 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 45 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 46 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 47 | `KXITFWMATCH-26NOV11CORROJ-ROJ` | ITF_WOMEN | fair_v1 | 87% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 649 min (STALE); data POOR (grade D, thinner serve sample 531.0, ratio 1.04); no external reference |
| 48 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 49 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 124 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.973, "by_level_share_of_ge_25pp": {"ATP": 0.0124, "CHALLENGER": 0.111, "DOUBLES": 0.0638, "ITF_MEN": 0.3379, "ITF_WOMEN": 0.4449, "OTHER": 0.0006, "WTA": 0.0147, "WTA125": 0.0148}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5559, "share_primary_cause_market_settled_or_in_play": 0.4441, "share_primary_cause_stale_quote_only": 0.2024}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 19822, "identity_ambiguous_share": 0.1959, "ticker_orientation": {"VERIFIED": 19822}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 13251, "with_external": 645, "coverage": 0.0487, "external_status": {"EXTERNAL_STALE": 409, "AGREES_WITH_KALSHI": 223, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 409, "MODEL_LONE_OUTLIER": 223, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3457, "share_external_supports_model": 0.0202}, "pregame_clean_ge_25pp": {"n": 6062, "with_external": 613, "coverage": 0.1011, "external_status": {"EXTERNAL_STALE": 384, "AGREES_WITH_KALSHI": 216, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 384, "MODEL_LONE_OUTLIER": 216, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3524, "share_external_supports_model": 0.0212}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 476.0, "median_sample_ratio": 2.46, "median_min_matches": 18.0, "median_max_days_since_last": 246.0, "share_severe_asymmetry": 0.2073, "data_status": {"POOR": 11304, "LIMITED": 4958, "ADEQUATE": 3560}, "comparison_lt_10pp": {"median_thinner_serve_points": 1670.0, "median_sample_ratio": 1.71, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1614, "model_minus_observed": 0.0696, "kalshi_minus_observed": -0.0696, "brier_diff_model_minus_kalshi": 0.0036}, "4-10x": {"n": 1095, "model_minus_observed": 0.0886, "kalshi_minus_observed": -0.0562, "brier_diff_model_minus_kalshi": 0.0099}, "<2x": {"n": 3929, "model_minus_observed": 0.1032, "kalshi_minus_observed": -0.0193, "brier_diff_model_minus_kalshi": 0.0152}, ">=10x": {"n": 1358, "model_minus_observed": 0.1259, "kalshi_minus_observed": -0.0467, "brier_diff_model_minus_kalshi": 0.0184}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 7996, "model": {"intercept": -0.56, "slope": 0.819, "slope_se": 0.028}, "kalshi_mid_same_rows": {"intercept": 0.171, "slope": 1.067, "slope_se": 0.032}, "mean_extremity_model": 0.1736, "mean_extremity_kalshi": 0.1705, "model_brier": 0.2333, "kalshi_brier": 0.2032, "brier_diff_model_minus_kalshi": 0.0301, "brier_diff_se": 0.0021, "model_logloss": 0.664, "kalshi_logloss": 0.5887}, "fair_v1": {"n": 7996, "model": {"intercept": -0.468, "slope": 1.022, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.217, "slope": 1.089, "slope_se": 0.032}, "mean_extremity_model": 0.1676, "mean_extremity_kalshi": 0.1702, "model_brier": 0.216, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.0127, "brier_diff_se": 0.0017, "model_logloss": 0.6213, "kalshi_logloss": 0.5887}, "gen1_elo": {"n": 7996, "model": {"intercept": -0.459, "slope": 1.007, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.218, "slope": 1.078, "slope_se": 0.031}, "mean_extremity_model": 0.1741, "mean_extremity_kalshi": 0.1704, "model_brier": 0.2151, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": 0.0117, "brier_diff_se": 0.0017, "model_logloss": 0.6198, "kalshi_logloss": 0.5889}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2534, "share_ge_15": 0.4491, "median_abs_gap": 13.17, "n": 52298}, "gen1_elo": {"share_ge_25": 0.2512, "share_ge_15": 0.445, "median_abs_gap": 13.0, "n": 52298}, "gen1_sr": {"share_ge_25": 0.3159, "share_ge_15": 0.5246, "median_abs_gap": 15.98, "n": 52298}, "gen2": {"share_ge_25": 0.3157, "share_ge_15": 0.5125, "median_abs_gap": 15.5, "n": 52298}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1518, "share_ge_15": 0.3549, "median_abs_gap": 10.71, "n": 39930}, "gen1_elo": {"share_ge_25": 0.1502, "share_ge_15": 0.3497, "median_abs_gap": 10.51, "n": 39930}, "gen1_sr": {"share_ge_25": 0.2154, "share_ge_15": 0.4401, "median_abs_gap": 13.0, "n": 39933}, "gen2": {"share_ge_25": 0.2303, "share_ge_15": 0.4388, "median_abs_gap": 12.84, "n": 39933}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.47, "share_ge_25_all": 0.0371, "share_ge_25_pregame_clean": 0.0311}, "WTA": {"median_abs_gap_pregame_clean": 7.65, "share_ge_25_all": 0.0592, "share_ge_25_pregame_clean": 0.0502}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2345, "share_within_10pp_all": 0.436, "share_within_10pp_pregame_clean": 0.4905, "corr_model_vs_mid_pregame_clean": 0.8497}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1154, "model_brier": 0.1968, "kalshi_brier": 0.1969, "brier_diff_model_minus_kalshi": -0.0001}, "10-15": {"n_settled": 1395, "model_brier": 0.2193, "kalshi_brier": 0.2093, "brier_diff_model_minus_kalshi": 0.0099}, "15-25": {"n_settled": 1769, "model_brier": 0.2254, "kalshi_brier": 0.2065, "brier_diff_model_minus_kalshi": 0.0189}, "25-40": {"n_settled": 1009, "model_brier": 0.225, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": 0.0215}, "3-5": {"n_settled": 741, "model_brier": 0.2089, "kalshi_brier": 0.2083, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 211, "model_brier": 0.3067, "kalshi_brier": 0.1672, "brier_diff_model_minus_kalshi": 0.1395}, "5-10": {"n_settled": 1717, "model_brier": 0.203, "kalshi_brier": 0.2014, "brier_diff_model_minus_kalshi": 0.0016}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'NO_SKILL:gen2|WTA', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.56, "slope": 0.819, "slope_se": 0.028}, "kalshi_slope": {"intercept": 0.171, "slope": 1.067, "slope_se": 0.032}, "n": 7996}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.501, "slope": 0.867, "slope_se": 0.023}, "kalshi_slope": {"intercept": 0.152, "slope": 1.067, "slope_se": 0.027}, "n": 10284}, "NO_SKILL:gen2|WTA": {"n_settled": 346, "model_brier": 0.25, "kalshi_brier": 0.2262, "brier_diff_model_minus_kalshi": 0.0238, "brier_diff_se": 0.0089, "corr_model_outcome": 0.2572, "corr_kalshi_outcome": 0.3102}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 691, "model_brier": 0.2986, "kalshi_brier": 0.2326, "brier_diff_model_minus_kalshi": 0.0661, "brier_diff_se": 0.0111, "corr_model_outcome": 0.1045, "corr_kalshi_outcome": 0.2761}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
