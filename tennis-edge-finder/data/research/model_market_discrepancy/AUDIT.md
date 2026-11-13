# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-13T14:14Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 91,920): 0-3 13.9%, 3-5 9.5%, 5-10 20.1%, 10-15 15.2%, 15-25 19.2%, 25-40 13.7%, 40+ 8.4%; median gap 11.94 pp.
* **Where the extremes live**: 97.4% of >=25 pp gaps are off the ATP/WTA main tour (ITF 78.4%, Challenger 11.0%, doubles 6.5%). Main tour: ATP 3.7% and WTA 5.9% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 20,323): MARKET_ALREADY_SETTLED_WHEN_PRICED 35.5%, STALE_QUOTE 20.0%, BOOK_QUALITY 16.2%, POOR_DATA 9.0%, POSSIBLY_IN_PLAY_QUOTE 5.9%, IDENTITY_AMBIGUOUS 4.2%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 1.7%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 35.5%, market_freshness 20.0%, execution 16.2%, data 12.3%, market_freshness/coverage 9.3%, mapping 4.2%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 55.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 44.8% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 20,323 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.8%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 27.0% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 485.0 points vs 1671.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.02, Gen-2 0.816, Gen-1 ledger 0.865 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 1041 model 0.2257 vs Kalshi 0.2034; n 214 model 0.307 vs Kalshi 0.1666.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 380,778 model-market comparisons (631,009 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 125,237 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-13T13:51:58.239081+00:00'], shadow board 106,524 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-13T13:52:02.116240+00:00'], Model 4 44,266 rows, 31,591 settled tickers, 11,916 tickers with an external scan.
* By model: {"gen1_ledger": 83630, "gen1_elo": 53529, "fair_v1": 53529, "gen2": 53529, "gen1_sr": 53529, "model4_fundamental": 41558, "model4_conditioned": 41474}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 91,920 | 13.9 | 9.5 | 20.1 | 15.2 | 19.2 | 13.7 | 8.4 | 11.94 | 41.3% | 22.1% |
| MW fair_v1 | 53,529 | 12.5 | 8.6 | 18.7 | 15.2 | 19.6 | 15.0 | 10.4 | 13.23 | 45.0% | 25.4% |
| MW gen1_elo | 53,529 | 12.3 | 8.7 | 19.1 | 15.3 | 19.4 | 15.0 | 10.2 | 13.01 | 44.6% | 25.2% |
| MW gen1_ledger | 38,391 | 15.8 | 10.8 | 22.2 | 15.2 | 18.6 | 11.9 | 5.5 | 10.29 | 36.0% | 17.5% |
| MW gen1_sr | 53,529 | 9.9 | 7.1 | 16.5 | 13.9 | 20.9 | 18.8 | 12.9 | 16.01 | 52.5% | 31.7% |
| MW gen2 | 53,529 | 10.8 | 7.5 | 16.6 | 13.7 | 19.7 | 17.7 | 14.0 | 15.56 | 51.4% | 31.7% |
| all families model4_conditioned | 41,474 | 22.2 | 17.9 | 34.6 | 16.9 | 4.9 | 2.2 | 1.2 | 6.06 | 8.4% | 3.4% |
| all families model4_fundamental | 41,558 | 17.3 | 13.5 | 34.0 | 19.9 | 9.9 | 3.8 | 1.5 | 7.6 | 15.2% | 5.3% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.5%, >=15pp 41.3%, >=20pp 30.5%, >=25pp 22.1%, >=30pp 16.0%, >=40pp 8.4%, >=50pp 3.9%
Executable gap (model outside the book, before fees): median 8.6pp; >=10pp 45.7%, >=25pp 17.6%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,130 | 27.9 | 16.0 | 28.0 | 13.2 | 10.7 | 3.5 | 0.6 | 5.77 | 14.9% | 4.1% |
| CHALLENGER | 8,400 | 16.4 | 9.6 | 20.6 | 15.2 | 15.7 | 11.3 | 11.2 | 10.93 | 38.2% | 22.5% |
| ITF_MEN | 15,844 | 9.6 | 7.3 | 17.1 | 14.9 | 21.1 | 17.1 | 12.9 | 15.45 | 51.1% | 30.0% |
| ITF_WOMEN | 20,712 | 9.3 | 7.0 | 16.1 | 14.6 | 22.2 | 18.6 | 12.1 | 16.04 | 52.9% | 30.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,110 | 16.6 | 13.2 | 24.9 | 20.7 | 16.8 | 6.7 | 1.1 | 8.65 | 24.6% | 7.8% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,130 | 26.2 | 15.7 | 26.3 | 15.7 | 11.3 | 3.9 | 0.8 | 6.1 | 16.0% | 4.7% |
| CHALLENGER | 8,400 | 14.4 | 9.1 | 19.0 | 13.8 | 18.4 | 13.6 | 11.7 | 12.54 | 43.7% | 25.3% |
| ITF_MEN | 15,844 | 8.2 | 6.2 | 15.2 | 13.8 | 20.4 | 19.9 | 16.3 | 17.84 | 56.6% | 36.2% |
| ITF_WOMEN | 20,712 | 7.8 | 5.8 | 14.1 | 12.7 | 20.7 | 21.2 | 17.8 | 19.2 | 59.6% | 39.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,110 | 14.1 | 10.3 | 21.5 | 16.2 | 22.5 | 12.8 | 2.5 | 11.28 | 37.8% | 15.3% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,130 | 23.4 | 14.1 | 25.6 | 15.5 | 14.3 | 5.9 | 1.1 | 7.03 | 21.3% | 7.0% |
| CHALLENGER | 8,400 | 15.2 | 9.6 | 20.8 | 15.6 | 16.0 | 11.9 | 11.0 | 11.16 | 38.9% | 22.9% |
| ITF_MEN | 15,844 | 9.3 | 7.3 | 17.2 | 14.3 | 21.4 | 17.3 | 13.2 | 15.73 | 51.9% | 30.5% |
| ITF_WOMEN | 20,712 | 9.2 | 6.8 | 16.2 | 15.6 | 22.1 | 18.7 | 11.4 | 15.82 | 52.2% | 30.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,110 | 22.4 | 17.2 | 31.8 | 15.2 | 9.0 | 3.3 | 1.0 | 6.12 | 13.3% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,499 | 28.1 | 19.6 | 29.1 | 12.2 | 8.1 | 2.5 | 0.4 | 5.24 | 11.0% | 3.0% |
| CHALLENGER | 5,090 | 23.2 | 14.7 | 27.6 | 14.7 | 12.9 | 5.4 | 1.5 | 6.97 | 19.8% | 6.9% |
| DOUBLES | 2,829 | 4.8 | 4.5 | 12.9 | 11.0 | 20.5 | 24.8 | 21.5 | 23.23 | 66.9% | 46.3% |
| ITF_MEN | 11,426 | 12.8 | 9.5 | 21.5 | 15.7 | 21.6 | 12.9 | 6.0 | 11.77 | 40.4% | 18.9% |
| ITF_WOMEN | 13,309 | 13.4 | 9.3 | 19.9 | 15.8 | 21.7 | 14.6 | 5.4 | 12.16 | 41.6% | 19.9% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,833 | 23.8 | 15.9 | 31.9 | 16.8 | 8.8 | 2.5 | 0.2 | 6.57 | 11.6% | 2.7% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,001 | 28.3 | 16.2 | 28.4 | 13.2 | 10.5 | 3.1 | 0.3 | 5.64 | 13.9% | 3.4% |
| CHALLENGER | 5,900 | 21.2 | 12.0 | 25.6 | 18.0 | 15.8 | 5.5 | 1.9 | 8.18 | 23.1% | 7.4% |
| ITF_MEN | 11,453 | 11.8 | 8.8 | 20.6 | 17.2 | 22.1 | 14.0 | 5.5 | 12.44 | 41.6% | 19.4% |
| ITF_WOMEN | 15,017 | 11.3 | 8.6 | 19.1 | 17.0 | 24.1 | 15.3 | 4.5 | 13.12 | 44.0% | 19.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,996 | 16.9 | 13.3 | 25.2 | 21.1 | 16.8 | 6.2 | 0.6 | 8.47 | 23.6% | 6.8% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,001 | 26.6 | 16.1 | 26.6 | 15.7 | 11.2 | 3.4 | 0.4 | 6.02 | 15.0% | 3.8% |
| CHALLENGER | 5,900 | 18.1 | 11.8 | 23.9 | 16.2 | 19.0 | 8.9 | 2.1 | 8.98 | 30.0% | 11.0% |
| ITF_MEN | 11,455 | 9.7 | 7.4 | 17.8 | 16.0 | 22.3 | 17.9 | 8.9 | 14.68 | 49.1% | 26.8% |
| ITF_WOMEN | 15,019 | 8.9 | 7.0 | 16.1 | 14.2 | 22.6 | 20.6 | 10.6 | 16.51 | 53.8% | 31.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,996 | 14.3 | 10.4 | 21.8 | 16.4 | 22.7 | 12.5 | 1.9 | 11.03 | 37.0% | 14.3% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,429 | 28.4 | 19.8 | 29.1 | 12.3 | 7.7 | 2.3 | 0.3 | 5.17 | 10.4% | 2.6% |
| CHALLENGER | 4,508 | 24.5 | 15.6 | 28.8 | 14.8 | 12.2 | 3.7 | 0.4 | 6.49 | 16.4% | 4.1% |
| DOUBLES | 2,648 | 4.7 | 4.5 | 13.1 | 11.0 | 20.4 | 24.7 | 21.7 | 23.2 | 66.7% | 46.4% |
| ITF_MEN | 9,872 | 13.6 | 10.0 | 22.9 | 16.3 | 21.7 | 11.4 | 4.1 | 10.9 | 37.2% | 15.5% |
| ITF_WOMEN | 11,459 | 14.1 | 9.8 | 20.9 | 16.3 | 21.8 | 13.4 | 3.6 | 11.38 | 38.8% | 17.0% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,770 | 24.2 | 16.3 | 31.9 | 16.8 | 8.8 | 2.0 | 0.1 | 6.43 | 10.8% | 2.0% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,829 | 4.8 | 4.5 | 12.9 | 11.0 | 20.5 | 24.8 | 21.5 | 23.23 | 66.9% | 46.3% |
| singles | 35,562 | 16.6 | 11.4 | 22.9 | 15.5 | 18.4 | 10.9 | 4.2 | 9.75 | 33.6% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 11,660 | 12.6 | 9.0 | 19.2 | 15.0 | 19.6 | 14.3 | 10.2 | 13.02 | 44.2% | 24.5% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 34,800 | 12.9 | 8.6 | 18.8 | 15.1 | 19.2 | 15.1 | 10.3 | 13.04 | 44.6% | 25.4% |
| UNKNOWN | 6,656 | 10.4 | 7.5 | 17.1 | 16.5 | 21.5 | 15.8 | 11.1 | 14.3 | 48.4% | 26.9% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 14,856 | 19.0 | 11.8 | 22.4 | 15.7 | 14.9 | 9.5 | 6.6 | 9.04 | 31.0% | 16.1% |
| B | 6,356 | 12.9 | 8.5 | 19.5 | 15.2 | 19.7 | 12.4 | 11.7 | 12.84 | 43.8% | 24.1% |
| C | 7,647 | 11.9 | 8.5 | 19.3 | 15.9 | 19.2 | 14.7 | 10.4 | 13.06 | 44.4% | 25.1% |
| D | 8,860 | 11.2 | 8.4 | 17.8 | 15.2 | 21.7 | 15.7 | 10.1 | 14.08 | 47.4% | 25.7% |
| F | 15,810 | 7.3 | 5.7 | 15.1 | 14.2 | 23.0 | 21.1 | 13.7 | 18.05 | 57.7% | 34.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 10,074 | 25.0 | 15.9 | 29.0 | 14.9 | 10.5 | 3.4 | 1.2 | 6.35 | 15.2% | 4.7% |
| B | 5,221 | 16.7 | 11.0 | 24.1 | 17.1 | 18.9 | 9.4 | 2.9 | 9.61 | 31.2% | 12.3% |
| C | 7,594 | 11.0 | 7.8 | 19.5 | 15.0 | 20.9 | 15.7 | 10.1 | 13.49 | 46.7% | 25.8% |
| D | 5,875 | 14.4 | 10.0 | 21.0 | 15.4 | 21.1 | 12.8 | 5.3 | 11.39 | 39.2% | 18.1% |
| F | 9,627 | 10.2 | 8.4 | 16.7 | 14.4 | 23.4 | 18.8 | 7.9 | 15.08 | 50.2% | 26.8% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 16,829 | 17.5 | 10.9 | 21.3 | 15.5 | 15.2 | 10.2 | 9.4 | 10.04 | 34.8% | 19.6% |
| LIMITED | 11,631 | 13.4 | 9.4 | 20.4 | 15.9 | 19.9 | 13.4 | 7.6 | 12.0 | 40.9% | 21.0% |
| POOR | 25,069 | 8.8 | 6.7 | 16.1 | 14.6 | 22.4 | 19.0 | 12.4 | 16.36 | 53.8% | 31.4% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,346 | 23.8 | 18.0 | 33.0 | 15.4 | 6.4 | 3.0 | 0.4 | 5.89 | 9.8% | 3.4% |
| GAME_SPREAD | 6,978 | 22.8 | 15.3 | 32.0 | 16.8 | 9.1 | 3.3 | 0.7 | 6.69 | 13.0% | 3.9% |
| MATCH_WINNER | 38,391 | 15.8 | 10.8 | 22.2 | 15.2 | 18.6 | 11.9 | 5.5 | 10.29 | 36.0% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 17,191 | 28.4 | 16.8 | 30.7 | 12.7 | 8.8 | 2.3 | 0.3 | 5.57 | 11.4% | 2.6% |
| TOTAL_GAMES | 11,700 | 9.7 | 10.8 | 36.4 | 25.6 | 10.4 | 4.2 | 2.9 | 9.12 | 17.4% | 7.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,746 | 24.5 | 28.8 | 33.3 | 8.0 | 3.9 | 1.2 | 0.3 | 4.79 | 5.4% | 1.5% |
| GAME_SPREAD | 9,594 | 46.7 | 15.8 | 25.2 | 7.4 | 2.4 | 1.9 | 0.6 | 3.33 | 4.9% | 2.5% |
| TOTAL_GAMES | 17,134 | 6.5 | 9.8 | 41.0 | 29.8 | 7.2 | 3.3 | 2.3 | 9.14 | 12.9% | 5.6% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,782 | 23.8 | 16.6 | 34.7 | 14.7 | 6.9 | 2.7 | 0.5 | 6.05 | 10.1% | 3.2% |
| GAME_SPREAD | 9,603 | 20.3 | 13.4 | 28.5 | 20.1 | 12.1 | 4.3 | 1.1 | 7.71 | 17.6% | 5.5% |
| TOTAL_GAMES | 17,173 | 10.0 | 10.9 | 36.5 | 24.2 | 11.3 | 4.4 | 2.6 | 9.0 | 18.3% | 7.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 53,529 | 45.0% | 25.4% | 13.23 | 35.5% | 15.1% | 10.71 |
| gen1_elo | 53,529 | 44.6% | 25.2% | 13.01 | 34.9% | 15.0% | 10.51 |
| gen1_sr | 53,529 | 52.5% | 31.7% | 16.01 | 43.9% | 21.4% | 12.99 |
| gen2 | 53,529 | 51.4% | 31.7% | 15.56 | 43.9% | 22.9% | 12.83 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,520 | 15.5 | 10.5 | 21.3 | 17.3 | 20.1 | 11.9 | 3.5 | 10.72 | 35.4% | 15.4% |
| STALE | 33,009 | 10.7 | 7.4 | 17.0 | 13.9 | 19.3 | 17.0 | 14.7 | 15.41 | 51.0% | 31.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 31,859 | 16.3 | 11.1 | 22.7 | 15.2 | 18.2 | 11.5 | 5.0 | 9.96 | 34.7% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 91,920 | 31859 | 23992 | 36069 | 25.3 | 150.3 | 1451.1 |
| ge_15pp | 37,951 | 11042 | 8560 | 18349 | 29.1 | 453.0 | 1451.1 |
| ge_25pp | 20,323 | 5246 | 3742 | 11335 | 35.0 | 594.3 | 1431.1 |
| lt_10pp | 40,018 | 15959 | 11334 | 12725 | 22.8 | 49.7 | 1421.7 |

Current slate `SL-20261113T141415Z-574844f5`: 182 priced rows, quote age at build {'median': 50.2, 'max': 70.2}, freshness {'STALE': 182}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 52 | 0.0 | 0.0 | 34.6 | 9.6 | 32.7 | 19.2 | 3.9 | 18.34 | 55.8% | 23.1% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 5,103 | 19.2 | 11.1 | 25.6 | 18.3 | 17.7 | 7.1 | 1.0 | 8.77 | 25.8% | 8.1% |
| KALSHI_LONE_OUTLIER | 32 | 6.2 | 6.2 | 75.0 | 6.2 | 3.1 | 3.1 | 0.0 | 6.16 | 6.2% | 3.1% |
| MARKETS_AGREE | 1,101 | 66.2 | 33.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,340 | 0.0 | 2.2 | 38.4 | 26.0 | 23.9 | 8.7 | 0.9 | 11.66 | 33.5% | 9.6% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 53,529 | 8657 (16.2%) | 27.0% | 0.9% | {"EXTERNAL_STALE": 5103, "AGREES_WITH_KALSHI": 2340, "ALL_AGREE": 1101, "SUPPORTS_MODEL_DIRECTION": 50, "AGREES_WITH_MODEL": 32, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 24,110 | 2129 (8.8%) | 36.8% | 1.5% | {"EXTERNAL_STALE": 1315, "AGREES_WITH_KALSHI": 783, "SUPPORTS_MODEL_DIRECTION": 29, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 13,615 | 648 (4.8%) | 34.6% | 2.0% | {"EXTERNAL_STALE": 411, "AGREES_WITH_KALSHI": 224, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 6,153 | 616 (10.0%) | 35.2% | 2.1% | {"EXTERNAL_STALE": 386, "AGREES_WITH_KALSHI": 217, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 21,290 | 4980 (23.4%) | 19.1% | 0.9% | {"EXTERNAL_STALE": 2855, "ALL_AGREE": 1101, "AGREES_WITH_KALSHI": 949, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 28, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 10,503 | 10.6 | 7.7 | 18.9 | 14.3 | 21.8 | 16.4 | 10.3 | 14.38 | 48.5% | 26.8% |
| 4-10x | 7,249 | 10.9 | 8.7 | 18.1 | 14.9 | 21.5 | 14.7 | 11.4 | 14.1 | 47.5% | 26.0% |
| <2x | 27,213 | 14.5 | 9.6 | 19.8 | 15.9 | 17.6 | 13.4 | 9.3 | 11.73 | 40.2% | 22.6% |
| >=10x | 8,564 | 10.2 | 6.4 | 15.2 | 14.2 | 21.8 | 18.9 | 13.3 | 16.52 | 54.0% | 32.2% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 14,111 | 12.3 | 8.6 | 19.6 | 16.0 | 19.2 | 13.7 | 10.6 | 12.85 | 43.5% | 24.3% |
| 300-1000 | 11,671 | 11.4 | 8.6 | 17.8 | 15.1 | 20.5 | 16.4 | 10.1 | 13.94 | 47.0% | 26.5% |
| <300 | 16,947 | 8.1 | 5.9 | 15.1 | 14.4 | 22.9 | 20.0 | 13.6 | 17.46 | 56.5% | 33.7% |
| >=3000 | 10,800 | 20.9 | 12.8 | 23.9 | 15.4 | 14.1 | 7.4 | 5.5 | 7.92 | 27.0% | 12.9% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1662 | 0.5472 | 0.4081 | 0.4765 | +0.071 | -0.068 | 0.0039 ± 0.0038 |
| ratio 4-10x | 1136 | 0.5714 | 0.4272 | 0.485 | +0.086 | -0.058 | 0.0099 ± 0.0048 |
| ratio <2x | 4047 | 0.5345 | 0.4115 | 0.4304 | +0.104 | -0.019 | 0.0151 ± 0.0022 |
| ratio >=10x | 1398 | 0.5582 | 0.3869 | 0.4306 | +0.128 | -0.044 | 0.0184 ± 0.0047 |
| thinner_sample 1000-3000 | 2274 | 0.5398 | 0.4126 | 0.4415 | +0.098 | -0.029 | 0.0131 ± 0.003 |
| thinner_sample 300-1000 | 1881 | 0.5593 | 0.4191 | 0.4684 | +0.091 | -0.049 | 0.0066 ± 0.0036 |
| thinner_sample <300 | 2693 | 0.5521 | 0.3855 | 0.44 | +0.112 | -0.054 | 0.0158 ± 0.0034 |
| thinner_sample >=3000 | 1395 | 0.5274 | 0.4337 | 0.4423 | +0.085 | -0.009 | 0.0141 ± 0.0031 |
| data_status ADEQUATE | 2220 | 0.5315 | 0.429 | 0.4383 | +0.093 | -0.009 | 0.0151 ± 0.0026 |
| data_status LIMITED | 2014 | 0.5463 | 0.4133 | 0.4603 | +0.086 | -0.047 | 0.0079 ± 0.0034 |
| data_status POOR | 4009 | 0.5542 | 0.3953 | 0.4457 | +0.108 | -0.050 | 0.0137 ± 0.0027 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1183 | 0.1965 | 0.1965 | +0.0000 ± 0.0004 | 0.5726 | 0.5727 | 0.5021 | 0.4869 | 0.4911 | -0.100 ± 0.0136 | -0.0087 (8) |
| 3-5 | 766 | 0.2088 | 0.2082 | +0.0006 ± 0.0013 | 0.6034 | 0.6005 | 0.502 | 0.4622 | 0.4739 | -0.099 ± 0.0169 | 0.01 (3) |
| 5-10 | 1778 | 0.2023 | 0.2005 | +0.0018 ± 0.0016 | 0.591 | 0.5845 | 0.5088 | 0.4348 | 0.4584 | -0.091 ± 0.0109 | -0.0143 (7) |
| 10-15 | 1432 | 0.2203 | 0.2106 | +0.0097 ± 0.003 | 0.6333 | 0.605 | 0.5244 | 0.401 | 0.4225 | -0.104 ± 0.0123 | -0.055 (6) |
| 15-25 | 1829 | 0.2253 | 0.2068 | +0.0185 ± 0.0041 | 0.6456 | 0.5969 | 0.5705 | 0.3761 | 0.4254 | -0.099 ± 0.0107 | -0.0045 (11) |
| 25-40 | 1041 | 0.2257 | 0.2034 | +0.0222 ± 0.0084 | 0.6418 | 0.5873 | 0.6431 | 0.3337 | 0.4515 | -0.066 ± 0.013 | -0.06 (2) |
| 40+ | 214 | 0.307 | 0.1666 | +0.1404 ± 0.0253 | 0.8206 | 0.5019 | 0.7244 | 0.2671 | 0.3505 | -0.089 ± 0.0244 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5979 | 0.1871 | 0.1879 | -0.0008 ± 0.0002 | 0.5507 | 0.5517 | 0.4917 | 0.4764 | 0.5056 | -0.023 ± 0.0057 | -0.01 (28) |
| 3-5 | 4060 | 0.199 | 0.1971 | +0.0019 ± 0.0006 | 0.579 | 0.5724 | 0.4812 | 0.4414 | 0.4367 | -0.058 ± 0.007 | 0.005 (6) |
| 5-10 | 8907 | 0.2006 | 0.1964 | +0.0042 ± 0.0007 | 0.587 | 0.5733 | 0.4821 | 0.4083 | 0.4166 | -0.049 ± 0.0047 | -0.0114 (22) |
| 10-15 | 7254 | 0.2023 | 0.1863 | +0.0161 ± 0.0013 | 0.5917 | 0.5463 | 0.4844 | 0.3604 | 0.3579 | -0.063 ± 0.0051 | -0.0379 (19) |
| 15-25 | 9360 | 0.2062 | 0.1669 | +0.0393 ± 0.0017 | 0.6043 | 0.4963 | 0.4977 | 0.3022 | 0.3003 | -0.067 ± 0.0042 | -0.0043 (51) |
| 25-40 | 7318 | 0.2226 | 0.1232 | +0.0993 ± 0.0026 | 0.6391 | 0.3804 | 0.5234 | 0.2092 | 0.2121 | -0.059 ± 0.004 | -0.0733 (3) |
| 40+ | 5052 | 0.3795 | 0.0439 | +0.3356 ± 0.0033 | 0.9891 | 0.1704 | 0.6276 | 0.1019 | 0.0572 | -0.076 ± 0.0028 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 946 | 0.2021 | 0.2024 | -0.0003 ± 0.0005 | 0.5844 | 0.5853 | 0.5087 | 0.4936 | 0.5169 | -0.096 ± 0.0156 | -0.0117 (6) |
| 3-5 | 688 | 0.2125 | 0.2097 | +0.0028 ± 0.0014 | 0.6087 | 0.6025 | 0.5193 | 0.4797 | 0.4622 | -0.123 ± 0.0187 | 0.01 (3) |
| 5-10 | 1535 | 0.2049 | 0.2032 | +0.0017 ± 0.0017 | 0.5954 | 0.5911 | 0.5379 | 0.4635 | 0.4906 | -0.084 ± 0.0119 | -0.01 (4) |
| 10-15 | 1330 | 0.2151 | 0.2072 | +0.0079 ± 0.0031 | 0.6229 | 0.6001 | 0.5575 | 0.4331 | 0.4662 | -0.102 ± 0.013 | -0.04 (5) |
| 15-25 | 1924 | 0.2332 | 0.2116 | +0.0216 ± 0.0041 | 0.6644 | 0.6073 | 0.5841 | 0.3884 | 0.433 | -0.099 ± 0.0107 | -0.0183 (12) |
| 25-40 | 1334 | 0.2664 | 0.2003 | +0.0661 ± 0.0077 | 0.7431 | 0.5811 | 0.6583 | 0.3446 | 0.3981 | -0.108 ± 0.0123 | -0.008 (5) |
| 40+ | 486 | 0.3749 | 0.1598 | +0.2151 ± 0.0182 | 1.0178 | 0.4849 | 0.7318 | 0.2426 | 0.2798 | -0.088 ± 0.0175 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5128 | 0.1905 | 0.1908 | -0.0002 ± 0.0002 | 0.5564 | 0.5567 | 0.5064 | 0.4913 | 0.5064 | -0.039 ± 0.0063 | -0.0154 (26) |
| 3-5 | 3563 | 0.1941 | 0.1933 | +0.0009 ± 0.0006 | 0.5656 | 0.5629 | 0.5112 | 0.4715 | 0.4791 | -0.043 ± 0.0075 | 0.01 (5) |
| 5-10 | 7961 | 0.1957 | 0.1924 | +0.0033 ± 0.0007 | 0.5757 | 0.5632 | 0.5066 | 0.4323 | 0.4493 | -0.039 ± 0.005 | -0.0117 (6) |
| 10-15 | 6579 | 0.2018 | 0.1896 | +0.0122 ± 0.0013 | 0.593 | 0.5554 | 0.5062 | 0.3823 | 0.396 | -0.050 ± 0.0054 | -0.0189 (18) |
| 15-25 | 9443 | 0.2161 | 0.1795 | +0.0366 ± 0.0017 | 0.6297 | 0.5271 | 0.5237 | 0.3282 | 0.335 | -0.060 ± 0.0044 | -0.014 (52) |
| 25-40 | 8490 | 0.2499 | 0.1377 | +0.1122 ± 0.0026 | 0.7061 | 0.42 | 0.5591 | 0.2418 | 0.2271 | -0.076 ± 0.004 | -0.0095 (20) |
| 40+ | 6766 | 0.4019 | 0.0594 | +0.3425 ± 0.0034 | 1.0589 | 0.2134 | 0.6545 | 0.1191 | 0.0804 | -0.074 ± 0.0029 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1161 | 0.1963 | 0.1974 | -0.0011 ± 0.0005 | 0.5724 | 0.575 | 0.5012 | 0.4857 | 0.5228 | -0.059 ± 0.0136 | -0.0191 (11) |
| 3-5 | 835 | 0.2088 | 0.2074 | +0.0014 ± 0.0013 | 0.6044 | 0.5998 | 0.4956 | 0.4561 | 0.4599 | -0.106 ± 0.0165 | 0.002 (5) |
| 5-10 | 1780 | 0.2032 | 0.199 | +0.0042 ± 0.0016 | 0.5921 | 0.5804 | 0.5098 | 0.4361 | 0.4438 | -0.104 ± 0.0109 | -0.01 (10) |
| 10-15 | 1481 | 0.2126 | 0.2031 | +0.0095 ± 0.0029 | 0.616 | 0.5888 | 0.5368 | 0.4136 | 0.4389 | -0.103 ± 0.0118 | -0.0286 (7) |
| 15-25 | 1732 | 0.231 | 0.2118 | +0.0192 ± 0.0043 | 0.6592 | 0.6076 | 0.5797 | 0.3857 | 0.433 | -0.102 ± 0.0111 | -0.03 (1) |
| 25-40 | 1025 | 0.2177 | 0.2058 | +0.0118 ± 0.0084 | 0.6253 | 0.5926 | 0.6514 | 0.3419 | 0.4751 | -0.059 ± 0.0131 | -0.0267 (3) |
| 40+ | 229 | 0.3093 | 0.1804 | +0.1289 ± 0.0253 | 0.8338 | 0.5323 | 0.7372 | 0.2806 | 0.3799 | -0.075 ± 0.0258 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5812 | 0.1867 | 0.1872 | -0.0005 ± 0.0002 | 0.5494 | 0.5499 | 0.487 | 0.4716 | 0.4864 | -0.037 ± 0.0057 | -0.0189 (44) |
| 3-5 | 4172 | 0.2046 | 0.2029 | +0.0017 ± 0.0006 | 0.5943 | 0.5886 | 0.4802 | 0.4407 | 0.4394 | -0.055 ± 0.0071 | -0.0073 (22) |
| 5-10 | 9020 | 0.1959 | 0.1905 | +0.0054 ± 0.0007 | 0.5753 | 0.5582 | 0.4847 | 0.4107 | 0.4106 | -0.056 ± 0.0046 | -0.0117 (42) |
| 10-15 | 7278 | 0.1955 | 0.1799 | +0.0155 ± 0.0012 | 0.5765 | 0.5326 | 0.4949 | 0.3715 | 0.3703 | -0.062 ± 0.005 | -0.0136 (14) |
| 15-25 | 9371 | 0.2111 | 0.1718 | +0.0392 ± 0.0017 | 0.6156 | 0.507 | 0.5094 | 0.3147 | 0.3123 | -0.068 ± 0.0043 | -0.0533 (3) |
| 25-40 | 7309 | 0.2165 | 0.1231 | +0.0934 ± 0.0026 | 0.6262 | 0.3794 | 0.525 | 0.2096 | 0.221 | -0.052 ± 0.004 | -0.02 (4) |
| 40+ | 4968 | 0.3879 | 0.0479 | +0.3401 ± 0.0035 | 1.0113 | 0.1804 | 0.6364 | 0.1073 | 0.0632 | -0.077 ± 0.003 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1636 | 0.1963 | 0.1959 | +0.0004 ± 0.0004 | 0.5707 | 0.5695 | 0.5062 | 0.4912 | 0.4866 | -0.076 ± 0.0112 | -0.0221 (56) |
| 3-5 | 1157 | 0.1893 | 0.1893 | -0.0000 ± 0.001 | 0.5567 | 0.5558 | 0.4984 | 0.4585 | 0.4771 | -0.054 ± 0.0131 | -0.0194 (34) |
| 5-10 | 2344 | 0.199 | 0.1939 | +0.0051 ± 0.0014 | 0.587 | 0.5706 | 0.5094 | 0.4357 | 0.4381 | -0.077 ± 0.0093 | -0.005 (78) |
| 10-15 | 1619 | 0.2154 | 0.203 | +0.0124 ± 0.0028 | 0.6255 | 0.5896 | 0.5449 | 0.4222 | 0.4317 | -0.088 ± 0.0115 | 0.0015 (67) |
| 15-25 | 2110 | 0.2322 | 0.2079 | +0.0244 ± 0.0039 | 0.6628 | 0.5995 | 0.5924 | 0.3974 | 0.4336 | -0.089 ± 0.01 | -0.0214 (59) |
| 25-40 | 1231 | 0.2422 | 0.2116 | +0.0305 ± 0.008 | 0.691 | 0.6064 | 0.6885 | 0.3768 | 0.4842 | -0.082 ± 0.0124 | -0.0243 (28) |
| 40+ | 455 | 0.3293 | 0.1972 | +0.1321 ± 0.02 | 0.9397 | 0.5762 | 0.8074 | 0.3306 | 0.4462 | -0.092 ± 0.0187 | -0.1137 (8) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5897 | 0.177 | 0.177 | +0.0001 ± 0.0002 | 0.5243 | 0.5236 | 0.5085 | 0.4933 | 0.4989 | -0.043 ± 0.0055 | -0.0154 (103) |
| 3-5 | 4053 | 0.1944 | 0.1935 | +0.0009 ± 0.0006 | 0.5674 | 0.5653 | 0.5016 | 0.4619 | 0.471 | -0.040 ± 0.007 | -0.0212 (73) |
| 5-10 | 8286 | 0.197 | 0.1905 | +0.0065 ± 0.0007 | 0.5812 | 0.5617 | 0.5027 | 0.4291 | 0.4229 | -0.061 ± 0.0048 | -0.0084 (134) |
| 10-15 | 5698 | 0.2109 | 0.1947 | +0.0162 ± 0.0014 | 0.6141 | 0.5704 | 0.5383 | 0.4154 | 0.4096 | -0.071 ± 0.0059 | -0.0054 (112) |
| 15-25 | 6983 | 0.2318 | 0.1995 | +0.0323 ± 0.0021 | 0.6664 | 0.5782 | 0.577 | 0.3817 | 0.3971 | -0.067 ± 0.0054 | -0.024 (112) |
| 25-40 | 4498 | 0.2578 | 0.1905 | +0.0673 ± 0.0041 | 0.7287 | 0.5545 | 0.6408 | 0.3286 | 0.3799 | -0.062 ± 0.0064 | -0.0267 (58) |
| 40+ | 2020 | 0.3704 | 0.159 | +0.2114 ± 0.0091 | 1.04 | 0.4742 | 0.7407 | 0.2411 | 0.2896 | -0.059 ± 0.0085 | -0.054 (15) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 8243 | 1.02 ± 0.031 | 1.081 | 0.1678 | 0.1711 | 0.216 | 0.2033 |
| gen2 | 8243 | 0.816 ± 0.028 | 1.059 | 0.1741 | 0.1714 | 0.2335 | 0.2032 |
| gen1_elo | 8243 | 1.003 ± 0.03 | 1.073 | 0.1742 | 0.1713 | 0.2151 | 0.2034 |
| gen1_sr | 8243 | 1.0 ± 0.036 | 1.107 | 0.1336 | 0.1729 | 0.2295 | 0.203 |
| gen1_ledger | 10552 | 0.865 ± 0.023 | 1.061 | 0.1904 | 0.1772 | 0.2173 | 0.2001 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 37,951)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 9,172 | 24.2% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 8,947 | 23.6% |
| BOOK_QUALITY | execution | 6,373 | 16.8% |
| POOR_DATA | data | 4,320 | 11.4% |
| LIMITED_DATA | data | 2,281 | 6.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 2,221 | 5.9% |
| IDENTITY_AMBIGUOUS | mapping | 1,559 | 4.1% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,430 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 1,064 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 583 | 1.5% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 24.2%, coverage 23.6%, data 17.4%, execution 16.8%, market_freshness/coverage 8.7%, mapping 4.1%, model_calibration_or_unknown 3.8%, model_calibration 1.5%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 95.1%, LOW_DATA_QUALITY 72.2%, THIN_PLAYER_HISTORY 60.1%, STALE_PLAYER_DATA 52.0%, STALE_KALSHI_QUOTE 48.4%, MODEL_INTERNAL_DISAGREEMENT 41.7%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 23.3%, MODEL_HIGH_UNCERTAINTY 18.8%, PLAYER_IDENTITY_RISK 15.0%, LEVEL_TRANSFER_RISK 9.3%, LOW_DISPLAYED_LIQUIDITY 8.7%, EVENT_MAPPING_RISK 7.0%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.2%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.9%, POST_SETTLEMENT_OBSERVATION 23.6%, POSSIBLE_IN_PLAY_QUOTE 6.3%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 20,323)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,209 | 35.5% |
| STALE_QUOTE | market_freshness | 4,068 | 20.0% |
| BOOK_QUALITY | execution | 3,291 | 16.2% |
| POOR_DATA | data | 1,826 | 9.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,199 | 5.9% |
| IDENTITY_AMBIGUOUS | mapping | 864 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 701 | 3.5% |
| LIMITED_DATA | data | 675 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 349 | 1.7% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 140 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 35.5%, market_freshness 20.0%, execution 16.2%, data 12.3%, market_freshness/coverage 9.3%, mapping 4.2%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.2%, START_UNVERIFIABLE 97.4%, LOW_DATA_QUALITY 75.2%, THIN_PLAYER_HISTORY 62.2%, STALE_KALSHI_QUOTE 55.8%, STALE_PLAYER_DATA 45.2%, MODEL_INTERNAL_DISAGREEMENT 41.7%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 22.4%, MODEL_HIGH_UNCERTAINTY 19.4%, PLAYER_IDENTITY_RISK 17.8%, LOW_DISPLAYED_LIQUIDITY 8.6%, EVENT_MAPPING_RISK 8.5%, LEVEL_TRANSFER_RISK 8.1%, MODEL_CALIBRATION_OUTLIER 4.6%, EXTERNAL_MARKET_REJECTION 1.7%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 38.3%, POST_SETTLEMENT_OBSERVATION 35.5%, POSSIBLE_IN_PLAY_QUOTE 6.4%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 16353, "IDENTITY_AMBIGUOUS": 3970}; ticker orientation: {"VERIFIED": 20323}.

Checks: discipline:AMBIGUOUS 1311, discipline:PASS 19012, identity_confidence:AMBIGUOUS 3617, identity_confidence:PASS 16706, level_mapping:NA 1323, level_mapping:PASS 19000, market_pair:AMBIGUOUS 518, market_pair:NA 431, market_pair:PASS 19374, model_complement:NA 393, model_complement:PASS 19930, namesake:AMBIGUOUS 6, namesake:PASS 20317, physical_match_id:NA 6708, physical_match_id:PASS 13615, player_ids:PASS 20323, same_pair_other_event:PASS 20323, ticker_orientation:PASS 20323

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,629 | 3.7% | 3.1% | 1.2% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 24, "market_freshness/coverage": 22} | 5.47 | 0.222 / 0.2181 (869) | 25.7% | 2.4% | 3.2% | 3.0% |
| CHALLENGER | 13,490 | 16.6% | 6.0% | 11.0% | {"coverage": 1378, "market_freshness": 274, "market_freshness/coverage": 244, "data": 164, "model_calibration_or_unknown": 83, "execution": 41, "model_calibration": 41, "mapping": 17, "possible_market_error": 1} | 7.3 | 0.2216 / 0.2112 (3132) | 41.8% | 13.5% | 4.0% | 22.9% |
| DOUBLES | 2,829 | 46.3% | 46.4% | 6.5% | {"execution": 724, "mapping": 398, "market_freshness": 106, "market_freshness/coverage": 76, "coverage": 7} | 23.2 | 0.2977 / 0.2314 (712) | 8.3% | 0.0% | 100.0% | 6.4% |
| ITF_MEN | 27,270 | 25.3% | 17.6% | 34.0% | {"coverage": 2449, "market_freshness": 1441, "execution": 1053, "data": 1019, "market_freshness/coverage": 704, "mapping": 233, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.73 | 0.2185 / 0.1979 (5791) | 42.4% | 69.7% | 14.3% | 21.8% |
| ITF_WOMEN | 34,021 | 26.5% | 18.6% | 44.4% | {"coverage": 3296, "market_freshness": 1986, "execution": 1390, "data": 1217, "market_freshness/coverage": 797, "mapping": 210, "model_calibration_or_unknown": 98, "model_calibration": 23} | 12.44 | 0.2034 / 0.1941 (6663) | 43.0% | 57.2% | 10.1% | 22.2% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,943 | 5.9% | 5.0% | 1.4% | {"market_freshness": 111, "model_calibration_or_unknown": 52, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.68 | 0.2311 / 0.2208 (816) | 30.3% | 2.0% | 1.2% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.4% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 523 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 519 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 725 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFMATCH-26NOV12VALRAT-RAT` | ITF_MEN | gen1_ledger | 92% / 4% | +88 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 10 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1333.0, ratio 3.64); no external reference |
| 6 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 7 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 8 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 9 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 10 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 11 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 628 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 12 | `KXITFMATCH-26NOV10KOUPOR-POR` | ITF_MEN | fair_v1 | 87% / 2% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.9h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 305 min (STALE); data POOR (grade D, thinner serve sample 1554.0, ratio 1.02); no external reference |
| 13 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 14 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 17 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 18 | `KXITFMATCH-26NOV13ALMJAD-ALM` | ITF_MEN | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 68 min (STALE); data LIMITED (grade C, thinner serve sample 691.0, ratio 3.98); no external reference |
| 19 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 20 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 21 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 151 min (STALE); no external reference |
| 22 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 23 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 24 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 25 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 26 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 27 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 28 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 163 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 29 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 30 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 31 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 32 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 33 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 34 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 35 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 36 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 37 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 38 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 39 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 40 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 41 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 42 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 43 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 44 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 45 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 46 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 47 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 48 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 49 | `KXITFWMATCH-26NOV11CORROJ-ROJ` | ITF_WOMEN | fair_v1 | 87% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade D, thinner serve sample 531.0, ratio 1.04); no external reference |
| 50 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9736, "by_level_share_of_ge_25pp": {"ATP": 0.0121, "CHALLENGER": 0.1104, "DOUBLES": 0.0645, "ITF_MEN": 0.34, "ITF_WOMEN": 0.4437, "OTHER": 0.0006, "WTA": 0.0144, "WTA125": 0.0144}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5577, "share_primary_cause_market_settled_or_in_play": 0.4482, "share_primary_cause_stale_quote_only": 0.2002}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 20323, "identity_ambiguous_share": 0.1953, "ticker_orientation": {"VERIFIED": 20323}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 13615, "with_external": 648, "coverage": 0.0476, "external_status": {"EXTERNAL_STALE": 411, "AGREES_WITH_KALSHI": 224, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 411, "MODEL_LONE_OUTLIER": 224, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3457, "share_external_supports_model": 0.0201}, "pregame_clean_ge_25pp": {"n": 6153, "with_external": 616, "coverage": 0.1001, "external_status": {"EXTERNAL_STALE": 386, "AGREES_WITH_KALSHI": 217, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 386, "MODEL_LONE_OUTLIER": 217, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3523, "share_external_supports_model": 0.0211}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 485.0, "median_sample_ratio": 2.44, "median_min_matches": 18.0, "median_max_days_since_last": 246.0, "share_severe_asymmetry": 0.206, "data_status": {"POOR": 11547, "LIMITED": 5122, "ADEQUATE": 3654}, "comparison_lt_10pp": {"median_thinner_serve_points": 1671.0, "median_sample_ratio": 1.71, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1662, "model_minus_observed": 0.0706, "kalshi_minus_observed": -0.0684, "brier_diff_model_minus_kalshi": 0.0039}, "4-10x": {"n": 1136, "model_minus_observed": 0.0864, "kalshi_minus_observed": -0.0578, "brier_diff_model_minus_kalshi": 0.0099}, "<2x": {"n": 4047, "model_minus_observed": 0.104, "kalshi_minus_observed": -0.0189, "brier_diff_model_minus_kalshi": 0.0151}, ">=10x": {"n": 1398, "model_minus_observed": 0.1276, "kalshi_minus_observed": -0.0438, "brier_diff_model_minus_kalshi": 0.0184}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 8243, "model": {"intercept": -0.562, "slope": 0.816, "slope_se": 0.028}, "kalshi_mid_same_rows": {"intercept": 0.165, "slope": 1.059, "slope_se": 0.031}, "mean_extremity_model": 0.1741, "mean_extremity_kalshi": 0.1714, "model_brier": 0.2335, "kalshi_brier": 0.2032, "brier_diff_model_minus_kalshi": 0.0302, "brier_diff_se": 0.0021, "model_logloss": 0.6646, "kalshi_logloss": 0.5888}, "fair_v1": {"n": 8243, "model": {"intercept": -0.472, "slope": 1.02, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.211, "slope": 1.081, "slope_se": 0.031}, "mean_extremity_model": 0.1678, "mean_extremity_kalshi": 0.1711, "model_brier": 0.216, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.0127, "brier_diff_se": 0.0017, "model_logloss": 0.6213, "kalshi_logloss": 0.5888}, "gen1_elo": {"n": 8243, "model": {"intercept": -0.457, "slope": 1.003, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.216, "slope": 1.073, "slope_se": 0.031}, "mean_extremity_model": 0.1742, "mean_extremity_kalshi": 0.1713, "model_brier": 0.2151, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": 0.0117, "brier_diff_se": 0.0017, "model_logloss": 0.6198, "kalshi_logloss": 0.589}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2543, "share_ge_15": 0.4504, "median_abs_gap": 13.23, "n": 53529}, "gen1_elo": {"share_ge_25": 0.2521, "share_ge_15": 0.4459, "median_abs_gap": 13.01, "n": 53529}, "gen1_sr": {"share_ge_25": 0.3167, "share_ge_15": 0.5255, "median_abs_gap": 16.01, "n": 53529}, "gen2": {"share_ge_25": 0.3167, "share_ge_15": 0.5138, "median_abs_gap": 15.56, "n": 53529}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1513, "share_ge_15": 0.3549, "median_abs_gap": 10.71, "n": 40651}, "gen1_elo": {"share_ge_25": 0.1499, "share_ge_15": 0.349, "median_abs_gap": 10.51, "n": 40651}, "gen1_sr": {"share_ge_25": 0.2144, "share_ge_15": 0.4394, "median_abs_gap": 12.99, "n": 40654}, "gen2": {"share_ge_25": 0.2295, "share_ge_15": 0.4389, "median_abs_gap": 12.83, "n": 40655}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.47, "share_ge_25_all": 0.037, "share_ge_25_pregame_clean": 0.0309}, "WTA": {"median_abs_gap_pregame_clean": 7.68, "share_ge_25_all": 0.0591, "share_ge_25_pregame_clean": 0.0501}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2341, "share_within_10pp_all": 0.4354, "share_within_10pp_pregame_clean": 0.4905, "corr_model_vs_mid_pregame_clean": 0.85}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1183, "model_brier": 0.1965, "kalshi_brier": 0.1965, "brier_diff_model_minus_kalshi": 0.0}, "10-15": {"n_settled": 1432, "model_brier": 0.2203, "kalshi_brier": 0.2106, "brier_diff_model_minus_kalshi": 0.0097}, "15-25": {"n_settled": 1829, "model_brier": 0.2253, "kalshi_brier": 0.2068, "brier_diff_model_minus_kalshi": 0.0185}, "25-40": {"n_settled": 1041, "model_brier": 0.2257, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": 0.0222}, "3-5": {"n_settled": 766, "model_brier": 0.2088, "kalshi_brier": 0.2082, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 214, "model_brier": 0.307, "kalshi_brier": 0.1666, "brier_diff_model_minus_kalshi": 0.1404}, "5-10": {"n_settled": 1778, "model_brier": 0.2023, "kalshi_brier": 0.2005, "brier_diff_model_minus_kalshi": 0.0018}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.562, "slope": 0.816, "slope_se": 0.028}, "kalshi_slope": {"intercept": 0.165, "slope": 1.059, "slope_se": 0.031}, "n": 8243}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.501, "slope": 0.865, "slope_se": 0.023}, "kalshi_slope": {"intercept": 0.149, "slope": 1.061, "slope_se": 0.027}, "n": 10552}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 712, "model_brier": 0.2977, "kalshi_brier": 0.2314, "brier_diff_model_minus_kalshi": 0.0664, "brier_diff_se": 0.0109, "corr_model_outcome": 0.1133, "corr_kalshi_outcome": 0.2849}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
