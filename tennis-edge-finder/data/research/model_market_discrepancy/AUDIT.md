# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-10T18:21Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 86,468): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.2%, 15-25 19.1%, 25-40 13.7%, 40+ 8.2%; median gap 11.85 pp.
* **Where the extremes live**: 97.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.9%, Challenger 11.1%, doubles 6.5%). Main tour: ATP 3.8% and WTA 5.9% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 18,918): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.5%, STALE_QUOTE 20.1%, BOOK_QUALITY 16.9%, POOR_DATA 9.2%, POSSIBLY_IN_PLAY_QUOTE 5.8%, IDENTITY_AMBIGUOUS 4.3%, IN_PLAY_QUOTE 3.4%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.8%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.5%, market_freshness 20.1%, execution 16.9%, data 12.5%, market_freshness/coverage 9.2%, mapping 4.3%, model_calibration_or_unknown 1.8%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 54.7% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.7% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 18,918 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.0% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 27.2% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 480.0 points vs 1722.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.016, Gen-2 0.812, Gen-1 ledger 0.862 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 960 model 0.2263 vs Kalshi 0.2051; n 196 model 0.3016 vs Kalshi 0.1723.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 363,046 model-market comparisons (597,551 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 120,386 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-10T18:00:29.068767+00:00'], shadow board 99,633 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-10T18:00:33.719298+00:00'], Model 4 43,685 rows, 29,975 settled tickers, 11,248 tickers with an external scan.
* By model: {"gen1_ledger": 80836, "gen1_elo": 50071, "fair_v1": 50071, "gen2": 50071, "gen1_sr": 50071, "model4_fundamental": 41005, "model4_conditioned": 40921}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 86,468 | 14.1 | 9.6 | 20.2 | 15.2 | 19.1 | 13.7 | 8.2 | 11.85 | 41.0% | 21.9% |
| MW fair_v1 | 50,071 | 12.8 | 8.6 | 18.8 | 15.2 | 19.6 | 14.9 | 10.1 | 13.08 | 44.6% | 25.1% |
| MW gen1_elo | 50,071 | 12.5 | 8.8 | 19.2 | 15.3 | 19.4 | 14.8 | 10.0 | 12.9 | 44.2% | 24.8% |
| MW gen1_ledger | 36,397 | 15.8 | 10.9 | 22.2 | 15.1 | 18.5 | 11.9 | 5.6 | 10.26 | 36.0% | 17.5% |
| MW gen1_sr | 50,071 | 10.0 | 7.2 | 16.7 | 13.9 | 20.8 | 18.7 | 12.7 | 15.87 | 52.2% | 31.4% |
| MW gen2 | 50,071 | 10.9 | 7.6 | 16.7 | 13.7 | 19.6 | 17.7 | 13.8 | 15.47 | 51.1% | 31.5% |
| all families model4_conditioned | 40,921 | 22.2 | 17.9 | 34.5 | 17.0 | 5.0 | 2.2 | 1.2 | 6.07 | 8.4% | 3.4% |
| all families model4_fundamental | 41,005 | 17.3 | 13.5 | 34.0 | 19.9 | 9.9 | 3.8 | 1.5 | 7.61 | 15.2% | 5.3% |

Configurable thresholds (primary): >=5pp 76.4%, >=10pp 56.2%, >=15pp 41.0%, >=20pp 30.2%, >=25pp 21.9%, >=30pp 15.8%, >=40pp 8.2%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.45pp; >=10pp 45.2%, >=25pp 17.3%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,076 | 28.1 | 15.7 | 28.0 | 13.3 | 10.7 | 3.6 | 0.6 | 5.84 | 14.9% | 4.2% |
| CHALLENGER | 7,951 | 16.4 | 9.7 | 20.6 | 15.2 | 16.0 | 11.3 | 10.8 | 10.86 | 38.1% | 22.1% |
| ITF_MEN | 14,263 | 9.7 | 7.3 | 17.0 | 14.9 | 21.2 | 17.3 | 12.7 | 15.45 | 51.1% | 30.0% |
| ITF_WOMEN | 19,368 | 9.5 | 7.0 | 16.1 | 14.7 | 22.1 | 18.6 | 12.0 | 15.93 | 52.6% | 30.5% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,080 | 16.7 | 13.2 | 25.1 | 20.7 | 16.5 | 6.8 | 1.1 | 8.61 | 24.3% | 7.8% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,076 | 26.5 | 15.6 | 26.2 | 15.8 | 11.2 | 3.9 | 0.8 | 6.09 | 16.0% | 4.7% |
| CHALLENGER | 7,951 | 14.5 | 9.1 | 19.1 | 13.8 | 18.5 | 13.5 | 11.4 | 12.47 | 43.5% | 24.9% |
| ITF_MEN | 14,263 | 8.0 | 6.2 | 15.0 | 13.7 | 20.2 | 20.4 | 16.5 | 17.97 | 57.0% | 36.9% |
| ITF_WOMEN | 19,368 | 7.9 | 5.9 | 14.1 | 12.7 | 20.6 | 21.2 | 17.6 | 19.07 | 59.4% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,080 | 14.0 | 10.4 | 21.8 | 16.2 | 22.4 | 12.8 | 2.5 | 11.2 | 37.6% | 15.3% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,076 | 23.2 | 14.1 | 25.7 | 15.5 | 14.4 | 6.0 | 1.1 | 7.09 | 21.6% | 7.1% |
| CHALLENGER | 7,951 | 15.1 | 9.7 | 20.8 | 15.6 | 16.2 | 11.9 | 10.8 | 11.2 | 38.9% | 22.6% |
| ITF_MEN | 14,263 | 9.4 | 7.3 | 17.1 | 14.2 | 21.7 | 17.4 | 13.0 | 15.81 | 52.0% | 30.4% |
| ITF_WOMEN | 19,368 | 9.2 | 6.9 | 16.3 | 15.7 | 22.1 | 18.5 | 11.3 | 15.6 | 51.9% | 29.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,080 | 22.6 | 17.1 | 31.9 | 15.3 | 8.8 | 3.2 | 1.0 | 6.12 | 13.1% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,453 | 28.0 | 19.5 | 29.3 | 12.2 | 8.0 | 2.6 | 0.5 | 5.27 | 11.0% | 3.0% |
| CHALLENGER | 4,931 | 22.6 | 14.5 | 28.0 | 14.7 | 13.2 | 5.5 | 1.5 | 7.03 | 20.2% | 7.0% |
| DOUBLES | 2,661 | 4.9 | 4.5 | 12.9 | 11.0 | 20.5 | 24.5 | 21.7 | 23.2 | 66.7% | 46.3% |
| ITF_MEN | 10,557 | 12.7 | 9.6 | 21.3 | 15.6 | 21.7 | 13.0 | 6.1 | 11.86 | 40.8% | 19.1% |
| ITF_WOMEN | 12,579 | 13.5 | 9.3 | 19.8 | 15.7 | 21.5 | 14.7 | 5.5 | 12.19 | 41.7% | 20.2% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,811 | 24.0 | 16.0 | 31.5 | 16.9 | 8.9 | 2.5 | 0.2 | 6.52 | 11.7% | 2.8% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,949 | 28.5 | 15.9 | 28.4 | 13.2 | 10.4 | 3.1 | 0.3 | 5.67 | 13.9% | 3.4% |
| CHALLENGER | 5,630 | 21.0 | 12.1 | 25.6 | 17.9 | 16.0 | 5.8 | 1.6 | 8.2 | 23.4% | 7.4% |
| ITF_MEN | 10,432 | 11.9 | 8.6 | 20.4 | 17.2 | 22.2 | 14.2 | 5.5 | 12.51 | 41.9% | 19.7% |
| ITF_WOMEN | 14,204 | 11.4 | 8.5 | 18.9 | 17.0 | 24.0 | 15.3 | 4.8 | 13.16 | 44.1% | 20.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,966 | 17.0 | 13.2 | 25.5 | 21.1 | 16.5 | 6.2 | 0.6 | 8.44 | 23.3% | 6.8% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,949 | 26.8 | 16.0 | 26.5 | 15.7 | 11.1 | 3.5 | 0.4 | 6.0 | 15.0% | 3.9% |
| CHALLENGER | 5,630 | 18.3 | 11.6 | 23.9 | 16.2 | 19.0 | 9.2 | 1.8 | 8.96 | 30.0% | 11.0% |
| ITF_MEN | 10,433 | 9.5 | 7.3 | 17.5 | 15.8 | 22.1 | 18.5 | 9.2 | 14.95 | 49.9% | 27.8% |
| ITF_WOMEN | 14,205 | 8.9 | 6.9 | 16.0 | 14.3 | 22.5 | 20.6 | 10.7 | 16.51 | 53.8% | 31.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,966 | 14.3 | 10.5 | 22.0 | 16.4 | 22.5 | 12.4 | 1.9 | 11.03 | 36.9% | 14.3% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,385 | 28.2 | 19.7 | 29.3 | 12.4 | 7.7 | 2.4 | 0.3 | 5.23 | 10.4% | 2.7% |
| CHALLENGER | 4,366 | 23.9 | 15.4 | 29.2 | 14.8 | 12.5 | 3.8 | 0.4 | 6.58 | 16.7% | 4.2% |
| DOUBLES | 2,494 | 4.8 | 4.5 | 13.1 | 11.1 | 20.3 | 24.5 | 21.8 | 23.12 | 66.6% | 46.2% |
| ITF_MEN | 9,115 | 13.5 | 10.1 | 22.8 | 16.1 | 21.8 | 11.5 | 4.2 | 11.02 | 37.5% | 15.7% |
| ITF_WOMEN | 10,823 | 14.1 | 9.8 | 20.9 | 16.2 | 21.6 | 13.7 | 3.7 | 11.42 | 39.0% | 17.3% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,748 | 24.3 | 16.4 | 31.5 | 16.9 | 8.9 | 2.0 | 0.1 | 6.42 | 10.9% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,661 | 4.9 | 4.5 | 12.9 | 11.0 | 20.5 | 24.5 | 21.7 | 23.2 | 66.7% | 46.3% |
| singles | 33,736 | 16.7 | 11.4 | 22.9 | 15.4 | 18.4 | 10.9 | 4.3 | 9.74 | 33.6% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 10,480 | 12.8 | 9.1 | 19.6 | 15.3 | 19.6 | 14.1 | 9.5 | 12.69 | 43.2% | 23.6% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 32,685 | 13.2 | 8.7 | 18.9 | 15.1 | 19.1 | 14.9 | 10.1 | 12.91 | 44.1% | 25.0% |
| UNKNOWN | 6,493 | 10.4 | 7.5 | 17.0 | 16.4 | 21.6 | 15.9 | 11.2 | 14.46 | 48.7% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 14,195 | 19.3 | 11.8 | 22.5 | 15.8 | 14.8 | 9.3 | 6.3 | 8.92 | 30.5% | 15.6% |
| B | 6,090 | 12.9 | 8.5 | 19.6 | 15.3 | 19.7 | 12.6 | 11.4 | 12.82 | 43.7% | 24.0% |
| C | 7,067 | 12.1 | 8.7 | 19.5 | 15.7 | 18.7 | 14.6 | 10.6 | 12.89 | 43.9% | 25.2% |
| D | 8,061 | 11.6 | 8.4 | 17.8 | 15.1 | 21.9 | 15.7 | 9.4 | 13.94 | 47.0% | 25.2% |
| F | 14,658 | 7.3 | 5.6 | 14.9 | 14.5 | 23.1 | 21.1 | 13.4 | 17.96 | 57.7% | 34.5% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,721 | 24.9 | 16.0 | 29.0 | 14.9 | 10.5 | 3.4 | 1.2 | 6.34 | 15.2% | 4.7% |
| B | 5,020 | 16.6 | 11.0 | 24.3 | 16.9 | 18.9 | 9.4 | 3.0 | 9.59 | 31.3% | 12.4% |
| C | 7,114 | 11.0 | 7.8 | 19.6 | 14.8 | 21.1 | 15.6 | 10.2 | 13.56 | 46.9% | 25.8% |
| D | 5,455 | 14.5 | 10.1 | 21.1 | 15.3 | 20.9 | 12.7 | 5.5 | 11.27 | 39.0% | 18.1% |
| F | 9,087 | 10.2 | 8.3 | 16.3 | 14.5 | 23.4 | 19.1 | 8.1 | 15.32 | 50.6% | 27.2% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 16,062 | 17.8 | 10.8 | 21.5 | 15.6 | 15.2 | 10.1 | 9.1 | 9.98 | 34.3% | 19.1% |
| LIMITED | 10,895 | 13.6 | 9.6 | 20.5 | 15.8 | 19.5 | 13.3 | 7.7 | 11.89 | 40.5% | 21.0% |
| POOR | 23,114 | 8.9 | 6.6 | 16.0 | 14.8 | 22.6 | 19.1 | 12.0 | 16.29 | 53.7% | 31.1% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,171 | 23.6 | 18.1 | 33.0 | 15.5 | 6.4 | 3.0 | 0.4 | 5.9 | 9.8% | 3.4% |
| GAME_SPREAD | 6,861 | 22.9 | 15.3 | 32.1 | 16.8 | 9.0 | 3.3 | 0.6 | 6.69 | 12.9% | 4.0% |
| MATCH_WINNER | 36,397 | 15.8 | 10.9 | 22.2 | 15.1 | 18.5 | 11.9 | 5.6 | 10.26 | 36.0% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 16,890 | 28.2 | 16.8 | 30.8 | 12.6 | 8.9 | 2.4 | 0.3 | 5.58 | 11.6% | 2.7% |
| TOTAL_GAMES | 11,493 | 9.8 | 10.8 | 36.1 | 25.8 | 10.5 | 4.2 | 2.9 | 9.15 | 17.5% | 7.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,553 | 24.4 | 28.7 | 33.3 | 8.1 | 4.0 | 1.2 | 0.3 | 4.8 | 5.4% | 1.5% |
| GAME_SPREAD | 9,459 | 46.8 | 15.9 | 25.1 | 7.4 | 2.3 | 1.9 | 0.6 | 3.31 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,909 | 6.6 | 9.8 | 40.7 | 29.9 | 7.3 | 3.3 | 2.4 | 9.17 | 13.0% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,589 | 23.8 | 16.6 | 34.6 | 14.8 | 6.9 | 2.7 | 0.5 | 6.06 | 10.1% | 3.2% |
| GAME_SPREAD | 9,468 | 20.4 | 13.5 | 28.4 | 20.1 | 12.1 | 4.4 | 1.2 | 7.65 | 17.6% | 5.5% |
| TOTAL_GAMES | 16,948 | 10.0 | 10.8 | 36.5 | 24.3 | 11.3 | 4.4 | 2.6 | 9.02 | 18.4% | 7.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 50,071 | 44.6% | 25.1% | 13.08 | 35.4% | 15.2% | 10.68 |
| gen1_elo | 50,071 | 44.2% | 24.8% | 12.9 | 34.9% | 15.0% | 10.49 |
| gen1_sr | 50,071 | 52.2% | 31.4% | 15.87 | 43.9% | 21.6% | 12.97 |
| gen2 | 50,071 | 51.1% | 31.5% | 15.47 | 43.9% | 23.1% | 12.83 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,098 | 15.5 | 10.4 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 29,973 | 10.9 | 7.4 | 17.0 | 13.9 | 19.2 | 17.0 | 14.7 | 15.32 | 50.8% | 31.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 29,865 | 16.4 | 11.2 | 22.7 | 15.2 | 18.1 | 11.4 | 5.0 | 9.91 | 34.5% | 16.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 86,468 | 29865 | 23570 | 33033 | 24.9 | 132.3 | 1451.1 |
| ge_15pp | 35,445 | 10311 | 8394 | 16740 | 28.7 | 439.3 | 1451.1 |
| ge_25pp | 18,918 | 4909 | 3666 | 10343 | 34.3 | 584.4 | 1431.1 |
| lt_10pp | 37,884 | 15017 | 11149 | 11718 | 22.7 | 49.5 | 1421.7 |

Current slate `SL-20261110T182103Z-ab841816`: 531 priced rows, quote age at build {'median': 54.8, 'max': 54.8}, freshness {'STALE': 531}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 51 | 0.0 | 0.0 | 35.3 | 9.8 | 31.4 | 19.6 | 3.9 | 18.34 | 54.9% | 23.5% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,857 | 19.3 | 11.0 | 25.5 | 18.1 | 17.9 | 7.3 | 0.9 | 8.77 | 26.1% | 8.2% |
| KALSHI_LONE_OUTLIER | 32 | 6.2 | 6.2 | 75.0 | 6.2 | 3.1 | 3.1 | 0.0 | 6.16 | 6.2% | 3.1% |
| MARKETS_AGREE | 1,062 | 66.6 | 33.4 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,257 | 0.0 | 2.2 | 38.5 | 26.0 | 23.7 | 8.8 | 0.9 | 11.65 | 33.4% | 9.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 50,071 | 8288 (16.6%) | 27.2% | 1.0% | {"EXTERNAL_STALE": 4857, "AGREES_WITH_KALSHI": 2257, "ALL_AGREE": 1062, "SUPPORTS_MODEL_DIRECTION": 49, "AGREES_WITH_MODEL": 32, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 22,335 | 2051 (9.2%) | 36.7% | 1.5% | {"EXTERNAL_STALE": 1268, "AGREES_WITH_KALSHI": 753, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 12,547 | 629 (5.0%) | 34.7% | 2.1% | {"EXTERNAL_STALE": 398, "AGREES_WITH_KALSHI": 218, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,840 | 598 (10.2%) | 35.3% | 2.2% | {"EXTERNAL_STALE": 374, "AGREES_WITH_KALSHI": 211, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 20,098 | 4767 (23.7%) | 19.3% | 0.9% | {"EXTERNAL_STALE": 2712, "ALL_AGREE": 1062, "AGREES_WITH_KALSHI": 918, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 28, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 9,795 | 10.8 | 7.7 | 19.1 | 14.3 | 21.6 | 16.4 | 10.1 | 14.16 | 48.1% | 26.5% |
| 4-10x | 6,660 | 11.1 | 8.5 | 18.1 | 15.0 | 21.9 | 14.7 | 10.7 | 14.04 | 47.4% | 25.4% |
| <2x | 25,652 | 14.8 | 9.7 | 20.0 | 15.9 | 17.5 | 13.2 | 9.0 | 11.57 | 39.7% | 22.2% |
| >=10x | 7,964 | 10.3 | 6.5 | 15.0 | 14.3 | 21.7 | 19.0 | 13.3 | 16.49 | 53.9% | 32.2% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 13,184 | 12.5 | 8.5 | 19.8 | 16.1 | 19.0 | 13.6 | 10.5 | 12.75 | 43.1% | 24.0% |
| 300-1000 | 10,724 | 11.8 | 8.8 | 17.8 | 15.0 | 20.8 | 16.3 | 9.6 | 13.76 | 46.7% | 25.9% |
| <300 | 15,793 | 8.2 | 5.8 | 15.1 | 14.6 | 22.8 | 20.1 | 13.4 | 17.34 | 56.4% | 33.5% |
| >=3000 | 10,370 | 21.1 | 12.8 | 24.1 | 15.5 | 13.9 | 7.3 | 5.2 | 7.82 | 26.5% | 12.6% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1528 | 0.5498 | 0.411 | 0.4804 | +0.070 | -0.069 | 0.0037 ± 0.0039 |
| ratio 4-10x | 1036 | 0.5775 | 0.4323 | 0.4865 | +0.091 | -0.054 | 0.0101 ± 0.005 |
| ratio <2x | 3748 | 0.5368 | 0.4142 | 0.4368 | +0.100 | -0.022 | 0.0147 ± 0.0023 |
| ratio >=10x | 1273 | 0.5655 | 0.393 | 0.4423 | +0.123 | -0.049 | 0.017 ± 0.005 |
| thinner_sample 1000-3000 | 2105 | 0.5412 | 0.4139 | 0.4461 | +0.095 | -0.032 | 0.0123 ± 0.0032 |
| thinner_sample 300-1000 | 1692 | 0.5661 | 0.4259 | 0.474 | +0.092 | -0.048 | 0.0057 ± 0.0038 |
| thinner_sample <300 | 2471 | 0.5576 | 0.3904 | 0.45 | +0.107 | -0.060 | 0.0149 ± 0.0036 |
| thinner_sample >=3000 | 1317 | 0.5279 | 0.4345 | 0.4442 | +0.084 | -0.010 | 0.0153 ± 0.0031 |
| data_status ADEQUATE | 2103 | 0.5316 | 0.429 | 0.4384 | +0.093 | -0.009 | 0.0158 ± 0.0026 |
| data_status LIMITED | 1853 | 0.5501 | 0.4169 | 0.4657 | +0.084 | -0.049 | 0.0081 ± 0.0035 |
| data_status POOR | 3629 | 0.5602 | 0.4007 | 0.4555 | +0.105 | -0.055 | 0.0122 ± 0.0028 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1099 | 0.1976 | 0.1978 | -0.0003 ± 0.0005 | 0.575 | 0.5756 | 0.504 | 0.4888 | 0.5023 | -0.094 ± 0.0142 | -0.0087 (8) |
| 3-5 | 697 | 0.2063 | 0.2058 | +0.0005 ± 0.0014 | 0.5978 | 0.5949 | 0.5047 | 0.465 | 0.4792 | -0.101 ± 0.0177 | 0.01 (3) |
| 5-10 | 1633 | 0.2045 | 0.2029 | +0.0016 ± 0.0017 | 0.596 | 0.5897 | 0.5128 | 0.439 | 0.463 | -0.095 ± 0.0115 | -0.0143 (7) |
| 10-15 | 1318 | 0.2187 | 0.2091 | +0.0096 ± 0.0031 | 0.6292 | 0.6019 | 0.5249 | 0.4015 | 0.4234 | -0.109 ± 0.0128 | -0.055 (6) |
| 15-25 | 1682 | 0.2269 | 0.2081 | +0.0188 ± 0.0043 | 0.6492 | 0.5997 | 0.5756 | 0.381 | 0.4304 | -0.107 ± 0.0112 | -0.0045 (11) |
| 25-40 | 960 | 0.2263 | 0.2051 | +0.0211 ± 0.0088 | 0.6433 | 0.591 | 0.6499 | 0.3404 | 0.4604 | -0.071 ± 0.0136 | -0.06 (2) |
| 40+ | 196 | 0.3016 | 0.1723 | +0.1293 ± 0.0267 | 0.8096 | 0.5164 | 0.7299 | 0.2741 | 0.3673 | -0.088 ± 0.0257 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5651 | 0.1864 | 0.1873 | -0.0009 ± 0.0002 | 0.5491 | 0.5502 | 0.4917 | 0.4765 | 0.5091 | -0.020 ± 0.0058 | -0.01 (28) |
| 3-5 | 3750 | 0.1988 | 0.1969 | +0.0019 ± 0.0006 | 0.5785 | 0.5719 | 0.4825 | 0.4427 | 0.4392 | -0.058 ± 0.0073 | 0.005 (6) |
| 5-10 | 8252 | 0.202 | 0.1981 | +0.0039 ± 0.0007 | 0.59 | 0.5771 | 0.4844 | 0.4106 | 0.421 | -0.048 ± 0.005 | -0.0114 (22) |
| 10-15 | 6732 | 0.2024 | 0.1862 | +0.0161 ± 0.0013 | 0.5915 | 0.5464 | 0.4856 | 0.3618 | 0.3589 | -0.065 ± 0.0053 | -0.0379 (19) |
| 15-25 | 8574 | 0.2071 | 0.167 | +0.0401 ± 0.0017 | 0.6063 | 0.4964 | 0.4999 | 0.3043 | 0.3006 | -0.071 ± 0.0044 | -0.0043 (51) |
| 25-40 | 6727 | 0.2243 | 0.1251 | +0.0992 ± 0.0027 | 0.6431 | 0.3853 | 0.5266 | 0.2129 | 0.2154 | -0.061 ± 0.0042 | -0.0733 (3) |
| 40+ | 4557 | 0.3816 | 0.0435 | +0.3382 ± 0.0035 | 0.9937 | 0.1693 | 0.6295 | 0.1011 | 0.0568 | -0.076 ± 0.0029 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 882 | 0.2054 | 0.2058 | -0.0004 ± 0.0005 | 0.5917 | 0.5929 | 0.5079 | 0.493 | 0.5193 | -0.098 ± 0.0164 | -0.0117 (6) |
| 3-5 | 622 | 0.2122 | 0.2092 | +0.0030 ± 0.0015 | 0.6075 | 0.6011 | 0.5161 | 0.4766 | 0.455 | -0.133 ± 0.0198 | 0.01 (3) |
| 5-10 | 1401 | 0.208 | 0.2058 | +0.0022 ± 0.0018 | 0.6026 | 0.5967 | 0.5405 | 0.466 | 0.4911 | -0.091 ± 0.0125 | -0.01 (4) |
| 10-15 | 1225 | 0.2149 | 0.2071 | +0.0077 ± 0.0033 | 0.6227 | 0.6001 | 0.5607 | 0.4364 | 0.4702 | -0.107 ± 0.0136 | -0.04 (5) |
| 15-25 | 1772 | 0.2324 | 0.2118 | +0.0206 ± 0.0043 | 0.661 | 0.6079 | 0.5866 | 0.391 | 0.4374 | -0.104 ± 0.0112 | -0.0183 (12) |
| 25-40 | 1241 | 0.2691 | 0.1993 | +0.0698 ± 0.008 | 0.7496 | 0.579 | 0.6609 | 0.3469 | 0.3948 | -0.119 ± 0.0127 | -0.008 (5) |
| 40+ | 442 | 0.3723 | 0.162 | +0.2103 ± 0.0191 | 1.0155 | 0.4899 | 0.7353 | 0.2474 | 0.2896 | -0.089 ± 0.0185 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4834 | 0.1912 | 0.1914 | -0.0002 ± 0.0002 | 0.558 | 0.5581 | 0.5075 | 0.4924 | 0.507 | -0.041 ± 0.0065 | -0.0154 (26) |
| 3-5 | 3301 | 0.1935 | 0.1924 | +0.0010 ± 0.0006 | 0.5637 | 0.5604 | 0.5123 | 0.4727 | 0.4786 | -0.046 ± 0.0078 | 0.01 (5) |
| 5-10 | 7340 | 0.1973 | 0.194 | +0.0033 ± 0.0008 | 0.5794 | 0.5671 | 0.5081 | 0.4339 | 0.4514 | -0.039 ± 0.0052 | -0.0117 (6) |
| 10-15 | 6073 | 0.2038 | 0.1915 | +0.0123 ± 0.0014 | 0.5978 | 0.56 | 0.5094 | 0.3855 | 0.3986 | -0.052 ± 0.0057 | -0.0189 (18) |
| 15-25 | 8662 | 0.217 | 0.1801 | +0.0370 ± 0.0018 | 0.6313 | 0.5289 | 0.5252 | 0.3297 | 0.3351 | -0.063 ± 0.0046 | -0.014 (52) |
| 25-40 | 7848 | 0.2521 | 0.1379 | +0.1142 ± 0.0027 | 0.7113 | 0.4209 | 0.5614 | 0.244 | 0.2264 | -0.080 ± 0.0042 | -0.0095 (20) |
| 40+ | 6185 | 0.4024 | 0.0591 | +0.3433 ± 0.0036 | 1.0602 | 0.2126 | 0.6546 | 0.1185 | 0.08 | -0.074 ± 0.003 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1078 | 0.1966 | 0.1978 | -0.0012 ± 0.0005 | 0.5729 | 0.5757 | 0.5024 | 0.4869 | 0.5269 | -0.059 ± 0.0142 | -0.0191 (11) |
| 3-5 | 761 | 0.2075 | 0.2058 | +0.0017 ± 0.0013 | 0.6017 | 0.596 | 0.498 | 0.4584 | 0.4586 | -0.115 ± 0.0172 | 0.002 (5) |
| 5-10 | 1652 | 0.2043 | 0.2003 | +0.0039 ± 0.0017 | 0.5943 | 0.5832 | 0.5134 | 0.4397 | 0.4492 | -0.107 ± 0.0113 | -0.01 (10) |
| 10-15 | 1343 | 0.2124 | 0.2033 | +0.0091 ± 0.003 | 0.6149 | 0.5892 | 0.5388 | 0.4156 | 0.4423 | -0.108 ± 0.0124 | -0.0286 (7) |
| 15-25 | 1604 | 0.232 | 0.2125 | +0.0195 ± 0.0045 | 0.6617 | 0.6093 | 0.5857 | 0.3915 | 0.4383 | -0.110 ± 0.0116 | -0.03 (1) |
| 25-40 | 941 | 0.2171 | 0.21 | +0.0071 ± 0.0088 | 0.6242 | 0.6023 | 0.6585 | 0.3478 | 0.4899 | -0.060 ± 0.0137 | -0.0267 (3) |
| 40+ | 206 | 0.3107 | 0.1798 | +0.1309 ± 0.0266 | 0.8393 | 0.5322 | 0.7403 | 0.2852 | 0.3786 | -0.087 ± 0.0272 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5463 | 0.1858 | 0.1863 | -0.0005 ± 0.0002 | 0.5471 | 0.5476 | 0.4856 | 0.4702 | 0.486 | -0.036 ± 0.0059 | -0.0189 (44) |
| 3-5 | 3895 | 0.2041 | 0.2022 | +0.0019 ± 0.0006 | 0.5933 | 0.587 | 0.4806 | 0.4411 | 0.4375 | -0.058 ± 0.0073 | -0.0073 (22) |
| 5-10 | 8360 | 0.197 | 0.1916 | +0.0054 ± 0.0007 | 0.5777 | 0.5608 | 0.4871 | 0.4131 | 0.4134 | -0.057 ± 0.0048 | -0.0117 (42) |
| 10-15 | 6721 | 0.1951 | 0.18 | +0.0151 ± 0.0013 | 0.5752 | 0.5319 | 0.4962 | 0.3729 | 0.3732 | -0.062 ± 0.0052 | -0.0136 (14) |
| 15-25 | 8643 | 0.2123 | 0.1723 | +0.0400 ± 0.0017 | 0.6184 | 0.5084 | 0.512 | 0.3174 | 0.3129 | -0.072 ± 0.0045 | -0.0533 (3) |
| 25-40 | 6677 | 0.2183 | 0.1252 | +0.0930 ± 0.0027 | 0.6301 | 0.3851 | 0.5279 | 0.2123 | 0.2245 | -0.053 ± 0.0042 | -0.02 (4) |
| 40+ | 4484 | 0.3894 | 0.048 | +0.3414 ± 0.0037 | 1.015 | 0.1806 | 0.6379 | 0.1067 | 0.0636 | -0.076 ± 0.0031 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1524 | 0.1976 | 0.1974 | +0.0001 ± 0.0004 | 0.5737 | 0.5732 | 0.5098 | 0.4948 | 0.4961 | -0.072 ± 0.0116 | -0.0221 (56) |
| 3-5 | 1080 | 0.1894 | 0.1896 | -0.0002 ± 0.0011 | 0.5568 | 0.5557 | 0.4985 | 0.4586 | 0.4796 | -0.053 ± 0.0136 | -0.0194 (34) |
| 5-10 | 2181 | 0.2001 | 0.195 | +0.0051 ± 0.0014 | 0.5901 | 0.5734 | 0.5086 | 0.435 | 0.4374 | -0.079 ± 0.0097 | -0.005 (78) |
| 10-15 | 1506 | 0.2157 | 0.203 | +0.0127 ± 0.0029 | 0.6257 | 0.5897 | 0.5429 | 0.4202 | 0.4283 | -0.092 ± 0.0119 | 0.0012 (66) |
| 15-25 | 1966 | 0.2314 | 0.208 | +0.0234 ± 0.004 | 0.6601 | 0.6 | 0.592 | 0.3972 | 0.4359 | -0.090 ± 0.0104 | -0.0214 (59) |
| 25-40 | 1167 | 0.2424 | 0.2107 | +0.0317 ± 0.0082 | 0.6914 | 0.6044 | 0.6892 | 0.3772 | 0.4824 | -0.089 ± 0.0127 | -0.0252 (27) |
| 40+ | 424 | 0.3275 | 0.1983 | +0.1292 ± 0.0207 | 0.94 | 0.5789 | 0.8153 | 0.3392 | 0.4575 | -0.099 ± 0.0193 | -0.1137 (8) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5536 | 0.1779 | 0.178 | -0.0001 ± 0.0002 | 0.5262 | 0.5259 | 0.5119 | 0.4967 | 0.5056 | -0.040 ± 0.0057 | -0.0154 (103) |
| 3-5 | 3820 | 0.1954 | 0.1947 | +0.0007 ± 0.0006 | 0.57 | 0.5677 | 0.5022 | 0.4624 | 0.4733 | -0.039 ± 0.0072 | -0.0212 (73) |
| 5-10 | 7749 | 0.1978 | 0.1911 | +0.0067 ± 0.0007 | 0.5832 | 0.5626 | 0.5023 | 0.4289 | 0.421 | -0.064 ± 0.005 | -0.0084 (134) |
| 10-15 | 5316 | 0.2105 | 0.1942 | +0.0163 ± 0.0015 | 0.6128 | 0.5693 | 0.5365 | 0.4136 | 0.4071 | -0.073 ± 0.0061 | -0.0057 (111) |
| 15-25 | 6506 | 0.2318 | 0.1995 | +0.0324 ± 0.0022 | 0.6658 | 0.5781 | 0.5762 | 0.3809 | 0.3962 | -0.070 ± 0.0056 | -0.026 (108) |
| 25-40 | 4218 | 0.2591 | 0.1906 | +0.0686 ± 0.0042 | 0.7319 | 0.5548 | 0.6407 | 0.3281 | 0.3777 | -0.067 ± 0.0066 | -0.0277 (53) |
| 40+ | 1902 | 0.3708 | 0.1581 | +0.2126 ± 0.0094 | 1.0451 | 0.4718 | 0.7442 | 0.2442 | 0.2918 | -0.064 ± 0.0087 | -0.054 (15) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 7585 | 1.016 ± 0.032 | 1.095 | 0.1678 | 0.1676 | 0.2164 | 0.2042 |
| gen2 | 7585 | 0.812 ± 0.029 | 1.067 | 0.1733 | 0.1679 | 0.2344 | 0.2041 |
| gen1_elo | 7585 | 1.002 ± 0.031 | 1.084 | 0.174 | 0.1677 | 0.2153 | 0.2043 |
| gen1_sr | 7585 | 0.995 ± 0.038 | 1.117 | 0.1332 | 0.1695 | 0.2304 | 0.2038 |
| gen1_ledger | 9848 | 0.862 ± 0.024 | 1.071 | 0.1893 | 0.1749 | 0.2177 | 0.2006 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 35,445)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 8,494 | 24.0% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 8,099 | 22.9% |
| BOOK_QUALITY | execution | 6,158 | 17.4% |
| POOR_DATA | data | 4,083 | 11.5% |
| LIMITED_DATA | data | 2,161 | 6.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 2,035 | 5.7% |
| IDENTITY_AMBIGUOUS | mapping | 1,463 | 4.1% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,397 | 3.9% |
| IN_PLAY_QUOTE | market_freshness/coverage | 986 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 568 | 1.6% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 24.0%, coverage 22.9%, data 17.6%, execution 17.4%, market_freshness/coverage 8.5%, mapping 4.1%, model_calibration_or_unknown 3.9%, model_calibration 1.6%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.6%, START_UNVERIFIABLE 94.8%, LOW_DATA_QUALITY 71.7%, THIN_PLAYER_HISTORY 59.9%, STALE_PLAYER_DATA 52.3%, STALE_KALSHI_QUOTE 47.2%, MODEL_INTERNAL_DISAGREEMENT 42.0%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 23.8%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 15.2%, LEVEL_TRANSFER_RISK 9.7%, LOW_DISPLAYED_LIQUIDITY 8.4%, EVENT_MAPPING_RISK 7.0%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.2%, POST_SETTLEMENT_OBSERVATION 22.9%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 18,918)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,522 | 34.5% |
| STALE_QUOTE | market_freshness | 3,802 | 20.1% |
| BOOK_QUALITY | execution | 3,189 | 16.9% |
| POOR_DATA | data | 1,736 | 9.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,091 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 818 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 645 | 3.4% |
| LIMITED_DATA | data | 633 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 343 | 1.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 138 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.5%, market_freshness 20.1%, execution 16.9%, data 12.5%, market_freshness/coverage 9.2%, mapping 4.3%, model_calibration_or_unknown 1.8%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.1%, START_UNVERIFIABLE 97.2%, LOW_DATA_QUALITY 74.9%, THIN_PLAYER_HISTORY 62.0%, STALE_KALSHI_QUOTE 54.7%, STALE_PLAYER_DATA 46.0%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 23.1%, MODEL_HIGH_UNCERTAINTY 19.2%, PLAYER_IDENTITY_RISK 18.2%, EVENT_MAPPING_RISK 8.6%, LEVEL_TRANSFER_RISK 8.6%, LOW_DISPLAYED_LIQUIDITY 8.3%, MODEL_CALIBRATION_OUTLIER 4.7%, EXTERNAL_MARKET_REJECTION 1.8%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.4%, POST_SETTLEMENT_OBSERVATION 34.5%, POSSIBLE_IN_PLAY_QUOTE 6.2%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 15142, "IDENTITY_AMBIGUOUS": 3776}; ticker orientation: {"VERIFIED": 18918}.

Checks: discipline:AMBIGUOUS 1231, discipline:PASS 17687, identity_confidence:AMBIGUOUS 3436, identity_confidence:PASS 15482, level_mapping:NA 1243, level_mapping:PASS 17675, market_pair:AMBIGUOUS 502, market_pair:NA 414, market_pair:PASS 18002, model_complement:NA 376, model_complement:PASS 18542, namesake:AMBIGUOUS 6, namesake:PASS 18912, physical_match_id:NA 6371, physical_match_id:PASS 12547, player_ids:PASS 18918, same_pair_other_event:PASS 18918, ticker_orientation:PASS 18918

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,529 | 3.8% | 3.1% | 1.3% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 24, "market_freshness/coverage": 22} | 5.5 | 0.2221 / 0.2177 (849) | 25.5% | 2.4% | 3.1% | 3.0% |
| CHALLENGER | 12,882 | 16.3% | 6.0% | 11.1% | {"coverage": 1271, "market_freshness": 258, "market_freshness/coverage": 233, "data": 164, "model_calibration_or_unknown": 81, "execution": 41, "model_calibration": 39, "mapping": 17, "possible_market_error": 1} | 7.35 | 0.2203 / 0.2092 (2969) | 40.7% | 14.1% | 4.0% | 22.4% |
| DOUBLES | 2,661 | 46.3% | 46.2% | 6.5% | {"execution": 681, "mapping": 366, "market_freshness": 106, "market_freshness/coverage": 71, "coverage": 7} | 23.12 | 0.2994 / 0.2322 (656) | 8.8% | 0.0% | 100.0% | 6.3% |
| ITF_MEN | 24,820 | 25.3% | 17.9% | 33.2% | {"coverage": 2174, "market_freshness": 1301, "execution": 1019, "data": 940, "market_freshness/coverage": 621, "mapping": 223, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.79 | 0.2198 / 0.2006 (5181) | 41.0% | 69.7% | 15.1% | 21.2% |
| ITF_WOMEN | 31,947 | 26.5% | 18.9% | 44.7% | {"coverage": 2991, "market_freshness": 1876, "execution": 1365, "data": 1164, "market_freshness/coverage": 732, "mapping": 206, "model_calibration_or_unknown": 95, "model_calibration": 23} | 12.48 | 0.2038 / 0.1943 (6162) | 42.0% | 57.2% | 9.9% | 21.7% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,891 | 5.9% | 5.1% | 1.5% | {"market_freshness": 111, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.65 | 0.2307 / 0.2205 (804) | 30.2% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.6% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 523 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 638 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 725 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 852 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.5h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 517 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFMATCH-26NOV10KOUPOR-POR` | ITF_MEN | fair_v1 | 87% / 2% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.9h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 305 min (STALE); data POOR (grade D, thinner serve sample 1554.0, ratio 1.02); no external reference |
| 12 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 13 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 15 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 20.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 1203 min (STALE); no external reference |
| 16 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 17 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 18 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 19 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 15.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 928 min (STALE); no external reference |
| 20 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 21 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 22 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 23 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 24 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 25 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 26 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 454 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 27 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 28 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 29 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 30 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 31 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 32 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 33 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 34 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 35 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 271 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 36 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 37 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 38 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 39 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 40 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 41 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 43 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 44 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 45 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 46 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 47 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 48 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 49 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 720 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 50 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9717, "by_level_share_of_ge_25pp": {"ATP": 0.013, "CHALLENGER": 0.1113, "DOUBLES": 0.0651, "ITF_MEN": 0.3324, "ITF_WOMEN": 0.4468, "OTHER": 0.0006, "WTA": 0.0154, "WTA125": 0.0155}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5467, "share_primary_cause_market_settled_or_in_play": 0.4366, "share_primary_cause_stale_quote_only": 0.201}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 18918, "identity_ambiguous_share": 0.1996, "ticker_orientation": {"VERIFIED": 18918}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 12547, "with_external": 629, "coverage": 0.0501, "external_status": {"EXTERNAL_STALE": 398, "AGREES_WITH_KALSHI": 218, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 398, "MODEL_LONE_OUTLIER": 218, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3466, "share_external_supports_model": 0.0207}, "pregame_clean_ge_25pp": {"n": 5840, "with_external": 598, "coverage": 0.1024, "external_status": {"EXTERNAL_STALE": 374, "AGREES_WITH_KALSHI": 211, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 374, "MODEL_LONE_OUTLIER": 211, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3528, "share_external_supports_model": 0.0217}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 480.0, "median_sample_ratio": 2.44, "median_min_matches": 18.0, "median_max_days_since_last": 244.0, "share_severe_asymmetry": 0.208, "data_status": {"POOR": 10685, "LIMITED": 4817, "ADEQUATE": 3416}, "comparison_lt_10pp": {"median_thinner_serve_points": 1722.0, "median_sample_ratio": 1.7, "median_min_matches": 89.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1528, "model_minus_observed": 0.0695, "kalshi_minus_observed": -0.0693, "brier_diff_model_minus_kalshi": 0.0037}, "4-10x": {"n": 1036, "model_minus_observed": 0.091, "kalshi_minus_observed": -0.0542, "brier_diff_model_minus_kalshi": 0.0101}, "<2x": {"n": 3748, "model_minus_observed": 0.1, "kalshi_minus_observed": -0.0225, "brier_diff_model_minus_kalshi": 0.0147}, ">=10x": {"n": 1273, "model_minus_observed": 0.1232, "kalshi_minus_observed": -0.0493, "brier_diff_model_minus_kalshi": 0.017}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 7585, "model": {"intercept": -0.559, "slope": 0.812, "slope_se": 0.029}, "kalshi_mid_same_rows": {"intercept": 0.167, "slope": 1.067, "slope_se": 0.033}, "mean_extremity_model": 0.1733, "mean_extremity_kalshi": 0.1679, "model_brier": 0.2344, "kalshi_brier": 0.2041, "brier_diff_model_minus_kalshi": 0.0303, "brier_diff_se": 0.0022, "model_logloss": 0.6667, "kalshi_logloss": 0.5906}, "fair_v1": {"n": 7585, "model": {"intercept": -0.456, "slope": 1.016, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.229, "slope": 1.095, "slope_se": 0.033}, "mean_extremity_model": 0.1678, "mean_extremity_kalshi": 0.1676, "model_brier": 0.2164, "kalshi_brier": 0.2042, "brier_diff_model_minus_kalshi": 0.0122, "brier_diff_se": 0.0018, "model_logloss": 0.6222, "kalshi_logloss": 0.5907}, "gen1_elo": {"n": 7585, "model": {"intercept": -0.446, "slope": 1.002, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.229, "slope": 1.084, "slope_se": 0.032}, "mean_extremity_model": 0.174, "mean_extremity_kalshi": 0.1677, "model_brier": 0.2153, "kalshi_brier": 0.2043, "brier_diff_model_minus_kalshi": 0.011, "brier_diff_se": 0.0018, "model_logloss": 0.6202, "kalshi_logloss": 0.591}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2506, "share_ge_15": 0.4461, "median_abs_gap": 13.08, "n": 50071}, "gen1_elo": {"share_ge_25": 0.2477, "share_ge_15": 0.4418, "median_abs_gap": 12.9, "n": 50071}, "gen1_sr": {"share_ge_25": 0.3141, "share_ge_15": 0.5216, "median_abs_gap": 15.87, "n": 50071}, "gen2": {"share_ge_25": 0.3149, "share_ge_15": 0.5109, "median_abs_gap": 15.47, "n": 50071}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1518, "share_ge_15": 0.3544, "median_abs_gap": 10.68, "n": 38465}, "gen1_elo": {"share_ge_25": 0.1498, "share_ge_15": 0.349, "median_abs_gap": 10.49, "n": 38465}, "gen1_sr": {"share_ge_25": 0.2159, "share_ge_15": 0.4392, "median_abs_gap": 12.97, "n": 38467}, "gen2": {"share_ge_25": 0.2308, "share_ge_15": 0.4385, "median_abs_gap": 12.83, "n": 38467}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.5, "share_ge_25_all": 0.0375, "share_ge_25_pregame_clean": 0.0314}, "WTA": {"median_abs_gap_pregame_clean": 7.65, "share_ge_25_all": 0.0595, "share_ge_25_pregame_clean": 0.0505}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2361, "share_within_10pp_all": 0.4381, "share_within_10pp_pregame_clean": 0.4915, "corr_model_vs_mid_pregame_clean": 0.8491}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1099, "model_brier": 0.1976, "kalshi_brier": 0.1978, "brier_diff_model_minus_kalshi": -0.0003}, "10-15": {"n_settled": 1318, "model_brier": 0.2187, "kalshi_brier": 0.2091, "brier_diff_model_minus_kalshi": 0.0096}, "15-25": {"n_settled": 1682, "model_brier": 0.2269, "kalshi_brier": 0.2081, "brier_diff_model_minus_kalshi": 0.0188}, "25-40": {"n_settled": 960, "model_brier": 0.2263, "kalshi_brier": 0.2051, "brier_diff_model_minus_kalshi": 0.0211}, "3-5": {"n_settled": 697, "model_brier": 0.2063, "kalshi_brier": 0.2058, "brier_diff_model_minus_kalshi": 0.0005}, "40+": {"n_settled": 196, "model_brier": 0.3016, "kalshi_brier": 0.1723, "brier_diff_model_minus_kalshi": 0.1293}, "5-10": {"n_settled": 1633, "model_brier": 0.2045, "kalshi_brier": 0.2029, "brier_diff_model_minus_kalshi": 0.0016}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.559, "slope": 0.812, "slope_se": 0.029}, "kalshi_slope": {"intercept": 0.167, "slope": 1.067, "slope_se": 0.033}, "n": 7585}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.492, "slope": 0.862, "slope_se": 0.024}, "kalshi_slope": {"intercept": 0.16, "slope": 1.071, "slope_se": 0.028}, "n": 9848}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 656, "model_brier": 0.2994, "kalshi_brier": 0.2322, "brier_diff_model_minus_kalshi": 0.0672, "brier_diff_se": 0.0115, "corr_model_outcome": 0.0991, "corr_kalshi_outcome": 0.2803}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
