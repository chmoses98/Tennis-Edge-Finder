# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-10T19:59Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 87,079): 0-3 14.0%, 3-5 9.6%, 5-10 20.2%, 10-15 15.2%, 15-25 19.1%, 25-40 13.7%, 40+ 8.2%; median gap 11.86 pp.
* **Where the extremes live**: 97.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 78.0%, Challenger 11.2%, doubles 6.5%). Main tour: ATP 3.8% and WTA 5.9% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 19,086): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.6%, STALE_QUOTE 20.1%, BOOK_QUALITY 16.8%, POOR_DATA 9.2%, POSSIBLY_IN_PLAY_QUOTE 5.7%, IDENTITY_AMBIGUOUS 4.3%, IN_PLAY_QUOTE 3.4%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.8%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.6%, market_freshness 20.1%, execution 16.8%, data 12.5%, market_freshness/coverage 9.1%, mapping 4.3%, model_calibration_or_unknown 1.8%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 54.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.7% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 19,086 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.9% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 27.3% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 480.0 points vs 1716.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.015, Gen-2 0.813, Gen-1 ledger 0.863 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 961 model 0.2263 vs Kalshi 0.2049; n 196 model 0.3016 vs Kalshi 0.1723.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 364,960 model-market comparisons (601,153 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 120,982 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-10T19:38:22.333133+00:00'], shadow board 100,356 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-10T19:38:27.034372+00:00'], Model 4 43,751 rows, 30,021 settled tickers, 11,250 tickers with an external scan.
* By model: {"gen1_ledger": 81168, "gen1_elo": 50434, "fair_v1": 50434, "gen2": 50434, "gen1_sr": 50434, "model4_fundamental": 41070, "model4_conditioned": 40986}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 87,079 | 14.0 | 9.6 | 20.2 | 15.2 | 19.1 | 13.7 | 8.2 | 11.86 | 41.0% | 21.9% |
| MW fair_v1 | 50,434 | 12.7 | 8.6 | 18.8 | 15.2 | 19.6 | 15.0 | 10.2 | 13.1 | 44.7% | 25.1% |
| MW gen1_elo | 50,434 | 12.5 | 8.8 | 19.2 | 15.3 | 19.4 | 14.9 | 10.0 | 12.93 | 44.2% | 24.9% |
| MW gen1_ledger | 36,645 | 15.8 | 10.9 | 22.2 | 15.1 | 18.6 | 11.9 | 5.6 | 10.27 | 36.0% | 17.5% |
| MW gen1_sr | 50,434 | 10.0 | 7.2 | 16.7 | 13.9 | 20.8 | 18.7 | 12.7 | 15.89 | 52.2% | 31.4% |
| MW gen2 | 50,434 | 10.9 | 7.6 | 16.7 | 13.7 | 19.6 | 17.7 | 13.8 | 15.47 | 51.1% | 31.5% |
| all families model4_conditioned | 40,986 | 22.2 | 17.9 | 34.5 | 17.0 | 5.0 | 2.2 | 1.2 | 6.07 | 8.4% | 3.4% |
| all families model4_fundamental | 41,070 | 17.3 | 13.5 | 34.0 | 19.9 | 9.9 | 3.8 | 1.5 | 7.61 | 15.3% | 5.3% |

Configurable thresholds (primary): >=5pp 76.4%, >=10pp 56.2%, >=15pp 41.0%, >=20pp 30.3%, >=25pp 21.9%, >=30pp 15.8%, >=40pp 8.2%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.47pp; >=10pp 45.3%, >=25pp 17.3%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,083 | 28.1 | 15.7 | 28.0 | 13.3 | 10.7 | 3.6 | 0.6 | 5.84 | 14.9% | 4.2% |
| CHALLENGER | 8,017 | 16.3 | 9.6 | 20.6 | 15.2 | 16.0 | 11.4 | 10.9 | 10.91 | 38.2% | 22.3% |
| ITF_MEN | 14,408 | 9.7 | 7.3 | 17.0 | 14.9 | 21.2 | 17.3 | 12.7 | 15.45 | 51.2% | 30.0% |
| ITF_WOMEN | 19,511 | 9.5 | 7.0 | 16.1 | 14.7 | 22.1 | 18.6 | 12.0 | 15.95 | 52.6% | 30.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,082 | 16.7 | 13.2 | 25.1 | 20.7 | 16.5 | 6.8 | 1.1 | 8.6 | 24.3% | 7.8% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,083 | 26.4 | 15.7 | 26.2 | 15.8 | 11.2 | 3.9 | 0.8 | 6.09 | 16.0% | 4.7% |
| CHALLENGER | 8,017 | 14.5 | 9.1 | 19.1 | 13.8 | 18.5 | 13.6 | 11.4 | 12.49 | 43.6% | 25.0% |
| ITF_MEN | 14,408 | 8.0 | 6.2 | 15.0 | 13.8 | 20.2 | 20.3 | 16.5 | 17.94 | 57.0% | 36.8% |
| ITF_WOMEN | 19,511 | 7.9 | 5.9 | 14.2 | 12.7 | 20.6 | 21.2 | 17.6 | 19.06 | 59.4% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,082 | 14.1 | 10.4 | 21.7 | 16.2 | 22.4 | 12.8 | 2.5 | 11.19 | 37.6% | 15.2% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,083 | 23.2 | 14.1 | 25.7 | 15.5 | 14.4 | 6.0 | 1.1 | 7.08 | 21.6% | 7.1% |
| CHALLENGER | 8,017 | 15.0 | 9.6 | 20.8 | 15.5 | 16.2 | 11.9 | 10.8 | 11.29 | 39.0% | 22.8% |
| ITF_MEN | 14,408 | 9.4 | 7.2 | 17.1 | 14.2 | 21.6 | 17.4 | 13.0 | 15.82 | 52.1% | 30.4% |
| ITF_WOMEN | 19,511 | 9.3 | 6.9 | 16.4 | 15.7 | 22.0 | 18.5 | 11.3 | 15.6 | 51.9% | 29.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,082 | 22.6 | 17.1 | 31.9 | 15.3 | 8.8 | 3.2 | 1.0 | 6.12 | 13.1% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,459 | 28.0 | 19.5 | 29.2 | 12.2 | 8.1 | 2.6 | 0.5 | 5.27 | 11.1% | 3.0% |
| CHALLENGER | 4,944 | 22.7 | 14.5 | 28.0 | 14.7 | 13.2 | 5.5 | 1.5 | 7.03 | 20.2% | 7.0% |
| DOUBLES | 2,675 | 4.9 | 4.5 | 12.9 | 11.0 | 20.5 | 24.6 | 21.7 | 23.15 | 66.7% | 46.2% |
| ITF_MEN | 10,667 | 12.7 | 9.5 | 21.3 | 15.6 | 21.8 | 13.0 | 6.1 | 11.87 | 40.9% | 19.1% |
| ITF_WOMEN | 12,682 | 13.5 | 9.3 | 19.8 | 15.7 | 21.5 | 14.7 | 5.5 | 12.18 | 41.7% | 20.1% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,813 | 24.1 | 16.0 | 31.4 | 16.9 | 8.9 | 2.5 | 0.2 | 6.46 | 11.6% | 2.8% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,956 | 28.5 | 15.9 | 28.4 | 13.2 | 10.5 | 3.1 | 0.3 | 5.67 | 13.9% | 3.4% |
| CHALLENGER | 5,656 | 21.0 | 12.0 | 25.7 | 17.9 | 16.0 | 5.8 | 1.6 | 8.2 | 23.4% | 7.4% |
| ITF_MEN | 10,538 | 11.9 | 8.6 | 20.4 | 17.2 | 22.2 | 14.2 | 5.5 | 12.52 | 41.9% | 19.7% |
| ITF_WOMEN | 14,303 | 11.4 | 8.6 | 19.0 | 17.0 | 24.0 | 15.3 | 4.8 | 13.15 | 44.1% | 20.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,968 | 17.0 | 13.2 | 25.4 | 21.1 | 16.5 | 6.2 | 0.6 | 8.43 | 23.3% | 6.8% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,956 | 26.8 | 16.0 | 26.5 | 15.7 | 11.2 | 3.5 | 0.4 | 6.0 | 15.0% | 3.9% |
| CHALLENGER | 5,656 | 18.3 | 11.6 | 23.9 | 16.2 | 19.1 | 9.2 | 1.8 | 8.97 | 30.1% | 11.0% |
| ITF_MEN | 10,539 | 9.5 | 7.3 | 17.5 | 15.9 | 22.1 | 18.5 | 9.2 | 14.95 | 49.8% | 27.7% |
| ITF_WOMEN | 14,304 | 9.0 | 7.0 | 16.0 | 14.3 | 22.5 | 20.6 | 10.7 | 16.51 | 53.8% | 31.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,968 | 14.3 | 10.5 | 22.0 | 16.4 | 22.5 | 12.4 | 1.9 | 11.03 | 36.8% | 14.3% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,391 | 28.2 | 19.7 | 29.2 | 12.4 | 7.8 | 2.3 | 0.3 | 5.23 | 10.5% | 2.7% |
| CHALLENGER | 4,379 | 24.0 | 15.3 | 29.2 | 14.8 | 12.5 | 3.8 | 0.4 | 6.58 | 16.7% | 4.2% |
| DOUBLES | 2,508 | 4.7 | 4.5 | 13.1 | 11.1 | 20.3 | 24.5 | 21.7 | 23.07 | 66.5% | 46.2% |
| ITF_MEN | 9,224 | 13.5 | 10.1 | 22.8 | 16.1 | 21.8 | 11.6 | 4.2 | 11.05 | 37.6% | 15.8% |
| ITF_WOMEN | 10,925 | 14.2 | 9.8 | 20.8 | 16.2 | 21.7 | 13.6 | 3.7 | 11.42 | 39.0% | 17.3% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,750 | 24.4 | 16.4 | 31.4 | 16.9 | 8.9 | 2.0 | 0.1 | 6.42 | 10.9% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,675 | 4.9 | 4.5 | 12.9 | 11.0 | 20.5 | 24.6 | 21.7 | 23.15 | 66.7% | 46.2% |
| singles | 33,970 | 16.7 | 11.4 | 22.9 | 15.4 | 18.4 | 10.9 | 4.3 | 9.74 | 33.6% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 10,586 | 12.8 | 9.0 | 19.6 | 15.3 | 19.6 | 14.2 | 9.6 | 12.73 | 43.4% | 23.8% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 32,924 | 13.2 | 8.7 | 18.9 | 15.1 | 19.1 | 15.0 | 10.1 | 12.94 | 44.2% | 25.1% |
| UNKNOWN | 6,511 | 10.4 | 7.5 | 17.0 | 16.4 | 21.6 | 15.9 | 11.2 | 14.48 | 48.8% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 14,263 | 19.3 | 11.8 | 22.5 | 15.8 | 14.8 | 9.4 | 6.3 | 8.98 | 30.6% | 15.7% |
| B | 6,125 | 12.8 | 8.4 | 19.7 | 15.3 | 19.7 | 12.5 | 11.5 | 12.83 | 43.7% | 24.0% |
| C | 7,116 | 12.1 | 8.7 | 19.5 | 15.8 | 18.8 | 14.6 | 10.6 | 12.92 | 43.9% | 25.1% |
| D | 8,148 | 11.6 | 8.4 | 17.8 | 15.1 | 22.0 | 15.7 | 9.5 | 13.96 | 47.1% | 25.2% |
| F | 14,782 | 7.3 | 5.6 | 14.9 | 14.4 | 23.1 | 21.1 | 13.5 | 17.99 | 57.7% | 34.6% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,754 | 24.9 | 16.0 | 29.0 | 14.9 | 10.6 | 3.4 | 1.2 | 6.34 | 15.2% | 4.7% |
| B | 5,039 | 16.6 | 10.9 | 24.3 | 16.8 | 18.9 | 9.4 | 3.0 | 9.59 | 31.3% | 12.4% |
| C | 7,170 | 11.0 | 7.8 | 19.6 | 14.8 | 21.1 | 15.5 | 10.2 | 13.54 | 46.8% | 25.7% |
| D | 5,518 | 14.5 | 10.1 | 21.0 | 15.3 | 20.9 | 12.7 | 5.5 | 11.28 | 39.0% | 18.1% |
| F | 9,164 | 10.2 | 8.3 | 16.4 | 14.5 | 23.4 | 19.1 | 8.1 | 15.32 | 50.6% | 27.2% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 16,145 | 17.7 | 10.8 | 21.5 | 15.6 | 15.2 | 10.1 | 9.1 | 9.99 | 34.4% | 19.2% |
| LIMITED | 10,963 | 13.6 | 9.5 | 20.5 | 15.9 | 19.5 | 13.3 | 7.7 | 11.91 | 40.5% | 21.0% |
| POOR | 23,326 | 8.9 | 6.6 | 16.0 | 14.7 | 22.6 | 19.1 | 12.1 | 16.3 | 53.8% | 31.1% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,190 | 23.6 | 18.1 | 33.0 | 15.5 | 6.4 | 3.0 | 0.4 | 5.9 | 9.8% | 3.4% |
| GAME_SPREAD | 6,875 | 22.9 | 15.3 | 32.0 | 16.8 | 9.0 | 3.3 | 0.7 | 6.69 | 13.0% | 4.0% |
| MATCH_WINNER | 36,645 | 15.8 | 10.9 | 22.2 | 15.1 | 18.6 | 11.9 | 5.6 | 10.27 | 36.0% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 16,920 | 28.3 | 16.8 | 30.8 | 12.6 | 8.9 | 2.4 | 0.3 | 5.58 | 11.6% | 2.7% |
| TOTAL_GAMES | 11,514 | 9.7 | 10.8 | 36.1 | 25.8 | 10.5 | 4.2 | 2.9 | 9.15 | 17.6% | 7.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,577 | 24.4 | 28.7 | 33.3 | 8.1 | 4.0 | 1.2 | 0.3 | 4.8 | 5.4% | 1.5% |
| GAME_SPREAD | 9,476 | 46.8 | 15.9 | 25.1 | 7.4 | 2.3 | 1.9 | 0.6 | 3.31 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,933 | 6.6 | 9.8 | 40.7 | 29.9 | 7.3 | 3.3 | 2.4 | 9.17 | 13.0% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,613 | 23.8 | 16.6 | 34.6 | 14.8 | 6.9 | 2.7 | 0.5 | 6.06 | 10.2% | 3.2% |
| GAME_SPREAD | 9,485 | 20.4 | 13.4 | 28.4 | 20.1 | 12.1 | 4.4 | 1.2 | 7.66 | 17.6% | 5.5% |
| TOTAL_GAMES | 16,972 | 10.0 | 10.8 | 36.5 | 24.3 | 11.3 | 4.4 | 2.6 | 9.02 | 18.4% | 7.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 50,434 | 44.7% | 25.1% | 13.1 | 35.5% | 15.2% | 10.7 |
| gen1_elo | 50,434 | 44.2% | 24.9% | 12.93 | 34.9% | 15.0% | 10.49 |
| gen1_sr | 50,434 | 52.2% | 31.4% | 15.89 | 43.9% | 21.6% | 12.97 |
| gen2 | 50,434 | 51.1% | 31.5% | 15.47 | 43.9% | 23.1% | 12.83 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,098 | 15.5 | 10.4 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 30,336 | 10.9 | 7.4 | 17.0 | 13.9 | 19.2 | 17.0 | 14.6 | 15.34 | 50.8% | 31.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 30,113 | 16.4 | 11.2 | 22.7 | 15.2 | 18.1 | 11.5 | 5.0 | 9.94 | 34.6% | 16.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 87,079 | 30113 | 23570 | 33396 | 25.0 | 134.3 | 1451.1 |
| ge_15pp | 35,744 | 10413 | 8394 | 16937 | 28.8 | 440.2 | 1451.1 |
| ge_25pp | 19,086 | 4954 | 3666 | 10466 | 34.4 | 588.1 | 1431.1 |
| lt_10pp | 38,114 | 15127 | 11149 | 11838 | 22.8 | 49.5 | 1421.7 |

Current slate `SL-20261110T195940Z-4985242e`: 568 priced rows, quote age at build {'median': 63.4, 'max': 93.4}, freshness {'STALE': 568}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 51 | 0.0 | 0.0 | 35.3 | 9.8 | 31.4 | 19.6 | 3.9 | 18.34 | 54.9% | 23.5% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,861 | 19.3 | 11.0 | 25.5 | 18.1 | 17.9 | 7.3 | 0.9 | 8.78 | 26.1% | 8.2% |
| KALSHI_LONE_OUTLIER | 32 | 6.2 | 6.2 | 75.0 | 6.2 | 3.1 | 3.1 | 0.0 | 6.16 | 6.2% | 3.1% |
| MARKETS_AGREE | 1,063 | 66.5 | 33.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,261 | 0.0 | 2.2 | 38.5 | 25.9 | 23.8 | 8.8 | 0.9 | 11.65 | 33.4% | 9.6% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 50,434 | 8297 (16.4%) | 27.3% | 1.0% | {"EXTERNAL_STALE": 4861, "AGREES_WITH_KALSHI": 2261, "ALL_AGREE": 1063, "SUPPORTS_MODEL_DIRECTION": 49, "AGREES_WITH_MODEL": 32, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 22,532 | 2054 (9.1%) | 36.8% | 1.5% | {"EXTERNAL_STALE": 1269, "AGREES_WITH_KALSHI": 755, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 12,670 | 630 (5.0%) | 34.6% | 2.1% | {"EXTERNAL_STALE": 399, "AGREES_WITH_KALSHI": 218, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,880 | 599 (10.2%) | 35.2% | 2.2% | {"EXTERNAL_STALE": 375, "AGREES_WITH_KALSHI": 211, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 20,218 | 4771 (23.6%) | 19.3% | 0.9% | {"EXTERNAL_STALE": 2713, "ALL_AGREE": 1063, "AGREES_WITH_KALSHI": 920, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 28, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 9,867 | 10.7 | 7.6 | 19.1 | 14.3 | 21.6 | 16.4 | 10.2 | 14.21 | 48.2% | 26.6% |
| 4-10x | 6,715 | 11.1 | 8.6 | 18.0 | 14.9 | 21.9 | 14.7 | 10.7 | 14.04 | 47.4% | 25.4% |
| <2x | 25,827 | 14.7 | 9.7 | 19.9 | 15.9 | 17.5 | 13.2 | 9.0 | 11.58 | 39.7% | 22.2% |
| >=10x | 8,025 | 10.2 | 6.4 | 15.1 | 14.3 | 21.6 | 19.0 | 13.3 | 16.51 | 54.0% | 32.3% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 13,279 | 12.5 | 8.5 | 19.8 | 16.1 | 19.0 | 13.6 | 10.5 | 12.78 | 43.1% | 24.1% |
| 300-1000 | 10,820 | 11.7 | 8.8 | 17.8 | 15.0 | 20.8 | 16.3 | 9.6 | 13.77 | 46.7% | 25.9% |
| <300 | 15,920 | 8.2 | 5.8 | 15.1 | 14.5 | 22.8 | 20.2 | 13.5 | 17.39 | 56.4% | 33.6% |
| >=3000 | 10,415 | 21.1 | 12.8 | 24.1 | 15.4 | 14.0 | 7.4 | 5.2 | 7.83 | 26.6% | 12.6% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1531 | 0.5497 | 0.4109 | 0.4801 | +0.070 | -0.069 | 0.0038 ± 0.0039 |
| ratio 4-10x | 1038 | 0.5769 | 0.4318 | 0.4855 | +0.091 | -0.054 | 0.0102 ± 0.005 |
| ratio <2x | 3760 | 0.5366 | 0.4143 | 0.4367 | +0.100 | -0.022 | 0.0146 ± 0.0023 |
| ratio >=10x | 1277 | 0.5652 | 0.3927 | 0.4417 | +0.124 | -0.049 | 0.0171 ± 0.005 |
| thinner_sample 1000-3000 | 2109 | 0.5411 | 0.4141 | 0.4467 | +0.095 | -0.033 | 0.0123 ± 0.0032 |
| thinner_sample 300-1000 | 1696 | 0.566 | 0.4258 | 0.4735 | +0.093 | -0.048 | 0.0059 ± 0.0038 |
| thinner_sample <300 | 2478 | 0.5571 | 0.3899 | 0.4492 | +0.108 | -0.059 | 0.015 ± 0.0035 |
| thinner_sample >=3000 | 1323 | 0.5278 | 0.4344 | 0.4437 | +0.084 | -0.009 | 0.0151 ± 0.0031 |
| data_status ADEQUATE | 2110 | 0.5316 | 0.429 | 0.4384 | +0.093 | -0.009 | 0.0157 ± 0.0026 |
| data_status LIMITED | 1856 | 0.5499 | 0.417 | 0.4661 | +0.084 | -0.049 | 0.0081 ± 0.0035 |
| data_status POOR | 3640 | 0.5598 | 0.4003 | 0.4547 | +0.105 | -0.054 | 0.0124 ± 0.0028 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1105 | 0.1977 | 0.198 | -0.0003 ± 0.0005 | 0.5754 | 0.5762 | 0.5043 | 0.4891 | 0.5032 | -0.093 ± 0.0142 | -0.0087 (8) |
| 3-5 | 698 | 0.2062 | 0.2057 | +0.0005 ± 0.0014 | 0.5976 | 0.5947 | 0.5046 | 0.4648 | 0.4785 | -0.101 ± 0.0177 | 0.01 (3) |
| 5-10 | 1638 | 0.2042 | 0.2025 | +0.0017 ± 0.0017 | 0.5954 | 0.5889 | 0.5123 | 0.4384 | 0.4621 | -0.095 ± 0.0115 | -0.0143 (7) |
| 10-15 | 1322 | 0.2193 | 0.2095 | +0.0099 ± 0.0031 | 0.6305 | 0.6026 | 0.5253 | 0.4019 | 0.4228 | -0.110 ± 0.0128 | -0.055 (6) |
| 15-25 | 1686 | 0.2267 | 0.2079 | +0.0187 ± 0.0043 | 0.6486 | 0.5991 | 0.575 | 0.3804 | 0.43 | -0.106 ± 0.0112 | -0.0045 (11) |
| 25-40 | 961 | 0.2263 | 0.2049 | +0.0214 ± 0.0087 | 0.6433 | 0.5906 | 0.6498 | 0.3402 | 0.4599 | -0.072 ± 0.0136 | -0.06 (2) |
| 40+ | 196 | 0.3016 | 0.1723 | +0.1293 ± 0.0267 | 0.8096 | 0.5164 | 0.7299 | 0.2741 | 0.3673 | -0.088 ± 0.0257 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5666 | 0.1867 | 0.1876 | -0.0009 ± 0.0002 | 0.5499 | 0.551 | 0.4917 | 0.4764 | 0.5097 | -0.019 ± 0.0058 | -0.01 (28) |
| 3-5 | 3756 | 0.1987 | 0.1969 | +0.0019 ± 0.0006 | 0.5784 | 0.5718 | 0.4825 | 0.4427 | 0.439 | -0.058 ± 0.0073 | 0.005 (6) |
| 5-10 | 8284 | 0.2018 | 0.1978 | +0.0040 ± 0.0007 | 0.5896 | 0.5765 | 0.484 | 0.4102 | 0.42 | -0.049 ± 0.0049 | -0.0114 (22) |
| 10-15 | 6749 | 0.2026 | 0.1863 | +0.0162 ± 0.0013 | 0.5919 | 0.5467 | 0.4856 | 0.3618 | 0.3586 | -0.065 ± 0.0053 | -0.0379 (19) |
| 15-25 | 8613 | 0.2068 | 0.167 | +0.0398 ± 0.0017 | 0.6056 | 0.4962 | 0.4993 | 0.3037 | 0.3006 | -0.070 ± 0.0044 | -0.0043 (51) |
| 25-40 | 6771 | 0.2242 | 0.1246 | +0.0996 ± 0.0027 | 0.6428 | 0.3841 | 0.5261 | 0.2123 | 0.2143 | -0.062 ± 0.0042 | -0.0733 (3) |
| 40+ | 4599 | 0.3817 | 0.0432 | +0.3384 ± 0.0035 | 0.9938 | 0.1686 | 0.6293 | 0.1009 | 0.0563 | -0.076 ± 0.0029 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 884 | 0.2052 | 0.2056 | -0.0004 ± 0.0005 | 0.5913 | 0.5925 | 0.5082 | 0.4933 | 0.5192 | -0.098 ± 0.0163 | -0.0117 (6) |
| 3-5 | 628 | 0.2117 | 0.2089 | +0.0028 ± 0.0015 | 0.6063 | 0.6005 | 0.5164 | 0.4769 | 0.4586 | -0.129 ± 0.0197 | 0.01 (3) |
| 5-10 | 1405 | 0.2078 | 0.2056 | +0.0021 ± 0.0018 | 0.6021 | 0.5963 | 0.5403 | 0.4658 | 0.4911 | -0.090 ± 0.0125 | -0.01 (4) |
| 10-15 | 1226 | 0.215 | 0.2071 | +0.0079 ± 0.0033 | 0.623 | 0.6001 | 0.5607 | 0.4364 | 0.4698 | -0.107 ± 0.0136 | -0.04 (5) |
| 15-25 | 1777 | 0.2324 | 0.2117 | +0.0207 ± 0.0043 | 0.661 | 0.6075 | 0.5863 | 0.3906 | 0.4367 | -0.104 ± 0.0112 | -0.0183 (12) |
| 25-40 | 1244 | 0.2689 | 0.1995 | +0.0694 ± 0.008 | 0.7491 | 0.5793 | 0.6607 | 0.3467 | 0.3955 | -0.118 ± 0.0127 | -0.008 (5) |
| 40+ | 442 | 0.3723 | 0.162 | +0.2103 ± 0.0191 | 1.0155 | 0.4899 | 0.7353 | 0.2474 | 0.2896 | -0.089 ± 0.0185 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4845 | 0.1911 | 0.1912 | -0.0002 ± 0.0002 | 0.5577 | 0.5578 | 0.5077 | 0.4926 | 0.5067 | -0.041 ± 0.0065 | -0.0154 (26) |
| 3-5 | 3319 | 0.1932 | 0.1922 | +0.0010 ± 0.0006 | 0.5631 | 0.5599 | 0.5119 | 0.4723 | 0.4794 | -0.045 ± 0.0078 | 0.01 (5) |
| 5-10 | 7365 | 0.197 | 0.1937 | +0.0033 ± 0.0008 | 0.5788 | 0.5665 | 0.5076 | 0.4334 | 0.4511 | -0.039 ± 0.0052 | -0.0117 (6) |
| 10-15 | 6089 | 0.2039 | 0.1915 | +0.0124 ± 0.0014 | 0.5979 | 0.56 | 0.5093 | 0.3854 | 0.3983 | -0.052 ± 0.0057 | -0.0189 (18) |
| 15-25 | 8699 | 0.2168 | 0.1798 | +0.0370 ± 0.0018 | 0.6309 | 0.5282 | 0.5246 | 0.3291 | 0.3343 | -0.063 ± 0.0046 | -0.014 (52) |
| 25-40 | 7897 | 0.2517 | 0.1379 | +0.1138 ± 0.0027 | 0.7104 | 0.4208 | 0.5608 | 0.2435 | 0.2267 | -0.079 ± 0.0042 | -0.0095 (20) |
| 40+ | 6224 | 0.4026 | 0.059 | +0.3436 ± 0.0035 | 1.0608 | 0.2122 | 0.6546 | 0.1184 | 0.0797 | -0.074 ± 0.003 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1082 | 0.1963 | 0.1975 | -0.0012 ± 0.0005 | 0.5723 | 0.5751 | 0.5023 | 0.4868 | 0.5268 | -0.059 ± 0.0141 | -0.0191 (11) |
| 3-5 | 764 | 0.2081 | 0.2065 | +0.0017 ± 0.0013 | 0.6034 | 0.5976 | 0.4987 | 0.4591 | 0.4594 | -0.114 ± 0.0172 | 0.002 (5) |
| 5-10 | 1655 | 0.2042 | 0.2003 | +0.0039 ± 0.0017 | 0.5942 | 0.5832 | 0.513 | 0.4393 | 0.4489 | -0.107 ± 0.0113 | -0.01 (10) |
| 10-15 | 1348 | 0.2128 | 0.2035 | +0.0093 ± 0.003 | 0.6158 | 0.5896 | 0.5389 | 0.4157 | 0.4414 | -0.108 ± 0.0124 | -0.0286 (7) |
| 15-25 | 1609 | 0.2318 | 0.212 | +0.0197 ± 0.0045 | 0.6612 | 0.6081 | 0.585 | 0.3909 | 0.4369 | -0.110 ± 0.0115 | -0.03 (1) |
| 25-40 | 942 | 0.2171 | 0.2098 | +0.0073 ± 0.0088 | 0.6243 | 0.6018 | 0.6583 | 0.3476 | 0.4894 | -0.060 ± 0.0137 | -0.0267 (3) |
| 40+ | 206 | 0.3107 | 0.1798 | +0.1309 ± 0.0266 | 0.8393 | 0.5322 | 0.7403 | 0.2852 | 0.3786 | -0.087 ± 0.0272 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5477 | 0.1859 | 0.1864 | -0.0005 ± 0.0002 | 0.5475 | 0.548 | 0.4858 | 0.4704 | 0.4858 | -0.036 ± 0.0059 | -0.0189 (44) |
| 3-5 | 3905 | 0.2045 | 0.2026 | +0.0019 ± 0.0006 | 0.5943 | 0.5878 | 0.481 | 0.4415 | 0.4379 | -0.058 ± 0.0073 | -0.0073 (22) |
| 5-10 | 8386 | 0.197 | 0.1917 | +0.0053 ± 0.0007 | 0.5778 | 0.5612 | 0.4866 | 0.4125 | 0.4135 | -0.056 ± 0.0048 | -0.0117 (42) |
| 10-15 | 6743 | 0.1953 | 0.1801 | +0.0152 ± 0.0013 | 0.5757 | 0.5322 | 0.4961 | 0.3728 | 0.3728 | -0.062 ± 0.0052 | -0.0136 (14) |
| 15-25 | 8682 | 0.212 | 0.1718 | +0.0402 ± 0.0017 | 0.6177 | 0.5072 | 0.5113 | 0.3168 | 0.3117 | -0.072 ± 0.0044 | -0.0533 (3) |
| 25-40 | 6715 | 0.2182 | 0.1248 | +0.0933 ± 0.0027 | 0.6299 | 0.384 | 0.5274 | 0.2118 | 0.2235 | -0.053 ± 0.0042 | -0.02 (4) |
| 40+ | 4530 | 0.3894 | 0.0477 | +0.3417 ± 0.0037 | 1.0148 | 0.1798 | 0.6375 | 0.1065 | 0.0629 | -0.076 ± 0.0031 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1528 | 0.1977 | 0.1975 | +0.0002 ± 0.0004 | 0.5741 | 0.5736 | 0.51 | 0.4949 | 0.4954 | -0.072 ± 0.0116 | -0.0221 (56) |
| 3-5 | 1085 | 0.1889 | 0.1891 | -0.0002 ± 0.0011 | 0.5558 | 0.5546 | 0.4986 | 0.4587 | 0.4793 | -0.054 ± 0.0135 | -0.0194 (34) |
| 5-10 | 2187 | 0.2002 | 0.1951 | +0.0051 ± 0.0014 | 0.5902 | 0.5735 | 0.5083 | 0.4348 | 0.4371 | -0.079 ± 0.0097 | -0.005 (78) |
| 10-15 | 1509 | 0.2156 | 0.2028 | +0.0128 ± 0.0029 | 0.6254 | 0.5891 | 0.5425 | 0.4198 | 0.4274 | -0.093 ± 0.0119 | 0.0012 (66) |
| 15-25 | 1969 | 0.2315 | 0.208 | +0.0235 ± 0.004 | 0.6606 | 0.6 | 0.5922 | 0.3973 | 0.4358 | -0.091 ± 0.0104 | -0.0214 (59) |
| 25-40 | 1168 | 0.2423 | 0.2108 | +0.0315 ± 0.0082 | 0.6911 | 0.6046 | 0.6892 | 0.3772 | 0.4829 | -0.089 ± 0.0127 | -0.0252 (27) |
| 40+ | 424 | 0.3275 | 0.1983 | +0.1292 ± 0.0207 | 0.94 | 0.5789 | 0.8153 | 0.3392 | 0.4575 | -0.099 ± 0.0193 | -0.1137 (8) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5545 | 0.1781 | 0.1782 | -0.0001 ± 0.0002 | 0.5269 | 0.5265 | 0.512 | 0.4968 | 0.5053 | -0.040 ± 0.0057 | -0.0154 (103) |
| 3-5 | 3838 | 0.1949 | 0.1942 | +0.0008 ± 0.0006 | 0.5689 | 0.5665 | 0.5023 | 0.4625 | 0.4729 | -0.040 ± 0.0072 | -0.0212 (73) |
| 5-10 | 7763 | 0.1978 | 0.1911 | +0.0067 ± 0.0007 | 0.5832 | 0.5626 | 0.5022 | 0.4287 | 0.4207 | -0.064 ± 0.005 | -0.0084 (134) |
| 10-15 | 5331 | 0.2103 | 0.1939 | +0.0164 ± 0.0015 | 0.6123 | 0.5686 | 0.5361 | 0.4133 | 0.4063 | -0.073 ± 0.0061 | -0.0057 (111) |
| 15-25 | 6517 | 0.2319 | 0.1995 | +0.0325 ± 0.0022 | 0.6661 | 0.5781 | 0.5765 | 0.3812 | 0.3963 | -0.070 ± 0.0056 | -0.026 (108) |
| 25-40 | 4221 | 0.259 | 0.1907 | +0.0683 ± 0.0042 | 0.7317 | 0.555 | 0.6407 | 0.3282 | 0.3781 | -0.067 ± 0.0066 | -0.0277 (53) |
| 40+ | 1903 | 0.3708 | 0.1581 | +0.2128 ± 0.0094 | 1.0452 | 0.4716 | 0.7442 | 0.2441 | 0.2916 | -0.064 ± 0.0087 | -0.054 (15) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 7606 | 1.015 ± 0.032 | 1.094 | 0.1678 | 0.1677 | 0.2164 | 0.2041 |
| gen2 | 7606 | 0.813 ± 0.029 | 1.068 | 0.1733 | 0.1681 | 0.2343 | 0.204 |
| gen1_elo | 7606 | 1.001 ± 0.031 | 1.083 | 0.174 | 0.1679 | 0.2153 | 0.2042 |
| gen1_sr | 7606 | 0.997 ± 0.038 | 1.117 | 0.1332 | 0.1696 | 0.2303 | 0.2037 |
| gen1_ledger | 9870 | 0.863 ± 0.024 | 1.07 | 0.1894 | 0.1751 | 0.2176 | 0.2006 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 35,744)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 8,591 | 24.0% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 8,193 | 22.9% |
| BOOK_QUALITY | execution | 6,192 | 17.3% |
| POOR_DATA | data | 4,119 | 11.5% |
| LIMITED_DATA | data | 2,177 | 6.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 2,035 | 5.7% |
| IDENTITY_AMBIGUOUS | mapping | 1,471 | 4.1% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,404 | 3.9% |
| IN_PLAY_QUOTE | market_freshness/coverage | 993 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 568 | 1.6% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 24.0%, coverage 22.9%, data 17.6%, execution 17.3%, market_freshness/coverage 8.5%, mapping 4.1%, model_calibration_or_unknown 3.9%, model_calibration 1.6%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.6%, START_UNVERIFIABLE 94.8%, LOW_DATA_QUALITY 71.7%, THIN_PLAYER_HISTORY 59.9%, STALE_PLAYER_DATA 52.4%, STALE_KALSHI_QUOTE 47.4%, MODEL_INTERNAL_DISAGREEMENT 41.9%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 23.8%, MODEL_HIGH_UNCERTAINTY 18.5%, PLAYER_IDENTITY_RISK 15.1%, LEVEL_TRANSFER_RISK 9.7%, LOW_DISPLAYED_LIQUIDITY 8.4%, EVENT_MAPPING_RISK 7.0%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.2%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.3%, POST_SETTLEMENT_OBSERVATION 22.9%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 19,086)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,602 | 34.6% |
| STALE_QUOTE | market_freshness | 3,842 | 20.1% |
| BOOK_QUALITY | execution | 3,204 | 16.8% |
| POOR_DATA | data | 1,754 | 9.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,091 | 5.7% |
| IDENTITY_AMBIGUOUS | mapping | 822 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 649 | 3.4% |
| LIMITED_DATA | data | 639 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 344 | 1.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 138 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.6%, market_freshness 20.1%, execution 16.8%, data 12.5%, market_freshness/coverage 9.1%, mapping 4.3%, model_calibration_or_unknown 1.8%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.1%, START_UNVERIFIABLE 97.2%, LOW_DATA_QUALITY 74.9%, THIN_PLAYER_HISTORY 62.0%, STALE_KALSHI_QUOTE 54.8%, STALE_PLAYER_DATA 45.9%, MODEL_INTERNAL_DISAGREEMENT 42.0%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 23.0%, MODEL_HIGH_UNCERTAINTY 19.1%, PLAYER_IDENTITY_RISK 18.1%, LEVEL_TRANSFER_RISK 8.6%, EVENT_MAPPING_RISK 8.6%, LOW_DISPLAYED_LIQUIDITY 8.3%, MODEL_CALIBRATION_OUTLIER 4.7%, EXTERNAL_MARKET_REJECTION 1.8%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.5%, POST_SETTLEMENT_OBSERVATION 34.6%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 15285, "IDENTITY_AMBIGUOUS": 3801}; ticker orientation: {"VERIFIED": 19086}.

Checks: discipline:AMBIGUOUS 1237, discipline:PASS 17849, identity_confidence:AMBIGUOUS 3461, identity_confidence:PASS 15625, level_mapping:NA 1249, level_mapping:PASS 17837, market_pair:AMBIGUOUS 504, market_pair:NA 415, market_pair:PASS 18167, model_complement:NA 377, model_complement:PASS 18709, namesake:AMBIGUOUS 6, namesake:PASS 19080, physical_match_id:NA 6416, physical_match_id:PASS 12670, player_ids:PASS 19086, same_pair_other_event:PASS 19086, ticker_orientation:PASS 19086

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,542 | 3.8% | 3.1% | 1.3% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 24, "market_freshness/coverage": 22} | 5.49 | 0.2221 / 0.2177 (849) | 25.5% | 2.4% | 3.1% | 3.0% |
| CHALLENGER | 12,961 | 16.4% | 6.0% | 11.2% | {"coverage": 1295, "market_freshness": 259, "market_freshness/coverage": 234, "data": 164, "model_calibration_or_unknown": 81, "execution": 41, "model_calibration": 39, "mapping": 17, "possible_market_error": 1} | 7.35 | 0.2206 / 0.2095 (2989) | 41.0% | 14.0% | 4.0% | 22.6% |
| DOUBLES | 2,675 | 46.2% | 46.2% | 6.5% | {"execution": 685, "mapping": 368, "market_freshness": 106, "market_freshness/coverage": 71, "coverage": 7} | 23.07 | 0.299 / 0.2321 (657) | 8.8% | 0.0% | 100.0% | 6.2% |
| ITF_MEN | 25,075 | 25.4% | 17.9% | 33.3% | {"coverage": 2202, "market_freshness": 1319, "execution": 1026, "data": 955, "market_freshness/coverage": 624, "mapping": 224, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.82 | 0.2196 / 0.2003 (5195) | 41.2% | 69.8% | 15.0% | 21.2% |
| ITF_WOMEN | 32,193 | 26.5% | 18.9% | 44.6% | {"coverage": 3019, "market_freshness": 1897, "execution": 1369, "data": 1173, "market_freshness/coverage": 732, "mapping": 207, "model_calibration_or_unknown": 96, "model_calibration": 23} | 12.47 | 0.2038 / 0.1942 (6170) | 42.2% | 57.3% | 9.9% | 21.6% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,895 | 5.9% | 5.0% | 1.5% | {"market_freshness": 111, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.65 | 0.2307 / 0.2205 (804) | 30.2% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.5% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 523 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.4h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 509 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 852 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 164 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFMATCH-26NOV10KOUPOR-POR` | ITF_MEN | fair_v1 | 87% / 2% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 80 min (STALE); data POOR (grade D, thinner serve sample 1554.0, ratio 1.02); no external reference |
| 12 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 13 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 15 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 20.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 1203 min (STALE); no external reference |
| 16 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 17 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 18 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 19 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 20 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 21 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 22 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 23 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 24 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 25 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 26 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 573 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 27 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 28 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 29 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 30 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 31 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 32 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 33 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 34 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 35 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 36 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 37 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 38 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 39 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 40 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 41 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 43 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 44 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 45 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 46 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 47 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 48 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 49 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 124 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 50 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.972, "by_level_share_of_ge_25pp": {"ATP": 0.0128, "CHALLENGER": 0.1117, "DOUBLES": 0.0648, "ITF_MEN": 0.3333, "ITF_WOMEN": 0.4462, "OTHER": 0.0006, "WTA": 0.0152, "WTA125": 0.0154}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5484, "share_primary_cause_market_settled_or_in_play": 0.4371, "share_primary_cause_stale_quote_only": 0.2013}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 19086, "identity_ambiguous_share": 0.1992, "ticker_orientation": {"VERIFIED": 19086}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 12670, "with_external": 630, "coverage": 0.0497, "external_status": {"EXTERNAL_STALE": 399, "AGREES_WITH_KALSHI": 218, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 399, "MODEL_LONE_OUTLIER": 218, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.346, "share_external_supports_model": 0.0206}, "pregame_clean_ge_25pp": {"n": 5880, "with_external": 599, "coverage": 0.1019, "external_status": {"EXTERNAL_STALE": 375, "AGREES_WITH_KALSHI": 211, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 375, "MODEL_LONE_OUTLIER": 211, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3523, "share_external_supports_model": 0.0217}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 480.0, "median_sample_ratio": 2.44, "median_min_matches": 18.0, "median_max_days_since_last": 245.0, "share_severe_asymmetry": 0.208, "data_status": {"POOR": 10795, "LIMITED": 4843, "ADEQUATE": 3448}, "comparison_lt_10pp": {"median_thinner_serve_points": 1716.0, "median_sample_ratio": 1.7, "median_min_matches": 89.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1531, "model_minus_observed": 0.0696, "kalshi_minus_observed": -0.0692, "brier_diff_model_minus_kalshi": 0.0038}, "4-10x": {"n": 1038, "model_minus_observed": 0.0914, "kalshi_minus_observed": -0.0538, "brier_diff_model_minus_kalshi": 0.0102}, "<2x": {"n": 3760, "model_minus_observed": 0.0999, "kalshi_minus_observed": -0.0224, "brier_diff_model_minus_kalshi": 0.0146}, ">=10x": {"n": 1277, "model_minus_observed": 0.1236, "kalshi_minus_observed": -0.049, "brier_diff_model_minus_kalshi": 0.0171}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 7606, "model": {"intercept": -0.558, "slope": 0.813, "slope_se": 0.029}, "kalshi_mid_same_rows": {"intercept": 0.168, "slope": 1.068, "slope_se": 0.033}, "mean_extremity_model": 0.1733, "mean_extremity_kalshi": 0.1681, "model_brier": 0.2343, "kalshi_brier": 0.204, "brier_diff_model_minus_kalshi": 0.0302, "brier_diff_se": 0.0022, "model_logloss": 0.6664, "kalshi_logloss": 0.5905}, "fair_v1": {"n": 7606, "model": {"intercept": -0.456, "slope": 1.015, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.228, "slope": 1.094, "slope_se": 0.033}, "mean_extremity_model": 0.1678, "mean_extremity_kalshi": 0.1677, "model_brier": 0.2164, "kalshi_brier": 0.2041, "brier_diff_model_minus_kalshi": 0.0123, "brier_diff_se": 0.0018, "model_logloss": 0.6222, "kalshi_logloss": 0.5906}, "gen1_elo": {"n": 7606, "model": {"intercept": -0.448, "slope": 1.001, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.227, "slope": 1.083, "slope_se": 0.032}, "mean_extremity_model": 0.174, "mean_extremity_kalshi": 0.1679, "model_brier": 0.2153, "kalshi_brier": 0.2042, "brier_diff_model_minus_kalshi": 0.0111, "brier_diff_se": 0.0018, "model_logloss": 0.6204, "kalshi_logloss": 0.5908}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2512, "share_ge_15": 0.4468, "median_abs_gap": 13.1, "n": 50434}, "gen1_elo": {"share_ge_25": 0.2485, "share_ge_15": 0.4424, "median_abs_gap": 12.93, "n": 50434}, "gen1_sr": {"share_ge_25": 0.3145, "share_ge_15": 0.5221, "median_abs_gap": 15.89, "n": 50434}, "gen2": {"share_ge_25": 0.315, "share_ge_15": 0.5112, "median_abs_gap": 15.47, "n": 50434}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1519, "share_ge_15": 0.3547, "median_abs_gap": 10.7, "n": 38705}, "gen1_elo": {"share_ge_25": 0.1501, "share_ge_15": 0.3493, "median_abs_gap": 10.49, "n": 38705}, "gen1_sr": {"share_ge_25": 0.2159, "share_ge_15": 0.4393, "median_abs_gap": 12.97, "n": 38707}, "gen2": {"share_ge_25": 0.2307, "share_ge_15": 0.4386, "median_abs_gap": 12.83, "n": 38707}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.49, "share_ge_25_all": 0.0375, "share_ge_25_pregame_clean": 0.0314}, "WTA": {"median_abs_gap_pregame_clean": 7.65, "share_ge_25_all": 0.0594, "share_ge_25_pregame_clean": 0.0504}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2359, "share_within_10pp_all": 0.4377, "share_within_10pp_pregame_clean": 0.4911, "corr_model_vs_mid_pregame_clean": 0.8492}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1105, "model_brier": 0.1977, "kalshi_brier": 0.198, "brier_diff_model_minus_kalshi": -0.0003}, "10-15": {"n_settled": 1322, "model_brier": 0.2193, "kalshi_brier": 0.2095, "brier_diff_model_minus_kalshi": 0.0099}, "15-25": {"n_settled": 1686, "model_brier": 0.2267, "kalshi_brier": 0.2079, "brier_diff_model_minus_kalshi": 0.0187}, "25-40": {"n_settled": 961, "model_brier": 0.2263, "kalshi_brier": 0.2049, "brier_diff_model_minus_kalshi": 0.0214}, "3-5": {"n_settled": 698, "model_brier": 0.2062, "kalshi_brier": 0.2057, "brier_diff_model_minus_kalshi": 0.0005}, "40+": {"n_settled": 196, "model_brier": 0.3016, "kalshi_brier": 0.1723, "brier_diff_model_minus_kalshi": 0.1293}, "5-10": {"n_settled": 1638, "model_brier": 0.2042, "kalshi_brier": 0.2025, "brier_diff_model_minus_kalshi": 0.0017}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.558, "slope": 0.813, "slope_se": 0.029}, "kalshi_slope": {"intercept": 0.168, "slope": 1.068, "slope_se": 0.033}, "n": 7606}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.493, "slope": 0.863, "slope_se": 0.024}, "kalshi_slope": {"intercept": 0.158, "slope": 1.07, "slope_se": 0.028}, "n": 9870}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 657, "model_brier": 0.299, "kalshi_brier": 0.2321, "brier_diff_model_minus_kalshi": 0.0669, "brier_diff_se": 0.0114, "corr_model_outcome": 0.1003, "corr_kalshi_outcome": 0.2815}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
