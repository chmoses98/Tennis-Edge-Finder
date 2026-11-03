# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-03T11:15Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 74,934): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.4%, 15-25 19.0%, 25-40 13.7%, 40+ 8.0%; median gap 11.8 pp.
* **Where the extremes live**: 96.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.5%, Challenger 10.9%, doubles 6.8%). Main tour: ATP 3.9% and WTA 6.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 16,251): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.6%, STALE_QUOTE 19.4%, BOOK_QUALITY 18.2%, POOR_DATA 9.4%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IDENTITY_AMBIGUOUS 4.2%, LIMITED_DATA 3.5%, IN_PLAY_QUOTE 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.6%, market_freshness 19.4%, execution 18.2%, data 12.9%, market_freshness/coverage 9.0%, mapping 4.2%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.5% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 16,251 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.8% of the time and with the model 1.1%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 479.0 points vs 1746.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.033, Gen-2 0.818, Gen-1 ledger 0.866 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 791 model 0.2196 vs Kalshi 0.2064; n 168 model 0.2896 vs Kalshi 0.181.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 322,890 model-market comparisons (526,051 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 107,290 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-03T11:03:44.518867+00:00'], shadow board 86,297 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-03T11:03:48.714394+00:00'], Model 4 40,986 rows, 25,912 settled tickers, 9,710 tickers with an external scan.
* By model: {"gen1_ledger": 72651, "gen1_elo": 43366, "fair_v1": 43366, "gen2": 43366, "gen1_sr": 43366, "model4_fundamental": 38423, "model4_conditioned": 38352}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 74,934 | 14.1 | 9.6 | 20.2 | 15.4 | 19.0 | 13.7 | 8.0 | 11.8 | 40.7% | 21.7% |
| MW fair_v1 | 43,366 | 12.9 | 8.7 | 18.8 | 15.5 | 19.5 | 14.7 | 9.8 | 12.95 | 44.1% | 24.5% |
| MW gen1_elo | 43,366 | 12.6 | 8.8 | 19.4 | 15.3 | 19.5 | 14.6 | 9.7 | 12.73 | 43.8% | 24.3% |
| MW gen1_ledger | 31,568 | 15.8 | 10.8 | 22.1 | 15.2 | 18.3 | 12.2 | 5.5 | 10.29 | 36.1% | 17.8% |
| MW gen1_sr | 43,366 | 10.2 | 7.3 | 16.9 | 13.9 | 20.6 | 18.6 | 12.5 | 15.7 | 51.7% | 31.1% |
| MW gen2 | 43,366 | 11.2 | 7.6 | 16.7 | 13.8 | 19.4 | 17.7 | 13.6 | 15.36 | 50.7% | 31.4% |
| all families model4_conditioned | 38,352 | 22.2 | 18.0 | 34.2 | 17.2 | 5.0 | 2.1 | 1.2 | 6.07 | 8.4% | 3.4% |
| all families model4_fundamental | 38,423 | 17.3 | 13.4 | 33.9 | 20.1 | 10.1 | 3.8 | 1.5 | 7.65 | 15.4% | 5.3% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.1%, >=15pp 40.7%, >=20pp 30.0%, >=25pp 21.7%, >=30pp 15.6%, >=40pp 8.0%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.29pp; >=10pp 44.7%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,822 | 28.0 | 15.5 | 27.9 | 13.4 | 10.9 | 3.7 | 0.6 | 5.88 | 15.2% | 4.3% |
| CHALLENGER | 6,563 | 16.1 | 9.7 | 20.8 | 15.4 | 15.8 | 11.5 | 10.6 | 10.86 | 37.9% | 22.1% |
| ITF_MEN | 11,960 | 9.9 | 7.4 | 16.9 | 15.0 | 21.4 | 17.5 | 12.1 | 15.35 | 50.9% | 29.5% |
| ITF_WOMEN | 16,860 | 9.5 | 7.0 | 16.0 | 15.2 | 22.1 | 18.1 | 12.1 | 15.74 | 52.3% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,896 | 17.1 | 13.0 | 24.6 | 21.3 | 16.3 | 6.6 | 1.1 | 8.68 | 24.1% | 7.8% |
| WTA125 | 1,259 | 15.9 | 7.1 | 22.9 | 19.9 | 20.4 | 12.2 | 1.7 | 10.67 | 34.3% | 13.9% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,822 | 26.5 | 15.8 | 26.1 | 15.6 | 11.5 | 3.8 | 0.8 | 6.08 | 16.0% | 4.5% |
| CHALLENGER | 6,563 | 15.1 | 9.0 | 18.6 | 14.1 | 18.4 | 13.5 | 11.3 | 12.38 | 43.2% | 24.8% |
| ITF_MEN | 11,960 | 8.1 | 6.2 | 15.1 | 13.7 | 19.7 | 20.8 | 16.5 | 18.0 | 56.9% | 37.3% |
| ITF_WOMEN | 16,860 | 7.9 | 5.8 | 14.1 | 12.8 | 20.6 | 21.2 | 17.7 | 19.1 | 59.5% | 38.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,896 | 14.5 | 10.3 | 21.7 | 16.1 | 22.0 | 12.8 | 2.6 | 11.03 | 37.4% | 15.4% |
| WTA125 | 1,259 | 10.2 | 7.2 | 16.4 | 15.7 | 24.3 | 17.6 | 8.7 | 15.19 | 50.6% | 26.3% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,822 | 22.7 | 13.7 | 25.2 | 15.7 | 15.4 | 6.2 | 1.2 | 7.34 | 22.8% | 7.4% |
| CHALLENGER | 6,563 | 15.2 | 9.5 | 21.0 | 15.7 | 15.9 | 11.9 | 10.8 | 11.15 | 38.6% | 22.7% |
| ITF_MEN | 11,960 | 9.4 | 7.2 | 17.3 | 14.1 | 22.0 | 17.6 | 12.5 | 15.77 | 52.1% | 30.1% |
| ITF_WOMEN | 16,860 | 9.3 | 7.0 | 16.4 | 15.8 | 22.1 | 18.1 | 11.4 | 15.51 | 51.5% | 29.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,896 | 22.9 | 16.7 | 32.0 | 15.0 | 9.0 | 3.4 | 1.1 | 6.12 | 13.4% | 4.5% |
| WTA125 | 1,259 | 21.2 | 13.0 | 25.9 | 18.4 | 15.2 | 6.0 | 0.3 | 8.02 | 21.4% | 6.3% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,249 | 25.8 | 19.6 | 30.6 | 12.5 | 8.4 | 2.6 | 0.4 | 5.48 | 11.5% | 3.1% |
| CHALLENGER | 4,244 | 22.5 | 14.4 | 27.3 | 14.6 | 13.7 | 5.9 | 1.6 | 7.15 | 21.2% | 7.5% |
| DOUBLES | 2,314 | 5.1 | 4.3 | 12.2 | 10.5 | 20.3 | 25.2 | 22.4 | 23.85 | 67.9% | 47.6% |
| ITF_MEN | 8,885 | 12.9 | 9.4 | 21.1 | 15.8 | 21.4 | 13.2 | 6.0 | 11.92 | 40.7% | 19.2% |
| ITF_WOMEN | 10,877 | 13.3 | 9.1 | 20.0 | 15.8 | 21.1 | 15.2 | 5.5 | 12.28 | 41.9% | 20.7% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,667 | 24.2 | 16.4 | 30.5 | 17.0 | 8.9 | 2.8 | 0.2 | 6.53 | 11.9% | 3.0% |
| WTA125 | 1,183 | 24.9 | 12.9 | 21.1 | 19.4 | 13.4 | 6.8 | 1.5 | 7.85 | 21.7% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,714 | 28.4 | 15.7 | 28.3 | 13.3 | 10.7 | 3.3 | 0.3 | 5.77 | 14.3% | 3.6% |
| CHALLENGER | 4,667 | 20.7 | 12.1 | 25.6 | 17.9 | 15.9 | 6.0 | 1.7 | 8.27 | 23.7% | 7.8% |
| ITF_MEN | 8,806 | 12.1 | 8.7 | 20.3 | 17.0 | 22.2 | 14.2 | 5.5 | 12.49 | 41.9% | 19.7% |
| ITF_WOMEN | 12,555 | 11.4 | 8.4 | 18.6 | 17.4 | 24.1 | 15.1 | 5.1 | 13.28 | 44.3% | 20.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,793 | 17.4 | 13.0 | 24.9 | 21.6 | 16.3 | 6.1 | 0.6 | 8.52 | 23.1% | 6.8% |
| WTA125 | 1,217 | 16.1 | 7.0 | 22.5 | 20.1 | 20.9 | 11.9 | 1.5 | 10.7 | 34.3% | 13.4% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,714 | 26.8 | 16.1 | 26.3 | 15.5 | 11.4 | 3.4 | 0.4 | 6.0 | 15.2% | 3.8% |
| CHALLENGER | 4,667 | 18.9 | 11.2 | 23.2 | 16.5 | 18.7 | 9.4 | 2.0 | 9.07 | 30.1% | 11.4% |
| ITF_MEN | 8,807 | 9.5 | 7.3 | 17.4 | 15.8 | 21.4 | 18.9 | 9.6 | 14.99 | 50.0% | 28.5% |
| ITF_WOMEN | 12,556 | 8.8 | 6.8 | 16.0 | 14.3 | 22.7 | 20.5 | 10.9 | 16.58 | 54.1% | 31.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,793 | 14.7 | 10.3 | 22.0 | 16.2 | 22.2 | 12.6 | 1.9 | 10.93 | 36.7% | 14.5% |
| WTA125 | 1,217 | 10.2 | 7.3 | 16.5 | 15.7 | 24.3 | 17.7 | 8.3 | 15.1 | 50.3% | 26.0% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,192 | 26.0 | 19.8 | 30.5 | 12.6 | 8.2 | 2.5 | 0.4 | 5.42 | 11.0% | 2.9% |
| CHALLENGER | 3,742 | 23.9 | 15.3 | 28.4 | 14.8 | 13.1 | 4.1 | 0.4 | 6.61 | 17.6% | 4.5% |
| DOUBLES | 2,175 | 5.1 | 4.4 | 12.4 | 10.6 | 20.1 | 25.1 | 22.4 | 23.84 | 67.6% | 47.5% |
| ITF_MEN | 7,606 | 13.8 | 10.0 | 22.8 | 16.4 | 21.4 | 11.7 | 4.0 | 11.0 | 37.1% | 15.7% |
| ITF_WOMEN | 9,311 | 14.0 | 9.6 | 21.2 | 16.4 | 21.2 | 14.2 | 3.5 | 11.45 | 39.0% | 17.7% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,607 | 24.5 | 16.9 | 30.4 | 17.1 | 8.9 | 2.2 | 0.1 | 6.37 | 11.1% | 2.2% |
| WTA125 | 1,052 | 26.1 | 13.7 | 22.1 | 20.4 | 12.4 | 4.8 | 0.5 | 7.36 | 17.7% | 5.2% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,314 | 5.1 | 4.3 | 12.2 | 10.5 | 20.3 | 25.2 | 22.4 | 23.85 | 67.9% | 47.6% |
| singles | 29,254 | 16.6 | 11.3 | 22.9 | 15.6 | 18.1 | 11.2 | 4.2 | 9.77 | 33.5% | 15.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 61 | 8.2 | 8.2 | 22.9 | 9.8 | 18.0 | 21.3 | 11.5 | 15.79 | 50.8% | 32.8% |
| Clay | 8,592 | 13.0 | 9.3 | 20.0 | 15.9 | 19.4 | 13.6 | 8.8 | 12.35 | 41.8% | 22.5% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 28,574 | 13.4 | 8.7 | 18.8 | 15.3 | 19.1 | 14.8 | 9.9 | 12.85 | 43.8% | 24.6% |
| UNKNOWN | 5,902 | 10.5 | 7.6 | 17.0 | 16.4 | 21.4 | 15.9 | 11.1 | 14.28 | 48.4% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 12,357 | 19.8 | 11.9 | 22.7 | 16.1 | 14.8 | 8.9 | 5.9 | 8.71 | 29.6% | 14.8% |
| B | 5,377 | 12.9 | 8.8 | 19.4 | 16.0 | 19.7 | 12.5 | 10.8 | 12.59 | 43.0% | 23.3% |
| C | 6,137 | 11.8 | 8.8 | 19.6 | 16.1 | 18.4 | 14.6 | 10.7 | 12.88 | 43.6% | 25.2% |
| D | 6,873 | 11.8 | 8.4 | 17.6 | 15.4 | 21.6 | 15.8 | 9.3 | 13.8 | 46.8% | 25.1% |
| F | 12,622 | 7.4 | 5.5 | 15.0 | 14.6 | 23.5 | 20.9 | 13.1 | 17.71 | 57.5% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,488 | 24.5 | 16.1 | 29.1 | 14.9 | 10.7 | 3.5 | 1.2 | 6.37 | 15.3% | 4.7% |
| B | 4,469 | 16.7 | 10.8 | 23.9 | 17.0 | 18.9 | 9.7 | 3.1 | 9.72 | 31.7% | 12.8% |
| C | 6,194 | 11.3 | 7.7 | 19.2 | 14.5 | 20.9 | 15.8 | 10.5 | 13.68 | 47.2% | 26.3% |
| D | 4,650 | 14.4 | 9.7 | 21.5 | 15.6 | 20.1 | 13.3 | 5.3 | 11.27 | 38.8% | 18.6% |
| F | 7,767 | 10.1 | 8.3 | 16.2 | 14.7 | 23.1 | 19.8 | 7.8 | 15.37 | 50.7% | 27.6% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 14,008 | 18.1 | 10.9 | 21.8 | 15.9 | 15.2 | 9.7 | 8.5 | 9.79 | 33.4% | 18.2% |
| LIMITED | 9,473 | 13.6 | 9.9 | 20.2 | 16.3 | 19.2 | 13.3 | 7.6 | 11.82 | 40.1% | 20.8% |
| POOR | 19,885 | 9.0 | 6.6 | 16.0 | 14.9 | 22.8 | 18.9 | 11.8 | 16.15 | 53.5% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,457 | 23.9 | 17.7 | 33.1 | 15.8 | 6.4 | 2.7 | 0.4 | 5.92 | 9.5% | 3.1% |
| GAME_SPREAD | 6,394 | 22.3 | 15.1 | 32.5 | 17.1 | 9.0 | 3.4 | 0.6 | 6.76 | 13.0% | 4.0% |
| MATCH_WINNER | 31,568 | 15.8 | 10.8 | 22.1 | 15.2 | 18.3 | 12.2 | 5.5 | 10.29 | 36.1% | 17.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 15,556 | 27.8 | 16.7 | 30.5 | 12.8 | 9.4 | 2.5 | 0.3 | 5.65 | 12.2% | 2.8% |
| TOTAL_GAMES | 10,652 | 9.9 | 10.8 | 35.3 | 26.2 | 10.6 | 4.2 | 3.0 | 9.25 | 17.8% | 7.3% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,631 | 24.5 | 28.9 | 33.3 | 8.2 | 4.0 | 0.9 | 0.3 | 4.79 | 5.2% | 1.2% |
| GAME_SPREAD | 8,866 | 46.7 | 16.2 | 24.9 | 7.5 | 2.3 | 1.8 | 0.6 | 3.31 | 4.7% | 2.5% |
| TOTAL_GAMES | 15,855 | 6.6 | 9.7 | 40.2 | 30.4 | 7.5 | 3.4 | 2.4 | 9.25 | 13.2% | 5.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,659 | 24.0 | 16.6 | 34.9 | 14.7 | 6.9 | 2.5 | 0.5 | 6.05 | 9.9% | 3.0% |
| GAME_SPREAD | 8,871 | 20.3 | 13.6 | 28.2 | 20.2 | 12.1 | 4.5 | 1.1 | 7.7 | 17.7% | 5.7% |
| TOTAL_GAMES | 15,893 | 9.9 | 10.6 | 36.2 | 24.6 | 11.6 | 4.4 | 2.7 | 9.13 | 18.7% | 7.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 43,366 | 44.1% | 24.5% | 12.95 | 35.4% | 15.2% | 10.71 |
| gen1_elo | 43,366 | 43.8% | 24.3% | 12.73 | 35.0% | 15.1% | 10.49 |
| gen1_sr | 43,366 | 51.7% | 31.1% | 15.7 | 43.9% | 21.7% | 12.96 |
| gen2 | 43,366 | 50.7% | 31.4% | 15.36 | 43.9% | 23.3% | 12.83 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 19,548 | 15.6 | 10.4 | 21.4 | 17.4 | 20.1 | 11.8 | 3.4 | 10.71 | 35.3% | 15.2% |
| STALE | 23,818 | 10.8 | 7.2 | 16.7 | 14.1 | 19.1 | 17.1 | 15.1 | 15.51 | 51.3% | 32.2% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 25,036 | 16.5 | 11.2 | 22.8 | 15.3 | 17.7 | 11.7 | 4.8 | 9.89 | 34.3% | 16.6% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 74,934 | 25036 | 23020 | 26878 | 24.6 | 117.6 | 1451.1 |
| ge_15pp | 30,492 | 8585 | 8187 | 13720 | 27.8 | 429.9 | 1451.1 |
| ge_25pp | 16,251 | 4150 | 3566 | 8535 | 32.1 | 582.4 | 1431.1 |
| lt_10pp | 32,908 | 12619 | 10891 | 9398 | 22.7 | 47.1 | 1421.1 |

Current slate `SL-20261103T111554Z-672f3ff4`: 616 priced rows, quote age at build {'median': 12.4, 'max': 12.5}, freshness {'AGING': 616}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 49 | 0.0 | 0.0 | 36.7 | 6.1 | 32.6 | 20.4 | 4.1 | 18.34 | 57.1% | 24.5% |
| EXTERNAL_LONE_OUTLIER | 26 | 65.4 | 34.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.37 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,273 | 19.4 | 10.8 | 25.5 | 18.1 | 17.9 | 7.3 | 1.0 | 8.75 | 26.2% | 8.3% |
| KALSHI_LONE_OUTLIER | 27 | 3.7 | 3.7 | 77.8 | 7.4 | 3.7 | 3.7 | 0.0 | 6.42 | 7.4% | 3.7% |
| MARKETS_AGREE | 872 | 66.4 | 33.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.2 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,916 | 0.0 | 2.4 | 37.0 | 26.3 | 24.2 | 9.4 | 0.8 | 11.86 | 34.4% | 10.2% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 43,366 | 7163 (16.5%) | 26.8% | 1.1% | {"EXTERNAL_STALE": 4273, "AGREES_WITH_KALSHI": 1916, "ALL_AGREE": 872, "SUPPORTS_MODEL_DIRECTION": 48, "AGREES_WITH_MODEL": 27, "EXTERNAL_OUTLIER": 26, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 19,108 | 1809 (9.5%) | 36.4% | 1.7% | {"EXTERNAL_STALE": 1120, "AGREES_WITH_KALSHI": 659, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 10,639 | 562 (5.3%) | 34.9% | 2.3% | {"EXTERNAL_STALE": 353, "AGREES_WITH_KALSHI": 196, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,123 | 534 (10.4%) | 35.4% | 2.4% | {"EXTERNAL_STALE": 332, "AGREES_WITH_KALSHI": 189, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 17,520 | 4073 (23.2%) | 18.5% | 1.0% | {"EXTERNAL_STALE": 2381, "ALL_AGREE": 872, "AGREES_WITH_KALSHI": 753, "EXTERNAL_OUTLIER": 26, "AGREES_WITH_MODEL": 23, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 8,403 | 10.4 | 7.6 | 19.5 | 14.7 | 21.7 | 16.2 | 9.9 | 14.09 | 47.8% | 26.1% |
| 4-10x | 5,799 | 11.1 | 8.6 | 18.5 | 15.3 | 22.1 | 14.3 | 10.1 | 13.76 | 46.5% | 24.3% |
| <2x | 22,285 | 15.1 | 9.8 | 19.8 | 16.2 | 17.4 | 12.9 | 8.7 | 11.47 | 39.0% | 21.7% |
| >=10x | 6,879 | 10.5 | 6.4 | 15.0 | 14.5 | 21.7 | 19.0 | 12.9 | 16.36 | 53.7% | 32.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 11,282 | 12.6 | 8.7 | 19.8 | 16.4 | 19.1 | 13.3 | 10.2 | 12.66 | 42.6% | 23.5% |
| 300-1000 | 9,313 | 11.9 | 8.8 | 17.7 | 15.4 | 20.4 | 16.3 | 9.5 | 13.58 | 46.1% | 25.7% |
| <300 | 13,677 | 8.3 | 5.8 | 15.1 | 14.7 | 23.2 | 19.9 | 13.0 | 17.12 | 56.1% | 33.0% |
| >=3000 | 9,094 | 21.5 | 12.9 | 24.2 | 15.8 | 13.7 | 7.0 | 4.9 | 7.64 | 25.6% | 11.9% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1234 | 0.5503 | 0.4103 | 0.4927 | +0.058 | -0.083 | -0.0016 ± 0.0044 |
| ratio 4-10x | 857 | 0.5817 | 0.4349 | 0.4924 | +0.089 | -0.058 | 0.0085 ± 0.0055 |
| ratio <2x | 3067 | 0.5372 | 0.415 | 0.4425 | +0.095 | -0.028 | 0.013 ± 0.0026 |
| ratio >=10x | 1050 | 0.5693 | 0.3949 | 0.4505 | +0.119 | -0.056 | 0.0146 ± 0.0056 |
| thinner_sample 1000-3000 | 1718 | 0.5391 | 0.4124 | 0.4523 | +0.087 | -0.040 | 0.0091 ± 0.0035 |
| thinner_sample 300-1000 | 1401 | 0.568 | 0.4259 | 0.4825 | +0.086 | -0.057 | 0.0037 ± 0.0042 |
| thinner_sample <300 | 2029 | 0.561 | 0.3927 | 0.4584 | +0.103 | -0.066 | 0.0116 ± 0.004 |
| thinner_sample >=3000 | 1060 | 0.5308 | 0.438 | 0.45 | +0.081 | -0.012 | 0.0152 ± 0.0035 |
| data_status ADEQUATE | 1726 | 0.5331 | 0.4308 | 0.4432 | +0.090 | -0.013 | 0.0139 ± 0.0029 |
| data_status LIMITED | 1523 | 0.5485 | 0.4158 | 0.4701 | +0.078 | -0.054 | 0.007 ± 0.0038 |
| data_status POOR | 2959 | 0.5635 | 0.402 | 0.466 | +0.098 | -0.064 | 0.0088 ± 0.0032 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 910 | 0.1997 | 0.2001 | -0.0004 ± 0.0005 | 0.5797 | 0.5808 | 0.5031 | 0.4879 | 0.5044 | -0.091 ± 0.0157 | -0.0087 (8) |
| 3-5 | 564 | 0.2066 | 0.2059 | +0.0007 ± 0.0015 | 0.5966 | 0.5931 | 0.5039 | 0.464 | 0.4752 | -0.107 ± 0.0196 | 0.01 (2) |
| 5-10 | 1321 | 0.2012 | 0.2009 | +0.0003 ± 0.0018 | 0.5882 | 0.5853 | 0.5122 | 0.4385 | 0.4709 | -0.090 ± 0.0128 | -0.0143 (7) |
| 10-15 | 1078 | 0.2183 | 0.209 | +0.0093 ± 0.0035 | 0.6287 | 0.6021 | 0.5272 | 0.4036 | 0.4267 | -0.108 ± 0.0141 | -0.048 (5) |
| 15-25 | 1376 | 0.2253 | 0.2096 | +0.0156 ± 0.0048 | 0.6458 | 0.6028 | 0.5762 | 0.381 | 0.439 | -0.104 ± 0.0123 | -0.004 (10) |
| 25-40 | 791 | 0.2196 | 0.2064 | +0.0131 ± 0.0096 | 0.6278 | 0.5946 | 0.6565 | 0.3466 | 0.4804 | -0.070 ± 0.0147 | -0.06 (2) |
| 40+ | 168 | 0.2896 | 0.181 | +0.1086 ± 0.0291 | 0.784 | 0.5376 | 0.7371 | 0.2849 | 0.3988 | -0.080 ± 0.0283 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4865 | 0.185 | 0.1858 | -0.0008 ± 0.0002 | 0.5456 | 0.5464 | 0.4875 | 0.4723 | 0.5007 | -0.025 ± 0.0063 | -0.01 (28) |
| 3-5 | 3253 | 0.1949 | 0.1928 | +0.0022 ± 0.0006 | 0.5686 | 0.561 | 0.4825 | 0.4427 | 0.4344 | -0.063 ± 0.0078 | 0.0 (3) |
| 5-10 | 7034 | 0.2007 | 0.1973 | +0.0034 ± 0.0008 | 0.5869 | 0.5753 | 0.4848 | 0.4112 | 0.4249 | -0.046 ± 0.0054 | -0.0114 (22) |
| 10-15 | 5796 | 0.201 | 0.1851 | +0.0158 ± 0.0014 | 0.5879 | 0.5443 | 0.4845 | 0.3606 | 0.3582 | -0.065 ± 0.0057 | -0.0281 (16) |
| 15-25 | 7258 | 0.2068 | 0.1677 | +0.0391 ± 0.0019 | 0.6059 | 0.4978 | 0.4998 | 0.3041 | 0.3031 | -0.070 ± 0.0048 | -0.0027 (45) |
| 25-40 | 5645 | 0.221 | 0.1254 | +0.0955 ± 0.003 | 0.6359 | 0.3858 | 0.5261 | 0.2121 | 0.2213 | -0.058 ± 0.0046 | -0.0733 (3) |
| 40+ | 3742 | 0.3837 | 0.0447 | +0.3390 ± 0.0039 | 0.9995 | 0.1732 | 0.6329 | 0.1042 | 0.0601 | -0.078 ± 0.0033 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 724 | 0.2075 | 0.2081 | -0.0006 ± 0.0006 | 0.5973 | 0.599 | 0.5059 | 0.4911 | 0.5235 | -0.097 ± 0.0183 | -0.0117 (6) |
| 3-5 | 514 | 0.2141 | 0.2113 | +0.0028 ± 0.0016 | 0.6101 | 0.6046 | 0.5141 | 0.4744 | 0.4553 | -0.131 ± 0.0218 | 0.01 (2) |
| 5-10 | 1144 | 0.2064 | 0.204 | +0.0024 ± 0.002 | 0.5992 | 0.5922 | 0.5424 | 0.4678 | 0.4921 | -0.097 ± 0.0138 | -0.01 (4) |
| 10-15 | 996 | 0.2149 | 0.2097 | +0.0052 ± 0.0036 | 0.6207 | 0.6062 | 0.5664 | 0.4421 | 0.4869 | -0.099 ± 0.0151 | -0.04 (5) |
| 15-25 | 1443 | 0.2303 | 0.2122 | +0.0181 ± 0.0047 | 0.6552 | 0.6086 | 0.5834 | 0.3882 | 0.4421 | -0.100 ± 0.0123 | -0.012 (10) |
| 25-40 | 1014 | 0.2684 | 0.1983 | +0.0701 ± 0.0088 | 0.7489 | 0.5772 | 0.6604 | 0.3466 | 0.3945 | -0.128 ± 0.014 | -0.008 (5) |
| 40+ | 373 | 0.3675 | 0.1633 | +0.2042 ± 0.0209 | 1.0028 | 0.4932 | 0.733 | 0.246 | 0.2949 | -0.085 ± 0.0201 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4178 | 0.1913 | 0.1915 | -0.0002 ± 0.0002 | 0.5583 | 0.5586 | 0.5077 | 0.4927 | 0.5098 | -0.039 ± 0.007 | -0.0154 (26) |
| 3-5 | 2876 | 0.1931 | 0.1919 | +0.0012 ± 0.0007 | 0.5622 | 0.5584 | 0.5104 | 0.4707 | 0.4743 | -0.048 ± 0.0084 | 0.01 (2) |
| 5-10 | 6239 | 0.1977 | 0.1939 | +0.0038 ± 0.0008 | 0.5803 | 0.5669 | 0.5088 | 0.4348 | 0.449 | -0.044 ± 0.0056 | -0.0117 (6) |
| 10-15 | 5200 | 0.2029 | 0.1919 | +0.0110 ± 0.0015 | 0.5948 | 0.5614 | 0.5132 | 0.3894 | 0.4079 | -0.048 ± 0.0062 | -0.0189 (18) |
| 15-25 | 7259 | 0.217 | 0.1805 | +0.0365 ± 0.002 | 0.6311 | 0.5299 | 0.5226 | 0.3274 | 0.3346 | -0.063 ± 0.005 | -0.0084 (43) |
| 25-40 | 6631 | 0.2509 | 0.1365 | +0.1144 ± 0.0029 | 0.7081 | 0.4176 | 0.5582 | 0.2415 | 0.2229 | -0.083 ± 0.0045 | -0.0095 (20) |
| 40+ | 5210 | 0.4008 | 0.0588 | +0.3420 ± 0.0039 | 1.057 | 0.2122 | 0.6542 | 0.1186 | 0.081 | -0.074 ± 0.0033 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 867 | 0.1959 | 0.1977 | -0.0018 ± 0.0005 | 0.5711 | 0.5756 | 0.5033 | 0.4879 | 0.5409 | -0.044 ± 0.0158 | -0.012 (10) |
| 3-5 | 608 | 0.2075 | 0.2055 | +0.0020 ± 0.0015 | 0.6002 | 0.5932 | 0.4983 | 0.4587 | 0.4556 | -0.121 ± 0.0191 | -0.0 (4) |
| 5-10 | 1363 | 0.2027 | 0.1999 | +0.0029 ± 0.0018 | 0.5907 | 0.582 | 0.5112 | 0.4374 | 0.4534 | -0.103 ± 0.0125 | -0.01 (9) |
| 10-15 | 1079 | 0.2089 | 0.2024 | +0.0066 ± 0.0034 | 0.6075 | 0.5876 | 0.5412 | 0.418 | 0.4541 | -0.102 ± 0.0137 | -0.0286 (7) |
| 15-25 | 1309 | 0.2332 | 0.2147 | +0.0185 ± 0.005 | 0.6647 | 0.6137 | 0.5887 | 0.3944 | 0.4439 | -0.114 ± 0.0128 | -0.03 (1) |
| 25-40 | 805 | 0.21 | 0.2116 | -0.0016 ± 0.0095 | 0.6073 | 0.6068 | 0.6641 | 0.3536 | 0.5093 | -0.056 ± 0.0145 | -0.0267 (3) |
| 40+ | 177 | 0.3056 | 0.1886 | +0.1170 ± 0.0291 | 0.8288 | 0.5552 | 0.7472 | 0.2944 | 0.4011 | -0.086 ± 0.03 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4658 | 0.1838 | 0.1844 | -0.0006 ± 0.0002 | 0.5418 | 0.5427 | 0.4832 | 0.4679 | 0.4871 | -0.032 ± 0.0064 | -0.0137 (41) |
| 3-5 | 3299 | 0.2008 | 0.1986 | +0.0022 ± 0.0006 | 0.5849 | 0.5775 | 0.481 | 0.4415 | 0.4347 | -0.062 ± 0.0079 | -0.01 (19) |
| 5-10 | 7161 | 0.1941 | 0.1897 | +0.0044 ± 0.0008 | 0.571 | 0.5565 | 0.4868 | 0.4128 | 0.4201 | -0.051 ± 0.0052 | -0.0105 (37) |
| 10-15 | 5745 | 0.1923 | 0.1785 | +0.0138 ± 0.0014 | 0.5689 | 0.5288 | 0.4954 | 0.3721 | 0.377 | -0.058 ± 0.0056 | -0.0146 (13) |
| 15-25 | 7377 | 0.213 | 0.1732 | +0.0398 ± 0.0019 | 0.6202 | 0.51 | 0.5137 | 0.3192 | 0.3154 | -0.073 ± 0.0048 | -0.0533 (3) |
| 25-40 | 5656 | 0.2161 | 0.1279 | +0.0881 ± 0.003 | 0.6251 | 0.3916 | 0.5296 | 0.2139 | 0.2343 | -0.048 ± 0.0046 | -0.02 (4) |
| 40+ | 3697 | 0.3935 | 0.0503 | +0.3432 ± 0.0042 | 1.0258 | 0.1873 | 0.6424 | 0.1108 | 0.0671 | -0.078 ± 0.0035 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1287 | 0.1949 | 0.1949 | -0.0000 ± 0.0004 | 0.5677 | 0.5676 | 0.5061 | 0.4911 | 0.4942 | -0.071 ± 0.0126 | -0.0213 (54) |
| 3-5 | 904 | 0.1884 | 0.188 | +0.0004 ± 0.0012 | 0.553 | 0.5509 | 0.4957 | 0.4558 | 0.4701 | -0.062 ± 0.0147 | -0.0194 (34) |
| 5-10 | 1870 | 0.2012 | 0.1966 | +0.0045 ± 0.0015 | 0.5911 | 0.5765 | 0.5056 | 0.4319 | 0.4385 | -0.075 ± 0.0105 | -0.005 (78) |
| 10-15 | 1287 | 0.2167 | 0.2032 | +0.0135 ± 0.0031 | 0.626 | 0.5901 | 0.5388 | 0.416 | 0.4211 | -0.093 ± 0.0129 | 0.0014 (65) |
| 15-25 | 1654 | 0.2305 | 0.2083 | +0.0222 ± 0.0044 | 0.6576 | 0.6008 | 0.5866 | 0.3918 | 0.4353 | -0.087 ± 0.0114 | -0.0214 (59) |
| 25-40 | 1028 | 0.2413 | 0.211 | +0.0303 ± 0.0088 | 0.6898 | 0.6049 | 0.6883 | 0.376 | 0.4835 | -0.091 ± 0.0134 | -0.0252 (27) |
| 40+ | 357 | 0.327 | 0.2027 | +0.1242 ± 0.0229 | 0.9477 | 0.5899 | 0.8203 | 0.3432 | 0.4678 | -0.099 ± 0.0212 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4817 | 0.1751 | 0.1753 | -0.0002 ± 0.0002 | 0.519 | 0.5191 | 0.5116 | 0.4964 | 0.5088 | -0.037 ± 0.0061 | -0.0145 (98) |
| 3-5 | 3314 | 0.1941 | 0.193 | +0.0011 ± 0.0006 | 0.566 | 0.5634 | 0.5017 | 0.4619 | 0.468 | -0.045 ± 0.0077 | -0.0204 (72) |
| 5-10 | 6747 | 0.1976 | 0.1911 | +0.0065 ± 0.0008 | 0.5813 | 0.5623 | 0.5009 | 0.4272 | 0.4214 | -0.063 ± 0.0054 | -0.0084 (134) |
| 10-15 | 4665 | 0.2109 | 0.1949 | +0.0160 ± 0.0016 | 0.6125 | 0.5711 | 0.5376 | 0.4147 | 0.4099 | -0.071 ± 0.0065 | -0.0053 (106) |
| 15-25 | 5609 | 0.2301 | 0.2 | +0.0301 ± 0.0024 | 0.6615 | 0.5793 | 0.573 | 0.3775 | 0.3999 | -0.065 ± 0.006 | -0.026 (108) |
| 25-40 | 3764 | 0.2584 | 0.1893 | +0.0691 ± 0.0045 | 0.7315 | 0.5518 | 0.6385 | 0.3259 | 0.3741 | -0.072 ± 0.0069 | -0.0246 (52) |
| 40+ | 1629 | 0.3726 | 0.1567 | +0.2159 ± 0.0102 | 1.0548 | 0.4668 | 0.7446 | 0.2428 | 0.2891 | -0.069 ± 0.0093 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 6208 | 1.033 ± 0.036 | 1.106 | 0.1691 | 0.1663 | 0.2145 | 0.2047 |
| gen2 | 6208 | 0.818 ± 0.032 | 1.076 | 0.1719 | 0.1667 | 0.2339 | 0.2045 |
| gen1_elo | 6208 | 1.009 ± 0.034 | 1.098 | 0.176 | 0.1664 | 0.2136 | 0.2049 |
| gen1_sr | 6208 | 1.005 ± 0.042 | 1.134 | 0.1321 | 0.1685 | 0.2299 | 0.2042 |
| gen1_ledger | 8387 | 0.866 ± 0.026 | 1.075 | 0.1886 | 0.1748 | 0.2173 | 0.2008 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 30,492)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 6,959 | 22.8% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,759 | 22.2% |
| BOOK_QUALITY | execution | 5,700 | 18.7% |
| POOR_DATA | data | 3,542 | 11.6% |
| LIMITED_DATA | data | 1,905 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,711 | 5.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,289 | 4.2% |
| IDENTITY_AMBIGUOUS | mapping | 1,249 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 858 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 519 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 22.8%, coverage 22.2%, execution 18.7%, data 17.9%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.2%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.3%, LOW_DATA_QUALITY 71.5%, THIN_PLAYER_HISTORY 60.0%, STALE_PLAYER_DATA 51.9%, STALE_KALSHI_QUOTE 45.0%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 33.0%, WIDE_SPREAD 24.9%, MODEL_HIGH_UNCERTAINTY 18.5%, PLAYER_IDENTITY_RISK 15.5%, LEVEL_TRANSFER_RISK 10.2%, LOW_DISPLAYED_LIQUIDITY 8.3%, EVENT_MAPPING_RISK 7.4%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.4%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.6%, POST_SETTLEMENT_OBSERVATION 22.2%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 16,251)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,455 | 33.6% |
| STALE_QUOTE | market_freshness | 3,146 | 19.4% |
| BOOK_QUALITY | execution | 2,965 | 18.2% |
| POOR_DATA | data | 1,532 | 9.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 901 | 5.5% |
| IDENTITY_AMBIGUOUS | mapping | 686 | 4.2% |
| LIMITED_DATA | data | 562 | 3.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 558 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 317 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 128 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.6%, market_freshness 19.4%, execution 18.2%, data 12.9%, market_freshness/coverage 9.0%, mapping 4.2%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.9%, LOW_DATA_QUALITY 75.1%, THIN_PLAYER_HISTORY 62.2%, STALE_KALSHI_QUOTE 52.5%, STALE_PLAYER_DATA 46.0%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 34.2%, WIDE_SPREAD 24.4%, MODEL_HIGH_UNCERTAINTY 19.1%, PLAYER_IDENTITY_RISK 18.5%, EVENT_MAPPING_RISK 9.1%, LEVEL_TRANSFER_RISK 9.0%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 5.0%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.5%, POST_SETTLEMENT_OBSERVATION 33.6%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 12918, "IDENTITY_AMBIGUOUS": 3333}; ticker orientation: {"VERIFIED": 16251}.

Checks: discipline:AMBIGUOUS 1102, discipline:PASS 15149, identity_confidence:AMBIGUOUS 3009, identity_confidence:PASS 13242, level_mapping:NA 1114, level_mapping:PASS 15137, market_pair:AMBIGUOUS 484, market_pair:NA 361, market_pair:PASS 15406, model_complement:NA 324, model_complement:PASS 15927, namesake:AMBIGUOUS 6, namesake:PASS 16245, physical_match_id:NA 5612, physical_match_id:PASS 10639, player_ids:PASS 16251, same_pair_other_event:PASS 16251, ticker_orientation:PASS 16251

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,071 | 3.9% | 3.4% | 1.4% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "coverage": 19, "market_freshness/coverage": 17} | 5.63 | 0.2214 / 0.2154 (729) | 24.0% | 2.6% | 3.1% | 2.7% |
| CHALLENGER | 10,807 | 16.3% | 6.3% | 10.9% | {"coverage": 1027, "market_freshness": 208, "market_freshness/coverage": 207, "data": 154, "model_calibration_or_unknown": 76, "execution": 41, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.39 | 0.2213 / 0.2102 (2480) | 36.8% | 15.9% | 4.2% | 22.2% |
| DOUBLES | 2,314 | 47.6% | 47.5% | 6.8% | {"execution": 631, "mapping": 297, "market_freshness": 106, "market_freshness/coverage": 61, "coverage": 7} | 23.84 | 0.3052 / 0.2386 (549) | 10.1% | 0.0% | 100.0% | 6.0% |
| ITF_MEN | 20,845 | 25.1% | 17.9% | 32.2% | {"coverage": 1812, "market_freshness": 1003, "execution": 946, "data": 781, "market_freshness/coverage": 497, "mapping": 193, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.79 | 0.217 / 0.1999 (4234) | 38.6% | 69.1% | 16.2% | 21.3% |
| ITF_WOMEN | 27,737 | 26.5% | 19.2% | 45.2% | {"coverage": 2538, "market_freshness": 1585, "execution": 1265, "data": 1061, "market_freshness/coverage": 622, "mapping": 173, "model_calibration_or_unknown": 83, "model_calibration": 22} | 12.55 | 0.2023 / 0.1942 (5148) | 40.1% | 57.4% | 9.8% | 21.2% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,563 | 6.0% | 5.1% | 1.7% | {"market_freshness": 101, "model_calibration_or_unknown": 50, "coverage": 37, "execution": 29, "data": 24, "model_calibration": 20, "market_freshness/coverage": 13, "mapping": 1} | 7.69 | 0.2287 / 0.2219 (703) | 29.0% | 2.0% | 1.4% | 3.6% |
| WTA125 | 2,442 | 11.2% | 9.6% | 1.7% | {"market_freshness": 84, "model_calibration_or_unknown": 51, "market_freshness/coverage": 41, "data": 38, "execution": 24, "model_calibration": 17, "coverage": 14, "mapping": 4} | 9.3 | 0.2098 / 0.1927 (710) | 28.1% | 11.0% | 4.4% | 7.1% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 286 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 3 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 4 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 5 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 6 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 7 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 8 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 572 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 9 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 10 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 21.3h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 1282 min (STALE); no external reference |
| 13 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 14 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 15.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 928 min (STALE); no external reference |
| 17 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 18 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 19 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 20 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 21 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 22 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 23 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 24 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 25 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 26 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 27 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 28 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 29 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 30 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 31 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 32 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 33 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 34 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 35 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 36 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 37 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 38 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 39 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 40 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 41 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 42 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 43 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 44 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 124 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 45 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 46 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.3h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 748 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |
| 47 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXATPCHALLENGERMATCH-26NOV02TOBSTO-TOB` | CHALLENGER | fair_v1 | 80% / 2% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 165 min (STALE); data POOR (grade F, thinner serve sample 159.0, ratio 20.58); no external reference |
| 49 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 50 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9686, "by_level_share_of_ge_25pp": {"ATP": 0.0144, "CHALLENGER": 0.1087, "DOUBLES": 0.0678, "ITF_MEN": 0.3224, "ITF_WOMEN": 0.4522, "OTHER": 0.0007, "WTA": 0.0169, "WTA125": 0.0168}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5252, "share_primary_cause_market_settled_or_in_play": 0.4254, "share_primary_cause_stale_quote_only": 0.1936}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 16251, "identity_ambiguous_share": 0.2051, "ticker_orientation": {"VERIFIED": 16251}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 10639, "with_external": 562, "coverage": 0.0528, "external_status": {"EXTERNAL_STALE": 353, "AGREES_WITH_KALSHI": 196, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 353, "MODEL_LONE_OUTLIER": 196, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3488, "share_external_supports_model": 0.0231}, "pregame_clean_ge_25pp": {"n": 5123, "with_external": 534, "coverage": 0.1042, "external_status": {"EXTERNAL_STALE": 332, "AGREES_WITH_KALSHI": 189, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 332, "MODEL_LONE_OUTLIER": 189, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3539, "share_external_supports_model": 0.0243}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 479.0, "median_sample_ratio": 2.47, "median_min_matches": 19.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2074, "data_status": {"POOR": 9157, "LIMITED": 4234, "ADEQUATE": 2860}, "comparison_lt_10pp": {"median_thinner_serve_points": 1746.0, "median_sample_ratio": 1.69, "median_min_matches": 91.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1234, "model_minus_observed": 0.0576, "kalshi_minus_observed": -0.0825, "brier_diff_model_minus_kalshi": -0.0016}, "4-10x": {"n": 857, "model_minus_observed": 0.0893, "kalshi_minus_observed": -0.0575, "brier_diff_model_minus_kalshi": 0.0085}, "<2x": {"n": 3067, "model_minus_observed": 0.0947, "kalshi_minus_observed": -0.0275, "brier_diff_model_minus_kalshi": 0.013}, ">=10x": {"n": 1050, "model_minus_observed": 0.1189, "kalshi_minus_observed": -0.0556, "brier_diff_model_minus_kalshi": 0.0146}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 6208, "model": {"intercept": -0.544, "slope": 0.818, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.19, "slope": 1.076, "slope_se": 0.036}, "mean_extremity_model": 0.1719, "mean_extremity_kalshi": 0.1667, "model_brier": 0.2339, "kalshi_brier": 0.2045, "brier_diff_model_minus_kalshi": 0.0293, "brier_diff_se": 0.0024, "model_logloss": 0.665, "kalshi_logloss": 0.5917}, "fair_v1": {"n": 6208, "model": {"intercept": -0.438, "slope": 1.033, "slope_se": 0.036}, "kalshi_mid_same_rows": {"intercept": 0.264, "slope": 1.106, "slope_se": 0.037}, "mean_extremity_model": 0.1691, "mean_extremity_kalshi": 0.1663, "model_brier": 0.2145, "kalshi_brier": 0.2047, "brier_diff_model_minus_kalshi": 0.0098, "brier_diff_se": 0.002, "model_logloss": 0.6178, "kalshi_logloss": 0.592}, "gen1_elo": {"n": 6208, "model": {"intercept": -0.421, "slope": 1.009, "slope_se": 0.034}, "kalshi_mid_same_rows": {"intercept": 0.274, "slope": 1.098, "slope_se": 0.036}, "mean_extremity_model": 0.176, "mean_extremity_kalshi": 0.1664, "model_brier": 0.2136, "kalshi_brier": 0.2049, "brier_diff_model_minus_kalshi": 0.0087, "brier_diff_se": 0.002, "model_logloss": 0.6164, "kalshi_logloss": 0.5923}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2453, "share_ge_15": 0.4406, "median_abs_gap": 12.95, "n": 43366}, "gen1_elo": {"share_ge_25": 0.243, "share_ge_15": 0.4377, "median_abs_gap": 12.73, "n": 43366}, "gen1_sr": {"share_ge_25": 0.3111, "share_ge_15": 0.5173, "median_abs_gap": 15.7, "n": 43366}, "gen2": {"share_ge_25": 0.3135, "share_ge_15": 0.5075, "median_abs_gap": 15.36, "n": 43366}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1517, "share_ge_15": 0.354, "median_abs_gap": 10.71, "n": 33758}, "gen1_elo": {"share_ge_25": 0.1509, "share_ge_15": 0.3499, "median_abs_gap": 10.49, "n": 33757}, "gen1_sr": {"share_ge_25": 0.2171, "share_ge_15": 0.4388, "median_abs_gap": 12.96, "n": 33760}, "gen2": {"share_ge_25": 0.2326, "share_ge_15": 0.4386, "median_abs_gap": 12.83, "n": 33760}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.63, "share_ge_25_all": 0.0385, "share_ge_25_pregame_clean": 0.0335}, "WTA": {"median_abs_gap_pregame_clean": 7.69, "share_ge_25_all": 0.0603, "share_ge_25_pregame_clean": 0.0511}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2372, "share_within_10pp_all": 0.4392, "share_within_10pp_pregame_clean": 0.4908, "corr_model_vs_mid_pregame_clean": 0.8494}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 910, "model_brier": 0.1997, "kalshi_brier": 0.2001, "brier_diff_model_minus_kalshi": -0.0004}, "10-15": {"n_settled": 1078, "model_brier": 0.2183, "kalshi_brier": 0.209, "brier_diff_model_minus_kalshi": 0.0093}, "15-25": {"n_settled": 1376, "model_brier": 0.2253, "kalshi_brier": 0.2096, "brier_diff_model_minus_kalshi": 0.0156}, "25-40": {"n_settled": 791, "model_brier": 0.2196, "kalshi_brier": 0.2064, "brier_diff_model_minus_kalshi": 0.0131}, "3-5": {"n_settled": 564, "model_brier": 0.2066, "kalshi_brier": 0.2059, "brier_diff_model_minus_kalshi": 0.0007}, "40+": {"n_settled": 168, "model_brier": 0.2896, "kalshi_brier": 0.181, "brier_diff_model_minus_kalshi": 0.1086}, "5-10": {"n_settled": 1321, "model_brier": 0.2012, "kalshi_brier": 0.2009, "brier_diff_model_minus_kalshi": 0.0003}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.544, "slope": 0.818, "slope_se": 0.032}, "kalshi_slope": {"intercept": 0.19, "slope": 1.076, "slope_se": 0.036}, "n": 6208}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.489, "slope": 0.866, "slope_se": 0.026}, "kalshi_slope": {"intercept": 0.172, "slope": 1.075, "slope_se": 0.03}, "n": 8387}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 549, "model_brier": 0.3052, "kalshi_brier": 0.2386, "brier_diff_model_minus_kalshi": 0.0666, "brier_diff_se": 0.0128, "corr_model_outcome": 0.0665, "corr_kalshi_outcome": 0.2318}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
