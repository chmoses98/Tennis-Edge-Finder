# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-24T17:02Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 51,822): 0-3 13.9%, 3-5 9.5%, 5-10 19.7%, 10-15 15.3%, 15-25 19.2%, 25-40 14.1%, 40+ 8.3%; median gap 12.12 pp.
* **Where the extremes live**: 96.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.8%, Challenger 11.9%, doubles 6.6%). Main tour: ATP 4.6% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 11,595): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.8%, STALE_QUOTE 18.8%, BOOK_QUALITY 17.9%, POOR_DATA 8.7%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.4%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.8%, market_freshness 18.8%, execution 17.9%, data 12.2%, market_freshness/coverage 9.0%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.6% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.8% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 11,595 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.1% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.1% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 494.0 points vs 1696.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.032, Gen-2 0.839, Gen-1 ledger 0.86 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 567 model 0.2232 vs Kalshi 0.2095; n 114 model 0.2782 vs Kalshi 0.1979.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 224,310 model-market comparisons (365,173 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 74,712 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-24T16:48:32.365170+00:00'], shadow board 60,020 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-24T16:48:36.163304+00:00'], Model 4 28,128 rows, 20,043 settled tickers, 7,036 tickers with an external scan.
* By model: {"gen1_ledger": 50756, "gen1_elo": 30184, "fair_v1": 30184, "gen2": 30184, "gen1_sr": 30184, "model4_fundamental": 26425, "model4_conditioned": 26393}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 51,822 | 13.9 | 9.5 | 19.7 | 15.3 | 19.2 | 14.1 | 8.3 | 12.12 | 41.6% | 22.4% |
| MW fair_v1 | 30,184 | 12.8 | 8.5 | 18.4 | 15.5 | 19.7 | 15.0 | 10.0 | 13.2 | 44.7% | 25.1% |
| MW gen1_elo | 30,184 | 12.7 | 8.5 | 18.9 | 15.2 | 19.9 | 15.0 | 9.7 | 13.02 | 44.6% | 24.8% |
| MW gen1_ledger | 21,638 | 15.5 | 10.8 | 21.5 | 15.0 | 18.6 | 12.8 | 5.8 | 10.55 | 37.2% | 18.6% |
| MW gen1_sr | 30,184 | 10.2 | 7.0 | 16.5 | 13.6 | 20.8 | 18.8 | 13.1 | 16.07 | 52.6% | 31.9% |
| MW gen2 | 30,184 | 10.9 | 7.3 | 16.2 | 14.0 | 19.4 | 18.0 | 14.2 | 15.67 | 51.6% | 32.2% |
| all families model4_conditioned | 26,393 | 21.9 | 18.9 | 34.8 | 17.5 | 4.3 | 1.5 | 1.0 | 5.96 | 6.9% | 2.5% |
| all families model4_fundamental | 26,425 | 16.8 | 13.3 | 34.2 | 20.4 | 10.6 | 3.4 | 1.3 | 7.75 | 15.3% | 4.7% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.9%, >=15pp 41.6%, >=20pp 31.0%, >=25pp 22.4%, >=30pp 16.2%, >=40pp 8.3%, >=50pp 3.9%
Executable gap (model outside the book, before fees): median 8.51pp; >=10pp 45.5%, >=25pp 17.5%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,636 | 28.2 | 14.2 | 24.8 | 15.4 | 11.9 | 4.7 | 0.8 | 6.17 | 17.3% | 5.4% |
| CHALLENGER | 4,664 | 15.8 | 10.0 | 20.4 | 15.4 | 14.8 | 12.5 | 11.2 | 11.08 | 38.4% | 23.6% |
| ITF_MEN | 8,359 | 10.1 | 7.3 | 16.8 | 14.6 | 21.6 | 17.4 | 12.2 | 15.43 | 51.2% | 29.6% |
| ITF_WOMEN | 11,975 | 9.4 | 6.9 | 15.9 | 15.3 | 22.2 | 18.2 | 12.0 | 15.79 | 52.5% | 30.2% |
| OTHER | 4 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 1,886 | 17.5 | 12.9 | 26.0 | 19.3 | 17.7 | 5.9 | 0.7 | 8.25 | 24.3% | 6.6% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,636 | 24.1 | 15.1 | 24.7 | 17.6 | 13.1 | 4.6 | 1.0 | 6.58 | 18.7% | 5.6% |
| CHALLENGER | 4,664 | 15.0 | 8.8 | 18.5 | 14.5 | 17.3 | 14.0 | 12.0 | 12.5 | 43.2% | 25.9% |
| ITF_MEN | 8,359 | 8.2 | 5.9 | 14.4 | 13.0 | 19.7 | 21.1 | 17.8 | 18.76 | 58.6% | 38.9% |
| ITF_WOMEN | 11,975 | 8.2 | 5.7 | 13.7 | 13.2 | 20.5 | 21.0 | 17.7 | 19.11 | 59.2% | 38.7% |
| OTHER | 4 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 1,886 | 13.9 | 10.2 | 22.2 | 16.3 | 22.6 | 13.4 | 1.3 | 10.96 | 37.3% | 14.7% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,636 | 23.8 | 12.7 | 23.7 | 16.5 | 15.1 | 7.0 | 1.2 | 7.49 | 23.2% | 8.2% |
| CHALLENGER | 4,664 | 14.3 | 9.2 | 20.4 | 15.5 | 16.2 | 13.1 | 11.3 | 11.49 | 40.6% | 24.4% |
| ITF_MEN | 8,359 | 9.7 | 7.3 | 16.9 | 13.8 | 22.2 | 17.8 | 12.3 | 15.82 | 52.3% | 30.1% |
| ITF_WOMEN | 11,975 | 9.4 | 6.6 | 16.3 | 15.8 | 22.7 | 18.1 | 11.2 | 15.6 | 51.9% | 29.3% |
| OTHER | 4 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 1,886 | 23.9 | 17.2 | 30.4 | 15.2 | 10.2 | 2.6 | 0.5 | 6.04 | 13.3% | 3.1% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,592 | 25.5 | 19.3 | 30.1 | 12.5 | 9.4 | 3.0 | 0.3 | 5.6 | 12.6% | 3.3% |
| CHALLENGER | 3,194 | 21.6 | 14.6 | 26.3 | 14.4 | 14.6 | 6.7 | 1.9 | 7.3 | 23.2% | 8.6% |
| DOUBLES | 1,633 | 5.3 | 4.7 | 11.6 | 10.3 | 21.1 | 26.0 | 20.9 | 23.73 | 68.0% | 46.9% |
| ITF_MEN | 6,172 | 13.7 | 9.0 | 20.0 | 16.1 | 21.2 | 13.3 | 6.5 | 12.16 | 41.0% | 19.8% |
| ITF_WOMEN | 7,092 | 12.6 | 9.0 | 19.2 | 15.2 | 21.6 | 16.3 | 6.1 | 12.84 | 44.0% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,074 | 22.4 | 15.8 | 29.9 | 17.9 | 10.0 | 3.6 | 0.4 | 6.92 | 14.0% | 4.0% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,564 | 28.5 | 14.4 | 25.2 | 15.3 | 11.7 | 4.3 | 0.5 | 6.0 | 16.5% | 4.8% |
| CHALLENGER | 3,278 | 20.7 | 12.4 | 25.2 | 17.8 | 15.1 | 6.8 | 1.9 | 8.31 | 23.8% | 8.7% |
| ITF_MEN | 6,119 | 12.2 | 8.8 | 20.3 | 16.5 | 22.8 | 14.3 | 5.1 | 12.54 | 42.2% | 19.4% |
| ITF_WOMEN | 8,938 | 11.2 | 8.2 | 18.1 | 17.4 | 24.2 | 15.3 | 5.5 | 13.51 | 45.1% | 20.9% |
| OTHER | 4 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 1,832 | 17.7 | 12.8 | 25.9 | 19.5 | 17.6 | 5.6 | 0.7 | 8.25 | 24.0% | 6.3% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,564 | 24.3 | 15.4 | 24.8 | 17.4 | 13.1 | 4.3 | 0.6 | 6.48 | 18.0% | 5.0% |
| CHALLENGER | 3,278 | 19.1 | 11.3 | 23.0 | 17.4 | 17.6 | 9.5 | 2.1 | 9.08 | 29.2% | 11.7% |
| ITF_MEN | 6,120 | 9.8 | 7.1 | 16.8 | 14.9 | 21.6 | 19.3 | 10.5 | 15.49 | 51.4% | 29.8% |
| ITF_WOMEN | 8,939 | 9.3 | 6.5 | 15.2 | 14.8 | 22.5 | 20.4 | 11.3 | 16.62 | 54.3% | 31.7% |
| OTHER | 4 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 1,832 | 14.0 | 10.3 | 22.2 | 16.3 | 22.6 | 13.2 | 1.4 | 10.96 | 37.2% | 14.6% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,543 | 25.7 | 19.6 | 30.1 | 12.7 | 8.9 | 2.8 | 0.2 | 5.53 | 11.9% | 3.0% |
| CHALLENGER | 2,782 | 23.1 | 15.7 | 27.8 | 14.3 | 14.0 | 4.6 | 0.5 | 6.71 | 19.1% | 5.1% |
| DOUBLES | 1,514 | 5.3 | 4.8 | 11.9 | 10.5 | 21.0 | 26.0 | 20.5 | 23.61 | 67.5% | 46.5% |
| ITF_MEN | 5,170 | 14.9 | 9.7 | 21.7 | 17.0 | 21.1 | 11.6 | 4.0 | 11.16 | 36.7% | 15.6% |
| ITF_WOMEN | 5,869 | 13.6 | 9.5 | 20.7 | 16.0 | 21.8 | 15.0 | 3.4 | 11.68 | 40.2% | 18.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,024 | 22.9 | 16.3 | 29.9 | 17.9 | 10.0 | 2.9 | 0.1 | 6.8 | 13.0% | 3.0% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,633 | 5.3 | 4.7 | 11.6 | 10.3 | 21.1 | 26.0 | 20.9 | 23.73 | 68.0% | 46.9% |
| singles | 20,005 | 16.3 | 11.3 | 22.3 | 15.4 | 18.4 | 11.7 | 4.6 | 10.02 | 34.7% | 16.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 3 | 33.3 | 33.3 | 0.0 | 0.0 | 33.3 | 0.0 | 0.0 | 4.01 | 33.3% | 0.0% |
| Clay | 6,666 | 13.0 | 9.0 | 19.2 | 15.6 | 18.7 | 14.6 | 10.0 | 12.83 | 43.2% | 24.5% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 18,677 | 13.3 | 8.5 | 18.5 | 15.2 | 19.7 | 14.9 | 9.8 | 13.1 | 44.5% | 24.8% |
| UNKNOWN | 4,601 | 10.7 | 7.5 | 17.1 | 16.8 | 20.6 | 16.3 | 11.0 | 14.12 | 47.9% | 27.3% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,539 | 19.5 | 11.9 | 21.4 | 16.4 | 15.1 | 9.3 | 6.4 | 9.15 | 30.7% | 15.7% |
| B | 3,747 | 12.5 | 8.7 | 19.7 | 16.1 | 19.2 | 12.7 | 11.1 | 12.62 | 43.0% | 23.8% |
| C | 4,231 | 11.4 | 8.7 | 19.8 | 15.2 | 19.4 | 14.8 | 10.8 | 13.2 | 44.9% | 25.5% |
| D | 4,697 | 12.1 | 7.7 | 17.4 | 15.4 | 21.4 | 15.8 | 10.2 | 13.98 | 47.4% | 26.0% |
| F | 8,970 | 7.6 | 5.5 | 15.1 | 14.5 | 23.5 | 21.3 | 12.6 | 17.82 | 57.3% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,141 | 23.2 | 15.8 | 28.8 | 15.1 | 11.6 | 4.0 | 1.4 | 6.65 | 17.2% | 5.5% |
| B | 2,949 | 16.2 | 10.4 | 23.1 | 16.2 | 19.4 | 10.7 | 3.9 | 10.05 | 34.1% | 14.6% |
| C | 4,248 | 11.2 | 7.5 | 18.1 | 14.3 | 21.5 | 16.8 | 10.6 | 14.39 | 48.9% | 27.3% |
| D | 3,010 | 14.3 | 9.8 | 19.9 | 14.5 | 21.0 | 14.5 | 6.1 | 12.05 | 41.5% | 20.6% |
| F | 5,290 | 10.3 | 8.4 | 15.6 | 15.1 | 22.6 | 19.9 | 8.1 | 15.29 | 50.6% | 27.9% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 9,810 | 17.8 | 10.7 | 20.7 | 16.2 | 15.6 | 10.1 | 8.9 | 10.23 | 34.7% | 19.1% |
| LIMITED | 6,369 | 13.2 | 10.0 | 20.4 | 15.7 | 19.3 | 13.5 | 7.9 | 11.98 | 40.7% | 21.4% |
| POOR | 14,005 | 9.1 | 6.3 | 16.0 | 14.9 | 22.7 | 19.2 | 11.8 | 16.26 | 53.6% | 30.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,996 | 25.9 | 19.7 | 33.8 | 12.7 | 5.5 | 2.1 | 0.2 | 5.46 | 7.8% | 2.4% |
| GAME_SPREAD | 4,815 | 22.2 | 15.3 | 33.5 | 17.3 | 9.2 | 2.3 | 0.3 | 6.73 | 11.8% | 2.6% |
| MATCH_WINNER | 21,638 | 15.5 | 10.8 | 21.5 | 15.0 | 18.6 | 12.8 | 5.8 | 10.55 | 37.2% | 18.6% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 10,660 | 28.9 | 17.1 | 30.9 | 12.5 | 8.1 | 2.1 | 0.4 | 5.48 | 10.5% | 2.5% |
| TOTAL_GAMES | 7,623 | 9.1 | 9.8 | 36.5 | 28.5 | 10.4 | 3.2 | 2.6 | 9.39 | 16.2% | 5.8% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,329 | 25.3 | 33.2 | 32.6 | 4.8 | 3.2 | 0.7 | 0.2 | 4.5 | 4.1% | 0.9% |
| GAME_SPREAD | 6,298 | 45.6 | 16.7 | 26.8 | 7.9 | 1.8 | 0.9 | 0.3 | 3.47 | 3.0% | 1.2% |
| TOTAL_GAMES | 10,766 | 5.1 | 7.9 | 41.3 | 34.2 | 6.9 | 2.5 | 2.1 | 9.54 | 11.5% | 4.6% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,337 | 24.2 | 17.5 | 35.5 | 12.7 | 7.1 | 2.6 | 0.4 | 5.88 | 10.1% | 2.9% |
| GAME_SPREAD | 6,301 | 19.5 | 13.4 | 27.9 | 20.7 | 13.2 | 4.3 | 0.9 | 7.96 | 18.5% | 5.2% |
| TOTAL_GAMES | 10,787 | 8.7 | 9.7 | 36.8 | 27.0 | 12.0 | 3.6 | 2.3 | 9.41 | 17.9% | 5.9% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 30,184 | 44.7% | 25.1% | 13.2 | 36.3% | 15.7% | 10.96 |
| gen1_elo | 30,184 | 44.6% | 24.8% | 13.02 | 36.0% | 15.8% | 10.77 |
| gen1_sr | 30,184 | 52.6% | 31.9% | 16.07 | 44.8% | 22.4% | 13.18 |
| gen2 | 30,184 | 51.6% | 32.2% | 15.67 | 44.7% | 24.0% | 13.11 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 15,236 | 15.7 | 10.4 | 21.3 | 17.2 | 20.1 | 12.0 | 3.3 | 10.75 | 35.5% | 15.3% |
| STALE | 14,948 | 9.9 | 6.6 | 15.6 | 13.8 | 19.2 | 18.1 | 16.9 | 17.02 | 54.2% | 35.0% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 15,106 | 16.5 | 11.3 | 22.2 | 15.1 | 17.8 | 12.2 | 4.8 | 9.99 | 34.8% | 17.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 51,822 | 15106 | 18708 | 18008 | 24.2 | 149.8 | 1400.4 |
| ge_15pp | 21,564 | 5260 | 6695 | 9609 | 26.6 | 443.4 | 1380.4 |
| ge_25pp | 11,595 | 2565 | 2927 | 6103 | 32.8 | 584.6 | 1380.4 |
| lt_10pp | 22,333 | 7563 | 8843 | 5927 | 22.4 | 47.9 | 1341.5 |

Current slate `SL-20261024T170224Z-e1975ed5`: 408 priced rows, quote age at build {'median': 14.3, 'max': 14.4}, freshness {'AGING': 408}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 24 | 0.0 | 0.0 | 25.0 | 4.2 | 37.5 | 33.3 | 0.0 | 20.48 | 70.8% | 33.3% |
| EXTERNAL_LONE_OUTLIER | 14 | 71.4 | 28.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.4 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,870 | 19.3 | 11.2 | 24.7 | 18.9 | 18.1 | 7.2 | 0.7 | 8.84 | 25.9% | 7.8% |
| KALSHI_LONE_OUTLIER | 18 | 5.6 | 5.6 | 72.2 | 5.6 | 5.6 | 5.6 | 0.0 | 6.16 | 11.1% | 5.6% |
| MARKETS_AGREE | 583 | 64.7 | 35.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,237 | 0.0 | 2.3 | 35.9 | 25.6 | 24.8 | 10.7 | 0.7 | 12.19 | 36.2% | 11.4% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 30,184 | 4746 (15.7%) | 26.1% | 0.9% | {"EXTERNAL_STALE": 2870, "AGREES_WITH_KALSHI": 1237, "ALL_AGREE": 583, "SUPPORTS_MODEL_DIRECTION": 23, "AGREES_WITH_MODEL": 18, "EXTERNAL_OUTLIER": 14, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 13,505 | 1210 (9.0%) | 37.0% | 1.6% | {"EXTERNAL_STALE": 743, "AGREES_WITH_KALSHI": 448, "SUPPORTS_MODEL_DIRECTION": 17, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 7,568 | 375 (5.0%) | 37.6% | 2.4% | {"EXTERNAL_STALE": 225, "AGREES_WITH_KALSHI": 141, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,670 | 352 (9.6%) | 38.1% | 2.6% | {"EXTERNAL_STALE": 209, "AGREES_WITH_KALSHI": 134, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 12,001 | 2676 (22.3%) | 17.7% | 0.8% | {"EXTERNAL_STALE": 1585, "ALL_AGREE": 583, "AGREES_WITH_KALSHI": 473, "AGREES_WITH_MODEL": 15, "EXTERNAL_OUTLIER": 14, "SUPPORTS_MODEL_DIRECTION": 5, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,759 | 10.3 | 7.5 | 19.4 | 14.3 | 22.2 | 16.1 | 10.2 | 14.26 | 48.5% | 26.3% |
| 4-10x | 3,947 | 10.9 | 8.2 | 19.2 | 15.3 | 21.3 | 14.9 | 10.1 | 13.76 | 46.4% | 25.1% |
| <2x | 15,278 | 14.9 | 9.7 | 19.0 | 16.4 | 17.5 | 13.1 | 9.3 | 11.89 | 39.9% | 22.4% |
| >=10x | 5,200 | 10.9 | 6.2 | 15.3 | 14.2 | 21.9 | 19.6 | 12.0 | 16.4 | 53.4% | 31.6% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 7,706 | 12.4 | 8.5 | 19.4 | 16.0 | 19.0 | 13.8 | 10.9 | 12.96 | 43.6% | 24.7% |
| 300-1000 | 6,443 | 11.6 | 8.6 | 17.3 | 15.3 | 20.5 | 16.3 | 10.3 | 13.96 | 47.2% | 26.7% |
| <300 | 9,890 | 8.6 | 5.6 | 15.5 | 14.7 | 23.1 | 20.1 | 12.4 | 17.02 | 55.6% | 32.5% |
| >=3000 | 6,145 | 21.4 | 13.0 | 23.1 | 16.4 | 14.2 | 7.1 | 4.8 | 7.96 | 26.1% | 11.9% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 862 | 0.5501 | 0.4117 | 0.5 | +0.050 | -0.088 | -0.0036 ± 0.0052 |
| ratio 4-10x | 591 | 0.588 | 0.4415 | 0.4941 | +0.094 | -0.053 | 0.0118 ± 0.0066 |
| ratio <2x | 2133 | 0.5384 | 0.4153 | 0.4454 | +0.093 | -0.030 | 0.0127 ± 0.0031 |
| ratio >=10x | 790 | 0.572 | 0.3965 | 0.4633 | +0.109 | -0.067 | 0.0076 ± 0.0065 |
| thinner_sample 1000-3000 | 1183 | 0.5428 | 0.4158 | 0.4455 | +0.097 | -0.030 | 0.0109 ± 0.0041 |
| thinner_sample 300-1000 | 996 | 0.567 | 0.4232 | 0.492 | +0.075 | -0.069 | 0.0009 ± 0.0051 |
| thinner_sample <300 | 1471 | 0.5611 | 0.3946 | 0.4643 | +0.097 | -0.070 | 0.0095 ± 0.0046 |
| thinner_sample >=3000 | 726 | 0.5366 | 0.4422 | 0.4669 | +0.070 | -0.025 | 0.0129 ± 0.0043 |
| data_status ADEQUATE | 1267 | 0.5391 | 0.4346 | 0.4515 | +0.088 | -0.017 | 0.0123 ± 0.0035 |
| data_status LIMITED | 1001 | 0.551 | 0.4169 | 0.4805 | +0.070 | -0.064 | 0.0044 ± 0.0048 |
| data_status POOR | 2108 | 0.5633 | 0.4018 | 0.4677 | +0.096 | -0.066 | 0.0081 ± 0.0038 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 639 | 0.2016 | 0.2025 | -0.0009 ± 0.0006 | 0.5839 | 0.5858 | 0.5035 | 0.4888 | 0.5243 | -0.071 ± 0.0188 | -0.01 (5) |
| 3-5 | 405 | 0.2033 | 0.2029 | +0.0003 ± 0.0018 | 0.5898 | 0.5874 | 0.5024 | 0.4623 | 0.4765 | -0.097 ± 0.0231 | 0.02 (1) |
| 5-10 | 905 | 0.2029 | 0.2022 | +0.0006 ± 0.0023 | 0.5925 | 0.5878 | 0.5118 | 0.4379 | 0.4663 | -0.091 ± 0.0155 | -0.0167 (6) |
| 10-15 | 756 | 0.2149 | 0.205 | +0.0099 ± 0.0041 | 0.6203 | 0.5917 | 0.5303 | 0.4062 | 0.4272 | -0.105 ± 0.0164 | -0.048 (5) |
| 15-25 | 990 | 0.2249 | 0.2122 | +0.0127 ± 0.0057 | 0.6445 | 0.608 | 0.5779 | 0.3822 | 0.4475 | -0.096 ± 0.0146 | -0.0033 (9) |
| 25-40 | 567 | 0.2232 | 0.2095 | +0.0137 ± 0.0115 | 0.6363 | 0.6023 | 0.6596 | 0.3495 | 0.4797 | -0.075 ± 0.0176 | -0.01 (1) |
| 40+ | 114 | 0.2782 | 0.1979 | +0.0803 ± 0.0361 | 0.7617 | 0.5807 | 0.7579 | 0.3106 | 0.4474 | -0.079 ± 0.0353 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3296 | 0.1847 | 0.1857 | -0.0010 ± 0.0003 | 0.545 | 0.546 | 0.4931 | 0.478 | 0.5121 | -0.021 ± 0.0076 | -0.0129 (17) |
| 3-5 | 2179 | 0.1991 | 0.198 | +0.0011 ± 0.0008 | 0.5793 | 0.5741 | 0.4852 | 0.4453 | 0.4502 | -0.052 ± 0.0097 | 0.0 (2) |
| 5-10 | 4747 | 0.1982 | 0.1949 | +0.0033 ± 0.001 | 0.5802 | 0.5691 | 0.4822 | 0.4084 | 0.4226 | -0.047 ± 0.0065 | -0.0119 (21) |
| 10-15 | 4016 | 0.1978 | 0.1797 | +0.0181 ± 0.0017 | 0.5813 | 0.5304 | 0.4869 | 0.3625 | 0.3513 | -0.074 ± 0.0067 | -0.0281 (16) |
| 15-25 | 5043 | 0.209 | 0.1696 | +0.0395 ± 0.0023 | 0.6119 | 0.5017 | 0.5062 | 0.3098 | 0.3083 | -0.075 ± 0.0058 | -0.0025 (44) |
| 25-40 | 3967 | 0.2226 | 0.1288 | +0.0938 ± 0.0036 | 0.6394 | 0.3944 | 0.5319 | 0.2185 | 0.2291 | -0.059 ± 0.0055 | -0.01 (1) |
| 40+ | 2585 | 0.3805 | 0.0455 | +0.3349 ± 0.0048 | 0.9911 | 0.1748 | 0.6332 | 0.1068 | 0.0646 | -0.077 ± 0.0039 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 500 | 0.2062 | 0.207 | -0.0008 ± 0.0007 | 0.5943 | 0.596 | 0.5077 | 0.4925 | 0.518 | -0.101 ± 0.0219 | -0.01 (3) |
| 3-5 | 364 | 0.2261 | 0.2234 | +0.0027 ± 0.002 | 0.6389 | 0.6332 | 0.5153 | 0.4754 | 0.456 | -0.129 ± 0.0264 | 0.02 (1) |
| 5-10 | 788 | 0.206 | 0.206 | -0.0000 ± 0.0024 | 0.5983 | 0.5975 | 0.5468 | 0.4719 | 0.5127 | -0.078 ± 0.0166 | -0.01 (4) |
| 10-15 | 721 | 0.2176 | 0.2094 | +0.0082 ± 0.0043 | 0.6248 | 0.6045 | 0.5661 | 0.4418 | 0.473 | -0.113 ± 0.0177 | -0.04 (5) |
| 15-25 | 1016 | 0.2302 | 0.2104 | +0.0198 ± 0.0057 | 0.6533 | 0.6035 | 0.588 | 0.3922 | 0.4439 | -0.102 ± 0.0147 | -0.0133 (9) |
| 25-40 | 713 | 0.2615 | 0.1974 | +0.0641 ± 0.0105 | 0.7297 | 0.5751 | 0.6531 | 0.3375 | 0.3955 | -0.113 ± 0.0163 | -0.0075 (4) |
| 40+ | 274 | 0.3572 | 0.1714 | +0.1858 ± 0.0247 | 0.9817 | 0.513 | 0.733 | 0.2492 | 0.3139 | -0.072 ± 0.0239 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2807 | 0.1936 | 0.1939 | -0.0003 ± 0.0003 | 0.5638 | 0.5644 | 0.511 | 0.4959 | 0.5123 | -0.042 ± 0.0086 | -0.0133 (15) |
| 3-5 | 1883 | 0.1999 | 0.199 | +0.0009 ± 0.0008 | 0.578 | 0.5755 | 0.515 | 0.4751 | 0.4833 | -0.045 ± 0.0105 | 0.02 (1) |
| 5-10 | 4183 | 0.1961 | 0.1942 | +0.0019 ± 0.001 | 0.5771 | 0.5679 | 0.5101 | 0.436 | 0.4631 | -0.033 ± 0.0069 | -0.0117 (6) |
| 10-15 | 3635 | 0.2017 | 0.1896 | +0.0122 ± 0.0018 | 0.5903 | 0.5524 | 0.5135 | 0.3896 | 0.4033 | -0.056 ± 0.0073 | -0.0189 (18) |
| 15-25 | 5011 | 0.2162 | 0.1782 | +0.0380 ± 0.0024 | 0.6279 | 0.524 | 0.5252 | 0.3292 | 0.3341 | -0.069 ± 0.006 | -0.0086 (42) |
| 25-40 | 4629 | 0.2513 | 0.1369 | +0.1144 ± 0.0035 | 0.707 | 0.4205 | 0.5578 | 0.2406 | 0.2214 | -0.085 ± 0.0054 | -0.0044 (18) |
| 40+ | 3685 | 0.3938 | 0.0606 | +0.3332 ± 0.0046 | 1.0364 | 0.2166 | 0.6506 | 0.1188 | 0.0844 | -0.072 ± 0.004 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 613 | 0.2 | 0.2021 | -0.0021 ± 0.0006 | 0.5807 | 0.5859 | 0.5015 | 0.4862 | 0.5465 | -0.034 ± 0.0188 | -0.0137 (8) |
| 3-5 | 433 | 0.2017 | 0.1997 | +0.0020 ± 0.0017 | 0.5863 | 0.5798 | 0.5072 | 0.4675 | 0.4642 | -0.121 ± 0.0223 | 0.0067 (3) |
| 5-10 | 921 | 0.2023 | 0.1987 | +0.0036 ± 0.0022 | 0.5911 | 0.5789 | 0.5076 | 0.4336 | 0.4441 | -0.104 ± 0.015 | -0.0071 (7) |
| 10-15 | 760 | 0.2089 | 0.2058 | +0.0032 ± 0.0041 | 0.607 | 0.5939 | 0.54 | 0.4165 | 0.4671 | -0.083 ± 0.0163 | -0.0317 (6) |
| 15-25 | 938 | 0.2311 | 0.2121 | +0.0190 ± 0.0059 | 0.6602 | 0.6073 | 0.5889 | 0.3945 | 0.4424 | -0.111 ± 0.015 | -0.03 (1) |
| 25-40 | 591 | 0.2138 | 0.2175 | -0.0037 ± 0.0112 | 0.6172 | 0.6208 | 0.6704 | 0.3592 | 0.5178 | -0.055 ± 0.0173 | 0.015 (2) |
| 40+ | 120 | 0.2938 | 0.2096 | +0.0842 ± 0.0365 | 0.8102 | 0.6066 | 0.7684 | 0.3189 | 0.4583 | -0.076 ± 0.0382 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3229 | 0.1849 | 0.1854 | -0.0005 ± 0.0003 | 0.5443 | 0.5451 | 0.4897 | 0.4745 | 0.4878 | -0.039 ± 0.0076 | -0.0163 (35) |
| 3-5 | 2188 | 0.1945 | 0.1924 | +0.0021 ± 0.0008 | 0.5715 | 0.5646 | 0.4872 | 0.4476 | 0.441 | -0.066 ± 0.0096 | -0.0094 (18) |
| 5-10 | 4792 | 0.1959 | 0.1901 | +0.0058 ± 0.0009 | 0.5757 | 0.5567 | 0.4831 | 0.4091 | 0.4071 | -0.061 ± 0.0063 | -0.01 (31) |
| 10-15 | 3914 | 0.1921 | 0.1767 | +0.0154 ± 0.0017 | 0.5679 | 0.5222 | 0.4999 | 0.3765 | 0.3753 | -0.065 ± 0.0067 | -0.015 (12) |
| 15-25 | 5223 | 0.2111 | 0.172 | +0.0391 ± 0.0022 | 0.6167 | 0.5075 | 0.5152 | 0.3202 | 0.3178 | -0.074 ± 0.0057 | -0.03 (2) |
| 25-40 | 3982 | 0.2194 | 0.1329 | +0.0865 ± 0.0036 | 0.633 | 0.4033 | 0.5379 | 0.2217 | 0.2449 | -0.050 ± 0.0055 | 0.01 (3) |
| 40+ | 2505 | 0.3952 | 0.0501 | +0.3451 ± 0.0051 | 1.0327 | 0.1868 | 0.6454 | 0.1132 | 0.0691 | -0.081 ± 0.0043 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1001 | 0.1951 | 0.1953 | -0.0002 ± 0.0005 | 0.5696 | 0.5696 | 0.5032 | 0.4881 | 0.4955 | -0.057 ± 0.0142 | -0.0224 (49) |
| 3-5 | 696 | 0.1921 | 0.1915 | +0.0006 ± 0.0013 | 0.5614 | 0.5587 | 0.4901 | 0.4502 | 0.4598 | -0.059 ± 0.017 | -0.0194 (34) |
| 5-10 | 1446 | 0.2021 | 0.1959 | +0.0062 ± 0.0018 | 0.5936 | 0.5744 | 0.4966 | 0.4233 | 0.4184 | -0.075 ± 0.0118 | -0.005 (78) |
| 10-15 | 965 | 0.2112 | 0.1989 | +0.0122 ± 0.0036 | 0.6118 | 0.58 | 0.5229 | 0.3998 | 0.4093 | -0.072 ± 0.0147 | 0.0014 (64) |
| 15-25 | 1293 | 0.2317 | 0.2101 | +0.0217 ± 0.005 | 0.6619 | 0.6048 | 0.578 | 0.3832 | 0.4261 | -0.075 ± 0.0128 | -0.0214 (59) |
| 25-40 | 785 | 0.2477 | 0.2074 | +0.0404 ± 0.01 | 0.7039 | 0.5961 | 0.6734 | 0.3609 | 0.4522 | -0.086 ± 0.0152 | -0.0219 (26) |
| 40+ | 260 | 0.3514 | 0.1975 | +0.1539 ± 0.0272 | 1.0146 | 0.5768 | 0.8089 | 0.3265 | 0.4269 | -0.095 ± 0.0248 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3260 | 0.183 | 0.1833 | -0.0002 ± 0.0003 | 0.5393 | 0.539 | 0.505 | 0.4896 | 0.5015 | -0.037 ± 0.0075 | -0.0157 (88) |
| 3-5 | 2266 | 0.1944 | 0.1926 | +0.0018 ± 0.0007 | 0.5674 | 0.5634 | 0.4962 | 0.4564 | 0.4537 | -0.053 ± 0.0094 | -0.0209 (69) |
| 5-10 | 4507 | 0.1973 | 0.1888 | +0.0085 ± 0.001 | 0.5804 | 0.5556 | 0.4914 | 0.4179 | 0.4 | -0.072 ± 0.0065 | -0.0082 (132) |
| 10-15 | 3162 | 0.2071 | 0.1908 | +0.0163 ± 0.0019 | 0.6029 | 0.5601 | 0.5296 | 0.4064 | 0.401 | -0.068 ± 0.0078 | -0.0053 (105) |
| 15-25 | 3925 | 0.2301 | 0.1993 | +0.0308 ± 0.0028 | 0.6637 | 0.5779 | 0.5698 | 0.3743 | 0.3944 | -0.068 ± 0.0072 | -0.0253 (107) |
| 25-40 | 2710 | 0.2587 | 0.1841 | +0.0746 ± 0.0052 | 0.7333 | 0.5373 | 0.6327 | 0.3188 | 0.3594 | -0.077 ± 0.008 | -0.0229 (51) |
| 40+ | 1200 | 0.378 | 0.1445 | +0.2334 ± 0.0115 | 1.0706 | 0.4354 | 0.73 | 0.2264 | 0.2592 | -0.071 ± 0.0103 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4376 | 1.032 ± 0.042 | 1.127 | 0.1687 | 0.1638 | 0.2144 | 0.2059 |
| gen2 | 4376 | 0.839 ± 0.04 | 1.093 | 0.1683 | 0.1644 | 0.2337 | 0.2056 |
| gen1_elo | 4376 | 1.006 ± 0.041 | 1.119 | 0.1756 | 0.1639 | 0.2133 | 0.2062 |
| gen1_sr | 4376 | 1.023 ± 0.051 | 1.168 | 0.1294 | 0.1663 | 0.2299 | 0.2052 |
| gen1_ledger | 6446 | 0.86 ± 0.03 | 1.07 | 0.1837 | 0.1782 | 0.2188 | 0.2001 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 21,564)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,001 | 23.2% |
| STALE_QUOTE | market_freshness | 4,698 | 21.8% |
| BOOK_QUALITY | execution | 4,001 | 18.6% |
| POOR_DATA | data | 2,431 | 11.3% |
| LIMITED_DATA | data | 1,323 | 6.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,178 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,014 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 907 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 646 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 364 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 23.2%, market_freshness 21.8%, execution 18.6%, data 17.4%, market_freshness/coverage 8.5%, model_calibration_or_unknown 4.7%, mapping 4.2%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.6%, START_UNVERIFIABLE 94.1%, LOW_DATA_QUALITY 70.8%, THIN_PLAYER_HISTORY 59.8%, STALE_PLAYER_DATA 49.3%, STALE_KALSHI_QUOTE 44.6%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 33.5%, WIDE_SPREAD 24.6%, MODEL_HIGH_UNCERTAINTY 18.0%, PLAYER_IDENTITY_RISK 16.4%, LEVEL_TRANSFER_RISK 11.1%, EVENT_MAPPING_RISK 8.0%, LOW_DISPLAYED_LIQUIDITY 8.0%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.2%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.8%, POST_SETTLEMENT_OBSERVATION 23.2%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 11,595)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,035 | 34.8% |
| STALE_QUOTE | market_freshness | 2,179 | 18.8% |
| BOOK_QUALITY | execution | 2,078 | 17.9% |
| POOR_DATA | data | 1,008 | 8.7% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 631 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 514 | 4.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 411 | 3.5% |
| LIMITED_DATA | data | 402 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 255 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 81 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.8%, market_freshness 18.8%, execution 17.9%, data 12.2%, market_freshness/coverage 9.0%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 96.9%, LOW_DATA_QUALITY 74.1%, THIN_PLAYER_HISTORY 61.9%, STALE_KALSHI_QUOTE 52.6%, STALE_PLAYER_DATA 43.9%, MODEL_INTERNAL_DISAGREEMENT 42.8%, ASYMMETRIC_SAMPLE_SIZE 34.7%, WIDE_SPREAD 23.7%, PLAYER_IDENTITY_RISK 19.7%, MODEL_HIGH_UNCERTAINTY 18.4%, LEVEL_TRANSFER_RISK 9.7%, EVENT_MAPPING_RISK 9.5%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.9%, POST_SETTLEMENT_OBSERVATION 34.8%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 9027, "IDENTITY_AMBIGUOUS": 2568}; ticker orientation: {"VERIFIED": 11595}.

Checks: discipline:AMBIGUOUS 766, discipline:PASS 10829, identity_confidence:AMBIGUOUS 2282, identity_confidence:PASS 9313, level_mapping:NA 778, level_mapping:PASS 10817, market_pair:AMBIGUOUS 403, market_pair:NA 293, market_pair:PASS 10899, model_complement:NA 260, model_complement:PASS 11335, namesake:AMBIGUOUS 6, namesake:PASS 11589, physical_match_id:NA 4027, physical_match_id:PASS 7568, player_ids:PASS 11595, same_pair_other_event:PASS 11595, ticker_orientation:PASS 11595

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,228 | 4.6% | 4.1% | 1.7% | {"market_freshness": 55, "model_calibration_or_unknown": 43, "data": 35, "execution": 23, "market_freshness/coverage": 14, "model_calibration": 13, "coverage": 12} | 5.88 | 0.2207 / 0.2159 (505) | 19.0% | 3.7% | 3.3% | 2.9% |
| CHALLENGER | 7,858 | 17.5% | 7.0% | 11.9% | {"coverage": 781, "market_freshness/coverage": 168, "market_freshness": 150, "data": 138, "model_calibration_or_unknown": 64, "execution": 31, "model_calibration": 28, "mapping": 15, "possible_market_error": 1} | 7.42 | 0.22 / 0.2085 (1890) | 35.1% | 17.7% | 3.8% | 22.9% |
| DOUBLES | 1,633 | 46.9% | 46.5% | 6.6% | {"execution": 398, "mapping": 200, "market_freshness": 106, "market_freshness/coverage": 55, "coverage": 7} | 23.61 | 0.3106 / 0.2358 (430) | 14.3% | 0.0% | 100.0% | 7.3% |
| ITF_MEN | 14,531 | 25.4% | 17.6% | 31.9% | {"coverage": 1385, "execution": 699, "market_freshness": 630, "data": 487, "market_freshness/coverage": 320, "mapping": 173, "model_calibration_or_unknown": 2, "model_calibration": 2} | 11.9 | 0.2155 / 0.1974 (3272) | 37.6% | 70.0% | 19.9% | 22.3% |
| ITF_WOMEN | 19,067 | 27.3% | 19.9% | 44.9% | {"coverage": 1826, "market_freshness": 1141, "execution": 887, "data": 716, "market_freshness/coverage": 436, "mapping": 120, "model_calibration_or_unknown": 69, "model_calibration": 11} | 12.84 | 0.2036 / 0.1944 (3700) | 40.1% | 55.9% | 9.9% | 22.3% |
| OTHER | 153 | 7.8% | 7.1% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.68 | 0.1411 / 0.1522 (42) | 30.1% | 6.5% | 5.2% | 7.8% |
| WTA | 2,960 | 5.7% | 5.1% | 1.5% | {"market_freshness": 57, "model_calibration_or_unknown": 36, "execution": 26, "model_calibration": 16, "data": 11, "coverage": 11, "market_freshness/coverage": 10, "mapping": 1} | 7.69 | 0.2353 / 0.2301 (495) | 25.0% | 1.4% | 1.7% | 3.5% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.5% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 769 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 17.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1037 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 15 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 16 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 17 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 18 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 19 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 20 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 21 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 22 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 23 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 24 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 25 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 26 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 27 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 28 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 29 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 30 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 31 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 32 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 33 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 34 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 35 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 36 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 37 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 39 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 321 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 41 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 42 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 43 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 44 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 46 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 752 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 47 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 48 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 49 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 765 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 50 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9687, "by_level_share_of_ge_25pp": {"ATP": 0.0168, "CHALLENGER": 0.1187, "DOUBLES": 0.0661, "ITF_MEN": 0.3189, "ITF_WOMEN": 0.449, "OTHER": 0.001, "WTA": 0.0145, "WTA125": 0.015}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5263, "share_primary_cause_market_settled_or_in_play": 0.4378, "share_primary_cause_stale_quote_only": 0.1879}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 11595, "identity_ambiguous_share": 0.2215, "ticker_orientation": {"VERIFIED": 11595}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 7568, "with_external": 375, "coverage": 0.0496, "external_status": {"EXTERNAL_STALE": 225, "AGREES_WITH_KALSHI": 141, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 225, "MODEL_LONE_OUTLIER": 141, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.376, "share_external_supports_model": 0.024}, "pregame_clean_ge_25pp": {"n": 3670, "with_external": 352, "coverage": 0.0959, "external_status": {"EXTERNAL_STALE": 209, "AGREES_WITH_KALSHI": 134, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 209, "MODEL_LONE_OUTLIER": 134, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3807, "share_external_supports_model": 0.0256}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 494.0, "median_sample_ratio": 2.43, "median_min_matches": 21.0, "median_max_days_since_last": 225.0, "share_severe_asymmetry": 0.2147, "data_status": {"POOR": 6453, "LIMITED": 3023, "ADEQUATE": 2119}, "comparison_lt_10pp": {"median_thinner_serve_points": 1696.0, "median_sample_ratio": 1.7, "median_min_matches": 95.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 862, "model_minus_observed": 0.0501, "kalshi_minus_observed": -0.0883, "brier_diff_model_minus_kalshi": -0.0036}, "4-10x": {"n": 591, "model_minus_observed": 0.0939, "kalshi_minus_observed": -0.0526, "brier_diff_model_minus_kalshi": 0.0118}, "<2x": {"n": 2133, "model_minus_observed": 0.093, "kalshi_minus_observed": -0.0301, "brier_diff_model_minus_kalshi": 0.0127}, ">=10x": {"n": 790, "model_minus_observed": 0.1087, "kalshi_minus_observed": -0.0668, "brier_diff_model_minus_kalshi": 0.0076}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4376, "model": {"intercept": -0.539, "slope": 0.839, "slope_se": 0.04}, "kalshi_mid_same_rows": {"intercept": 0.214, "slope": 1.093, "slope_se": 0.044}, "mean_extremity_model": 0.1683, "mean_extremity_kalshi": 0.1644, "model_brier": 0.2337, "kalshi_brier": 0.2056, "brier_diff_model_minus_kalshi": 0.0281, "brier_diff_se": 0.0029, "model_logloss": 0.6638, "kalshi_logloss": 0.5939}, "fair_v1": {"n": 4376, "model": {"intercept": -0.419, "slope": 1.032, "slope_se": 0.042}, "kalshi_mid_same_rows": {"intercept": 0.292, "slope": 1.127, "slope_se": 0.044}, "mean_extremity_model": 0.1687, "mean_extremity_kalshi": 0.1638, "model_brier": 0.2144, "kalshi_brier": 0.2059, "brier_diff_model_minus_kalshi": 0.0085, "brier_diff_se": 0.0024, "model_logloss": 0.6176, "kalshi_logloss": 0.5944}, "gen1_elo": {"n": 4376, "model": {"intercept": -0.398, "slope": 1.006, "slope_se": 0.041}, "kalshi_mid_same_rows": {"intercept": 0.308, "slope": 1.119, "slope_se": 0.044}, "mean_extremity_model": 0.1756, "mean_extremity_kalshi": 0.1639, "model_brier": 0.2133, "kalshi_brier": 0.2062, "brier_diff_model_minus_kalshi": 0.0071, "brier_diff_se": 0.0024, "model_logloss": 0.6163, "kalshi_logloss": 0.5951}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2507, "share_ge_15": 0.4474, "median_abs_gap": 13.2, "n": 30184}, "gen1_elo": {"share_ge_25": 0.2476, "share_ge_15": 0.4465, "median_abs_gap": 13.02, "n": 30184}, "gen1_sr": {"share_ge_25": 0.3185, "share_ge_15": 0.5265, "median_abs_gap": 16.07, "n": 30184}, "gen2": {"share_ge_25": 0.3217, "share_ge_15": 0.5156, "median_abs_gap": 15.67, "n": 30184}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.157, "share_ge_15": 0.3627, "median_abs_gap": 10.96, "n": 23369}, "gen1_elo": {"share_ge_25": 0.1575, "share_ge_15": 0.3604, "median_abs_gap": 10.77, "n": 23366}, "gen1_sr": {"share_ge_25": 0.2239, "share_ge_15": 0.448, "median_abs_gap": 13.18, "n": 23370}, "gen2": {"share_ge_25": 0.24, "share_ge_15": 0.4467, "median_abs_gap": 13.11, "n": 23371}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.88, "share_ge_25_all": 0.0461, "share_ge_25_pregame_clean": 0.0411}, "WTA": {"median_abs_gap_pregame_clean": 7.69, "share_ge_25_all": 0.0568, "share_ge_25_pregame_clean": 0.0515}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2339, "share_within_10pp_all": 0.431, "share_within_10pp_pregame_clean": 0.4845, "corr_model_vs_mid_pregame_clean": 0.8431}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 639, "model_brier": 0.2016, "kalshi_brier": 0.2025, "brier_diff_model_minus_kalshi": -0.0009}, "10-15": {"n_settled": 756, "model_brier": 0.2149, "kalshi_brier": 0.205, "brier_diff_model_minus_kalshi": 0.0099}, "15-25": {"n_settled": 990, "model_brier": 0.2249, "kalshi_brier": 0.2122, "brier_diff_model_minus_kalshi": 0.0127}, "25-40": {"n_settled": 567, "model_brier": 0.2232, "kalshi_brier": 0.2095, "brier_diff_model_minus_kalshi": 0.0137}, "3-5": {"n_settled": 405, "model_brier": 0.2033, "kalshi_brier": 0.2029, "brier_diff_model_minus_kalshi": 0.0003}, "40+": {"n_settled": 114, "model_brier": 0.2782, "kalshi_brier": 0.1979, "brier_diff_model_minus_kalshi": 0.0803}, "5-10": {"n_settled": 905, "model_brier": 0.2029, "kalshi_brier": 0.2022, "brier_diff_model_minus_kalshi": 0.0006}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.539, "slope": 0.839, "slope_se": 0.04}, "kalshi_slope": {"intercept": 0.214, "slope": 1.093, "slope_se": 0.044}, "n": 4376}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.51, "slope": 0.86, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.149, "slope": 1.07, "slope_se": 0.035}, "n": 6446}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 430, "model_brier": 0.3106, "kalshi_brier": 0.2358, "brier_diff_model_minus_kalshi": 0.0749, "brier_diff_se": 0.0146, "corr_model_outcome": 0.0433, "corr_kalshi_outcome": 0.2527}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
