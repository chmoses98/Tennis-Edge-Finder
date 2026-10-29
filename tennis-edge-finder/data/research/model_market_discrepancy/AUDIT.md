# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-29T18:12Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 68,306): 0-3 14.1%, 3-5 9.6%, 5-10 20.1%, 10-15 15.3%, 15-25 19.1%, 25-40 13.9%, 40+ 8.0%; median gap 11.88 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.9%, Challenger 10.9%, doubles 6.5%). Main tour: ATP 4.2% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 14,942): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.8%, STALE_QUOTE 18.8%, BOOK_QUALITY 18.6%, POOR_DATA 9.4%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IDENTITY_AMBIGUOUS 4.1%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.8%, market_freshness 18.8%, execution 18.6%, data 12.9%, market_freshness/coverage 9.1%, mapping 4.1%, model_calibration_or_unknown 2.1%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 51.9% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.8% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 14,942 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.9% of the time and with the model 1.1%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 460.0 points vs 1658.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.017, Gen-2 0.807, Gen-1 ledger 0.859 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 722 model 0.2225 vs Kalshi 0.2069; n 151 model 0.2818 vs Kalshi 0.1882.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 291,261 model-market comparisons (475,486 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 97,581 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-29T17:56:40.437532+00:00'], shadow board 78,058 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-29T17:56:44.477735+00:00'], Model 4 36,549 rows, 23,685 settled tickers, 8,675 tickers with an external scan.
* By model: {"gen1_ledger": 65765, "gen1_elo": 39237, "fair_v1": 39237, "gen2": 39237, "gen1_sr": 39237, "model4_fundamental": 34296, "model4_conditioned": 34252}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 68,306 | 14.1 | 9.6 | 20.1 | 15.3 | 19.1 | 13.9 | 8.0 | 11.88 | 40.9% | 21.9% |
| MW fair_v1 | 39,237 | 12.9 | 8.7 | 18.7 | 15.4 | 19.5 | 15.0 | 9.8 | 13.02 | 44.3% | 24.8% |
| MW gen1_elo | 39,237 | 12.6 | 8.6 | 19.3 | 15.4 | 19.5 | 14.9 | 9.8 | 12.93 | 44.1% | 24.6% |
| MW gen1_ledger | 29,069 | 15.6 | 10.8 | 22.0 | 15.2 | 18.5 | 12.4 | 5.5 | 10.4 | 36.4% | 17.9% |
| MW gen1_sr | 39,237 | 10.1 | 7.2 | 16.9 | 13.8 | 20.7 | 18.6 | 12.8 | 15.87 | 52.1% | 31.4% |
| MW gen2 | 39,237 | 11.1 | 7.5 | 16.5 | 13.8 | 19.4 | 17.8 | 13.8 | 15.48 | 51.0% | 31.6% |
| all families model4_conditioned | 34,252 | 22.4 | 18.2 | 34.2 | 17.2 | 4.9 | 1.9 | 1.1 | 6.0 | 8.0% | 3.0% |
| all families model4_fundamental | 34,296 | 17.3 | 13.3 | 33.8 | 20.3 | 10.2 | 3.7 | 1.4 | 7.7 | 15.2% | 5.0% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.3%, >=15pp 40.9%, >=20pp 30.3%, >=25pp 21.9%, >=30pp 15.8%, >=40pp 8.0%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.3pp; >=10pp 44.8%, >=25pp 17.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,400 | 27.3 | 15.5 | 27.5 | 13.5 | 11.7 | 4.1 | 0.6 | 5.93 | 16.3% | 4.7% |
| CHALLENGER | 5,876 | 16.2 | 9.8 | 20.8 | 15.2 | 15.4 | 11.8 | 10.7 | 10.91 | 37.9% | 22.5% |
| ITF_MEN | 10,962 | 9.8 | 7.4 | 17.1 | 15.1 | 21.2 | 17.6 | 12.0 | 15.22 | 50.7% | 29.5% |
| ITF_WOMEN | 15,477 | 9.7 | 7.1 | 15.8 | 15.1 | 22.1 | 18.2 | 12.0 | 15.73 | 52.3% | 30.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,439 | 18.2 | 13.7 | 24.6 | 20.0 | 16.1 | 6.4 | 0.9 | 8.25 | 23.4% | 7.3% |
| WTA125 | 1,077 | 16.1 | 7.7 | 22.5 | 19.1 | 20.2 | 12.5 | 1.9 | 10.77 | 34.6% | 14.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,400 | 26.1 | 15.4 | 25.4 | 16.2 | 12.0 | 4.1 | 0.8 | 6.23 | 16.9% | 4.9% |
| CHALLENGER | 5,876 | 15.1 | 9.0 | 18.3 | 14.3 | 18.2 | 13.7 | 11.5 | 12.55 | 43.4% | 25.2% |
| ITF_MEN | 10,962 | 8.0 | 6.1 | 15.0 | 13.8 | 19.6 | 20.6 | 16.9 | 18.01 | 57.0% | 37.5% |
| ITF_WOMEN | 15,477 | 8.1 | 5.8 | 14.0 | 12.6 | 20.6 | 21.3 | 17.6 | 19.21 | 59.5% | 38.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,439 | 15.2 | 11.0 | 22.0 | 15.4 | 22.0 | 12.6 | 1.9 | 10.59 | 36.4% | 14.4% |
| WTA125 | 1,077 | 9.6 | 6.3 | 16.5 | 16.5 | 24.4 | 17.5 | 9.2 | 15.35 | 51.1% | 26.7% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,400 | 22.4 | 13.0 | 24.4 | 16.0 | 16.2 | 6.7 | 1.3 | 7.58 | 24.2% | 8.0% |
| CHALLENGER | 5,876 | 14.9 | 9.3 | 21.1 | 16.1 | 15.6 | 12.2 | 10.9 | 11.29 | 38.6% | 23.0% |
| ITF_MEN | 10,962 | 9.2 | 7.1 | 17.5 | 14.4 | 21.6 | 17.9 | 12.3 | 15.68 | 51.8% | 30.2% |
| ITF_WOMEN | 15,477 | 9.5 | 6.8 | 16.3 | 15.8 | 22.1 | 18.1 | 11.4 | 15.5 | 51.5% | 29.5% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,439 | 23.6 | 16.6 | 31.7 | 14.6 | 9.3 | 2.9 | 1.3 | 6.07 | 13.5% | 4.1% |
| WTA125 | 1,077 | 22.0 | 12.9 | 26.7 | 16.8 | 15.0 | 6.1 | 0.4 | 7.99 | 21.5% | 6.5% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,978 | 24.5 | 18.9 | 31.2 | 12.9 | 9.0 | 3.0 | 0.5 | 5.75 | 12.5% | 3.5% |
| CHALLENGER | 3,984 | 22.5 | 14.6 | 27.1 | 14.6 | 13.6 | 6.0 | 1.6 | 7.08 | 21.2% | 7.6% |
| DOUBLES | 2,087 | 5.2 | 4.5 | 12.2 | 10.7 | 20.9 | 25.1 | 21.4 | 23.54 | 67.4% | 46.5% |
| ITF_MEN | 8,361 | 13.0 | 9.4 | 21.2 | 15.9 | 21.3 | 13.3 | 5.9 | 11.91 | 40.6% | 19.2% |
| ITF_WOMEN | 9,972 | 13.1 | 9.2 | 19.6 | 15.6 | 21.4 | 15.5 | 5.6 | 12.43 | 42.5% | 21.1% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,447 | 24.4 | 15.3 | 30.2 | 17.8 | 9.2 | 2.8 | 0.3 | 6.78 | 12.2% | 3.0% |
| WTA125 | 1,091 | 24.8 | 12.7 | 21.1 | 18.9 | 13.7 | 7.2 | 1.6 | 7.93 | 22.6% | 8.9% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,302 | 27.6 | 15.6 | 27.9 | 13.4 | 11.4 | 3.7 | 0.4 | 5.89 | 15.5% | 4.1% |
| CHALLENGER | 4,124 | 21.2 | 12.3 | 25.9 | 17.7 | 15.2 | 6.1 | 1.5 | 8.02 | 22.9% | 7.6% |
| ITF_MEN | 8,048 | 12.0 | 8.8 | 20.6 | 17.1 | 22.0 | 14.3 | 5.3 | 12.41 | 41.5% | 19.6% |
| ITF_WOMEN | 11,540 | 11.5 | 8.5 | 18.3 | 17.3 | 24.0 | 15.2 | 5.2 | 13.34 | 44.4% | 20.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,359 | 18.6 | 13.7 | 24.8 | 20.3 | 16.2 | 5.9 | 0.6 | 8.18 | 22.7% | 6.5% |
| WTA125 | 1,041 | 16.3 | 7.6 | 22.0 | 19.4 | 20.8 | 12.3 | 1.6 | 11.02 | 34.7% | 13.9% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,302 | 26.4 | 15.8 | 25.6 | 16.2 | 11.9 | 3.8 | 0.5 | 6.2 | 16.1% | 4.2% |
| CHALLENGER | 4,124 | 19.2 | 11.5 | 23.0 | 16.8 | 18.5 | 9.2 | 1.8 | 9.02 | 29.5% | 11.0% |
| ITF_MEN | 8,049 | 9.4 | 7.2 | 17.4 | 16.0 | 21.3 | 18.9 | 9.8 | 14.97 | 49.9% | 28.6% |
| ITF_WOMEN | 11,541 | 8.9 | 6.7 | 15.9 | 14.1 | 22.8 | 20.8 | 10.8 | 16.68 | 54.4% | 31.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,359 | 15.3 | 11.1 | 22.1 | 15.5 | 22.2 | 12.5 | 1.2 | 10.53 | 35.9% | 13.7% |
| WTA125 | 1,041 | 9.6 | 6.3 | 16.6 | 16.7 | 24.3 | 17.8 | 8.7 | 15.19 | 50.7% | 26.4% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,924 | 24.6 | 19.1 | 31.3 | 13.1 | 8.7 | 2.9 | 0.4 | 5.67 | 11.9% | 3.3% |
| CHALLENGER | 3,514 | 24.0 | 15.6 | 28.2 | 14.7 | 12.9 | 4.1 | 0.5 | 6.58 | 17.5% | 4.5% |
| DOUBLES | 1,959 | 5.1 | 4.6 | 12.4 | 10.9 | 20.8 | 25.0 | 21.2 | 23.41 | 67.0% | 46.2% |
| ITF_MEN | 7,143 | 13.8 | 9.9 | 22.8 | 16.5 | 21.2 | 11.8 | 3.9 | 10.95 | 36.9% | 15.7% |
| ITF_WOMEN | 8,487 | 13.7 | 9.7 | 20.9 | 16.3 | 21.5 | 14.5 | 3.5 | 11.61 | 39.5% | 18.0% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,393 | 24.8 | 15.7 | 30.2 | 17.9 | 9.2 | 2.1 | 0.1 | 6.6 | 11.4% | 2.2% |
| WTA125 | 967 | 26.2 | 13.4 | 22.1 | 20.1 | 12.6 | 5.1 | 0.5 | 7.37 | 18.2% | 5.6% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,087 | 5.2 | 4.5 | 12.2 | 10.7 | 20.9 | 25.1 | 21.4 | 23.54 | 67.4% | 46.5% |
| singles | 26,982 | 16.4 | 11.2 | 22.8 | 15.6 | 18.3 | 11.4 | 4.3 | 9.88 | 34.0% | 15.7% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,845 | 13.1 | 9.3 | 20.1 | 15.6 | 19.1 | 13.8 | 9.0 | 12.35 | 41.8% | 22.7% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 25,692 | 13.4 | 8.7 | 18.5 | 15.1 | 19.3 | 15.1 | 9.9 | 12.99 | 44.3% | 25.0% |
| UNKNOWN | 5,451 | 10.4 | 7.7 | 17.2 | 16.6 | 21.0 | 16.0 | 11.1 | 14.14 | 48.0% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 10,852 | 20.0 | 12.2 | 22.4 | 15.7 | 14.7 | 9.2 | 5.9 | 8.57 | 29.9% | 15.1% |
| B | 4,814 | 12.8 | 9.0 | 19.2 | 16.0 | 19.3 | 12.7 | 11.0 | 12.61 | 43.0% | 23.7% |
| C | 5,613 | 12.0 | 8.9 | 19.9 | 15.8 | 18.6 | 14.3 | 10.5 | 12.8 | 43.4% | 24.8% |
| D | 6,202 | 12.0 | 8.3 | 17.6 | 15.4 | 21.6 | 15.8 | 9.3 | 13.76 | 46.7% | 25.1% |
| F | 11,756 | 7.4 | 5.6 | 15.0 | 14.7 | 23.3 | 21.0 | 13.0 | 17.71 | 57.4% | 34.0% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,709 | 24.1 | 15.7 | 28.8 | 15.3 | 11.0 | 3.8 | 1.3 | 6.54 | 16.1% | 5.1% |
| B | 4,076 | 17.1 | 10.6 | 24.0 | 16.3 | 18.9 | 9.9 | 3.2 | 9.64 | 31.9% | 13.0% |
| C | 5,673 | 11.2 | 7.9 | 19.5 | 14.7 | 21.0 | 15.7 | 10.1 | 13.46 | 46.7% | 25.7% |
| D | 4,266 | 14.5 | 10.0 | 21.6 | 15.3 | 20.1 | 13.1 | 5.5 | 11.25 | 38.6% | 18.6% |
| F | 7,345 | 9.9 | 8.3 | 16.0 | 15.0 | 23.2 | 19.9 | 7.8 | 15.44 | 50.8% | 27.7% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 12,302 | 18.3 | 11.1 | 21.4 | 15.4 | 15.2 | 10.0 | 8.7 | 9.74 | 33.9% | 18.7% |
| LIMITED | 8,609 | 13.5 | 10.0 | 20.4 | 16.3 | 19.0 | 13.3 | 7.5 | 11.74 | 39.8% | 20.8% |
| POOR | 18,326 | 9.0 | 6.5 | 16.0 | 15.0 | 22.6 | 19.1 | 11.7 | 16.16 | 53.4% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,489 | 24.1 | 18.1 | 33.1 | 15.0 | 6.6 | 2.7 | 0.4 | 5.85 | 9.7% | 3.1% |
| GAME_SPREAD | 5,869 | 22.2 | 15.2 | 33.0 | 17.2 | 8.9 | 3.0 | 0.6 | 6.74 | 12.4% | 3.5% |
| MATCH_WINNER | 29,069 | 15.6 | 10.8 | 22.0 | 15.2 | 18.5 | 12.4 | 5.5 | 10.4 | 36.4% | 17.9% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 13,558 | 27.4 | 16.7 | 31.1 | 12.5 | 9.6 | 2.4 | 0.3 | 5.69 | 12.3% | 2.7% |
| TOTAL_GAMES | 9,756 | 9.6 | 10.4 | 35.9 | 26.7 | 10.5 | 4.0 | 2.8 | 9.29 | 17.4% | 6.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,123 | 24.5 | 30.1 | 32.9 | 7.3 | 4.1 | 0.9 | 0.3 | 4.7 | 5.2% | 1.1% |
| GAME_SPREAD | 8,017 | 47.3 | 16.0 | 25.4 | 7.3 | 2.2 | 1.3 | 0.6 | 3.27 | 4.0% | 1.8% |
| TOTAL_GAMES | 14,112 | 6.4 | 9.2 | 40.4 | 31.4 | 7.2 | 3.1 | 2.2 | 9.31 | 12.6% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,134 | 23.9 | 16.9 | 34.8 | 14.4 | 7.1 | 2.6 | 0.4 | 6.01 | 10.1% | 3.0% |
| GAME_SPREAD | 8,020 | 20.2 | 13.6 | 27.9 | 20.5 | 12.5 | 4.2 | 1.1 | 7.78 | 17.9% | 5.3% |
| TOTAL_GAMES | 14,142 | 10.0 | 10.2 | 36.3 | 25.3 | 11.5 | 4.2 | 2.4 | 9.19 | 18.2% | 6.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 39,237 | 44.3% | 24.8% | 13.02 | 35.6% | 15.4% | 10.74 |
| gen1_elo | 39,237 | 44.1% | 24.6% | 12.93 | 35.3% | 15.4% | 10.55 |
| gen1_sr | 39,237 | 52.1% | 31.4% | 15.87 | 44.2% | 21.9% | 13.03 |
| gen2 | 39,237 | 51.0% | 31.6% | 15.48 | 44.1% | 23.5% | 12.94 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 18,552 | 15.6 | 10.6 | 21.3 | 17.1 | 20.1 | 12.0 | 3.3 | 10.71 | 35.4% | 15.3% |
| STALE | 20,685 | 10.6 | 7.1 | 16.3 | 13.8 | 19.0 | 17.6 | 15.7 | 15.99 | 52.3% | 33.3% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 22,537 | 16.3 | 11.1 | 22.7 | 15.4 | 17.9 | 11.9 | 4.7 | 9.97 | 34.5% | 16.6% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 68,306 | 22537 | 22024 | 23745 | 24.3 | 123.0 | 1451.1 |
| ge_15pp | 27,967 | 7780 | 7857 | 12330 | 26.9 | 434.0 | 1451.1 |
| ge_25pp | 14,942 | 3746 | 3436 | 7760 | 31.7 | 582.7 | 1431.1 |
| lt_10pp | 29,874 | 11291 | 10435 | 8148 | 22.4 | 47.0 | 1421.1 |

Current slate `SL-20261029T181241Z-24f01ae0`: 396 priced rows, quote age at build {'median': 16.4, 'max': 16.4}, freshness {'AGING': 396}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 44 | 0.0 | 0.0 | 31.8 | 6.8 | 34.1 | 22.7 | 4.5 | 20.33 | 61.4% | 27.3% |
| EXTERNAL_LONE_OUTLIER | 24 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.37 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,873 | 19.6 | 11.2 | 25.1 | 18.1 | 17.9 | 7.3 | 0.9 | 8.68 | 26.1% | 8.2% |
| KALSHI_LONE_OUTLIER | 26 | 3.9 | 3.9 | 76.9 | 7.7 | 3.9 | 3.9 | 0.0 | 6.31 | 7.7% | 3.9% |
| MARKETS_AGREE | 764 | 65.2 | 34.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.25 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,657 | 0.0 | 2.4 | 36.3 | 25.4 | 24.7 | 10.2 | 1.0 | 12.0 | 35.9% | 11.2% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 39,237 | 6388 (16.3%) | 25.9% | 1.1% | {"EXTERNAL_STALE": 3873, "AGREES_WITH_KALSHI": 1657, "ALL_AGREE": 764, "SUPPORTS_MODEL_DIRECTION": 43, "AGREES_WITH_MODEL": 26, "EXTERNAL_OUTLIER": 24, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 17,388 | 1636 (9.4%) | 36.4% | 1.8% | {"EXTERNAL_STALE": 1012, "AGREES_WITH_KALSHI": 595, "SUPPORTS_MODEL_DIRECTION": 27, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 9,734 | 515 (5.3%) | 35.9% | 2.5% | {"EXTERNAL_STALE": 317, "AGREES_WITH_KALSHI": 185, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,672 | 488 (10.4%) | 36.5% | 2.7% | {"EXTERNAL_STALE": 297, "AGREES_WITH_KALSHI": 178, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 15,814 | 3626 (22.9%) | 17.7% | 1.0% | {"EXTERNAL_STALE": 2161, "ALL_AGREE": 764, "AGREES_WITH_KALSHI": 641, "EXTERNAL_OUTLIER": 24, "AGREES_WITH_MODEL": 22, "SUPPORTS_MODEL_DIRECTION": 13, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 7,694 | 10.4 | 7.4 | 19.8 | 14.4 | 21.5 | 16.6 | 10.0 | 14.09 | 48.0% | 26.5% |
| 4-10x | 5,298 | 11.1 | 8.6 | 18.5 | 15.6 | 21.9 | 14.4 | 9.9 | 13.67 | 46.2% | 24.3% |
| <2x | 19,803 | 15.2 | 10.0 | 19.4 | 16.0 | 17.4 | 13.1 | 8.9 | 11.58 | 39.4% | 22.0% |
| >=10x | 6,442 | 10.5 | 6.4 | 15.2 | 14.4 | 21.6 | 19.2 | 12.7 | 16.24 | 53.4% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 10,008 | 12.7 | 8.8 | 19.6 | 16.1 | 18.9 | 13.5 | 10.4 | 12.69 | 42.9% | 23.9% |
| 300-1000 | 8,484 | 12.1 | 8.7 | 17.8 | 15.2 | 20.3 | 16.4 | 9.5 | 13.59 | 46.2% | 25.9% |
| <300 | 12,737 | 8.3 | 5.8 | 15.2 | 14.8 | 23.0 | 20.0 | 12.9 | 17.06 | 55.9% | 32.9% |
| >=3000 | 8,008 | 21.6 | 13.3 | 23.9 | 15.6 | 13.8 | 7.2 | 4.7 | 7.53 | 25.7% | 11.9% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1130 | 0.5499 | 0.4108 | 0.4965 | +0.053 | -0.086 | -0.0015 ± 0.0046 |
| ratio 4-10x | 776 | 0.5779 | 0.4316 | 0.4923 | +0.086 | -0.061 | 0.0077 ± 0.0057 |
| ratio <2x | 2699 | 0.5374 | 0.4142 | 0.4487 | +0.089 | -0.034 | 0.0114 ± 0.0028 |
| ratio >=10x | 981 | 0.5678 | 0.3933 | 0.4526 | +0.115 | -0.059 | 0.0132 ± 0.0058 |
| thinner_sample 1000-3000 | 1511 | 0.5394 | 0.4129 | 0.454 | +0.085 | -0.041 | 0.0087 ± 0.0037 |
| thinner_sample 300-1000 | 1268 | 0.5669 | 0.4247 | 0.4858 | +0.081 | -0.061 | 0.0026 ± 0.0045 |
| thinner_sample <300 | 1890 | 0.5589 | 0.3914 | 0.4614 | +0.098 | -0.070 | 0.0104 ± 0.0041 |
| thinner_sample >=3000 | 917 | 0.5313 | 0.4372 | 0.4624 | +0.069 | -0.025 | 0.0131 ± 0.0038 |
| data_status ADEQUATE | 1515 | 0.5339 | 0.431 | 0.4495 | +0.084 | -0.018 | 0.0129 ± 0.0031 |
| data_status LIMITED | 1353 | 0.5488 | 0.4158 | 0.4775 | +0.071 | -0.062 | 0.005 ± 0.0041 |
| data_status POOR | 2718 | 0.5614 | 0.4001 | 0.4676 | +0.094 | -0.068 | 0.008 ± 0.0033 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 816 | 0.1985 | 0.199 | -0.0005 ± 0.0005 | 0.5763 | 0.5777 | 0.5034 | 0.4882 | 0.511 | -0.086 ± 0.0166 | -0.01 (5) |
| 3-5 | 508 | 0.2067 | 0.2069 | -0.0002 ± 0.0016 | 0.5965 | 0.5957 | 0.5029 | 0.463 | 0.4843 | -0.097 ± 0.0206 | 0.02 (1) |
| 5-10 | 1169 | 0.2005 | 0.2012 | -0.0007 ± 0.002 | 0.5867 | 0.5856 | 0.5093 | 0.4356 | 0.4748 | -0.085 ± 0.0135 | -0.0167 (6) |
| 10-15 | 982 | 0.2209 | 0.2123 | +0.0086 ± 0.0037 | 0.6343 | 0.6101 | 0.5265 | 0.4028 | 0.4287 | -0.108 ± 0.0148 | -0.048 (5) |
| 15-25 | 1238 | 0.2247 | 0.2121 | +0.0126 ± 0.0051 | 0.645 | 0.6085 | 0.5764 | 0.3808 | 0.4467 | -0.100 ± 0.0131 | -0.0033 (9) |
| 25-40 | 722 | 0.2225 | 0.2069 | +0.0156 ± 0.0101 | 0.6346 | 0.5955 | 0.6555 | 0.3449 | 0.4751 | -0.073 ± 0.0155 | -0.01 (1) |
| 40+ | 151 | 0.2818 | 0.1882 | +0.0936 ± 0.0308 | 0.7682 | 0.5554 | 0.7408 | 0.2924 | 0.4172 | -0.077 ± 0.0305 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4432 | 0.1833 | 0.1841 | -0.0008 ± 0.0002 | 0.5407 | 0.5419 | 0.4867 | 0.4714 | 0.5018 | -0.023 ± 0.0065 | -0.0129 (17) |
| 3-5 | 2996 | 0.1962 | 0.1942 | +0.0020 ± 0.0007 | 0.5716 | 0.5646 | 0.4821 | 0.4422 | 0.4366 | -0.060 ± 0.0081 | 0.0 (2) |
| 5-10 | 6332 | 0.2013 | 0.1981 | +0.0033 ± 0.0008 | 0.5882 | 0.5769 | 0.483 | 0.4094 | 0.4255 | -0.044 ± 0.0057 | -0.0119 (21) |
| 10-15 | 5302 | 0.2023 | 0.1865 | +0.0158 ± 0.0015 | 0.591 | 0.5477 | 0.4832 | 0.3592 | 0.3568 | -0.066 ± 0.006 | -0.0281 (16) |
| 15-25 | 6605 | 0.2061 | 0.1679 | +0.0382 ± 0.002 | 0.6048 | 0.4985 | 0.4998 | 0.3036 | 0.3049 | -0.070 ± 0.005 | -0.0025 (44) |
| 25-40 | 5230 | 0.2221 | 0.1258 | +0.0963 ± 0.0031 | 0.6385 | 0.3865 | 0.5264 | 0.2122 | 0.2203 | -0.059 ± 0.0048 | -0.01 (1) |
| 40+ | 3402 | 0.3837 | 0.0449 | +0.3387 ± 0.0041 | 0.9996 | 0.1737 | 0.6326 | 0.104 | 0.0603 | -0.078 ± 0.0034 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 640 | 0.205 | 0.2056 | -0.0006 ± 0.0006 | 0.5914 | 0.5931 | 0.5088 | 0.4939 | 0.5203 | -0.103 ± 0.0194 | -0.01 (3) |
| 3-5 | 456 | 0.2218 | 0.2193 | +0.0025 ± 0.0018 | 0.628 | 0.6229 | 0.5125 | 0.4728 | 0.4561 | -0.128 ± 0.0234 | 0.02 (1) |
| 5-10 | 1021 | 0.2074 | 0.2071 | +0.0004 ± 0.0021 | 0.601 | 0.5989 | 0.5437 | 0.469 | 0.5054 | -0.086 ± 0.0147 | -0.01 (4) |
| 10-15 | 911 | 0.2172 | 0.2105 | +0.0067 ± 0.0038 | 0.6255 | 0.6082 | 0.5644 | 0.44 | 0.4775 | -0.109 ± 0.0159 | -0.04 (5) |
| 15-25 | 1295 | 0.2296 | 0.2143 | +0.0153 ± 0.005 | 0.6539 | 0.6128 | 0.5837 | 0.3883 | 0.4494 | -0.095 ± 0.0131 | -0.0133 (9) |
| 25-40 | 922 | 0.2676 | 0.1967 | +0.0709 ± 0.0092 | 0.7473 | 0.574 | 0.6576 | 0.3435 | 0.3905 | -0.132 ± 0.0146 | -0.0075 (4) |
| 40+ | 341 | 0.3608 | 0.1672 | +0.1936 ± 0.0219 | 0.9907 | 0.502 | 0.7328 | 0.2476 | 0.305 | -0.080 ± 0.0214 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3812 | 0.1886 | 0.1889 | -0.0003 ± 0.0002 | 0.5518 | 0.5522 | 0.5088 | 0.4938 | 0.5087 | -0.042 ± 0.0073 | -0.0133 (15) |
| 3-5 | 2596 | 0.1971 | 0.1958 | +0.0013 ± 0.0007 | 0.5711 | 0.5672 | 0.5116 | 0.4719 | 0.4742 | -0.050 ± 0.0089 | 0.02 (1) |
| 5-10 | 5624 | 0.1984 | 0.195 | +0.0034 ± 0.0009 | 0.582 | 0.5691 | 0.5102 | 0.4361 | 0.4531 | -0.043 ± 0.006 | -0.0117 (6) |
| 10-15 | 4739 | 0.2056 | 0.1933 | +0.0122 ± 0.0016 | 0.6009 | 0.5643 | 0.5124 | 0.3886 | 0.402 | -0.054 ± 0.0065 | -0.0189 (18) |
| 15-25 | 6637 | 0.2174 | 0.1815 | +0.0359 ± 0.0021 | 0.6323 | 0.5323 | 0.5238 | 0.3284 | 0.3378 | -0.062 ± 0.0053 | -0.0086 (42) |
| 25-40 | 6097 | 0.2514 | 0.136 | +0.1154 ± 0.003 | 0.7092 | 0.4175 | 0.5576 | 0.2408 | 0.2206 | -0.086 ± 0.0047 | -0.0044 (18) |
| 40+ | 4794 | 0.3973 | 0.059 | +0.3383 ± 0.0041 | 1.0485 | 0.2122 | 0.6513 | 0.1171 | 0.0811 | -0.073 ± 0.0034 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 783 | 0.1954 | 0.1976 | -0.0022 ± 0.0006 | 0.5695 | 0.5751 | 0.5008 | 0.4854 | 0.5466 | -0.037 ± 0.0166 | -0.0137 (8) |
| 3-5 | 541 | 0.206 | 0.2042 | +0.0018 ± 0.0016 | 0.5953 | 0.5891 | 0.4941 | 0.4545 | 0.4529 | -0.121 ± 0.0202 | 0.0067 (3) |
| 5-10 | 1213 | 0.2032 | 0.2016 | +0.0016 ± 0.0019 | 0.5922 | 0.5862 | 0.5091 | 0.4354 | 0.4608 | -0.094 ± 0.0133 | -0.0071 (7) |
| 10-15 | 976 | 0.2091 | 0.2049 | +0.0041 ± 0.0036 | 0.6077 | 0.5936 | 0.5385 | 0.4152 | 0.4611 | -0.095 ± 0.0145 | -0.0317 (6) |
| 15-25 | 1172 | 0.2322 | 0.2163 | +0.0160 ± 0.0053 | 0.6624 | 0.6176 | 0.5866 | 0.3923 | 0.4488 | -0.109 ± 0.0136 | -0.03 (1) |
| 25-40 | 740 | 0.2131 | 0.2128 | +0.0003 ± 0.0099 | 0.6149 | 0.6093 | 0.6632 | 0.3526 | 0.5054 | -0.059 ± 0.0153 | 0.015 (2) |
| 40+ | 161 | 0.2958 | 0.1971 | +0.0987 ± 0.0308 | 0.8063 | 0.5754 | 0.7489 | 0.2984 | 0.4224 | -0.073 ± 0.0319 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4278 | 0.1833 | 0.1839 | -0.0006 ± 0.0002 | 0.5399 | 0.541 | 0.4831 | 0.4678 | 0.4857 | -0.034 ± 0.0066 | -0.0163 (35) |
| 3-5 | 2938 | 0.2022 | 0.2002 | +0.0020 ± 0.0007 | 0.5875 | 0.5802 | 0.4818 | 0.4423 | 0.437 | -0.062 ± 0.0084 | -0.0094 (18) |
| 5-10 | 6502 | 0.1948 | 0.1911 | +0.0037 ± 0.0008 | 0.5731 | 0.5599 | 0.4839 | 0.4099 | 0.4223 | -0.046 ± 0.0055 | -0.01 (31) |
| 10-15 | 5242 | 0.1914 | 0.1786 | +0.0128 ± 0.0014 | 0.5661 | 0.529 | 0.4929 | 0.3695 | 0.3789 | -0.055 ± 0.0059 | -0.015 (12) |
| 15-25 | 6732 | 0.2119 | 0.1728 | +0.0391 ± 0.002 | 0.6172 | 0.5095 | 0.5117 | 0.317 | 0.3157 | -0.071 ± 0.0051 | -0.03 (2) |
| 25-40 | 5228 | 0.2162 | 0.1291 | +0.0872 ± 0.0031 | 0.6258 | 0.3938 | 0.5296 | 0.2141 | 0.2358 | -0.048 ± 0.0048 | 0.01 (3) |
| 40+ | 3379 | 0.3945 | 0.0505 | +0.3439 ± 0.0044 | 1.0287 | 0.1884 | 0.6428 | 0.1112 | 0.0669 | -0.079 ± 0.0037 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1177 | 0.1961 | 0.1962 | -0.0002 ± 0.0005 | 0.5709 | 0.571 | 0.5048 | 0.4897 | 0.4953 | -0.067 ± 0.0132 | -0.0224 (49) |
| 3-5 | 834 | 0.1867 | 0.1858 | +0.0008 ± 0.0012 | 0.5475 | 0.5448 | 0.4974 | 0.4576 | 0.4652 | -0.067 ± 0.0153 | -0.0194 (34) |
| 5-10 | 1730 | 0.2016 | 0.1967 | +0.0049 ± 0.0016 | 0.5924 | 0.577 | 0.501 | 0.4274 | 0.4318 | -0.075 ± 0.0109 | -0.005 (78) |
| 10-15 | 1187 | 0.2151 | 0.2034 | +0.0117 ± 0.0032 | 0.6222 | 0.5907 | 0.5364 | 0.4137 | 0.4254 | -0.084 ± 0.0134 | 0.0014 (64) |
| 15-25 | 1530 | 0.2314 | 0.211 | +0.0204 ± 0.0046 | 0.6598 | 0.607 | 0.5819 | 0.3872 | 0.4346 | -0.082 ± 0.0119 | -0.0214 (59) |
| 25-40 | 952 | 0.2451 | 0.2101 | +0.0350 ± 0.0091 | 0.7 | 0.6022 | 0.6834 | 0.3714 | 0.4716 | -0.096 ± 0.0139 | -0.0219 (26) |
| 40+ | 321 | 0.3318 | 0.2038 | +0.1280 ± 0.0242 | 0.9592 | 0.5931 | 0.8151 | 0.3381 | 0.4579 | -0.094 ± 0.0226 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4388 | 0.1761 | 0.1763 | -0.0002 ± 0.0002 | 0.5211 | 0.5213 | 0.5089 | 0.4936 | 0.5055 | -0.038 ± 0.0064 | -0.0157 (88) |
| 3-5 | 3001 | 0.1926 | 0.1912 | +0.0014 ± 0.0006 | 0.5612 | 0.5584 | 0.5027 | 0.4629 | 0.4642 | -0.050 ± 0.0081 | -0.0209 (69) |
| 5-10 | 6104 | 0.1986 | 0.1914 | +0.0072 ± 0.0008 | 0.5842 | 0.5634 | 0.4961 | 0.4224 | 0.4125 | -0.067 ± 0.0057 | -0.0082 (132) |
| 10-15 | 4288 | 0.2107 | 0.1955 | +0.0152 ± 0.0017 | 0.6123 | 0.5723 | 0.5341 | 0.4111 | 0.4095 | -0.068 ± 0.0068 | -0.0053 (105) |
| 15-25 | 5206 | 0.2292 | 0.2012 | +0.0280 ± 0.0024 | 0.6599 | 0.5819 | 0.5686 | 0.3734 | 0.4001 | -0.061 ± 0.0063 | -0.0253 (107) |
| 25-40 | 3488 | 0.2613 | 0.1869 | +0.0745 ± 0.0046 | 0.7391 | 0.5453 | 0.6359 | 0.3231 | 0.3632 | -0.081 ± 0.0072 | -0.0229 (51) |
| 40+ | 1509 | 0.374 | 0.1546 | +0.2194 ± 0.0105 | 1.0564 | 0.4615 | 0.7393 | 0.2384 | 0.2803 | -0.070 ± 0.0096 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5586 | 1.017 ± 0.037 | 1.093 | 0.1694 | 0.1664 | 0.2148 | 0.2061 |
| gen2 | 5586 | 0.807 ± 0.034 | 1.053 | 0.1716 | 0.1668 | 0.2344 | 0.206 |
| gen1_elo | 5586 | 0.998 ± 0.036 | 1.091 | 0.1756 | 0.1666 | 0.2135 | 0.2063 |
| gen1_sr | 5586 | 0.99 ± 0.044 | 1.113 | 0.1317 | 0.1688 | 0.2303 | 0.2056 |
| gen1_ledger | 7731 | 0.859 ± 0.027 | 1.058 | 0.1875 | 0.1764 | 0.2179 | 0.2013 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 27,967)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,245 | 22.3% |
| STALE_QUOTE | market_freshness | 6,121 | 21.9% |
| BOOK_QUALITY | execution | 5,325 | 19.0% |
| POOR_DATA | data | 3,299 | 11.8% |
| LIMITED_DATA | data | 1,739 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,591 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,216 | 4.3% |
| IDENTITY_AMBIGUOUS | mapping | 1,140 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 805 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 485 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.3%, market_freshness 21.9%, execution 19.0%, data 18.0%, market_freshness/coverage 8.6%, model_calibration_or_unknown 4.3%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.5%, LOW_DATA_QUALITY 71.9%, THIN_PLAYER_HISTORY 60.7%, STALE_PLAYER_DATA 52.5%, STALE_KALSHI_QUOTE 44.1%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 33.5%, WIDE_SPREAD 25.1%, MODEL_HIGH_UNCERTAINTY 18.0%, PLAYER_IDENTITY_RISK 15.6%, LEVEL_TRANSFER_RISK 10.4%, LOW_DISPLAYED_LIQUIDITY 8.0%, EVENT_MAPPING_RISK 7.4%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.8%, POST_SETTLEMENT_OBSERVATION 22.3%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 14,942)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,046 | 33.8% |
| STALE_QUOTE | market_freshness | 2,801 | 18.8% |
| BOOK_QUALITY | execution | 2,776 | 18.6% |
| POOR_DATA | data | 1,407 | 9.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 836 | 5.6% |
| IDENTITY_AMBIGUOUS | mapping | 608 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 520 | 3.5% |
| LIMITED_DATA | data | 517 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 307 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 123 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.8%, market_freshness 18.8%, execution 18.6%, data 12.9%, market_freshness/coverage 9.1%, mapping 4.1%, model_calibration_or_unknown 2.1%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.8%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 75.2%, THIN_PLAYER_HISTORY 62.9%, STALE_KALSHI_QUOTE 51.9%, STALE_PLAYER_DATA 46.6%, MODEL_INTERNAL_DISAGREEMENT 42.8%, ASYMMETRIC_SAMPLE_SIZE 34.6%, WIDE_SPREAD 24.5%, MODEL_HIGH_UNCERTAINTY 18.7%, PLAYER_IDENTITY_RISK 18.4%, LEVEL_TRANSFER_RISK 9.2%, EVENT_MAPPING_RISK 9.0%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.8%, POST_SETTLEMENT_OBSERVATION 33.8%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 11868, "IDENTITY_AMBIGUOUS": 3074}; ticker orientation: {"VERIFIED": 14942}.

Checks: discipline:AMBIGUOUS 970, discipline:PASS 13972, identity_confidence:AMBIGUOUS 2754, identity_confidence:PASS 12188, level_mapping:NA 982, level_mapping:PASS 13960, market_pair:AMBIGUOUS 479, market_pair:NA 347, market_pair:PASS 14116, model_complement:NA 311, model_complement:PASS 14631, namesake:AMBIGUOUS 6, namesake:PASS 14936, physical_match_id:NA 5208, physical_match_id:PASS 9734, player_ids:PASS 14942, same_pair_other_event:PASS 14942, ticker_orientation:PASS 14942

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,378 | 4.2% | 3.8% | 1.5% | {"market_freshness": 56, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "market_freshness/coverage": 17, "coverage": 13} | 5.84 | 0.2201 / 0.2168 (619) | 21.6% | 2.9% | 3.2% | 2.8% |
| CHALLENGER | 9,860 | 16.5% | 6.2% | 10.9% | {"coverage": 955, "market_freshness/coverage": 195, "market_freshness": 165, "data": 144, "model_calibration_or_unknown": 75, "execution": 37, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.25 | 0.2199 / 0.2107 (2251) | 35.3% | 15.7% | 4.1% | 22.5% |
| DOUBLES | 2,087 | 46.5% | 46.2% | 6.5% | {"execution": 551, "mapping": 248, "market_freshness": 106, "market_freshness/coverage": 58, "coverage": 7} | 23.41 | 0.3062 / 0.2386 (504) | 11.2% | 0.0% | 100.0% | 6.1% |
| ITF_MEN | 19,323 | 25.1% | 17.7% | 32.4% | {"coverage": 1693, "execution": 903, "market_freshness": 881, "data": 718, "market_freshness/coverage": 459, "mapping": 183, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.72 | 0.2166 / 0.1997 (3988) | 37.5% | 70.0% | 16.8% | 21.4% |
| ITF_WOMEN | 25,449 | 26.7% | 19.4% | 45.4% | {"coverage": 2337, "market_freshness": 1445, "execution": 1208, "data": 969, "market_freshness/coverage": 574, "mapping": 154, "model_calibration_or_unknown": 81, "model_calibration": 21} | 12.63 | 0.2038 / 0.1957 (4670) | 39.3% | 57.6% | 10.0% | 21.3% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,886 | 5.7% | 4.9% | 1.5% | {"market_freshness": 76, "model_calibration_or_unknown": 43, "coverage": 28, "execution": 27, "data": 19, "model_calibration": 18, "market_freshness/coverage": 11, "mapping": 1} | 7.54 | 0.2371 / 0.2301 (607) | 26.3% | 1.1% | 1.4% | 3.5% |
| WTA125 | 2,168 | 11.6% | 9.9% | 1.7% | {"market_freshness": 70, "model_calibration_or_unknown": 51, "market_freshness/coverage": 41, "data": 38, "execution": 21, "model_calibration": 15, "coverage": 12, "mapping": 4} | 9.21 | 0.209 / 0.1921 (636) | 25.5% | 11.3% | 4.9% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 286 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 3 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 4 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 5 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 6 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 7 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 8 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 572 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 9 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 10 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 113 min (STALE); no external reference |
| 13 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 14 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 17 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 18 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 19 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 20 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 21 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 22 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 23 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 24 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 25 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 26 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 27 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 28 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 29 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 30 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 31 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 32 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 33 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 34 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 35 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 36 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 37 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 38 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 39 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 213 min (STALE); no external reference |
| 40 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 41 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 42 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 43 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.1h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 446 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 44 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 45 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 46 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 12.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 768 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 49 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 50 | `KXATPDOUBLES-26OCT29MICVANARROLI-MICVAN` | DOUBLES | gen1_ledger | 98% / 20% | +77 | BOOK_QUALITY | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.97, "by_level_share_of_ge_25pp": {"ATP": 0.0152, "CHALLENGER": 0.1087, "DOUBLES": 0.0649, "ITF_MEN": 0.3243, "ITF_WOMEN": 0.4544, "OTHER": 0.0008, "WTA": 0.0149, "WTA125": 0.0169}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5193, "share_primary_cause_market_settled_or_in_play": 0.4284, "share_primary_cause_stale_quote_only": 0.1875}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 14942, "identity_ambiguous_share": 0.2057, "ticker_orientation": {"VERIFIED": 14942}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 9734, "with_external": 515, "coverage": 0.0529, "external_status": {"EXTERNAL_STALE": 317, "AGREES_WITH_KALSHI": 185, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 317, "MODEL_LONE_OUTLIER": 185, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3592, "share_external_supports_model": 0.0252}, "pregame_clean_ge_25pp": {"n": 4672, "with_external": 488, "coverage": 0.1045, "external_status": {"EXTERNAL_STALE": 297, "AGREES_WITH_KALSHI": 178, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 297, "MODEL_LONE_OUTLIER": 178, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3648, "share_external_supports_model": 0.0266}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 460.0, "median_sample_ratio": 2.5, "median_min_matches": 18.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2114, "data_status": {"POOR": 8502, "LIMITED": 3843, "ADEQUATE": 2597}, "comparison_lt_10pp": {"median_thinner_serve_points": 1658.0, "median_sample_ratio": 1.73, "median_min_matches": 89.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1130, "model_minus_observed": 0.0535, "kalshi_minus_observed": -0.0857, "brier_diff_model_minus_kalshi": -0.0015}, "4-10x": {"n": 776, "model_minus_observed": 0.0856, "kalshi_minus_observed": -0.0607, "brier_diff_model_minus_kalshi": 0.0077}, "<2x": {"n": 2699, "model_minus_observed": 0.0888, "kalshi_minus_observed": -0.0344, "brier_diff_model_minus_kalshi": 0.0114}, ">=10x": {"n": 981, "model_minus_observed": 0.1152, "kalshi_minus_observed": -0.0593, "brier_diff_model_minus_kalshi": 0.0132}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 5586, "model": {"intercept": -0.532, "slope": 0.807, "slope_se": 0.034}, "kalshi_mid_same_rows": {"intercept": 0.196, "slope": 1.053, "slope_se": 0.038}, "mean_extremity_model": 0.1716, "mean_extremity_kalshi": 0.1668, "model_brier": 0.2344, "kalshi_brier": 0.206, "brier_diff_model_minus_kalshi": 0.0284, "brier_diff_se": 0.0025, "model_logloss": 0.6663, "kalshi_logloss": 0.5949}, "fair_v1": {"n": 5586, "model": {"intercept": -0.41, "slope": 1.017, "slope_se": 0.037}, "kalshi_mid_same_rows": {"intercept": 0.286, "slope": 1.093, "slope_se": 0.038}, "mean_extremity_model": 0.1694, "mean_extremity_kalshi": 0.1664, "model_brier": 0.2148, "kalshi_brier": 0.2061, "brier_diff_model_minus_kalshi": 0.0086, "brier_diff_se": 0.0021, "model_logloss": 0.6185, "kalshi_logloss": 0.5952}, "gen1_elo": {"n": 5586, "model": {"intercept": -0.385, "slope": 0.998, "slope_se": 0.036}, "kalshi_mid_same_rows": {"intercept": 0.309, "slope": 1.091, "slope_se": 0.038}, "mean_extremity_model": 0.1756, "mean_extremity_kalshi": 0.1666, "model_brier": 0.2135, "kalshi_brier": 0.2063, "brier_diff_model_minus_kalshi": 0.0072, "brier_diff_se": 0.0021, "model_logloss": 0.6159, "kalshi_logloss": 0.5955}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2481, "share_ge_15": 0.4432, "median_abs_gap": 13.02, "n": 39237}, "gen1_elo": {"share_ge_25": 0.2463, "share_ge_15": 0.4411, "median_abs_gap": 12.93, "n": 39237}, "gen1_sr": {"share_ge_25": 0.3135, "share_ge_15": 0.5206, "median_abs_gap": 15.87, "n": 39237}, "gen2": {"share_ge_25": 0.3164, "share_ge_15": 0.5105, "median_abs_gap": 15.48, "n": 39237}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1536, "share_ge_15": 0.3557, "median_abs_gap": 10.74, "n": 30420}, "gen1_elo": {"share_ge_25": 0.1537, "share_ge_15": 0.3526, "median_abs_gap": 10.55, "n": 30419}, "gen1_sr": {"share_ge_25": 0.2186, "share_ge_15": 0.4421, "median_abs_gap": 13.03, "n": 30422}, "gen2": {"share_ge_25": 0.2349, "share_ge_15": 0.4414, "median_abs_gap": 12.94, "n": 30422}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.84, "share_ge_25_all": 0.0422, "share_ge_25_pregame_clean": 0.0377}, "WTA": {"median_abs_gap_pregame_clean": 7.54, "share_ge_25_all": 0.0574, "share_ge_25_pregame_clean": 0.049}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2365, "share_within_10pp_all": 0.4374, "share_within_10pp_pregame_clean": 0.4896, "corr_model_vs_mid_pregame_clean": 0.8503}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 816, "model_brier": 0.1985, "kalshi_brier": 0.199, "brier_diff_model_minus_kalshi": -0.0005}, "10-15": {"n_settled": 982, "model_brier": 0.2209, "kalshi_brier": 0.2123, "brier_diff_model_minus_kalshi": 0.0086}, "15-25": {"n_settled": 1238, "model_brier": 0.2247, "kalshi_brier": 0.2121, "brier_diff_model_minus_kalshi": 0.0126}, "25-40": {"n_settled": 722, "model_brier": 0.2225, "kalshi_brier": 0.2069, "brier_diff_model_minus_kalshi": 0.0156}, "3-5": {"n_settled": 508, "model_brier": 0.2067, "kalshi_brier": 0.2069, "brier_diff_model_minus_kalshi": -0.0002}, "40+": {"n_settled": 151, "model_brier": 0.2818, "kalshi_brier": 0.1882, "brier_diff_model_minus_kalshi": 0.0936}, "5-10": {"n_settled": 1169, "model_brier": 0.2005, "kalshi_brier": 0.2012, "brier_diff_model_minus_kalshi": -0.0007}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.532, "slope": 0.807, "slope_se": 0.034}, "kalshi_slope": {"intercept": 0.196, "slope": 1.053, "slope_se": 0.038}, "n": 5586}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.489, "slope": 0.859, "slope_se": 0.027}, "kalshi_slope": {"intercept": 0.167, "slope": 1.058, "slope_se": 0.031}, "n": 7731}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 504, "model_brier": 0.3062, "kalshi_brier": 0.2386, "brier_diff_model_minus_kalshi": 0.0676, "brier_diff_se": 0.0133, "corr_model_outcome": 0.0646, "corr_kalshi_outcome": 0.229}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
