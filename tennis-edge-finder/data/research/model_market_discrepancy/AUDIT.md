# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-14T19:32Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 92,781): 0-3 13.9%, 3-5 9.5%, 5-10 20.1%, 10-15 15.2%, 15-25 19.2%, 25-40 13.8%, 40+ 8.4%; median gap 11.95 pp.
* **Where the extremes live**: 97.4% of >=25 pp gaps are off the ATP/WTA main tour (ITF 78.3%, Challenger 11.1%, doubles 6.5%). Main tour: ATP 3.7% and WTA 5.9% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 20,570): MARKET_ALREADY_SETTLED_WHEN_PRICED 35.7%, STALE_QUOTE 19.9%, BOOK_QUALITY 16.2%, POOR_DATA 8.9%, POSSIBLY_IN_PLAY_QUOTE 5.9%, IDENTITY_AMBIGUOUS 4.3%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 1.7%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 35.7%, market_freshness 19.9%, execution 16.2%, data 12.2%, market_freshness/coverage 9.4%, mapping 4.3%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 55.9% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 45.0% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 20,570 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.7%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 27.0% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 491.0 points vs 1681.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.018, Gen-2 0.815, Gen-1 ledger 0.86 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 1049 model 0.2251 vs Kalshi 0.2039; n 215 model 0.3093 vs Kalshi 0.1669.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA. Not implemented here.

## 1. Observations

* 383,571 model-market comparisons (636,156 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 126,158 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-14T19:10:02.785886+00:00'], shadow board 107,530 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-14T19:10:06.665344+00:00'], Model 4 44,376 rows, 31,927 settled tickers, 12,010 tickers with an external scan.
* By model: {"gen1_ledger": 84185, "gen1_elo": 54035, "fair_v1": 54035, "gen2": 54035, "gen1_sr": 54035, "model4_fundamental": 41665, "model4_conditioned": 41581}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 92,781 | 13.9 | 9.5 | 20.1 | 15.2 | 19.2 | 13.8 | 8.4 | 11.95 | 41.3% | 22.2% |
| MW fair_v1 | 54,035 | 12.5 | 8.6 | 18.6 | 15.2 | 19.6 | 15.1 | 10.5 | 13.25 | 45.1% | 25.5% |
| MW gen1_elo | 54,035 | 12.3 | 8.7 | 19.1 | 15.2 | 19.4 | 15.0 | 10.3 | 13.02 | 44.7% | 25.3% |
| MW gen1_ledger | 38,746 | 15.8 | 10.8 | 22.2 | 15.2 | 18.6 | 12.0 | 5.5 | 10.29 | 36.1% | 17.5% |
| MW gen1_sr | 54,035 | 9.9 | 7.1 | 16.5 | 13.9 | 20.9 | 18.8 | 12.9 | 16.02 | 52.6% | 31.7% |
| MW gen2 | 54,035 | 10.8 | 7.5 | 16.6 | 13.7 | 19.7 | 17.7 | 14.0 | 15.56 | 51.4% | 31.7% |
| all families model4_conditioned | 41,581 | 22.2 | 17.9 | 34.6 | 16.9 | 4.9 | 2.2 | 1.2 | 6.07 | 8.4% | 3.4% |
| all families model4_fundamental | 41,665 | 17.3 | 13.6 | 34.0 | 19.9 | 9.9 | 3.8 | 1.5 | 7.6 | 15.2% | 5.3% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.5%, >=15pp 41.3%, >=20pp 30.6%, >=25pp 22.2%, >=30pp 16.1%, >=40pp 8.4%, >=50pp 3.9%
Executable gap (model outside the book, before fees): median 8.63pp; >=10pp 45.8%, >=25pp 17.7%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,144 | 27.9 | 16.0 | 28.0 | 13.2 | 10.7 | 3.5 | 0.6 | 5.77 | 14.8% | 4.1% |
| CHALLENGER | 8,491 | 16.3 | 9.6 | 20.6 | 15.2 | 15.7 | 11.4 | 11.2 | 10.94 | 38.3% | 22.6% |
| ITF_MEN | 16,053 | 9.6 | 7.3 | 17.0 | 14.9 | 21.0 | 17.2 | 13.0 | 15.46 | 51.2% | 30.2% |
| ITF_WOMEN | 20,893 | 9.3 | 7.0 | 16.1 | 14.6 | 22.2 | 18.6 | 12.1 | 16.05 | 52.9% | 30.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,121 | 16.5 | 13.2 | 24.9 | 20.7 | 16.9 | 6.8 | 1.1 | 8.68 | 24.7% | 7.8% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,144 | 26.3 | 15.7 | 26.4 | 15.8 | 11.2 | 3.9 | 0.8 | 6.09 | 15.9% | 4.7% |
| CHALLENGER | 8,491 | 14.3 | 9.1 | 19.1 | 13.7 | 18.4 | 13.7 | 11.7 | 12.55 | 43.7% | 25.3% |
| ITF_MEN | 16,053 | 8.2 | 6.2 | 15.2 | 13.8 | 20.3 | 19.9 | 16.4 | 17.85 | 56.6% | 36.3% |
| ITF_WOMEN | 20,893 | 7.8 | 5.8 | 14.1 | 12.7 | 20.6 | 21.2 | 17.8 | 19.2 | 59.6% | 39.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,121 | 14.0 | 10.3 | 21.5 | 16.2 | 22.6 | 12.8 | 2.5 | 11.3 | 37.9% | 15.3% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,144 | 23.5 | 14.2 | 25.6 | 15.4 | 14.2 | 5.9 | 1.1 | 6.99 | 21.3% | 7.0% |
| CHALLENGER | 8,491 | 15.2 | 9.5 | 20.8 | 15.6 | 16.0 | 11.9 | 11.0 | 11.18 | 39.0% | 22.9% |
| ITF_MEN | 16,053 | 9.3 | 7.3 | 17.2 | 14.3 | 21.3 | 17.4 | 13.3 | 15.77 | 51.9% | 30.6% |
| ITF_WOMEN | 20,893 | 9.2 | 6.8 | 16.2 | 15.5 | 22.1 | 18.7 | 11.5 | 15.86 | 52.2% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,121 | 22.3 | 17.1 | 31.8 | 15.3 | 9.1 | 3.4 | 1.0 | 6.15 | 13.5% | 4.4% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,513 | 28.1 | 19.5 | 29.3 | 12.1 | 8.0 | 2.5 | 0.4 | 5.24 | 11.0% | 2.9% |
| CHALLENGER | 5,152 | 23.2 | 14.7 | 27.5 | 14.7 | 13.0 | 5.4 | 1.5 | 6.97 | 19.9% | 6.9% |
| DOUBLES | 2,874 | 4.7 | 4.5 | 12.7 | 10.9 | 20.6 | 25.1 | 21.5 | 23.46 | 67.2% | 46.6% |
| ITF_MEN | 11,532 | 12.8 | 9.6 | 21.5 | 15.7 | 21.6 | 12.8 | 6.0 | 11.77 | 40.4% | 18.8% |
| ITF_WOMEN | 13,427 | 13.5 | 9.3 | 19.9 | 15.8 | 21.6 | 14.6 | 5.4 | 12.14 | 41.5% | 19.9% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,843 | 23.7 | 15.8 | 32.0 | 16.7 | 9.1 | 2.5 | 0.2 | 6.6 | 11.8% | 2.7% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,015 | 28.4 | 16.2 | 28.4 | 13.2 | 10.4 | 3.1 | 0.3 | 5.64 | 13.8% | 3.4% |
| CHALLENGER | 5,951 | 21.1 | 12.1 | 25.7 | 18.0 | 15.8 | 5.5 | 1.8 | 8.18 | 23.1% | 7.3% |
| ITF_MEN | 11,544 | 11.9 | 8.8 | 20.6 | 17.2 | 22.1 | 14.0 | 5.5 | 12.41 | 41.5% | 19.4% |
| ITF_WOMEN | 15,120 | 11.3 | 8.6 | 19.1 | 17.0 | 24.1 | 15.3 | 4.5 | 13.11 | 43.9% | 19.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,006 | 16.8 | 13.2 | 25.2 | 21.0 | 16.9 | 6.2 | 0.6 | 8.52 | 23.8% | 6.9% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,015 | 26.6 | 16.0 | 26.6 | 15.7 | 11.2 | 3.4 | 0.4 | 6.01 | 14.9% | 3.8% |
| CHALLENGER | 5,951 | 18.1 | 11.8 | 24.0 | 16.2 | 19.0 | 8.9 | 2.0 | 8.97 | 30.0% | 11.0% |
| ITF_MEN | 11,546 | 9.8 | 7.4 | 17.7 | 16.0 | 22.3 | 17.8 | 9.0 | 14.66 | 49.1% | 26.8% |
| ITF_WOMEN | 15,122 | 8.9 | 7.0 | 16.1 | 14.2 | 22.6 | 20.6 | 10.6 | 16.5 | 53.8% | 31.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,006 | 14.3 | 10.4 | 21.7 | 16.4 | 22.8 | 12.5 | 1.9 | 11.16 | 37.2% | 14.4% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,443 | 28.4 | 19.7 | 29.3 | 12.3 | 7.7 | 2.3 | 0.3 | 5.2 | 10.3% | 2.6% |
| CHALLENGER | 4,557 | 24.6 | 15.5 | 28.7 | 14.8 | 12.3 | 3.7 | 0.4 | 6.48 | 16.4% | 4.1% |
| DOUBLES | 2,687 | 4.6 | 4.5 | 13.0 | 10.9 | 20.4 | 25.0 | 21.7 | 23.41 | 67.1% | 46.7% |
| ITF_MEN | 9,954 | 13.6 | 10.1 | 23.0 | 16.3 | 21.7 | 11.4 | 4.1 | 10.9 | 37.2% | 15.5% |
| ITF_WOMEN | 11,567 | 14.1 | 9.8 | 21.0 | 16.4 | 21.7 | 13.4 | 3.6 | 11.36 | 38.7% | 17.0% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,778 | 24.1 | 16.2 | 32.0 | 16.7 | 9.0 | 2.0 | 0.1 | 6.44 | 11.0% | 2.0% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,874 | 4.7 | 4.5 | 12.7 | 10.9 | 20.6 | 25.1 | 21.5 | 23.46 | 67.2% | 46.6% |
| singles | 35,872 | 16.6 | 11.3 | 22.9 | 15.5 | 18.4 | 10.9 | 4.2 | 9.75 | 33.6% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 11,817 | 12.6 | 8.9 | 19.2 | 15.0 | 19.6 | 14.3 | 10.3 | 13.06 | 44.3% | 24.7% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 35,134 | 12.9 | 8.6 | 18.8 | 15.0 | 19.2 | 15.1 | 10.4 | 13.06 | 44.7% | 25.5% |
| UNKNOWN | 6,671 | 10.5 | 7.5 | 17.1 | 16.5 | 21.5 | 15.8 | 11.1 | 14.3 | 48.4% | 26.9% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 15,000 | 19.0 | 11.8 | 22.3 | 15.7 | 14.9 | 9.6 | 6.7 | 9.08 | 31.2% | 16.3% |
| B | 6,423 | 12.8 | 8.6 | 19.4 | 15.3 | 19.9 | 12.4 | 11.7 | 12.92 | 43.9% | 24.1% |
| C | 7,757 | 11.9 | 8.5 | 19.2 | 16.0 | 19.2 | 14.8 | 10.6 | 13.09 | 44.5% | 25.3% |
| D | 8,955 | 11.2 | 8.3 | 17.8 | 15.2 | 21.6 | 15.8 | 10.1 | 14.1 | 47.5% | 25.9% |
| F | 15,900 | 7.3 | 5.7 | 15.1 | 14.2 | 23.0 | 21.1 | 13.7 | 18.06 | 57.8% | 34.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 10,179 | 25.0 | 15.9 | 29.0 | 14.8 | 10.6 | 3.4 | 1.2 | 6.36 | 15.3% | 4.7% |
| B | 5,277 | 16.7 | 11.0 | 24.0 | 17.0 | 18.9 | 9.4 | 2.9 | 9.61 | 31.2% | 12.3% |
| C | 7,683 | 11.0 | 7.8 | 19.4 | 14.9 | 20.9 | 15.8 | 10.1 | 13.56 | 46.8% | 25.9% |
| D | 5,931 | 14.3 | 9.9 | 21.0 | 15.6 | 21.0 | 12.8 | 5.3 | 11.42 | 39.1% | 18.1% |
| F | 9,676 | 10.2 | 8.4 | 16.8 | 14.5 | 23.5 | 18.8 | 7.9 | 15.08 | 50.2% | 26.8% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 16,994 | 17.4 | 10.8 | 21.3 | 15.5 | 15.2 | 10.3 | 9.5 | 10.09 | 35.0% | 19.8% |
| LIMITED | 11,785 | 13.4 | 9.4 | 20.3 | 15.9 | 19.9 | 13.4 | 7.7 | 12.01 | 41.0% | 21.1% |
| POOR | 25,256 | 8.8 | 6.6 | 16.1 | 14.6 | 22.4 | 19.0 | 12.4 | 16.37 | 53.9% | 31.5% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,402 | 23.8 | 18.0 | 33.0 | 15.4 | 6.3 | 3.0 | 0.4 | 5.89 | 9.8% | 3.4% |
| GAME_SPREAD | 6,989 | 22.8 | 15.3 | 32.1 | 16.8 | 9.1 | 3.3 | 0.7 | 6.68 | 13.0% | 3.9% |
| MATCH_WINNER | 38,746 | 15.8 | 10.8 | 22.2 | 15.2 | 18.6 | 12.0 | 5.5 | 10.29 | 36.1% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 17,285 | 28.4 | 16.8 | 30.8 | 12.7 | 8.8 | 2.3 | 0.3 | 5.57 | 11.4% | 2.6% |
| TOTAL_GAMES | 11,739 | 9.7 | 10.8 | 36.5 | 25.6 | 10.4 | 4.2 | 2.8 | 9.12 | 17.4% | 7.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,800 | 24.5 | 28.8 | 33.2 | 8.0 | 3.9 | 1.2 | 0.3 | 4.79 | 5.4% | 1.5% |
| GAME_SPREAD | 9,605 | 46.6 | 15.8 | 25.2 | 7.4 | 2.4 | 1.9 | 0.6 | 3.33 | 4.9% | 2.5% |
| TOTAL_GAMES | 17,176 | 6.5 | 9.8 | 41.1 | 29.8 | 7.2 | 3.3 | 2.3 | 9.14 | 12.9% | 5.6% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,836 | 23.9 | 16.7 | 34.6 | 14.7 | 6.9 | 2.7 | 0.5 | 6.05 | 10.1% | 3.2% |
| GAME_SPREAD | 9,614 | 20.3 | 13.4 | 28.5 | 20.2 | 12.1 | 4.3 | 1.1 | 7.71 | 17.6% | 5.5% |
| TOTAL_GAMES | 17,215 | 10.0 | 10.9 | 36.5 | 24.3 | 11.3 | 4.4 | 2.6 | 9.01 | 18.2% | 7.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 54,035 | 45.1% | 25.5% | 13.25 | 35.5% | 15.1% | 10.71 |
| gen1_elo | 54,035 | 44.7% | 25.3% | 13.02 | 34.9% | 15.0% | 10.5 |
| gen1_sr | 54,035 | 52.6% | 31.7% | 16.02 | 43.9% | 21.4% | 12.98 |
| gen2 | 54,035 | 51.4% | 31.7% | 15.56 | 43.9% | 22.9% | 12.82 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,625 | 15.4 | 10.5 | 21.3 | 17.2 | 20.1 | 11.9 | 3.5 | 10.72 | 35.4% | 15.4% |
| STALE | 33,410 | 10.7 | 7.4 | 17.0 | 13.9 | 19.3 | 17.0 | 14.8 | 15.45 | 51.1% | 31.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 32,214 | 16.3 | 11.1 | 22.6 | 15.2 | 18.2 | 11.5 | 5.0 | 9.98 | 34.7% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 92,781 | 32214 | 24097 | 36470 | 25.3 | 154.6 | 1451.1 |
| ge_15pp | 38,361 | 11180 | 8601 | 18580 | 29.3 | 455.5 | 1451.1 |
| ge_25pp | 20,570 | 5315 | 3763 | 11492 | 35.0 | 599.0 | 1431.1 |
| lt_10pp | 40,345 | 16124 | 11387 | 12834 | 22.8 | 49.7 | 1421.7 |

Current slate `SL-20261114T193232Z-18d074ee`: 206 priced rows, quote age at build {'median': 60.6, 'max': 90.6}, freshness {'STALE': 206}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 52 | 0.0 | 0.0 | 34.6 | 9.6 | 32.7 | 19.2 | 3.9 | 18.34 | 55.8% | 23.1% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 5,131 | 19.2 | 11.1 | 25.7 | 18.3 | 17.6 | 7.1 | 0.9 | 8.76 | 25.7% | 8.1% |
| KALSHI_LONE_OUTLIER | 32 | 6.2 | 6.2 | 75.0 | 6.2 | 3.1 | 3.1 | 0.0 | 6.16 | 6.2% | 3.1% |
| MARKETS_AGREE | 1,112 | 66.2 | 33.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,354 | 0.0 | 2.2 | 38.5 | 25.9 | 24.0 | 8.6 | 0.9 | 11.65 | 33.5% | 9.5% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 54,035 | 8710 (16.1%) | 27.0% | 0.9% | {"EXTERNAL_STALE": 5131, "AGREES_WITH_KALSHI": 2354, "ALL_AGREE": 1112, "SUPPORTS_MODEL_DIRECTION": 50, "AGREES_WITH_MODEL": 32, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 24,382 | 2139 (8.8%) | 36.8% | 1.5% | {"EXTERNAL_STALE": 1320, "AGREES_WITH_KALSHI": 788, "SUPPORTS_MODEL_DIRECTION": 29, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 13,793 | 652 (4.7%) | 34.4% | 2.0% | {"EXTERNAL_STALE": 415, "AGREES_WITH_KALSHI": 224, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 6,190 | 619 (10.0%) | 35.1% | 2.1% | {"EXTERNAL_STALE": 389, "AGREES_WITH_KALSHI": 217, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 21,452 | 5015 (23.4%) | 19.1% | 0.9% | {"EXTERNAL_STALE": 2872, "ALL_AGREE": 1112, "AGREES_WITH_KALSHI": 956, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 28, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 10,610 | 10.5 | 7.7 | 18.9 | 14.3 | 21.7 | 16.4 | 10.5 | 14.42 | 48.6% | 26.9% |
| 4-10x | 7,315 | 10.8 | 8.6 | 18.1 | 14.9 | 21.5 | 14.8 | 11.4 | 14.12 | 47.6% | 26.2% |
| <2x | 27,505 | 14.4 | 9.6 | 19.8 | 15.9 | 17.6 | 13.4 | 9.3 | 11.77 | 40.3% | 22.7% |
| >=10x | 8,605 | 10.2 | 6.4 | 15.2 | 14.2 | 21.8 | 18.9 | 13.3 | 16.54 | 54.0% | 32.2% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 14,321 | 12.2 | 8.6 | 19.5 | 16.1 | 19.2 | 13.7 | 10.7 | 12.9 | 43.6% | 24.4% |
| 300-1000 | 11,785 | 11.4 | 8.6 | 17.8 | 15.1 | 20.5 | 16.4 | 10.2 | 13.95 | 47.1% | 26.6% |
| <300 | 17,026 | 8.1 | 5.9 | 15.1 | 14.4 | 22.9 | 20.0 | 13.6 | 17.47 | 56.5% | 33.7% |
| >=3000 | 10,903 | 20.9 | 12.7 | 23.9 | 15.3 | 14.1 | 7.6 | 5.5 | 7.93 | 27.2% | 13.1% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1689 | 0.5473 | 0.4085 | 0.4748 | +0.072 | -0.066 | 0.0044 ± 0.0038 |
| ratio 4-10x | 1150 | 0.5716 | 0.4273 | 0.4843 | +0.087 | -0.057 | 0.0098 ± 0.0047 |
| ratio <2x | 4119 | 0.5339 | 0.4114 | 0.4312 | +0.103 | -0.020 | 0.0146 ± 0.0022 |
| ratio >=10x | 1407 | 0.5581 | 0.3869 | 0.43 | +0.128 | -0.043 | 0.0184 ± 0.0047 |
| thinner_sample 1000-3000 | 2320 | 0.5388 | 0.4121 | 0.4409 | +0.098 | -0.029 | 0.0131 ± 0.003 |
| thinner_sample 300-1000 | 1910 | 0.5596 | 0.4192 | 0.4665 | +0.093 | -0.047 | 0.0069 ± 0.0036 |
| thinner_sample <300 | 2708 | 0.5517 | 0.3852 | 0.4394 | +0.112 | -0.054 | 0.0158 ± 0.0034 |
| thinner_sample >=3000 | 1427 | 0.5279 | 0.4345 | 0.4457 | +0.082 | -0.011 | 0.0128 ± 0.003 |
| data_status ADEQUATE | 2263 | 0.5316 | 0.4294 | 0.4401 | +0.091 | -0.011 | 0.0145 ± 0.0026 |
| data_status LIMITED | 2050 | 0.5461 | 0.4135 | 0.461 | +0.085 | -0.048 | 0.0078 ± 0.0033 |
| data_status POOR | 4052 | 0.5537 | 0.395 | 0.444 | +0.110 | -0.049 | 0.0138 ± 0.0027 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1202 | 0.1971 | 0.1971 | +0.0000 ± 0.0004 | 0.5741 | 0.5742 | 0.5029 | 0.4877 | 0.4917 | -0.099 ± 0.0135 | -0.0087 (8) |
| 3-5 | 788 | 0.2077 | 0.207 | +0.0007 ± 0.0013 | 0.6012 | 0.5982 | 0.4985 | 0.4587 | 0.4695 | -0.098 ± 0.0166 | 0.0025 (4) |
| 5-10 | 1802 | 0.2027 | 0.2005 | +0.0021 ± 0.0016 | 0.5917 | 0.5846 | 0.5096 | 0.4357 | 0.4573 | -0.092 ± 0.0109 | -0.0143 (7) |
| 10-15 | 1454 | 0.2214 | 0.2117 | +0.0097 ± 0.003 | 0.6358 | 0.6075 | 0.5247 | 0.4014 | 0.423 | -0.103 ± 0.0123 | -0.055 (6) |
| 15-25 | 1855 | 0.2249 | 0.2069 | +0.0181 ± 0.0041 | 0.6448 | 0.5969 | 0.5698 | 0.3754 | 0.4259 | -0.097 ± 0.0106 | -0.0045 (11) |
| 25-40 | 1049 | 0.2251 | 0.2039 | +0.0212 ± 0.0084 | 0.6406 | 0.5883 | 0.6431 | 0.3335 | 0.4528 | -0.063 ± 0.013 | -0.06 (2) |
| 40+ | 215 | 0.3093 | 0.1669 | +0.1424 ± 0.0253 | 0.8271 | 0.5025 | 0.7252 | 0.268 | 0.3488 | -0.092 ± 0.0245 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 6049 | 0.1874 | 0.1882 | -0.0008 ± 0.0002 | 0.5514 | 0.5523 | 0.4921 | 0.4769 | 0.506 | -0.023 ± 0.0057 | -0.01 (28) |
| 3-5 | 4125 | 0.1991 | 0.1973 | +0.0018 ± 0.0006 | 0.5795 | 0.5732 | 0.4797 | 0.4399 | 0.4371 | -0.056 ± 0.007 | -0.005 (10) |
| 5-10 | 9015 | 0.2007 | 0.1963 | +0.0043 ± 0.0007 | 0.587 | 0.5731 | 0.4824 | 0.4086 | 0.4164 | -0.049 ± 0.0047 | -0.0114 (22) |
| 10-15 | 7351 | 0.2027 | 0.1864 | +0.0163 ± 0.0013 | 0.5925 | 0.5466 | 0.4841 | 0.3602 | 0.3567 | -0.064 ± 0.0051 | -0.0379 (19) |
| 15-25 | 9470 | 0.206 | 0.167 | +0.0390 ± 0.0016 | 0.6038 | 0.4963 | 0.4975 | 0.302 | 0.3007 | -0.066 ± 0.0042 | -0.0043 (51) |
| 25-40 | 7415 | 0.2222 | 0.1236 | +0.0986 ± 0.0026 | 0.6385 | 0.3811 | 0.5231 | 0.2088 | 0.2128 | -0.058 ± 0.004 | -0.0733 (3) |
| 40+ | 5139 | 0.3799 | 0.0437 | +0.3362 ± 0.0033 | 0.9901 | 0.1701 | 0.6275 | 0.1017 | 0.0566 | -0.077 ± 0.0028 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 964 | 0.202 | 0.2023 | -0.0002 ± 0.0005 | 0.5843 | 0.585 | 0.5075 | 0.4924 | 0.5145 | -0.096 ± 0.0154 | -0.0117 (6) |
| 3-5 | 705 | 0.212 | 0.2091 | +0.0029 ± 0.0014 | 0.6082 | 0.6021 | 0.5183 | 0.4787 | 0.4596 | -0.123 ± 0.0185 | 0.01 (3) |
| 5-10 | 1558 | 0.2042 | 0.2028 | +0.0014 ± 0.0017 | 0.5937 | 0.5901 | 0.5377 | 0.4632 | 0.4917 | -0.082 ± 0.0118 | -0.012 (5) |
| 10-15 | 1352 | 0.2164 | 0.2077 | +0.0087 ± 0.0031 | 0.6257 | 0.6011 | 0.5581 | 0.4338 | 0.4638 | -0.104 ± 0.0129 | -0.04 (5) |
| 15-25 | 1949 | 0.2339 | 0.2128 | +0.0211 ± 0.0041 | 0.6659 | 0.61 | 0.5842 | 0.3885 | 0.4341 | -0.097 ± 0.0107 | -0.0183 (12) |
| 25-40 | 1347 | 0.2658 | 0.2002 | +0.0655 ± 0.0076 | 0.7418 | 0.5809 | 0.6578 | 0.3444 | 0.3987 | -0.106 ± 0.0123 | -0.008 (5) |
| 40+ | 490 | 0.3743 | 0.1601 | +0.2142 ± 0.0181 | 1.0173 | 0.4854 | 0.7326 | 0.2438 | 0.2816 | -0.088 ± 0.0175 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5209 | 0.1896 | 0.1898 | -0.0002 ± 0.0002 | 0.5543 | 0.5546 | 0.5054 | 0.4902 | 0.5049 | -0.039 ± 0.0062 | -0.0154 (26) |
| 3-5 | 3617 | 0.1939 | 0.1929 | +0.0010 ± 0.0006 | 0.5653 | 0.5624 | 0.5107 | 0.471 | 0.4764 | -0.045 ± 0.0075 | 0.01 (5) |
| 5-10 | 8059 | 0.1955 | 0.1922 | +0.0032 ± 0.0007 | 0.5751 | 0.5629 | 0.5065 | 0.4322 | 0.4497 | -0.038 ± 0.0049 | -0.015 (10) |
| 10-15 | 6668 | 0.2026 | 0.1898 | +0.0127 ± 0.0013 | 0.5945 | 0.5556 | 0.5059 | 0.3821 | 0.3935 | -0.051 ± 0.0054 | -0.0189 (18) |
| 15-25 | 9554 | 0.2169 | 0.1806 | +0.0363 ± 0.0017 | 0.6316 | 0.5299 | 0.5242 | 0.3285 | 0.336 | -0.059 ± 0.0044 | -0.014 (52) |
| 25-40 | 8592 | 0.2494 | 0.1377 | +0.1117 ± 0.0025 | 0.705 | 0.42 | 0.5585 | 0.2412 | 0.2275 | -0.074 ± 0.004 | -0.0095 (20) |
| 40+ | 6865 | 0.4018 | 0.0591 | +0.3427 ± 0.0034 | 1.0592 | 0.2126 | 0.6546 | 0.119 | 0.0804 | -0.073 ± 0.0029 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1185 | 0.1967 | 0.1978 | -0.0011 ± 0.0005 | 0.5735 | 0.5761 | 0.5014 | 0.4859 | 0.5224 | -0.059 ± 0.0135 | -0.0191 (11) |
| 3-5 | 849 | 0.2097 | 0.208 | +0.0017 ± 0.0013 | 0.6076 | 0.6019 | 0.4972 | 0.4577 | 0.457 | -0.109 ± 0.0163 | 0.0017 (6) |
| 5-10 | 1810 | 0.2039 | 0.1996 | +0.0042 ± 0.0016 | 0.5934 | 0.5817 | 0.5102 | 0.4364 | 0.4436 | -0.104 ± 0.0108 | -0.01 (10) |
| 10-15 | 1503 | 0.2126 | 0.2033 | +0.0093 ± 0.0029 | 0.6162 | 0.5893 | 0.5372 | 0.4139 | 0.4398 | -0.101 ± 0.0117 | -0.0286 (7) |
| 15-25 | 1752 | 0.2309 | 0.2117 | +0.0192 ± 0.0043 | 0.6589 | 0.6071 | 0.5787 | 0.3847 | 0.4321 | -0.101 ± 0.0111 | -0.03 (1) |
| 25-40 | 1037 | 0.2185 | 0.2059 | +0.0126 ± 0.0084 | 0.6272 | 0.5928 | 0.6512 | 0.3417 | 0.4735 | -0.059 ± 0.013 | -0.0267 (3) |
| 40+ | 229 | 0.3093 | 0.1804 | +0.1289 ± 0.0253 | 0.8338 | 0.5323 | 0.7372 | 0.2806 | 0.3799 | -0.075 ± 0.0258 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5886 | 0.1869 | 0.1874 | -0.0005 ± 0.0002 | 0.55 | 0.5504 | 0.4873 | 0.4718 | 0.4862 | -0.037 ± 0.0057 | -0.0189 (44) |
| 3-5 | 4213 | 0.2047 | 0.203 | +0.0018 ± 0.0006 | 0.5949 | 0.5889 | 0.4814 | 0.4418 | 0.4394 | -0.056 ± 0.0071 | -0.0062 (26) |
| 5-10 | 9147 | 0.1967 | 0.1911 | +0.0056 ± 0.0007 | 0.5773 | 0.5597 | 0.4853 | 0.4113 | 0.4099 | -0.057 ± 0.0046 | -0.0117 (42) |
| 10-15 | 7372 | 0.1956 | 0.18 | +0.0156 ± 0.0012 | 0.5767 | 0.5325 | 0.4948 | 0.3715 | 0.37 | -0.062 ± 0.005 | -0.0136 (14) |
| 15-25 | 9476 | 0.2106 | 0.1716 | +0.0390 ± 0.0017 | 0.6146 | 0.5063 | 0.5087 | 0.314 | 0.3123 | -0.067 ± 0.0043 | -0.0533 (3) |
| 25-40 | 7413 | 0.2167 | 0.1235 | +0.0932 ± 0.0026 | 0.6266 | 0.3802 | 0.5249 | 0.2094 | 0.2208 | -0.051 ± 0.004 | -0.02 (4) |
| 40+ | 5057 | 0.3882 | 0.0475 | +0.3407 ± 0.0035 | 1.0121 | 0.1798 | 0.6361 | 0.1069 | 0.0623 | -0.077 ± 0.0029 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1667 | 0.197 | 0.1967 | +0.0003 ± 0.0004 | 0.5728 | 0.572 | 0.5068 | 0.4917 | 0.4913 | -0.072 ± 0.0111 | -0.0305 (58) |
| 3-5 | 1172 | 0.19 | 0.19 | +0.0000 ± 0.001 | 0.5584 | 0.5574 | 0.4986 | 0.4588 | 0.4761 | -0.055 ± 0.013 | -0.0194 (34) |
| 5-10 | 2375 | 0.1987 | 0.1936 | +0.0051 ± 0.0014 | 0.5861 | 0.5698 | 0.5098 | 0.4362 | 0.4387 | -0.076 ± 0.0093 | -0.005 (78) |
| 10-15 | 1639 | 0.2157 | 0.2033 | +0.0124 ± 0.0028 | 0.6259 | 0.5902 | 0.5445 | 0.4218 | 0.432 | -0.087 ± 0.0114 | 0.0015 (67) |
| 15-25 | 2133 | 0.2324 | 0.2077 | +0.0247 ± 0.0039 | 0.6633 | 0.5991 | 0.5927 | 0.3977 | 0.4332 | -0.089 ± 0.01 | -0.0214 (59) |
| 25-40 | 1243 | 0.2421 | 0.2125 | +0.0296 ± 0.008 | 0.6908 | 0.6084 | 0.6888 | 0.3773 | 0.4859 | -0.080 ± 0.0124 | -0.0297 (29) |
| 40+ | 461 | 0.3312 | 0.1993 | +0.1319 ± 0.0199 | 0.9475 | 0.5807 | 0.8079 | 0.3311 | 0.4469 | -0.092 ± 0.0188 | -0.117 (10) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5995 | 0.1777 | 0.1777 | -0.0000 ± 0.0002 | 0.5261 | 0.5256 | 0.5087 | 0.4935 | 0.5008 | -0.041 ± 0.0055 | -0.0202 (108) |
| 3-5 | 4103 | 0.1948 | 0.1939 | +0.0009 ± 0.0006 | 0.5684 | 0.5663 | 0.502 | 0.4622 | 0.4709 | -0.041 ± 0.007 | -0.022 (74) |
| 5-10 | 8384 | 0.1972 | 0.1908 | +0.0065 ± 0.0007 | 0.5815 | 0.5621 | 0.5035 | 0.4298 | 0.4238 | -0.061 ± 0.0048 | -0.0085 (136) |
| 10-15 | 5770 | 0.2108 | 0.1947 | +0.0162 ± 0.0014 | 0.6139 | 0.5703 | 0.5374 | 0.4144 | 0.409 | -0.070 ± 0.0059 | -0.0054 (112) |
| 15-25 | 7057 | 0.2318 | 0.1993 | +0.0325 ± 0.0021 | 0.6665 | 0.5779 | 0.5771 | 0.3817 | 0.3966 | -0.067 ± 0.0053 | -0.024 (112) |
| 25-40 | 4548 | 0.2584 | 0.1915 | +0.0669 ± 0.0041 | 0.7303 | 0.5567 | 0.6416 | 0.3294 | 0.3813 | -0.061 ± 0.0064 | -0.03 (65) |
| 40+ | 2040 | 0.3715 | 0.1604 | +0.2111 ± 0.0091 | 1.0448 | 0.4775 | 0.7417 | 0.2422 | 0.2912 | -0.059 ± 0.0085 | -0.0641 (22) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 8365 | 1.018 ± 0.03 | 1.075 | 0.1677 | 0.1712 | 0.2161 | 0.2036 |
| gen2 | 8365 | 0.815 ± 0.027 | 1.056 | 0.1742 | 0.1714 | 0.2334 | 0.2035 |
| gen1_elo | 8365 | 0.999 ± 0.03 | 1.067 | 0.174 | 0.1714 | 0.2154 | 0.2037 |
| gen1_sr | 8365 | 1.002 ± 0.036 | 1.101 | 0.1336 | 0.1729 | 0.2294 | 0.2032 |
| gen1_ledger | 10690 | 0.86 ± 0.023 | 1.058 | 0.1904 | 0.1771 | 0.2176 | 0.2004 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 38,361)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 9,238 | 24.1% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 9,106 | 23.7% |
| BOOK_QUALITY | execution | 6,429 | 16.8% |
| POOR_DATA | data | 4,347 | 11.3% |
| LIMITED_DATA | data | 2,296 | 6.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 2,252 | 5.9% |
| IDENTITY_AMBIGUOUS | mapping | 1,580 | 4.1% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,443 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 1,082 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 587 | 1.5% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 24.1%, coverage 23.7%, data 17.3%, execution 16.8%, market_freshness/coverage 8.7%, mapping 4.1%, model_calibration_or_unknown 3.8%, model_calibration 1.5%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 95.1%, LOW_DATA_QUALITY 72.1%, THIN_PLAYER_HISTORY 59.9%, STALE_PLAYER_DATA 51.8%, STALE_KALSHI_QUOTE 48.4%, MODEL_INTERNAL_DISAGREEMENT 41.6%, ASYMMETRIC_SAMPLE_SIZE 33.0%, WIDE_SPREAD 23.2%, MODEL_HIGH_UNCERTAINTY 18.9%, PLAYER_IDENTITY_RISK 15.0%, LEVEL_TRANSFER_RISK 9.2%, LOW_DISPLAYED_LIQUIDITY 8.7%, EVENT_MAPPING_RISK 7.0%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.1%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 26.1%, POST_SETTLEMENT_OBSERVATION 23.7%, POSSIBLE_IN_PLAY_QUOTE 6.3%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 20,570)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,337 | 35.7% |
| STALE_QUOTE | market_freshness | 4,099 | 19.9% |
| BOOK_QUALITY | execution | 3,324 | 16.2% |
| POOR_DATA | data | 1,840 | 8.9% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,216 | 5.9% |
| IDENTITY_AMBIGUOUS | mapping | 877 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 709 | 3.5% |
| LIMITED_DATA | data | 678 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 349 | 1.7% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 140 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 35.7%, market_freshness 19.9%, execution 16.2%, data 12.2%, market_freshness/coverage 9.4%, mapping 4.3%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.2%, START_UNVERIFIABLE 97.4%, LOW_DATA_QUALITY 75.2%, THIN_PLAYER_HISTORY 61.9%, STALE_KALSHI_QUOTE 55.9%, STALE_PLAYER_DATA 45.0%, MODEL_INTERNAL_DISAGREEMENT 41.5%, ASYMMETRIC_SAMPLE_SIZE 34.2%, WIDE_SPREAD 22.4%, MODEL_HIGH_UNCERTAINTY 19.5%, PLAYER_IDENTITY_RISK 17.8%, LOW_DISPLAYED_LIQUIDITY 8.6%, EVENT_MAPPING_RISK 8.5%, LEVEL_TRANSFER_RISK 8.0%, MODEL_CALIBRATION_OUTLIER 4.6%, EXTERNAL_MARKET_REJECTION 1.7%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 38.5%, POST_SETTLEMENT_OBSERVATION 35.7%, POSSIBLE_IN_PLAY_QUOTE 6.4%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 16559, "IDENTITY_AMBIGUOUS": 4011}; ticker orientation: {"VERIFIED": 20570}.

Checks: discipline:AMBIGUOUS 1340, discipline:PASS 19230, identity_confidence:AMBIGUOUS 3658, identity_confidence:PASS 16912, level_mapping:NA 1352, level_mapping:PASS 19218, market_pair:AMBIGUOUS 519, market_pair:NA 437, market_pair:PASS 19614, model_complement:NA 399, model_complement:PASS 20171, namesake:AMBIGUOUS 6, namesake:PASS 20564, physical_match_id:NA 6777, physical_match_id:PASS 13793, player_ids:PASS 20570, same_pair_other_event:PASS 20570, ticker_orientation:PASS 20570

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,657 | 3.7% | 3.1% | 1.2% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 24, "market_freshness/coverage": 22} | 5.47 | 0.2216 / 0.218 (875) | 25.7% | 2.4% | 3.2% | 3.0% |
| CHALLENGER | 13,643 | 16.7% | 5.9% | 11.1% | {"coverage": 1403, "market_freshness": 277, "market_freshness/coverage": 249, "data": 166, "model_calibration_or_unknown": 80, "execution": 41, "model_calibration": 41, "mapping": 17, "possible_market_error": 1} | 7.3 | 0.2212 / 0.2116 (3184) | 41.9% | 13.5% | 3.9% | 23.0% |
| DOUBLES | 2,874 | 46.6% | 46.7% | 6.5% | {"execution": 737, "mapping": 411, "market_freshness": 106, "market_freshness/coverage": 79, "coverage": 7} | 23.41 | 0.2983 / 0.2317 (728) | 8.1% | 0.0% | 100.0% | 6.5% |
| ITF_MEN | 27,585 | 25.4% | 17.6% | 34.1% | {"coverage": 2509, "market_freshness": 1453, "execution": 1059, "data": 1028, "market_freshness/coverage": 716, "mapping": 233, "model_calibration_or_unknown": 6, "model_calibration": 6} | 11.73 | 0.2187 / 0.1983 (5911) | 42.5% | 69.5% | 14.2% | 22.1% |
| ITF_WOMEN | 34,320 | 26.5% | 18.6% | 44.2% | {"coverage": 3339, "market_freshness": 2000, "execution": 1404, "data": 1223, "market_freshness/coverage": 802, "mapping": 210, "model_calibration_or_unknown": 99, "model_calibration": 23} | 12.42 | 0.2037 / 0.1943 (6727) | 43.1% | 57.1% | 10.1% | 22.2% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,964 | 5.9% | 5.1% | 1.4% | {"market_freshness": 113, "model_calibration_or_unknown": 53, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.69 | 0.2319 / 0.2213 (818) | 30.3% | 1.9% | 1.2% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.4% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 523 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 519 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 21.5h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 1296 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFMATCH-26NOV12VALRAT-RAT` | ITF_MEN | gen1_ledger | 92% / 4% | +88 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 10 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1333.0, ratio 3.64); no external reference |
| 6 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 7 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 8 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 9 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 117 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 10 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 11 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 19.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 1173 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 12 | `KXITFMATCH-26NOV10KOUPOR-POR` | ITF_MEN | fair_v1 | 87% / 2% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.9h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 305 min (STALE); data POOR (grade D, thinner serve sample 1554.0, ratio 1.02); no external reference |
| 13 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 14 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 547 min (STALE); no external reference |
| 17 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 18 | `KXITFMATCH-26NOV13ALMJAD-ALM` | ITF_MEN | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 385 min (STALE); data LIMITED (grade C, thinner serve sample 691.0, ratio 3.98); no external reference |
| 19 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 20 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 21 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 17.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1037 min (STALE); no external reference |
| 22 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 23 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 24 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 25 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 26 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 27 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 28 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 573 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 29 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 30 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 31 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 32 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 33 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 34 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 35 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 36 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 37 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 365 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 38 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 39 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 40 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 41 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 42 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 43 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 44 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 45 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 46 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 47 | `KXITFMATCH-26NOV14SCHJAD-SCH` | ITF_MEN | fair_v1 | 89% / 10% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 293 min (STALE); data LIMITED (grade C, thinner serve sample 691.0, ratio 2.01); no external reference |
| 48 | `KXITFMATCH-26NOV13JADZIN-ZIN` | ITF_MEN | fair_v1 | 89% / 10% | +80 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 76 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade D, thinner serve sample 691.0, ratio 5.99); no external reference |
| 49 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 50 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9737, "by_level_share_of_ge_25pp": {"ATP": 0.0119, "CHALLENGER": 0.1106, "DOUBLES": 0.0651, "ITF_MEN": 0.3408, "ITF_WOMEN": 0.4424, "OTHER": 0.0006, "WTA": 0.0143, "WTA125": 0.0142}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5587, "share_primary_cause_market_settled_or_in_play": 0.4503, "share_primary_cause_stale_quote_only": 0.1993}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 20570, "identity_ambiguous_share": 0.195, "ticker_orientation": {"VERIFIED": 20570}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 13793, "with_external": 652, "coverage": 0.0473, "external_status": {"EXTERNAL_STALE": 415, "AGREES_WITH_KALSHI": 224, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 415, "MODEL_LONE_OUTLIER": 224, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3436, "share_external_supports_model": 0.0199}, "pregame_clean_ge_25pp": {"n": 6190, "with_external": 619, "coverage": 0.1, "external_status": {"EXTERNAL_STALE": 389, "AGREES_WITH_KALSHI": 217, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 389, "MODEL_LONE_OUTLIER": 217, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3506, "share_external_supports_model": 0.021}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 491.0, "median_sample_ratio": 2.43, "median_min_matches": 18.0, "median_max_days_since_last": 246.0, "share_severe_asymmetry": 0.2048, "data_status": {"POOR": 11642, "LIMITED": 5208, "ADEQUATE": 3720}, "comparison_lt_10pp": {"median_thinner_serve_points": 1681.0, "median_sample_ratio": 1.71, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1689, "model_minus_observed": 0.0724, "kalshi_minus_observed": -0.0663, "brier_diff_model_minus_kalshi": 0.0044}, "4-10x": {"n": 1150, "model_minus_observed": 0.0872, "kalshi_minus_observed": -0.0571, "brier_diff_model_minus_kalshi": 0.0098}, "<2x": {"n": 4119, "model_minus_observed": 0.1027, "kalshi_minus_observed": -0.0198, "brier_diff_model_minus_kalshi": 0.0146}, ">=10x": {"n": 1407, "model_minus_observed": 0.1281, "kalshi_minus_observed": -0.0431, "brier_diff_model_minus_kalshi": 0.0184}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 8365, "model": {"intercept": -0.561, "slope": 0.815, "slope_se": 0.027}, "kalshi_mid_same_rows": {"intercept": 0.163, "slope": 1.056, "slope_se": 0.031}, "mean_extremity_model": 0.1742, "mean_extremity_kalshi": 0.1714, "model_brier": 0.2334, "kalshi_brier": 0.2035, "brier_diff_model_minus_kalshi": 0.0299, "brier_diff_se": 0.0021, "model_logloss": 0.6645, "kalshi_logloss": 0.5893}, "fair_v1": {"n": 8365, "model": {"intercept": -0.471, "slope": 1.018, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.207, "slope": 1.075, "slope_se": 0.031}, "mean_extremity_model": 0.1677, "mean_extremity_kalshi": 0.1712, "model_brier": 0.2161, "kalshi_brier": 0.2036, "brier_diff_model_minus_kalshi": 0.0125, "brier_diff_se": 0.0017, "model_logloss": 0.6217, "kalshi_logloss": 0.5894}, "gen1_elo": {"n": 8365, "model": {"intercept": -0.458, "slope": 0.999, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.211, "slope": 1.067, "slope_se": 0.03}, "mean_extremity_model": 0.174, "mean_extremity_kalshi": 0.1714, "model_brier": 0.2154, "kalshi_brier": 0.2037, "brier_diff_model_minus_kalshi": 0.0117, "brier_diff_se": 0.0017, "model_logloss": 0.6206, "kalshi_logloss": 0.5897}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2553, "share_ge_15": 0.4512, "median_abs_gap": 13.25, "n": 54035}, "gen1_elo": {"share_ge_25": 0.2532, "share_ge_15": 0.4468, "median_abs_gap": 13.02, "n": 54035}, "gen1_sr": {"share_ge_25": 0.3172, "share_ge_15": 0.5258, "median_abs_gap": 16.02, "n": 54035}, "gen2": {"share_ge_25": 0.3174, "share_ge_15": 0.5141, "median_abs_gap": 15.56, "n": 54035}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1512, "share_ge_15": 0.3548, "median_abs_gap": 10.71, "n": 40920}, "gen1_elo": {"share_ge_25": 0.1499, "share_ge_15": 0.3489, "median_abs_gap": 10.5, "n": 40920}, "gen1_sr": {"share_ge_25": 0.214, "share_ge_15": 0.4389, "median_abs_gap": 12.98, "n": 40923}, "gen2": {"share_ge_25": 0.2293, "share_ge_15": 0.4386, "median_abs_gap": 12.82, "n": 40924}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.47, "share_ge_25_all": 0.0368, "share_ge_25_pregame_clean": 0.0308}, "WTA": {"median_abs_gap_pregame_clean": 7.69, "share_ge_25_all": 0.0594, "share_ge_25_pregame_clean": 0.0506}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2337, "share_within_10pp_all": 0.4348, "share_within_10pp_pregame_clean": 0.4905, "corr_model_vs_mid_pregame_clean": 0.8497}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1202, "model_brier": 0.1971, "kalshi_brier": 0.1971, "brier_diff_model_minus_kalshi": 0.0}, "10-15": {"n_settled": 1454, "model_brier": 0.2214, "kalshi_brier": 0.2117, "brier_diff_model_minus_kalshi": 0.0097}, "15-25": {"n_settled": 1855, "model_brier": 0.2249, "kalshi_brier": 0.2069, "brier_diff_model_minus_kalshi": 0.0181}, "25-40": {"n_settled": 1049, "model_brier": 0.2251, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0212}, "3-5": {"n_settled": 788, "model_brier": 0.2077, "kalshi_brier": 0.207, "brier_diff_model_minus_kalshi": 0.0007}, "40+": {"n_settled": 215, "model_brier": 0.3093, "kalshi_brier": 0.1669, "brier_diff_model_minus_kalshi": 0.1424}, "5-10": {"n_settled": 1802, "model_brier": 0.2027, "kalshi_brier": 0.2005, "brier_diff_model_minus_kalshi": 0.0021}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'NO_SKILL:gen2|WTA', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.561, "slope": 0.815, "slope_se": 0.027}, "kalshi_slope": {"intercept": 0.163, "slope": 1.056, "slope_se": 0.031}, "n": 8365}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.496, "slope": 0.86, "slope_se": 0.023}, "kalshi_slope": {"intercept": 0.15, "slope": 1.058, "slope_se": 0.026}, "n": 10690}, "NO_SKILL:gen2|WTA": {"n_settled": 349, "model_brier": 0.2503, "kalshi_brier": 0.2266, "brier_diff_model_minus_kalshi": 0.0238, "brier_diff_se": 0.0089, "corr_model_outcome": 0.2571, "corr_kalshi_outcome": 0.3077}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 728, "model_brier": 0.2983, "kalshi_brier": 0.2317, "brier_diff_model_minus_kalshi": 0.0666, "brier_diff_se": 0.0109, "corr_model_outcome": 0.1135, "corr_kalshi_outcome": 0.2818}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
