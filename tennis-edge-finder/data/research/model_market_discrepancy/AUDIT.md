# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-08T15:42Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 82,206): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 19.1%, 25-40 13.6%, 40+ 8.1%; median gap 11.84 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.8%, Challenger 10.8%, doubles 6.7%). Main tour: ATP 3.8% and WTA 6.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 17,849): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.3%, STALE_QUOTE 19.4%, BOOK_QUALITY 17.4%, POOR_DATA 9.1%, POSSIBLY_IN_PLAY_QUOTE 5.8%, IDENTITY_AMBIGUOUS 4.4%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.3%, market_freshness 19.4%, execution 17.4%, data 12.6%, market_freshness/coverage 9.3%, mapping 4.4%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 53.7% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.6% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 17,849 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.6% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 494.0 points vs 1734.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.028, Gen-2 0.82, Gen-1 ledger 0.866 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 914 model 0.222 vs Kalshi 0.2058; n 189 model 0.295 vs Kalshi 0.1767.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 348,389 model-market comparisons (570,842 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 116,174 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-08T15:27:01.081416+00:00'], shadow board 94,408 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-08T15:27:04.128419+00:00'], Model 4 42,838 rows, 29,056 settled tickers, 10,902 tickers with an external scan.
* By model: {"gen1_ledger": 78295, "gen1_elo": 47449, "fair_v1": 47449, "gen2": 47449, "gen1_sr": 47449, "model4_fundamental": 40191, "model4_conditioned": 40107}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 82,206 | 14.1 | 9.6 | 20.2 | 15.3 | 19.1 | 13.6 | 8.1 | 11.84 | 40.9% | 21.7% |
| MW fair_v1 | 47,449 | 12.8 | 8.7 | 18.7 | 15.4 | 19.6 | 14.8 | 10.0 | 13.05 | 44.4% | 24.8% |
| MW gen1_elo | 47,449 | 12.6 | 8.9 | 19.2 | 15.3 | 19.5 | 14.7 | 9.8 | 12.84 | 44.0% | 24.5% |
| MW gen1_ledger | 34,757 | 15.8 | 10.9 | 22.2 | 15.1 | 18.5 | 12.0 | 5.5 | 10.26 | 36.0% | 17.5% |
| MW gen1_sr | 47,449 | 10.1 | 7.3 | 16.7 | 13.9 | 20.7 | 18.7 | 12.6 | 15.83 | 52.0% | 31.3% |
| MW gen2 | 47,449 | 11.0 | 7.5 | 16.6 | 13.7 | 19.6 | 17.7 | 13.7 | 15.46 | 51.0% | 31.4% |
| all families model4_conditioned | 40,107 | 22.2 | 18.0 | 34.2 | 17.1 | 5.0 | 2.2 | 1.2 | 6.07 | 8.5% | 3.4% |
| all families model4_fundamental | 40,191 | 17.4 | 13.5 | 33.9 | 19.9 | 10.0 | 3.8 | 1.5 | 7.62 | 15.3% | 5.4% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.1%, >=15pp 40.9%, >=20pp 30.1%, >=25pp 21.7%, >=30pp 15.7%, >=40pp 8.1%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.39pp; >=10pp 45.0%, >=25pp 17.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,991 | 28.5 | 15.7 | 27.4 | 13.5 | 10.7 | 3.6 | 0.6 | 5.8 | 15.0% | 4.2% |
| CHALLENGER | 7,146 | 16.0 | 9.7 | 20.6 | 15.4 | 16.0 | 11.5 | 10.8 | 10.94 | 38.3% | 22.3% |
| ITF_MEN | 13,427 | 9.8 | 7.3 | 17.0 | 15.1 | 21.2 | 17.2 | 12.3 | 15.26 | 50.7% | 29.5% |
| ITF_WOMEN | 18,499 | 9.5 | 7.1 | 16.0 | 14.8 | 22.2 | 18.4 | 12.0 | 15.89 | 52.6% | 30.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,053 | 16.8 | 13.2 | 24.6 | 20.9 | 16.6 | 6.8 | 1.1 | 8.68 | 24.5% | 7.9% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,991 | 26.8 | 15.7 | 26.0 | 15.5 | 11.4 | 3.8 | 0.8 | 6.06 | 16.1% | 4.6% |
| CHALLENGER | 7,146 | 14.6 | 9.1 | 18.8 | 13.9 | 18.7 | 13.5 | 11.5 | 12.52 | 43.6% | 24.9% |
| ITF_MEN | 13,427 | 8.2 | 6.1 | 15.1 | 13.7 | 20.0 | 20.4 | 16.4 | 17.94 | 56.9% | 36.9% |
| ITF_WOMEN | 18,499 | 7.9 | 5.8 | 14.1 | 12.8 | 20.7 | 21.2 | 17.5 | 19.08 | 59.4% | 38.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,053 | 14.1 | 10.1 | 21.6 | 16.3 | 22.5 | 12.9 | 2.5 | 11.28 | 37.9% | 15.4% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,991 | 23.1 | 14.1 | 25.2 | 15.6 | 14.8 | 6.1 | 1.1 | 7.1 | 22.0% | 7.2% |
| CHALLENGER | 7,146 | 15.1 | 9.6 | 20.6 | 15.6 | 16.2 | 12.0 | 10.9 | 11.39 | 39.1% | 22.9% |
| ITF_MEN | 13,427 | 9.5 | 7.3 | 17.2 | 14.2 | 21.8 | 17.2 | 12.7 | 15.65 | 51.7% | 29.9% |
| ITF_WOMEN | 18,499 | 9.3 | 6.9 | 16.2 | 15.7 | 22.2 | 18.3 | 11.4 | 15.6 | 51.9% | 29.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,053 | 22.8 | 17.1 | 31.8 | 15.4 | 8.7 | 3.3 | 1.1 | 6.12 | 13.0% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,391 | 27.2 | 19.7 | 29.5 | 12.3 | 8.2 | 2.6 | 0.5 | 5.31 | 11.2% | 3.0% |
| CHALLENGER | 4,621 | 22.5 | 14.4 | 27.6 | 14.8 | 13.5 | 5.7 | 1.6 | 7.08 | 20.8% | 7.3% |
| DOUBLES | 2,583 | 4.8 | 4.6 | 12.8 | 11.0 | 20.4 | 24.4 | 22.0 | 23.31 | 66.8% | 46.4% |
| ITF_MEN | 9,942 | 12.9 | 9.6 | 21.5 | 15.6 | 21.6 | 12.9 | 5.8 | 11.76 | 40.4% | 18.7% |
| ITF_WOMEN | 12,017 | 13.4 | 9.2 | 19.9 | 15.6 | 21.5 | 14.9 | 5.5 | 12.25 | 41.8% | 20.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,798 | 23.7 | 16.1 | 31.4 | 17.0 | 8.9 | 2.6 | 0.2 | 6.54 | 11.7% | 2.8% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,870 | 28.9 | 15.8 | 27.8 | 13.4 | 10.5 | 3.2 | 0.3 | 5.65 | 14.0% | 3.5% |
| CHALLENGER | 5,051 | 20.7 | 12.0 | 25.5 | 18.2 | 16.0 | 6.1 | 1.6 | 8.28 | 23.6% | 7.6% |
| ITF_MEN | 9,784 | 12.1 | 8.7 | 20.7 | 17.3 | 22.1 | 14.0 | 5.2 | 12.37 | 41.3% | 19.3% |
| ITF_WOMEN | 13,588 | 11.4 | 8.6 | 18.9 | 17.1 | 24.1 | 15.1 | 4.8 | 13.18 | 44.1% | 19.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,939 | 17.1 | 13.2 | 24.9 | 21.3 | 16.6 | 6.3 | 0.6 | 8.5 | 23.5% | 6.9% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,870 | 27.1 | 16.1 | 26.2 | 15.4 | 11.3 | 3.4 | 0.4 | 5.96 | 15.2% | 3.8% |
| CHALLENGER | 5,051 | 18.4 | 11.4 | 23.7 | 16.3 | 19.2 | 9.3 | 1.8 | 9.02 | 30.2% | 11.1% |
| ITF_MEN | 9,785 | 9.6 | 7.2 | 17.6 | 16.0 | 21.8 | 18.7 | 9.1 | 14.88 | 49.6% | 27.7% |
| ITF_WOMEN | 13,589 | 8.9 | 6.9 | 16.1 | 14.4 | 22.6 | 20.5 | 10.6 | 16.49 | 53.7% | 31.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,939 | 14.4 | 10.2 | 21.8 | 16.5 | 22.7 | 12.6 | 1.9 | 11.09 | 37.2% | 14.5% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,328 | 27.5 | 19.9 | 29.5 | 12.5 | 7.9 | 2.4 | 0.3 | 5.27 | 10.7% | 2.8% |
| CHALLENGER | 4,087 | 23.8 | 15.3 | 28.7 | 14.9 | 12.8 | 4.0 | 0.4 | 6.61 | 17.3% | 4.5% |
| DOUBLES | 2,421 | 4.7 | 4.6 | 13.0 | 11.1 | 20.2 | 24.4 | 22.0 | 23.22 | 66.6% | 46.4% |
| ITF_MEN | 8,544 | 13.7 | 10.2 | 23.1 | 16.1 | 21.7 | 11.4 | 3.8 | 10.8 | 36.9% | 15.2% |
| ITF_WOMEN | 10,309 | 14.0 | 9.8 | 21.0 | 16.1 | 21.6 | 13.8 | 3.6 | 11.44 | 39.1% | 17.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,735 | 24.0 | 16.5 | 31.4 | 17.0 | 8.9 | 2.0 | 0.1 | 6.43 | 11.0% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,583 | 4.8 | 4.6 | 12.8 | 11.0 | 20.4 | 24.4 | 22.0 | 23.31 | 66.8% | 46.4% |
| singles | 32,174 | 16.6 | 11.4 | 23.0 | 15.5 | 18.3 | 11.0 | 4.2 | 9.72 | 33.5% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 9,792 | 12.7 | 9.1 | 19.9 | 15.6 | 19.6 | 13.9 | 9.3 | 12.61 | 42.8% | 23.2% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 30,880 | 13.4 | 8.7 | 18.7 | 15.2 | 19.2 | 14.8 | 9.9 | 12.91 | 44.0% | 24.8% |
| UNKNOWN | 6,364 | 10.5 | 7.6 | 17.1 | 16.3 | 21.5 | 15.9 | 11.1 | 14.32 | 48.5% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 13,507 | 19.5 | 11.9 | 22.3 | 15.9 | 14.9 | 9.2 | 6.3 | 8.91 | 30.3% | 15.4% |
| B | 5,802 | 12.6 | 8.6 | 19.6 | 15.6 | 19.8 | 12.9 | 10.9 | 12.79 | 43.6% | 23.8% |
| C | 6,725 | 11.9 | 8.8 | 19.5 | 15.6 | 18.7 | 14.7 | 10.8 | 13.0 | 44.1% | 25.5% |
| D | 7,685 | 11.7 | 8.3 | 17.9 | 15.3 | 21.8 | 15.7 | 9.4 | 13.9 | 46.9% | 25.1% |
| F | 13,730 | 7.4 | 5.6 | 14.8 | 14.7 | 23.5 | 20.8 | 13.1 | 17.79 | 57.4% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,363 | 24.6 | 16.1 | 29.1 | 15.0 | 10.6 | 3.4 | 1.2 | 6.36 | 15.3% | 4.7% |
| B | 4,860 | 16.6 | 10.8 | 24.3 | 16.8 | 18.9 | 9.6 | 3.0 | 9.65 | 31.5% | 12.6% |
| C | 6,839 | 11.0 | 7.8 | 19.5 | 14.6 | 21.0 | 15.7 | 10.4 | 13.67 | 47.1% | 26.1% |
| D | 5,197 | 14.5 | 10.1 | 21.4 | 15.3 | 20.9 | 12.5 | 5.3 | 11.24 | 38.7% | 17.8% |
| F | 8,498 | 10.2 | 8.3 | 16.2 | 14.6 | 23.4 | 19.4 | 7.8 | 15.36 | 50.7% | 27.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 15,242 | 17.8 | 10.9 | 21.4 | 15.8 | 15.2 | 10.1 | 8.9 | 9.99 | 34.2% | 18.9% |
| LIMITED | 10,402 | 13.6 | 9.7 | 20.4 | 15.8 | 19.5 | 13.4 | 7.6 | 11.91 | 40.5% | 21.0% |
| POOR | 21,805 | 9.0 | 6.6 | 16.0 | 14.9 | 22.8 | 18.9 | 11.8 | 16.18 | 53.5% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,941 | 23.6 | 17.9 | 33.0 | 15.6 | 6.4 | 3.0 | 0.4 | 5.92 | 9.8% | 3.4% |
| GAME_SPREAD | 6,705 | 22.9 | 15.4 | 32.0 | 16.8 | 8.9 | 3.4 | 0.7 | 6.68 | 13.0% | 4.0% |
| MATCH_WINNER | 34,757 | 15.8 | 10.9 | 22.2 | 15.1 | 18.5 | 12.0 | 5.5 | 10.26 | 36.0% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 16,570 | 28.1 | 16.8 | 30.8 | 12.7 | 9.0 | 2.4 | 0.3 | 5.61 | 11.7% | 2.7% |
| TOTAL_GAMES | 11,298 | 9.8 | 10.9 | 35.7 | 25.9 | 10.6 | 4.2 | 2.9 | 9.18 | 17.7% | 7.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,231 | 24.5 | 28.6 | 33.3 | 8.2 | 4.0 | 1.1 | 0.3 | 4.8 | 5.4% | 1.4% |
| GAME_SPREAD | 9,240 | 47.0 | 16.0 | 24.7 | 7.5 | 2.3 | 1.9 | 0.6 | 3.29 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,636 | 6.6 | 9.9 | 40.2 | 30.2 | 7.4 | 3.3 | 2.4 | 9.2 | 13.1% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,267 | 23.8 | 16.6 | 34.6 | 14.8 | 6.9 | 2.7 | 0.5 | 6.06 | 10.2% | 3.2% |
| GAME_SPREAD | 9,249 | 20.7 | 13.6 | 28.2 | 20.1 | 12.0 | 4.4 | 1.2 | 7.61 | 17.5% | 5.6% |
| TOTAL_GAMES | 16,675 | 10.0 | 10.8 | 36.3 | 24.3 | 11.5 | 4.5 | 2.6 | 9.04 | 18.5% | 7.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 47,449 | 44.4% | 24.8% | 13.05 | 35.3% | 15.0% | 10.68 |
| gen1_elo | 47,449 | 44.0% | 24.5% | 12.84 | 34.8% | 14.8% | 10.49 |
| gen1_sr | 47,449 | 52.0% | 31.3% | 15.83 | 43.9% | 21.5% | 12.98 |
| gen2 | 47,449 | 51.0% | 31.4% | 15.46 | 43.8% | 23.0% | 12.85 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,034 | 15.5 | 10.5 | 21.3 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 27,415 | 10.9 | 7.3 | 16.8 | 14.0 | 19.3 | 17.0 | 14.8 | 15.43 | 51.1% | 31.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 28,225 | 16.4 | 11.2 | 22.8 | 15.2 | 18.0 | 11.5 | 4.9 | 9.88 | 34.4% | 16.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 82,206 | 28225 | 23506 | 30475 | 24.8 | 127.9 | 1451.1 |
| ge_15pp | 33,588 | 9704 | 8373 | 15511 | 28.3 | 435.4 | 1451.1 |
| ge_25pp | 17,849 | 4617 | 3655 | 9577 | 33.5 | 581.7 | 1431.1 |
| lt_10pp | 36,059 | 14226 | 11116 | 10717 | 22.6 | 47.9 | 1421.1 |

Current slate `SL-20261108T154223Z-d9ffad87`: 249 priced rows, quote age at build {'median': 15.7, 'max': 15.7}, freshness {'AGING': 249}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 51 | 0.0 | 0.0 | 35.3 | 9.8 | 31.4 | 19.6 | 3.9 | 18.34 | 54.9% | 23.5% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,700 | 19.2 | 11.0 | 25.4 | 18.0 | 18.0 | 7.5 | 1.0 | 8.82 | 26.5% | 8.4% |
| KALSHI_LONE_OUTLIER | 30 | 6.7 | 6.7 | 73.3 | 6.7 | 3.3 | 3.3 | 0.0 | 6.16 | 6.7% | 3.3% |
| MARKETS_AGREE | 990 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,100 | 0.0 | 2.2 | 37.3 | 26.3 | 24.1 | 9.1 | 0.9 | 11.81 | 34.1% | 10.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 47,449 | 7900 (16.7%) | 26.6% | 1.0% | {"EXTERNAL_STALE": 4700, "AGREES_WITH_KALSHI": 2100, "ALL_AGREE": 990, "SUPPORTS_MODEL_DIRECTION": 49, "AGREES_WITH_MODEL": 30, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 21,085 | 1989 (9.4%) | 36.0% | 1.5% | {"EXTERNAL_STALE": 1243, "AGREES_WITH_KALSHI": 716, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 11,770 | 618 (5.2%) | 34.0% | 2.1% | {"EXTERNAL_STALE": 395, "AGREES_WITH_KALSHI": 210, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,492 | 588 (10.7%) | 34.5% | 2.2% | {"EXTERNAL_STALE": 372, "AGREES_WITH_KALSHI": 203, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 19,064 | 4505 (23.6%) | 18.4% | 0.9% | {"EXTERNAL_STALE": 2611, "ALL_AGREE": 990, "AGREES_WITH_KALSHI": 831, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 26, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 9,302 | 10.5 | 7.7 | 19.4 | 14.6 | 21.6 | 16.3 | 9.9 | 14.09 | 47.8% | 26.2% |
| 4-10x | 6,349 | 11.2 | 8.5 | 18.3 | 15.2 | 22.1 | 14.4 | 10.2 | 13.88 | 46.8% | 24.7% |
| <2x | 24,230 | 14.9 | 9.8 | 19.7 | 16.0 | 17.6 | 13.1 | 8.9 | 11.57 | 39.6% | 22.0% |
| >=10x | 7,568 | 10.3 | 6.4 | 15.0 | 14.4 | 21.7 | 18.9 | 13.2 | 16.43 | 53.8% | 32.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 12,457 | 12.4 | 8.6 | 19.8 | 16.2 | 19.1 | 13.6 | 10.4 | 12.78 | 43.1% | 24.0% |
| 300-1000 | 10,267 | 11.8 | 8.7 | 17.7 | 15.1 | 20.8 | 16.3 | 9.6 | 13.8 | 46.7% | 25.9% |
| <300 | 14,846 | 8.3 | 5.8 | 15.1 | 14.8 | 23.1 | 19.9 | 13.1 | 17.14 | 56.0% | 33.0% |
| >=3000 | 9,879 | 21.3 | 12.9 | 23.8 | 15.6 | 13.9 | 7.3 | 5.1 | 7.76 | 26.4% | 12.4% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1459 | 0.5488 | 0.4101 | 0.4873 | +0.061 | -0.077 | 0.0011 ± 0.004 |
| ratio 4-10x | 992 | 0.577 | 0.4327 | 0.4869 | +0.090 | -0.054 | 0.0087 ± 0.005 |
| ratio <2x | 3566 | 0.5363 | 0.4136 | 0.4369 | +0.099 | -0.023 | 0.0144 ± 0.0024 |
| ratio >=10x | 1222 | 0.5668 | 0.3936 | 0.4501 | +0.117 | -0.057 | 0.0137 ± 0.0051 |
| thinner_sample 1000-3000 | 2003 | 0.5398 | 0.4121 | 0.4483 | +0.091 | -0.036 | 0.0112 ± 0.0033 |
| thinner_sample 300-1000 | 1639 | 0.5643 | 0.4243 | 0.4735 | +0.091 | -0.049 | 0.0049 ± 0.0038 |
| thinner_sample <300 | 2337 | 0.5587 | 0.3911 | 0.4561 | +0.103 | -0.065 | 0.0123 ± 0.0037 |
| thinner_sample >=3000 | 1260 | 0.5288 | 0.4354 | 0.446 | +0.083 | -0.011 | 0.0149 ± 0.0032 |
| data_status ADEQUATE | 2011 | 0.5316 | 0.4287 | 0.4406 | +0.091 | -0.012 | 0.0151 ± 0.0027 |
| data_status LIMITED | 1771 | 0.5481 | 0.4154 | 0.4664 | +0.082 | -0.051 | 0.0073 ± 0.0036 |
| data_status POOR | 3457 | 0.5607 | 0.4009 | 0.4599 | +0.101 | -0.059 | 0.0101 ± 0.0029 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1048 | 0.1978 | 0.198 | -0.0002 ± 0.0005 | 0.5757 | 0.5763 | 0.5022 | 0.487 | 0.4981 | -0.095 ± 0.0145 | -0.0087 (8) |
| 3-5 | 668 | 0.2055 | 0.2054 | +0.0001 ± 0.0014 | 0.5957 | 0.5939 | 0.5049 | 0.4651 | 0.4835 | -0.095 ± 0.018 | 0.01 (3) |
| 5-10 | 1555 | 0.2025 | 0.2014 | +0.0012 ± 0.0017 | 0.5916 | 0.5865 | 0.512 | 0.4382 | 0.465 | -0.092 ± 0.0118 | -0.0143 (7) |
| 10-15 | 1256 | 0.2184 | 0.2096 | +0.0087 ± 0.0032 | 0.6286 | 0.6031 | 0.5239 | 0.4003 | 0.426 | -0.103 ± 0.0131 | -0.055 (6) |
| 15-25 | 1609 | 0.2259 | 0.2083 | +0.0176 ± 0.0044 | 0.6469 | 0.6001 | 0.576 | 0.3814 | 0.4332 | -0.104 ± 0.0114 | -0.0045 (11) |
| 25-40 | 914 | 0.222 | 0.2058 | +0.0162 ± 0.0089 | 0.6336 | 0.5926 | 0.6514 | 0.3417 | 0.4705 | -0.065 ± 0.0137 | -0.06 (2) |
| 40+ | 189 | 0.295 | 0.1767 | +0.1183 ± 0.0274 | 0.7946 | 0.5268 | 0.7316 | 0.2768 | 0.381 | -0.081 ± 0.0265 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5451 | 0.1854 | 0.1863 | -0.0009 ± 0.0002 | 0.5469 | 0.548 | 0.4903 | 0.4751 | 0.5069 | -0.020 ± 0.0059 | -0.01 (28) |
| 3-5 | 3633 | 0.1979 | 0.1962 | +0.0017 ± 0.0006 | 0.5763 | 0.5701 | 0.483 | 0.4432 | 0.4415 | -0.056 ± 0.0074 | 0.005 (6) |
| 5-10 | 7880 | 0.2013 | 0.1978 | +0.0035 ± 0.0007 | 0.5884 | 0.5766 | 0.4846 | 0.4109 | 0.4242 | -0.045 ± 0.0051 | -0.0114 (22) |
| 10-15 | 6504 | 0.2021 | 0.1862 | +0.0159 ± 0.0013 | 0.5908 | 0.5463 | 0.4856 | 0.3616 | 0.3599 | -0.064 ± 0.0054 | -0.0379 (19) |
| 15-25 | 8251 | 0.2063 | 0.167 | +0.0393 ± 0.0018 | 0.6046 | 0.4963 | 0.4997 | 0.3042 | 0.3021 | -0.070 ± 0.0045 | -0.0043 (51) |
| 25-40 | 6364 | 0.2223 | 0.126 | +0.0963 ± 0.0028 | 0.6389 | 0.3872 | 0.5265 | 0.2128 | 0.2203 | -0.058 ± 0.0043 | -0.0733 (3) |
| 40+ | 4244 | 0.383 | 0.0436 | +0.3394 ± 0.0037 | 0.9974 | 0.1697 | 0.6311 | 0.1014 | 0.0577 | -0.076 ± 0.003 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 839 | 0.2056 | 0.206 | -0.0004 ± 0.0005 | 0.592 | 0.5932 | 0.5059 | 0.4911 | 0.5149 | -0.100 ± 0.0168 | -0.0117 (6) |
| 3-5 | 596 | 0.2116 | 0.2085 | +0.0031 ± 0.0015 | 0.6063 | 0.5997 | 0.5136 | 0.4741 | 0.4513 | -0.132 ± 0.0201 | 0.01 (3) |
| 5-10 | 1340 | 0.207 | 0.2051 | +0.0019 ± 0.0019 | 0.6003 | 0.5952 | 0.5405 | 0.466 | 0.4933 | -0.088 ± 0.0128 | -0.01 (4) |
| 10-15 | 1165 | 0.2132 | 0.2072 | +0.0060 ± 0.0033 | 0.6192 | 0.6005 | 0.5626 | 0.4382 | 0.479 | -0.100 ± 0.0139 | -0.04 (5) |
| 15-25 | 1692 | 0.2321 | 0.2124 | +0.0197 ± 0.0044 | 0.6599 | 0.6093 | 0.5853 | 0.3898 | 0.4385 | -0.100 ± 0.0115 | -0.0183 (12) |
| 25-40 | 1186 | 0.2664 | 0.1988 | +0.0676 ± 0.0081 | 0.7432 | 0.5778 | 0.66 | 0.3459 | 0.3971 | -0.117 ± 0.013 | -0.008 (5) |
| 40+ | 421 | 0.3715 | 0.1626 | +0.2089 ± 0.0197 | 1.0133 | 0.4914 | 0.7364 | 0.2476 | 0.2922 | -0.087 ± 0.0189 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4670 | 0.1921 | 0.1923 | -0.0002 ± 0.0002 | 0.56 | 0.5601 | 0.5074 | 0.4923 | 0.5081 | -0.039 ± 0.0066 | -0.0154 (26) |
| 3-5 | 3185 | 0.1927 | 0.1916 | +0.0012 ± 0.0006 | 0.5622 | 0.5585 | 0.5114 | 0.4718 | 0.476 | -0.047 ± 0.008 | 0.01 (5) |
| 5-10 | 7039 | 0.1969 | 0.1935 | +0.0034 ± 0.0008 | 0.5787 | 0.5663 | 0.5088 | 0.4347 | 0.4513 | -0.040 ± 0.0053 | -0.0117 (6) |
| 10-15 | 5835 | 0.2029 | 0.1917 | +0.0112 ± 0.0014 | 0.5952 | 0.5604 | 0.5104 | 0.3865 | 0.4041 | -0.047 ± 0.0058 | -0.0189 (18) |
| 15-25 | 8296 | 0.2171 | 0.1814 | +0.0358 ± 0.0018 | 0.6313 | 0.5319 | 0.5256 | 0.33 | 0.3388 | -0.060 ± 0.0047 | -0.014 (52) |
| 25-40 | 7464 | 0.2508 | 0.1377 | +0.1130 ± 0.0027 | 0.7084 | 0.4206 | 0.5603 | 0.2434 | 0.2271 | -0.079 ± 0.0043 | -0.0095 (20) |
| 40+ | 5838 | 0.4017 | 0.058 | +0.3436 ± 0.0036 | 1.0586 | 0.21 | 0.6542 | 0.1181 | 0.0791 | -0.074 ± 0.0031 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1018 | 0.1957 | 0.1971 | -0.0014 ± 0.0005 | 0.5712 | 0.5746 | 0.5025 | 0.4872 | 0.5314 | -0.052 ± 0.0145 | -0.0191 (11) |
| 3-5 | 722 | 0.2077 | 0.2062 | +0.0015 ± 0.0014 | 0.602 | 0.5966 | 0.4992 | 0.4597 | 0.4626 | -0.110 ± 0.0177 | 0.002 (5) |
| 5-10 | 1588 | 0.203 | 0.1995 | +0.0035 ± 0.0017 | 0.5913 | 0.5813 | 0.5127 | 0.4389 | 0.4509 | -0.104 ± 0.0116 | -0.01 (10) |
| 10-15 | 1272 | 0.2118 | 0.2032 | +0.0086 ± 0.0031 | 0.6142 | 0.5891 | 0.5372 | 0.4139 | 0.4426 | -0.105 ± 0.0127 | -0.0286 (7) |
| 15-25 | 1539 | 0.2312 | 0.2129 | +0.0183 ± 0.0046 | 0.66 | 0.6102 | 0.5866 | 0.3925 | 0.4418 | -0.107 ± 0.0118 | -0.03 (1) |
| 25-40 | 902 | 0.2118 | 0.21 | +0.0019 ± 0.009 | 0.6122 | 0.6023 | 0.6591 | 0.3483 | 0.4989 | -0.053 ± 0.0138 | -0.0267 (3) |
| 40+ | 198 | 0.3082 | 0.1841 | +0.1242 ± 0.0273 | 0.8344 | 0.5426 | 0.7433 | 0.2886 | 0.3889 | -0.085 ± 0.028 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5245 | 0.1853 | 0.186 | -0.0007 ± 0.0002 | 0.5462 | 0.5471 | 0.486 | 0.4707 | 0.4902 | -0.032 ± 0.006 | -0.0189 (44) |
| 3-5 | 3756 | 0.2038 | 0.2021 | +0.0017 ± 0.0006 | 0.5927 | 0.5867 | 0.4803 | 0.4408 | 0.4393 | -0.056 ± 0.0075 | -0.0073 (22) |
| 5-10 | 8027 | 0.1959 | 0.1907 | +0.0053 ± 0.0007 | 0.5752 | 0.5587 | 0.4874 | 0.4134 | 0.4148 | -0.056 ± 0.0049 | -0.0117 (42) |
| 10-15 | 6455 | 0.194 | 0.179 | +0.0150 ± 0.0013 | 0.5728 | 0.5294 | 0.4949 | 0.3715 | 0.3723 | -0.061 ± 0.0053 | -0.0136 (14) |
| 15-25 | 8334 | 0.2121 | 0.1726 | +0.0394 ± 0.0018 | 0.6181 | 0.509 | 0.5128 | 0.3183 | 0.315 | -0.071 ± 0.0045 | -0.0533 (3) |
| 25-40 | 6316 | 0.216 | 0.1268 | +0.0893 ± 0.0028 | 0.6252 | 0.3884 | 0.5285 | 0.213 | 0.2313 | -0.048 ± 0.0043 | -0.02 (4) |
| 40+ | 4194 | 0.3919 | 0.0486 | +0.3433 ± 0.0039 | 1.0212 | 0.1822 | 0.6402 | 0.1075 | 0.0646 | -0.076 ± 0.0033 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1455 | 0.1981 | 0.1981 | +0.0000 ± 0.0004 | 0.5747 | 0.5746 | 0.5082 | 0.4932 | 0.4969 | -0.069 ± 0.0119 | -0.0221 (56) |
| 3-5 | 1048 | 0.1884 | 0.1883 | +0.0000 ± 0.0011 | 0.5548 | 0.5529 | 0.497 | 0.4571 | 0.4752 | -0.055 ± 0.0137 | -0.0194 (34) |
| 5-10 | 2109 | 0.2 | 0.1951 | +0.0049 ± 0.0014 | 0.5898 | 0.5736 | 0.5083 | 0.4347 | 0.4391 | -0.077 ± 0.0098 | -0.005 (78) |
| 10-15 | 1451 | 0.2146 | 0.2023 | +0.0123 ± 0.0029 | 0.6227 | 0.5882 | 0.542 | 0.4192 | 0.4294 | -0.088 ± 0.0121 | 0.0012 (66) |
| 15-25 | 1897 | 0.2309 | 0.2075 | +0.0234 ± 0.0041 | 0.659 | 0.5989 | 0.5915 | 0.3966 | 0.436 | -0.089 ± 0.0105 | -0.0214 (59) |
| 25-40 | 1136 | 0.2397 | 0.2105 | +0.0292 ± 0.0083 | 0.6847 | 0.6039 | 0.6887 | 0.3768 | 0.4859 | -0.086 ± 0.0128 | -0.0252 (27) |
| 40+ | 408 | 0.3236 | 0.2018 | +0.1218 ± 0.0212 | 0.9314 | 0.5873 | 0.818 | 0.3421 | 0.4681 | -0.095 ± 0.0197 | -0.1137 (8) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5356 | 0.1778 | 0.1779 | -0.0001 ± 0.0002 | 0.5261 | 0.5258 | 0.5115 | 0.4963 | 0.5056 | -0.039 ± 0.0058 | -0.0154 (103) |
| 3-5 | 3710 | 0.1948 | 0.194 | +0.0008 ± 0.0006 | 0.5685 | 0.5662 | 0.5014 | 0.4616 | 0.4725 | -0.039 ± 0.0073 | -0.0212 (73) |
| 5-10 | 7533 | 0.1965 | 0.19 | +0.0065 ± 0.0008 | 0.5802 | 0.5603 | 0.5017 | 0.4282 | 0.4223 | -0.062 ± 0.0051 | -0.0084 (134) |
| 10-15 | 5157 | 0.2099 | 0.1936 | +0.0163 ± 0.0015 | 0.611 | 0.5678 | 0.5371 | 0.4142 | 0.408 | -0.072 ± 0.0062 | -0.0057 (111) |
| 15-25 | 6280 | 0.2315 | 0.1999 | +0.0316 ± 0.0022 | 0.6649 | 0.5792 | 0.5768 | 0.3814 | 0.399 | -0.068 ± 0.0057 | -0.026 (108) |
| 25-40 | 4090 | 0.2566 | 0.1906 | +0.0660 ± 0.0043 | 0.7264 | 0.5548 | 0.6407 | 0.3283 | 0.3817 | -0.065 ± 0.0067 | -0.0277 (53) |
| 40+ | 1817 | 0.3694 | 0.1593 | +0.2102 ± 0.0097 | 1.0424 | 0.4745 | 0.7458 | 0.245 | 0.2961 | -0.063 ± 0.0089 | -0.054 (15) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 7239 | 1.028 ± 0.033 | 1.098 | 0.1688 | 0.1683 | 0.2149 | 0.2041 |
| gen2 | 7239 | 0.82 ± 0.03 | 1.07 | 0.1735 | 0.1686 | 0.2334 | 0.204 |
| gen1_elo | 7239 | 1.011 ± 0.032 | 1.088 | 0.1751 | 0.1683 | 0.214 | 0.2042 |
| gen1_sr | 7239 | 1.006 ± 0.039 | 1.127 | 0.1334 | 0.1702 | 0.2294 | 0.2037 |
| gen1_ledger | 9504 | 0.866 ± 0.024 | 1.075 | 0.1896 | 0.1753 | 0.2169 | 0.2005 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 33,588)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 7,773 | 23.1% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,638 | 22.7% |
| BOOK_QUALITY | execution | 5,996 | 17.8% |
| POOR_DATA | data | 3,866 | 11.5% |
| LIMITED_DATA | data | 2,092 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,933 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 1,402 | 4.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,377 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 960 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 550 | 1.6% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 23.1%, coverage 22.7%, execution 17.8%, data 17.7%, market_freshness/coverage 8.6%, mapping 4.2%, model_calibration_or_unknown 4.1%, model_calibration 1.6%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.6%, LOW_DATA_QUALITY 71.5%, THIN_PLAYER_HISTORY 59.7%, STALE_PLAYER_DATA 52.1%, STALE_KALSHI_QUOTE 46.2%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 24.1%, MODEL_HIGH_UNCERTAINTY 18.7%, PLAYER_IDENTITY_RISK 15.3%, LEVEL_TRANSFER_RISK 10.0%, LOW_DISPLAYED_LIQUIDITY 8.3%, EVENT_MAPPING_RISK 7.2%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.2%, POST_SETTLEMENT_OBSERVATION 22.7%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 17,849)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,124 | 34.3% |
| STALE_QUOTE | market_freshness | 3,459 | 19.4% |
| BOOK_QUALITY | execution | 3,108 | 17.4% |
| POOR_DATA | data | 1,626 | 9.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,030 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 778 | 4.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 630 | 3.5% |
| LIMITED_DATA | data | 616 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 342 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 135 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.3%, market_freshness 19.4%, execution 17.4%, data 12.6%, market_freshness/coverage 9.3%, mapping 4.4%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 74.7%, THIN_PLAYER_HISTORY 61.6%, STALE_KALSHI_QUOTE 53.7%, STALE_PLAYER_DATA 45.7%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 34.2%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 19.3%, PLAYER_IDENTITY_RISK 18.3%, EVENT_MAPPING_RISK 8.9%, LEVEL_TRANSFER_RISK 8.8%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.8%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.4%, POST_SETTLEMENT_OBSERVATION 34.3%, POSSIBLE_IN_PLAY_QUOTE 6.2%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 14245, "IDENTITY_AMBIGUOUS": 3604}; ticker orientation: {"VERIFIED": 17849}.

Checks: discipline:AMBIGUOUS 1199, discipline:PASS 16650, identity_confidence:AMBIGUOUS 3273, identity_confidence:PASS 14576, level_mapping:NA 1211, level_mapping:PASS 16638, market_pair:AMBIGUOUS 492, market_pair:NA 403, market_pair:PASS 16954, model_complement:NA 365, model_complement:PASS 17484, namesake:AMBIGUOUS 6, namesake:PASS 17843, physical_match_id:NA 6079, physical_match_id:PASS 11770, player_ids:PASS 17849, same_pair_other_event:PASS 17849, ticker_orientation:PASS 17849

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,382 | 3.8% | 3.2% | 1.4% | {"market_freshness": 57, "model_calibration_or_unknown": 54, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 22, "market_freshness/coverage": 20} | 5.52 | 0.2241 / 0.2194 (823) | 24.8% | 2.5% | 3.1% | 2.9% |
| CHALLENGER | 11,767 | 16.4% | 6.2% | 10.8% | {"coverage": 1139, "market_freshness": 228, "market_freshness/coverage": 222, "data": 164, "model_calibration_or_unknown": 79, "execution": 42, "model_calibration": 36, "mapping": 17, "possible_market_error": 1} | 7.39 | 0.2207 / 0.2104 (2768) | 38.1% | 15.0% | 4.0% | 22.3% |
| DOUBLES | 2,583 | 46.4% | 46.4% | 6.7% | {"execution": 665, "mapping": 352, "market_freshness": 106, "market_freshness/coverage": 69, "coverage": 7} | 23.22 | 0.2974 / 0.2321 (646) | 9.1% | 0.0% | 100.0% | 6.3% |
| ITF_MEN | 23,369 | 24.9% | 17.4% | 32.6% | {"coverage": 2052, "market_freshness": 1130, "execution": 985, "data": 852, "market_freshness/coverage": 590, "mapping": 204, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.66 | 0.2176 / 0.1998 (4982) | 40.0% | 68.8% | 15.1% | 21.6% |
| ITF_WOMEN | 30,516 | 26.4% | 18.9% | 45.2% | {"coverage": 2849, "market_freshness": 1734, "execution": 1333, "data": 1125, "market_freshness/coverage": 702, "mapping": 199, "model_calibration_or_unknown": 95, "model_calibration": 23} | 12.51 | 0.2023 / 0.194 (5918) | 41.2% | 57.1% | 9.9% | 21.7% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,851 | 6.0% | 5.1% | 1.6% | {"market_freshness": 111, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.67 | 0.2304 / 0.2206 (794) | 29.9% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.6% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 113 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.4h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 509 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 773 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 869 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 12 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 20.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 1203 min (STALE); no external reference |
| 15 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 16 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 18 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 17.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1037 min (STALE); no external reference |
| 19 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 20 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 21 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 22 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 23 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 24 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 25 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 163 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 26 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 27 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 28 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 29 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 30 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 31 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 32 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 33 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 34 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 365 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 35 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 36 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 37 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 38 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 39 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 40 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 41 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 213 min (STALE); no external reference |
| 43 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 44 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 45 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 46 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 77 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 49 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 50 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 82 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9702, "by_level_share_of_ge_25pp": {"ATP": 0.0136, "CHALLENGER": 0.108, "DOUBLES": 0.0672, "ITF_MEN": 0.3263, "ITF_WOMEN": 0.4516, "OTHER": 0.0007, "WTA": 0.0163, "WTA125": 0.0164}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5366, "share_primary_cause_market_settled_or_in_play": 0.4361, "share_primary_cause_stale_quote_only": 0.1938}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 17849, "identity_ambiguous_share": 0.2019, "ticker_orientation": {"VERIFIED": 17849}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 11770, "with_external": 618, "coverage": 0.0525, "external_status": {"EXTERNAL_STALE": 395, "AGREES_WITH_KALSHI": 210, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 395, "MODEL_LONE_OUTLIER": 210, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3398, "share_external_supports_model": 0.021}, "pregame_clean_ge_25pp": {"n": 5492, "with_external": 588, "coverage": 0.1071, "external_status": {"EXTERNAL_STALE": 372, "AGREES_WITH_KALSHI": 203, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 372, "MODEL_LONE_OUTLIER": 203, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3452, "share_external_supports_model": 0.0221}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 494.0, "median_sample_ratio": 2.46, "median_min_matches": 19.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2086, "data_status": {"POOR": 9974, "LIMITED": 4646, "ADEQUATE": 3229}, "comparison_lt_10pp": {"median_thinner_serve_points": 1734.0, "median_sample_ratio": 1.7, "median_min_matches": 90.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1459, "model_minus_observed": 0.0615, "kalshi_minus_observed": -0.0772, "brier_diff_model_minus_kalshi": 0.0011}, "4-10x": {"n": 992, "model_minus_observed": 0.0901, "kalshi_minus_observed": -0.0542, "brier_diff_model_minus_kalshi": 0.0087}, "<2x": {"n": 3566, "model_minus_observed": 0.0994, "kalshi_minus_observed": -0.0233, "brier_diff_model_minus_kalshi": 0.0144}, ">=10x": {"n": 1222, "model_minus_observed": 0.1167, "kalshi_minus_observed": -0.0565, "brier_diff_model_minus_kalshi": 0.0137}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 7239, "model": {"intercept": -0.553, "slope": 0.82, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.181, "slope": 1.07, "slope_se": 0.033}, "mean_extremity_model": 0.1735, "mean_extremity_kalshi": 0.1686, "model_brier": 0.2334, "kalshi_brier": 0.204, "brier_diff_model_minus_kalshi": 0.0294, "brier_diff_se": 0.0022, "model_logloss": 0.6643, "kalshi_logloss": 0.5906}, "fair_v1": {"n": 7239, "model": {"intercept": -0.448, "slope": 1.028, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.247, "slope": 1.098, "slope_se": 0.034}, "mean_extremity_model": 0.1688, "mean_extremity_kalshi": 0.1683, "model_brier": 0.2149, "kalshi_brier": 0.2041, "brier_diff_model_minus_kalshi": 0.0108, "brier_diff_se": 0.0018, "model_logloss": 0.619, "kalshi_logloss": 0.5908}, "gen1_elo": {"n": 7239, "model": {"intercept": -0.436, "slope": 1.011, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.249, "slope": 1.088, "slope_se": 0.033}, "mean_extremity_model": 0.1751, "mean_extremity_kalshi": 0.1683, "model_brier": 0.214, "kalshi_brier": 0.2042, "brier_diff_model_minus_kalshi": 0.0098, "brier_diff_se": 0.0018, "model_logloss": 0.6174, "kalshi_logloss": 0.5909}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2481, "share_ge_15": 0.4444, "median_abs_gap": 13.05, "n": 47449}, "gen1_elo": {"share_ge_25": 0.2453, "share_ge_15": 0.4403, "median_abs_gap": 12.84, "n": 47449}, "gen1_sr": {"share_ge_25": 0.313, "share_ge_15": 0.5203, "median_abs_gap": 15.83, "n": 47449}, "gen2": {"share_ge_25": 0.314, "share_ge_15": 0.5104, "median_abs_gap": 15.46, "n": 47449}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1504, "share_ge_15": 0.3532, "median_abs_gap": 10.68, "n": 36516}, "gen1_elo": {"share_ge_25": 0.1483, "share_ge_15": 0.3481, "median_abs_gap": 10.49, "n": 36516}, "gen1_sr": {"share_ge_25": 0.2151, "share_ge_15": 0.4389, "median_abs_gap": 12.98, "n": 36518}, "gen2": {"share_ge_25": 0.2304, "share_ge_15": 0.4384, "median_abs_gap": 12.85, "n": 36518}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.52, "share_ge_25_all": 0.0379, "share_ge_25_pregame_clean": 0.0323}, "WTA": {"median_abs_gap_pregame_clean": 7.67, "share_ge_25_all": 0.06, "share_ge_25_pregame_clean": 0.0509}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2367, "share_within_10pp_all": 0.4386, "share_within_10pp_pregame_clean": 0.4919, "corr_model_vs_mid_pregame_clean": 0.8507}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1048, "model_brier": 0.1978, "kalshi_brier": 0.198, "brier_diff_model_minus_kalshi": -0.0002}, "10-15": {"n_settled": 1256, "model_brier": 0.2184, "kalshi_brier": 0.2096, "brier_diff_model_minus_kalshi": 0.0087}, "15-25": {"n_settled": 1609, "model_brier": 0.2259, "kalshi_brier": 0.2083, "brier_diff_model_minus_kalshi": 0.0176}, "25-40": {"n_settled": 914, "model_brier": 0.222, "kalshi_brier": 0.2058, "brier_diff_model_minus_kalshi": 0.0162}, "3-5": {"n_settled": 668, "model_brier": 0.2055, "kalshi_brier": 0.2054, "brier_diff_model_minus_kalshi": 0.0001}, "40+": {"n_settled": 189, "model_brier": 0.295, "kalshi_brier": 0.1767, "brier_diff_model_minus_kalshi": 0.1183}, "5-10": {"n_settled": 1555, "model_brier": 0.2025, "kalshi_brier": 0.2014, "brier_diff_model_minus_kalshi": 0.0012}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.553, "slope": 0.82, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.181, "slope": 1.07, "slope_se": 0.033}, "n": 7239}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.484, "slope": 0.866, "slope_se": 0.024}, "kalshi_slope": {"intercept": 0.175, "slope": 1.075, "slope_se": 0.028}, "n": 9504}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 646, "model_brier": 0.2974, "kalshi_brier": 0.2321, "brier_diff_model_minus_kalshi": 0.0652, "brier_diff_se": 0.0115, "corr_model_outcome": 0.1054, "corr_kalshi_outcome": 0.2829}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
