# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-30T15:06Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 70,261): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 19.0%, 25-40 13.8%, 40+ 8.0%; median gap 11.85 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.9%, Challenger 10.8%, doubles 6.6%). Main tour: ATP 4.1% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 15,322): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.1%, STALE_QUOTE 18.8%, BOOK_QUALITY 18.3%, POOR_DATA 9.4%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IDENTITY_AMBIGUOUS 4.1%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.1%, market_freshness 18.8%, execution 18.3%, data 12.8%, market_freshness/coverage 9.1%, mapping 4.1%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.4% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.2% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 15,322 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.1% of the time and with the model 1.1%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 475.5 points vs 1695.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.015, Gen-2 0.804, Gen-1 ledger 0.855 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 745 model 0.2225 vs Kalshi 0.2057; n 155 model 0.2842 vs Kalshi 0.1885.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 298,652 model-market comparisons (488,154 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 100,283 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-30T14:49:08.965476+00:00'], shadow board 80,279 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-30T14:49:12.889537+00:00'], Model 4 37,163 rows, 24,155 settled tickers, 8,874 tickers with an external scan.
* By model: {"gen1_ledger": 67504, "gen1_elo": 40349, "fair_v1": 40349, "gen2": 40349, "gen1_sr": 40349, "model4_fundamental": 34898, "model4_conditioned": 34854}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 70,261 | 14.1 | 9.6 | 20.2 | 15.3 | 19.0 | 13.8 | 8.0 | 11.85 | 40.8% | 21.8% |
| MW fair_v1 | 40,349 | 12.9 | 8.7 | 18.7 | 15.4 | 19.5 | 14.9 | 9.9 | 13.01 | 44.3% | 24.8% |
| MW gen1_elo | 40,349 | 12.5 | 8.6 | 19.4 | 15.4 | 19.5 | 14.8 | 9.8 | 12.93 | 44.1% | 24.6% |
| MW gen1_ledger | 29,912 | 15.6 | 10.8 | 22.2 | 15.3 | 18.4 | 12.3 | 5.5 | 10.35 | 36.2% | 17.8% |
| MW gen1_sr | 40,349 | 10.2 | 7.2 | 16.9 | 13.8 | 20.7 | 18.6 | 12.7 | 15.85 | 52.0% | 31.3% |
| MW gen2 | 40,349 | 11.1 | 7.6 | 16.6 | 13.8 | 19.3 | 17.8 | 13.8 | 15.44 | 50.9% | 31.6% |
| all families model4_conditioned | 34,854 | 22.5 | 18.3 | 34.1 | 17.1 | 4.9 | 1.9 | 1.1 | 5.98 | 8.0% | 3.1% |
| all families model4_fundamental | 34,898 | 17.4 | 13.4 | 33.9 | 20.2 | 10.1 | 3.6 | 1.4 | 7.65 | 15.2% | 5.0% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.2%, >=15pp 40.8%, >=20pp 30.2%, >=25pp 21.8%, >=30pp 15.7%, >=40pp 8.0%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.3pp; >=10pp 44.8%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,451 | 27.3 | 15.4 | 27.8 | 13.4 | 11.5 | 4.0 | 0.6 | 5.92 | 16.1% | 4.6% |
| CHALLENGER | 5,989 | 16.2 | 9.8 | 20.9 | 15.1 | 15.4 | 11.7 | 10.9 | 10.91 | 38.0% | 22.6% |
| ITF_MEN | 11,347 | 9.8 | 7.4 | 17.0 | 15.1 | 21.2 | 17.5 | 11.9 | 15.22 | 50.7% | 29.5% |
| ITF_WOMEN | 15,910 | 9.7 | 7.1 | 15.9 | 15.1 | 22.0 | 18.1 | 12.1 | 15.66 | 52.2% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,514 | 18.3 | 13.7 | 24.9 | 19.9 | 16.0 | 6.3 | 1.0 | 8.2 | 23.3% | 7.3% |
| WTA125 | 1,132 | 16.5 | 7.3 | 22.4 | 19.0 | 21.0 | 11.9 | 1.9 | 10.73 | 34.8% | 13.8% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,451 | 26.0 | 15.4 | 25.9 | 16.1 | 11.8 | 4.1 | 0.8 | 6.22 | 16.6% | 4.8% |
| CHALLENGER | 5,989 | 15.1 | 9.0 | 18.3 | 14.2 | 18.1 | 13.5 | 11.7 | 12.5 | 43.3% | 25.3% |
| ITF_MEN | 11,347 | 8.0 | 6.2 | 15.1 | 13.8 | 19.5 | 20.7 | 16.6 | 17.94 | 56.8% | 37.3% |
| ITF_WOMEN | 15,910 | 8.0 | 5.8 | 14.0 | 12.8 | 20.6 | 21.1 | 17.6 | 19.08 | 59.3% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,514 | 15.3 | 10.9 | 22.3 | 15.2 | 21.9 | 12.6 | 1.9 | 10.59 | 36.4% | 14.4% |
| WTA125 | 1,132 | 9.9 | 6.6 | 17.0 | 15.8 | 24.1 | 17.8 | 8.8 | 15.21 | 50.7% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,451 | 22.1 | 13.3 | 24.5 | 16.0 | 16.1 | 6.6 | 1.3 | 7.59 | 24.1% | 7.9% |
| CHALLENGER | 5,989 | 15.0 | 9.3 | 20.9 | 16.1 | 15.6 | 12.1 | 11.1 | 11.34 | 38.8% | 23.2% |
| ITF_MEN | 11,347 | 9.3 | 7.1 | 17.5 | 14.3 | 21.8 | 17.7 | 12.3 | 15.69 | 51.9% | 30.0% |
| ITF_WOMEN | 15,910 | 9.4 | 6.9 | 16.4 | 15.8 | 22.1 | 17.9 | 11.5 | 15.49 | 51.5% | 29.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,514 | 23.6 | 16.6 | 32.2 | 14.3 | 9.1 | 3.0 | 1.3 | 6.07 | 13.3% | 4.3% |
| WTA125 | 1,132 | 21.6 | 12.9 | 26.8 | 17.6 | 15.0 | 5.8 | 0.3 | 8.0 | 21.2% | 6.2% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,027 | 24.5 | 19.2 | 31.1 | 12.7 | 9.1 | 2.9 | 0.5 | 5.73 | 12.5% | 3.4% |
| CHALLENGER | 4,051 | 22.5 | 14.6 | 27.4 | 14.5 | 13.5 | 5.9 | 1.6 | 7.08 | 21.0% | 7.5% |
| DOUBLES | 2,159 | 5.0 | 4.3 | 12.2 | 10.7 | 21.1 | 25.0 | 21.7 | 23.6 | 67.8% | 46.7% |
| ITF_MEN | 8,598 | 13.0 | 9.4 | 21.2 | 15.9 | 21.4 | 13.3 | 5.8 | 11.89 | 40.5% | 19.1% |
| ITF_WOMEN | 10,270 | 13.1 | 9.1 | 19.9 | 15.8 | 21.2 | 15.3 | 5.5 | 12.32 | 42.0% | 20.8% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,512 | 24.5 | 15.5 | 30.6 | 17.4 | 9.1 | 2.7 | 0.3 | 6.68 | 12.0% | 3.0% |
| WTA125 | 1,146 | 25.1 | 12.7 | 20.9 | 19.5 | 13.4 | 6.9 | 1.6 | 7.89 | 21.9% | 8.5% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,352 | 27.7 | 15.6 | 28.1 | 13.4 | 11.2 | 3.6 | 0.4 | 5.88 | 15.2% | 4.0% |
| CHALLENGER | 4,194 | 21.2 | 12.3 | 26.0 | 17.6 | 15.3 | 6.1 | 1.6 | 8.03 | 22.9% | 7.6% |
| ITF_MEN | 8,302 | 11.9 | 8.8 | 20.5 | 17.2 | 22.1 | 14.3 | 5.1 | 12.39 | 41.5% | 19.4% |
| ITF_WOMEN | 11,812 | 11.6 | 8.5 | 18.5 | 17.3 | 23.9 | 15.0 | 5.2 | 13.26 | 44.1% | 20.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,432 | 18.6 | 13.7 | 25.1 | 20.1 | 16.1 | 5.8 | 0.6 | 8.14 | 22.5% | 6.4% |
| WTA125 | 1,096 | 16.8 | 7.2 | 21.9 | 19.2 | 21.5 | 11.7 | 1.6 | 10.97 | 34.8% | 13.3% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,352 | 26.2 | 15.7 | 26.1 | 16.0 | 11.8 | 3.7 | 0.5 | 6.19 | 15.9% | 4.2% |
| CHALLENGER | 4,194 | 19.3 | 11.5 | 23.0 | 16.7 | 18.5 | 9.0 | 2.0 | 8.99 | 29.5% | 11.0% |
| ITF_MEN | 8,303 | 9.4 | 7.3 | 17.5 | 16.1 | 21.3 | 18.8 | 9.5 | 14.91 | 49.7% | 28.3% |
| ITF_WOMEN | 11,813 | 8.9 | 6.8 | 15.9 | 14.3 | 22.7 | 20.6 | 10.8 | 16.54 | 54.0% | 31.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,432 | 15.5 | 11.0 | 22.4 | 15.3 | 22.1 | 12.5 | 1.2 | 10.38 | 35.8% | 13.7% |
| WTA125 | 1,096 | 9.9 | 6.7 | 17.1 | 16.0 | 24.0 | 18.1 | 8.3 | 15.12 | 50.4% | 26.4% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,972 | 24.6 | 19.5 | 31.1 | 12.8 | 8.8 | 2.8 | 0.4 | 5.67 | 12.0% | 3.2% |
| CHALLENGER | 3,572 | 23.9 | 15.6 | 28.6 | 14.6 | 12.8 | 4.0 | 0.5 | 6.59 | 17.2% | 4.5% |
| DOUBLES | 2,024 | 4.9 | 4.5 | 12.4 | 10.8 | 20.9 | 24.9 | 21.6 | 23.54 | 67.4% | 46.5% |
| ITF_MEN | 7,342 | 13.8 | 10.0 | 22.9 | 16.5 | 21.3 | 11.7 | 3.8 | 10.92 | 36.8% | 15.5% |
| ITF_WOMEN | 8,752 | 13.8 | 9.6 | 21.1 | 16.4 | 21.3 | 14.3 | 3.5 | 11.5 | 39.1% | 17.8% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,458 | 24.8 | 15.8 | 30.7 | 17.4 | 9.1 | 2.1 | 0.1 | 6.48 | 11.2% | 2.2% |
| WTA125 | 1,019 | 26.4 | 13.4 | 21.9 | 20.6 | 12.4 | 4.8 | 0.5 | 7.35 | 17.7% | 5.3% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,159 | 5.0 | 4.3 | 12.2 | 10.7 | 21.1 | 25.0 | 21.7 | 23.6 | 67.8% | 46.7% |
| singles | 27,753 | 16.4 | 11.2 | 22.9 | 15.6 | 18.2 | 11.3 | 4.2 | 9.83 | 33.7% | 15.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,996 | 13.1 | 9.3 | 20.2 | 15.7 | 19.0 | 13.7 | 8.9 | 12.28 | 41.6% | 22.6% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 26,480 | 13.4 | 8.7 | 18.6 | 15.1 | 19.2 | 15.0 | 10.0 | 12.96 | 44.2% | 25.0% |
| UNKNOWN | 5,624 | 10.3 | 7.8 | 17.0 | 16.4 | 21.4 | 16.0 | 11.1 | 14.27 | 48.4% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 11,205 | 20.0 | 12.1 | 22.4 | 15.6 | 14.7 | 9.1 | 6.1 | 8.52 | 29.9% | 15.2% |
| B | 5,009 | 12.9 | 9.0 | 19.4 | 15.8 | 19.4 | 12.6 | 11.0 | 12.54 | 42.9% | 23.6% |
| C | 5,783 | 11.8 | 8.9 | 19.9 | 15.8 | 18.5 | 14.3 | 10.7 | 12.84 | 43.6% | 25.0% |
| D | 6,386 | 11.9 | 8.3 | 17.5 | 15.3 | 21.6 | 16.0 | 9.4 | 13.84 | 47.0% | 25.4% |
| F | 11,966 | 7.3 | 5.6 | 15.1 | 14.8 | 23.4 | 20.9 | 13.0 | 17.65 | 57.2% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,969 | 24.2 | 15.8 | 29.0 | 15.2 | 10.9 | 3.6 | 1.3 | 6.51 | 15.9% | 4.9% |
| B | 4,264 | 16.9 | 10.7 | 24.1 | 16.8 | 18.8 | 9.6 | 3.1 | 9.63 | 31.5% | 12.7% |
| C | 5,856 | 11.3 | 7.9 | 19.4 | 14.6 | 21.0 | 15.7 | 10.1 | 13.48 | 46.8% | 25.8% |
| D | 4,380 | 14.4 | 9.8 | 21.8 | 15.4 | 20.0 | 13.3 | 5.4 | 11.25 | 38.7% | 18.6% |
| F | 7,443 | 9.8 | 8.3 | 16.1 | 15.0 | 23.2 | 19.9 | 7.7 | 15.42 | 50.8% | 27.6% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 12,685 | 18.3 | 11.0 | 21.5 | 15.4 | 15.1 | 9.9 | 8.9 | 9.74 | 33.9% | 18.8% |
| LIMITED | 8,939 | 13.7 | 10.0 | 20.4 | 16.1 | 19.1 | 13.2 | 7.6 | 11.7 | 39.8% | 20.7% |
| POOR | 18,725 | 8.9 | 6.6 | 16.0 | 15.0 | 22.7 | 19.0 | 11.8 | 16.15 | 53.5% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,675 | 24.3 | 18.2 | 33.0 | 14.8 | 6.5 | 2.7 | 0.4 | 5.81 | 9.6% | 3.1% |
| GAME_SPREAD | 6,004 | 22.3 | 15.2 | 32.8 | 17.1 | 9.0 | 2.9 | 0.6 | 6.73 | 12.5% | 3.5% |
| MATCH_WINNER | 29,912 | 15.6 | 10.8 | 22.2 | 15.3 | 18.4 | 12.3 | 5.5 | 10.35 | 36.2% | 17.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 13,902 | 27.6 | 16.6 | 31.0 | 12.5 | 9.4 | 2.5 | 0.3 | 5.67 | 12.2% | 2.8% |
| TOTAL_GAMES | 9,987 | 9.9 | 10.6 | 35.7 | 26.6 | 10.4 | 4.0 | 2.8 | 9.25 | 17.2% | 6.8% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,319 | 24.6 | 30.1 | 32.8 | 7.3 | 4.1 | 0.9 | 0.3 | 4.7 | 5.2% | 1.1% |
| GAME_SPREAD | 8,158 | 47.5 | 16.1 | 25.1 | 7.2 | 2.2 | 1.3 | 0.6 | 3.24 | 4.1% | 1.9% |
| TOTAL_GAMES | 14,377 | 6.6 | 9.5 | 40.2 | 31.2 | 7.2 | 3.2 | 2.2 | 9.28 | 12.6% | 5.4% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,330 | 24.0 | 16.8 | 34.9 | 14.2 | 7.1 | 2.6 | 0.4 | 5.99 | 10.1% | 3.0% |
| GAME_SPREAD | 8,161 | 20.2 | 13.6 | 28.1 | 20.4 | 12.3 | 4.2 | 1.1 | 7.75 | 17.7% | 5.3% |
| TOTAL_GAMES | 14,407 | 10.2 | 10.3 | 36.3 | 25.2 | 11.5 | 4.2 | 2.4 | 9.16 | 18.1% | 6.6% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 40,349 | 44.3% | 24.8% | 13.01 | 35.5% | 15.2% | 10.71 |
| gen1_elo | 40,349 | 44.1% | 24.6% | 12.93 | 35.2% | 15.2% | 10.53 |
| gen1_sr | 40,349 | 52.0% | 31.3% | 15.85 | 44.0% | 21.7% | 13.0 |
| gen2 | 40,349 | 50.9% | 31.6% | 15.44 | 43.9% | 23.3% | 12.86 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 18,643 | 15.6 | 10.6 | 21.3 | 17.2 | 20.1 | 12.0 | 3.3 | 10.71 | 35.4% | 15.3% |
| STALE | 21,706 | 10.6 | 7.1 | 16.5 | 13.8 | 19.0 | 17.3 | 15.6 | 15.76 | 51.9% | 33.0% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 23,380 | 16.3 | 11.1 | 22.9 | 15.4 | 17.9 | 11.8 | 4.7 | 9.94 | 34.3% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 70,261 | 23380 | 22115 | 24766 | 24.4 | 124.9 | 1451.1 |
| ge_15pp | 28,698 | 8029 | 7884 | 12785 | 26.9 | 435.4 | 1451.1 |
| ge_25pp | 15,322 | 3855 | 3443 | 8024 | 32.1 | 585.8 | 1431.1 |
| lt_10pp | 30,795 | 11746 | 10480 | 8569 | 22.4 | 47.0 | 1421.1 |

Current slate `SL-20261030T150619Z-101c8e24`: 326 priced rows, quote age at build {'median': 17.6, 'max': 17.6}, freshness {'AGING': 326}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 45 | 0.0 | 0.0 | 31.1 | 6.7 | 35.6 | 22.2 | 4.4 | 20.19 | 62.2% | 26.7% |
| EXTERNAL_LONE_OUTLIER | 25 | 64.0 | 36.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.43 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,007 | 19.8 | 11.1 | 25.4 | 17.8 | 17.8 | 7.1 | 0.9 | 8.53 | 25.9% | 8.0% |
| KALSHI_LONE_OUTLIER | 27 | 3.7 | 3.7 | 77.8 | 7.4 | 3.7 | 3.7 | 0.0 | 6.42 | 7.4% | 3.7% |
| MARKETS_AGREE | 793 | 65.5 | 34.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.21 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,727 | 0.0 | 2.4 | 36.5 | 25.3 | 24.9 | 9.9 | 0.9 | 11.99 | 35.7% | 10.8% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 40,349 | 6624 (16.4%) | 26.1% | 1.1% | {"EXTERNAL_STALE": 4007, "AGREES_WITH_KALSHI": 1727, "ALL_AGREE": 793, "SUPPORTS_MODEL_DIRECTION": 44, "AGREES_WITH_MODEL": 27, "EXTERNAL_OUTLIER": 25, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 17,870 | 1684 (9.4%) | 36.6% | 1.8% | {"EXTERNAL_STALE": 1037, "AGREES_WITH_KALSHI": 617, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 10,005 | 522 (5.2%) | 35.8% | 2.5% | {"EXTERNAL_STALE": 322, "AGREES_WITH_KALSHI": 187, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,753 | 495 (10.4%) | 36.4% | 2.6% | {"EXTERNAL_STALE": 302, "AGREES_WITH_KALSHI": 180, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 16,280 | 3783 (23.2%) | 17.8% | 0.9% | {"EXTERNAL_STALE": 2255, "ALL_AGREE": 793, "AGREES_WITH_KALSHI": 673, "EXTERNAL_OUTLIER": 25, "AGREES_WITH_MODEL": 23, "SUPPORTS_MODEL_DIRECTION": 13, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 7,876 | 10.5 | 7.5 | 19.5 | 14.4 | 21.5 | 16.5 | 10.0 | 14.09 | 48.0% | 26.5% |
| 4-10x | 5,450 | 11.0 | 8.5 | 18.7 | 15.5 | 21.9 | 14.3 | 9.9 | 13.63 | 46.2% | 24.3% |
| <2x | 20,469 | 15.2 | 10.0 | 19.6 | 16.0 | 17.4 | 13.0 | 9.0 | 11.55 | 39.4% | 22.0% |
| >=10x | 6,554 | 10.4 | 6.4 | 15.1 | 14.5 | 21.7 | 19.2 | 12.8 | 16.35 | 53.7% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 10,459 | 12.8 | 8.9 | 19.6 | 15.9 | 19.0 | 13.4 | 10.4 | 12.66 | 42.8% | 23.8% |
| 300-1000 | 8,724 | 11.9 | 8.7 | 17.8 | 15.3 | 20.2 | 16.4 | 9.6 | 13.59 | 46.2% | 25.9% |
| <300 | 12,934 | 8.2 | 5.8 | 15.2 | 14.8 | 23.1 | 20.0 | 12.9 | 17.07 | 56.0% | 32.9% |
| >=3000 | 8,232 | 21.5 | 13.0 | 24.1 | 15.6 | 13.7 | 7.1 | 5.0 | 7.57 | 25.8% | 12.1% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1158 | 0.5497 | 0.4105 | 0.4974 | +0.052 | -0.087 | -0.0021 ± 0.0045 |
| ratio 4-10x | 803 | 0.581 | 0.4342 | 0.4944 | +0.087 | -0.060 | 0.0077 ± 0.0056 |
| ratio <2x | 2778 | 0.5382 | 0.415 | 0.4471 | +0.091 | -0.032 | 0.0123 ± 0.0027 |
| ratio >=10x | 994 | 0.5685 | 0.3941 | 0.4527 | +0.116 | -0.059 | 0.0134 ± 0.0058 |
| thinner_sample 1000-3000 | 1565 | 0.5404 | 0.4133 | 0.4518 | +0.089 | -0.038 | 0.0096 ± 0.0037 |
| thinner_sample 300-1000 | 1308 | 0.5681 | 0.4259 | 0.4862 | +0.082 | -0.060 | 0.0026 ± 0.0044 |
| thinner_sample <300 | 1913 | 0.5597 | 0.3921 | 0.4611 | +0.099 | -0.069 | 0.0109 ± 0.0041 |
| thinner_sample >=3000 | 947 | 0.5318 | 0.4379 | 0.4646 | +0.067 | -0.027 | 0.0127 ± 0.0037 |
| data_status ADEQUATE | 1556 | 0.5344 | 0.4315 | 0.4505 | +0.084 | -0.019 | 0.013 ± 0.0031 |
| data_status LIMITED | 1402 | 0.5499 | 0.4166 | 0.4743 | +0.076 | -0.058 | 0.0062 ± 0.004 |
| data_status POOR | 2775 | 0.5624 | 0.4011 | 0.4681 | +0.094 | -0.067 | 0.0081 ± 0.0033 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 830 | 0.1995 | 0.1999 | -0.0004 ± 0.0005 | 0.5787 | 0.5798 | 0.5042 | 0.489 | 0.5084 | -0.089 ± 0.0165 | -0.01 (5) |
| 3-5 | 526 | 0.2052 | 0.2056 | -0.0004 ± 0.0016 | 0.5929 | 0.5926 | 0.5042 | 0.4643 | 0.4886 | -0.095 ± 0.0202 | 0.02 (1) |
| 5-10 | 1207 | 0.2015 | 0.2019 | -0.0004 ± 0.0019 | 0.5892 | 0.5875 | 0.5107 | 0.4369 | 0.4739 | -0.086 ± 0.0134 | -0.0167 (6) |
| 10-15 | 1002 | 0.2202 | 0.2118 | +0.0084 ± 0.0036 | 0.6328 | 0.6088 | 0.528 | 0.4044 | 0.4311 | -0.107 ± 0.0146 | -0.048 (5) |
| 15-25 | 1268 | 0.2258 | 0.2128 | +0.0130 ± 0.0051 | 0.6475 | 0.6099 | 0.5772 | 0.3818 | 0.4464 | -0.101 ± 0.013 | -0.0033 (9) |
| 25-40 | 745 | 0.2225 | 0.2057 | +0.0169 ± 0.0099 | 0.6344 | 0.5932 | 0.6547 | 0.3447 | 0.4725 | -0.075 ± 0.0152 | -0.01 (1) |
| 40+ | 155 | 0.2842 | 0.1885 | +0.0957 ± 0.0305 | 0.7739 | 0.5561 | 0.7384 | 0.2901 | 0.4129 | -0.076 ± 0.0302 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4551 | 0.1843 | 0.1851 | -0.0008 ± 0.0002 | 0.543 | 0.5441 | 0.487 | 0.4718 | 0.5019 | -0.023 ± 0.0065 | -0.0129 (17) |
| 3-5 | 3080 | 0.195 | 0.1933 | +0.0018 ± 0.0006 | 0.569 | 0.5625 | 0.4824 | 0.4426 | 0.4393 | -0.058 ± 0.008 | 0.0 (2) |
| 5-10 | 6542 | 0.2023 | 0.1989 | +0.0034 ± 0.0008 | 0.5904 | 0.5787 | 0.4851 | 0.4115 | 0.4259 | -0.046 ± 0.0056 | -0.0119 (21) |
| 10-15 | 5423 | 0.2014 | 0.1855 | +0.0159 ± 0.0015 | 0.5888 | 0.5454 | 0.4848 | 0.3608 | 0.3583 | -0.066 ± 0.0059 | -0.0281 (16) |
| 15-25 | 6792 | 0.2069 | 0.1685 | +0.0384 ± 0.002 | 0.6064 | 0.4996 | 0.5002 | 0.3042 | 0.3052 | -0.070 ± 0.005 | -0.0025 (44) |
| 25-40 | 5371 | 0.2217 | 0.1254 | +0.0963 ± 0.003 | 0.6375 | 0.3856 | 0.526 | 0.2119 | 0.2197 | -0.059 ± 0.0047 | -0.01 (1) |
| 40+ | 3539 | 0.3849 | 0.0444 | +0.3404 ± 0.004 | 1.0024 | 0.1722 | 0.6329 | 0.1036 | 0.0588 | -0.079 ± 0.0033 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 659 | 0.2054 | 0.2061 | -0.0007 ± 0.0006 | 0.5923 | 0.5941 | 0.508 | 0.4931 | 0.525 | -0.099 ± 0.0191 | -0.01 (3) |
| 3-5 | 468 | 0.2207 | 0.2179 | +0.0027 ± 0.0017 | 0.6258 | 0.6203 | 0.512 | 0.4724 | 0.453 | -0.130 ± 0.0229 | 0.02 (1) |
| 5-10 | 1054 | 0.2085 | 0.2078 | +0.0007 ± 0.0021 | 0.6036 | 0.6008 | 0.543 | 0.4683 | 0.5028 | -0.088 ± 0.0145 | -0.01 (4) |
| 10-15 | 929 | 0.2161 | 0.2101 | +0.0061 ± 0.0038 | 0.6231 | 0.6073 | 0.564 | 0.4397 | 0.4801 | -0.106 ± 0.0157 | -0.04 (5) |
| 15-25 | 1333 | 0.2298 | 0.2142 | +0.0156 ± 0.005 | 0.6543 | 0.6128 | 0.5835 | 0.3882 | 0.4479 | -0.096 ± 0.0129 | -0.0133 (9) |
| 25-40 | 940 | 0.2677 | 0.1973 | +0.0703 ± 0.0091 | 0.7477 | 0.5753 | 0.6591 | 0.3448 | 0.3926 | -0.132 ± 0.0145 | -0.0075 (4) |
| 40+ | 350 | 0.3638 | 0.1663 | +0.1975 ± 0.0216 | 0.9969 | 0.5001 | 0.7323 | 0.2474 | 0.3 | -0.083 ± 0.0211 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3933 | 0.1897 | 0.1899 | -0.0003 ± 0.0002 | 0.5543 | 0.5546 | 0.509 | 0.494 | 0.5103 | -0.040 ± 0.0072 | -0.0133 (15) |
| 3-5 | 2665 | 0.1963 | 0.1951 | +0.0011 ± 0.0007 | 0.5695 | 0.5659 | 0.5099 | 0.4703 | 0.4739 | -0.048 ± 0.0087 | 0.02 (1) |
| 5-10 | 5809 | 0.1988 | 0.1954 | +0.0034 ± 0.0009 | 0.583 | 0.57 | 0.5101 | 0.436 | 0.4527 | -0.042 ± 0.0059 | -0.0117 (6) |
| 10-15 | 4867 | 0.2044 | 0.1925 | +0.0119 ± 0.0016 | 0.598 | 0.5623 | 0.5126 | 0.3887 | 0.4035 | -0.052 ± 0.0064 | -0.0189 (18) |
| 15-25 | 6805 | 0.2172 | 0.1815 | +0.0357 ± 0.002 | 0.6317 | 0.5324 | 0.5234 | 0.3281 | 0.3377 | -0.061 ± 0.0052 | -0.0086 (42) |
| 25-40 | 6273 | 0.2514 | 0.1359 | +0.1154 ± 0.003 | 0.7093 | 0.4168 | 0.5577 | 0.2409 | 0.2206 | -0.086 ± 0.0046 | -0.0044 (18) |
| 40+ | 4946 | 0.399 | 0.0586 | +0.3404 ± 0.004 | 1.0532 | 0.2113 | 0.6525 | 0.1174 | 0.0807 | -0.073 ± 0.0034 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 796 | 0.1962 | 0.1985 | -0.0022 ± 0.0006 | 0.5713 | 0.577 | 0.4992 | 0.4838 | 0.5452 | -0.037 ± 0.0165 | -0.0137 (8) |
| 3-5 | 559 | 0.2057 | 0.204 | +0.0017 ± 0.0015 | 0.5945 | 0.5886 | 0.4951 | 0.4555 | 0.4544 | -0.120 ± 0.0198 | 0.0067 (3) |
| 5-10 | 1249 | 0.2031 | 0.2013 | +0.0018 ± 0.0019 | 0.592 | 0.5856 | 0.511 | 0.4372 | 0.4604 | -0.096 ± 0.0131 | -0.0071 (7) |
| 10-15 | 1004 | 0.2087 | 0.204 | +0.0047 ± 0.0035 | 0.6072 | 0.5916 | 0.5394 | 0.416 | 0.4602 | -0.096 ± 0.0143 | -0.0317 (6) |
| 15-25 | 1202 | 0.2347 | 0.2174 | +0.0174 ± 0.0052 | 0.6688 | 0.62 | 0.5885 | 0.3943 | 0.4468 | -0.113 ± 0.0135 | -0.03 (1) |
| 25-40 | 760 | 0.213 | 0.2127 | +0.0003 ± 0.0098 | 0.6145 | 0.6095 | 0.6629 | 0.3525 | 0.5053 | -0.059 ± 0.0151 | 0.015 (2) |
| 40+ | 163 | 0.2995 | 0.196 | +0.1035 ± 0.0306 | 0.8153 | 0.5732 | 0.7492 | 0.2987 | 0.4172 | -0.077 ± 0.0316 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4391 | 0.1839 | 0.1846 | -0.0007 ± 0.0002 | 0.5412 | 0.5425 | 0.4819 | 0.4666 | 0.4867 | -0.032 ± 0.0066 | -0.0163 (35) |
| 3-5 | 3027 | 0.2021 | 0.2 | +0.0021 ± 0.0007 | 0.5872 | 0.5798 | 0.4804 | 0.441 | 0.4348 | -0.063 ± 0.0083 | -0.0094 (18) |
| 5-10 | 6700 | 0.1944 | 0.1905 | +0.0039 ± 0.0008 | 0.572 | 0.5585 | 0.4858 | 0.4118 | 0.4228 | -0.048 ± 0.0054 | -0.01 (31) |
| 10-15 | 5406 | 0.1921 | 0.1786 | +0.0135 ± 0.0014 | 0.5682 | 0.5291 | 0.4942 | 0.3708 | 0.3774 | -0.057 ± 0.0058 | -0.015 (12) |
| 15-25 | 6906 | 0.2138 | 0.1735 | +0.0403 ± 0.002 | 0.6222 | 0.5109 | 0.5135 | 0.319 | 0.3142 | -0.074 ± 0.005 | -0.03 (2) |
| 25-40 | 5362 | 0.2162 | 0.1287 | +0.0875 ± 0.0031 | 0.6255 | 0.3932 | 0.5294 | 0.2139 | 0.2352 | -0.048 ± 0.0047 | 0.01 (3) |
| 40+ | 3506 | 0.3948 | 0.05 | +0.3448 ± 0.0043 | 1.0293 | 0.1866 | 0.6425 | 0.1103 | 0.0656 | -0.079 ± 0.0036 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1196 | 0.196 | 0.1962 | -0.0002 ± 0.0004 | 0.5708 | 0.5709 | 0.5044 | 0.4893 | 0.4941 | -0.069 ± 0.0131 | -0.0224 (49) |
| 3-5 | 852 | 0.1872 | 0.1862 | +0.0010 ± 0.0012 | 0.5488 | 0.5458 | 0.4964 | 0.4565 | 0.4624 | -0.069 ± 0.0152 | -0.0194 (34) |
| 5-10 | 1776 | 0.2015 | 0.1968 | +0.0046 ± 0.0016 | 0.5919 | 0.5772 | 0.5025 | 0.4288 | 0.4347 | -0.076 ± 0.0108 | -0.005 (78) |
| 10-15 | 1211 | 0.2165 | 0.2038 | +0.0127 ± 0.0032 | 0.6253 | 0.5915 | 0.5377 | 0.4149 | 0.4228 | -0.089 ± 0.0133 | 0.0014 (64) |
| 15-25 | 1551 | 0.2324 | 0.2111 | +0.0213 ± 0.0046 | 0.6622 | 0.6072 | 0.5839 | 0.3892 | 0.4346 | -0.085 ± 0.0118 | -0.0214 (59) |
| 25-40 | 980 | 0.2441 | 0.2107 | +0.0334 ± 0.009 | 0.6976 | 0.604 | 0.6842 | 0.3722 | 0.4755 | -0.094 ± 0.0138 | -0.0219 (26) |
| 40+ | 327 | 0.3343 | 0.2031 | +0.1312 ± 0.024 | 0.9686 | 0.5915 | 0.8158 | 0.3392 | 0.4557 | -0.099 ± 0.0225 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4491 | 0.1758 | 0.1761 | -0.0003 ± 0.0002 | 0.5207 | 0.521 | 0.509 | 0.4937 | 0.5063 | -0.037 ± 0.0063 | -0.0157 (88) |
| 3-5 | 3089 | 0.1937 | 0.1922 | +0.0015 ± 0.0006 | 0.5639 | 0.5608 | 0.5027 | 0.4629 | 0.4636 | -0.051 ± 0.008 | -0.0209 (69) |
| 5-10 | 6340 | 0.199 | 0.1923 | +0.0067 ± 0.0008 | 0.5847 | 0.5652 | 0.4984 | 0.4247 | 0.4177 | -0.065 ± 0.0056 | -0.0082 (132) |
| 10-15 | 4400 | 0.2109 | 0.1951 | +0.0158 ± 0.0017 | 0.6126 | 0.5714 | 0.5364 | 0.4135 | 0.4098 | -0.070 ± 0.0067 | -0.0053 (105) |
| 15-25 | 5314 | 0.2305 | 0.2011 | +0.0294 ± 0.0024 | 0.6624 | 0.5817 | 0.5708 | 0.3755 | 0.3991 | -0.064 ± 0.0062 | -0.0253 (107) |
| 25-40 | 3608 | 0.2605 | 0.1878 | +0.0727 ± 0.0045 | 0.7368 | 0.5477 | 0.6364 | 0.3238 | 0.3667 | -0.077 ± 0.0071 | -0.0229 (51) |
| 40+ | 1534 | 0.378 | 0.1536 | +0.2244 ± 0.0104 | 1.0704 | 0.4596 | 0.7406 | 0.239 | 0.2771 | -0.075 ± 0.0095 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5733 | 1.015 ± 0.037 | 1.089 | 0.1692 | 0.1663 | 0.2152 | 0.2062 |
| gen2 | 5733 | 0.804 ± 0.033 | 1.054 | 0.1714 | 0.1667 | 0.2345 | 0.206 |
| gen1_elo | 5733 | 0.991 ± 0.035 | 1.086 | 0.1757 | 0.1664 | 0.2141 | 0.2064 |
| gen1_sr | 5733 | 0.989 ± 0.044 | 1.113 | 0.1316 | 0.1686 | 0.2304 | 0.2057 |
| gen1_ledger | 7893 | 0.855 ± 0.026 | 1.057 | 0.1877 | 0.1758 | 0.2183 | 0.2014 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 28,698)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,460 | 22.5% |
| STALE_QUOTE | market_freshness | 6,343 | 22.1% |
| BOOK_QUALITY | execution | 5,397 | 18.8% |
| POOR_DATA | data | 3,351 | 11.7% |
| LIMITED_DATA | data | 1,778 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,635 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,229 | 4.3% |
| IDENTITY_AMBIGUOUS | mapping | 1,183 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 829 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 492 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.5%, market_freshness 22.1%, execution 18.8%, data 17.9%, market_freshness/coverage 8.6%, model_calibration_or_unknown 4.3%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.4%, START_UNVERIFIABLE 94.5%, LOW_DATA_QUALITY 71.7%, THIN_PLAYER_HISTORY 60.2%, STALE_PLAYER_DATA 52.3%, STALE_KALSHI_QUOTE 44.5%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 33.4%, WIDE_SPREAD 24.9%, MODEL_HIGH_UNCERTAINTY 18.2%, PLAYER_IDENTITY_RISK 15.6%, LEVEL_TRANSFER_RISK 10.5%, LOW_DISPLAYED_LIQUIDITY 8.1%, EVENT_MAPPING_RISK 7.5%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.4%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.0%, POST_SETTLEMENT_OBSERVATION 22.5%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 15,322)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,222 | 34.1% |
| STALE_QUOTE | market_freshness | 2,878 | 18.8% |
| BOOK_QUALITY | execution | 2,808 | 18.3% |
| POOR_DATA | data | 1,436 | 9.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 859 | 5.6% |
| IDENTITY_AMBIGUOUS | mapping | 633 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 537 | 3.5% |
| LIMITED_DATA | data | 519 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 306 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 123 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.1%, market_freshness 18.8%, execution 18.3%, data 12.8%, market_freshness/coverage 9.1%, mapping 4.1%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 75.1%, THIN_PLAYER_HISTORY 62.5%, STALE_KALSHI_QUOTE 52.4%, STALE_PLAYER_DATA 46.3%, MODEL_INTERNAL_DISAGREEMENT 42.5%, ASYMMETRIC_SAMPLE_SIZE 34.4%, WIDE_SPREAD 24.3%, MODEL_HIGH_UNCERTAINTY 18.9%, PLAYER_IDENTITY_RISK 18.4%, LEVEL_TRANSFER_RISK 9.3%, EVENT_MAPPING_RISK 9.0%, LOW_DISPLAYED_LIQUIDITY 8.0%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.1%, POST_SETTLEMENT_OBSERVATION 34.1%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 12186, "IDENTITY_AMBIGUOUS": 3136}; ticker orientation: {"VERIFIED": 15322}.

Checks: discipline:AMBIGUOUS 1008, discipline:PASS 14314, identity_confidence:AMBIGUOUS 2813, identity_confidence:PASS 12509, level_mapping:NA 1020, level_mapping:PASS 14302, market_pair:AMBIGUOUS 482, market_pair:NA 350, market_pair:PASS 14490, model_complement:NA 314, model_complement:PASS 15008, namesake:AMBIGUOUS 6, namesake:PASS 15316, physical_match_id:NA 5317, physical_match_id:PASS 10005, player_ids:PASS 15322, same_pair_other_event:PASS 15322, ticker_orientation:PASS 15322

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,478 | 4.1% | 3.7% | 1.5% | {"market_freshness": 56, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "market_freshness/coverage": 17, "coverage": 13} | 5.83 | 0.2219 / 0.2176 (635) | 22.0% | 2.9% | 3.2% | 2.8% |
| CHALLENGER | 10,040 | 16.5% | 6.2% | 10.8% | {"coverage": 981, "market_freshness/coverage": 198, "market_freshness": 172, "data": 144, "model_calibration_or_unknown": 74, "execution": 37, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.25 | 0.2211 / 0.2119 (2285) | 35.7% | 15.6% | 4.1% | 22.7% |
| DOUBLES | 2,159 | 46.7% | 46.5% | 6.6% | {"execution": 566, "mapping": 269, "market_freshness": 106, "market_freshness/coverage": 60, "coverage": 7} | 23.54 | 0.3086 / 0.2394 (519) | 10.8% | 0.0% | 100.0% | 6.2% |
| ITF_MEN | 19,945 | 25.0% | 17.6% | 32.5% | {"coverage": 1757, "market_freshness": 916, "execution": 913, "data": 730, "market_freshness/coverage": 478, "mapping": 183, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.72 | 0.2166 / 0.1998 (4080) | 38.1% | 69.3% | 16.4% | 21.6% |
| ITF_WOMEN | 26,180 | 26.5% | 19.1% | 45.4% | {"coverage": 2421, "market_freshness": 1476, "execution": 1214, "data": 988, "market_freshness/coverage": 590, "mapping": 158, "model_calibration_or_unknown": 81, "model_calibration": 21} | 12.54 | 0.2037 / 0.1951 (4788) | 39.8% | 57.1% | 9.9% | 21.4% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,026 | 5.7% | 4.8% | 1.5% | {"market_freshness": 79, "model_calibration_or_unknown": 43, "coverage": 30, "execution": 28, "data": 19, "model_calibration": 18, "market_freshness/coverage": 11, "mapping": 1} | 7.46 | 0.2373 / 0.231 (619) | 27.1% | 1.3% | 1.4% | 3.4% |
| WTA125 | 2,278 | 11.1% | 9.5% | 1.7% | {"market_freshness": 71, "model_calibration_or_unknown": 51, "market_freshness/coverage": 41, "data": 38, "execution": 21, "model_calibration": 15, "coverage": 12, "mapping": 4} | 9.17 | 0.2103 / 0.1925 (658) | 26.6% | 10.8% | 4.7% | 7.2% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 17.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 1025 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 3 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 4 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 5 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 311 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 6 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 852 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 7 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 8 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 628 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 9 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 10 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 113 min (STALE); no external reference |
| 13 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 14 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 207 min (STALE); no external reference |
| 17 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 18 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 19 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 20 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 21 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 22 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 23 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 24 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 25 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 26 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 27 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 28 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 29 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 30 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 31 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 32 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 33 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 34 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 35 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 36 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 37 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 38 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 39 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 213 min (STALE); no external reference |
| 40 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 41 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 42 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 43 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.1h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 446 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 44 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 45 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 252 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |
| 46 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 47 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 48 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 49 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 12.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 768 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 50 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9702, "by_level_share_of_ge_25pp": {"ATP": 0.0148, "CHALLENGER": 0.1083, "DOUBLES": 0.0658, "ITF_MEN": 0.3253, "ITF_WOMEN": 0.4535, "OTHER": 0.0008, "WTA": 0.0149, "WTA125": 0.0165}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5237, "share_primary_cause_market_settled_or_in_play": 0.4319, "share_primary_cause_stale_quote_only": 0.1878}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 15322, "identity_ambiguous_share": 0.2047, "ticker_orientation": {"VERIFIED": 15322}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 10005, "with_external": 522, "coverage": 0.0522, "external_status": {"EXTERNAL_STALE": 322, "AGREES_WITH_KALSHI": 187, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 322, "MODEL_LONE_OUTLIER": 187, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3582, "share_external_supports_model": 0.0249}, "pregame_clean_ge_25pp": {"n": 4753, "with_external": 495, "coverage": 0.1041, "external_status": {"EXTERNAL_STALE": 302, "AGREES_WITH_KALSHI": 180, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 302, "MODEL_LONE_OUTLIER": 180, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3636, "share_external_supports_model": 0.0263}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 475.5, "median_sample_ratio": 2.48, "median_min_matches": 19.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.21, "data_status": {"POOR": 8674, "LIMITED": 3961, "ADEQUATE": 2687}, "comparison_lt_10pp": {"median_thinner_serve_points": 1695.0, "median_sample_ratio": 1.71, "median_min_matches": 90.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1158, "model_minus_observed": 0.0523, "kalshi_minus_observed": -0.0869, "brier_diff_model_minus_kalshi": -0.0021}, "4-10x": {"n": 803, "model_minus_observed": 0.0866, "kalshi_minus_observed": -0.0602, "brier_diff_model_minus_kalshi": 0.0077}, "<2x": {"n": 2778, "model_minus_observed": 0.0911, "kalshi_minus_observed": -0.0321, "brier_diff_model_minus_kalshi": 0.0123}, ">=10x": {"n": 994, "model_minus_observed": 0.1158, "kalshi_minus_observed": -0.0586, "brier_diff_model_minus_kalshi": 0.0134}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 5733, "model": {"intercept": -0.53, "slope": 0.804, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.196, "slope": 1.054, "slope_se": 0.037}, "mean_extremity_model": 0.1714, "mean_extremity_kalshi": 0.1667, "model_brier": 0.2345, "kalshi_brier": 0.206, "brier_diff_model_minus_kalshi": 0.0285, "brier_diff_se": 0.0025, "model_logloss": 0.6667, "kalshi_logloss": 0.5951}, "fair_v1": {"n": 5733, "model": {"intercept": -0.416, "slope": 1.015, "slope_se": 0.037}, "kalshi_mid_same_rows": {"intercept": 0.278, "slope": 1.089, "slope_se": 0.038}, "mean_extremity_model": 0.1692, "mean_extremity_kalshi": 0.1663, "model_brier": 0.2152, "kalshi_brier": 0.2062, "brier_diff_model_minus_kalshi": 0.009, "brier_diff_se": 0.0021, "model_logloss": 0.6194, "kalshi_logloss": 0.5954}, "gen1_elo": {"n": 5733, "model": {"intercept": -0.393, "slope": 0.991, "slope_se": 0.035}, "kalshi_mid_same_rows": {"intercept": 0.297, "slope": 1.086, "slope_se": 0.037}, "mean_extremity_model": 0.1757, "mean_extremity_kalshi": 0.1664, "model_brier": 0.2141, "kalshi_brier": 0.2064, "brier_diff_model_minus_kalshi": 0.0077, "brier_diff_se": 0.0021, "model_logloss": 0.6175, "kalshi_logloss": 0.5958}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.248, "share_ge_15": 0.4429, "median_abs_gap": 13.01, "n": 40349}, "gen1_elo": {"share_ge_25": 0.246, "share_ge_15": 0.4412, "median_abs_gap": 12.93, "n": 40349}, "gen1_sr": {"share_ge_25": 0.313, "share_ge_15": 0.5199, "median_abs_gap": 15.85, "n": 40349}, "gen2": {"share_ge_25": 0.3159, "share_ge_15": 0.5094, "median_abs_gap": 15.44, "n": 40349}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1523, "share_ge_15": 0.3546, "median_abs_gap": 10.71, "n": 31194}, "gen1_elo": {"share_ge_25": 0.1522, "share_ge_15": 0.3519, "median_abs_gap": 10.53, "n": 31193}, "gen1_sr": {"share_ge_25": 0.2169, "share_ge_15": 0.4402, "median_abs_gap": 13.0, "n": 31196}, "gen2": {"share_ge_25": 0.2332, "share_ge_15": 0.4393, "median_abs_gap": 12.86, "n": 31196}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.83, "share_ge_25_all": 0.0414, "share_ge_25_pregame_clean": 0.037}, "WTA": {"median_abs_gap_pregame_clean": 7.46, "share_ge_25_all": 0.0569, "share_ge_25_pregame_clean": 0.0483}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2365, "share_within_10pp_all": 0.4383, "share_within_10pp_pregame_clean": 0.4909, "corr_model_vs_mid_pregame_clean": 0.8507}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 830, "model_brier": 0.1995, "kalshi_brier": 0.1999, "brier_diff_model_minus_kalshi": -0.0004}, "10-15": {"n_settled": 1002, "model_brier": 0.2202, "kalshi_brier": 0.2118, "brier_diff_model_minus_kalshi": 0.0084}, "15-25": {"n_settled": 1268, "model_brier": 0.2258, "kalshi_brier": 0.2128, "brier_diff_model_minus_kalshi": 0.013}, "25-40": {"n_settled": 745, "model_brier": 0.2225, "kalshi_brier": 0.2057, "brier_diff_model_minus_kalshi": 0.0169}, "3-5": {"n_settled": 526, "model_brier": 0.2052, "kalshi_brier": 0.2056, "brier_diff_model_minus_kalshi": -0.0004}, "40+": {"n_settled": 155, "model_brier": 0.2842, "kalshi_brier": 0.1885, "brier_diff_model_minus_kalshi": 0.0957}, "5-10": {"n_settled": 1207, "model_brier": 0.2015, "kalshi_brier": 0.2019, "brier_diff_model_minus_kalshi": -0.0004}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.53, "slope": 0.804, "slope_se": 0.033}, "kalshi_slope": {"intercept": 0.196, "slope": 1.054, "slope_se": 0.037}, "n": 5733}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.49, "slope": 0.855, "slope_se": 0.026}, "kalshi_slope": {"intercept": 0.164, "slope": 1.057, "slope_se": 0.031}, "n": 7893}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 519, "model_brier": 0.3086, "kalshi_brier": 0.2394, "brier_diff_model_minus_kalshi": 0.0692, "brier_diff_se": 0.0131, "corr_model_outcome": 0.0557, "corr_kalshi_outcome": 0.2204}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
