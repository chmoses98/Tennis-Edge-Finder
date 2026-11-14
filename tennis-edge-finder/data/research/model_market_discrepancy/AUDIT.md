# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-14T07:54Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 92,435): 0-3 13.9%, 3-5 9.5%, 5-10 20.1%, 10-15 15.2%, 15-25 19.2%, 25-40 13.8%, 40+ 8.4%; median gap 11.95 pp.
* **Where the extremes live**: 97.4% of >=25 pp gaps are off the ATP/WTA main tour (ITF 78.3%, Challenger 11.1%, doubles 6.5%). Main tour: ATP 3.7% and WTA 5.9% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 20,479): MARKET_ALREADY_SETTLED_WHEN_PRICED 35.7%, STALE_QUOTE 19.9%, BOOK_QUALITY 16.1%, POOR_DATA 9.0%, POSSIBLY_IN_PLAY_QUOTE 5.9%, IDENTITY_AMBIGUOUS 4.2%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 1.7%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 35.7%, market_freshness 19.9%, execution 16.1%, data 12.3%, market_freshness/coverage 9.4%, mapping 4.2%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 55.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 45.1% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 20,479 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.7%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 27.0% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 490.0 points vs 1678.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.022, Gen-2 0.819, Gen-1 ledger 0.864 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 1045 model 0.2254 vs Kalshi 0.2037; n 214 model 0.307 vs Kalshi 0.1666.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA. Not implemented here.

## 1. Observations

* 382,498 model-market comparisons (634,185 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 125,754 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-14T07:34:11.637874+00:00'], shadow board 107,158 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-14T07:34:14.781019+00:00'], Model 4 44,334 rows, 31,817 settled tickers, 11,978 tickers with an external scan.
* By model: {"gen1_ledger": 83944, "gen1_elo": 53848, "fair_v1": 53848, "gen2": 53848, "gen1_sr": 53848, "model4_fundamental": 41623, "model4_conditioned": 41539}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 92,435 | 13.9 | 9.5 | 20.1 | 15.2 | 19.2 | 13.8 | 8.4 | 11.95 | 41.3% | 22.2% |
| MW fair_v1 | 53,848 | 12.5 | 8.6 | 18.6 | 15.2 | 19.6 | 15.0 | 10.5 | 13.24 | 45.1% | 25.5% |
| MW gen1_elo | 53,848 | 12.3 | 8.7 | 19.1 | 15.2 | 19.4 | 15.0 | 10.3 | 13.02 | 44.7% | 25.3% |
| MW gen1_ledger | 38,587 | 15.8 | 10.8 | 22.2 | 15.2 | 18.6 | 11.9 | 5.5 | 10.29 | 36.1% | 17.5% |
| MW gen1_sr | 53,848 | 9.9 | 7.1 | 16.5 | 13.9 | 20.9 | 18.8 | 12.9 | 16.02 | 52.6% | 31.7% |
| MW gen2 | 53,848 | 10.8 | 7.5 | 16.6 | 13.7 | 19.7 | 17.7 | 14.0 | 15.56 | 51.4% | 31.7% |
| all families model4_conditioned | 41,539 | 22.2 | 17.9 | 34.6 | 16.9 | 4.9 | 2.2 | 1.2 | 6.06 | 8.4% | 3.4% |
| all families model4_fundamental | 41,623 | 17.3 | 13.6 | 34.0 | 19.9 | 9.9 | 3.8 | 1.5 | 7.6 | 15.2% | 5.3% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.5%, >=15pp 41.3%, >=20pp 30.6%, >=25pp 22.2%, >=30pp 16.1%, >=40pp 8.4%, >=50pp 3.9%
Executable gap (model outside the book, before fees): median 8.62pp; >=10pp 45.8%, >=25pp 17.7%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,138 | 27.9 | 16.0 | 28.0 | 13.2 | 10.7 | 3.5 | 0.6 | 5.77 | 14.8% | 4.1% |
| CHALLENGER | 8,450 | 16.3 | 9.6 | 20.6 | 15.2 | 15.7 | 11.4 | 11.2 | 10.94 | 38.3% | 22.6% |
| ITF_MEN | 15,992 | 9.6 | 7.3 | 17.0 | 14.9 | 21.0 | 17.1 | 13.0 | 15.45 | 51.1% | 30.1% |
| ITF_WOMEN | 20,818 | 9.3 | 7.0 | 16.1 | 14.6 | 22.2 | 18.6 | 12.1 | 16.05 | 52.9% | 30.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,117 | 16.6 | 13.2 | 24.9 | 20.7 | 16.8 | 6.7 | 1.1 | 8.66 | 24.6% | 7.8% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,138 | 26.3 | 15.7 | 26.4 | 15.8 | 11.3 | 3.9 | 0.8 | 6.09 | 15.9% | 4.7% |
| CHALLENGER | 8,450 | 14.4 | 9.1 | 19.0 | 13.7 | 18.4 | 13.7 | 11.7 | 12.55 | 43.7% | 25.4% |
| ITF_MEN | 15,992 | 8.2 | 6.2 | 15.2 | 13.8 | 20.3 | 19.9 | 16.4 | 17.84 | 56.6% | 36.3% |
| ITF_WOMEN | 20,818 | 7.8 | 5.9 | 14.1 | 12.7 | 20.7 | 21.2 | 17.8 | 19.21 | 59.7% | 39.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,117 | 14.1 | 10.3 | 21.5 | 16.3 | 22.6 | 12.8 | 2.5 | 11.28 | 37.9% | 15.3% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,138 | 23.5 | 14.2 | 25.6 | 15.4 | 14.3 | 5.9 | 1.1 | 7.01 | 21.3% | 7.0% |
| CHALLENGER | 8,450 | 15.2 | 9.5 | 20.7 | 15.5 | 16.0 | 11.9 | 11.1 | 11.17 | 39.0% | 23.0% |
| ITF_MEN | 15,992 | 9.3 | 7.3 | 17.2 | 14.3 | 21.3 | 17.3 | 13.2 | 15.75 | 51.9% | 30.6% |
| ITF_WOMEN | 20,818 | 9.2 | 6.8 | 16.2 | 15.5 | 22.1 | 18.7 | 11.5 | 15.84 | 52.2% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,117 | 22.4 | 17.2 | 31.8 | 15.2 | 9.1 | 3.3 | 1.0 | 6.12 | 13.4% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,507 | 28.1 | 19.6 | 29.2 | 12.1 | 8.1 | 2.5 | 0.4 | 5.24 | 11.0% | 2.9% |
| CHALLENGER | 5,116 | 23.3 | 14.7 | 27.6 | 14.6 | 12.9 | 5.4 | 1.5 | 6.94 | 19.8% | 6.9% |
| DOUBLES | 2,857 | 4.8 | 4.4 | 12.8 | 10.9 | 20.6 | 25.0 | 21.6 | 23.41 | 67.1% | 46.6% |
| ITF_MEN | 11,500 | 12.8 | 9.6 | 21.5 | 15.7 | 21.6 | 12.8 | 6.0 | 11.77 | 40.4% | 18.8% |
| ITF_WOMEN | 13,363 | 13.5 | 9.3 | 19.9 | 15.8 | 21.6 | 14.5 | 5.3 | 12.14 | 41.5% | 19.9% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,839 | 23.8 | 15.8 | 32.0 | 16.8 | 9.0 | 2.5 | 0.2 | 6.57 | 11.7% | 2.7% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,009 | 28.4 | 16.2 | 28.4 | 13.2 | 10.4 | 3.1 | 0.3 | 5.64 | 13.8% | 3.4% |
| CHALLENGER | 5,915 | 21.2 | 12.1 | 25.7 | 18.0 | 15.7 | 5.5 | 1.8 | 8.16 | 23.1% | 7.3% |
| ITF_MEN | 11,515 | 11.9 | 8.8 | 20.6 | 17.2 | 22.1 | 14.0 | 5.4 | 12.42 | 41.5% | 19.4% |
| ITF_WOMEN | 15,064 | 11.3 | 8.6 | 19.2 | 17.0 | 24.1 | 15.2 | 4.5 | 13.1 | 43.9% | 19.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,002 | 16.8 | 13.3 | 25.2 | 21.1 | 16.9 | 6.2 | 0.6 | 8.5 | 23.6% | 6.8% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,009 | 26.6 | 16.0 | 26.7 | 15.7 | 11.2 | 3.4 | 0.4 | 6.02 | 15.0% | 3.8% |
| CHALLENGER | 5,915 | 18.1 | 11.8 | 23.9 | 16.2 | 19.0 | 8.9 | 2.0 | 8.95 | 30.0% | 10.9% |
| ITF_MEN | 11,517 | 9.8 | 7.4 | 17.8 | 16.0 | 22.3 | 17.9 | 9.0 | 14.66 | 49.1% | 26.8% |
| ITF_WOMEN | 15,066 | 8.9 | 7.0 | 16.1 | 14.2 | 22.6 | 20.6 | 10.6 | 16.51 | 53.8% | 31.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,002 | 14.3 | 10.4 | 21.7 | 16.5 | 22.8 | 12.5 | 1.9 | 11.08 | 37.1% | 14.4% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,437 | 28.4 | 19.7 | 29.2 | 12.3 | 7.7 | 2.3 | 0.3 | 5.2 | 10.3% | 2.6% |
| CHALLENGER | 4,523 | 24.6 | 15.5 | 28.7 | 14.8 | 12.2 | 3.7 | 0.4 | 6.48 | 16.3% | 4.1% |
| DOUBLES | 2,671 | 4.6 | 4.5 | 13.1 | 10.9 | 20.4 | 24.9 | 21.7 | 23.31 | 67.0% | 46.6% |
| ITF_MEN | 9,927 | 13.6 | 10.0 | 22.9 | 16.3 | 21.7 | 11.4 | 4.1 | 10.9 | 37.2% | 15.5% |
| ITF_WOMEN | 11,505 | 14.1 | 9.8 | 21.0 | 16.4 | 21.8 | 13.4 | 3.5 | 11.35 | 38.7% | 16.9% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,774 | 24.1 | 16.2 | 32.0 | 16.7 | 8.9 | 2.0 | 0.1 | 6.44 | 10.9% | 2.0% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,857 | 4.8 | 4.4 | 12.8 | 10.9 | 20.6 | 25.0 | 21.6 | 23.41 | 67.1% | 46.6% |
| singles | 35,730 | 16.7 | 11.3 | 22.9 | 15.5 | 18.4 | 10.9 | 4.2 | 9.74 | 33.6% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 11,770 | 12.6 | 9.0 | 19.2 | 14.9 | 19.6 | 14.3 | 10.3 | 13.05 | 44.3% | 24.7% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 35,000 | 12.9 | 8.6 | 18.8 | 15.1 | 19.2 | 15.1 | 10.4 | 13.05 | 44.6% | 25.5% |
| UNKNOWN | 6,665 | 10.5 | 7.5 | 17.1 | 16.6 | 21.5 | 15.8 | 11.1 | 14.3 | 48.4% | 26.9% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 14,953 | 19.0 | 11.8 | 22.3 | 15.7 | 14.9 | 9.6 | 6.7 | 9.06 | 31.1% | 16.2% |
| B | 6,392 | 12.9 | 8.5 | 19.4 | 15.2 | 19.8 | 12.3 | 11.7 | 12.88 | 43.9% | 24.1% |
| C | 7,719 | 11.8 | 8.5 | 19.2 | 16.0 | 19.2 | 14.7 | 10.6 | 13.08 | 44.5% | 25.3% |
| D | 8,920 | 11.2 | 8.3 | 17.8 | 15.2 | 21.6 | 15.8 | 10.1 | 14.09 | 47.4% | 25.9% |
| F | 15,864 | 7.3 | 5.7 | 15.1 | 14.2 | 23.0 | 21.1 | 13.7 | 18.05 | 57.7% | 34.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 10,137 | 25.0 | 15.9 | 29.0 | 14.8 | 10.6 | 3.4 | 1.2 | 6.35 | 15.2% | 4.7% |
| B | 5,250 | 16.8 | 11.0 | 24.1 | 17.0 | 18.9 | 9.3 | 2.9 | 9.61 | 31.2% | 12.3% |
| C | 7,643 | 11.0 | 7.8 | 19.5 | 14.9 | 20.9 | 15.8 | 10.1 | 13.54 | 46.8% | 25.9% |
| D | 5,908 | 14.3 | 9.9 | 21.1 | 15.5 | 21.1 | 12.8 | 5.3 | 11.42 | 39.2% | 18.1% |
| F | 9,649 | 10.2 | 8.4 | 16.8 | 14.5 | 23.5 | 18.8 | 7.9 | 15.07 | 50.2% | 26.7% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 16,938 | 17.5 | 10.8 | 21.3 | 15.5 | 15.2 | 10.2 | 9.5 | 10.08 | 34.9% | 19.7% |
| LIMITED | 11,725 | 13.4 | 9.4 | 20.3 | 15.9 | 19.8 | 13.4 | 7.7 | 12.01 | 41.0% | 21.1% |
| POOR | 25,185 | 8.8 | 6.6 | 16.1 | 14.6 | 22.4 | 19.0 | 12.4 | 16.37 | 53.8% | 31.4% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,378 | 23.8 | 18.0 | 33.0 | 15.4 | 6.4 | 3.0 | 0.4 | 5.89 | 9.8% | 3.4% |
| GAME_SPREAD | 6,986 | 22.8 | 15.3 | 32.1 | 16.8 | 9.1 | 3.3 | 0.7 | 6.68 | 13.0% | 3.9% |
| MATCH_WINNER | 38,587 | 15.8 | 10.8 | 22.2 | 15.2 | 18.6 | 11.9 | 5.5 | 10.29 | 36.1% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 17,245 | 28.4 | 16.8 | 30.8 | 12.7 | 8.8 | 2.3 | 0.3 | 5.57 | 11.4% | 2.6% |
| TOTAL_GAMES | 11,724 | 9.7 | 10.8 | 36.5 | 25.6 | 10.4 | 4.2 | 2.8 | 9.12 | 17.4% | 7.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,776 | 24.5 | 28.8 | 33.2 | 8.0 | 3.9 | 1.2 | 0.3 | 4.79 | 5.4% | 1.5% |
| GAME_SPREAD | 9,602 | 46.6 | 15.8 | 25.2 | 7.4 | 2.4 | 1.9 | 0.6 | 3.33 | 4.9% | 2.5% |
| TOTAL_GAMES | 17,161 | 6.5 | 9.8 | 41.0 | 29.8 | 7.2 | 3.3 | 2.3 | 9.14 | 12.9% | 5.6% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,812 | 23.9 | 16.7 | 34.6 | 14.7 | 6.9 | 2.7 | 0.5 | 6.05 | 10.1% | 3.2% |
| GAME_SPREAD | 9,611 | 20.3 | 13.4 | 28.5 | 20.2 | 12.1 | 4.3 | 1.1 | 7.71 | 17.6% | 5.5% |
| TOTAL_GAMES | 17,200 | 10.0 | 10.9 | 36.5 | 24.3 | 11.3 | 4.4 | 2.6 | 9.01 | 18.2% | 7.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 53,848 | 45.1% | 25.5% | 13.24 | 35.5% | 15.1% | 10.71 |
| gen1_elo | 53,848 | 44.7% | 25.3% | 13.02 | 34.9% | 15.0% | 10.5 |
| gen1_sr | 53,848 | 52.6% | 31.7% | 16.02 | 43.9% | 21.4% | 12.98 |
| gen2 | 53,848 | 51.4% | 31.7% | 15.56 | 43.9% | 22.9% | 12.82 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,625 | 15.4 | 10.5 | 21.3 | 17.2 | 20.1 | 11.9 | 3.5 | 10.72 | 35.4% | 15.4% |
| STALE | 33,223 | 10.7 | 7.4 | 17.0 | 13.9 | 19.3 | 17.0 | 14.8 | 15.45 | 51.1% | 31.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 32,055 | 16.3 | 11.1 | 22.7 | 15.2 | 18.2 | 11.5 | 5.0 | 9.97 | 34.7% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 92,435 | 32055 | 24097 | 36283 | 25.3 | 154.5 | 1451.1 |
| ge_15pp | 38,197 | 11115 | 8601 | 18481 | 29.2 | 455.7 | 1451.1 |
| ge_25pp | 20,479 | 5281 | 3763 | 11435 | 35.0 | 599.9 | 1431.1 |
| lt_10pp | 40,216 | 16055 | 11387 | 12774 | 22.8 | 49.7 | 1421.7 |

Current slate `SL-20261114T075400Z-3690c009`: 154 priced rows, quote age at build {'median': 48.1, 'max': 58.1}, freshness {'STALE': 154}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 52 | 0.0 | 0.0 | 34.6 | 9.6 | 32.7 | 19.2 | 3.9 | 18.34 | 55.8% | 23.1% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 5,120 | 19.2 | 11.1 | 25.7 | 18.3 | 17.7 | 7.1 | 1.0 | 8.77 | 25.8% | 8.1% |
| KALSHI_LONE_OUTLIER | 32 | 6.2 | 6.2 | 75.0 | 6.2 | 3.1 | 3.1 | 0.0 | 6.16 | 6.2% | 3.1% |
| MARKETS_AGREE | 1,107 | 66.1 | 33.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,344 | 0.0 | 2.2 | 38.4 | 25.9 | 23.9 | 8.7 | 0.9 | 11.65 | 33.5% | 9.6% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 53,848 | 8684 (16.1%) | 27.0% | 0.9% | {"EXTERNAL_STALE": 5120, "AGREES_WITH_KALSHI": 2344, "ALL_AGREE": 1107, "SUPPORTS_MODEL_DIRECTION": 50, "AGREES_WITH_MODEL": 32, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 24,283 | 2134 (8.8%) | 36.7% | 1.5% | {"EXTERNAL_STALE": 1319, "AGREES_WITH_KALSHI": 784, "SUPPORTS_MODEL_DIRECTION": 29, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 13,736 | 650 (4.7%) | 34.5% | 2.0% | {"EXTERNAL_STALE": 413, "AGREES_WITH_KALSHI": 224, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 6,166 | 617 (10.0%) | 35.2% | 2.1% | {"EXTERNAL_STALE": 387, "AGREES_WITH_KALSHI": 217, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 21,392 | 4999 (23.4%) | 19.0% | 0.9% | {"EXTERNAL_STALE": 2865, "ALL_AGREE": 1107, "AGREES_WITH_KALSHI": 952, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 28, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 10,571 | 10.5 | 7.7 | 18.9 | 14.3 | 21.7 | 16.4 | 10.4 | 14.41 | 48.6% | 26.9% |
| 4-10x | 7,292 | 10.8 | 8.6 | 18.1 | 14.9 | 21.5 | 14.7 | 11.4 | 14.12 | 47.6% | 26.1% |
| <2x | 27,398 | 14.4 | 9.6 | 19.8 | 15.9 | 17.6 | 13.4 | 9.3 | 11.77 | 40.3% | 22.7% |
| >=10x | 8,587 | 10.2 | 6.4 | 15.2 | 14.2 | 21.8 | 18.9 | 13.3 | 16.53 | 54.0% | 32.3% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 14,244 | 12.2 | 8.6 | 19.5 | 16.1 | 19.2 | 13.7 | 10.7 | 12.89 | 43.6% | 24.4% |
| 300-1000 | 11,748 | 11.4 | 8.6 | 17.8 | 15.1 | 20.5 | 16.4 | 10.2 | 13.94 | 47.0% | 26.6% |
| <300 | 16,991 | 8.1 | 5.9 | 15.1 | 14.4 | 22.9 | 20.0 | 13.6 | 17.47 | 56.5% | 33.7% |
| >=3000 | 10,865 | 20.9 | 12.8 | 23.9 | 15.3 | 14.1 | 7.5 | 5.5 | 7.92 | 27.1% | 13.0% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1677 | 0.5469 | 0.4083 | 0.4758 | +0.071 | -0.068 | 0.0042 ± 0.0038 |
| ratio 4-10x | 1144 | 0.5712 | 0.4272 | 0.4851 | +0.086 | -0.058 | 0.0095 ± 0.0047 |
| ratio <2x | 4097 | 0.5343 | 0.4116 | 0.4315 | +0.103 | -0.020 | 0.0147 ± 0.0022 |
| ratio >=10x | 1404 | 0.5579 | 0.3867 | 0.4302 | +0.128 | -0.043 | 0.0184 ± 0.0047 |
| thinner_sample 1000-3000 | 2302 | 0.5392 | 0.4125 | 0.4418 | +0.097 | -0.029 | 0.013 ± 0.003 |
| thinner_sample 300-1000 | 1898 | 0.5593 | 0.419 | 0.4673 | +0.092 | -0.048 | 0.0068 ± 0.0036 |
| thinner_sample <300 | 2704 | 0.5517 | 0.3853 | 0.4397 | +0.112 | -0.054 | 0.0158 ± 0.0034 |
| thinner_sample >=3000 | 1418 | 0.5277 | 0.4343 | 0.4457 | +0.082 | -0.011 | 0.0132 ± 0.003 |
| data_status ADEQUATE | 2252 | 0.5318 | 0.4296 | 0.4409 | +0.091 | -0.011 | 0.0145 ± 0.0026 |
| data_status LIMITED | 2036 | 0.5461 | 0.4135 | 0.4607 | +0.085 | -0.047 | 0.008 ± 0.0033 |
| data_status POOR | 4034 | 0.5536 | 0.395 | 0.4447 | +0.109 | -0.050 | 0.0137 ± 0.0027 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1196 | 0.1959 | 0.1959 | -0.0000 ± 0.0004 | 0.5711 | 0.5713 | 0.5027 | 0.4875 | 0.4933 | -0.098 ± 0.0135 | -0.0087 (8) |
| 3-5 | 783 | 0.2082 | 0.2075 | +0.0007 ± 0.0013 | 0.6023 | 0.5993 | 0.4999 | 0.4601 | 0.4713 | -0.098 ± 0.0167 | 0.01 (3) |
| 5-10 | 1793 | 0.2024 | 0.2005 | +0.0019 ± 0.0016 | 0.5911 | 0.5845 | 0.5095 | 0.4355 | 0.4584 | -0.091 ± 0.0109 | -0.0143 (7) |
| 10-15 | 1447 | 0.2207 | 0.211 | +0.0097 ± 0.003 | 0.6341 | 0.6059 | 0.5241 | 0.4007 | 0.4223 | -0.103 ± 0.0123 | -0.055 (6) |
| 15-25 | 1844 | 0.2255 | 0.2073 | +0.0181 ± 0.0041 | 0.6458 | 0.598 | 0.5704 | 0.376 | 0.4262 | -0.098 ± 0.0107 | -0.0045 (11) |
| 25-40 | 1045 | 0.2254 | 0.2037 | +0.0216 ± 0.0084 | 0.6412 | 0.5879 | 0.6426 | 0.3331 | 0.4517 | -0.064 ± 0.013 | -0.06 (2) |
| 40+ | 214 | 0.307 | 0.1666 | +0.1404 ± 0.0253 | 0.8206 | 0.5019 | 0.7244 | 0.2671 | 0.3505 | -0.089 ± 0.0244 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 6035 | 0.1868 | 0.1877 | -0.0008 ± 0.0002 | 0.5501 | 0.5511 | 0.4921 | 0.4768 | 0.5067 | -0.022 ± 0.0057 | -0.01 (28) |
| 3-5 | 4108 | 0.1992 | 0.1974 | +0.0018 ± 0.0006 | 0.5797 | 0.5734 | 0.4804 | 0.4406 | 0.4377 | -0.056 ± 0.007 | 0.005 (6) |
| 5-10 | 8981 | 0.2005 | 0.1962 | +0.0043 ± 0.0007 | 0.5866 | 0.5728 | 0.4823 | 0.4085 | 0.4164 | -0.049 ± 0.0047 | -0.0114 (22) |
| 10-15 | 7330 | 0.2023 | 0.1861 | +0.0162 ± 0.0013 | 0.5917 | 0.546 | 0.4839 | 0.36 | 0.3569 | -0.064 ± 0.0051 | -0.0379 (19) |
| 15-25 | 9430 | 0.2062 | 0.1671 | +0.0390 ± 0.0016 | 0.6041 | 0.4967 | 0.4977 | 0.3022 | 0.301 | -0.066 ± 0.0042 | -0.0043 (51) |
| 25-40 | 7381 | 0.2222 | 0.1235 | +0.0987 ± 0.0026 | 0.6385 | 0.381 | 0.5229 | 0.2086 | 0.2124 | -0.058 ± 0.004 | -0.0733 (3) |
| 40+ | 5121 | 0.3794 | 0.0437 | +0.3357 ± 0.0033 | 0.9889 | 0.1701 | 0.6272 | 0.1016 | 0.0566 | -0.077 ± 0.0028 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 958 | 0.2017 | 0.202 | -0.0003 ± 0.0005 | 0.5836 | 0.5844 | 0.5077 | 0.4927 | 0.5167 | -0.094 ± 0.0155 | -0.0117 (6) |
| 3-5 | 702 | 0.2111 | 0.2081 | +0.0030 ± 0.0014 | 0.6058 | 0.5992 | 0.5186 | 0.4789 | 0.4587 | -0.125 ± 0.0185 | 0.01 (3) |
| 5-10 | 1549 | 0.2045 | 0.2029 | +0.0016 ± 0.0017 | 0.5943 | 0.5905 | 0.5386 | 0.4641 | 0.4919 | -0.083 ± 0.0118 | -0.01 (4) |
| 10-15 | 1345 | 0.2156 | 0.2074 | +0.0082 ± 0.0031 | 0.624 | 0.6005 | 0.5574 | 0.4331 | 0.4647 | -0.103 ± 0.0129 | -0.04 (5) |
| 15-25 | 1941 | 0.2334 | 0.2125 | +0.0209 ± 0.0041 | 0.6647 | 0.6093 | 0.5839 | 0.3881 | 0.4343 | -0.097 ± 0.0107 | -0.0183 (12) |
| 25-40 | 1341 | 0.2661 | 0.2003 | +0.0658 ± 0.0077 | 0.7426 | 0.5811 | 0.6579 | 0.3445 | 0.3982 | -0.107 ± 0.0123 | -0.008 (5) |
| 40+ | 486 | 0.3749 | 0.1598 | +0.2151 ± 0.0182 | 1.0178 | 0.4849 | 0.7318 | 0.2426 | 0.2798 | -0.088 ± 0.0175 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5185 | 0.1897 | 0.1899 | -0.0002 ± 0.0002 | 0.5546 | 0.5548 | 0.5056 | 0.4905 | 0.5051 | -0.040 ± 0.0062 | -0.0154 (26) |
| 3-5 | 3608 | 0.1933 | 0.1923 | +0.0010 ± 0.0006 | 0.5638 | 0.5608 | 0.5106 | 0.471 | 0.4764 | -0.045 ± 0.0075 | 0.01 (5) |
| 5-10 | 8029 | 0.1955 | 0.1922 | +0.0033 ± 0.0007 | 0.5751 | 0.5628 | 0.5068 | 0.4325 | 0.4496 | -0.038 ± 0.005 | -0.0117 (6) |
| 10-15 | 6643 | 0.2021 | 0.1897 | +0.0124 ± 0.0013 | 0.5934 | 0.5553 | 0.5056 | 0.3817 | 0.3944 | -0.050 ± 0.0054 | -0.0189 (18) |
| 15-25 | 9529 | 0.2166 | 0.1804 | +0.0362 ± 0.0017 | 0.6308 | 0.5294 | 0.5238 | 0.3282 | 0.3359 | -0.058 ± 0.0044 | -0.014 (52) |
| 25-40 | 8559 | 0.2495 | 0.1377 | +0.1117 ± 0.0026 | 0.7051 | 0.4202 | 0.5585 | 0.2412 | 0.2274 | -0.075 ± 0.004 | -0.0095 (20) |
| 40+ | 6833 | 0.4018 | 0.0591 | +0.3427 ± 0.0034 | 1.0588 | 0.2126 | 0.6542 | 0.1187 | 0.0799 | -0.074 ± 0.0029 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1180 | 0.1967 | 0.1977 | -0.0011 ± 0.0005 | 0.5734 | 0.5759 | 0.5018 | 0.4863 | 0.522 | -0.060 ± 0.0135 | -0.0191 (11) |
| 3-5 | 843 | 0.2092 | 0.2075 | +0.0016 ± 0.0013 | 0.6057 | 0.6004 | 0.4956 | 0.456 | 0.4567 | -0.108 ± 0.0164 | 0.002 (5) |
| 5-10 | 1799 | 0.2032 | 0.1991 | +0.0041 ± 0.0016 | 0.5919 | 0.5805 | 0.5102 | 0.4363 | 0.4447 | -0.103 ± 0.0108 | -0.01 (10) |
| 10-15 | 1497 | 0.2122 | 0.203 | +0.0092 ± 0.0029 | 0.6152 | 0.5887 | 0.537 | 0.4138 | 0.4402 | -0.101 ± 0.0117 | -0.0286 (7) |
| 15-25 | 1743 | 0.2312 | 0.2118 | +0.0195 ± 0.0043 | 0.6597 | 0.6075 | 0.5794 | 0.3854 | 0.432 | -0.102 ± 0.0111 | -0.03 (1) |
| 25-40 | 1031 | 0.2178 | 0.206 | +0.0118 ± 0.0084 | 0.6256 | 0.5929 | 0.6508 | 0.3413 | 0.4743 | -0.058 ± 0.0131 | -0.0267 (3) |
| 40+ | 229 | 0.3093 | 0.1804 | +0.1289 ± 0.0253 | 0.8338 | 0.5323 | 0.7372 | 0.2806 | 0.3799 | -0.075 ± 0.0258 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5873 | 0.1867 | 0.1872 | -0.0005 ± 0.0002 | 0.5495 | 0.5499 | 0.4873 | 0.4719 | 0.4861 | -0.037 ± 0.0057 | -0.0189 (44) |
| 3-5 | 4196 | 0.2046 | 0.2029 | +0.0017 ± 0.0006 | 0.5946 | 0.5887 | 0.4805 | 0.4409 | 0.439 | -0.056 ± 0.0071 | -0.0073 (22) |
| 5-10 | 9112 | 0.1963 | 0.1908 | +0.0055 ± 0.0007 | 0.5765 | 0.559 | 0.4852 | 0.4113 | 0.4101 | -0.057 ± 0.0046 | -0.0117 (42) |
| 10-15 | 7352 | 0.1953 | 0.1797 | +0.0155 ± 0.0012 | 0.576 | 0.5321 | 0.4947 | 0.3714 | 0.3702 | -0.062 ± 0.005 | -0.0136 (14) |
| 15-25 | 9443 | 0.2108 | 0.1717 | +0.0391 ± 0.0017 | 0.615 | 0.5065 | 0.509 | 0.3143 | 0.3122 | -0.067 ± 0.0043 | -0.0533 (3) |
| 25-40 | 7374 | 0.2164 | 0.1234 | +0.0930 ± 0.0026 | 0.6259 | 0.3799 | 0.5246 | 0.2091 | 0.2209 | -0.051 ± 0.004 | -0.02 (4) |
| 40+ | 5036 | 0.3879 | 0.0476 | +0.3403 ± 0.0035 | 1.0113 | 0.1801 | 0.6361 | 0.107 | 0.0625 | -0.077 ± 0.0029 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1659 | 0.1965 | 0.1963 | +0.0003 ± 0.0004 | 0.5714 | 0.5707 | 0.5066 | 0.4916 | 0.4907 | -0.072 ± 0.0111 | -0.0311 (57) |
| 3-5 | 1167 | 0.1896 | 0.1896 | -0.0001 ± 0.001 | 0.5573 | 0.5565 | 0.4985 | 0.4586 | 0.4773 | -0.054 ± 0.013 | -0.0194 (34) |
| 5-10 | 2364 | 0.1989 | 0.1937 | +0.0052 ± 0.0014 | 0.5867 | 0.5703 | 0.51 | 0.4364 | 0.4387 | -0.077 ± 0.0093 | -0.005 (78) |
| 10-15 | 1631 | 0.2155 | 0.2034 | +0.0121 ± 0.0028 | 0.6256 | 0.5905 | 0.5446 | 0.4219 | 0.4329 | -0.086 ± 0.0115 | 0.0015 (67) |
| 15-25 | 2124 | 0.2321 | 0.2073 | +0.0248 ± 0.0039 | 0.6623 | 0.5982 | 0.5923 | 0.3974 | 0.4327 | -0.089 ± 0.01 | -0.0214 (59) |
| 25-40 | 1238 | 0.2425 | 0.2123 | +0.0302 ± 0.008 | 0.6918 | 0.608 | 0.6884 | 0.3769 | 0.4847 | -0.082 ± 0.0124 | -0.0297 (29) |
| 40+ | 459 | 0.3288 | 0.1991 | +0.1297 ± 0.02 | 0.9397 | 0.5804 | 0.8073 | 0.3304 | 0.4488 | -0.089 ± 0.0187 | -0.1033 (9) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5974 | 0.1775 | 0.1775 | +0.0000 ± 0.0002 | 0.5255 | 0.525 | 0.5088 | 0.4936 | 0.5007 | -0.041 ± 0.0055 | -0.0204 (104) |
| 3-5 | 4093 | 0.1945 | 0.1937 | +0.0008 ± 0.0006 | 0.5677 | 0.5657 | 0.502 | 0.4622 | 0.4713 | -0.040 ± 0.007 | -0.022 (74) |
| 5-10 | 8353 | 0.1972 | 0.1907 | +0.0065 ± 0.0007 | 0.5815 | 0.562 | 0.5034 | 0.4297 | 0.4236 | -0.061 ± 0.0048 | -0.0085 (136) |
| 10-15 | 5743 | 0.2109 | 0.1948 | +0.0161 ± 0.0014 | 0.614 | 0.5707 | 0.5378 | 0.4149 | 0.4099 | -0.070 ± 0.0059 | -0.0054 (112) |
| 15-25 | 7029 | 0.2315 | 0.199 | +0.0325 ± 0.0021 | 0.6657 | 0.5772 | 0.5768 | 0.3814 | 0.3965 | -0.067 ± 0.0054 | -0.024 (112) |
| 25-40 | 4534 | 0.2583 | 0.1913 | +0.0670 ± 0.0041 | 0.7299 | 0.5562 | 0.6411 | 0.3289 | 0.3807 | -0.061 ± 0.0064 | -0.0311 (63) |
| 40+ | 2032 | 0.3706 | 0.1602 | +0.2105 ± 0.0091 | 1.0418 | 0.4768 | 0.7413 | 0.2417 | 0.2913 | -0.058 ± 0.0085 | -0.0465 (20) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 8322 | 1.022 ± 0.031 | 1.08 | 0.1676 | 0.1711 | 0.2159 | 0.2034 |
| gen2 | 8322 | 0.819 ± 0.028 | 1.06 | 0.1739 | 0.1714 | 0.2332 | 0.2033 |
| gen1_elo | 8322 | 1.003 ± 0.03 | 1.071 | 0.174 | 0.1713 | 0.2151 | 0.2035 |
| gen1_sr | 8322 | 1.006 ± 0.036 | 1.107 | 0.1335 | 0.1729 | 0.2292 | 0.203 |
| gen1_ledger | 10642 | 0.864 ± 0.023 | 1.061 | 0.1903 | 0.1772 | 0.2174 | 0.2003 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 38,197)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 9,183 | 24.0% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 9,066 | 23.7% |
| BOOK_QUALITY | execution | 6,401 | 16.8% |
| POOR_DATA | data | 4,343 | 11.4% |
| LIMITED_DATA | data | 2,286 | 6.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 2,245 | 5.9% |
| IDENTITY_AMBIGUOUS | mapping | 1,570 | 4.1% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,441 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 1,078 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 583 | 1.5% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 24.0%, coverage 23.7%, data 17.3%, execution 16.8%, market_freshness/coverage 8.7%, mapping 4.1%, model_calibration_or_unknown 3.8%, model_calibration 1.5%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 95.1%, LOW_DATA_QUALITY 72.1%, THIN_PLAYER_HISTORY 60.0%, STALE_PLAYER_DATA 51.8%, STALE_KALSHI_QUOTE 48.4%, MODEL_INTERNAL_DISAGREEMENT 41.6%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 23.2%, MODEL_HIGH_UNCERTAINTY 18.8%, PLAYER_IDENTITY_RISK 15.0%, LEVEL_TRANSFER_RISK 9.2%, LOW_DISPLAYED_LIQUIDITY 8.7%, EVENT_MAPPING_RISK 7.0%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.1%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 26.1%, POST_SETTLEMENT_OBSERVATION 23.7%, POSSIBLE_IN_PLAY_QUOTE 6.3%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 20,479)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,306 | 35.7% |
| STALE_QUOTE | market_freshness | 4,073 | 19.9% |
| BOOK_QUALITY | execution | 3,305 | 16.1% |
| POOR_DATA | data | 1,840 | 9.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,213 | 5.9% |
| IDENTITY_AMBIGUOUS | mapping | 871 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 708 | 3.5% |
| LIMITED_DATA | data | 675 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 347 | 1.7% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 140 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 35.7%, market_freshness 19.9%, execution 16.1%, data 12.3%, market_freshness/coverage 9.4%, mapping 4.2%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.2%, START_UNVERIFIABLE 97.4%, LOW_DATA_QUALITY 75.2%, THIN_PLAYER_HISTORY 62.0%, STALE_KALSHI_QUOTE 55.8%, STALE_PLAYER_DATA 45.0%, MODEL_INTERNAL_DISAGREEMENT 41.6%, ASYMMETRIC_SAMPLE_SIZE 34.2%, WIDE_SPREAD 22.4%, MODEL_HIGH_UNCERTAINTY 19.5%, PLAYER_IDENTITY_RISK 17.8%, LOW_DISPLAYED_LIQUIDITY 8.6%, EVENT_MAPPING_RISK 8.5%, LEVEL_TRANSFER_RISK 8.0%, MODEL_CALIBRATION_OUTLIER 4.6%, EXTERNAL_MARKET_REJECTION 1.7%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 38.6%, POST_SETTLEMENT_OBSERVATION 35.7%, POSSIBLE_IN_PLAY_QUOTE 6.5%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 16484, "IDENTITY_AMBIGUOUS": 3995}; ticker orientation: {"VERIFIED": 20479}.

Checks: discipline:AMBIGUOUS 1331, discipline:PASS 19148, identity_confidence:AMBIGUOUS 3642, identity_confidence:PASS 16837, level_mapping:NA 1343, level_mapping:PASS 19136, market_pair:AMBIGUOUS 518, market_pair:NA 435, market_pair:PASS 19526, model_complement:NA 397, model_complement:PASS 20082, namesake:AMBIGUOUS 6, namesake:PASS 20473, physical_match_id:NA 6743, physical_match_id:PASS 13736, player_ids:PASS 20479, same_pair_other_event:PASS 20479, ticker_orientation:PASS 20479

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,645 | 3.7% | 3.1% | 1.2% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 24, "market_freshness/coverage": 22} | 5.47 | 0.222 / 0.2184 (873) | 25.7% | 2.4% | 3.2% | 3.0% |
| CHALLENGER | 13,566 | 16.7% | 5.9% | 11.1% | {"coverage": 1399, "market_freshness": 274, "market_freshness/coverage": 249, "data": 164, "model_calibration_or_unknown": 80, "execution": 41, "model_calibration": 41, "mapping": 17, "possible_market_error": 1} | 7.29 | 0.2213 / 0.2115 (3172) | 41.8% | 13.5% | 4.0% | 23.1% |
| DOUBLES | 2,857 | 46.6% | 46.6% | 6.5% | {"execution": 734, "mapping": 405, "market_freshness": 106, "market_freshness/coverage": 79, "coverage": 7} | 23.31 | 0.2982 / 0.2321 (723) | 8.2% | 0.0% | 100.0% | 6.5% |
| ITF_MEN | 27,492 | 25.4% | 17.6% | 34.1% | {"coverage": 2491, "market_freshness": 1445, "execution": 1056, "data": 1030, "market_freshness/coverage": 713, "mapping": 233, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.73 | 0.218 / 0.1978 (5867) | 42.4% | 69.6% | 14.2% | 22.0% |
| ITF_WOMEN | 34,181 | 26.5% | 18.6% | 44.2% | {"coverage": 3330, "market_freshness": 1987, "execution": 1391, "data": 1220, "market_freshness/coverage": 801, "mapping": 210, "model_calibration_or_unknown": 98, "model_calibration": 23} | 12.41 | 0.2036 / 0.1941 (6699) | 43.0% | 57.2% | 10.1% | 22.3% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,956 | 5.9% | 5.0% | 1.4% | {"market_freshness": 111, "model_calibration_or_unknown": 53, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.69 | 0.2319 / 0.2213 (818) | 30.3% | 2.0% | 1.2% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.4% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 113 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 725 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFMATCH-26NOV12VALRAT-RAT` | ITF_MEN | gen1_ledger | 92% / 4% | +88 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 10 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1333.0, ratio 3.64); no external reference |
| 6 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 7 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 8 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 311 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 9 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 10 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 11 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 572 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 12 | `KXITFMATCH-26NOV10KOUPOR-POR` | ITF_MEN | fair_v1 | 87% / 2% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.1h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 493 min (STALE); data POOR (grade D, thinner serve sample 1554.0, ratio 1.02); no external reference |
| 13 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 14 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 21.3h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 1282 min (STALE); no external reference |
| 17 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 18 | `KXITFMATCH-26NOV13ALMJAD-ALM` | ITF_MEN | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 68 min (STALE); data LIMITED (grade C, thinner serve sample 691.0, ratio 3.98); no external reference |
| 19 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 20 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 21 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 22 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 23 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 24 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 25 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 26 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 27 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 28 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 573 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 29 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 30 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 31 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 32 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 33 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 34 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 35 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 36 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 37 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 271 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 38 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 39 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 40 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 41 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 42 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 43 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 44 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 45 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 768 min (STALE); no external reference |
| 46 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 47 | `KXITFMATCH-26NOV13JADZIN-ZIN` | ITF_MEN | fair_v1 | 89% / 10% | +80 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 28 min (AGING); data POOR (grade D, thinner serve sample 691.0, ratio 5.99); no external reference |
| 48 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 49 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 50 | `KXITFWMATCH-26NOV11CORROJ-ROJ` | ITF_WOMEN | fair_v1 | 87% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 649 min (STALE); data POOR (grade D, thinner serve sample 531.0, ratio 1.04); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9737, "by_level_share_of_ge_25pp": {"ATP": 0.012, "CHALLENGER": 0.1106, "DOUBLES": 0.065, "ITF_MEN": 0.3408, "ITF_WOMEN": 0.4424, "OTHER": 0.0006, "WTA": 0.0143, "WTA125": 0.0143}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5584, "share_primary_cause_market_settled_or_in_play": 0.4506, "share_primary_cause_stale_quote_only": 0.1989}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 20479, "identity_ambiguous_share": 0.1951, "ticker_orientation": {"VERIFIED": 20479}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 13736, "with_external": 650, "coverage": 0.0473, "external_status": {"EXTERNAL_STALE": 413, "AGREES_WITH_KALSHI": 224, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 413, "MODEL_LONE_OUTLIER": 224, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3446, "share_external_supports_model": 0.02}, "pregame_clean_ge_25pp": {"n": 6166, "with_external": 617, "coverage": 0.1001, "external_status": {"EXTERNAL_STALE": 387, "AGREES_WITH_KALSHI": 217, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 387, "MODEL_LONE_OUTLIER": 217, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3517, "share_external_supports_model": 0.0211}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 490.0, "median_sample_ratio": 2.43, "median_min_matches": 18.0, "median_max_days_since_last": 246.0, "share_severe_asymmetry": 0.205, "data_status": {"POOR": 11600, "LIMITED": 5181, "ADEQUATE": 3698}, "comparison_lt_10pp": {"median_thinner_serve_points": 1678.0, "median_sample_ratio": 1.71, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1677, "model_minus_observed": 0.0711, "kalshi_minus_observed": -0.0676, "brier_diff_model_minus_kalshi": 0.0042}, "4-10x": {"n": 1144, "model_minus_observed": 0.086, "kalshi_minus_observed": -0.058, "brier_diff_model_minus_kalshi": 0.0095}, "<2x": {"n": 4097, "model_minus_observed": 0.1027, "kalshi_minus_observed": -0.0199, "brier_diff_model_minus_kalshi": 0.0147}, ">=10x": {"n": 1404, "model_minus_observed": 0.1277, "kalshi_minus_observed": -0.0435, "brier_diff_model_minus_kalshi": 0.0184}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 8322, "model": {"intercept": -0.561, "slope": 0.819, "slope_se": 0.028}, "kalshi_mid_same_rows": {"intercept": 0.166, "slope": 1.06, "slope_se": 0.031}, "mean_extremity_model": 0.1739, "mean_extremity_kalshi": 0.1714, "model_brier": 0.2332, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.0299, "brier_diff_se": 0.0021, "model_logloss": 0.6639, "kalshi_logloss": 0.5889}, "fair_v1": {"n": 8322, "model": {"intercept": -0.47, "slope": 1.022, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.211, "slope": 1.08, "slope_se": 0.031}, "mean_extremity_model": 0.1676, "mean_extremity_kalshi": 0.1711, "model_brier": 0.2159, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": 0.0125, "brier_diff_se": 0.0017, "model_logloss": 0.6211, "kalshi_logloss": 0.589}, "gen1_elo": {"n": 8322, "model": {"intercept": -0.458, "slope": 1.003, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.214, "slope": 1.071, "slope_se": 0.03}, "mean_extremity_model": 0.174, "mean_extremity_kalshi": 0.1713, "model_brier": 0.2151, "kalshi_brier": 0.2035, "brier_diff_model_minus_kalshi": 0.0116, "brier_diff_se": 0.0017, "model_logloss": 0.6199, "kalshi_logloss": 0.5892}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2551, "share_ge_15": 0.451, "median_abs_gap": 13.24, "n": 53848}, "gen1_elo": {"share_ge_25": 0.2529, "share_ge_15": 0.4466, "median_abs_gap": 13.02, "n": 53848}, "gen1_sr": {"share_ge_25": 0.3172, "share_ge_15": 0.5259, "median_abs_gap": 16.02, "n": 53848}, "gen2": {"share_ge_25": 0.3173, "share_ge_15": 0.5141, "median_abs_gap": 15.56, "n": 53848}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1511, "share_ge_15": 0.3546, "median_abs_gap": 10.71, "n": 40789}, "gen1_elo": {"share_ge_25": 0.1497, "share_ge_15": 0.3488, "median_abs_gap": 10.5, "n": 40789}, "gen1_sr": {"share_ge_25": 0.214, "share_ge_15": 0.439, "median_abs_gap": 12.98, "n": 40792}, "gen2": {"share_ge_25": 0.2293, "share_ge_15": 0.4386, "median_abs_gap": 12.82, "n": 40793}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.47, "share_ge_25_all": 0.0369, "share_ge_25_pregame_clean": 0.0309}, "WTA": {"median_abs_gap_pregame_clean": 7.69, "share_ge_25_all": 0.0591, "share_ge_25_pregame_clean": 0.0503}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2339, "share_within_10pp_all": 0.4351, "share_within_10pp_pregame_clean": 0.4907, "corr_model_vs_mid_pregame_clean": 0.8499}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1196, "model_brier": 0.1959, "kalshi_brier": 0.1959, "brier_diff_model_minus_kalshi": -0.0}, "10-15": {"n_settled": 1447, "model_brier": 0.2207, "kalshi_brier": 0.211, "brier_diff_model_minus_kalshi": 0.0097}, "15-25": {"n_settled": 1844, "model_brier": 0.2255, "kalshi_brier": 0.2073, "brier_diff_model_minus_kalshi": 0.0181}, "25-40": {"n_settled": 1045, "model_brier": 0.2254, "kalshi_brier": 0.2037, "brier_diff_model_minus_kalshi": 0.0216}, "3-5": {"n_settled": 783, "model_brier": 0.2082, "kalshi_brier": 0.2075, "brier_diff_model_minus_kalshi": 0.0007}, "40+": {"n_settled": 214, "model_brier": 0.307, "kalshi_brier": 0.1666, "brier_diff_model_minus_kalshi": 0.1404}, "5-10": {"n_settled": 1793, "model_brier": 0.2024, "kalshi_brier": 0.2005, "brier_diff_model_minus_kalshi": 0.0019}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'NO_SKILL:gen2|WTA', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.561, "slope": 0.819, "slope_se": 0.028}, "kalshi_slope": {"intercept": 0.166, "slope": 1.06, "slope_se": 0.031}, "n": 8322}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.497, "slope": 0.864, "slope_se": 0.023}, "kalshi_slope": {"intercept": 0.151, "slope": 1.061, "slope_se": 0.026}, "n": 10642}, "NO_SKILL:gen2|WTA": {"n_settled": 349, "model_brier": 0.2503, "kalshi_brier": 0.2266, "brier_diff_model_minus_kalshi": 0.0238, "brier_diff_se": 0.0089, "corr_model_outcome": 0.2571, "corr_kalshi_outcome": 0.3077}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 723, "model_brier": 0.2982, "kalshi_brier": 0.2321, "brier_diff_model_minus_kalshi": 0.0661, "brier_diff_se": 0.0109, "corr_model_outcome": 0.1142, "corr_kalshi_outcome": 0.2785}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
