# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-13T12:58Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 91,721): 0-3 13.9%, 3-5 9.5%, 5-10 20.1%, 10-15 15.2%, 15-25 19.2%, 25-40 13.8%, 40+ 8.3%; median gap 11.94 pp.
* **Where the extremes live**: 97.4% of >=25 pp gaps are off the ATP/WTA main tour (ITF 78.4%, Challenger 11.0%, doubles 6.4%). Main tour: ATP 3.7% and WTA 5.9% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 20,274): MARKET_ALREADY_SETTLED_WHEN_PRICED 35.4%, STALE_QUOTE 20.1%, BOOK_QUALITY 16.2%, POOR_DATA 9.0%, POSSIBLY_IN_PLAY_QUOTE 5.9%, IDENTITY_AMBIGUOUS 4.2%, IN_PLAY_QUOTE 3.4%, LIMITED_DATA 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 1.7%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 35.4%, market_freshness 20.1%, execution 16.2%, data 12.3%, market_freshness/coverage 9.3%, mapping 4.2%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 55.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 44.7% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 20,274 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.8%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 27.0% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 484.0 points vs 1670.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.02, Gen-2 0.817, Gen-1 ledger 0.865 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 1039 model 0.2253 vs Kalshi 0.2033; n 214 model 0.307 vs Kalshi 0.1666.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 380,142 model-market comparisons (629,813 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 125,047 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-13T12:36:58.060100+00:00'], shadow board 106,280 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-13T12:37:01.693049+00:00'], Model 4 44,246 rows, 31,573 settled tickers, 11,916 tickers with an external scan.
* By model: {"gen1_ledger": 83518, "gen1_elo": 53406, "fair_v1": 53406, "gen2": 53406, "gen1_sr": 53406, "model4_fundamental": 41542, "model4_conditioned": 41458}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 91,721 | 13.9 | 9.5 | 20.1 | 15.2 | 19.2 | 13.8 | 8.3 | 11.94 | 41.3% | 22.1% |
| MW fair_v1 | 53,406 | 12.5 | 8.6 | 18.7 | 15.2 | 19.6 | 15.0 | 10.4 | 13.22 | 45.0% | 25.4% |
| MW gen1_elo | 53,406 | 12.3 | 8.7 | 19.1 | 15.3 | 19.4 | 15.0 | 10.2 | 13.01 | 44.6% | 25.2% |
| MW gen1_ledger | 38,315 | 15.8 | 10.8 | 22.2 | 15.2 | 18.6 | 12.0 | 5.5 | 10.29 | 36.1% | 17.5% |
| MW gen1_sr | 53,406 | 9.9 | 7.1 | 16.5 | 13.9 | 20.9 | 18.8 | 12.8 | 16.01 | 52.5% | 31.7% |
| MW gen2 | 53,406 | 10.8 | 7.5 | 16.6 | 13.7 | 19.7 | 17.7 | 13.9 | 15.55 | 51.4% | 31.7% |
| all families model4_conditioned | 41,458 | 22.2 | 17.9 | 34.6 | 16.9 | 4.9 | 2.2 | 1.2 | 6.06 | 8.4% | 3.4% |
| all families model4_fundamental | 41,542 | 17.3 | 13.5 | 34.0 | 19.9 | 9.9 | 3.8 | 1.5 | 7.6 | 15.2% | 5.3% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.5%, >=15pp 41.3%, >=20pp 30.5%, >=25pp 22.1%, >=30pp 16.0%, >=40pp 8.3%, >=50pp 3.9%
Executable gap (model outside the book, before fees): median 8.6pp; >=10pp 45.7%, >=25pp 17.6%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,128 | 27.9 | 16.0 | 28.0 | 13.2 | 10.7 | 3.5 | 0.6 | 5.77 | 14.9% | 4.1% |
| CHALLENGER | 8,378 | 16.3 | 9.6 | 20.6 | 15.2 | 15.7 | 11.3 | 11.2 | 10.93 | 38.2% | 22.5% |
| ITF_MEN | 15,784 | 9.6 | 7.3 | 17.1 | 14.9 | 21.1 | 17.2 | 12.8 | 15.45 | 51.1% | 30.0% |
| ITF_WOMEN | 20,675 | 9.3 | 7.0 | 16.1 | 14.6 | 22.2 | 18.7 | 12.1 | 16.04 | 52.9% | 30.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,108 | 16.6 | 13.3 | 24.9 | 20.7 | 16.8 | 6.7 | 1.1 | 8.65 | 24.6% | 7.8% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,128 | 26.3 | 15.7 | 26.3 | 15.8 | 11.3 | 3.9 | 0.8 | 6.1 | 16.0% | 4.7% |
| CHALLENGER | 8,378 | 14.4 | 9.1 | 19.0 | 13.8 | 18.4 | 13.6 | 11.6 | 12.54 | 43.7% | 25.3% |
| ITF_MEN | 15,784 | 8.2 | 6.2 | 15.2 | 13.8 | 20.4 | 19.9 | 16.3 | 17.84 | 56.6% | 36.2% |
| ITF_WOMEN | 20,675 | 7.8 | 5.8 | 14.1 | 12.6 | 20.7 | 21.2 | 17.8 | 19.2 | 59.6% | 39.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,108 | 14.1 | 10.3 | 21.6 | 16.2 | 22.5 | 12.8 | 2.5 | 11.25 | 37.8% | 15.3% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,128 | 23.4 | 14.1 | 25.6 | 15.5 | 14.3 | 5.9 | 1.1 | 7.03 | 21.3% | 7.0% |
| CHALLENGER | 8,378 | 15.1 | 9.6 | 20.8 | 15.6 | 16.0 | 11.9 | 11.0 | 11.16 | 38.9% | 22.9% |
| ITF_MEN | 15,784 | 9.3 | 7.3 | 17.2 | 14.3 | 21.4 | 17.3 | 13.2 | 15.73 | 51.8% | 30.4% |
| ITF_WOMEN | 20,675 | 9.2 | 6.8 | 16.2 | 15.6 | 22.1 | 18.7 | 11.4 | 15.82 | 52.2% | 30.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,108 | 22.4 | 17.2 | 31.8 | 15.2 | 9.0 | 3.3 | 1.0 | 6.12 | 13.3% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,497 | 28.1 | 19.6 | 29.1 | 12.1 | 8.1 | 2.5 | 0.4 | 5.24 | 11.1% | 3.0% |
| CHALLENGER | 5,077 | 23.1 | 14.6 | 27.7 | 14.7 | 12.9 | 5.4 | 1.5 | 6.99 | 19.9% | 6.9% |
| DOUBLES | 2,819 | 4.8 | 4.5 | 12.8 | 11.0 | 20.5 | 24.8 | 21.5 | 23.23 | 66.9% | 46.3% |
| ITF_MEN | 11,394 | 12.8 | 9.5 | 21.5 | 15.7 | 21.6 | 12.9 | 6.0 | 11.77 | 40.5% | 18.9% |
| ITF_WOMEN | 13,292 | 13.4 | 9.3 | 19.9 | 15.8 | 21.7 | 14.6 | 5.4 | 12.17 | 41.6% | 19.9% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,831 | 23.9 | 15.9 | 31.8 | 16.8 | 8.8 | 2.5 | 0.2 | 6.57 | 11.6% | 2.7% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,999 | 28.4 | 16.2 | 28.4 | 13.2 | 10.5 | 3.1 | 0.3 | 5.64 | 13.9% | 3.4% |
| CHALLENGER | 5,885 | 21.1 | 12.1 | 25.7 | 18.0 | 15.8 | 5.6 | 1.8 | 8.2 | 23.1% | 7.4% |
| ITF_MEN | 11,421 | 11.8 | 8.8 | 20.6 | 17.2 | 22.1 | 14.0 | 5.5 | 12.44 | 41.6% | 19.4% |
| ITF_WOMEN | 15,001 | 11.3 | 8.6 | 19.1 | 17.0 | 24.1 | 15.3 | 4.5 | 13.13 | 44.0% | 19.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,994 | 16.9 | 13.3 | 25.2 | 21.1 | 16.8 | 6.2 | 0.6 | 8.47 | 23.5% | 6.8% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,999 | 26.6 | 16.1 | 26.6 | 15.7 | 11.2 | 3.4 | 0.4 | 6.02 | 15.0% | 3.8% |
| CHALLENGER | 5,885 | 18.1 | 11.7 | 23.9 | 16.3 | 19.1 | 8.9 | 2.1 | 8.99 | 30.0% | 11.0% |
| ITF_MEN | 11,423 | 9.7 | 7.4 | 17.8 | 16.0 | 22.3 | 17.9 | 9.0 | 14.69 | 49.2% | 26.9% |
| ITF_WOMEN | 15,003 | 8.9 | 7.0 | 16.1 | 14.2 | 22.6 | 20.6 | 10.6 | 16.51 | 53.8% | 31.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,994 | 14.3 | 10.4 | 21.8 | 16.4 | 22.7 | 12.5 | 1.9 | 11.03 | 37.0% | 14.4% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,427 | 28.4 | 19.8 | 29.1 | 12.3 | 7.8 | 2.3 | 0.3 | 5.17 | 10.4% | 2.6% |
| CHALLENGER | 4,495 | 24.4 | 15.5 | 28.8 | 14.9 | 12.2 | 3.7 | 0.4 | 6.5 | 16.4% | 4.1% |
| DOUBLES | 2,638 | 4.7 | 4.5 | 13.1 | 11.0 | 20.4 | 24.7 | 21.7 | 23.2 | 66.7% | 46.4% |
| ITF_MEN | 9,843 | 13.6 | 10.0 | 22.9 | 16.3 | 21.6 | 11.4 | 4.1 | 10.9 | 37.2% | 15.5% |
| ITF_WOMEN | 11,442 | 14.1 | 9.8 | 20.9 | 16.3 | 21.8 | 13.4 | 3.6 | 11.39 | 38.8% | 17.0% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,768 | 24.2 | 16.3 | 31.8 | 16.8 | 8.8 | 2.0 | 0.1 | 6.43 | 10.9% | 2.0% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,819 | 4.8 | 4.5 | 12.8 | 11.0 | 20.5 | 24.8 | 21.5 | 23.23 | 66.9% | 46.3% |
| singles | 35,496 | 16.6 | 11.3 | 22.9 | 15.5 | 18.4 | 10.9 | 4.3 | 9.76 | 33.6% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 11,617 | 12.7 | 9.0 | 19.2 | 14.9 | 19.6 | 14.4 | 10.1 | 13.0 | 44.2% | 24.5% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 34,727 | 12.9 | 8.6 | 18.8 | 15.1 | 19.2 | 15.1 | 10.3 | 13.04 | 44.6% | 25.4% |
| UNKNOWN | 6,649 | 10.4 | 7.5 | 17.1 | 16.5 | 21.5 | 15.8 | 11.1 | 14.32 | 48.4% | 26.9% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 14,815 | 19.0 | 11.8 | 22.4 | 15.8 | 14.9 | 9.5 | 6.6 | 9.04 | 31.0% | 16.1% |
| B | 6,348 | 12.9 | 8.5 | 19.5 | 15.2 | 19.7 | 12.4 | 11.6 | 12.83 | 43.8% | 24.0% |
| C | 7,618 | 11.9 | 8.5 | 19.3 | 15.9 | 19.3 | 14.7 | 10.4 | 13.03 | 44.3% | 25.1% |
| D | 8,836 | 11.2 | 8.4 | 17.8 | 15.2 | 21.7 | 15.7 | 10.0 | 14.08 | 47.4% | 25.7% |
| F | 15,789 | 7.3 | 5.7 | 15.0 | 14.2 | 23.0 | 21.1 | 13.7 | 18.05 | 57.7% | 34.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 10,046 | 25.0 | 15.9 | 29.0 | 14.9 | 10.5 | 3.4 | 1.2 | 6.35 | 15.2% | 4.7% |
| B | 5,215 | 16.7 | 11.0 | 24.1 | 17.1 | 18.8 | 9.4 | 2.9 | 9.6 | 31.2% | 12.3% |
| C | 7,575 | 11.0 | 7.8 | 19.5 | 15.0 | 20.9 | 15.7 | 10.1 | 13.49 | 46.7% | 25.7% |
| D | 5,861 | 14.4 | 10.0 | 21.0 | 15.4 | 21.1 | 12.8 | 5.3 | 11.39 | 39.2% | 18.1% |
| F | 9,618 | 10.2 | 8.4 | 16.7 | 14.4 | 23.4 | 18.8 | 7.9 | 15.08 | 50.2% | 26.8% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 16,786 | 17.5 | 10.9 | 21.3 | 15.5 | 15.2 | 10.2 | 9.3 | 10.03 | 34.8% | 19.6% |
| LIMITED | 11,597 | 13.4 | 9.4 | 20.4 | 15.9 | 19.9 | 13.4 | 7.6 | 11.99 | 40.9% | 21.0% |
| POOR | 25,023 | 8.8 | 6.7 | 16.1 | 14.6 | 22.4 | 19.0 | 12.4 | 16.36 | 53.8% | 31.4% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,338 | 23.8 | 18.0 | 33.0 | 15.4 | 6.4 | 3.0 | 0.4 | 5.89 | 9.8% | 3.4% |
| GAME_SPREAD | 6,975 | 22.8 | 15.3 | 32.0 | 16.8 | 9.1 | 3.3 | 0.7 | 6.69 | 13.0% | 3.9% |
| MATCH_WINNER | 38,315 | 15.8 | 10.8 | 22.2 | 15.2 | 18.6 | 12.0 | 5.5 | 10.29 | 36.1% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 17,175 | 28.4 | 16.8 | 30.7 | 12.7 | 8.8 | 2.3 | 0.3 | 5.57 | 11.4% | 2.6% |
| TOTAL_GAMES | 11,691 | 9.7 | 10.8 | 36.4 | 25.6 | 10.4 | 4.2 | 2.9 | 9.13 | 17.4% | 7.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,742 | 24.5 | 28.8 | 33.3 | 8.1 | 3.9 | 1.2 | 0.3 | 4.79 | 5.4% | 1.5% |
| GAME_SPREAD | 9,591 | 46.7 | 15.8 | 25.2 | 7.4 | 2.4 | 1.9 | 0.6 | 3.33 | 4.9% | 2.5% |
| TOTAL_GAMES | 17,125 | 6.5 | 9.8 | 41.0 | 29.8 | 7.2 | 3.3 | 2.3 | 9.14 | 12.9% | 5.6% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,778 | 23.8 | 16.6 | 34.7 | 14.7 | 6.9 | 2.7 | 0.5 | 6.05 | 10.1% | 3.2% |
| GAME_SPREAD | 9,600 | 20.3 | 13.4 | 28.5 | 20.2 | 12.2 | 4.3 | 1.1 | 7.71 | 17.6% | 5.5% |
| TOTAL_GAMES | 17,164 | 10.0 | 10.9 | 36.5 | 24.3 | 11.3 | 4.4 | 2.6 | 9.01 | 18.3% | 7.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 53,406 | 45.0% | 25.4% | 13.22 | 35.5% | 15.1% | 10.71 |
| gen1_elo | 53,406 | 44.6% | 25.2% | 13.01 | 34.9% | 15.0% | 10.51 |
| gen1_sr | 53,406 | 52.5% | 31.7% | 16.01 | 44.0% | 21.4% | 12.99 |
| gen2 | 53,406 | 51.4% | 31.7% | 15.55 | 43.9% | 23.0% | 12.84 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,471 | 15.4 | 10.5 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.72 | 35.4% | 15.3% |
| STALE | 32,935 | 10.7 | 7.4 | 17.0 | 13.9 | 19.3 | 17.0 | 14.7 | 15.4 | 51.0% | 31.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 31,783 | 16.3 | 11.1 | 22.7 | 15.2 | 18.2 | 11.5 | 5.0 | 9.97 | 34.7% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 91,721 | 31783 | 23943 | 35995 | 25.3 | 149.5 | 1451.1 |
| ge_15pp | 37,868 | 11020 | 8544 | 18304 | 29.1 | 452.9 | 1451.1 |
| ge_25pp | 20,274 | 5238 | 3732 | 11304 | 35.0 | 594.3 | 1431.1 |
| lt_10pp | 39,933 | 15916 | 11312 | 12705 | 22.8 | 49.7 | 1421.7 |

Current slate `SL-20261113T125846Z-71c52a06`: 210 priced rows, quote age at build {'median': 54.7, 'max': 54.7}, freshness {'STALE': 210}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 52 | 0.0 | 0.0 | 34.6 | 9.6 | 32.7 | 19.2 | 3.9 | 18.34 | 55.8% | 23.1% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 5,108 | 19.2 | 11.1 | 25.6 | 18.3 | 17.7 | 7.1 | 1.0 | 8.77 | 25.8% | 8.1% |
| KALSHI_LONE_OUTLIER | 32 | 6.2 | 6.2 | 75.0 | 6.2 | 3.1 | 3.1 | 0.0 | 6.16 | 6.2% | 3.1% |
| MARKETS_AGREE | 1,092 | 66.1 | 33.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,332 | 0.0 | 2.1 | 38.4 | 26.0 | 23.8 | 8.7 | 0.9 | 11.66 | 33.5% | 9.6% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 53,406 | 8645 (16.2%) | 27.0% | 0.9% | {"EXTERNAL_STALE": 5108, "AGREES_WITH_KALSHI": 2332, "ALL_AGREE": 1092, "SUPPORTS_MODEL_DIRECTION": 50, "AGREES_WITH_MODEL": 32, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 24,049 | 2127 (8.8%) | 36.7% | 1.5% | {"EXTERNAL_STALE": 1316, "AGREES_WITH_KALSHI": 780, "SUPPORTS_MODEL_DIRECTION": 29, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 13,574 | 648 (4.8%) | 34.6% | 2.0% | {"EXTERNAL_STALE": 411, "AGREES_WITH_KALSHI": 224, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 6,146 | 616 (10.0%) | 35.2% | 2.1% | {"EXTERNAL_STALE": 386, "AGREES_WITH_KALSHI": 217, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 21,248 | 4971 (23.4%) | 19.0% | 0.9% | {"EXTERNAL_STALE": 2858, "ALL_AGREE": 1092, "AGREES_WITH_KALSHI": 946, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 28, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 10,477 | 10.6 | 7.7 | 18.9 | 14.3 | 21.8 | 16.4 | 10.3 | 14.39 | 48.5% | 26.7% |
| 4-10x | 7,231 | 10.9 | 8.7 | 18.1 | 14.8 | 21.5 | 14.7 | 11.3 | 14.1 | 47.5% | 26.0% |
| <2x | 27,142 | 14.5 | 9.6 | 19.9 | 15.9 | 17.6 | 13.4 | 9.2 | 11.72 | 40.2% | 22.6% |
| >=10x | 8,556 | 10.2 | 6.4 | 15.2 | 14.2 | 21.8 | 18.9 | 13.3 | 16.52 | 54.0% | 32.2% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 14,065 | 12.3 | 8.6 | 19.6 | 16.0 | 19.2 | 13.7 | 10.5 | 12.85 | 43.4% | 24.2% |
| 300-1000 | 11,641 | 11.5 | 8.7 | 17.8 | 15.1 | 20.6 | 16.4 | 10.0 | 13.94 | 47.0% | 26.5% |
| <300 | 16,927 | 8.1 | 5.9 | 15.1 | 14.4 | 22.8 | 20.0 | 13.6 | 17.47 | 56.5% | 33.7% |
| >=3000 | 10,773 | 20.9 | 12.8 | 24.0 | 15.4 | 14.1 | 7.4 | 5.5 | 7.92 | 27.0% | 12.9% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1659 | 0.5471 | 0.408 | 0.4768 | +0.070 | -0.069 | 0.0036 ± 0.0038 |
| ratio 4-10x | 1134 | 0.5716 | 0.4273 | 0.485 | +0.087 | -0.058 | 0.0101 ± 0.0048 |
| ratio <2x | 4044 | 0.5345 | 0.4115 | 0.4305 | +0.104 | -0.019 | 0.0151 ± 0.0022 |
| ratio >=10x | 1397 | 0.5581 | 0.3866 | 0.4309 | +0.127 | -0.044 | 0.0183 ± 0.0047 |
| thinner_sample 1000-3000 | 2271 | 0.54 | 0.4128 | 0.4417 | +0.098 | -0.029 | 0.0131 ± 0.003 |
| thinner_sample 300-1000 | 1879 | 0.5591 | 0.4188 | 0.4683 | +0.091 | -0.050 | 0.0064 ± 0.0036 |
| thinner_sample <300 | 2690 | 0.552 | 0.3854 | 0.4401 | +0.112 | -0.055 | 0.0159 ± 0.0034 |
| thinner_sample >=3000 | 1394 | 0.5274 | 0.4337 | 0.4426 | +0.085 | -0.009 | 0.0141 ± 0.0031 |
| data_status ADEQUATE | 2219 | 0.5316 | 0.429 | 0.4385 | +0.093 | -0.009 | 0.0151 ± 0.0026 |
| data_status LIMITED | 2010 | 0.5464 | 0.4135 | 0.4607 | +0.086 | -0.047 | 0.0077 ± 0.0034 |
| data_status POOR | 4005 | 0.5541 | 0.3952 | 0.4457 | +0.108 | -0.051 | 0.0138 ± 0.0027 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1181 | 0.1968 | 0.1968 | +0.0000 ± 0.0004 | 0.5732 | 0.5733 | 0.5021 | 0.4869 | 0.4911 | -0.100 ± 0.0137 | -0.0087 (8) |
| 3-5 | 765 | 0.209 | 0.2084 | +0.0006 ± 0.0013 | 0.604 | 0.6011 | 0.5025 | 0.4627 | 0.4745 | -0.099 ± 0.0169 | 0.01 (3) |
| 5-10 | 1777 | 0.2023 | 0.2005 | +0.0017 ± 0.0016 | 0.5909 | 0.5845 | 0.5087 | 0.4348 | 0.4586 | -0.090 ± 0.011 | -0.0143 (7) |
| 10-15 | 1431 | 0.22 | 0.2104 | +0.0096 ± 0.003 | 0.6325 | 0.6045 | 0.5242 | 0.4008 | 0.4228 | -0.103 ± 0.0123 | -0.055 (6) |
| 15-25 | 1827 | 0.2254 | 0.2069 | +0.0185 ± 0.0041 | 0.6458 | 0.597 | 0.5706 | 0.3761 | 0.4253 | -0.099 ± 0.0107 | -0.0045 (11) |
| 25-40 | 1039 | 0.2253 | 0.2033 | +0.0220 ± 0.0084 | 0.6409 | 0.5871 | 0.6428 | 0.3333 | 0.4514 | -0.066 ± 0.013 | -0.06 (2) |
| 40+ | 214 | 0.307 | 0.1666 | +0.1404 ± 0.0253 | 0.8206 | 0.5019 | 0.7244 | 0.2671 | 0.3505 | -0.089 ± 0.0244 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5972 | 0.1873 | 0.1881 | -0.0008 ± 0.0002 | 0.5511 | 0.5521 | 0.4915 | 0.4762 | 0.5054 | -0.023 ± 0.0057 | -0.01 (28) |
| 3-5 | 4057 | 0.1991 | 0.1972 | +0.0019 ± 0.0006 | 0.5792 | 0.5727 | 0.4814 | 0.4416 | 0.437 | -0.058 ± 0.007 | 0.005 (6) |
| 5-10 | 8901 | 0.2007 | 0.1965 | +0.0042 ± 0.0007 | 0.5871 | 0.5735 | 0.4822 | 0.4084 | 0.4167 | -0.049 ± 0.0047 | -0.0114 (22) |
| 10-15 | 7244 | 0.2023 | 0.1863 | +0.0160 ± 0.0013 | 0.5917 | 0.5466 | 0.4845 | 0.3606 | 0.3584 | -0.063 ± 0.0051 | -0.0379 (19) |
| 15-25 | 9348 | 0.2062 | 0.167 | +0.0392 ± 0.0017 | 0.6042 | 0.4965 | 0.4978 | 0.3023 | 0.3006 | -0.067 ± 0.0042 | -0.0043 (51) |
| 25-40 | 7303 | 0.2226 | 0.1233 | +0.0992 ± 0.0026 | 0.6391 | 0.3807 | 0.5233 | 0.2093 | 0.2122 | -0.059 ± 0.004 | -0.0733 (3) |
| 40+ | 5029 | 0.3794 | 0.044 | +0.3353 ± 0.0033 | 0.9886 | 0.1707 | 0.6276 | 0.1019 | 0.0575 | -0.076 ± 0.0028 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 945 | 0.2023 | 0.2026 | -0.0003 ± 0.0005 | 0.5849 | 0.5858 | 0.5091 | 0.494 | 0.5175 | -0.096 ± 0.0156 | -0.0117 (6) |
| 3-5 | 688 | 0.2125 | 0.2097 | +0.0028 ± 0.0014 | 0.6087 | 0.6025 | 0.5193 | 0.4797 | 0.4622 | -0.123 ± 0.0187 | 0.01 (3) |
| 5-10 | 1535 | 0.2049 | 0.2032 | +0.0017 ± 0.0017 | 0.5954 | 0.5911 | 0.5379 | 0.4635 | 0.4906 | -0.084 ± 0.0119 | -0.01 (4) |
| 10-15 | 1329 | 0.2151 | 0.2073 | +0.0078 ± 0.0031 | 0.6228 | 0.6002 | 0.5576 | 0.4331 | 0.4665 | -0.102 ± 0.013 | -0.04 (5) |
| 15-25 | 1919 | 0.2332 | 0.2117 | +0.0215 ± 0.0041 | 0.6642 | 0.6075 | 0.5839 | 0.3882 | 0.433 | -0.099 ± 0.0107 | -0.0183 (12) |
| 25-40 | 1332 | 0.2661 | 0.2002 | +0.0660 ± 0.0077 | 0.7422 | 0.5809 | 0.658 | 0.3443 | 0.3979 | -0.108 ± 0.0123 | -0.008 (5) |
| 40+ | 486 | 0.3749 | 0.1598 | +0.2151 ± 0.0182 | 1.0178 | 0.4849 | 0.7318 | 0.2426 | 0.2798 | -0.088 ± 0.0175 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5126 | 0.1906 | 0.1909 | -0.0002 ± 0.0002 | 0.5566 | 0.5569 | 0.5066 | 0.4914 | 0.5066 | -0.039 ± 0.0063 | -0.0154 (26) |
| 3-5 | 3558 | 0.1943 | 0.1935 | +0.0009 ± 0.0006 | 0.5661 | 0.5635 | 0.5114 | 0.4718 | 0.4795 | -0.043 ± 0.0076 | 0.01 (5) |
| 5-10 | 7956 | 0.1958 | 0.1925 | +0.0033 ± 0.0007 | 0.5759 | 0.5634 | 0.5066 | 0.4324 | 0.4495 | -0.038 ± 0.005 | -0.0117 (6) |
| 10-15 | 6569 | 0.2021 | 0.1899 | +0.0122 ± 0.0013 | 0.5935 | 0.5561 | 0.5066 | 0.3827 | 0.3964 | -0.050 ± 0.0055 | -0.0189 (18) |
| 15-25 | 9430 | 0.216 | 0.1795 | +0.0365 ± 0.0017 | 0.6295 | 0.5272 | 0.5235 | 0.328 | 0.335 | -0.059 ± 0.0044 | -0.014 (52) |
| 25-40 | 8472 | 0.2499 | 0.1378 | +0.1121 ± 0.0026 | 0.7059 | 0.4203 | 0.5591 | 0.2418 | 0.2273 | -0.076 ± 0.004 | -0.0095 (20) |
| 40+ | 6743 | 0.4016 | 0.0595 | +0.3421 ± 0.0034 | 1.058 | 0.2138 | 0.6545 | 0.1191 | 0.0807 | -0.073 ± 0.0029 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1160 | 0.1964 | 0.1976 | -0.0011 ± 0.0005 | 0.5727 | 0.5753 | 0.5009 | 0.4855 | 0.5224 | -0.060 ± 0.0136 | -0.0191 (11) |
| 3-5 | 834 | 0.209 | 0.2076 | +0.0014 ± 0.0013 | 0.6049 | 0.6004 | 0.496 | 0.4565 | 0.4604 | -0.106 ± 0.0165 | 0.002 (5) |
| 5-10 | 1779 | 0.2032 | 0.1991 | +0.0042 ± 0.0016 | 0.592 | 0.5804 | 0.5099 | 0.4361 | 0.4441 | -0.104 ± 0.0109 | -0.01 (10) |
| 10-15 | 1478 | 0.2123 | 0.203 | +0.0094 ± 0.0029 | 0.6155 | 0.5885 | 0.5368 | 0.4135 | 0.4391 | -0.102 ± 0.0118 | -0.0286 (7) |
| 15-25 | 1732 | 0.231 | 0.2118 | +0.0192 ± 0.0043 | 0.6592 | 0.6076 | 0.5797 | 0.3857 | 0.433 | -0.102 ± 0.0111 | -0.03 (1) |
| 25-40 | 1022 | 0.2174 | 0.2059 | +0.0115 ± 0.0084 | 0.6247 | 0.5927 | 0.6513 | 0.3417 | 0.4755 | -0.058 ± 0.0131 | -0.0267 (3) |
| 40+ | 229 | 0.3093 | 0.1804 | +0.1289 ± 0.0253 | 0.8338 | 0.5323 | 0.7372 | 0.2806 | 0.3799 | -0.075 ± 0.0258 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5809 | 0.1868 | 0.1873 | -0.0005 ± 0.0002 | 0.5496 | 0.55 | 0.487 | 0.4716 | 0.4863 | -0.037 ± 0.0058 | -0.0189 (44) |
| 3-5 | 4168 | 0.2047 | 0.203 | +0.0017 ± 0.0006 | 0.5946 | 0.5889 | 0.4804 | 0.4409 | 0.4395 | -0.055 ± 0.0071 | -0.0073 (22) |
| 5-10 | 9013 | 0.1959 | 0.1906 | +0.0053 ± 0.0007 | 0.5753 | 0.5584 | 0.4848 | 0.4108 | 0.411 | -0.056 ± 0.0046 | -0.0117 (42) |
| 10-15 | 7267 | 0.1955 | 0.1801 | +0.0155 ± 0.0012 | 0.5766 | 0.5329 | 0.4951 | 0.3718 | 0.3707 | -0.062 ± 0.005 | -0.0136 (14) |
| 15-25 | 9358 | 0.2111 | 0.172 | +0.0392 ± 0.0017 | 0.6157 | 0.5073 | 0.5095 | 0.3148 | 0.3127 | -0.068 ± 0.0043 | -0.0533 (3) |
| 25-40 | 7293 | 0.2166 | 0.1233 | +0.0933 ± 0.0026 | 0.6262 | 0.3797 | 0.5251 | 0.2097 | 0.2212 | -0.052 ± 0.004 | -0.02 (4) |
| 40+ | 4946 | 0.3878 | 0.048 | +0.3398 ± 0.0035 | 1.011 | 0.1807 | 0.6364 | 0.1073 | 0.0635 | -0.076 ± 0.003 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1635 | 0.1964 | 0.196 | +0.0004 ± 0.0004 | 0.5709 | 0.5698 | 0.5064 | 0.4914 | 0.4869 | -0.076 ± 0.0112 | -0.0221 (56) |
| 3-5 | 1157 | 0.1893 | 0.1893 | -0.0000 ± 0.001 | 0.5567 | 0.5558 | 0.4984 | 0.4585 | 0.4771 | -0.054 ± 0.0131 | -0.0194 (34) |
| 5-10 | 2341 | 0.1991 | 0.194 | +0.0051 ± 0.0014 | 0.5873 | 0.5709 | 0.509 | 0.4354 | 0.4378 | -0.077 ± 0.0093 | -0.005 (78) |
| 10-15 | 1618 | 0.2155 | 0.2031 | +0.0124 ± 0.0028 | 0.6256 | 0.5898 | 0.5451 | 0.4223 | 0.432 | -0.088 ± 0.0115 | 0.0015 (67) |
| 15-25 | 2110 | 0.2322 | 0.2079 | +0.0244 ± 0.0039 | 0.6628 | 0.5995 | 0.5924 | 0.3974 | 0.4336 | -0.089 ± 0.01 | -0.0214 (59) |
| 25-40 | 1227 | 0.2416 | 0.2117 | +0.0299 ± 0.008 | 0.6894 | 0.6064 | 0.6882 | 0.3765 | 0.4849 | -0.081 ± 0.0124 | -0.0243 (28) |
| 40+ | 455 | 0.3293 | 0.1972 | +0.1321 ± 0.02 | 0.9397 | 0.5762 | 0.8074 | 0.3306 | 0.4462 | -0.092 ± 0.0187 | -0.1137 (8) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5895 | 0.1771 | 0.177 | +0.0001 ± 0.0002 | 0.5244 | 0.5238 | 0.5087 | 0.4934 | 0.4991 | -0.043 ± 0.0055 | -0.0154 (103) |
| 3-5 | 4053 | 0.1944 | 0.1935 | +0.0009 ± 0.0006 | 0.5674 | 0.5653 | 0.5016 | 0.4619 | 0.471 | -0.040 ± 0.007 | -0.0212 (73) |
| 5-10 | 8281 | 0.1971 | 0.1906 | +0.0065 ± 0.0007 | 0.5814 | 0.5619 | 0.5026 | 0.429 | 0.4228 | -0.061 ± 0.0049 | -0.0084 (134) |
| 10-15 | 5691 | 0.211 | 0.1948 | +0.0162 ± 0.0015 | 0.6142 | 0.5706 | 0.5382 | 0.4152 | 0.4096 | -0.070 ± 0.0059 | -0.0054 (112) |
| 15-25 | 6982 | 0.2317 | 0.1995 | +0.0323 ± 0.0021 | 0.6662 | 0.5782 | 0.577 | 0.3817 | 0.3972 | -0.067 ± 0.0054 | -0.024 (112) |
| 25-40 | 4490 | 0.2577 | 0.1905 | +0.0672 ± 0.0041 | 0.7283 | 0.5544 | 0.6406 | 0.3284 | 0.38 | -0.062 ± 0.0064 | -0.0267 (58) |
| 40+ | 2018 | 0.3703 | 0.1592 | +0.2112 ± 0.0091 | 1.0397 | 0.4746 | 0.7408 | 0.2413 | 0.2899 | -0.059 ± 0.0085 | -0.054 (15) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 8234 | 1.02 ± 0.031 | 1.081 | 0.1677 | 0.1711 | 0.216 | 0.2033 |
| gen2 | 8234 | 0.817 ± 0.028 | 1.059 | 0.174 | 0.1714 | 0.2334 | 0.2033 |
| gen1_elo | 8234 | 1.003 ± 0.03 | 1.073 | 0.1742 | 0.1713 | 0.215 | 0.2034 |
| gen1_sr | 8234 | 1.001 ± 0.036 | 1.107 | 0.1335 | 0.1729 | 0.2295 | 0.203 |
| gen1_ledger | 10543 | 0.865 ± 0.023 | 1.061 | 0.1904 | 0.1772 | 0.2173 | 0.2002 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 37,868)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 9,168 | 24.2% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 8,909 | 23.5% |
| BOOK_QUALITY | execution | 6,363 | 16.8% |
| POOR_DATA | data | 4,310 | 11.4% |
| LIMITED_DATA | data | 2,277 | 6.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 2,219 | 5.9% |
| IDENTITY_AMBIGUOUS | mapping | 1,551 | 4.1% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,427 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 1,061 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 582 | 1.5% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 24.2%, coverage 23.5%, data 17.4%, execution 16.8%, market_freshness/coverage 8.7%, mapping 4.1%, model_calibration_or_unknown 3.8%, model_calibration 1.5%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 95.1%, LOW_DATA_QUALITY 72.2%, THIN_PLAYER_HISTORY 60.2%, STALE_PLAYER_DATA 52.0%, STALE_KALSHI_QUOTE 48.3%, MODEL_INTERNAL_DISAGREEMENT 41.7%, ASYMMETRIC_SAMPLE_SIZE 33.2%, WIDE_SPREAD 23.3%, MODEL_HIGH_UNCERTAINTY 18.7%, PLAYER_IDENTITY_RISK 15.0%, LEVEL_TRANSFER_RISK 9.3%, LOW_DISPLAYED_LIQUIDITY 8.7%, EVENT_MAPPING_RISK 7.0%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.2%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.8%, POST_SETTLEMENT_OBSERVATION 23.5%, POSSIBLE_IN_PLAY_QUOTE 6.3%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 20,274)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,178 | 35.4% |
| STALE_QUOTE | market_freshness | 4,071 | 20.1% |
| BOOK_QUALITY | execution | 3,285 | 16.2% |
| POOR_DATA | data | 1,823 | 9.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,197 | 5.9% |
| IDENTITY_AMBIGUOUS | mapping | 859 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 698 | 3.4% |
| LIMITED_DATA | data | 675 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 347 | 1.7% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 140 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 35.4%, market_freshness 20.1%, execution 16.2%, data 12.3%, market_freshness/coverage 9.3%, mapping 4.2%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.2%, START_UNVERIFIABLE 97.4%, LOW_DATA_QUALITY 75.2%, THIN_PLAYER_HISTORY 62.3%, STALE_KALSHI_QUOTE 55.8%, STALE_PLAYER_DATA 45.3%, MODEL_INTERNAL_DISAGREEMENT 41.8%, ASYMMETRIC_SAMPLE_SIZE 34.4%, WIDE_SPREAD 22.4%, MODEL_HIGH_UNCERTAINTY 19.4%, PLAYER_IDENTITY_RISK 17.8%, LOW_DISPLAYED_LIQUIDITY 8.5%, EVENT_MAPPING_RISK 8.5%, LEVEL_TRANSFER_RISK 8.1%, MODEL_CALIBRATION_OUTLIER 4.6%, EXTERNAL_MARKET_REJECTION 1.7%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 38.3%, POST_SETTLEMENT_OBSERVATION 35.4%, POSSIBLE_IN_PLAY_QUOTE 6.4%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 16311, "IDENTITY_AMBIGUOUS": 3963}; ticker orientation: {"VERIFIED": 20274}.

Checks: discipline:AMBIGUOUS 1306, discipline:PASS 18968, identity_confidence:AMBIGUOUS 3610, identity_confidence:PASS 16664, level_mapping:NA 1318, level_mapping:PASS 18956, market_pair:AMBIGUOUS 518, market_pair:NA 429, market_pair:PASS 19327, model_complement:NA 391, model_complement:PASS 19883, namesake:AMBIGUOUS 6, namesake:PASS 20268, physical_match_id:NA 6700, physical_match_id:PASS 13574, player_ids:PASS 20274, same_pair_other_event:PASS 20274, ticker_orientation:PASS 20274

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,625 | 3.7% | 3.1% | 1.2% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 24, "market_freshness/coverage": 22} | 5.47 | 0.222 / 0.2181 (869) | 25.7% | 2.4% | 3.2% | 3.0% |
| CHALLENGER | 13,455 | 16.6% | 6.0% | 11.0% | {"coverage": 1373, "market_freshness": 275, "market_freshness/coverage": 243, "data": 164, "model_calibration_or_unknown": 81, "execution": 41, "model_calibration": 41, "mapping": 17, "possible_market_error": 1} | 7.32 | 0.2216 / 0.2112 (3130) | 41.8% | 13.6% | 4.0% | 22.9% |
| DOUBLES | 2,819 | 46.3% | 46.4% | 6.4% | {"execution": 723, "mapping": 394, "market_freshness": 106, "market_freshness/coverage": 76, "coverage": 7} | 23.2 | 0.2977 / 0.2314 (712) | 8.3% | 0.0% | 100.0% | 6.4% |
| ITF_MEN | 27,178 | 25.3% | 17.6% | 34.0% | {"coverage": 2434, "market_freshness": 1443, "execution": 1048, "data": 1017, "market_freshness/coverage": 700, "mapping": 232, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.73 | 0.2183 / 0.1979 (5779) | 42.4% | 69.8% | 14.3% | 21.8% |
| ITF_WOMEN | 33,967 | 26.5% | 18.6% | 44.4% | {"coverage": 3285, "market_freshness": 1986, "execution": 1390, "data": 1216, "market_freshness/coverage": 797, "mapping": 210, "model_calibration_or_unknown": 98, "model_calibration": 23} | 12.44 | 0.2035 / 0.1942 (6659) | 43.0% | 57.3% | 10.1% | 22.1% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,939 | 5.9% | 5.0% | 1.4% | {"market_freshness": 111, "model_calibration_or_unknown": 52, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.67 | 0.2311 / 0.2208 (816) | 30.3% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.5% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 404 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 519 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 21.5h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 1296 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFMATCH-26NOV12VALRAT-RAT` | ITF_MEN | gen1_ledger | 92% / 4% | +88 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 10 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1333.0, ratio 3.64); no external reference |
| 6 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 7 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 8 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 9 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 172 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 10 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 769 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 11 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 12 | `KXITFMATCH-26NOV10KOUPOR-POR` | ITF_MEN | fair_v1 | 87% / 2% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 80 min (STALE); data POOR (grade D, thinner serve sample 1554.0, ratio 1.02); no external reference |
| 13 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 14 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 21.3h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 1282 min (STALE); no external reference |
| 17 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 18 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 19 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 20 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 17.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1037 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 22 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 23 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 24 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 25 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 26 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 27 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 573 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 28 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 29 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 30 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 31 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 32 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 33 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 34 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 35 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 36 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 37 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 38 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 39 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 40 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 41 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 42 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 43 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 44 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 463 min (STALE); no external reference |
| 45 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 46 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 47 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 48 | `KXITFWMATCH-26NOV11CORROJ-ROJ` | ITF_WOMEN | fair_v1 | 87% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade D, thinner serve sample 531.0, ratio 1.04); no external reference |
| 49 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 50 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9736, "by_level_share_of_ge_25pp": {"ATP": 0.0121, "CHALLENGER": 0.1103, "DOUBLES": 0.0644, "ITF_MEN": 0.3396, "ITF_WOMEN": 0.4442, "OTHER": 0.0006, "WTA": 0.0144, "WTA125": 0.0145}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5576, "share_primary_cause_market_settled_or_in_play": 0.4474, "share_primary_cause_stale_quote_only": 0.2008}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 20274, "identity_ambiguous_share": 0.1955, "ticker_orientation": {"VERIFIED": 20274}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 13574, "with_external": 648, "coverage": 0.0477, "external_status": {"EXTERNAL_STALE": 411, "AGREES_WITH_KALSHI": 224, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 411, "MODEL_LONE_OUTLIER": 224, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3457, "share_external_supports_model": 0.0201}, "pregame_clean_ge_25pp": {"n": 6146, "with_external": 616, "coverage": 0.1002, "external_status": {"EXTERNAL_STALE": 386, "AGREES_WITH_KALSHI": 217, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 386, "MODEL_LONE_OUTLIER": 217, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3523, "share_external_supports_model": 0.0211}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 484.0, "median_sample_ratio": 2.44, "median_min_matches": 18.0, "median_max_days_since_last": 246.0, "share_severe_asymmetry": 0.2063, "data_status": {"POOR": 11531, "LIMITED": 5103, "ADEQUATE": 3640}, "comparison_lt_10pp": {"median_thinner_serve_points": 1670.0, "median_sample_ratio": 1.71, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1659, "model_minus_observed": 0.0703, "kalshi_minus_observed": -0.0688, "brier_diff_model_minus_kalshi": 0.0036}, "4-10x": {"n": 1134, "model_minus_observed": 0.0866, "kalshi_minus_observed": -0.0577, "brier_diff_model_minus_kalshi": 0.0101}, "<2x": {"n": 4044, "model_minus_observed": 0.104, "kalshi_minus_observed": -0.019, "brier_diff_model_minus_kalshi": 0.0151}, ">=10x": {"n": 1397, "model_minus_observed": 0.1271, "kalshi_minus_observed": -0.0443, "brier_diff_model_minus_kalshi": 0.0183}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 8234, "model": {"intercept": -0.562, "slope": 0.817, "slope_se": 0.028}, "kalshi_mid_same_rows": {"intercept": 0.165, "slope": 1.059, "slope_se": 0.031}, "mean_extremity_model": 0.174, "mean_extremity_kalshi": 0.1714, "model_brier": 0.2334, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.0302, "brier_diff_se": 0.0021, "model_logloss": 0.6645, "kalshi_logloss": 0.5888}, "fair_v1": {"n": 8234, "model": {"intercept": -0.471, "slope": 1.02, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.212, "slope": 1.081, "slope_se": 0.031}, "mean_extremity_model": 0.1677, "mean_extremity_kalshi": 0.1711, "model_brier": 0.216, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.0126, "brier_diff_se": 0.0017, "model_logloss": 0.6213, "kalshi_logloss": 0.5889}, "gen1_elo": {"n": 8234, "model": {"intercept": -0.456, "slope": 1.003, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.217, "slope": 1.073, "slope_se": 0.031}, "mean_extremity_model": 0.1742, "mean_extremity_kalshi": 0.1713, "model_brier": 0.215, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": 0.0116, "brier_diff_se": 0.0017, "model_logloss": 0.6197, "kalshi_logloss": 0.5891}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2542, "share_ge_15": 0.4503, "median_abs_gap": 13.22, "n": 53406}, "gen1_elo": {"share_ge_25": 0.2519, "share_ge_15": 0.4457, "median_abs_gap": 13.01, "n": 53406}, "gen1_sr": {"share_ge_25": 0.3166, "share_ge_15": 0.5254, "median_abs_gap": 16.01, "n": 53406}, "gen2": {"share_ge_25": 0.3166, "share_ge_15": 0.5138, "median_abs_gap": 15.55, "n": 53406}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1514, "share_ge_15": 0.355, "median_abs_gap": 10.71, "n": 40584}, "gen1_elo": {"share_ge_25": 0.1499, "share_ge_15": 0.3491, "median_abs_gap": 10.51, "n": 40584}, "gen1_sr": {"share_ge_25": 0.2145, "share_ge_15": 0.4396, "median_abs_gap": 12.99, "n": 40587}, "gen2": {"share_ge_25": 0.2296, "share_ge_15": 0.439, "median_abs_gap": 12.84, "n": 40588}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.47, "share_ge_25_all": 0.037, "share_ge_25_pregame_clean": 0.031}, "WTA": {"median_abs_gap_pregame_clean": 7.67, "share_ge_25_all": 0.0591, "share_ge_25_pregame_clean": 0.0502}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2341, "share_within_10pp_all": 0.4354, "share_within_10pp_pregame_clean": 0.4904, "corr_model_vs_mid_pregame_clean": 0.85}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1181, "model_brier": 0.1968, "kalshi_brier": 0.1968, "brier_diff_model_minus_kalshi": 0.0}, "10-15": {"n_settled": 1431, "model_brier": 0.22, "kalshi_brier": 0.2104, "brier_diff_model_minus_kalshi": 0.0096}, "15-25": {"n_settled": 1827, "model_brier": 0.2254, "kalshi_brier": 0.2069, "brier_diff_model_minus_kalshi": 0.0185}, "25-40": {"n_settled": 1039, "model_brier": 0.2253, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.022}, "3-5": {"n_settled": 765, "model_brier": 0.209, "kalshi_brier": 0.2084, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 214, "model_brier": 0.307, "kalshi_brier": 0.1666, "brier_diff_model_minus_kalshi": 0.1404}, "5-10": {"n_settled": 1777, "model_brier": 0.2023, "kalshi_brier": 0.2005, "brier_diff_model_minus_kalshi": 0.0017}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.562, "slope": 0.817, "slope_se": 0.028}, "kalshi_slope": {"intercept": 0.165, "slope": 1.059, "slope_se": 0.031}, "n": 8234}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.5, "slope": 0.865, "slope_se": 0.023}, "kalshi_slope": {"intercept": 0.15, "slope": 1.061, "slope_se": 0.027}, "n": 10543}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 712, "model_brier": 0.2977, "kalshi_brier": 0.2314, "brier_diff_model_minus_kalshi": 0.0664, "brier_diff_se": 0.0109, "corr_model_outcome": 0.1133, "corr_kalshi_outcome": 0.2849}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
