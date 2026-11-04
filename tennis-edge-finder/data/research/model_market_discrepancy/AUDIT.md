# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-04T06:53Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 76,050): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.4%, 15-25 19.0%, 25-40 13.7%, 40+ 8.0%; median gap 11.8 pp.
* **Where the extremes live**: 96.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.5%, Challenger 10.8%, doubles 6.7%). Main tour: ATP 3.9% and WTA 6.1% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 16,475): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.4%, STALE_QUOTE 19.6%, BOOK_QUALITY 18.1%, POOR_DATA 9.4%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IDENTITY_AMBIGUOUS 4.2%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.4%, market_freshness 19.6%, execution 18.1%, data 12.9%, market_freshness/coverage 9.1%, mapping 4.2%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.7% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 16,475 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.8% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 476.0 points vs 1743.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.027, Gen-2 0.816, Gen-1 ledger 0.865 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 816 model 0.2207 vs Kalshi 0.2064; n 175 model 0.2937 vs Kalshi 0.1769.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 326,870 model-market comparisons (532,908 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 108,735 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-04T06:36:13.660493+00:00'], shadow board 87,481 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-04T06:36:17.092943+00:00'], Model 4 41,375 rows, 26,639 settled tickers, 10,109 tickers with an external scan.
* By model: {"gen1_ledger": 73559, "gen1_elo": 43961, "fair_v1": 43961, "gen2": 43961, "gen1_sr": 43961, "model4_fundamental": 38775, "model4_conditioned": 38692}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 76,050 | 14.1 | 9.6 | 20.2 | 15.4 | 19.0 | 13.7 | 8.0 | 11.8 | 40.7% | 21.7% |
| MW fair_v1 | 43,961 | 12.9 | 8.7 | 18.8 | 15.5 | 19.5 | 14.7 | 9.8 | 12.96 | 44.1% | 24.5% |
| MW gen1_elo | 43,961 | 12.6 | 8.8 | 19.4 | 15.4 | 19.5 | 14.6 | 9.7 | 12.73 | 43.8% | 24.3% |
| MW gen1_ledger | 32,089 | 15.8 | 10.9 | 22.1 | 15.2 | 18.4 | 12.2 | 5.5 | 10.29 | 36.1% | 17.7% |
| MW gen1_sr | 43,961 | 10.2 | 7.3 | 16.9 | 13.9 | 20.6 | 18.6 | 12.5 | 15.7 | 51.7% | 31.1% |
| MW gen2 | 43,961 | 11.2 | 7.6 | 16.7 | 13.8 | 19.4 | 17.7 | 13.6 | 15.36 | 50.8% | 31.3% |
| all families model4_conditioned | 38,692 | 22.2 | 18.0 | 34.2 | 17.2 | 5.0 | 2.2 | 1.2 | 6.06 | 8.4% | 3.4% |
| all families model4_fundamental | 38,775 | 17.3 | 13.4 | 33.9 | 20.0 | 10.1 | 3.8 | 1.6 | 7.64 | 15.4% | 5.3% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.1%, >=15pp 40.7%, >=20pp 30.0%, >=25pp 21.7%, >=30pp 15.6%, >=40pp 8.0%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.31pp; >=10pp 44.7%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,854 | 28.1 | 15.5 | 27.8 | 13.4 | 10.8 | 3.7 | 0.6 | 5.85 | 15.1% | 4.3% |
| CHALLENGER | 6,657 | 16.1 | 9.8 | 20.8 | 15.3 | 15.9 | 11.4 | 10.6 | 10.84 | 37.9% | 22.0% |
| ITF_MEN | 12,176 | 9.8 | 7.3 | 16.9 | 15.1 | 21.4 | 17.4 | 12.1 | 15.35 | 50.9% | 29.5% |
| ITF_WOMEN | 17,069 | 9.5 | 7.1 | 16.0 | 15.1 | 22.1 | 18.2 | 12.0 | 15.74 | 52.3% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,920 | 17.0 | 13.0 | 24.7 | 21.2 | 16.3 | 6.7 | 1.1 | 8.68 | 24.1% | 7.8% |
| WTA125 | 1,279 | 15.9 | 7.0 | 22.8 | 19.9 | 20.5 | 12.1 | 1.7 | 10.67 | 34.3% | 13.8% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,854 | 26.7 | 15.7 | 26.1 | 15.5 | 11.5 | 3.7 | 0.8 | 6.07 | 16.0% | 4.5% |
| CHALLENGER | 6,657 | 15.0 | 9.0 | 18.6 | 14.2 | 18.4 | 13.5 | 11.3 | 12.4 | 43.2% | 24.8% |
| ITF_MEN | 12,176 | 8.1 | 6.2 | 15.1 | 13.7 | 19.8 | 20.8 | 16.4 | 17.98 | 56.9% | 37.2% |
| ITF_WOMEN | 17,069 | 7.9 | 5.8 | 14.1 | 12.8 | 20.6 | 21.2 | 17.7 | 19.07 | 59.4% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,920 | 14.4 | 10.2 | 21.8 | 16.1 | 22.1 | 12.8 | 2.6 | 11.03 | 37.5% | 15.4% |
| WTA125 | 1,279 | 10.2 | 7.3 | 16.3 | 15.6 | 24.3 | 17.4 | 8.8 | 15.18 | 50.5% | 26.2% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,854 | 22.8 | 13.8 | 25.1 | 15.7 | 15.3 | 6.2 | 1.2 | 7.3 | 22.7% | 7.4% |
| CHALLENGER | 6,657 | 15.2 | 9.6 | 21.0 | 15.6 | 15.9 | 11.9 | 10.8 | 11.15 | 38.6% | 22.7% |
| ITF_MEN | 12,176 | 9.3 | 7.2 | 17.3 | 14.2 | 22.0 | 17.5 | 12.5 | 15.75 | 52.0% | 30.0% |
| ITF_WOMEN | 17,069 | 9.3 | 6.9 | 16.4 | 15.8 | 22.2 | 18.1 | 11.3 | 15.52 | 51.6% | 29.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,920 | 22.9 | 16.7 | 31.9 | 15.0 | 9.0 | 3.3 | 1.1 | 6.12 | 13.4% | 4.4% |
| WTA125 | 1,279 | 21.4 | 13.1 | 25.8 | 18.3 | 15.2 | 5.9 | 0.3 | 8.01 | 21.3% | 6.2% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,271 | 26.1 | 19.6 | 30.3 | 12.4 | 8.4 | 2.6 | 0.4 | 5.43 | 11.5% | 3.1% |
| CHALLENGER | 4,301 | 22.5 | 14.5 | 27.3 | 14.6 | 13.7 | 5.9 | 1.6 | 7.1 | 21.1% | 7.5% |
| DOUBLES | 2,345 | 5.1 | 4.4 | 12.2 | 10.4 | 20.5 | 25.1 | 22.3 | 23.76 | 67.8% | 47.4% |
| ITF_MEN | 9,079 | 12.9 | 9.5 | 21.1 | 15.8 | 21.5 | 13.2 | 6.0 | 11.91 | 40.7% | 19.2% |
| ITF_WOMEN | 11,052 | 13.4 | 9.1 | 19.9 | 15.7 | 21.2 | 15.2 | 5.5 | 12.27 | 41.9% | 20.6% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,687 | 24.1 | 16.3 | 30.6 | 16.9 | 9.1 | 2.7 | 0.2 | 6.57 | 12.0% | 3.0% |
| WTA125 | 1,205 | 25.3 | 12.9 | 21.1 | 19.2 | 13.3 | 6.7 | 1.5 | 7.81 | 21.5% | 8.2% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,741 | 28.6 | 15.7 | 28.2 | 13.3 | 10.6 | 3.3 | 0.3 | 5.75 | 14.2% | 3.6% |
| CHALLENGER | 4,730 | 20.6 | 12.2 | 25.7 | 17.9 | 15.9 | 6.0 | 1.7 | 8.23 | 23.6% | 7.7% |
| ITF_MEN | 8,981 | 12.0 | 8.6 | 20.3 | 17.1 | 22.2 | 14.2 | 5.5 | 12.51 | 41.9% | 19.7% |
| ITF_WOMEN | 12,714 | 11.3 | 8.5 | 18.7 | 17.3 | 24.0 | 15.2 | 5.1 | 13.28 | 44.3% | 20.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,815 | 17.3 | 13.0 | 25.0 | 21.6 | 16.3 | 6.2 | 0.6 | 8.52 | 23.2% | 6.9% |
| WTA125 | 1,235 | 16.2 | 7.0 | 22.4 | 20.2 | 21.0 | 11.7 | 1.5 | 10.67 | 34.2% | 13.3% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,741 | 27.0 | 16.1 | 26.3 | 15.4 | 11.4 | 3.3 | 0.4 | 5.99 | 15.1% | 3.7% |
| CHALLENGER | 4,730 | 18.9 | 11.2 | 23.3 | 16.6 | 18.8 | 9.4 | 1.9 | 9.06 | 30.1% | 11.3% |
| ITF_MEN | 8,982 | 9.5 | 7.3 | 17.4 | 15.8 | 21.4 | 18.9 | 9.6 | 14.98 | 49.9% | 28.5% |
| ITF_WOMEN | 12,715 | 8.8 | 6.8 | 15.9 | 14.4 | 22.7 | 20.5 | 10.9 | 16.58 | 54.1% | 31.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,815 | 14.6 | 10.3 | 22.0 | 16.2 | 22.2 | 12.6 | 1.9 | 10.93 | 36.8% | 14.6% |
| WTA125 | 1,235 | 10.3 | 7.4 | 16.5 | 15.7 | 24.3 | 17.6 | 8.3 | 15.02 | 50.1% | 25.8% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,214 | 26.3 | 19.8 | 30.3 | 12.6 | 8.1 | 2.5 | 0.4 | 5.38 | 11.0% | 2.9% |
| CHALLENGER | 3,793 | 23.8 | 15.4 | 28.4 | 14.8 | 13.1 | 4.1 | 0.4 | 6.61 | 17.6% | 4.5% |
| DOUBLES | 2,205 | 5.0 | 4.5 | 12.4 | 10.6 | 20.2 | 25.0 | 22.3 | 23.73 | 67.5% | 47.3% |
| ITF_MEN | 7,790 | 13.7 | 10.1 | 22.7 | 16.3 | 21.5 | 11.7 | 4.0 | 11.02 | 37.2% | 15.7% |
| ITF_WOMEN | 9,464 | 14.0 | 9.6 | 21.1 | 16.3 | 21.3 | 14.1 | 3.5 | 11.46 | 39.0% | 17.7% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,627 | 24.5 | 16.7 | 30.6 | 17.0 | 9.0 | 2.1 | 0.1 | 6.43 | 11.2% | 2.2% |
| WTA125 | 1,070 | 26.4 | 13.7 | 22.1 | 20.2 | 12.3 | 4.8 | 0.5 | 7.3 | 17.6% | 5.2% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,345 | 5.1 | 4.4 | 12.2 | 10.4 | 20.5 | 25.1 | 22.3 | 23.76 | 67.8% | 47.4% |
| singles | 29,744 | 16.6 | 11.4 | 22.9 | 15.5 | 18.2 | 11.2 | 4.2 | 9.76 | 33.6% | 15.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 77 | 7.8 | 9.1 | 19.5 | 11.7 | 19.5 | 20.8 | 11.7 | 15.79 | 51.9% | 32.5% |
| Clay | 8,770 | 12.9 | 9.3 | 19.9 | 15.9 | 19.5 | 13.7 | 8.8 | 12.39 | 41.9% | 22.4% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 28,908 | 13.4 | 8.7 | 18.8 | 15.3 | 19.1 | 14.8 | 9.8 | 12.84 | 43.8% | 24.7% |
| UNKNOWN | 5,969 | 10.5 | 7.6 | 17.0 | 16.4 | 21.5 | 15.9 | 11.1 | 14.3 | 48.5% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 12,513 | 19.8 | 11.9 | 22.7 | 16.0 | 14.8 | 8.9 | 5.9 | 8.72 | 29.6% | 14.8% |
| B | 5,440 | 12.9 | 8.8 | 19.5 | 15.9 | 19.6 | 12.6 | 10.8 | 12.59 | 43.0% | 23.4% |
| C | 6,206 | 11.9 | 8.9 | 19.6 | 16.1 | 18.4 | 14.6 | 10.6 | 12.87 | 43.6% | 25.2% |
| D | 6,988 | 11.7 | 8.4 | 17.7 | 15.5 | 21.7 | 15.7 | 9.2 | 13.76 | 46.7% | 24.9% |
| F | 12,814 | 7.4 | 5.5 | 14.9 | 14.7 | 23.5 | 20.9 | 13.1 | 17.73 | 57.5% | 34.0% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,607 | 24.6 | 16.1 | 29.0 | 14.9 | 10.7 | 3.4 | 1.2 | 6.36 | 15.4% | 4.7% |
| B | 4,532 | 16.8 | 10.8 | 24.0 | 16.9 | 18.8 | 9.7 | 3.1 | 9.69 | 31.6% | 12.8% |
| C | 6,298 | 11.3 | 7.7 | 19.2 | 14.5 | 21.0 | 15.8 | 10.3 | 13.67 | 47.2% | 26.1% |
| D | 4,742 | 14.3 | 9.8 | 21.4 | 15.6 | 20.4 | 13.1 | 5.4 | 11.32 | 38.9% | 18.5% |
| F | 7,910 | 10.1 | 8.4 | 16.1 | 14.6 | 23.1 | 19.7 | 7.9 | 15.38 | 50.7% | 27.6% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 14,180 | 18.1 | 10.9 | 21.8 | 15.8 | 15.2 | 9.8 | 8.5 | 9.8 | 33.4% | 18.3% |
| LIMITED | 9,589 | 13.6 | 9.9 | 20.3 | 16.2 | 19.2 | 13.3 | 7.5 | 11.8 | 40.0% | 20.8% |
| POOR | 20,192 | 9.0 | 6.6 | 16.0 | 15.0 | 22.8 | 18.9 | 11.8 | 16.15 | 53.5% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,537 | 23.9 | 17.8 | 33.1 | 15.7 | 6.4 | 2.8 | 0.4 | 5.92 | 9.5% | 3.2% |
| GAME_SPREAD | 6,449 | 22.4 | 15.1 | 32.4 | 17.1 | 9.0 | 3.4 | 0.6 | 6.74 | 13.0% | 4.0% |
| MATCH_WINNER | 32,089 | 15.8 | 10.9 | 22.1 | 15.2 | 18.4 | 12.2 | 5.5 | 10.29 | 36.1% | 17.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 15,716 | 27.8 | 16.7 | 30.5 | 12.8 | 9.4 | 2.5 | 0.3 | 5.65 | 12.2% | 2.8% |
| TOTAL_GAMES | 10,744 | 9.9 | 10.8 | 35.4 | 26.1 | 10.5 | 4.2 | 3.0 | 9.22 | 17.8% | 7.2% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,748 | 24.5 | 28.9 | 33.2 | 8.2 | 4.0 | 1.0 | 0.3 | 4.79 | 5.2% | 1.2% |
| GAME_SPREAD | 8,948 | 46.7 | 16.2 | 24.8 | 7.5 | 2.3 | 1.9 | 0.6 | 3.31 | 4.8% | 2.5% |
| TOTAL_GAMES | 15,996 | 6.6 | 9.7 | 40.2 | 30.3 | 7.4 | 3.4 | 2.4 | 9.23 | 13.2% | 5.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,783 | 23.9 | 16.6 | 34.8 | 14.7 | 6.9 | 2.5 | 0.5 | 6.05 | 10.0% | 3.0% |
| GAME_SPREAD | 8,957 | 20.4 | 13.5 | 28.3 | 20.1 | 12.1 | 4.5 | 1.2 | 7.66 | 17.8% | 5.7% |
| TOTAL_GAMES | 16,035 | 10.0 | 10.7 | 36.2 | 24.5 | 11.6 | 4.5 | 2.6 | 9.09 | 18.7% | 7.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 43,961 | 44.1% | 24.5% | 12.96 | 35.4% | 15.2% | 10.71 |
| gen1_elo | 43,961 | 43.8% | 24.3% | 12.73 | 35.0% | 15.1% | 10.5 |
| gen1_sr | 43,961 | 51.7% | 31.1% | 15.7 | 43.9% | 21.7% | 12.98 |
| gen2 | 43,961 | 50.8% | 31.3% | 15.36 | 43.9% | 23.3% | 12.84 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 19,548 | 15.6 | 10.4 | 21.4 | 17.4 | 20.1 | 11.8 | 3.4 | 10.71 | 35.3% | 15.2% |
| STALE | 24,413 | 10.8 | 7.3 | 16.7 | 14.1 | 19.1 | 17.1 | 14.9 | 15.45 | 51.1% | 32.0% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 25,557 | 16.5 | 11.2 | 22.7 | 15.3 | 17.8 | 11.7 | 4.8 | 9.89 | 34.4% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 76,050 | 25557 | 23020 | 27473 | 24.6 | 115.7 | 1451.1 |
| ge_15pp | 30,953 | 8778 | 8187 | 13988 | 27.9 | 424.3 | 1451.1 |
| ge_25pp | 16,475 | 4225 | 3566 | 8684 | 32.4 | 580.2 | 1431.1 |
| lt_10pp | 33,403 | 12880 | 10891 | 9632 | 22.7 | 47.3 | 1421.1 |

Current slate `SL-20261104T065332Z-bee12bc8`: 880 priced rows, quote age at build {'median': 17.9, 'max': 17.9}, freshness {'AGING': 880}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 49 | 0.0 | 0.0 | 36.7 | 6.1 | 32.6 | 20.4 | 4.1 | 18.34 | 57.1% | 24.5% |
| EXTERNAL_LONE_OUTLIER | 28 | 67.9 | 32.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,330 | 19.5 | 10.9 | 25.5 | 17.9 | 17.8 | 7.4 | 0.9 | 8.71 | 26.1% | 8.3% |
| KALSHI_LONE_OUTLIER | 27 | 3.7 | 3.7 | 77.8 | 7.4 | 3.7 | 3.7 | 0.0 | 6.42 | 7.4% | 3.7% |
| MARKETS_AGREE | 887 | 66.0 | 34.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.21 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,949 | 0.0 | 2.4 | 37.1 | 26.2 | 24.3 | 9.2 | 0.8 | 11.81 | 34.3% | 10.1% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 43,961 | 7270 (16.5%) | 26.8% | 1.0% | {"EXTERNAL_STALE": 4330, "AGREES_WITH_KALSHI": 1949, "ALL_AGREE": 887, "SUPPORTS_MODEL_DIRECTION": 48, "EXTERNAL_OUTLIER": 28, "AGREES_WITH_MODEL": 27, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 19,376 | 1830 (9.4%) | 36.6% | 1.6% | {"EXTERNAL_STALE": 1131, "AGREES_WITH_KALSHI": 669, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 10,788 | 569 (5.3%) | 34.4% | 2.3% | {"EXTERNAL_STALE": 360, "AGREES_WITH_KALSHI": 196, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,200 | 540 (10.4%) | 35.0% | 2.4% | {"EXTERNAL_STALE": 338, "AGREES_WITH_KALSHI": 189, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 17,754 | 4147 (23.4%) | 18.5% | 1.0% | {"EXTERNAL_STALE": 2422, "ALL_AGREE": 887, "AGREES_WITH_KALSHI": 769, "EXTERNAL_OUTLIER": 28, "AGREES_WITH_MODEL": 23, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 8,533 | 10.4 | 7.7 | 19.4 | 14.8 | 21.7 | 16.1 | 9.9 | 14.02 | 47.7% | 26.0% |
| 4-10x | 5,871 | 11.1 | 8.5 | 18.6 | 15.4 | 22.1 | 14.2 | 10.0 | 13.75 | 46.4% | 24.3% |
| <2x | 22,574 | 15.1 | 9.8 | 19.8 | 16.2 | 17.4 | 13.0 | 8.7 | 11.48 | 39.1% | 21.7% |
| >=10x | 6,983 | 10.4 | 6.3 | 15.0 | 14.5 | 21.7 | 19.1 | 13.0 | 16.41 | 53.8% | 32.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 11,432 | 12.6 | 8.7 | 19.8 | 16.4 | 19.1 | 13.4 | 10.1 | 12.64 | 42.5% | 23.5% |
| 300-1000 | 9,451 | 11.8 | 8.8 | 17.7 | 15.5 | 20.5 | 16.2 | 9.4 | 13.58 | 46.1% | 25.6% |
| <300 | 13,870 | 8.3 | 5.8 | 15.1 | 14.7 | 23.1 | 20.0 | 13.1 | 17.12 | 56.2% | 33.0% |
| >=3000 | 9,208 | 21.4 | 12.9 | 24.1 | 15.8 | 13.7 | 7.1 | 4.9 | 7.64 | 25.7% | 12.0% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1291 | 0.548 | 0.4082 | 0.4903 | +0.058 | -0.082 | -0.0007 ± 0.0043 |
| ratio 4-10x | 888 | 0.582 | 0.4353 | 0.491 | +0.091 | -0.056 | 0.0092 ± 0.0054 |
| ratio <2x | 3181 | 0.5367 | 0.4143 | 0.4423 | +0.094 | -0.028 | 0.013 ± 0.0025 |
| ratio >=10x | 1083 | 0.5695 | 0.3955 | 0.4497 | +0.120 | -0.054 | 0.0159 ± 0.0055 |
| thinner_sample 1000-3000 | 1777 | 0.5385 | 0.4119 | 0.4524 | +0.086 | -0.041 | 0.0088 ± 0.0034 |
| thinner_sample 300-1000 | 1455 | 0.5676 | 0.4261 | 0.4838 | +0.084 | -0.058 | 0.0029 ± 0.0041 |
| thinner_sample <300 | 2109 | 0.5607 | 0.3922 | 0.4557 | +0.105 | -0.064 | 0.0136 ± 0.0039 |
| thinner_sample >=3000 | 1102 | 0.5291 | 0.4362 | 0.4483 | +0.081 | -0.012 | 0.0155 ± 0.0034 |
| data_status ADEQUATE | 1803 | 0.5312 | 0.4288 | 0.4426 | +0.089 | -0.014 | 0.0139 ± 0.0029 |
| data_status LIMITED | 1558 | 0.5488 | 0.4159 | 0.4711 | +0.078 | -0.055 | 0.0064 ± 0.0038 |
| data_status POOR | 3082 | 0.5632 | 0.4019 | 0.4643 | +0.099 | -0.062 | 0.0099 ± 0.0031 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 942 | 0.1992 | 0.1997 | -0.0005 ± 0.0005 | 0.5787 | 0.5799 | 0.5017 | 0.4866 | 0.5053 | -0.091 ± 0.0154 | -0.0087 (8) |
| 3-5 | 589 | 0.2047 | 0.2041 | +0.0006 ± 0.0015 | 0.5923 | 0.589 | 0.5022 | 0.4623 | 0.4754 | -0.105 ± 0.0191 | 0.01 (2) |
| 5-10 | 1370 | 0.2008 | 0.2008 | +0.0001 ± 0.0018 | 0.5873 | 0.5849 | 0.5128 | 0.4391 | 0.4723 | -0.089 ± 0.0126 | -0.0143 (7) |
| 10-15 | 1121 | 0.2208 | 0.2109 | +0.0098 ± 0.0034 | 0.6346 | 0.6062 | 0.5261 | 0.4026 | 0.4237 | -0.111 ± 0.0139 | -0.048 (5) |
| 15-25 | 1430 | 0.2247 | 0.2089 | +0.0159 ± 0.0047 | 0.6442 | 0.6012 | 0.5761 | 0.381 | 0.4385 | -0.105 ± 0.0121 | -0.004 (10) |
| 25-40 | 816 | 0.2207 | 0.2064 | +0.0143 ± 0.0095 | 0.6303 | 0.5947 | 0.6557 | 0.3456 | 0.4779 | -0.071 ± 0.0145 | -0.06 (2) |
| 40+ | 175 | 0.2937 | 0.1769 | +0.1168 ± 0.0284 | 0.7931 | 0.5276 | 0.7355 | 0.2823 | 0.3886 | -0.087 ± 0.0276 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5013 | 0.1852 | 0.1861 | -0.0009 ± 0.0002 | 0.5456 | 0.5466 | 0.4863 | 0.4711 | 0.5023 | -0.022 ± 0.0062 | -0.01 (28) |
| 3-5 | 3348 | 0.1965 | 0.1949 | +0.0016 ± 0.0006 | 0.5718 | 0.5656 | 0.4807 | 0.4409 | 0.44 | -0.056 ± 0.0077 | 0.0 (3) |
| 5-10 | 7222 | 0.2008 | 0.1978 | +0.0030 ± 0.0008 | 0.5869 | 0.5765 | 0.4851 | 0.4116 | 0.4283 | -0.043 ± 0.0053 | -0.0114 (22) |
| 10-15 | 6009 | 0.2026 | 0.1865 | +0.0161 ± 0.0014 | 0.5921 | 0.5473 | 0.4858 | 0.362 | 0.3588 | -0.065 ± 0.0056 | -0.0281 (16) |
| 15-25 | 7492 | 0.2067 | 0.1676 | +0.0391 ± 0.0019 | 0.6055 | 0.4977 | 0.4999 | 0.3044 | 0.3031 | -0.071 ± 0.0047 | -0.0027 (45) |
| 25-40 | 5777 | 0.2221 | 0.1265 | +0.0956 ± 0.0029 | 0.6381 | 0.3886 | 0.5269 | 0.2131 | 0.2223 | -0.058 ± 0.0045 | -0.0733 (3) |
| 40+ | 3817 | 0.3834 | 0.0453 | +0.3381 ± 0.0039 | 0.9986 | 0.1749 | 0.6327 | 0.1043 | 0.0608 | -0.077 ± 0.0033 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 754 | 0.2064 | 0.2071 | -0.0006 ± 0.0006 | 0.5949 | 0.5967 | 0.5043 | 0.4896 | 0.5212 | -0.097 ± 0.0179 | -0.0117 (6) |
| 3-5 | 529 | 0.213 | 0.2104 | +0.0027 ± 0.0016 | 0.6079 | 0.6028 | 0.5114 | 0.4717 | 0.4537 | -0.131 ± 0.0214 | 0.01 (2) |
| 5-10 | 1182 | 0.2066 | 0.204 | +0.0026 ± 0.002 | 0.5994 | 0.5916 | 0.5409 | 0.4662 | 0.489 | -0.098 ± 0.0136 | -0.01 (4) |
| 10-15 | 1040 | 0.2137 | 0.2085 | +0.0052 ± 0.0035 | 0.6191 | 0.6035 | 0.5652 | 0.4409 | 0.4856 | -0.100 ± 0.0148 | -0.04 (5) |
| 15-25 | 1497 | 0.2315 | 0.2123 | +0.0192 ± 0.0047 | 0.6577 | 0.6087 | 0.5846 | 0.3892 | 0.4402 | -0.104 ± 0.0122 | -0.012 (10) |
| 25-40 | 1056 | 0.269 | 0.1998 | +0.0692 ± 0.0086 | 0.7498 | 0.5807 | 0.6615 | 0.3478 | 0.3968 | -0.127 ± 0.0137 | -0.008 (5) |
| 40+ | 385 | 0.3677 | 0.163 | +0.2047 ± 0.0205 | 1.0021 | 0.4923 | 0.7345 | 0.2472 | 0.2961 | -0.086 ± 0.0197 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4323 | 0.1919 | 0.1923 | -0.0004 ± 0.0002 | 0.5594 | 0.5601 | 0.5073 | 0.4923 | 0.5135 | -0.035 ± 0.0069 | -0.0154 (26) |
| 3-5 | 2939 | 0.1927 | 0.1918 | +0.0009 ± 0.0006 | 0.5612 | 0.5582 | 0.51 | 0.4703 | 0.4781 | -0.044 ± 0.0083 | 0.01 (2) |
| 5-10 | 6439 | 0.1979 | 0.1942 | +0.0037 ± 0.0008 | 0.5804 | 0.5672 | 0.5071 | 0.4331 | 0.4479 | -0.043 ± 0.0056 | -0.0117 (6) |
| 10-15 | 5371 | 0.203 | 0.192 | +0.0110 ± 0.0015 | 0.5956 | 0.5616 | 0.5127 | 0.3889 | 0.4074 | -0.048 ± 0.0061 | -0.0189 (18) |
| 15-25 | 7483 | 0.2177 | 0.1812 | +0.0365 ± 0.0019 | 0.6324 | 0.5313 | 0.5238 | 0.3286 | 0.336 | -0.063 ± 0.005 | -0.0084 (43) |
| 25-40 | 6812 | 0.2517 | 0.1381 | +0.1136 ± 0.0029 | 0.7095 | 0.4217 | 0.5603 | 0.2436 | 0.2259 | -0.083 ± 0.0045 | -0.0095 (20) |
| 40+ | 5311 | 0.4013 | 0.0598 | +0.3415 ± 0.0039 | 1.0578 | 0.215 | 0.6549 | 0.1196 | 0.0823 | -0.074 ± 0.0033 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 908 | 0.1963 | 0.1979 | -0.0017 ± 0.0005 | 0.5719 | 0.5762 | 0.5014 | 0.486 | 0.5363 | -0.049 ± 0.0154 | -0.012 (10) |
| 3-5 | 636 | 0.2081 | 0.2066 | +0.0016 ± 0.0015 | 0.6011 | 0.5952 | 0.4967 | 0.4571 | 0.4591 | -0.116 ± 0.0188 | -0.0 (4) |
| 5-10 | 1412 | 0.2025 | 0.1991 | +0.0034 ± 0.0018 | 0.5902 | 0.5803 | 0.5118 | 0.438 | 0.4504 | -0.107 ± 0.0123 | -0.01 (9) |
| 10-15 | 1125 | 0.211 | 0.2044 | +0.0067 ± 0.0033 | 0.6125 | 0.5922 | 0.5398 | 0.4166 | 0.4524 | -0.103 ± 0.0135 | -0.0286 (7) |
| 15-25 | 1354 | 0.2315 | 0.2133 | +0.0182 ± 0.0049 | 0.6606 | 0.6106 | 0.589 | 0.3943 | 0.4446 | -0.114 ± 0.0125 | -0.03 (1) |
| 25-40 | 824 | 0.2116 | 0.2108 | +0.0008 ± 0.0094 | 0.6108 | 0.605 | 0.6634 | 0.3524 | 0.5049 | -0.058 ± 0.0144 | -0.0267 (3) |
| 40+ | 184 | 0.3097 | 0.1845 | +0.1252 ± 0.0284 | 0.8397 | 0.5449 | 0.746 | 0.2915 | 0.3913 | -0.092 ± 0.0292 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4819 | 0.1837 | 0.1844 | -0.0007 ± 0.0002 | 0.5412 | 0.5423 | 0.482 | 0.4666 | 0.4877 | -0.030 ± 0.0063 | -0.0137 (41) |
| 3-5 | 3415 | 0.204 | 0.2023 | +0.0017 ± 0.0006 | 0.5917 | 0.5856 | 0.4807 | 0.4412 | 0.4404 | -0.056 ± 0.0078 | -0.01 (19) |
| 5-10 | 7418 | 0.1959 | 0.1911 | +0.0048 ± 0.0008 | 0.5749 | 0.5596 | 0.4875 | 0.4135 | 0.4179 | -0.054 ± 0.0051 | -0.0105 (37) |
| 10-15 | 5899 | 0.1935 | 0.1794 | +0.0141 ± 0.0014 | 0.5715 | 0.5306 | 0.4951 | 0.3718 | 0.3757 | -0.059 ± 0.0055 | -0.0146 (13) |
| 15-25 | 7589 | 0.2123 | 0.1727 | +0.0396 ± 0.0019 | 0.619 | 0.5091 | 0.5142 | 0.3196 | 0.3162 | -0.072 ± 0.0048 | -0.0533 (3) |
| 25-40 | 5764 | 0.2169 | 0.1279 | +0.0890 ± 0.003 | 0.6267 | 0.3917 | 0.5301 | 0.2146 | 0.2335 | -0.050 ± 0.0045 | -0.02 (4) |
| 40+ | 3774 | 0.393 | 0.0509 | +0.3421 ± 0.0041 | 1.0245 | 0.1891 | 0.6422 | 0.1108 | 0.0678 | -0.077 ± 0.0035 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1331 | 0.196 | 0.196 | +0.0000 ± 0.0004 | 0.5699 | 0.5697 | 0.5059 | 0.491 | 0.4921 | -0.072 ± 0.0124 | -0.0213 (54) |
| 3-5 | 937 | 0.1894 | 0.1891 | +0.0003 ± 0.0011 | 0.5563 | 0.5543 | 0.4951 | 0.4552 | 0.4696 | -0.061 ± 0.0145 | -0.0194 (34) |
| 5-10 | 1920 | 0.2008 | 0.1959 | +0.0049 ± 0.0015 | 0.59 | 0.5746 | 0.5057 | 0.4321 | 0.4359 | -0.078 ± 0.0103 | -0.005 (78) |
| 10-15 | 1320 | 0.2164 | 0.2032 | +0.0132 ± 0.0031 | 0.6258 | 0.5903 | 0.5395 | 0.4166 | 0.4227 | -0.093 ± 0.0128 | 0.0014 (65) |
| 15-25 | 1694 | 0.2303 | 0.2075 | +0.0228 ± 0.0044 | 0.6574 | 0.599 | 0.5883 | 0.3934 | 0.4357 | -0.089 ± 0.0112 | -0.0214 (59) |
| 25-40 | 1052 | 0.2417 | 0.2098 | +0.0318 ± 0.0086 | 0.6903 | 0.6023 | 0.687 | 0.3748 | 0.48 | -0.091 ± 0.0132 | -0.0252 (27) |
| 40+ | 367 | 0.3254 | 0.2026 | +0.1228 ± 0.0225 | 0.9414 | 0.5896 | 0.8171 | 0.34 | 0.4659 | -0.095 ± 0.0209 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4919 | 0.1759 | 0.1761 | -0.0002 ± 0.0002 | 0.5208 | 0.5208 | 0.5114 | 0.4962 | 0.5064 | -0.039 ± 0.006 | -0.0145 (98) |
| 3-5 | 3366 | 0.1945 | 0.1935 | +0.0010 ± 0.0006 | 0.567 | 0.5646 | 0.5011 | 0.4613 | 0.4685 | -0.044 ± 0.0077 | -0.0204 (72) |
| 5-10 | 6856 | 0.1976 | 0.191 | +0.0067 ± 0.0008 | 0.5814 | 0.5621 | 0.5004 | 0.4267 | 0.4198 | -0.064 ± 0.0053 | -0.0084 (134) |
| 10-15 | 4728 | 0.2105 | 0.1944 | +0.0161 ± 0.0016 | 0.6116 | 0.5698 | 0.5371 | 0.4141 | 0.4088 | -0.072 ± 0.0065 | -0.0053 (106) |
| 15-25 | 5688 | 0.2299 | 0.1996 | +0.0304 ± 0.0023 | 0.6612 | 0.5783 | 0.574 | 0.3786 | 0.4001 | -0.066 ± 0.006 | -0.026 (108) |
| 25-40 | 3821 | 0.2581 | 0.1892 | +0.0689 ± 0.0044 | 0.7304 | 0.5515 | 0.6383 | 0.3257 | 0.3742 | -0.071 ± 0.0069 | -0.0246 (52) |
| 40+ | 1662 | 0.3713 | 0.1572 | +0.2141 ± 0.0101 | 1.0495 | 0.4687 | 0.7435 | 0.2423 | 0.29 | -0.067 ± 0.0092 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 6443 | 1.027 ± 0.035 | 1.106 | 0.1691 | 0.1669 | 0.2148 | 0.2046 |
| gen2 | 6443 | 0.816 ± 0.032 | 1.074 | 0.1728 | 0.1673 | 0.2339 | 0.2044 |
| gen1_elo | 6443 | 1.004 ± 0.034 | 1.097 | 0.1758 | 0.167 | 0.214 | 0.2046 |
| gen1_sr | 6443 | 1.003 ± 0.041 | 1.132 | 0.1329 | 0.169 | 0.2298 | 0.2041 |
| gen1_ledger | 8621 | 0.865 ± 0.025 | 1.071 | 0.189 | 0.1756 | 0.2173 | 0.2006 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 30,953)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 7,127 | 23.0% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,827 | 22.1% |
| BOOK_QUALITY | execution | 5,741 | 18.6% |
| POOR_DATA | data | 3,606 | 11.7% |
| LIMITED_DATA | data | 1,935 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,744 | 5.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,304 | 4.2% |
| IDENTITY_AMBIGUOUS | mapping | 1,274 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 875 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 519 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 23.0%, coverage 22.1%, execution 18.6%, data 17.9%, market_freshness/coverage 8.5%, model_calibration_or_unknown 4.2%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.3%, LOW_DATA_QUALITY 71.6%, THIN_PLAYER_HISTORY 60.0%, STALE_PLAYER_DATA 52.1%, STALE_KALSHI_QUOTE 45.2%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 33.0%, WIDE_SPREAD 24.8%, MODEL_HIGH_UNCERTAINTY 18.5%, PLAYER_IDENTITY_RISK 15.5%, LEVEL_TRANSFER_RISK 10.2%, LOW_DISPLAYED_LIQUIDITY 8.3%, EVENT_MAPPING_RISK 7.4%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.5%, POST_SETTLEMENT_OBSERVATION 22.1%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 16,475)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,506 | 33.4% |
| STALE_QUOTE | market_freshness | 3,223 | 19.6% |
| BOOK_QUALITY | execution | 2,987 | 18.1% |
| POOR_DATA | data | 1,553 | 9.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 921 | 5.6% |
| IDENTITY_AMBIGUOUS | mapping | 698 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 572 | 3.5% |
| LIMITED_DATA | data | 567 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 319 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 128 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.4%, market_freshness 19.6%, execution 18.1%, data 12.9%, market_freshness/coverage 9.1%, mapping 4.2%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 96.9%, LOW_DATA_QUALITY 75.1%, THIN_PLAYER_HISTORY 62.2%, STALE_KALSHI_QUOTE 52.7%, STALE_PLAYER_DATA 46.2%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 34.2%, WIDE_SPREAD 24.3%, MODEL_HIGH_UNCERTAINTY 19.1%, PLAYER_IDENTITY_RISK 18.5%, LEVEL_TRANSFER_RISK 9.1%, EVENT_MAPPING_RISK 9.0%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 5.0%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.4%, POST_SETTLEMENT_OBSERVATION 33.4%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 13100, "IDENTITY_AMBIGUOUS": 3375}; ticker orientation: {"VERIFIED": 16475}.

Checks: discipline:AMBIGUOUS 1111, discipline:PASS 15364, identity_confidence:AMBIGUOUS 3051, identity_confidence:PASS 13424, level_mapping:NA 1123, level_mapping:PASS 15352, market_pair:AMBIGUOUS 484, market_pair:NA 364, market_pair:PASS 15627, model_complement:NA 327, model_complement:PASS 16148, namesake:AMBIGUOUS 6, namesake:PASS 16469, physical_match_id:NA 5687, physical_match_id:PASS 10788, player_ids:PASS 16475, same_pair_other_event:PASS 16475, ticker_orientation:PASS 16475

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,125 | 3.9% | 3.3% | 1.4% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 21, "market_freshness/coverage": 17} | 5.6 | 0.2227 / 0.2169 (751) | 24.3% | 2.6% | 3.1% | 2.8% |
| CHALLENGER | 10,958 | 16.3% | 6.3% | 10.8% | {"coverage": 1041, "market_freshness/coverage": 213, "market_freshness": 209, "data": 155, "model_calibration_or_unknown": 76, "execution": 41, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.38 | 0.2208 / 0.2101 (2562) | 37.2% | 15.9% | 4.2% | 22.2% |
| DOUBLES | 2,345 | 47.4% | 47.3% | 6.7% | {"execution": 637, "mapping": 300, "market_freshness": 106, "market_freshness/coverage": 61, "coverage": 7} | 23.73 | 0.304 / 0.2381 (555) | 10.0% | 0.0% | 100.0% | 6.0% |
| ITF_MEN | 21,255 | 25.1% | 17.8% | 32.4% | {"coverage": 1825, "market_freshness": 1036, "execution": 954, "data": 797, "market_freshness/coverage": 514, "mapping": 198, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.81 | 0.2173 / 0.1994 (4405) | 38.8% | 69.2% | 16.0% | 21.1% |
| ITF_WOMEN | 28,121 | 26.5% | 19.1% | 45.2% | {"coverage": 2560, "market_freshness": 1623, "execution": 1272, "data": 1069, "market_freshness/coverage": 632, "mapping": 177, "model_calibration_or_unknown": 85, "model_calibration": 22} | 12.55 | 0.2027 / 0.1941 (5288) | 40.2% | 57.4% | 9.8% | 21.1% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,607 | 6.1% | 5.2% | 1.7% | {"market_freshness": 105, "model_calibration_or_unknown": 50, "coverage": 37, "execution": 29, "data": 24, "model_calibration": 20, "market_freshness/coverage": 13, "mapping": 1} | 7.7 | 0.2298 / 0.2234 (735) | 29.3% | 2.0% | 1.4% | 3.6% |
| WTA125 | 2,484 | 11.1% | 9.5% | 1.7% | {"market_freshness": 85, "model_calibration_or_unknown": 51, "market_freshness/coverage": 42, "data": 39, "execution": 24, "model_calibration": 17, "coverage": 14, "mapping": 4} | 9.21 | 0.208 / 0.1906 (726) | 28.5% | 10.9% | 4.3% | 7.2% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.4h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 509 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 3 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 4 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 5 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 311 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 6 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 7 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 8 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 9 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 10 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 194 min (STALE); no external reference |
| 13 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 14 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 17 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 18 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 19 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 20 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 21 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 22 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 23 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 24 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 25 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 26 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 27 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 28 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 29 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 30 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 31 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 365 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 32 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 33 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 34 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 35 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 36 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 37 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 38 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 39 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 768 min (STALE); no external reference |
| 40 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 41 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 42 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 43 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 44 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 720 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 45 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 46 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 252 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |
| 47 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXATPCHALLENGERMATCH-26NOV02TOBSTO-TOB` | CHALLENGER | fair_v1 | 80% / 2% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 165 min (STALE); data POOR (grade F, thinner serve sample 159.0, ratio 20.58); no external reference |
| 49 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 50 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9686, "by_level_share_of_ge_25pp": {"ATP": 0.0144, "CHALLENGER": 0.1085, "DOUBLES": 0.0674, "ITF_MEN": 0.3236, "ITF_WOMEN": 0.4516, "OTHER": 0.0007, "WTA": 0.0169, "WTA125": 0.0168}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5271, "share_primary_cause_market_settled_or_in_play": 0.4248, "share_primary_cause_stale_quote_only": 0.1956}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 16475, "identity_ambiguous_share": 0.2049, "ticker_orientation": {"VERIFIED": 16475}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 10788, "with_external": 569, "coverage": 0.0527, "external_status": {"EXTERNAL_STALE": 360, "AGREES_WITH_KALSHI": 196, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 360, "MODEL_LONE_OUTLIER": 196, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3445, "share_external_supports_model": 0.0228}, "pregame_clean_ge_25pp": {"n": 5200, "with_external": 540, "coverage": 0.1038, "external_status": {"EXTERNAL_STALE": 338, "AGREES_WITH_KALSHI": 189, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 338, "MODEL_LONE_OUTLIER": 189, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.35, "share_external_supports_model": 0.0241}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 476.0, "median_sample_ratio": 2.46, "median_min_matches": 19.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2084, "data_status": {"POOR": 9295, "LIMITED": 4277, "ADEQUATE": 2903}, "comparison_lt_10pp": {"median_thinner_serve_points": 1743.0, "median_sample_ratio": 1.69, "median_min_matches": 91.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1291, "model_minus_observed": 0.0577, "kalshi_minus_observed": -0.0821, "brier_diff_model_minus_kalshi": -0.0007}, "4-10x": {"n": 888, "model_minus_observed": 0.091, "kalshi_minus_observed": -0.0557, "brier_diff_model_minus_kalshi": 0.0092}, "<2x": {"n": 3181, "model_minus_observed": 0.0944, "kalshi_minus_observed": -0.028, "brier_diff_model_minus_kalshi": 0.013}, ">=10x": {"n": 1083, "model_minus_observed": 0.1198, "kalshi_minus_observed": -0.0542, "brier_diff_model_minus_kalshi": 0.0159}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 6443, "model": {"intercept": -0.546, "slope": 0.816, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.188, "slope": 1.074, "slope_se": 0.036}, "mean_extremity_model": 0.1728, "mean_extremity_kalshi": 0.1673, "model_brier": 0.2339, "kalshi_brier": 0.2044, "brier_diff_model_minus_kalshi": 0.0295, "brier_diff_se": 0.0024, "model_logloss": 0.665, "kalshi_logloss": 0.5913}, "fair_v1": {"n": 6443, "model": {"intercept": -0.435, "slope": 1.027, "slope_se": 0.035}, "kalshi_mid_same_rows": {"intercept": 0.264, "slope": 1.106, "slope_se": 0.036}, "mean_extremity_model": 0.1691, "mean_extremity_kalshi": 0.1669, "model_brier": 0.2148, "kalshi_brier": 0.2046, "brier_diff_model_minus_kalshi": 0.0102, "brier_diff_se": 0.0019, "model_logloss": 0.6184, "kalshi_logloss": 0.5916}, "gen1_elo": {"n": 6443, "model": {"intercept": -0.421, "slope": 1.004, "slope_se": 0.034}, "kalshi_mid_same_rows": {"intercept": 0.27, "slope": 1.097, "slope_se": 0.035}, "mean_extremity_model": 0.1758, "mean_extremity_kalshi": 0.167, "model_brier": 0.214, "kalshi_brier": 0.2046, "brier_diff_model_minus_kalshi": 0.0093, "brier_diff_se": 0.0019, "model_logloss": 0.6172, "kalshi_logloss": 0.5918}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2454, "share_ge_15": 0.4408, "median_abs_gap": 12.96, "n": 43961}, "gen1_elo": {"share_ge_25": 0.2429, "share_ge_15": 0.4379, "median_abs_gap": 12.73, "n": 43961}, "gen1_sr": {"share_ge_25": 0.3111, "share_ge_15": 0.5175, "median_abs_gap": 15.7, "n": 43961}, "gen2": {"share_ge_25": 0.3132, "share_ge_15": 0.5076, "median_abs_gap": 15.36, "n": 43961}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1519, "share_ge_15": 0.3541, "median_abs_gap": 10.71, "n": 34222}, "gen1_elo": {"share_ge_25": 0.1507, "share_ge_15": 0.3501, "median_abs_gap": 10.5, "n": 34222}, "gen1_sr": {"share_ge_25": 0.2172, "share_ge_15": 0.4391, "median_abs_gap": 12.98, "n": 34224}, "gen2": {"share_ge_25": 0.2326, "share_ge_15": 0.4387, "median_abs_gap": 12.84, "n": 34224}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.6, "share_ge_25_all": 0.0387, "share_ge_25_pregame_clean": 0.0334}, "WTA": {"median_abs_gap_pregame_clean": 7.7, "share_ge_25_all": 0.0606, "share_ge_25_pregame_clean": 0.0516}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2374, "share_within_10pp_all": 0.4392, "share_within_10pp_pregame_clean": 0.4907, "corr_model_vs_mid_pregame_clean": 0.8497}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 942, "model_brier": 0.1992, "kalshi_brier": 0.1997, "brier_diff_model_minus_kalshi": -0.0005}, "10-15": {"n_settled": 1121, "model_brier": 0.2208, "kalshi_brier": 0.2109, "brier_diff_model_minus_kalshi": 0.0098}, "15-25": {"n_settled": 1430, "model_brier": 0.2247, "kalshi_brier": 0.2089, "brier_diff_model_minus_kalshi": 0.0159}, "25-40": {"n_settled": 816, "model_brier": 0.2207, "kalshi_brier": 0.2064, "brier_diff_model_minus_kalshi": 0.0143}, "3-5": {"n_settled": 589, "model_brier": 0.2047, "kalshi_brier": 0.2041, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 175, "model_brier": 0.2937, "kalshi_brier": 0.1769, "brier_diff_model_minus_kalshi": 0.1168}, "5-10": {"n_settled": 1370, "model_brier": 0.2008, "kalshi_brier": 0.2008, "brier_diff_model_minus_kalshi": 0.0001}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.546, "slope": 0.816, "slope_se": 0.032}, "kalshi_slope": {"intercept": 0.188, "slope": 1.074, "slope_se": 0.036}, "n": 6443}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.49, "slope": 0.865, "slope_se": 0.025}, "kalshi_slope": {"intercept": 0.168, "slope": 1.071, "slope_se": 0.03}, "n": 8621}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 555, "model_brier": 0.304, "kalshi_brier": 0.2381, "brier_diff_model_minus_kalshi": 0.0659, "brier_diff_se": 0.0127, "corr_model_outcome": 0.0736, "corr_kalshi_outcome": 0.2361}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
