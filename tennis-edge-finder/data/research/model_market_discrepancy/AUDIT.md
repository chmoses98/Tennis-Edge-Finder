# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-14T11:21Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 92,570): 0-3 13.9%, 3-5 9.5%, 5-10 20.1%, 10-15 15.2%, 15-25 19.2%, 25-40 13.8%, 40+ 8.4%; median gap 11.95 pp.
* **Where the extremes live**: 97.4% of >=25 pp gaps are off the ATP/WTA main tour (ITF 78.3%, Challenger 11.1%, doubles 6.5%). Main tour: ATP 3.7% and WTA 5.9% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 20,511): MARKET_ALREADY_SETTLED_WHEN_PRICED 35.7%, STALE_QUOTE 19.9%, BOOK_QUALITY 16.2%, POOR_DATA 9.0%, POSSIBLY_IN_PLAY_QUOTE 5.9%, IDENTITY_AMBIGUOUS 4.3%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 1.7%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 35.7%, market_freshness 19.9%, execution 16.2%, data 12.3%, market_freshness/coverage 9.4%, mapping 4.3%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 55.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 45.0% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 20,511 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.7%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 27.0% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 491.0 points vs 1680.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.023, Gen-2 0.819, Gen-1 ledger 0.864 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 1046 model 0.2252 vs Kalshi 0.2038; n 214 model 0.307 vs Kalshi 0.1666.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA. Not implemented here.

## 1. Observations

* 382,929 model-market comparisons (634,954 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 125,934 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-14T11:00:15.468853+00:00'], shadow board 107,294 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-14T11:00:19.052068+00:00'], Model 4 44,358 rows, 31,831 settled tickers, 11,998 tickers with an external scan.
* By model: {"gen1_ledger": 84055, "gen1_elo": 53916, "fair_v1": 53916, "gen2": 53916, "gen1_sr": 53916, "model4_fundamental": 41647, "model4_conditioned": 41563}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 92,570 | 13.9 | 9.5 | 20.1 | 15.2 | 19.2 | 13.8 | 8.4 | 11.95 | 41.3% | 22.2% |
| MW fair_v1 | 53,916 | 12.5 | 8.6 | 18.6 | 15.2 | 19.6 | 15.1 | 10.5 | 13.24 | 45.1% | 25.5% |
| MW gen1_elo | 53,916 | 12.3 | 8.7 | 19.1 | 15.2 | 19.4 | 15.0 | 10.3 | 13.02 | 44.7% | 25.3% |
| MW gen1_ledger | 38,654 | 15.8 | 10.8 | 22.2 | 15.2 | 18.6 | 12.0 | 5.5 | 10.29 | 36.1% | 17.5% |
| MW gen1_sr | 53,916 | 9.9 | 7.1 | 16.5 | 13.9 | 20.9 | 18.8 | 12.9 | 16.02 | 52.6% | 31.7% |
| MW gen2 | 53,916 | 10.8 | 7.5 | 16.6 | 13.7 | 19.7 | 17.7 | 14.0 | 15.56 | 51.4% | 31.7% |
| all families model4_conditioned | 41,563 | 22.2 | 17.9 | 34.6 | 16.9 | 4.9 | 2.2 | 1.2 | 6.06 | 8.4% | 3.4% |
| all families model4_fundamental | 41,647 | 17.3 | 13.6 | 34.0 | 19.9 | 9.9 | 3.8 | 1.5 | 7.6 | 15.2% | 5.3% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.5%, >=15pp 41.3%, >=20pp 30.6%, >=25pp 22.2%, >=30pp 16.1%, >=40pp 8.4%, >=50pp 3.9%
Executable gap (model outside the book, before fees): median 8.62pp; >=10pp 45.8%, >=25pp 17.7%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,141 | 27.9 | 16.0 | 28.0 | 13.2 | 10.7 | 3.5 | 0.6 | 5.77 | 14.8% | 4.1% |
| CHALLENGER | 8,459 | 16.3 | 9.6 | 20.6 | 15.2 | 15.7 | 11.4 | 11.2 | 10.94 | 38.3% | 22.6% |
| ITF_MEN | 16,018 | 9.6 | 7.3 | 17.0 | 14.9 | 21.0 | 17.1 | 12.9 | 15.45 | 51.1% | 30.1% |
| ITF_WOMEN | 20,846 | 9.3 | 7.0 | 16.1 | 14.6 | 22.2 | 18.6 | 12.1 | 16.04 | 52.9% | 30.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,119 | 16.5 | 13.2 | 24.9 | 20.7 | 16.9 | 6.8 | 1.1 | 8.68 | 24.7% | 7.8% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,141 | 26.3 | 15.7 | 26.4 | 15.8 | 11.2 | 3.9 | 0.8 | 6.09 | 15.9% | 4.7% |
| CHALLENGER | 8,459 | 14.3 | 9.1 | 19.1 | 13.7 | 18.4 | 13.7 | 11.7 | 12.55 | 43.7% | 25.4% |
| ITF_MEN | 16,018 | 8.2 | 6.2 | 15.2 | 13.8 | 20.3 | 19.9 | 16.4 | 17.82 | 56.5% | 36.2% |
| ITF_WOMEN | 20,846 | 7.8 | 5.8 | 14.1 | 12.7 | 20.6 | 21.2 | 17.8 | 19.21 | 59.6% | 39.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,119 | 14.0 | 10.3 | 21.5 | 16.3 | 22.6 | 12.8 | 2.5 | 11.28 | 37.9% | 15.3% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,141 | 23.5 | 14.2 | 25.6 | 15.4 | 14.2 | 5.9 | 1.1 | 7.01 | 21.3% | 7.0% |
| CHALLENGER | 8,459 | 15.2 | 9.5 | 20.7 | 15.6 | 16.0 | 11.9 | 11.1 | 11.16 | 39.0% | 23.0% |
| ITF_MEN | 16,018 | 9.3 | 7.3 | 17.2 | 14.3 | 21.3 | 17.3 | 13.2 | 15.75 | 51.9% | 30.6% |
| ITF_WOMEN | 20,846 | 9.2 | 6.8 | 16.2 | 15.5 | 22.1 | 18.7 | 11.5 | 15.85 | 52.2% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,119 | 22.4 | 17.1 | 31.8 | 15.3 | 9.1 | 3.3 | 1.0 | 6.12 | 13.4% | 4.4% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,510 | 28.1 | 19.5 | 29.2 | 12.1 | 8.1 | 2.5 | 0.4 | 5.24 | 11.0% | 2.9% |
| CHALLENGER | 5,124 | 23.3 | 14.7 | 27.6 | 14.6 | 12.9 | 5.4 | 1.5 | 6.94 | 19.8% | 6.9% |
| DOUBLES | 2,868 | 4.7 | 4.5 | 12.8 | 10.9 | 20.5 | 25.1 | 21.6 | 23.41 | 67.2% | 46.6% |
| ITF_MEN | 11,517 | 12.8 | 9.6 | 21.6 | 15.7 | 21.6 | 12.8 | 6.0 | 11.77 | 40.4% | 18.8% |
| ITF_WOMEN | 13,389 | 13.5 | 9.3 | 19.9 | 15.8 | 21.6 | 14.5 | 5.4 | 12.14 | 41.5% | 19.9% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,841 | 23.7 | 15.8 | 32.0 | 16.7 | 9.0 | 2.5 | 0.2 | 6.59 | 11.7% | 2.7% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,012 | 28.4 | 16.2 | 28.4 | 13.2 | 10.4 | 3.1 | 0.3 | 5.64 | 13.8% | 3.4% |
| CHALLENGER | 5,923 | 21.1 | 12.1 | 25.8 | 18.0 | 15.7 | 5.5 | 1.8 | 8.16 | 23.1% | 7.3% |
| ITF_MEN | 11,535 | 11.9 | 8.8 | 20.6 | 17.2 | 22.1 | 14.0 | 5.4 | 12.42 | 41.5% | 19.4% |
| ITF_WOMEN | 15,089 | 11.3 | 8.6 | 19.1 | 17.1 | 24.1 | 15.3 | 4.5 | 13.11 | 43.9% | 19.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,004 | 16.8 | 13.2 | 25.2 | 21.0 | 16.9 | 6.2 | 0.6 | 8.51 | 23.7% | 6.8% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,012 | 26.6 | 16.0 | 26.7 | 15.7 | 11.2 | 3.4 | 0.4 | 6.01 | 15.0% | 3.8% |
| CHALLENGER | 5,923 | 18.1 | 11.8 | 24.0 | 16.2 | 19.0 | 8.9 | 2.0 | 8.96 | 29.9% | 10.9% |
| ITF_MEN | 11,537 | 9.8 | 7.4 | 17.8 | 16.0 | 22.3 | 17.8 | 9.0 | 14.64 | 49.0% | 26.8% |
| ITF_WOMEN | 15,091 | 8.9 | 7.0 | 16.1 | 14.2 | 22.6 | 20.6 | 10.6 | 16.51 | 53.8% | 31.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,004 | 14.3 | 10.4 | 21.7 | 16.4 | 22.8 | 12.5 | 1.9 | 11.11 | 37.1% | 14.4% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,440 | 28.4 | 19.7 | 29.3 | 12.3 | 7.7 | 2.3 | 0.3 | 5.2 | 10.3% | 2.6% |
| CHALLENGER | 4,530 | 24.7 | 15.5 | 28.7 | 14.8 | 12.2 | 3.7 | 0.4 | 6.46 | 16.3% | 4.1% |
| DOUBLES | 2,682 | 4.6 | 4.5 | 13.0 | 10.9 | 20.4 | 24.9 | 21.7 | 23.35 | 67.0% | 46.6% |
| ITF_MEN | 9,944 | 13.6 | 10.1 | 23.0 | 16.3 | 21.7 | 11.4 | 4.1 | 10.9 | 37.2% | 15.5% |
| ITF_WOMEN | 11,531 | 14.1 | 9.8 | 21.0 | 16.4 | 21.7 | 13.4 | 3.6 | 11.35 | 38.7% | 17.0% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,776 | 24.1 | 16.2 | 32.0 | 16.7 | 8.9 | 2.0 | 0.1 | 6.44 | 11.0% | 2.0% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,868 | 4.7 | 4.5 | 12.8 | 10.9 | 20.5 | 25.1 | 21.6 | 23.41 | 67.2% | 46.6% |
| singles | 35,786 | 16.6 | 11.4 | 22.9 | 15.5 | 18.4 | 10.9 | 4.2 | 9.74 | 33.6% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 11,791 | 12.6 | 9.0 | 19.2 | 15.0 | 19.6 | 14.3 | 10.3 | 13.03 | 44.3% | 24.6% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 35,044 | 12.9 | 8.6 | 18.8 | 15.0 | 19.2 | 15.1 | 10.4 | 13.06 | 44.6% | 25.5% |
| UNKNOWN | 6,668 | 10.5 | 7.5 | 17.1 | 16.5 | 21.5 | 15.8 | 11.1 | 14.3 | 48.4% | 26.9% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 14,975 | 19.0 | 11.8 | 22.3 | 15.7 | 14.9 | 9.6 | 6.7 | 9.06 | 31.1% | 16.2% |
| B | 6,402 | 12.9 | 8.5 | 19.4 | 15.2 | 19.9 | 12.3 | 11.7 | 12.89 | 43.9% | 24.0% |
| C | 7,732 | 11.9 | 8.5 | 19.2 | 16.0 | 19.1 | 14.8 | 10.6 | 13.08 | 44.5% | 25.3% |
| D | 8,933 | 11.2 | 8.3 | 17.8 | 15.2 | 21.6 | 15.8 | 10.1 | 14.1 | 47.5% | 25.9% |
| F | 15,874 | 7.3 | 5.7 | 15.1 | 14.2 | 23.0 | 21.1 | 13.7 | 18.05 | 57.7% | 34.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 10,158 | 25.0 | 15.9 | 29.0 | 14.8 | 10.6 | 3.4 | 1.2 | 6.35 | 15.2% | 4.7% |
| B | 5,261 | 16.8 | 11.0 | 24.0 | 17.0 | 18.9 | 9.4 | 3.0 | 9.61 | 31.2% | 12.3% |
| C | 7,663 | 11.0 | 7.8 | 19.5 | 14.9 | 20.9 | 15.8 | 10.1 | 13.56 | 46.8% | 25.9% |
| D | 5,916 | 14.3 | 9.9 | 21.1 | 15.5 | 21.0 | 12.8 | 5.3 | 11.41 | 39.1% | 18.1% |
| F | 9,656 | 10.2 | 8.4 | 16.8 | 14.5 | 23.5 | 18.8 | 7.9 | 15.07 | 50.2% | 26.7% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 16,962 | 17.5 | 10.8 | 21.3 | 15.5 | 15.2 | 10.3 | 9.5 | 10.08 | 34.9% | 19.7% |
| LIMITED | 11,746 | 13.4 | 9.4 | 20.3 | 15.9 | 19.8 | 13.4 | 7.7 | 12.01 | 41.0% | 21.2% |
| POOR | 25,208 | 8.8 | 6.6 | 16.1 | 14.6 | 22.4 | 19.0 | 12.4 | 16.37 | 53.8% | 31.4% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,390 | 23.8 | 18.0 | 33.0 | 15.4 | 6.3 | 3.0 | 0.4 | 5.89 | 9.7% | 3.4% |
| GAME_SPREAD | 6,989 | 22.8 | 15.3 | 32.1 | 16.8 | 9.1 | 3.3 | 0.7 | 6.68 | 13.0% | 3.9% |
| MATCH_WINNER | 38,654 | 15.8 | 10.8 | 22.2 | 15.2 | 18.6 | 12.0 | 5.5 | 10.29 | 36.1% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 17,265 | 28.4 | 16.8 | 30.8 | 12.7 | 8.8 | 2.3 | 0.3 | 5.57 | 11.4% | 2.6% |
| TOTAL_GAMES | 11,733 | 9.7 | 10.8 | 36.5 | 25.6 | 10.4 | 4.2 | 2.8 | 9.12 | 17.4% | 7.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,788 | 24.5 | 28.8 | 33.2 | 8.0 | 3.9 | 1.2 | 0.3 | 4.79 | 5.4% | 1.5% |
| GAME_SPREAD | 9,605 | 46.6 | 15.8 | 25.2 | 7.4 | 2.4 | 1.9 | 0.6 | 3.33 | 4.9% | 2.5% |
| TOTAL_GAMES | 17,170 | 6.5 | 9.8 | 41.0 | 29.8 | 7.2 | 3.3 | 2.3 | 9.14 | 12.9% | 5.6% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,824 | 23.9 | 16.7 | 34.6 | 14.7 | 6.9 | 2.7 | 0.5 | 6.05 | 10.1% | 3.2% |
| GAME_SPREAD | 9,614 | 20.3 | 13.4 | 28.5 | 20.2 | 12.1 | 4.3 | 1.1 | 7.71 | 17.6% | 5.5% |
| TOTAL_GAMES | 17,209 | 10.0 | 10.9 | 36.5 | 24.3 | 11.3 | 4.4 | 2.6 | 9.01 | 18.2% | 7.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 53,916 | 45.1% | 25.5% | 13.24 | 35.5% | 15.1% | 10.71 |
| gen1_elo | 53,916 | 44.7% | 25.3% | 13.02 | 34.9% | 15.0% | 10.5 |
| gen1_sr | 53,916 | 52.6% | 31.7% | 16.02 | 43.9% | 21.4% | 12.98 |
| gen2 | 53,916 | 51.4% | 31.7% | 15.56 | 43.9% | 22.9% | 12.82 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,625 | 15.4 | 10.5 | 21.3 | 17.2 | 20.1 | 11.9 | 3.5 | 10.72 | 35.4% | 15.4% |
| STALE | 33,291 | 10.7 | 7.4 | 17.0 | 13.9 | 19.3 | 17.0 | 14.8 | 15.44 | 51.1% | 31.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 32,122 | 16.3 | 11.1 | 22.7 | 15.2 | 18.2 | 11.5 | 5.0 | 9.97 | 34.7% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 92,570 | 32122 | 24097 | 36351 | 25.3 | 154.0 | 1451.1 |
| ge_15pp | 38,255 | 11140 | 8601 | 18514 | 29.2 | 455.5 | 1451.1 |
| ge_25pp | 20,511 | 5295 | 3763 | 11453 | 35.0 | 599.0 | 1431.1 |
| lt_10pp | 40,272 | 16087 | 11387 | 12798 | 22.8 | 49.7 | 1421.7 |

Current slate `SL-20261114T112132Z-299de7ad`: 164 priced rows, quote age at build {'median': 55.0, 'max': 85.0}, freshness {'STALE': 164}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 52 | 0.0 | 0.0 | 34.6 | 9.6 | 32.7 | 19.2 | 3.9 | 18.34 | 55.8% | 23.1% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 5,128 | 19.2 | 11.1 | 25.7 | 18.3 | 17.7 | 7.1 | 1.0 | 8.76 | 25.7% | 8.1% |
| KALSHI_LONE_OUTLIER | 32 | 6.2 | 6.2 | 75.0 | 6.2 | 3.1 | 3.1 | 0.0 | 6.16 | 6.2% | 3.1% |
| MARKETS_AGREE | 1,110 | 66.1 | 33.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,349 | 0.0 | 2.2 | 38.4 | 25.9 | 23.9 | 8.6 | 0.9 | 11.65 | 33.5% | 9.5% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 53,916 | 8700 (16.1%) | 27.0% | 0.9% | {"EXTERNAL_STALE": 5128, "AGREES_WITH_KALSHI": 2349, "ALL_AGREE": 1110, "SUPPORTS_MODEL_DIRECTION": 50, "AGREES_WITH_MODEL": 32, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 24,316 | 2137 (8.8%) | 36.8% | 1.5% | {"EXTERNAL_STALE": 1320, "AGREES_WITH_KALSHI": 786, "SUPPORTS_MODEL_DIRECTION": 29, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 13,754 | 651 (4.7%) | 34.4% | 2.0% | {"EXTERNAL_STALE": 414, "AGREES_WITH_KALSHI": 224, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 6,176 | 618 (10.0%) | 35.1% | 2.1% | {"EXTERNAL_STALE": 388, "AGREES_WITH_KALSHI": 217, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 21,416 | 5009 (23.4%) | 19.1% | 0.9% | {"EXTERNAL_STALE": 2870, "ALL_AGREE": 1110, "AGREES_WITH_KALSHI": 954, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 28, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 10,585 | 10.5 | 7.7 | 18.9 | 14.3 | 21.7 | 16.4 | 10.4 | 14.41 | 48.6% | 26.9% |
| 4-10x | 7,301 | 10.8 | 8.6 | 18.1 | 14.9 | 21.5 | 14.7 | 11.4 | 14.12 | 47.6% | 26.1% |
| <2x | 27,439 | 14.4 | 9.6 | 19.8 | 15.9 | 17.6 | 13.4 | 9.3 | 11.77 | 40.3% | 22.7% |
| >=10x | 8,591 | 10.2 | 6.4 | 15.2 | 14.2 | 21.8 | 18.9 | 13.3 | 16.52 | 54.0% | 32.2% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 14,272 | 12.2 | 8.6 | 19.5 | 16.1 | 19.2 | 13.8 | 10.7 | 12.89 | 43.6% | 24.4% |
| 300-1000 | 11,763 | 11.4 | 8.6 | 17.8 | 15.1 | 20.4 | 16.4 | 10.2 | 13.94 | 47.1% | 26.6% |
| <300 | 16,999 | 8.1 | 5.8 | 15.1 | 14.4 | 22.9 | 20.0 | 13.6 | 17.47 | 56.5% | 33.6% |
| >=3000 | 10,882 | 20.9 | 12.8 | 23.9 | 15.3 | 14.1 | 7.5 | 5.5 | 7.92 | 27.1% | 13.1% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1679 | 0.547 | 0.4081 | 0.4759 | +0.071 | -0.068 | 0.0041 ± 0.0038 |
| ratio 4-10x | 1146 | 0.5709 | 0.4268 | 0.4852 | +0.086 | -0.058 | 0.0095 ± 0.0047 |
| ratio <2x | 4099 | 0.5343 | 0.4117 | 0.4313 | +0.103 | -0.020 | 0.0147 ± 0.0022 |
| ratio >=10x | 1404 | 0.5579 | 0.3867 | 0.4302 | +0.128 | -0.043 | 0.0184 ± 0.0047 |
| thinner_sample 1000-3000 | 2304 | 0.5392 | 0.4124 | 0.4418 | +0.097 | -0.029 | 0.0129 ± 0.003 |
| thinner_sample 300-1000 | 1899 | 0.5592 | 0.419 | 0.4671 | +0.092 | -0.048 | 0.0068 ± 0.0036 |
| thinner_sample <300 | 2706 | 0.5516 | 0.3852 | 0.4398 | +0.112 | -0.055 | 0.0157 ± 0.0034 |
| thinner_sample >=3000 | 1419 | 0.5278 | 0.4345 | 0.4454 | +0.082 | -0.011 | 0.0132 ± 0.003 |
| data_status ADEQUATE | 2253 | 0.5318 | 0.4297 | 0.4407 | +0.091 | -0.011 | 0.0145 ± 0.0026 |
| data_status LIMITED | 2038 | 0.5461 | 0.4134 | 0.4607 | +0.085 | -0.047 | 0.0079 ± 0.0033 |
| data_status POOR | 4037 | 0.5535 | 0.3949 | 0.4446 | +0.109 | -0.050 | 0.0137 ± 0.0027 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1197 | 0.1961 | 0.1961 | -0.0000 ± 0.0004 | 0.5715 | 0.5717 | 0.5028 | 0.4877 | 0.4929 | -0.098 ± 0.0135 | -0.0087 (8) |
| 3-5 | 783 | 0.2082 | 0.2075 | +0.0007 ± 0.0013 | 0.6023 | 0.5993 | 0.4999 | 0.4601 | 0.4713 | -0.098 ± 0.0167 | 0.01 (3) |
| 5-10 | 1794 | 0.2024 | 0.2004 | +0.0020 ± 0.0016 | 0.5911 | 0.5844 | 0.5094 | 0.4355 | 0.4582 | -0.091 ± 0.0109 | -0.0143 (7) |
| 10-15 | 1448 | 0.2207 | 0.2111 | +0.0096 ± 0.003 | 0.6341 | 0.6062 | 0.524 | 0.4007 | 0.4227 | -0.103 ± 0.0123 | -0.055 (6) |
| 15-25 | 1846 | 0.2253 | 0.2071 | +0.0182 ± 0.0041 | 0.6455 | 0.5974 | 0.5702 | 0.3757 | 0.4258 | -0.098 ± 0.0107 | -0.0045 (11) |
| 25-40 | 1046 | 0.2252 | 0.2038 | +0.0214 ± 0.0084 | 0.6407 | 0.588 | 0.6427 | 0.3332 | 0.4522 | -0.064 ± 0.013 | -0.06 (2) |
| 40+ | 214 | 0.307 | 0.1666 | +0.1404 ± 0.0253 | 0.8206 | 0.5019 | 0.7244 | 0.2671 | 0.3505 | -0.089 ± 0.0244 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 6036 | 0.1869 | 0.1877 | -0.0008 ± 0.0002 | 0.5502 | 0.5512 | 0.4921 | 0.4768 | 0.5066 | -0.022 ± 0.0057 | -0.01 (28) |
| 3-5 | 4108 | 0.1992 | 0.1974 | +0.0018 ± 0.0006 | 0.5797 | 0.5734 | 0.4804 | 0.4406 | 0.4377 | -0.056 ± 0.007 | 0.005 (6) |
| 5-10 | 8986 | 0.2005 | 0.1962 | +0.0043 ± 0.0007 | 0.5867 | 0.5729 | 0.4823 | 0.4085 | 0.4164 | -0.049 ± 0.0047 | -0.0114 (22) |
| 10-15 | 7333 | 0.2023 | 0.1862 | +0.0162 ± 0.0013 | 0.5917 | 0.5461 | 0.4839 | 0.36 | 0.357 | -0.064 ± 0.0051 | -0.0379 (19) |
| 15-25 | 9438 | 0.2061 | 0.167 | +0.0391 ± 0.0016 | 0.604 | 0.4964 | 0.4976 | 0.302 | 0.3007 | -0.066 ± 0.0042 | -0.0043 (51) |
| 25-40 | 7390 | 0.2221 | 0.1235 | +0.0987 ± 0.0026 | 0.6382 | 0.3808 | 0.5229 | 0.2086 | 0.2124 | -0.058 ± 0.004 | -0.0733 (3) |
| 40+ | 5123 | 0.3794 | 0.0438 | +0.3356 ± 0.0033 | 0.9887 | 0.1702 | 0.6272 | 0.1017 | 0.0568 | -0.076 ± 0.0028 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 959 | 0.202 | 0.2022 | -0.0003 ± 0.0005 | 0.5841 | 0.5849 | 0.5079 | 0.4928 | 0.5162 | -0.095 ± 0.0155 | -0.0117 (6) |
| 3-5 | 704 | 0.2113 | 0.2083 | +0.0030 ± 0.0014 | 0.6062 | 0.5995 | 0.5189 | 0.4793 | 0.4588 | -0.125 ± 0.0184 | 0.01 (3) |
| 5-10 | 1549 | 0.2045 | 0.2029 | +0.0016 ± 0.0017 | 0.5943 | 0.5905 | 0.5386 | 0.4641 | 0.4919 | -0.083 ± 0.0118 | -0.01 (4) |
| 10-15 | 1345 | 0.2156 | 0.2074 | +0.0082 ± 0.0031 | 0.624 | 0.6005 | 0.5574 | 0.4331 | 0.4647 | -0.103 ± 0.0129 | -0.04 (5) |
| 15-25 | 1941 | 0.2334 | 0.2125 | +0.0209 ± 0.0041 | 0.6647 | 0.6093 | 0.5839 | 0.3881 | 0.4343 | -0.097 ± 0.0107 | -0.0183 (12) |
| 25-40 | 1342 | 0.266 | 0.2002 | +0.0659 ± 0.0076 | 0.7424 | 0.5807 | 0.6577 | 0.3443 | 0.3979 | -0.107 ± 0.0123 | -0.008 (5) |
| 40+ | 488 | 0.374 | 0.1598 | +0.2142 ± 0.0182 | 1.0153 | 0.4846 | 0.7318 | 0.2428 | 0.2807 | -0.087 ± 0.0175 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5189 | 0.1897 | 0.1899 | -0.0002 ± 0.0002 | 0.5545 | 0.5548 | 0.5057 | 0.4906 | 0.5051 | -0.040 ± 0.0062 | -0.0154 (26) |
| 3-5 | 3613 | 0.1935 | 0.1924 | +0.0011 ± 0.0006 | 0.5642 | 0.5611 | 0.5108 | 0.4711 | 0.4761 | -0.046 ± 0.0075 | 0.01 (5) |
| 5-10 | 8030 | 0.1955 | 0.1922 | +0.0033 ± 0.0007 | 0.5751 | 0.5628 | 0.5068 | 0.4325 | 0.4497 | -0.038 ± 0.005 | -0.0117 (6) |
| 10-15 | 6643 | 0.2021 | 0.1897 | +0.0124 ± 0.0013 | 0.5934 | 0.5553 | 0.5056 | 0.3817 | 0.3944 | -0.050 ± 0.0054 | -0.0189 (18) |
| 15-25 | 9529 | 0.2166 | 0.1804 | +0.0362 ± 0.0017 | 0.6308 | 0.5294 | 0.5238 | 0.3282 | 0.3359 | -0.058 ± 0.0044 | -0.014 (52) |
| 25-40 | 8566 | 0.2494 | 0.1376 | +0.1118 ± 0.0026 | 0.7049 | 0.4199 | 0.5583 | 0.241 | 0.2272 | -0.075 ± 0.004 | -0.0095 (20) |
| 40+ | 6844 | 0.4015 | 0.0591 | +0.3424 ± 0.0034 | 1.0581 | 0.2126 | 0.6542 | 0.1189 | 0.0802 | -0.073 ± 0.0029 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1181 | 0.1968 | 0.1979 | -0.0011 ± 0.0005 | 0.5737 | 0.5763 | 0.5017 | 0.4862 | 0.5224 | -0.059 ± 0.0135 | -0.0191 (11) |
| 3-5 | 843 | 0.2092 | 0.2075 | +0.0016 ± 0.0013 | 0.6057 | 0.6004 | 0.4956 | 0.456 | 0.4567 | -0.108 ± 0.0164 | 0.002 (5) |
| 5-10 | 1800 | 0.2032 | 0.199 | +0.0042 ± 0.0016 | 0.5919 | 0.5804 | 0.5101 | 0.4363 | 0.4444 | -0.103 ± 0.0108 | -0.01 (10) |
| 10-15 | 1499 | 0.2122 | 0.2032 | +0.0090 ± 0.0029 | 0.6152 | 0.589 | 0.537 | 0.4138 | 0.441 | -0.100 ± 0.0117 | -0.0286 (7) |
| 15-25 | 1745 | 0.2311 | 0.2115 | +0.0195 ± 0.0043 | 0.6593 | 0.6069 | 0.5791 | 0.3851 | 0.4315 | -0.102 ± 0.0111 | -0.03 (1) |
| 25-40 | 1031 | 0.2178 | 0.206 | +0.0118 ± 0.0084 | 0.6256 | 0.5929 | 0.6508 | 0.3413 | 0.4743 | -0.058 ± 0.0131 | -0.0267 (3) |
| 40+ | 229 | 0.3093 | 0.1804 | +0.1289 ± 0.0253 | 0.8338 | 0.5323 | 0.7372 | 0.2806 | 0.3799 | -0.075 ± 0.0258 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5875 | 0.1867 | 0.1872 | -0.0005 ± 0.0002 | 0.5495 | 0.55 | 0.4873 | 0.4718 | 0.4861 | -0.037 ± 0.0057 | -0.0189 (44) |
| 3-5 | 4196 | 0.2046 | 0.2029 | +0.0017 ± 0.0006 | 0.5946 | 0.5887 | 0.4805 | 0.4409 | 0.439 | -0.056 ± 0.0071 | -0.0073 (22) |
| 5-10 | 9115 | 0.1963 | 0.1908 | +0.0055 ± 0.0007 | 0.5765 | 0.559 | 0.4852 | 0.4112 | 0.41 | -0.057 ± 0.0046 | -0.0117 (42) |
| 10-15 | 7358 | 0.1953 | 0.1798 | +0.0154 ± 0.0012 | 0.576 | 0.5323 | 0.4947 | 0.3714 | 0.3706 | -0.061 ± 0.005 | -0.0136 (14) |
| 15-25 | 9452 | 0.2107 | 0.1715 | +0.0391 ± 0.0017 | 0.6147 | 0.5062 | 0.5089 | 0.3141 | 0.312 | -0.067 ± 0.0043 | -0.0533 (3) |
| 25-40 | 7380 | 0.2164 | 0.1233 | +0.0931 ± 0.0026 | 0.626 | 0.3798 | 0.5246 | 0.2091 | 0.2207 | -0.051 ± 0.004 | -0.02 (4) |
| 40+ | 5038 | 0.3879 | 0.0476 | +0.3403 ± 0.0035 | 1.0112 | 0.1801 | 0.636 | 0.107 | 0.0625 | -0.077 ± 0.0029 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1659 | 0.1965 | 0.1963 | +0.0003 ± 0.0004 | 0.5714 | 0.5707 | 0.5066 | 0.4916 | 0.4907 | -0.072 ± 0.0111 | -0.0311 (57) |
| 3-5 | 1167 | 0.1896 | 0.1896 | -0.0001 ± 0.001 | 0.5573 | 0.5565 | 0.4985 | 0.4586 | 0.4773 | -0.054 ± 0.013 | -0.0194 (34) |
| 5-10 | 2366 | 0.1988 | 0.1937 | +0.0051 ± 0.0014 | 0.5866 | 0.5702 | 0.5098 | 0.4362 | 0.4387 | -0.077 ± 0.0093 | -0.005 (78) |
| 10-15 | 1633 | 0.2155 | 0.2033 | +0.0122 ± 0.0028 | 0.6254 | 0.5901 | 0.5444 | 0.4216 | 0.4323 | -0.086 ± 0.0115 | 0.0015 (67) |
| 15-25 | 2127 | 0.2319 | 0.2074 | +0.0245 ± 0.0039 | 0.6619 | 0.5984 | 0.5925 | 0.3975 | 0.4335 | -0.089 ± 0.01 | -0.0214 (59) |
| 25-40 | 1238 | 0.2425 | 0.2123 | +0.0302 ± 0.008 | 0.6918 | 0.608 | 0.6884 | 0.3769 | 0.4847 | -0.082 ± 0.0124 | -0.0297 (29) |
| 40+ | 459 | 0.3288 | 0.1991 | +0.1297 ± 0.02 | 0.9397 | 0.5804 | 0.8073 | 0.3304 | 0.4488 | -0.089 ± 0.0187 | -0.1033 (9) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5975 | 0.1775 | 0.1775 | +0.0000 ± 0.0002 | 0.5254 | 0.5249 | 0.5087 | 0.4935 | 0.5006 | -0.041 ± 0.0055 | -0.0204 (104) |
| 3-5 | 4093 | 0.1945 | 0.1937 | +0.0008 ± 0.0006 | 0.5677 | 0.5657 | 0.502 | 0.4622 | 0.4713 | -0.040 ± 0.007 | -0.022 (74) |
| 5-10 | 8358 | 0.1971 | 0.1907 | +0.0065 ± 0.0007 | 0.5814 | 0.562 | 0.5033 | 0.4297 | 0.4237 | -0.061 ± 0.0048 | -0.0085 (136) |
| 10-15 | 5752 | 0.2108 | 0.1947 | +0.0161 ± 0.0014 | 0.6138 | 0.5705 | 0.5376 | 0.4147 | 0.4096 | -0.070 ± 0.0059 | -0.0054 (112) |
| 15-25 | 7035 | 0.2314 | 0.1991 | +0.0323 ± 0.0021 | 0.6654 | 0.5773 | 0.5769 | 0.3815 | 0.397 | -0.067 ± 0.0054 | -0.024 (112) |
| 25-40 | 4534 | 0.2583 | 0.1913 | +0.0670 ± 0.0041 | 0.7299 | 0.5562 | 0.6411 | 0.3289 | 0.3807 | -0.061 ± 0.0064 | -0.0311 (63) |
| 40+ | 2032 | 0.3706 | 0.1602 | +0.2105 ± 0.0091 | 1.0418 | 0.4768 | 0.7413 | 0.2417 | 0.2913 | -0.058 ± 0.0085 | -0.0465 (20) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 8328 | 1.023 ± 0.031 | 1.08 | 0.1676 | 0.1712 | 0.2158 | 0.2034 |
| gen2 | 8328 | 0.819 ± 0.028 | 1.06 | 0.1739 | 0.1714 | 0.2332 | 0.2033 |
| gen1_elo | 8328 | 1.003 ± 0.03 | 1.072 | 0.174 | 0.1713 | 0.2151 | 0.2035 |
| gen1_sr | 8328 | 1.006 ± 0.036 | 1.107 | 0.1335 | 0.1729 | 0.2292 | 0.203 |
| gen1_ledger | 10649 | 0.864 ± 0.023 | 1.061 | 0.1903 | 0.1772 | 0.2173 | 0.2003 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 38,255)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 9,209 | 24.1% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 9,075 | 23.7% |
| BOOK_QUALITY | execution | 6,411 | 16.8% |
| POOR_DATA | data | 4,343 | 11.3% |
| LIMITED_DATA | data | 2,290 | 6.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 2,245 | 5.9% |
| IDENTITY_AMBIGUOUS | mapping | 1,576 | 4.1% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,441 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 1,078 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 586 | 1.5% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 24.1%, coverage 23.7%, data 17.3%, execution 16.8%, market_freshness/coverage 8.7%, mapping 4.1%, model_calibration_or_unknown 3.8%, model_calibration 1.5%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 95.1%, LOW_DATA_QUALITY 72.1%, THIN_PLAYER_HISTORY 59.9%, STALE_PLAYER_DATA 51.8%, STALE_KALSHI_QUOTE 48.4%, MODEL_INTERNAL_DISAGREEMENT 41.6%, ASYMMETRIC_SAMPLE_SIZE 33.0%, WIDE_SPREAD 23.2%, MODEL_HIGH_UNCERTAINTY 18.9%, PLAYER_IDENTITY_RISK 15.0%, LEVEL_TRANSFER_RISK 9.2%, LOW_DISPLAYED_LIQUIDITY 8.7%, EVENT_MAPPING_RISK 7.0%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.1%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 26.0%, POST_SETTLEMENT_OBSERVATION 23.7%, POSSIBLE_IN_PLAY_QUOTE 6.3%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 20,511)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,314 | 35.7% |
| STALE_QUOTE | market_freshness | 4,085 | 19.9% |
| BOOK_QUALITY | execution | 3,312 | 16.2% |
| POOR_DATA | data | 1,838 | 9.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,213 | 5.9% |
| IDENTITY_AMBIGUOUS | mapping | 876 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 708 | 3.5% |
| LIMITED_DATA | data | 677 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 347 | 1.7% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 140 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 35.7%, market_freshness 19.9%, execution 16.2%, data 12.3%, market_freshness/coverage 9.4%, mapping 4.3%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.2%, START_UNVERIFIABLE 97.4%, LOW_DATA_QUALITY 75.2%, THIN_PLAYER_HISTORY 61.9%, STALE_KALSHI_QUOTE 55.8%, STALE_PLAYER_DATA 45.0%, MODEL_INTERNAL_DISAGREEMENT 41.6%, ASYMMETRIC_SAMPLE_SIZE 34.2%, WIDE_SPREAD 22.4%, MODEL_HIGH_UNCERTAINTY 19.5%, PLAYER_IDENTITY_RISK 17.8%, LOW_DISPLAYED_LIQUIDITY 8.6%, EVENT_MAPPING_RISK 8.5%, LEVEL_TRANSFER_RISK 8.0%, MODEL_CALIBRATION_OUTLIER 4.6%, EXTERNAL_MARKET_REJECTION 1.7%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 38.5%, POST_SETTLEMENT_OBSERVATION 35.7%, POSSIBLE_IN_PLAY_QUOTE 6.4%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 16509, "IDENTITY_AMBIGUOUS": 4002}; ticker orientation: {"VERIFIED": 20511}.

Checks: discipline:AMBIGUOUS 1337, discipline:PASS 19174, identity_confidence:AMBIGUOUS 3649, identity_confidence:PASS 16862, level_mapping:NA 1349, level_mapping:PASS 19162, market_pair:AMBIGUOUS 518, market_pair:NA 435, market_pair:PASS 19558, model_complement:NA 397, model_complement:PASS 20114, namesake:AMBIGUOUS 6, namesake:PASS 20505, physical_match_id:NA 6757, physical_match_id:PASS 13754, player_ids:PASS 20511, same_pair_other_event:PASS 20511, ticker_orientation:PASS 20511

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,651 | 3.7% | 3.1% | 1.2% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 24, "market_freshness/coverage": 22} | 5.47 | 0.222 / 0.2184 (873) | 25.7% | 2.4% | 3.2% | 3.0% |
| CHALLENGER | 13,583 | 16.7% | 5.9% | 11.1% | {"coverage": 1400, "market_freshness": 275, "market_freshness/coverage": 249, "data": 164, "model_calibration_or_unknown": 80, "execution": 41, "model_calibration": 41, "mapping": 17, "possible_market_error": 1} | 7.28 | 0.2214 / 0.2117 (3174) | 41.8% | 13.5% | 4.0% | 23.0% |
| DOUBLES | 2,868 | 46.6% | 46.6% | 6.5% | {"execution": 736, "mapping": 409, "market_freshness": 106, "market_freshness/coverage": 79, "coverage": 7} | 23.35 | 0.2978 / 0.232 (724) | 8.2% | 0.0% | 100.0% | 6.5% |
| ITF_MEN | 27,535 | 25.4% | 17.6% | 34.1% | {"coverage": 2496, "market_freshness": 1448, "execution": 1056, "data": 1029, "market_freshness/coverage": 713, "mapping": 233, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.73 | 0.218 / 0.1978 (5873) | 42.4% | 69.6% | 14.2% | 22.0% |
| ITF_WOMEN | 34,235 | 26.5% | 18.6% | 44.2% | {"coverage": 3332, "market_freshness": 1994, "execution": 1396, "data": 1221, "market_freshness/coverage": 801, "mapping": 211, "model_calibration_or_unknown": 98, "model_calibration": 23} | 12.41 | 0.2035 / 0.194 (6703) | 43.1% | 57.1% | 10.1% | 22.2% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,960 | 5.9% | 5.0% | 1.4% | {"market_freshness": 112, "model_calibration_or_unknown": 53, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.69 | 0.2319 / 0.2213 (818) | 30.3% | 2.0% | 1.2% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.4% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 523 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.4h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 509 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFMATCH-26NOV12VALRAT-RAT` | ITF_MEN | gen1_ledger | 92% / 4% | +88 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 10 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1333.0, ratio 3.64); no external reference |
| 6 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 7 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 8 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 9 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 117 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 10 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 11 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 12 | `KXITFMATCH-26NOV10KOUPOR-POR` | ITF_MEN | fair_v1 | 87% / 2% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.9h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 305 min (STALE); data POOR (grade D, thinner serve sample 1554.0, ratio 1.02); no external reference |
| 13 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 14 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 17 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 18 | `KXITFMATCH-26NOV13ALMJAD-ALM` | ITF_MEN | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 385 min (STALE); data LIMITED (grade C, thinner serve sample 691.0, ratio 3.98); no external reference |
| 19 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 20 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 21 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 22 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 23 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 24 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 25 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 26 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 27 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 28 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 163 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 29 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 30 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 31 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 32 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 33 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 34 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 35 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 36 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 37 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 271 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 38 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 39 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 40 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 41 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 42 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 43 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 44 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 45 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 46 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 47 | `KXITFMATCH-26NOV13JADZIN-ZIN` | ITF_MEN | fair_v1 | 89% / 10% | +80 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 28 min (AGING); data POOR (grade D, thinner serve sample 691.0, ratio 5.99); no external reference |
| 48 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 49 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 50 | `KXITFWMATCH-26NOV11CORROJ-ROJ` | ITF_WOMEN | fair_v1 | 87% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade D, thinner serve sample 531.0, ratio 1.04); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9738, "by_level_share_of_ge_25pp": {"ATP": 0.0119, "CHALLENGER": 0.1106, "DOUBLES": 0.0652, "ITF_MEN": 0.3406, "ITF_WOMEN": 0.4425, "OTHER": 0.0006, "WTA": 0.0143, "WTA125": 0.0143}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5584, "share_primary_cause_market_settled_or_in_play": 0.4502, "share_primary_cause_stale_quote_only": 0.1992}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 20511, "identity_ambiguous_share": 0.1951, "ticker_orientation": {"VERIFIED": 20511}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 13754, "with_external": 651, "coverage": 0.0473, "external_status": {"EXTERNAL_STALE": 414, "AGREES_WITH_KALSHI": 224, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 414, "MODEL_LONE_OUTLIER": 224, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3441, "share_external_supports_model": 0.02}, "pregame_clean_ge_25pp": {"n": 6176, "with_external": 618, "coverage": 0.1001, "external_status": {"EXTERNAL_STALE": 388, "AGREES_WITH_KALSHI": 217, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 388, "MODEL_LONE_OUTLIER": 217, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3511, "share_external_supports_model": 0.021}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 491.0, "median_sample_ratio": 2.43, "median_min_matches": 18.0, "median_max_days_since_last": 246.0, "share_severe_asymmetry": 0.2047, "data_status": {"POOR": 11609, "LIMITED": 5198, "ADEQUATE": 3704}, "comparison_lt_10pp": {"median_thinner_serve_points": 1680.0, "median_sample_ratio": 1.71, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1679, "model_minus_observed": 0.0711, "kalshi_minus_observed": -0.0678, "brier_diff_model_minus_kalshi": 0.0041}, "4-10x": {"n": 1146, "model_minus_observed": 0.0858, "kalshi_minus_observed": -0.0583, "brier_diff_model_minus_kalshi": 0.0095}, "<2x": {"n": 4099, "model_minus_observed": 0.103, "kalshi_minus_observed": -0.0197, "brier_diff_model_minus_kalshi": 0.0147}, ">=10x": {"n": 1404, "model_minus_observed": 0.1277, "kalshi_minus_observed": -0.0435, "brier_diff_model_minus_kalshi": 0.0184}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 8328, "model": {"intercept": -0.562, "slope": 0.819, "slope_se": 0.028}, "kalshi_mid_same_rows": {"intercept": 0.165, "slope": 1.06, "slope_se": 0.031}, "mean_extremity_model": 0.1739, "mean_extremity_kalshi": 0.1714, "model_brier": 0.2332, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.0299, "brier_diff_se": 0.0021, "model_logloss": 0.6639, "kalshi_logloss": 0.5888}, "fair_v1": {"n": 8328, "model": {"intercept": -0.471, "slope": 1.023, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.211, "slope": 1.08, "slope_se": 0.031}, "mean_extremity_model": 0.1676, "mean_extremity_kalshi": 0.1712, "model_brier": 0.2158, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": 0.0125, "brier_diff_se": 0.0017, "model_logloss": 0.621, "kalshi_logloss": 0.589}, "gen1_elo": {"n": 8328, "model": {"intercept": -0.457, "slope": 1.003, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.215, "slope": 1.072, "slope_se": 0.03}, "mean_extremity_model": 0.174, "mean_extremity_kalshi": 0.1713, "model_brier": 0.2151, "kalshi_brier": 0.2035, "brier_diff_model_minus_kalshi": 0.0116, "brier_diff_se": 0.0017, "model_logloss": 0.6199, "kalshi_logloss": 0.5892}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2551, "share_ge_15": 0.451, "median_abs_gap": 13.24, "n": 53916}, "gen1_elo": {"share_ge_25": 0.253, "share_ge_15": 0.4466, "median_abs_gap": 13.02, "n": 53916}, "gen1_sr": {"share_ge_25": 0.3171, "share_ge_15": 0.5258, "median_abs_gap": 16.02, "n": 53916}, "gen2": {"share_ge_25": 0.3172, "share_ge_15": 0.5139, "median_abs_gap": 15.56, "n": 53916}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1512, "share_ge_15": 0.3547, "median_abs_gap": 10.71, "n": 40847}, "gen1_elo": {"share_ge_25": 0.1498, "share_ge_15": 0.3488, "median_abs_gap": 10.5, "n": 40847}, "gen1_sr": {"share_ge_25": 0.2139, "share_ge_15": 0.439, "median_abs_gap": 12.98, "n": 40850}, "gen2": {"share_ge_25": 0.2292, "share_ge_15": 0.4385, "median_abs_gap": 12.82, "n": 40851}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.47, "share_ge_25_all": 0.0368, "share_ge_25_pregame_clean": 0.0308}, "WTA": {"median_abs_gap_pregame_clean": 7.69, "share_ge_25_all": 0.0593, "share_ge_25_pregame_clean": 0.0504}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2339, "share_within_10pp_all": 0.435, "share_within_10pp_pregame_clean": 0.4907, "corr_model_vs_mid_pregame_clean": 0.8498}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1197, "model_brier": 0.1961, "kalshi_brier": 0.1961, "brier_diff_model_minus_kalshi": -0.0}, "10-15": {"n_settled": 1448, "model_brier": 0.2207, "kalshi_brier": 0.2111, "brier_diff_model_minus_kalshi": 0.0096}, "15-25": {"n_settled": 1846, "model_brier": 0.2253, "kalshi_brier": 0.2071, "brier_diff_model_minus_kalshi": 0.0182}, "25-40": {"n_settled": 1046, "model_brier": 0.2252, "kalshi_brier": 0.2038, "brier_diff_model_minus_kalshi": 0.0214}, "3-5": {"n_settled": 783, "model_brier": 0.2082, "kalshi_brier": 0.2075, "brier_diff_model_minus_kalshi": 0.0007}, "40+": {"n_settled": 214, "model_brier": 0.307, "kalshi_brier": 0.1666, "brier_diff_model_minus_kalshi": 0.1404}, "5-10": {"n_settled": 1794, "model_brier": 0.2024, "kalshi_brier": 0.2004, "brier_diff_model_minus_kalshi": 0.002}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'NO_SKILL:gen2|WTA', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.562, "slope": 0.819, "slope_se": 0.028}, "kalshi_slope": {"intercept": 0.165, "slope": 1.06, "slope_se": 0.031}, "n": 8328}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.497, "slope": 0.864, "slope_se": 0.023}, "kalshi_slope": {"intercept": 0.152, "slope": 1.061, "slope_se": 0.026}, "n": 10649}, "NO_SKILL:gen2|WTA": {"n_settled": 349, "model_brier": 0.2503, "kalshi_brier": 0.2266, "brier_diff_model_minus_kalshi": 0.0238, "brier_diff_se": 0.0089, "corr_model_outcome": 0.2571, "corr_kalshi_outcome": 0.3077}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 724, "model_brier": 0.2978, "kalshi_brier": 0.232, "brier_diff_model_minus_kalshi": 0.0658, "brier_diff_se": 0.0109, "corr_model_outcome": 0.1151, "corr_kalshi_outcome": 0.2798}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
