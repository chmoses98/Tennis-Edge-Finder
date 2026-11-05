# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-05T21:22Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 80,010): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 19.1%, 25-40 13.7%, 40+ 8.0%; median gap 11.83 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.8%, Challenger 10.7%, doubles 6.7%). Main tour: ATP 3.8% and WTA 6.1% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 17,355): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.0%, STALE_QUOTE 19.5%, BOOK_QUALITY 17.7%, POOR_DATA 9.3%, POSSIBLY_IN_PLAY_QUOTE 5.7%, IDENTITY_AMBIGUOUS 4.3%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.0%, market_freshness 19.5%, execution 17.7%, data 12.7%, market_freshness/coverage 9.2%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 53.3% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.2% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 17,355 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.3% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.4% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 489.5 points vs 1716.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.033, Gen-2 0.828, Gen-1 ledger 0.868 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 885 model 0.2214 vs Kalshi 0.2031; n 185 model 0.2959 vs Kalshi 0.1755.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 340,260 model-market comparisons (556,950 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 113,222 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-05T21:06:10.850705+00:00'], shadow board 91,979 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-05T21:06:15.648657+00:00'], Model 4 42,209 rows, 28,176 settled tickers, 10,618 tickers with an external scan.
* By model: {"gen1_ledger": 76315, "gen1_elo": 46220, "fair_v1": 46220, "gen2": 46220, "gen1_sr": 46220, "model4_fundamental": 39574, "model4_conditioned": 39491}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 80,010 | 14.1 | 9.6 | 20.2 | 15.3 | 19.1 | 13.7 | 8.0 | 11.83 | 40.8% | 21.7% |
| MW fair_v1 | 46,220 | 12.8 | 8.7 | 18.7 | 15.4 | 19.6 | 14.8 | 9.9 | 13.03 | 44.3% | 24.7% |
| MW gen1_elo | 46,220 | 12.6 | 8.8 | 19.3 | 15.4 | 19.5 | 14.6 | 9.8 | 12.79 | 43.9% | 24.4% |
| MW gen1_ledger | 33,790 | 15.8 | 10.9 | 22.2 | 15.2 | 18.4 | 12.1 | 5.5 | 10.27 | 36.0% | 17.5% |
| MW gen1_sr | 46,220 | 10.1 | 7.3 | 16.7 | 13.9 | 20.7 | 18.8 | 12.6 | 15.82 | 52.0% | 31.3% |
| MW gen2 | 46,220 | 11.0 | 7.6 | 16.6 | 13.8 | 19.6 | 17.7 | 13.7 | 15.45 | 51.0% | 31.4% |
| all families model4_conditioned | 39,491 | 22.2 | 18.0 | 34.2 | 17.2 | 5.0 | 2.2 | 1.2 | 6.07 | 8.5% | 3.4% |
| all families model4_fundamental | 39,574 | 17.4 | 13.5 | 33.9 | 19.9 | 10.0 | 3.8 | 1.5 | 7.62 | 15.3% | 5.4% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.1%, >=15pp 40.8%, >=20pp 30.0%, >=25pp 21.7%, >=30pp 15.6%, >=40pp 8.0%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.36pp; >=10pp 45.0%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,920 | 28.4 | 15.7 | 27.6 | 13.4 | 10.6 | 3.6 | 0.6 | 5.77 | 14.9% | 4.3% |
| CHALLENGER | 6,913 | 15.8 | 9.8 | 20.7 | 15.3 | 16.2 | 11.4 | 10.7 | 10.94 | 38.3% | 22.1% |
| ITF_MEN | 13,039 | 9.8 | 7.4 | 17.1 | 15.2 | 21.2 | 17.3 | 12.0 | 15.18 | 50.5% | 29.3% |
| ITF_WOMEN | 18,010 | 9.5 | 7.1 | 16.0 | 14.8 | 22.1 | 18.3 | 12.1 | 15.89 | 52.6% | 30.5% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,005 | 16.7 | 13.2 | 24.6 | 21.0 | 16.5 | 6.9 | 1.1 | 8.68 | 24.5% | 8.0% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,920 | 26.9 | 15.8 | 26.0 | 15.4 | 11.4 | 3.7 | 0.8 | 6.02 | 15.9% | 4.5% |
| CHALLENGER | 6,913 | 14.7 | 9.1 | 18.6 | 14.0 | 18.7 | 13.5 | 11.3 | 12.5 | 43.6% | 24.9% |
| ITF_MEN | 13,039 | 8.2 | 6.1 | 15.2 | 13.8 | 20.0 | 20.4 | 16.3 | 17.88 | 56.7% | 36.7% |
| ITF_WOMEN | 18,010 | 7.8 | 5.8 | 14.1 | 12.9 | 20.7 | 21.2 | 17.6 | 19.13 | 59.5% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,005 | 14.1 | 10.2 | 21.9 | 16.1 | 22.2 | 13.0 | 2.6 | 11.2 | 37.8% | 15.6% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,920 | 22.9 | 14.0 | 25.2 | 15.6 | 15.0 | 6.1 | 1.2 | 7.18 | 22.3% | 7.3% |
| CHALLENGER | 6,913 | 15.2 | 9.6 | 20.9 | 15.6 | 16.0 | 11.9 | 10.8 | 11.2 | 38.8% | 22.7% |
| ITF_MEN | 13,039 | 9.5 | 7.2 | 17.3 | 14.3 | 21.9 | 17.3 | 12.4 | 15.61 | 51.7% | 29.8% |
| ITF_WOMEN | 18,010 | 9.3 | 6.9 | 16.3 | 15.8 | 22.2 | 18.1 | 11.5 | 15.59 | 51.8% | 29.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,005 | 22.7 | 17.0 | 31.9 | 15.2 | 8.8 | 3.3 | 1.1 | 6.12 | 13.2% | 4.4% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,321 | 26.8 | 19.7 | 30.0 | 12.3 | 8.2 | 2.6 | 0.4 | 5.36 | 11.2% | 3.0% |
| CHALLENGER | 4,457 | 22.2 | 14.5 | 27.8 | 14.7 | 13.6 | 5.8 | 1.5 | 7.1 | 20.9% | 7.3% |
| DOUBLES | 2,503 | 5.0 | 4.6 | 12.7 | 11.0 | 20.1 | 24.8 | 21.8 | 23.51 | 66.7% | 46.6% |
| ITF_MEN | 9,675 | 13.1 | 9.6 | 21.3 | 15.8 | 21.5 | 13.0 | 5.8 | 11.77 | 40.3% | 18.8% |
| ITF_WOMEN | 11,678 | 13.3 | 9.2 | 20.0 | 15.7 | 21.4 | 14.9 | 5.5 | 12.24 | 41.8% | 20.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,751 | 24.2 | 15.9 | 31.2 | 16.7 | 9.1 | 2.6 | 0.2 | 6.57 | 12.0% | 2.9% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,805 | 28.9 | 15.9 | 28.0 | 13.3 | 10.4 | 3.2 | 0.3 | 5.64 | 13.9% | 3.5% |
| CHALLENGER | 4,891 | 20.4 | 12.2 | 25.6 | 18.1 | 16.2 | 6.0 | 1.6 | 8.28 | 23.8% | 7.6% |
| ITF_MEN | 9,540 | 12.0 | 8.7 | 20.7 | 17.4 | 22.0 | 14.1 | 5.3 | 12.38 | 41.3% | 19.3% |
| ITF_WOMEN | 13,269 | 11.3 | 8.6 | 18.8 | 17.0 | 24.0 | 15.2 | 5.0 | 13.23 | 44.2% | 20.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,893 | 17.0 | 13.3 | 24.9 | 21.3 | 16.5 | 6.3 | 0.6 | 8.52 | 23.4% | 6.9% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,805 | 27.2 | 16.2 | 26.2 | 15.4 | 11.3 | 3.3 | 0.4 | 5.96 | 15.0% | 3.7% |
| CHALLENGER | 4,891 | 18.5 | 11.4 | 23.4 | 16.4 | 19.2 | 9.3 | 1.9 | 9.06 | 30.3% | 11.1% |
| ITF_MEN | 9,541 | 9.7 | 7.3 | 17.6 | 16.0 | 21.7 | 18.6 | 9.2 | 14.86 | 49.5% | 27.8% |
| ITF_WOMEN | 13,270 | 8.8 | 6.8 | 16.0 | 14.4 | 22.7 | 20.5 | 10.8 | 16.55 | 54.0% | 31.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,893 | 14.3 | 10.3 | 22.1 | 16.2 | 22.4 | 12.7 | 1.9 | 11.03 | 37.0% | 14.6% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,264 | 26.9 | 19.9 | 29.9 | 12.5 | 8.0 | 2.5 | 0.3 | 5.32 | 10.8% | 2.8% |
| CHALLENGER | 3,938 | 23.5 | 15.4 | 28.9 | 14.8 | 13.0 | 4.0 | 0.4 | 6.62 | 17.4% | 4.4% |
| DOUBLES | 2,351 | 4.8 | 4.6 | 12.9 | 11.1 | 19.9 | 24.8 | 21.8 | 23.39 | 66.4% | 46.5% |
| ITF_MEN | 8,323 | 13.9 | 10.1 | 22.9 | 16.3 | 21.5 | 11.5 | 3.8 | 10.83 | 36.8% | 15.3% |
| ITF_WOMEN | 10,003 | 14.0 | 9.7 | 21.1 | 16.2 | 21.6 | 13.8 | 3.6 | 11.42 | 39.0% | 17.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,690 | 24.5 | 16.3 | 31.2 | 16.8 | 9.1 | 2.1 | 0.1 | 6.43 | 11.2% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,503 | 5.0 | 4.6 | 12.7 | 11.0 | 20.1 | 24.8 | 21.8 | 23.51 | 66.7% | 46.6% |
| singles | 31,287 | 16.6 | 11.4 | 23.0 | 15.5 | 18.3 | 11.0 | 4.2 | 9.74 | 33.5% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 156 | 7.7 | 8.3 | 12.2 | 7.7 | 20.5 | 28.2 | 15.4 | 21.41 | 64.1% | 43.6% |
| Clay | 9,446 | 12.7 | 9.1 | 19.8 | 15.7 | 19.7 | 13.8 | 9.2 | 12.6 | 42.7% | 23.0% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 30,141 | 13.4 | 8.8 | 18.8 | 15.2 | 19.2 | 14.8 | 9.8 | 12.86 | 43.9% | 24.7% |
| UNKNOWN | 6,240 | 10.4 | 7.6 | 17.0 | 16.4 | 21.5 | 16.1 | 11.1 | 14.39 | 48.6% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 13,073 | 19.4 | 12.0 | 22.4 | 15.9 | 15.0 | 9.1 | 6.1 | 8.9 | 30.3% | 15.3% |
| B | 5,645 | 12.8 | 8.8 | 19.8 | 15.7 | 19.5 | 12.7 | 10.8 | 12.59 | 43.0% | 23.4% |
| C | 6,560 | 11.9 | 8.9 | 19.5 | 15.8 | 18.6 | 14.8 | 10.6 | 12.96 | 44.0% | 25.4% |
| D | 7,497 | 11.7 | 8.4 | 17.9 | 15.4 | 21.5 | 15.7 | 9.4 | 13.76 | 46.7% | 25.1% |
| F | 13,445 | 7.5 | 5.6 | 14.8 | 14.6 | 23.5 | 20.8 | 13.1 | 17.73 | 57.5% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,999 | 24.5 | 16.0 | 29.2 | 14.9 | 10.7 | 3.4 | 1.2 | 6.38 | 15.3% | 4.6% |
| B | 4,744 | 16.6 | 10.8 | 24.2 | 16.9 | 18.8 | 9.6 | 3.1 | 9.68 | 31.5% | 12.7% |
| C | 6,679 | 11.2 | 7.9 | 19.5 | 14.8 | 20.9 | 15.7 | 10.3 | 13.49 | 46.8% | 25.9% |
| D | 5,066 | 14.6 | 10.1 | 21.5 | 15.4 | 20.6 | 12.7 | 5.3 | 11.19 | 38.5% | 18.0% |
| F | 8,302 | 10.2 | 8.4 | 16.2 | 14.6 | 23.3 | 19.5 | 7.8 | 15.33 | 50.6% | 27.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 14,790 | 17.7 | 11.0 | 21.5 | 15.8 | 15.4 | 10.0 | 8.7 | 9.97 | 34.1% | 18.7% |
| LIMITED | 10,098 | 13.6 | 9.8 | 20.4 | 15.9 | 19.3 | 13.4 | 7.6 | 11.86 | 40.3% | 20.9% |
| POOR | 21,332 | 9.1 | 6.6 | 16.0 | 14.9 | 22.7 | 18.9 | 11.8 | 16.14 | 53.4% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,714 | 23.8 | 17.8 | 33.2 | 15.6 | 6.4 | 2.9 | 0.4 | 5.92 | 9.7% | 3.3% |
| GAME_SPREAD | 6,576 | 22.5 | 15.2 | 32.2 | 16.9 | 9.0 | 3.4 | 0.6 | 6.72 | 13.1% | 4.0% |
| MATCH_WINNER | 33,790 | 15.8 | 10.9 | 22.2 | 15.2 | 18.4 | 12.1 | 5.5 | 10.27 | 36.0% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 16,156 | 27.9 | 16.7 | 30.7 | 12.7 | 9.2 | 2.5 | 0.3 | 5.64 | 11.9% | 2.7% |
| TOTAL_GAMES | 11,055 | 9.8 | 10.8 | 35.5 | 26.0 | 10.7 | 4.3 | 3.0 | 9.22 | 17.9% | 7.2% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,996 | 24.4 | 28.9 | 33.2 | 8.1 | 4.0 | 1.1 | 0.3 | 4.79 | 5.3% | 1.4% |
| GAME_SPREAD | 9,111 | 46.8 | 16.1 | 24.8 | 7.5 | 2.3 | 1.9 | 0.6 | 3.3 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,384 | 6.5 | 9.8 | 40.2 | 30.2 | 7.5 | 3.3 | 2.4 | 9.22 | 13.2% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,031 | 23.9 | 16.6 | 34.8 | 14.7 | 6.9 | 2.6 | 0.5 | 6.05 | 10.0% | 3.1% |
| GAME_SPREAD | 9,120 | 20.6 | 13.6 | 28.2 | 20.1 | 11.9 | 4.5 | 1.1 | 7.63 | 17.6% | 5.6% |
| TOTAL_GAMES | 16,423 | 10.0 | 10.8 | 36.2 | 24.3 | 11.5 | 4.5 | 2.6 | 9.07 | 18.7% | 7.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 46,220 | 44.3% | 24.7% | 13.03 | 35.4% | 15.1% | 10.71 |
| gen1_elo | 46,220 | 43.9% | 24.4% | 12.79 | 34.9% | 14.9% | 10.49 |
| gen1_sr | 46,220 | 52.0% | 31.3% | 15.82 | 44.0% | 21.7% | 13.01 |
| gen2 | 46,220 | 51.0% | 31.4% | 15.45 | 43.9% | 23.1% | 12.86 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 19,896 | 15.5 | 10.5 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 26,324 | 10.8 | 7.4 | 16.8 | 14.0 | 19.3 | 17.1 | 14.8 | 15.45 | 51.1% | 31.9% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 27,258 | 16.4 | 11.2 | 22.8 | 15.3 | 17.9 | 11.6 | 4.8 | 9.88 | 34.3% | 16.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 80,010 | 27258 | 23368 | 29384 | 24.7 | 126.0 | 1451.1 |
| ge_15pp | 32,646 | 9354 | 8324 | 14968 | 28.1 | 431.8 | 1451.1 |
| ge_25pp | 17,355 | 4468 | 3632 | 9255 | 33.1 | 579.9 | 1431.1 |
| lt_10pp | 35,115 | 13744 | 11051 | 10320 | 22.6 | 47.9 | 1421.1 |

Current slate `SL-20261105T212244Z-b9182c91`: 264 priced rows, quote age at build {'median': 16.9, 'max': 16.9}, freshness {'AGING': 264}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 49 | 0.0 | 0.0 | 36.7 | 6.1 | 32.6 | 20.4 | 4.1 | 18.34 | 57.1% | 24.5% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,606 | 19.1 | 10.9 | 25.4 | 17.9 | 18.2 | 7.5 | 1.0 | 8.86 | 26.6% | 8.4% |
| KALSHI_LONE_OUTLIER | 30 | 6.7 | 6.7 | 73.3 | 6.7 | 3.3 | 3.3 | 0.0 | 6.16 | 6.7% | 3.3% |
| MARKETS_AGREE | 936 | 65.8 | 34.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.2 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,026 | 0.0 | 2.3 | 36.8 | 26.5 | 24.2 | 9.3 | 0.9 | 11.86 | 34.4% | 10.2% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 46,220 | 7676 (16.6%) | 26.4% | 1.0% | {"EXTERNAL_STALE": 4606, "AGREES_WITH_KALSHI": 2026, "ALL_AGREE": 936, "SUPPORTS_MODEL_DIRECTION": 48, "AGREES_WITH_MODEL": 30, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 20,493 | 1953 (9.5%) | 35.7% | 1.5% | {"EXTERNAL_STALE": 1226, "AGREES_WITH_KALSHI": 697, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 11,425 | 607 (5.3%) | 33.9% | 2.1% | {"EXTERNAL_STALE": 388, "AGREES_WITH_KALSHI": 206, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,400 | 577 (10.7%) | 34.5% | 2.2% | {"EXTERNAL_STALE": 365, "AGREES_WITH_KALSHI": 199, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 18,602 | 4356 (23.4%) | 18.2% | 1.0% | {"EXTERNAL_STALE": 2554, "ALL_AGREE": 936, "AGREES_WITH_KALSHI": 793, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 26, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 9,058 | 10.4 | 7.7 | 19.5 | 14.6 | 21.6 | 16.2 | 9.9 | 14.08 | 47.7% | 26.1% |
| 4-10x | 6,204 | 11.3 | 8.6 | 18.4 | 15.3 | 22.0 | 14.3 | 10.1 | 13.75 | 46.4% | 24.4% |
| <2x | 23,563 | 14.8 | 9.8 | 19.7 | 16.1 | 17.6 | 13.2 | 8.8 | 11.57 | 39.6% | 22.0% |
| >=10x | 7,395 | 10.5 | 6.4 | 15.0 | 14.4 | 21.7 | 18.9 | 13.1 | 16.35 | 53.7% | 32.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 12,092 | 12.4 | 8.7 | 19.9 | 16.2 | 19.0 | 13.5 | 10.3 | 12.69 | 42.8% | 23.8% |
| 300-1000 | 10,009 | 11.8 | 8.8 | 17.7 | 15.2 | 20.7 | 16.4 | 9.5 | 13.69 | 46.5% | 25.9% |
| <300 | 14,551 | 8.3 | 5.8 | 15.1 | 14.7 | 23.1 | 19.9 | 13.1 | 17.1 | 56.0% | 32.9% |
| >=3000 | 9,568 | 21.2 | 13.0 | 23.8 | 15.7 | 14.0 | 7.3 | 5.0 | 7.75 | 26.3% | 12.3% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1400 | 0.5471 | 0.4078 | 0.49 | +0.057 | -0.082 | 0.0004 ± 0.0041 |
| ratio 4-10x | 964 | 0.576 | 0.4312 | 0.4865 | +0.089 | -0.055 | 0.0091 ± 0.0051 |
| ratio <2x | 3410 | 0.5367 | 0.4135 | 0.4361 | +0.101 | -0.022 | 0.0146 ± 0.0024 |
| ratio >=10x | 1179 | 0.564 | 0.3906 | 0.4461 | +0.118 | -0.056 | 0.0148 ± 0.0052 |
| thinner_sample 1000-3000 | 1923 | 0.5389 | 0.4114 | 0.4477 | +0.091 | -0.036 | 0.0109 ± 0.0033 |
| thinner_sample 300-1000 | 1582 | 0.5627 | 0.4223 | 0.4753 | +0.087 | -0.053 | 0.0043 ± 0.0039 |
| thinner_sample <300 | 2270 | 0.5573 | 0.3892 | 0.4537 | +0.103 | -0.065 | 0.0132 ± 0.0037 |
| thinner_sample >=3000 | 1178 | 0.5305 | 0.4367 | 0.4457 | +0.085 | -0.009 | 0.0158 ± 0.0033 |
| data_status ADEQUATE | 1915 | 0.5322 | 0.4288 | 0.4397 | +0.092 | -0.011 | 0.0156 ± 0.0028 |
| data_status LIMITED | 1692 | 0.5475 | 0.4149 | 0.4675 | +0.080 | -0.053 | 0.0066 ± 0.0036 |
| data_status POOR | 3346 | 0.5591 | 0.3987 | 0.4588 | +0.100 | -0.060 | 0.0106 ± 0.003 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1000 | 0.1972 | 0.1976 | -0.0003 ± 0.0005 | 0.5741 | 0.575 | 0.5028 | 0.4877 | 0.5 | -0.096 ± 0.0149 | -0.0087 (8) |
| 3-5 | 640 | 0.2046 | 0.2046 | +0.0000 ± 0.0014 | 0.5931 | 0.5916 | 0.5027 | 0.4628 | 0.4813 | -0.095 ± 0.0183 | 0.01 (2) |
| 5-10 | 1491 | 0.2016 | 0.2008 | +0.0008 ± 0.0017 | 0.5896 | 0.5852 | 0.5113 | 0.4375 | 0.4668 | -0.090 ± 0.012 | -0.0143 (7) |
| 10-15 | 1207 | 0.2185 | 0.2089 | +0.0095 ± 0.0033 | 0.629 | 0.6012 | 0.5228 | 0.3993 | 0.4217 | -0.106 ± 0.0134 | -0.048 (5) |
| 15-25 | 1545 | 0.2245 | 0.2079 | +0.0166 ± 0.0045 | 0.6435 | 0.5992 | 0.5744 | 0.3797 | 0.435 | -0.102 ± 0.0116 | -0.004 (10) |
| 25-40 | 885 | 0.2214 | 0.2031 | +0.0183 ± 0.0091 | 0.6316 | 0.5865 | 0.6506 | 0.3406 | 0.4667 | -0.068 ± 0.0138 | -0.06 (2) |
| 40+ | 185 | 0.2959 | 0.1755 | +0.1204 ± 0.0276 | 0.7971 | 0.524 | 0.7304 | 0.2755 | 0.3784 | -0.083 ± 0.0268 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5258 | 0.1855 | 0.1864 | -0.0009 ± 0.0002 | 0.5468 | 0.5478 | 0.4887 | 0.4734 | 0.5044 | -0.022 ± 0.006 | -0.01 (28) |
| 3-5 | 3538 | 0.1973 | 0.1957 | +0.0016 ± 0.0006 | 0.5743 | 0.5685 | 0.4805 | 0.4408 | 0.4401 | -0.055 ± 0.0075 | 0.0 (3) |
| 5-10 | 7613 | 0.2012 | 0.198 | +0.0032 ± 0.0008 | 0.5881 | 0.5772 | 0.4843 | 0.4106 | 0.4264 | -0.043 ± 0.0052 | -0.0114 (22) |
| 10-15 | 6318 | 0.2014 | 0.1855 | +0.0160 ± 0.0014 | 0.5892 | 0.5444 | 0.4846 | 0.3607 | 0.3583 | -0.064 ± 0.0054 | -0.0281 (16) |
| 15-25 | 7991 | 0.2056 | 0.1668 | +0.0388 ± 0.0018 | 0.603 | 0.4958 | 0.4988 | 0.3033 | 0.3026 | -0.069 ± 0.0046 | -0.0027 (45) |
| 25-40 | 6167 | 0.2226 | 0.1257 | +0.0970 ± 0.0028 | 0.6394 | 0.3865 | 0.5265 | 0.2126 | 0.2196 | -0.058 ± 0.0044 | -0.0733 (3) |
| 40+ | 4084 | 0.3826 | 0.0442 | +0.3384 ± 0.0038 | 0.9968 | 0.1715 | 0.631 | 0.1024 | 0.0585 | -0.077 ± 0.0031 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 803 | 0.2042 | 0.2045 | -0.0004 ± 0.0005 | 0.5888 | 0.59 | 0.5065 | 0.4917 | 0.5143 | -0.103 ± 0.0172 | -0.0117 (6) |
| 3-5 | 571 | 0.2107 | 0.2077 | +0.0030 ± 0.0015 | 0.6039 | 0.5977 | 0.5128 | 0.4732 | 0.4518 | -0.132 ± 0.0205 | 0.01 (2) |
| 5-10 | 1283 | 0.2071 | 0.2052 | +0.0019 ± 0.0019 | 0.6006 | 0.5954 | 0.5387 | 0.4642 | 0.4918 | -0.089 ± 0.013 | -0.01 (4) |
| 10-15 | 1113 | 0.2117 | 0.2064 | +0.0052 ± 0.0034 | 0.6158 | 0.5985 | 0.5628 | 0.4384 | 0.4825 | -0.097 ± 0.0142 | -0.04 (5) |
| 15-25 | 1623 | 0.2307 | 0.212 | +0.0187 ± 0.0045 | 0.6559 | 0.6083 | 0.5837 | 0.3883 | 0.4393 | -0.098 ± 0.0117 | -0.012 (10) |
| 25-40 | 1147 | 0.2659 | 0.1967 | +0.0692 ± 0.0082 | 0.7422 | 0.573 | 0.658 | 0.3439 | 0.3932 | -0.119 ± 0.0131 | -0.008 (5) |
| 40+ | 413 | 0.3707 | 0.162 | +0.2088 ± 0.0198 | 1.0078 | 0.4899 | 0.7345 | 0.2458 | 0.2906 | -0.086 ± 0.0191 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4524 | 0.1918 | 0.1921 | -0.0003 ± 0.0002 | 0.5592 | 0.5596 | 0.5078 | 0.4927 | 0.5106 | -0.038 ± 0.0067 | -0.0154 (26) |
| 3-5 | 3072 | 0.1925 | 0.1915 | +0.0010 ± 0.0006 | 0.5615 | 0.5583 | 0.5106 | 0.471 | 0.4775 | -0.045 ± 0.0081 | 0.01 (2) |
| 5-10 | 6805 | 0.1977 | 0.1942 | +0.0035 ± 0.0008 | 0.5804 | 0.5679 | 0.5075 | 0.4335 | 0.45 | -0.041 ± 0.0054 | -0.0117 (6) |
| 10-15 | 5676 | 0.2017 | 0.1913 | +0.0104 ± 0.0015 | 0.5927 | 0.5596 | 0.5103 | 0.3864 | 0.4072 | -0.044 ± 0.0059 | -0.0189 (18) |
| 15-25 | 7999 | 0.2165 | 0.1808 | +0.0357 ± 0.0019 | 0.6292 | 0.5303 | 0.5237 | 0.3282 | 0.3372 | -0.060 ± 0.0048 | -0.0084 (43) |
| 25-40 | 7246 | 0.2503 | 0.1368 | +0.1134 ± 0.0028 | 0.7066 | 0.4186 | 0.5597 | 0.2427 | 0.2258 | -0.080 ± 0.0043 | -0.0095 (20) |
| 40+ | 5647 | 0.4013 | 0.0591 | +0.3421 ± 0.0037 | 1.0578 | 0.2132 | 0.6543 | 0.1191 | 0.0808 | -0.074 ± 0.0032 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 978 | 0.1957 | 0.1971 | -0.0014 ± 0.0005 | 0.571 | 0.5744 | 0.5029 | 0.4875 | 0.5337 | -0.050 ± 0.0148 | -0.012 (10) |
| 3-5 | 680 | 0.2064 | 0.2049 | +0.0015 ± 0.0014 | 0.5983 | 0.5931 | 0.4944 | 0.4549 | 0.4574 | -0.112 ± 0.0182 | -0.0 (4) |
| 5-10 | 1528 | 0.2024 | 0.199 | +0.0033 ± 0.0017 | 0.5897 | 0.5803 | 0.5124 | 0.4387 | 0.4522 | -0.103 ± 0.0118 | -0.01 (9) |
| 10-15 | 1223 | 0.2111 | 0.202 | +0.0090 ± 0.0032 | 0.6127 | 0.5861 | 0.5364 | 0.4133 | 0.4399 | -0.107 ± 0.0129 | -0.0286 (7) |
| 15-25 | 1471 | 0.2307 | 0.2125 | +0.0182 ± 0.0047 | 0.6586 | 0.6093 | 0.5853 | 0.3911 | 0.4412 | -0.107 ± 0.0121 | -0.03 (1) |
| 25-40 | 878 | 0.2117 | 0.2079 | +0.0038 ± 0.0091 | 0.611 | 0.5976 | 0.6585 | 0.3477 | 0.4954 | -0.056 ± 0.0139 | -0.0267 (3) |
| 40+ | 195 | 0.3097 | 0.1824 | +0.1274 ± 0.0275 | 0.8383 | 0.5387 | 0.7419 | 0.2873 | 0.3846 | -0.087 ± 0.0282 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5081 | 0.185 | 0.1857 | -0.0007 ± 0.0002 | 0.5452 | 0.5461 | 0.4857 | 0.4703 | 0.4897 | -0.032 ± 0.0061 | -0.0137 (41) |
| 3-5 | 3602 | 0.2038 | 0.2021 | +0.0016 ± 0.0006 | 0.5917 | 0.5863 | 0.477 | 0.4376 | 0.4375 | -0.055 ± 0.0076 | -0.01 (19) |
| 5-10 | 7790 | 0.1959 | 0.1909 | +0.0050 ± 0.0007 | 0.575 | 0.5592 | 0.4872 | 0.4132 | 0.4166 | -0.054 ± 0.005 | -0.0105 (37) |
| 10-15 | 6271 | 0.1933 | 0.1783 | +0.0151 ± 0.0013 | 0.5712 | 0.5276 | 0.4938 | 0.3706 | 0.3708 | -0.062 ± 0.0054 | -0.0146 (13) |
| 15-25 | 8068 | 0.2113 | 0.1721 | +0.0392 ± 0.0018 | 0.6165 | 0.5077 | 0.5121 | 0.3176 | 0.3151 | -0.070 ± 0.0046 | -0.0533 (3) |
| 25-40 | 6112 | 0.217 | 0.1269 | +0.0901 ± 0.0029 | 0.6273 | 0.3891 | 0.5291 | 0.2135 | 0.2309 | -0.049 ± 0.0044 | -0.02 (4) |
| 40+ | 4045 | 0.3918 | 0.0494 | +0.3424 ± 0.004 | 1.0213 | 0.1845 | 0.6405 | 0.1086 | 0.0658 | -0.076 ± 0.0033 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1410 | 0.1969 | 0.197 | -0.0001 ± 0.0004 | 0.5722 | 0.5721 | 0.5087 | 0.4937 | 0.4986 | -0.068 ± 0.0121 | -0.0213 (54) |
| 3-5 | 1007 | 0.1884 | 0.1882 | +0.0002 ± 0.0011 | 0.5547 | 0.5523 | 0.4953 | 0.4554 | 0.4717 | -0.058 ± 0.0139 | -0.0194 (34) |
| 5-10 | 2040 | 0.199 | 0.1945 | +0.0044 ± 0.0015 | 0.5863 | 0.5718 | 0.5069 | 0.4332 | 0.4402 | -0.074 ± 0.01 | -0.005 (78) |
| 10-15 | 1403 | 0.2142 | 0.2015 | +0.0127 ± 0.003 | 0.6218 | 0.5866 | 0.5414 | 0.4186 | 0.4269 | -0.090 ± 0.0123 | 0.0014 (65) |
| 15-25 | 1825 | 0.2305 | 0.2069 | +0.0235 ± 0.0042 | 0.6578 | 0.5975 | 0.5891 | 0.3941 | 0.4334 | -0.088 ± 0.0108 | -0.0214 (59) |
| 25-40 | 1108 | 0.24 | 0.2099 | +0.0302 ± 0.0084 | 0.6857 | 0.6025 | 0.6881 | 0.3759 | 0.4838 | -0.088 ± 0.0129 | -0.0252 (27) |
| 40+ | 393 | 0.3271 | 0.2023 | +0.1247 ± 0.0217 | 0.9425 | 0.5885 | 0.8163 | 0.3403 | 0.4631 | -0.098 ± 0.0203 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5188 | 0.1776 | 0.1778 | -0.0002 ± 0.0002 | 0.5256 | 0.5255 | 0.5124 | 0.4971 | 0.5093 | -0.037 ± 0.0059 | -0.0145 (98) |
| 3-5 | 3574 | 0.1954 | 0.1947 | +0.0007 ± 0.0006 | 0.5697 | 0.5673 | 0.5002 | 0.4605 | 0.4715 | -0.040 ± 0.0075 | -0.0204 (72) |
| 5-10 | 7268 | 0.1957 | 0.1895 | +0.0062 ± 0.0008 | 0.5774 | 0.5588 | 0.5007 | 0.4271 | 0.4227 | -0.061 ± 0.0052 | -0.0084 (134) |
| 10-15 | 4983 | 0.2089 | 0.1928 | +0.0160 ± 0.0015 | 0.6085 | 0.5663 | 0.5366 | 0.4137 | 0.4086 | -0.071 ± 0.0063 | -0.0053 (106) |
| 15-25 | 6056 | 0.2301 | 0.199 | +0.0311 ± 0.0023 | 0.6614 | 0.5771 | 0.5749 | 0.3796 | 0.3984 | -0.067 ± 0.0058 | -0.026 (108) |
| 25-40 | 3988 | 0.257 | 0.1893 | +0.0677 ± 0.0043 | 0.7273 | 0.5518 | 0.6393 | 0.3266 | 0.3774 | -0.068 ± 0.0067 | -0.0246 (52) |
| 40+ | 1759 | 0.3702 | 0.16 | +0.2103 ± 0.0098 | 1.0448 | 0.476 | 0.744 | 0.2435 | 0.2939 | -0.064 ± 0.0091 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 6953 | 1.033 ± 0.033 | 1.105 | 0.1694 | 0.1696 | 0.2143 | 0.2033 |
| gen2 | 6953 | 0.828 ± 0.03 | 1.077 | 0.1736 | 0.1699 | 0.2327 | 0.2031 |
| gen1_elo | 6953 | 1.011 ± 0.032 | 1.095 | 0.176 | 0.1696 | 0.2135 | 0.2034 |
| gen1_sr | 6953 | 1.011 ± 0.04 | 1.136 | 0.1335 | 0.1716 | 0.2291 | 0.2028 |
| gen1_ledger | 9186 | 0.868 ± 0.025 | 1.077 | 0.1902 | 0.1766 | 0.2165 | 0.1999 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 32,646)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 7,531 | 23.1% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,359 | 22.5% |
| BOOK_QUALITY | execution | 5,901 | 18.1% |
| POOR_DATA | data | 3,801 | 11.6% |
| LIMITED_DATA | data | 2,028 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,857 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,358 | 4.2% |
| IDENTITY_AMBIGUOUS | mapping | 1,336 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 932 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 542 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 23.1%, coverage 22.5%, execution 18.1%, data 17.9%, market_freshness/coverage 8.5%, model_calibration_or_unknown 4.2%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.5%, LOW_DATA_QUALITY 71.6%, THIN_PLAYER_HISTORY 59.9%, STALE_PLAYER_DATA 52.0%, STALE_KALSHI_QUOTE 45.9%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 24.3%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 15.3%, LEVEL_TRANSFER_RISK 10.1%, LOW_DISPLAYED_LIQUIDITY 8.4%, EVENT_MAPPING_RISK 7.2%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.0%, POST_SETTLEMENT_OBSERVATION 22.5%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 17,355)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,896 | 34.0% |
| STALE_QUOTE | market_freshness | 3,378 | 19.5% |
| BOOK_QUALITY | execution | 3,065 | 17.7% |
| POOR_DATA | data | 1,612 | 9.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 991 | 5.7% |
| IDENTITY_AMBIGUOUS | mapping | 741 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 609 | 3.5% |
| LIMITED_DATA | data | 595 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 334 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 133 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.0%, market_freshness 19.5%, execution 17.7%, data 12.7%, market_freshness/coverage 9.2%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 75.0%, THIN_PLAYER_HISTORY 61.9%, STALE_KALSHI_QUOTE 53.3%, STALE_PLAYER_DATA 45.9%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 23.8%, MODEL_HIGH_UNCERTAINTY 19.3%, PLAYER_IDENTITY_RISK 18.4%, LEVEL_TRANSFER_RISK 8.9%, EVENT_MAPPING_RISK 8.9%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.0%, POST_SETTLEMENT_OBSERVATION 34.0%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 13838, "IDENTITY_AMBIGUOUS": 3517}; ticker orientation: {"VERIFIED": 17355}.

Checks: discipline:AMBIGUOUS 1167, discipline:PASS 16188, identity_confidence:AMBIGUOUS 3187, identity_confidence:PASS 14168, level_mapping:NA 1179, level_mapping:PASS 16176, market_pair:AMBIGUOUS 491, market_pair:NA 376, market_pair:PASS 16488, model_complement:NA 338, model_complement:PASS 17017, namesake:AMBIGUOUS 6, namesake:PASS 17349, physical_match_id:NA 5930, physical_match_id:PASS 11425, player_ids:PASS 17355, same_pair_other_event:PASS 17355, ticker_orientation:PASS 17355

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,241 | 3.8% | 3.3% | 1.4% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 21, "market_freshness/coverage": 17} | 5.54 | 0.2267 / 0.2217 (791) | 24.6% | 2.5% | 3.1% | 2.8% |
| CHALLENGER | 11,370 | 16.3% | 6.2% | 10.7% | {"coverage": 1089, "market_freshness/coverage": 216, "market_freshness": 215, "data": 157, "model_calibration_or_unknown": 78, "execution": 41, "model_calibration": 36, "mapping": 17, "possible_market_error": 1} | 7.39 | 0.2197 / 0.2092 (2658) | 37.7% | 15.5% | 4.1% | 22.4% |
| DOUBLES | 2,503 | 46.6% | 46.5% | 6.7% | {"execution": 661, "mapping": 327, "market_freshness": 106, "market_freshness/coverage": 66, "coverage": 7} | 23.39 | 0.2987 / 0.2342 (613) | 9.3% | 0.0% | 100.0% | 6.1% |
| ITF_MEN | 22,714 | 24.8% | 17.5% | 32.5% | {"coverage": 1960, "market_freshness": 1095, "execution": 975, "data": 837, "market_freshness/coverage": 563, "mapping": 204, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.66 | 0.2158 / 0.1985 (4787) | 39.6% | 69.1% | 15.3% | 21.4% |
| ITF_WOMEN | 29,688 | 26.5% | 19.0% | 45.3% | {"coverage": 2764, "market_freshness": 1702, "execution": 1305, "data": 1112, "market_freshness/coverage": 681, "mapping": 187, "model_calibration_or_unknown": 92, "model_calibration": 22} | 12.52 | 0.2028 / 0.1932 (5716) | 40.8% | 57.2% | 9.8% | 21.6% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,756 | 6.1% | 5.1% | 1.7% | {"market_freshness": 110, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 21, "market_freshness/coverage": 13, "mapping": 1} | 7.69 | 0.2299 / 0.2206 (768) | 29.7% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.7% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1895 (764) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 523 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 638 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 17.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 1025 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 852 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 12 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 15 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 16 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 18 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 151 min (STALE); no external reference |
| 19 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 20 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 21 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 22 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 23 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 24 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 25 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 163 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 26 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 27 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 28 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 29 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 30 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 31 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 32 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 33 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 34 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 365 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 35 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 36 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 37 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 38 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 39 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 40 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 41 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 463 min (STALE); no external reference |
| 43 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 44 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 45 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 46 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 720 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 49 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 50 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.3h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 748 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9697, "by_level_share_of_ge_25pp": {"ATP": 0.0137, "CHALLENGER": 0.1066, "DOUBLES": 0.0672, "ITF_MEN": 0.3251, "ITF_WOMEN": 0.4532, "OTHER": 0.0007, "WTA": 0.0167, "WTA125": 0.0169}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5333, "share_primary_cause_market_settled_or_in_play": 0.4319, "share_primary_cause_stale_quote_only": 0.1946}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 17355, "identity_ambiguous_share": 0.2027, "ticker_orientation": {"VERIFIED": 17355}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 11425, "with_external": 607, "coverage": 0.0531, "external_status": {"EXTERNAL_STALE": 388, "AGREES_WITH_KALSHI": 206, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 388, "MODEL_LONE_OUTLIER": 206, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3394, "share_external_supports_model": 0.0214}, "pregame_clean_ge_25pp": {"n": 5400, "with_external": 577, "coverage": 0.1069, "external_status": {"EXTERNAL_STALE": 365, "AGREES_WITH_KALSHI": 199, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 365, "MODEL_LONE_OUTLIER": 199, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3449, "share_external_supports_model": 0.0225}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 489.5, "median_sample_ratio": 2.46, "median_min_matches": 19.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2087, "data_status": {"POOR": 9760, "LIMITED": 4504, "ADEQUATE": 3091}, "comparison_lt_10pp": {"median_thinner_serve_points": 1716.0, "median_sample_ratio": 1.7, "median_min_matches": 89.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1400, "model_minus_observed": 0.0571, "kalshi_minus_observed": -0.0822, "brier_diff_model_minus_kalshi": 0.0004}, "4-10x": {"n": 964, "model_minus_observed": 0.0895, "kalshi_minus_observed": -0.0554, "brier_diff_model_minus_kalshi": 0.0091}, "<2x": {"n": 3410, "model_minus_observed": 0.1006, "kalshi_minus_observed": -0.0225, "brier_diff_model_minus_kalshi": 0.0146}, ">=10x": {"n": 1179, "model_minus_observed": 0.1178, "kalshi_minus_observed": -0.0555, "brier_diff_model_minus_kalshi": 0.0148}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 6953, "model": {"intercept": -0.557, "slope": 0.828, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.188, "slope": 1.077, "slope_se": 0.034}, "mean_extremity_model": 0.1736, "mean_extremity_kalshi": 0.1699, "model_brier": 0.2327, "kalshi_brier": 0.2031, "brier_diff_model_minus_kalshi": 0.0296, "brier_diff_se": 0.0023, "model_logloss": 0.6624, "kalshi_logloss": 0.5885}, "fair_v1": {"n": 6953, "model": {"intercept": -0.449, "slope": 1.033, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.254, "slope": 1.105, "slope_se": 0.034}, "mean_extremity_model": 0.1694, "mean_extremity_kalshi": 0.1696, "model_brier": 0.2143, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.011, "brier_diff_se": 0.0018, "model_logloss": 0.6174, "kalshi_logloss": 0.5888}, "gen1_elo": {"n": 6953, "model": {"intercept": -0.437, "slope": 1.011, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.255, "slope": 1.095, "slope_se": 0.034}, "mean_extremity_model": 0.176, "mean_extremity_kalshi": 0.1696, "model_brier": 0.2135, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": 0.0102, "brier_diff_se": 0.0018, "model_logloss": 0.6162, "kalshi_logloss": 0.5889}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2472, "share_ge_15": 0.4434, "median_abs_gap": 13.03, "n": 46220}, "gen1_elo": {"share_ge_25": 0.2441, "share_ge_15": 0.4393, "median_abs_gap": 12.79, "n": 46220}, "gen1_sr": {"share_ge_25": 0.3132, "share_ge_15": 0.5203, "median_abs_gap": 15.82, "n": 46220}, "gen2": {"share_ge_25": 0.3135, "share_ge_15": 0.5097, "median_abs_gap": 15.45, "n": 46220}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1513, "share_ge_15": 0.3538, "median_abs_gap": 10.71, "n": 35682}, "gen1_elo": {"share_ge_25": 0.1491, "share_ge_15": 0.3487, "median_abs_gap": 10.49, "n": 35682}, "gen1_sr": {"share_ge_25": 0.2168, "share_ge_15": 0.4403, "median_abs_gap": 13.01, "n": 35684}, "gen2": {"share_ge_25": 0.2312, "share_ge_15": 0.439, "median_abs_gap": 12.86, "n": 35684}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.54, "share_ge_25_all": 0.038, "share_ge_25_pregame_clean": 0.0328}, "WTA": {"median_abs_gap_pregame_clean": 7.69, "share_ge_25_all": 0.0608, "share_ge_25_pregame_clean": 0.0515}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2368, "share_within_10pp_all": 0.4389, "share_within_10pp_pregame_clean": 0.4915, "corr_model_vs_mid_pregame_clean": 0.8512}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1000, "model_brier": 0.1972, "kalshi_brier": 0.1976, "brier_diff_model_minus_kalshi": -0.0003}, "10-15": {"n_settled": 1207, "model_brier": 0.2185, "kalshi_brier": 0.2089, "brier_diff_model_minus_kalshi": 0.0095}, "15-25": {"n_settled": 1545, "model_brier": 0.2245, "kalshi_brier": 0.2079, "brier_diff_model_minus_kalshi": 0.0166}, "25-40": {"n_settled": 885, "model_brier": 0.2214, "kalshi_brier": 0.2031, "brier_diff_model_minus_kalshi": 0.0183}, "3-5": {"n_settled": 640, "model_brier": 0.2046, "kalshi_brier": 0.2046, "brier_diff_model_minus_kalshi": 0.0}, "40+": {"n_settled": 185, "model_brier": 0.2959, "kalshi_brier": 0.1755, "brier_diff_model_minus_kalshi": 0.1204}, "5-10": {"n_settled": 1491, "model_brier": 0.2016, "kalshi_brier": 0.2008, "brier_diff_model_minus_kalshi": 0.0008}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.557, "slope": 0.828, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.188, "slope": 1.077, "slope_se": 0.034}, "n": 6953}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.486, "slope": 0.868, "slope_se": 0.025}, "kalshi_slope": {"intercept": 0.177, "slope": 1.077, "slope_se": 0.029}, "n": 9186}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 613, "model_brier": 0.2987, "kalshi_brier": 0.2342, "brier_diff_model_minus_kalshi": 0.0645, "brier_diff_se": 0.0119, "corr_model_outcome": 0.0915, "corr_kalshi_outcome": 0.2689}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
