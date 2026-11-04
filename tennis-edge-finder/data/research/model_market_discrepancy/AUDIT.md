# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-04T21:03Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 78,055): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 19.1%, 25-40 13.7%, 40+ 8.0%; median gap 11.83 pp.
* **Where the extremes live**: 96.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.7%, Challenger 10.7%, doubles 6.7%). Main tour: ATP 3.8% and WTA 6.1% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 16,935): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.6%, STALE_QUOTE 19.4%, BOOK_QUALITY 17.9%, POOR_DATA 9.4%, POSSIBLY_IN_PLAY_QUOTE 5.7%, IDENTITY_AMBIGUOUS 4.2%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.6%, market_freshness 19.4%, execution 17.9%, data 12.8%, market_freshness/coverage 9.3%, mapping 4.2%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.9% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.9% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 16,935 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.3% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.6% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 477.0 points vs 1725.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.041, Gen-2 0.833, Gen-1 ledger 0.872 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 854 model 0.2206 vs Kalshi 0.2042; n 183 model 0.2938 vs Kalshi 0.1766.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 333,707 model-market comparisons (545,095 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 111,040 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-04T20:50:53.140142+00:00'], shadow board 89,738 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-04T20:50:56.720149+00:00'], Model 4 41,843 rows, 27,461 settled tickers, 10,288 tickers with an external scan.
* By model: {"gen1_ledger": 74970, "gen1_elo": 45097, "fair_v1": 45097, "gen2": 45097, "gen1_sr": 45097, "model4_fundamental": 39216, "model4_conditioned": 39133}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 78,055 | 14.1 | 9.6 | 20.2 | 15.3 | 19.1 | 13.7 | 8.0 | 11.83 | 40.8% | 21.7% |
| MW fair_v1 | 45,097 | 12.8 | 8.7 | 18.8 | 15.5 | 19.6 | 14.8 | 9.9 | 13.01 | 44.2% | 24.6% |
| MW gen1_elo | 45,097 | 12.6 | 8.8 | 19.3 | 15.4 | 19.5 | 14.7 | 9.7 | 12.77 | 43.9% | 24.4% |
| MW gen1_ledger | 32,958 | 15.8 | 10.9 | 22.1 | 15.2 | 18.4 | 12.1 | 5.5 | 10.29 | 36.1% | 17.7% |
| MW gen1_sr | 45,097 | 10.2 | 7.3 | 16.7 | 13.9 | 20.6 | 18.7 | 12.5 | 15.77 | 51.9% | 31.3% |
| MW gen2 | 45,097 | 11.1 | 7.6 | 16.7 | 13.8 | 19.5 | 17.8 | 13.6 | 15.4 | 50.9% | 31.4% |
| all families model4_conditioned | 39,133 | 22.2 | 18.0 | 34.1 | 17.2 | 5.0 | 2.2 | 1.2 | 6.07 | 8.5% | 3.5% |
| all families model4_fundamental | 39,216 | 17.4 | 13.5 | 33.8 | 19.9 | 10.0 | 3.8 | 1.5 | 7.63 | 15.4% | 5.4% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.1%, >=15pp 40.8%, >=20pp 30.0%, >=25pp 21.7%, >=30pp 15.6%, >=40pp 8.0%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.34pp; >=10pp 44.9%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,891 | 28.4 | 15.6 | 27.7 | 13.4 | 10.7 | 3.7 | 0.6 | 5.84 | 15.0% | 4.3% |
| CHALLENGER | 6,786 | 16.0 | 9.9 | 20.7 | 15.3 | 16.1 | 11.3 | 10.7 | 10.91 | 38.1% | 22.0% |
| ITF_MEN | 12,601 | 9.8 | 7.3 | 16.9 | 15.1 | 21.4 | 17.3 | 12.1 | 15.31 | 50.8% | 29.4% |
| ITF_WOMEN | 17,539 | 9.5 | 7.1 | 16.0 | 15.0 | 22.1 | 18.3 | 12.0 | 15.79 | 52.5% | 30.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,965 | 16.8 | 13.2 | 24.6 | 21.1 | 16.4 | 6.9 | 1.1 | 8.68 | 24.3% | 8.0% |
| WTA125 | 1,309 | 15.7 | 7.0 | 22.7 | 19.9 | 20.6 | 12.4 | 1.8 | 10.7 | 34.7% | 14.1% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,891 | 26.8 | 15.7 | 26.0 | 15.4 | 11.5 | 3.7 | 0.8 | 6.06 | 16.0% | 4.5% |
| CHALLENGER | 6,786 | 14.9 | 9.0 | 18.6 | 14.1 | 18.6 | 13.4 | 11.4 | 12.48 | 43.4% | 24.8% |
| ITF_MEN | 12,601 | 8.1 | 6.2 | 15.2 | 13.7 | 19.8 | 20.7 | 16.4 | 17.93 | 56.8% | 37.1% |
| ITF_WOMEN | 17,539 | 7.8 | 5.8 | 14.1 | 12.8 | 20.6 | 21.3 | 17.6 | 19.1 | 59.4% | 38.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,965 | 14.2 | 10.2 | 21.9 | 15.9 | 22.1 | 13.1 | 2.6 | 11.13 | 37.8% | 15.7% |
| WTA125 | 1,309 | 10.2 | 7.2 | 16.5 | 15.4 | 24.2 | 17.5 | 9.0 | 15.22 | 50.7% | 26.5% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,891 | 22.9 | 13.9 | 25.1 | 15.6 | 15.1 | 6.2 | 1.2 | 7.26 | 22.5% | 7.3% |
| CHALLENGER | 6,786 | 15.2 | 9.5 | 20.9 | 15.7 | 16.0 | 11.9 | 10.9 | 11.21 | 38.8% | 22.8% |
| ITF_MEN | 12,601 | 9.4 | 7.1 | 17.2 | 14.3 | 22.0 | 17.4 | 12.6 | 15.73 | 52.0% | 30.0% |
| ITF_WOMEN | 17,539 | 9.3 | 6.9 | 16.3 | 15.8 | 22.2 | 18.2 | 11.3 | 15.56 | 51.7% | 29.5% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,965 | 22.9 | 16.9 | 31.8 | 15.1 | 8.9 | 3.4 | 1.1 | 6.12 | 13.4% | 4.5% |
| WTA125 | 1,309 | 21.2 | 13.2 | 25.7 | 18.8 | 15.0 | 5.7 | 0.3 | 8.01 | 21.0% | 6.0% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,298 | 26.4 | 19.7 | 30.1 | 12.4 | 8.3 | 2.6 | 0.4 | 5.39 | 11.4% | 3.0% |
| CHALLENGER | 4,370 | 22.3 | 14.6 | 27.4 | 14.7 | 13.6 | 5.8 | 1.6 | 7.09 | 21.0% | 7.4% |
| DOUBLES | 2,415 | 5.0 | 4.4 | 12.6 | 10.6 | 20.5 | 24.9 | 22.0 | 23.6 | 67.4% | 46.9% |
| ITF_MEN | 9,384 | 12.9 | 9.5 | 21.1 | 15.8 | 21.5 | 13.2 | 6.0 | 11.87 | 40.6% | 19.1% |
| ITF_WOMEN | 11,389 | 13.4 | 9.1 | 19.9 | 15.7 | 21.3 | 15.0 | 5.5 | 12.28 | 41.9% | 20.5% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,717 | 24.2 | 16.0 | 31.0 | 16.7 | 9.2 | 2.7 | 0.2 | 6.57 | 12.1% | 2.9% |
| WTA125 | 1,236 | 25.2 | 13.0 | 21.5 | 19.0 | 13.1 | 6.6 | 1.5 | 7.69 | 21.2% | 8.1% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,777 | 28.8 | 15.8 | 28.1 | 13.4 | 10.5 | 3.3 | 0.3 | 5.69 | 14.0% | 3.6% |
| CHALLENGER | 4,803 | 20.5 | 12.3 | 25.6 | 17.9 | 16.1 | 6.0 | 1.6 | 8.24 | 23.7% | 7.6% |
| ITF_MEN | 9,255 | 12.0 | 8.7 | 20.5 | 17.2 | 22.2 | 14.1 | 5.4 | 12.47 | 41.6% | 19.4% |
| ITF_WOMEN | 13,004 | 11.3 | 8.5 | 18.7 | 17.2 | 24.1 | 15.2 | 5.0 | 13.28 | 44.3% | 20.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,855 | 17.1 | 13.2 | 25.0 | 21.4 | 16.4 | 6.3 | 0.6 | 8.52 | 23.3% | 6.9% |
| WTA125 | 1,261 | 16.0 | 6.9 | 22.4 | 20.1 | 20.9 | 12.0 | 1.6 | 10.67 | 34.5% | 13.6% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,777 | 27.1 | 16.1 | 26.3 | 15.3 | 11.4 | 3.3 | 0.4 | 5.98 | 15.1% | 3.7% |
| CHALLENGER | 4,803 | 18.7 | 11.3 | 23.3 | 16.5 | 19.0 | 9.3 | 1.9 | 9.07 | 30.2% | 11.2% |
| ITF_MEN | 9,256 | 9.5 | 7.3 | 17.6 | 15.9 | 21.5 | 18.8 | 9.4 | 14.92 | 49.7% | 28.2% |
| ITF_WOMEN | 13,005 | 8.8 | 6.7 | 16.0 | 14.4 | 22.7 | 20.6 | 10.9 | 16.58 | 54.1% | 31.5% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,855 | 14.4 | 10.4 | 22.2 | 16.0 | 22.4 | 12.7 | 2.0 | 10.96 | 37.0% | 14.7% |
| WTA125 | 1,261 | 10.2 | 7.3 | 16.6 | 15.5 | 24.2 | 17.6 | 8.5 | 15.1 | 50.3% | 26.1% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,241 | 26.6 | 19.9 | 30.1 | 12.6 | 8.0 | 2.5 | 0.4 | 5.36 | 10.9% | 2.9% |
| CHALLENGER | 3,857 | 23.6 | 15.5 | 28.5 | 14.9 | 13.0 | 4.0 | 0.4 | 6.61 | 17.5% | 4.5% |
| DOUBLES | 2,269 | 4.9 | 4.5 | 12.8 | 10.8 | 20.3 | 24.9 | 21.9 | 23.54 | 67.1% | 46.8% |
| ITF_MEN | 8,051 | 13.7 | 10.1 | 22.8 | 16.3 | 21.6 | 11.7 | 3.9 | 10.95 | 37.1% | 15.6% |
| ITF_WOMEN | 9,742 | 14.1 | 9.6 | 21.0 | 16.2 | 21.5 | 13.9 | 3.6 | 11.44 | 39.1% | 17.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,656 | 24.6 | 16.4 | 31.0 | 16.7 | 9.2 | 2.1 | 0.1 | 6.43 | 11.3% | 2.2% |
| WTA125 | 1,095 | 26.4 | 13.9 | 22.6 | 19.8 | 12.2 | 4.8 | 0.5 | 7.2 | 17.3% | 5.2% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,415 | 5.0 | 4.4 | 12.6 | 10.6 | 20.5 | 24.9 | 22.0 | 23.6 | 67.4% | 46.9% |
| singles | 30,543 | 16.6 | 11.4 | 22.9 | 15.5 | 18.2 | 11.1 | 4.2 | 9.77 | 33.6% | 15.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 122 | 8.2 | 9.8 | 14.8 | 8.2 | 20.5 | 25.4 | 13.1 | 18.92 | 59.0% | 38.5% |
| Clay | 9,114 | 12.8 | 9.2 | 19.7 | 15.8 | 19.8 | 13.7 | 9.0 | 12.56 | 42.5% | 22.7% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 29,532 | 13.4 | 8.7 | 18.8 | 15.2 | 19.1 | 14.8 | 9.9 | 12.86 | 43.8% | 24.7% |
| UNKNOWN | 6,092 | 10.4 | 7.7 | 17.1 | 16.4 | 21.5 | 15.9 | 11.2 | 14.3 | 48.5% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 12,790 | 19.6 | 12.0 | 22.5 | 15.9 | 14.9 | 9.0 | 6.1 | 8.8 | 30.0% | 15.1% |
| B | 5,541 | 12.9 | 8.8 | 19.6 | 15.7 | 19.6 | 12.7 | 10.7 | 12.59 | 43.0% | 23.4% |
| C | 6,378 | 11.8 | 8.9 | 19.5 | 15.9 | 18.7 | 14.6 | 10.6 | 12.89 | 43.8% | 25.1% |
| D | 7,229 | 11.8 | 8.3 | 17.9 | 15.4 | 21.5 | 15.7 | 9.4 | 13.75 | 46.6% | 25.1% |
| F | 13,159 | 7.4 | 5.5 | 14.9 | 14.7 | 23.5 | 20.9 | 13.1 | 17.79 | 57.6% | 34.0% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,788 | 24.6 | 16.1 | 29.0 | 14.9 | 10.7 | 3.4 | 1.2 | 6.37 | 15.4% | 4.7% |
| B | 4,638 | 16.7 | 10.7 | 24.1 | 16.8 | 19.0 | 9.6 | 3.1 | 9.7 | 31.7% | 12.7% |
| C | 6,485 | 11.3 | 7.8 | 19.4 | 14.6 | 21.0 | 15.7 | 10.3 | 13.56 | 46.9% | 25.9% |
| D | 4,906 | 14.3 | 9.9 | 21.5 | 15.6 | 20.4 | 12.9 | 5.5 | 11.26 | 38.7% | 18.4% |
| F | 8,141 | 10.2 | 8.4 | 16.2 | 14.6 | 23.1 | 19.6 | 7.9 | 15.37 | 50.7% | 27.5% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 14,491 | 17.9 | 11.0 | 21.6 | 15.7 | 15.3 | 9.9 | 8.6 | 9.9 | 33.8% | 18.5% |
| LIMITED | 9,828 | 13.5 | 9.9 | 20.4 | 16.1 | 19.3 | 13.3 | 7.5 | 11.82 | 40.1% | 20.8% |
| POOR | 20,778 | 9.0 | 6.5 | 16.0 | 15.0 | 22.7 | 18.9 | 11.8 | 16.18 | 53.5% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,634 | 23.8 | 17.7 | 33.1 | 15.7 | 6.4 | 2.9 | 0.4 | 5.93 | 9.7% | 3.3% |
| GAME_SPREAD | 6,515 | 22.4 | 15.1 | 32.3 | 17.1 | 9.1 | 3.4 | 0.6 | 6.74 | 13.1% | 4.0% |
| MATCH_WINNER | 32,958 | 15.8 | 10.9 | 22.1 | 15.2 | 18.4 | 12.1 | 5.5 | 10.29 | 36.1% | 17.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 15,940 | 27.8 | 16.8 | 30.6 | 12.8 | 9.3 | 2.5 | 0.3 | 5.64 | 12.1% | 2.8% |
| TOTAL_GAMES | 10,899 | 9.9 | 10.8 | 35.3 | 26.1 | 10.6 | 4.3 | 3.0 | 9.23 | 17.9% | 7.3% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,888 | 24.5 | 28.8 | 33.2 | 8.2 | 4.0 | 1.1 | 0.3 | 4.79 | 5.3% | 1.4% |
| GAME_SPREAD | 9,038 | 46.8 | 16.1 | 24.8 | 7.5 | 2.3 | 1.9 | 0.6 | 3.31 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,207 | 6.6 | 9.8 | 40.1 | 30.3 | 7.4 | 3.4 | 2.4 | 9.23 | 13.2% | 5.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,923 | 23.9 | 16.6 | 34.8 | 14.7 | 6.9 | 2.6 | 0.5 | 6.05 | 10.1% | 3.1% |
| GAME_SPREAD | 9,047 | 20.5 | 13.5 | 28.2 | 20.1 | 12.1 | 4.5 | 1.2 | 7.64 | 17.7% | 5.7% |
| TOTAL_GAMES | 16,246 | 10.1 | 10.7 | 36.1 | 24.4 | 11.5 | 4.5 | 2.6 | 9.08 | 18.7% | 7.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 45,097 | 44.2% | 24.6% | 13.01 | 35.4% | 15.2% | 10.71 |
| gen1_elo | 45,097 | 43.9% | 24.4% | 12.77 | 34.9% | 15.0% | 10.5 |
| gen1_sr | 45,097 | 51.9% | 31.3% | 15.77 | 44.0% | 21.8% | 13.0 |
| gen2 | 45,097 | 50.9% | 31.4% | 15.4 | 43.9% | 23.2% | 12.86 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 19,823 | 15.5 | 10.5 | 21.3 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 25,274 | 10.7 | 7.3 | 16.7 | 14.0 | 19.2 | 17.0 | 15.0 | 15.5 | 51.2% | 32.0% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 26,426 | 16.4 | 11.2 | 22.7 | 15.3 | 17.9 | 11.6 | 4.9 | 9.9 | 34.4% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 78,055 | 26426 | 23295 | 28334 | 24.7 | 120.3 | 1451.1 |
| ge_15pp | 31,844 | 9090 | 8296 | 14458 | 27.9 | 428.1 | 1451.1 |
| ge_25pp | 16,935 | 4359 | 3617 | 8959 | 32.8 | 579.9 | 1431.1 |
| lt_10pp | 34,245 | 13304 | 11022 | 9919 | 22.7 | 47.4 | 1421.1 |

Current slate `SL-20261104T210347Z-bc1d89ce`: 451 priced rows, quote age at build {'median': 13.2, 'max': 13.3}, freshness {'AGING': 451}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 49 | 0.0 | 0.0 | 36.7 | 6.1 | 32.6 | 20.4 | 4.1 | 18.34 | 57.1% | 24.5% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,457 | 19.2 | 10.9 | 25.6 | 17.9 | 18.0 | 7.5 | 0.9 | 8.82 | 26.5% | 8.4% |
| KALSHI_LONE_OUTLIER | 27 | 3.7 | 3.7 | 77.8 | 7.4 | 3.7 | 3.7 | 0.0 | 6.42 | 7.4% | 3.7% |
| MARKETS_AGREE | 915 | 65.9 | 34.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.2 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,981 | 0.0 | 2.3 | 36.9 | 26.4 | 24.3 | 9.2 | 0.9 | 11.86 | 34.4% | 10.1% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 45,097 | 7458 (16.5%) | 26.6% | 1.0% | {"EXTERNAL_STALE": 4457, "AGREES_WITH_KALSHI": 1981, "ALL_AGREE": 915, "SUPPORTS_MODEL_DIRECTION": 48, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 27, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 19,955 | 1892 (9.5%) | 36.0% | 1.6% | {"EXTERNAL_STALE": 1180, "AGREES_WITH_KALSHI": 682, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 11,114 | 589 (5.3%) | 34.0% | 2.2% | {"EXTERNAL_STALE": 376, "AGREES_WITH_KALSHI": 200, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,303 | 559 (10.5%) | 34.5% | 2.3% | {"EXTERNAL_STALE": 353, "AGREES_WITH_KALSHI": 193, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 18,172 | 4242 (23.3%) | 18.3% | 0.9% | {"EXTERNAL_STALE": 2480, "ALL_AGREE": 915, "AGREES_WITH_KALSHI": 777, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 23, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 8,791 | 10.4 | 7.8 | 19.4 | 14.8 | 21.6 | 16.1 | 9.9 | 14.02 | 47.6% | 26.0% |
| 4-10x | 6,019 | 11.2 | 8.5 | 18.5 | 15.3 | 22.1 | 14.2 | 10.1 | 13.74 | 46.4% | 24.3% |
| <2x | 23,088 | 14.9 | 9.9 | 19.7 | 16.1 | 17.5 | 13.1 | 8.8 | 11.54 | 39.4% | 21.9% |
| >=10x | 7,199 | 10.4 | 6.3 | 15.0 | 14.4 | 21.7 | 19.1 | 13.1 | 16.43 | 53.8% | 32.2% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 11,760 | 12.5 | 8.7 | 19.9 | 16.2 | 19.1 | 13.4 | 10.2 | 12.66 | 42.7% | 23.6% |
| 300-1000 | 9,720 | 11.8 | 8.8 | 17.7 | 15.4 | 20.7 | 16.2 | 9.4 | 13.64 | 46.3% | 25.6% |
| <300 | 14,235 | 8.3 | 5.8 | 15.1 | 14.7 | 23.1 | 20.0 | 13.1 | 17.15 | 56.1% | 33.1% |
| >=3000 | 9,382 | 21.3 | 13.0 | 24.0 | 15.7 | 13.9 | 7.1 | 5.0 | 7.71 | 26.0% | 12.1% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1353 | 0.5485 | 0.4095 | 0.49 | +0.059 | -0.081 | 0.0003 ± 0.0042 |
| ratio 4-10x | 922 | 0.5794 | 0.433 | 0.4892 | +0.090 | -0.056 | 0.0091 ± 0.0053 |
| ratio <2x | 3302 | 0.5374 | 0.4144 | 0.4394 | +0.098 | -0.025 | 0.0138 ± 0.0025 |
| ratio >=10x | 1134 | 0.5655 | 0.3913 | 0.4427 | +0.123 | -0.051 | 0.0159 ± 0.0053 |
| thinner_sample 1000-3000 | 1858 | 0.5395 | 0.4127 | 0.4505 | +0.089 | -0.038 | 0.0099 ± 0.0034 |
| thinner_sample 300-1000 | 1520 | 0.5654 | 0.4246 | 0.4789 | +0.086 | -0.054 | 0.0038 ± 0.004 |
| thinner_sample <300 | 2197 | 0.5587 | 0.3899 | 0.4511 | +0.108 | -0.061 | 0.0141 ± 0.0038 |
| thinner_sample >=3000 | 1136 | 0.5304 | 0.4373 | 0.4498 | +0.081 | -0.013 | 0.0151 ± 0.0034 |
| data_status ADEQUATE | 1859 | 0.5323 | 0.4297 | 0.4416 | +0.091 | -0.012 | 0.0148 ± 0.0028 |
| data_status LIMITED | 1628 | 0.5486 | 0.4156 | 0.4711 | +0.077 | -0.056 | 0.0058 ± 0.0037 |
| data_status POOR | 3224 | 0.5612 | 0.4001 | 0.4587 | +0.102 | -0.059 | 0.0109 ± 0.003 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 972 | 0.1983 | 0.1988 | -0.0005 ± 0.0005 | 0.5766 | 0.5776 | 0.5018 | 0.4867 | 0.5021 | -0.094 ± 0.0152 | -0.0087 (8) |
| 3-5 | 615 | 0.2033 | 0.2027 | +0.0006 ± 0.0015 | 0.5894 | 0.5859 | 0.5062 | 0.4663 | 0.478 | -0.104 ± 0.0186 | 0.01 (2) |
| 5-10 | 1435 | 0.2009 | 0.2001 | +0.0009 ± 0.0018 | 0.5874 | 0.583 | 0.5121 | 0.4383 | 0.4669 | -0.091 ± 0.0123 | -0.0143 (7) |
| 10-15 | 1171 | 0.2191 | 0.2099 | +0.0092 ± 0.0033 | 0.6306 | 0.6036 | 0.5252 | 0.4017 | 0.4253 | -0.107 ± 0.0136 | -0.048 (5) |
| 15-25 | 1481 | 0.2243 | 0.2076 | +0.0167 ± 0.0046 | 0.6434 | 0.5983 | 0.5758 | 0.3807 | 0.4355 | -0.105 ± 0.0119 | -0.004 (10) |
| 25-40 | 854 | 0.2206 | 0.2042 | +0.0164 ± 0.0092 | 0.6299 | 0.5891 | 0.6516 | 0.3418 | 0.4707 | -0.068 ± 0.0141 | -0.06 (2) |
| 40+ | 183 | 0.2938 | 0.1766 | +0.1172 ± 0.0278 | 0.7927 | 0.5263 | 0.7308 | 0.2757 | 0.3825 | -0.080 ± 0.0271 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5127 | 0.1856 | 0.1865 | -0.0008 ± 0.0002 | 0.5467 | 0.5476 | 0.4878 | 0.4726 | 0.5024 | -0.023 ± 0.0061 | -0.01 (28) |
| 3-5 | 3426 | 0.1961 | 0.1945 | +0.0016 ± 0.0006 | 0.5711 | 0.565 | 0.4812 | 0.4414 | 0.4405 | -0.055 ± 0.0076 | 0.0 (3) |
| 5-10 | 7407 | 0.2008 | 0.1975 | +0.0033 ± 0.0008 | 0.5868 | 0.5756 | 0.4853 | 0.4117 | 0.4264 | -0.044 ± 0.0052 | -0.0114 (22) |
| 10-15 | 6150 | 0.2018 | 0.186 | +0.0158 ± 0.0014 | 0.5902 | 0.546 | 0.4856 | 0.3618 | 0.36 | -0.064 ± 0.0055 | -0.0281 (16) |
| 15-25 | 7703 | 0.2057 | 0.1665 | +0.0392 ± 0.0018 | 0.6033 | 0.4949 | 0.4993 | 0.3038 | 0.3017 | -0.071 ± 0.0046 | -0.0027 (45) |
| 25-40 | 5963 | 0.2223 | 0.1259 | +0.0963 ± 0.0029 | 0.6387 | 0.3871 | 0.5265 | 0.2128 | 0.2207 | -0.058 ± 0.0045 | -0.0733 (3) |
| 40+ | 3968 | 0.3814 | 0.0449 | +0.3364 ± 0.0038 | 0.9933 | 0.1733 | 0.6307 | 0.1027 | 0.06 | -0.076 ± 0.0032 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 779 | 0.206 | 0.2064 | -0.0004 ± 0.0006 | 0.5931 | 0.5944 | 0.5057 | 0.491 | 0.516 | -0.102 ± 0.0176 | -0.0117 (6) |
| 3-5 | 551 | 0.2115 | 0.2086 | +0.0030 ± 0.0016 | 0.606 | 0.5997 | 0.5131 | 0.4735 | 0.4519 | -0.132 ± 0.0209 | 0.01 (2) |
| 5-10 | 1233 | 0.2053 | 0.2028 | +0.0024 ± 0.0019 | 0.5962 | 0.5886 | 0.5408 | 0.4662 | 0.4907 | -0.094 ± 0.0132 | -0.01 (4) |
| 10-15 | 1078 | 0.2115 | 0.2058 | +0.0057 ± 0.0035 | 0.6139 | 0.597 | 0.5629 | 0.4387 | 0.4814 | -0.100 ± 0.0144 | -0.04 (5) |
| 15-25 | 1568 | 0.2306 | 0.2119 | +0.0187 ± 0.0045 | 0.6557 | 0.608 | 0.5851 | 0.3898 | 0.4413 | -0.099 ± 0.0119 | -0.012 (10) |
| 25-40 | 1100 | 0.267 | 0.1982 | +0.0688 ± 0.0084 | 0.7451 | 0.5765 | 0.6589 | 0.3447 | 0.3945 | -0.122 ± 0.0134 | -0.008 (5) |
| 40+ | 402 | 0.369 | 0.164 | +0.2050 ± 0.0202 | 1.004 | 0.4946 | 0.7355 | 0.246 | 0.296 | -0.081 ± 0.0194 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4411 | 0.1927 | 0.193 | -0.0003 ± 0.0002 | 0.5612 | 0.5616 | 0.5083 | 0.4933 | 0.5112 | -0.038 ± 0.0068 | -0.0154 (26) |
| 3-5 | 3006 | 0.1927 | 0.1917 | +0.0009 ± 0.0006 | 0.5618 | 0.5586 | 0.5096 | 0.4699 | 0.477 | -0.045 ± 0.0082 | 0.01 (2) |
| 5-10 | 6609 | 0.1968 | 0.1931 | +0.0037 ± 0.0008 | 0.5777 | 0.5646 | 0.5082 | 0.4341 | 0.4492 | -0.042 ± 0.0055 | -0.0117 (6) |
| 10-15 | 5519 | 0.2014 | 0.1905 | +0.0109 ± 0.0015 | 0.5919 | 0.5579 | 0.5118 | 0.3879 | 0.4068 | -0.047 ± 0.006 | -0.0189 (18) |
| 15-25 | 7699 | 0.2167 | 0.1806 | +0.0362 ± 0.0019 | 0.6301 | 0.5296 | 0.5239 | 0.3287 | 0.3367 | -0.062 ± 0.0049 | -0.0084 (43) |
| 25-40 | 7015 | 0.2504 | 0.1373 | +0.1131 ± 0.0028 | 0.7067 | 0.4195 | 0.5595 | 0.2426 | 0.2259 | -0.081 ± 0.0044 | -0.0095 (20) |
| 40+ | 5485 | 0.4 | 0.06 | +0.3400 ± 0.0038 | 1.0541 | 0.2152 | 0.654 | 0.1191 | 0.0824 | -0.073 ± 0.0032 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 940 | 0.1971 | 0.1987 | -0.0016 ± 0.0005 | 0.574 | 0.5779 | 0.5014 | 0.486 | 0.5351 | -0.049 ± 0.0152 | -0.012 (10) |
| 3-5 | 662 | 0.2048 | 0.2034 | +0.0014 ± 0.0014 | 0.5934 | 0.588 | 0.4961 | 0.4565 | 0.4607 | -0.111 ± 0.0184 | -0.0 (4) |
| 5-10 | 1466 | 0.2022 | 0.1986 | +0.0036 ± 0.0017 | 0.5891 | 0.5788 | 0.5124 | 0.4387 | 0.4495 | -0.106 ± 0.012 | -0.01 (9) |
| 10-15 | 1182 | 0.2111 | 0.2025 | +0.0086 ± 0.0032 | 0.6131 | 0.5878 | 0.539 | 0.4159 | 0.4442 | -0.108 ± 0.0131 | -0.0286 (7) |
| 15-25 | 1415 | 0.2306 | 0.2119 | +0.0187 ± 0.0048 | 0.6587 | 0.6075 | 0.5869 | 0.3926 | 0.441 | -0.112 ± 0.0122 | -0.03 (1) |
| 25-40 | 854 | 0.2116 | 0.2095 | +0.0021 ± 0.0092 | 0.6109 | 0.6015 | 0.6603 | 0.3495 | 0.5 | -0.055 ± 0.0141 | -0.0267 (3) |
| 40+ | 192 | 0.3122 | 0.1808 | +0.1314 ± 0.0276 | 0.8441 | 0.5354 | 0.7417 | 0.2868 | 0.3802 | -0.093 ± 0.0282 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4930 | 0.1844 | 0.1851 | -0.0007 ± 0.0002 | 0.5432 | 0.5442 | 0.4831 | 0.4677 | 0.4868 | -0.032 ± 0.0062 | -0.0137 (41) |
| 3-5 | 3488 | 0.2043 | 0.2027 | +0.0016 ± 0.0006 | 0.5924 | 0.5867 | 0.48 | 0.4405 | 0.4412 | -0.054 ± 0.0078 | -0.01 (19) |
| 5-10 | 7579 | 0.1956 | 0.1905 | +0.0051 ± 0.0008 | 0.5741 | 0.5581 | 0.4878 | 0.4138 | 0.4165 | -0.055 ± 0.0051 | -0.0105 (37) |
| 10-15 | 6073 | 0.1935 | 0.1787 | +0.0149 ± 0.0013 | 0.5718 | 0.5289 | 0.4951 | 0.3719 | 0.3728 | -0.062 ± 0.0054 | -0.0146 (13) |
| 15-25 | 7810 | 0.2115 | 0.1715 | +0.0400 ± 0.0018 | 0.617 | 0.5062 | 0.5129 | 0.3184 | 0.3138 | -0.073 ± 0.0047 | -0.0533 (3) |
| 25-40 | 5946 | 0.217 | 0.1274 | +0.0896 ± 0.0029 | 0.6274 | 0.3903 | 0.5298 | 0.2142 | 0.2324 | -0.049 ± 0.0045 | -0.02 (4) |
| 40+ | 3918 | 0.3915 | 0.0499 | +0.3416 ± 0.004 | 1.0205 | 0.1859 | 0.6404 | 0.1088 | 0.0664 | -0.076 ± 0.0034 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1372 | 0.1965 | 0.1966 | -0.0001 ± 0.0004 | 0.571 | 0.5711 | 0.5072 | 0.4922 | 0.4971 | -0.068 ± 0.0122 | -0.0213 (54) |
| 3-5 | 980 | 0.1886 | 0.1884 | +0.0002 ± 0.0011 | 0.5549 | 0.5528 | 0.4948 | 0.4549 | 0.4704 | -0.059 ± 0.0142 | -0.0194 (34) |
| 5-10 | 1977 | 0.1986 | 0.194 | +0.0046 ± 0.0015 | 0.5847 | 0.57 | 0.507 | 0.4334 | 0.439 | -0.076 ± 0.0101 | -0.005 (78) |
| 10-15 | 1359 | 0.2147 | 0.2016 | +0.0131 ± 0.003 | 0.6217 | 0.5866 | 0.5402 | 0.4174 | 0.4238 | -0.092 ± 0.0125 | 0.0014 (65) |
| 15-25 | 1772 | 0.2306 | 0.2069 | +0.0237 ± 0.0043 | 0.6582 | 0.5976 | 0.589 | 0.3941 | 0.4334 | -0.089 ± 0.0109 | -0.0214 (59) |
| 25-40 | 1076 | 0.2403 | 0.2097 | +0.0306 ± 0.0085 | 0.6868 | 0.6022 | 0.6862 | 0.3739 | 0.4814 | -0.088 ± 0.0131 | -0.0252 (27) |
| 40+ | 379 | 0.3296 | 0.2018 | +0.1277 ± 0.0221 | 0.9513 | 0.5875 | 0.8153 | 0.338 | 0.4591 | -0.098 ± 0.0208 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5034 | 0.1774 | 0.1776 | -0.0002 ± 0.0002 | 0.5244 | 0.5244 | 0.5118 | 0.4965 | 0.5079 | -0.037 ± 0.006 | -0.0145 (98) |
| 3-5 | 3472 | 0.1943 | 0.1934 | +0.0009 ± 0.0006 | 0.5664 | 0.5643 | 0.5014 | 0.4616 | 0.4709 | -0.041 ± 0.0076 | -0.0204 (72) |
| 5-10 | 7018 | 0.1958 | 0.1892 | +0.0066 ± 0.0008 | 0.5769 | 0.5579 | 0.5006 | 0.427 | 0.4205 | -0.063 ± 0.0052 | -0.0084 (134) |
| 10-15 | 4847 | 0.2096 | 0.1932 | +0.0164 ± 0.0016 | 0.6094 | 0.5669 | 0.5367 | 0.4138 | 0.4071 | -0.073 ± 0.0064 | -0.0053 (106) |
| 15-25 | 5861 | 0.2302 | 0.1992 | +0.0309 ± 0.0023 | 0.6616 | 0.5776 | 0.5747 | 0.3793 | 0.3991 | -0.067 ± 0.0059 | -0.026 (108) |
| 25-40 | 3899 | 0.2572 | 0.1889 | +0.0683 ± 0.0044 | 0.7282 | 0.5509 | 0.6377 | 0.325 | 0.375 | -0.069 ± 0.0068 | -0.0246 (52) |
| 40+ | 1709 | 0.3728 | 0.1582 | +0.2146 ± 0.01 | 1.0532 | 0.4716 | 0.7432 | 0.2416 | 0.2891 | -0.067 ± 0.0092 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 6711 | 1.041 ± 0.034 | 1.113 | 0.1692 | 0.1685 | 0.2141 | 0.2034 |
| gen2 | 6711 | 0.833 ± 0.031 | 1.084 | 0.1734 | 0.1688 | 0.2327 | 0.2032 |
| gen1_elo | 6711 | 1.013 ± 0.033 | 1.103 | 0.1758 | 0.1686 | 0.2137 | 0.2034 |
| gen1_sr | 6711 | 1.018 ± 0.041 | 1.147 | 0.1333 | 0.1705 | 0.2289 | 0.2029 |
| gen1_ledger | 8915 | 0.872 ± 0.025 | 1.081 | 0.1895 | 0.1764 | 0.2166 | 0.1997 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 31,844)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 7,301 | 22.9% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,088 | 22.3% |
| BOOK_QUALITY | execution | 5,840 | 18.3% |
| POOR_DATA | data | 3,728 | 11.7% |
| LIMITED_DATA | data | 1,986 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,818 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,336 | 4.2% |
| IDENTITY_AMBIGUOUS | mapping | 1,306 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 910 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 530 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 22.9%, coverage 22.3%, execution 18.3%, data 17.9%, market_freshness/coverage 8.6%, model_calibration_or_unknown 4.2%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.4%, LOW_DATA_QUALITY 71.6%, THIN_PLAYER_HISTORY 60.0%, STALE_PLAYER_DATA 52.1%, STALE_KALSHI_QUOTE 45.4%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 24.5%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 15.4%, LEVEL_TRANSFER_RISK 10.1%, LOW_DISPLAYED_LIQUIDITY 8.3%, EVENT_MAPPING_RISK 7.3%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.7%, POST_SETTLEMENT_OBSERVATION 22.3%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 16,935)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,695 | 33.6% |
| STALE_QUOTE | market_freshness | 3,285 | 19.4% |
| BOOK_QUALITY | execution | 3,036 | 17.9% |
| POOR_DATA | data | 1,596 | 9.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 972 | 5.7% |
| IDENTITY_AMBIGUOUS | mapping | 718 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 600 | 3.5% |
| LIMITED_DATA | data | 574 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 327 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 131 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.6%, market_freshness 19.4%, execution 17.9%, data 12.8%, market_freshness/coverage 9.3%, mapping 4.2%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 96.9%, LOW_DATA_QUALITY 75.1%, THIN_PLAYER_HISTORY 62.2%, STALE_KALSHI_QUOTE 52.9%, STALE_PLAYER_DATA 46.2%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 24.0%, MODEL_HIGH_UNCERTAINTY 19.2%, PLAYER_IDENTITY_RISK 18.4%, LEVEL_TRANSFER_RISK 9.0%, EVENT_MAPPING_RISK 8.9%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.7%, POST_SETTLEMENT_OBSERVATION 33.6%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 13490, "IDENTITY_AMBIGUOUS": 3445}; ticker orientation: {"VERIFIED": 16935}.

Checks: discipline:AMBIGUOUS 1133, discipline:PASS 15802, identity_confidence:AMBIGUOUS 3121, identity_confidence:PASS 13814, level_mapping:NA 1145, level_mapping:PASS 15790, market_pair:AMBIGUOUS 485, market_pair:NA 372, market_pair:PASS 16078, model_complement:NA 334, model_complement:PASS 16601, namesake:AMBIGUOUS 6, namesake:PASS 16929, physical_match_id:NA 5821, physical_match_id:PASS 11114, player_ids:PASS 16935, same_pair_other_event:PASS 16935, ticker_orientation:PASS 16935

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,189 | 3.8% | 3.3% | 1.4% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 21, "market_freshness/coverage": 17} | 5.55 | 0.2277 / 0.2221 (773) | 24.3% | 2.5% | 3.1% | 2.8% |
| CHALLENGER | 11,156 | 16.3% | 6.2% | 10.7% | {"coverage": 1064, "market_freshness/coverage": 214, "market_freshness": 211, "data": 157, "model_calibration_or_unknown": 77, "execution": 41, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.39 | 0.2204 / 0.2101 (2602) | 37.4% | 15.7% | 4.1% | 22.4% |
| DOUBLES | 2,415 | 46.9% | 46.8% | 6.7% | {"execution": 647, "mapping": 309, "market_freshness": 106, "market_freshness/coverage": 64, "coverage": 7} | 23.54 | 0.3019 / 0.2358 (584) | 9.7% | 0.0% | 100.0% | 6.0% |
| ITF_MEN | 21,985 | 25.0% | 17.6% | 32.5% | {"coverage": 1900, "market_freshness": 1052, "execution": 968, "data": 823, "market_freshness/coverage": 551, "mapping": 202, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.76 | 0.2154 / 0.1973 (4617) | 39.1% | 69.3% | 15.7% | 21.3% |
| ITF_WOMEN | 28,928 | 26.5% | 19.1% | 45.2% | {"coverage": 2648, "market_freshness": 1661, "execution": 1297, "data": 1091, "market_freshness/coverage": 669, "mapping": 184, "model_calibration_or_unknown": 88, "model_calibration": 22} | 12.55 | 0.2021 / 0.1926 (5508) | 40.4% | 57.3% | 9.9% | 21.4% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,682 | 6.1% | 5.2% | 1.7% | {"market_freshness": 108, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 21, "market_freshness/coverage": 13, "mapping": 1} | 7.7 | 0.2316 / 0.2233 (752) | 29.4% | 2.1% | 1.3% | 3.6% |
| WTA125 | 2,545 | 11.2% | 9.7% | 1.7% | {"market_freshness": 88, "model_calibration_or_unknown": 54, "market_freshness/coverage": 43, "data": 39, "execution": 24, "model_calibration": 19, "coverage": 14, "mapping": 4} | 9.17 | 0.207 / 0.1909 (748) | 28.7% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 16.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 969 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 3 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 4 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 5 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 6 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 773 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 7 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 8 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 20.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 1252 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
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
| 22 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 23 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 24 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 25 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 26 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 27 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 28 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 29 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 30 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 31 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 271 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 32 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 33 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 34 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 35 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 36 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 37 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 38 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 39 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 768 min (STALE); no external reference |
| 40 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 41 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 42 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 43 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 44 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 77 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 45 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 46 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.3h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 748 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |
| 47 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXATPCHALLENGERMATCH-26NOV02TOBSTO-TOB` | CHALLENGER | fair_v1 | 80% / 2% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 165 min (STALE); data POOR (grade F, thinner serve sample 159.0, ratio 20.58); no external reference |
| 49 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 50 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.969, "by_level_share_of_ge_25pp": {"ATP": 0.014, "CHALLENGER": 0.1073, "DOUBLES": 0.0669, "ITF_MEN": 0.325, "ITF_WOMEN": 0.4523, "OTHER": 0.0007, "WTA": 0.0169, "WTA125": 0.0168}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.529, "share_primary_cause_market_settled_or_in_play": 0.4291, "share_primary_cause_stale_quote_only": 0.194}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 16935, "identity_ambiguous_share": 0.2034, "ticker_orientation": {"VERIFIED": 16935}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 11114, "with_external": 589, "coverage": 0.053, "external_status": {"EXTERNAL_STALE": 376, "AGREES_WITH_KALSHI": 200, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 376, "MODEL_LONE_OUTLIER": 200, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3396, "share_external_supports_model": 0.0221}, "pregame_clean_ge_25pp": {"n": 5303, "with_external": 559, "coverage": 0.1054, "external_status": {"EXTERNAL_STALE": 353, "AGREES_WITH_KALSHI": 193, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 353, "MODEL_LONE_OUTLIER": 193, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3453, "share_external_supports_model": 0.0233}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 477.0, "median_sample_ratio": 2.47, "median_min_matches": 18.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2099, "data_status": {"POOR": 9568, "LIMITED": 4370, "ADEQUATE": 2997}, "comparison_lt_10pp": {"median_thinner_serve_points": 1725.0, "median_sample_ratio": 1.7, "median_min_matches": 90.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1353, "model_minus_observed": 0.0585, "kalshi_minus_observed": -0.0805, "brier_diff_model_minus_kalshi": 0.0003}, "4-10x": {"n": 922, "model_minus_observed": 0.0903, "kalshi_minus_observed": -0.0562, "brier_diff_model_minus_kalshi": 0.0091}, "<2x": {"n": 3302, "model_minus_observed": 0.0979, "kalshi_minus_observed": -0.025, "brier_diff_model_minus_kalshi": 0.0138}, ">=10x": {"n": 1134, "model_minus_observed": 0.1228, "kalshi_minus_observed": -0.0514, "brier_diff_model_minus_kalshi": 0.0159}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 6711, "model": {"intercept": -0.559, "slope": 0.833, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.189, "slope": 1.084, "slope_se": 0.035}, "mean_extremity_model": 0.1734, "mean_extremity_kalshi": 0.1688, "model_brier": 0.2327, "kalshi_brier": 0.2032, "brier_diff_model_minus_kalshi": 0.0295, "brier_diff_se": 0.0023, "model_logloss": 0.6622, "kalshi_logloss": 0.5885}, "fair_v1": {"n": 6711, "model": {"intercept": -0.45, "slope": 1.041, "slope_se": 0.034}, "kalshi_mid_same_rows": {"intercept": 0.257, "slope": 1.113, "slope_se": 0.035}, "mean_extremity_model": 0.1692, "mean_extremity_kalshi": 0.1685, "model_brier": 0.2141, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": 0.0108, "brier_diff_se": 0.0019, "model_logloss": 0.6169, "kalshi_logloss": 0.5887}, "gen1_elo": {"n": 6711, "model": {"intercept": -0.437, "slope": 1.013, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.26, "slope": 1.103, "slope_se": 0.035}, "mean_extremity_model": 0.1758, "mean_extremity_kalshi": 0.1686, "model_brier": 0.2137, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": 0.0102, "brier_diff_se": 0.0019, "model_logloss": 0.6164, "kalshi_logloss": 0.5889}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2464, "share_ge_15": 0.4425, "median_abs_gap": 13.01, "n": 45097}, "gen1_elo": {"share_ge_25": 0.244, "share_ge_15": 0.4389, "median_abs_gap": 12.77, "n": 45097}, "gen1_sr": {"share_ge_25": 0.3127, "share_ge_15": 0.5192, "median_abs_gap": 15.77, "n": 45097}, "gen2": {"share_ge_25": 0.314, "share_ge_15": 0.5088, "median_abs_gap": 15.4, "n": 45097}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1517, "share_ge_15": 0.3543, "median_abs_gap": 10.71, "n": 34961}, "gen1_elo": {"share_ge_25": 0.1503, "share_ge_15": 0.3495, "median_abs_gap": 10.5, "n": 34961}, "gen1_sr": {"share_ge_25": 0.2177, "share_ge_15": 0.4399, "median_abs_gap": 13.0, "n": 34963}, "gen2": {"share_ge_25": 0.2325, "share_ge_15": 0.4393, "median_abs_gap": 12.86, "n": 34963}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.55, "share_ge_25_all": 0.0383, "share_ge_25_pregame_clean": 0.0331}, "WTA": {"median_abs_gap_pregame_clean": 7.7, "share_ge_25_all": 0.0613, "share_ge_25_pregame_clean": 0.0519}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2369, "share_within_10pp_all": 0.4387, "share_within_10pp_pregame_clean": 0.4908, "corr_model_vs_mid_pregame_clean": 0.8506}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 972, "model_brier": 0.1983, "kalshi_brier": 0.1988, "brier_diff_model_minus_kalshi": -0.0005}, "10-15": {"n_settled": 1171, "model_brier": 0.2191, "kalshi_brier": 0.2099, "brier_diff_model_minus_kalshi": 0.0092}, "15-25": {"n_settled": 1481, "model_brier": 0.2243, "kalshi_brier": 0.2076, "brier_diff_model_minus_kalshi": 0.0167}, "25-40": {"n_settled": 854, "model_brier": 0.2206, "kalshi_brier": 0.2042, "brier_diff_model_minus_kalshi": 0.0164}, "3-5": {"n_settled": 615, "model_brier": 0.2033, "kalshi_brier": 0.2027, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 183, "model_brier": 0.2938, "kalshi_brier": 0.1766, "brier_diff_model_minus_kalshi": 0.1172}, "5-10": {"n_settled": 1435, "model_brier": 0.2009, "kalshi_brier": 0.2001, "brier_diff_model_minus_kalshi": 0.0009}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.559, "slope": 0.833, "slope_se": 0.031}, "kalshi_slope": {"intercept": 0.189, "slope": 1.084, "slope_se": 0.035}, "n": 6711}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.491, "slope": 0.872, "slope_se": 0.025}, "kalshi_slope": {"intercept": 0.174, "slope": 1.081, "slope_se": 0.029}, "n": 8915}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 584, "model_brier": 0.3019, "kalshi_brier": 0.2358, "brier_diff_model_minus_kalshi": 0.0661, "brier_diff_se": 0.0123, "corr_model_outcome": 0.081, "corr_kalshi_outcome": 0.2542}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
