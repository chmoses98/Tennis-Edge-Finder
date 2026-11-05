# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-05T05:34Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 78,509): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 19.1%, 25-40 13.7%, 40+ 8.0%; median gap 11.81 pp.
* **Where the extremes live**: 96.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.7%, Challenger 10.7%, doubles 6.7%). Main tour: ATP 3.8% and WTA 6.1% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 17,002): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.5%, STALE_QUOTE 19.5%, BOOK_QUALITY 17.9%, POOR_DATA 9.4%, POSSIBLY_IN_PLAY_QUOTE 5.7%, IDENTITY_AMBIGUOUS 4.2%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.5%, market_freshness 19.5%, execution 17.9%, data 12.8%, market_freshness/coverage 9.3%, mapping 4.2%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.9% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.8% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 17,002 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.4% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.4% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 479.0 points vs 1722.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.046, Gen-2 0.838, Gen-1 ledger 0.877 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 860 model 0.2206 vs Kalshi 0.2038; n 184 model 0.2944 vs Kalshi 0.1759.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 335,178 model-market comparisons (547,683 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 111,662 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-05T05:22:55.421248+00:00'], shadow board 90,180 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-05T05:22:58.119502+00:00'], Model 4 41,946 rows, 27,607 settled tickers, 10,471 tickers with an external scan.
* By model: {"gen1_ledger": 75355, "gen1_elo": 45318, "fair_v1": 45318, "gen2": 45318, "gen1_sr": 45318, "model4_fundamental": 39317, "model4_conditioned": 39234}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 78,509 | 14.1 | 9.6 | 20.2 | 15.3 | 19.1 | 13.7 | 8.0 | 11.81 | 40.8% | 21.7% |
| MW fair_v1 | 45,318 | 12.8 | 8.7 | 18.8 | 15.4 | 19.6 | 14.8 | 9.8 | 13.0 | 44.2% | 24.6% |
| MW gen1_elo | 45,318 | 12.6 | 8.8 | 19.3 | 15.4 | 19.5 | 14.6 | 9.7 | 12.76 | 43.9% | 24.3% |
| MW gen1_ledger | 33,191 | 15.8 | 10.9 | 22.1 | 15.2 | 18.4 | 12.1 | 5.5 | 10.28 | 36.0% | 17.6% |
| MW gen1_sr | 45,318 | 10.2 | 7.3 | 16.7 | 13.9 | 20.7 | 18.7 | 12.5 | 15.76 | 51.9% | 31.2% |
| MW gen2 | 45,318 | 11.1 | 7.6 | 16.7 | 13.8 | 19.5 | 17.7 | 13.6 | 15.39 | 50.9% | 31.4% |
| all families model4_conditioned | 39,234 | 22.2 | 18.0 | 34.1 | 17.2 | 5.0 | 2.2 | 1.2 | 6.07 | 8.5% | 3.5% |
| all families model4_fundamental | 39,317 | 17.4 | 13.5 | 33.8 | 19.9 | 10.0 | 3.8 | 1.5 | 7.63 | 15.4% | 5.4% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.1%, >=15pp 40.8%, >=20pp 30.0%, >=25pp 21.7%, >=30pp 15.6%, >=40pp 8.0%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.33pp; >=10pp 44.9%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,899 | 28.4 | 15.6 | 27.7 | 13.4 | 10.7 | 3.7 | 0.6 | 5.84 | 14.9% | 4.3% |
| CHALLENGER | 6,809 | 16.0 | 9.9 | 20.7 | 15.3 | 16.2 | 11.3 | 10.7 | 10.91 | 38.1% | 22.0% |
| ITF_MEN | 12,684 | 9.9 | 7.3 | 17.1 | 15.1 | 21.3 | 17.3 | 12.1 | 15.21 | 50.6% | 29.3% |
| ITF_WOMEN | 17,634 | 9.5 | 7.1 | 16.0 | 14.9 | 22.1 | 18.3 | 12.0 | 15.79 | 52.4% | 30.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,973 | 16.8 | 13.2 | 24.7 | 21.0 | 16.4 | 6.9 | 1.1 | 8.68 | 24.4% | 8.0% |
| WTA125 | 1,313 | 15.8 | 6.9 | 22.6 | 19.9 | 20.6 | 12.3 | 1.8 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,899 | 26.8 | 15.8 | 26.0 | 15.4 | 11.5 | 3.7 | 0.8 | 6.04 | 16.0% | 4.5% |
| CHALLENGER | 6,809 | 14.9 | 9.0 | 18.6 | 14.1 | 18.7 | 13.4 | 11.3 | 12.48 | 43.4% | 24.8% |
| ITF_MEN | 12,684 | 8.1 | 6.2 | 15.2 | 13.8 | 19.8 | 20.6 | 16.3 | 17.9 | 56.7% | 36.9% |
| ITF_WOMEN | 17,634 | 7.8 | 5.8 | 14.1 | 12.9 | 20.6 | 21.2 | 17.6 | 19.09 | 59.4% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,973 | 14.1 | 10.2 | 21.9 | 15.9 | 22.1 | 13.1 | 2.6 | 11.18 | 37.8% | 15.7% |
| WTA125 | 1,313 | 10.1 | 7.2 | 16.4 | 15.4 | 24.2 | 17.5 | 9.1 | 15.22 | 50.8% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,899 | 22.9 | 13.9 | 25.2 | 15.6 | 15.1 | 6.2 | 1.2 | 7.26 | 22.4% | 7.3% |
| CHALLENGER | 6,809 | 15.2 | 9.5 | 20.9 | 15.6 | 16.0 | 11.9 | 10.9 | 11.2 | 38.7% | 22.8% |
| ITF_MEN | 12,684 | 9.5 | 7.2 | 17.3 | 14.2 | 22.0 | 17.4 | 12.5 | 15.68 | 51.8% | 29.9% |
| ITF_WOMEN | 17,634 | 9.3 | 6.9 | 16.3 | 15.8 | 22.2 | 18.2 | 11.3 | 15.55 | 51.7% | 29.5% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,973 | 22.8 | 16.9 | 31.8 | 15.1 | 8.9 | 3.4 | 1.1 | 6.12 | 13.3% | 4.4% |
| WTA125 | 1,313 | 21.2 | 13.2 | 25.7 | 18.8 | 14.9 | 5.8 | 0.3 | 8.01 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,306 | 26.5 | 19.7 | 30.1 | 12.4 | 8.3 | 2.6 | 0.4 | 5.38 | 11.3% | 3.0% |
| CHALLENGER | 4,393 | 22.3 | 14.6 | 27.5 | 14.7 | 13.6 | 5.8 | 1.6 | 7.09 | 20.9% | 7.4% |
| DOUBLES | 2,435 | 5.0 | 4.4 | 12.6 | 10.7 | 20.4 | 25.0 | 21.9 | 23.56 | 67.3% | 46.9% |
| ITF_MEN | 9,467 | 13.0 | 9.5 | 21.2 | 15.8 | 21.5 | 13.1 | 5.9 | 11.83 | 40.5% | 19.0% |
| ITF_WOMEN | 11,476 | 13.4 | 9.2 | 19.9 | 15.7 | 21.3 | 14.9 | 5.5 | 12.26 | 41.8% | 20.5% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,723 | 24.3 | 16.0 | 31.1 | 16.6 | 9.2 | 2.7 | 0.2 | 6.57 | 12.1% | 2.9% |
| WTA125 | 1,242 | 25.3 | 13.0 | 21.4 | 19.0 | 13.0 | 6.8 | 1.4 | 7.69 | 21.3% | 8.2% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,785 | 28.8 | 15.8 | 28.1 | 13.4 | 10.4 | 3.2 | 0.3 | 5.67 | 14.0% | 3.6% |
| CHALLENGER | 4,823 | 20.6 | 12.2 | 25.5 | 17.9 | 16.1 | 6.0 | 1.6 | 8.24 | 23.7% | 7.6% |
| ITF_MEN | 9,328 | 12.0 | 8.7 | 20.6 | 17.2 | 22.1 | 14.0 | 5.3 | 12.44 | 41.5% | 19.4% |
| ITF_WOMEN | 13,087 | 11.3 | 8.5 | 18.8 | 17.1 | 24.1 | 15.2 | 5.0 | 13.27 | 44.3% | 20.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,863 | 17.1 | 13.2 | 25.0 | 21.4 | 16.4 | 6.3 | 0.6 | 8.52 | 23.4% | 7.0% |
| WTA125 | 1,265 | 16.1 | 6.9 | 22.4 | 20.2 | 20.9 | 11.9 | 1.7 | 10.7 | 34.5% | 13.6% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,785 | 27.1 | 16.1 | 26.3 | 15.3 | 11.4 | 3.3 | 0.4 | 5.96 | 15.1% | 3.7% |
| CHALLENGER | 4,823 | 18.7 | 11.3 | 23.2 | 16.4 | 19.1 | 9.3 | 1.9 | 9.07 | 30.3% | 11.2% |
| ITF_MEN | 9,329 | 9.5 | 7.3 | 17.6 | 15.9 | 21.6 | 18.7 | 9.4 | 14.91 | 49.6% | 28.1% |
| ITF_WOMEN | 13,088 | 8.8 | 6.7 | 16.0 | 14.4 | 22.7 | 20.6 | 10.9 | 16.58 | 54.1% | 31.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,863 | 14.4 | 10.3 | 22.2 | 16.1 | 22.4 | 12.8 | 2.0 | 10.97 | 37.1% | 14.7% |
| WTA125 | 1,265 | 10.2 | 7.3 | 16.6 | 15.5 | 24.2 | 17.6 | 8.5 | 15.13 | 50.4% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,249 | 26.7 | 19.9 | 30.0 | 12.5 | 8.0 | 2.5 | 0.4 | 5.34 | 10.8% | 2.9% |
| CHALLENGER | 3,879 | 23.6 | 15.4 | 28.6 | 14.9 | 13.0 | 4.0 | 0.4 | 6.61 | 17.4% | 4.5% |
| DOUBLES | 2,287 | 4.9 | 4.5 | 12.8 | 10.8 | 20.2 | 24.9 | 21.9 | 23.54 | 67.0% | 46.8% |
| ITF_MEN | 8,127 | 13.8 | 10.1 | 22.8 | 16.3 | 21.5 | 11.6 | 3.9 | 10.89 | 37.0% | 15.5% |
| ITF_WOMEN | 9,825 | 14.0 | 9.7 | 21.0 | 16.2 | 21.5 | 13.9 | 3.6 | 11.44 | 39.0% | 17.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,662 | 24.6 | 16.4 | 31.1 | 16.6 | 9.2 | 2.1 | 0.1 | 6.43 | 11.4% | 2.2% |
| WTA125 | 1,101 | 26.4 | 13.9 | 22.4 | 19.8 | 12.1 | 4.9 | 0.5 | 7.2 | 17.4% | 5.4% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,435 | 5.0 | 4.4 | 12.6 | 10.7 | 20.4 | 25.0 | 21.9 | 23.56 | 67.3% | 46.9% |
| singles | 30,756 | 16.6 | 11.4 | 22.9 | 15.5 | 18.2 | 11.1 | 4.2 | 9.76 | 33.6% | 15.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 128 | 8.6 | 9.4 | 14.8 | 8.6 | 20.3 | 25.0 | 13.3 | 17.66 | 58.6% | 38.3% |
| Clay | 9,176 | 12.8 | 9.2 | 19.8 | 15.8 | 19.8 | 13.7 | 8.9 | 12.54 | 42.4% | 22.7% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 29,652 | 13.4 | 8.7 | 18.9 | 15.2 | 19.1 | 14.8 | 9.8 | 12.85 | 43.8% | 24.7% |
| UNKNOWN | 6,125 | 10.4 | 7.7 | 17.0 | 16.3 | 21.5 | 15.9 | 11.1 | 14.3 | 48.5% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 12,845 | 19.6 | 12.0 | 22.5 | 15.9 | 15.0 | 9.0 | 6.1 | 8.81 | 30.0% | 15.0% |
| B | 5,563 | 12.9 | 8.8 | 19.7 | 15.7 | 19.6 | 12.7 | 10.7 | 12.57 | 42.9% | 23.4% |
| C | 6,411 | 11.9 | 8.9 | 19.5 | 15.9 | 18.7 | 14.6 | 10.5 | 12.89 | 43.7% | 25.1% |
| D | 7,280 | 11.8 | 8.4 | 17.9 | 15.4 | 21.5 | 15.7 | 9.3 | 13.71 | 46.5% | 25.0% |
| F | 13,219 | 7.4 | 5.5 | 14.9 | 14.7 | 23.6 | 20.9 | 13.1 | 17.74 | 57.5% | 34.0% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,845 | 24.6 | 16.0 | 29.1 | 14.9 | 10.7 | 3.4 | 1.2 | 6.37 | 15.4% | 4.7% |
| B | 4,667 | 16.7 | 10.7 | 24.2 | 16.8 | 19.0 | 9.6 | 3.1 | 9.68 | 31.6% | 12.6% |
| C | 6,539 | 11.2 | 7.8 | 19.4 | 14.7 | 21.0 | 15.7 | 10.3 | 13.56 | 46.9% | 25.9% |
| D | 4,951 | 14.4 | 10.0 | 21.5 | 15.5 | 20.3 | 12.8 | 5.4 | 11.24 | 38.6% | 18.2% |
| F | 8,189 | 10.2 | 8.4 | 16.1 | 14.6 | 23.1 | 19.6 | 7.9 | 15.36 | 50.6% | 27.5% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 14,542 | 17.9 | 11.0 | 21.6 | 15.7 | 15.3 | 9.9 | 8.6 | 9.9 | 33.8% | 18.5% |
| LIMITED | 9,887 | 13.6 | 9.9 | 20.4 | 16.1 | 19.3 | 13.2 | 7.5 | 11.8 | 40.1% | 20.7% |
| POOR | 20,889 | 9.0 | 6.6 | 16.0 | 15.0 | 22.7 | 18.9 | 11.8 | 16.15 | 53.4% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,666 | 23.8 | 17.7 | 33.1 | 15.7 | 6.4 | 2.9 | 0.4 | 5.93 | 9.7% | 3.3% |
| GAME_SPREAD | 6,537 | 22.5 | 15.1 | 32.3 | 17.0 | 9.1 | 3.4 | 0.6 | 6.73 | 13.1% | 4.0% |
| MATCH_WINNER | 33,191 | 15.8 | 10.9 | 22.1 | 15.2 | 18.4 | 12.1 | 5.5 | 10.28 | 36.0% | 17.6% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 15,996 | 27.8 | 16.8 | 30.6 | 12.7 | 9.3 | 2.5 | 0.3 | 5.64 | 12.0% | 2.8% |
| TOTAL_GAMES | 10,941 | 9.8 | 10.8 | 35.4 | 26.1 | 10.6 | 4.3 | 3.0 | 9.22 | 17.9% | 7.2% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,920 | 24.4 | 28.8 | 33.2 | 8.2 | 4.0 | 1.1 | 0.3 | 4.79 | 5.3% | 1.4% |
| GAME_SPREAD | 9,060 | 46.8 | 16.2 | 24.8 | 7.5 | 2.3 | 1.9 | 0.6 | 3.31 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,254 | 6.6 | 9.8 | 40.1 | 30.3 | 7.4 | 3.4 | 2.4 | 9.23 | 13.2% | 5.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,955 | 23.9 | 16.6 | 34.8 | 14.7 | 6.9 | 2.6 | 0.5 | 6.05 | 10.1% | 3.1% |
| GAME_SPREAD | 9,069 | 20.5 | 13.5 | 28.2 | 20.1 | 12.0 | 4.5 | 1.2 | 7.64 | 17.7% | 5.7% |
| TOTAL_GAMES | 16,293 | 10.0 | 10.8 | 36.1 | 24.4 | 11.5 | 4.5 | 2.6 | 9.08 | 18.7% | 7.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 45,318 | 44.2% | 24.6% | 13.0 | 35.4% | 15.2% | 10.71 |
| gen1_elo | 45,318 | 43.9% | 24.3% | 12.76 | 34.9% | 15.0% | 10.5 |
| gen1_sr | 45,318 | 51.9% | 31.2% | 15.76 | 44.0% | 21.8% | 13.0 |
| gen2 | 45,318 | 50.9% | 31.4% | 15.39 | 43.9% | 23.2% | 12.86 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 19,823 | 15.5 | 10.5 | 21.3 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 25,495 | 10.8 | 7.3 | 16.8 | 14.0 | 19.2 | 17.0 | 14.8 | 15.45 | 51.1% | 31.9% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 26,659 | 16.4 | 11.2 | 22.8 | 15.3 | 17.9 | 11.6 | 4.9 | 9.89 | 34.4% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 78,509 | 26659 | 23295 | 28555 | 24.7 | 117.5 | 1451.1 |
| ge_15pp | 31,996 | 9159 | 8296 | 14541 | 27.9 | 424.8 | 1451.1 |
| ge_25pp | 17,002 | 4390 | 3617 | 8995 | 32.8 | 578.3 | 1431.1 |
| lt_10pp | 34,482 | 13433 | 11022 | 10027 | 22.6 | 47.8 | 1421.1 |

Current slate `SL-20261105T053439Z-d2ac067a`: 597 priced rows, quote age at build {'median': 12.0, 'max': 12.1}, freshness {'AGING': 597}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 49 | 0.0 | 0.0 | 36.7 | 6.1 | 32.6 | 20.4 | 4.1 | 18.34 | 57.1% | 24.5% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,510 | 19.2 | 10.9 | 25.4 | 17.9 | 18.2 | 7.5 | 0.9 | 8.82 | 26.6% | 8.4% |
| KALSHI_LONE_OUTLIER | 27 | 3.7 | 3.7 | 77.8 | 7.4 | 3.7 | 3.7 | 0.0 | 6.42 | 7.4% | 3.7% |
| MARKETS_AGREE | 917 | 66.0 | 34.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.19 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,986 | 0.0 | 2.3 | 36.9 | 26.3 | 24.4 | 9.3 | 0.9 | 11.87 | 34.5% | 10.1% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 45,318 | 7518 (16.6%) | 26.4% | 1.0% | {"EXTERNAL_STALE": 4510, "AGREES_WITH_KALSHI": 1986, "ALL_AGREE": 917, "SUPPORTS_MODEL_DIRECTION": 48, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 27, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 20,038 | 1914 (9.6%) | 35.8% | 1.6% | {"EXTERNAL_STALE": 1199, "AGREES_WITH_KALSHI": 685, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 11,150 | 594 (5.3%) | 33.8% | 2.2% | {"EXTERNAL_STALE": 380, "AGREES_WITH_KALSHI": 201, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,330 | 564 (10.6%) | 34.4% | 2.3% | {"EXTERNAL_STALE": 357, "AGREES_WITH_KALSHI": 194, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 18,280 | 4272 (23.4%) | 18.2% | 0.9% | {"EXTERNAL_STALE": 2506, "ALL_AGREE": 917, "AGREES_WITH_KALSHI": 779, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 23, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 8,842 | 10.4 | 7.8 | 19.5 | 14.8 | 21.6 | 16.1 | 9.9 | 14.0 | 47.6% | 25.9% |
| 4-10x | 6,057 | 11.3 | 8.5 | 18.5 | 15.3 | 22.1 | 14.2 | 10.0 | 13.69 | 46.3% | 24.2% |
| <2x | 23,180 | 14.9 | 9.9 | 19.7 | 16.1 | 17.6 | 13.1 | 8.8 | 11.54 | 39.4% | 21.8% |
| >=10x | 7,239 | 10.4 | 6.3 | 15.0 | 14.4 | 21.6 | 19.1 | 13.0 | 16.42 | 53.8% | 32.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 11,825 | 12.5 | 8.7 | 19.9 | 16.2 | 19.1 | 13.4 | 10.2 | 12.65 | 42.6% | 23.6% |
| 300-1000 | 9,775 | 11.8 | 8.8 | 17.7 | 15.4 | 20.7 | 16.2 | 9.4 | 13.63 | 46.2% | 25.5% |
| <300 | 14,301 | 8.3 | 5.8 | 15.1 | 14.7 | 23.1 | 20.0 | 13.1 | 17.13 | 56.1% | 33.0% |
| >=3000 | 9,417 | 21.3 | 13.0 | 24.0 | 15.7 | 13.9 | 7.1 | 5.0 | 7.71 | 26.0% | 12.1% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1361 | 0.5483 | 0.4092 | 0.4893 | +0.059 | -0.080 | 0.0005 ± 0.0042 |
| ratio 4-10x | 927 | 0.5789 | 0.4326 | 0.4887 | +0.090 | -0.056 | 0.0091 ± 0.0052 |
| ratio <2x | 3326 | 0.5371 | 0.4141 | 0.4378 | +0.099 | -0.024 | 0.0143 ± 0.0025 |
| ratio >=10x | 1147 | 0.5654 | 0.3913 | 0.4438 | +0.122 | -0.052 | 0.0156 ± 0.0053 |
| thinner_sample 1000-3000 | 1868 | 0.5389 | 0.412 | 0.4486 | +0.090 | -0.037 | 0.0104 ± 0.0034 |
| thinner_sample 300-1000 | 1534 | 0.565 | 0.424 | 0.4778 | +0.087 | -0.054 | 0.0041 ± 0.004 |
| thinner_sample <300 | 2214 | 0.5587 | 0.39 | 0.4517 | +0.107 | -0.062 | 0.014 ± 0.0038 |
| thinner_sample >=3000 | 1145 | 0.5305 | 0.4372 | 0.448 | +0.083 | -0.011 | 0.0156 ± 0.0033 |
| data_status ADEQUATE | 1872 | 0.5323 | 0.4295 | 0.4396 | +0.093 | -0.010 | 0.0154 ± 0.0028 |
| data_status LIMITED | 1636 | 0.5481 | 0.415 | 0.47 | +0.078 | -0.055 | 0.0063 ± 0.0037 |
| data_status POOR | 3253 | 0.561 | 0.4 | 0.4587 | +0.102 | -0.059 | 0.0109 ± 0.003 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 978 | 0.1975 | 0.198 | -0.0005 ± 0.0005 | 0.5748 | 0.5759 | 0.5026 | 0.4875 | 0.5031 | -0.093 ± 0.0151 | -0.0087 (8) |
| 3-5 | 618 | 0.2029 | 0.2023 | +0.0006 ± 0.0015 | 0.5884 | 0.5849 | 0.5049 | 0.465 | 0.4773 | -0.103 ± 0.0185 | 0.01 (2) |
| 5-10 | 1443 | 0.2004 | 0.1995 | +0.0009 ± 0.0018 | 0.5862 | 0.5818 | 0.5119 | 0.4381 | 0.4664 | -0.091 ± 0.0122 | -0.0143 (7) |
| 10-15 | 1183 | 0.2186 | 0.2089 | +0.0097 ± 0.0033 | 0.6295 | 0.6013 | 0.5244 | 0.4009 | 0.4227 | -0.108 ± 0.0135 | -0.048 (5) |
| 15-25 | 1495 | 0.2244 | 0.2074 | +0.0170 ± 0.0046 | 0.6435 | 0.598 | 0.5756 | 0.3806 | 0.4348 | -0.105 ± 0.0118 | -0.004 (10) |
| 25-40 | 860 | 0.2206 | 0.2038 | +0.0169 ± 0.0092 | 0.6299 | 0.5882 | 0.6515 | 0.3416 | 0.4698 | -0.068 ± 0.014 | -0.06 (2) |
| 40+ | 184 | 0.2944 | 0.1759 | +0.1185 ± 0.0277 | 0.7938 | 0.5247 | 0.7303 | 0.2753 | 0.3804 | -0.081 ± 0.0269 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5153 | 0.1851 | 0.1859 | -0.0008 ± 0.0002 | 0.5455 | 0.5464 | 0.4881 | 0.4729 | 0.5028 | -0.023 ± 0.0061 | -0.01 (28) |
| 3-5 | 3442 | 0.1957 | 0.1941 | +0.0016 ± 0.0006 | 0.5701 | 0.5639 | 0.4802 | 0.4404 | 0.4393 | -0.055 ± 0.0076 | 0.0 (3) |
| 5-10 | 7442 | 0.2004 | 0.1971 | +0.0034 ± 0.0008 | 0.5859 | 0.5746 | 0.485 | 0.4113 | 0.4258 | -0.044 ± 0.0052 | -0.0114 (22) |
| 10-15 | 6203 | 0.2013 | 0.1855 | +0.0159 ± 0.0014 | 0.5891 | 0.5447 | 0.4855 | 0.3616 | 0.3595 | -0.064 ± 0.0055 | -0.0281 (16) |
| 15-25 | 7759 | 0.2061 | 0.1666 | +0.0394 ± 0.0018 | 0.604 | 0.4953 | 0.4997 | 0.3041 | 0.3018 | -0.071 ± 0.0046 | -0.0027 (45) |
| 25-40 | 5989 | 0.2223 | 0.1259 | +0.0964 ± 0.0029 | 0.6387 | 0.387 | 0.5267 | 0.2129 | 0.2207 | -0.058 ± 0.0044 | -0.0733 (3) |
| 40+ | 3976 | 0.3814 | 0.0449 | +0.3365 ± 0.0038 | 0.9933 | 0.1732 | 0.6307 | 0.1027 | 0.0599 | -0.076 ± 0.0032 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 784 | 0.2049 | 0.2053 | -0.0004 ± 0.0006 | 0.5906 | 0.5919 | 0.5062 | 0.4915 | 0.5166 | -0.101 ± 0.0175 | -0.0117 (6) |
| 3-5 | 557 | 0.2101 | 0.207 | +0.0030 ± 0.0015 | 0.6027 | 0.5962 | 0.5125 | 0.4729 | 0.4506 | -0.133 ± 0.0207 | 0.01 (2) |
| 5-10 | 1239 | 0.205 | 0.2025 | +0.0025 ± 0.0019 | 0.5955 | 0.5879 | 0.5406 | 0.4661 | 0.4899 | -0.094 ± 0.0132 | -0.01 (4) |
| 10-15 | 1086 | 0.2106 | 0.2053 | +0.0053 ± 0.0034 | 0.6119 | 0.5956 | 0.5627 | 0.4384 | 0.4825 | -0.098 ± 0.0143 | -0.04 (5) |
| 15-25 | 1581 | 0.231 | 0.2118 | +0.0192 ± 0.0045 | 0.6564 | 0.6079 | 0.5848 | 0.3894 | 0.4396 | -0.100 ± 0.0118 | -0.012 (10) |
| 25-40 | 1110 | 0.2673 | 0.1978 | +0.0695 ± 0.0084 | 0.7461 | 0.5755 | 0.6589 | 0.3447 | 0.3937 | -0.122 ± 0.0134 | -0.008 (5) |
| 40+ | 404 | 0.3691 | 0.1633 | +0.2057 ± 0.0201 | 1.0039 | 0.4931 | 0.7349 | 0.2457 | 0.2946 | -0.082 ± 0.0193 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4438 | 0.1919 | 0.1922 | -0.0003 ± 0.0002 | 0.5593 | 0.5597 | 0.5084 | 0.4933 | 0.511 | -0.038 ± 0.0068 | -0.0154 (26) |
| 3-5 | 3023 | 0.192 | 0.191 | +0.0010 ± 0.0006 | 0.5602 | 0.557 | 0.5098 | 0.4701 | 0.477 | -0.045 ± 0.0082 | 0.01 (2) |
| 5-10 | 6643 | 0.1964 | 0.1928 | +0.0036 ± 0.0008 | 0.5768 | 0.5638 | 0.5082 | 0.4342 | 0.4493 | -0.042 ± 0.0055 | -0.0117 (6) |
| 10-15 | 5541 | 0.2009 | 0.19 | +0.0108 ± 0.0015 | 0.5906 | 0.5568 | 0.5115 | 0.3875 | 0.4068 | -0.046 ± 0.0059 | -0.0189 (18) |
| 15-25 | 7759 | 0.2169 | 0.1808 | +0.0361 ± 0.0019 | 0.6304 | 0.5302 | 0.524 | 0.3287 | 0.3368 | -0.061 ± 0.0049 | -0.0084 (43) |
| 25-40 | 7063 | 0.2506 | 0.1372 | +0.1134 ± 0.0028 | 0.7076 | 0.4193 | 0.5599 | 0.243 | 0.226 | -0.081 ± 0.0044 | -0.0095 (20) |
| 40+ | 5497 | 0.4001 | 0.06 | +0.3402 ± 0.0038 | 1.0544 | 0.2152 | 0.6541 | 0.1192 | 0.0822 | -0.073 ± 0.0032 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 949 | 0.1962 | 0.1977 | -0.0016 ± 0.0005 | 0.572 | 0.5758 | 0.5023 | 0.4869 | 0.5353 | -0.049 ± 0.0151 | -0.012 (10) |
| 3-5 | 665 | 0.2042 | 0.2028 | +0.0014 ± 0.0014 | 0.592 | 0.5865 | 0.4957 | 0.4561 | 0.4602 | -0.111 ± 0.0183 | -0.0 (4) |
| 5-10 | 1475 | 0.2019 | 0.1983 | +0.0037 ± 0.0017 | 0.5883 | 0.578 | 0.5128 | 0.439 | 0.4495 | -0.106 ± 0.012 | -0.01 (9) |
| 10-15 | 1192 | 0.2105 | 0.2015 | +0.0090 ± 0.0032 | 0.6118 | 0.5854 | 0.5376 | 0.4145 | 0.4413 | -0.108 ± 0.013 | -0.0286 (7) |
| 15-25 | 1429 | 0.2306 | 0.2117 | +0.0190 ± 0.0047 | 0.6585 | 0.607 | 0.5866 | 0.3924 | 0.4402 | -0.112 ± 0.0122 | -0.03 (1) |
| 25-40 | 858 | 0.2113 | 0.2093 | +0.0020 ± 0.0092 | 0.6102 | 0.601 | 0.6603 | 0.3494 | 0.5 | -0.055 ± 0.0141 | -0.0267 (3) |
| 40+ | 193 | 0.3126 | 0.1801 | +0.1325 ± 0.0275 | 0.8448 | 0.5339 | 0.7411 | 0.2864 | 0.3782 | -0.094 ± 0.028 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4968 | 0.1839 | 0.1846 | -0.0007 ± 0.0002 | 0.5419 | 0.5429 | 0.4841 | 0.4687 | 0.4877 | -0.032 ± 0.0062 | -0.0137 (41) |
| 3-5 | 3506 | 0.2036 | 0.2021 | +0.0016 ± 0.0006 | 0.5909 | 0.5851 | 0.4794 | 0.4399 | 0.4404 | -0.054 ± 0.0077 | -0.01 (19) |
| 5-10 | 7613 | 0.1954 | 0.1903 | +0.0051 ± 0.0007 | 0.5736 | 0.5576 | 0.488 | 0.414 | 0.4165 | -0.055 ± 0.005 | -0.0105 (37) |
| 10-15 | 6123 | 0.193 | 0.178 | +0.0150 ± 0.0013 | 0.5707 | 0.5274 | 0.4945 | 0.3712 | 0.3715 | -0.062 ± 0.0054 | -0.0146 (13) |
| 15-25 | 7861 | 0.2116 | 0.1716 | +0.0400 ± 0.0018 | 0.6172 | 0.5065 | 0.513 | 0.3186 | 0.314 | -0.073 ± 0.0047 | -0.0533 (3) |
| 25-40 | 5967 | 0.2169 | 0.1274 | +0.0895 ± 0.0029 | 0.6271 | 0.3903 | 0.5299 | 0.2143 | 0.2326 | -0.049 ± 0.0045 | -0.02 (4) |
| 40+ | 3926 | 0.3915 | 0.0499 | +0.3416 ± 0.004 | 1.0204 | 0.1858 | 0.6403 | 0.1088 | 0.0662 | -0.076 ± 0.0034 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1378 | 0.1961 | 0.1962 | -0.0001 ± 0.0004 | 0.57 | 0.5701 | 0.5074 | 0.4924 | 0.4971 | -0.068 ± 0.0122 | -0.0213 (54) |
| 3-5 | 986 | 0.1886 | 0.1884 | +0.0002 ± 0.0011 | 0.5547 | 0.5527 | 0.4945 | 0.4547 | 0.4706 | -0.059 ± 0.0141 | -0.0194 (34) |
| 5-10 | 1992 | 0.198 | 0.1933 | +0.0047 ± 0.0015 | 0.5832 | 0.5684 | 0.5073 | 0.4337 | 0.4388 | -0.076 ± 0.0101 | -0.005 (78) |
| 10-15 | 1366 | 0.214 | 0.201 | +0.0130 ± 0.003 | 0.62 | 0.5853 | 0.5404 | 0.4176 | 0.4246 | -0.091 ± 0.0125 | 0.0014 (65) |
| 15-25 | 1788 | 0.2305 | 0.2064 | +0.0241 ± 0.0042 | 0.6578 | 0.5965 | 0.589 | 0.3941 | 0.4323 | -0.089 ± 0.0109 | -0.0214 (59) |
| 25-40 | 1080 | 0.2402 | 0.2097 | +0.0306 ± 0.0085 | 0.6864 | 0.602 | 0.6863 | 0.3739 | 0.4815 | -0.088 ± 0.013 | -0.0252 (27) |
| 40+ | 381 | 0.3291 | 0.2016 | +0.1275 ± 0.0221 | 0.9496 | 0.5869 | 0.8152 | 0.338 | 0.4593 | -0.098 ± 0.0207 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5060 | 0.1768 | 0.177 | -0.0002 ± 0.0002 | 0.523 | 0.5231 | 0.5121 | 0.4969 | 0.5085 | -0.037 ± 0.006 | -0.0145 (98) |
| 3-5 | 3493 | 0.1941 | 0.1933 | +0.0008 ± 0.0006 | 0.5658 | 0.5638 | 0.501 | 0.4612 | 0.4715 | -0.040 ± 0.0075 | -0.0204 (72) |
| 5-10 | 7075 | 0.1951 | 0.1886 | +0.0066 ± 0.0008 | 0.5753 | 0.5564 | 0.5009 | 0.4273 | 0.4209 | -0.063 ± 0.0052 | -0.0084 (134) |
| 10-15 | 4878 | 0.2092 | 0.1928 | +0.0163 ± 0.0016 | 0.6084 | 0.5662 | 0.5367 | 0.4137 | 0.4075 | -0.072 ± 0.0064 | -0.0053 (106) |
| 15-25 | 5920 | 0.23 | 0.1987 | +0.0313 ± 0.0023 | 0.661 | 0.5765 | 0.5745 | 0.3791 | 0.398 | -0.067 ± 0.0058 | -0.026 (108) |
| 25-40 | 3915 | 0.2573 | 0.1889 | +0.0684 ± 0.0044 | 0.7282 | 0.5508 | 0.6379 | 0.3253 | 0.375 | -0.069 ± 0.0068 | -0.0246 (52) |
| 40+ | 1719 | 0.3721 | 0.1583 | +0.2139 ± 0.0099 | 1.0512 | 0.4718 | 0.7431 | 0.2417 | 0.2897 | -0.066 ± 0.0091 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 6761 | 1.046 ± 0.034 | 1.119 | 0.1694 | 0.1689 | 0.2139 | 0.2029 |
| gen2 | 6761 | 0.838 ± 0.031 | 1.09 | 0.1736 | 0.1692 | 0.2324 | 0.2027 |
| gen1_elo | 6761 | 1.02 ± 0.033 | 1.109 | 0.176 | 0.169 | 0.2133 | 0.2029 |
| gen1_sr | 6761 | 1.023 ± 0.04 | 1.153 | 0.1334 | 0.1709 | 0.2287 | 0.2024 |
| gen1_ledger | 8971 | 0.877 ± 0.025 | 1.086 | 0.1897 | 0.1767 | 0.2162 | 0.1993 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 31,996)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 7,379 | 23.1% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,096 | 22.2% |
| BOOK_QUALITY | execution | 5,852 | 18.3% |
| POOR_DATA | data | 3,740 | 11.7% |
| LIMITED_DATA | data | 2,000 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,828 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,342 | 4.2% |
| IDENTITY_AMBIGUOUS | mapping | 1,312 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 916 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 530 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 23.1%, coverage 22.2%, execution 18.3%, data 17.9%, market_freshness/coverage 8.6%, model_calibration_or_unknown 4.2%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.4%, LOW_DATA_QUALITY 71.6%, THIN_PLAYER_HISTORY 60.0%, STALE_PLAYER_DATA 52.2%, STALE_KALSHI_QUOTE 45.5%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 24.5%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 15.4%, LEVEL_TRANSFER_RISK 10.2%, LOW_DISPLAYED_LIQUIDITY 8.3%, EVENT_MAPPING_RISK 7.3%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.6%, POST_SETTLEMENT_OBSERVATION 22.2%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 17,002)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,700 | 33.5% |
| STALE_QUOTE | market_freshness | 3,317 | 19.5% |
| BOOK_QUALITY | execution | 3,043 | 17.9% |
| POOR_DATA | data | 1,598 | 9.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 976 | 5.7% |
| IDENTITY_AMBIGUOUS | mapping | 723 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 603 | 3.5% |
| LIMITED_DATA | data | 580 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 330 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 131 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.5%, market_freshness 19.5%, execution 17.9%, data 12.8%, market_freshness/coverage 9.3%, mapping 4.2%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 96.9%, LOW_DATA_QUALITY 75.1%, THIN_PLAYER_HISTORY 62.1%, STALE_KALSHI_QUOTE 52.9%, STALE_PLAYER_DATA 46.2%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 24.0%, MODEL_HIGH_UNCERTAINTY 19.2%, PLAYER_IDENTITY_RISK 18.5%, LEVEL_TRANSFER_RISK 9.0%, EVENT_MAPPING_RISK 8.9%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.6%, POST_SETTLEMENT_OBSERVATION 33.5%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 13540, "IDENTITY_AMBIGUOUS": 3462}; ticker orientation: {"VERIFIED": 17002}.

Checks: discipline:AMBIGUOUS 1142, discipline:PASS 15860, identity_confidence:AMBIGUOUS 3138, identity_confidence:PASS 13864, level_mapping:NA 1154, level_mapping:PASS 15848, market_pair:AMBIGUOUS 485, market_pair:NA 372, market_pair:PASS 16145, model_complement:NA 334, model_complement:PASS 16668, namesake:AMBIGUOUS 6, namesake:PASS 16996, physical_match_id:NA 5852, physical_match_id:PASS 11150, player_ids:PASS 17002, same_pair_other_event:PASS 17002, ticker_orientation:PASS 17002

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,205 | 3.8% | 3.3% | 1.4% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 21, "market_freshness/coverage": 17} | 5.55 | 0.2268 / 0.2211 (779) | 24.4% | 2.5% | 3.1% | 2.8% |
| CHALLENGER | 11,202 | 16.2% | 6.2% | 10.7% | {"coverage": 1065, "market_freshness/coverage": 215, "market_freshness": 212, "data": 157, "model_calibration_or_unknown": 77, "execution": 41, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.38 | 0.2202 / 0.2096 (2616) | 37.5% | 15.6% | 4.1% | 22.3% |
| DOUBLES | 2,435 | 46.9% | 46.8% | 6.7% | {"execution": 651, "mapping": 314, "market_freshness": 106, "market_freshness/coverage": 64, "coverage": 7} | 23.54 | 0.301 / 0.2348 (590) | 9.6% | 0.0% | 100.0% | 6.1% |
| ITF_MEN | 22,151 | 24.9% | 17.6% | 32.5% | {"coverage": 1900, "market_freshness": 1063, "execution": 969, "data": 824, "market_freshness/coverage": 555, "mapping": 202, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.72 | 0.2151 / 0.1971 (4651) | 39.1% | 69.2% | 15.6% | 21.2% |
| ITF_WOMEN | 29,110 | 26.4% | 19.1% | 45.2% | {"coverage": 2652, "market_freshness": 1679, "execution": 1299, "data": 1097, "market_freshness/coverage": 671, "mapping": 184, "model_calibration_or_unknown": 90, "model_calibration": 22} | 12.54 | 0.2017 / 0.1921 (5548) | 40.4% | 57.3% | 9.9% | 21.3% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,696 | 6.1% | 5.2% | 1.7% | {"market_freshness": 109, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 21, "market_freshness/coverage": 13, "mapping": 1} | 7.7 | 0.2316 / 0.2233 (752) | 29.5% | 2.1% | 1.3% | 3.6% |
| WTA125 | 2,555 | 11.3% | 9.8% | 1.7% | {"market_freshness": 89, "model_calibration_or_unknown": 55, "market_freshness/coverage": 43, "data": 40, "execution": 24, "model_calibration": 19, "coverage": 14, "mapping": 4} | 9.17 | 0.2069 / 0.1902 (754) | 28.7% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 16.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 969 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 3 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 4 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 5 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 6 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 7 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 8 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 572 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 9 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 10 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 20.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 1203 min (STALE); no external reference |
| 13 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 14 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 15.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 928 min (STALE); no external reference |
| 17 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 18 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 19 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 20 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 21 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 22 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 23 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 24 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 25 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 26 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 27 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 28 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 29 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 30 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 31 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 271 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 32 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 33 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 34 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 35 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 36 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 37 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 38 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 39 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 40 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 41 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 42 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 43 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 44 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 720 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 45 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 46 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 252 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |
| 47 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXATPCHALLENGERMATCH-26NOV02TOBSTO-TOB` | CHALLENGER | fair_v1 | 80% / 2% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 165 min (STALE); data POOR (grade F, thinner serve sample 159.0, ratio 20.58); no external reference |
| 49 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 50 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.969, "by_level_share_of_ge_25pp": {"ATP": 0.0139, "CHALLENGER": 0.107, "DOUBLES": 0.0672, "ITF_MEN": 0.3247, "ITF_WOMEN": 0.4525, "OTHER": 0.0007, "WTA": 0.0169, "WTA125": 0.0169}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5291, "share_primary_cause_market_settled_or_in_play": 0.4282, "share_primary_cause_stale_quote_only": 0.1951}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 17002, "identity_ambiguous_share": 0.2036, "ticker_orientation": {"VERIFIED": 17002}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 11150, "with_external": 594, "coverage": 0.0533, "external_status": {"EXTERNAL_STALE": 380, "AGREES_WITH_KALSHI": 201, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 380, "MODEL_LONE_OUTLIER": 201, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3384, "share_external_supports_model": 0.0219}, "pregame_clean_ge_25pp": {"n": 5330, "with_external": 564, "coverage": 0.1058, "external_status": {"EXTERNAL_STALE": 357, "AGREES_WITH_KALSHI": 194, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 357, "MODEL_LONE_OUTLIER": 194, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.344, "share_external_supports_model": 0.023}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 479.0, "median_sample_ratio": 2.47, "median_min_matches": 18.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2101, "data_status": {"POOR": 9601, "LIMITED": 4392, "ADEQUATE": 3009}, "comparison_lt_10pp": {"median_thinner_serve_points": 1722.0, "median_sample_ratio": 1.7, "median_min_matches": 90.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1361, "model_minus_observed": 0.059, "kalshi_minus_observed": -0.0801, "brier_diff_model_minus_kalshi": 0.0005}, "4-10x": {"n": 927, "model_minus_observed": 0.0902, "kalshi_minus_observed": -0.056, "brier_diff_model_minus_kalshi": 0.0091}, "<2x": {"n": 3326, "model_minus_observed": 0.0994, "kalshi_minus_observed": -0.0237, "brier_diff_model_minus_kalshi": 0.0143}, ">=10x": {"n": 1147, "model_minus_observed": 0.1216, "kalshi_minus_observed": -0.0524, "brier_diff_model_minus_kalshi": 0.0156}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 6761, "model": {"intercept": -0.564, "slope": 0.838, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.188, "slope": 1.09, "slope_se": 0.035}, "mean_extremity_model": 0.1736, "mean_extremity_kalshi": 0.1692, "model_brier": 0.2324, "kalshi_brier": 0.2027, "brier_diff_model_minus_kalshi": 0.0297, "brier_diff_se": 0.0023, "model_logloss": 0.6615, "kalshi_logloss": 0.5873}, "fair_v1": {"n": 6761, "model": {"intercept": -0.455, "slope": 1.046, "slope_se": 0.034}, "kalshi_mid_same_rows": {"intercept": 0.256, "slope": 1.119, "slope_se": 0.035}, "mean_extremity_model": 0.1694, "mean_extremity_kalshi": 0.1689, "model_brier": 0.2139, "kalshi_brier": 0.2029, "brier_diff_model_minus_kalshi": 0.011, "brier_diff_se": 0.0019, "model_logloss": 0.6162, "kalshi_logloss": 0.5875}, "gen1_elo": {"n": 6761, "model": {"intercept": -0.442, "slope": 1.02, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.259, "slope": 1.109, "slope_se": 0.035}, "mean_extremity_model": 0.176, "mean_extremity_kalshi": 0.169, "model_brier": 0.2133, "kalshi_brier": 0.2029, "brier_diff_model_minus_kalshi": 0.0103, "brier_diff_se": 0.0019, "model_logloss": 0.6155, "kalshi_logloss": 0.5876}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.246, "share_ge_15": 0.4422, "median_abs_gap": 13.0, "n": 45318}, "gen1_elo": {"share_ge_25": 0.2434, "share_ge_15": 0.4385, "median_abs_gap": 12.76, "n": 45318}, "gen1_sr": {"share_ge_25": 0.3122, "share_ge_15": 0.5191, "median_abs_gap": 15.76, "n": 45318}, "gen2": {"share_ge_25": 0.3135, "share_ge_15": 0.5086, "median_abs_gap": 15.39, "n": 45318}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1516, "share_ge_15": 0.3542, "median_abs_gap": 10.71, "n": 35157}, "gen1_elo": {"share_ge_25": 0.15, "share_ge_15": 0.3494, "median_abs_gap": 10.5, "n": 35157}, "gen1_sr": {"share_ge_25": 0.2175, "share_ge_15": 0.4402, "median_abs_gap": 13.0, "n": 35159}, "gen2": {"share_ge_25": 0.2323, "share_ge_15": 0.4393, "median_abs_gap": 12.86, "n": 35159}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.55, "share_ge_25_all": 0.0382, "share_ge_25_pregame_clean": 0.033}, "WTA": {"median_abs_gap_pregame_clean": 7.7, "share_ge_25_all": 0.0613, "share_ge_25_pregame_clean": 0.0519}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2372, "share_within_10pp_all": 0.4392, "share_within_10pp_pregame_clean": 0.4911, "corr_model_vs_mid_pregame_clean": 0.8509}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 978, "model_brier": 0.1975, "kalshi_brier": 0.198, "brier_diff_model_minus_kalshi": -0.0005}, "10-15": {"n_settled": 1183, "model_brier": 0.2186, "kalshi_brier": 0.2089, "brier_diff_model_minus_kalshi": 0.0097}, "15-25": {"n_settled": 1495, "model_brier": 0.2244, "kalshi_brier": 0.2074, "brier_diff_model_minus_kalshi": 0.017}, "25-40": {"n_settled": 860, "model_brier": 0.2206, "kalshi_brier": 0.2038, "brier_diff_model_minus_kalshi": 0.0169}, "3-5": {"n_settled": 618, "model_brier": 0.2029, "kalshi_brier": 0.2023, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 184, "model_brier": 0.2944, "kalshi_brier": 0.1759, "brier_diff_model_minus_kalshi": 0.1185}, "5-10": {"n_settled": 1443, "model_brier": 0.2004, "kalshi_brier": 0.1995, "brier_diff_model_minus_kalshi": 0.0009}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.564, "slope": 0.838, "slope_se": 0.031}, "kalshi_slope": {"intercept": 0.188, "slope": 1.09, "slope_se": 0.035}, "n": 6761}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.494, "slope": 0.877, "slope_se": 0.025}, "kalshi_slope": {"intercept": 0.174, "slope": 1.086, "slope_se": 0.029}, "n": 8971}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 590, "model_brier": 0.301, "kalshi_brier": 0.2348, "brier_diff_model_minus_kalshi": 0.0662, "brier_diff_se": 0.0122, "corr_model_outcome": 0.086, "corr_kalshi_outcome": 0.2617}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
