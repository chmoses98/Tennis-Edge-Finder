# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-09T03:06Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 25,869): 0-3 14.1%, 3-5 9.5%, 5-10 19.8%, 10-15 15.5%, 15-25 18.6%, 25-40 14.0%, 40+ 8.5%; median gap 12.0 pp.
* **Where the extremes live**: 98.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.1%, Challenger 12.2%, doubles 6.6%). Main tour: ATP 1.6% and WTA 8.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 5,808): MARKET_ALREADY_SETTLED_WHEN_PRICED 39.6%, STALE_QUOTE 17.2%, BOOK_QUALITY 16.9%, POOR_DATA 7.9%, POSSIBLY_IN_PLAY_QUOTE 5.5%, LIMITED_DATA 4.3%, IN_PLAY_QUOTE 3.5%, IDENTITY_AMBIGUOUS 3.2%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.2%. By class: coverage 39.6%, market_freshness 17.2%, execution 16.9%, data 12.2%, market_freshness/coverage 9.0%, mapping 3.2%, model_calibration_or_unknown 1.9%, model_calibration 0.2%.
* **Stale / settled / in-play**: 55.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 48.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 5,808 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 16.9% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 2.1%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 14.5% of the time and with the model 0.3%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 623.0 points vs 1761.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.1, Gen-2 0.879, Gen-1 ledger 0.921 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 242 model 0.217 vs Kalshi 0.2014; n 53 model 0.2878 vs Kalshi 0.1771.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 98,529 model-market comparisons (164,531 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 37,192 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-09T03:00:30.150945+00:00'], shadow board 27,054 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-09T03:00:33.006840+00:00'], Model 4 10,292 rows, 11,184 settled tickers, 3,039 tickers with an external scan.
* By model: {"gen1_ledger": 23860, "gen1_elo": 13594, "fair_v1": 13594, "gen2": 13594, "gen1_sr": 13594, "model4_fundamental": 10151, "model4_conditioned": 10142}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 25,869 | 14.1 | 9.5 | 19.8 | 15.5 | 18.6 | 14.0 | 8.5 | 12.0 | 41.0% | 22.4% |
| MW fair_v1 | 13,594 | 13.4 | 8.7 | 18.3 | 16.3 | 18.4 | 14.8 | 10.2 | 12.94 | 43.4% | 25.0% |
| MW gen1_elo | 13,594 | 12.9 | 8.8 | 20.0 | 14.9 | 19.1 | 14.6 | 9.6 | 12.51 | 43.3% | 24.2% |
| MW gen1_ledger | 12,275 | 14.9 | 10.5 | 21.6 | 14.6 | 18.8 | 13.0 | 6.6 | 10.83 | 38.4% | 19.6% |
| MW gen1_sr | 13,594 | 10.2 | 7.8 | 16.1 | 14.1 | 21.4 | 18.5 | 11.9 | 15.61 | 51.8% | 30.3% |
| MW gen2 | 13,594 | 12.1 | 7.2 | 16.1 | 14.3 | 19.7 | 17.3 | 13.3 | 15.22 | 50.4% | 30.7% |
| all families model4_conditioned | 10,142 | 22.2 | 20.5 | 35.7 | 15.9 | 4.1 | 0.9 | 0.8 | 5.68 | 5.7% | 1.7% |
| all families model4_fundamental | 10,151 | 16.6 | 13.2 | 35.4 | 20.2 | 10.8 | 2.8 | 1.1 | 7.67 | 14.6% | 3.8% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.5%, >=15pp 41.0%, >=20pp 30.7%, >=25pp 22.4%, >=30pp 16.4%, >=40pp 8.5%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.53pp; >=10pp 45.7%, >=25pp 18.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,020 | 28.2 | 15.0 | 24.5 | 17.6 | 12.2 | 1.3 | 1.1 | 5.95 | 14.6% | 2.4% |
| CHALLENGER | 2,290 | 15.5 | 10.7 | 18.6 | 16.2 | 12.9 | 13.1 | 13.0 | 11.9 | 39.0% | 26.1% |
| ITF_MEN | 3,931 | 11.1 | 8.7 | 18.5 | 15.0 | 19.2 | 15.0 | 12.5 | 13.75 | 46.7% | 27.5% |
| ITF_WOMEN | 5,475 | 10.4 | 6.7 | 15.9 | 16.4 | 21.6 | 18.7 | 10.4 | 15.3 | 50.7% | 29.1% |
| WTA | 546 | 24.4 | 9.3 | 25.5 | 15.9 | 16.9 | 6.0 | 2.0 | 7.87 | 24.9% | 8.1% |
| WTA125 | 332 | 11.8 | 6.3 | 21.7 | 26.2 | 15.4 | 16.3 | 2.4 | 11.4 | 34.0% | 18.7% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,020 | 22.8 | 13.9 | 24.6 | 18.5 | 16.7 | 2.2 | 1.3 | 6.9 | 20.1% | 3.4% |
| CHALLENGER | 2,290 | 15.3 | 7.5 | 17.9 | 13.4 | 18.1 | 14.4 | 13.4 | 13.14 | 45.9% | 27.8% |
| ITF_MEN | 3,931 | 10.6 | 7.5 | 16.9 | 14.8 | 19.9 | 17.3 | 13.1 | 15.25 | 50.3% | 30.4% |
| ITF_WOMEN | 5,475 | 9.2 | 6.0 | 12.9 | 13.1 | 20.6 | 21.3 | 17.0 | 18.92 | 58.9% | 38.3% |
| WTA | 546 | 22.5 | 5.3 | 18.7 | 14.8 | 20.7 | 15.9 | 2.0 | 11.74 | 38.6% | 17.9% |
| WTA125 | 332 | 4.5 | 2.7 | 17.2 | 21.1 | 22.0 | 21.1 | 11.4 | 17.24 | 54.5% | 32.5% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,020 | 26.1 | 13.3 | 29.5 | 15.6 | 11.3 | 3.0 | 1.2 | 6.53 | 15.5% | 4.2% |
| CHALLENGER | 2,290 | 16.0 | 10.6 | 20.0 | 14.2 | 14.0 | 12.2 | 13.0 | 10.97 | 39.2% | 25.2% |
| ITF_MEN | 3,931 | 10.2 | 8.8 | 18.8 | 14.0 | 20.2 | 15.5 | 12.5 | 14.13 | 48.2% | 28.0% |
| ITF_WOMEN | 5,475 | 9.6 | 6.7 | 16.8 | 15.7 | 23.2 | 18.7 | 9.2 | 15.48 | 51.1% | 27.9% |
| WTA | 546 | 23.3 | 12.8 | 35.7 | 14.3 | 9.2 | 3.5 | 1.3 | 6.87 | 13.9% | 4.8% |
| WTA125 | 332 | 21.4 | 11.4 | 30.7 | 16.9 | 14.2 | 4.8 | 0.6 | 7.99 | 19.6% | 5.4% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 547 | 29.6 | 22.7 | 36.2 | 10.1 | 1.3 | 0.2 | 0.0 | 4.8 | 1.5% | 0.2% |
| CHALLENGER | 1,484 | 23.4 | 17.2 | 25.7 | 13.9 | 12.2 | 5.5 | 2.0 | 6.56 | 19.7% | 7.5% |
| DOUBLES | 763 | 3.9 | 3.4 | 10.9 | 11.3 | 20.1 | 24.6 | 25.8 | 25.42 | 70.5% | 50.5% |
| ITF_MEN | 3,850 | 14.7 | 8.6 | 20.9 | 15.1 | 20.3 | 12.6 | 7.8 | 11.84 | 40.7% | 20.4% |
| ITF_WOMEN | 4,536 | 11.6 | 9.3 | 19.8 | 14.4 | 22.3 | 16.8 | 5.8 | 13.04 | 44.8% | 22.5% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 444 | 21.2 | 11.5 | 25.4 | 18.7 | 15.3 | 7.2 | 0.7 | 8.42 | 23.2% | 7.9% |
| WTA125 | 502 | 16.5 | 12.8 | 22.5 | 20.1 | 16.5 | 8.8 | 2.8 | 9.35 | 28.1% | 11.6% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,015 | 28.3 | 14.9 | 24.5 | 17.7 | 12.2 | 1.3 | 1.1 | 5.96 | 14.6% | 2.4% |
| CHALLENGER | 1,609 | 20.5 | 13.8 | 23.9 | 19.1 | 13.2 | 6.6 | 2.8 | 7.99 | 22.6% | 9.4% |
| ITF_MEN | 2,795 | 13.8 | 10.9 | 22.0 | 16.7 | 19.2 | 12.1 | 5.2 | 10.9 | 36.5% | 17.3% |
| ITF_WOMEN | 3,894 | 12.9 | 8.4 | 18.7 | 18.8 | 23.1 | 14.9 | 3.2 | 12.61 | 41.2% | 18.1% |
| WTA | 543 | 24.3 | 9.4 | 25.6 | 15.8 | 16.9 | 5.9 | 2.0 | 7.85 | 24.9% | 7.9% |
| WTA125 | 319 | 12.2 | 6.6 | 21.0 | 26.6 | 15.7 | 16.3 | 1.6 | 11.33 | 33.5% | 17.9% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,015 | 22.8 | 13.9 | 24.7 | 18.5 | 16.6 | 2.2 | 1.3 | 6.9 | 20.1% | 3.5% |
| CHALLENGER | 1,609 | 20.2 | 9.9 | 22.7 | 16.5 | 18.5 | 9.6 | 2.7 | 9.08 | 30.8% | 12.2% |
| ITF_MEN | 2,796 | 12.6 | 9.1 | 19.5 | 16.6 | 21.2 | 14.9 | 6.0 | 12.46 | 42.2% | 21.0% |
| ITF_WOMEN | 3,894 | 10.7 | 7.1 | 14.6 | 14.2 | 23.0 | 20.2 | 10.1 | 16.24 | 53.3% | 30.3% |
| WTA | 543 | 22.5 | 5.3 | 18.8 | 14.9 | 20.6 | 15.8 | 2.0 | 11.73 | 38.5% | 17.9% |
| WTA125 | 319 | 4.7 | 2.8 | 17.2 | 21.9 | 21.3 | 21.6 | 10.3 | 16.84 | 53.3% | 32.0% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 532 | 29.9 | 22.9 | 36.3 | 10.2 | 0.6 | 0.2 | 0.0 | 4.79 | 0.8% | 0.2% |
| CHALLENGER | 1,254 | 25.6 | 19.5 | 27.9 | 13.6 | 11.2 | 2.1 | 0.1 | 5.8 | 13.4% | 2.1% |
| DOUBLES | 703 | 3.8 | 3.4 | 11.1 | 11.2 | 20.3 | 24.3 | 25.8 | 25.29 | 70.4% | 50.1% |
| ITF_MEN | 3,093 | 16.4 | 9.5 | 23.2 | 16.2 | 20.1 | 10.2 | 4.5 | 10.21 | 34.7% | 14.6% |
| ITF_WOMEN | 3,682 | 12.8 | 10.1 | 21.8 | 15.3 | 22.6 | 15.0 | 2.4 | 11.42 | 40.0% | 17.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 414 | 21.7 | 12.1 | 26.1 | 18.8 | 15.7 | 5.6 | 0.0 | 8.3 | 21.3% | 5.6% |
| WTA125 | 417 | 18.5 | 14.2 | 24.9 | 23.0 | 14.6 | 4.6 | 0.2 | 8.22 | 19.4% | 4.8% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 763 | 3.9 | 3.4 | 10.9 | 11.3 | 20.1 | 24.6 | 25.8 | 25.42 | 70.5% | 50.5% |
| singles | 11,512 | 15.7 | 11.0 | 22.3 | 14.8 | 18.7 | 12.3 | 5.3 | 10.26 | 36.3% | 17.6% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 3,146 | 13.4 | 9.5 | 20.2 | 15.7 | 16.1 | 14.5 | 10.5 | 12.22 | 41.1% | 25.0% |
| Hard | 9,105 | 13.6 | 8.4 | 18.1 | 16.2 | 19.0 | 14.6 | 10.1 | 12.99 | 43.6% | 24.7% |
| UNKNOWN | 1,343 | 11.7 | 8.0 | 14.8 | 18.0 | 20.2 | 16.9 | 10.3 | 14.11 | 47.4% | 27.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,936 | 19.5 | 10.7 | 20.3 | 17.2 | 14.7 | 9.6 | 8.2 | 9.94 | 32.4% | 17.7% |
| B | 1,803 | 15.1 | 9.4 | 19.6 | 17.5 | 16.6 | 11.8 | 9.9 | 11.28 | 38.3% | 21.7% |
| C | 2,108 | 12.3 | 10.0 | 19.6 | 15.4 | 18.4 | 14.7 | 9.5 | 12.69 | 42.6% | 24.2% |
| D | 2,587 | 10.9 | 8.3 | 17.3 | 16.4 | 22.1 | 15.0 | 9.9 | 14.02 | 47.1% | 25.0% |
| F | 3,160 | 7.5 | 5.1 | 14.9 | 14.8 | 21.1 | 22.9 | 13.5 | 18.41 | 57.6% | 36.5% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,388 | 22.1 | 15.6 | 27.6 | 15.6 | 12.1 | 5.1 | 1.9 | 6.95 | 19.2% | 7.0% |
| B | 1,933 | 14.5 | 9.7 | 24.6 | 16.2 | 18.5 | 11.7 | 4.7 | 10.34 | 34.9% | 16.4% |
| C | 2,513 | 11.9 | 8.0 | 18.2 | 14.1 | 20.8 | 15.8 | 11.1 | 13.77 | 47.7% | 26.9% |
| D | 2,046 | 13.9 | 9.2 | 21.3 | 13.0 | 22.0 | 14.2 | 6.3 | 12.08 | 42.6% | 20.5% |
| F | 2,395 | 9.2 | 7.8 | 14.2 | 13.6 | 23.5 | 21.4 | 10.2 | 16.91 | 55.1% | 31.6% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 4,456 | 18.1 | 9.8 | 19.5 | 17.3 | 15.0 | 10.0 | 10.2 | 10.69 | 35.3% | 20.2% |
| LIMITED | 3,350 | 14.6 | 10.5 | 20.7 | 16.1 | 17.5 | 13.4 | 7.2 | 11.31 | 38.1% | 20.7% |
| POOR | 5,788 | 9.1 | 6.6 | 16.0 | 15.6 | 21.6 | 19.3 | 11.9 | 16.06 | 52.8% | 31.2% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,276 | 30.0 | 25.1 | 37.6 | 5.5 | 1.6 | 0.3 | 0.0 | 4.54 | 1.9% | 0.3% |
| GAME_SPREAD | 2,175 | 24.9 | 15.6 | 36.9 | 17.7 | 4.5 | 0.2 | 0.1 | 6.14 | 4.9% | 0.4% |
| MATCH_WINNER | 12,275 | 14.9 | 10.5 | 21.6 | 14.6 | 18.8 | 13.0 | 6.6 | 10.83 | 38.4% | 19.6% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 3,962 | 31.3 | 19.9 | 30.5 | 10.3 | 6.5 | 1.2 | 0.3 | 4.84 | 8.0% | 1.5% |
| TOTAL_GAMES | 3,148 | 7.2 | 9.0 | 38.7 | 30.6 | 9.3 | 3.0 | 2.1 | 9.45 | 14.4% | 5.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,772 | 24.4 | 38.6 | 31.0 | 0.3 | 4.9 | 0.6 | 0.2 | 4.34 | 5.7% | 0.7% |
| GAME_SPREAD | 2,622 | 46.0 | 14.4 | 29.2 | 8.2 | 1.2 | 0.8 | 0.3 | 3.54 | 2.2% | 1.0% |
| TOTAL_GAMES | 3,748 | 3.3 | 6.4 | 44.9 | 37.1 | 5.3 | 1.2 | 1.8 | 9.58 | 8.3% | 3.0% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,772 | 25.6 | 18.2 | 36.2 | 9.8 | 7.1 | 2.7 | 0.4 | 5.62 | 10.2% | 3.1% |
| GAME_SPREAD | 2,622 | 18.8 | 13.1 | 27.8 | 22.4 | 14.5 | 2.8 | 0.7 | 8.23 | 18.0% | 3.4% |
| TOTAL_GAMES | 3,757 | 6.1 | 8.3 | 39.8 | 29.1 | 11.8 | 2.8 | 2.1 | 9.57 | 16.7% | 4.9% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 13,594 | 43.4% | 25.0% | 12.94 | 33.2% | 14.4% | 10.37 |
| gen1_elo | 13,594 | 43.3% | 24.2% | 12.51 | 32.8% | 13.9% | 9.85 |
| gen1_sr | 13,594 | 51.8% | 30.3% | 15.61 | 42.7% | 19.9% | 12.7 |
| gen2 | 13,594 | 50.4% | 30.7% | 15.22 | 42.6% | 21.6% | 12.59 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 6,788 | 16.3 | 11.0 | 21.4 | 17.6 | 18.6 | 11.7 | 3.5 | 10.36 | 33.8% | 15.2% |
| STALE | 6,806 | 10.5 | 6.3 | 15.2 | 14.9 | 18.3 | 17.9 | 16.9 | 16.7 | 53.1% | 34.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 5,743 | 17.0 | 11.7 | 23.6 | 14.4 | 16.8 | 11.8 | 4.7 | 9.38 | 33.3% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 25,869 | 5743 | 10260 | 9866 | 25.1 | 166.6 | 1400.4 |
| ge_15pp | 10,617 | 1915 | 3580 | 5122 | 28.8 | 455.5 | 1380.4 |
| ge_25pp | 5,808 | 948 | 1622 | 3238 | 37.9 | 574.8 | 1380.4 |
| lt_10pp | 11,253 | 3003 | 4933 | 3317 | 23.7 | 49.8 | 1230.8 |

Current slate `SL-20261009T030625Z-0f2bac21`: 658 priced rows, quote age at build {'median': 6.3, 'max': 6.4}, freshness {'FRESH': 658}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 4 | 0.0 | 0.0 | 25.0 | 0.0 | 75.0 | 0.0 | 0.0 | 20.45 | 75.0% | 0.0% |
| EXTERNAL_LONE_OUTLIER | 3 | 33.3 | 66.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 3.05 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 732 | 24.9 | 11.3 | 20.8 | 20.6 | 14.8 | 7.2 | 0.4 | 7.98 | 22.4% | 7.6% |
| MARKETS_AGREE | 76 | 79.0 | 21.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.99 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 138 | 0.0 | 2.9 | 32.6 | 32.6 | 21.7 | 10.1 | 0.0 | 11.87 | 31.9% | 10.1% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 13,594 | 953 (7.0%) | 14.5% | 0.3% | {"EXTERNAL_STALE": 732, "AGREES_WITH_KALSHI": 138, "ALL_AGREE": 76, "SUPPORTS_MODEL_DIRECTION": 3, "EXTERNAL_OUTLIER": 3, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 5,903 | 211 (3.6%) | 20.8% | 1.4% | {"EXTERNAL_STALE": 164, "AGREES_WITH_KALSHI": 44, "SUPPORTS_MODEL_DIRECTION": 3} |
| fair_v1_ge_25pp | 3,398 | 70 (2.1%) | 20.0% | 0.0% | {"EXTERNAL_STALE": 56, "AGREES_WITH_KALSHI": 14} |
| fair_v1_ge_25pp_pregame_clean | 1,463 | 68 (4.7%) | 20.6% | 0.0% | {"EXTERNAL_STALE": 54, "AGREES_WITH_KALSHI": 14} |
| fair_v1_lt_10pp | 5,481 | 546 (10.0%) | 9.0% | 0.0% | {"EXTERNAL_STALE": 417, "ALL_AGREE": 76, "AGREES_WITH_KALSHI": 49, "EXTERNAL_OUTLIER": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 2,787 | 11.6 | 8.4 | 19.6 | 15.6 | 20.9 | 13.9 | 10.0 | 13.06 | 44.8% | 23.9% |
| 4-10x | 1,934 | 11.2 | 9.2 | 18.4 | 15.2 | 20.1 | 16.8 | 9.2 | 13.65 | 46.0% | 26.0% |
| <2x | 7,137 | 15.4 | 9.2 | 18.3 | 17.3 | 16.6 | 13.2 | 9.9 | 12.05 | 39.8% | 23.2% |
| >=10x | 1,736 | 10.4 | 6.4 | 15.7 | 14.5 | 19.9 | 20.6 | 12.6 | 16.48 | 53.0% | 33.2% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 3,533 | 14.2 | 8.6 | 19.4 | 16.0 | 17.8 | 12.9 | 11.0 | 12.17 | 41.8% | 23.9% |
| 300-1000 | 3,365 | 11.8 | 9.1 | 16.6 | 16.4 | 20.9 | 16.1 | 9.2 | 13.74 | 46.1% | 25.2% |
| <300 | 3,648 | 8.1 | 6.0 | 15.8 | 14.9 | 21.1 | 21.0 | 13.1 | 17.2 | 55.2% | 34.1% |
| >=3000 | 3,048 | 20.6 | 11.4 | 21.8 | 17.9 | 13.2 | 8.2 | 6.9 | 8.93 | 28.3% | 15.1% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 432 | 0.5418 | 0.4097 | 0.4884 | +0.053 | -0.079 | 0.0014 ± 0.0071 |
| ratio 4-10x | 304 | 0.5817 | 0.4399 | 0.523 | +0.059 | -0.083 | -0.0024 ± 0.009 |
| ratio <2x | 915 | 0.5436 | 0.4185 | 0.459 | +0.085 | -0.041 | 0.0112 ± 0.0048 |
| ratio >=10x | 292 | 0.5481 | 0.3781 | 0.4384 | +0.110 | -0.060 | 0.0135 ± 0.0103 |
| thinner_sample 1000-3000 | 524 | 0.5474 | 0.4229 | 0.4695 | +0.078 | -0.047 | 0.0052 ± 0.0062 |
| thinner_sample 300-1000 | 536 | 0.5699 | 0.4291 | 0.5 | +0.070 | -0.071 | 0.0011 ± 0.0068 |
| thinner_sample <300 | 594 | 0.5429 | 0.3821 | 0.463 | +0.080 | -0.081 | 0.0089 ± 0.0069 |
| thinner_sample >=3000 | 289 | 0.5316 | 0.4342 | 0.4464 | +0.085 | -0.012 | 0.0192 ± 0.0068 |
| data_status ADEQUATE | 505 | 0.5302 | 0.4254 | 0.4436 | +0.087 | -0.018 | 0.0128 ± 0.0055 |
| data_status LIMITED | 499 | 0.5646 | 0.4321 | 0.499 | +0.066 | -0.067 | 0.0001 ± 0.0068 |
| data_status POOR | 939 | 0.5526 | 0.3979 | 0.4739 | +0.079 | -0.076 | 0.0081 ± 0.0054 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 292 | 0.1862 | 0.1875 | -0.0013 ± 0.0009 | 0.5482 | 0.5515 | 0.4917 | 0.4771 | 0.5171 | -0.069 ± 0.0266 | -0.01 (3) |
| 3-5 | 197 | 0.1865 | 0.1874 | -0.0009 ± 0.0025 | 0.5522 | 0.5522 | 0.5145 | 0.4745 | 0.5025 | -0.070 ± 0.0313 | 0.02 (1) |
| 5-10 | 398 | 0.2012 | 0.2034 | -0.0022 ± 0.0034 | 0.5891 | 0.5941 | 0.5217 | 0.4477 | 0.4899 | -0.087 ± 0.0236 | -0.0125 (4) |
| 10-15 | 345 | 0.2127 | 0.2076 | +0.0051 ± 0.0062 | 0.612 | 0.5963 | 0.5226 | 0.3984 | 0.4377 | -0.093 ± 0.0246 | -0.0633 (3) |
| 15-25 | 416 | 0.2227 | 0.2127 | +0.0100 ± 0.0088 | 0.637 | 0.6132 | 0.5736 | 0.378 | 0.4495 | -0.082 ± 0.0226 | -0.0133 (6) |
| 25-40 | 242 | 0.217 | 0.2014 | +0.0156 ± 0.0171 | 0.6232 | 0.5781 | 0.6473 | 0.3383 | 0.4669 | -0.070 ± 0.0256 | -0.01 (1) |
| 40+ | 53 | 0.2878 | 0.1771 | +0.1107 ± 0.0514 | 0.7805 | 0.5305 | 0.7594 | 0.311 | 0.4151 | -0.127 ± 0.0502 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1437 | 0.1673 | 0.1681 | -0.0008 ± 0.0004 | 0.5032 | 0.5039 | 0.4722 | 0.4574 | 0.4934 | -0.027 ± 0.011 | -0.0188 (8) |
| 3-5 | 956 | 0.191 | 0.1872 | +0.0039 ± 0.0011 | 0.563 | 0.548 | 0.479 | 0.4394 | 0.4069 | -0.093 ± 0.0142 | 0.02 (1) |
| 5-10 | 2036 | 0.193 | 0.1909 | +0.0021 ± 0.0014 | 0.5688 | 0.5616 | 0.4919 | 0.4182 | 0.4357 | -0.054 ± 0.0098 | -0.0082 (17) |
| 10-15 | 1853 | 0.1979 | 0.1815 | +0.0165 ± 0.0025 | 0.5798 | 0.5335 | 0.4717 | 0.3471 | 0.3432 | -0.074 ± 0.0099 | -0.0475 (4) |
| 15-25 | 2172 | 0.1999 | 0.1638 | +0.0361 ± 0.0034 | 0.5891 | 0.4882 | 0.4892 | 0.2932 | 0.2997 | -0.070 ± 0.0087 | -0.0048 (29) |
| 25-40 | 1835 | 0.2163 | 0.1236 | +0.0927 ± 0.0051 | 0.6247 | 0.3827 | 0.527 | 0.2135 | 0.2251 | -0.059 ± 0.0079 | -0.01 (1) |
| 40+ | 1269 | 0.3707 | 0.0455 | +0.3251 ± 0.0066 | 0.9666 | 0.1785 | 0.6227 | 0.1067 | 0.0599 | -0.083 ± 0.0057 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 228 | 0.1954 | 0.1956 | -0.0003 ± 0.001 | 0.5743 | 0.5752 | 0.4903 | 0.4751 | 0.4781 | -0.103 ± 0.031 | -0.01 (1) |
| 3-5 | 149 | 0.2036 | 0.2049 | -0.0014 ± 0.003 | 0.586 | 0.5915 | 0.52 | 0.48 | 0.5101 | -0.060 ± 0.039 | 0.02 (1) |
| 5-10 | 334 | 0.1928 | 0.1898 | +0.0030 ± 0.0036 | 0.5674 | 0.5607 | 0.5674 | 0.4924 | 0.506 | -0.100 ± 0.0247 | -0.01 (4) |
| 10-15 | 332 | 0.217 | 0.2109 | +0.0060 ± 0.0063 | 0.6201 | 0.6089 | 0.5811 | 0.4564 | 0.5 | -0.095 ± 0.0262 | -0.05 (4) |
| 15-25 | 465 | 0.2245 | 0.207 | +0.0176 ± 0.0084 | 0.6378 | 0.5957 | 0.5997 | 0.4024 | 0.4624 | -0.097 ± 0.0217 | -0.01 (5) |
| 25-40 | 316 | 0.2704 | 0.2016 | +0.0688 ± 0.0159 | 0.7556 | 0.5836 | 0.6707 | 0.3571 | 0.4051 | -0.138 ± 0.0253 | -0.025 (2) |
| 40+ | 119 | 0.3395 | 0.1867 | +0.1527 ± 0.0384 | 0.9544 | 0.5477 | 0.7618 | 0.2833 | 0.3782 | -0.068 ± 0.0368 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1305 | 0.174 | 0.1747 | -0.0007 ± 0.0004 | 0.5205 | 0.5222 | 0.4921 | 0.4776 | 0.5027 | -0.034 ± 0.012 | -0.0217 (6) |
| 3-5 | 802 | 0.1887 | 0.1859 | +0.0028 ± 0.0012 | 0.5492 | 0.5429 | 0.5211 | 0.4813 | 0.4663 | -0.069 ± 0.0154 | 0.02 (1) |
| 5-10 | 1790 | 0.1842 | 0.1801 | +0.0041 ± 0.0015 | 0.5496 | 0.5354 | 0.5191 | 0.4456 | 0.4559 | -0.057 ± 0.0102 | -0.01 (5) |
| 10-15 | 1628 | 0.1947 | 0.1813 | +0.0133 ± 0.0026 | 0.575 | 0.5308 | 0.5155 | 0.3911 | 0.4029 | -0.063 ± 0.0107 | -0.02 (14) |
| 15-25 | 2267 | 0.2141 | 0.1725 | +0.0416 ± 0.0034 | 0.6236 | 0.5106 | 0.5289 | 0.3332 | 0.3277 | -0.085 ± 0.0088 | -0.0026 (27) |
| 25-40 | 2096 | 0.2475 | 0.1371 | +0.1104 ± 0.0052 | 0.7012 | 0.4183 | 0.5612 | 0.2445 | 0.23 | -0.088 ± 0.0081 | -0.015 (6) |
| 40+ | 1670 | 0.4024 | 0.0678 | +0.3346 ± 0.0073 | 1.0541 | 0.238 | 0.6688 | 0.1311 | 0.1024 | -0.071 ± 0.0062 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 297 | 0.1915 | 0.194 | -0.0026 ± 0.0009 | 0.5616 | 0.5687 | 0.4966 | 0.4813 | 0.5455 | -0.025 ± 0.0258 | -0.0133 (6) |
| 3-5 | 204 | 0.184 | 0.1826 | +0.0014 ± 0.0024 | 0.5429 | 0.5389 | 0.4991 | 0.4599 | 0.4657 | -0.119 ± 0.0317 | -0.01 (1) |
| 5-10 | 420 | 0.1977 | 0.1976 | +0.0000 ± 0.0033 | 0.5813 | 0.5795 | 0.5111 | 0.4373 | 0.469 | -0.089 ± 0.0227 | -0.01 (4) |
| 10-15 | 325 | 0.215 | 0.2138 | +0.0013 ± 0.0064 | 0.62 | 0.6115 | 0.5357 | 0.4126 | 0.4708 | -0.083 ± 0.0253 | -0.044 (5) |
| 15-25 | 407 | 0.2244 | 0.2081 | +0.0163 ± 0.0088 | 0.6452 | 0.601 | 0.5795 | 0.386 | 0.4398 | -0.100 ± 0.0224 | -0.03 (1) |
| 25-40 | 243 | 0.2003 | 0.2073 | -0.0070 ± 0.0169 | 0.5835 | 0.5937 | 0.6551 | 0.3433 | 0.5062 | -0.045 ± 0.0249 | 0.0 (1) |
| 40+ | 47 | 0.3129 | 0.1765 | +0.1364 ± 0.0556 | 0.8395 | 0.5287 | 0.7528 | 0.2988 | 0.383 | -0.139 ± 0.0556 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1364 | 0.1794 | 0.1803 | -0.0009 ± 0.0004 | 0.532 | 0.534 | 0.483 | 0.4678 | 0.4963 | -0.032 ± 0.0115 | -0.0183 (23) |
| 3-5 | 955 | 0.183 | 0.1804 | +0.0026 ± 0.0011 | 0.5407 | 0.5341 | 0.4689 | 0.4297 | 0.4157 | -0.084 ± 0.0143 | -0.0243 (7) |
| 5-10 | 2183 | 0.1852 | 0.1804 | +0.0048 ± 0.0014 | 0.5516 | 0.5356 | 0.4809 | 0.4066 | 0.4127 | -0.060 ± 0.0092 | -0.01 (18) |
| 10-15 | 1729 | 0.1957 | 0.1795 | +0.0161 ± 0.0025 | 0.5756 | 0.5268 | 0.4885 | 0.365 | 0.3597 | -0.078 ± 0.0101 | -0.03 (9) |
| 15-25 | 2336 | 0.2031 | 0.1678 | +0.0353 ± 0.0033 | 0.5981 | 0.4988 | 0.4927 | 0.2972 | 0.3061 | -0.064 ± 0.0085 | -0.03 (2) |
| 25-40 | 1786 | 0.2118 | 0.1196 | +0.0923 ± 0.0052 | 0.6142 | 0.3709 | 0.5231 | 0.2056 | 0.2223 | -0.057 ± 0.0077 | 0.0 (1) |
| 40+ | 1205 | 0.3853 | 0.047 | +0.3383 ± 0.007 | 1.0066 | 0.1831 | 0.6307 | 0.1079 | 0.0573 | -0.086 ± 0.006 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 582 | 0.2013 | 0.2014 | -0.0001 ± 0.0006 | 0.5853 | 0.5851 | 0.4997 | 0.4848 | 0.4863 | -0.048 ± 0.0185 | -0.0226 (46) |
| 3-5 | 435 | 0.195 | 0.1937 | +0.0013 ± 0.0017 | 0.5708 | 0.5661 | 0.4795 | 0.44 | 0.446 | -0.050 ± 0.0211 | -0.0058 (33) |
| 5-10 | 888 | 0.1919 | 0.1868 | +0.0052 ± 0.0022 | 0.5682 | 0.5547 | 0.4796 | 0.4062 | 0.4088 | -0.058 ± 0.0148 | -0.0049 (73) |
| 10-15 | 580 | 0.2041 | 0.1947 | +0.0095 ± 0.0046 | 0.5974 | 0.5709 | 0.4825 | 0.3596 | 0.381 | -0.043 ± 0.0182 | 0.0014 (64) |
| 15-25 | 782 | 0.2329 | 0.2077 | +0.0251 ± 0.0064 | 0.6598 | 0.6007 | 0.5481 | 0.3538 | 0.3875 | -0.056 ± 0.0164 | -0.0216 (58) |
| 25-40 | 443 | 0.245 | 0.1854 | +0.0596 ± 0.0127 | 0.6898 | 0.5442 | 0.6266 | 0.3132 | 0.3725 | -0.074 ± 0.0191 | -0.0216 (25) |
| 40+ | 149 | 0.3493 | 0.1859 | +0.1634 ± 0.0358 | 0.9929 | 0.5499 | 0.7782 | 0.2869 | 0.3893 | -0.060 ± 0.0322 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1721 | 0.1862 | 0.1862 | +0.0000 ± 0.0004 | 0.5474 | 0.5463 | 0.5006 | 0.4855 | 0.4863 | -0.043 ± 0.0103 | -0.0155 (82) |
| 3-5 | 1213 | 0.1861 | 0.1835 | +0.0026 ± 0.001 | 0.5461 | 0.5402 | 0.4908 | 0.4513 | 0.4419 | -0.057 ± 0.0123 | -0.0148 (63) |
| 5-10 | 2491 | 0.1911 | 0.1833 | +0.0078 ± 0.0013 | 0.5663 | 0.5445 | 0.4768 | 0.4031 | 0.3914 | -0.065 ± 0.0087 | -0.0087 (125) |
| 10-15 | 1701 | 0.1999 | 0.186 | +0.0140 ± 0.0026 | 0.5874 | 0.5499 | 0.4965 | 0.3734 | 0.3774 | -0.056 ± 0.0103 | -0.0053 (105) |
| 15-25 | 2202 | 0.2255 | 0.1951 | +0.0305 ± 0.0037 | 0.6496 | 0.569 | 0.5421 | 0.347 | 0.3669 | -0.056 ± 0.0095 | -0.0255 (106) |
| 25-40 | 1546 | 0.2397 | 0.1604 | +0.0793 ± 0.0064 | 0.6791 | 0.4782 | 0.5891 | 0.2745 | 0.3079 | -0.060 ± 0.0099 | -0.0206 (47) |
| 40+ | 736 | 0.3648 | 0.1095 | +0.2553 ± 0.013 | 1.0013 | 0.3447 | 0.6821 | 0.1773 | 0.1889 | -0.067 ± 0.0113 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 1943 | 1.1 ± 0.065 | 1.196 | 0.1709 | 0.1696 | 0.2084 | 0.2012 |
| gen2 | 1943 | 0.879 ± 0.057 | 1.127 | 0.1871 | 0.169 | 0.2272 | 0.2011 |
| gen1_elo | 1943 | 1.089 ± 0.063 | 1.187 | 0.1748 | 0.1701 | 0.2069 | 0.2011 |
| gen1_sr | 1943 | 1.09 ± 0.073 | 1.206 | 0.1446 | 0.1715 | 0.2222 | 0.2009 |
| gen1_ledger | 3859 | 0.921 ± 0.041 | 1.079 | 0.1729 | 0.1912 | 0.216 | 0.195 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 10,617)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,927 | 27.6% |
| STALE_QUOTE | market_freshness | 2,228 | 21.0% |
| BOOK_QUALITY | execution | 1,853 | 17.4% |
| POOR_DATA | data | 1,119 | 10.5% |
| LIMITED_DATA | data | 773 | 7.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 581 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 464 | 4.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 322 | 3.0% |
| IDENTITY_AMBIGUOUS | mapping | 306 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 44 | 0.4% |

Cause class: coverage 27.6%, market_freshness 21.0%, data 17.8%, execution 17.4%, market_freshness/coverage 8.5%, model_calibration_or_unknown 4.4%, mapping 2.9%, model_calibration 0.4%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.3%, START_UNVERIFIABLE 96.3%, LOW_DATA_QUALITY 69.0%, STALE_PLAYER_DATA 57.6%, THIN_PLAYER_HISTORY 57.4%, STALE_KALSHI_QUOTE 48.2%, MODEL_INTERNAL_DISAGREEMENT 37.3%, ASYMMETRIC_SAMPLE_SIZE 30.7%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 16.2%, PLAYER_IDENTITY_RISK 11.2%, LEVEL_TRANSFER_RISK 8.9%, EVENT_MAPPING_RISK 7.8%, LOW_DISPLAYED_LIQUIDITY 7.4%, MODEL_CALIBRATION_OUTLIER 3.3%, EXTERNAL_MARKET_REJECTION 0.7%, UNKNOWN 0.5%, EXTERNAL_MARKET_CONFIRMATION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 30.1%, POST_SETTLEMENT_OBSERVATION 27.6%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### >= ge_25 pp (N = 5,808)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,297 | 39.6% |
| STALE_QUOTE | market_freshness | 996 | 17.2% |
| BOOK_QUALITY | execution | 979 | 16.9% |
| POOR_DATA | data | 458 | 7.9% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 319 | 5.5% |
| LIMITED_DATA | data | 249 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 203 | 3.5% |
| IDENTITY_AMBIGUOUS | mapping | 187 | 3.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 109 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 11 | 0.2% |

Cause class: coverage 39.6%, market_freshness 17.2%, execution 16.9%, data 12.2%, market_freshness/coverage 9.0%, mapping 3.2%, model_calibration_or_unknown 1.9%, model_calibration 0.2%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.7%, START_UNVERIFIABLE 98.2%, LOW_DATA_QUALITY 71.7%, THIN_PLAYER_HISTORY 58.9%, STALE_KALSHI_QUOTE 55.8%, STALE_PLAYER_DATA 52.4%, MODEL_INTERNAL_DISAGREEMENT 38.6%, ASYMMETRIC_SAMPLE_SIZE 32.4%, WIDE_SPREAD 23.0%, MODEL_HIGH_UNCERTAINTY 17.6%, PLAYER_IDENTITY_RISK 14.1%, EVENT_MAPPING_RISK 9.5%, LOW_DISPLAYED_LIQUIDITY 7.6%, LEVEL_TRANSFER_RISK 7.6%, MODEL_CALIBRATION_OUTLIER 4.1%, EXTERNAL_MARKET_REJECTION 0.3%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 42.5%, POST_SETTLEMENT_OBSERVATION 39.6%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.7%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 4826, "IDENTITY_AMBIGUOUS": 982}; ticker orientation: {"VERIFIED": 5808}.

Checks: discipline:AMBIGUOUS 385, discipline:PASS 5423, identity_confidence:AMBIGUOUS 819, identity_confidence:PASS 4989, level_mapping:NA 397, level_mapping:PASS 5411, market_pair:AMBIGUOUS 220, market_pair:NA 130, market_pair:PASS 5458, model_complement:NA 97, model_complement:PASS 5711, namesake:PASS 5808, physical_match_id:NA 2410, physical_match_id:PASS 3398, player_ids:PASS 5808, same_pair_other_event:PASS 5808, ticker_orientation:PASS 5808

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,567 | 1.6% | 1.6% | 0.4% | {"market_freshness": 20, "execution": 5} | 5.43 | 0.2183 / 0.2094 (141) | 19.7% | 0.1% | 5.8% | 1.3% |
| CHALLENGER | 3,774 | 18.8% | 6.2% | 12.2% | {"coverage": 445, "market_freshness": 107, "market_freshness/coverage": 85, "model_calibration_or_unknown": 39, "data": 25, "execution": 4, "model_calibration": 3} | 6.76 | 0.2239 / 0.206 (894) | 46.0% | 4.7% | 1.7% | 24.1% |
| DOUBLES | 763 | 50.5% | 50.1% | 6.6% | {"execution": 145, "market_freshness": 106, "mapping": 101, "market_freshness/coverage": 26, "coverage": 7} | 25.29 | 0.3188 / 0.2271 (213) | 30.7% | 0.0% | 100.0% | 7.9% |
| ITF_MEN | 7,781 | 24.0% | 15.9% | 32.1% | {"coverage": 767, "execution": 383, "data": 267, "market_freshness": 266, "market_freshness/coverage": 162, "mapping": 19, "model_calibration_or_unknown": 1} | 10.59 | 0.2109 / 0.193 (1929) | 38.7% | 54.4% | 6.2% | 24.3% |
| ITF_WOMEN | 10,011 | 26.1% | 17.8% | 45.0% | {"coverage": 1061, "market_freshness": 439, "execution": 425, "data": 391, "market_freshness/coverage": 208, "mapping": 61, "model_calibration_or_unknown": 22, "model_calibration": 7} | 12.12 | 0.2011 / 0.1921 (2149) | 39.8% | 57.9% | 9.7% | 24.3% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 990 | 8.0% | 6.9% | 1.4% | {"market_freshness": 34, "model_calibration_or_unknown": 16, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.03 | 0.2039 / 0.1997 (149) | 33.7% | 2.1% | 1.2% | 3.3% |
| WTA125 | 834 | 14.4% | 10.5% | 2.1% | {"market_freshness/coverage": 31, "model_calibration_or_unknown": 29, "market_freshness": 22, "data": 13, "coverage": 12, "execution": 8, "mapping": 4, "model_calibration": 1} | 10.01 | 0.2257 / 0.2107 (285) | 26.1% | 6.3% | 4.1% | 11.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 5 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 6 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 7 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 8 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 9 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 10 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 11 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 12 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 14 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 16 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 321 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 17 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 18 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 19 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 20 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 21 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 765 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 22 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 23 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 24 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 25 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 26 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 27 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 28 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 29 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 30 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 64 min (STALE); no external reference |
| 31 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 32 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 33 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 34 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 36 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 153 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 37 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 38 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 39 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 40 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 41 | `KXITFWMATCH-26OCT08ARISAV-SAV` | ITF_WOMEN | fair_v1 | 75% / 2% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.3h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 26 min (AGING); no external reference |
| 42 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 230 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 43 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 687 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 44 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 45 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 46 | `KXITFWMATCH-26OCT08ARAWAN-ARA` | ITF_WOMEN | fair_v1 | 77% / 6% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 123 min (STALE); data POOR (grade D, thinner serve sample 553.0, ratio 3.97); no external reference |
| 47 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 66 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 48 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 49 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 50 | `KXITFWMATCH-26OCT08YANZHE-YAN` | ITF_WOMEN | fair_v1 | 90% / 18% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 61 min before settlement (in-play print); quote age at model time 166 min (STALE); data LIMITED (grade C, thinner serve sample 1212.0, ratio 2.36); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9822, "by_level_share_of_ge_25pp": {"ATP": 0.0043, "CHALLENGER": 0.1219, "DOUBLES": 0.0663, "ITF_MEN": 0.3211, "ITF_WOMEN": 0.4501, "OTHER": 0.0021, "WTA": 0.0136, "WTA125": 0.0207}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5575, "share_primary_cause_market_settled_or_in_play": 0.4854, "share_primary_cause_stale_quote_only": 0.1715}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 5808, "identity_ambiguous_share": 0.1691, "ticker_orientation": {"VERIFIED": 5808}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 3398, "with_external": 70, "coverage": 0.0206, "external_status": {"EXTERNAL_STALE": 56, "AGREES_WITH_KALSHI": 14}, "triangulation": {"INSUFFICIENT_INPUTS": 56, "MODEL_LONE_OUTLIER": 14}, "share_external_agrees_with_kalshi": 0.2, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 1463, "with_external": 68, "coverage": 0.0465, "external_status": {"EXTERNAL_STALE": 54, "AGREES_WITH_KALSHI": 14}, "triangulation": {"INSUFFICIENT_INPUTS": 54, "MODEL_LONE_OUTLIER": 14}, "share_external_agrees_with_kalshi": 0.2059, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 623.0, "median_sample_ratio": 2.32, "median_min_matches": 21.0, "median_max_days_since_last": 196.0, "share_severe_asymmetry": 0.1744, "data_status": {"POOR": 2993, "LIMITED": 1767, "ADEQUATE": 1048}, "comparison_lt_10pp": {"median_thinner_serve_points": 1761.0, "median_sample_ratio": 1.74, "median_min_matches": 75.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 432, "model_minus_observed": 0.0534, "kalshi_minus_observed": -0.0787, "brier_diff_model_minus_kalshi": 0.0014}, "4-10x": {"n": 304, "model_minus_observed": 0.0587, "kalshi_minus_observed": -0.0831, "brier_diff_model_minus_kalshi": -0.0024}, "<2x": {"n": 915, "model_minus_observed": 0.0846, "kalshi_minus_observed": -0.0405, "brier_diff_model_minus_kalshi": 0.0112}, ">=10x": {"n": 292, "model_minus_observed": 0.1097, "kalshi_minus_observed": -0.0603, "brier_diff_model_minus_kalshi": 0.0135}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 1943, "model": {"intercept": -0.565, "slope": 0.879, "slope_se": 0.057}, "kalshi_mid_same_rows": {"intercept": 0.227, "slope": 1.127, "slope_se": 0.065}, "mean_extremity_model": 0.1871, "mean_extremity_kalshi": 0.169, "model_brier": 0.2272, "kalshi_brier": 0.2011, "brier_diff_model_minus_kalshi": 0.0262, "brier_diff_se": 0.0043, "model_logloss": 0.6498, "kalshi_logloss": 0.5843}, "fair_v1": {"n": 1943, "model": {"intercept": -0.397, "slope": 1.1, "slope_se": 0.065}, "kalshi_mid_same_rows": {"intercept": 0.351, "slope": 1.196, "slope_se": 0.067}, "mean_extremity_model": 0.1709, "mean_extremity_kalshi": 0.1696, "model_brier": 0.2084, "kalshi_brier": 0.2012, "brier_diff_model_minus_kalshi": 0.0073, "brier_diff_se": 0.0035, "model_logloss": 0.603, "kalshi_logloss": 0.5842}, "gen1_elo": {"n": 1943, "model": {"intercept": -0.372, "slope": 1.089, "slope_se": 0.063}, "kalshi_mid_same_rows": {"intercept": 0.359, "slope": 1.187, "slope_se": 0.066}, "mean_extremity_model": 0.1748, "mean_extremity_kalshi": 0.1701, "model_brier": 0.2069, "kalshi_brier": 0.2011, "brier_diff_model_minus_kalshi": 0.0058, "brier_diff_se": 0.0034, "model_logloss": 0.6006, "kalshi_logloss": 0.584}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.25, "share_ge_15": 0.4342, "median_abs_gap": 12.94, "n": 13594}, "gen1_elo": {"share_ge_25": 0.2419, "share_ge_15": 0.4331, "median_abs_gap": 12.51, "n": 13594}, "gen1_sr": {"share_ge_25": 0.3034, "share_ge_15": 0.5179, "median_abs_gap": 15.61, "n": 13594}, "gen2": {"share_ge_25": 0.3068, "share_ge_15": 0.5038, "median_abs_gap": 15.22, "n": 13594}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1438, "share_ge_15": 0.3322, "median_abs_gap": 10.37, "n": 10175}, "gen1_elo": {"share_ge_25": 0.1394, "share_ge_15": 0.3279, "median_abs_gap": 9.85, "n": 10174}, "gen1_sr": {"share_ge_25": 0.1986, "share_ge_15": 0.4266, "median_abs_gap": 12.7, "n": 10175}, "gen2": {"share_ge_25": 0.2161, "share_ge_15": 0.4258, "median_abs_gap": 12.59, "n": 10176}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.43, "share_ge_25_all": 0.016, "share_ge_25_pregame_clean": 0.0162}, "WTA": {"median_abs_gap_pregame_clean": 8.03, "share_ge_25_all": 0.0798, "share_ge_25_pregame_clean": 0.069}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2367, "share_within_10pp_all": 0.435, "share_within_10pp_pregame_clean": 0.4999, "corr_model_vs_mid_pregame_clean": 0.8509}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 292, "model_brier": 0.1862, "kalshi_brier": 0.1875, "brier_diff_model_minus_kalshi": -0.0013}, "10-15": {"n_settled": 345, "model_brier": 0.2127, "kalshi_brier": 0.2076, "brier_diff_model_minus_kalshi": 0.0051}, "15-25": {"n_settled": 416, "model_brier": 0.2227, "kalshi_brier": 0.2127, "brier_diff_model_minus_kalshi": 0.01}, "25-40": {"n_settled": 242, "model_brier": 0.217, "kalshi_brier": 0.2014, "brier_diff_model_minus_kalshi": 0.0156}, "3-5": {"n_settled": 197, "model_brier": 0.1865, "kalshi_brier": 0.1874, "brier_diff_model_minus_kalshi": -0.0009}, "40+": {"n_settled": 53, "model_brier": 0.2878, "kalshi_brier": 0.1771, "brier_diff_model_minus_kalshi": 0.1107}, "5-10": {"n_settled": 398, "model_brier": 0.2012, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": -0.0022}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.565, "slope": 0.879, "slope_se": 0.057}, "kalshi_slope": {"intercept": 0.227, "slope": 1.127, "slope_se": 0.065}, "n": 1943}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 213, "model_brier": 0.3188, "kalshi_brier": 0.2271, "brier_diff_model_minus_kalshi": 0.0917, "brier_diff_se": 0.0216, "corr_model_outcome": -0.0023, "corr_kalshi_outcome": 0.3188}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
