# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-27T23:44Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 61,805): 0-3 14.0%, 3-5 9.5%, 5-10 19.9%, 10-15 15.4%, 15-25 19.1%, 25-40 14.0%, 40+ 8.0%; median gap 11.97 pp.
* **Where the extremes live**: 96.8% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.8%, Challenger 11.7%, doubles 6.5%). Main tour: ATP 4.4% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 13,617): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.6%, BOOK_QUALITY 18.9%, STALE_QUOTE 18.7%, POOR_DATA 9.1%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IDENTITY_AMBIGUOUS 4.2%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.6%, execution 18.9%, market_freshness 18.7%, data 12.5%, market_freshness/coverage 9.0%, mapping 4.2%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 51.5% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.6% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 13,617 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.3% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.1%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.9% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 455.0 points vs 1754.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.029, Gen-2 0.813, Gen-1 ledger 0.862 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 646 model 0.2216 vs Kalshi 0.2089; n 134 model 0.2706 vs Kalshi 0.2006.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 268,584 model-market comparisons (435,725 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 89,681 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-27T23:33:11.760406+00:00'], shadow board 70,972 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-27T23:33:15.317197+00:00'], Model 4 34,531 rows, 22,131 settled tickers, 7,882 tickers with an external scan.
* By model: {"gen1_ledger": 60916, "gen1_elo": 35685, "fair_v1": 35685, "gen2": 35685, "gen1_sr": 35685, "model4_fundamental": 32486, "model4_conditioned": 32442}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 61,805 | 14.0 | 9.5 | 19.9 | 15.4 | 19.1 | 14.0 | 8.0 | 11.97 | 41.1% | 22.0% |
| MW fair_v1 | 35,685 | 12.9 | 8.7 | 18.5 | 15.5 | 19.6 | 15.0 | 9.8 | 13.08 | 44.4% | 24.8% |
| MW gen1_elo | 35,685 | 12.7 | 8.5 | 19.3 | 15.4 | 19.6 | 14.8 | 9.7 | 12.92 | 44.1% | 24.5% |
| MW gen1_ledger | 26,120 | 15.6 | 10.7 | 21.8 | 15.2 | 18.5 | 12.6 | 5.6 | 10.47 | 36.7% | 18.3% |
| MW gen1_sr | 35,685 | 10.2 | 7.1 | 16.8 | 13.5 | 20.8 | 18.7 | 12.8 | 15.97 | 52.3% | 31.5% |
| MW gen2 | 35,685 | 11.1 | 7.5 | 16.3 | 13.8 | 19.5 | 18.0 | 13.9 | 15.58 | 51.4% | 31.9% |
| all families model4_conditioned | 32,442 | 22.1 | 18.2 | 34.5 | 17.4 | 4.8 | 1.9 | 1.1 | 6.05 | 7.8% | 3.0% |
| all families model4_fundamental | 32,486 | 17.0 | 13.2 | 34.1 | 20.4 | 10.2 | 3.7 | 1.4 | 7.75 | 15.3% | 5.1% |

Configurable thresholds (primary): >=5pp 76.4%, >=10pp 56.5%, >=15pp 41.1%, >=20pp 30.6%, >=25pp 22.0%, >=30pp 15.9%, >=40pp 8.0%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.35pp; >=10pp 44.9%, >=25pp 17.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,231 | 27.0 | 15.7 | 27.1 | 13.9 | 11.5 | 4.2 | 0.6 | 5.93 | 16.4% | 4.8% |
| CHALLENGER | 5,635 | 16.0 | 9.8 | 20.1 | 15.7 | 15.5 | 12.1 | 10.8 | 11.15 | 38.4% | 22.9% |
| ITF_MEN | 9,609 | 9.9 | 7.1 | 16.4 | 15.0 | 21.5 | 17.8 | 12.3 | 15.53 | 51.5% | 30.0% |
| ITF_WOMEN | 13,919 | 9.6 | 6.9 | 15.9 | 15.2 | 22.1 | 18.4 | 11.9 | 15.74 | 52.4% | 30.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,308 | 17.2 | 13.8 | 24.9 | 20.4 | 16.6 | 6.6 | 0.6 | 8.39 | 23.8% | 7.2% |
| WTA125 | 977 | 15.2 | 7.2 | 23.2 | 19.6 | 20.8 | 12.3 | 1.7 | 11.03 | 34.8% | 14.0% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,231 | 25.4 | 15.5 | 25.3 | 16.8 | 11.9 | 4.2 | 0.8 | 6.31 | 17.0% | 5.0% |
| CHALLENGER | 5,635 | 15.1 | 8.8 | 17.8 | 14.7 | 18.1 | 13.9 | 11.8 | 12.79 | 43.7% | 25.6% |
| ITF_MEN | 9,609 | 7.9 | 6.0 | 14.2 | 13.0 | 19.9 | 21.2 | 17.8 | 18.79 | 58.9% | 39.0% |
| ITF_WOMEN | 13,919 | 7.9 | 5.6 | 14.0 | 12.8 | 20.6 | 21.5 | 17.6 | 19.36 | 59.7% | 39.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,308 | 14.5 | 10.8 | 22.1 | 15.8 | 22.4 | 12.9 | 1.5 | 10.8 | 36.8% | 14.4% |
| WTA125 | 977 | 8.2 | 6.0 | 17.0 | 17.0 | 25.0 | 18.0 | 8.8 | 15.85 | 51.8% | 26.8% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,231 | 22.7 | 12.7 | 24.6 | 16.1 | 16.2 | 6.5 | 1.4 | 7.58 | 24.0% | 7.9% |
| CHALLENGER | 5,635 | 14.6 | 9.1 | 21.2 | 15.9 | 15.8 | 12.4 | 11.0 | 11.39 | 39.2% | 23.4% |
| ITF_MEN | 9,609 | 9.6 | 7.0 | 16.7 | 14.2 | 21.9 | 18.2 | 12.4 | 15.99 | 52.5% | 30.6% |
| ITF_WOMEN | 13,919 | 9.3 | 6.7 | 16.5 | 15.9 | 22.2 | 18.1 | 11.2 | 15.51 | 51.6% | 29.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,308 | 23.7 | 16.2 | 31.8 | 15.0 | 9.7 | 2.5 | 1.1 | 6.12 | 13.3% | 3.5% |
| WTA125 | 977 | 22.4 | 12.2 | 26.8 | 16.6 | 15.2 | 6.5 | 0.4 | 7.99 | 22.0% | 6.9% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,878 | 24.6 | 19.1 | 30.7 | 12.8 | 9.1 | 3.1 | 0.5 | 5.74 | 12.7% | 3.7% |
| CHALLENGER | 3,844 | 22.2 | 14.4 | 26.9 | 14.8 | 14.0 | 6.2 | 1.6 | 7.2 | 21.7% | 7.8% |
| DOUBLES | 1,883 | 5.1 | 4.6 | 12.2 | 10.5 | 20.8 | 25.3 | 21.7 | 23.81 | 67.7% | 46.9% |
| ITF_MEN | 7,270 | 13.0 | 9.1 | 20.2 | 16.0 | 21.8 | 13.7 | 6.3 | 12.24 | 41.8% | 20.0% |
| ITF_WOMEN | 8,735 | 12.9 | 8.9 | 19.6 | 15.5 | 21.3 | 16.0 | 5.8 | 12.57 | 43.2% | 21.9% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,370 | 23.9 | 15.5 | 30.1 | 17.7 | 9.6 | 2.9 | 0.3 | 6.79 | 12.8% | 3.2% |
| WTA125 | 991 | 23.7 | 13.0 | 20.9 | 18.8 | 13.8 | 8.0 | 1.8 | 8.14 | 23.6% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,142 | 27.3 | 15.8 | 27.5 | 13.8 | 11.4 | 3.9 | 0.4 | 5.91 | 15.6% | 4.3% |
| CHALLENGER | 3,957 | 20.9 | 12.4 | 25.0 | 18.2 | 15.4 | 6.4 | 1.6 | 8.27 | 23.4% | 7.9% |
| ITF_MEN | 7,102 | 12.0 | 8.6 | 19.7 | 17.0 | 22.6 | 14.6 | 5.4 | 12.82 | 42.7% | 20.1% |
| ITF_WOMEN | 10,453 | 11.4 | 8.2 | 18.3 | 17.3 | 24.0 | 15.4 | 5.4 | 13.46 | 44.8% | 20.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,239 | 17.4 | 13.8 | 25.0 | 20.6 | 16.6 | 6.1 | 0.6 | 8.28 | 23.3% | 6.7% |
| WTA125 | 944 | 15.5 | 7.0 | 22.9 | 19.9 | 21.3 | 12.0 | 1.5 | 11.03 | 34.8% | 13.5% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,142 | 25.6 | 15.8 | 25.4 | 16.8 | 11.9 | 4.0 | 0.5 | 6.23 | 16.3% | 4.4% |
| CHALLENGER | 3,957 | 19.4 | 11.1 | 22.3 | 17.2 | 18.5 | 9.5 | 1.9 | 9.2 | 29.9% | 11.5% |
| ITF_MEN | 7,103 | 9.3 | 7.2 | 16.5 | 15.1 | 21.7 | 19.4 | 10.8 | 15.61 | 51.9% | 30.2% |
| ITF_WOMEN | 10,454 | 9.0 | 6.4 | 15.6 | 14.2 | 22.7 | 20.9 | 11.1 | 16.88 | 54.7% | 32.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,239 | 14.6 | 10.8 | 22.2 | 15.8 | 22.6 | 12.7 | 1.3 | 10.78 | 36.6% | 14.0% |
| WTA125 | 944 | 8.2 | 6.0 | 17.1 | 17.3 | 25.0 | 18.3 | 8.2 | 15.68 | 51.5% | 26.5% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,825 | 24.8 | 19.3 | 30.7 | 13.0 | 8.7 | 3.0 | 0.4 | 5.67 | 12.2% | 3.5% |
| CHALLENGER | 3,388 | 23.6 | 15.3 | 28.1 | 14.8 | 13.4 | 4.2 | 0.4 | 6.62 | 18.0% | 4.7% |
| DOUBLES | 1,763 | 5.0 | 4.7 | 12.4 | 10.6 | 20.6 | 25.2 | 21.4 | 23.62 | 67.3% | 46.6% |
| ITF_MEN | 6,173 | 13.9 | 9.7 | 21.8 | 16.7 | 21.8 | 12.1 | 4.0 | 11.34 | 37.9% | 16.1% |
| ITF_WOMEN | 7,374 | 13.6 | 9.3 | 20.9 | 16.3 | 21.4 | 14.9 | 3.6 | 11.7 | 39.9% | 18.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,316 | 24.3 | 15.9 | 30.1 | 17.8 | 9.6 | 2.3 | 0.1 | 6.68 | 11.9% | 2.4% |
| WTA125 | 872 | 25.3 | 13.9 | 22.0 | 19.9 | 12.6 | 5.6 | 0.6 | 7.33 | 18.8% | 6.2% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,883 | 5.1 | 4.6 | 12.2 | 10.5 | 20.8 | 25.3 | 21.7 | 23.81 | 67.7% | 46.9% |
| singles | 24,237 | 16.4 | 11.2 | 22.5 | 15.6 | 18.3 | 11.6 | 4.4 | 9.97 | 34.3% | 16.0% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,509 | 12.9 | 9.3 | 19.9 | 15.7 | 19.0 | 13.9 | 9.2 | 12.51 | 42.1% | 23.1% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 22,939 | 13.4 | 8.8 | 18.4 | 15.2 | 19.4 | 15.2 | 9.7 | 13.02 | 44.2% | 24.9% |
| UNKNOWN | 4,988 | 10.6 | 7.3 | 17.0 | 16.8 | 21.1 | 16.1 | 11.2 | 14.26 | 48.4% | 27.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 10,206 | 19.7 | 12.4 | 22.1 | 16.0 | 14.8 | 9.2 | 5.9 | 8.77 | 29.8% | 15.1% |
| B | 4,384 | 12.6 | 8.6 | 19.0 | 16.4 | 19.5 | 13.0 | 10.9 | 12.79 | 43.3% | 23.9% |
| C | 4,950 | 11.9 | 8.9 | 19.7 | 15.9 | 19.1 | 14.4 | 10.1 | 12.93 | 43.6% | 24.5% |
| D | 5,464 | 12.2 | 8.0 | 17.5 | 15.5 | 21.3 | 15.9 | 9.6 | 13.83 | 46.8% | 25.5% |
| F | 10,681 | 7.4 | 5.5 | 14.9 | 14.6 | 23.5 | 21.3 | 13.0 | 17.96 | 57.7% | 34.2% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,279 | 24.0 | 15.8 | 28.7 | 15.1 | 11.1 | 3.9 | 1.4 | 6.52 | 16.3% | 5.2% |
| B | 3,560 | 16.7 | 10.0 | 24.2 | 16.3 | 19.4 | 10.1 | 3.3 | 9.81 | 32.8% | 13.4% |
| C | 5,004 | 11.0 | 7.5 | 19.2 | 14.6 | 21.3 | 15.9 | 10.5 | 13.96 | 47.7% | 26.4% |
| D | 3,674 | 14.4 | 9.8 | 20.6 | 15.6 | 20.5 | 13.4 | 5.7 | 11.55 | 39.6% | 19.1% |
| F | 6,603 | 9.8 | 8.2 | 15.4 | 15.0 | 22.9 | 20.7 | 7.9 | 15.77 | 51.5% | 28.6% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 11,593 | 17.9 | 11.1 | 21.2 | 15.8 | 15.3 | 10.1 | 8.5 | 9.95 | 33.9% | 18.6% |
| LIMITED | 7,592 | 13.7 | 10.0 | 20.1 | 16.4 | 19.4 | 13.2 | 7.2 | 11.86 | 39.8% | 20.5% |
| POOR | 16,500 | 9.0 | 6.4 | 15.9 | 14.9 | 22.6 | 19.3 | 11.8 | 16.29 | 53.8% | 31.1% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,090 | 24.3 | 18.4 | 33.3 | 14.7 | 6.3 | 2.6 | 0.3 | 5.78 | 9.3% | 2.9% |
| GAME_SPREAD | 5,585 | 22.2 | 15.3 | 33.1 | 16.9 | 9.1 | 2.8 | 0.5 | 6.73 | 12.4% | 3.3% |
| MATCH_WINNER | 26,120 | 15.6 | 10.7 | 21.8 | 15.2 | 18.5 | 12.6 | 5.6 | 10.47 | 36.7% | 18.3% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 12,866 | 27.6 | 16.6 | 31.1 | 12.6 | 9.3 | 2.4 | 0.3 | 5.68 | 12.0% | 2.7% |
| TOTAL_GAMES | 9,231 | 9.2 | 10.2 | 36.1 | 27.1 | 10.6 | 4.0 | 2.8 | 9.36 | 17.5% | 6.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,551 | 24.5 | 30.6 | 32.9 | 7.0 | 3.9 | 0.8 | 0.2 | 4.67 | 5.0% | 1.0% |
| GAME_SPREAD | 7,591 | 46.8 | 16.4 | 25.7 | 7.4 | 1.9 | 1.2 | 0.6 | 3.31 | 3.7% | 1.8% |
| TOTAL_GAMES | 13,300 | 5.8 | 8.6 | 40.8 | 32.1 | 7.3 | 3.1 | 2.2 | 9.42 | 12.7% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,562 | 23.8 | 16.9 | 35.0 | 14.3 | 7.2 | 2.5 | 0.4 | 6.03 | 10.1% | 2.9% |
| GAME_SPREAD | 7,594 | 19.7 | 13.4 | 28.4 | 20.6 | 12.4 | 4.4 | 1.1 | 7.84 | 17.8% | 5.5% |
| TOTAL_GAMES | 13,330 | 9.5 | 9.9 | 36.6 | 25.6 | 11.7 | 4.3 | 2.5 | 9.28 | 18.4% | 6.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 35,685 | 44.4% | 24.8% | 13.08 | 35.9% | 15.5% | 10.85 |
| gen1_elo | 35,685 | 44.1% | 24.5% | 12.92 | 35.5% | 15.5% | 10.65 |
| gen1_sr | 35,685 | 52.3% | 31.5% | 15.97 | 44.6% | 22.2% | 13.04 |
| gen2 | 35,685 | 51.4% | 31.9% | 15.58 | 44.6% | 23.9% | 13.06 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 17,703 | 15.6 | 10.5 | 21.3 | 17.3 | 20.1 | 12.0 | 3.3 | 10.72 | 35.3% | 15.3% |
| STALE | 17,982 | 10.3 | 6.9 | 15.8 | 13.8 | 19.1 | 18.0 | 16.1 | 16.46 | 53.2% | 34.2% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 19,588 | 16.4 | 11.1 | 22.5 | 15.3 | 17.8 | 12.1 | 4.8 | 10.01 | 34.7% | 16.9% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 61,805 | 19588 | 21175 | 21042 | 24.1 | 123.5 | 1400.4 |
| ge_15pp | 25,424 | 6798 | 7545 | 11081 | 26.6 | 429.8 | 1399.2 |
| ge_25pp | 13,617 | 3307 | 3295 | 7015 | 31.4 | 574.8 | 1380.4 |
| lt_10pp | 26,865 | 9784 | 10013 | 7068 | 22.4 | 47.0 | 1341.5 |

Current slate `SL-20261027T234449Z-670761c3`: 768 priced rows, quote age at build {'median': 12.0, 'max': 12.0}, freshness {'AGING': 768}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 38 | 0.0 | 0.0 | 31.6 | 7.9 | 39.5 | 21.1 | 0.0 | 20.05 | 60.5% | 21.1% |
| EXTERNAL_LONE_OUTLIER | 19 | 79.0 | 21.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,490 | 19.9 | 11.2 | 25.0 | 18.3 | 17.8 | 7.1 | 0.7 | 8.71 | 25.7% | 7.9% |
| KALSHI_LONE_OUTLIER | 22 | 4.5 | 4.5 | 77.3 | 4.5 | 4.5 | 4.5 | 0.0 | 6.16 | 9.1% | 4.5% |
| MARKETS_AGREE | 689 | 65.3 | 34.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.23 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,489 | 0.0 | 2.5 | 34.9 | 26.8 | 24.9 | 10.3 | 0.7 | 12.24 | 35.8% | 10.9% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 35,685 | 5747 (16.1%) | 25.9% | 1.0% | {"EXTERNAL_STALE": 3490, "AGREES_WITH_KALSHI": 1489, "ALL_AGREE": 689, "SUPPORTS_MODEL_DIRECTION": 37, "AGREES_WITH_MODEL": 22, "EXTERNAL_OUTLIER": 19, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 15,827 | 1455 (9.2%) | 36.6% | 1.7% | {"EXTERNAL_STALE": 897, "AGREES_WITH_KALSHI": 533, "SUPPORTS_MODEL_DIRECTION": 23, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 8,848 | 447 (5.1%) | 36.5% | 2.0% | {"EXTERNAL_STALE": 275, "AGREES_WITH_KALSHI": 163, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,320 | 423 (9.8%) | 36.9% | 2.1% | {"EXTERNAL_STALE": 258, "AGREES_WITH_KALSHI": 156, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 14,312 | 3249 (22.7%) | 17.1% | 0.9% | {"EXTERNAL_STALE": 1953, "ALL_AGREE": 689, "AGREES_WITH_KALSHI": 557, "EXTERNAL_OUTLIER": 19, "AGREES_WITH_MODEL": 19, "SUPPORTS_MODEL_DIRECTION": 11, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 6,890 | 10.4 | 7.5 | 19.3 | 14.7 | 21.8 | 16.4 | 9.9 | 14.13 | 48.2% | 26.3% |
| 4-10x | 4,691 | 11.1 | 8.5 | 18.6 | 15.4 | 21.6 | 14.8 | 10.0 | 13.74 | 46.3% | 24.7% |
| <2x | 18,218 | 15.1 | 10.0 | 19.2 | 16.3 | 17.4 | 13.1 | 8.8 | 11.66 | 39.3% | 21.9% |
| >=10x | 5,886 | 10.6 | 6.1 | 15.3 | 14.2 | 21.9 | 19.4 | 12.6 | 16.48 | 53.9% | 32.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 9,013 | 12.9 | 8.4 | 19.2 | 16.3 | 19.2 | 13.5 | 10.4 | 12.82 | 43.1% | 23.9% |
| 300-1000 | 7,489 | 11.8 | 8.8 | 17.4 | 15.3 | 20.4 | 16.6 | 9.7 | 13.79 | 46.6% | 26.2% |
| <300 | 11,661 | 8.3 | 5.7 | 15.3 | 14.8 | 23.0 | 20.2 | 12.7 | 17.1 | 55.9% | 32.9% |
| >=3000 | 7,522 | 21.1 | 13.6 | 23.6 | 16.0 | 13.8 | 7.2 | 4.6 | 7.69 | 25.6% | 11.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1000 | 0.5508 | 0.4129 | 0.503 | +0.048 | -0.090 | -0.0031 ± 0.0049 |
| ratio 4-10x | 682 | 0.5861 | 0.4383 | 0.4941 | +0.092 | -0.056 | 0.0094 ± 0.0061 |
| ratio <2x | 2465 | 0.5374 | 0.4146 | 0.4483 | +0.089 | -0.034 | 0.0108 ± 0.0029 |
| ratio >=10x | 892 | 0.5708 | 0.3947 | 0.4552 | +0.116 | -0.060 | 0.0113 ± 0.0061 |
| thinner_sample 1000-3000 | 1354 | 0.538 | 0.4118 | 0.4513 | +0.087 | -0.040 | 0.0086 ± 0.0039 |
| thinner_sample 300-1000 | 1122 | 0.5699 | 0.4268 | 0.4938 | +0.076 | -0.067 | 0.0006 ± 0.0048 |
| thinner_sample <300 | 1709 | 0.5615 | 0.3936 | 0.4617 | +0.100 | -0.068 | 0.0098 ± 0.0043 |
| thinner_sample >=3000 | 854 | 0.5353 | 0.4413 | 0.4649 | +0.070 | -0.024 | 0.013 ± 0.0039 |
| data_status ADEQUATE | 1433 | 0.536 | 0.4328 | 0.4501 | +0.086 | -0.017 | 0.0125 ± 0.0032 |
| data_status LIMITED | 1170 | 0.5494 | 0.4164 | 0.4872 | +0.062 | -0.071 | 0.0026 ± 0.0044 |
| data_status POOR | 2436 | 0.5639 | 0.4017 | 0.4663 | +0.098 | -0.065 | 0.0079 ± 0.0035 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 741 | 0.2011 | 0.2016 | -0.0005 ± 0.0006 | 0.5823 | 0.5835 | 0.5026 | 0.4876 | 0.5128 | -0.085 ± 0.0176 | -0.01 (5) |
| 3-5 | 456 | 0.2051 | 0.2054 | -0.0003 ± 0.0017 | 0.5935 | 0.5928 | 0.5046 | 0.4647 | 0.4868 | -0.095 ± 0.0218 | 0.02 (1) |
| 5-10 | 1041 | 0.2033 | 0.2035 | -0.0003 ± 0.0021 | 0.5929 | 0.5913 | 0.5141 | 0.4402 | 0.4755 | -0.089 ± 0.0145 | -0.0167 (6) |
| 10-15 | 884 | 0.2209 | 0.2114 | +0.0095 ± 0.0039 | 0.6345 | 0.607 | 0.5294 | 0.4055 | 0.4276 | -0.110 ± 0.0156 | -0.048 (5) |
| 15-25 | 1137 | 0.2239 | 0.2107 | +0.0132 ± 0.0053 | 0.6431 | 0.6046 | 0.5759 | 0.3803 | 0.445 | -0.099 ± 0.0136 | -0.0033 (9) |
| 25-40 | 646 | 0.2216 | 0.2089 | +0.0128 ± 0.0107 | 0.6321 | 0.6006 | 0.6566 | 0.3468 | 0.4799 | -0.072 ± 0.0164 | -0.01 (1) |
| 40+ | 134 | 0.2706 | 0.2006 | +0.0700 ± 0.0333 | 0.7412 | 0.5849 | 0.7452 | 0.2961 | 0.4478 | -0.055 ± 0.0329 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3888 | 0.1845 | 0.1852 | -0.0007 ± 0.0002 | 0.5444 | 0.545 | 0.4872 | 0.4721 | 0.4967 | -0.031 ± 0.007 | -0.0129 (17) |
| 3-5 | 2616 | 0.1961 | 0.1946 | +0.0015 ± 0.0007 | 0.5717 | 0.5658 | 0.4861 | 0.4463 | 0.4453 | -0.057 ± 0.0087 | 0.0 (2) |
| 5-10 | 5507 | 0.2004 | 0.1964 | +0.0040 ± 0.0009 | 0.586 | 0.5725 | 0.4864 | 0.4125 | 0.4222 | -0.051 ± 0.006 | -0.0119 (21) |
| 10-15 | 4707 | 0.2025 | 0.1854 | +0.0171 ± 0.0016 | 0.5918 | 0.5452 | 0.4888 | 0.3645 | 0.3571 | -0.071 ± 0.0063 | -0.0281 (16) |
| 15-25 | 5871 | 0.2071 | 0.1674 | +0.0397 ± 0.0021 | 0.6073 | 0.4963 | 0.5013 | 0.305 | 0.303 | -0.075 ± 0.0053 | -0.0025 (44) |
| 25-40 | 4615 | 0.222 | 0.1262 | +0.0958 ± 0.0033 | 0.6379 | 0.3871 | 0.5278 | 0.214 | 0.2225 | -0.060 ± 0.0051 | -0.01 (1) |
| 40+ | 3014 | 0.378 | 0.0464 | +0.3316 ± 0.0044 | 0.9842 | 0.1775 | 0.6299 | 0.1041 | 0.0647 | -0.074 ± 0.0037 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 582 | 0.2059 | 0.2065 | -0.0006 ± 0.0007 | 0.5931 | 0.5946 | 0.5108 | 0.4955 | 0.5155 | -0.109 ± 0.0204 | -0.01 (3) |
| 3-5 | 407 | 0.2271 | 0.2236 | +0.0035 ± 0.0019 | 0.6412 | 0.6338 | 0.511 | 0.4713 | 0.4423 | -0.141 ± 0.025 | 0.02 (1) |
| 5-10 | 906 | 0.2081 | 0.2082 | -0.0001 ± 0.0023 | 0.6025 | 0.6023 | 0.5493 | 0.4743 | 0.5155 | -0.083 ± 0.0157 | -0.01 (4) |
| 10-15 | 824 | 0.2201 | 0.213 | +0.0071 ± 0.004 | 0.6319 | 0.6133 | 0.5673 | 0.443 | 0.4794 | -0.109 ± 0.0168 | -0.04 (5) |
| 15-25 | 1183 | 0.2293 | 0.2124 | +0.0169 ± 0.0052 | 0.6528 | 0.6078 | 0.585 | 0.3898 | 0.4472 | -0.101 ± 0.0136 | -0.0133 (9) |
| 25-40 | 828 | 0.2668 | 0.1973 | +0.0696 ± 0.0097 | 0.7456 | 0.5752 | 0.6535 | 0.3391 | 0.3889 | -0.124 ± 0.0154 | -0.0075 (4) |
| 40+ | 309 | 0.3591 | 0.1698 | +0.1892 ± 0.0232 | 0.9837 | 0.5078 | 0.7336 | 0.2472 | 0.3107 | -0.073 ± 0.0225 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3315 | 0.1918 | 0.1919 | -0.0001 ± 0.0003 | 0.5603 | 0.5602 | 0.5116 | 0.4966 | 0.5062 | -0.048 ± 0.0079 | -0.0133 (15) |
| 3-5 | 2222 | 0.1979 | 0.1962 | +0.0018 ± 0.0008 | 0.5733 | 0.5686 | 0.5179 | 0.4781 | 0.4752 | -0.056 ± 0.0096 | 0.02 (1) |
| 5-10 | 4906 | 0.1987 | 0.1957 | +0.0031 ± 0.001 | 0.5834 | 0.571 | 0.5154 | 0.4413 | 0.4613 | -0.040 ± 0.0064 | -0.0117 (6) |
| 10-15 | 4215 | 0.2061 | 0.1937 | +0.0124 ± 0.0017 | 0.6021 | 0.5642 | 0.5154 | 0.3915 | 0.4045 | -0.056 ± 0.0069 | -0.0189 (18) |
| 15-25 | 5869 | 0.2156 | 0.1781 | +0.0376 ± 0.0022 | 0.6275 | 0.5231 | 0.5234 | 0.328 | 0.3333 | -0.068 ± 0.0056 | -0.0086 (42) |
| 25-40 | 5386 | 0.2514 | 0.1362 | +0.1151 ± 0.0032 | 0.7086 | 0.418 | 0.556 | 0.2394 | 0.2187 | -0.086 ± 0.005 | -0.0044 (18) |
| 40+ | 4305 | 0.3948 | 0.06 | +0.3348 ± 0.0043 | 1.0386 | 0.215 | 0.6509 | 0.1177 | 0.0839 | -0.071 ± 0.0037 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 719 | 0.1977 | 0.1997 | -0.0021 ± 0.0006 | 0.5746 | 0.5797 | 0.5014 | 0.4861 | 0.5452 | -0.039 ± 0.0174 | -0.0137 (8) |
| 3-5 | 491 | 0.2023 | 0.2007 | +0.0015 ± 0.0016 | 0.5874 | 0.582 | 0.5039 | 0.4642 | 0.4664 | -0.120 ± 0.0211 | 0.0067 (3) |
| 5-10 | 1072 | 0.2039 | 0.2015 | +0.0024 ± 0.0021 | 0.594 | 0.5855 | 0.5114 | 0.4373 | 0.4571 | -0.099 ± 0.0141 | -0.0071 (7) |
| 10-15 | 881 | 0.2117 | 0.2069 | +0.0048 ± 0.0038 | 0.6135 | 0.5976 | 0.5401 | 0.4169 | 0.4597 | -0.097 ± 0.0154 | -0.0317 (6) |
| 15-25 | 1068 | 0.2313 | 0.2155 | +0.0158 ± 0.0055 | 0.6606 | 0.6154 | 0.5873 | 0.3927 | 0.4494 | -0.107 ± 0.0142 | -0.03 (1) |
| 25-40 | 664 | 0.2139 | 0.2161 | -0.0022 ± 0.0105 | 0.617 | 0.6172 | 0.6663 | 0.3558 | 0.512 | -0.059 ± 0.0163 | 0.015 (2) |
| 40+ | 144 | 0.2886 | 0.2056 | +0.0829 ± 0.0329 | 0.7926 | 0.5956 | 0.7541 | 0.3037 | 0.4444 | -0.062 ± 0.0345 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3836 | 0.1846 | 0.1851 | -0.0006 ± 0.0002 | 0.5434 | 0.5443 | 0.4858 | 0.4706 | 0.4875 | -0.035 ± 0.007 | -0.0163 (35) |
| 3-5 | 2553 | 0.1989 | 0.1969 | +0.0020 ± 0.0007 | 0.5805 | 0.5738 | 0.4874 | 0.4478 | 0.4434 | -0.063 ± 0.009 | -0.0094 (18) |
| 5-10 | 5667 | 0.1942 | 0.1894 | +0.0049 ± 0.0009 | 0.5716 | 0.5548 | 0.4876 | 0.4135 | 0.4179 | -0.055 ± 0.0058 | -0.01 (31) |
| 10-15 | 4590 | 0.1942 | 0.1794 | +0.0147 ± 0.0016 | 0.5726 | 0.5305 | 0.4986 | 0.3753 | 0.3767 | -0.064 ± 0.0063 | -0.015 (12) |
| 15-25 | 6003 | 0.2118 | 0.1722 | +0.0397 ± 0.0021 | 0.6176 | 0.5076 | 0.512 | 0.317 | 0.3137 | -0.074 ± 0.0053 | -0.03 (2) |
| 25-40 | 4590 | 0.2187 | 0.1292 | +0.0894 ± 0.0033 | 0.6313 | 0.3937 | 0.5319 | 0.2159 | 0.2344 | -0.053 ± 0.0051 | 0.01 (3) |
| 40+ | 2979 | 0.3906 | 0.0513 | +0.3393 ± 0.0047 | 1.0202 | 0.1907 | 0.6411 | 0.1117 | 0.0698 | -0.077 ± 0.004 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1105 | 0.196 | 0.1961 | -0.0001 ± 0.0005 | 0.5708 | 0.5707 | 0.5035 | 0.4884 | 0.4932 | -0.066 ± 0.0136 | -0.0224 (49) |
| 3-5 | 761 | 0.1907 | 0.1903 | +0.0005 ± 0.0013 | 0.558 | 0.5559 | 0.4945 | 0.4547 | 0.4665 | -0.060 ± 0.0162 | -0.0194 (34) |
| 5-10 | 1595 | 0.2022 | 0.1964 | +0.0058 ± 0.0017 | 0.5943 | 0.5751 | 0.4968 | 0.4233 | 0.4207 | -0.080 ± 0.0113 | -0.005 (78) |
| 10-15 | 1089 | 0.2148 | 0.2028 | +0.0120 ± 0.0034 | 0.6212 | 0.5892 | 0.5304 | 0.4077 | 0.4187 | -0.078 ± 0.014 | 0.0014 (64) |
| 15-25 | 1409 | 0.2318 | 0.2106 | +0.0213 ± 0.0048 | 0.661 | 0.6058 | 0.58 | 0.3852 | 0.4301 | -0.079 ± 0.0123 | -0.0214 (59) |
| 25-40 | 881 | 0.2427 | 0.2097 | +0.0330 ± 0.0094 | 0.6937 | 0.6013 | 0.6789 | 0.367 | 0.4699 | -0.087 ± 0.0144 | -0.0219 (26) |
| 40+ | 289 | 0.3379 | 0.2008 | +0.1371 ± 0.0257 | 0.9767 | 0.587 | 0.8083 | 0.3285 | 0.4429 | -0.090 ± 0.0237 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3831 | 0.1795 | 0.1797 | -0.0002 ± 0.0002 | 0.5296 | 0.5292 | 0.5048 | 0.4896 | 0.4983 | -0.041 ± 0.0069 | -0.0157 (88) |
| 3-5 | 2622 | 0.1941 | 0.1922 | +0.0020 ± 0.0007 | 0.5655 | 0.561 | 0.5027 | 0.4629 | 0.458 | -0.056 ± 0.0087 | -0.0209 (69) |
| 5-10 | 5280 | 0.1975 | 0.1897 | +0.0079 ± 0.0009 | 0.5823 | 0.5574 | 0.4944 | 0.4209 | 0.4059 | -0.071 ± 0.006 | -0.0082 (132) |
| 10-15 | 3727 | 0.2119 | 0.1958 | +0.0161 ± 0.0018 | 0.6148 | 0.5729 | 0.5304 | 0.4075 | 0.403 | -0.069 ± 0.0073 | -0.0053 (105) |
| 15-25 | 4515 | 0.23 | 0.1994 | +0.0306 ± 0.0026 | 0.6624 | 0.5777 | 0.5679 | 0.3723 | 0.3925 | -0.068 ± 0.0067 | -0.0253 (107) |
| 25-40 | 3130 | 0.2584 | 0.185 | +0.0735 ± 0.0048 | 0.7326 | 0.5401 | 0.6323 | 0.3192 | 0.361 | -0.077 ± 0.0075 | -0.0229 (51) |
| 40+ | 1335 | 0.3726 | 0.1485 | +0.2241 ± 0.011 | 1.0545 | 0.4465 | 0.7301 | 0.2286 | 0.2689 | -0.068 ± 0.0099 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5039 | 1.029 ± 0.04 | 1.097 | 0.1678 | 0.1641 | 0.215 | 0.207 |
| gen2 | 5039 | 0.813 ± 0.036 | 1.057 | 0.1688 | 0.1646 | 0.2352 | 0.2069 |
| gen1_elo | 5039 | 1.004 ± 0.038 | 1.096 | 0.1743 | 0.1642 | 0.2138 | 0.2071 |
| gen1_sr | 5039 | 0.991 ± 0.047 | 1.121 | 0.1295 | 0.1665 | 0.2312 | 0.2065 |
| gen1_ledger | 7129 | 0.862 ± 0.028 | 1.062 | 0.1845 | 0.1765 | 0.2183 | 0.2013 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 25,424)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,655 | 22.2% |
| STALE_QUOTE | market_freshness | 5,499 | 21.6% |
| BOOK_QUALITY | execution | 4,922 | 19.4% |
| POOR_DATA | data | 2,946 | 11.6% |
| LIMITED_DATA | data | 1,576 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,402 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,184 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 1,056 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 735 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 448 | 1.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.2%, market_freshness 21.6%, execution 19.4%, data 17.8%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.7%, mapping 4.2%, model_calibration 1.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.1%, LOW_DATA_QUALITY 71.3%, THIN_PLAYER_HISTORY 60.4%, STALE_PLAYER_DATA 51.6%, STALE_KALSHI_QUOTE 43.6%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 33.4%, WIDE_SPREAD 25.4%, MODEL_HIGH_UNCERTAINTY 17.6%, PLAYER_IDENTITY_RISK 16.0%, LEVEL_TRANSFER_RISK 10.5%, LOW_DISPLAYED_LIQUIDITY 7.9%, EVENT_MAPPING_RISK 7.6%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.8%, POST_SETTLEMENT_OBSERVATION 22.2%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 13,617)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,577 | 33.6% |
| BOOK_QUALITY | execution | 2,581 | 18.9% |
| STALE_QUOTE | market_freshness | 2,541 | 18.7% |
| POOR_DATA | data | 1,242 | 9.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 749 | 5.5% |
| IDENTITY_AMBIGUOUS | mapping | 572 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 475 | 3.5% |
| LIMITED_DATA | data | 464 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 302 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 113 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.6%, execution 18.9%, market_freshness 18.7%, data 12.5%, market_freshness/coverage 9.0%, mapping 4.2%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.8%, LOW_DATA_QUALITY 74.7%, THIN_PLAYER_HISTORY 62.9%, STALE_KALSHI_QUOTE 51.5%, STALE_PLAYER_DATA 46.0%, MODEL_INTERNAL_DISAGREEMENT 42.5%, ASYMMETRIC_SAMPLE_SIZE 34.6%, WIDE_SPREAD 24.8%, PLAYER_IDENTITY_RISK 19.0%, MODEL_HIGH_UNCERTAINTY 18.1%, LEVEL_TRANSFER_RISK 9.3%, EVENT_MAPPING_RISK 9.1%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.7%, POST_SETTLEMENT_OBSERVATION 33.6%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 10712, "IDENTITY_AMBIGUOUS": 2905}; ticker orientation: {"VERIFIED": 13617}.

Checks: discipline:AMBIGUOUS 884, discipline:PASS 12733, identity_confidence:AMBIGUOUS 2593, identity_confidence:PASS 11024, level_mapping:NA 896, level_mapping:PASS 12721, market_pair:AMBIGUOUS 470, market_pair:NA 328, market_pair:PASS 12819, model_complement:NA 293, model_complement:PASS 13324, namesake:AMBIGUOUS 6, namesake:PASS 13611, physical_match_id:NA 4769, physical_match_id:PASS 8848, player_ids:PASS 13617, same_pair_other_event:PASS 13617, ticker_orientation:PASS 13617

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,109 | 4.4% | 4.0% | 1.7% | {"market_freshness": 56, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "market_freshness/coverage": 15, "coverage": 13} | 5.84 | 0.2198 / 0.2158 (585) | 20.9% | 3.1% | 3.3% | 2.8% |
| CHALLENGER | 9,479 | 16.7% | 6.4% | 11.7% | {"coverage": 924, "market_freshness/coverage": 191, "market_freshness": 165, "data": 144, "model_calibration_or_unknown": 74, "execution": 36, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.37 | 0.2189 / 0.2094 (2181) | 34.8% | 16.2% | 4.2% | 22.5% |
| DOUBLES | 1,883 | 46.9% | 46.6% | 6.5% | {"execution": 497, "mapping": 219, "market_freshness": 106, "market_freshness/coverage": 55, "coverage": 7} | 23.62 | 0.3095 / 0.2365 (449) | 12.4% | 0.0% | 100.0% | 6.4% |
| ITF_MEN | 16,879 | 25.7% | 18.2% | 31.9% | {"coverage": 1523, "execution": 848, "market_freshness": 768, "data": 613, "market_freshness/coverage": 396, "mapping": 183, "model_calibration": 6, "model_calibration_or_unknown": 2} | 12.06 | 0.2168 / 0.1992 (3550) | 36.5% | 70.4% | 18.3% | 21.3% |
| ITF_WOMEN | 22,654 | 27.0% | 19.8% | 45.0% | {"coverage": 2079, "market_freshness": 1314, "execution": 1123, "data": 858, "market_freshness/coverage": 514, "mapping": 147, "model_calibration_or_unknown": 78, "model_calibration": 13} | 12.77 | 0.2046 / 0.1975 (4194) | 38.9% | 58.1% | 10.2% | 21.3% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,678 | 5.7% | 5.1% | 1.5% | {"market_freshness": 74, "model_calibration_or_unknown": 43, "execution": 27, "data": 19, "coverage": 18, "model_calibration": 17, "market_freshness/coverage": 11, "mapping": 1} | 7.64 | 0.2336 / 0.2276 (575) | 25.2% | 1.1% | 1.4% | 3.3% |
| WTA125 | 1,968 | 11.9% | 10.0% | 1.7% | {"market_freshness": 56, "model_calibration_or_unknown": 50, "market_freshness/coverage": 41, "data": 36, "execution": 21, "model_calibration": 14, "coverage": 12, "mapping": 4} | 9.38 | 0.2138 / 0.1968 (592) | 24.9% | 12.0% | 5.4% | 7.7% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
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
| 17 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 18 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 19 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 20 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 21 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 22 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 23 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 24 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 25 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 26 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 365 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 27 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 28 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 29 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 30 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 31 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 32 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 33 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 34 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 213 min (STALE); no external reference |
| 35 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 36 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 37 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 38 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 720 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 39 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 40 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 41 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 42 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 43 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 44 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 45 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 46 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 47 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 49 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 752 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 50 | `KXITFMATCH-26OCT27GHESAD-GHE` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 471 min (STALE); data POOR (grade F, thinner serve sample 276.0, ratio 6.69); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.968, "by_level_share_of_ge_25pp": {"ATP": 0.0165, "CHALLENGER": 0.1165, "DOUBLES": 0.0649, "ITF_MEN": 0.3186, "ITF_WOMEN": 0.4499, "OTHER": 0.0009, "WTA": 0.0154, "WTA125": 0.0172}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5152, "share_primary_cause_market_settled_or_in_play": 0.426, "share_primary_cause_stale_quote_only": 0.1866}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 13617, "identity_ambiguous_share": 0.2133, "ticker_orientation": {"VERIFIED": 13617}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 8848, "with_external": 447, "coverage": 0.0505, "external_status": {"EXTERNAL_STALE": 275, "AGREES_WITH_KALSHI": 163, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 275, "MODEL_LONE_OUTLIER": 163, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3647, "share_external_supports_model": 0.0201}, "pregame_clean_ge_25pp": {"n": 4320, "with_external": 423, "coverage": 0.0979, "external_status": {"EXTERNAL_STALE": 258, "AGREES_WITH_KALSHI": 156, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 258, "MODEL_LONE_OUTLIER": 156, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3688, "share_external_supports_model": 0.0213}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 455.0, "median_sample_ratio": 2.47, "median_min_matches": 18.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2131, "data_status": {"POOR": 7744, "LIMITED": 3426, "ADEQUATE": 2447}, "comparison_lt_10pp": {"median_thinner_serve_points": 1754.0, "median_sample_ratio": 1.69, "median_min_matches": 94.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1000, "model_minus_observed": 0.0478, "kalshi_minus_observed": -0.0901, "brier_diff_model_minus_kalshi": -0.0031}, "4-10x": {"n": 682, "model_minus_observed": 0.092, "kalshi_minus_observed": -0.0558, "brier_diff_model_minus_kalshi": 0.0094}, "<2x": {"n": 2465, "model_minus_observed": 0.0892, "kalshi_minus_observed": -0.0336, "brier_diff_model_minus_kalshi": 0.0108}, ">=10x": {"n": 892, "model_minus_observed": 0.1157, "kalshi_minus_observed": -0.0605, "brier_diff_model_minus_kalshi": 0.0113}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 5039, "model": {"intercept": -0.537, "slope": 0.813, "slope_se": 0.036}, "kalshi_mid_same_rows": {"intercept": 0.192, "slope": 1.057, "slope_se": 0.04}, "mean_extremity_model": 0.1688, "mean_extremity_kalshi": 0.1646, "model_brier": 0.2352, "kalshi_brier": 0.2069, "brier_diff_model_minus_kalshi": 0.0284, "brier_diff_se": 0.0027, "model_logloss": 0.668, "kalshi_logloss": 0.5968}, "fair_v1": {"n": 5039, "model": {"intercept": -0.415, "slope": 1.029, "slope_se": 0.04}, "kalshi_mid_same_rows": {"intercept": 0.283, "slope": 1.097, "slope_se": 0.041}, "mean_extremity_model": 0.1678, "mean_extremity_kalshi": 0.1641, "model_brier": 0.215, "kalshi_brier": 0.207, "brier_diff_model_minus_kalshi": 0.008, "brier_diff_se": 0.0022, "model_logloss": 0.619, "kalshi_logloss": 0.5971}, "gen1_elo": {"n": 5039, "model": {"intercept": -0.388, "slope": 1.004, "slope_se": 0.038}, "kalshi_mid_same_rows": {"intercept": 0.305, "slope": 1.096, "slope_se": 0.04}, "mean_extremity_model": 0.1743, "mean_extremity_kalshi": 0.1642, "model_brier": 0.2138, "kalshi_brier": 0.2071, "brier_diff_model_minus_kalshi": 0.0066, "brier_diff_se": 0.0022, "model_logloss": 0.6168, "kalshi_logloss": 0.5972}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2479, "share_ge_15": 0.4435, "median_abs_gap": 13.08, "n": 35685}, "gen1_elo": {"share_ge_25": 0.2452, "share_ge_15": 0.441, "median_abs_gap": 12.92, "n": 35685}, "gen1_sr": {"share_ge_25": 0.3153, "share_ge_15": 0.5231, "median_abs_gap": 15.97, "n": 35685}, "gen2": {"share_ge_25": 0.3192, "share_ge_15": 0.5139, "median_abs_gap": 15.58, "n": 35685}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1551, "share_ge_15": 0.3585, "median_abs_gap": 10.85, "n": 27843}, "gen1_elo": {"share_ge_25": 0.155, "share_ge_15": 0.3549, "median_abs_gap": 10.65, "n": 27841}, "gen1_sr": {"share_ge_25": 0.2224, "share_ge_15": 0.4458, "median_abs_gap": 13.04, "n": 27844}, "gen2": {"share_ge_25": 0.2389, "share_ge_15": 0.4459, "median_abs_gap": 13.06, "n": 27845}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.84, "share_ge_25_all": 0.044, "share_ge_25_pregame_clean": 0.0397}, "WTA": {"median_abs_gap_pregame_clean": 7.64, "share_ge_25_all": 0.0571, "share_ge_25_pregame_clean": 0.0509}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2358, "share_within_10pp_all": 0.4347, "share_within_10pp_pregame_clean": 0.4863, "corr_model_vs_mid_pregame_clean": 0.8458}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 741, "model_brier": 0.2011, "kalshi_brier": 0.2016, "brier_diff_model_minus_kalshi": -0.0005}, "10-15": {"n_settled": 884, "model_brier": 0.2209, "kalshi_brier": 0.2114, "brier_diff_model_minus_kalshi": 0.0095}, "15-25": {"n_settled": 1137, "model_brier": 0.2239, "kalshi_brier": 0.2107, "brier_diff_model_minus_kalshi": 0.0132}, "25-40": {"n_settled": 646, "model_brier": 0.2216, "kalshi_brier": 0.2089, "brier_diff_model_minus_kalshi": 0.0128}, "3-5": {"n_settled": 456, "model_brier": 0.2051, "kalshi_brier": 0.2054, "brier_diff_model_minus_kalshi": -0.0003}, "40+": {"n_settled": 134, "model_brier": 0.2706, "kalshi_brier": 0.2006, "brier_diff_model_minus_kalshi": 0.07}, "5-10": {"n_settled": 1041, "model_brier": 0.2033, "kalshi_brier": 0.2035, "brier_diff_model_minus_kalshi": -0.0003}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.537, "slope": 0.813, "slope_se": 0.036}, "kalshi_slope": {"intercept": 0.192, "slope": 1.057, "slope_se": 0.04}, "n": 5039}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.494, "slope": 0.862, "slope_se": 0.028}, "kalshi_slope": {"intercept": 0.161, "slope": 1.062, "slope_se": 0.033}, "n": 7129}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 449, "model_brier": 0.3095, "kalshi_brier": 0.2365, "brier_diff_model_minus_kalshi": 0.073, "brier_diff_se": 0.0143, "corr_model_outcome": 0.0459, "corr_kalshi_outcome": 0.2472}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
