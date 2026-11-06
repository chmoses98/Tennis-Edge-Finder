# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-06T08:19Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 80,461): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 19.1%, 25-40 13.6%, 40+ 8.0%; median gap 11.81 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.8%, Challenger 10.7%, doubles 6.7%). Main tour: ATP 3.8% and WTA 6.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 17,409): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.9%, STALE_QUOTE 19.5%, BOOK_QUALITY 17.6%, POOR_DATA 9.3%, POSSIBLY_IN_PLAY_QUOTE 5.8%, IDENTITY_AMBIGUOUS 4.3%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.9%, market_freshness 19.5%, execution 17.6%, data 12.7%, market_freshness/coverage 9.3%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 53.3% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.2% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 17,409 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.3% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.5% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 490.0 points vs 1719.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.032, Gen-2 0.826, Gen-1 ledger 0.868 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 891 model 0.2223 vs Kalshi 0.2039; n 186 model 0.2966 vs Kalshi 0.1748.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 341,745 model-market comparisons (559,557 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 113,831 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-06T08:00:54.657751+00:00'], shadow board 92,431 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-06T08:00:58.400847+00:00'], Model 4 42,304 rows, 28,300 settled tickers, 10,714 tickers with an external scan.
* By model: {"gen1_ledger": 76702, "gen1_elo": 46447, "fair_v1": 46447, "gen2": 46447, "gen1_sr": 46447, "model4_fundamental": 39669, "model4_conditioned": 39586}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 80,461 | 14.1 | 9.6 | 20.2 | 15.3 | 19.1 | 13.6 | 8.0 | 11.81 | 40.8% | 21.6% |
| MW fair_v1 | 46,447 | 12.8 | 8.7 | 18.8 | 15.4 | 19.6 | 14.8 | 9.9 | 13.02 | 44.3% | 24.7% |
| MW gen1_elo | 46,447 | 12.6 | 8.8 | 19.3 | 15.4 | 19.5 | 14.6 | 9.8 | 12.77 | 43.9% | 24.3% |
| MW gen1_ledger | 34,014 | 15.7 | 10.9 | 22.2 | 15.2 | 18.4 | 12.0 | 5.5 | 10.26 | 35.9% | 17.5% |
| MW gen1_sr | 46,447 | 10.1 | 7.3 | 16.7 | 14.0 | 20.7 | 18.7 | 12.5 | 15.78 | 52.0% | 31.3% |
| MW gen2 | 46,447 | 11.0 | 7.6 | 16.7 | 13.8 | 19.7 | 17.7 | 13.6 | 15.43 | 50.9% | 31.3% |
| all families model4_conditioned | 39,586 | 22.2 | 18.0 | 34.2 | 17.2 | 5.0 | 2.2 | 1.2 | 6.07 | 8.5% | 3.4% |
| all families model4_fundamental | 39,669 | 17.4 | 13.5 | 33.9 | 19.9 | 10.0 | 3.8 | 1.5 | 7.62 | 15.3% | 5.3% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.1%, >=15pp 40.8%, >=20pp 30.0%, >=25pp 21.6%, >=30pp 15.6%, >=40pp 8.0%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.36pp; >=10pp 45.0%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,927 | 28.6 | 15.7 | 27.6 | 13.4 | 10.6 | 3.6 | 0.6 | 5.77 | 14.8% | 4.2% |
| CHALLENGER | 6,945 | 15.9 | 9.8 | 20.8 | 15.3 | 16.2 | 11.3 | 10.7 | 10.92 | 38.2% | 22.0% |
| ITF_MEN | 13,129 | 9.8 | 7.4 | 17.1 | 15.2 | 21.3 | 17.3 | 11.9 | 15.18 | 50.5% | 29.2% |
| ITF_WOMEN | 18,093 | 9.6 | 7.1 | 16.0 | 14.8 | 22.1 | 18.3 | 12.1 | 15.84 | 52.5% | 30.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,020 | 16.8 | 13.2 | 24.7 | 20.9 | 16.6 | 6.8 | 1.1 | 8.68 | 24.5% | 7.9% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,927 | 26.9 | 15.8 | 26.0 | 15.4 | 11.4 | 3.7 | 0.8 | 6.02 | 15.9% | 4.5% |
| CHALLENGER | 6,945 | 14.7 | 9.1 | 18.8 | 14.0 | 18.7 | 13.5 | 11.3 | 12.48 | 43.5% | 24.8% |
| ITF_MEN | 13,129 | 8.2 | 6.1 | 15.2 | 13.8 | 20.0 | 20.5 | 16.2 | 17.85 | 56.7% | 36.6% |
| ITF_WOMEN | 18,093 | 7.8 | 5.8 | 14.1 | 12.9 | 20.8 | 21.1 | 17.6 | 19.1 | 59.4% | 38.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,020 | 14.1 | 10.2 | 21.8 | 16.1 | 22.4 | 12.9 | 2.5 | 11.23 | 37.9% | 15.5% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,927 | 22.9 | 14.0 | 25.2 | 15.6 | 15.0 | 6.1 | 1.2 | 7.2 | 22.3% | 7.3% |
| CHALLENGER | 6,945 | 15.2 | 9.6 | 20.8 | 15.6 | 16.1 | 11.9 | 10.8 | 11.2 | 38.8% | 22.7% |
| ITF_MEN | 13,129 | 9.5 | 7.3 | 17.3 | 14.3 | 21.9 | 17.2 | 12.4 | 15.57 | 51.6% | 29.6% |
| ITF_WOMEN | 18,093 | 9.3 | 6.9 | 16.3 | 15.8 | 22.2 | 18.1 | 11.4 | 15.57 | 51.8% | 29.5% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,020 | 22.7 | 17.1 | 31.9 | 15.2 | 8.7 | 3.3 | 1.1 | 6.12 | 13.1% | 4.4% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,328 | 26.9 | 19.7 | 29.9 | 12.3 | 8.2 | 2.6 | 0.4 | 5.34 | 11.2% | 3.0% |
| CHALLENGER | 4,487 | 22.3 | 14.5 | 27.7 | 14.8 | 13.5 | 5.8 | 1.5 | 7.09 | 20.8% | 7.3% |
| DOUBLES | 2,526 | 4.9 | 4.5 | 12.9 | 11.1 | 20.1 | 24.6 | 21.9 | 23.35 | 66.5% | 46.5% |
| ITF_MEN | 9,752 | 13.0 | 9.6 | 21.3 | 15.8 | 21.6 | 12.9 | 5.8 | 11.77 | 40.3% | 18.7% |
| ITF_WOMEN | 11,750 | 13.3 | 9.3 | 20.0 | 15.7 | 21.4 | 14.9 | 5.5 | 12.23 | 41.7% | 20.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,766 | 23.9 | 15.9 | 31.4 | 16.9 | 9.1 | 2.6 | 0.2 | 6.57 | 11.9% | 2.8% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,812 | 29.0 | 15.8 | 28.0 | 13.3 | 10.4 | 3.2 | 0.3 | 5.64 | 13.9% | 3.5% |
| CHALLENGER | 4,916 | 20.5 | 12.1 | 25.6 | 18.1 | 16.1 | 5.9 | 1.6 | 8.27 | 23.6% | 7.5% |
| ITF_MEN | 9,615 | 12.0 | 8.6 | 20.7 | 17.4 | 22.0 | 14.1 | 5.2 | 12.38 | 41.3% | 19.3% |
| ITF_WOMEN | 13,331 | 11.4 | 8.6 | 18.9 | 17.0 | 24.1 | 15.2 | 4.9 | 13.19 | 44.1% | 20.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,908 | 17.1 | 13.2 | 25.0 | 21.2 | 16.6 | 6.3 | 0.6 | 8.51 | 23.4% | 6.9% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,812 | 27.2 | 16.2 | 26.3 | 15.3 | 11.3 | 3.3 | 0.4 | 5.95 | 15.0% | 3.7% |
| CHALLENGER | 4,916 | 18.4 | 11.4 | 23.6 | 16.3 | 19.1 | 9.3 | 1.9 | 9.02 | 30.2% | 11.1% |
| ITF_MEN | 9,616 | 9.6 | 7.2 | 17.6 | 16.0 | 21.7 | 18.6 | 9.2 | 14.86 | 49.5% | 27.8% |
| ITF_WOMEN | 13,332 | 8.8 | 6.8 | 16.0 | 14.4 | 22.8 | 20.4 | 10.7 | 16.52 | 53.9% | 31.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,908 | 14.3 | 10.3 | 22.0 | 16.3 | 22.5 | 12.6 | 1.9 | 11.03 | 37.1% | 14.5% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,271 | 27.0 | 19.9 | 29.9 | 12.4 | 7.9 | 2.5 | 0.3 | 5.31 | 10.7% | 2.8% |
| CHALLENGER | 3,963 | 23.6 | 15.4 | 28.8 | 14.9 | 12.9 | 4.0 | 0.4 | 6.61 | 17.3% | 4.4% |
| DOUBLES | 2,370 | 4.8 | 4.6 | 13.1 | 11.1 | 19.9 | 24.6 | 21.9 | 23.23 | 66.3% | 46.4% |
| ITF_MEN | 8,389 | 13.8 | 10.2 | 22.9 | 16.3 | 21.6 | 11.4 | 3.8 | 10.84 | 36.9% | 15.2% |
| ITF_WOMEN | 10,064 | 14.0 | 9.8 | 21.1 | 16.2 | 21.5 | 13.8 | 3.6 | 11.41 | 38.9% | 17.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,705 | 24.3 | 16.3 | 31.4 | 16.9 | 9.0 | 2.0 | 0.1 | 6.43 | 11.1% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,526 | 4.9 | 4.5 | 12.9 | 11.1 | 20.1 | 24.6 | 21.9 | 23.35 | 66.5% | 46.5% |
| singles | 31,488 | 16.6 | 11.4 | 23.0 | 15.5 | 18.3 | 11.0 | 4.2 | 9.73 | 33.5% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 158 | 7.6 | 8.2 | 12.7 | 7.6 | 20.2 | 28.5 | 15.2 | 21.41 | 63.9% | 43.7% |
| Clay | 9,513 | 12.7 | 9.1 | 19.9 | 15.7 | 19.7 | 13.8 | 9.1 | 12.59 | 42.6% | 22.9% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 30,266 | 13.4 | 8.8 | 18.8 | 15.2 | 19.2 | 14.8 | 9.8 | 12.85 | 43.8% | 24.6% |
| UNKNOWN | 6,273 | 10.5 | 7.6 | 17.0 | 16.4 | 21.4 | 16.0 | 11.1 | 14.32 | 48.5% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 13,154 | 19.5 | 11.9 | 22.4 | 15.9 | 15.0 | 9.1 | 6.1 | 8.88 | 30.2% | 15.2% |
| B | 5,672 | 12.8 | 8.7 | 19.8 | 15.7 | 19.6 | 12.7 | 10.7 | 12.61 | 43.0% | 23.4% |
| C | 6,588 | 12.0 | 8.9 | 19.5 | 15.7 | 18.6 | 14.7 | 10.6 | 12.92 | 43.9% | 25.3% |
| D | 7,544 | 11.7 | 8.3 | 17.9 | 15.4 | 21.6 | 15.7 | 9.3 | 13.79 | 46.6% | 25.1% |
| F | 13,489 | 7.5 | 5.6 | 14.8 | 14.7 | 23.5 | 20.8 | 13.1 | 17.71 | 57.4% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,079 | 24.5 | 16.1 | 29.2 | 15.0 | 10.7 | 3.4 | 1.2 | 6.37 | 15.3% | 4.6% |
| B | 4,773 | 16.6 | 10.8 | 24.2 | 16.9 | 18.8 | 9.6 | 3.1 | 9.67 | 31.5% | 12.7% |
| C | 6,720 | 11.1 | 7.8 | 19.6 | 14.7 | 20.9 | 15.6 | 10.3 | 13.48 | 46.8% | 25.9% |
| D | 5,103 | 14.6 | 10.1 | 21.4 | 15.4 | 20.7 | 12.6 | 5.2 | 11.19 | 38.6% | 17.8% |
| F | 8,339 | 10.2 | 8.4 | 16.2 | 14.6 | 23.3 | 19.5 | 7.8 | 15.32 | 50.6% | 27.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 14,864 | 17.8 | 10.9 | 21.6 | 15.8 | 15.3 | 10.0 | 8.7 | 9.96 | 34.0% | 18.7% |
| LIMITED | 10,160 | 13.7 | 9.8 | 20.4 | 15.9 | 19.3 | 13.4 | 7.5 | 11.83 | 40.2% | 20.9% |
| POOR | 21,423 | 9.1 | 6.6 | 16.0 | 15.0 | 22.7 | 18.8 | 11.8 | 16.1 | 53.3% | 30.6% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,722 | 23.8 | 17.8 | 33.1 | 15.6 | 6.4 | 2.9 | 0.4 | 5.91 | 9.7% | 3.3% |
| GAME_SPREAD | 6,597 | 22.5 | 15.3 | 32.2 | 16.9 | 9.0 | 3.4 | 0.6 | 6.71 | 13.0% | 4.0% |
| MATCH_WINNER | 34,014 | 15.7 | 10.9 | 22.2 | 15.2 | 18.4 | 12.0 | 5.5 | 10.26 | 35.9% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 16,224 | 27.9 | 16.7 | 30.8 | 12.7 | 9.2 | 2.4 | 0.3 | 5.64 | 11.9% | 2.7% |
| TOTAL_GAMES | 11,121 | 9.8 | 10.8 | 35.6 | 25.9 | 10.7 | 4.2 | 2.9 | 9.2 | 17.9% | 7.2% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,004 | 24.4 | 28.9 | 33.2 | 8.1 | 4.0 | 1.1 | 0.3 | 4.79 | 5.3% | 1.4% |
| GAME_SPREAD | 9,132 | 46.9 | 16.1 | 24.7 | 7.5 | 2.3 | 1.9 | 0.6 | 3.29 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,450 | 6.6 | 9.8 | 40.2 | 30.2 | 7.5 | 3.3 | 2.4 | 9.22 | 13.2% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,039 | 23.9 | 16.6 | 34.8 | 14.6 | 6.9 | 2.6 | 0.5 | 6.04 | 10.0% | 3.1% |
| GAME_SPREAD | 9,141 | 20.6 | 13.6 | 28.2 | 20.0 | 11.9 | 4.5 | 1.2 | 7.61 | 17.5% | 5.6% |
| TOTAL_GAMES | 16,489 | 10.0 | 10.8 | 36.2 | 24.3 | 11.6 | 4.5 | 2.6 | 9.06 | 18.7% | 7.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 46,447 | 44.3% | 24.7% | 13.02 | 35.3% | 15.1% | 10.7 |
| gen1_elo | 46,447 | 43.9% | 24.3% | 12.77 | 34.8% | 14.8% | 10.49 |
| gen1_sr | 46,447 | 52.0% | 31.3% | 15.78 | 44.0% | 21.6% | 13.0 |
| gen2 | 46,447 | 50.9% | 31.3% | 15.43 | 43.9% | 23.1% | 12.85 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 19,896 | 15.5 | 10.5 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 26,551 | 10.8 | 7.3 | 16.8 | 14.0 | 19.3 | 17.0 | 14.7 | 15.38 | 51.0% | 31.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 27,482 | 16.4 | 11.2 | 22.8 | 15.3 | 17.9 | 11.5 | 4.8 | 9.87 | 34.3% | 16.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 80,461 | 27482 | 23368 | 29611 | 24.7 | 124.8 | 1451.1 |
| ge_15pp | 32,788 | 9421 | 8324 | 15043 | 28.1 | 430.2 | 1451.1 |
| ge_25pp | 17,409 | 4492 | 3632 | 9285 | 33.1 | 579.0 | 1431.1 |
| lt_10pp | 35,344 | 13861 | 11051 | 10432 | 22.6 | 47.9 | 1421.1 |

Current slate `SL-20261106T081927Z-06b89b19`: 293 priced rows, quote age at build {'median': 18.9, 'max': 19.0}, freshness {'AGING': 293}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 49 | 0.0 | 0.0 | 36.7 | 6.1 | 32.6 | 20.4 | 4.1 | 18.34 | 57.1% | 24.5% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,630 | 19.2 | 10.9 | 25.5 | 17.8 | 18.1 | 7.5 | 1.0 | 8.82 | 26.5% | 8.4% |
| KALSHI_LONE_OUTLIER | 30 | 6.7 | 6.7 | 73.3 | 6.7 | 3.3 | 3.3 | 0.0 | 6.16 | 6.7% | 3.3% |
| MARKETS_AGREE | 948 | 66.0 | 34.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,048 | 0.0 | 2.3 | 37.0 | 26.5 | 24.2 | 9.2 | 0.9 | 11.83 | 34.2% | 10.1% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 46,447 | 7734 (16.7%) | 26.5% | 1.0% | {"EXTERNAL_STALE": 4630, "AGREES_WITH_KALSHI": 2048, "ALL_AGREE": 948, "SUPPORTS_MODEL_DIRECTION": 48, "AGREES_WITH_MODEL": 30, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 20,568 | 1960 (9.5%) | 35.8% | 1.5% | {"EXTERNAL_STALE": 1229, "AGREES_WITH_KALSHI": 701, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 11,455 | 609 (5.3%) | 33.8% | 2.1% | {"EXTERNAL_STALE": 390, "AGREES_WITH_KALSHI": 206, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,410 | 579 (10.7%) | 34.4% | 2.2% | {"EXTERNAL_STALE": 367, "AGREES_WITH_KALSHI": 199, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 18,714 | 4401 (23.5%) | 18.3% | 1.0% | {"EXTERNAL_STALE": 2576, "ALL_AGREE": 948, "AGREES_WITH_KALSHI": 804, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 26, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 9,114 | 10.5 | 7.7 | 19.5 | 14.7 | 21.6 | 16.2 | 9.8 | 14.04 | 47.7% | 26.1% |
| 4-10x | 6,230 | 11.4 | 8.6 | 18.4 | 15.3 | 22.0 | 14.3 | 10.1 | 13.75 | 46.4% | 24.4% |
| <2x | 23,680 | 14.9 | 9.8 | 19.8 | 16.1 | 17.6 | 13.1 | 8.8 | 11.55 | 39.5% | 21.9% |
| >=10x | 7,423 | 10.5 | 6.4 | 15.0 | 14.4 | 21.7 | 18.9 | 13.0 | 16.35 | 53.7% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 12,164 | 12.4 | 8.7 | 19.9 | 16.2 | 19.0 | 13.5 | 10.2 | 12.68 | 42.8% | 23.7% |
| 300-1000 | 10,065 | 11.8 | 8.8 | 17.7 | 15.2 | 20.7 | 16.3 | 9.5 | 13.7 | 46.5% | 25.8% |
| <300 | 14,596 | 8.3 | 5.8 | 15.1 | 14.7 | 23.1 | 19.8 | 13.0 | 17.1 | 56.0% | 32.9% |
| >=3000 | 9,622 | 21.3 | 12.9 | 23.9 | 15.7 | 14.0 | 7.2 | 5.0 | 7.75 | 26.2% | 12.2% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1414 | 0.5477 | 0.4083 | 0.4901 | +0.058 | -0.082 | 0.0004 ± 0.0041 |
| ratio 4-10x | 966 | 0.5762 | 0.4315 | 0.4865 | +0.090 | -0.055 | 0.0092 ± 0.0051 |
| ratio <2x | 3433 | 0.5367 | 0.4136 | 0.4366 | +0.100 | -0.023 | 0.0145 ± 0.0024 |
| ratio >=10x | 1188 | 0.5639 | 0.3907 | 0.447 | +0.117 | -0.056 | 0.0148 ± 0.0052 |
| thinner_sample 1000-3000 | 1939 | 0.5391 | 0.4119 | 0.4477 | +0.091 | -0.036 | 0.0112 ± 0.0033 |
| thinner_sample 300-1000 | 1593 | 0.5631 | 0.4225 | 0.4752 | +0.088 | -0.053 | 0.0044 ± 0.0039 |
| thinner_sample <300 | 2281 | 0.5573 | 0.3894 | 0.4546 | +0.103 | -0.065 | 0.0132 ± 0.0037 |
| thinner_sample >=3000 | 1188 | 0.53 | 0.4363 | 0.447 | +0.083 | -0.011 | 0.0151 ± 0.0033 |
| data_status ADEQUATE | 1932 | 0.5322 | 0.4288 | 0.4405 | +0.092 | -0.012 | 0.0154 ± 0.0028 |
| data_status LIMITED | 1703 | 0.5474 | 0.4149 | 0.4668 | +0.081 | -0.052 | 0.0068 ± 0.0036 |
| data_status POOR | 3366 | 0.5594 | 0.399 | 0.4596 | +0.100 | -0.061 | 0.0105 ± 0.003 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1005 | 0.197 | 0.1974 | -0.0003 ± 0.0005 | 0.5738 | 0.5746 | 0.5024 | 0.4873 | 0.4995 | -0.096 ± 0.0148 | -0.0087 (8) |
| 3-5 | 645 | 0.2049 | 0.2049 | -0.0000 ± 0.0014 | 0.5937 | 0.5923 | 0.5029 | 0.463 | 0.4822 | -0.095 ± 0.0183 | 0.01 (2) |
| 5-10 | 1508 | 0.201 | 0.2003 | +0.0007 ± 0.0017 | 0.5882 | 0.584 | 0.5115 | 0.4377 | 0.4675 | -0.089 ± 0.0119 | -0.0143 (7) |
| 10-15 | 1214 | 0.2184 | 0.2091 | +0.0093 ± 0.0033 | 0.6289 | 0.6015 | 0.5229 | 0.3994 | 0.4226 | -0.105 ± 0.0133 | -0.048 (5) |
| 15-25 | 1552 | 0.2245 | 0.208 | +0.0165 ± 0.0045 | 0.6436 | 0.5996 | 0.5747 | 0.3799 | 0.4356 | -0.101 ± 0.0116 | -0.004 (10) |
| 25-40 | 891 | 0.2223 | 0.2039 | +0.0185 ± 0.009 | 0.6344 | 0.5882 | 0.6513 | 0.3414 | 0.4669 | -0.068 ± 0.0138 | -0.06 (2) |
| 40+ | 186 | 0.2966 | 0.1748 | +0.1217 ± 0.0275 | 0.7985 | 0.5224 | 0.73 | 0.2752 | 0.3763 | -0.084 ± 0.0267 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5278 | 0.1854 | 0.1862 | -0.0009 ± 0.0002 | 0.5467 | 0.5476 | 0.4887 | 0.4735 | 0.504 | -0.022 ± 0.006 | -0.01 (28) |
| 3-5 | 3556 | 0.1978 | 0.1961 | +0.0016 ± 0.0006 | 0.5758 | 0.5697 | 0.4811 | 0.4413 | 0.4398 | -0.056 ± 0.0075 | 0.0 (3) |
| 5-10 | 7668 | 0.2007 | 0.1976 | +0.0031 ± 0.0008 | 0.587 | 0.5762 | 0.4843 | 0.4107 | 0.427 | -0.043 ± 0.0051 | -0.0114 (22) |
| 10-15 | 6352 | 0.2017 | 0.1859 | +0.0158 ± 0.0013 | 0.5898 | 0.5453 | 0.4849 | 0.3609 | 0.3594 | -0.063 ± 0.0054 | -0.0281 (16) |
| 15-25 | 8018 | 0.2056 | 0.167 | +0.0386 ± 0.0018 | 0.6029 | 0.4963 | 0.4989 | 0.3035 | 0.3034 | -0.068 ± 0.0046 | -0.0027 (45) |
| 25-40 | 6193 | 0.2229 | 0.1261 | +0.0968 ± 0.0028 | 0.64 | 0.3876 | 0.5268 | 0.2131 | 0.2201 | -0.058 ± 0.0044 | -0.0733 (3) |
| 40+ | 4101 | 0.3827 | 0.0444 | +0.3383 ± 0.0038 | 0.9971 | 0.1721 | 0.6312 | 0.1024 | 0.0588 | -0.076 ± 0.0031 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 808 | 0.2043 | 0.2047 | -0.0003 ± 0.0005 | 0.5892 | 0.5904 | 0.5064 | 0.4915 | 0.5136 | -0.103 ± 0.0171 | -0.0117 (6) |
| 3-5 | 577 | 0.2105 | 0.2075 | +0.0030 ± 0.0015 | 0.6033 | 0.5969 | 0.5118 | 0.4722 | 0.4506 | -0.132 ± 0.0204 | 0.01 (2) |
| 5-10 | 1290 | 0.2069 | 0.2049 | +0.0020 ± 0.0019 | 0.6001 | 0.5947 | 0.5392 | 0.4646 | 0.4915 | -0.090 ± 0.013 | -0.01 (4) |
| 10-15 | 1123 | 0.2112 | 0.2061 | +0.0050 ± 0.0034 | 0.6146 | 0.5978 | 0.5632 | 0.4389 | 0.4835 | -0.096 ± 0.0141 | -0.04 (5) |
| 15-25 | 1640 | 0.2307 | 0.2124 | +0.0183 ± 0.0045 | 0.6558 | 0.6093 | 0.5841 | 0.3886 | 0.4409 | -0.097 ± 0.0116 | -0.012 (10) |
| 25-40 | 1148 | 0.2662 | 0.1967 | +0.0695 ± 0.0082 | 0.7431 | 0.5731 | 0.6581 | 0.344 | 0.3929 | -0.120 ± 0.0131 | -0.008 (5) |
| 40+ | 415 | 0.3727 | 0.162 | +0.2107 ± 0.0198 | 1.0163 | 0.4901 | 0.7352 | 0.2464 | 0.2892 | -0.087 ± 0.019 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4537 | 0.1917 | 0.192 | -0.0003 ± 0.0002 | 0.5589 | 0.5593 | 0.5076 | 0.4925 | 0.5102 | -0.038 ± 0.0067 | -0.0154 (26) |
| 3-5 | 3095 | 0.1926 | 0.1916 | +0.0010 ± 0.0006 | 0.5616 | 0.5582 | 0.5103 | 0.4707 | 0.4766 | -0.046 ± 0.0081 | 0.01 (2) |
| 5-10 | 6834 | 0.1973 | 0.1939 | +0.0034 ± 0.0008 | 0.5795 | 0.5672 | 0.5081 | 0.434 | 0.4505 | -0.041 ± 0.0054 | -0.0117 (6) |
| 10-15 | 5705 | 0.2017 | 0.1914 | +0.0103 ± 0.0014 | 0.5926 | 0.5598 | 0.5103 | 0.3863 | 0.4075 | -0.044 ± 0.0059 | -0.0189 (18) |
| 15-25 | 8064 | 0.2166 | 0.1813 | +0.0352 ± 0.0019 | 0.6293 | 0.5318 | 0.5242 | 0.3286 | 0.3389 | -0.059 ± 0.0048 | -0.0084 (43) |
| 25-40 | 7265 | 0.2507 | 0.1372 | +0.1134 ± 0.0028 | 0.7082 | 0.4195 | 0.5599 | 0.2429 | 0.226 | -0.080 ± 0.0043 | -0.0095 (20) |
| 40+ | 5666 | 0.4016 | 0.0592 | +0.3424 ± 0.0037 | 1.0592 | 0.2134 | 0.6546 | 0.1192 | 0.0807 | -0.074 ± 0.0032 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 984 | 0.1959 | 0.1974 | -0.0015 ± 0.0005 | 0.5714 | 0.5751 | 0.5028 | 0.4874 | 0.5356 | -0.049 ± 0.0148 | -0.012 (10) |
| 3-5 | 687 | 0.2069 | 0.2054 | +0.0015 ± 0.0014 | 0.5994 | 0.5944 | 0.4947 | 0.4552 | 0.4585 | -0.110 ± 0.0181 | -0.0 (4) |
| 5-10 | 1538 | 0.2021 | 0.1987 | +0.0034 ± 0.0017 | 0.5892 | 0.5796 | 0.5124 | 0.4387 | 0.4519 | -0.103 ± 0.0118 | -0.01 (9) |
| 10-15 | 1231 | 0.2107 | 0.2014 | +0.0093 ± 0.0032 | 0.612 | 0.5847 | 0.5362 | 0.413 | 0.4387 | -0.108 ± 0.0128 | -0.0286 (7) |
| 15-25 | 1483 | 0.2305 | 0.2126 | +0.0179 ± 0.0047 | 0.6583 | 0.6095 | 0.5851 | 0.391 | 0.4417 | -0.106 ± 0.012 | -0.03 (1) |
| 25-40 | 883 | 0.2122 | 0.2085 | +0.0037 ± 0.009 | 0.613 | 0.599 | 0.6591 | 0.3482 | 0.496 | -0.055 ± 0.0139 | -0.0267 (3) |
| 40+ | 195 | 0.3097 | 0.1824 | +0.1274 ± 0.0275 | 0.8383 | 0.5387 | 0.7419 | 0.2873 | 0.3846 | -0.087 ± 0.0282 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5110 | 0.1853 | 0.186 | -0.0007 ± 0.0002 | 0.546 | 0.5469 | 0.4859 | 0.4706 | 0.4906 | -0.031 ± 0.0061 | -0.0137 (41) |
| 3-5 | 3626 | 0.2042 | 0.2026 | +0.0017 ± 0.0006 | 0.5932 | 0.5875 | 0.4778 | 0.4383 | 0.4379 | -0.055 ± 0.0076 | -0.01 (19) |
| 5-10 | 7834 | 0.1956 | 0.1906 | +0.0050 ± 0.0007 | 0.5743 | 0.5585 | 0.4869 | 0.413 | 0.4164 | -0.054 ± 0.005 | -0.0105 (37) |
| 10-15 | 6295 | 0.1933 | 0.1781 | +0.0152 ± 0.0013 | 0.5711 | 0.5273 | 0.4937 | 0.3704 | 0.3703 | -0.062 ± 0.0053 | -0.0146 (13) |
| 15-25 | 8106 | 0.2112 | 0.1723 | +0.0389 ± 0.0018 | 0.6163 | 0.5083 | 0.5122 | 0.3177 | 0.3158 | -0.069 ± 0.0046 | -0.0533 (3) |
| 25-40 | 6137 | 0.217 | 0.1274 | +0.0896 ± 0.0029 | 0.6273 | 0.3903 | 0.5293 | 0.2138 | 0.2319 | -0.049 ± 0.0044 | -0.02 (4) |
| 40+ | 4058 | 0.3919 | 0.0494 | +0.3425 ± 0.0039 | 1.0218 | 0.1847 | 0.6406 | 0.1086 | 0.0658 | -0.076 ± 0.0033 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1417 | 0.1973 | 0.1974 | -0.0001 ± 0.0004 | 0.573 | 0.573 | 0.5084 | 0.4934 | 0.4996 | -0.067 ± 0.0121 | -0.0213 (54) |
| 3-5 | 1015 | 0.1885 | 0.1882 | +0.0003 ± 0.0011 | 0.555 | 0.5523 | 0.495 | 0.4552 | 0.47 | -0.059 ± 0.0139 | -0.0194 (34) |
| 5-10 | 2054 | 0.199 | 0.1946 | +0.0044 ± 0.0015 | 0.5872 | 0.572 | 0.507 | 0.4334 | 0.4406 | -0.074 ± 0.01 | -0.005 (78) |
| 10-15 | 1415 | 0.2137 | 0.2015 | +0.0122 ± 0.003 | 0.6206 | 0.5866 | 0.5421 | 0.4193 | 0.4297 | -0.089 ± 0.0123 | 0.0014 (65) |
| 15-25 | 1833 | 0.2302 | 0.2069 | +0.0233 ± 0.0042 | 0.6572 | 0.5975 | 0.5892 | 0.3942 | 0.4343 | -0.088 ± 0.0107 | -0.0214 (59) |
| 25-40 | 1113 | 0.2399 | 0.2097 | +0.0302 ± 0.0084 | 0.6853 | 0.6022 | 0.6881 | 0.3759 | 0.4834 | -0.088 ± 0.0129 | -0.0252 (27) |
| 40+ | 394 | 0.3272 | 0.2019 | +0.1254 ± 0.0216 | 0.9427 | 0.5874 | 0.8158 | 0.3398 | 0.4619 | -0.098 ± 0.0203 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5215 | 0.1776 | 0.1778 | -0.0002 ± 0.0002 | 0.5256 | 0.5255 | 0.5121 | 0.4968 | 0.5093 | -0.036 ± 0.0059 | -0.0145 (98) |
| 3-5 | 3600 | 0.1954 | 0.1947 | +0.0008 ± 0.0006 | 0.5698 | 0.5673 | 0.5002 | 0.4605 | 0.4708 | -0.040 ± 0.0074 | -0.0204 (72) |
| 5-10 | 7321 | 0.196 | 0.1898 | +0.0063 ± 0.0008 | 0.5787 | 0.5595 | 0.5007 | 0.4271 | 0.4226 | -0.061 ± 0.0051 | -0.0084 (134) |
| 10-15 | 5022 | 0.2084 | 0.1928 | +0.0156 ± 0.0015 | 0.6073 | 0.5662 | 0.537 | 0.4141 | 0.4108 | -0.070 ± 0.0063 | -0.0053 (106) |
| 15-25 | 6094 | 0.2301 | 0.1992 | +0.0309 ± 0.0023 | 0.6615 | 0.5775 | 0.5751 | 0.3797 | 0.3992 | -0.066 ± 0.0058 | -0.026 (108) |
| 25-40 | 4004 | 0.2567 | 0.1893 | +0.0673 ± 0.0043 | 0.7265 | 0.5519 | 0.6393 | 0.3267 | 0.3779 | -0.067 ± 0.0067 | -0.0246 (52) |
| 40+ | 1765 | 0.3706 | 0.1596 | +0.2111 ± 0.0098 | 1.0464 | 0.475 | 0.7438 | 0.2431 | 0.2929 | -0.064 ± 0.0091 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 7001 | 1.032 ± 0.033 | 1.107 | 0.1694 | 0.1694 | 0.2143 | 0.2033 |
| gen2 | 7001 | 0.826 ± 0.03 | 1.078 | 0.1737 | 0.1698 | 0.2327 | 0.2032 |
| gen1_elo | 7001 | 1.011 ± 0.032 | 1.097 | 0.1759 | 0.1695 | 0.2135 | 0.2034 |
| gen1_sr | 7001 | 1.01 ± 0.039 | 1.137 | 0.1336 | 0.1714 | 0.229 | 0.2028 |
| gen1_ledger | 9241 | 0.868 ± 0.024 | 1.077 | 0.1901 | 0.1765 | 0.2164 | 0.2 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 32,788)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 7,582 | 23.1% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,373 | 22.5% |
| BOOK_QUALITY | execution | 5,909 | 18.0% |
| POOR_DATA | data | 3,822 | 11.7% |
| LIMITED_DATA | data | 2,036 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,880 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,357 | 4.1% |
| IDENTITY_AMBIGUOUS | mapping | 1,348 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 936 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 544 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 23.1%, coverage 22.5%, execution 18.0%, data 17.9%, market_freshness/coverage 8.6%, model_calibration_or_unknown 4.1%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.5%, LOW_DATA_QUALITY 71.6%, THIN_PLAYER_HISTORY 59.9%, STALE_PLAYER_DATA 52.1%, STALE_KALSHI_QUOTE 45.9%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 24.2%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 15.3%, LEVEL_TRANSFER_RISK 10.1%, LOW_DISPLAYED_LIQUIDITY 8.4%, EVENT_MAPPING_RISK 7.2%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.9%, POST_SETTLEMENT_OBSERVATION 22.5%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 17,409)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,907 | 33.9% |
| STALE_QUOTE | market_freshness | 3,390 | 19.5% |
| BOOK_QUALITY | execution | 3,067 | 17.6% |
| POOR_DATA | data | 1,613 | 9.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,004 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 750 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 613 | 3.5% |
| LIMITED_DATA | data | 597 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 334 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 133 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.9%, market_freshness 19.5%, execution 17.6%, data 12.7%, market_freshness/coverage 9.3%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 75.0%, THIN_PLAYER_HISTORY 61.9%, STALE_KALSHI_QUOTE 53.3%, STALE_PLAYER_DATA 45.9%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 23.7%, MODEL_HIGH_UNCERTAINTY 19.3%, PLAYER_IDENTITY_RISK 18.4%, LEVEL_TRANSFER_RISK 8.9%, EVENT_MAPPING_RISK 8.9%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.0%, POST_SETTLEMENT_OBSERVATION 33.9%, POSSIBLE_IN_PLAY_QUOTE 6.2%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 13873, "IDENTITY_AMBIGUOUS": 3536}; ticker orientation: {"VERIFIED": 17409}.

Checks: discipline:AMBIGUOUS 1174, discipline:PASS 16235, identity_confidence:AMBIGUOUS 3206, identity_confidence:PASS 14203, level_mapping:NA 1186, level_mapping:PASS 16223, market_pair:AMBIGUOUS 491, market_pair:NA 378, market_pair:PASS 16540, model_complement:NA 340, model_complement:PASS 17069, namesake:AMBIGUOUS 6, namesake:PASS 17403, physical_match_id:NA 5954, physical_match_id:PASS 11455, player_ids:PASS 17409, same_pair_other_event:PASS 17409, ticker_orientation:PASS 17409

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,255 | 3.8% | 3.3% | 1.4% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 21, "market_freshness/coverage": 17} | 5.52 | 0.2264 / 0.2215 (793) | 24.6% | 2.5% | 3.1% | 2.8% |
| CHALLENGER | 11,432 | 16.2% | 6.2% | 10.7% | {"coverage": 1090, "market_freshness/coverage": 218, "market_freshness": 216, "data": 157, "model_calibration_or_unknown": 78, "execution": 41, "model_calibration": 36, "mapping": 17, "possible_market_error": 1} | 7.39 | 0.2194 / 0.2096 (2680) | 37.8% | 15.4% | 4.1% | 22.3% |
| DOUBLES | 2,526 | 46.5% | 46.4% | 6.7% | {"execution": 662, "mapping": 332, "market_freshness": 106, "market_freshness/coverage": 67, "coverage": 7} | 23.23 | 0.2976 / 0.2337 (620) | 9.3% | 0.0% | 100.0% | 6.2% |
| ITF_MEN | 22,881 | 24.8% | 17.4% | 32.5% | {"coverage": 1963, "market_freshness": 1106, "execution": 977, "data": 838, "market_freshness/coverage": 568, "mapping": 204, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.67 | 0.2155 / 0.1983 (4817) | 39.7% | 69.0% | 15.2% | 21.3% |
| ITF_WOMEN | 29,843 | 26.4% | 18.9% | 45.3% | {"coverage": 2771, "market_freshness": 1702, "execution": 1304, "data": 1114, "market_freshness/coverage": 690, "mapping": 191, "model_calibration_or_unknown": 92, "model_calibration": 22} | 12.5 | 0.2031 / 0.1934 (5752) | 40.9% | 57.2% | 9.8% | 21.6% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,786 | 6.0% | 5.1% | 1.7% | {"market_freshness": 110, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 21, "market_freshness/coverage": 13, "mapping": 1} | 7.69 | 0.2299 / 0.2206 (768) | 29.8% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.7% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 523 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.4h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 509 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 773 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 628 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 12 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 21.3h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 1282 min (STALE); no external reference |
| 15 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 16 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 18 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 19 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 20 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 21 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 22 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 23 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 24 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 25 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 163 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 26 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 27 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 28 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 29 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 30 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 31 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 32 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 33 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 34 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 35 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 36 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 37 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 38 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 39 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 40 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 41 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 768 min (STALE); no external reference |
| 43 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 44 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 45 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 46 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 379 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 49 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 50 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.3h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 748 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9697, "by_level_share_of_ge_25pp": {"ATP": 0.0136, "CHALLENGER": 0.1065, "DOUBLES": 0.0674, "ITF_MEN": 0.3253, "ITF_WOMEN": 0.453, "OTHER": 0.0007, "WTA": 0.0166, "WTA125": 0.0168}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5333, "share_primary_cause_market_settled_or_in_play": 0.4322, "share_primary_cause_stale_quote_only": 0.1947}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 17409, "identity_ambiguous_share": 0.2031, "ticker_orientation": {"VERIFIED": 17409}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 11455, "with_external": 609, "coverage": 0.0532, "external_status": {"EXTERNAL_STALE": 390, "AGREES_WITH_KALSHI": 206, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 390, "MODEL_LONE_OUTLIER": 206, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3383, "share_external_supports_model": 0.0213}, "pregame_clean_ge_25pp": {"n": 5410, "with_external": 579, "coverage": 0.107, "external_status": {"EXTERNAL_STALE": 367, "AGREES_WITH_KALSHI": 199, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 367, "MODEL_LONE_OUTLIER": 199, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3437, "share_external_supports_model": 0.0225}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 490.0, "median_sample_ratio": 2.46, "median_min_matches": 19.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2087, "data_status": {"POOR": 9784, "LIMITED": 4523, "ADEQUATE": 3102}, "comparison_lt_10pp": {"median_thinner_serve_points": 1719.0, "median_sample_ratio": 1.7, "median_min_matches": 90.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1414, "model_minus_observed": 0.0576, "kalshi_minus_observed": -0.0818, "brier_diff_model_minus_kalshi": 0.0004}, "4-10x": {"n": 966, "model_minus_observed": 0.0897, "kalshi_minus_observed": -0.0551, "brier_diff_model_minus_kalshi": 0.0092}, "<2x": {"n": 3433, "model_minus_observed": 0.1, "kalshi_minus_observed": -0.023, "brier_diff_model_minus_kalshi": 0.0145}, ">=10x": {"n": 1188, "model_minus_observed": 0.1169, "kalshi_minus_observed": -0.0563, "brier_diff_model_minus_kalshi": 0.0148}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 7001, "model": {"intercept": -0.556, "slope": 0.826, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.188, "slope": 1.078, "slope_se": 0.034}, "mean_extremity_model": 0.1737, "mean_extremity_kalshi": 0.1698, "model_brier": 0.2327, "kalshi_brier": 0.2032, "brier_diff_model_minus_kalshi": 0.0296, "brier_diff_se": 0.0023, "model_logloss": 0.6626, "kalshi_logloss": 0.5886}, "fair_v1": {"n": 7001, "model": {"intercept": -0.447, "slope": 1.032, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.256, "slope": 1.107, "slope_se": 0.034}, "mean_extremity_model": 0.1694, "mean_extremity_kalshi": 0.1694, "model_brier": 0.2143, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.011, "brier_diff_se": 0.0018, "model_logloss": 0.6174, "kalshi_logloss": 0.5888}, "gen1_elo": {"n": 7001, "model": {"intercept": -0.435, "slope": 1.011, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.257, "slope": 1.097, "slope_se": 0.034}, "mean_extremity_model": 0.1759, "mean_extremity_kalshi": 0.1695, "model_brier": 0.2135, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": 0.0101, "brier_diff_se": 0.0018, "model_logloss": 0.6163, "kalshi_logloss": 0.589}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2466, "share_ge_15": 0.4428, "median_abs_gap": 13.02, "n": 46447}, "gen1_elo": {"share_ge_25": 0.2434, "share_ge_15": 0.4388, "median_abs_gap": 12.77, "n": 46447}, "gen1_sr": {"share_ge_25": 0.3126, "share_ge_15": 0.5197, "median_abs_gap": 15.78, "n": 46447}, "gen2": {"share_ge_25": 0.3128, "share_ge_15": 0.5094, "median_abs_gap": 15.43, "n": 46447}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1508, "share_ge_15": 0.3533, "median_abs_gap": 10.7, "n": 35866}, "gen1_elo": {"share_ge_25": 0.1485, "share_ge_15": 0.3484, "median_abs_gap": 10.49, "n": 35866}, "gen1_sr": {"share_ge_25": 0.2163, "share_ge_15": 0.4397, "median_abs_gap": 13.0, "n": 35868}, "gen2": {"share_ge_25": 0.2306, "share_ge_15": 0.4387, "median_abs_gap": 12.85, "n": 35868}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.52, "share_ge_25_all": 0.0379, "share_ge_25_pregame_clean": 0.0327}, "WTA": {"median_abs_gap_pregame_clean": 7.69, "share_ge_25_all": 0.0604, "share_ge_25_pregame_clean": 0.0512}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.237, "share_within_10pp_all": 0.4393, "share_within_10pp_pregame_clean": 0.4918, "corr_model_vs_mid_pregame_clean": 0.8513}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1005, "model_brier": 0.197, "kalshi_brier": 0.1974, "brier_diff_model_minus_kalshi": -0.0003}, "10-15": {"n_settled": 1214, "model_brier": 0.2184, "kalshi_brier": 0.2091, "brier_diff_model_minus_kalshi": 0.0093}, "15-25": {"n_settled": 1552, "model_brier": 0.2245, "kalshi_brier": 0.208, "brier_diff_model_minus_kalshi": 0.0165}, "25-40": {"n_settled": 891, "model_brier": 0.2223, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0185}, "3-5": {"n_settled": 645, "model_brier": 0.2049, "kalshi_brier": 0.2049, "brier_diff_model_minus_kalshi": -0.0}, "40+": {"n_settled": 186, "model_brier": 0.2966, "kalshi_brier": 0.1748, "brier_diff_model_minus_kalshi": 0.1217}, "5-10": {"n_settled": 1508, "model_brier": 0.201, "kalshi_brier": 0.2003, "brier_diff_model_minus_kalshi": 0.0007}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.556, "slope": 0.826, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.188, "slope": 1.078, "slope_se": 0.034}, "n": 7001}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.483, "slope": 0.868, "slope_se": 0.024}, "kalshi_slope": {"intercept": 0.179, "slope": 1.077, "slope_se": 0.029}, "n": 9241}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 620, "model_brier": 0.2976, "kalshi_brier": 0.2337, "brier_diff_model_minus_kalshi": 0.0639, "brier_diff_se": 0.0118, "corr_model_outcome": 0.0972, "corr_kalshi_outcome": 0.2717}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
