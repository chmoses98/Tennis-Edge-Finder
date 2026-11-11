# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-11T17:37Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 88,980): 0-3 14.0%, 3-5 9.5%, 5-10 20.1%, 10-15 15.2%, 15-25 19.2%, 25-40 13.7%, 40+ 8.3%; median gap 11.91 pp.
* **Where the extremes live**: 97.3% of >=25 pp gaps are off the ATP/WTA main tour (ITF 78.2%, Challenger 11.2%, doubles 6.4%). Main tour: ATP 3.7% and WTA 5.9% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 19,613): MARKET_ALREADY_SETTLED_WHEN_PRICED 35.0%, STALE_QUOTE 20.2%, BOOK_QUALITY 16.4%, POOR_DATA 9.1%, POSSIBLY_IN_PLAY_QUOTE 5.9%, IDENTITY_AMBIGUOUS 4.2%, IN_PLAY_QUOTE 3.4%, LIMITED_DATA 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 1.8%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 35.0%, market_freshness 20.2%, execution 16.4%, data 12.4%, market_freshness/coverage 9.3%, mapping 4.2%, model_calibration_or_unknown 1.8%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 55.4% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 44.3% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 19,613 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.7% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.9%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.9% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 476.0 points vs 1682.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.023, Gen-2 0.818, Gen-1 ledger 0.869 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 1000 model 0.2253 vs Kalshi 0.2027; n 207 model 0.3061 vs Kalshi 0.1699.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 371,693 model-market comparisons (613,824 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 122,381 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-11T17:14:56.490480+00:00'], shadow board 103,064 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-11T17:15:01.596265+00:00'], Model 4 43,986 rows, 30,671 settled tickers, 11,651 tickers with an external scan.
* By model: {"gen1_ledger": 82013, "gen1_elo": 51793, "fair_v1": 51793, "gen2": 51793, "gen1_sr": 51793, "model4_fundamental": 41296, "model4_conditioned": 41212}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 88,980 | 14.0 | 9.5 | 20.1 | 15.2 | 19.2 | 13.7 | 8.3 | 11.91 | 41.2% | 22.0% |
| MW fair_v1 | 51,793 | 12.6 | 8.6 | 18.7 | 15.2 | 19.6 | 15.0 | 10.3 | 13.15 | 44.8% | 25.3% |
| MW gen1_elo | 51,793 | 12.4 | 8.7 | 19.2 | 15.3 | 19.4 | 15.0 | 10.1 | 12.99 | 44.5% | 25.1% |
| MW gen1_ledger | 37,187 | 15.8 | 10.8 | 22.1 | 15.1 | 18.6 | 12.0 | 5.6 | 10.29 | 36.1% | 17.5% |
| MW gen1_sr | 51,793 | 9.9 | 7.2 | 16.6 | 13.9 | 20.9 | 18.7 | 12.8 | 15.96 | 52.4% | 31.6% |
| MW gen2 | 51,793 | 10.9 | 7.5 | 16.6 | 13.8 | 19.7 | 17.7 | 13.9 | 15.49 | 51.2% | 31.6% |
| all families model4_conditioned | 41,212 | 22.2 | 17.9 | 34.5 | 16.9 | 5.0 | 2.2 | 1.2 | 6.06 | 8.4% | 3.4% |
| all families model4_fundamental | 41,296 | 17.3 | 13.5 | 34.0 | 20.0 | 9.9 | 3.8 | 1.5 | 7.61 | 15.2% | 5.3% |

Configurable thresholds (primary): >=5pp 76.5%, >=10pp 56.4%, >=15pp 41.2%, >=20pp 30.4%, >=25pp 22.0%, >=30pp 15.9%, >=40pp 8.3%, >=50pp 3.9%
Executable gap (model outside the book, before fees): median 8.55pp; >=10pp 45.6%, >=25pp 17.5%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,105 | 28.0 | 15.9 | 28.0 | 13.2 | 10.7 | 3.6 | 0.6 | 5.77 | 14.9% | 4.2% |
| CHALLENGER | 8,192 | 16.4 | 9.6 | 20.5 | 15.2 | 15.8 | 11.4 | 11.1 | 10.93 | 38.3% | 22.5% |
| ITF_MEN | 15,023 | 9.6 | 7.3 | 17.0 | 14.9 | 21.1 | 17.2 | 12.8 | 15.45 | 51.1% | 30.1% |
| ITF_WOMEN | 20,048 | 9.4 | 7.0 | 16.1 | 14.7 | 22.1 | 18.6 | 12.0 | 15.99 | 52.7% | 30.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,092 | 16.7 | 13.3 | 25.0 | 20.6 | 16.6 | 6.7 | 1.1 | 8.56 | 24.3% | 7.8% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,105 | 26.4 | 15.6 | 26.3 | 15.7 | 11.2 | 3.9 | 0.8 | 6.09 | 15.9% | 4.7% |
| CHALLENGER | 8,192 | 14.4 | 9.1 | 19.0 | 13.8 | 18.4 | 13.7 | 11.5 | 12.5 | 43.6% | 25.2% |
| ITF_MEN | 15,023 | 8.1 | 6.1 | 15.0 | 14.0 | 20.3 | 20.0 | 16.5 | 17.87 | 56.8% | 36.5% |
| ITF_WOMEN | 20,048 | 7.8 | 5.9 | 14.2 | 12.7 | 20.7 | 21.1 | 17.6 | 19.1 | 59.5% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,092 | 14.2 | 10.4 | 21.7 | 16.2 | 22.4 | 12.7 | 2.5 | 11.18 | 37.6% | 15.2% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,105 | 23.4 | 14.1 | 25.6 | 15.4 | 14.4 | 6.0 | 1.1 | 7.04 | 21.5% | 7.1% |
| CHALLENGER | 8,192 | 15.0 | 9.6 | 20.8 | 15.6 | 16.1 | 12.0 | 10.9 | 11.3 | 39.0% | 22.9% |
| ITF_MEN | 15,023 | 9.3 | 7.2 | 17.1 | 14.2 | 21.5 | 17.4 | 13.2 | 15.84 | 52.1% | 30.5% |
| ITF_WOMEN | 20,048 | 9.2 | 6.8 | 16.3 | 15.6 | 22.1 | 18.6 | 11.3 | 15.7 | 52.0% | 30.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,092 | 22.5 | 17.2 | 31.9 | 15.3 | 8.9 | 3.3 | 1.0 | 6.12 | 13.2% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,476 | 28.2 | 19.5 | 29.1 | 12.1 | 8.1 | 2.5 | 0.4 | 5.24 | 11.1% | 3.0% |
| CHALLENGER | 4,957 | 22.7 | 14.5 | 28.0 | 14.7 | 13.1 | 5.5 | 1.5 | 7.03 | 20.1% | 7.0% |
| DOUBLES | 2,717 | 4.9 | 4.5 | 13.0 | 11.0 | 20.6 | 24.5 | 21.6 | 23.06 | 66.6% | 46.1% |
| ITF_MEN | 10,897 | 12.7 | 9.4 | 21.4 | 15.6 | 21.8 | 13.0 | 6.1 | 11.87 | 40.9% | 19.1% |
| ITF_WOMEN | 12,920 | 13.5 | 9.3 | 19.7 | 15.7 | 21.6 | 14.7 | 5.5 | 12.2 | 41.7% | 20.1% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,815 | 24.1 | 16.0 | 31.5 | 16.9 | 8.9 | 2.5 | 0.2 | 6.44 | 11.6% | 2.8% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,976 | 28.5 | 16.1 | 28.4 | 13.2 | 10.4 | 3.1 | 0.3 | 5.64 | 13.8% | 3.4% |
| CHALLENGER | 5,757 | 21.2 | 12.0 | 25.7 | 17.9 | 15.8 | 5.7 | 1.8 | 8.19 | 23.2% | 7.4% |
| ITF_MEN | 10,948 | 11.8 | 8.6 | 20.6 | 17.2 | 22.2 | 14.0 | 5.5 | 12.48 | 41.7% | 19.6% |
| ITF_WOMEN | 14,646 | 11.3 | 8.6 | 19.1 | 17.1 | 24.0 | 15.3 | 4.7 | 13.14 | 44.0% | 20.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,978 | 17.0 | 13.4 | 25.4 | 21.0 | 16.6 | 6.2 | 0.6 | 8.42 | 23.3% | 6.8% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,976 | 26.7 | 16.0 | 26.6 | 15.7 | 11.1 | 3.5 | 0.4 | 6.01 | 15.0% | 3.8% |
| CHALLENGER | 5,757 | 18.2 | 11.6 | 23.9 | 16.3 | 18.9 | 9.1 | 2.0 | 8.97 | 30.0% | 11.1% |
| ITF_MEN | 10,949 | 9.6 | 7.2 | 17.5 | 16.1 | 22.2 | 18.1 | 9.1 | 14.85 | 49.5% | 27.2% |
| ITF_WOMEN | 14,647 | 8.9 | 7.0 | 16.1 | 14.2 | 22.5 | 20.6 | 10.7 | 16.51 | 53.8% | 31.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,978 | 14.4 | 10.5 | 21.9 | 16.4 | 22.6 | 12.4 | 1.9 | 11.03 | 36.8% | 14.3% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,406 | 28.5 | 19.7 | 29.1 | 12.3 | 7.8 | 2.3 | 0.3 | 5.19 | 10.4% | 2.7% |
| CHALLENGER | 4,384 | 24.0 | 15.4 | 29.2 | 14.8 | 12.4 | 3.8 | 0.4 | 6.58 | 16.6% | 4.2% |
| DOUBLES | 2,546 | 4.8 | 4.5 | 13.2 | 11.0 | 20.4 | 24.4 | 21.6 | 22.95 | 66.5% | 46.0% |
| ITF_MEN | 9,414 | 13.5 | 9.9 | 22.8 | 16.1 | 21.9 | 11.5 | 4.2 | 11.04 | 37.6% | 15.7% |
| ITF_WOMEN | 11,119 | 14.2 | 9.8 | 20.8 | 16.2 | 21.7 | 13.6 | 3.7 | 11.42 | 39.0% | 17.2% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,752 | 24.4 | 16.4 | 31.4 | 16.8 | 8.8 | 2.0 | 0.1 | 6.42 | 10.9% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,717 | 4.9 | 4.5 | 13.0 | 11.0 | 20.6 | 24.5 | 21.6 | 23.06 | 66.6% | 46.1% |
| singles | 34,470 | 16.7 | 11.3 | 22.9 | 15.4 | 18.5 | 11.0 | 4.3 | 9.77 | 33.7% | 15.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 11,035 | 12.7 | 8.9 | 19.4 | 15.2 | 19.6 | 14.4 | 9.8 | 12.89 | 43.8% | 24.1% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 33,766 | 13.1 | 8.7 | 18.8 | 15.0 | 19.1 | 15.0 | 10.2 | 12.98 | 44.4% | 25.2% |
| UNKNOWN | 6,579 | 10.4 | 7.5 | 17.1 | 16.5 | 21.5 | 15.8 | 11.2 | 14.35 | 48.6% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 14,487 | 19.2 | 11.8 | 22.4 | 15.8 | 14.8 | 9.5 | 6.5 | 9.0 | 30.7% | 16.0% |
| B | 6,217 | 13.0 | 8.5 | 19.6 | 15.3 | 19.6 | 12.4 | 11.5 | 12.74 | 43.6% | 23.9% |
| C | 7,309 | 12.0 | 8.6 | 19.5 | 16.1 | 18.9 | 14.5 | 10.4 | 12.89 | 43.8% | 24.9% |
| D | 8,455 | 11.4 | 8.3 | 17.9 | 15.0 | 21.9 | 15.7 | 9.8 | 14.05 | 47.4% | 25.4% |
| F | 15,325 | 7.3 | 5.7 | 14.9 | 14.4 | 23.0 | 21.1 | 13.6 | 18.01 | 57.8% | 34.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,806 | 25.0 | 15.9 | 28.9 | 14.8 | 10.7 | 3.5 | 1.2 | 6.35 | 15.3% | 4.7% |
| B | 5,073 | 16.7 | 10.9 | 24.2 | 16.9 | 18.9 | 9.4 | 3.0 | 9.6 | 31.3% | 12.4% |
| C | 7,301 | 11.0 | 7.8 | 19.6 | 14.9 | 21.0 | 15.5 | 10.1 | 13.46 | 46.7% | 25.6% |
| D | 5,642 | 14.5 | 10.0 | 21.1 | 15.3 | 20.9 | 12.7 | 5.5 | 11.32 | 39.1% | 18.2% |
| F | 9,365 | 10.2 | 8.3 | 16.5 | 14.5 | 23.5 | 19.0 | 8.0 | 15.28 | 50.5% | 27.0% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 16,430 | 17.7 | 10.9 | 21.4 | 15.5 | 15.1 | 10.2 | 9.2 | 10.0 | 34.5% | 19.4% |
| LIMITED | 11,186 | 13.5 | 9.5 | 20.5 | 16.1 | 19.6 | 13.3 | 7.6 | 11.91 | 40.5% | 20.9% |
| POOR | 24,177 | 8.8 | 6.6 | 16.1 | 14.6 | 22.6 | 19.1 | 12.3 | 16.37 | 53.9% | 31.3% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,258 | 23.7 | 18.1 | 33.0 | 15.4 | 6.4 | 3.0 | 0.4 | 5.9 | 9.8% | 3.4% |
| GAME_SPREAD | 6,924 | 22.8 | 15.3 | 32.1 | 16.7 | 9.1 | 3.3 | 0.7 | 6.69 | 13.1% | 4.0% |
| MATCH_WINNER | 37,187 | 15.8 | 10.8 | 22.1 | 15.1 | 18.6 | 12.0 | 5.6 | 10.29 | 36.1% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 17,028 | 28.4 | 16.8 | 30.6 | 12.7 | 8.9 | 2.3 | 0.3 | 5.57 | 11.5% | 2.6% |
| TOTAL_GAMES | 11,592 | 9.7 | 10.8 | 36.3 | 25.7 | 10.4 | 4.2 | 2.9 | 9.14 | 17.5% | 7.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,658 | 24.5 | 28.7 | 33.3 | 8.1 | 4.0 | 1.2 | 0.3 | 4.8 | 5.4% | 1.5% |
| GAME_SPREAD | 9,534 | 46.7 | 15.9 | 25.1 | 7.4 | 2.4 | 1.9 | 0.6 | 3.33 | 4.9% | 2.5% |
| TOTAL_GAMES | 17,020 | 6.6 | 9.8 | 40.8 | 29.9 | 7.3 | 3.3 | 2.4 | 9.16 | 12.9% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,694 | 23.8 | 16.6 | 34.6 | 14.8 | 6.9 | 2.7 | 0.5 | 6.05 | 10.1% | 3.2% |
| GAME_SPREAD | 9,543 | 20.4 | 13.4 | 28.4 | 20.2 | 12.1 | 4.4 | 1.1 | 7.7 | 17.6% | 5.5% |
| TOTAL_GAMES | 17,059 | 10.0 | 10.8 | 36.6 | 24.3 | 11.3 | 4.4 | 2.6 | 9.02 | 18.3% | 7.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 51,793 | 44.8% | 25.3% | 13.15 | 35.5% | 15.2% | 10.71 |
| gen1_elo | 51,793 | 44.5% | 25.1% | 12.99 | 35.0% | 15.0% | 10.51 |
| gen1_sr | 51,793 | 52.4% | 31.6% | 15.96 | 44.0% | 21.6% | 13.0 |
| gen2 | 51,793 | 51.2% | 31.6% | 15.49 | 43.9% | 23.0% | 12.83 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,229 | 15.5 | 10.5 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 31,564 | 10.8 | 7.4 | 17.0 | 13.9 | 19.2 | 17.0 | 14.7 | 15.37 | 50.9% | 31.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 30,655 | 16.4 | 11.1 | 22.7 | 15.2 | 18.2 | 11.5 | 5.0 | 9.96 | 34.7% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 88,980 | 30655 | 23701 | 34624 | 25.2 | 140.6 | 1451.1 |
| ge_15pp | 36,662 | 10640 | 8447 | 17575 | 29.0 | 444.1 | 1451.1 |
| ge_25pp | 19,613 | 5055 | 3694 | 10864 | 34.5 | 592.5 | 1431.1 |
| lt_10pp | 38,817 | 15361 | 11206 | 12250 | 22.8 | 49.7 | 1421.7 |

Current slate `SL-20261111T173729Z-17e8d6bd`: 335 priced rows, quote age at build {'median': 53.3, 'max': 63.3}, freshness {'STALE': 335}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 52 | 0.0 | 0.0 | 34.6 | 9.6 | 32.7 | 19.2 | 3.9 | 18.34 | 55.8% | 23.1% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 5,027 | 19.2 | 11.1 | 25.6 | 18.2 | 17.8 | 7.2 | 1.0 | 8.78 | 25.9% | 8.2% |
| KALSHI_LONE_OUTLIER | 32 | 6.2 | 6.2 | 75.0 | 6.2 | 3.1 | 3.1 | 0.0 | 6.16 | 6.2% | 3.1% |
| MARKETS_AGREE | 1,075 | 66.3 | 33.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,286 | 0.0 | 2.2 | 38.5 | 25.9 | 23.8 | 8.8 | 0.9 | 11.65 | 33.5% | 9.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 51,793 | 8501 (16.4%) | 26.9% | 1.0% | {"EXTERNAL_STALE": 5027, "AGREES_WITH_KALSHI": 2286, "ALL_AGREE": 1075, "SUPPORTS_MODEL_DIRECTION": 50, "AGREES_WITH_MODEL": 32, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 23,223 | 2099 (9.0%) | 36.4% | 1.5% | {"EXTERNAL_STALE": 1303, "AGREES_WITH_KALSHI": 765, "SUPPORTS_MODEL_DIRECTION": 29, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 13,096 | 645 (4.9%) | 34.4% | 2.0% | {"EXTERNAL_STALE": 410, "AGREES_WITH_KALSHI": 222, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 6,006 | 614 (10.2%) | 35.0% | 2.1% | {"EXTERNAL_STALE": 386, "AGREES_WITH_KALSHI": 215, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 20,687 | 4888 (23.6%) | 19.0% | 0.9% | {"EXTERNAL_STALE": 2808, "ALL_AGREE": 1075, "AGREES_WITH_KALSHI": 930, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 28, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 10,153 | 10.7 | 7.5 | 19.1 | 14.3 | 21.7 | 16.4 | 10.2 | 14.32 | 48.4% | 26.7% |
| 4-10x | 6,957 | 11.1 | 8.7 | 17.8 | 14.8 | 21.7 | 14.7 | 11.2 | 14.1 | 47.6% | 25.9% |
| <2x | 26,397 | 14.6 | 9.6 | 19.9 | 16.0 | 17.5 | 13.3 | 9.1 | 11.63 | 39.9% | 22.4% |
| >=10x | 8,286 | 10.1 | 6.5 | 15.1 | 14.3 | 21.7 | 19.0 | 13.3 | 16.52 | 54.0% | 32.3% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 13,583 | 12.4 | 8.5 | 19.8 | 16.1 | 19.0 | 13.7 | 10.5 | 12.78 | 43.2% | 24.2% |
| 300-1000 | 11,217 | 11.7 | 8.6 | 17.9 | 15.1 | 20.7 | 16.3 | 9.8 | 13.83 | 46.8% | 26.1% |
| <300 | 16,435 | 8.1 | 5.9 | 15.0 | 14.5 | 22.9 | 20.1 | 13.6 | 17.47 | 56.5% | 33.7% |
| >=3000 | 10,558 | 21.1 | 12.8 | 24.0 | 15.4 | 13.9 | 7.4 | 5.3 | 7.84 | 26.7% | 12.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1584 | 0.5479 | 0.4081 | 0.4785 | +0.069 | -0.070 | 0.0035 ± 0.0039 |
| ratio 4-10x | 1081 | 0.5739 | 0.4287 | 0.4829 | +0.091 | -0.054 | 0.0104 ± 0.0049 |
| ratio <2x | 3879 | 0.5354 | 0.4129 | 0.4328 | +0.103 | -0.020 | 0.015 ± 0.0023 |
| ratio >=10x | 1331 | 0.5608 | 0.3876 | 0.435 | +0.126 | -0.047 | 0.0186 ± 0.0049 |
| thinner_sample 1000-3000 | 2172 | 0.5393 | 0.4121 | 0.4438 | +0.096 | -0.032 | 0.0129 ± 0.0031 |
| thinner_sample 300-1000 | 1777 | 0.5621 | 0.4219 | 0.4682 | +0.094 | -0.046 | 0.0064 ± 0.0037 |
| thinner_sample <300 | 2576 | 0.5548 | 0.3869 | 0.4449 | +0.110 | -0.058 | 0.0156 ± 0.0035 |
| thinner_sample >=3000 | 1350 | 0.5273 | 0.434 | 0.4415 | +0.086 | -0.007 | 0.0151 ± 0.0031 |
| data_status ADEQUATE | 2149 | 0.5311 | 0.4287 | 0.4369 | +0.094 | -0.008 | 0.0159 ± 0.0026 |
| data_status LIMITED | 1918 | 0.5476 | 0.4146 | 0.4625 | +0.085 | -0.048 | 0.0084 ± 0.0034 |
| data_status POOR | 3808 | 0.5567 | 0.3967 | 0.4496 | +0.107 | -0.053 | 0.013 ± 0.0028 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1140 | 0.1972 | 0.1972 | -0.0001 ± 0.0005 | 0.5741 | 0.5744 | 0.503 | 0.4877 | 0.4956 | -0.098 ± 0.0139 | -0.0087 (8) |
| 3-5 | 725 | 0.2071 | 0.2065 | +0.0006 ± 0.0014 | 0.5999 | 0.5967 | 0.5011 | 0.4614 | 0.4731 | -0.102 ± 0.0173 | 0.01 (3) |
| 5-10 | 1687 | 0.2038 | 0.2021 | +0.0016 ± 0.0016 | 0.5944 | 0.5881 | 0.5101 | 0.4362 | 0.4606 | -0.093 ± 0.0113 | -0.0143 (7) |
| 10-15 | 1369 | 0.2184 | 0.2092 | +0.0093 ± 0.0031 | 0.6285 | 0.6018 | 0.5243 | 0.401 | 0.4237 | -0.106 ± 0.0126 | -0.055 (6) |
| 15-25 | 1747 | 0.2253 | 0.2064 | +0.0190 ± 0.0042 | 0.6456 | 0.5955 | 0.5727 | 0.3781 | 0.4264 | -0.104 ± 0.011 | -0.0045 (11) |
| 25-40 | 1000 | 0.2253 | 0.2027 | +0.0226 ± 0.0085 | 0.6411 | 0.5852 | 0.6454 | 0.3359 | 0.454 | -0.069 ± 0.0132 | -0.06 (2) |
| 40+ | 207 | 0.3061 | 0.1699 | +0.1362 ± 0.026 | 0.819 | 0.5099 | 0.7265 | 0.2687 | 0.3575 | -0.086 ± 0.0252 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5816 | 0.187 | 0.1879 | -0.0009 ± 0.0002 | 0.5505 | 0.5516 | 0.4913 | 0.476 | 0.5084 | -0.020 ± 0.0058 | -0.01 (28) |
| 3-5 | 3901 | 0.1994 | 0.1974 | +0.0020 ± 0.0006 | 0.58 | 0.5731 | 0.4812 | 0.4414 | 0.4358 | -0.060 ± 0.0072 | 0.005 (6) |
| 5-10 | 8548 | 0.2016 | 0.1973 | +0.0043 ± 0.0007 | 0.5891 | 0.5754 | 0.483 | 0.4092 | 0.4172 | -0.050 ± 0.0049 | -0.0114 (22) |
| 10-15 | 6988 | 0.2016 | 0.1856 | +0.0160 ± 0.0013 | 0.5898 | 0.5451 | 0.4852 | 0.3613 | 0.3588 | -0.064 ± 0.0052 | -0.0379 (19) |
| 15-25 | 8955 | 0.2057 | 0.166 | +0.0396 ± 0.0017 | 0.6031 | 0.494 | 0.4977 | 0.3021 | 0.2994 | -0.069 ± 0.0043 | -0.0043 (51) |
| 25-40 | 7047 | 0.2232 | 0.1236 | +0.0996 ± 0.0026 | 0.6406 | 0.3812 | 0.5243 | 0.2104 | 0.2126 | -0.060 ± 0.0041 | -0.0733 (3) |
| 40+ | 4804 | 0.381 | 0.0439 | +0.3371 ± 0.0034 | 0.9922 | 0.1703 | 0.6287 | 0.1012 | 0.0572 | -0.075 ± 0.0029 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 910 | 0.2036 | 0.2039 | -0.0003 ± 0.0005 | 0.5875 | 0.5886 | 0.5078 | 0.4929 | 0.5187 | -0.096 ± 0.016 | -0.0117 (6) |
| 3-5 | 654 | 0.213 | 0.2101 | +0.0029 ± 0.0014 | 0.6098 | 0.6035 | 0.5156 | 0.476 | 0.4572 | -0.128 ± 0.0193 | 0.01 (3) |
| 5-10 | 1460 | 0.2057 | 0.204 | +0.0018 ± 0.0018 | 0.5974 | 0.5927 | 0.539 | 0.4645 | 0.4918 | -0.087 ± 0.0122 | -0.01 (4) |
| 10-15 | 1271 | 0.2142 | 0.2069 | +0.0073 ± 0.0032 | 0.6212 | 0.5992 | 0.5586 | 0.4342 | 0.4697 | -0.103 ± 0.0133 | -0.04 (5) |
| 15-25 | 1833 | 0.2317 | 0.2107 | +0.0210 ± 0.0042 | 0.6595 | 0.6052 | 0.5852 | 0.3895 | 0.4354 | -0.102 ± 0.011 | -0.0183 (12) |
| 25-40 | 1279 | 0.2668 | 0.2 | +0.0668 ± 0.0078 | 0.7439 | 0.5805 | 0.6598 | 0.3459 | 0.3987 | -0.112 ± 0.0126 | -0.008 (5) |
| 40+ | 468 | 0.3744 | 0.1584 | +0.2160 ± 0.0184 | 1.0178 | 0.4811 | 0.7319 | 0.2433 | 0.2799 | -0.091 ± 0.0178 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4979 | 0.1902 | 0.1904 | -0.0002 ± 0.0002 | 0.5555 | 0.5556 | 0.5075 | 0.4923 | 0.5065 | -0.041 ± 0.0064 | -0.0154 (26) |
| 3-5 | 3432 | 0.1948 | 0.1939 | +0.0009 ± 0.0006 | 0.5669 | 0.5642 | 0.5107 | 0.471 | 0.4787 | -0.044 ± 0.0077 | 0.01 (5) |
| 5-10 | 7633 | 0.1962 | 0.1928 | +0.0034 ± 0.0008 | 0.5771 | 0.5643 | 0.5071 | 0.4329 | 0.4495 | -0.040 ± 0.0051 | -0.0117 (6) |
| 10-15 | 6355 | 0.2023 | 0.1904 | +0.0119 ± 0.0014 | 0.5943 | 0.5574 | 0.5077 | 0.3837 | 0.3984 | -0.049 ± 0.0056 | -0.0189 (18) |
| 15-25 | 9033 | 0.2154 | 0.1785 | +0.0369 ± 0.0018 | 0.6275 | 0.5251 | 0.5237 | 0.3283 | 0.334 | -0.062 ± 0.0045 | -0.014 (52) |
| 25-40 | 8148 | 0.2508 | 0.1377 | +0.1131 ± 0.0026 | 0.7082 | 0.4201 | 0.5597 | 0.2423 | 0.2266 | -0.077 ± 0.0041 | -0.0095 (20) |
| 40+ | 6479 | 0.4023 | 0.0591 | +0.3432 ± 0.0035 | 1.06 | 0.2128 | 0.6546 | 0.1187 | 0.0801 | -0.073 ± 0.003 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1113 | 0.1954 | 0.1965 | -0.0011 ± 0.0005 | 0.5702 | 0.5729 | 0.5008 | 0.4854 | 0.5238 | -0.060 ± 0.0139 | -0.0191 (11) |
| 3-5 | 791 | 0.2092 | 0.2076 | +0.0016 ± 0.0013 | 0.6055 | 0.6002 | 0.4975 | 0.4579 | 0.4589 | -0.112 ± 0.0169 | 0.002 (5) |
| 5-10 | 1696 | 0.2038 | 0.1996 | +0.0042 ± 0.0016 | 0.5933 | 0.5817 | 0.5113 | 0.4376 | 0.4458 | -0.107 ± 0.0112 | -0.01 (10) |
| 10-15 | 1410 | 0.212 | 0.2027 | +0.0093 ± 0.003 | 0.6143 | 0.5877 | 0.5381 | 0.415 | 0.4404 | -0.106 ± 0.0121 | -0.0286 (7) |
| 15-25 | 1663 | 0.2307 | 0.2116 | +0.0191 ± 0.0044 | 0.6586 | 0.6071 | 0.5821 | 0.388 | 0.4354 | -0.106 ± 0.0113 | -0.03 (1) |
| 25-40 | 984 | 0.217 | 0.2065 | +0.0105 ± 0.0086 | 0.6239 | 0.5939 | 0.6536 | 0.3435 | 0.4797 | -0.061 ± 0.0133 | -0.0267 (3) |
| 40+ | 218 | 0.314 | 0.1776 | +0.1364 ± 0.0258 | 0.8455 | 0.5261 | 0.7381 | 0.2805 | 0.3716 | -0.084 ± 0.0263 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5607 | 0.1856 | 0.1861 | -0.0005 ± 0.0002 | 0.5468 | 0.5472 | 0.4864 | 0.471 | 0.4856 | -0.037 ± 0.0058 | -0.0189 (44) |
| 3-5 | 4016 | 0.2055 | 0.2036 | +0.0019 ± 0.0006 | 0.5964 | 0.5901 | 0.4815 | 0.4419 | 0.4382 | -0.058 ± 0.0072 | -0.0073 (22) |
| 5-10 | 8689 | 0.1964 | 0.1911 | +0.0053 ± 0.0007 | 0.5764 | 0.5597 | 0.4862 | 0.4123 | 0.4129 | -0.056 ± 0.0047 | -0.0117 (42) |
| 10-15 | 6997 | 0.195 | 0.1797 | +0.0153 ± 0.0013 | 0.5751 | 0.5315 | 0.4962 | 0.3729 | 0.3723 | -0.062 ± 0.0051 | -0.0136 (14) |
| 15-25 | 8996 | 0.2108 | 0.1716 | +0.0392 ± 0.0017 | 0.615 | 0.5065 | 0.5096 | 0.3149 | 0.3122 | -0.069 ± 0.0044 | -0.0533 (3) |
| 25-40 | 7027 | 0.2176 | 0.1234 | +0.0942 ± 0.0026 | 0.6285 | 0.3801 | 0.5259 | 0.2103 | 0.2206 | -0.053 ± 0.0041 | -0.02 (4) |
| 40+ | 4727 | 0.3894 | 0.0479 | +0.3415 ± 0.0036 | 1.0147 | 0.1805 | 0.6376 | 0.1067 | 0.0633 | -0.076 ± 0.0031 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1584 | 0.1962 | 0.1959 | +0.0003 ± 0.0004 | 0.5707 | 0.5698 | 0.5082 | 0.4931 | 0.4912 | -0.075 ± 0.0114 | -0.0221 (56) |
| 3-5 | 1108 | 0.1889 | 0.1889 | +0.0000 ± 0.0011 | 0.5555 | 0.5538 | 0.4985 | 0.4586 | 0.4765 | -0.056 ± 0.0134 | -0.0194 (34) |
| 5-10 | 2242 | 0.1997 | 0.1947 | +0.0050 ± 0.0014 | 0.589 | 0.5728 | 0.5075 | 0.4338 | 0.4371 | -0.077 ± 0.0095 | -0.005 (78) |
| 10-15 | 1557 | 0.2153 | 0.2021 | +0.0133 ± 0.0028 | 0.6247 | 0.5873 | 0.5437 | 0.421 | 0.4271 | -0.093 ± 0.0117 | 0.0012 (66) |
| 15-25 | 2033 | 0.2315 | 0.2076 | +0.0239 ± 0.004 | 0.6608 | 0.599 | 0.5911 | 0.3961 | 0.4333 | -0.090 ± 0.0102 | -0.0214 (59) |
| 25-40 | 1198 | 0.2412 | 0.2108 | +0.0304 ± 0.0081 | 0.6886 | 0.6044 | 0.6884 | 0.3768 | 0.4841 | -0.085 ± 0.0125 | -0.0252 (27) |
| 40+ | 438 | 0.326 | 0.198 | +0.1280 ± 0.0203 | 0.9337 | 0.5773 | 0.8108 | 0.3348 | 0.4543 | -0.094 ± 0.019 | -0.1137 (8) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5737 | 0.1766 | 0.1766 | +0.0000 ± 0.0002 | 0.5233 | 0.5227 | 0.5104 | 0.4951 | 0.5018 | -0.042 ± 0.0056 | -0.0154 (103) |
| 3-5 | 3930 | 0.1942 | 0.1933 | +0.0008 ± 0.0006 | 0.5668 | 0.5643 | 0.5024 | 0.4626 | 0.472 | -0.040 ± 0.0071 | -0.0212 (73) |
| 5-10 | 8010 | 0.1972 | 0.1907 | +0.0064 ± 0.0007 | 0.5816 | 0.562 | 0.5023 | 0.4287 | 0.4227 | -0.061 ± 0.0049 | -0.0084 (134) |
| 10-15 | 5497 | 0.2104 | 0.1936 | +0.0168 ± 0.0015 | 0.6126 | 0.5679 | 0.5364 | 0.4136 | 0.4051 | -0.074 ± 0.006 | -0.0057 (111) |
| 15-25 | 6773 | 0.2312 | 0.199 | +0.0322 ± 0.0021 | 0.6647 | 0.5773 | 0.5759 | 0.3804 | 0.396 | -0.068 ± 0.0055 | -0.026 (108) |
| 25-40 | 4367 | 0.2572 | 0.1904 | +0.0668 ± 0.0041 | 0.7272 | 0.5543 | 0.6397 | 0.3276 | 0.3799 | -0.062 ± 0.0065 | -0.0277 (53) |
| 40+ | 1968 | 0.368 | 0.1597 | +0.2084 ± 0.0093 | 1.0359 | 0.4754 | 0.7412 | 0.2419 | 0.2932 | -0.058 ± 0.0086 | -0.054 (15) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 7875 | 1.023 ± 0.031 | 1.095 | 0.1677 | 0.1696 | 0.2159 | 0.2032 |
| gen2 | 7875 | 0.818 ± 0.028 | 1.072 | 0.1737 | 0.1699 | 0.2334 | 0.2032 |
| gen1_elo | 7875 | 1.007 ± 0.031 | 1.085 | 0.1741 | 0.1698 | 0.215 | 0.2033 |
| gen1_sr | 7875 | 1.004 ± 0.037 | 1.121 | 0.1335 | 0.1714 | 0.2296 | 0.2029 |
| gen1_ledger | 10160 | 0.869 ± 0.023 | 1.071 | 0.1897 | 0.1763 | 0.2171 | 0.2 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 36,662)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 8,870 | 24.2% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 8,517 | 23.2% |
| BOOK_QUALITY | execution | 6,252 | 17.1% |
| POOR_DATA | data | 4,201 | 11.5% |
| LIMITED_DATA | data | 2,204 | 6.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 2,124 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 1,492 | 4.1% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,406 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 1,022 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 573 | 1.6% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 24.2%, coverage 23.2%, data 17.5%, execution 17.1%, market_freshness/coverage 8.6%, mapping 4.1%, model_calibration_or_unknown 3.8%, model_calibration 1.6%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.6%, START_UNVERIFIABLE 95.0%, LOW_DATA_QUALITY 72.0%, THIN_PLAYER_HISTORY 60.2%, STALE_PLAYER_DATA 52.1%, STALE_KALSHI_QUOTE 47.9%, MODEL_INTERNAL_DISAGREEMENT 41.8%, ASYMMETRIC_SAMPLE_SIZE 33.2%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 15.0%, LEVEL_TRANSFER_RISK 9.5%, LOW_DISPLAYED_LIQUIDITY 8.5%, EVENT_MAPPING_RISK 6.9%, MODEL_CALIBRATION_OUTLIER 3.5%, EXTERNAL_MARKET_REJECTION 3.2%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.6%, POST_SETTLEMENT_OBSERVATION 23.2%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 19,613)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,868 | 35.0% |
| STALE_QUOTE | market_freshness | 3,955 | 20.2% |
| BOOK_QUALITY | execution | 3,223 | 16.4% |
| POOR_DATA | data | 1,786 | 9.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,149 | 5.9% |
| IDENTITY_AMBIGUOUS | mapping | 830 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 668 | 3.4% |
| LIMITED_DATA | data | 650 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 344 | 1.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 139 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 35.0%, market_freshness 20.2%, execution 16.4%, data 12.4%, market_freshness/coverage 9.3%, mapping 4.2%, model_calibration_or_unknown 1.8%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.1%, START_UNVERIFIABLE 97.3%, LOW_DATA_QUALITY 75.1%, THIN_PLAYER_HISTORY 62.3%, STALE_KALSHI_QUOTE 55.4%, STALE_PLAYER_DATA 45.5%, MODEL_INTERNAL_DISAGREEMENT 41.9%, ASYMMETRIC_SAMPLE_SIZE 34.4%, WIDE_SPREAD 22.6%, MODEL_HIGH_UNCERTAINTY 19.2%, PLAYER_IDENTITY_RISK 17.9%, LOW_DISPLAYED_LIQUIDITY 8.4%, EVENT_MAPPING_RISK 8.4%, LEVEL_TRANSFER_RISK 8.3%, MODEL_CALIBRATION_OUTLIER 4.6%, EXTERNAL_MARKET_REJECTION 1.8%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 38.0%, POST_SETTLEMENT_OBSERVATION 35.0%, POSSIBLE_IN_PLAY_QUOTE 6.3%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 15753, "IDENTITY_AMBIGUOUS": 3860}; ticker orientation: {"VERIFIED": 19613}.

Checks: discipline:AMBIGUOUS 1252, discipline:PASS 18361, identity_confidence:AMBIGUOUS 3520, identity_confidence:PASS 16093, level_mapping:NA 1264, level_mapping:PASS 18349, market_pair:AMBIGUOUS 504, market_pair:NA 423, market_pair:PASS 18686, model_complement:NA 385, model_complement:PASS 19228, namesake:AMBIGUOUS 6, namesake:PASS 19607, physical_match_id:NA 6517, physical_match_id:PASS 13096, player_ids:PASS 19613, same_pair_other_event:PASS 19613, ticker_orientation:PASS 19613

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,581 | 3.7% | 3.1% | 1.2% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 24, "market_freshness/coverage": 22} | 5.47 | 0.2215 / 0.2173 (857) | 25.6% | 2.4% | 3.2% | 3.0% |
| CHALLENGER | 13,149 | 16.6% | 6.0% | 11.2% | {"coverage": 1338, "market_freshness": 267, "market_freshness/coverage": 238, "data": 164, "model_calibration_or_unknown": 80, "execution": 41, "model_calibration": 40, "mapping": 17, "possible_market_error": 1} | 7.34 | 0.2213 / 0.2106 (3051) | 41.6% | 13.9% | 4.0% | 22.9% |
| DOUBLES | 2,717 | 46.1% | 46.0% | 6.4% | {"execution": 691, "mapping": 375, "market_freshness": 106, "market_freshness/coverage": 73, "coverage": 7} | 22.95 | 0.2983 / 0.2329 (678) | 8.6% | 0.0% | 100.0% | 6.3% |
| ITF_MEN | 25,920 | 25.4% | 17.8% | 33.6% | {"coverage": 2315, "market_freshness": 1376, "execution": 1033, "data": 974, "market_freshness/coverage": 662, "mapping": 224, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.79 | 0.2188 / 0.1988 (5441) | 42.0% | 70.1% | 14.7% | 21.4% |
| ITF_WOMEN | 32,968 | 26.5% | 18.8% | 44.6% | {"coverage": 3129, "market_freshness": 1945, "execution": 1375, "data": 1197, "market_freshness/coverage": 765, "mapping": 208, "model_calibration_or_unknown": 97, "model_calibration": 23} | 12.47 | 0.2029 / 0.1931 (6388) | 42.7% | 57.4% | 10.0% | 21.9% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,907 | 5.9% | 5.0% | 1.5% | {"market_freshness": 111, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.64 | 0.2308 / 0.2206 (808) | 30.3% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.5% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 113 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 519 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 21.5h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 1296 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 311 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 117 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFMATCH-26NOV10KOUPOR-POR` | ITF_MEN | fair_v1 | 87% / 2% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 80 min (STALE); data POOR (grade D, thinner serve sample 1554.0, ratio 1.02); no external reference |
| 12 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 13 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 15 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 21.3h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 1282 min (STALE); no external reference |
| 16 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 17 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 18 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 19 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 151 min (STALE); no external reference |
| 20 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 21 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 22 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 23 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 24 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 25 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 26 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 573 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 27 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 28 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 29 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 30 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 31 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 32 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 33 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 34 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 35 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 271 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 36 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 37 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 38 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 39 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 40 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 41 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 43 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 463 min (STALE); no external reference |
| 44 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 45 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 46 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 47 | `KXITFWMATCH-26NOV11CORROJ-ROJ` | ITF_WOMEN | fair_v1 | 87% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 434 min (STALE); data POOR (grade D, thinner serve sample 531.0, ratio 1.04); no external reference |
| 48 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 49 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 720 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9727, "by_level_share_of_ge_25pp": {"ATP": 0.0125, "CHALLENGER": 0.1115, "DOUBLES": 0.0638, "ITF_MEN": 0.3363, "ITF_WOMEN": 0.4456, "OTHER": 0.0006, "WTA": 0.0148, "WTA125": 0.0149}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5539, "share_primary_cause_market_settled_or_in_play": 0.4429, "share_primary_cause_stale_quote_only": 0.2017}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 19613, "identity_ambiguous_share": 0.1968, "ticker_orientation": {"VERIFIED": 19613}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 13096, "with_external": 645, "coverage": 0.0493, "external_status": {"EXTERNAL_STALE": 410, "AGREES_WITH_KALSHI": 222, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 410, "MODEL_LONE_OUTLIER": 222, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3442, "share_external_supports_model": 0.0202}, "pregame_clean_ge_25pp": {"n": 6006, "with_external": 614, "coverage": 0.1022, "external_status": {"EXTERNAL_STALE": 386, "AGREES_WITH_KALSHI": 215, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 386, "MODEL_LONE_OUTLIER": 215, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3502, "share_external_supports_model": 0.0212}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 476.0, "median_sample_ratio": 2.44, "median_min_matches": 18.0, "median_max_days_since_last": 246.0, "share_severe_asymmetry": 0.2074, "data_status": {"POOR": 11166, "LIMITED": 4914, "ADEQUATE": 3533}, "comparison_lt_10pp": {"median_thinner_serve_points": 1682.0, "median_sample_ratio": 1.71, "median_min_matches": 87.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1584, "model_minus_observed": 0.0693, "kalshi_minus_observed": -0.0704, "brier_diff_model_minus_kalshi": 0.0035}, "4-10x": {"n": 1081, "model_minus_observed": 0.091, "kalshi_minus_observed": -0.0542, "brier_diff_model_minus_kalshi": 0.0104}, "<2x": {"n": 3879, "model_minus_observed": 0.1026, "kalshi_minus_observed": -0.02, "brier_diff_model_minus_kalshi": 0.015}, ">=10x": {"n": 1331, "model_minus_observed": 0.1258, "kalshi_minus_observed": -0.0474, "brier_diff_model_minus_kalshi": 0.0186}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 7875, "model": {"intercept": -0.559, "slope": 0.818, "slope_se": 0.028}, "kalshi_mid_same_rows": {"intercept": 0.173, "slope": 1.072, "slope_se": 0.032}, "mean_extremity_model": 0.1737, "mean_extremity_kalshi": 0.1699, "model_brier": 0.2334, "kalshi_brier": 0.2032, "brier_diff_model_minus_kalshi": 0.0303, "brier_diff_se": 0.0021, "model_logloss": 0.6643, "kalshi_logloss": 0.5885}, "fair_v1": {"n": 7875, "model": {"intercept": -0.467, "slope": 1.023, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.222, "slope": 1.095, "slope_se": 0.032}, "mean_extremity_model": 0.1677, "mean_extremity_kalshi": 0.1696, "model_brier": 0.2159, "kalshi_brier": 0.2032, "brier_diff_model_minus_kalshi": 0.0127, "brier_diff_se": 0.0017, "model_logloss": 0.6211, "kalshi_logloss": 0.5885}, "gen1_elo": {"n": 7875, "model": {"intercept": -0.456, "slope": 1.007, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.223, "slope": 1.085, "slope_se": 0.032}, "mean_extremity_model": 0.1741, "mean_extremity_kalshi": 0.1698, "model_brier": 0.215, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.0117, "brier_diff_se": 0.0017, "model_logloss": 0.6196, "kalshi_logloss": 0.5887}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2529, "share_ge_15": 0.4484, "median_abs_gap": 13.15, "n": 51793}, "gen1_elo": {"share_ge_25": 0.2506, "share_ge_15": 0.4445, "median_abs_gap": 12.99, "n": 51793}, "gen1_sr": {"share_ge_25": 0.3155, "share_ge_15": 0.5241, "median_abs_gap": 15.96, "n": 51793}, "gen2": {"share_ge_25": 0.3155, "share_ge_15": 0.5121, "median_abs_gap": 15.49, "n": 51793}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1517, "share_ge_15": 0.3546, "median_abs_gap": 10.71, "n": 39589}, "gen1_elo": {"share_ge_25": 0.1501, "share_ge_15": 0.3497, "median_abs_gap": 10.51, "n": 39589}, "gen1_sr": {"share_ge_25": 0.2155, "share_ge_15": 0.4399, "median_abs_gap": 13.0, "n": 39591}, "gen2": {"share_ge_25": 0.2302, "share_ge_15": 0.4386, "median_abs_gap": 12.83, "n": 39591}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.47, "share_ge_25_all": 0.0372, "share_ge_25_pregame_clean": 0.0312}, "WTA": {"median_abs_gap_pregame_clean": 7.64, "share_ge_25_all": 0.0593, "share_ge_25_pregame_clean": 0.0503}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2348, "share_within_10pp_all": 0.4362, "share_within_10pp_pregame_clean": 0.4906, "corr_model_vs_mid_pregame_clean": 0.8495}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1140, "model_brier": 0.1972, "kalshi_brier": 0.1972, "brier_diff_model_minus_kalshi": -0.0001}, "10-15": {"n_settled": 1369, "model_brier": 0.2184, "kalshi_brier": 0.2092, "brier_diff_model_minus_kalshi": 0.0093}, "15-25": {"n_settled": 1747, "model_brier": 0.2253, "kalshi_brier": 0.2064, "brier_diff_model_minus_kalshi": 0.019}, "25-40": {"n_settled": 1000, "model_brier": 0.2253, "kalshi_brier": 0.2027, "brier_diff_model_minus_kalshi": 0.0226}, "3-5": {"n_settled": 725, "model_brier": 0.2071, "kalshi_brier": 0.2065, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 207, "model_brier": 0.3061, "kalshi_brier": 0.1699, "brier_diff_model_minus_kalshi": 0.1362}, "5-10": {"n_settled": 1687, "model_brier": 0.2038, "kalshi_brier": 0.2021, "brier_diff_model_minus_kalshi": 0.0016}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.559, "slope": 0.818, "slope_se": 0.028}, "kalshi_slope": {"intercept": 0.173, "slope": 1.072, "slope_se": 0.032}, "n": 7875}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.5, "slope": 0.869, "slope_se": 0.023}, "kalshi_slope": {"intercept": 0.155, "slope": 1.071, "slope_se": 0.027}, "n": 10160}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 678, "model_brier": 0.2983, "kalshi_brier": 0.2329, "brier_diff_model_minus_kalshi": 0.0654, "brier_diff_se": 0.0112, "corr_model_outcome": 0.1027, "corr_kalshi_outcome": 0.274}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
