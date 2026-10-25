# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-25T22:20Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 54,472): 0-3 13.9%, 3-5 9.5%, 5-10 19.8%, 10-15 15.4%, 15-25 19.3%, 25-40 14.0%, 40+ 8.2%; median gap 12.06 pp.
* **Where the extremes live**: 96.8% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.0%, Challenger 12.0%, doubles 7.1%). Main tour: ATP 4.4% and WTA 5.4% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 12,060): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.4%, BOOK_QUALITY 18.8%, STALE_QUOTE 18.5%, POOR_DATA 8.5%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.4%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.4%, execution 18.8%, market_freshness 18.5%, data 12.0%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 51.9% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.3% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 12,060 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.4% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 490.5 points vs 1762.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.035, Gen-2 0.831, Gen-1 ledger 0.861 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 586 model 0.2216 vs Kalshi 0.2107; n 116 model 0.2743 vs Kalshi 0.202.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 238,465 model-market comparisons (386,068 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 80,510 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-25T22:04:35.853965+00:00'], shadow board 62,771 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-25T22:04:40.703137+00:00'], Model 4 30,393 rows, 20,617 settled tickers, 7,308 tickers with an external scan.
* By model: {"gen1_ledger": 55121, "gen1_elo": 31566, "fair_v1": 31566, "gen2": 31566, "gen1_sr": 31566, "model4_fundamental": 28562, "model4_conditioned": 28518}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 54,472 | 13.9 | 9.5 | 19.8 | 15.4 | 19.3 | 14.0 | 8.2 | 12.06 | 41.4% | 22.1% |
| MW fair_v1 | 31,566 | 12.8 | 8.6 | 18.5 | 15.6 | 19.8 | 14.9 | 9.8 | 13.14 | 44.5% | 24.8% |
| MW gen1_elo | 31,566 | 12.7 | 8.5 | 19.0 | 15.2 | 19.9 | 15.0 | 9.6 | 13.0 | 44.5% | 24.6% |
| MW gen1_ledger | 22,906 | 15.4 | 10.7 | 21.7 | 15.2 | 18.6 | 12.6 | 5.9 | 10.55 | 37.1% | 18.5% |
| MW gen1_sr | 31,566 | 10.2 | 7.1 | 16.8 | 13.6 | 20.8 | 18.7 | 12.9 | 15.99 | 52.3% | 31.6% |
| MW gen2 | 31,566 | 11.0 | 7.3 | 16.2 | 14.0 | 19.4 | 17.9 | 14.0 | 15.59 | 51.4% | 31.9% |
| all families model4_conditioned | 28,518 | 21.7 | 18.5 | 34.5 | 17.8 | 4.7 | 1.7 | 1.1 | 6.06 | 7.5% | 2.8% |
| all families model4_fundamental | 28,562 | 16.7 | 13.2 | 33.9 | 20.7 | 10.6 | 3.6 | 1.4 | 7.83 | 15.6% | 5.0% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.8%, >=15pp 41.4%, >=20pp 30.8%, >=25pp 22.1%, >=30pp 16.0%, >=40pp 8.2%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.41pp; >=10pp 45.2%, >=25pp 17.2%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,888 | 27.6 | 14.3 | 25.9 | 15.2 | 11.8 | 4.4 | 0.7 | 6.14 | 17.0% | 5.1% |
| CHALLENGER | 5,012 | 15.6 | 10.1 | 20.1 | 15.7 | 15.5 | 12.4 | 10.7 | 11.17 | 38.6% | 23.1% |
| ITF_MEN | 8,556 | 10.0 | 7.3 | 16.7 | 14.6 | 21.5 | 17.6 | 12.2 | 15.5 | 51.4% | 29.8% |
| ITF_WOMEN | 12,332 | 9.4 | 6.8 | 15.8 | 15.3 | 22.4 | 18.2 | 11.9 | 15.84 | 52.6% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,051 | 17.2 | 13.3 | 26.1 | 19.6 | 17.4 | 5.9 | 0.6 | 8.25 | 23.9% | 6.5% |
| WTA125 | 721 | 13.3 | 7.2 | 21.8 | 21.6 | 21.1 | 13.0 | 1.9 | 11.65 | 36.1% | 15.0% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,888 | 24.0 | 15.1 | 25.3 | 17.7 | 12.5 | 4.5 | 0.9 | 6.63 | 17.9% | 5.4% |
| CHALLENGER | 5,012 | 14.9 | 8.8 | 18.0 | 14.6 | 18.1 | 14.1 | 11.5 | 12.74 | 43.6% | 25.6% |
| ITF_MEN | 8,556 | 8.1 | 5.8 | 14.3 | 13.0 | 19.6 | 21.2 | 17.9 | 18.81 | 58.7% | 39.1% |
| ITF_WOMEN | 12,332 | 8.2 | 5.6 | 13.7 | 13.0 | 20.6 | 21.1 | 17.8 | 19.21 | 59.5% | 38.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,051 | 14.3 | 10.3 | 22.3 | 15.9 | 22.6 | 13.3 | 1.2 | 10.87 | 37.1% | 14.5% |
| WTA125 | 721 | 6.4 | 5.4 | 16.8 | 17.9 | 25.2 | 19.7 | 8.6 | 16.74 | 53.5% | 28.3% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,888 | 23.3 | 12.5 | 24.3 | 16.4 | 15.6 | 6.7 | 1.3 | 7.53 | 23.6% | 8.0% |
| CHALLENGER | 5,012 | 14.3 | 9.2 | 20.8 | 15.4 | 16.3 | 13.1 | 10.9 | 11.47 | 40.2% | 24.0% |
| ITF_MEN | 8,556 | 9.6 | 7.3 | 16.8 | 13.8 | 22.1 | 17.9 | 12.4 | 15.98 | 52.5% | 30.4% |
| ITF_WOMEN | 12,332 | 9.3 | 6.6 | 16.3 | 15.8 | 22.7 | 18.1 | 11.1 | 15.65 | 52.0% | 29.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,051 | 23.7 | 17.2 | 30.7 | 15.3 | 9.8 | 2.6 | 0.7 | 6.04 | 13.1% | 3.4% |
| WTA125 | 721 | 22.3 | 11.4 | 27.3 | 16.1 | 16.1 | 6.4 | 0.4 | 8.01 | 22.9% | 6.8% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,776 | 24.8 | 19.3 | 29.9 | 13.1 | 9.6 | 3.0 | 0.3 | 5.67 | 12.9% | 3.3% |
| CHALLENGER | 3,453 | 21.1 | 14.2 | 26.7 | 14.9 | 14.8 | 6.7 | 1.7 | 7.44 | 23.2% | 8.4% |
| DOUBLES | 1,796 | 5.1 | 4.5 | 12.3 | 10.2 | 20.2 | 25.8 | 21.8 | 24.04 | 67.8% | 47.7% |
| ITF_MEN | 6,319 | 13.7 | 9.2 | 19.8 | 16.2 | 21.5 | 13.3 | 6.4 | 12.2 | 41.2% | 19.7% |
| ITF_WOMEN | 7,392 | 12.6 | 8.8 | 19.4 | 15.3 | 21.7 | 16.1 | 6.1 | 12.87 | 43.9% | 22.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,228 | 22.6 | 15.5 | 30.7 | 18.1 | 9.6 | 3.2 | 0.3 | 6.86 | 13.1% | 3.5% |
| WTA125 | 793 | 20.8 | 13.4 | 21.9 | 18.4 | 14.6 | 8.7 | 2.1 | 8.33 | 25.5% | 10.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,808 | 27.9 | 14.6 | 26.3 | 15.1 | 11.7 | 4.1 | 0.4 | 6.0 | 16.1% | 4.5% |
| CHALLENGER | 3,536 | 20.4 | 12.6 | 24.8 | 18.1 | 15.5 | 6.9 | 1.8 | 8.43 | 24.1% | 8.6% |
| ITF_MEN | 6,240 | 12.2 | 8.8 | 20.2 | 16.6 | 22.7 | 14.4 | 5.1 | 12.57 | 42.2% | 19.5% |
| ITF_WOMEN | 9,212 | 11.2 | 8.1 | 18.1 | 17.4 | 24.4 | 15.4 | 5.5 | 13.56 | 45.2% | 20.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 1,992 | 17.4 | 13.2 | 26.1 | 19.8 | 17.3 | 5.6 | 0.7 | 8.25 | 23.5% | 6.2% |
| WTA125 | 695 | 13.7 | 7.0 | 21.3 | 22.0 | 21.7 | 12.7 | 1.6 | 11.66 | 36.0% | 14.2% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,808 | 24.2 | 15.5 | 25.5 | 17.7 | 12.5 | 4.1 | 0.5 | 6.49 | 17.2% | 4.7% |
| CHALLENGER | 3,536 | 19.0 | 11.3 | 22.3 | 17.4 | 18.3 | 9.7 | 2.0 | 9.36 | 30.0% | 11.7% |
| ITF_MEN | 6,241 | 9.7 | 7.1 | 16.8 | 15.1 | 21.6 | 19.3 | 10.5 | 15.49 | 51.4% | 29.8% |
| ITF_WOMEN | 9,213 | 9.3 | 6.4 | 15.2 | 14.5 | 22.6 | 20.6 | 11.4 | 16.83 | 54.6% | 32.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 1,992 | 14.4 | 10.3 | 22.3 | 16.0 | 22.6 | 13.1 | 1.3 | 10.87 | 37.0% | 14.4% |
| WTA125 | 695 | 6.2 | 5.6 | 16.8 | 18.3 | 25.2 | 20.1 | 7.8 | 16.54 | 53.1% | 27.9% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,725 | 24.9 | 19.6 | 29.9 | 13.3 | 9.2 | 2.9 | 0.2 | 5.65 | 12.3% | 3.1% |
| CHALLENGER | 3,026 | 22.4 | 15.1 | 28.1 | 14.9 | 14.2 | 4.7 | 0.5 | 6.94 | 19.4% | 5.2% |
| DOUBLES | 1,676 | 5.1 | 4.6 | 12.6 | 10.4 | 20.0 | 25.8 | 21.6 | 23.9 | 67.4% | 47.4% |
| ITF_MEN | 5,297 | 14.8 | 9.8 | 21.5 | 17.0 | 21.4 | 11.6 | 3.9 | 11.23 | 36.9% | 15.5% |
| ITF_WOMEN | 6,145 | 13.4 | 9.3 | 20.8 | 16.1 | 21.9 | 14.9 | 3.6 | 11.83 | 40.4% | 18.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,176 | 23.0 | 15.9 | 30.7 | 18.1 | 9.6 | 2.5 | 0.1 | 6.8 | 12.2% | 2.6% |
| WTA125 | 682 | 22.6 | 14.7 | 23.3 | 19.8 | 13.1 | 6.0 | 0.6 | 7.6 | 19.7% | 6.6% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,796 | 5.1 | 4.5 | 12.3 | 10.2 | 20.2 | 25.8 | 21.8 | 24.04 | 67.8% | 47.7% |
| singles | 21,110 | 16.2 | 11.2 | 22.5 | 15.6 | 18.4 | 11.5 | 4.5 | 10.01 | 34.5% | 16.0% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 6,907 | 12.9 | 9.0 | 19.3 | 15.8 | 19.0 | 14.2 | 9.7 | 12.71 | 43.0% | 23.9% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 19,762 | 13.3 | 8.7 | 18.6 | 15.3 | 19.8 | 14.9 | 9.6 | 13.06 | 44.2% | 24.5% |
| UNKNOWN | 4,648 | 10.7 | 7.4 | 16.9 | 16.8 | 20.6 | 16.4 | 11.1 | 14.16 | 48.1% | 27.4% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,094 | 19.5 | 12.0 | 21.7 | 16.4 | 14.9 | 9.2 | 6.2 | 9.02 | 30.3% | 15.4% |
| B | 3,920 | 12.2 | 8.7 | 19.3 | 16.4 | 19.6 | 12.8 | 10.9 | 12.79 | 43.3% | 23.7% |
| C | 4,405 | 11.7 | 8.9 | 19.5 | 15.4 | 19.3 | 14.7 | 10.5 | 13.1 | 44.5% | 25.2% |
| D | 4,820 | 12.1 | 7.8 | 17.3 | 15.4 | 21.7 | 15.6 | 10.0 | 14.01 | 47.4% | 25.6% |
| F | 9,327 | 7.5 | 5.5 | 15.0 | 14.6 | 23.7 | 21.2 | 12.5 | 17.82 | 57.4% | 33.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,581 | 23.1 | 15.9 | 29.0 | 15.3 | 11.5 | 4.0 | 1.4 | 6.66 | 16.8% | 5.4% |
| B | 3,105 | 16.0 | 10.4 | 23.2 | 16.2 | 20.0 | 10.5 | 3.7 | 10.06 | 34.2% | 14.2% |
| C | 4,521 | 10.9 | 7.2 | 18.4 | 14.4 | 21.1 | 16.8 | 11.1 | 14.49 | 49.1% | 27.9% |
| D | 3,121 | 14.3 | 9.6 | 19.9 | 14.9 | 21.1 | 14.2 | 6.0 | 12.05 | 41.3% | 20.2% |
| F | 5,578 | 10.2 | 8.3 | 15.8 | 15.2 | 22.7 | 19.7 | 8.1 | 15.27 | 50.5% | 27.8% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 10,381 | 17.7 | 10.8 | 21.0 | 16.1 | 15.6 | 10.2 | 8.7 | 10.14 | 34.4% | 18.9% |
| LIMITED | 6,694 | 13.4 | 10.2 | 20.0 | 16.1 | 19.4 | 13.3 | 7.6 | 11.95 | 40.3% | 20.9% |
| POOR | 14,491 | 9.1 | 6.3 | 15.9 | 15.0 | 22.9 | 19.1 | 11.7 | 16.3 | 53.7% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,716 | 24.8 | 18.8 | 33.5 | 14.3 | 6.1 | 2.3 | 0.2 | 5.66 | 8.6% | 2.5% |
| GAME_SPREAD | 5,159 | 22.3 | 15.3 | 33.3 | 17.1 | 9.1 | 2.5 | 0.3 | 6.72 | 12.0% | 2.9% |
| MATCH_WINNER | 22,906 | 15.4 | 10.7 | 21.7 | 15.2 | 18.6 | 12.6 | 5.9 | 10.55 | 37.1% | 18.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 11,946 | 27.8 | 16.3 | 31.3 | 12.7 | 9.2 | 2.3 | 0.3 | 5.7 | 11.8% | 2.6% |
| TOTAL_GAMES | 8,370 | 9.1 | 9.9 | 36.1 | 27.8 | 10.6 | 3.7 | 2.8 | 9.41 | 17.1% | 6.6% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 10,242 | 24.5 | 31.6 | 32.7 | 6.4 | 3.7 | 0.8 | 0.2 | 4.62 | 4.8% | 1.0% |
| GAME_SPREAD | 6,687 | 45.8 | 16.8 | 26.4 | 7.8 | 1.8 | 1.0 | 0.4 | 3.43 | 3.2% | 1.4% |
| TOTAL_GAMES | 11,589 | 5.3 | 8.0 | 40.8 | 33.5 | 7.3 | 2.8 | 2.3 | 9.56 | 12.4% | 5.2% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 10,253 | 23.5 | 17.0 | 35.3 | 14.0 | 7.3 | 2.6 | 0.4 | 6.05 | 10.3% | 3.0% |
| GAME_SPREAD | 6,690 | 19.8 | 13.1 | 27.9 | 20.9 | 13.0 | 4.3 | 1.0 | 7.96 | 18.2% | 5.3% |
| TOTAL_GAMES | 11,619 | 8.9 | 9.8 | 36.2 | 26.5 | 12.0 | 4.1 | 2.5 | 9.42 | 18.6% | 6.6% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 31,566 | 44.5% | 24.8% | 13.14 | 36.1% | 15.5% | 10.92 |
| gen1_elo | 31,566 | 44.5% | 24.6% | 13.0 | 35.9% | 15.6% | 10.73 |
| gen1_sr | 31,566 | 52.3% | 31.6% | 15.99 | 44.5% | 22.2% | 13.04 |
| gen2 | 31,566 | 51.4% | 31.9% | 15.59 | 44.5% | 23.8% | 13.04 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 16,061 | 15.6 | 10.4 | 21.4 | 17.3 | 20.2 | 11.9 | 3.3 | 10.72 | 35.3% | 15.1% |
| STALE | 15,505 | 10.0 | 6.7 | 15.4 | 13.8 | 19.3 | 18.1 | 16.6 | 17.0 | 54.1% | 34.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 16,374 | 16.3 | 11.2 | 22.4 | 15.3 | 17.8 | 12.0 | 4.9 | 10.02 | 34.8% | 17.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 54,472 | 16374 | 19533 | 18565 | 24.1 | 140.9 | 1400.4 |
| ge_15pp | 22,550 | 5694 | 6959 | 9897 | 26.3 | 440.2 | 1380.4 |
| ge_25pp | 12,060 | 2775 | 3020 | 6265 | 31.9 | 584.0 | 1380.4 |
| lt_10pp | 23,525 | 8170 | 9239 | 6116 | 22.4 | 47.5 | 1341.5 |

Current slate `SL-20261025T222016Z-6e73ff1e`: 815 priced rows, quote age at build {'median': 16.2, 'max': 16.2}, freshness {'AGING': 815}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 28 | 0.0 | 0.0 | 21.4 | 10.7 | 39.3 | 28.6 | 0.0 | 20.48 | 67.9% | 28.6% |
| EXTERNAL_LONE_OUTLIER | 18 | 77.8 | 22.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,063 | 19.2 | 11.3 | 24.8 | 18.8 | 18.1 | 7.1 | 0.6 | 8.83 | 25.8% | 7.7% |
| KALSHI_LONE_OUTLIER | 20 | 5.0 | 5.0 | 75.0 | 5.0 | 5.0 | 5.0 | 0.0 | 5.8 | 10.0% | 5.0% |
| MARKETS_AGREE | 619 | 65.3 | 34.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.21 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,345 | 0.0 | 2.6 | 35.2 | 26.5 | 24.7 | 10.3 | 0.7 | 12.04 | 35.7% | 11.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 31,566 | 5093 (16.1%) | 26.4% | 0.9% | {"EXTERNAL_STALE": 3063, "AGREES_WITH_KALSHI": 1345, "ALL_AGREE": 619, "SUPPORTS_MODEL_DIRECTION": 27, "AGREES_WITH_MODEL": 20, "EXTERNAL_OUTLIER": 18, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 14,057 | 1291 (9.2%) | 37.2% | 1.6% | {"EXTERNAL_STALE": 790, "AGREES_WITH_KALSHI": 480, "SUPPORTS_MODEL_DIRECTION": 19, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 7,823 | 393 (5.0%) | 37.7% | 2.3% | {"EXTERNAL_STALE": 236, "AGREES_WITH_KALSHI": 148, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,792 | 370 (9.8%) | 38.1% | 2.4% | {"EXTERNAL_STALE": 220, "AGREES_WITH_KALSHI": 141, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 12,586 | 2865 (22.8%) | 17.8% | 0.8% | {"EXTERNAL_STALE": 1696, "ALL_AGREE": 619, "AGREES_WITH_KALSHI": 509, "EXTERNAL_OUTLIER": 18, "AGREES_WITH_MODEL": 17, "SUPPORTS_MODEL_DIRECTION": 5, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 6,008 | 10.2 | 7.6 | 19.4 | 14.6 | 22.4 | 15.9 | 9.9 | 14.14 | 48.3% | 25.9% |
| 4-10x | 4,075 | 11.1 | 8.3 | 18.8 | 15.5 | 21.6 | 14.7 | 9.9 | 13.74 | 46.2% | 24.6% |
| <2x | 16,128 | 14.9 | 9.8 | 19.1 | 16.4 | 17.5 | 13.1 | 9.0 | 11.8 | 39.6% | 22.1% |
| >=10x | 5,355 | 10.7 | 6.1 | 15.2 | 14.2 | 22.0 | 19.7 | 12.1 | 16.49 | 53.8% | 31.8% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 8,100 | 12.4 | 8.6 | 19.1 | 16.1 | 19.1 | 13.9 | 10.7 | 12.99 | 43.6% | 24.5% |
| 300-1000 | 6,622 | 11.6 | 8.6 | 17.3 | 15.4 | 20.7 | 16.2 | 10.1 | 13.91 | 47.1% | 26.3% |
| <300 | 10,259 | 8.5 | 5.6 | 15.4 | 14.8 | 23.3 | 20.1 | 12.4 | 17.05 | 55.7% | 32.5% |
| >=3000 | 6,585 | 21.3 | 13.1 | 23.6 | 16.4 | 14.1 | 6.9 | 4.6 | 7.85 | 25.6% | 11.6% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 893 | 0.551 | 0.4132 | 0.5039 | +0.047 | -0.091 | -0.0045 ± 0.0052 |
| ratio 4-10x | 605 | 0.5888 | 0.4431 | 0.4992 | +0.090 | -0.056 | 0.0101 ± 0.0065 |
| ratio <2x | 2223 | 0.5389 | 0.4159 | 0.4489 | +0.090 | -0.033 | 0.0113 ± 0.0031 |
| ratio >=10x | 822 | 0.5706 | 0.395 | 0.4611 | +0.110 | -0.066 | 0.0078 ± 0.0064 |
| thinner_sample 1000-3000 | 1236 | 0.5426 | 0.416 | 0.4506 | +0.092 | -0.035 | 0.009 ± 0.0041 |
| thinner_sample 300-1000 | 1017 | 0.5668 | 0.423 | 0.4936 | +0.073 | -0.071 | 0.0 ± 0.0051 |
| thinner_sample <300 | 1529 | 0.5622 | 0.3956 | 0.465 | +0.097 | -0.069 | 0.0089 ± 0.0045 |
| thinner_sample >=3000 | 761 | 0.5369 | 0.443 | 0.4717 | +0.065 | -0.029 | 0.0116 ± 0.0042 |
| data_status ADEQUATE | 1316 | 0.5384 | 0.4345 | 0.4544 | +0.084 | -0.020 | 0.0112 ± 0.0034 |
| data_status LIMITED | 1045 | 0.5515 | 0.4179 | 0.4861 | +0.065 | -0.068 | 0.0028 ± 0.0046 |
| data_status POOR | 2182 | 0.5639 | 0.4023 | 0.4688 | +0.095 | -0.067 | 0.0074 ± 0.0037 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 666 | 0.2017 | 0.2025 | -0.0008 ± 0.0006 | 0.5844 | 0.5861 | 0.5017 | 0.4868 | 0.5195 | -0.075 ± 0.0184 | -0.01 (5) |
| 3-5 | 420 | 0.2059 | 0.2051 | +0.0008 ± 0.0018 | 0.5952 | 0.5918 | 0.5027 | 0.4626 | 0.4714 | -0.108 ± 0.0228 | 0.02 (1) |
| 5-10 | 935 | 0.202 | 0.2021 | -0.0001 ± 0.0022 | 0.5904 | 0.5875 | 0.5141 | 0.44 | 0.4727 | -0.089 ± 0.0152 | -0.0167 (6) |
| 10-15 | 792 | 0.215 | 0.2065 | +0.0085 ± 0.004 | 0.6205 | 0.5953 | 0.5309 | 0.4068 | 0.4343 | -0.101 ± 0.0161 | -0.048 (5) |
| 15-25 | 1028 | 0.2258 | 0.2137 | +0.0121 ± 0.0056 | 0.6473 | 0.6112 | 0.578 | 0.3822 | 0.4494 | -0.095 ± 0.0144 | -0.0033 (9) |
| 25-40 | 586 | 0.2216 | 0.2107 | +0.0110 ± 0.0113 | 0.6326 | 0.6048 | 0.66 | 0.3501 | 0.4846 | -0.071 ± 0.0173 | -0.01 (1) |
| 40+ | 116 | 0.2743 | 0.202 | +0.0723 ± 0.036 | 0.7526 | 0.5904 | 0.7587 | 0.3114 | 0.4569 | -0.070 ± 0.0354 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3424 | 0.1852 | 0.1861 | -0.0009 ± 0.0003 | 0.5461 | 0.547 | 0.4914 | 0.4764 | 0.5076 | -0.024 ± 0.0075 | -0.0129 (17) |
| 3-5 | 2261 | 0.1991 | 0.1979 | +0.0012 ± 0.0008 | 0.5788 | 0.5732 | 0.4839 | 0.444 | 0.448 | -0.053 ± 0.0095 | 0.0 (2) |
| 5-10 | 4889 | 0.1984 | 0.1952 | +0.0032 ± 0.0009 | 0.5813 | 0.57 | 0.4837 | 0.4098 | 0.4246 | -0.047 ± 0.0064 | -0.0119 (21) |
| 10-15 | 4179 | 0.1979 | 0.1806 | +0.0173 ± 0.0016 | 0.5813 | 0.5324 | 0.488 | 0.3636 | 0.3561 | -0.071 ± 0.0066 | -0.0281 (16) |
| 15-25 | 5256 | 0.2088 | 0.1694 | +0.0394 ± 0.0022 | 0.6113 | 0.5007 | 0.5042 | 0.3077 | 0.3069 | -0.074 ± 0.0056 | -0.0025 (44) |
| 25-40 | 4108 | 0.2228 | 0.1287 | +0.0942 ± 0.0035 | 0.6399 | 0.3939 | 0.5323 | 0.2189 | 0.2291 | -0.060 ± 0.0054 | -0.01 (1) |
| 40+ | 2660 | 0.3794 | 0.0451 | +0.3342 ± 0.0047 | 0.9881 | 0.1738 | 0.6322 | 0.1064 | 0.0639 | -0.078 ± 0.0039 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 525 | 0.2084 | 0.2091 | -0.0007 ± 0.0007 | 0.599 | 0.6007 | 0.5066 | 0.4915 | 0.52 | -0.102 ± 0.0216 | -0.01 (3) |
| 3-5 | 372 | 0.2258 | 0.2227 | +0.0031 ± 0.002 | 0.6382 | 0.6318 | 0.5152 | 0.4754 | 0.4516 | -0.136 ± 0.0261 | 0.02 (1) |
| 5-10 | 817 | 0.207 | 0.2066 | +0.0004 ± 0.0024 | 0.6002 | 0.5985 | 0.5472 | 0.4723 | 0.5104 | -0.082 ± 0.0164 | -0.01 (4) |
| 10-15 | 755 | 0.2163 | 0.21 | +0.0063 ± 0.0042 | 0.6217 | 0.6056 | 0.5648 | 0.4406 | 0.4795 | -0.107 ± 0.0174 | -0.04 (5) |
| 15-25 | 1053 | 0.2292 | 0.2109 | +0.0183 ± 0.0056 | 0.6511 | 0.6043 | 0.5876 | 0.392 | 0.4473 | -0.098 ± 0.0144 | -0.0133 (9) |
| 25-40 | 740 | 0.2657 | 0.1993 | +0.0664 ± 0.0103 | 0.743 | 0.5801 | 0.655 | 0.3399 | 0.3946 | -0.117 ± 0.0162 | -0.0075 (4) |
| 40+ | 281 | 0.3519 | 0.1748 | +0.1771 ± 0.0246 | 0.968 | 0.5207 | 0.7338 | 0.25 | 0.3238 | -0.064 ± 0.0238 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2920 | 0.1937 | 0.194 | -0.0003 ± 0.0003 | 0.5637 | 0.5642 | 0.5126 | 0.4976 | 0.5134 | -0.043 ± 0.0085 | -0.0133 (15) |
| 3-5 | 1941 | 0.1996 | 0.1985 | +0.0011 ± 0.0008 | 0.577 | 0.5741 | 0.5141 | 0.4742 | 0.4796 | -0.049 ± 0.0103 | 0.02 (1) |
| 5-10 | 4327 | 0.1973 | 0.1951 | +0.0022 ± 0.001 | 0.5805 | 0.5698 | 0.5111 | 0.437 | 0.4624 | -0.035 ± 0.0068 | -0.0117 (6) |
| 10-15 | 3779 | 0.2012 | 0.1894 | +0.0118 ± 0.0018 | 0.5905 | 0.5521 | 0.5143 | 0.3904 | 0.4054 | -0.055 ± 0.0072 | -0.0189 (18) |
| 15-25 | 5204 | 0.2158 | 0.1787 | +0.0371 ± 0.0023 | 0.6267 | 0.5251 | 0.5249 | 0.3289 | 0.3363 | -0.066 ± 0.0059 | -0.0086 (42) |
| 25-40 | 4799 | 0.2531 | 0.1367 | +0.1164 ± 0.0034 | 0.7118 | 0.4198 | 0.5581 | 0.241 | 0.2186 | -0.088 ± 0.0053 | -0.0044 (18) |
| 40+ | 3807 | 0.3918 | 0.0608 | +0.3310 ± 0.0046 | 1.0309 | 0.2169 | 0.6499 | 0.119 | 0.0859 | -0.070 ± 0.0039 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 638 | 0.1994 | 0.2016 | -0.0021 ± 0.0006 | 0.5795 | 0.5847 | 0.501 | 0.4858 | 0.547 | -0.034 ± 0.0185 | -0.0137 (8) |
| 3-5 | 453 | 0.2031 | 0.2017 | +0.0014 ± 0.0017 | 0.5897 | 0.5848 | 0.5058 | 0.466 | 0.4702 | -0.117 ± 0.022 | 0.0067 (3) |
| 5-10 | 963 | 0.2027 | 0.1994 | +0.0033 ± 0.0022 | 0.5918 | 0.5805 | 0.5094 | 0.4355 | 0.4486 | -0.104 ± 0.0148 | -0.0071 (7) |
| 10-15 | 782 | 0.2087 | 0.2056 | +0.0031 ± 0.004 | 0.6065 | 0.5935 | 0.5406 | 0.417 | 0.468 | -0.083 ± 0.0161 | -0.0317 (6) |
| 15-25 | 972 | 0.2314 | 0.2143 | +0.0172 ± 0.0058 | 0.6609 | 0.6121 | 0.5893 | 0.3948 | 0.4475 | -0.108 ± 0.0148 | -0.03 (1) |
| 25-40 | 612 | 0.2138 | 0.2181 | -0.0043 ± 0.011 | 0.6169 | 0.6219 | 0.6695 | 0.3587 | 0.518 | -0.054 ± 0.0169 | 0.015 (2) |
| 40+ | 123 | 0.2879 | 0.2151 | +0.0728 ± 0.0362 | 0.7962 | 0.6188 | 0.7691 | 0.3198 | 0.4715 | -0.063 ± 0.0383 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3352 | 0.1864 | 0.1871 | -0.0007 ± 0.0003 | 0.548 | 0.5491 | 0.4893 | 0.4741 | 0.4937 | -0.033 ± 0.0075 | -0.0163 (35) |
| 3-5 | 2268 | 0.1957 | 0.1938 | +0.0018 ± 0.0007 | 0.5741 | 0.5679 | 0.4876 | 0.4479 | 0.4458 | -0.062 ± 0.0095 | -0.0094 (18) |
| 5-10 | 4983 | 0.1957 | 0.1902 | +0.0055 ± 0.0009 | 0.5751 | 0.5568 | 0.484 | 0.4099 | 0.4102 | -0.059 ± 0.0062 | -0.01 (31) |
| 10-15 | 4041 | 0.1917 | 0.1765 | +0.0152 ± 0.0016 | 0.567 | 0.5218 | 0.4997 | 0.3763 | 0.3761 | -0.064 ± 0.0066 | -0.015 (12) |
| 15-25 | 5401 | 0.2111 | 0.1721 | +0.0390 ± 0.0022 | 0.6166 | 0.5074 | 0.5144 | 0.3193 | 0.3175 | -0.073 ± 0.0056 | -0.03 (2) |
| 25-40 | 4134 | 0.2193 | 0.1316 | +0.0876 ± 0.0036 | 0.6328 | 0.4 | 0.5367 | 0.2207 | 0.2417 | -0.052 ± 0.0054 | 0.01 (3) |
| 40+ | 2598 | 0.3936 | 0.0507 | +0.3429 ± 0.005 | 1.0284 | 0.188 | 0.6448 | 0.1136 | 0.0704 | -0.080 ± 0.0042 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1024 | 0.1961 | 0.1962 | -0.0001 ± 0.0005 | 0.5716 | 0.5715 | 0.502 | 0.4869 | 0.4922 | -0.061 ± 0.014 | -0.0224 (49) |
| 3-5 | 707 | 0.1924 | 0.1916 | +0.0008 ± 0.0013 | 0.5623 | 0.5591 | 0.4909 | 0.4511 | 0.4583 | -0.062 ± 0.0168 | -0.0194 (34) |
| 5-10 | 1491 | 0.2022 | 0.1965 | +0.0057 ± 0.0017 | 0.5936 | 0.5755 | 0.4964 | 0.423 | 0.4219 | -0.074 ± 0.0117 | -0.005 (78) |
| 10-15 | 994 | 0.2099 | 0.1982 | +0.0117 ± 0.0035 | 0.6089 | 0.5784 | 0.5246 | 0.4015 | 0.4135 | -0.071 ± 0.0144 | 0.0014 (64) |
| 15-25 | 1332 | 0.2317 | 0.2118 | +0.0199 ± 0.0049 | 0.6614 | 0.6087 | 0.5795 | 0.3848 | 0.4324 | -0.073 ± 0.0126 | -0.0214 (59) |
| 25-40 | 807 | 0.2469 | 0.2087 | +0.0382 ± 0.0099 | 0.7033 | 0.5991 | 0.6764 | 0.364 | 0.4585 | -0.087 ± 0.015 | -0.0219 (26) |
| 40+ | 267 | 0.3467 | 0.2029 | +0.1438 ± 0.027 | 1.0025 | 0.5933 | 0.8095 | 0.3282 | 0.4382 | -0.089 ± 0.0249 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3386 | 0.1827 | 0.1829 | -0.0002 ± 0.0003 | 0.5381 | 0.5377 | 0.5028 | 0.4874 | 0.4968 | -0.040 ± 0.0074 | -0.0157 (88) |
| 3-5 | 2344 | 0.1956 | 0.1937 | +0.0019 ± 0.0007 | 0.5703 | 0.5659 | 0.4977 | 0.458 | 0.4539 | -0.055 ± 0.0092 | -0.0209 (69) |
| 5-10 | 4688 | 0.1965 | 0.1885 | +0.0080 ± 0.001 | 0.5788 | 0.5546 | 0.4915 | 0.418 | 0.4032 | -0.070 ± 0.0064 | -0.0082 (132) |
| 10-15 | 3305 | 0.2068 | 0.1908 | +0.0160 ± 0.0019 | 0.6023 | 0.5598 | 0.5292 | 0.4062 | 0.4018 | -0.067 ± 0.0076 | -0.0053 (105) |
| 15-25 | 4094 | 0.2305 | 0.2008 | +0.0296 ± 0.0028 | 0.6643 | 0.5812 | 0.5703 | 0.3748 | 0.3981 | -0.065 ± 0.007 | -0.0253 (107) |
| 25-40 | 2785 | 0.2591 | 0.186 | +0.0731 ± 0.0052 | 0.7349 | 0.5418 | 0.634 | 0.3204 | 0.363 | -0.077 ± 0.008 | -0.0229 (51) |
| 40+ | 1225 | 0.3759 | 0.146 | +0.2299 ± 0.0115 | 1.0646 | 0.4399 | 0.7318 | 0.2283 | 0.2653 | -0.070 ± 0.0102 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4543 | 1.035 ± 0.042 | 1.11 | 0.1685 | 0.1632 | 0.2144 | 0.2069 |
| gen2 | 4543 | 0.831 ± 0.039 | 1.077 | 0.1682 | 0.1639 | 0.2339 | 0.2066 |
| gen1_elo | 4543 | 1.007 ± 0.04 | 1.108 | 0.1752 | 0.1633 | 0.2133 | 0.2071 |
| gen1_sr | 4543 | 1.017 ± 0.05 | 1.143 | 0.1293 | 0.1658 | 0.2302 | 0.2062 |
| gen1_ledger | 6622 | 0.861 ± 0.029 | 1.065 | 0.1838 | 0.1772 | 0.2186 | 0.201 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 22,550)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,164 | 22.9% |
| STALE_QUOTE | market_freshness | 4,830 | 21.4% |
| BOOK_QUALITY | execution | 4,326 | 19.2% |
| POOR_DATA | data | 2,517 | 11.2% |
| LIMITED_DATA | data | 1,395 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,221 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,076 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 952 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 664 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 404 | 1.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.9%, market_freshness 21.4%, execution 19.2%, data 17.3%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.8%, mapping 4.2%, model_calibration 1.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 93.9%, LOW_DATA_QUALITY 70.6%, THIN_PLAYER_HISTORY 59.3%, STALE_PLAYER_DATA 49.4%, STALE_KALSHI_QUOTE 43.9%, MODEL_INTERNAL_DISAGREEMENT 42.6%, ASYMMETRIC_SAMPLE_SIZE 33.2%, WIDE_SPREAD 25.2%, MODEL_HIGH_UNCERTAINTY 18.0%, PLAYER_IDENTITY_RISK 16.6%, LEVEL_TRANSFER_RISK 10.7%, EVENT_MAPPING_RISK 8.3%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 3.9%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.4%, POST_SETTLEMENT_OBSERVATION 22.9%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 12,060)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,148 | 34.4% |
| BOOK_QUALITY | execution | 2,265 | 18.8% |
| STALE_QUOTE | market_freshness | 2,230 | 18.5% |
| POOR_DATA | data | 1,024 | 8.5% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 652 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 533 | 4.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 423 | 3.5% |
| LIMITED_DATA | data | 420 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 268 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 96 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.4%, execution 18.8%, market_freshness 18.5%, data 12.0%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.8%, LOW_DATA_QUALITY 74.1%, THIN_PLAYER_HISTORY 61.4%, STALE_KALSHI_QUOTE 51.9%, STALE_PLAYER_DATA 43.9%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 24.6%, PLAYER_IDENTITY_RISK 20.0%, MODEL_HIGH_UNCERTAINTY 18.3%, EVENT_MAPPING_RISK 10.0%, LEVEL_TRANSFER_RISK 9.4%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 5.1%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.5%, POST_SETTLEMENT_OBSERVATION 34.4%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 9337, "IDENTITY_AMBIGUOUS": 2723}; ticker orientation: {"VERIFIED": 12060}.

Checks: discipline:AMBIGUOUS 856, discipline:PASS 11204, identity_confidence:AMBIGUOUS 2417, identity_confidence:PASS 9643, level_mapping:NA 868, level_mapping:PASS 11192, market_pair:AMBIGUOUS 461, market_pair:NA 300, market_pair:PASS 11299, model_complement:NA 267, model_complement:PASS 11793, namesake:AMBIGUOUS 6, namesake:PASS 12054, physical_match_id:NA 4237, physical_match_id:PASS 7823, player_ids:PASS 12060, same_pair_other_event:PASS 12060, ticker_orientation:PASS 12060

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,664 | 4.4% | 4.0% | 1.7% | {"market_freshness": 53, "model_calibration_or_unknown": 47, "data": 35, "execution": 24, "model_calibration": 20, "market_freshness/coverage": 15, "coverage": 13} | 5.92 | 0.2239 / 0.2208 (539) | 18.9% | 3.4% | 3.3% | 2.8% |
| CHALLENGER | 8,465 | 17.1% | 7.0% | 12.0% | {"coverage": 812, "market_freshness/coverage": 173, "market_freshness": 162, "data": 145, "model_calibration_or_unknown": 71, "model_calibration": 34, "execution": 33, "mapping": 16, "possible_market_error": 1} | 7.63 | 0.2183 / 0.2087 (1993) | 34.2% | 17.6% | 4.1% | 22.5% |
| DOUBLES | 1,796 | 47.7% | 47.4% | 7.1% | {"execution": 475, "mapping": 213, "market_freshness": 106, "market_freshness/coverage": 55, "coverage": 7} | 23.9 | 0.3106 / 0.2361 (437) | 13.0% | 0.0% | 100.0% | 6.7% |
| ITF_MEN | 14,875 | 25.5% | 17.7% | 31.5% | {"coverage": 1429, "execution": 719, "market_freshness": 643, "data": 496, "market_freshness/coverage": 333, "mapping": 175, "model_calibration_or_unknown": 2, "model_calibration": 2} | 11.94 | 0.2164 / 0.1986 (3331) | 37.4% | 69.9% | 19.9% | 22.4% |
| ITF_WOMEN | 19,724 | 27.2% | 19.9% | 44.5% | {"coverage": 1862, "market_freshness": 1164, "execution": 963, "data": 726, "market_freshness/coverage": 450, "mapping": 123, "model_calibration_or_unknown": 69, "model_calibration": 11} | 12.93 | 0.2033 / 0.1958 (3800) | 39.6% | 56.5% | 10.1% | 22.1% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,279 | 5.4% | 4.9% | 1.5% | {"market_freshness": 60, "model_calibration_or_unknown": 38, "execution": 26, "model_calibration": 16, "data": 14, "coverage": 12, "market_freshness/coverage": 10, "mapping": 1} | 7.65 | 0.2327 / 0.2282 (521) | 24.1% | 1.3% | 1.6% | 3.4% |
| WTA125 | 1,514 | 12.8% | 10.5% | 1.6% | {"market_freshness": 40, "model_calibration_or_unknown": 39, "market_freshness/coverage": 38, "data": 28, "execution": 20, "model_calibration": 13, "coverage": 12, "mapping": 4} | 9.72 | 0.2178 / 0.2042 (502) | 22.6% | 11.5% | 7.1% | 9.0% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 769 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 17.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1037 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 15 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 16 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 17 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 18 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 19 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 20 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 21 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 22 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 23 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 24 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 271 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 25 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 26 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 27 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 28 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 29 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 30 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 31 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 32 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 33 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 34 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 35 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 36 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 37 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 39 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 9.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 553 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 41 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 42 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 43 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 44 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 46 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 162 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 47 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 48 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 49 | `KXWTADOUBLES-26OCT25DABSTEBUCFER-BUCFER` | DOUBLES | gen1_ledger | 93% / 16% | +77 | BOOK_QUALITY | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9682, "by_level_share_of_ge_25pp": {"ATP": 0.0172, "CHALLENGER": 0.12, "DOUBLES": 0.071, "ITF_MEN": 0.315, "ITF_WOMEN": 0.4451, "OTHER": 0.001, "WTA": 0.0147, "WTA125": 0.0161}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5195, "share_primary_cause_market_settled_or_in_play": 0.4331, "share_primary_cause_stale_quote_only": 0.1849}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 12060, "identity_ambiguous_share": 0.2258, "ticker_orientation": {"VERIFIED": 12060}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 7823, "with_external": 393, "coverage": 0.0502, "external_status": {"EXTERNAL_STALE": 236, "AGREES_WITH_KALSHI": 148, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 236, "MODEL_LONE_OUTLIER": 148, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3766, "share_external_supports_model": 0.0229}, "pregame_clean_ge_25pp": {"n": 3792, "with_external": 370, "coverage": 0.0976, "external_status": {"EXTERNAL_STALE": 220, "AGREES_WITH_KALSHI": 141, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 220, "MODEL_LONE_OUTLIER": 141, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3811, "share_external_supports_model": 0.0243}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 490.5, "median_sample_ratio": 2.41, "median_min_matches": 21.0, "median_max_days_since_last": 227.0, "share_severe_asymmetry": 0.2138, "data_status": {"POOR": 6666, "LIMITED": 3175, "ADEQUATE": 2219}, "comparison_lt_10pp": {"median_thinner_serve_points": 1762.0, "median_sample_ratio": 1.67, "median_min_matches": 98.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 893, "model_minus_observed": 0.0471, "kalshi_minus_observed": -0.0907, "brier_diff_model_minus_kalshi": -0.0045}, "4-10x": {"n": 605, "model_minus_observed": 0.0896, "kalshi_minus_observed": -0.056, "brier_diff_model_minus_kalshi": 0.0101}, "<2x": {"n": 2223, "model_minus_observed": 0.09, "kalshi_minus_observed": -0.0331, "brier_diff_model_minus_kalshi": 0.0113}, ">=10x": {"n": 822, "model_minus_observed": 0.1095, "kalshi_minus_observed": -0.066, "brier_diff_model_minus_kalshi": 0.0078}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4543, "model": {"intercept": -0.531, "slope": 0.831, "slope_se": 0.039}, "kalshi_mid_same_rows": {"intercept": 0.21, "slope": 1.077, "slope_se": 0.043}, "mean_extremity_model": 0.1682, "mean_extremity_kalshi": 0.1639, "model_brier": 0.2339, "kalshi_brier": 0.2066, "brier_diff_model_minus_kalshi": 0.0273, "brier_diff_se": 0.0028, "model_logloss": 0.6646, "kalshi_logloss": 0.5962}, "fair_v1": {"n": 4543, "model": {"intercept": -0.416, "slope": 1.035, "slope_se": 0.042}, "kalshi_mid_same_rows": {"intercept": 0.286, "slope": 1.11, "slope_se": 0.043}, "mean_extremity_model": 0.1685, "mean_extremity_kalshi": 0.1632, "model_brier": 0.2144, "kalshi_brier": 0.2069, "brier_diff_model_minus_kalshi": 0.0074, "brier_diff_se": 0.0023, "model_logloss": 0.6177, "kalshi_logloss": 0.5967}, "gen1_elo": {"n": 4543, "model": {"intercept": -0.389, "slope": 1.007, "slope_se": 0.04}, "kalshi_mid_same_rows": {"intercept": 0.309, "slope": 1.108, "slope_se": 0.043}, "mean_extremity_model": 0.1752, "mean_extremity_kalshi": 0.1633, "model_brier": 0.2133, "kalshi_brier": 0.2071, "brier_diff_model_minus_kalshi": 0.0062, "brier_diff_se": 0.0023, "model_logloss": 0.6161, "kalshi_logloss": 0.5971}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2478, "share_ge_15": 0.4453, "median_abs_gap": 13.14, "n": 31566}, "gen1_elo": {"share_ge_25": 0.2458, "share_ge_15": 0.4448, "median_abs_gap": 13.0, "n": 31566}, "gen1_sr": {"share_ge_25": 0.3158, "share_ge_15": 0.5234, "median_abs_gap": 15.99, "n": 31566}, "gen2": {"share_ge_25": 0.3193, "share_ge_15": 0.5137, "median_abs_gap": 15.59, "n": 31566}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1548, "share_ge_15": 0.3606, "median_abs_gap": 10.92, "n": 24489}, "gen1_elo": {"share_ge_25": 0.1558, "share_ge_15": 0.3588, "median_abs_gap": 10.73, "n": 24486}, "gen1_sr": {"share_ge_25": 0.222, "share_ge_15": 0.4446, "median_abs_gap": 13.04, "n": 24490}, "gen2": {"share_ge_25": 0.2382, "share_ge_15": 0.4448, "median_abs_gap": 13.04, "n": 24491}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.92, "share_ge_25_all": 0.0444, "share_ge_25_pregame_clean": 0.0395}, "WTA": {"median_abs_gap_pregame_clean": 7.65, "share_ge_25_all": 0.054, "share_ge_25_pregame_clean": 0.0489}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2337, "share_within_10pp_all": 0.4319, "share_within_10pp_pregame_clean": 0.4844, "corr_model_vs_mid_pregame_clean": 0.843}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 666, "model_brier": 0.2017, "kalshi_brier": 0.2025, "brier_diff_model_minus_kalshi": -0.0008}, "10-15": {"n_settled": 792, "model_brier": 0.215, "kalshi_brier": 0.2065, "brier_diff_model_minus_kalshi": 0.0085}, "15-25": {"n_settled": 1028, "model_brier": 0.2258, "kalshi_brier": 0.2137, "brier_diff_model_minus_kalshi": 0.0121}, "25-40": {"n_settled": 586, "model_brier": 0.2216, "kalshi_brier": 0.2107, "brier_diff_model_minus_kalshi": 0.011}, "3-5": {"n_settled": 420, "model_brier": 0.2059, "kalshi_brier": 0.2051, "brier_diff_model_minus_kalshi": 0.0008}, "40+": {"n_settled": 116, "model_brier": 0.2743, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0723}, "5-10": {"n_settled": 935, "model_brier": 0.202, "kalshi_brier": 0.2021, "brier_diff_model_minus_kalshi": -0.0001}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.531, "slope": 0.831, "slope_se": 0.039}, "kalshi_slope": {"intercept": 0.21, "slope": 1.077, "slope_se": 0.043}, "n": 4543}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.499, "slope": 0.861, "slope_se": 0.029}, "kalshi_slope": {"intercept": 0.159, "slope": 1.065, "slope_se": 0.034}, "n": 6622}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 437, "model_brier": 0.3106, "kalshi_brier": 0.2361, "brier_diff_model_minus_kalshi": 0.0746, "brier_diff_se": 0.0144, "corr_model_outcome": 0.0381, "corr_kalshi_outcome": 0.2506}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
