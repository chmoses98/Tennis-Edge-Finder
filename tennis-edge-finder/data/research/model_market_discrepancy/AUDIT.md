# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-05T07:53Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 78,963): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 19.1%, 25-40 13.6%, 40+ 8.0%; median gap 11.79 pp.
* **Where the extremes live**: 96.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.7%, Challenger 10.7%, doubles 6.7%). Main tour: ATP 3.8% and WTA 6.1% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 17,063): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.5%, STALE_QUOTE 19.6%, BOOK_QUALITY 17.9%, POOR_DATA 9.4%, POSSIBLY_IN_PLAY_QUOTE 5.7%, IDENTITY_AMBIGUOUS 4.3%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.5%, market_freshness 19.6%, execution 17.9%, data 12.8%, market_freshness/coverage 9.3%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.9% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.7% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 17,063 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.4% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.4%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.4% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 479.0 points vs 1719.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.044, Gen-2 0.837, Gen-1 ledger 0.875 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 863 model 0.2211 vs Kalshi 0.2039; n 184 model 0.2944 vs Kalshi 0.1759.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 336,658 model-market comparisons (550,293 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 112,270 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-05T07:36:12.380007+00:00'], shadow board 90,632 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-05T07:36:15.922727+00:00'], Model 4 42,046 rows, 27,633 settled tickers, 10,531 tickers with an external scan.
* By model: {"gen1_ledger": 75735, "gen1_elo": 45544, "fair_v1": 45544, "gen2": 45544, "gen1_sr": 45544, "model4_fundamental": 39415, "model4_conditioned": 39332}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 78,963 | 14.1 | 9.6 | 20.2 | 15.3 | 19.1 | 13.6 | 8.0 | 11.79 | 40.7% | 21.6% |
| MW fair_v1 | 45,544 | 12.9 | 8.7 | 18.8 | 15.4 | 19.6 | 14.8 | 9.8 | 12.99 | 44.2% | 24.6% |
| MW gen1_elo | 45,544 | 12.6 | 8.8 | 19.3 | 15.4 | 19.5 | 14.6 | 9.7 | 12.74 | 43.8% | 24.3% |
| MW gen1_ledger | 33,419 | 15.8 | 10.9 | 22.2 | 15.1 | 18.4 | 12.1 | 5.5 | 10.26 | 36.0% | 17.6% |
| MW gen1_sr | 45,544 | 10.2 | 7.3 | 16.7 | 13.9 | 20.7 | 18.7 | 12.5 | 15.76 | 51.9% | 31.2% |
| MW gen2 | 45,544 | 11.1 | 7.6 | 16.7 | 13.8 | 19.5 | 17.7 | 13.6 | 15.38 | 50.8% | 31.3% |
| all families model4_conditioned | 39,332 | 22.2 | 18.0 | 34.2 | 17.2 | 5.0 | 2.2 | 1.2 | 6.07 | 8.5% | 3.5% |
| all families model4_fundamental | 39,415 | 17.4 | 13.5 | 33.9 | 19.9 | 10.0 | 3.8 | 1.5 | 7.63 | 15.4% | 5.4% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.0%, >=15pp 40.7%, >=20pp 29.9%, >=25pp 21.6%, >=30pp 15.6%, >=40pp 8.0%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.33pp; >=10pp 44.8%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,907 | 28.4 | 15.6 | 27.6 | 13.4 | 10.7 | 3.7 | 0.6 | 5.82 | 14.9% | 4.3% |
| CHALLENGER | 6,835 | 16.0 | 9.9 | 20.8 | 15.2 | 16.2 | 11.3 | 10.7 | 10.91 | 38.1% | 21.9% |
| ITF_MEN | 12,770 | 9.9 | 7.3 | 17.1 | 15.1 | 21.3 | 17.2 | 12.0 | 15.18 | 50.5% | 29.2% |
| ITF_WOMEN | 17,725 | 9.5 | 7.1 | 16.1 | 14.9 | 22.1 | 18.3 | 11.9 | 15.77 | 52.4% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,981 | 16.7 | 13.2 | 24.6 | 21.0 | 16.4 | 6.9 | 1.1 | 8.73 | 24.4% | 8.0% |
| WTA125 | 1,320 | 15.8 | 6.9 | 22.6 | 20.0 | 20.5 | 12.3 | 1.9 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,907 | 26.9 | 15.8 | 26.0 | 15.4 | 11.5 | 3.7 | 0.8 | 6.03 | 16.0% | 4.5% |
| CHALLENGER | 6,835 | 14.9 | 9.0 | 18.6 | 14.0 | 18.7 | 13.4 | 11.3 | 12.48 | 43.4% | 24.7% |
| ITF_MEN | 12,770 | 8.2 | 6.2 | 15.2 | 13.8 | 19.9 | 20.6 | 16.2 | 17.84 | 56.6% | 36.8% |
| ITF_WOMEN | 17,725 | 7.8 | 5.8 | 14.2 | 12.9 | 20.6 | 21.2 | 17.5 | 19.07 | 59.4% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,981 | 14.1 | 10.2 | 22.0 | 15.9 | 22.1 | 13.1 | 2.6 | 11.19 | 37.8% | 15.7% |
| WTA125 | 1,320 | 10.2 | 7.3 | 16.4 | 15.4 | 24.2 | 17.5 | 9.1 | 15.22 | 50.8% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,907 | 22.9 | 13.9 | 25.2 | 15.6 | 15.1 | 6.1 | 1.2 | 7.2 | 22.4% | 7.3% |
| CHALLENGER | 6,835 | 15.2 | 9.5 | 20.9 | 15.6 | 16.0 | 11.9 | 10.9 | 11.18 | 38.7% | 22.7% |
| ITF_MEN | 12,770 | 9.5 | 7.2 | 17.3 | 14.2 | 22.0 | 17.3 | 12.4 | 15.63 | 51.7% | 29.7% |
| ITF_WOMEN | 17,725 | 9.3 | 6.9 | 16.3 | 15.9 | 22.2 | 18.2 | 11.2 | 15.53 | 51.6% | 29.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,981 | 22.8 | 17.0 | 31.8 | 15.2 | 8.9 | 3.4 | 1.1 | 6.12 | 13.3% | 4.4% |
| WTA125 | 1,320 | 21.2 | 13.2 | 25.7 | 18.9 | 14.8 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,315 | 26.7 | 19.6 | 30.0 | 12.3 | 8.2 | 2.6 | 0.4 | 5.37 | 11.3% | 3.0% |
| CHALLENGER | 4,414 | 22.2 | 14.5 | 27.6 | 14.7 | 13.5 | 5.8 | 1.5 | 7.09 | 20.9% | 7.4% |
| DOUBLES | 2,458 | 5.0 | 4.3 | 12.6 | 10.9 | 20.4 | 24.9 | 21.9 | 23.55 | 67.2% | 46.8% |
| ITF_MEN | 9,551 | 13.0 | 9.6 | 21.3 | 15.7 | 21.5 | 13.1 | 5.9 | 11.79 | 40.4% | 18.9% |
| ITF_WOMEN | 11,553 | 13.4 | 9.2 | 20.0 | 15.7 | 21.3 | 14.9 | 5.5 | 12.22 | 41.7% | 20.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,729 | 24.3 | 15.9 | 31.1 | 16.5 | 9.2 | 2.7 | 0.2 | 6.57 | 12.2% | 2.9% |
| WTA125 | 1,250 | 25.3 | 13.1 | 21.3 | 19.0 | 13.0 | 6.9 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,793 | 28.8 | 15.8 | 28.1 | 13.4 | 10.4 | 3.2 | 0.3 | 5.67 | 14.0% | 3.6% |
| CHALLENGER | 4,845 | 20.6 | 12.2 | 25.6 | 17.9 | 16.1 | 6.0 | 1.6 | 8.23 | 23.8% | 7.6% |
| ITF_MEN | 9,413 | 12.0 | 8.7 | 20.6 | 17.3 | 22.1 | 14.0 | 5.3 | 12.39 | 41.4% | 19.3% |
| ITF_WOMEN | 13,158 | 11.3 | 8.6 | 18.8 | 17.1 | 24.1 | 15.2 | 5.0 | 13.25 | 44.2% | 20.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,871 | 17.0 | 13.3 | 24.9 | 21.4 | 16.5 | 6.3 | 0.6 | 8.53 | 23.4% | 7.0% |
| WTA125 | 1,272 | 16.1 | 6.8 | 22.3 | 20.2 | 20.9 | 11.9 | 1.7 | 10.7 | 34.5% | 13.6% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,793 | 27.2 | 16.1 | 26.3 | 15.4 | 11.4 | 3.3 | 0.4 | 5.96 | 15.1% | 3.7% |
| CHALLENGER | 4,845 | 18.7 | 11.3 | 23.3 | 16.4 | 19.1 | 9.3 | 1.9 | 9.06 | 30.3% | 11.2% |
| ITF_MEN | 9,414 | 9.6 | 7.3 | 17.6 | 15.9 | 21.6 | 18.6 | 9.3 | 14.89 | 49.5% | 28.0% |
| ITF_WOMEN | 13,159 | 8.8 | 6.7 | 16.1 | 14.4 | 22.7 | 20.5 | 10.8 | 16.58 | 54.0% | 31.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,871 | 14.3 | 10.3 | 22.2 | 16.1 | 22.4 | 12.8 | 1.9 | 11.03 | 37.1% | 14.7% |
| WTA125 | 1,272 | 10.2 | 7.4 | 16.5 | 15.5 | 24.2 | 17.6 | 8.6 | 15.14 | 50.4% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,258 | 26.9 | 19.8 | 30.0 | 12.5 | 8.0 | 2.5 | 0.3 | 5.33 | 10.8% | 2.8% |
| CHALLENGER | 3,898 | 23.6 | 15.4 | 28.8 | 14.8 | 12.9 | 4.0 | 0.4 | 6.61 | 17.4% | 4.5% |
| DOUBLES | 2,310 | 4.9 | 4.4 | 12.8 | 11.0 | 20.2 | 24.9 | 21.8 | 23.54 | 66.9% | 46.7% |
| ITF_MEN | 8,211 | 13.8 | 10.2 | 22.9 | 16.2 | 21.5 | 11.6 | 3.9 | 10.85 | 36.9% | 15.4% |
| ITF_WOMEN | 9,897 | 14.0 | 9.7 | 21.1 | 16.2 | 21.4 | 13.8 | 3.6 | 11.41 | 38.9% | 17.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,668 | 24.6 | 16.3 | 31.1 | 16.6 | 9.2 | 2.1 | 0.1 | 6.43 | 11.4% | 2.2% |
| WTA125 | 1,109 | 26.4 | 14.0 | 22.3 | 19.8 | 12.1 | 5.0 | 0.5 | 7.2 | 17.6% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,458 | 5.0 | 4.3 | 12.6 | 10.9 | 20.4 | 24.9 | 21.9 | 23.55 | 67.2% | 46.8% |
| singles | 30,961 | 16.6 | 11.4 | 23.0 | 15.5 | 18.2 | 11.1 | 4.2 | 9.73 | 33.5% | 15.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 132 | 8.3 | 9.1 | 14.4 | 8.3 | 19.7 | 26.5 | 13.6 | 19.99 | 59.9% | 40.2% |
| Clay | 9,243 | 12.8 | 9.2 | 19.9 | 15.8 | 19.7 | 13.7 | 8.9 | 12.52 | 42.4% | 22.6% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 29,774 | 13.4 | 8.7 | 18.9 | 15.2 | 19.1 | 14.8 | 9.8 | 12.84 | 43.8% | 24.6% |
| UNKNOWN | 6,158 | 10.5 | 7.7 | 17.0 | 16.4 | 21.5 | 15.8 | 11.1 | 14.29 | 48.4% | 26.9% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 12,905 | 19.6 | 12.0 | 22.5 | 15.9 | 15.0 | 9.0 | 6.1 | 8.81 | 30.0% | 15.0% |
| B | 5,585 | 12.9 | 8.8 | 19.7 | 15.7 | 19.5 | 12.7 | 10.7 | 12.56 | 42.9% | 23.4% |
| C | 6,444 | 11.9 | 8.9 | 19.6 | 15.9 | 18.6 | 14.6 | 10.4 | 12.89 | 43.7% | 25.0% |
| D | 7,331 | 11.8 | 8.4 | 17.9 | 15.4 | 21.5 | 15.7 | 9.2 | 13.69 | 46.4% | 24.9% |
| F | 13,279 | 7.4 | 5.6 | 14.9 | 14.7 | 23.5 | 20.9 | 13.0 | 17.71 | 57.5% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,900 | 24.6 | 16.0 | 29.1 | 14.9 | 10.7 | 3.4 | 1.2 | 6.37 | 15.3% | 4.7% |
| B | 4,696 | 16.7 | 10.8 | 24.3 | 16.8 | 18.9 | 9.6 | 3.1 | 9.66 | 31.5% | 12.6% |
| C | 6,594 | 11.2 | 7.8 | 19.4 | 14.7 | 20.9 | 15.7 | 10.2 | 13.53 | 46.8% | 25.9% |
| D | 4,993 | 14.5 | 10.1 | 21.5 | 15.4 | 20.3 | 12.7 | 5.4 | 11.18 | 38.4% | 18.1% |
| F | 8,236 | 10.2 | 8.4 | 16.2 | 14.6 | 23.2 | 19.6 | 7.8 | 15.34 | 50.6% | 27.4% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 14,598 | 17.9 | 11.0 | 21.6 | 15.7 | 15.3 | 9.9 | 8.6 | 9.9 | 33.8% | 18.5% |
| LIMITED | 9,946 | 13.6 | 9.8 | 20.5 | 16.1 | 19.3 | 13.2 | 7.5 | 11.77 | 40.0% | 20.7% |
| POOR | 21,000 | 9.0 | 6.6 | 16.1 | 15.0 | 22.7 | 18.9 | 11.7 | 16.09 | 53.3% | 30.6% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,698 | 23.8 | 17.8 | 33.2 | 15.6 | 6.4 | 2.9 | 0.4 | 5.92 | 9.7% | 3.3% |
| GAME_SPREAD | 6,559 | 22.5 | 15.2 | 32.3 | 17.0 | 9.0 | 3.4 | 0.6 | 6.73 | 13.0% | 4.0% |
| MATCH_WINNER | 33,419 | 15.8 | 10.9 | 22.2 | 15.1 | 18.4 | 12.1 | 5.5 | 10.26 | 36.0% | 17.6% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 16,052 | 27.9 | 16.8 | 30.6 | 12.8 | 9.2 | 2.5 | 0.3 | 5.63 | 12.0% | 2.8% |
| TOTAL_GAMES | 10,983 | 9.8 | 10.8 | 35.5 | 26.0 | 10.6 | 4.3 | 3.0 | 9.21 | 17.9% | 7.2% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,952 | 24.5 | 28.8 | 33.2 | 8.2 | 4.0 | 1.1 | 0.3 | 4.79 | 5.3% | 1.4% |
| GAME_SPREAD | 9,082 | 46.8 | 16.1 | 24.8 | 7.5 | 2.3 | 1.9 | 0.6 | 3.31 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,298 | 6.5 | 9.8 | 40.2 | 30.3 | 7.5 | 3.4 | 2.4 | 9.23 | 13.2% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,987 | 23.9 | 16.6 | 34.8 | 14.7 | 6.9 | 2.6 | 0.5 | 6.05 | 10.1% | 3.1% |
| GAME_SPREAD | 9,091 | 20.6 | 13.5 | 28.2 | 20.1 | 12.0 | 4.5 | 1.1 | 7.64 | 17.6% | 5.6% |
| TOTAL_GAMES | 16,337 | 10.0 | 10.8 | 36.2 | 24.4 | 11.5 | 4.5 | 2.6 | 9.07 | 18.7% | 7.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 45,544 | 44.2% | 24.6% | 12.99 | 35.4% | 15.1% | 10.71 |
| gen1_elo | 45,544 | 43.8% | 24.3% | 12.74 | 34.9% | 15.0% | 10.49 |
| gen1_sr | 45,544 | 51.9% | 31.2% | 15.76 | 44.0% | 21.7% | 13.01 |
| gen2 | 45,544 | 50.8% | 31.3% | 15.38 | 43.9% | 23.2% | 12.86 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 19,823 | 15.5 | 10.5 | 21.3 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 25,721 | 10.8 | 7.3 | 16.9 | 14.0 | 19.2 | 17.0 | 14.8 | 15.39 | 51.0% | 31.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 26,887 | 16.4 | 11.2 | 22.8 | 15.2 | 17.9 | 11.6 | 4.8 | 9.86 | 34.3% | 16.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 78,963 | 26887 | 23295 | 28781 | 24.7 | 115.8 | 1451.1 |
| ge_15pp | 32,140 | 9224 | 8296 | 14620 | 27.9 | 421.8 | 1451.1 |
| ge_25pp | 17,063 | 4415 | 3617 | 9031 | 32.8 | 576.8 | 1431.1 |
| lt_10pp | 34,730 | 13569 | 11022 | 10139 | 22.6 | 47.8 | 1421.1 |

Current slate `SL-20261105T075336Z-a4ce41cb`: 581 priced rows, quote age at build {'median': 17.8, 'max': 17.9}, freshness {'AGING': 581}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 49 | 0.0 | 0.0 | 36.7 | 6.1 | 32.6 | 20.4 | 4.1 | 18.34 | 57.1% | 24.5% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,550 | 19.2 | 10.9 | 25.4 | 17.9 | 18.2 | 7.5 | 1.0 | 8.85 | 26.6% | 8.4% |
| KALSHI_LONE_OUTLIER | 30 | 6.7 | 6.7 | 73.3 | 6.7 | 3.3 | 3.3 | 0.0 | 6.16 | 6.7% | 3.3% |
| MARKETS_AGREE | 926 | 66.0 | 34.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.18 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,001 | 0.0 | 2.3 | 36.8 | 26.3 | 24.3 | 9.3 | 0.8 | 11.88 | 34.5% | 10.2% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 45,544 | 7585 (16.7%) | 26.4% | 1.0% | {"EXTERNAL_STALE": 4550, "AGREES_WITH_KALSHI": 2001, "ALL_AGREE": 926, "SUPPORTS_MODEL_DIRECTION": 48, "AGREES_WITH_MODEL": 30, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 20,117 | 1932 (9.6%) | 35.8% | 1.6% | {"EXTERNAL_STALE": 1211, "AGREES_WITH_KALSHI": 691, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 11,186 | 601 (5.4%) | 33.9% | 2.2% | {"EXTERNAL_STALE": 384, "AGREES_WITH_KALSHI": 204, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,354 | 571 (10.7%) | 34.5% | 2.3% | {"EXTERNAL_STALE": 361, "AGREES_WITH_KALSHI": 197, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 18,392 | 4307 (23.4%) | 18.2% | 1.0% | {"EXTERNAL_STALE": 2525, "ALL_AGREE": 926, "AGREES_WITH_KALSHI": 783, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 26, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 8,893 | 10.4 | 7.8 | 19.6 | 14.8 | 21.6 | 16.1 | 9.8 | 13.98 | 47.5% | 25.9% |
| 4-10x | 6,094 | 11.4 | 8.5 | 18.5 | 15.3 | 22.1 | 14.2 | 9.9 | 13.66 | 46.2% | 24.1% |
| <2x | 23,277 | 14.9 | 9.8 | 19.8 | 16.1 | 17.6 | 13.1 | 8.8 | 11.53 | 39.4% | 21.8% |
| >=10x | 7,280 | 10.4 | 6.4 | 15.0 | 14.4 | 21.6 | 19.1 | 13.0 | 16.38 | 53.7% | 32.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 11,894 | 12.5 | 8.7 | 20.0 | 16.2 | 19.0 | 13.4 | 10.1 | 12.64 | 42.6% | 23.6% |
| 300-1000 | 9,828 | 11.8 | 8.8 | 17.8 | 15.4 | 20.7 | 16.1 | 9.3 | 13.61 | 46.1% | 25.5% |
| <300 | 14,366 | 8.3 | 5.8 | 15.2 | 14.7 | 23.1 | 19.9 | 13.0 | 17.11 | 56.0% | 33.0% |
| >=3000 | 9,456 | 21.3 | 13.0 | 23.9 | 15.6 | 13.9 | 7.1 | 5.0 | 7.71 | 26.1% | 12.1% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1363 | 0.5485 | 0.4093 | 0.4901 | +0.059 | -0.081 | 0.0002 ± 0.0042 |
| ratio 4-10x | 930 | 0.5788 | 0.4325 | 0.4892 | +0.090 | -0.057 | 0.009 ± 0.0052 |
| ratio <2x | 3332 | 0.5371 | 0.414 | 0.4373 | +0.100 | -0.023 | 0.0144 ± 0.0025 |
| ratio >=10x | 1149 | 0.5652 | 0.3912 | 0.4447 | +0.120 | -0.053 | 0.0152 ± 0.0053 |
| thinner_sample 1000-3000 | 1871 | 0.5388 | 0.4119 | 0.4479 | +0.091 | -0.036 | 0.0105 ± 0.0033 |
| thinner_sample 300-1000 | 1537 | 0.5653 | 0.424 | 0.4782 | +0.087 | -0.054 | 0.004 ± 0.004 |
| thinner_sample <300 | 2219 | 0.5586 | 0.39 | 0.4529 | +0.106 | -0.063 | 0.0136 ± 0.0038 |
| thinner_sample >=3000 | 1147 | 0.5306 | 0.4371 | 0.4473 | +0.083 | -0.010 | 0.0159 ± 0.0034 |
| data_status ADEQUATE | 1874 | 0.5323 | 0.4294 | 0.4392 | +0.093 | -0.010 | 0.0155 ± 0.0028 |
| data_status LIMITED | 1640 | 0.548 | 0.4149 | 0.4695 | +0.079 | -0.055 | 0.0063 ± 0.0037 |
| data_status POOR | 3260 | 0.561 | 0.4 | 0.4595 | +0.102 | -0.060 | 0.0106 ± 0.003 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 980 | 0.1974 | 0.1979 | -0.0005 ± 0.0005 | 0.5746 | 0.5758 | 0.5029 | 0.4877 | 0.5041 | -0.092 ± 0.0151 | -0.0087 (8) |
| 3-5 | 619 | 0.2028 | 0.2022 | +0.0006 ± 0.0015 | 0.5883 | 0.5847 | 0.5047 | 0.4649 | 0.4766 | -0.103 ± 0.0185 | 0.01 (2) |
| 5-10 | 1446 | 0.2006 | 0.1996 | +0.0009 ± 0.0018 | 0.5865 | 0.582 | 0.5119 | 0.4381 | 0.4661 | -0.091 ± 0.0122 | -0.0143 (7) |
| 10-15 | 1183 | 0.2186 | 0.2089 | +0.0097 ± 0.0033 | 0.6295 | 0.6013 | 0.5244 | 0.4009 | 0.4227 | -0.108 ± 0.0135 | -0.048 (5) |
| 15-25 | 1499 | 0.2246 | 0.2081 | +0.0165 ± 0.0046 | 0.6438 | 0.5998 | 0.5752 | 0.3802 | 0.4356 | -0.104 ± 0.0118 | -0.004 (10) |
| 25-40 | 863 | 0.2211 | 0.2039 | +0.0172 ± 0.0092 | 0.6308 | 0.5885 | 0.6518 | 0.3418 | 0.4693 | -0.068 ± 0.014 | -0.06 (2) |
| 40+ | 184 | 0.2944 | 0.1759 | +0.1185 ± 0.0277 | 0.7938 | 0.5247 | 0.7303 | 0.2753 | 0.3804 | -0.081 ± 0.0269 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5160 | 0.185 | 0.1859 | -0.0009 ± 0.0002 | 0.5454 | 0.5463 | 0.4883 | 0.473 | 0.5033 | -0.023 ± 0.0061 | -0.01 (28) |
| 3-5 | 3446 | 0.1958 | 0.1941 | +0.0017 ± 0.0006 | 0.5702 | 0.5639 | 0.4801 | 0.4403 | 0.4388 | -0.056 ± 0.0076 | 0.0 (3) |
| 5-10 | 7453 | 0.2005 | 0.1971 | +0.0034 ± 0.0008 | 0.5861 | 0.5746 | 0.485 | 0.4113 | 0.4255 | -0.045 ± 0.0052 | -0.0114 (22) |
| 10-15 | 6205 | 0.2014 | 0.1855 | +0.0158 ± 0.0014 | 0.5891 | 0.5449 | 0.4855 | 0.3616 | 0.3597 | -0.064 ± 0.0055 | -0.0281 (16) |
| 15-25 | 7776 | 0.2061 | 0.167 | +0.0391 ± 0.0018 | 0.6041 | 0.4964 | 0.4995 | 0.304 | 0.3026 | -0.070 ± 0.0046 | -0.0027 (45) |
| 25-40 | 6003 | 0.2225 | 0.1259 | +0.0966 ± 0.0029 | 0.6392 | 0.3872 | 0.527 | 0.2132 | 0.2207 | -0.058 ± 0.0044 | -0.0733 (3) |
| 40+ | 3983 | 0.3815 | 0.0448 | +0.3367 ± 0.0038 | 0.9936 | 0.1732 | 0.6308 | 0.1028 | 0.0598 | -0.076 ± 0.0032 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 784 | 0.2049 | 0.2053 | -0.0004 ± 0.0006 | 0.5906 | 0.5919 | 0.5062 | 0.4915 | 0.5166 | -0.101 ± 0.0175 | -0.0117 (6) |
| 3-5 | 557 | 0.2101 | 0.207 | +0.0030 ± 0.0015 | 0.6027 | 0.5962 | 0.5125 | 0.4729 | 0.4506 | -0.133 ± 0.0207 | 0.01 (2) |
| 5-10 | 1244 | 0.2054 | 0.2028 | +0.0025 ± 0.0019 | 0.5964 | 0.5888 | 0.5405 | 0.4659 | 0.4895 | -0.094 ± 0.0132 | -0.01 (4) |
| 10-15 | 1087 | 0.2105 | 0.2053 | +0.0052 ± 0.0034 | 0.6117 | 0.5958 | 0.5627 | 0.4384 | 0.483 | -0.098 ± 0.0143 | -0.04 (5) |
| 15-25 | 1581 | 0.231 | 0.2118 | +0.0192 ± 0.0045 | 0.6564 | 0.6079 | 0.5848 | 0.3894 | 0.4396 | -0.100 ± 0.0118 | -0.012 (10) |
| 25-40 | 1116 | 0.2673 | 0.1983 | +0.0691 ± 0.0084 | 0.7461 | 0.5767 | 0.6589 | 0.3447 | 0.3943 | -0.121 ± 0.0133 | -0.008 (5) |
| 40+ | 405 | 0.3682 | 0.1638 | +0.2044 ± 0.0201 | 1.0017 | 0.4941 | 0.7354 | 0.246 | 0.2963 | -0.081 ± 0.0193 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4440 | 0.1918 | 0.1921 | -0.0003 ± 0.0002 | 0.5591 | 0.5595 | 0.5084 | 0.4933 | 0.511 | -0.038 ± 0.0068 | -0.0154 (26) |
| 3-5 | 3025 | 0.1919 | 0.191 | +0.0009 ± 0.0006 | 0.56 | 0.5568 | 0.5099 | 0.4703 | 0.4774 | -0.045 ± 0.0081 | 0.01 (2) |
| 5-10 | 6655 | 0.1966 | 0.193 | +0.0036 ± 0.0008 | 0.5772 | 0.5644 | 0.5081 | 0.434 | 0.4494 | -0.042 ± 0.0055 | -0.0117 (6) |
| 10-15 | 5550 | 0.2008 | 0.19 | +0.0108 ± 0.0015 | 0.5905 | 0.5568 | 0.5116 | 0.3876 | 0.407 | -0.046 ± 0.0059 | -0.0189 (18) |
| 15-25 | 7767 | 0.217 | 0.1808 | +0.0362 ± 0.0019 | 0.6305 | 0.5303 | 0.524 | 0.3287 | 0.3367 | -0.061 ± 0.0049 | -0.0084 (43) |
| 25-40 | 7081 | 0.2506 | 0.1376 | +0.1130 ± 0.0028 | 0.7075 | 0.4203 | 0.5602 | 0.2433 | 0.2268 | -0.080 ± 0.0044 | -0.0095 (20) |
| 40+ | 5508 | 0.4001 | 0.0601 | +0.3401 ± 0.0038 | 1.0543 | 0.2155 | 0.6543 | 0.1195 | 0.0826 | -0.073 ± 0.0032 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 951 | 0.196 | 0.1975 | -0.0015 ± 0.0005 | 0.5716 | 0.5754 | 0.5019 | 0.4865 | 0.5342 | -0.050 ± 0.0151 | -0.012 (10) |
| 3-5 | 666 | 0.2043 | 0.2028 | +0.0015 ± 0.0014 | 0.5921 | 0.5866 | 0.4957 | 0.4561 | 0.4595 | -0.112 ± 0.0183 | -0.0 (4) |
| 5-10 | 1479 | 0.202 | 0.1983 | +0.0037 ± 0.0017 | 0.5885 | 0.5782 | 0.5129 | 0.4392 | 0.4496 | -0.106 ± 0.012 | -0.01 (9) |
| 10-15 | 1192 | 0.2105 | 0.2015 | +0.0090 ± 0.0032 | 0.6118 | 0.5854 | 0.5376 | 0.4145 | 0.4413 | -0.108 ± 0.013 | -0.0286 (7) |
| 15-25 | 1433 | 0.2308 | 0.2123 | +0.0184 ± 0.0047 | 0.6588 | 0.6089 | 0.5861 | 0.3919 | 0.441 | -0.110 ± 0.0122 | -0.03 (1) |
| 25-40 | 860 | 0.2114 | 0.2094 | +0.0020 ± 0.0092 | 0.6104 | 0.6013 | 0.6604 | 0.3495 | 0.5 | -0.054 ± 0.0141 | -0.0267 (3) |
| 40+ | 193 | 0.3126 | 0.1801 | +0.1325 ± 0.0275 | 0.8448 | 0.5339 | 0.7411 | 0.2864 | 0.3782 | -0.094 ± 0.028 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4974 | 0.1838 | 0.1845 | -0.0007 ± 0.0002 | 0.5417 | 0.5427 | 0.484 | 0.4686 | 0.4873 | -0.032 ± 0.0062 | -0.0137 (41) |
| 3-5 | 3510 | 0.2036 | 0.202 | +0.0016 ± 0.0006 | 0.5908 | 0.5851 | 0.4793 | 0.4399 | 0.4399 | -0.055 ± 0.0077 | -0.01 (19) |
| 5-10 | 7625 | 0.1955 | 0.1903 | +0.0051 ± 0.0007 | 0.5738 | 0.5577 | 0.4881 | 0.4141 | 0.4164 | -0.056 ± 0.005 | -0.0105 (37) |
| 10-15 | 6126 | 0.1931 | 0.1781 | +0.0150 ± 0.0013 | 0.5707 | 0.5275 | 0.4945 | 0.3712 | 0.3717 | -0.062 ± 0.0054 | -0.0146 (13) |
| 15-25 | 7877 | 0.2116 | 0.172 | +0.0397 ± 0.0018 | 0.6172 | 0.5075 | 0.5128 | 0.3184 | 0.3146 | -0.072 ± 0.0047 | -0.0533 (3) |
| 25-40 | 5981 | 0.217 | 0.1275 | +0.0895 ± 0.0029 | 0.6274 | 0.3906 | 0.5302 | 0.2146 | 0.2329 | -0.049 ± 0.0045 | -0.02 (4) |
| 40+ | 3933 | 0.3915 | 0.0498 | +0.3417 ± 0.004 | 1.0203 | 0.1858 | 0.6403 | 0.1089 | 0.0661 | -0.077 ± 0.0034 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1379 | 0.196 | 0.1961 | -0.0001 ± 0.0004 | 0.5699 | 0.57 | 0.5075 | 0.4925 | 0.4975 | -0.067 ± 0.0122 | -0.0213 (54) |
| 3-5 | 987 | 0.1886 | 0.1884 | +0.0002 ± 0.0011 | 0.5547 | 0.5528 | 0.4946 | 0.4547 | 0.4711 | -0.058 ± 0.0141 | -0.0194 (34) |
| 5-10 | 1997 | 0.1983 | 0.1937 | +0.0046 ± 0.0015 | 0.584 | 0.5697 | 0.5073 | 0.4337 | 0.4397 | -0.075 ± 0.0101 | -0.005 (78) |
| 10-15 | 1367 | 0.2139 | 0.2009 | +0.0130 ± 0.003 | 0.6198 | 0.585 | 0.5402 | 0.4174 | 0.4243 | -0.091 ± 0.0125 | 0.0014 (65) |
| 15-25 | 1790 | 0.2307 | 0.2066 | +0.0241 ± 0.0042 | 0.6582 | 0.5968 | 0.5892 | 0.3942 | 0.4324 | -0.089 ± 0.0109 | -0.0214 (59) |
| 25-40 | 1081 | 0.2401 | 0.2098 | +0.0303 ± 0.0085 | 0.6861 | 0.6023 | 0.6863 | 0.374 | 0.482 | -0.087 ± 0.013 | -0.0252 (27) |
| 40+ | 383 | 0.329 | 0.2018 | +0.1272 ± 0.022 | 0.949 | 0.5875 | 0.8153 | 0.3383 | 0.4595 | -0.097 ± 0.0206 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5064 | 0.1768 | 0.177 | -0.0002 ± 0.0002 | 0.523 | 0.523 | 0.5122 | 0.497 | 0.5089 | -0.037 ± 0.006 | -0.0145 (98) |
| 3-5 | 3498 | 0.1945 | 0.1938 | +0.0007 ± 0.0006 | 0.5669 | 0.5651 | 0.5007 | 0.461 | 0.4723 | -0.039 ± 0.0075 | -0.0204 (72) |
| 5-10 | 7089 | 0.1953 | 0.1888 | +0.0065 ± 0.0008 | 0.5756 | 0.557 | 0.5009 | 0.4273 | 0.4215 | -0.063 ± 0.0052 | -0.0084 (134) |
| 10-15 | 4883 | 0.209 | 0.1927 | +0.0163 ± 0.0016 | 0.6081 | 0.5659 | 0.5365 | 0.4135 | 0.4073 | -0.072 ± 0.0064 | -0.0053 (106) |
| 15-25 | 5931 | 0.23 | 0.1987 | +0.0313 ± 0.0023 | 0.6611 | 0.5764 | 0.5746 | 0.3792 | 0.3979 | -0.067 ± 0.0058 | -0.026 (108) |
| 25-40 | 3917 | 0.2572 | 0.1889 | +0.0682 ± 0.0044 | 0.7279 | 0.5509 | 0.638 | 0.3254 | 0.3753 | -0.069 ± 0.0068 | -0.0246 (52) |
| 40+ | 1724 | 0.3722 | 0.1585 | +0.2137 ± 0.0099 | 1.051 | 0.4723 | 0.7433 | 0.2422 | 0.29 | -0.066 ± 0.0091 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 6774 | 1.044 ± 0.034 | 1.116 | 0.1694 | 0.1689 | 0.214 | 0.203 |
| gen2 | 6774 | 0.837 ± 0.031 | 1.087 | 0.1736 | 0.1692 | 0.2325 | 0.2029 |
| gen1_elo | 6774 | 1.019 ± 0.033 | 1.106 | 0.1759 | 0.169 | 0.2133 | 0.2031 |
| gen1_sr | 6774 | 1.022 ± 0.04 | 1.15 | 0.1334 | 0.1709 | 0.2287 | 0.2026 |
| gen1_ledger | 8984 | 0.875 ± 0.025 | 1.084 | 0.1898 | 0.1767 | 0.2163 | 0.1994 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 32,140)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 7,441 | 23.2% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,110 | 22.1% |
| BOOK_QUALITY | execution | 5,862 | 18.2% |
| POOR_DATA | data | 3,765 | 11.7% |
| LIMITED_DATA | data | 2,009 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,832 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,346 | 4.2% |
| IDENTITY_AMBIGUOUS | mapping | 1,320 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 919 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 535 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 23.2%, coverage 22.1%, execution 18.2%, data 18.0%, market_freshness/coverage 8.6%, model_calibration_or_unknown 4.2%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.5%, LOW_DATA_QUALITY 71.6%, THIN_PLAYER_HISTORY 59.9%, STALE_PLAYER_DATA 52.3%, STALE_KALSHI_QUOTE 45.5%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 24.4%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 15.4%, LEVEL_TRANSFER_RISK 10.2%, LOW_DISPLAYED_LIQUIDITY 8.3%, EVENT_MAPPING_RISK 7.3%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.6%, POST_SETTLEMENT_OBSERVATION 22.1%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 17,063)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,711 | 33.5% |
| STALE_QUOTE | market_freshness | 3,341 | 19.6% |
| BOOK_QUALITY | execution | 3,048 | 17.9% |
| POOR_DATA | data | 1,604 | 9.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 977 | 5.7% |
| IDENTITY_AMBIGUOUS | mapping | 728 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 603 | 3.5% |
| LIMITED_DATA | data | 586 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 332 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 132 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.5%, market_freshness 19.6%, execution 17.9%, data 12.8%, market_freshness/coverage 9.3%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 96.9%, LOW_DATA_QUALITY 75.1%, THIN_PLAYER_HISTORY 62.1%, STALE_KALSHI_QUOTE 52.9%, STALE_PLAYER_DATA 46.3%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 23.9%, MODEL_HIGH_UNCERTAINTY 19.2%, PLAYER_IDENTITY_RISK 18.5%, LEVEL_TRANSFER_RISK 9.0%, EVENT_MAPPING_RISK 8.9%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.5%, POST_SETTLEMENT_OBSERVATION 33.5%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 13587, "IDENTITY_AMBIGUOUS": 3476}; ticker orientation: {"VERIFIED": 17063}.

Checks: discipline:AMBIGUOUS 1150, discipline:PASS 15913, identity_confidence:AMBIGUOUS 3152, identity_confidence:PASS 13911, level_mapping:NA 1162, level_mapping:PASS 15901, market_pair:AMBIGUOUS 485, market_pair:NA 372, market_pair:PASS 16206, model_complement:NA 334, model_complement:PASS 16729, namesake:AMBIGUOUS 6, namesake:PASS 17057, physical_match_id:NA 5877, physical_match_id:PASS 11186, player_ids:PASS 17063, same_pair_other_event:PASS 17063, ticker_orientation:PASS 17063

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,222 | 3.8% | 3.3% | 1.4% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 21, "market_freshness/coverage": 17} | 5.54 | 0.2268 / 0.2211 (779) | 24.5% | 2.5% | 3.1% | 2.8% |
| CHALLENGER | 11,249 | 16.2% | 6.2% | 10.7% | {"coverage": 1067, "market_freshness/coverage": 215, "market_freshness": 214, "data": 157, "model_calibration_or_unknown": 77, "execution": 41, "model_calibration": 36, "mapping": 17, "possible_market_error": 1} | 7.37 | 0.2202 / 0.2095 (2620) | 37.5% | 15.6% | 4.1% | 22.3% |
| DOUBLES | 2,458 | 46.8% | 46.7% | 6.7% | {"execution": 655, "mapping": 318, "market_freshness": 106, "market_freshness/coverage": 64, "coverage": 7} | 23.54 | 0.301 / 0.2348 (590) | 9.5% | 0.0% | 100.0% | 6.0% |
| ITF_MEN | 22,321 | 24.8% | 17.5% | 32.5% | {"coverage": 1900, "market_freshness": 1075, "execution": 970, "data": 830, "market_freshness/coverage": 555, "mapping": 202, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.68 | 0.2151 / 0.1971 (4651) | 39.2% | 69.2% | 15.5% | 21.0% |
| ITF_WOMEN | 29,278 | 26.4% | 19.0% | 45.2% | {"coverage": 2661, "market_freshness": 1687, "execution": 1299, "data": 1102, "market_freshness/coverage": 672, "mapping": 185, "model_calibration_or_unknown": 91, "model_calibration": 22} | 12.52 | 0.2019 / 0.1926 (5570) | 40.5% | 57.3% | 9.9% | 21.2% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,710 | 6.1% | 5.2% | 1.7% | {"market_freshness": 110, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 21, "market_freshness/coverage": 13, "mapping": 1} | 7.7 | 0.2316 / 0.2233 (752) | 29.6% | 2.1% | 1.3% | 3.6% |
| WTA125 | 2,570 | 11.3% | 9.8% | 1.7% | {"market_freshness": 90, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 19, "coverage": 14, "mapping": 4} | 9.17 | 0.2069 / 0.1902 (754) | 28.8% | 10.7% | 4.2% | 7.3% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 17.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 1025 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 3 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 4 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 5 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 6 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 172 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 7 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 769 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 8 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 164 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 9 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 10 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 13 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 14 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 17 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 18 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 19 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 20 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 21 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 22 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 23 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 24 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 25 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 26 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 27 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 28 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 29 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 30 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 31 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 32 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 33 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 34 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 35 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 36 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 37 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 38 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 39 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 213 min (STALE); no external reference |
| 40 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 41 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 42 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 43 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 44 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 720 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 45 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 46 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 163 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |
| 47 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXATPCHALLENGERMATCH-26NOV02TOBSTO-TOB` | CHALLENGER | fair_v1 | 80% / 2% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 165 min (STALE); data POOR (grade F, thinner serve sample 159.0, ratio 20.58); no external reference |
| 49 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 50 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9693, "by_level_share_of_ge_25pp": {"ATP": 0.0139, "CHALLENGER": 0.107, "DOUBLES": 0.0674, "ITF_MEN": 0.3247, "ITF_WOMEN": 0.4524, "OTHER": 0.0007, "WTA": 0.0169, "WTA125": 0.0171}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5293, "share_primary_cause_market_settled_or_in_play": 0.4273, "share_primary_cause_stale_quote_only": 0.1958}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 17063, "identity_ambiguous_share": 0.2037, "ticker_orientation": {"VERIFIED": 17063}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 11186, "with_external": 601, "coverage": 0.0537, "external_status": {"EXTERNAL_STALE": 384, "AGREES_WITH_KALSHI": 204, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 384, "MODEL_LONE_OUTLIER": 204, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3394, "share_external_supports_model": 0.0216}, "pregame_clean_ge_25pp": {"n": 5354, "with_external": 571, "coverage": 0.1066, "external_status": {"EXTERNAL_STALE": 361, "AGREES_WITH_KALSHI": 197, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 361, "MODEL_LONE_OUTLIER": 197, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.345, "share_external_supports_model": 0.0228}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 479.0, "median_sample_ratio": 2.46, "median_min_matches": 19.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.21, "data_status": {"POOR": 9627, "LIMITED": 4414, "ADEQUATE": 3022}, "comparison_lt_10pp": {"median_thinner_serve_points": 1719.0, "median_sample_ratio": 1.7, "median_min_matches": 89.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1363, "model_minus_observed": 0.0585, "kalshi_minus_observed": -0.0808, "brier_diff_model_minus_kalshi": 0.0002}, "4-10x": {"n": 930, "model_minus_observed": 0.0896, "kalshi_minus_observed": -0.0568, "brier_diff_model_minus_kalshi": 0.009}, "<2x": {"n": 3332, "model_minus_observed": 0.0998, "kalshi_minus_observed": -0.0233, "brier_diff_model_minus_kalshi": 0.0144}, ">=10x": {"n": 1149, "model_minus_observed": 0.1204, "kalshi_minus_observed": -0.0535, "brier_diff_model_minus_kalshi": 0.0152}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 6774, "model": {"intercept": -0.563, "slope": 0.837, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.189, "slope": 1.087, "slope_se": 0.035}, "mean_extremity_model": 0.1736, "mean_extremity_kalshi": 0.1692, "model_brier": 0.2325, "kalshi_brier": 0.2029, "brier_diff_model_minus_kalshi": 0.0296, "brier_diff_se": 0.0023, "model_logloss": 0.6616, "kalshi_logloss": 0.5877}, "fair_v1": {"n": 6774, "model": {"intercept": -0.454, "slope": 1.044, "slope_se": 0.034}, "kalshi_mid_same_rows": {"intercept": 0.256, "slope": 1.116, "slope_se": 0.035}, "mean_extremity_model": 0.1694, "mean_extremity_kalshi": 0.1689, "model_brier": 0.214, "kalshi_brier": 0.203, "brier_diff_model_minus_kalshi": 0.0109, "brier_diff_se": 0.0019, "model_logloss": 0.6164, "kalshi_logloss": 0.5879}, "gen1_elo": {"n": 6774, "model": {"intercept": -0.441, "slope": 1.019, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.258, "slope": 1.106, "slope_se": 0.034}, "mean_extremity_model": 0.1759, "mean_extremity_kalshi": 0.169, "model_brier": 0.2133, "kalshi_brier": 0.2031, "brier_diff_model_minus_kalshi": 0.0102, "brier_diff_se": 0.0019, "model_logloss": 0.6156, "kalshi_logloss": 0.5881}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2456, "share_ge_15": 0.4417, "median_abs_gap": 12.99, "n": 45544}, "gen1_elo": {"share_ge_25": 0.2429, "share_ge_15": 0.438, "median_abs_gap": 12.74, "n": 45544}, "gen1_sr": {"share_ge_25": 0.3119, "share_ge_15": 0.519, "median_abs_gap": 15.76, "n": 45544}, "gen2": {"share_ge_25": 0.3129, "share_ge_15": 0.5083, "median_abs_gap": 15.38, "n": 45544}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1514, "share_ge_15": 0.354, "median_abs_gap": 10.71, "n": 35358}, "gen1_elo": {"share_ge_25": 0.1496, "share_ge_15": 0.349, "median_abs_gap": 10.49, "n": 35358}, "gen1_sr": {"share_ge_25": 0.2174, "share_ge_15": 0.4404, "median_abs_gap": 13.01, "n": 35360}, "gen2": {"share_ge_25": 0.232, "share_ge_15": 0.4392, "median_abs_gap": 12.86, "n": 35360}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.54, "share_ge_25_all": 0.0381, "share_ge_25_pregame_clean": 0.0329}, "WTA": {"median_abs_gap_pregame_clean": 7.7, "share_ge_25_all": 0.0614, "share_ge_25_pregame_clean": 0.052}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2374, "share_within_10pp_all": 0.4398, "share_within_10pp_pregame_clean": 0.4916, "corr_model_vs_mid_pregame_clean": 0.8513}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 980, "model_brier": 0.1974, "kalshi_brier": 0.1979, "brier_diff_model_minus_kalshi": -0.0005}, "10-15": {"n_settled": 1183, "model_brier": 0.2186, "kalshi_brier": 0.2089, "brier_diff_model_minus_kalshi": 0.0097}, "15-25": {"n_settled": 1499, "model_brier": 0.2246, "kalshi_brier": 0.2081, "brier_diff_model_minus_kalshi": 0.0165}, "25-40": {"n_settled": 863, "model_brier": 0.2211, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0172}, "3-5": {"n_settled": 619, "model_brier": 0.2028, "kalshi_brier": 0.2022, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 184, "model_brier": 0.2944, "kalshi_brier": 0.1759, "brier_diff_model_minus_kalshi": 0.1185}, "5-10": {"n_settled": 1446, "model_brier": 0.2006, "kalshi_brier": 0.1996, "brier_diff_model_minus_kalshi": 0.0009}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.563, "slope": 0.837, "slope_se": 0.031}, "kalshi_slope": {"intercept": 0.189, "slope": 1.087, "slope_se": 0.035}, "n": 6774}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.492, "slope": 0.875, "slope_se": 0.025}, "kalshi_slope": {"intercept": 0.175, "slope": 1.084, "slope_se": 0.029}, "n": 8984}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 590, "model_brier": 0.301, "kalshi_brier": 0.2348, "brier_diff_model_minus_kalshi": 0.0662, "brier_diff_se": 0.0122, "corr_model_outcome": 0.086, "corr_kalshi_outcome": 0.2617}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
