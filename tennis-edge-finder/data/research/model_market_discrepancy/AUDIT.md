# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-03T08:07Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 74,561): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.4%, 15-25 19.0%, 25-40 13.7%, 40+ 8.0%; median gap 11.8 pp.
* **Where the extremes live**: 96.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.5%, Challenger 10.9%, doubles 6.8%). Main tour: ATP 3.9% and WTA 6.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 16,166): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.7%, STALE_QUOTE 19.1%, BOOK_QUALITY 18.3%, POOR_DATA 9.4%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IDENTITY_AMBIGUOUS 4.2%, LIMITED_DATA 3.5%, IN_PLAY_QUOTE 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.7%, market_freshness 19.1%, execution 18.3%, data 12.9%, market_freshness/coverage 9.0%, mapping 4.2%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.4% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.6% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 16,166 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.9% of the time and with the model 1.1%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 482.0 points vs 1750.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.033, Gen-2 0.82, Gen-1 ledger 0.865 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 789 model 0.2196 vs Kalshi 0.2069; n 163 model 0.2851 vs Kalshi 0.1859.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 321,228 model-market comparisons (523,171 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 107,035 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-03T07:56:09.368800+00:00'], shadow board 85,727 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-03T07:56:12.985668+00:00'], Model 4 40,781 rows, 25,814 settled tickers, 9,650 tickers with an external scan.
* By model: {"gen1_ledger": 72495, "gen1_elo": 43079, "fair_v1": 43079, "gen2": 43079, "gen1_sr": 43079, "model4_fundamental": 38244, "model4_conditioned": 38173}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 74,561 | 14.1 | 9.6 | 20.2 | 15.4 | 19.0 | 13.7 | 8.0 | 11.8 | 40.7% | 21.7% |
| MW fair_v1 | 43,079 | 12.9 | 8.7 | 18.8 | 15.5 | 19.5 | 14.7 | 9.8 | 12.95 | 44.1% | 24.5% |
| MW gen1_elo | 43,079 | 12.6 | 8.8 | 19.4 | 15.4 | 19.5 | 14.6 | 9.7 | 12.73 | 43.8% | 24.3% |
| MW gen1_ledger | 31,482 | 15.8 | 10.8 | 22.1 | 15.2 | 18.3 | 12.2 | 5.5 | 10.29 | 36.1% | 17.8% |
| MW gen1_sr | 43,079 | 10.2 | 7.3 | 16.9 | 13.9 | 20.6 | 18.6 | 12.5 | 15.71 | 51.7% | 31.1% |
| MW gen2 | 43,079 | 11.2 | 7.6 | 16.6 | 13.8 | 19.4 | 17.7 | 13.7 | 15.37 | 50.8% | 31.4% |
| all families model4_conditioned | 38,173 | 22.2 | 18.0 | 34.2 | 17.2 | 5.0 | 2.1 | 1.2 | 6.07 | 8.4% | 3.4% |
| all families model4_fundamental | 38,244 | 17.3 | 13.4 | 33.9 | 20.1 | 10.1 | 3.8 | 1.5 | 7.65 | 15.4% | 5.3% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.1%, >=15pp 40.7%, >=20pp 30.0%, >=25pp 21.7%, >=30pp 15.6%, >=40pp 8.0%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.28pp; >=10pp 44.7%, >=25pp 16.9%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,804 | 27.9 | 15.5 | 27.9 | 13.4 | 10.9 | 3.7 | 0.6 | 5.89 | 15.2% | 4.3% |
| CHALLENGER | 6,494 | 16.1 | 9.7 | 20.8 | 15.4 | 15.8 | 11.5 | 10.6 | 10.91 | 38.0% | 22.1% |
| ITF_MEN | 11,867 | 9.9 | 7.4 | 16.9 | 15.0 | 21.3 | 17.5 | 12.0 | 15.32 | 50.8% | 29.5% |
| ITF_WOMEN | 16,785 | 9.5 | 7.0 | 16.0 | 15.2 | 22.1 | 18.1 | 12.1 | 15.74 | 52.3% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,880 | 17.2 | 13.0 | 24.6 | 21.2 | 16.3 | 6.6 | 1.1 | 8.65 | 24.0% | 7.7% |
| WTA125 | 1,243 | 15.8 | 7.2 | 22.9 | 19.7 | 20.4 | 12.3 | 1.7 | 10.7 | 34.4% | 14.0% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,804 | 26.4 | 15.8 | 26.1 | 15.6 | 11.5 | 3.8 | 0.8 | 6.09 | 16.1% | 4.6% |
| CHALLENGER | 6,494 | 15.0 | 9.0 | 18.6 | 14.1 | 18.4 | 13.5 | 11.4 | 12.44 | 43.3% | 24.9% |
| ITF_MEN | 11,867 | 8.1 | 6.2 | 15.1 | 13.7 | 19.7 | 20.8 | 16.5 | 17.97 | 56.9% | 37.2% |
| ITF_WOMEN | 16,785 | 7.9 | 5.8 | 14.1 | 12.8 | 20.6 | 21.2 | 17.7 | 19.12 | 59.5% | 38.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,880 | 14.6 | 10.3 | 21.7 | 16.1 | 22.1 | 12.8 | 2.5 | 11.03 | 37.4% | 15.3% |
| WTA125 | 1,243 | 10.1 | 7.2 | 16.4 | 15.8 | 24.1 | 17.7 | 8.8 | 15.18 | 50.5% | 26.5% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,804 | 22.6 | 13.7 | 25.2 | 15.7 | 15.4 | 6.3 | 1.2 | 7.36 | 22.8% | 7.4% |
| CHALLENGER | 6,494 | 15.1 | 9.5 | 20.9 | 15.7 | 15.9 | 12.0 | 10.8 | 11.2 | 38.7% | 22.8% |
| ITF_MEN | 11,867 | 9.4 | 7.2 | 17.3 | 14.1 | 22.0 | 17.6 | 12.5 | 15.77 | 52.0% | 30.1% |
| ITF_WOMEN | 16,785 | 9.3 | 7.0 | 16.4 | 15.9 | 22.1 | 18.0 | 11.4 | 15.51 | 51.5% | 29.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,880 | 22.8 | 16.7 | 32.0 | 15.1 | 9.0 | 3.4 | 1.1 | 6.12 | 13.4% | 4.5% |
| WTA125 | 1,243 | 21.0 | 12.9 | 25.9 | 18.6 | 15.2 | 6.0 | 0.3 | 8.06 | 21.6% | 6.4% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,244 | 25.7 | 19.6 | 30.6 | 12.5 | 8.5 | 2.6 | 0.5 | 5.5 | 11.5% | 3.1% |
| CHALLENGER | 4,244 | 22.5 | 14.4 | 27.3 | 14.6 | 13.7 | 5.9 | 1.6 | 7.15 | 21.2% | 7.5% |
| DOUBLES | 2,309 | 5.2 | 4.3 | 12.1 | 10.5 | 20.3 | 25.3 | 22.4 | 23.85 | 68.0% | 47.6% |
| ITF_MEN | 8,854 | 13.0 | 9.4 | 21.1 | 15.8 | 21.4 | 13.2 | 6.0 | 11.91 | 40.6% | 19.2% |
| ITF_WOMEN | 10,832 | 13.3 | 9.1 | 19.9 | 15.8 | 21.1 | 15.3 | 5.5 | 12.3 | 41.9% | 20.8% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,667 | 24.2 | 16.4 | 30.5 | 17.0 | 8.9 | 2.8 | 0.2 | 6.53 | 11.9% | 3.0% |
| WTA125 | 1,183 | 24.9 | 12.9 | 21.1 | 19.4 | 13.4 | 6.8 | 1.5 | 7.85 | 21.7% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,696 | 28.4 | 15.6 | 28.3 | 13.3 | 10.7 | 3.3 | 0.3 | 5.77 | 14.3% | 3.6% |
| CHALLENGER | 4,605 | 20.7 | 12.1 | 25.6 | 18.0 | 15.9 | 6.0 | 1.7 | 8.24 | 23.6% | 7.7% |
| ITF_MEN | 8,716 | 12.1 | 8.8 | 20.4 | 17.1 | 22.1 | 14.2 | 5.4 | 12.44 | 41.7% | 19.6% |
| ITF_WOMEN | 12,498 | 11.3 | 8.4 | 18.6 | 17.4 | 24.1 | 15.1 | 5.1 | 13.29 | 44.3% | 20.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,777 | 17.5 | 13.0 | 24.9 | 21.6 | 16.3 | 6.0 | 0.7 | 8.47 | 23.0% | 6.7% |
| WTA125 | 1,201 | 16.1 | 7.1 | 22.5 | 20.0 | 20.9 | 12.0 | 1.5 | 10.7 | 34.4% | 13.5% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,696 | 26.8 | 16.1 | 26.3 | 15.5 | 11.5 | 3.4 | 0.4 | 6.02 | 15.3% | 3.8% |
| CHALLENGER | 4,605 | 18.9 | 11.3 | 23.2 | 16.6 | 18.7 | 9.4 | 1.9 | 9.04 | 30.0% | 11.3% |
| ITF_MEN | 8,717 | 9.5 | 7.3 | 17.4 | 15.9 | 21.4 | 18.9 | 9.5 | 14.97 | 49.9% | 28.4% |
| ITF_WOMEN | 12,499 | 8.8 | 6.8 | 16.0 | 14.3 | 22.7 | 20.5 | 11.0 | 16.59 | 54.2% | 31.5% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,777 | 14.8 | 10.4 | 21.9 | 16.2 | 22.2 | 12.6 | 1.8 | 10.93 | 36.7% | 14.4% |
| WTA125 | 1,201 | 10.1 | 7.3 | 16.6 | 15.8 | 24.1 | 17.8 | 8.3 | 15.02 | 50.2% | 26.1% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,187 | 25.8 | 19.8 | 30.6 | 12.7 | 8.2 | 2.5 | 0.4 | 5.46 | 11.1% | 2.9% |
| CHALLENGER | 3,742 | 23.9 | 15.3 | 28.4 | 14.8 | 13.1 | 4.1 | 0.4 | 6.61 | 17.6% | 4.5% |
| DOUBLES | 2,170 | 5.1 | 4.4 | 12.3 | 10.6 | 20.1 | 25.2 | 22.4 | 23.84 | 67.6% | 47.6% |
| ITF_MEN | 7,575 | 13.8 | 10.0 | 22.8 | 16.3 | 21.4 | 11.7 | 4.0 | 10.95 | 37.0% | 15.7% |
| ITF_WOMEN | 9,272 | 14.0 | 9.6 | 21.1 | 16.4 | 21.3 | 14.2 | 3.5 | 11.5 | 39.0% | 17.8% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,607 | 24.5 | 16.9 | 30.4 | 17.1 | 8.9 | 2.2 | 0.1 | 6.37 | 11.1% | 2.2% |
| WTA125 | 1,052 | 26.1 | 13.7 | 22.1 | 20.4 | 12.4 | 4.8 | 0.5 | 7.36 | 17.7% | 5.2% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,309 | 5.2 | 4.3 | 12.1 | 10.5 | 20.3 | 25.3 | 22.4 | 23.85 | 68.0% | 47.6% |
| singles | 29,173 | 16.6 | 11.4 | 22.9 | 15.6 | 18.1 | 11.2 | 4.2 | 9.76 | 33.5% | 15.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 52 | 5.8 | 9.6 | 23.1 | 9.6 | 19.2 | 21.1 | 11.5 | 19.99 | 51.9% | 32.7% |
| Clay | 8,502 | 13.0 | 9.3 | 19.9 | 15.9 | 19.3 | 13.6 | 8.8 | 12.36 | 41.8% | 22.5% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 28,419 | 13.4 | 8.7 | 18.8 | 15.3 | 19.2 | 14.8 | 9.9 | 12.85 | 43.8% | 24.6% |
| UNKNOWN | 5,869 | 10.6 | 7.6 | 17.0 | 16.4 | 21.4 | 16.0 | 11.1 | 14.26 | 48.4% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 12,265 | 19.9 | 11.9 | 22.6 | 16.0 | 14.8 | 8.9 | 5.9 | 8.69 | 29.6% | 14.8% |
| B | 5,348 | 12.8 | 8.8 | 19.4 | 15.9 | 19.6 | 12.6 | 10.8 | 12.61 | 43.0% | 23.4% |
| C | 6,109 | 11.8 | 8.8 | 19.5 | 16.1 | 18.4 | 14.6 | 10.7 | 12.89 | 43.7% | 25.3% |
| D | 6,820 | 11.8 | 8.4 | 17.6 | 15.4 | 21.6 | 15.8 | 9.3 | 13.78 | 46.8% | 25.1% |
| F | 12,537 | 7.4 | 5.6 | 15.0 | 14.7 | 23.5 | 20.9 | 13.0 | 17.71 | 57.4% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,480 | 24.5 | 16.1 | 29.1 | 15.0 | 10.7 | 3.5 | 1.2 | 6.37 | 15.3% | 4.7% |
| B | 4,460 | 16.7 | 10.7 | 23.9 | 17.0 | 18.9 | 9.7 | 3.1 | 9.72 | 31.7% | 12.8% |
| C | 6,180 | 11.4 | 7.7 | 19.2 | 14.5 | 20.9 | 15.9 | 10.4 | 13.69 | 47.2% | 26.3% |
| D | 4,629 | 14.3 | 9.7 | 21.5 | 15.6 | 20.1 | 13.3 | 5.4 | 11.29 | 38.8% | 18.7% |
| F | 7,733 | 10.1 | 8.3 | 16.1 | 14.7 | 23.1 | 19.8 | 7.8 | 15.4 | 50.7% | 27.6% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 13,893 | 18.1 | 10.9 | 21.8 | 15.8 | 15.2 | 9.7 | 8.6 | 9.78 | 33.4% | 18.3% |
| LIMITED | 9,440 | 13.6 | 9.9 | 20.2 | 16.3 | 19.2 | 13.3 | 7.6 | 11.82 | 40.1% | 20.9% |
| POOR | 19,746 | 9.0 | 6.6 | 16.0 | 15.0 | 22.7 | 19.0 | 11.7 | 16.14 | 53.4% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,448 | 23.9 | 17.7 | 33.1 | 15.8 | 6.4 | 2.7 | 0.4 | 5.92 | 9.5% | 3.1% |
| GAME_SPREAD | 6,378 | 22.2 | 15.1 | 32.6 | 17.0 | 9.1 | 3.4 | 0.6 | 6.76 | 13.1% | 4.0% |
| MATCH_WINNER | 31,482 | 15.8 | 10.8 | 22.1 | 15.2 | 18.3 | 12.2 | 5.5 | 10.29 | 36.1% | 17.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 15,532 | 27.8 | 16.7 | 30.6 | 12.8 | 9.4 | 2.5 | 0.3 | 5.65 | 12.2% | 2.8% |
| TOTAL_GAMES | 10,631 | 9.9 | 10.8 | 35.3 | 26.3 | 10.6 | 4.2 | 3.0 | 9.25 | 17.8% | 7.2% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,583 | 24.5 | 28.9 | 33.3 | 8.2 | 4.0 | 0.9 | 0.3 | 4.79 | 5.2% | 1.2% |
| GAME_SPREAD | 8,823 | 46.7 | 16.2 | 24.9 | 7.5 | 2.2 | 1.9 | 0.6 | 3.31 | 4.7% | 2.5% |
| TOTAL_GAMES | 15,767 | 6.5 | 9.7 | 40.1 | 30.4 | 7.5 | 3.3 | 2.4 | 9.25 | 13.2% | 5.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,611 | 23.9 | 16.6 | 34.8 | 14.8 | 6.9 | 2.5 | 0.5 | 6.06 | 9.9% | 3.0% |
| GAME_SPREAD | 8,828 | 20.2 | 13.6 | 28.2 | 20.2 | 12.1 | 4.5 | 1.2 | 7.71 | 17.8% | 5.7% |
| TOTAL_GAMES | 15,805 | 9.9 | 10.6 | 36.1 | 24.6 | 11.6 | 4.4 | 2.7 | 9.13 | 18.7% | 7.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 43,079 | 44.1% | 24.5% | 12.95 | 35.4% | 15.1% | 10.7 |
| gen1_elo | 43,079 | 43.8% | 24.3% | 12.73 | 35.0% | 15.1% | 10.49 |
| gen1_sr | 43,079 | 51.7% | 31.1% | 15.71 | 43.8% | 21.7% | 12.95 |
| gen2 | 43,079 | 50.8% | 31.4% | 15.37 | 43.9% | 23.2% | 12.83 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 19,548 | 15.6 | 10.4 | 21.4 | 17.4 | 20.1 | 11.8 | 3.4 | 10.71 | 35.3% | 15.2% |
| STALE | 23,531 | 10.8 | 7.2 | 16.6 | 14.0 | 19.1 | 17.1 | 15.2 | 15.54 | 51.3% | 32.3% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 24,950 | 16.5 | 11.2 | 22.8 | 15.3 | 17.7 | 11.7 | 4.8 | 9.88 | 34.3% | 16.6% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 74,561 | 24950 | 23020 | 26591 | 24.5 | 119.0 | 1451.1 |
| ge_15pp | 30,332 | 8554 | 8187 | 13591 | 27.6 | 431.0 | 1451.1 |
| ge_25pp | 16,166 | 4133 | 3566 | 8467 | 31.9 | 584.1 | 1431.1 |
| lt_10pp | 32,755 | 12578 | 10891 | 9286 | 22.6 | 47.1 | 1421.1 |

Current slate `SL-20261103T080733Z-9ad00357`: 667 priced rows, quote age at build {'median': 11.6, 'max': 11.7}, freshness {'AGING': 667}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 49 | 0.0 | 0.0 | 36.7 | 6.1 | 32.6 | 20.4 | 4.1 | 18.34 | 57.1% | 24.5% |
| EXTERNAL_LONE_OUTLIER | 26 | 65.4 | 34.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.37 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,221 | 19.5 | 10.8 | 25.4 | 18.1 | 18.0 | 7.3 | 0.9 | 8.71 | 26.2% | 8.2% |
| KALSHI_LONE_OUTLIER | 27 | 3.7 | 3.7 | 77.8 | 7.4 | 3.7 | 3.7 | 0.0 | 6.42 | 7.4% | 3.7% |
| MARKETS_AGREE | 872 | 66.4 | 33.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.2 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,913 | 0.0 | 2.4 | 37.0 | 26.4 | 24.1 | 9.4 | 0.8 | 11.85 | 34.3% | 10.2% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 43,079 | 7108 (16.5%) | 26.9% | 1.1% | {"EXTERNAL_STALE": 4221, "AGREES_WITH_KALSHI": 1913, "ALL_AGREE": 872, "SUPPORTS_MODEL_DIRECTION": 48, "AGREES_WITH_MODEL": 27, "EXTERNAL_OUTLIER": 26, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 18,979 | 1792 (9.4%) | 36.7% | 1.7% | {"EXTERNAL_STALE": 1105, "AGREES_WITH_KALSHI": 657, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 10,571 | 556 (5.3%) | 35.2% | 2.3% | {"EXTERNAL_STALE": 347, "AGREES_WITH_KALSHI": 196, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,071 | 528 (10.4%) | 35.8% | 2.5% | {"EXTERNAL_STALE": 326, "AGREES_WITH_KALSHI": 189, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 17,408 | 4043 (23.2%) | 18.6% | 1.0% | {"EXTERNAL_STALE": 2352, "ALL_AGREE": 872, "AGREES_WITH_KALSHI": 752, "EXTERNAL_OUTLIER": 26, "AGREES_WITH_MODEL": 23, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 8,341 | 10.4 | 7.5 | 19.4 | 14.7 | 21.7 | 16.3 | 9.9 | 14.09 | 47.9% | 26.2% |
| 4-10x | 5,764 | 11.1 | 8.6 | 18.5 | 15.3 | 22.1 | 14.2 | 10.1 | 13.75 | 46.5% | 24.3% |
| <2x | 22,131 | 15.1 | 9.9 | 19.8 | 16.2 | 17.3 | 12.9 | 8.7 | 11.47 | 39.0% | 21.7% |
| >=10x | 6,843 | 10.4 | 6.4 | 15.0 | 14.5 | 21.7 | 19.1 | 12.9 | 16.35 | 53.7% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 11,219 | 12.6 | 8.7 | 19.7 | 16.4 | 19.1 | 13.3 | 10.2 | 12.68 | 42.7% | 23.5% |
| 300-1000 | 9,247 | 11.9 | 8.8 | 17.7 | 15.4 | 20.4 | 16.3 | 9.5 | 13.58 | 46.2% | 25.8% |
| <300 | 13,591 | 8.3 | 5.8 | 15.2 | 14.7 | 23.2 | 19.9 | 12.9 | 17.1 | 56.1% | 32.9% |
| >=3000 | 9,022 | 21.5 | 12.9 | 24.2 | 15.8 | 13.6 | 7.0 | 4.9 | 7.64 | 25.6% | 11.9% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1231 | 0.5505 | 0.4108 | 0.4939 | +0.057 | -0.083 | -0.0021 ± 0.0044 |
| ratio 4-10x | 852 | 0.5822 | 0.4352 | 0.4941 | +0.088 | -0.059 | 0.0085 ± 0.0055 |
| ratio <2x | 3050 | 0.5375 | 0.4156 | 0.443 | +0.095 | -0.027 | 0.0127 ± 0.0026 |
| ratio >=10x | 1046 | 0.5695 | 0.3954 | 0.4512 | +0.118 | -0.056 | 0.0139 ± 0.0056 |
| thinner_sample 1000-3000 | 1709 | 0.5393 | 0.4129 | 0.4523 | +0.087 | -0.039 | 0.009 ± 0.0035 |
| thinner_sample 300-1000 | 1397 | 0.5685 | 0.4268 | 0.4839 | +0.085 | -0.057 | 0.0031 ± 0.0042 |
| thinner_sample <300 | 2018 | 0.5613 | 0.3931 | 0.4599 | +0.101 | -0.067 | 0.0111 ± 0.004 |
| thinner_sample >=3000 | 1055 | 0.531 | 0.4384 | 0.4502 | +0.081 | -0.012 | 0.0152 ± 0.0035 |
| data_status ADEQUATE | 1714 | 0.5331 | 0.4312 | 0.4428 | +0.090 | -0.012 | 0.0138 ± 0.0029 |
| data_status LIMITED | 1521 | 0.549 | 0.4162 | 0.4707 | +0.078 | -0.054 | 0.0069 ± 0.0038 |
| data_status POOR | 2944 | 0.5639 | 0.4027 | 0.4677 | +0.096 | -0.065 | 0.0081 ± 0.0032 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 906 | 0.1998 | 0.2002 | -0.0004 ± 0.0005 | 0.5801 | 0.5812 | 0.5032 | 0.4881 | 0.5044 | -0.091 ± 0.0157 | -0.0087 (8) |
| 3-5 | 564 | 0.2066 | 0.2059 | +0.0007 ± 0.0015 | 0.5966 | 0.5931 | 0.5039 | 0.464 | 0.4752 | -0.107 ± 0.0196 | 0.01 (2) |
| 5-10 | 1316 | 0.2008 | 0.2006 | +0.0002 ± 0.0019 | 0.5874 | 0.5846 | 0.5119 | 0.4382 | 0.4711 | -0.090 ± 0.0128 | -0.0143 (7) |
| 10-15 | 1070 | 0.2193 | 0.21 | +0.0093 ± 0.0035 | 0.6308 | 0.6045 | 0.5287 | 0.4052 | 0.428 | -0.109 ± 0.0141 | -0.048 (5) |
| 15-25 | 1371 | 0.2251 | 0.2094 | +0.0157 ± 0.0048 | 0.6455 | 0.6024 | 0.5765 | 0.3812 | 0.4391 | -0.104 ± 0.0124 | -0.004 (10) |
| 25-40 | 789 | 0.2196 | 0.2069 | +0.0127 ± 0.0096 | 0.6279 | 0.5956 | 0.657 | 0.347 | 0.4816 | -0.069 ± 0.0147 | -0.06 (2) |
| 40+ | 163 | 0.2851 | 0.1859 | +0.0992 ± 0.0297 | 0.7744 | 0.5494 | 0.7395 | 0.2893 | 0.411 | -0.076 ± 0.0291 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4857 | 0.1851 | 0.1859 | -0.0008 ± 0.0002 | 0.5457 | 0.5465 | 0.4877 | 0.4724 | 0.5009 | -0.024 ± 0.0063 | -0.01 (28) |
| 3-5 | 3252 | 0.1949 | 0.1928 | +0.0022 ± 0.0006 | 0.5685 | 0.561 | 0.4825 | 0.4427 | 0.4345 | -0.063 ± 0.0078 | 0.0 (3) |
| 5-10 | 7004 | 0.2007 | 0.1973 | +0.0035 ± 0.0008 | 0.5869 | 0.5753 | 0.4848 | 0.4112 | 0.4248 | -0.046 ± 0.0054 | -0.0114 (22) |
| 10-15 | 5763 | 0.2013 | 0.1854 | +0.0159 ± 0.0014 | 0.5887 | 0.545 | 0.4849 | 0.361 | 0.3581 | -0.065 ± 0.0057 | -0.0281 (16) |
| 15-25 | 7229 | 0.2068 | 0.1678 | +0.0390 ± 0.0019 | 0.606 | 0.4981 | 0.5 | 0.3043 | 0.3036 | -0.070 ± 0.0048 | -0.0027 (45) |
| 25-40 | 5634 | 0.2209 | 0.1256 | +0.0953 ± 0.003 | 0.6357 | 0.3861 | 0.5262 | 0.2122 | 0.2217 | -0.058 ± 0.0046 | -0.0733 (3) |
| 40+ | 3723 | 0.3835 | 0.0449 | +0.3386 ± 0.004 | 0.9991 | 0.1735 | 0.6328 | 0.1042 | 0.0604 | -0.077 ± 0.0033 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 724 | 0.2075 | 0.2081 | -0.0006 ± 0.0006 | 0.5973 | 0.599 | 0.5059 | 0.4911 | 0.5235 | -0.097 ± 0.0183 | -0.0117 (6) |
| 3-5 | 511 | 0.2152 | 0.2124 | +0.0028 ± 0.0016 | 0.6129 | 0.6075 | 0.5146 | 0.4749 | 0.456 | -0.131 ± 0.0219 | 0.01 (2) |
| 5-10 | 1139 | 0.2068 | 0.2043 | +0.0025 ± 0.002 | 0.6002 | 0.593 | 0.5429 | 0.4682 | 0.4917 | -0.098 ± 0.0138 | -0.01 (4) |
| 10-15 | 991 | 0.2149 | 0.2096 | +0.0053 ± 0.0036 | 0.6208 | 0.6061 | 0.5663 | 0.442 | 0.4864 | -0.100 ± 0.0152 | -0.04 (5) |
| 15-25 | 1437 | 0.2298 | 0.2121 | +0.0176 ± 0.0048 | 0.6539 | 0.6085 | 0.5834 | 0.3881 | 0.4433 | -0.099 ± 0.0124 | -0.012 (10) |
| 25-40 | 1010 | 0.2684 | 0.1984 | +0.0700 ± 0.0088 | 0.7489 | 0.5773 | 0.6609 | 0.3471 | 0.395 | -0.128 ± 0.014 | -0.008 (5) |
| 40+ | 367 | 0.3639 | 0.1656 | +0.1984 ± 0.0211 | 0.9947 | 0.4985 | 0.7326 | 0.2475 | 0.2997 | -0.082 ± 0.0204 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4176 | 0.1914 | 0.1916 | -0.0002 ± 0.0002 | 0.5585 | 0.5588 | 0.5077 | 0.4927 | 0.5098 | -0.039 ± 0.007 | -0.0154 (26) |
| 3-5 | 2869 | 0.1935 | 0.1923 | +0.0012 ± 0.0007 | 0.5632 | 0.5596 | 0.5108 | 0.471 | 0.4747 | -0.048 ± 0.0084 | 0.01 (2) |
| 5-10 | 6220 | 0.1979 | 0.1942 | +0.0037 ± 0.0008 | 0.5809 | 0.5676 | 0.5092 | 0.4352 | 0.4497 | -0.044 ± 0.0057 | -0.0117 (6) |
| 10-15 | 5168 | 0.2031 | 0.1916 | +0.0115 ± 0.0015 | 0.5953 | 0.5607 | 0.5129 | 0.3891 | 0.4056 | -0.050 ± 0.0062 | -0.0189 (18) |
| 15-25 | 7234 | 0.2169 | 0.1806 | +0.0363 ± 0.002 | 0.6309 | 0.5301 | 0.5227 | 0.3274 | 0.3352 | -0.062 ± 0.005 | -0.0084 (43) |
| 25-40 | 6609 | 0.2507 | 0.1365 | +0.1141 ± 0.0029 | 0.7077 | 0.4178 | 0.5583 | 0.2415 | 0.2233 | -0.083 ± 0.0045 | -0.0095 (20) |
| 40+ | 5186 | 0.4001 | 0.059 | +0.3411 ± 0.0039 | 1.0553 | 0.2125 | 0.6538 | 0.1186 | 0.0814 | -0.073 ± 0.0033 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 860 | 0.1964 | 0.1982 | -0.0018 ± 0.0005 | 0.572 | 0.5766 | 0.5024 | 0.487 | 0.5395 | -0.044 ± 0.0159 | -0.012 (10) |
| 3-5 | 606 | 0.2068 | 0.2048 | +0.0020 ± 0.0015 | 0.5986 | 0.5918 | 0.4979 | 0.4582 | 0.4554 | -0.121 ± 0.0191 | -0.0 (4) |
| 5-10 | 1359 | 0.2026 | 0.1998 | +0.0028 ± 0.0018 | 0.5904 | 0.5818 | 0.5112 | 0.4374 | 0.454 | -0.102 ± 0.0125 | -0.01 (9) |
| 10-15 | 1076 | 0.2089 | 0.2023 | +0.0066 ± 0.0034 | 0.6075 | 0.5875 | 0.5419 | 0.4186 | 0.4545 | -0.102 ± 0.0137 | -0.0286 (7) |
| 15-25 | 1302 | 0.2337 | 0.2153 | +0.0184 ± 0.005 | 0.6659 | 0.6152 | 0.5896 | 0.3952 | 0.4447 | -0.114 ± 0.0129 | -0.03 (1) |
| 25-40 | 804 | 0.2101 | 0.2119 | -0.0017 ± 0.0095 | 0.6075 | 0.6075 | 0.6646 | 0.3539 | 0.51 | -0.056 ± 0.0145 | -0.0267 (3) |
| 40+ | 172 | 0.3025 | 0.1935 | +0.1090 ± 0.0297 | 0.8227 | 0.5669 | 0.7504 | 0.2988 | 0.4128 | -0.082 ± 0.0308 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4635 | 0.1841 | 0.1847 | -0.0006 ± 0.0002 | 0.5423 | 0.5433 | 0.4831 | 0.4678 | 0.4874 | -0.031 ± 0.0064 | -0.0137 (41) |
| 3-5 | 3276 | 0.2007 | 0.1985 | +0.0022 ± 0.0006 | 0.5845 | 0.5771 | 0.4804 | 0.4409 | 0.4335 | -0.063 ± 0.0079 | -0.01 (19) |
| 5-10 | 7145 | 0.194 | 0.1896 | +0.0045 ± 0.0008 | 0.5708 | 0.5562 | 0.4868 | 0.4128 | 0.4197 | -0.051 ± 0.0052 | -0.0105 (37) |
| 10-15 | 5730 | 0.1924 | 0.1787 | +0.0137 ± 0.0014 | 0.569 | 0.5292 | 0.4957 | 0.3724 | 0.3778 | -0.058 ± 0.0056 | -0.0146 (13) |
| 15-25 | 7352 | 0.2133 | 0.1735 | +0.0398 ± 0.0019 | 0.6209 | 0.5108 | 0.5142 | 0.3196 | 0.316 | -0.073 ± 0.0048 | -0.0533 (3) |
| 25-40 | 5646 | 0.216 | 0.1281 | +0.0879 ± 0.003 | 0.6249 | 0.3919 | 0.5296 | 0.214 | 0.2347 | -0.048 ± 0.0046 | -0.02 (4) |
| 40+ | 3678 | 0.3934 | 0.0505 | +0.3430 ± 0.0042 | 1.0258 | 0.1877 | 0.6425 | 0.1109 | 0.0674 | -0.078 ± 0.0035 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1283 | 0.1949 | 0.1949 | -0.0000 ± 0.0004 | 0.5677 | 0.5676 | 0.506 | 0.491 | 0.4942 | -0.070 ± 0.0126 | -0.0213 (54) |
| 3-5 | 898 | 0.1888 | 0.1885 | +0.0003 ± 0.0012 | 0.5539 | 0.5521 | 0.4968 | 0.4569 | 0.4722 | -0.061 ± 0.0148 | -0.0194 (34) |
| 5-10 | 1863 | 0.2012 | 0.1967 | +0.0045 ± 0.0015 | 0.5912 | 0.5766 | 0.5055 | 0.4317 | 0.4385 | -0.075 ± 0.0105 | -0.005 (78) |
| 10-15 | 1283 | 0.217 | 0.2037 | +0.0133 ± 0.0031 | 0.6266 | 0.5912 | 0.5395 | 0.4167 | 0.4224 | -0.092 ± 0.013 | 0.0014 (65) |
| 15-25 | 1650 | 0.2303 | 0.2082 | +0.0221 ± 0.0044 | 0.6568 | 0.6007 | 0.5866 | 0.3917 | 0.4358 | -0.087 ± 0.0114 | -0.0214 (59) |
| 25-40 | 1025 | 0.2412 | 0.2112 | +0.0300 ± 0.0088 | 0.6897 | 0.6054 | 0.6885 | 0.3761 | 0.4839 | -0.091 ± 0.0134 | -0.0252 (27) |
| 40+ | 354 | 0.326 | 0.2043 | +0.1217 ± 0.023 | 0.946 | 0.5939 | 0.8218 | 0.3451 | 0.4718 | -0.098 ± 0.0214 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4813 | 0.175 | 0.1753 | -0.0002 ± 0.0002 | 0.519 | 0.5191 | 0.5116 | 0.4964 | 0.5088 | -0.037 ± 0.0061 | -0.0145 (98) |
| 3-5 | 3303 | 0.1943 | 0.1932 | +0.0011 ± 0.0006 | 0.5663 | 0.5637 | 0.5021 | 0.4624 | 0.4684 | -0.045 ± 0.0077 | -0.0204 (72) |
| 5-10 | 6735 | 0.1977 | 0.1912 | +0.0065 ± 0.0008 | 0.5814 | 0.5625 | 0.5009 | 0.4273 | 0.4217 | -0.062 ± 0.0054 | -0.0084 (134) |
| 10-15 | 4659 | 0.211 | 0.1951 | +0.0159 ± 0.0016 | 0.6126 | 0.5715 | 0.5378 | 0.4149 | 0.4104 | -0.070 ± 0.0065 | -0.0053 (106) |
| 15-25 | 5602 | 0.2301 | 0.2001 | +0.0300 ± 0.0024 | 0.6614 | 0.5794 | 0.5732 | 0.3777 | 0.4002 | -0.065 ± 0.006 | -0.026 (108) |
| 25-40 | 3757 | 0.2585 | 0.1893 | +0.0693 ± 0.0045 | 0.7317 | 0.5516 | 0.6385 | 0.3259 | 0.3737 | -0.072 ± 0.0069 | -0.0246 (52) |
| 40+ | 1622 | 0.3726 | 0.1573 | +0.2153 ± 0.0102 | 1.0551 | 0.4683 | 0.7452 | 0.2433 | 0.2904 | -0.069 ± 0.0093 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 6179 | 1.033 ± 0.036 | 1.103 | 0.1693 | 0.166 | 0.2144 | 0.205 |
| gen2 | 6179 | 0.82 ± 0.032 | 1.073 | 0.1718 | 0.1664 | 0.2336 | 0.2048 |
| gen1_elo | 6179 | 1.009 ± 0.034 | 1.096 | 0.1761 | 0.1661 | 0.2136 | 0.2051 |
| gen1_sr | 6179 | 1.007 ± 0.042 | 1.132 | 0.1321 | 0.1682 | 0.2297 | 0.2045 |
| gen1_ledger | 8356 | 0.865 ± 0.026 | 1.073 | 0.1887 | 0.1747 | 0.2173 | 0.201 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 30,332)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 6,845 | 22.6% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,741 | 22.2% |
| BOOK_QUALITY | execution | 5,694 | 18.8% |
| POOR_DATA | data | 3,534 | 11.7% |
| LIMITED_DATA | data | 1,900 | 6.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,704 | 5.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,292 | 4.3% |
| IDENTITY_AMBIGUOUS | mapping | 1,249 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 854 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 518 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 22.6%, coverage 22.2%, execution 18.8%, data 17.9%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.3%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.4%, START_UNVERIFIABLE 94.3%, LOW_DATA_QUALITY 71.5%, THIN_PLAYER_HISTORY 59.9%, STALE_PLAYER_DATA 51.9%, STALE_KALSHI_QUOTE 44.8%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 25.0%, MODEL_HIGH_UNCERTAINTY 18.5%, PLAYER_IDENTITY_RISK 15.6%, LEVEL_TRANSFER_RISK 10.2%, LOW_DISPLAYED_LIQUIDITY 8.2%, EVENT_MAPPING_RISK 7.4%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 3.4%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.6%, POST_SETTLEMENT_OBSERVATION 22.2%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 16,166)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,443 | 33.7% |
| STALE_QUOTE | market_freshness | 3,088 | 19.1% |
| BOOK_QUALITY | execution | 2,963 | 18.3% |
| POOR_DATA | data | 1,526 | 9.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 896 | 5.5% |
| IDENTITY_AMBIGUOUS | mapping | 687 | 4.2% |
| LIMITED_DATA | data | 560 | 3.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 556 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 318 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 128 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.7%, market_freshness 19.1%, execution 18.3%, data 12.9%, market_freshness/coverage 9.0%, mapping 4.2%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.9%, LOW_DATA_QUALITY 75.1%, THIN_PLAYER_HISTORY 62.1%, STALE_KALSHI_QUOTE 52.4%, STALE_PLAYER_DATA 46.0%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 34.2%, WIDE_SPREAD 24.4%, MODEL_HIGH_UNCERTAINTY 19.1%, PLAYER_IDENTITY_RISK 18.5%, EVENT_MAPPING_RISK 9.1%, LEVEL_TRANSFER_RISK 9.1%, LOW_DISPLAYED_LIQUIDITY 8.1%, MODEL_CALIBRATION_OUTLIER 5.0%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.6%, POST_SETTLEMENT_OBSERVATION 33.7%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 12847, "IDENTITY_AMBIGUOUS": 3319}; ticker orientation: {"VERIFIED": 16166}.

Checks: discipline:AMBIGUOUS 1100, discipline:PASS 15066, identity_confidence:AMBIGUOUS 2995, identity_confidence:PASS 13171, level_mapping:NA 1112, level_mapping:PASS 15054, market_pair:AMBIGUOUS 484, market_pair:NA 359, market_pair:PASS 15323, model_complement:NA 322, model_complement:PASS 15844, namesake:AMBIGUOUS 6, namesake:PASS 16160, physical_match_id:NA 5595, physical_match_id:PASS 10571, player_ids:PASS 16166, same_pair_other_event:PASS 16166, ticker_orientation:PASS 16166

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,048 | 3.9% | 3.4% | 1.5% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "coverage": 19, "market_freshness/coverage": 17} | 5.64 | 0.2214 / 0.2154 (729) | 23.8% | 2.6% | 3.1% | 2.7% |
| CHALLENGER | 10,738 | 16.3% | 6.3% | 10.9% | {"coverage": 1022, "market_freshness/coverage": 207, "market_freshness": 201, "data": 154, "model_calibration_or_unknown": 77, "execution": 41, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.39 | 0.2212 / 0.2102 (2478) | 36.4% | 16.0% | 4.2% | 22.3% |
| DOUBLES | 2,309 | 47.6% | 47.6% | 6.8% | {"execution": 629, "mapping": 297, "market_freshness": 106, "market_freshness/coverage": 61, "coverage": 7} | 23.84 | 0.3059 / 0.2388 (547) | 10.1% | 0.0% | 100.0% | 6.0% |
| ITF_MEN | 20,721 | 25.1% | 17.8% | 32.2% | {"coverage": 1811, "market_freshness": 974, "execution": 945, "data": 774, "market_freshness/coverage": 497, "mapping": 192, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.76 | 0.2172 / 0.2002 (4226) | 38.3% | 69.1% | 16.2% | 21.4% |
| ITF_WOMEN | 27,617 | 26.5% | 19.2% | 45.3% | {"coverage": 2532, "market_freshness": 1567, "execution": 1266, "data": 1060, "market_freshness/coverage": 615, "mapping": 175, "model_calibration_or_unknown": 83, "model_calibration": 22} | 12.56 | 0.2019 / 0.1946 (5112) | 40.0% | 57.3% | 9.8% | 21.2% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,547 | 6.0% | 5.1% | 1.7% | {"market_freshness": 98, "model_calibration_or_unknown": 50, "coverage": 37, "execution": 29, "data": 24, "model_calibration": 20, "market_freshness/coverage": 13, "mapping": 1} | 7.68 | 0.2297 / 0.2229 (691) | 28.8% | 2.0% | 1.4% | 3.6% |
| WTA125 | 2,426 | 11.2% | 9.6% | 1.7% | {"market_freshness": 83, "model_calibration_or_unknown": 51, "market_freshness/coverage": 41, "data": 38, "execution": 24, "model_calibration": 17, "coverage": 14, "mapping": 4} | 9.26 | 0.2098 / 0.1927 (710) | 27.7% | 11.0% | 4.5% | 7.1% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 16.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 969 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 3 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 4 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 5 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 311 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 6 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 773 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 7 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 8 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 20.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 1252 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 9 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 10 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 20.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 1203 min (STALE); no external reference |
| 13 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 14 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 207 min (STALE); no external reference |
| 17 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 18 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 19 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 20 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 21 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 22 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 23 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 24 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 25 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 26 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 27 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 28 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 29 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 30 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 31 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 32 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 33 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 34 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 35 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 36 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 37 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 38 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 39 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 463 min (STALE); no external reference |
| 40 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 41 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 42 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 43 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 44 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 77 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 45 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 46 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.3h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 748 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |
| 47 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXATPCHALLENGERMATCH-26NOV02TOBSTO-TOB` | CHALLENGER | fair_v1 | 80% / 2% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 165 min (STALE); data POOR (grade F, thinner serve sample 159.0, ratio 20.58); no external reference |
| 49 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 50 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9686, "by_level_share_of_ge_25pp": {"ATP": 0.0145, "CHALLENGER": 0.1086, "DOUBLES": 0.068, "ITF_MEN": 0.3217, "ITF_WOMEN": 0.4528, "OTHER": 0.0007, "WTA": 0.0168, "WTA125": 0.0168}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5238, "share_primary_cause_market_settled_or_in_play": 0.4265, "share_primary_cause_stale_quote_only": 0.191}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 16166, "identity_ambiguous_share": 0.2053, "ticker_orientation": {"VERIFIED": 16166}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 10571, "with_external": 556, "coverage": 0.0526, "external_status": {"EXTERNAL_STALE": 347, "AGREES_WITH_KALSHI": 196, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 347, "MODEL_LONE_OUTLIER": 196, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3525, "share_external_supports_model": 0.0234}, "pregame_clean_ge_25pp": {"n": 5071, "with_external": 528, "coverage": 0.1041, "external_status": {"EXTERNAL_STALE": 326, "AGREES_WITH_KALSHI": 189, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 326, "MODEL_LONE_OUTLIER": 189, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.358, "share_external_supports_model": 0.0246}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 482.0, "median_sample_ratio": 2.47, "median_min_matches": 19.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2073, "data_status": {"POOR": 9101, "LIMITED": 4223, "ADEQUATE": 2842}, "comparison_lt_10pp": {"median_thinner_serve_points": 1750.0, "median_sample_ratio": 1.69, "median_min_matches": 91.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1231, "model_minus_observed": 0.0566, "kalshi_minus_observed": -0.0831, "brier_diff_model_minus_kalshi": -0.0021}, "4-10x": {"n": 852, "model_minus_observed": 0.0881, "kalshi_minus_observed": -0.059, "brier_diff_model_minus_kalshi": 0.0085}, "<2x": {"n": 3050, "model_minus_observed": 0.0945, "kalshi_minus_observed": -0.0274, "brier_diff_model_minus_kalshi": 0.0127}, ">=10x": {"n": 1046, "model_minus_observed": 0.1183, "kalshi_minus_observed": -0.0558, "brier_diff_model_minus_kalshi": 0.0139}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 6179, "model": {"intercept": -0.542, "slope": 0.82, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.191, "slope": 1.073, "slope_se": 0.036}, "mean_extremity_model": 0.1718, "mean_extremity_kalshi": 0.1664, "model_brier": 0.2336, "kalshi_brier": 0.2048, "brier_diff_model_minus_kalshi": 0.0288, "brier_diff_se": 0.0024, "model_logloss": 0.6645, "kalshi_logloss": 0.5924}, "fair_v1": {"n": 6179, "model": {"intercept": -0.435, "slope": 1.033, "slope_se": 0.036}, "kalshi_mid_same_rows": {"intercept": 0.264, "slope": 1.103, "slope_se": 0.037}, "mean_extremity_model": 0.1693, "mean_extremity_kalshi": 0.166, "model_brier": 0.2144, "kalshi_brier": 0.205, "brier_diff_model_minus_kalshi": 0.0094, "brier_diff_se": 0.002, "model_logloss": 0.6177, "kalshi_logloss": 0.5927}, "gen1_elo": {"n": 6179, "model": {"intercept": -0.419, "slope": 1.009, "slope_se": 0.034}, "kalshi_mid_same_rows": {"intercept": 0.275, "slope": 1.096, "slope_se": 0.036}, "mean_extremity_model": 0.1761, "mean_extremity_kalshi": 0.1661, "model_brier": 0.2136, "kalshi_brier": 0.2051, "brier_diff_model_minus_kalshi": 0.0084, "brier_diff_se": 0.002, "model_logloss": 0.6162, "kalshi_logloss": 0.593}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2454, "share_ge_15": 0.4406, "median_abs_gap": 12.95, "n": 43079}, "gen1_elo": {"share_ge_25": 0.2432, "share_ge_15": 0.4378, "median_abs_gap": 12.73, "n": 43079}, "gen1_sr": {"share_ge_25": 0.3113, "share_ge_15": 0.5174, "median_abs_gap": 15.71, "n": 43079}, "gen2": {"share_ge_25": 0.3137, "share_ge_15": 0.5077, "median_abs_gap": 15.37, "n": 43079}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1514, "share_ge_15": 0.3536, "median_abs_gap": 10.7, "n": 33499}, "gen1_elo": {"share_ge_25": 0.1506, "share_ge_15": 0.3496, "median_abs_gap": 10.49, "n": 33498}, "gen1_sr": {"share_ge_25": 0.2169, "share_ge_15": 0.4384, "median_abs_gap": 12.95, "n": 33501}, "gen2": {"share_ge_25": 0.2325, "share_ge_15": 0.4386, "median_abs_gap": 12.83, "n": 33501}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.64, "share_ge_25_all": 0.0387, "share_ge_25_pregame_clean": 0.0337}, "WTA": {"median_abs_gap_pregame_clean": 7.68, "share_ge_25_all": 0.0598, "share_ge_25_pregame_clean": 0.0506}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2374, "share_within_10pp_all": 0.4393, "share_within_10pp_pregame_clean": 0.491, "corr_model_vs_mid_pregame_clean": 0.8496}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 906, "model_brier": 0.1998, "kalshi_brier": 0.2002, "brier_diff_model_minus_kalshi": -0.0004}, "10-15": {"n_settled": 1070, "model_brier": 0.2193, "kalshi_brier": 0.21, "brier_diff_model_minus_kalshi": 0.0093}, "15-25": {"n_settled": 1371, "model_brier": 0.2251, "kalshi_brier": 0.2094, "brier_diff_model_minus_kalshi": 0.0157}, "25-40": {"n_settled": 789, "model_brier": 0.2196, "kalshi_brier": 0.2069, "brier_diff_model_minus_kalshi": 0.0127}, "3-5": {"n_settled": 564, "model_brier": 0.2066, "kalshi_brier": 0.2059, "brier_diff_model_minus_kalshi": 0.0007}, "40+": {"n_settled": 163, "model_brier": 0.2851, "kalshi_brier": 0.1859, "brier_diff_model_minus_kalshi": 0.0992}, "5-10": {"n_settled": 1316, "model_brier": 0.2008, "kalshi_brier": 0.2006, "brier_diff_model_minus_kalshi": 0.0002}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.542, "slope": 0.82, "slope_se": 0.032}, "kalshi_slope": {"intercept": 0.191, "slope": 1.073, "slope_se": 0.036}, "n": 6179}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.487, "slope": 0.865, "slope_se": 0.026}, "kalshi_slope": {"intercept": 0.174, "slope": 1.073, "slope_se": 0.03}, "n": 8356}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 547, "model_brier": 0.3059, "kalshi_brier": 0.2388, "brier_diff_model_minus_kalshi": 0.0671, "brier_diff_se": 0.0129, "corr_model_outcome": 0.0635, "corr_kalshi_outcome": 0.2298}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
