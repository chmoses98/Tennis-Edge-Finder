# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-11T01:56Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 28,031): 0-3 14.6%, 3-5 9.7%, 5-10 20.0%, 10-15 15.4%, 15-25 18.4%, 25-40 13.6%, 40+ 8.2%; median gap 11.76 pp.
* **Where the extremes live**: 98.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.8%, Challenger 11.8%, doubles 7.2%). Main tour: ATP 1.5% and WTA 7.4% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 6,127): MARKET_ALREADY_SETTLED_WHEN_PRICED 39.6%, BOOK_QUALITY 16.9%, STALE_QUOTE 16.5%, POOR_DATA 8.0%, POSSIBLY_IN_PLAY_QUOTE 5.5%, LIMITED_DATA 4.3%, IDENTITY_AMBIGUOUS 3.7%, IN_PLAY_QUOTE 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.8%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.3%. By class: coverage 39.6%, execution 16.9%, market_freshness 16.5%, data 12.3%, market_freshness/coverage 8.9%, mapping 3.7%, model_calibration_or_unknown 1.8%, model_calibration 0.3%.
* **Stale / settled / in-play**: 55.1% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 48.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 6,127 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 17.4% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 2.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 18.1% of the time and with the model 0.2%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 643.0 points vs 1892.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.06, Gen-2 0.855, Gen-1 ledger 0.877 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 257 model 0.2195 vs Kalshi 0.2015; n 57 model 0.2912 vs Kalshi 0.167.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 110,894 model-market comparisons (182,540 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 41,740 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-11T01:50:20.440975+00:00'], shadow board 29,392 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-11T01:50:23.030612+00:00'], Model 4 12,358 rows, 12,270 settled tickers, 3,383 tickers with an external scan.
* By model: {"gen1_ledger": 27407, "gen1_elo": 14768, "fair_v1": 14768, "gen2": 14768, "gen1_sr": 14768, "model4_fundamental": 12212, "model4_conditioned": 12203}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 28,031 | 14.6 | 9.7 | 20.0 | 15.4 | 18.4 | 13.6 | 8.2 | 11.76 | 40.3% | 21.9% |
| MW fair_v1 | 14,768 | 13.8 | 8.7 | 18.5 | 16.2 | 18.4 | 14.5 | 9.8 | 12.75 | 42.7% | 24.4% |
| MW gen1_elo | 14,768 | 13.3 | 9.1 | 20.2 | 15.0 | 18.8 | 14.3 | 9.4 | 12.26 | 42.4% | 23.7% |
| MW gen1_ledger | 13,263 | 15.5 | 10.8 | 21.6 | 14.4 | 18.6 | 12.7 | 6.4 | 10.53 | 37.6% | 19.1% |
| MW gen1_sr | 14,768 | 10.2 | 7.9 | 16.4 | 14.4 | 21.5 | 18.1 | 11.5 | 15.41 | 51.1% | 29.6% |
| MW gen2 | 14,768 | 12.1 | 7.3 | 16.3 | 14.3 | 19.9 | 17.0 | 13.0 | 14.99 | 50.0% | 30.0% |
| all families model4_conditioned | 12,203 | 22.1 | 20.2 | 36.0 | 15.8 | 4.1 | 0.9 | 0.9 | 5.71 | 5.9% | 1.8% |
| all families model4_fundamental | 12,212 | 16.8 | 13.4 | 35.9 | 19.7 | 10.6 | 2.5 | 1.1 | 7.55 | 14.2% | 3.6% |

Configurable thresholds (primary): >=5pp 75.7%, >=10pp 55.7%, >=15pp 40.3%, >=20pp 30.1%, >=25pp 21.9%, >=30pp 16.0%, >=40pp 8.2%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.35pp; >=10pp 45.1%, >=25pp 17.6%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,209 | 30.6 | 14.1 | 25.2 | 16.9 | 11.1 | 1.2 | 0.9 | 5.84 | 13.2% | 2.1% |
| CHALLENGER | 2,451 | 15.9 | 10.8 | 18.8 | 16.2 | 13.3 | 12.6 | 12.3 | 11.67 | 38.3% | 24.9% |
| ITF_MEN | 4,212 | 11.6 | 8.8 | 18.5 | 15.0 | 19.1 | 15.1 | 12.0 | 13.59 | 46.2% | 27.1% |
| ITF_WOMEN | 5,855 | 10.2 | 6.6 | 15.9 | 16.4 | 21.7 | 18.5 | 10.6 | 15.34 | 50.8% | 29.1% |
| WTA | 654 | 22.2 | 10.7 | 25.5 | 16.2 | 17.3 | 6.4 | 1.7 | 7.96 | 25.4% | 8.1% |
| WTA125 | 387 | 12.1 | 6.5 | 23.3 | 24.3 | 16.5 | 15.2 | 2.1 | 11.31 | 33.9% | 17.3% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,209 | 24.2 | 14.1 | 24.8 | 18.8 | 15.1 | 1.9 | 1.1 | 6.9 | 18.1% | 3.0% |
| CHALLENGER | 2,451 | 15.5 | 7.5 | 18.5 | 13.5 | 18.2 | 13.9 | 12.9 | 12.94 | 45.0% | 26.9% |
| ITF_MEN | 4,212 | 10.4 | 7.5 | 16.9 | 14.9 | 19.9 | 17.7 | 12.7 | 15.25 | 50.3% | 30.4% |
| ITF_WOMEN | 5,855 | 9.0 | 5.9 | 12.9 | 12.9 | 21.3 | 20.9 | 17.2 | 19.07 | 59.3% | 38.0% |
| WTA | 654 | 20.3 | 7.3 | 18.0 | 15.3 | 20.8 | 16.5 | 1.7 | 12.31 | 39.0% | 18.2% |
| WTA125 | 387 | 4.1 | 3.1 | 18.6 | 20.2 | 24.0 | 19.6 | 10.3 | 17.19 | 54.0% | 30.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,209 | 26.6 | 14.6 | 29.4 | 15.1 | 10.8 | 2.6 | 1.0 | 6.29 | 14.4% | 3.6% |
| CHALLENGER | 2,451 | 15.8 | 10.6 | 20.3 | 15.0 | 14.2 | 11.9 | 12.2 | 10.75 | 38.3% | 24.1% |
| ITF_MEN | 4,212 | 10.4 | 8.9 | 19.2 | 13.9 | 20.0 | 15.4 | 12.1 | 13.94 | 47.6% | 27.6% |
| ITF_WOMEN | 5,855 | 9.9 | 6.7 | 16.7 | 15.7 | 22.9 | 18.8 | 9.4 | 15.48 | 51.0% | 28.2% |
| WTA | 654 | 22.3 | 14.7 | 33.8 | 16.2 | 9.0 | 2.9 | 1.1 | 6.62 | 13.0% | 4.0% |
| WTA125 | 387 | 23.0 | 11.1 | 30.5 | 15.8 | 13.4 | 5.7 | 0.5 | 7.73 | 19.6% | 6.2% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 667 | 31.3 | 23.5 | 34.2 | 9.2 | 1.4 | 0.5 | 0.0 | 4.61 | 1.8% | 0.4% |
| CHALLENGER | 1,632 | 23.8 | 17.1 | 26.5 | 13.5 | 12.1 | 5.2 | 1.8 | 6.45 | 19.1% | 7.0% |
| DOUBLES | 860 | 4.0 | 3.1 | 10.2 | 11.3 | 19.9 | 25.5 | 26.1 | 25.84 | 71.4% | 51.5% |
| ITF_MEN | 4,062 | 15.0 | 8.6 | 21.2 | 15.3 | 20.3 | 12.0 | 7.5 | 11.67 | 39.9% | 19.5% |
| ITF_WOMEN | 4,795 | 11.7 | 9.3 | 19.8 | 14.6 | 22.4 | 16.7 | 5.6 | 12.98 | 44.6% | 22.2% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 539 | 22.8 | 13.9 | 25.4 | 17.1 | 14.3 | 5.9 | 0.6 | 7.91 | 20.8% | 6.5% |
| WTA125 | 559 | 18.6 | 13.8 | 22.2 | 19.0 | 15.6 | 8.2 | 2.7 | 8.91 | 26.5% | 10.9% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,198 | 30.5 | 14.0 | 25.4 | 16.9 | 11.1 | 1.2 | 0.9 | 5.86 | 13.2% | 2.1% |
| CHALLENGER | 1,750 | 20.9 | 13.7 | 23.8 | 19.1 | 13.8 | 6.2 | 2.6 | 8.05 | 22.6% | 8.8% |
| ITF_MEN | 2,984 | 14.4 | 11.1 | 22.2 | 16.7 | 19.0 | 11.8 | 4.9 | 10.62 | 35.7% | 16.7% |
| ITF_WOMEN | 4,155 | 12.7 | 8.4 | 18.8 | 19.1 | 23.2 | 14.6 | 3.2 | 12.6 | 41.0% | 17.8% |
| WTA | 649 | 22.0 | 10.8 | 25.7 | 16.2 | 17.3 | 6.3 | 1.7 | 7.94 | 25.3% | 8.0% |
| WTA125 | 372 | 12.6 | 6.7 | 22.3 | 24.7 | 16.9 | 15.3 | 1.3 | 11.32 | 33.6% | 16.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,198 | 24.0 | 14.1 | 24.9 | 18.8 | 15.2 | 1.9 | 1.1 | 6.9 | 18.2% | 3.0% |
| CHALLENGER | 1,750 | 20.2 | 9.8 | 23.2 | 16.3 | 18.7 | 9.2 | 2.6 | 9.06 | 30.5% | 11.8% |
| ITF_MEN | 2,985 | 12.5 | 9.2 | 19.7 | 16.7 | 21.5 | 14.7 | 5.8 | 12.45 | 42.0% | 20.5% |
| ITF_WOMEN | 4,155 | 10.6 | 7.1 | 14.6 | 14.1 | 23.9 | 19.6 | 10.1 | 16.26 | 53.6% | 29.7% |
| WTA | 649 | 20.3 | 7.4 | 18.0 | 15.4 | 20.6 | 16.5 | 1.7 | 12.25 | 38.8% | 18.2% |
| WTA125 | 372 | 4.3 | 3.2 | 18.6 | 20.7 | 23.7 | 20.2 | 9.4 | 16.79 | 53.2% | 29.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 647 | 31.4 | 23.8 | 34.5 | 9.3 | 0.6 | 0.5 | 0.0 | 4.61 | 1.1% | 0.5% |
| CHALLENGER | 1,395 | 25.8 | 19.0 | 28.7 | 13.2 | 11.2 | 2.0 | 0.1 | 5.78 | 13.3% | 2.1% |
| DOUBLES | 793 | 3.9 | 3.1 | 10.5 | 11.3 | 20.1 | 25.4 | 25.7 | 25.72 | 71.1% | 51.1% |
| ITF_MEN | 3,280 | 16.8 | 9.5 | 23.5 | 16.3 | 20.1 | 9.6 | 4.3 | 10.04 | 33.9% | 13.9% |
| ITF_WOMEN | 3,918 | 12.9 | 10.1 | 21.7 | 15.4 | 22.6 | 14.9 | 2.4 | 11.5 | 39.9% | 17.3% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 509 | 23.4 | 14.5 | 25.9 | 17.1 | 14.5 | 4.5 | 0.0 | 7.52 | 19.1% | 4.5% |
| WTA125 | 472 | 20.8 | 15.2 | 23.9 | 21.4 | 13.8 | 4.5 | 0.4 | 7.53 | 18.6% | 4.9% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 860 | 4.0 | 3.1 | 10.2 | 11.3 | 19.9 | 25.5 | 26.1 | 25.84 | 71.4% | 51.5% |
| singles | 12,403 | 16.3 | 11.3 | 22.4 | 14.7 | 18.5 | 11.8 | 5.0 | 9.97 | 35.3% | 16.8% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 3,353 | 13.6 | 9.6 | 20.1 | 16.1 | 16.3 | 13.9 | 10.3 | 12.06 | 40.5% | 24.2% |
| Grass | 21 | 14.3 | 23.8 | 14.3 | 14.3 | 19.1 | 14.3 | 0.0 | 7.35 | 33.3% | 14.3% |
| Hard | 9,927 | 14.2 | 8.5 | 18.4 | 16.0 | 18.8 | 14.4 | 9.7 | 12.79 | 42.9% | 24.1% |
| UNKNOWN | 1,467 | 11.4 | 8.2 | 15.8 | 17.9 | 20.2 | 16.5 | 10.0 | 13.98 | 46.8% | 26.5% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,515 | 20.1 | 10.7 | 21.0 | 17.2 | 14.6 | 9.0 | 7.4 | 9.46 | 31.1% | 16.4% |
| B | 1,989 | 14.9 | 9.4 | 19.2 | 17.2 | 17.0 | 12.1 | 10.1 | 11.51 | 39.3% | 22.2% |
| C | 2,239 | 12.6 | 9.8 | 19.4 | 15.1 | 18.9 | 14.9 | 9.3 | 12.71 | 43.2% | 24.2% |
| D | 2,714 | 10.8 | 8.4 | 17.6 | 16.2 | 22.1 | 14.9 | 9.9 | 13.94 | 46.9% | 24.8% |
| F | 3,311 | 7.8 | 5.2 | 14.9 | 15.0 | 20.8 | 22.9 | 13.4 | 18.31 | 57.0% | 36.2% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,864 | 22.9 | 16.2 | 28.0 | 14.9 | 11.5 | 4.7 | 1.8 | 6.71 | 18.0% | 6.4% |
| B | 2,078 | 15.3 | 9.8 | 23.9 | 16.1 | 19.1 | 11.4 | 4.4 | 10.2 | 34.8% | 15.7% |
| C | 2,677 | 11.9 | 7.7 | 17.7 | 14.3 | 20.8 | 16.0 | 11.5 | 14.2 | 48.4% | 27.5% |
| D | 2,131 | 14.3 | 9.4 | 21.3 | 13.1 | 21.8 | 13.9 | 6.2 | 11.86 | 41.9% | 20.1% |
| F | 2,513 | 9.3 | 7.7 | 14.5 | 13.6 | 23.7 | 21.3 | 9.9 | 16.91 | 54.9% | 31.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 5,012 | 18.6 | 9.8 | 20.0 | 17.1 | 14.9 | 10.0 | 9.7 | 10.46 | 34.6% | 19.7% |
| LIMITED | 3,690 | 14.9 | 10.5 | 20.5 | 16.0 | 18.1 | 13.0 | 6.9 | 11.22 | 38.0% | 20.0% |
| POOR | 6,066 | 9.2 | 6.7 | 16.1 | 15.6 | 21.4 | 19.2 | 11.8 | 15.98 | 52.4% | 31.0% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,752 | 30.8 | 24.7 | 36.5 | 5.6 | 1.8 | 0.6 | 0.1 | 4.54 | 2.4% | 0.6% |
| GAME_SPREAD | 2,665 | 25.2 | 15.8 | 36.9 | 17.0 | 4.5 | 0.4 | 0.2 | 6.08 | 5.1% | 0.6% |
| MATCH_WINNER | 13,263 | 15.5 | 10.8 | 21.6 | 14.4 | 18.6 | 12.7 | 6.4 | 10.53 | 37.6% | 19.1% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 4,810 | 33.6 | 19.5 | 30.4 | 9.5 | 5.5 | 1.2 | 0.2 | 4.66 | 7.0% | 1.4% |
| TOTAL_GAMES | 3,893 | 7.0 | 9.1 | 38.8 | 30.3 | 9.9 | 2.5 | 2.4 | 9.5 | 14.8% | 4.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,463 | 25.4 | 37.6 | 31.8 | 0.3 | 4.2 | 0.5 | 0.1 | 4.33 | 4.8% | 0.6% |
| GAME_SPREAD | 3,161 | 44.7 | 15.2 | 30.0 | 7.7 | 1.2 | 0.8 | 0.4 | 3.65 | 2.4% | 1.2% |
| TOTAL_GAMES | 4,579 | 3.4 | 6.7 | 44.1 | 36.5 | 6.0 | 1.3 | 2.0 | 9.59 | 9.3% | 3.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,463 | 25.7 | 18.7 | 36.9 | 9.4 | 6.6 | 2.3 | 0.3 | 5.54 | 9.2% | 2.6% |
| GAME_SPREAD | 3,161 | 18.9 | 13.1 | 30.1 | 20.8 | 13.9 | 2.5 | 0.8 | 7.88 | 17.2% | 3.2% |
| TOTAL_GAMES | 4,588 | 6.6 | 8.5 | 38.9 | 28.9 | 12.3 | 2.6 | 2.2 | 9.59 | 17.1% | 4.9% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 14,768 | 42.7% | 24.4% | 12.75 | 32.5% | 13.8% | 10.18 |
| gen1_elo | 14,768 | 42.4% | 23.7% | 12.26 | 31.9% | 13.4% | 9.59 |
| gen1_sr | 14,768 | 51.1% | 29.6% | 15.41 | 41.9% | 19.0% | 12.54 |
| gen2 | 14,768 | 50.0% | 30.0% | 14.99 | 42.2% | 20.9% | 12.44 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 7,644 | 16.8 | 11.0 | 21.6 | 17.7 | 18.4 | 11.1 | 3.3 | 10.11 | 32.8% | 14.3% |
| STALE | 7,124 | 10.6 | 6.2 | 15.2 | 14.6 | 18.3 | 18.2 | 16.9 | 16.95 | 53.4% | 35.2% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 6,731 | 17.8 | 12.0 | 23.5 | 14.2 | 16.7 | 11.2 | 4.6 | 9.18 | 32.5% | 15.8% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 28,031 | 6731 | 11116 | 10184 | 24.4 | 155.7 | 1400.4 |
| ge_15pp | 11,299 | 2188 | 3794 | 5317 | 28.3 | 457.8 | 1380.4 |
| ge_25pp | 6,127 | 1065 | 1686 | 3376 | 35.9 | 581.9 | 1380.4 |
| lt_10pp | 12,420 | 3590 | 5416 | 3414 | 23.1 | 49.5 | 1341.5 |

Current slate `SL-20261011T015602Z-d1889027`: 543 priced rows, quote age at build {'median': 6.1, 'max': 6.1}, freshness {'FRESH': 543}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 4 | 0.0 | 0.0 | 25.0 | 0.0 | 75.0 | 0.0 | 0.0 | 20.45 | 75.0% | 0.0% |
| EXTERNAL_LONE_OUTLIER | 5 | 40.0 | 60.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 3.05 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 943 | 23.9 | 11.3 | 22.3 | 19.6 | 16.4 | 6.2 | 0.3 | 7.98 | 22.9% | 6.5% |
| MARKETS_AGREE | 159 | 74.8 | 25.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.95 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 246 | 0.0 | 4.5 | 35.4 | 33.3 | 17.9 | 8.5 | 0.4 | 11.26 | 26.8% | 8.9% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 14,768 | 1357 (9.2%) | 18.1% | 0.2% | {"EXTERNAL_STALE": 943, "AGREES_WITH_KALSHI": 246, "ALL_AGREE": 159, "EXTERNAL_OUTLIER": 5, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 6,312 | 285 (4.5%) | 23.2% | 1.1% | {"EXTERNAL_STALE": 216, "AGREES_WITH_KALSHI": 66, "SUPPORTS_MODEL_DIRECTION": 3} |
| fair_v1_ge_25pp | 3,600 | 83 (2.3%) | 26.5% | 0.0% | {"EXTERNAL_STALE": 61, "AGREES_WITH_KALSHI": 22} |
| fair_v1_ge_25pp_pregame_clean | 1,531 | 81 (5.3%) | 27.2% | 0.0% | {"EXTERNAL_STALE": 59, "AGREES_WITH_KALSHI": 22} |
| fair_v1_lt_10pp | 6,061 | 805 (13.3%) | 12.2% | 0.0% | {"EXTERNAL_STALE": 542, "ALL_AGREE": 159, "AGREES_WITH_KALSHI": 98, "EXTERNAL_OUTLIER": 5, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 2,983 | 11.6 | 8.6 | 19.7 | 15.3 | 20.8 | 13.9 | 10.0 | 13.06 | 44.8% | 23.9% |
| 4-10x | 2,029 | 11.3 | 9.1 | 18.7 | 15.3 | 20.0 | 16.3 | 9.3 | 13.46 | 45.6% | 25.6% |
| <2x | 7,927 | 15.9 | 9.2 | 18.7 | 17.3 | 16.7 | 12.9 | 9.4 | 11.83 | 39.0% | 22.3% |
| >=10x | 1,829 | 11.2 | 6.5 | 15.7 | 14.2 | 19.7 | 20.6 | 12.2 | 16.18 | 52.5% | 32.8% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 3,894 | 14.0 | 8.6 | 19.3 | 15.9 | 18.3 | 12.9 | 10.9 | 12.44 | 42.2% | 23.8% |
| 300-1000 | 3,565 | 11.8 | 9.1 | 16.9 | 16.2 | 20.9 | 16.0 | 9.2 | 13.73 | 46.1% | 25.2% |
| <300 | 3,817 | 8.5 | 6.0 | 15.8 | 15.0 | 20.9 | 20.9 | 12.9 | 17.08 | 54.7% | 33.8% |
| >=3000 | 3,492 | 21.5 | 11.4 | 22.3 | 17.8 | 13.0 | 7.8 | 6.1 | 8.5 | 26.9% | 13.9% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 470 | 0.538 | 0.4056 | 0.4766 | +0.061 | -0.071 | 0.0031 ± 0.0068 |
| ratio 4-10x | 323 | 0.5814 | 0.4396 | 0.5232 | +0.058 | -0.084 | 0.0005 ± 0.0087 |
| ratio <2x | 1079 | 0.5403 | 0.4189 | 0.4541 | +0.086 | -0.035 | 0.0126 ± 0.0043 |
| ratio >=10x | 304 | 0.5489 | 0.3812 | 0.4375 | +0.111 | -0.056 | 0.0162 ± 0.01 |
| thinner_sample 1000-3000 | 598 | 0.5431 | 0.4192 | 0.4615 | +0.082 | -0.042 | 0.0083 ± 0.0059 |
| thinner_sample 300-1000 | 581 | 0.5665 | 0.4256 | 0.4923 | +0.074 | -0.067 | 0.002 ± 0.0065 |
| thinner_sample <300 | 617 | 0.5429 | 0.3832 | 0.4571 | +0.086 | -0.074 | 0.012 ± 0.0068 |
| thinner_sample >=3000 | 380 | 0.5306 | 0.4371 | 0.4526 | +0.078 | -0.016 | 0.0173 ± 0.0058 |
| data_status ADEQUATE | 608 | 0.5307 | 0.429 | 0.4474 | +0.083 | -0.018 | 0.0132 ± 0.0049 |
| data_status LIMITED | 584 | 0.5576 | 0.4257 | 0.4846 | +0.073 | -0.059 | 0.0034 ± 0.0062 |
| data_status POOR | 984 | 0.5511 | 0.3974 | 0.4685 | +0.083 | -0.071 | 0.0103 ± 0.0053 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 339 | 0.1929 | 0.1943 | -0.0015 ± 0.0008 | 0.5633 | 0.5669 | 0.4912 | 0.4765 | 0.5251 | -0.050 ± 0.025 | -0.01 (3) |
| 3-5 | 223 | 0.1893 | 0.1907 | -0.0015 ± 0.0023 | 0.5589 | 0.5604 | 0.5106 | 0.4707 | 0.5067 | -0.055 ± 0.0296 | 0.02 (1) |
| 5-10 | 448 | 0.2013 | 0.2023 | -0.0010 ± 0.0032 | 0.5885 | 0.5908 | 0.5222 | 0.448 | 0.4844 | -0.083 ± 0.0221 | -0.0125 (4) |
| 10-15 | 394 | 0.213 | 0.2049 | +0.0081 ± 0.0057 | 0.6133 | 0.5908 | 0.5168 | 0.3931 | 0.4188 | -0.095 ± 0.0228 | -0.0633 (3) |
| 15-25 | 458 | 0.229 | 0.2149 | +0.0142 ± 0.0085 | 0.6537 | 0.6176 | 0.5755 | 0.3799 | 0.441 | -0.084 ± 0.0216 | -0.0133 (6) |
| 25-40 | 257 | 0.2195 | 0.2015 | +0.0181 ± 0.0166 | 0.6284 | 0.5785 | 0.648 | 0.3395 | 0.463 | -0.071 ± 0.0249 | -0.01 (1) |
| 40+ | 57 | 0.2912 | 0.167 | +0.1242 ± 0.0482 | 0.7869 | 0.5063 | 0.7464 | 0.3009 | 0.386 | -0.132 ± 0.0468 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1695 | 0.1733 | 0.1742 | -0.0009 ± 0.0003 | 0.5173 | 0.5184 | 0.4759 | 0.4612 | 0.4968 | -0.022 ± 0.0103 | -0.0188 (8) |
| 3-5 | 1064 | 0.1921 | 0.1891 | +0.0030 ± 0.0011 | 0.5656 | 0.5533 | 0.4788 | 0.4392 | 0.4173 | -0.080 ± 0.0135 | 0.02 (1) |
| 5-10 | 2284 | 0.1953 | 0.1925 | +0.0028 ± 0.0014 | 0.5735 | 0.5649 | 0.4895 | 0.4158 | 0.4308 | -0.052 ± 0.0093 | -0.0082 (17) |
| 10-15 | 2056 | 0.2006 | 0.182 | +0.0186 ± 0.0024 | 0.5866 | 0.5351 | 0.4731 | 0.3486 | 0.3361 | -0.079 ± 0.0094 | -0.0475 (4) |
| 15-25 | 2364 | 0.2032 | 0.1659 | +0.0373 ± 0.0033 | 0.5981 | 0.4932 | 0.495 | 0.2986 | 0.3029 | -0.069 ± 0.0084 | -0.0048 (29) |
| 25-40 | 1965 | 0.2188 | 0.1227 | +0.0962 ± 0.0049 | 0.6304 | 0.3797 | 0.5269 | 0.2132 | 0.2198 | -0.061 ± 0.0076 | -0.01 (1) |
| 40+ | 1343 | 0.3725 | 0.0438 | +0.3287 ± 0.0063 | 0.9702 | 0.1741 | 0.6228 | 0.1059 | 0.0566 | -0.085 ± 0.0054 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 261 | 0.1954 | 0.1959 | -0.0005 ± 0.0009 | 0.5727 | 0.5743 | 0.4946 | 0.4797 | 0.4943 | -0.082 ± 0.0289 | -0.01 (1) |
| 3-5 | 172 | 0.2083 | 0.2089 | -0.0007 ± 0.0028 | 0.5976 | 0.6009 | 0.5217 | 0.4817 | 0.5058 | -0.059 ± 0.0365 | 0.02 (1) |
| 5-10 | 383 | 0.196 | 0.1932 | +0.0028 ± 0.0034 | 0.5744 | 0.5679 | 0.5616 | 0.4867 | 0.5039 | -0.087 ± 0.0232 | -0.01 (4) |
| 10-15 | 368 | 0.2163 | 0.2066 | +0.0097 ± 0.006 | 0.6192 | 0.5994 | 0.5774 | 0.4526 | 0.481 | -0.101 ± 0.0245 | -0.05 (4) |
| 15-25 | 527 | 0.2271 | 0.209 | +0.0182 ± 0.0079 | 0.6437 | 0.6006 | 0.5996 | 0.4024 | 0.4611 | -0.086 ± 0.0204 | -0.01 (5) |
| 25-40 | 339 | 0.2745 | 0.2026 | +0.0719 ± 0.0155 | 0.7704 | 0.5856 | 0.674 | 0.3595 | 0.4041 | -0.135 ± 0.0244 | -0.025 (2) |
| 40+ | 126 | 0.3464 | 0.1881 | +0.1584 ± 0.0376 | 0.9703 | 0.5511 | 0.7614 | 0.2824 | 0.373 | -0.065 ± 0.0361 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1495 | 0.1768 | 0.1772 | -0.0004 ± 0.0004 | 0.526 | 0.5271 | 0.492 | 0.4776 | 0.501 | -0.031 ± 0.0113 | -0.0217 (6) |
| 3-5 | 911 | 0.1932 | 0.1919 | +0.0013 ± 0.0012 | 0.5606 | 0.5577 | 0.5226 | 0.4827 | 0.4852 | -0.048 ± 0.0147 | 0.02 (1) |
| 5-10 | 2020 | 0.1865 | 0.1828 | +0.0037 ± 0.0014 | 0.5542 | 0.5414 | 0.5143 | 0.4408 | 0.4559 | -0.048 ± 0.0096 | -0.01 (5) |
| 10-15 | 1778 | 0.1967 | 0.1808 | +0.0159 ± 0.0025 | 0.5797 | 0.5304 | 0.5181 | 0.3936 | 0.3948 | -0.070 ± 0.0102 | -0.02 (14) |
| 15-25 | 2540 | 0.2151 | 0.1746 | +0.0405 ± 0.0033 | 0.6255 | 0.5164 | 0.5347 | 0.339 | 0.337 | -0.076 ± 0.0084 | -0.0026 (27) |
| 25-40 | 2255 | 0.2497 | 0.1373 | +0.1124 ± 0.005 | 0.7103 | 0.4178 | 0.5619 | 0.2455 | 0.2275 | -0.088 ± 0.0078 | -0.015 (6) |
| 40+ | 1772 | 0.4058 | 0.0674 | +0.3384 ± 0.0071 | 1.063 | 0.2371 | 0.6698 | 0.1315 | 0.1005 | -0.072 ± 0.006 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 340 | 0.1953 | 0.198 | -0.0027 ± 0.0009 | 0.5695 | 0.5768 | 0.4979 | 0.4827 | 0.5559 | -0.009 ± 0.0243 | -0.0133 (6) |
| 3-5 | 238 | 0.188 | 0.1867 | +0.0014 ± 0.0022 | 0.5521 | 0.5487 | 0.4973 | 0.4579 | 0.4622 | -0.108 ± 0.0295 | -0.01 (1) |
| 5-10 | 485 | 0.2004 | 0.1983 | +0.0021 ± 0.003 | 0.5885 | 0.5815 | 0.5099 | 0.4361 | 0.4536 | -0.092 ± 0.0209 | -0.01 (4) |
| 10-15 | 368 | 0.2158 | 0.2141 | +0.0017 ± 0.006 | 0.6217 | 0.6119 | 0.5373 | 0.415 | 0.4701 | -0.074 ± 0.0239 | -0.044 (5) |
| 15-25 | 435 | 0.2296 | 0.2088 | +0.0208 ± 0.0086 | 0.6591 | 0.6025 | 0.5797 | 0.3863 | 0.4299 | -0.104 ± 0.0216 | -0.03 (1) |
| 25-40 | 261 | 0.2021 | 0.2055 | -0.0034 ± 0.0163 | 0.5869 | 0.5896 | 0.6528 | 0.3412 | 0.4981 | -0.045 ± 0.0241 | 0.0 (1) |
| 40+ | 49 | 0.3106 | 0.1697 | +0.1409 ± 0.0534 | 0.834 | 0.5113 | 0.7427 | 0.2906 | 0.3673 | -0.138 ± 0.0533 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1598 | 0.1827 | 0.1836 | -0.0009 ± 0.0004 | 0.5383 | 0.5401 | 0.4813 | 0.4662 | 0.4994 | -0.022 ± 0.0108 | -0.0183 (23) |
| 3-5 | 1117 | 0.1836 | 0.1812 | +0.0024 ± 0.001 | 0.5423 | 0.5367 | 0.4743 | 0.4351 | 0.4244 | -0.074 ± 0.0132 | -0.0243 (7) |
| 5-10 | 2464 | 0.1901 | 0.1849 | +0.0051 ± 0.0013 | 0.5635 | 0.5469 | 0.4809 | 0.407 | 0.4091 | -0.060 ± 0.0087 | -0.01 (18) |
| 10-15 | 1898 | 0.1978 | 0.1819 | +0.0158 ± 0.0024 | 0.5808 | 0.5328 | 0.4929 | 0.3698 | 0.3656 | -0.073 ± 0.0097 | -0.03 (9) |
| 15-25 | 2499 | 0.2071 | 0.1687 | +0.0384 ± 0.0032 | 0.6085 | 0.5009 | 0.4969 | 0.3015 | 0.3029 | -0.069 ± 0.0083 | -0.03 (2) |
| 25-40 | 1918 | 0.212 | 0.1174 | +0.0946 ± 0.0049 | 0.6145 | 0.3653 | 0.5209 | 0.2038 | 0.2164 | -0.059 ± 0.0074 | 0.0 (1) |
| 40+ | 1277 | 0.3859 | 0.0453 | +0.3405 ± 0.0067 | 1.0077 | 0.1787 | 0.6299 | 0.1071 | 0.054 | -0.087 ± 0.0057 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 630 | 0.2032 | 0.2035 | -0.0003 ± 0.0006 | 0.5896 | 0.5898 | 0.4998 | 0.4848 | 0.4921 | -0.042 ± 0.018 | -0.0226 (46) |
| 3-5 | 470 | 0.2003 | 0.1989 | +0.0014 ± 0.0017 | 0.582 | 0.5769 | 0.4807 | 0.4411 | 0.4426 | -0.053 ± 0.0206 | -0.0058 (33) |
| 5-10 | 957 | 0.1928 | 0.187 | +0.0057 ± 0.0021 | 0.5699 | 0.5551 | 0.4793 | 0.4058 | 0.4054 | -0.061 ± 0.0142 | -0.0049 (73) |
| 10-15 | 620 | 0.2045 | 0.1945 | +0.0100 ± 0.0044 | 0.5976 | 0.5707 | 0.4901 | 0.3672 | 0.3871 | -0.045 ± 0.0177 | 0.0014 (64) |
| 15-25 | 823 | 0.2352 | 0.2093 | +0.0259 ± 0.0063 | 0.669 | 0.6041 | 0.5522 | 0.358 | 0.39 | -0.057 ± 0.016 | -0.0216 (58) |
| 25-40 | 466 | 0.2502 | 0.1869 | +0.0634 ± 0.0125 | 0.7037 | 0.5475 | 0.6334 | 0.32 | 0.3734 | -0.084 ± 0.0187 | -0.0216 (25) |
| 40+ | 157 | 0.3608 | 0.1894 | +0.1714 ± 0.0356 | 1.0507 | 0.5579 | 0.7856 | 0.2918 | 0.3885 | -0.064 ± 0.0319 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1948 | 0.193 | 0.193 | -0.0000 ± 0.0004 | 0.5629 | 0.5617 | 0.5003 | 0.4851 | 0.4897 | -0.038 ± 0.0099 | -0.0155 (82) |
| 3-5 | 1366 | 0.1895 | 0.1866 | +0.0029 ± 0.0009 | 0.5539 | 0.5471 | 0.4891 | 0.4496 | 0.4341 | -0.061 ± 0.0117 | -0.0148 (63) |
| 5-10 | 2748 | 0.1909 | 0.1827 | +0.0082 ± 0.0012 | 0.5656 | 0.5429 | 0.4758 | 0.4021 | 0.3872 | -0.067 ± 0.0083 | -0.0087 (125) |
| 10-15 | 1857 | 0.2008 | 0.1866 | +0.0142 ± 0.0025 | 0.5887 | 0.5516 | 0.5037 | 0.3805 | 0.384 | -0.055 ± 0.0099 | -0.0053 (105) |
| 15-25 | 2369 | 0.2307 | 0.1975 | +0.0332 ± 0.0036 | 0.6655 | 0.5743 | 0.5465 | 0.3514 | 0.3651 | -0.060 ± 0.0092 | -0.0255 (106) |
| 25-40 | 1633 | 0.2491 | 0.1626 | +0.0865 ± 0.0063 | 0.7075 | 0.4836 | 0.5971 | 0.2823 | 0.3043 | -0.073 ± 0.0097 | -0.0206 (47) |
| 40+ | 791 | 0.3809 | 0.1197 | +0.2612 ± 0.0132 | 1.0777 | 0.3708 | 0.6964 | 0.1885 | 0.1972 | -0.069 ± 0.0116 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2176 | 1.06 ± 0.06 | 1.176 | 0.1692 | 0.17 | 0.2112 | 0.202 |
| gen2 | 2176 | 0.855 ± 0.053 | 1.115 | 0.1859 | 0.1693 | 0.2288 | 0.202 |
| gen1_elo | 2176 | 1.058 ± 0.059 | 1.163 | 0.173 | 0.1704 | 0.2094 | 0.202 |
| gen1_sr | 2176 | 1.049 ± 0.068 | 1.191 | 0.144 | 0.1717 | 0.2239 | 0.2018 |
| gen1_ledger | 4123 | 0.877 ± 0.039 | 1.066 | 0.1735 | 0.1889 | 0.2183 | 0.1965 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 11,299)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,084 | 27.3% |
| STALE_QUOTE | market_freshness | 2,273 | 20.1% |
| BOOK_QUALITY | execution | 1,969 | 17.4% |
| POOR_DATA | data | 1,196 | 10.6% |
| LIMITED_DATA | data | 880 | 7.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 622 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 511 | 4.5% |
| IDENTITY_AMBIGUOUS | mapping | 362 | 3.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 336 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 66 | 0.6% |

Cause class: coverage 27.3%, market_freshness 20.1%, data 18.4%, execution 17.4%, market_freshness/coverage 8.5%, model_calibration_or_unknown 4.5%, mapping 3.2%, model_calibration 0.6%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.1%, START_UNVERIFIABLE 96.0%, LOW_DATA_QUALITY 68.1%, STALE_PLAYER_DATA 57.0%, THIN_PLAYER_HISTORY 56.2%, STALE_KALSHI_QUOTE 47.1%, MODEL_INTERNAL_DISAGREEMENT 37.1%, ASYMMETRIC_SAMPLE_SIZE 30.0%, WIDE_SPREAD 23.3%, MODEL_HIGH_UNCERTAINTY 16.4%, PLAYER_IDENTITY_RISK 11.6%, LEVEL_TRANSFER_RISK 8.9%, EVENT_MAPPING_RISK 8.1%, LOW_DISPLAYED_LIQUIDITY 7.4%, MODEL_CALIBRATION_OUTLIER 3.5%, EXTERNAL_MARKET_REJECTION 0.9%, UNKNOWN 0.6%, EXTERNAL_MARKET_CONFIRMATION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 29.8%, POST_SETTLEMENT_OBSERVATION 27.3%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### >= ge_25 pp (N = 6,127)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,424 | 39.6% |
| BOOK_QUALITY | execution | 1,034 | 16.9% |
| STALE_QUOTE | market_freshness | 1,013 | 16.5% |
| POOR_DATA | data | 489 | 8.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 337 | 5.5% |
| LIMITED_DATA | data | 262 | 4.3% |
| IDENTITY_AMBIGUOUS | mapping | 227 | 3.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 209 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 113 | 1.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 19 | 0.3% |

Cause class: coverage 39.6%, execution 16.9%, market_freshness 16.5%, data 12.3%, market_freshness/coverage 8.9%, mapping 3.7%, model_calibration_or_unknown 1.8%, model_calibration 0.3%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.5%, START_UNVERIFIABLE 98.1%, LOW_DATA_QUALITY 71.3%, THIN_PLAYER_HISTORY 58.0%, STALE_KALSHI_QUOTE 55.1%, STALE_PLAYER_DATA 51.4%, MODEL_INTERNAL_DISAGREEMENT 38.4%, ASYMMETRIC_SAMPLE_SIZE 31.8%, WIDE_SPREAD 22.9%, MODEL_HIGH_UNCERTAINTY 17.8%, PLAYER_IDENTITY_RISK 14.7%, EVENT_MAPPING_RISK 9.9%, LOW_DISPLAYED_LIQUIDITY 7.5%, LEVEL_TRANSFER_RISK 7.5%, MODEL_CALIBRATION_OUTLIER 4.4%, EXTERNAL_MARKET_REJECTION 0.5%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 42.4%, POST_SETTLEMENT_OBSERVATION 39.6%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.7%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 5062, "IDENTITY_AMBIGUOUS": 1065}; ticker orientation: {"VERIFIED": 6127}.

Checks: discipline:AMBIGUOUS 443, discipline:PASS 5684, identity_confidence:AMBIGUOUS 902, identity_confidence:PASS 5225, level_mapping:NA 455, level_mapping:PASS 5672, market_pair:AMBIGUOUS 221, market_pair:NA 140, market_pair:PASS 5766, model_complement:NA 107, model_complement:PASS 6020, namesake:PASS 6127, physical_match_id:NA 2527, physical_match_id:PASS 3600, player_ids:PASS 6127, same_pair_other_event:PASS 6127, ticker_orientation:PASS 6127

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,876 | 1.5% | 1.5% | 0.5% | {"market_freshness": 20, "execution": 8} | 5.24 | 0.2072 / 0.205 (203) | 17.3% | 0.1% | 5.9% | 1.7% |
| CHALLENGER | 4,083 | 17.8% | 5.8% | 11.8% | {"coverage": 455, "market_freshness": 108, "market_freshness/coverage": 87, "model_calibration_or_unknown": 39, "data": 25, "execution": 8, "model_calibration": 3} | 6.72 | 0.2242 / 0.2062 (948) | 43.1% | 4.8% | 1.7% | 23.0% |
| DOUBLES | 860 | 51.5% | 51.1% | 7.2% | {"execution": 165, "mapping": 134, "market_freshness": 106, "market_freshness/coverage": 31, "coverage": 7} | 25.72 | 0.3281 / 0.23 (244) | 27.2% | 0.0% | 100.0% | 7.8% |
| ITF_MEN | 8,274 | 23.4% | 15.2% | 31.6% | {"coverage": 812, "execution": 392, "data": 271, "market_freshness": 270, "market_freshness/coverage": 169, "mapping": 19, "model_calibration_or_unknown": 1} | 10.29 | 0.2101 / 0.1939 (2051) | 37.7% | 53.3% | 6.3% | 24.3% |
| ITF_WOMEN | 10,650 | 26.0% | 17.6% | 45.2% | {"coverage": 1133, "market_freshness": 447, "execution": 444, "data": 427, "market_freshness/coverage": 218, "mapping": 68, "model_calibration_or_unknown": 23, "model_calibration": 9} | 12.14 | 0.2052 / 0.1921 (2313) | 38.7% | 57.0% | 9.5% | 24.2% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,193 | 7.4% | 6.5% | 1.4% | {"market_freshness": 35, "model_calibration_or_unknown": 20, "data": 11, "market_freshness/coverage": 9, "model_calibration": 4, "execution": 4, "coverage": 4, "mapping": 1} | 7.78 | 0.2167 / 0.2137 (189) | 29.3% | 1.8% | 1.1% | 2.9% |
| WTA125 | 946 | 13.5% | 10.1% | 2.1% | {"market_freshness/coverage": 31, "model_calibration_or_unknown": 28, "market_freshness": 25, "data": 17, "coverage": 12, "execution": 8, "mapping": 4, "model_calibration": 3} | 9.55 | 0.2353 / 0.2197 (309) | 24.6% | 7.1% | 3.8% | 10.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 5 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 6 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 7 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 8 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 9 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 10 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 11 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 12 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 14 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 15 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 16 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 9.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 553 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 18 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 19 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 20 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 21 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 22 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 874 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 23 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 24 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 25 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 26 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 27 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 28 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 29 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 30 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 31 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 189 min (STALE); no external reference |
| 32 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 33 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 34 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 110 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 35 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 36 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 37 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 253 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 38 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 39 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 22 min (AGING); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 40 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 41 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 42 | `KXITFWMATCH-26OCT08ARISAV-SAV` | ITF_WOMEN | fair_v1 | 75% / 2% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 43 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 256 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 44 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 687 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 45 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 46 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 47 | `KXITFMATCH-26OCT09DELSTE-DEL` | ITF_MEN | fair_v1 | 78% / 6% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.9h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 780 min (STALE); data POOR (grade F, thinner serve sample 477.0, ratio 8.93); no external reference |
| 48 | `KXITFWMATCH-26OCT08ARAWAN-ARA` | ITF_WOMEN | fair_v1 | 77% / 6% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 123 min (STALE); data POOR (grade D, thinner serve sample 553.0, ratio 3.97); no external reference |
| 49 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 708 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9811, "by_level_share_of_ge_25pp": {"ATP": 0.0046, "CHALLENGER": 0.1183, "DOUBLES": 0.0723, "ITF_MEN": 0.3157, "ITF_WOMEN": 0.4519, "OTHER": 0.002, "WTA": 0.0144, "WTA125": 0.0209}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.551, "share_primary_cause_market_settled_or_in_play": 0.4847, "share_primary_cause_stale_quote_only": 0.1653}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 6127, "identity_ambiguous_share": 0.1738, "ticker_orientation": {"VERIFIED": 6127}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 3600, "with_external": 83, "coverage": 0.0231, "external_status": {"EXTERNAL_STALE": 61, "AGREES_WITH_KALSHI": 22}, "triangulation": {"INSUFFICIENT_INPUTS": 61, "MODEL_LONE_OUTLIER": 22}, "share_external_agrees_with_kalshi": 0.2651, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 1531, "with_external": 81, "coverage": 0.0529, "external_status": {"EXTERNAL_STALE": 59, "AGREES_WITH_KALSHI": 22}, "triangulation": {"INSUFFICIENT_INPUTS": 59, "MODEL_LONE_OUTLIER": 22}, "share_external_agrees_with_kalshi": 0.2716, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 643.0, "median_sample_ratio": 2.28, "median_min_matches": 21.0, "median_max_days_since_last": 197.0, "share_severe_asymmetry": 0.1725, "data_status": {"POOR": 3105, "LIMITED": 1884, "ADEQUATE": 1138}, "comparison_lt_10pp": {"median_thinner_serve_points": 1892.0, "median_sample_ratio": 1.67, "median_min_matches": 85.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 470, "model_minus_observed": 0.0614, "kalshi_minus_observed": -0.071, "brier_diff_model_minus_kalshi": 0.0031}, "4-10x": {"n": 323, "model_minus_observed": 0.0582, "kalshi_minus_observed": -0.0836, "brier_diff_model_minus_kalshi": 0.0005}, "<2x": {"n": 1079, "model_minus_observed": 0.0862, "kalshi_minus_observed": -0.0353, "brier_diff_model_minus_kalshi": 0.0126}, ">=10x": {"n": 304, "model_minus_observed": 0.1114, "kalshi_minus_observed": -0.0563, "brier_diff_model_minus_kalshi": 0.0162}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2176, "model": {"intercept": -0.551, "slope": 0.855, "slope_se": 0.053}, "kalshi_mid_same_rows": {"intercept": 0.211, "slope": 1.115, "slope_se": 0.061}, "mean_extremity_model": 0.1859, "mean_extremity_kalshi": 0.1693, "model_brier": 0.2288, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0268, "brier_diff_se": 0.004, "model_logloss": 0.6539, "kalshi_logloss": 0.5863}, "fair_v1": {"n": 2176, "model": {"intercept": -0.4, "slope": 1.06, "slope_se": 0.06}, "kalshi_mid_same_rows": {"intercept": 0.316, "slope": 1.176, "slope_se": 0.063}, "mean_extremity_model": 0.1692, "mean_extremity_kalshi": 0.17, "model_brier": 0.2112, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0092, "brier_diff_se": 0.0032, "model_logloss": 0.6096, "kalshi_logloss": 0.5859}, "gen1_elo": {"n": 2176, "model": {"intercept": -0.378, "slope": 1.058, "slope_se": 0.059}, "kalshi_mid_same_rows": {"intercept": 0.316, "slope": 1.163, "slope_se": 0.062}, "mean_extremity_model": 0.173, "mean_extremity_kalshi": 0.1704, "model_brier": 0.2094, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0074, "brier_diff_se": 0.0032, "model_logloss": 0.6066, "kalshi_logloss": 0.5859}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2438, "share_ge_15": 0.4274, "median_abs_gap": 12.75, "n": 14768}, "gen1_elo": {"share_ge_25": 0.2369, "share_ge_15": 0.4244, "median_abs_gap": 12.26, "n": 14768}, "gen1_sr": {"share_ge_25": 0.2962, "share_ge_15": 0.5109, "median_abs_gap": 15.41, "n": 14768}, "gen2": {"share_ge_25": 0.3005, "share_ge_15": 0.4997, "median_abs_gap": 14.99, "n": 14768}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1378, "share_ge_15": 0.325, "median_abs_gap": 10.18, "n": 11108}, "gen1_elo": {"share_ge_25": 0.1342, "share_ge_15": 0.3188, "median_abs_gap": 9.59, "n": 11107}, "gen1_sr": {"share_ge_25": 0.19, "share_ge_15": 0.4185, "median_abs_gap": 12.54, "n": 11108}, "gen2": {"share_ge_25": 0.2087, "share_ge_15": 0.4216, "median_abs_gap": 12.44, "n": 11109}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.24, "share_ge_25_all": 0.0149, "share_ge_25_pregame_clean": 0.0152}, "WTA": {"median_abs_gap_pregame_clean": 7.78, "share_ge_25_all": 0.0738, "share_ge_25_pregame_clean": 0.0648}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2431, "share_within_10pp_all": 0.4431, "share_within_10pp_pregame_clean": 0.5075, "corr_model_vs_mid_pregame_clean": 0.8521}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 339, "model_brier": 0.1929, "kalshi_brier": 0.1943, "brier_diff_model_minus_kalshi": -0.0015}, "10-15": {"n_settled": 394, "model_brier": 0.213, "kalshi_brier": 0.2049, "brier_diff_model_minus_kalshi": 0.0081}, "15-25": {"n_settled": 458, "model_brier": 0.229, "kalshi_brier": 0.2149, "brier_diff_model_minus_kalshi": 0.0142}, "25-40": {"n_settled": 257, "model_brier": 0.2195, "kalshi_brier": 0.2015, "brier_diff_model_minus_kalshi": 0.0181}, "3-5": {"n_settled": 223, "model_brier": 0.1893, "kalshi_brier": 0.1907, "brier_diff_model_minus_kalshi": -0.0015}, "40+": {"n_settled": 57, "model_brier": 0.2912, "kalshi_brier": 0.167, "brier_diff_model_minus_kalshi": 0.1242}, "5-10": {"n_settled": 448, "model_brier": 0.2013, "kalshi_brier": 0.2023, "brier_diff_model_minus_kalshi": -0.001}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.551, "slope": 0.855, "slope_se": 0.053}, "kalshi_slope": {"intercept": 0.211, "slope": 1.115, "slope_se": 0.061}, "n": 2176}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.533, "slope": 0.877, "slope_se": 0.039}, "kalshi_slope": {"intercept": 0.125, "slope": 1.066, "slope_se": 0.043}, "n": 4123}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 244, "model_brier": 0.3281, "kalshi_brier": 0.23, "brier_diff_model_minus_kalshi": 0.0981, "brier_diff_se": 0.0206, "corr_model_outcome": -0.0148, "corr_kalshi_outcome": 0.2896}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
