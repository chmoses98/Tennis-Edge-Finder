# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-17T05:28Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 35,714): 0-3 14.5%, 3-5 9.5%, 5-10 20.0%, 10-15 15.2%, 15-25 18.8%, 25-40 13.6%, 40+ 8.3%; median gap 11.85 pp.
* **Where the extremes live**: 98.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.0%, Challenger 12.2%, doubles 6.7%). Main tour: ATP 1.6% and WTA 5.9% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 7,822): MARKET_ALREADY_SETTLED_WHEN_PRICED 36.6%, STALE_QUOTE 18.2%, BOOK_QUALITY 17.3%, POOR_DATA 8.4%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 4.0%, IN_PLAY_QUOTE 3.2%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.5%. By class: coverage 36.6%, market_freshness 18.2%, execution 17.3%, data 12.4%, market_freshness/coverage 8.7%, mapping 4.3%, model_calibration_or_unknown 2.0%, model_calibration 0.5%.
* **Stale / settled / in-play**: 53.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 45.3% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 7,822 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.0% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 3.9%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 21.9% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 562.0 points vs 1798.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.062, Gen-2 0.859, Gen-1 ledger 0.875 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 364 model 0.2241 vs Kalshi 0.208; n 74 model 0.2888 vs Kalshi 0.1769.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 142,942 model-market comparisons (237,542 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 50,060 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-17T05:22:50.871342+00:00'], shadow board 39,714 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-17T05:22:53.019379+00:00'], Model 4 15,182 rows, 15,004 settled tickers, 5,176 tickers with an external scan.
* By model: {"gen1_ledger": 33127, "gen1_elo": 19971, "fair_v1": 19971, "gen2": 19971, "gen1_sr": 19971, "model4_fundamental": 14970, "model4_conditioned": 14961}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 35,714 | 14.5 | 9.5 | 20.0 | 15.2 | 18.8 | 13.6 | 8.3 | 11.85 | 40.7% | 21.9% |
| MW fair_v1 | 19,971 | 13.6 | 8.4 | 18.5 | 15.7 | 19.2 | 14.6 | 9.9 | 12.99 | 43.8% | 24.6% |
| MW gen1_elo | 19,971 | 13.2 | 9.0 | 19.7 | 15.1 | 19.1 | 14.3 | 9.7 | 12.47 | 43.1% | 23.9% |
| MW gen1_ledger | 15,743 | 15.8 | 10.8 | 21.9 | 14.7 | 18.3 | 12.3 | 6.2 | 10.39 | 36.9% | 18.5% |
| MW gen1_sr | 19,971 | 9.7 | 7.5 | 16.3 | 14.2 | 21.5 | 18.7 | 12.0 | 15.88 | 52.3% | 30.8% |
| MW gen2 | 19,971 | 11.4 | 7.1 | 16.5 | 14.1 | 20.0 | 17.7 | 13.2 | 15.43 | 50.9% | 30.9% |
| all families model4_conditioned | 14,961 | 21.6 | 19.8 | 34.8 | 17.0 | 4.6 | 1.4 | 0.9 | 5.86 | 6.9% | 2.3% |
| all families model4_fundamental | 14,970 | 16.7 | 13.3 | 35.2 | 19.7 | 10.9 | 3.0 | 1.1 | 7.65 | 15.0% | 4.1% |

Configurable thresholds (primary): >=5pp 76.0%, >=10pp 56.0%, >=15pp 40.7%, >=20pp 30.3%, >=25pp 21.9%, >=30pp 15.9%, >=40pp 8.3%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.49pp; >=10pp 45.4%, >=25pp 17.5%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,408 | 31.0 | 14.2 | 24.9 | 17.1 | 10.8 | 1.3 | 0.8 | 5.75 | 12.9% | 2.1% |
| CHALLENGER | 3,308 | 16.0 | 9.8 | 20.1 | 15.8 | 14.4 | 12.3 | 11.6 | 11.5 | 38.3% | 23.8% |
| ITF_MEN | 5,708 | 10.9 | 8.2 | 17.6 | 14.8 | 19.8 | 16.4 | 12.4 | 14.45 | 48.6% | 28.8% |
| ITF_WOMEN | 7,835 | 10.5 | 6.6 | 16.1 | 15.7 | 22.2 | 18.0 | 11.0 | 15.49 | 51.2% | 29.0% |
| WTA | 1,071 | 20.7 | 12.1 | 25.3 | 15.5 | 19.8 | 5.5 | 1.0 | 7.78 | 26.3% | 6.5% |
| WTA125 | 641 | 13.1 | 7.6 | 23.6 | 20.3 | 20.0 | 13.4 | 2.0 | 11.2 | 35.4% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,408 | 24.5 | 14.4 | 24.7 | 18.8 | 14.3 | 2.1 | 1.1 | 6.74 | 17.5% | 3.2% |
| CHALLENGER | 3,308 | 14.8 | 8.0 | 19.4 | 13.5 | 17.9 | 14.3 | 12.2 | 12.74 | 44.4% | 26.5% |
| ITF_MEN | 5,708 | 9.5 | 6.8 | 15.8 | 13.6 | 19.8 | 19.5 | 15.0 | 16.84 | 54.3% | 34.5% |
| ITF_WOMEN | 7,835 | 8.6 | 5.7 | 13.8 | 13.4 | 21.3 | 20.8 | 16.5 | 18.69 | 58.6% | 37.3% |
| WTA | 1,071 | 17.2 | 8.2 | 20.7 | 15.4 | 22.1 | 15.2 | 1.1 | 11.5 | 38.5% | 16.3% |
| WTA125 | 641 | 6.4 | 4.8 | 17.5 | 17.9 | 25.1 | 19.2 | 9.1 | 16.84 | 53.3% | 28.2% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,408 | 28.3 | 13.8 | 28.3 | 15.3 | 11.1 | 2.3 | 0.8 | 6.1 | 14.3% | 3.2% |
| CHALLENGER | 3,308 | 14.7 | 10.3 | 20.8 | 15.0 | 15.4 | 12.0 | 11.8 | 11.02 | 39.2% | 23.8% |
| ITF_MEN | 5,708 | 10.0 | 8.1 | 18.0 | 14.1 | 20.5 | 16.7 | 12.6 | 14.97 | 49.8% | 29.3% |
| ITF_WOMEN | 7,835 | 9.9 | 7.0 | 16.6 | 15.7 | 22.7 | 17.9 | 10.2 | 15.38 | 50.9% | 28.2% |
| WTA | 1,071 | 23.4 | 16.1 | 31.6 | 15.2 | 10.7 | 2.2 | 0.7 | 6.05 | 13.6% | 2.9% |
| WTA125 | 641 | 22.3 | 12.5 | 29.3 | 15.4 | 14.2 | 5.9 | 0.3 | 7.73 | 20.4% | 6.2% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 794 | 31.4 | 22.5 | 33.8 | 9.9 | 1.6 | 0.8 | 0.0 | 4.63 | 2.4% | 0.8% |
| CHALLENGER | 2,257 | 22.7 | 15.1 | 27.6 | 14.7 | 12.8 | 5.2 | 2.0 | 6.93 | 20.0% | 7.2% |
| DOUBLES | 1,073 | 5.2 | 3.8 | 11.2 | 10.8 | 20.1 | 24.6 | 24.2 | 24.11 | 69.0% | 48.8% |
| ITF_MEN | 4,814 | 14.7 | 8.7 | 20.7 | 15.4 | 20.8 | 12.6 | 7.1 | 11.86 | 40.5% | 19.7% |
| ITF_WOMEN | 5,183 | 11.8 | 9.3 | 19.4 | 14.9 | 22.3 | 16.5 | 5.9 | 13.04 | 44.6% | 22.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 761 | 21.8 | 16.2 | 28.2 | 16.4 | 12.2 | 4.7 | 0.4 | 6.98 | 17.3% | 5.1% |
| WTA125 | 712 | 20.9 | 13.9 | 22.6 | 18.4 | 14.0 | 8.0 | 2.1 | 8.2 | 24.2% | 10.1% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,394 | 31.0 | 14.1 | 25.0 | 17.1 | 10.8 | 1.2 | 0.8 | 5.82 | 12.8% | 2.0% |
| CHALLENGER | 2,348 | 20.9 | 12.4 | 25.3 | 18.3 | 14.9 | 5.9 | 2.3 | 8.23 | 23.1% | 8.2% |
| ITF_MEN | 4,153 | 13.3 | 10.1 | 20.9 | 16.6 | 20.2 | 13.3 | 5.7 | 11.53 | 39.1% | 18.9% |
| ITF_WOMEN | 5,852 | 12.4 | 8.0 | 18.3 | 17.8 | 23.6 | 14.9 | 5.1 | 13.08 | 43.6% | 20.0% |
| WTA | 1,051 | 20.9 | 11.6 | 25.6 | 15.5 | 19.9 | 5.4 | 1.1 | 7.82 | 26.4% | 6.5% |
| WTA125 | 615 | 13.5 | 7.5 | 23.1 | 20.6 | 20.6 | 13.0 | 1.6 | 11.31 | 35.3% | 14.6% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,394 | 24.4 | 14.5 | 24.8 | 18.8 | 14.3 | 2.1 | 1.1 | 6.76 | 17.5% | 3.2% |
| CHALLENGER | 2,348 | 18.9 | 10.4 | 24.3 | 16.2 | 18.2 | 9.4 | 2.5 | 9.01 | 30.1% | 11.9% |
| ITF_MEN | 4,154 | 11.1 | 8.1 | 18.2 | 15.3 | 21.9 | 16.9 | 8.5 | 14.1 | 47.3% | 25.4% |
| ITF_WOMEN | 5,852 | 9.7 | 6.5 | 15.3 | 14.6 | 23.3 | 20.0 | 10.5 | 16.41 | 53.8% | 30.5% |
| WTA | 1,051 | 17.1 | 8.1 | 20.7 | 15.4 | 22.2 | 15.3 | 1.1 | 11.55 | 38.6% | 16.5% |
| WTA125 | 615 | 6.2 | 5.0 | 17.6 | 18.4 | 25.0 | 19.7 | 8.1 | 16.68 | 52.8% | 27.8% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 774 | 31.4 | 22.7 | 34.0 | 10.1 | 1.0 | 0.8 | 0.0 | 4.62 | 1.8% | 0.8% |
| CHALLENGER | 1,941 | 24.6 | 16.4 | 29.7 | 14.4 | 11.9 | 2.4 | 0.5 | 6.31 | 14.8% | 2.9% |
| DOUBLES | 987 | 5.4 | 4.0 | 11.4 | 10.9 | 20.0 | 24.7 | 23.6 | 24.07 | 68.3% | 48.3% |
| ITF_MEN | 3,975 | 16.1 | 9.5 | 22.6 | 16.3 | 20.6 | 10.6 | 4.2 | 10.54 | 35.5% | 14.8% |
| ITF_WOMEN | 4,241 | 12.9 | 10.0 | 21.2 | 15.8 | 22.5 | 14.8 | 2.8 | 11.64 | 40.1% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 727 | 22.3 | 16.8 | 28.5 | 16.4 | 12.4 | 3.7 | 0.0 | 6.8 | 16.1% | 3.7% |
| WTA125 | 604 | 22.9 | 15.4 | 24.2 | 20.0 | 12.4 | 4.8 | 0.3 | 7.3 | 17.5% | 5.1% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,073 | 5.2 | 3.8 | 11.2 | 10.8 | 20.1 | 24.6 | 24.2 | 24.11 | 69.0% | 48.8% |
| singles | 14,670 | 16.5 | 11.3 | 22.6 | 15.0 | 18.2 | 11.4 | 4.9 | 9.86 | 34.5% | 16.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 4,696 | 13.3 | 8.8 | 19.2 | 15.7 | 18.1 | 14.7 | 10.2 | 12.75 | 42.9% | 24.9% |
| Grass | 228 | 10.5 | 11.4 | 18.4 | 14.0 | 22.4 | 15.3 | 7.9 | 14.04 | 45.6% | 23.2% |
| Hard | 12,920 | 14.0 | 8.4 | 18.5 | 15.2 | 19.6 | 14.4 | 9.9 | 12.97 | 43.9% | 24.2% |
| UNKNOWN | 2,127 | 12.1 | 7.3 | 16.9 | 18.7 | 19.1 | 15.7 | 10.2 | 13.35 | 45.0% | 25.9% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,823 | 19.9 | 10.7 | 21.2 | 16.8 | 15.7 | 8.9 | 6.8 | 9.45 | 31.4% | 15.7% |
| B | 2,614 | 13.9 | 9.1 | 19.6 | 16.3 | 18.6 | 12.3 | 10.2 | 12.01 | 41.1% | 22.5% |
| C | 2,899 | 12.6 | 9.5 | 20.0 | 14.2 | 19.2 | 14.5 | 10.0 | 12.69 | 43.7% | 24.5% |
| D | 3,417 | 11.8 | 7.8 | 17.4 | 15.8 | 21.9 | 15.4 | 9.8 | 13.94 | 47.1% | 25.2% |
| F | 5,218 | 8.1 | 5.4 | 14.9 | 14.8 | 21.7 | 21.6 | 13.4 | 17.98 | 56.8% | 35.1% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,629 | 23.3 | 15.9 | 28.8 | 15.1 | 11.0 | 4.3 | 1.6 | 6.62 | 17.0% | 6.0% |
| B | 2,346 | 14.9 | 10.1 | 24.0 | 16.4 | 19.3 | 10.9 | 4.3 | 10.18 | 34.5% | 15.2% |
| C | 3,104 | 12.1 | 7.8 | 18.0 | 14.4 | 20.9 | 15.7 | 11.2 | 13.84 | 47.8% | 26.9% |
| D | 2,328 | 14.1 | 9.8 | 20.6 | 13.8 | 21.3 | 13.8 | 6.7 | 11.86 | 41.8% | 20.5% |
| F | 3,336 | 10.5 | 7.7 | 15.3 | 13.9 | 23.4 | 20.3 | 8.9 | 16.16 | 52.6% | 29.2% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 6,583 | 18.1 | 9.7 | 20.4 | 16.6 | 16.3 | 9.9 | 9.1 | 10.51 | 35.3% | 19.0% |
| LIMITED | 4,629 | 14.6 | 10.4 | 20.8 | 15.3 | 18.6 | 12.9 | 7.5 | 11.31 | 39.0% | 20.4% |
| POOR | 8,759 | 9.7 | 6.5 | 15.9 | 15.2 | 21.8 | 19.0 | 11.9 | 15.99 | 52.7% | 30.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,305 | 30.4 | 24.0 | 35.6 | 6.8 | 2.1 | 0.9 | 0.1 | 4.6 | 3.2% | 1.0% |
| GAME_SPREAD | 3,048 | 25.7 | 16.2 | 36.1 | 17.2 | 4.2 | 0.4 | 0.2 | 5.99 | 4.9% | 0.7% |
| MATCH_WINNER | 15,743 | 15.8 | 10.8 | 21.9 | 14.7 | 18.3 | 12.3 | 6.2 | 10.39 | 36.9% | 18.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 6,201 | 32.9 | 19.1 | 30.7 | 10.3 | 5.6 | 1.3 | 0.2 | 4.81 | 7.1% | 1.5% |
| TOTAL_GAMES | 4,806 | 6.6 | 8.9 | 38.5 | 29.2 | 11.3 | 3.2 | 2.3 | 9.55 | 16.8% | 5.5% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,202 | 25.6 | 37.5 | 31.1 | 1.1 | 3.8 | 0.6 | 0.2 | 4.32 | 4.7% | 0.8% |
| GAME_SPREAD | 3,669 | 45.5 | 16.6 | 28.2 | 7.4 | 1.2 | 0.7 | 0.3 | 3.49 | 2.2% | 1.1% |
| TOTAL_GAMES | 6,090 | 3.7 | 6.5 | 41.8 | 36.4 | 7.2 | 2.4 | 1.9 | 9.82 | 11.6% | 4.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,202 | 26.4 | 18.3 | 36.8 | 9.4 | 6.5 | 2.3 | 0.4 | 5.53 | 9.2% | 2.6% |
| GAME_SPREAD | 3,669 | 19.5 | 13.5 | 30.0 | 20.9 | 13.0 | 2.5 | 0.7 | 7.75 | 16.1% | 3.2% |
| TOTAL_GAMES | 6,099 | 6.8 | 9.0 | 37.1 | 27.7 | 13.4 | 3.9 | 2.1 | 9.69 | 19.3% | 6.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 19,971 | 43.8% | 24.6% | 12.99 | 35.0% | 15.2% | 10.64 |
| gen1_elo | 19,971 | 43.1% | 23.9% | 12.47 | 33.9% | 14.9% | 10.08 |
| gen1_sr | 19,971 | 52.3% | 30.8% | 15.88 | 44.4% | 21.4% | 13.23 |
| gen2 | 19,971 | 50.9% | 30.9% | 15.43 | 44.1% | 22.8% | 13.01 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 10,656 | 16.5 | 10.4 | 21.6 | 17.2 | 19.6 | 11.3 | 3.4 | 10.41 | 34.3% | 14.7% |
| STALE | 9,315 | 10.2 | 6.2 | 15.0 | 14.0 | 18.8 | 18.4 | 17.5 | 17.35 | 54.6% | 35.9% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 9,211 | 17.6 | 11.7 | 23.4 | 14.7 | 16.8 | 11.1 | 4.7 | 9.34 | 32.6% | 15.8% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 35,714 | 9211 | 14128 | 12375 | 24.1 | 159.5 | 1400.4 |
| ge_15pp | 14,548 | 3007 | 4941 | 6600 | 26.9 | 462.7 | 1380.4 |
| ge_25pp | 7,822 | 1457 | 2153 | 4212 | 34.5 | 597.4 | 1380.4 |
| lt_10pp | 15,720 | 4852 | 6806 | 4062 | 22.2 | 48.3 | 1341.5 |

Current slate `SL-20261017T052835Z-6f46a16b`: 511 priced rows, quote age at build {'median': 6.0, 'max': 6.1}, freshness {'FRESH': 511}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 11 | 0.0 | 0.0 | 36.4 | 0.0 | 45.5 | 18.2 | 0.0 | 20.19 | 63.6% | 18.2% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,772 | 21.9 | 10.9 | 23.2 | 17.7 | 18.9 | 6.8 | 0.6 | 8.47 | 26.3% | 7.4% |
| KALSHI_LONE_OUTLIER | 9 | 11.1 | 0.0 | 66.7 | 0.0 | 11.1 | 11.1 | 0.0 | 5.14 | 22.2% | 11.1% |
| MARKETS_AGREE | 294 | 69.0 | 30.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.14 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 587 | 0.0 | 3.6 | 35.3 | 27.4 | 24.4 | 8.5 | 0.8 | 11.66 | 33.7% | 9.4% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 19,971 | 2685 (13.4%) | 21.9% | 0.7% | {"EXTERNAL_STALE": 1772, "AGREES_WITH_KALSHI": 587, "ALL_AGREE": 294, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 10, "AGREES_WITH_MODEL": 9, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 8,742 | 673 (7.7%) | 29.4% | 1.3% | {"EXTERNAL_STALE": 466, "AGREES_WITH_KALSHI": 198, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 4,903 | 189 (3.9%) | 29.1% | 1.6% | {"EXTERNAL_STALE": 131, "AGREES_WITH_KALSHI": 55, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,335 | 178 (7.6%) | 29.8% | 1.7% | {"EXTERNAL_STALE": 122, "AGREES_WITH_KALSHI": 53, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 8,099 | 1537 (19.0%) | 14.8% | 0.7% | {"EXTERNAL_STALE": 992, "ALL_AGREE": 294, "AGREES_WITH_KALSHI": 228, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 7, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,860 | 11.1 | 7.7 | 19.4 | 14.9 | 22.1 | 14.3 | 10.4 | 13.82 | 46.9% | 24.7% |
| 4-10x | 2,576 | 12.8 | 8.9 | 19.9 | 15.4 | 18.6 | 15.1 | 9.2 | 12.59 | 42.9% | 24.3% |
| <2x | 10,439 | 15.4 | 9.2 | 18.9 | 16.6 | 17.7 | 13.1 | 9.1 | 11.91 | 39.9% | 22.2% |
| >=10x | 3,096 | 11.0 | 6.5 | 15.1 | 13.6 | 21.2 | 19.5 | 13.0 | 16.49 | 53.8% | 32.5% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 5,316 | 13.5 | 8.3 | 19.3 | 15.8 | 19.9 | 12.8 | 10.4 | 12.8 | 43.1% | 23.2% |
| 300-1000 | 4,474 | 12.0 | 8.7 | 17.3 | 15.8 | 20.8 | 15.9 | 9.5 | 13.73 | 46.2% | 25.4% |
| <300 | 5,917 | 9.1 | 6.0 | 15.6 | 14.6 | 21.4 | 20.3 | 12.9 | 16.86 | 54.7% | 33.3% |
| >=3000 | 4,264 | 21.6 | 11.8 | 22.9 | 16.9 | 13.7 | 7.5 | 5.8 | 8.3 | 26.9% | 13.2% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 624 | 0.5372 | 0.4044 | 0.484 | +0.053 | -0.080 | 0.0002 ± 0.0059 |
| ratio 4-10x | 415 | 0.5855 | 0.4478 | 0.5108 | +0.075 | -0.063 | 0.0078 ± 0.0077 |
| ratio <2x | 1529 | 0.5364 | 0.4144 | 0.4539 | +0.083 | -0.040 | 0.0112 ± 0.0036 |
| ratio >=10x | 505 | 0.5439 | 0.377 | 0.4178 | +0.126 | -0.041 | 0.0158 ± 0.0078 |
| thinner_sample 1000-3000 | 866 | 0.5431 | 0.4178 | 0.4723 | +0.071 | -0.054 | 0.005 ± 0.0049 |
| thinner_sample 300-1000 | 739 | 0.5592 | 0.4211 | 0.4844 | +0.075 | -0.063 | 0.002 ± 0.0057 |
| thinner_sample <300 | 947 | 0.5427 | 0.3826 | 0.4351 | +0.108 | -0.052 | 0.016 ± 0.0056 |
| thinner_sample >=3000 | 521 | 0.5286 | 0.4352 | 0.4607 | +0.068 | -0.025 | 0.0142 ± 0.0051 |
| data_status ADEQUATE | 894 | 0.5332 | 0.4288 | 0.4597 | +0.073 | -0.031 | 0.0093 ± 0.0042 |
| data_status LIMITED | 766 | 0.5512 | 0.4221 | 0.4909 | +0.060 | -0.069 | 0.0024 ± 0.0053 |
| data_status POOR | 1413 | 0.5478 | 0.3931 | 0.4473 | +0.101 | -0.054 | 0.0129 ± 0.0045 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 478 | 0.1924 | 0.1939 | -0.0014 ± 0.0007 | 0.5629 | 0.5658 | 0.4938 | 0.479 | 0.5293 | -0.041 ± 0.0211 | -0.01 (5) |
| 3-5 | 295 | 0.1905 | 0.1909 | -0.0004 ± 0.002 | 0.5609 | 0.5605 | 0.509 | 0.4692 | 0.4915 | -0.071 ± 0.026 | 0.02 (1) |
| 5-10 | 645 | 0.1976 | 0.1969 | +0.0007 ± 0.0027 | 0.5809 | 0.5768 | 0.5095 | 0.435 | 0.4605 | -0.086 ± 0.0181 | -0.0167 (6) |
| 10-15 | 545 | 0.213 | 0.205 | +0.0081 ± 0.0049 | 0.614 | 0.5917 | 0.5175 | 0.3937 | 0.422 | -0.083 ± 0.0193 | -0.048 (5) |
| 15-25 | 672 | 0.2304 | 0.2153 | +0.0151 ± 0.007 | 0.6559 | 0.6163 | 0.5751 | 0.3799 | 0.4405 | -0.080 ± 0.0178 | -0.0033 (9) |
| 25-40 | 364 | 0.2241 | 0.208 | +0.0161 ± 0.0143 | 0.638 | 0.598 | 0.6448 | 0.3363 | 0.4643 | -0.061 ± 0.0218 | -0.01 (1) |
| 40+ | 74 | 0.2888 | 0.1769 | +0.1119 ± 0.0433 | 0.7848 | 0.5268 | 0.7422 | 0.2957 | 0.3919 | -0.107 ± 0.043 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2226 | 0.1781 | 0.1794 | -0.0013 ± 0.0003 | 0.5299 | 0.5314 | 0.478 | 0.463 | 0.5009 | -0.017 ± 0.0091 | -0.0129 (17) |
| 3-5 | 1357 | 0.1915 | 0.1897 | +0.0018 ± 0.001 | 0.5627 | 0.5543 | 0.4779 | 0.4383 | 0.4333 | -0.063 ± 0.012 | 0.0 (2) |
| 5-10 | 2999 | 0.1921 | 0.1894 | +0.0026 ± 0.0012 | 0.5664 | 0.5567 | 0.4828 | 0.4089 | 0.4251 | -0.047 ± 0.0081 | -0.0119 (21) |
| 10-15 | 2614 | 0.2019 | 0.183 | +0.0189 ± 0.0021 | 0.59 | 0.538 | 0.4779 | 0.3533 | 0.3405 | -0.075 ± 0.0083 | -0.0281 (16) |
| 15-25 | 3178 | 0.2087 | 0.171 | +0.0376 ± 0.0029 | 0.6096 | 0.5051 | 0.5012 | 0.3051 | 0.3087 | -0.068 ± 0.0073 | -0.0025 (44) |
| 25-40 | 2492 | 0.22 | 0.1262 | +0.0938 ± 0.0044 | 0.6331 | 0.389 | 0.5278 | 0.2148 | 0.2251 | -0.060 ± 0.0069 | -0.01 (1) |
| 40+ | 1686 | 0.3756 | 0.0429 | +0.3328 ± 0.0057 | 0.9779 | 0.1701 | 0.6258 | 0.1051 | 0.0563 | -0.085 ± 0.0047 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 355 | 0.1979 | 0.1983 | -0.0004 ± 0.0008 | 0.5772 | 0.578 | 0.5004 | 0.4852 | 0.507 | -0.078 ± 0.0248 | -0.01 (3) |
| 3-5 | 246 | 0.2088 | 0.2082 | +0.0006 ± 0.0024 | 0.5997 | 0.5996 | 0.5162 | 0.4761 | 0.4837 | -0.077 ± 0.0307 | 0.02 (1) |
| 5-10 | 563 | 0.1971 | 0.1962 | +0.0009 ± 0.0028 | 0.5772 | 0.5748 | 0.548 | 0.473 | 0.5044 | -0.073 ± 0.0193 | -0.01 (4) |
| 10-15 | 501 | 0.2171 | 0.2092 | +0.0079 ± 0.0051 | 0.6221 | 0.604 | 0.5671 | 0.4427 | 0.477 | -0.087 ± 0.0213 | -0.04 (5) |
| 15-25 | 742 | 0.2291 | 0.2091 | +0.0200 ± 0.0066 | 0.6502 | 0.6006 | 0.5866 | 0.39 | 0.4407 | -0.087 ± 0.017 | -0.0133 (9) |
| 25-40 | 483 | 0.2643 | 0.1998 | +0.0645 ± 0.0128 | 0.7396 | 0.5808 | 0.6596 | 0.3447 | 0.4017 | -0.106 ± 0.0202 | -0.0075 (4) |
| 40+ | 183 | 0.3611 | 0.1779 | +0.1832 ± 0.0307 | 1.0036 | 0.5267 | 0.7393 | 0.2576 | 0.3224 | -0.068 ± 0.0301 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1870 | 0.1818 | 0.1822 | -0.0004 ± 0.0003 | 0.5385 | 0.5393 | 0.4993 | 0.4846 | 0.5075 | -0.033 ± 0.0102 | -0.0133 (15) |
| 3-5 | 1185 | 0.192 | 0.1913 | +0.0008 ± 0.001 | 0.5588 | 0.557 | 0.5162 | 0.4762 | 0.4861 | -0.040 ± 0.0129 | 0.02 (1) |
| 5-10 | 2669 | 0.1903 | 0.1872 | +0.0031 ± 0.0013 | 0.5628 | 0.5516 | 0.5097 | 0.4356 | 0.4537 | -0.043 ± 0.0085 | -0.0117 (6) |
| 10-15 | 2306 | 0.1975 | 0.185 | +0.0125 ± 0.0022 | 0.5806 | 0.5401 | 0.517 | 0.3925 | 0.4072 | -0.053 ± 0.0091 | -0.0189 (18) |
| 15-25 | 3329 | 0.2161 | 0.1763 | +0.0398 ± 0.0029 | 0.6278 | 0.52 | 0.5307 | 0.3342 | 0.3343 | -0.073 ± 0.0074 | -0.0086 (42) |
| 25-40 | 2938 | 0.2475 | 0.137 | +0.1105 ± 0.0043 | 0.7016 | 0.4189 | 0.5583 | 0.2422 | 0.2274 | -0.082 ± 0.0068 | -0.0044 (18) |
| 40+ | 2255 | 0.3993 | 0.0668 | +0.3325 ± 0.0062 | 1.05 | 0.2334 | 0.6621 | 0.1257 | 0.0976 | -0.067 ± 0.0053 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 458 | 0.1926 | 0.1952 | -0.0026 ± 0.0007 | 0.564 | 0.5705 | 0.4942 | 0.4789 | 0.5524 | -0.003 ± 0.021 | -0.0137 (8) |
| 3-5 | 334 | 0.1895 | 0.1873 | +0.0022 ± 0.0019 | 0.5554 | 0.5503 | 0.4997 | 0.4602 | 0.4551 | -0.117 ± 0.0248 | 0.0067 (3) |
| 5-10 | 676 | 0.2025 | 0.1982 | +0.0043 ± 0.0026 | 0.5924 | 0.5788 | 0.504 | 0.4303 | 0.4349 | -0.097 ± 0.0175 | -0.0071 (7) |
| 10-15 | 530 | 0.2075 | 0.2065 | +0.0010 ± 0.0049 | 0.6026 | 0.5962 | 0.5362 | 0.4132 | 0.4736 | -0.063 ± 0.0196 | -0.0317 (6) |
| 15-25 | 624 | 0.2354 | 0.2099 | +0.0255 ± 0.0072 | 0.6702 | 0.604 | 0.5826 | 0.3893 | 0.4199 | -0.107 ± 0.0181 | -0.03 (1) |
| 25-40 | 381 | 0.2112 | 0.2121 | -0.0010 ± 0.0138 | 0.6097 | 0.6075 | 0.6493 | 0.3397 | 0.4934 | -0.042 ± 0.021 | 0.015 (2) |
| 40+ | 70 | 0.3064 | 0.1929 | +0.1135 ± 0.0469 | 0.8277 | 0.5631 | 0.7471 | 0.294 | 0.4 | -0.086 ± 0.0496 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2102 | 0.184 | 0.185 | -0.0009 ± 0.0003 | 0.5428 | 0.5443 | 0.4828 | 0.4676 | 0.4952 | -0.024 ± 0.0094 | -0.0163 (35) |
| 3-5 | 1449 | 0.1873 | 0.184 | +0.0033 ± 0.0009 | 0.5516 | 0.5437 | 0.4793 | 0.4398 | 0.4189 | -0.084 ± 0.0116 | -0.0094 (18) |
| 5-10 | 3191 | 0.1941 | 0.1875 | +0.0066 ± 0.0011 | 0.5723 | 0.551 | 0.48 | 0.4061 | 0.3961 | -0.070 ± 0.0077 | -0.01 (31) |
| 10-15 | 2468 | 0.1947 | 0.1799 | +0.0148 ± 0.0021 | 0.5737 | 0.529 | 0.4955 | 0.3722 | 0.3744 | -0.064 ± 0.0085 | -0.015 (12) |
| 15-25 | 3269 | 0.2099 | 0.1695 | +0.0403 ± 0.0028 | 0.6142 | 0.5024 | 0.5042 | 0.309 | 0.3047 | -0.073 ± 0.0072 | -0.03 (2) |
| 25-40 | 2445 | 0.2154 | 0.1247 | +0.0907 ± 0.0045 | 0.6228 | 0.3841 | 0.5248 | 0.2092 | 0.227 | -0.056 ± 0.0068 | 0.01 (3) |
| 40+ | 1628 | 0.3893 | 0.0464 | +0.3429 ± 0.006 | 1.0155 | 0.1792 | 0.6354 | 0.1083 | 0.0584 | -0.085 ± 0.0051 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 794 | 0.1951 | 0.1954 | -0.0002 ± 0.0005 | 0.5707 | 0.5709 | 0.5073 | 0.4922 | 0.5 | -0.047 ± 0.0157 | -0.0224 (49) |
| 3-5 | 566 | 0.1945 | 0.1939 | +0.0006 ± 0.0015 | 0.5672 | 0.5643 | 0.4808 | 0.441 | 0.4505 | -0.048 ± 0.0186 | -0.0194 (34) |
| 5-10 | 1189 | 0.1963 | 0.1904 | +0.0059 ± 0.0019 | 0.5787 | 0.5621 | 0.488 | 0.4144 | 0.4121 | -0.064 ± 0.0129 | -0.005 (78) |
| 10-15 | 750 | 0.208 | 0.197 | +0.0109 ± 0.0041 | 0.6047 | 0.576 | 0.5056 | 0.3825 | 0.3987 | -0.053 ± 0.0163 | 0.0014 (64) |
| 15-25 | 1002 | 0.2339 | 0.2115 | +0.0224 ± 0.0057 | 0.6666 | 0.6089 | 0.5639 | 0.3691 | 0.4102 | -0.057 ± 0.0145 | -0.0214 (59) |
| 25-40 | 580 | 0.2505 | 0.1959 | +0.0545 ± 0.0113 | 0.7065 | 0.5695 | 0.6457 | 0.3333 | 0.4 | -0.080 ± 0.0171 | -0.0219 (26) |
| 40+ | 193 | 0.3701 | 0.1933 | +0.1769 ± 0.0321 | 1.0713 | 0.5679 | 0.793 | 0.3026 | 0.3886 | -0.075 ± 0.029 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2366 | 0.1871 | 0.1872 | -0.0001 ± 0.0003 | 0.5498 | 0.5489 | 0.5021 | 0.4867 | 0.4975 | -0.034 ± 0.0089 | -0.0157 (88) |
| 3-5 | 1616 | 0.1878 | 0.1853 | +0.0025 ± 0.0009 | 0.55 | 0.5441 | 0.4884 | 0.4488 | 0.4381 | -0.057 ± 0.0108 | -0.0209 (69) |
| 5-10 | 3302 | 0.193 | 0.1853 | +0.0077 ± 0.0011 | 0.5705 | 0.5484 | 0.4819 | 0.4083 | 0.3958 | -0.064 ± 0.0076 | -0.0082 (132) |
| 10-15 | 2222 | 0.2043 | 0.1903 | +0.0140 ± 0.0023 | 0.5965 | 0.5591 | 0.5104 | 0.3873 | 0.392 | -0.054 ± 0.0092 | -0.0053 (105) |
| 15-25 | 2802 | 0.2305 | 0.1981 | +0.0324 ± 0.0033 | 0.6645 | 0.5756 | 0.5558 | 0.3606 | 0.3769 | -0.062 ± 0.0085 | -0.0253 (107) |
| 25-40 | 1902 | 0.2537 | 0.1698 | +0.0839 ± 0.006 | 0.7192 | 0.5018 | 0.6072 | 0.2931 | 0.3186 | -0.075 ± 0.0092 | -0.0229 (51) |
| 40+ | 913 | 0.385 | 0.1309 | +0.2541 ± 0.0128 | 1.0918 | 0.3995 | 0.7089 | 0.2019 | 0.218 | -0.068 ± 0.0114 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3073 | 1.062 ± 0.051 | 1.166 | 0.1681 | 0.1716 | 0.2114 | 0.2021 |
| gen2 | 3073 | 0.859 ± 0.046 | 1.124 | 0.1755 | 0.1716 | 0.2295 | 0.2021 |
| gen1_elo | 3073 | 1.045 ± 0.05 | 1.15 | 0.1733 | 0.172 | 0.2106 | 0.202 |
| gen1_sr | 3073 | 1.069 ± 0.06 | 1.189 | 0.1351 | 0.1733 | 0.2255 | 0.2019 |
| gen1_ledger | 5074 | 0.875 ± 0.035 | 1.077 | 0.1772 | 0.1859 | 0.2179 | 0.1975 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 14,548)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,621 | 24.9% |
| STALE_QUOTE | market_freshness | 3,037 | 20.9% |
| BOOK_QUALITY | execution | 2,595 | 17.8% |
| POOR_DATA | data | 1,599 | 11.0% |
| LIMITED_DATA | data | 1,046 | 7.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 788 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 693 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 586 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 411 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 172 | 1.2% |

Cause class: coverage 24.9%, market_freshness 20.9%, data 18.2%, execution 17.8%, market_freshness/coverage 8.2%, model_calibration_or_unknown 4.8%, mapping 4.0%, model_calibration 1.2%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 95.8%, LOW_DATA_QUALITY 69.1%, THIN_PLAYER_HISTORY 57.8%, STALE_PLAYER_DATA 52.1%, STALE_KALSHI_QUOTE 45.4%, MODEL_INTERNAL_DISAGREEMENT 39.5%, ASYMMETRIC_SAMPLE_SIZE 31.7%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 17.7%, PLAYER_IDENTITY_RISK 14.1%, LEVEL_TRANSFER_RISK 8.3%, EVENT_MAPPING_RISK 7.9%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 3.4%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 27.3%, POST_SETTLEMENT_OBSERVATION 24.9%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 7,822)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,863 | 36.6% |
| STALE_QUOTE | market_freshness | 1,426 | 18.2% |
| BOOK_QUALITY | execution | 1,355 | 17.3% |
| POOR_DATA | data | 656 | 8.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 425 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 339 | 4.3% |
| LIMITED_DATA | data | 312 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 254 | 3.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 153 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 39 | 0.5% |

Cause class: coverage 36.6%, market_freshness 18.2%, execution 17.3%, data 12.4%, market_freshness/coverage 8.7%, mapping 4.3%, model_calibration_or_unknown 2.0%, model_calibration 0.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.9%, START_UNVERIFIABLE 98.2%, LOW_DATA_QUALITY 72.7%, THIN_PLAYER_HISTORY 60.2%, STALE_KALSHI_QUOTE 53.8%, STALE_PLAYER_DATA 47.1%, MODEL_INTERNAL_DISAGREEMENT 40.5%, ASYMMETRIC_SAMPLE_SIZE 33.5%, WIDE_SPREAD 23.2%, MODEL_HIGH_UNCERTAINTY 18.1%, PLAYER_IDENTITY_RISK 17.4%, EVENT_MAPPING_RISK 9.6%, LOW_DISPLAYED_LIQUIDITY 8.0%, LEVEL_TRANSFER_RISK 7.3%, MODEL_CALIBRATION_OUTLIER 4.4%, EXTERNAL_MARKET_REJECTION 1.0%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 39.3%, POST_SETTLEMENT_OBSERVATION 36.6%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 6260, "IDENTITY_AMBIGUOUS": 1562}; ticker orientation: {"VERIFIED": 7822}.

Checks: discipline:AMBIGUOUS 524, discipline:PASS 7298, identity_confidence:AMBIGUOUS 1363, identity_confidence:PASS 6459, level_mapping:NA 536, level_mapping:PASS 7286, market_pair:AMBIGUOUS 283, market_pair:NA 196, market_pair:PASS 7343, model_complement:NA 163, model_complement:PASS 7659, namesake:PASS 7822, physical_match_id:NA 2919, physical_match_id:PASS 4903, player_ids:PASS 7822, same_pair_other_event:PASS 7822, ticker_orientation:PASS 7822

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,202 | 1.6% | 1.6% | 0.4% | {"market_freshness": 21, "execution": 8, "data": 5, "market_freshness/coverage": 1} | 5.24 | 0.2088 / 0.2109 (259) | 15.9% | 1.3% | 5.2% | 1.5% |
| CHALLENGER | 5,565 | 17.1% | 5.8% | 12.2% | {"coverage": 581, "market_freshness/coverage": 121, "market_freshness": 112, "data": 63, "model_calibration_or_unknown": 46, "execution": 13, "model_calibration": 9, "mapping": 6} | 7.12 | 0.2173 / 0.2045 (1461) | 37.2% | 9.4% | 2.4% | 22.9% |
| DOUBLES | 1,073 | 48.8% | 48.3% | 6.7% | {"execution": 215, "mapping": 156, "market_freshness": 106, "market_freshness/coverage": 40, "coverage": 7} | 24.07 | 0.3264 / 0.2327 (326) | 21.8% | 0.0% | 100.0% | 8.0% |
| ITF_MEN | 10,522 | 24.6% | 16.9% | 33.1% | {"coverage": 1010, "execution": 525, "market_freshness": 406, "data": 351, "market_freshness/coverage": 205, "mapping": 92, "model_calibration_or_unknown": 2} | 11.12 | 0.2134 / 0.1946 (2574) | 36.4% | 61.1% | 12.3% | 22.8% |
| ITF_WOMEN | 13,018 | 26.3% | 19.0% | 43.8% | {"coverage": 1248, "market_freshness": 706, "execution": 565, "data": 515, "market_freshness/coverage": 263, "mapping": 79, "model_calibration_or_unknown": 43, "model_calibration": 10} | 12.56 | 0.2019 / 0.1916 (2722) | 39.1% | 56.9% | 10.0% | 22.5% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,832 | 5.9% | 5.3% | 1.4% | {"market_freshness": 36, "model_calibration_or_unknown": 23, "execution": 15, "data": 11, "market_freshness/coverage": 10, "model_calibration": 9, "coverage": 4, "mapping": 1} | 7.4 | 0.2402 / 0.2328 (293) | 24.2% | 1.9% | 2.0% | 2.9% |
| WTA125 | 1,353 | 12.6% | 9.9% | 2.2% | {"market_freshness/coverage": 38, "model_calibration_or_unknown": 37, "market_freshness": 37, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.17 | 0.2167 / 0.2061 (470) | 23.0% | 7.5% | 4.7% | 9.9% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 5 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 6 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 7 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 207 min (STALE); no external reference |
| 9 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 10 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 11 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 12 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 13 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 14 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 15 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 16 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 17 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 18 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 19 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 20 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 22 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 23 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 24 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 25 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 26 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 27 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 92 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 28 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 29 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 30 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 31 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 32 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 162 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 33 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 34 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 35 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 36 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 37 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 33 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 38 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 39 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFWMATCH-26OCT16ESTLAB-LAB` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 68 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1475.0, ratio 2.28); no external reference |
| 41 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 42 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 43 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 44 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.8h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 359 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 45 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 46 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 47 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 48 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 49 | `KXATPCHALLENGERMATCH-26OCT13GIUSEA-SEA` | CHALLENGER | fair_v1 | 76% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 757 min (STALE); no external reference |
| 50 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 64 min (STALE); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9816, "by_level_share_of_ge_25pp": {"ATP": 0.0045, "CHALLENGER": 0.1216, "DOUBLES": 0.067, "ITF_MEN": 0.3312, "ITF_WOMEN": 0.4384, "OTHER": 0.0015, "WTA": 0.0139, "WTA125": 0.0219}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5385, "share_primary_cause_market_settled_or_in_play": 0.4528, "share_primary_cause_stale_quote_only": 0.1823}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 7822, "identity_ambiguous_share": 0.1997, "ticker_orientation": {"VERIFIED": 7822}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 4903, "with_external": 189, "coverage": 0.0385, "external_status": {"EXTERNAL_STALE": 131, "AGREES_WITH_KALSHI": 55, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 131, "MODEL_LONE_OUTLIER": 55, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.291, "share_external_supports_model": 0.0159}, "pregame_clean_ge_25pp": {"n": 2335, "with_external": 178, "coverage": 0.0762, "external_status": {"EXTERNAL_STALE": 122, "AGREES_WITH_KALSHI": 53, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 122, "MODEL_LONE_OUTLIER": 53, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.2978, "share_external_supports_model": 0.0169}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 562.0, "median_sample_ratio": 2.36, "median_min_matches": 20.0, "median_max_days_since_last": 204.0, "share_severe_asymmetry": 0.2028, "data_status": {"POOR": 4175, "LIMITED": 2221, "ADEQUATE": 1426}, "comparison_lt_10pp": {"median_thinner_serve_points": 1798.0, "median_sample_ratio": 1.68, "median_min_matches": 90.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 624, "model_minus_observed": 0.0532, "kalshi_minus_observed": -0.0796, "brier_diff_model_minus_kalshi": 0.0002}, "4-10x": {"n": 415, "model_minus_observed": 0.0747, "kalshi_minus_observed": -0.063, "brier_diff_model_minus_kalshi": 0.0078}, "<2x": {"n": 1529, "model_minus_observed": 0.0825, "kalshi_minus_observed": -0.0395, "brier_diff_model_minus_kalshi": 0.0112}, ">=10x": {"n": 505, "model_minus_observed": 0.1261, "kalshi_minus_observed": -0.0408, "brier_diff_model_minus_kalshi": 0.0158}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3073, "model": {"intercept": -0.541, "slope": 0.859, "slope_se": 0.046}, "kalshi_mid_same_rows": {"intercept": 0.232, "slope": 1.124, "slope_se": 0.052}, "mean_extremity_model": 0.1755, "mean_extremity_kalshi": 0.1716, "model_brier": 0.2295, "kalshi_brier": 0.2021, "brier_diff_model_minus_kalshi": 0.0274, "brier_diff_se": 0.0034, "model_logloss": 0.6549, "kalshi_logloss": 0.5862}, "fair_v1": {"n": 3073, "model": {"intercept": -0.403, "slope": 1.062, "slope_se": 0.051}, "kalshi_mid_same_rows": {"intercept": 0.31, "slope": 1.166, "slope_se": 0.053}, "mean_extremity_model": 0.1681, "mean_extremity_kalshi": 0.1716, "model_brier": 0.2114, "kalshi_brier": 0.2021, "brier_diff_model_minus_kalshi": 0.0092, "brier_diff_se": 0.0027, "model_logloss": 0.6101, "kalshi_logloss": 0.5861}, "gen1_elo": {"n": 3073, "model": {"intercept": -0.399, "slope": 1.045, "slope_se": 0.05}, "kalshi_mid_same_rows": {"intercept": 0.298, "slope": 1.15, "slope_se": 0.052}, "mean_extremity_model": 0.1733, "mean_extremity_kalshi": 0.172, "model_brier": 0.2106, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0086, "brier_diff_se": 0.0027, "model_logloss": 0.6092, "kalshi_logloss": 0.5858}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2455, "share_ge_15": 0.4377, "median_abs_gap": 12.99, "n": 19971}, "gen1_elo": {"share_ge_25": 0.2393, "share_ge_15": 0.4307, "median_abs_gap": 12.47, "n": 19971}, "gen1_sr": {"share_ge_25": 0.3075, "share_ge_15": 0.523, "median_abs_gap": 15.88, "n": 19971}, "gen2": {"share_ge_25": 0.3087, "share_ge_15": 0.5088, "median_abs_gap": 15.43, "n": 19971}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1515, "share_ge_15": 0.3497, "median_abs_gap": 10.64, "n": 15413}, "gen1_elo": {"share_ge_25": 0.1488, "share_ge_15": 0.3387, "median_abs_gap": 10.08, "n": 15412}, "gen1_sr": {"share_ge_25": 0.2144, "share_ge_15": 0.4444, "median_abs_gap": 13.23, "n": 15413}, "gen2": {"share_ge_25": 0.2276, "share_ge_15": 0.4409, "median_abs_gap": 13.01, "n": 15414}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.24, "share_ge_25_all": 0.0159, "share_ge_25_pregame_clean": 0.0157}, "WTA": {"median_abs_gap_pregame_clean": 7.4, "share_ge_25_all": 0.0595, "share_ge_25_pregame_clean": 0.0534}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2402, "share_within_10pp_all": 0.4402, "share_within_10pp_pregame_clean": 0.498, "corr_model_vs_mid_pregame_clean": 0.8435}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 478, "model_brier": 0.1924, "kalshi_brier": 0.1939, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 545, "model_brier": 0.213, "kalshi_brier": 0.205, "brier_diff_model_minus_kalshi": 0.0081}, "15-25": {"n_settled": 672, "model_brier": 0.2304, "kalshi_brier": 0.2153, "brier_diff_model_minus_kalshi": 0.0151}, "25-40": {"n_settled": 364, "model_brier": 0.2241, "kalshi_brier": 0.208, "brier_diff_model_minus_kalshi": 0.0161}, "3-5": {"n_settled": 295, "model_brier": 0.1905, "kalshi_brier": 0.1909, "brier_diff_model_minus_kalshi": -0.0004}, "40+": {"n_settled": 74, "model_brier": 0.2888, "kalshi_brier": 0.1769, "brier_diff_model_minus_kalshi": 0.1119}, "5-10": {"n_settled": 645, "model_brier": 0.1976, "kalshi_brier": 0.1969, "brier_diff_model_minus_kalshi": 0.0007}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.541, "slope": 0.859, "slope_se": 0.046}, "kalshi_slope": {"intercept": 0.232, "slope": 1.124, "slope_se": 0.052}, "n": 3073}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.515, "slope": 0.875, "slope_se": 0.035}, "kalshi_slope": {"intercept": 0.143, "slope": 1.077, "slope_se": 0.039}, "n": 5074}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 326, "model_brier": 0.3264, "kalshi_brier": 0.2327, "brier_diff_model_minus_kalshi": 0.0937, "brier_diff_se": 0.0174, "corr_model_outcome": 0.0139, "corr_kalshi_outcome": 0.2622}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
