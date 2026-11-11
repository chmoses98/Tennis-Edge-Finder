# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-11T21:13Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 89,474): 0-3 13.9%, 3-5 9.5%, 5-10 20.1%, 10-15 15.2%, 15-25 19.2%, 25-40 13.8%, 40+ 8.3%; median gap 11.92 pp.
* **Where the extremes live**: 97.3% of >=25 pp gaps are off the ATP/WTA main tour (ITF 78.2%, Challenger 11.1%, doubles 6.4%). Main tour: ATP 3.7% and WTA 5.9% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 19,755): MARKET_ALREADY_SETTLED_WHEN_PRICED 35.1%, STALE_QUOTE 20.2%, BOOK_QUALITY 16.4%, POOR_DATA 9.0%, POSSIBLY_IN_PLAY_QUOTE 5.9%, IDENTITY_AMBIGUOUS 4.2%, IN_PLAY_QUOTE 3.4%, LIMITED_DATA 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 1.7%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 35.1%, market_freshness 20.2%, execution 16.4%, data 12.3%, market_freshness/coverage 9.3%, mapping 4.2%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 55.6% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 44.4% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 19,755 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.9%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.9% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 476.0 points vs 1675.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.019, Gen-2 0.816, Gen-1 ledger 0.866 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 1001 model 0.2253 vs Kalshi 0.2026; n 209 model 0.3057 vs Kalshi 0.1684.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 373,172 model-market comparisons (616,681 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 122,820 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-11T20:49:50.696083+00:00'], shadow board 103,660 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-11T20:49:55.434683+00:00'], Model 4 44,013 rows, 30,755 settled tickers, 11,656 tickers with an external scan.
* By model: {"gen1_ledger": 82248, "gen1_elo": 52093, "fair_v1": 52093, "gen2": 52093, "gen1_sr": 52093, "model4_fundamental": 41318, "model4_conditioned": 41234}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 89,474 | 13.9 | 9.5 | 20.1 | 15.2 | 19.2 | 13.8 | 8.3 | 11.92 | 41.2% | 22.1% |
| MW fair_v1 | 52,093 | 12.6 | 8.6 | 18.7 | 15.2 | 19.6 | 15.0 | 10.3 | 13.17 | 44.9% | 25.4% |
| MW gen1_elo | 52,093 | 12.3 | 8.7 | 19.1 | 15.3 | 19.4 | 15.0 | 10.1 | 13.0 | 44.5% | 25.1% |
| MW gen1_ledger | 37,381 | 15.8 | 10.8 | 22.2 | 15.1 | 18.6 | 11.9 | 5.6 | 10.29 | 36.1% | 17.5% |
| MW gen1_sr | 52,093 | 9.9 | 7.1 | 16.6 | 13.9 | 20.9 | 18.8 | 12.8 | 15.98 | 52.5% | 31.6% |
| MW gen2 | 52,093 | 10.8 | 7.5 | 16.6 | 13.8 | 19.6 | 17.7 | 13.9 | 15.5 | 51.2% | 31.6% |
| all families model4_conditioned | 41,234 | 22.2 | 17.9 | 34.5 | 16.9 | 5.0 | 2.2 | 1.2 | 6.07 | 8.4% | 3.4% |
| all families model4_fundamental | 41,318 | 17.3 | 13.5 | 34.0 | 20.0 | 9.9 | 3.8 | 1.5 | 7.61 | 15.2% | 5.3% |

Configurable thresholds (primary): >=5pp 76.5%, >=10pp 56.4%, >=15pp 41.2%, >=20pp 30.5%, >=25pp 22.1%, >=30pp 16.0%, >=40pp 8.3%, >=50pp 3.9%
Executable gap (model outside the book, before fees): median 8.55pp; >=10pp 45.6%, >=25pp 17.6%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,108 | 28.0 | 15.9 | 28.0 | 13.3 | 10.7 | 3.5 | 0.6 | 5.77 | 14.8% | 4.2% |
| CHALLENGER | 8,223 | 16.4 | 9.6 | 20.5 | 15.2 | 15.8 | 11.4 | 11.1 | 10.94 | 38.3% | 22.5% |
| ITF_MEN | 15,163 | 9.6 | 7.3 | 17.0 | 14.8 | 21.1 | 17.3 | 12.9 | 15.5 | 51.3% | 30.2% |
| ITF_WOMEN | 20,172 | 9.4 | 7.0 | 16.1 | 14.7 | 22.1 | 18.6 | 12.0 | 16.0 | 52.8% | 30.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,094 | 16.6 | 13.3 | 25.0 | 20.6 | 16.6 | 6.7 | 1.1 | 8.6 | 24.4% | 7.8% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,108 | 26.4 | 15.7 | 26.3 | 15.7 | 11.2 | 3.9 | 0.8 | 6.09 | 15.9% | 4.7% |
| CHALLENGER | 8,223 | 14.4 | 9.1 | 19.0 | 13.8 | 18.4 | 13.7 | 11.6 | 12.53 | 43.7% | 25.3% |
| ITF_MEN | 15,163 | 8.1 | 6.1 | 15.0 | 14.0 | 20.2 | 20.0 | 16.5 | 17.91 | 56.8% | 36.6% |
| ITF_WOMEN | 20,172 | 7.8 | 5.9 | 14.1 | 12.7 | 20.7 | 21.1 | 17.6 | 19.11 | 59.5% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,094 | 14.2 | 10.4 | 21.6 | 16.2 | 22.4 | 12.7 | 2.5 | 11.19 | 37.6% | 15.2% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,108 | 23.4 | 14.1 | 25.6 | 15.5 | 14.4 | 6.0 | 1.1 | 7.04 | 21.4% | 7.1% |
| CHALLENGER | 8,223 | 15.0 | 9.6 | 20.8 | 15.6 | 16.1 | 12.0 | 10.9 | 11.3 | 39.0% | 22.9% |
| ITF_MEN | 15,163 | 9.3 | 7.2 | 17.1 | 14.2 | 21.5 | 17.4 | 13.2 | 15.87 | 52.1% | 30.6% |
| ITF_WOMEN | 20,172 | 9.2 | 6.8 | 16.3 | 15.6 | 22.1 | 18.7 | 11.4 | 15.74 | 52.1% | 30.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,094 | 22.5 | 17.2 | 31.8 | 15.3 | 8.9 | 3.3 | 1.0 | 6.12 | 13.2% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,479 | 28.2 | 19.5 | 29.1 | 12.1 | 8.1 | 2.5 | 0.4 | 5.24 | 11.1% | 3.0% |
| CHALLENGER | 4,971 | 22.8 | 14.5 | 28.0 | 14.8 | 13.1 | 5.5 | 1.5 | 7.02 | 20.0% | 7.0% |
| DOUBLES | 2,732 | 4.9 | 4.5 | 13.1 | 10.9 | 20.5 | 24.4 | 21.6 | 23.09 | 66.6% | 46.1% |
| ITF_MEN | 10,984 | 12.7 | 9.5 | 21.4 | 15.6 | 21.8 | 13.0 | 6.1 | 11.86 | 40.8% | 19.1% |
| ITF_WOMEN | 12,993 | 13.5 | 9.3 | 19.8 | 15.7 | 21.6 | 14.6 | 5.5 | 12.19 | 41.7% | 20.1% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,817 | 24.1 | 16.0 | 31.4 | 16.8 | 8.9 | 2.5 | 0.2 | 6.44 | 11.7% | 2.8% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,979 | 28.5 | 16.1 | 28.4 | 13.2 | 10.4 | 3.1 | 0.3 | 5.64 | 13.8% | 3.4% |
| CHALLENGER | 5,783 | 21.1 | 11.9 | 25.7 | 18.0 | 15.8 | 5.6 | 1.9 | 8.21 | 23.3% | 7.5% |
| ITF_MEN | 11,021 | 11.8 | 8.6 | 20.6 | 17.2 | 22.2 | 14.1 | 5.5 | 12.48 | 41.8% | 19.6% |
| ITF_WOMEN | 14,722 | 11.3 | 8.6 | 19.1 | 17.0 | 24.0 | 15.3 | 4.7 | 13.14 | 44.0% | 20.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,980 | 16.9 | 13.4 | 25.3 | 21.0 | 16.6 | 6.2 | 0.6 | 8.43 | 23.4% | 6.8% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,979 | 26.7 | 16.0 | 26.6 | 15.7 | 11.2 | 3.4 | 0.4 | 6.01 | 15.0% | 3.8% |
| CHALLENGER | 5,783 | 18.2 | 11.6 | 23.8 | 16.3 | 18.9 | 9.0 | 2.1 | 8.99 | 30.1% | 11.1% |
| ITF_MEN | 11,022 | 9.6 | 7.2 | 17.6 | 16.1 | 22.1 | 18.2 | 9.1 | 14.84 | 49.5% | 27.3% |
| ITF_WOMEN | 14,723 | 8.9 | 7.0 | 16.0 | 14.3 | 22.5 | 20.6 | 10.7 | 16.51 | 53.8% | 31.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,980 | 14.4 | 10.5 | 21.9 | 16.4 | 22.6 | 12.4 | 1.9 | 11.03 | 36.9% | 14.3% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,409 | 28.5 | 19.7 | 29.1 | 12.3 | 7.8 | 2.3 | 0.3 | 5.2 | 10.4% | 2.7% |
| CHALLENGER | 4,398 | 24.1 | 15.3 | 29.1 | 14.9 | 12.4 | 3.8 | 0.4 | 6.58 | 16.6% | 4.2% |
| DOUBLES | 2,561 | 4.8 | 4.5 | 13.3 | 11.0 | 20.4 | 24.3 | 21.7 | 22.96 | 66.4% | 46.0% |
| ITF_MEN | 9,482 | 13.5 | 10.0 | 22.9 | 16.1 | 21.9 | 11.5 | 4.2 | 11.02 | 37.5% | 15.7% |
| ITF_WOMEN | 11,184 | 14.2 | 9.8 | 20.9 | 16.2 | 21.8 | 13.6 | 3.6 | 11.42 | 38.9% | 17.2% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,754 | 24.4 | 16.4 | 31.4 | 16.8 | 8.9 | 2.0 | 0.1 | 6.42 | 10.9% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,732 | 4.9 | 4.5 | 13.1 | 10.9 | 20.5 | 24.4 | 21.6 | 23.09 | 66.6% | 46.1% |
| singles | 34,649 | 16.6 | 11.3 | 22.9 | 15.4 | 18.5 | 11.0 | 4.3 | 9.77 | 33.7% | 15.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 11,138 | 12.7 | 8.9 | 19.4 | 15.1 | 19.6 | 14.4 | 9.9 | 12.94 | 43.9% | 24.3% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 33,954 | 13.1 | 8.7 | 18.8 | 15.0 | 19.1 | 15.0 | 10.3 | 12.99 | 44.4% | 25.3% |
| UNKNOWN | 6,588 | 10.4 | 7.4 | 17.1 | 16.5 | 21.5 | 15.9 | 11.2 | 14.41 | 48.6% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 14,534 | 19.2 | 11.8 | 22.4 | 15.8 | 14.8 | 9.5 | 6.5 | 9.0 | 30.8% | 16.0% |
| B | 6,235 | 13.0 | 8.6 | 19.6 | 15.3 | 19.7 | 12.4 | 11.5 | 12.74 | 43.6% | 23.9% |
| C | 7,359 | 12.0 | 8.6 | 19.5 | 16.1 | 18.9 | 14.6 | 10.4 | 12.9 | 43.9% | 24.9% |
| D | 8,524 | 11.4 | 8.3 | 17.9 | 15.0 | 21.9 | 15.8 | 9.8 | 14.08 | 47.5% | 25.6% |
| F | 15,441 | 7.3 | 5.7 | 14.9 | 14.3 | 23.0 | 21.1 | 13.7 | 18.06 | 57.8% | 34.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,837 | 25.0 | 15.9 | 28.9 | 14.9 | 10.7 | 3.4 | 1.2 | 6.35 | 15.3% | 4.7% |
| B | 5,091 | 16.7 | 10.9 | 24.2 | 16.9 | 19.0 | 9.4 | 3.0 | 9.6 | 31.3% | 12.4% |
| C | 7,347 | 11.0 | 7.8 | 19.6 | 14.8 | 21.0 | 15.5 | 10.1 | 13.46 | 46.6% | 25.6% |
| D | 5,683 | 14.5 | 10.0 | 21.1 | 15.3 | 20.9 | 12.7 | 5.5 | 11.32 | 39.1% | 18.2% |
| F | 9,423 | 10.2 | 8.3 | 16.6 | 14.5 | 23.5 | 19.0 | 8.0 | 15.24 | 50.4% | 27.0% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 16,482 | 17.7 | 10.9 | 21.4 | 15.5 | 15.1 | 10.2 | 9.2 | 10.0 | 34.5% | 19.4% |
| LIMITED | 11,249 | 13.5 | 9.4 | 20.5 | 16.0 | 19.6 | 13.3 | 7.6 | 11.91 | 40.6% | 20.9% |
| POOR | 24,362 | 8.8 | 6.6 | 16.0 | 14.6 | 22.6 | 19.1 | 12.3 | 16.39 | 54.0% | 31.4% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,266 | 23.7 | 18.0 | 33.0 | 15.4 | 6.4 | 3.0 | 0.4 | 5.9 | 9.8% | 3.4% |
| GAME_SPREAD | 6,929 | 22.8 | 15.3 | 32.1 | 16.7 | 9.1 | 3.3 | 0.7 | 6.69 | 13.1% | 4.0% |
| MATCH_WINNER | 37,381 | 15.8 | 10.8 | 22.2 | 15.1 | 18.6 | 11.9 | 5.6 | 10.29 | 36.1% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 17,047 | 28.4 | 16.8 | 30.6 | 12.7 | 8.8 | 2.3 | 0.3 | 5.58 | 11.5% | 2.6% |
| TOTAL_GAMES | 11,601 | 9.8 | 10.8 | 36.2 | 25.7 | 10.4 | 4.2 | 2.9 | 9.14 | 17.5% | 7.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,666 | 24.5 | 28.7 | 33.3 | 8.1 | 4.0 | 1.2 | 0.3 | 4.8 | 5.4% | 1.5% |
| GAME_SPREAD | 9,539 | 46.7 | 15.9 | 25.2 | 7.4 | 2.4 | 1.9 | 0.6 | 3.33 | 4.9% | 2.5% |
| TOTAL_GAMES | 17,029 | 6.6 | 9.8 | 40.8 | 29.9 | 7.3 | 3.3 | 2.4 | 9.16 | 13.0% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,702 | 23.8 | 16.6 | 34.6 | 14.8 | 6.9 | 2.7 | 0.5 | 6.05 | 10.1% | 3.2% |
| GAME_SPREAD | 9,548 | 20.3 | 13.4 | 28.4 | 20.2 | 12.1 | 4.4 | 1.1 | 7.7 | 17.6% | 5.5% |
| TOTAL_GAMES | 17,068 | 10.0 | 10.8 | 36.5 | 24.3 | 11.3 | 4.4 | 2.6 | 9.02 | 18.3% | 7.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 52,093 | 44.9% | 25.4% | 13.17 | 35.5% | 15.2% | 10.71 |
| gen1_elo | 52,093 | 44.5% | 25.1% | 13.0 | 35.0% | 15.0% | 10.51 |
| gen1_sr | 52,093 | 52.5% | 31.6% | 15.98 | 44.0% | 21.6% | 13.0 |
| gen2 | 52,093 | 51.2% | 31.6% | 15.5 | 43.9% | 23.1% | 12.84 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,229 | 15.5 | 10.5 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 31,864 | 10.8 | 7.4 | 17.0 | 13.9 | 19.3 | 17.0 | 14.7 | 15.39 | 51.0% | 31.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 30,849 | 16.3 | 11.1 | 22.7 | 15.2 | 18.2 | 11.5 | 5.0 | 9.96 | 34.7% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 89,474 | 30849 | 23701 | 34924 | 25.2 | 143.0 | 1451.1 |
| ge_15pp | 36,904 | 10704 | 8447 | 17753 | 29.1 | 448.0 | 1451.1 |
| ge_25pp | 19,755 | 5083 | 3694 | 10978 | 34.6 | 594.9 | 1431.1 |
| lt_10pp | 39,004 | 15462 | 11206 | 12336 | 22.8 | 49.6 | 1421.7 |

Current slate `SL-20261111T211314Z-7436dbae`: 418 priced rows, quote age at build {'median': 56.3, 'max': 96.2}, freshness {'STALE': 418}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 52 | 0.0 | 0.0 | 34.6 | 9.6 | 32.7 | 19.2 | 3.9 | 18.34 | 55.8% | 23.1% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 5,029 | 19.1 | 11.1 | 25.6 | 18.2 | 17.8 | 7.2 | 1.0 | 8.78 | 25.9% | 8.1% |
| KALSHI_LONE_OUTLIER | 32 | 6.2 | 6.2 | 75.0 | 6.2 | 3.1 | 3.1 | 0.0 | 6.16 | 6.2% | 3.1% |
| MARKETS_AGREE | 1,077 | 66.4 | 33.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,293 | 0.0 | 2.2 | 38.5 | 25.9 | 23.7 | 8.8 | 0.9 | 11.65 | 33.5% | 9.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 52,093 | 8512 (16.3%) | 26.9% | 1.0% | {"EXTERNAL_STALE": 5029, "AGREES_WITH_KALSHI": 2293, "ALL_AGREE": 1077, "SUPPORTS_MODEL_DIRECTION": 50, "AGREES_WITH_MODEL": 32, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 23,401 | 2100 (9.0%) | 36.5% | 1.5% | {"EXTERNAL_STALE": 1302, "AGREES_WITH_KALSHI": 767, "SUPPORTS_MODEL_DIRECTION": 29, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 13,210 | 645 (4.9%) | 34.6% | 2.0% | {"EXTERNAL_STALE": 409, "AGREES_WITH_KALSHI": 223, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 6,048 | 613 (10.1%) | 35.2% | 2.1% | {"EXTERNAL_STALE": 384, "AGREES_WITH_KALSHI": 216, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 20,773 | 4894 (23.6%) | 19.1% | 0.9% | {"EXTERNAL_STALE": 2809, "ALL_AGREE": 1077, "AGREES_WITH_KALSHI": 933, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 28, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 10,215 | 10.7 | 7.5 | 19.1 | 14.3 | 21.7 | 16.5 | 10.2 | 14.38 | 48.5% | 26.8% |
| 4-10x | 7,017 | 11.1 | 8.7 | 17.8 | 14.8 | 21.7 | 14.8 | 11.2 | 14.12 | 47.7% | 26.0% |
| <2x | 26,519 | 14.6 | 9.6 | 19.9 | 15.9 | 17.5 | 13.3 | 9.2 | 11.65 | 39.9% | 22.5% |
| >=10x | 8,342 | 10.1 | 6.5 | 15.0 | 14.3 | 21.8 | 19.0 | 13.3 | 16.54 | 54.0% | 32.3% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 13,655 | 12.4 | 8.6 | 19.8 | 16.0 | 19.0 | 13.7 | 10.5 | 12.79 | 43.2% | 24.2% |
| 300-1000 | 11,304 | 11.6 | 8.6 | 17.8 | 15.1 | 20.7 | 16.4 | 9.9 | 13.88 | 46.9% | 26.2% |
| <300 | 16,548 | 8.1 | 5.9 | 15.0 | 14.4 | 22.9 | 20.1 | 13.6 | 17.48 | 56.6% | 33.7% |
| >=3000 | 10,586 | 21.1 | 12.8 | 24.0 | 15.4 | 13.9 | 7.4 | 5.4 | 7.85 | 26.7% | 12.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1594 | 0.5472 | 0.4075 | 0.4787 | +0.069 | -0.071 | 0.0034 ± 0.0039 |
| ratio 4-10x | 1084 | 0.5742 | 0.4294 | 0.4843 | +0.090 | -0.055 | 0.0104 ± 0.0049 |
| ratio <2x | 3889 | 0.5353 | 0.4127 | 0.4325 | +0.103 | -0.020 | 0.0151 ± 0.0023 |
| ratio >=10x | 1336 | 0.5605 | 0.3875 | 0.4341 | +0.126 | -0.047 | 0.0187 ± 0.0049 |
| thinner_sample 1000-3000 | 2176 | 0.5393 | 0.4121 | 0.443 | +0.096 | -0.031 | 0.013 ± 0.0031 |
| thinner_sample 300-1000 | 1792 | 0.5612 | 0.421 | 0.4688 | +0.092 | -0.048 | 0.0065 ± 0.0037 |
| thinner_sample <300 | 2583 | 0.5547 | 0.3868 | 0.4448 | +0.110 | -0.058 | 0.0155 ± 0.0035 |
| thinner_sample >=3000 | 1352 | 0.5277 | 0.4345 | 0.4416 | +0.086 | -0.007 | 0.0151 ± 0.0031 |
| data_status ADEQUATE | 2151 | 0.5314 | 0.429 | 0.437 | +0.094 | -0.008 | 0.0159 ± 0.0026 |
| data_status LIMITED | 1923 | 0.5473 | 0.4144 | 0.4623 | +0.085 | -0.048 | 0.0084 ± 0.0034 |
| data_status POOR | 3829 | 0.5562 | 0.3965 | 0.4495 | +0.107 | -0.053 | 0.0131 ± 0.0028 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1146 | 0.197 | 0.1971 | -0.0001 ± 0.0005 | 0.5737 | 0.5741 | 0.5031 | 0.4879 | 0.4965 | -0.097 ± 0.0139 | -0.0087 (8) |
| 3-5 | 730 | 0.2079 | 0.2072 | +0.0006 ± 0.0014 | 0.6015 | 0.5982 | 0.5021 | 0.4624 | 0.474 | -0.102 ± 0.0173 | 0.01 (3) |
| 5-10 | 1691 | 0.2039 | 0.2024 | +0.0016 ± 0.0016 | 0.5947 | 0.5886 | 0.5097 | 0.4358 | 0.4607 | -0.092 ± 0.0113 | -0.0143 (7) |
| 10-15 | 1374 | 0.219 | 0.2093 | +0.0097 ± 0.0031 | 0.6297 | 0.602 | 0.5245 | 0.4011 | 0.4221 | -0.108 ± 0.0125 | -0.055 (6) |
| 15-25 | 1752 | 0.2256 | 0.2071 | +0.0185 ± 0.0042 | 0.6462 | 0.5975 | 0.572 | 0.3775 | 0.4269 | -0.103 ± 0.011 | -0.0045 (11) |
| 25-40 | 1001 | 0.2253 | 0.2026 | +0.0227 ± 0.0085 | 0.641 | 0.5848 | 0.6452 | 0.3356 | 0.4535 | -0.069 ± 0.0132 | -0.06 (2) |
| 40+ | 209 | 0.3057 | 0.1684 | +0.1373 ± 0.0257 | 0.818 | 0.506 | 0.7245 | 0.267 | 0.3541 | -0.086 ± 0.0249 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5838 | 0.1874 | 0.1883 | -0.0009 ± 0.0002 | 0.5514 | 0.5525 | 0.4914 | 0.4761 | 0.5091 | -0.019 ± 0.0058 | -0.01 (28) |
| 3-5 | 3919 | 0.1997 | 0.1977 | +0.0020 ± 0.0006 | 0.5805 | 0.5737 | 0.4814 | 0.4416 | 0.4363 | -0.060 ± 0.0072 | 0.005 (6) |
| 5-10 | 8572 | 0.2017 | 0.1975 | +0.0042 ± 0.0007 | 0.5894 | 0.5759 | 0.483 | 0.4092 | 0.4179 | -0.049 ± 0.0049 | -0.0114 (22) |
| 10-15 | 7014 | 0.2017 | 0.1856 | +0.0162 ± 0.0013 | 0.5901 | 0.5449 | 0.485 | 0.3611 | 0.3579 | -0.065 ± 0.0052 | -0.0379 (19) |
| 15-25 | 9001 | 0.2058 | 0.1663 | +0.0395 ± 0.0017 | 0.6033 | 0.4948 | 0.4971 | 0.3015 | 0.2992 | -0.068 ± 0.0043 | -0.0043 (51) |
| 25-40 | 7083 | 0.2229 | 0.1231 | +0.0999 ± 0.0026 | 0.6401 | 0.3799 | 0.5238 | 0.2098 | 0.2118 | -0.060 ± 0.0041 | -0.0733 (3) |
| 40+ | 4852 | 0.3808 | 0.0436 | +0.3371 ± 0.0034 | 0.9918 | 0.1697 | 0.6285 | 0.1011 | 0.0569 | -0.075 ± 0.0029 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 912 | 0.2036 | 0.204 | -0.0004 ± 0.0005 | 0.5876 | 0.5888 | 0.508 | 0.493 | 0.5197 | -0.095 ± 0.016 | -0.0117 (6) |
| 3-5 | 660 | 0.2145 | 0.2113 | +0.0032 ± 0.0014 | 0.6131 | 0.606 | 0.5172 | 0.4777 | 0.4545 | -0.132 ± 0.0192 | 0.01 (3) |
| 5-10 | 1464 | 0.2055 | 0.2037 | +0.0019 ± 0.0018 | 0.5969 | 0.592 | 0.5389 | 0.4644 | 0.4911 | -0.087 ± 0.0122 | -0.01 (4) |
| 10-15 | 1275 | 0.2145 | 0.2074 | +0.0071 ± 0.0032 | 0.6219 | 0.6007 | 0.558 | 0.4336 | 0.4698 | -0.102 ± 0.0133 | -0.04 (5) |
| 15-25 | 1840 | 0.2322 | 0.2109 | +0.0213 ± 0.0042 | 0.6607 | 0.6057 | 0.585 | 0.3894 | 0.4342 | -0.103 ± 0.0109 | -0.0183 (12) |
| 25-40 | 1283 | 0.2665 | 0.2002 | +0.0663 ± 0.0078 | 0.7432 | 0.5808 | 0.6594 | 0.3454 | 0.3991 | -0.111 ± 0.0126 | -0.008 (5) |
| 40+ | 469 | 0.3744 | 0.1581 | +0.2163 ± 0.0184 | 1.0176 | 0.4804 | 0.7316 | 0.243 | 0.2793 | -0.091 ± 0.0177 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4996 | 0.191 | 0.1911 | -0.0002 ± 0.0002 | 0.5571 | 0.5573 | 0.5074 | 0.4923 | 0.5062 | -0.041 ± 0.0064 | -0.0154 (26) |
| 3-5 | 3445 | 0.1952 | 0.1942 | +0.0010 ± 0.0006 | 0.5679 | 0.5649 | 0.5115 | 0.4718 | 0.4781 | -0.045 ± 0.0077 | 0.01 (5) |
| 5-10 | 7663 | 0.1963 | 0.1928 | +0.0035 ± 0.0008 | 0.5772 | 0.5643 | 0.507 | 0.4329 | 0.4492 | -0.040 ± 0.0051 | -0.0117 (6) |
| 10-15 | 6386 | 0.2023 | 0.1904 | +0.0119 ± 0.0014 | 0.5943 | 0.5576 | 0.507 | 0.3831 | 0.3979 | -0.049 ± 0.0055 | -0.0189 (18) |
| 15-25 | 9079 | 0.2154 | 0.1784 | +0.0371 ± 0.0017 | 0.6276 | 0.5247 | 0.5234 | 0.3279 | 0.3331 | -0.062 ± 0.0045 | -0.014 (52) |
| 25-40 | 8185 | 0.2505 | 0.1375 | +0.1130 ± 0.0026 | 0.7075 | 0.4195 | 0.5592 | 0.2417 | 0.2261 | -0.077 ± 0.0041 | -0.0095 (20) |
| 40+ | 6525 | 0.4022 | 0.059 | +0.3433 ± 0.0035 | 1.0598 | 0.2122 | 0.6546 | 0.1186 | 0.08 | -0.073 ± 0.0029 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1120 | 0.1959 | 0.197 | -0.0011 ± 0.0005 | 0.5715 | 0.574 | 0.5009 | 0.4854 | 0.5232 | -0.060 ± 0.0139 | -0.0191 (11) |
| 3-5 | 795 | 0.2091 | 0.2077 | +0.0014 ± 0.0013 | 0.6053 | 0.6004 | 0.498 | 0.4584 | 0.4616 | -0.110 ± 0.0169 | 0.002 (5) |
| 5-10 | 1701 | 0.2038 | 0.1996 | +0.0043 ± 0.0016 | 0.5933 | 0.5814 | 0.5112 | 0.4375 | 0.445 | -0.107 ± 0.0111 | -0.01 (10) |
| 10-15 | 1413 | 0.2122 | 0.2026 | +0.0095 ± 0.003 | 0.6148 | 0.5876 | 0.5381 | 0.4149 | 0.4395 | -0.107 ± 0.0121 | -0.0286 (7) |
| 15-25 | 1669 | 0.2311 | 0.2126 | +0.0185 ± 0.0044 | 0.6595 | 0.6098 | 0.5813 | 0.3872 | 0.4362 | -0.104 ± 0.0114 | -0.03 (1) |
| 25-40 | 986 | 0.217 | 0.2061 | +0.0109 ± 0.0086 | 0.624 | 0.593 | 0.6532 | 0.343 | 0.4787 | -0.061 ± 0.0133 | -0.0267 (3) |
| 40+ | 219 | 0.3138 | 0.1768 | +0.1369 ± 0.0257 | 0.8448 | 0.524 | 0.737 | 0.2795 | 0.3699 | -0.084 ± 0.0262 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5638 | 0.1862 | 0.1867 | -0.0005 ± 0.0002 | 0.5483 | 0.5486 | 0.4863 | 0.4709 | 0.4853 | -0.037 ± 0.0058 | -0.0189 (44) |
| 3-5 | 4028 | 0.2055 | 0.2037 | +0.0018 ± 0.0006 | 0.5965 | 0.5904 | 0.4815 | 0.442 | 0.4394 | -0.057 ± 0.0072 | -0.0073 (22) |
| 5-10 | 8710 | 0.1965 | 0.1912 | +0.0053 ± 0.0007 | 0.5767 | 0.56 | 0.4864 | 0.4124 | 0.4131 | -0.056 ± 0.0047 | -0.0117 (42) |
| 10-15 | 7020 | 0.195 | 0.1798 | +0.0152 ± 0.0013 | 0.5751 | 0.5317 | 0.4958 | 0.3725 | 0.3722 | -0.062 ± 0.0051 | -0.0136 (14) |
| 15-25 | 9040 | 0.2108 | 0.1718 | +0.0390 ± 0.0017 | 0.6151 | 0.5071 | 0.509 | 0.3143 | 0.3119 | -0.068 ± 0.0044 | -0.0533 (3) |
| 25-40 | 7074 | 0.2173 | 0.1228 | +0.0945 ± 0.0026 | 0.6281 | 0.3786 | 0.5253 | 0.2096 | 0.2195 | -0.053 ± 0.004 | -0.02 (4) |
| 40+ | 4769 | 0.3894 | 0.0477 | +0.3417 ± 0.0036 | 1.0146 | 0.1799 | 0.6374 | 0.1066 | 0.0629 | -0.076 ± 0.003 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1591 | 0.1966 | 0.1963 | +0.0004 ± 0.0004 | 0.5715 | 0.5705 | 0.509 | 0.4939 | 0.4903 | -0.076 ± 0.0113 | -0.0221 (56) |
| 3-5 | 1110 | 0.1897 | 0.1898 | -0.0001 ± 0.0011 | 0.5575 | 0.5561 | 0.498 | 0.4581 | 0.4775 | -0.054 ± 0.0134 | -0.0194 (34) |
| 5-10 | 2252 | 0.1997 | 0.1947 | +0.0050 ± 0.0014 | 0.5889 | 0.5728 | 0.5077 | 0.434 | 0.4374 | -0.077 ± 0.0095 | -0.005 (78) |
| 10-15 | 1562 | 0.2157 | 0.2023 | +0.0134 ± 0.0028 | 0.6257 | 0.5879 | 0.5435 | 0.4208 | 0.4264 | -0.093 ± 0.0117 | 0.0012 (66) |
| 15-25 | 2036 | 0.2319 | 0.2077 | +0.0242 ± 0.004 | 0.6618 | 0.5992 | 0.5912 | 0.3961 | 0.4327 | -0.090 ± 0.0102 | -0.0214 (59) |
| 25-40 | 1199 | 0.2412 | 0.2106 | +0.0306 ± 0.0081 | 0.6886 | 0.604 | 0.6882 | 0.3766 | 0.4837 | -0.085 ± 0.0125 | -0.0252 (27) |
| 40+ | 439 | 0.3259 | 0.1976 | +0.1284 ± 0.0203 | 0.9334 | 0.5763 | 0.8102 | 0.3344 | 0.4533 | -0.094 ± 0.0189 | -0.1137 (8) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5766 | 0.1771 | 0.177 | +0.0000 ± 0.0002 | 0.5243 | 0.5237 | 0.5101 | 0.4949 | 0.5007 | -0.043 ± 0.0056 | -0.0154 (103) |
| 3-5 | 3938 | 0.1948 | 0.1939 | +0.0008 ± 0.0006 | 0.5682 | 0.5658 | 0.5023 | 0.4625 | 0.4718 | -0.041 ± 0.0071 | -0.0212 (73) |
| 5-10 | 8036 | 0.1973 | 0.1908 | +0.0065 ± 0.0007 | 0.5819 | 0.5622 | 0.5024 | 0.4288 | 0.4227 | -0.061 ± 0.0049 | -0.0084 (134) |
| 10-15 | 5522 | 0.2111 | 0.194 | +0.0171 ± 0.0015 | 0.614 | 0.5687 | 0.5365 | 0.4136 | 0.404 | -0.075 ± 0.006 | -0.0057 (111) |
| 15-25 | 6784 | 0.2313 | 0.1991 | +0.0322 ± 0.0021 | 0.665 | 0.5774 | 0.5758 | 0.3804 | 0.3959 | -0.068 ± 0.0055 | -0.026 (108) |
| 25-40 | 4381 | 0.2573 | 0.1901 | +0.0672 ± 0.0041 | 0.7275 | 0.5535 | 0.6395 | 0.3273 | 0.3789 | -0.063 ± 0.0065 | -0.0277 (53) |
| 40+ | 1975 | 0.368 | 0.1592 | +0.2089 ± 0.0092 | 1.0356 | 0.4742 | 0.7407 | 0.2415 | 0.2922 | -0.058 ± 0.0086 | -0.054 (15) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 7903 | 1.019 ± 0.031 | 1.089 | 0.1677 | 0.1699 | 0.2161 | 0.2034 |
| gen2 | 7903 | 0.816 ± 0.028 | 1.066 | 0.1737 | 0.1702 | 0.2336 | 0.2034 |
| gen1_elo | 7903 | 1.004 ± 0.031 | 1.079 | 0.1741 | 0.17 | 0.2152 | 0.2035 |
| gen1_sr | 7903 | 1.0 ± 0.037 | 1.115 | 0.1335 | 0.1717 | 0.2297 | 0.2031 |
| gen1_ledger | 10189 | 0.866 ± 0.023 | 1.066 | 0.1898 | 0.1764 | 0.2173 | 0.2002 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 36,904)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 8,953 | 24.3% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 8,600 | 23.3% |
| BOOK_QUALITY | execution | 6,282 | 17.0% |
| POOR_DATA | data | 4,205 | 11.4% |
| LIMITED_DATA | data | 2,209 | 6.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 2,141 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 1,499 | 4.1% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,410 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 1,031 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 573 | 1.6% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 24.3%, coverage 23.3%, data 17.4%, execution 17.0%, market_freshness/coverage 8.6%, mapping 4.1%, model_calibration_or_unknown 3.8%, model_calibration 1.6%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.6%, START_UNVERIFIABLE 95.0%, LOW_DATA_QUALITY 72.1%, THIN_PLAYER_HISTORY 60.3%, STALE_PLAYER_DATA 52.1%, STALE_KALSHI_QUOTE 48.1%, MODEL_INTERNAL_DISAGREEMENT 41.8%, ASYMMETRIC_SAMPLE_SIZE 33.2%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 15.0%, LEVEL_TRANSFER_RISK 9.4%, LOW_DISPLAYED_LIQUIDITY 8.6%, EVENT_MAPPING_RISK 6.9%, MODEL_CALIBRATION_OUTLIER 3.5%, EXTERNAL_MARKET_REJECTION 3.2%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.7%, POST_SETTLEMENT_OBSERVATION 23.3%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 19,755)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,936 | 35.1% |
| STALE_QUOTE | market_freshness | 3,997 | 20.2% |
| BOOK_QUALITY | execution | 3,235 | 16.4% |
| POOR_DATA | data | 1,786 | 9.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,159 | 5.9% |
| IDENTITY_AMBIGUOUS | mapping | 834 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 674 | 3.4% |
| LIMITED_DATA | data | 650 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 344 | 1.7% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 139 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 35.1%, market_freshness 20.2%, execution 16.4%, data 12.3%, market_freshness/coverage 9.3%, mapping 4.2%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.1%, START_UNVERIFIABLE 97.3%, LOW_DATA_QUALITY 75.1%, THIN_PLAYER_HISTORY 62.4%, STALE_KALSHI_QUOTE 55.6%, STALE_PLAYER_DATA 45.5%, MODEL_INTERNAL_DISAGREEMENT 41.9%, ASYMMETRIC_SAMPLE_SIZE 34.4%, WIDE_SPREAD 22.6%, MODEL_HIGH_UNCERTAINTY 19.2%, PLAYER_IDENTITY_RISK 17.9%, LOW_DISPLAYED_LIQUIDITY 8.4%, EVENT_MAPPING_RISK 8.4%, LEVEL_TRANSFER_RISK 8.3%, MODEL_CALIBRATION_OUTLIER 4.6%, EXTERNAL_MARKET_REJECTION 1.8%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 38.1%, POST_SETTLEMENT_OBSERVATION 35.1%, POSSIBLE_IN_PLAY_QUOTE 6.3%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 15879, "IDENTITY_AMBIGUOUS": 3876}; ticker orientation: {"VERIFIED": 19755}.

Checks: discipline:AMBIGUOUS 1259, discipline:PASS 18496, identity_confidence:AMBIGUOUS 3536, identity_confidence:PASS 16219, level_mapping:NA 1271, level_mapping:PASS 18484, market_pair:AMBIGUOUS 504, market_pair:NA 427, market_pair:PASS 18824, model_complement:NA 389, model_complement:PASS 19366, namesake:AMBIGUOUS 6, namesake:PASS 19749, physical_match_id:NA 6545, physical_match_id:PASS 13210, player_ids:PASS 19755, same_pair_other_event:PASS 19755, ticker_orientation:PASS 19755

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,587 | 3.7% | 3.1% | 1.2% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 24, "market_freshness/coverage": 22} | 5.47 | 0.2221 / 0.2178 (861) | 25.6% | 2.4% | 3.2% | 3.0% |
| CHALLENGER | 13,194 | 16.7% | 6.1% | 11.1% | {"coverage": 1342, "market_freshness": 274, "market_freshness/coverage": 238, "data": 164, "model_calibration_or_unknown": 80, "execution": 41, "model_calibration": 40, "mapping": 17, "possible_market_error": 1} | 7.35 | 0.2213 / 0.2106 (3051) | 41.7% | 13.9% | 4.0% | 22.8% |
| DOUBLES | 2,732 | 46.1% | 46.0% | 6.4% | {"execution": 695, "mapping": 378, "market_freshness": 106, "market_freshness/coverage": 73, "coverage": 7} | 22.96 | 0.2986 / 0.2331 (679) | 8.6% | 0.0% | 100.0% | 6.3% |
| ITF_MEN | 26,147 | 25.5% | 17.8% | 33.8% | {"coverage": 2350, "market_freshness": 1399, "execution": 1037, "data": 975, "market_freshness/coverage": 672, "mapping": 225, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.79 | 0.2194 / 0.1993 (5479) | 42.2% | 70.2% | 14.6% | 21.6% |
| ITF_WOMEN | 33,165 | 26.5% | 18.8% | 44.5% | {"coverage": 3158, "market_freshness": 1957, "execution": 1379, "data": 1196, "market_freshness/coverage": 771, "mapping": 208, "model_calibration_or_unknown": 97, "model_calibration": 23} | 12.46 | 0.203 / 0.1931 (6402) | 42.8% | 57.4% | 10.0% | 21.9% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,911 | 5.9% | 5.0% | 1.5% | {"market_freshness": 111, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.64 | 0.2308 / 0.2206 (808) | 30.3% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.5% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 404 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 286 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.5h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 517 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFMATCH-26NOV10KOUPOR-POR` | ITF_MEN | fair_v1 | 87% / 2% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.9h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 305 min (STALE); data POOR (grade D, thinner serve sample 1554.0, ratio 1.02); no external reference |
| 12 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 13 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 15 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 20.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 1203 min (STALE); no external reference |
| 16 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 17 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 18 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 19 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 20 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 21 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 22 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 23 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 24 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 25 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 26 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 454 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 27 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 28 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 29 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 30 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 31 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 32 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 33 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 34 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 35 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 36 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 37 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 38 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 39 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 40 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 41 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 43 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 213 min (STALE); no external reference |
| 44 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 45 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 46 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 47 | `KXITFWMATCH-26NOV11CORROJ-ROJ` | ITF_WOMEN | fair_v1 | 87% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade D, thinner serve sample 531.0, ratio 1.04); no external reference |
| 48 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 49 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.1h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 446 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9728, "by_level_share_of_ge_25pp": {"ATP": 0.0124, "CHALLENGER": 0.1112, "DOUBLES": 0.0637, "ITF_MEN": 0.3376, "ITF_WOMEN": 0.4449, "OTHER": 0.0006, "WTA": 0.0147, "WTA125": 0.0148}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5557, "share_primary_cause_market_settled_or_in_play": 0.4439, "share_primary_cause_stale_quote_only": 0.2023}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 19755, "identity_ambiguous_share": 0.1962, "ticker_orientation": {"VERIFIED": 19755}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 13210, "with_external": 645, "coverage": 0.0488, "external_status": {"EXTERNAL_STALE": 409, "AGREES_WITH_KALSHI": 223, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 409, "MODEL_LONE_OUTLIER": 223, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3457, "share_external_supports_model": 0.0202}, "pregame_clean_ge_25pp": {"n": 6048, "with_external": 613, "coverage": 0.1014, "external_status": {"EXTERNAL_STALE": 384, "AGREES_WITH_KALSHI": 216, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 384, "MODEL_LONE_OUTLIER": 216, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3524, "share_external_supports_model": 0.0212}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 476.0, "median_sample_ratio": 2.45, "median_min_matches": 18.0, "median_max_days_since_last": 246.0, "share_severe_asymmetry": 0.2072, "data_status": {"POOR": 11263, "LIMITED": 4940, "ADEQUATE": 3552}, "comparison_lt_10pp": {"median_thinner_serve_points": 1675.0, "median_sample_ratio": 1.71, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1594, "model_minus_observed": 0.0685, "kalshi_minus_observed": -0.0712, "brier_diff_model_minus_kalshi": 0.0034}, "4-10x": {"n": 1084, "model_minus_observed": 0.0898, "kalshi_minus_observed": -0.055, "brier_diff_model_minus_kalshi": 0.0104}, "<2x": {"n": 3889, "model_minus_observed": 0.1028, "kalshi_minus_observed": -0.0198, "brier_diff_model_minus_kalshi": 0.0151}, ">=10x": {"n": 1336, "model_minus_observed": 0.1264, "kalshi_minus_observed": -0.0466, "brier_diff_model_minus_kalshi": 0.0187}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 7903, "model": {"intercept": -0.56, "slope": 0.816, "slope_se": 0.028}, "kalshi_mid_same_rows": {"intercept": 0.17, "slope": 1.066, "slope_se": 0.032}, "mean_extremity_model": 0.1737, "mean_extremity_kalshi": 0.1702, "model_brier": 0.2336, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": 0.0303, "brier_diff_se": 0.0021, "model_logloss": 0.6648, "kalshi_logloss": 0.5889}, "fair_v1": {"n": 7903, "model": {"intercept": -0.466, "slope": 1.019, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.219, "slope": 1.089, "slope_se": 0.032}, "mean_extremity_model": 0.1677, "mean_extremity_kalshi": 0.1699, "model_brier": 0.2161, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": 0.0127, "brier_diff_se": 0.0017, "model_logloss": 0.6216, "kalshi_logloss": 0.589}, "gen1_elo": {"n": 7903, "model": {"intercept": -0.455, "slope": 1.004, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.221, "slope": 1.079, "slope_se": 0.031}, "mean_extremity_model": 0.1741, "mean_extremity_kalshi": 0.17, "model_brier": 0.2152, "kalshi_brier": 0.2035, "brier_diff_model_minus_kalshi": 0.0117, "brier_diff_se": 0.0017, "model_logloss": 0.62, "kalshi_logloss": 0.5892}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2536, "share_ge_15": 0.4492, "median_abs_gap": 13.17, "n": 52093}, "gen1_elo": {"share_ge_25": 0.2514, "share_ge_15": 0.4452, "median_abs_gap": 13.0, "n": 52093}, "gen1_sr": {"share_ge_25": 0.3161, "share_ge_15": 0.5248, "median_abs_gap": 15.98, "n": 52093}, "gen2": {"share_ge_25": 0.316, "share_ge_15": 0.5125, "median_abs_gap": 15.5, "n": 52093}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1521, "share_ge_15": 0.3551, "median_abs_gap": 10.71, "n": 39769}, "gen1_elo": {"share_ge_25": 0.1505, "share_ge_15": 0.35, "median_abs_gap": 10.51, "n": 39769}, "gen1_sr": {"share_ge_25": 0.2157, "share_ge_15": 0.4402, "median_abs_gap": 13.0, "n": 39771}, "gen2": {"share_ge_25": 0.2306, "share_ge_15": 0.4388, "median_abs_gap": 12.84, "n": 39771}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.47, "share_ge_25_all": 0.0372, "share_ge_25_pregame_clean": 0.0312}, "WTA": {"median_abs_gap_pregame_clean": 7.64, "share_ge_25_all": 0.0593, "share_ge_25_pregame_clean": 0.0503}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2345, "share_within_10pp_all": 0.4359, "share_within_10pp_pregame_clean": 0.4905, "corr_model_vs_mid_pregame_clean": 0.8494}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1146, "model_brier": 0.197, "kalshi_brier": 0.1971, "brier_diff_model_minus_kalshi": -0.0001}, "10-15": {"n_settled": 1374, "model_brier": 0.219, "kalshi_brier": 0.2093, "brier_diff_model_minus_kalshi": 0.0097}, "15-25": {"n_settled": 1752, "model_brier": 0.2256, "kalshi_brier": 0.2071, "brier_diff_model_minus_kalshi": 0.0185}, "25-40": {"n_settled": 1001, "model_brier": 0.2253, "kalshi_brier": 0.2026, "brier_diff_model_minus_kalshi": 0.0227}, "3-5": {"n_settled": 730, "model_brier": 0.2079, "kalshi_brier": 0.2072, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 209, "model_brier": 0.3057, "kalshi_brier": 0.1684, "brier_diff_model_minus_kalshi": 0.1373}, "5-10": {"n_settled": 1691, "model_brier": 0.2039, "kalshi_brier": 0.2024, "brier_diff_model_minus_kalshi": 0.0016}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.56, "slope": 0.816, "slope_se": 0.028}, "kalshi_slope": {"intercept": 0.17, "slope": 1.066, "slope_se": 0.032}, "n": 7903}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.501, "slope": 0.866, "slope_se": 0.023}, "kalshi_slope": {"intercept": 0.152, "slope": 1.066, "slope_se": 0.027}, "n": 10189}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 679, "model_brier": 0.2986, "kalshi_brier": 0.2331, "brier_diff_model_minus_kalshi": 0.0656, "brier_diff_se": 0.0112, "corr_model_outcome": 0.1024, "corr_kalshi_outcome": 0.2721}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
