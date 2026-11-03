# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-03T16:47Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 75,406): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.4%, 15-25 19.0%, 25-40 13.7%, 40+ 8.0%; median gap 11.81 pp.
* **Where the extremes live**: 96.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.5%, Challenger 10.9%, doubles 6.8%). Main tour: ATP 3.9% and WTA 6.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 16,371): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.6%, STALE_QUOTE 19.4%, BOOK_QUALITY 18.2%, POOR_DATA 9.4%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IDENTITY_AMBIGUOUS 4.2%, IN_PLAY_QUOTE 3.4%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.6%, market_freshness 19.4%, execution 18.2%, data 12.9%, market_freshness/coverage 9.0%, mapping 4.2%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.6% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.6% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 16,371 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.7% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 479.0 points vs 1745.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.022, Gen-2 0.811, Gen-1 ledger 0.861 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 800 model 0.22 vs Kalshi 0.2065; n 172 model 0.2915 vs Kalshi 0.1797.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 324,681 model-market comparisons (529,123 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 107,839 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-03T16:28:02.036440+00:00'], shadow board 86,843 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-03T16:28:06.784113+00:00'], Model 4 41,203 rows, 26,219 settled tickers, 9,761 tickers with an external scan.
* By model: {"gen1_ledger": 72990, "gen1_elo": 43641, "fair_v1": 43641, "gen2": 43641, "gen1_sr": 43641, "model4_fundamental": 38605, "model4_conditioned": 38522}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 75,406 | 14.1 | 9.6 | 20.2 | 15.4 | 19.0 | 13.7 | 8.0 | 11.81 | 40.7% | 21.7% |
| MW fair_v1 | 43,641 | 12.9 | 8.7 | 18.8 | 15.5 | 19.5 | 14.7 | 9.8 | 12.96 | 44.1% | 24.6% |
| MW gen1_elo | 43,641 | 12.6 | 8.8 | 19.4 | 15.3 | 19.5 | 14.6 | 9.7 | 12.73 | 43.8% | 24.3% |
| MW gen1_ledger | 31,765 | 15.8 | 10.8 | 22.1 | 15.2 | 18.3 | 12.2 | 5.6 | 10.29 | 36.1% | 17.8% |
| MW gen1_sr | 43,641 | 10.2 | 7.2 | 16.9 | 13.9 | 20.6 | 18.6 | 12.5 | 15.71 | 51.7% | 31.1% |
| MW gen2 | 43,641 | 11.2 | 7.6 | 16.7 | 13.8 | 19.4 | 17.7 | 13.7 | 15.36 | 50.8% | 31.4% |
| all families model4_conditioned | 38,522 | 22.2 | 18.0 | 34.1 | 17.2 | 5.0 | 2.2 | 1.2 | 6.07 | 8.5% | 3.4% |
| all families model4_fundamental | 38,605 | 17.3 | 13.4 | 33.9 | 20.0 | 10.1 | 3.8 | 1.6 | 7.65 | 15.4% | 5.3% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.1%, >=15pp 40.7%, >=20pp 30.0%, >=25pp 21.7%, >=30pp 15.6%, >=40pp 8.0%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.3pp; >=10pp 44.7%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,840 | 28.1 | 15.5 | 27.8 | 13.4 | 10.8 | 3.7 | 0.6 | 5.86 | 15.2% | 4.3% |
| CHALLENGER | 6,625 | 16.1 | 9.8 | 20.9 | 15.4 | 15.8 | 11.5 | 10.6 | 10.84 | 37.9% | 22.1% |
| ITF_MEN | 12,053 | 9.8 | 7.3 | 16.8 | 15.0 | 21.4 | 17.5 | 12.1 | 15.39 | 51.0% | 29.6% |
| ITF_WOMEN | 16,940 | 9.5 | 7.0 | 16.0 | 15.2 | 22.1 | 18.1 | 12.1 | 15.74 | 52.3% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,908 | 17.1 | 13.0 | 24.6 | 21.2 | 16.3 | 6.7 | 1.1 | 8.68 | 24.1% | 7.8% |
| WTA125 | 1,269 | 15.9 | 7.1 | 22.9 | 19.9 | 20.5 | 12.1 | 1.6 | 10.67 | 34.3% | 13.8% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,840 | 26.6 | 15.7 | 26.0 | 15.6 | 11.5 | 3.8 | 0.8 | 6.07 | 16.0% | 4.6% |
| CHALLENGER | 6,625 | 15.0 | 9.0 | 18.6 | 14.2 | 18.4 | 13.6 | 11.3 | 12.38 | 43.2% | 24.9% |
| ITF_MEN | 12,053 | 8.1 | 6.2 | 15.0 | 13.7 | 19.7 | 20.8 | 16.5 | 18.01 | 57.0% | 37.3% |
| ITF_WOMEN | 16,940 | 7.9 | 5.8 | 14.1 | 12.8 | 20.6 | 21.1 | 17.7 | 19.08 | 59.4% | 38.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,908 | 14.4 | 10.2 | 21.8 | 16.1 | 22.1 | 12.8 | 2.6 | 11.03 | 37.5% | 15.4% |
| WTA125 | 1,269 | 10.2 | 7.2 | 16.3 | 15.6 | 24.5 | 17.4 | 8.7 | 15.19 | 50.6% | 26.1% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,840 | 22.7 | 13.8 | 25.1 | 15.7 | 15.3 | 6.2 | 1.2 | 7.3 | 22.8% | 7.4% |
| CHALLENGER | 6,625 | 15.2 | 9.5 | 21.0 | 15.7 | 15.9 | 11.9 | 10.8 | 11.11 | 38.6% | 22.7% |
| ITF_MEN | 12,053 | 9.3 | 7.2 | 17.3 | 14.1 | 22.0 | 17.6 | 12.6 | 15.81 | 52.1% | 30.1% |
| ITF_WOMEN | 16,940 | 9.3 | 7.0 | 16.4 | 15.8 | 22.1 | 18.1 | 11.4 | 15.52 | 51.6% | 29.5% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,908 | 22.9 | 16.7 | 32.0 | 15.0 | 9.0 | 3.3 | 1.1 | 6.12 | 13.5% | 4.4% |
| WTA125 | 1,269 | 21.4 | 13.1 | 25.9 | 18.4 | 15.1 | 5.9 | 0.3 | 8.01 | 21.4% | 6.2% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,259 | 26.0 | 19.6 | 30.5 | 12.5 | 8.4 | 2.7 | 0.4 | 5.47 | 11.5% | 3.1% |
| CHALLENGER | 4,279 | 22.5 | 14.4 | 27.3 | 14.6 | 13.7 | 5.9 | 1.6 | 7.12 | 21.1% | 7.5% |
| DOUBLES | 2,320 | 5.2 | 4.3 | 12.2 | 10.5 | 20.3 | 25.3 | 22.4 | 23.85 | 67.9% | 47.6% |
| ITF_MEN | 8,960 | 12.9 | 9.5 | 21.1 | 15.8 | 21.4 | 13.3 | 6.0 | 11.96 | 40.7% | 19.3% |
| ITF_WOMEN | 10,931 | 13.3 | 9.1 | 19.9 | 15.8 | 21.1 | 15.2 | 5.5 | 12.28 | 41.8% | 20.7% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,674 | 24.1 | 16.4 | 30.5 | 16.9 | 9.0 | 2.8 | 0.2 | 6.54 | 12.0% | 3.0% |
| WTA125 | 1,193 | 25.2 | 12.8 | 21.0 | 19.4 | 13.3 | 6.7 | 1.5 | 7.83 | 21.5% | 8.2% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,729 | 28.5 | 15.7 | 28.2 | 13.3 | 10.6 | 3.3 | 0.3 | 5.77 | 14.2% | 3.6% |
| CHALLENGER | 4,709 | 20.6 | 12.2 | 25.6 | 17.9 | 15.9 | 6.0 | 1.7 | 8.24 | 23.6% | 7.7% |
| ITF_MEN | 8,865 | 12.0 | 8.7 | 20.3 | 17.1 | 22.2 | 14.2 | 5.5 | 12.5 | 42.0% | 19.8% |
| ITF_WOMEN | 12,598 | 11.3 | 8.4 | 18.6 | 17.3 | 24.0 | 15.1 | 5.1 | 13.28 | 44.2% | 20.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,804 | 17.3 | 13.0 | 25.0 | 21.5 | 16.3 | 6.2 | 0.6 | 8.52 | 23.2% | 6.8% |
| WTA125 | 1,226 | 16.1 | 7.0 | 22.5 | 20.1 | 21.0 | 11.8 | 1.5 | 10.67 | 34.2% | 13.2% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,729 | 27.0 | 16.1 | 26.3 | 15.5 | 11.4 | 3.4 | 0.4 | 5.99 | 15.2% | 3.8% |
| CHALLENGER | 4,709 | 18.9 | 11.2 | 23.2 | 16.6 | 18.7 | 9.4 | 1.9 | 9.07 | 30.0% | 11.3% |
| ITF_MEN | 8,866 | 9.5 | 7.3 | 17.3 | 15.9 | 21.4 | 18.9 | 9.6 | 14.99 | 50.0% | 28.6% |
| ITF_WOMEN | 12,599 | 8.8 | 6.8 | 16.0 | 14.3 | 22.7 | 20.4 | 10.9 | 16.57 | 54.1% | 31.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,804 | 14.7 | 10.3 | 22.0 | 16.2 | 22.3 | 12.6 | 1.9 | 10.94 | 36.8% | 14.5% |
| WTA125 | 1,226 | 10.3 | 7.3 | 16.5 | 15.7 | 24.6 | 17.5 | 8.2 | 15.06 | 50.2% | 25.7% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,202 | 26.2 | 19.8 | 30.4 | 12.6 | 8.1 | 2.5 | 0.4 | 5.4 | 11.0% | 2.9% |
| CHALLENGER | 3,777 | 23.9 | 15.4 | 28.4 | 14.8 | 13.0 | 4.1 | 0.5 | 6.61 | 17.6% | 4.5% |
| DOUBLES | 2,180 | 5.1 | 4.4 | 12.3 | 10.6 | 20.1 | 25.2 | 22.4 | 23.84 | 67.6% | 47.6% |
| ITF_MEN | 7,679 | 13.8 | 10.1 | 22.7 | 16.3 | 21.4 | 11.8 | 4.0 | 11.02 | 37.2% | 15.8% |
| ITF_WOMEN | 9,352 | 14.0 | 9.6 | 21.1 | 16.4 | 21.2 | 14.2 | 3.5 | 11.46 | 39.0% | 17.7% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,614 | 24.5 | 16.9 | 30.5 | 17.0 | 9.0 | 2.2 | 0.1 | 6.39 | 11.2% | 2.2% |
| WTA125 | 1,062 | 26.5 | 13.6 | 22.0 | 20.4 | 12.3 | 4.7 | 0.5 | 7.32 | 17.5% | 5.2% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,320 | 5.2 | 4.3 | 12.2 | 10.5 | 20.3 | 25.3 | 22.4 | 23.85 | 67.9% | 47.6% |
| singles | 29,445 | 16.6 | 11.4 | 22.9 | 15.6 | 18.1 | 11.2 | 4.2 | 9.76 | 33.5% | 15.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 71 | 8.4 | 9.9 | 21.1 | 11.3 | 18.3 | 19.7 | 11.3 | 14.87 | 49.3% | 31.0% |
| Clay | 8,674 | 13.0 | 9.3 | 19.9 | 15.9 | 19.4 | 13.6 | 8.8 | 12.35 | 41.9% | 22.5% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 28,726 | 13.4 | 8.7 | 18.8 | 15.3 | 19.1 | 14.8 | 9.9 | 12.85 | 43.8% | 24.7% |
| UNKNOWN | 5,933 | 10.5 | 7.6 | 17.0 | 16.4 | 21.5 | 16.0 | 11.1 | 14.3 | 48.5% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 12,443 | 19.8 | 11.9 | 22.7 | 16.1 | 14.8 | 8.9 | 5.9 | 8.72 | 29.6% | 14.8% |
| B | 5,407 | 12.8 | 8.8 | 19.4 | 15.9 | 19.6 | 12.6 | 10.8 | 12.59 | 43.0% | 23.4% |
| C | 6,161 | 11.9 | 8.8 | 19.6 | 16.1 | 18.4 | 14.6 | 10.7 | 12.87 | 43.6% | 25.2% |
| D | 6,922 | 11.8 | 8.4 | 17.6 | 15.4 | 21.6 | 15.8 | 9.3 | 13.77 | 46.7% | 25.1% |
| F | 12,708 | 7.4 | 5.5 | 14.9 | 14.6 | 23.5 | 20.9 | 13.1 | 17.74 | 57.5% | 34.0% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,544 | 24.5 | 16.1 | 29.1 | 15.0 | 10.7 | 3.5 | 1.2 | 6.37 | 15.4% | 4.7% |
| B | 4,491 | 16.7 | 10.8 | 23.9 | 17.0 | 18.8 | 9.7 | 3.1 | 9.71 | 31.6% | 12.8% |
| C | 6,224 | 11.4 | 7.7 | 19.2 | 14.5 | 20.9 | 15.9 | 10.4 | 13.67 | 47.2% | 26.3% |
| D | 4,683 | 14.4 | 9.8 | 21.4 | 15.6 | 20.2 | 13.3 | 5.4 | 11.29 | 38.8% | 18.6% |
| F | 7,823 | 10.1 | 8.3 | 16.2 | 14.7 | 23.1 | 19.7 | 7.9 | 15.37 | 50.7% | 27.7% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 14,110 | 18.0 | 10.9 | 21.8 | 15.9 | 15.2 | 9.8 | 8.5 | 9.8 | 33.4% | 18.3% |
| LIMITED | 9,511 | 13.6 | 9.9 | 20.2 | 16.2 | 19.2 | 13.3 | 7.6 | 11.82 | 40.1% | 20.9% |
| POOR | 20,020 | 9.0 | 6.6 | 16.0 | 15.0 | 22.8 | 18.9 | 11.8 | 16.16 | 53.5% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,489 | 23.9 | 17.7 | 33.1 | 15.8 | 6.4 | 2.8 | 0.4 | 5.92 | 9.6% | 3.2% |
| GAME_SPREAD | 6,414 | 22.2 | 15.1 | 32.5 | 17.1 | 9.0 | 3.4 | 0.6 | 6.75 | 13.1% | 4.0% |
| MATCH_WINNER | 31,765 | 15.8 | 10.8 | 22.1 | 15.2 | 18.3 | 12.2 | 5.6 | 10.29 | 36.1% | 17.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 15,616 | 27.8 | 16.7 | 30.5 | 12.8 | 9.4 | 2.5 | 0.3 | 5.65 | 12.2% | 2.8% |
| TOTAL_GAMES | 10,682 | 9.9 | 10.8 | 35.3 | 26.2 | 10.6 | 4.3 | 3.0 | 9.25 | 17.9% | 7.3% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,692 | 24.5 | 28.9 | 33.2 | 8.2 | 4.0 | 1.0 | 0.3 | 4.79 | 5.2% | 1.3% |
| GAME_SPREAD | 8,908 | 46.7 | 16.2 | 24.8 | 7.5 | 2.3 | 1.9 | 0.6 | 3.32 | 4.8% | 2.5% |
| TOTAL_GAMES | 15,922 | 6.6 | 9.7 | 40.2 | 30.3 | 7.4 | 3.4 | 2.4 | 9.24 | 13.2% | 5.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,727 | 23.9 | 16.6 | 34.8 | 14.7 | 7.0 | 2.5 | 0.5 | 6.05 | 10.0% | 3.1% |
| GAME_SPREAD | 8,917 | 20.3 | 13.6 | 28.2 | 20.1 | 12.1 | 4.5 | 1.2 | 7.7 | 17.8% | 5.7% |
| TOTAL_GAMES | 15,961 | 9.9 | 10.6 | 36.2 | 24.5 | 11.6 | 4.5 | 2.7 | 9.11 | 18.8% | 7.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 43,641 | 44.1% | 24.6% | 12.96 | 35.4% | 15.2% | 10.71 |
| gen1_elo | 43,641 | 43.8% | 24.3% | 12.73 | 35.0% | 15.1% | 10.49 |
| gen1_sr | 43,641 | 51.7% | 31.1% | 15.71 | 43.9% | 21.7% | 12.97 |
| gen2 | 43,641 | 50.8% | 31.4% | 15.36 | 43.8% | 23.2% | 12.83 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 19,548 | 15.6 | 10.4 | 21.4 | 17.4 | 20.1 | 11.8 | 3.4 | 10.71 | 35.3% | 15.2% |
| STALE | 24,093 | 10.8 | 7.3 | 16.7 | 14.1 | 19.1 | 17.1 | 15.1 | 15.5 | 51.2% | 32.1% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 25,233 | 16.5 | 11.2 | 22.7 | 15.3 | 17.7 | 11.7 | 4.9 | 9.88 | 34.3% | 16.6% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 75,406 | 25233 | 23020 | 27153 | 24.6 | 118.5 | 1451.1 |
| ge_15pp | 30,693 | 8654 | 8187 | 13852 | 27.9 | 429.2 | 1451.1 |
| ge_25pp | 16,371 | 4188 | 3566 | 8617 | 32.3 | 581.7 | 1431.1 |
| lt_10pp | 33,113 | 12721 | 10891 | 9501 | 22.7 | 47.2 | 1421.1 |

Current slate `SL-20261103T164735Z-726b0ecc`: 585 priced rows, quote age at build {'median': 20.0, 'max': 20.1}, freshness {'AGING': 585}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 49 | 0.0 | 0.0 | 36.7 | 6.1 | 32.6 | 20.4 | 4.1 | 18.34 | 57.1% | 24.5% |
| EXTERNAL_LONE_OUTLIER | 27 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.3 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,317 | 19.4 | 11.0 | 25.5 | 18.0 | 17.9 | 7.3 | 0.9 | 8.71 | 26.1% | 8.2% |
| KALSHI_LONE_OUTLIER | 27 | 3.7 | 3.7 | 77.8 | 7.4 | 3.7 | 3.7 | 0.0 | 6.42 | 7.4% | 3.7% |
| MARKETS_AGREE | 876 | 66.3 | 33.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.2 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,927 | 0.0 | 2.3 | 37.0 | 26.3 | 24.2 | 9.3 | 0.8 | 11.86 | 34.4% | 10.2% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 43,641 | 7223 (16.6%) | 26.7% | 1.0% | {"EXTERNAL_STALE": 4317, "AGREES_WITH_KALSHI": 1927, "ALL_AGREE": 876, "SUPPORTS_MODEL_DIRECTION": 48, "EXTERNAL_OUTLIER": 27, "AGREES_WITH_MODEL": 27, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 19,240 | 1819 (9.4%) | 36.4% | 1.7% | {"EXTERNAL_STALE": 1126, "AGREES_WITH_KALSHI": 663, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 10,721 | 564 (5.3%) | 34.8% | 2.3% | {"EXTERNAL_STALE": 355, "AGREES_WITH_KALSHI": 196, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,148 | 535 (10.4%) | 35.3% | 2.4% | {"EXTERNAL_STALE": 333, "AGREES_WITH_KALSHI": 189, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 17,623 | 4114 (23.3%) | 18.4% | 1.0% | {"EXTERNAL_STALE": 2413, "ALL_AGREE": 876, "AGREES_WITH_KALSHI": 757, "EXTERNAL_OUTLIER": 27, "AGREES_WITH_MODEL": 23, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 8,460 | 10.4 | 7.6 | 19.5 | 14.7 | 21.7 | 16.2 | 9.9 | 14.09 | 47.8% | 26.1% |
| 4-10x | 5,831 | 11.1 | 8.5 | 18.5 | 15.4 | 22.2 | 14.3 | 10.1 | 13.76 | 46.5% | 24.3% |
| <2x | 22,432 | 15.1 | 9.8 | 19.8 | 16.2 | 17.3 | 13.0 | 8.8 | 11.48 | 39.1% | 21.7% |
| >=10x | 6,918 | 10.5 | 6.4 | 15.0 | 14.5 | 21.7 | 19.0 | 13.0 | 16.37 | 53.7% | 32.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 11,345 | 12.6 | 8.7 | 19.8 | 16.4 | 19.1 | 13.4 | 10.1 | 12.66 | 42.6% | 23.5% |
| 300-1000 | 9,373 | 11.8 | 8.8 | 17.7 | 15.5 | 20.4 | 16.2 | 9.5 | 13.59 | 46.2% | 25.7% |
| <300 | 13,762 | 8.3 | 5.8 | 15.1 | 14.7 | 23.2 | 19.9 | 13.1 | 17.12 | 56.2% | 33.0% |
| >=3000 | 9,161 | 21.4 | 13.0 | 24.2 | 15.8 | 13.6 | 7.1 | 4.9 | 7.64 | 25.7% | 12.0% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1258 | 0.5489 | 0.4084 | 0.4913 | +0.058 | -0.083 | -0.0011 ± 0.0044 |
| ratio 4-10x | 869 | 0.5826 | 0.4353 | 0.4925 | +0.090 | -0.057 | 0.0085 ± 0.0054 |
| ratio <2x | 3112 | 0.5367 | 0.4143 | 0.4428 | +0.094 | -0.029 | 0.0128 ± 0.0026 |
| ratio >=10x | 1066 | 0.5683 | 0.394 | 0.4484 | +0.120 | -0.054 | 0.0156 ± 0.0055 |
| thinner_sample 1000-3000 | 1743 | 0.539 | 0.4121 | 0.4538 | +0.085 | -0.042 | 0.0084 ± 0.0035 |
| thinner_sample 300-1000 | 1422 | 0.5673 | 0.4255 | 0.4817 | +0.086 | -0.056 | 0.0035 ± 0.0042 |
| thinner_sample <300 | 2068 | 0.5601 | 0.3914 | 0.4565 | +0.104 | -0.065 | 0.0128 ± 0.0039 |
| thinner_sample >=3000 | 1072 | 0.53 | 0.4369 | 0.4496 | +0.080 | -0.013 | 0.0152 ± 0.0034 |
| data_status ADEQUATE | 1750 | 0.5323 | 0.4297 | 0.444 | +0.088 | -0.014 | 0.0136 ± 0.0029 |
| data_status LIMITED | 1539 | 0.5488 | 0.4159 | 0.4717 | +0.077 | -0.056 | 0.0063 ± 0.0038 |
| data_status POOR | 3016 | 0.5625 | 0.4009 | 0.4639 | +0.099 | -0.063 | 0.0096 ± 0.0032 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 918 | 0.1995 | 0.1999 | -0.0005 ± 0.0005 | 0.5792 | 0.5804 | 0.5022 | 0.4871 | 0.5044 | -0.090 ± 0.0156 | -0.0087 (8) |
| 3-5 | 574 | 0.2056 | 0.205 | +0.0006 ± 0.0015 | 0.5945 | 0.591 | 0.5017 | 0.4618 | 0.4739 | -0.107 ± 0.0194 | 0.01 (2) |
| 5-10 | 1333 | 0.2012 | 0.2013 | -0.0001 ± 0.0018 | 0.5882 | 0.5862 | 0.5117 | 0.438 | 0.4726 | -0.088 ± 0.0128 | -0.0143 (7) |
| 10-15 | 1102 | 0.2209 | 0.2112 | +0.0097 ± 0.0034 | 0.6351 | 0.6071 | 0.5265 | 0.4029 | 0.4247 | -0.110 ± 0.014 | -0.048 (5) |
| 15-25 | 1406 | 0.2253 | 0.2096 | +0.0157 ± 0.0048 | 0.6457 | 0.603 | 0.5758 | 0.3807 | 0.4388 | -0.104 ± 0.0122 | -0.004 (10) |
| 25-40 | 800 | 0.22 | 0.2065 | +0.0135 ± 0.0096 | 0.6289 | 0.5948 | 0.6564 | 0.3461 | 0.48 | -0.070 ± 0.0146 | -0.06 (2) |
| 40+ | 172 | 0.2915 | 0.1797 | +0.1118 ± 0.0287 | 0.7885 | 0.5343 | 0.7371 | 0.285 | 0.3953 | -0.085 ± 0.0281 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4918 | 0.1851 | 0.1859 | -0.0009 ± 0.0002 | 0.5455 | 0.5464 | 0.4871 | 0.4718 | 0.5022 | -0.022 ± 0.0062 | -0.01 (28) |
| 3-5 | 3298 | 0.196 | 0.1941 | +0.0018 ± 0.0006 | 0.5706 | 0.5639 | 0.4811 | 0.4413 | 0.4375 | -0.059 ± 0.0078 | 0.0 (3) |
| 5-10 | 7103 | 0.2012 | 0.1979 | +0.0032 ± 0.0008 | 0.5878 | 0.5768 | 0.4845 | 0.411 | 0.4264 | -0.044 ± 0.0053 | -0.0114 (22) |
| 10-15 | 5906 | 0.2023 | 0.1866 | +0.0157 ± 0.0014 | 0.5915 | 0.5477 | 0.4861 | 0.3622 | 0.3603 | -0.064 ± 0.0056 | -0.0281 (16) |
| 15-25 | 7389 | 0.2067 | 0.168 | +0.0388 ± 0.0019 | 0.6058 | 0.4986 | 0.5 | 0.3044 | 0.304 | -0.070 ± 0.0047 | -0.0027 (45) |
| 25-40 | 5724 | 0.2212 | 0.1261 | +0.0950 ± 0.0029 | 0.6363 | 0.3874 | 0.5263 | 0.2124 | 0.2224 | -0.057 ± 0.0046 | -0.0733 (3) |
| 40+ | 3789 | 0.3838 | 0.0447 | +0.3391 ± 0.0039 | 0.9995 | 0.173 | 0.6329 | 0.1042 | 0.0599 | -0.078 ± 0.0032 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 734 | 0.2076 | 0.2082 | -0.0006 ± 0.0006 | 0.5976 | 0.5993 | 0.5048 | 0.4901 | 0.5218 | -0.098 ± 0.0182 | -0.0117 (6) |
| 3-5 | 520 | 0.213 | 0.2101 | +0.0029 ± 0.0016 | 0.6076 | 0.6019 | 0.5118 | 0.4722 | 0.4519 | -0.133 ± 0.0216 | 0.01 (2) |
| 5-10 | 1158 | 0.2066 | 0.2041 | +0.0026 ± 0.002 | 0.5997 | 0.5921 | 0.5412 | 0.4665 | 0.4896 | -0.098 ± 0.0137 | -0.01 (4) |
| 10-15 | 1015 | 0.2158 | 0.2105 | +0.0053 ± 0.0036 | 0.6238 | 0.608 | 0.5658 | 0.4415 | 0.4857 | -0.101 ± 0.015 | -0.04 (5) |
| 15-25 | 1465 | 0.2317 | 0.2132 | +0.0186 ± 0.0047 | 0.6585 | 0.6108 | 0.5839 | 0.3886 | 0.441 | -0.102 ± 0.0123 | -0.012 (10) |
| 25-40 | 1034 | 0.2684 | 0.1991 | +0.0694 ± 0.0087 | 0.749 | 0.5788 | 0.6604 | 0.3467 | 0.3956 | -0.127 ± 0.0139 | -0.008 (5) |
| 40+ | 379 | 0.3657 | 0.1638 | +0.2019 ± 0.0207 | 0.9977 | 0.4941 | 0.7336 | 0.2465 | 0.2982 | -0.084 ± 0.02 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4218 | 0.1916 | 0.1919 | -0.0003 ± 0.0002 | 0.5591 | 0.5595 | 0.5075 | 0.4925 | 0.5114 | -0.038 ± 0.007 | -0.0154 (26) |
| 3-5 | 2903 | 0.1932 | 0.1922 | +0.0010 ± 0.0007 | 0.5622 | 0.5589 | 0.5094 | 0.4697 | 0.4757 | -0.046 ± 0.0083 | 0.01 (2) |
| 5-10 | 6347 | 0.1984 | 0.1946 | +0.0038 ± 0.0008 | 0.5817 | 0.5683 | 0.5075 | 0.4335 | 0.4471 | -0.044 ± 0.0056 | -0.0117 (6) |
| 10-15 | 5284 | 0.2034 | 0.1926 | +0.0108 ± 0.0015 | 0.5967 | 0.5631 | 0.5134 | 0.3895 | 0.4086 | -0.047 ± 0.0061 | -0.0189 (18) |
| 15-25 | 7364 | 0.2173 | 0.181 | +0.0363 ± 0.0019 | 0.6317 | 0.5309 | 0.5232 | 0.3281 | 0.3358 | -0.062 ± 0.005 | -0.0084 (43) |
| 25-40 | 6742 | 0.251 | 0.1373 | +0.1137 ± 0.0029 | 0.7082 | 0.4197 | 0.5593 | 0.2426 | 0.225 | -0.082 ± 0.0045 | -0.0095 (20) |
| 40+ | 5269 | 0.4005 | 0.0595 | +0.3410 ± 0.0039 | 1.0561 | 0.2138 | 0.6545 | 0.1188 | 0.0824 | -0.073 ± 0.0033 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 878 | 0.1965 | 0.1981 | -0.0017 ± 0.0005 | 0.5722 | 0.5764 | 0.5027 | 0.4872 | 0.5376 | -0.047 ± 0.0157 | -0.012 (10) |
| 3-5 | 618 | 0.2085 | 0.2067 | +0.0018 ± 0.0015 | 0.6024 | 0.5959 | 0.4962 | 0.4565 | 0.4563 | -0.117 ± 0.0191 | -0.0 (4) |
| 5-10 | 1381 | 0.2023 | 0.1995 | +0.0027 ± 0.0018 | 0.5896 | 0.5812 | 0.5109 | 0.4371 | 0.454 | -0.102 ± 0.0124 | -0.01 (9) |
| 10-15 | 1104 | 0.212 | 0.2054 | +0.0066 ± 0.0034 | 0.6149 | 0.5948 | 0.5401 | 0.4168 | 0.4529 | -0.103 ± 0.0137 | -0.0286 (7) |
| 15-25 | 1330 | 0.2325 | 0.2138 | +0.0187 ± 0.0049 | 0.6632 | 0.6118 | 0.5881 | 0.3938 | 0.4429 | -0.114 ± 0.0127 | -0.03 (1) |
| 25-40 | 813 | 0.2111 | 0.211 | +0.0001 ± 0.0094 | 0.6098 | 0.6054 | 0.6641 | 0.3532 | 0.5068 | -0.058 ± 0.0145 | -0.0267 (3) |
| 40+ | 181 | 0.3079 | 0.1872 | +0.1206 ± 0.0288 | 0.8361 | 0.5517 | 0.7477 | 0.2942 | 0.3978 | -0.091 ± 0.0296 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4707 | 0.1836 | 0.1842 | -0.0006 ± 0.0002 | 0.5411 | 0.542 | 0.4823 | 0.467 | 0.4852 | -0.033 ± 0.0063 | -0.0137 (41) |
| 3-5 | 3356 | 0.203 | 0.2011 | +0.0019 ± 0.0006 | 0.5897 | 0.5829 | 0.4808 | 0.4413 | 0.4374 | -0.059 ± 0.0079 | -0.01 (19) |
| 5-10 | 7292 | 0.1954 | 0.1909 | +0.0045 ± 0.0008 | 0.574 | 0.5592 | 0.4872 | 0.4132 | 0.42 | -0.051 ± 0.0052 | -0.0105 (37) |
| 10-15 | 5828 | 0.1936 | 0.1796 | +0.0139 ± 0.0014 | 0.5718 | 0.5314 | 0.4952 | 0.372 | 0.3765 | -0.059 ± 0.0056 | -0.0146 (13) |
| 15-25 | 7474 | 0.2132 | 0.1733 | +0.0399 ± 0.0019 | 0.6211 | 0.5105 | 0.5141 | 0.3195 | 0.3156 | -0.073 ± 0.0048 | -0.0533 (3) |
| 25-40 | 5724 | 0.2164 | 0.1278 | +0.0886 ± 0.003 | 0.6257 | 0.3913 | 0.5298 | 0.2142 | 0.2338 | -0.049 ± 0.0046 | -0.02 (4) |
| 40+ | 3746 | 0.3934 | 0.0503 | +0.3431 ± 0.0041 | 1.0255 | 0.1873 | 0.6424 | 0.1107 | 0.067 | -0.078 ± 0.0035 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1302 | 0.1958 | 0.1958 | -0.0000 ± 0.0004 | 0.5696 | 0.5695 | 0.5053 | 0.4903 | 0.4931 | -0.071 ± 0.0125 | -0.0213 (54) |
| 3-5 | 914 | 0.1897 | 0.1895 | +0.0002 ± 0.0012 | 0.5561 | 0.555 | 0.4949 | 0.455 | 0.4716 | -0.060 ± 0.0147 | -0.0194 (34) |
| 5-10 | 1891 | 0.2011 | 0.1964 | +0.0047 ± 0.0015 | 0.5908 | 0.5759 | 0.5053 | 0.4316 | 0.4368 | -0.077 ± 0.0104 | -0.005 (78) |
| 10-15 | 1302 | 0.2173 | 0.2036 | +0.0137 ± 0.0031 | 0.6282 | 0.5912 | 0.538 | 0.4152 | 0.4194 | -0.094 ± 0.0129 | 0.0014 (65) |
| 15-25 | 1678 | 0.2309 | 0.2082 | +0.0226 ± 0.0044 | 0.6584 | 0.6006 | 0.5879 | 0.393 | 0.4356 | -0.089 ± 0.0113 | -0.0214 (59) |
| 25-40 | 1042 | 0.2414 | 0.2103 | +0.0311 ± 0.0087 | 0.6898 | 0.6032 | 0.6879 | 0.3757 | 0.4818 | -0.091 ± 0.0133 | -0.0252 (27) |
| 40+ | 360 | 0.326 | 0.2018 | +0.1242 ± 0.0227 | 0.9445 | 0.5875 | 0.8193 | 0.3423 | 0.4667 | -0.098 ± 0.021 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4849 | 0.1758 | 0.1759 | -0.0002 ± 0.0002 | 0.5205 | 0.5205 | 0.5117 | 0.4965 | 0.5077 | -0.038 ± 0.0061 | -0.0145 (98) |
| 3-5 | 3330 | 0.1947 | 0.1937 | +0.0010 ± 0.0006 | 0.5672 | 0.5649 | 0.5011 | 0.4614 | 0.4688 | -0.043 ± 0.0077 | -0.0204 (72) |
| 5-10 | 6793 | 0.198 | 0.1914 | +0.0066 ± 0.0008 | 0.5822 | 0.5632 | 0.5006 | 0.4269 | 0.4204 | -0.064 ± 0.0054 | -0.0084 (134) |
| 10-15 | 4695 | 0.2109 | 0.1948 | +0.0162 ± 0.0016 | 0.6128 | 0.5708 | 0.5369 | 0.414 | 0.4085 | -0.072 ± 0.0065 | -0.0053 (106) |
| 15-25 | 5645 | 0.2303 | 0.2 | +0.0303 ± 0.0023 | 0.662 | 0.5792 | 0.5736 | 0.3782 | 0.4 | -0.066 ± 0.006 | -0.026 (108) |
| 25-40 | 3795 | 0.258 | 0.189 | +0.0690 ± 0.0044 | 0.7303 | 0.551 | 0.6388 | 0.3262 | 0.3744 | -0.072 ± 0.0069 | -0.0246 (52) |
| 40+ | 1640 | 0.372 | 0.1562 | +0.2158 ± 0.0101 | 1.0525 | 0.4657 | 0.7443 | 0.2428 | 0.289 | -0.069 ± 0.0092 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 6305 | 1.022 ± 0.035 | 1.099 | 0.169 | 0.1667 | 0.215 | 0.2051 |
| gen2 | 6305 | 0.811 ± 0.032 | 1.066 | 0.1722 | 0.1671 | 0.2343 | 0.2049 |
| gen1_elo | 6305 | 0.997 ± 0.034 | 1.09 | 0.1758 | 0.1668 | 0.2143 | 0.2052 |
| gen1_sr | 6305 | 0.995 ± 0.042 | 1.124 | 0.1324 | 0.1688 | 0.2302 | 0.2046 |
| gen1_ledger | 8489 | 0.861 ± 0.026 | 1.069 | 0.1887 | 0.1751 | 0.2177 | 0.2009 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 30,693)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 7,018 | 22.9% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,812 | 22.2% |
| BOOK_QUALITY | execution | 5,724 | 18.6% |
| POOR_DATA | data | 3,562 | 11.6% |
| LIMITED_DATA | data | 1,909 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,732 | 5.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,296 | 4.2% |
| IDENTITY_AMBIGUOUS | mapping | 1,256 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 864 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 519 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 22.9%, coverage 22.2%, execution 18.6%, data 17.8%, market_freshness/coverage 8.5%, model_calibration_or_unknown 4.2%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.3%, LOW_DATA_QUALITY 71.5%, THIN_PLAYER_HISTORY 60.0%, STALE_PLAYER_DATA 51.9%, STALE_KALSHI_QUOTE 45.1%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 33.0%, WIDE_SPREAD 24.9%, MODEL_HIGH_UNCERTAINTY 18.5%, PLAYER_IDENTITY_RISK 15.5%, LEVEL_TRANSFER_RISK 10.2%, LOW_DISPLAYED_LIQUIDITY 8.3%, EVENT_MAPPING_RISK 7.4%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.4%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.6%, POST_SETTLEMENT_OBSERVATION 22.2%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 16,371)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,498 | 33.6% |
| STALE_QUOTE | market_freshness | 3,171 | 19.4% |
| BOOK_QUALITY | execution | 2,979 | 18.2% |
| POOR_DATA | data | 1,545 | 9.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 914 | 5.6% |
| IDENTITY_AMBIGUOUS | mapping | 690 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 563 | 3.4% |
| LIMITED_DATA | data | 562 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 320 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 128 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.6%, market_freshness 19.4%, execution 18.2%, data 12.9%, market_freshness/coverage 9.0%, mapping 4.2%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.9%, LOW_DATA_QUALITY 75.0%, THIN_PLAYER_HISTORY 62.2%, STALE_KALSHI_QUOTE 52.6%, STALE_PLAYER_DATA 46.0%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 34.1%, WIDE_SPREAD 24.4%, MODEL_HIGH_UNCERTAINTY 19.1%, PLAYER_IDENTITY_RISK 18.5%, LEVEL_TRANSFER_RISK 9.1%, EVENT_MAPPING_RISK 9.0%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 5.0%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.6%, POST_SETTLEMENT_OBSERVATION 33.6%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 13019, "IDENTITY_AMBIGUOUS": 3352}; ticker orientation: {"VERIFIED": 16371}.

Checks: discipline:AMBIGUOUS 1105, discipline:PASS 15266, identity_confidence:AMBIGUOUS 3028, identity_confidence:PASS 13343, level_mapping:NA 1117, level_mapping:PASS 15254, market_pair:AMBIGUOUS 484, market_pair:NA 363, market_pair:PASS 15524, model_complement:NA 326, model_complement:PASS 16045, namesake:AMBIGUOUS 6, namesake:PASS 16365, physical_match_id:NA 5650, physical_match_id:PASS 10721, player_ids:PASS 16371, same_pair_other_event:PASS 16371, ticker_orientation:PASS 16371

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,099 | 3.9% | 3.4% | 1.5% | {"market_freshness": 58, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 20, "market_freshness/coverage": 17} | 5.62 | 0.2226 / 0.2166 (735) | 24.1% | 2.6% | 3.1% | 2.8% |
| CHALLENGER | 10,904 | 16.3% | 6.3% | 10.9% | {"coverage": 1037, "market_freshness/coverage": 210, "market_freshness": 209, "data": 154, "model_calibration_or_unknown": 78, "execution": 41, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.39 | 0.2218 / 0.2108 (2502) | 37.1% | 15.9% | 4.2% | 22.2% |
| DOUBLES | 2,320 | 47.6% | 47.6% | 6.8% | {"execution": 633, "mapping": 298, "market_freshness": 106, "market_freshness/coverage": 61, "coverage": 7} | 23.84 | 0.3042 / 0.2385 (554) | 10.1% | 0.0% | 100.0% | 6.0% |
| ITF_MEN | 21,013 | 25.2% | 17.9% | 32.4% | {"coverage": 1825, "market_freshness": 1019, "execution": 953, "data": 793, "market_freshness/coverage": 504, "mapping": 195, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.81 | 0.2173 / 0.1996 (4310) | 38.7% | 69.2% | 16.1% | 21.3% |
| ITF_WOMEN | 27,871 | 26.5% | 19.1% | 45.1% | {"coverage": 2557, "market_freshness": 1591, "execution": 1269, "data": 1062, "market_freshness/coverage": 629, "mapping": 174, "model_calibration_or_unknown": 84, "model_calibration": 22} | 12.55 | 0.2031 / 0.1947 (5216) | 40.2% | 57.4% | 9.8% | 21.2% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,582 | 6.0% | 5.1% | 1.7% | {"market_freshness": 103, "model_calibration_or_unknown": 50, "coverage": 37, "execution": 29, "data": 24, "model_calibration": 20, "market_freshness/coverage": 13, "mapping": 1} | 7.7 | 0.228 / 0.2224 (725) | 29.2% | 2.0% | 1.4% | 3.6% |
| WTA125 | 2,462 | 11.1% | 9.5% | 1.7% | {"market_freshness": 83, "model_calibration_or_unknown": 51, "market_freshness/coverage": 42, "data": 38, "execution": 24, "model_calibration": 17, "coverage": 14, "mapping": 4} | 9.21 | 0.2098 / 0.1927 (710) | 28.3% | 11.0% | 4.4% | 7.1% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.4h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 509 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 3 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 4 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 5 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 6 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 773 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 7 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 8 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 164 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 9 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 10 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 113 min (STALE); no external reference |
| 13 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 14 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 207 min (STALE); no external reference |
| 17 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 18 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
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
| 31 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
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
| 42 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 43 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 44 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 124 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 45 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 46 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 252 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |
| 47 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXATPCHALLENGERMATCH-26NOV02TOBSTO-TOB` | CHALLENGER | fair_v1 | 80% / 2% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 165 min (STALE); data POOR (grade F, thinner serve sample 159.0, ratio 20.58); no external reference |
| 49 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 50 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9687, "by_level_share_of_ge_25pp": {"ATP": 0.0145, "CHALLENGER": 0.1089, "DOUBLES": 0.0675, "ITF_MEN": 0.3236, "ITF_WOMEN": 0.4513, "OTHER": 0.0007, "WTA": 0.0169, "WTA125": 0.0167}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5264, "share_primary_cause_market_settled_or_in_play": 0.426, "share_primary_cause_stale_quote_only": 0.1937}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 16371, "identity_ambiguous_share": 0.2048, "ticker_orientation": {"VERIFIED": 16371}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 10721, "with_external": 564, "coverage": 0.0526, "external_status": {"EXTERNAL_STALE": 355, "AGREES_WITH_KALSHI": 196, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 355, "MODEL_LONE_OUTLIER": 196, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3475, "share_external_supports_model": 0.023}, "pregame_clean_ge_25pp": {"n": 5148, "with_external": 535, "coverage": 0.1039, "external_status": {"EXTERNAL_STALE": 333, "AGREES_WITH_KALSHI": 189, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 333, "MODEL_LONE_OUTLIER": 189, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3533, "share_external_supports_model": 0.0243}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 479.0, "median_sample_ratio": 2.46, "median_min_matches": 19.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2074, "data_status": {"POOR": 9229, "LIMITED": 4252, "ADEQUATE": 2890}, "comparison_lt_10pp": {"median_thinner_serve_points": 1745.0, "median_sample_ratio": 1.69, "median_min_matches": 91.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1258, "model_minus_observed": 0.0576, "kalshi_minus_observed": -0.0829, "brier_diff_model_minus_kalshi": -0.0011}, "4-10x": {"n": 869, "model_minus_observed": 0.0901, "kalshi_minus_observed": -0.0572, "brier_diff_model_minus_kalshi": 0.0085}, "<2x": {"n": 3112, "model_minus_observed": 0.0939, "kalshi_minus_observed": -0.0285, "brier_diff_model_minus_kalshi": 0.0128}, ">=10x": {"n": 1066, "model_minus_observed": 0.1199, "kalshi_minus_observed": -0.0544, "brier_diff_model_minus_kalshi": 0.0156}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 6305, "model": {"intercept": -0.544, "slope": 0.811, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.186, "slope": 1.066, "slope_se": 0.036}, "mean_extremity_model": 0.1722, "mean_extremity_kalshi": 0.1671, "model_brier": 0.2343, "kalshi_brier": 0.2049, "brier_diff_model_minus_kalshi": 0.0293, "brier_diff_se": 0.0024, "model_logloss": 0.6661, "kalshi_logloss": 0.5926}, "fair_v1": {"n": 6305, "model": {"intercept": -0.433, "slope": 1.022, "slope_se": 0.035}, "kalshi_mid_same_rows": {"intercept": 0.264, "slope": 1.099, "slope_se": 0.036}, "mean_extremity_model": 0.169, "mean_extremity_kalshi": 0.1667, "model_brier": 0.215, "kalshi_brier": 0.2051, "brier_diff_model_minus_kalshi": 0.0099, "brier_diff_se": 0.002, "model_logloss": 0.6191, "kalshi_logloss": 0.5929}, "gen1_elo": {"n": 6305, "model": {"intercept": -0.419, "slope": 0.997, "slope_se": 0.034}, "kalshi_mid_same_rows": {"intercept": 0.271, "slope": 1.09, "slope_se": 0.036}, "mean_extremity_model": 0.1758, "mean_extremity_kalshi": 0.1668, "model_brier": 0.2143, "kalshi_brier": 0.2052, "brier_diff_model_minus_kalshi": 0.0091, "brier_diff_se": 0.002, "model_logloss": 0.6181, "kalshi_logloss": 0.5931}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2457, "share_ge_15": 0.4409, "median_abs_gap": 12.96, "n": 43641}, "gen1_elo": {"share_ge_25": 0.2433, "share_ge_15": 0.438, "median_abs_gap": 12.73, "n": 43641}, "gen1_sr": {"share_ge_25": 0.3112, "share_ge_15": 0.5175, "median_abs_gap": 15.71, "n": 43641}, "gen2": {"share_ge_25": 0.3135, "share_ge_15": 0.5076, "median_abs_gap": 15.36, "n": 43641}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1517, "share_ge_15": 0.3538, "median_abs_gap": 10.71, "n": 33937}, "gen1_elo": {"share_ge_25": 0.1507, "share_ge_15": 0.3498, "median_abs_gap": 10.49, "n": 33936}, "gen1_sr": {"share_ge_25": 0.217, "share_ge_15": 0.4387, "median_abs_gap": 12.97, "n": 33939}, "gen2": {"share_ge_25": 0.2323, "share_ge_15": 0.4384, "median_abs_gap": 12.83, "n": 33939}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.62, "share_ge_25_all": 0.0389, "share_ge_25_pregame_clean": 0.0337}, "WTA": {"median_abs_gap_pregame_clean": 7.7, "share_ge_25_all": 0.0605, "share_ge_25_pregame_clean": 0.0514}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2373, "share_within_10pp_all": 0.4391, "share_within_10pp_pregame_clean": 0.4909, "corr_model_vs_mid_pregame_clean": 0.8495}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 918, "model_brier": 0.1995, "kalshi_brier": 0.1999, "brier_diff_model_minus_kalshi": -0.0005}, "10-15": {"n_settled": 1102, "model_brier": 0.2209, "kalshi_brier": 0.2112, "brier_diff_model_minus_kalshi": 0.0097}, "15-25": {"n_settled": 1406, "model_brier": 0.2253, "kalshi_brier": 0.2096, "brier_diff_model_minus_kalshi": 0.0157}, "25-40": {"n_settled": 800, "model_brier": 0.22, "kalshi_brier": 0.2065, "brier_diff_model_minus_kalshi": 0.0135}, "3-5": {"n_settled": 574, "model_brier": 0.2056, "kalshi_brier": 0.205, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 172, "model_brier": 0.2915, "kalshi_brier": 0.1797, "brier_diff_model_minus_kalshi": 0.1118}, "5-10": {"n_settled": 1333, "model_brier": 0.2012, "kalshi_brier": 0.2013, "brier_diff_model_minus_kalshi": -0.0001}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.544, "slope": 0.811, "slope_se": 0.032}, "kalshi_slope": {"intercept": 0.186, "slope": 1.066, "slope_se": 0.036}, "n": 6305}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.489, "slope": 0.861, "slope_se": 0.026}, "kalshi_slope": {"intercept": 0.169, "slope": 1.069, "slope_se": 0.03}, "n": 8489}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 554, "model_brier": 0.3042, "kalshi_brier": 0.2385, "brier_diff_model_minus_kalshi": 0.0657, "brier_diff_se": 0.0127, "corr_model_outcome": 0.0713, "corr_kalshi_outcome": 0.2333}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
