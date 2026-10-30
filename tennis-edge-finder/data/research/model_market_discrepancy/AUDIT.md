# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-30T13:36Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 70,009): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 19.0%, 25-40 13.8%, 40+ 8.0%; median gap 11.86 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.9%, Challenger 10.8%, doubles 6.6%). Main tour: ATP 4.2% and WTA 5.6% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 15,278): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.0%, STALE_QUOTE 18.8%, BOOK_QUALITY 18.4%, POOR_DATA 9.4%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IDENTITY_AMBIGUOUS 4.1%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.0%, market_freshness 18.8%, execution 18.4%, data 12.8%, market_freshness/coverage 9.1%, mapping 4.1%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.3% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.1% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 15,278 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.0% of the time and with the model 1.1%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 474.0 points vs 1685.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.016, Gen-2 0.805, Gen-1 ledger 0.856 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 743 model 0.2221 vs Kalshi 0.2059; n 155 model 0.2842 vs Kalshi 0.1885.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 297,704 model-market comparisons (486,526 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 99,898 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-30T13:19:41.342319+00:00'], shadow board 79,992 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-30T13:19:45.359223+00:00'], Model 4 37,091 rows, 24,106 settled tickers, 8,863 tickers with an external scan.
* By model: {"gen1_ledger": 67276, "gen1_elo": 40205, "fair_v1": 40205, "gen2": 40205, "gen1_sr": 40205, "model4_fundamental": 34826, "model4_conditioned": 34782}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 70,009 | 14.1 | 9.6 | 20.2 | 15.3 | 19.0 | 13.8 | 8.0 | 11.86 | 40.9% | 21.8% |
| MW fair_v1 | 40,205 | 12.9 | 8.7 | 18.7 | 15.3 | 19.5 | 14.9 | 9.9 | 13.01 | 44.3% | 24.8% |
| MW gen1_elo | 40,205 | 12.5 | 8.6 | 19.3 | 15.4 | 19.5 | 14.8 | 9.8 | 12.93 | 44.1% | 24.6% |
| MW gen1_ledger | 29,804 | 15.6 | 10.8 | 22.1 | 15.3 | 18.4 | 12.3 | 5.5 | 10.36 | 36.2% | 17.8% |
| MW gen1_sr | 40,205 | 10.1 | 7.2 | 16.9 | 13.8 | 20.7 | 18.6 | 12.7 | 15.85 | 52.0% | 31.3% |
| MW gen2 | 40,205 | 11.1 | 7.5 | 16.6 | 13.8 | 19.4 | 17.8 | 13.8 | 15.44 | 50.9% | 31.6% |
| all families model4_conditioned | 34,782 | 22.5 | 18.3 | 34.1 | 17.1 | 4.9 | 1.9 | 1.1 | 5.98 | 8.0% | 3.1% |
| all families model4_fundamental | 34,826 | 17.4 | 13.3 | 33.9 | 20.2 | 10.1 | 3.6 | 1.4 | 7.66 | 15.2% | 5.0% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.2%, >=15pp 40.9%, >=20pp 30.2%, >=25pp 21.8%, >=30pp 15.7%, >=40pp 8.0%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.3pp; >=10pp 44.8%, >=25pp 17.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,445 | 27.3 | 15.4 | 27.7 | 13.4 | 11.5 | 4.0 | 0.6 | 5.92 | 16.1% | 4.6% |
| CHALLENGER | 5,974 | 16.2 | 9.8 | 20.9 | 15.1 | 15.4 | 11.8 | 10.9 | 10.91 | 38.0% | 22.6% |
| ITF_MEN | 11,301 | 9.8 | 7.4 | 17.0 | 15.1 | 21.2 | 17.6 | 11.9 | 15.22 | 50.7% | 29.5% |
| ITF_WOMEN | 15,863 | 9.7 | 7.1 | 15.9 | 15.1 | 22.0 | 18.1 | 12.1 | 15.67 | 52.2% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,494 | 18.2 | 13.7 | 24.9 | 19.9 | 16.1 | 6.3 | 1.0 | 8.2 | 23.3% | 7.3% |
| WTA125 | 1,122 | 16.5 | 7.4 | 22.4 | 18.9 | 20.9 | 12.0 | 1.9 | 10.73 | 34.8% | 13.9% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,445 | 26.0 | 15.4 | 25.9 | 16.1 | 11.8 | 4.1 | 0.8 | 6.22 | 16.7% | 4.9% |
| CHALLENGER | 5,974 | 15.1 | 9.0 | 18.3 | 14.2 | 18.1 | 13.6 | 11.7 | 12.51 | 43.3% | 25.3% |
| ITF_MEN | 11,301 | 8.0 | 6.2 | 15.1 | 13.8 | 19.5 | 20.7 | 16.6 | 17.94 | 56.8% | 37.3% |
| ITF_WOMEN | 15,863 | 8.0 | 5.8 | 14.0 | 12.8 | 20.6 | 21.2 | 17.6 | 19.1 | 59.4% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,494 | 15.3 | 10.9 | 22.2 | 15.3 | 21.9 | 12.5 | 1.9 | 10.59 | 36.3% | 14.4% |
| WTA125 | 1,122 | 9.9 | 6.6 | 16.8 | 15.9 | 24.2 | 17.6 | 8.9 | 15.22 | 50.8% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,445 | 22.1 | 13.3 | 24.5 | 16.1 | 16.1 | 6.6 | 1.3 | 7.59 | 24.1% | 7.9% |
| CHALLENGER | 5,974 | 15.0 | 9.3 | 20.9 | 16.1 | 15.6 | 12.1 | 11.1 | 11.33 | 38.7% | 23.2% |
| ITF_MEN | 11,301 | 9.3 | 7.2 | 17.4 | 14.3 | 21.8 | 17.8 | 12.3 | 15.69 | 51.8% | 30.0% |
| ITF_WOMEN | 15,863 | 9.4 | 6.9 | 16.4 | 15.8 | 22.0 | 18.0 | 11.4 | 15.49 | 51.5% | 29.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,494 | 23.6 | 16.7 | 32.1 | 14.3 | 9.1 | 2.9 | 1.2 | 6.06 | 13.3% | 4.2% |
| WTA125 | 1,122 | 21.6 | 12.9 | 26.8 | 17.5 | 15.0 | 5.9 | 0.4 | 8.0 | 21.2% | 6.2% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,021 | 24.4 | 19.2 | 31.1 | 12.7 | 9.1 | 2.9 | 0.5 | 5.74 | 12.5% | 3.4% |
| CHALLENGER | 4,043 | 22.5 | 14.6 | 27.4 | 14.5 | 13.5 | 5.9 | 1.6 | 7.09 | 21.0% | 7.5% |
| DOUBLES | 2,151 | 5.1 | 4.4 | 12.2 | 10.7 | 21.1 | 25.0 | 21.7 | 23.56 | 67.7% | 46.6% |
| ITF_MEN | 8,573 | 13.0 | 9.4 | 21.2 | 15.9 | 21.4 | 13.3 | 5.8 | 11.9 | 40.5% | 19.1% |
| ITF_WOMEN | 10,238 | 13.1 | 9.2 | 19.9 | 15.8 | 21.2 | 15.3 | 5.5 | 12.32 | 42.0% | 20.9% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,493 | 24.4 | 15.5 | 30.7 | 17.5 | 9.0 | 2.7 | 0.3 | 6.6 | 11.9% | 2.9% |
| WTA125 | 1,136 | 25.1 | 12.7 | 20.9 | 19.3 | 13.5 | 7.0 | 1.6 | 7.88 | 22.0% | 8.5% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,346 | 27.7 | 15.6 | 28.0 | 13.4 | 11.3 | 3.6 | 0.4 | 5.88 | 15.3% | 4.0% |
| CHALLENGER | 4,185 | 21.2 | 12.3 | 26.0 | 17.6 | 15.3 | 6.1 | 1.6 | 8.03 | 22.9% | 7.7% |
| ITF_MEN | 8,275 | 11.9 | 8.8 | 20.5 | 17.2 | 22.1 | 14.3 | 5.2 | 12.41 | 41.5% | 19.5% |
| ITF_WOMEN | 11,783 | 11.6 | 8.5 | 18.5 | 17.3 | 23.9 | 15.1 | 5.2 | 13.27 | 44.1% | 20.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,412 | 18.5 | 13.7 | 25.1 | 20.2 | 16.2 | 5.8 | 0.5 | 8.15 | 22.5% | 6.3% |
| WTA125 | 1,086 | 16.8 | 7.3 | 21.9 | 19.1 | 21.4 | 11.8 | 1.7 | 11.0 | 34.9% | 13.4% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,346 | 26.3 | 15.7 | 26.1 | 16.1 | 11.8 | 3.7 | 0.5 | 6.2 | 15.9% | 4.2% |
| CHALLENGER | 4,185 | 19.3 | 11.5 | 22.9 | 16.7 | 18.5 | 9.0 | 2.0 | 8.99 | 29.5% | 11.0% |
| ITF_MEN | 8,276 | 9.5 | 7.3 | 17.5 | 16.1 | 21.3 | 18.8 | 9.6 | 14.93 | 49.7% | 28.4% |
| ITF_WOMEN | 11,784 | 8.9 | 6.8 | 15.9 | 14.3 | 22.7 | 20.6 | 10.8 | 16.54 | 54.1% | 31.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,412 | 15.5 | 10.9 | 22.4 | 15.4 | 22.1 | 12.4 | 1.2 | 10.4 | 35.8% | 13.6% |
| WTA125 | 1,086 | 9.9 | 6.6 | 16.9 | 16.0 | 24.1 | 18.0 | 8.4 | 15.14 | 50.5% | 26.3% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,967 | 24.6 | 19.5 | 31.2 | 12.9 | 8.7 | 2.8 | 0.4 | 5.67 | 11.9% | 3.2% |
| CHALLENGER | 3,565 | 24.0 | 15.5 | 28.6 | 14.7 | 12.8 | 4.0 | 0.5 | 6.59 | 17.2% | 4.5% |
| DOUBLES | 2,019 | 5.0 | 4.5 | 12.4 | 10.8 | 20.9 | 24.9 | 21.6 | 23.51 | 67.3% | 46.4% |
| ITF_MEN | 7,321 | 13.8 | 10.0 | 22.9 | 16.5 | 21.3 | 11.8 | 3.8 | 10.94 | 36.9% | 15.5% |
| ITF_WOMEN | 8,726 | 13.7 | 9.6 | 21.1 | 16.4 | 21.3 | 14.3 | 3.5 | 11.5 | 39.1% | 17.8% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,439 | 24.8 | 15.8 | 30.7 | 17.5 | 9.0 | 2.1 | 0.1 | 6.44 | 11.1% | 2.1% |
| WTA125 | 1,011 | 26.4 | 13.4 | 22.0 | 20.4 | 12.5 | 4.8 | 0.5 | 7.32 | 17.8% | 5.3% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,151 | 5.1 | 4.4 | 12.2 | 10.7 | 21.1 | 25.0 | 21.7 | 23.56 | 67.7% | 46.6% |
| singles | 27,653 | 16.4 | 11.2 | 22.9 | 15.6 | 18.2 | 11.3 | 4.2 | 9.83 | 33.8% | 15.6% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,973 | 13.1 | 9.3 | 20.2 | 15.6 | 19.0 | 13.8 | 8.9 | 12.3 | 41.7% | 22.7% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 26,382 | 13.4 | 8.7 | 18.6 | 15.1 | 19.2 | 15.0 | 10.0 | 12.98 | 44.2% | 25.0% |
| UNKNOWN | 5,601 | 10.4 | 7.8 | 17.1 | 16.5 | 21.3 | 16.0 | 11.1 | 14.23 | 48.4% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 11,150 | 20.0 | 12.1 | 22.4 | 15.6 | 14.7 | 9.1 | 6.1 | 8.53 | 29.9% | 15.2% |
| B | 4,984 | 12.9 | 9.0 | 19.3 | 15.8 | 19.4 | 12.6 | 11.0 | 12.54 | 43.0% | 23.6% |
| C | 5,765 | 11.8 | 8.9 | 19.9 | 15.8 | 18.5 | 14.4 | 10.7 | 12.82 | 43.6% | 25.0% |
| D | 6,365 | 11.9 | 8.3 | 17.6 | 15.3 | 21.6 | 16.0 | 9.3 | 13.83 | 46.9% | 25.3% |
| F | 11,941 | 7.3 | 5.6 | 15.1 | 14.8 | 23.4 | 20.9 | 13.0 | 17.66 | 57.3% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,928 | 24.1 | 15.8 | 29.0 | 15.2 | 11.0 | 3.7 | 1.3 | 6.51 | 15.9% | 5.0% |
| B | 4,243 | 16.9 | 10.7 | 24.2 | 16.7 | 18.7 | 9.7 | 3.1 | 9.61 | 31.5% | 12.8% |
| C | 5,833 | 11.3 | 7.9 | 19.4 | 14.7 | 21.0 | 15.7 | 10.1 | 13.48 | 46.8% | 25.8% |
| D | 4,369 | 14.4 | 9.8 | 21.8 | 15.4 | 20.0 | 13.2 | 5.4 | 11.25 | 38.7% | 18.6% |
| F | 7,431 | 9.8 | 8.3 | 16.1 | 15.0 | 23.2 | 19.9 | 7.7 | 15.42 | 50.8% | 27.6% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 12,623 | 18.3 | 11.0 | 21.5 | 15.3 | 15.1 | 9.9 | 8.9 | 9.74 | 33.9% | 18.8% |
| LIMITED | 8,904 | 13.6 | 10.0 | 20.4 | 16.1 | 19.1 | 13.2 | 7.6 | 11.7 | 39.8% | 20.7% |
| POOR | 18,678 | 9.0 | 6.5 | 16.0 | 15.0 | 22.7 | 19.1 | 11.7 | 16.14 | 53.4% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,651 | 24.3 | 18.1 | 33.0 | 14.9 | 6.5 | 2.7 | 0.4 | 5.82 | 9.7% | 3.1% |
| GAME_SPREAD | 5,986 | 22.2 | 15.2 | 32.8 | 17.1 | 9.0 | 2.9 | 0.6 | 6.73 | 12.6% | 3.5% |
| MATCH_WINNER | 29,804 | 15.6 | 10.8 | 22.1 | 15.3 | 18.4 | 12.3 | 5.5 | 10.36 | 36.2% | 17.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 13,851 | 27.6 | 16.7 | 31.0 | 12.5 | 9.4 | 2.5 | 0.3 | 5.66 | 12.2% | 2.8% |
| TOTAL_GAMES | 9,960 | 9.8 | 10.6 | 35.7 | 26.6 | 10.4 | 4.0 | 2.8 | 9.25 | 17.3% | 6.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,295 | 24.6 | 30.1 | 32.8 | 7.3 | 4.1 | 0.9 | 0.3 | 4.7 | 5.2% | 1.1% |
| GAME_SPREAD | 8,140 | 47.5 | 16.0 | 25.2 | 7.3 | 2.2 | 1.3 | 0.6 | 3.25 | 4.1% | 1.9% |
| TOTAL_GAMES | 14,347 | 6.5 | 9.4 | 40.3 | 31.2 | 7.2 | 3.2 | 2.2 | 9.28 | 12.6% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,306 | 24.0 | 16.8 | 34.9 | 14.3 | 7.1 | 2.6 | 0.4 | 6.0 | 10.1% | 3.0% |
| GAME_SPREAD | 8,143 | 20.2 | 13.6 | 28.0 | 20.4 | 12.4 | 4.3 | 1.1 | 7.75 | 17.7% | 5.3% |
| TOTAL_GAMES | 14,377 | 10.1 | 10.3 | 36.3 | 25.2 | 11.5 | 4.2 | 2.4 | 9.16 | 18.1% | 6.6% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 40,205 | 44.3% | 24.8% | 13.01 | 35.5% | 15.3% | 10.71 |
| gen1_elo | 40,205 | 44.1% | 24.6% | 12.93 | 35.2% | 15.3% | 10.53 |
| gen1_sr | 40,205 | 52.0% | 31.3% | 15.85 | 44.1% | 21.7% | 13.01 |
| gen2 | 40,205 | 50.9% | 31.6% | 15.44 | 44.0% | 23.4% | 12.86 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 18,643 | 15.6 | 10.6 | 21.3 | 17.2 | 20.1 | 12.0 | 3.3 | 10.71 | 35.4% | 15.3% |
| STALE | 21,562 | 10.6 | 7.1 | 16.4 | 13.8 | 19.0 | 17.4 | 15.6 | 15.8 | 52.0% | 33.0% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 23,272 | 16.3 | 11.1 | 22.8 | 15.4 | 17.8 | 11.8 | 4.7 | 9.94 | 34.4% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 70,009 | 23272 | 22115 | 24622 | 24.4 | 124.9 | 1451.1 |
| ge_15pp | 28,607 | 7996 | 7884 | 12727 | 26.9 | 436.0 | 1451.1 |
| ge_25pp | 15,278 | 3844 | 3443 | 7991 | 32.0 | 585.9 | 1431.1 |
| lt_10pp | 30,676 | 11687 | 10480 | 8509 | 22.4 | 47.1 | 1421.1 |

Current slate `SL-20261030T133611Z-e96382eb`: 338 priced rows, quote age at build {'median': 16.9, 'max': 16.9}, freshness {'AGING': 338}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 45 | 0.0 | 0.0 | 31.1 | 6.7 | 35.6 | 22.2 | 4.4 | 20.19 | 62.2% | 26.7% |
| EXTERNAL_LONE_OUTLIER | 25 | 64.0 | 36.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.43 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,997 | 19.8 | 11.1 | 25.4 | 17.8 | 17.8 | 7.1 | 0.9 | 8.52 | 25.9% | 8.0% |
| KALSHI_LONE_OUTLIER | 27 | 3.7 | 3.7 | 77.8 | 7.4 | 3.7 | 3.7 | 0.0 | 6.42 | 7.4% | 3.7% |
| MARKETS_AGREE | 784 | 65.4 | 34.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.21 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,716 | 0.0 | 2.5 | 36.4 | 25.4 | 24.9 | 10.0 | 0.9 | 12.0 | 35.8% | 10.9% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 40,205 | 6594 (16.4%) | 26.0% | 1.1% | {"EXTERNAL_STALE": 3997, "AGREES_WITH_KALSHI": 1716, "ALL_AGREE": 784, "SUPPORTS_MODEL_DIRECTION": 44, "AGREES_WITH_MODEL": 27, "EXTERNAL_OUTLIER": 25, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 17,812 | 1679 (9.4%) | 36.6% | 1.8% | {"EXTERNAL_STALE": 1034, "AGREES_WITH_KALSHI": 615, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 9,972 | 521 (5.2%) | 35.9% | 2.5% | {"EXTERNAL_STALE": 321, "AGREES_WITH_KALSHI": 187, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,747 | 494 (10.4%) | 36.4% | 2.6% | {"EXTERNAL_STALE": 301, "AGREES_WITH_KALSHI": 180, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 16,220 | 3764 (23.2%) | 17.7% | 1.0% | {"EXTERNAL_STALE": 2252, "ALL_AGREE": 784, "AGREES_WITH_KALSHI": 666, "EXTERNAL_OUTLIER": 25, "AGREES_WITH_MODEL": 23, "SUPPORTS_MODEL_DIRECTION": 13, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 7,857 | 10.5 | 7.5 | 19.6 | 14.4 | 21.5 | 16.5 | 10.0 | 14.09 | 48.0% | 26.5% |
| 4-10x | 5,431 | 11.0 | 8.5 | 18.7 | 15.5 | 21.9 | 14.4 | 9.9 | 13.6 | 46.2% | 24.3% |
| <2x | 20,377 | 15.2 | 10.0 | 19.5 | 16.0 | 17.4 | 13.0 | 9.0 | 11.55 | 39.4% | 22.0% |
| >=10x | 6,540 | 10.4 | 6.4 | 15.1 | 14.5 | 21.7 | 19.2 | 12.7 | 16.35 | 53.6% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 10,394 | 12.8 | 8.9 | 19.5 | 15.9 | 19.0 | 13.4 | 10.4 | 12.66 | 42.9% | 23.8% |
| 300-1000 | 8,701 | 11.9 | 8.7 | 17.9 | 15.3 | 20.3 | 16.4 | 9.5 | 13.59 | 46.2% | 25.9% |
| <300 | 12,907 | 8.2 | 5.8 | 15.2 | 14.8 | 23.0 | 20.0 | 12.9 | 17.06 | 56.0% | 32.9% |
| >=3000 | 8,203 | 21.5 | 13.1 | 24.1 | 15.5 | 13.7 | 7.1 | 4.9 | 7.57 | 25.8% | 12.1% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1155 | 0.5496 | 0.4103 | 0.497 | +0.053 | -0.087 | -0.002 ± 0.0046 |
| ratio 4-10x | 800 | 0.5809 | 0.4342 | 0.4963 | +0.085 | -0.062 | 0.007 ± 0.0056 |
| ratio <2x | 2769 | 0.5382 | 0.415 | 0.4467 | +0.091 | -0.032 | 0.0124 ± 0.0027 |
| ratio >=10x | 994 | 0.5685 | 0.3941 | 0.4527 | +0.116 | -0.059 | 0.0134 ± 0.0058 |
| thinner_sample 1000-3000 | 1560 | 0.5404 | 0.4133 | 0.4519 | +0.088 | -0.039 | 0.0097 ± 0.0037 |
| thinner_sample 300-1000 | 1305 | 0.5679 | 0.4256 | 0.4866 | +0.081 | -0.061 | 0.0023 ± 0.0044 |
| thinner_sample <300 | 1911 | 0.5597 | 0.3921 | 0.4615 | +0.098 | -0.070 | 0.0107 ± 0.0041 |
| thinner_sample >=3000 | 942 | 0.5322 | 0.4382 | 0.4628 | +0.069 | -0.025 | 0.0132 ± 0.0037 |
| data_status ADEQUATE | 1549 | 0.5347 | 0.4317 | 0.45 | +0.085 | -0.018 | 0.0133 ± 0.0031 |
| data_status LIMITED | 1398 | 0.5495 | 0.4163 | 0.4735 | +0.076 | -0.057 | 0.0063 ± 0.004 |
| data_status POOR | 2771 | 0.5624 | 0.4011 | 0.4688 | +0.094 | -0.068 | 0.0078 ± 0.0033 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 829 | 0.1995 | 0.1999 | -0.0004 ± 0.0005 | 0.5786 | 0.5798 | 0.5043 | 0.4891 | 0.509 | -0.088 ± 0.0165 | -0.01 (5) |
| 3-5 | 523 | 0.2055 | 0.2059 | -0.0004 ± 0.0016 | 0.5936 | 0.5932 | 0.5035 | 0.4637 | 0.4876 | -0.095 ± 0.0203 | 0.02 (1) |
| 5-10 | 1203 | 0.2014 | 0.2017 | -0.0003 ± 0.0019 | 0.5889 | 0.587 | 0.511 | 0.4372 | 0.4738 | -0.087 ± 0.0134 | -0.0167 (6) |
| 10-15 | 1001 | 0.2201 | 0.2118 | +0.0083 ± 0.0036 | 0.6326 | 0.6089 | 0.528 | 0.4044 | 0.4316 | -0.107 ± 0.0146 | -0.048 (5) |
| 15-25 | 1264 | 0.2258 | 0.2125 | +0.0132 ± 0.0051 | 0.6475 | 0.6093 | 0.577 | 0.3815 | 0.4454 | -0.102 ± 0.013 | -0.0033 (9) |
| 25-40 | 743 | 0.2221 | 0.2059 | +0.0162 ± 0.01 | 0.6336 | 0.5938 | 0.6549 | 0.3448 | 0.4738 | -0.075 ± 0.0152 | -0.01 (1) |
| 40+ | 155 | 0.2842 | 0.1885 | +0.0957 ± 0.0305 | 0.7739 | 0.5561 | 0.7384 | 0.2901 | 0.4129 | -0.076 ± 0.0302 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4544 | 0.1843 | 0.1851 | -0.0008 ± 0.0002 | 0.543 | 0.5441 | 0.4869 | 0.4717 | 0.502 | -0.023 ± 0.0065 | -0.0129 (17) |
| 3-5 | 3065 | 0.1952 | 0.1935 | +0.0017 ± 0.0006 | 0.5695 | 0.563 | 0.4823 | 0.4425 | 0.4398 | -0.058 ± 0.008 | 0.0 (2) |
| 5-10 | 6516 | 0.2023 | 0.1988 | +0.0035 ± 0.0008 | 0.5906 | 0.5787 | 0.485 | 0.4114 | 0.4251 | -0.046 ± 0.0056 | -0.0119 (21) |
| 10-15 | 5409 | 0.2012 | 0.1854 | +0.0158 ± 0.0015 | 0.5885 | 0.5453 | 0.4846 | 0.3606 | 0.3583 | -0.066 ± 0.0059 | -0.0281 (16) |
| 15-25 | 6772 | 0.2068 | 0.168 | +0.0388 ± 0.002 | 0.6062 | 0.4984 | 0.5002 | 0.3042 | 0.304 | -0.071 ± 0.005 | -0.0025 (44) |
| 25-40 | 5359 | 0.2215 | 0.1255 | +0.0960 ± 0.003 | 0.637 | 0.3858 | 0.5259 | 0.2118 | 0.2202 | -0.059 ± 0.0047 | -0.01 (1) |
| 40+ | 3518 | 0.3849 | 0.0446 | +0.3403 ± 0.0041 | 1.0026 | 0.1729 | 0.6331 | 0.1039 | 0.0591 | -0.079 ± 0.0034 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 658 | 0.2054 | 0.2061 | -0.0007 ± 0.0006 | 0.5923 | 0.5942 | 0.5081 | 0.4932 | 0.5258 | -0.098 ± 0.0191 | -0.01 (3) |
| 3-5 | 466 | 0.221 | 0.2184 | +0.0026 ± 0.0017 | 0.6266 | 0.6213 | 0.5127 | 0.4731 | 0.4549 | -0.129 ± 0.023 | 0.02 (1) |
| 5-10 | 1050 | 0.2083 | 0.2075 | +0.0009 ± 0.0021 | 0.6032 | 0.6 | 0.5433 | 0.4686 | 0.5019 | -0.089 ± 0.0145 | -0.01 (4) |
| 10-15 | 926 | 0.2163 | 0.2102 | +0.0062 ± 0.0038 | 0.6236 | 0.6076 | 0.564 | 0.4396 | 0.4795 | -0.107 ± 0.0157 | -0.04 (5) |
| 15-25 | 1331 | 0.23 | 0.2141 | +0.0159 ± 0.005 | 0.6547 | 0.6125 | 0.5833 | 0.388 | 0.447 | -0.097 ± 0.0129 | -0.0133 (9) |
| 25-40 | 939 | 0.2679 | 0.1971 | +0.0708 ± 0.0091 | 0.7481 | 0.5748 | 0.659 | 0.3448 | 0.3919 | -0.132 ± 0.0144 | -0.0075 (4) |
| 40+ | 348 | 0.3628 | 0.1666 | +0.1961 ± 0.0217 | 0.9945 | 0.5008 | 0.7323 | 0.247 | 0.3017 | -0.081 ± 0.0212 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3922 | 0.1896 | 0.1899 | -0.0003 ± 0.0002 | 0.5542 | 0.5546 | 0.5091 | 0.4941 | 0.5107 | -0.040 ± 0.0072 | -0.0133 (15) |
| 3-5 | 2653 | 0.1963 | 0.1952 | +0.0011 ± 0.0007 | 0.5696 | 0.566 | 0.5107 | 0.471 | 0.4753 | -0.048 ± 0.0088 | 0.02 (1) |
| 5-10 | 5785 | 0.1988 | 0.1953 | +0.0035 ± 0.0009 | 0.5831 | 0.5699 | 0.51 | 0.4359 | 0.4522 | -0.043 ± 0.0059 | -0.0117 (6) |
| 10-15 | 4852 | 0.2046 | 0.1925 | +0.0121 ± 0.0016 | 0.5985 | 0.5624 | 0.5124 | 0.3886 | 0.4025 | -0.053 ± 0.0064 | -0.0189 (18) |
| 15-25 | 6794 | 0.2173 | 0.1813 | +0.0360 ± 0.002 | 0.6319 | 0.5318 | 0.5234 | 0.3281 | 0.3369 | -0.062 ± 0.0052 | -0.0086 (42) |
| 25-40 | 6256 | 0.2516 | 0.1358 | +0.1158 ± 0.003 | 0.7098 | 0.4166 | 0.5577 | 0.2409 | 0.2201 | -0.086 ± 0.0046 | -0.0044 (18) |
| 40+ | 4921 | 0.3987 | 0.0587 | +0.3400 ± 0.004 | 1.0524 | 0.2116 | 0.6524 | 0.1173 | 0.0809 | -0.073 ± 0.0034 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 795 | 0.1958 | 0.198 | -0.0022 ± 0.0006 | 0.5705 | 0.5761 | 0.4995 | 0.4841 | 0.5447 | -0.038 ± 0.0165 | -0.0137 (8) |
| 3-5 | 557 | 0.2054 | 0.2037 | +0.0017 ± 0.0015 | 0.5938 | 0.5878 | 0.4954 | 0.4558 | 0.4542 | -0.120 ± 0.0198 | 0.0067 (3) |
| 5-10 | 1242 | 0.2033 | 0.2016 | +0.0017 ± 0.0019 | 0.5925 | 0.5861 | 0.5106 | 0.4368 | 0.4605 | -0.095 ± 0.0131 | -0.0071 (7) |
| 10-15 | 1004 | 0.2087 | 0.204 | +0.0047 ± 0.0035 | 0.6072 | 0.5916 | 0.5394 | 0.416 | 0.4602 | -0.096 ± 0.0143 | -0.0317 (6) |
| 15-25 | 1198 | 0.2345 | 0.2173 | +0.0172 ± 0.0052 | 0.6683 | 0.6198 | 0.5887 | 0.3945 | 0.4474 | -0.112 ± 0.0135 | -0.03 (1) |
| 25-40 | 759 | 0.2127 | 0.2127 | -0.0000 ± 0.0098 | 0.6139 | 0.6096 | 0.6629 | 0.3524 | 0.5059 | -0.058 ± 0.0151 | 0.015 (2) |
| 40+ | 163 | 0.2995 | 0.196 | +0.1035 ± 0.0306 | 0.8153 | 0.5732 | 0.7492 | 0.2987 | 0.4172 | -0.077 ± 0.0316 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4372 | 0.1835 | 0.1841 | -0.0007 ± 0.0002 | 0.5402 | 0.5415 | 0.4826 | 0.4673 | 0.486 | -0.033 ± 0.0066 | -0.0163 (35) |
| 3-5 | 3011 | 0.202 | 0.1999 | +0.0021 ± 0.0007 | 0.587 | 0.5796 | 0.4806 | 0.4411 | 0.4347 | -0.063 ± 0.0083 | -0.0094 (18) |
| 5-10 | 6675 | 0.1944 | 0.1906 | +0.0039 ± 0.0008 | 0.5721 | 0.5587 | 0.4856 | 0.4115 | 0.4229 | -0.047 ± 0.0054 | -0.01 (31) |
| 10-15 | 5401 | 0.1922 | 0.1787 | +0.0134 ± 0.0014 | 0.5684 | 0.5293 | 0.4943 | 0.3708 | 0.3775 | -0.057 ± 0.0058 | -0.015 (12) |
| 15-25 | 6886 | 0.2135 | 0.1733 | +0.0401 ± 0.002 | 0.6216 | 0.5106 | 0.5134 | 0.3189 | 0.3144 | -0.074 ± 0.005 | -0.03 (2) |
| 25-40 | 5349 | 0.216 | 0.1287 | +0.0873 ± 0.0031 | 0.6252 | 0.3933 | 0.5295 | 0.214 | 0.2356 | -0.048 ± 0.0047 | 0.01 (3) |
| 40+ | 3489 | 0.3948 | 0.0502 | +0.3446 ± 0.0043 | 1.0295 | 0.1872 | 0.6427 | 0.1105 | 0.0659 | -0.079 ± 0.0036 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1194 | 0.196 | 0.1961 | -0.0002 ± 0.0004 | 0.5706 | 0.5708 | 0.5045 | 0.4893 | 0.4941 | -0.069 ± 0.0131 | -0.0224 (49) |
| 3-5 | 850 | 0.1872 | 0.1863 | +0.0009 ± 0.0012 | 0.5488 | 0.546 | 0.4966 | 0.4567 | 0.4635 | -0.069 ± 0.0152 | -0.0194 (34) |
| 5-10 | 1770 | 0.2011 | 0.1964 | +0.0047 ± 0.0016 | 0.5911 | 0.5762 | 0.5024 | 0.4288 | 0.4339 | -0.077 ± 0.0108 | -0.005 (78) |
| 10-15 | 1208 | 0.2167 | 0.2041 | +0.0126 ± 0.0032 | 0.6258 | 0.5922 | 0.5375 | 0.4147 | 0.423 | -0.089 ± 0.0134 | 0.0014 (64) |
| 15-25 | 1550 | 0.2322 | 0.211 | +0.0212 ± 0.0046 | 0.6616 | 0.607 | 0.5837 | 0.389 | 0.4348 | -0.085 ± 0.0118 | -0.0214 (59) |
| 25-40 | 976 | 0.2443 | 0.2104 | +0.0339 ± 0.009 | 0.6981 | 0.6032 | 0.6839 | 0.372 | 0.4744 | -0.095 ± 0.0138 | -0.0219 (26) |
| 40+ | 327 | 0.3343 | 0.2031 | +0.1312 ± 0.024 | 0.9686 | 0.5915 | 0.8158 | 0.3392 | 0.4557 | -0.099 ± 0.0225 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4479 | 0.1759 | 0.1762 | -0.0003 ± 0.0002 | 0.5208 | 0.5211 | 0.5089 | 0.4936 | 0.5061 | -0.037 ± 0.0063 | -0.0157 (88) |
| 3-5 | 3082 | 0.1936 | 0.1921 | +0.0015 ± 0.0006 | 0.5636 | 0.5605 | 0.5028 | 0.463 | 0.4633 | -0.051 ± 0.008 | -0.0209 (69) |
| 5-10 | 6300 | 0.1987 | 0.1917 | +0.0070 ± 0.0008 | 0.5841 | 0.5639 | 0.4982 | 0.4246 | 0.416 | -0.066 ± 0.0056 | -0.0082 (132) |
| 10-15 | 4384 | 0.2111 | 0.1954 | +0.0157 ± 0.0017 | 0.6131 | 0.5719 | 0.5361 | 0.4131 | 0.4097 | -0.070 ± 0.0068 | -0.0053 (105) |
| 15-25 | 5306 | 0.2299 | 0.2009 | +0.0290 ± 0.0024 | 0.6611 | 0.5813 | 0.5705 | 0.3752 | 0.3997 | -0.063 ± 0.0062 | -0.0253 (107) |
| 25-40 | 3595 | 0.2606 | 0.1872 | +0.0734 ± 0.0045 | 0.7371 | 0.5464 | 0.6363 | 0.3238 | 0.3655 | -0.079 ± 0.0071 | -0.0229 (51) |
| 40+ | 1532 | 0.378 | 0.1538 | +0.2242 ± 0.0104 | 1.0704 | 0.46 | 0.7407 | 0.2392 | 0.2774 | -0.074 ± 0.0095 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5718 | 1.016 ± 0.037 | 1.089 | 0.1694 | 0.1663 | 0.2151 | 0.2062 |
| gen2 | 5718 | 0.805 ± 0.034 | 1.053 | 0.1715 | 0.1668 | 0.2345 | 0.206 |
| gen1_elo | 5718 | 0.992 ± 0.035 | 1.086 | 0.1758 | 0.1665 | 0.2139 | 0.2063 |
| gen1_sr | 5718 | 0.989 ± 0.044 | 1.112 | 0.1316 | 0.1687 | 0.2304 | 0.2057 |
| gen1_ledger | 7875 | 0.856 ± 0.027 | 1.058 | 0.1878 | 0.1759 | 0.2182 | 0.2013 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 28,607)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,435 | 22.5% |
| STALE_QUOTE | market_freshness | 6,317 | 22.1% |
| BOOK_QUALITY | execution | 5,390 | 18.8% |
| POOR_DATA | data | 3,346 | 11.7% |
| LIMITED_DATA | data | 1,775 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,624 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,227 | 4.3% |
| IDENTITY_AMBIGUOUS | mapping | 1,176 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 826 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 490 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.5%, market_freshness 22.1%, execution 18.8%, data 17.9%, market_freshness/coverage 8.6%, model_calibration_or_unknown 4.3%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.5%, LOW_DATA_QUALITY 71.8%, THIN_PLAYER_HISTORY 60.3%, STALE_PLAYER_DATA 52.3%, STALE_KALSHI_QUOTE 44.5%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 33.4%, WIDE_SPREAD 24.9%, MODEL_HIGH_UNCERTAINTY 18.2%, PLAYER_IDENTITY_RISK 15.6%, LEVEL_TRANSFER_RISK 10.5%, LOW_DISPLAYED_LIQUIDITY 8.1%, EVENT_MAPPING_RISK 7.5%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.4%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.0%, POST_SETTLEMENT_OBSERVATION 22.5%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 15,278)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,200 | 34.0% |
| STALE_QUOTE | market_freshness | 2,872 | 18.8% |
| BOOK_QUALITY | execution | 2,807 | 18.4% |
| POOR_DATA | data | 1,434 | 9.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 852 | 5.6% |
| IDENTITY_AMBIGUOUS | mapping | 629 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 535 | 3.5% |
| LIMITED_DATA | data | 519 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 306 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 123 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.0%, market_freshness 18.8%, execution 18.4%, data 12.8%, market_freshness/coverage 9.1%, mapping 4.1%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 75.1%, THIN_PLAYER_HISTORY 62.5%, STALE_KALSHI_QUOTE 52.3%, STALE_PLAYER_DATA 46.3%, MODEL_INTERNAL_DISAGREEMENT 42.6%, ASYMMETRIC_SAMPLE_SIZE 34.5%, WIDE_SPREAD 24.4%, MODEL_HIGH_UNCERTAINTY 18.9%, PLAYER_IDENTITY_RISK 18.4%, LEVEL_TRANSFER_RISK 9.3%, EVENT_MAPPING_RISK 9.0%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.1%, POST_SETTLEMENT_OBSERVATION 34.0%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 12151, "IDENTITY_AMBIGUOUS": 3127}; ticker orientation: {"VERIFIED": 15278}.

Checks: discipline:AMBIGUOUS 1003, discipline:PASS 14275, identity_confidence:AMBIGUOUS 2806, identity_confidence:PASS 12472, level_mapping:NA 1015, level_mapping:PASS 14263, market_pair:AMBIGUOUS 480, market_pair:NA 349, market_pair:PASS 14449, model_complement:NA 313, model_complement:PASS 14965, namesake:AMBIGUOUS 6, namesake:PASS 15272, physical_match_id:NA 5306, physical_match_id:PASS 9972, player_ids:PASS 15278, same_pair_other_event:PASS 15278, ticker_orientation:PASS 15278

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,466 | 4.2% | 3.7% | 1.5% | {"market_freshness": 56, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "market_freshness/coverage": 17, "coverage": 13} | 5.84 | 0.2219 / 0.2176 (635) | 21.9% | 2.9% | 3.2% | 2.8% |
| CHALLENGER | 10,017 | 16.5% | 6.2% | 10.8% | {"coverage": 977, "market_freshness/coverage": 198, "market_freshness": 172, "data": 144, "model_calibration_or_unknown": 74, "execution": 37, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.25 | 0.2209 / 0.2116 (2283) | 35.6% | 15.6% | 4.1% | 22.6% |
| DOUBLES | 2,151 | 46.6% | 46.4% | 6.6% | {"execution": 566, "mapping": 265, "market_freshness": 106, "market_freshness/coverage": 59, "coverage": 7} | 23.51 | 0.3088 / 0.2386 (516) | 10.9% | 0.0% | 100.0% | 6.1% |
| ITF_MEN | 19,874 | 25.0% | 17.6% | 32.5% | {"coverage": 1746, "market_freshness": 916, "execution": 913, "data": 730, "market_freshness/coverage": 475, "mapping": 183, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.72 | 0.2165 / 0.1999 (4072) | 38.0% | 69.4% | 16.4% | 21.5% |
| ITF_WOMEN | 26,101 | 26.6% | 19.2% | 45.4% | {"coverage": 2414, "market_freshness": 1473, "execution": 1214, "data": 986, "market_freshness/coverage": 585, "mapping": 158, "model_calibration_or_unknown": 81, "model_calibration": 21} | 12.54 | 0.2037 / 0.1953 (4780) | 39.7% | 57.2% | 10.0% | 21.4% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,987 | 5.6% | 4.8% | 1.5% | {"market_freshness": 76, "model_calibration_or_unknown": 43, "coverage": 30, "execution": 27, "data": 19, "model_calibration": 18, "market_freshness/coverage": 11, "mapping": 1} | 7.45 | 0.2371 / 0.2301 (607) | 26.8% | 1.1% | 1.4% | 3.4% |
| WTA125 | 2,258 | 11.2% | 9.5% | 1.7% | {"market_freshness": 71, "model_calibration_or_unknown": 51, "market_freshness/coverage": 41, "data": 38, "execution": 21, "model_calibration": 15, "coverage": 12, "mapping": 4} | 9.17 | 0.2103 / 0.1925 (658) | 26.4% | 10.8% | 4.7% | 7.1% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 16.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 969 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 3 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 4 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 5 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 6 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 773 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 7 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 8 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 164 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 9 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 10 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 113 min (STALE); no external reference |
| 13 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 14 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 15.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 928 min (STALE); no external reference |
| 17 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 18 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 19 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 20 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 21 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 22 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 23 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 24 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 25 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 26 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 27 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 28 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 29 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 30 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 31 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 32 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 33 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 34 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 35 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 36 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 37 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 38 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 39 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 40 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 41 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 42 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 43 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 124 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 44 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 45 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 82 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |
| 46 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 47 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 48 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 49 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 22.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1345 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 50 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9704, "by_level_share_of_ge_25pp": {"ATP": 0.0149, "CHALLENGER": 0.1083, "DOUBLES": 0.0656, "ITF_MEN": 0.3254, "ITF_WOMEN": 0.4537, "OTHER": 0.0008, "WTA": 0.0147, "WTA125": 0.0166}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.523, "share_primary_cause_market_settled_or_in_play": 0.4312, "share_primary_cause_stale_quote_only": 0.188}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 15278, "identity_ambiguous_share": 0.2047, "ticker_orientation": {"VERIFIED": 15278}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 9972, "with_external": 521, "coverage": 0.0522, "external_status": {"EXTERNAL_STALE": 321, "AGREES_WITH_KALSHI": 187, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 321, "MODEL_LONE_OUTLIER": 187, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3589, "share_external_supports_model": 0.025}, "pregame_clean_ge_25pp": {"n": 4747, "with_external": 494, "coverage": 0.1041, "external_status": {"EXTERNAL_STALE": 301, "AGREES_WITH_KALSHI": 180, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 301, "MODEL_LONE_OUTLIER": 180, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3644, "share_external_supports_model": 0.0263}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 474.0, "median_sample_ratio": 2.48, "median_min_matches": 19.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.21, "data_status": {"POOR": 8653, "LIMITED": 3950, "ADEQUATE": 2675}, "comparison_lt_10pp": {"median_thinner_serve_points": 1685.0, "median_sample_ratio": 1.71, "median_min_matches": 89.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1155, "model_minus_observed": 0.0526, "kalshi_minus_observed": -0.0866, "brier_diff_model_minus_kalshi": -0.002}, "4-10x": {"n": 800, "model_minus_observed": 0.0847, "kalshi_minus_observed": -0.062, "brier_diff_model_minus_kalshi": 0.007}, "<2x": {"n": 2769, "model_minus_observed": 0.0915, "kalshi_minus_observed": -0.0318, "brier_diff_model_minus_kalshi": 0.0124}, ">=10x": {"n": 994, "model_minus_observed": 0.1158, "kalshi_minus_observed": -0.0586, "brier_diff_model_minus_kalshi": 0.0134}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 5718, "model": {"intercept": -0.532, "slope": 0.805, "slope_se": 0.034}, "kalshi_mid_same_rows": {"intercept": 0.194, "slope": 1.053, "slope_se": 0.037}, "mean_extremity_model": 0.1715, "mean_extremity_kalshi": 0.1668, "model_brier": 0.2345, "kalshi_brier": 0.206, "brier_diff_model_minus_kalshi": 0.0285, "brier_diff_se": 0.0025, "model_logloss": 0.6668, "kalshi_logloss": 0.595}, "fair_v1": {"n": 5718, "model": {"intercept": -0.416, "slope": 1.016, "slope_se": 0.037}, "kalshi_mid_same_rows": {"intercept": 0.279, "slope": 1.089, "slope_se": 0.038}, "mean_extremity_model": 0.1694, "mean_extremity_kalshi": 0.1663, "model_brier": 0.2151, "kalshi_brier": 0.2062, "brier_diff_model_minus_kalshi": 0.0089, "brier_diff_se": 0.0021, "model_logloss": 0.6193, "kalshi_logloss": 0.5953}, "gen1_elo": {"n": 5718, "model": {"intercept": -0.393, "slope": 0.992, "slope_se": 0.035}, "kalshi_mid_same_rows": {"intercept": 0.298, "slope": 1.086, "slope_se": 0.037}, "mean_extremity_model": 0.1758, "mean_extremity_kalshi": 0.1665, "model_brier": 0.2139, "kalshi_brier": 0.2063, "brier_diff_model_minus_kalshi": 0.0076, "brier_diff_se": 0.0021, "model_logloss": 0.6172, "kalshi_logloss": 0.5957}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.248, "share_ge_15": 0.443, "median_abs_gap": 13.01, "n": 40205}, "gen1_elo": {"share_ge_25": 0.2461, "share_ge_15": 0.4412, "median_abs_gap": 12.93, "n": 40205}, "gen1_sr": {"share_ge_25": 0.3131, "share_ge_15": 0.5201, "median_abs_gap": 15.85, "n": 40205}, "gen2": {"share_ge_25": 0.316, "share_ge_15": 0.5095, "median_abs_gap": 15.44, "n": 40205}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1526, "share_ge_15": 0.355, "median_abs_gap": 10.71, "n": 31093}, "gen1_elo": {"share_ge_25": 0.1526, "share_ge_15": 0.3521, "median_abs_gap": 10.53, "n": 31092}, "gen1_sr": {"share_ge_25": 0.2172, "share_ge_15": 0.4406, "median_abs_gap": 13.01, "n": 31095}, "gen2": {"share_ge_25": 0.2335, "share_ge_15": 0.4396, "median_abs_gap": 12.86, "n": 31095}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.84, "share_ge_25_all": 0.0415, "share_ge_25_pregame_clean": 0.0371}, "WTA": {"median_abs_gap_pregame_clean": 7.45, "share_ge_25_all": 0.0564, "share_ge_25_pregame_clean": 0.0478}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2365, "share_within_10pp_all": 0.4382, "share_within_10pp_pregame_clean": 0.4907, "corr_model_vs_mid_pregame_clean": 0.8506}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 829, "model_brier": 0.1995, "kalshi_brier": 0.1999, "brier_diff_model_minus_kalshi": -0.0004}, "10-15": {"n_settled": 1001, "model_brier": 0.2201, "kalshi_brier": 0.2118, "brier_diff_model_minus_kalshi": 0.0083}, "15-25": {"n_settled": 1264, "model_brier": 0.2258, "kalshi_brier": 0.2125, "brier_diff_model_minus_kalshi": 0.0132}, "25-40": {"n_settled": 743, "model_brier": 0.2221, "kalshi_brier": 0.2059, "brier_diff_model_minus_kalshi": 0.0162}, "3-5": {"n_settled": 523, "model_brier": 0.2055, "kalshi_brier": 0.2059, "brier_diff_model_minus_kalshi": -0.0004}, "40+": {"n_settled": 155, "model_brier": 0.2842, "kalshi_brier": 0.1885, "brier_diff_model_minus_kalshi": 0.0957}, "5-10": {"n_settled": 1203, "model_brier": 0.2014, "kalshi_brier": 0.2017, "brier_diff_model_minus_kalshi": -0.0003}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.532, "slope": 0.805, "slope_se": 0.034}, "kalshi_slope": {"intercept": 0.194, "slope": 1.053, "slope_se": 0.037}, "n": 5718}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.49, "slope": 0.856, "slope_se": 0.027}, "kalshi_slope": {"intercept": 0.164, "slope": 1.058, "slope_se": 0.031}, "n": 7875}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 516, "model_brier": 0.3088, "kalshi_brier": 0.2386, "brier_diff_model_minus_kalshi": 0.0702, "brier_diff_se": 0.0132, "corr_model_outcome": 0.0571, "corr_kalshi_outcome": 0.2264}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
