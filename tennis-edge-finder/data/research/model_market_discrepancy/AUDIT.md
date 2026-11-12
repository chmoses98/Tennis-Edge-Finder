# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-12T21:21Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 91,269): 0-3 13.9%, 3-5 9.5%, 5-10 20.1%, 10-15 15.2%, 15-25 19.2%, 25-40 13.8%, 40+ 8.3%; median gap 11.95 pp.
* **Where the extremes live**: 97.3% of >=25 pp gaps are off the ATP/WTA main tour (ITF 78.4%, Challenger 11.0%, doubles 6.4%). Main tour: ATP 3.7% and WTA 5.9% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 20,183): MARKET_ALREADY_SETTLED_WHEN_PRICED 35.4%, STALE_QUOTE 20.1%, BOOK_QUALITY 16.2%, POOR_DATA 9.0%, POSSIBLY_IN_PLAY_QUOTE 5.9%, IDENTITY_AMBIGUOUS 4.2%, IN_PLAY_QUOTE 3.4%, LIMITED_DATA 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 1.7%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 35.4%, market_freshness 20.1%, execution 16.2%, data 12.3%, market_freshness/coverage 9.3%, mapping 4.2%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 55.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 44.7% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 20,183 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.8%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.9% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 480.0 points vs 1667.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.025, Gen-2 0.822, Gen-1 ledger 0.868 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 1028 model 0.2249 vs Kalshi 0.204; n 212 model 0.3052 vs Kalshi 0.1675.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA. Not implemented here.

## 1. Observations

* 378,743 model-market comparisons (627,211 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 124,561 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-12T21:00:27.429457+00:00'], shadow board 105,776 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-12T21:00:31.687567+00:00'], Model 4 44,194 rows, 31,341 settled tickers, 11,785 tickers with an external scan.
* By model: {"gen1_ledger": 83235, "gen1_elo": 53153, "fair_v1": 53153, "gen2": 53153, "gen1_sr": 53153, "model4_fundamental": 41490, "model4_conditioned": 41406}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 91,269 | 13.9 | 9.5 | 20.1 | 15.2 | 19.2 | 13.8 | 8.3 | 11.95 | 41.3% | 22.1% |
| MW fair_v1 | 53,153 | 12.5 | 8.6 | 18.7 | 15.2 | 19.6 | 15.1 | 10.4 | 13.23 | 45.0% | 25.4% |
| MW gen1_elo | 53,153 | 12.3 | 8.7 | 19.1 | 15.2 | 19.4 | 15.0 | 10.2 | 13.01 | 44.6% | 25.2% |
| MW gen1_ledger | 38,116 | 15.7 | 10.8 | 22.1 | 15.2 | 18.6 | 12.0 | 5.5 | 10.3 | 36.1% | 17.5% |
| MW gen1_sr | 53,153 | 9.9 | 7.1 | 16.5 | 13.9 | 20.9 | 18.8 | 12.8 | 16.01 | 52.6% | 31.7% |
| MW gen2 | 53,153 | 10.8 | 7.5 | 16.6 | 13.7 | 19.7 | 17.7 | 13.9 | 15.56 | 51.4% | 31.7% |
| all families model4_conditioned | 41,406 | 22.2 | 17.9 | 34.6 | 16.9 | 5.0 | 2.2 | 1.2 | 6.07 | 8.4% | 3.4% |
| all families model4_fundamental | 41,490 | 17.3 | 13.5 | 34.0 | 19.9 | 9.9 | 3.8 | 1.5 | 7.61 | 15.2% | 5.3% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.5%, >=15pp 41.3%, >=20pp 30.5%, >=25pp 22.1%, >=30pp 16.0%, >=40pp 8.3%, >=50pp 3.9%
Executable gap (model outside the book, before fees): median 8.59pp; >=10pp 45.7%, >=25pp 17.6%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,124 | 27.9 | 15.9 | 28.0 | 13.3 | 10.7 | 3.5 | 0.6 | 5.79 | 14.9% | 4.2% |
| CHALLENGER | 8,332 | 16.3 | 9.6 | 20.6 | 15.3 | 15.8 | 11.3 | 11.2 | 10.94 | 38.3% | 22.5% |
| ITF_MEN | 15,661 | 9.6 | 7.3 | 17.1 | 14.8 | 21.1 | 17.2 | 12.8 | 15.45 | 51.1% | 30.0% |
| ITF_WOMEN | 20,599 | 9.3 | 7.0 | 16.1 | 14.6 | 22.2 | 18.7 | 12.1 | 16.04 | 52.9% | 30.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,104 | 16.6 | 13.3 | 24.9 | 20.7 | 16.7 | 6.7 | 1.1 | 8.65 | 24.5% | 7.8% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,124 | 26.3 | 15.7 | 26.3 | 15.8 | 11.3 | 3.9 | 0.8 | 6.1 | 16.0% | 4.7% |
| CHALLENGER | 8,332 | 14.4 | 9.1 | 19.0 | 13.8 | 18.4 | 13.6 | 11.6 | 12.55 | 43.7% | 25.2% |
| ITF_MEN | 15,661 | 8.1 | 6.2 | 15.2 | 13.8 | 20.4 | 19.9 | 16.3 | 17.85 | 56.7% | 36.2% |
| ITF_WOMEN | 20,599 | 7.8 | 5.8 | 14.1 | 12.6 | 20.7 | 21.2 | 17.7 | 19.2 | 59.6% | 39.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,104 | 14.1 | 10.3 | 21.6 | 16.2 | 22.5 | 12.8 | 2.5 | 11.23 | 37.8% | 15.3% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,124 | 23.4 | 14.1 | 25.6 | 15.5 | 14.3 | 5.9 | 1.1 | 7.04 | 21.4% | 7.1% |
| CHALLENGER | 8,332 | 15.1 | 9.6 | 20.8 | 15.6 | 16.1 | 11.9 | 11.0 | 11.2 | 39.0% | 22.9% |
| ITF_MEN | 15,661 | 9.3 | 7.3 | 17.2 | 14.2 | 21.4 | 17.3 | 13.2 | 15.75 | 51.9% | 30.5% |
| ITF_WOMEN | 20,599 | 9.2 | 6.8 | 16.2 | 15.6 | 22.1 | 18.7 | 11.4 | 15.83 | 52.2% | 30.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,104 | 22.4 | 17.2 | 31.8 | 15.3 | 9.0 | 3.3 | 1.0 | 6.12 | 13.3% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,493 | 28.1 | 19.5 | 29.2 | 12.2 | 8.1 | 2.5 | 0.4 | 5.24 | 11.1% | 3.0% |
| CHALLENGER | 5,044 | 22.9 | 14.6 | 27.8 | 14.8 | 13.0 | 5.4 | 1.5 | 7.01 | 19.9% | 6.9% |
| DOUBLES | 2,796 | 4.8 | 4.4 | 12.8 | 11.1 | 20.6 | 24.8 | 21.5 | 23.23 | 66.9% | 46.3% |
| ITF_MEN | 11,310 | 12.8 | 9.5 | 21.5 | 15.7 | 21.6 | 12.9 | 6.0 | 11.8 | 40.5% | 18.9% |
| ITF_WOMEN | 13,241 | 13.4 | 9.3 | 19.9 | 15.7 | 21.7 | 14.6 | 5.4 | 12.18 | 41.6% | 20.0% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,827 | 23.9 | 15.9 | 31.7 | 16.9 | 8.9 | 2.5 | 0.2 | 6.57 | 11.6% | 2.7% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,995 | 28.4 | 16.1 | 28.5 | 13.2 | 10.5 | 3.1 | 0.3 | 5.64 | 13.9% | 3.4% |
| CHALLENGER | 5,853 | 21.0 | 12.0 | 25.7 | 18.0 | 15.8 | 5.6 | 1.8 | 8.23 | 23.2% | 7.4% |
| ITF_MEN | 11,334 | 11.8 | 8.7 | 20.6 | 17.2 | 22.1 | 14.0 | 5.5 | 12.45 | 41.6% | 19.5% |
| ITF_WOMEN | 14,954 | 11.3 | 8.6 | 19.1 | 17.0 | 24.1 | 15.3 | 4.6 | 13.14 | 44.0% | 19.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,990 | 16.9 | 13.3 | 25.2 | 21.0 | 16.7 | 6.2 | 0.6 | 8.45 | 23.5% | 6.8% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,995 | 26.6 | 16.0 | 26.6 | 15.7 | 11.2 | 3.4 | 0.4 | 6.02 | 15.0% | 3.8% |
| CHALLENGER | 5,853 | 18.1 | 11.7 | 23.8 | 16.3 | 19.0 | 9.0 | 2.1 | 9.0 | 30.1% | 11.1% |
| ITF_MEN | 11,336 | 9.6 | 7.3 | 17.8 | 16.0 | 22.3 | 18.0 | 9.0 | 14.74 | 49.3% | 27.0% |
| ITF_WOMEN | 14,956 | 8.9 | 7.0 | 16.1 | 14.2 | 22.6 | 20.6 | 10.7 | 16.52 | 53.8% | 31.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,990 | 14.3 | 10.5 | 21.8 | 16.4 | 22.6 | 12.5 | 1.9 | 11.03 | 37.0% | 14.4% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,423 | 28.4 | 19.7 | 29.2 | 12.3 | 7.8 | 2.3 | 0.3 | 5.2 | 10.4% | 2.6% |
| CHALLENGER | 4,464 | 24.3 | 15.4 | 28.9 | 14.9 | 12.3 | 3.7 | 0.4 | 6.55 | 16.5% | 4.1% |
| DOUBLES | 2,615 | 4.7 | 4.4 | 13.0 | 11.1 | 20.4 | 24.7 | 21.7 | 23.2 | 66.7% | 46.4% |
| ITF_MEN | 9,769 | 13.6 | 10.0 | 22.9 | 16.3 | 21.7 | 11.4 | 4.2 | 10.94 | 37.2% | 15.5% |
| ITF_WOMEN | 11,397 | 14.0 | 9.9 | 20.9 | 16.3 | 21.8 | 13.5 | 3.6 | 11.42 | 38.9% | 17.1% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,764 | 24.3 | 16.3 | 31.7 | 16.8 | 8.8 | 2.0 | 0.1 | 6.43 | 10.9% | 2.0% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,796 | 4.8 | 4.4 | 12.8 | 11.1 | 20.6 | 24.8 | 21.5 | 23.23 | 66.9% | 46.3% |
| singles | 35,320 | 16.6 | 11.3 | 22.9 | 15.5 | 18.4 | 10.9 | 4.3 | 9.77 | 33.7% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 11,527 | 12.6 | 9.0 | 19.3 | 15.0 | 19.6 | 14.4 | 10.1 | 13.0 | 44.1% | 24.6% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 34,578 | 12.9 | 8.6 | 18.8 | 15.0 | 19.2 | 15.1 | 10.3 | 13.04 | 44.6% | 25.4% |
| UNKNOWN | 6,635 | 10.4 | 7.5 | 17.1 | 16.6 | 21.5 | 15.8 | 11.1 | 14.32 | 48.5% | 26.9% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 14,733 | 19.0 | 11.8 | 22.4 | 15.8 | 14.9 | 9.5 | 6.6 | 9.04 | 31.0% | 16.1% |
| B | 6,330 | 13.0 | 8.5 | 19.5 | 15.3 | 19.7 | 12.5 | 11.6 | 12.82 | 43.7% | 24.0% |
| C | 7,558 | 11.9 | 8.5 | 19.4 | 15.9 | 19.3 | 14.7 | 10.4 | 13.02 | 44.3% | 25.0% |
| D | 8,788 | 11.2 | 8.3 | 17.8 | 15.1 | 21.7 | 15.7 | 10.0 | 14.1 | 47.5% | 25.8% |
| F | 15,744 | 7.3 | 5.7 | 15.0 | 14.3 | 23.0 | 21.1 | 13.7 | 18.06 | 57.8% | 34.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,982 | 24.9 | 15.9 | 29.0 | 14.9 | 10.6 | 3.4 | 1.3 | 6.37 | 15.3% | 4.7% |
| B | 5,188 | 16.6 | 11.0 | 24.1 | 17.0 | 18.9 | 9.3 | 2.9 | 9.61 | 31.2% | 12.3% |
| C | 7,524 | 11.0 | 7.8 | 19.5 | 15.0 | 21.0 | 15.7 | 10.1 | 13.5 | 46.7% | 25.7% |
| D | 5,826 | 14.4 | 10.0 | 21.1 | 15.4 | 21.0 | 12.8 | 5.4 | 11.38 | 39.2% | 18.1% |
| F | 9,596 | 10.2 | 8.4 | 16.7 | 14.4 | 23.4 | 18.8 | 8.0 | 15.09 | 50.2% | 26.8% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 16,700 | 17.5 | 10.9 | 21.4 | 15.5 | 15.2 | 10.2 | 9.3 | 10.03 | 34.7% | 19.5% |
| LIMITED | 11,524 | 13.5 | 9.4 | 20.4 | 15.9 | 19.9 | 13.4 | 7.6 | 11.98 | 40.8% | 21.0% |
| POOR | 24,929 | 8.8 | 6.6 | 16.1 | 14.6 | 22.5 | 19.1 | 12.4 | 16.37 | 53.9% | 31.4% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,322 | 23.7 | 18.0 | 33.0 | 15.4 | 6.4 | 3.0 | 0.4 | 5.9 | 9.8% | 3.4% |
| GAME_SPREAD | 6,963 | 22.8 | 15.3 | 32.0 | 16.9 | 9.1 | 3.3 | 0.7 | 6.69 | 13.1% | 4.0% |
| MATCH_WINNER | 38,116 | 15.7 | 10.8 | 22.1 | 15.2 | 18.6 | 12.0 | 5.5 | 10.3 | 36.1% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 17,143 | 28.3 | 16.8 | 30.7 | 12.7 | 8.8 | 2.3 | 0.3 | 5.58 | 11.4% | 2.6% |
| TOTAL_GAMES | 11,667 | 9.7 | 10.8 | 36.4 | 25.7 | 10.4 | 4.2 | 2.9 | 9.14 | 17.5% | 7.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,726 | 24.4 | 28.8 | 33.3 | 8.1 | 4.0 | 1.2 | 0.3 | 4.79 | 5.4% | 1.5% |
| GAME_SPREAD | 9,579 | 46.6 | 15.8 | 25.2 | 7.4 | 2.4 | 1.9 | 0.6 | 3.33 | 4.9% | 2.5% |
| TOTAL_GAMES | 17,101 | 6.5 | 9.8 | 40.9 | 29.8 | 7.3 | 3.3 | 2.3 | 9.15 | 12.9% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,762 | 23.8 | 16.6 | 34.7 | 14.8 | 6.9 | 2.7 | 0.5 | 6.05 | 10.1% | 3.2% |
| GAME_SPREAD | 9,588 | 20.3 | 13.4 | 28.4 | 20.2 | 12.2 | 4.3 | 1.1 | 7.71 | 17.6% | 5.5% |
| TOTAL_GAMES | 17,140 | 10.0 | 10.9 | 36.5 | 24.3 | 11.3 | 4.4 | 2.6 | 9.01 | 18.3% | 7.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 53,153 | 45.0% | 25.4% | 13.23 | 35.5% | 15.2% | 10.72 |
| gen1_elo | 53,153 | 44.6% | 25.2% | 13.01 | 34.9% | 15.0% | 10.51 |
| gen1_sr | 53,153 | 52.6% | 31.7% | 16.01 | 44.0% | 21.5% | 13.0 |
| gen2 | 53,153 | 51.4% | 31.7% | 15.56 | 43.9% | 23.0% | 12.85 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,388 | 15.4 | 10.4 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.72 | 35.5% | 15.4% |
| STALE | 32,765 | 10.7 | 7.4 | 17.0 | 13.9 | 19.3 | 17.0 | 14.7 | 15.41 | 51.0% | 31.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 31,584 | 16.3 | 11.1 | 22.6 | 15.3 | 18.2 | 11.5 | 5.0 | 9.99 | 34.7% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 91,269 | 31584 | 23860 | 35825 | 25.3 | 149.9 | 1451.1 |
| ge_15pp | 37,702 | 10961 | 8518 | 18223 | 29.1 | 453.9 | 1451.1 |
| ge_25pp | 20,183 | 5207 | 3724 | 11252 | 35.0 | 595.9 | 1431.1 |
| lt_10pp | 39,718 | 15804 | 11272 | 12642 | 22.8 | 49.7 | 1421.7 |

Current slate `SL-20261112T212133Z-c10587d3`: 258 priced rows, quote age at build {'median': 49.2, 'max': 59.3}, freshness {'STALE': 258}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 52 | 0.0 | 0.0 | 34.6 | 9.6 | 32.7 | 19.2 | 3.9 | 18.34 | 55.8% | 23.1% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 5,096 | 19.1 | 11.1 | 25.7 | 18.3 | 17.8 | 7.1 | 1.0 | 8.79 | 25.8% | 8.1% |
| KALSHI_LONE_OUTLIER | 32 | 6.2 | 6.2 | 75.0 | 6.2 | 3.1 | 3.1 | 0.0 | 6.16 | 6.2% | 3.1% |
| MARKETS_AGREE | 1,083 | 66.3 | 33.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,315 | 0.0 | 2.2 | 38.4 | 26.0 | 23.7 | 8.8 | 0.9 | 11.66 | 33.4% | 9.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 53,153 | 8607 (16.2%) | 26.9% | 0.9% | {"EXTERNAL_STALE": 5096, "AGREES_WITH_KALSHI": 2315, "ALL_AGREE": 1083, "SUPPORTS_MODEL_DIRECTION": 50, "AGREES_WITH_MODEL": 32, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 23,942 | 2120 (8.8%) | 36.5% | 1.5% | {"EXTERNAL_STALE": 1316, "AGREES_WITH_KALSHI": 773, "SUPPORTS_MODEL_DIRECTION": 29, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 13,514 | 648 (4.8%) | 34.6% | 2.0% | {"EXTERNAL_STALE": 411, "AGREES_WITH_KALSHI": 224, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 6,135 | 616 (10.0%) | 35.2% | 2.1% | {"EXTERNAL_STALE": 386, "AGREES_WITH_KALSHI": 217, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 21,145 | 4946 (23.4%) | 19.0% | 0.9% | {"EXTERNAL_STALE": 2848, "ALL_AGREE": 1083, "AGREES_WITH_KALSHI": 940, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 28, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 10,424 | 10.6 | 7.6 | 18.9 | 14.3 | 21.8 | 16.4 | 10.3 | 14.42 | 48.6% | 26.8% |
| 4-10x | 7,195 | 10.9 | 8.7 | 18.0 | 14.8 | 21.5 | 14.7 | 11.4 | 14.12 | 47.6% | 26.1% |
| <2x | 26,995 | 14.5 | 9.6 | 19.9 | 15.9 | 17.6 | 13.4 | 9.2 | 11.72 | 40.2% | 22.6% |
| >=10x | 8,539 | 10.1 | 6.5 | 15.2 | 14.2 | 21.8 | 19.0 | 13.3 | 16.52 | 54.0% | 32.2% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 13,969 | 12.3 | 8.6 | 19.6 | 16.0 | 19.2 | 13.7 | 10.5 | 12.85 | 43.4% | 24.2% |
| 300-1000 | 11,584 | 11.5 | 8.7 | 17.8 | 15.1 | 20.6 | 16.5 | 10.0 | 13.94 | 47.0% | 26.5% |
| <300 | 16,882 | 8.1 | 5.9 | 15.1 | 14.4 | 22.9 | 20.0 | 13.6 | 17.47 | 56.5% | 33.7% |
| >=3000 | 10,718 | 20.9 | 12.7 | 24.0 | 15.4 | 14.0 | 7.5 | 5.4 | 7.92 | 26.9% | 12.9% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1642 | 0.5469 | 0.4077 | 0.4762 | +0.071 | -0.069 | 0.0035 ± 0.0038 |
| ratio 4-10x | 1118 | 0.5713 | 0.4273 | 0.4839 | +0.087 | -0.057 | 0.0103 ± 0.0048 |
| ratio <2x | 3989 | 0.5343 | 0.4115 | 0.4307 | +0.104 | -0.019 | 0.0151 ± 0.0023 |
| ratio >=10x | 1391 | 0.5576 | 0.3862 | 0.4321 | +0.126 | -0.046 | 0.0178 ± 0.0048 |
| thinner_sample 1000-3000 | 2237 | 0.5394 | 0.4125 | 0.4408 | +0.099 | -0.028 | 0.0133 ± 0.0031 |
| thinner_sample 300-1000 | 1854 | 0.5591 | 0.4192 | 0.4676 | +0.091 | -0.048 | 0.0061 ± 0.0036 |
| thinner_sample <300 | 2671 | 0.5517 | 0.3847 | 0.441 | +0.111 | -0.056 | 0.0156 ± 0.0034 |
| thinner_sample >=3000 | 1378 | 0.5275 | 0.4339 | 0.4434 | +0.084 | -0.009 | 0.0142 ± 0.0031 |
| data_status ADEQUATE | 2195 | 0.5314 | 0.429 | 0.4383 | +0.093 | -0.009 | 0.0152 ± 0.0026 |
| data_status LIMITED | 1979 | 0.5463 | 0.4137 | 0.4598 | +0.086 | -0.046 | 0.0082 ± 0.0034 |
| data_status POOR | 3966 | 0.5537 | 0.3947 | 0.4463 | +0.107 | -0.052 | 0.0133 ± 0.0027 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1173 | 0.1969 | 0.1969 | -0.0000 ± 0.0004 | 0.5733 | 0.5735 | 0.5017 | 0.4865 | 0.4919 | -0.099 ± 0.0137 | -0.0087 (8) |
| 3-5 | 752 | 0.2082 | 0.2076 | +0.0005 ± 0.0013 | 0.6022 | 0.5995 | 0.5004 | 0.4606 | 0.4734 | -0.099 ± 0.0171 | 0.01 (3) |
| 5-10 | 1758 | 0.2022 | 0.2004 | +0.0018 ± 0.0016 | 0.5907 | 0.5839 | 0.5083 | 0.4344 | 0.4579 | -0.091 ± 0.011 | -0.0143 (7) |
| 10-15 | 1415 | 0.2188 | 0.2094 | +0.0094 ± 0.003 | 0.6293 | 0.6021 | 0.5242 | 0.4008 | 0.4233 | -0.104 ± 0.0124 | -0.055 (6) |
| 15-25 | 1802 | 0.2254 | 0.2061 | +0.0193 ± 0.0042 | 0.646 | 0.595 | 0.5705 | 0.3761 | 0.4234 | -0.102 ± 0.0108 | -0.0045 (11) |
| 25-40 | 1028 | 0.2249 | 0.204 | +0.0210 ± 0.0084 | 0.64 | 0.5885 | 0.6437 | 0.3339 | 0.4543 | -0.065 ± 0.0131 | -0.06 (2) |
| 40+ | 212 | 0.3052 | 0.1675 | +0.1377 ± 0.0255 | 0.8164 | 0.5038 | 0.7246 | 0.2672 | 0.3538 | -0.087 ± 0.0246 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5931 | 0.1871 | 0.188 | -0.0009 ± 0.0002 | 0.5507 | 0.5518 | 0.4911 | 0.4758 | 0.5067 | -0.021 ± 0.0057 | -0.01 (28) |
| 3-5 | 4020 | 0.1992 | 0.1972 | +0.0020 ± 0.0006 | 0.5794 | 0.5727 | 0.4801 | 0.4403 | 0.4348 | -0.059 ± 0.0071 | 0.005 (6) |
| 5-10 | 8826 | 0.2007 | 0.1964 | +0.0043 ± 0.0007 | 0.5871 | 0.573 | 0.4817 | 0.4079 | 0.4157 | -0.050 ± 0.0048 | -0.0114 (22) |
| 10-15 | 7177 | 0.2014 | 0.1856 | +0.0157 ± 0.0013 | 0.5891 | 0.545 | 0.4843 | 0.3604 | 0.3593 | -0.062 ± 0.0051 | -0.0379 (19) |
| 15-25 | 9251 | 0.2058 | 0.1659 | +0.0399 ± 0.0017 | 0.6034 | 0.4936 | 0.4973 | 0.3017 | 0.2983 | -0.069 ± 0.0042 | -0.0043 (51) |
| 25-40 | 7248 | 0.2225 | 0.1235 | +0.0990 ± 0.0026 | 0.6391 | 0.381 | 0.5233 | 0.2092 | 0.2125 | -0.059 ± 0.004 | -0.0733 (3) |
| 40+ | 4994 | 0.3794 | 0.0442 | +0.3352 ± 0.0034 | 0.9887 | 0.171 | 0.6277 | 0.1019 | 0.0579 | -0.076 ± 0.0028 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 937 | 0.2014 | 0.2018 | -0.0004 ± 0.0005 | 0.5823 | 0.5837 | 0.509 | 0.494 | 0.5208 | -0.093 ± 0.0157 | -0.0117 (6) |
| 3-5 | 680 | 0.2131 | 0.2103 | +0.0028 ± 0.0014 | 0.6099 | 0.6036 | 0.5179 | 0.4783 | 0.4603 | -0.124 ± 0.0189 | 0.01 (3) |
| 5-10 | 1511 | 0.2042 | 0.2026 | +0.0016 ± 0.0017 | 0.594 | 0.5898 | 0.5373 | 0.4629 | 0.4904 | -0.084 ± 0.012 | -0.01 (4) |
| 10-15 | 1319 | 0.2156 | 0.2079 | +0.0077 ± 0.0031 | 0.624 | 0.6014 | 0.5568 | 0.4324 | 0.4663 | -0.102 ± 0.0131 | -0.04 (5) |
| 15-25 | 1896 | 0.2324 | 0.2108 | +0.0216 ± 0.0041 | 0.6613 | 0.6052 | 0.5835 | 0.3878 | 0.4325 | -0.100 ± 0.0108 | -0.0183 (12) |
| 25-40 | 1317 | 0.2661 | 0.1999 | +0.0663 ± 0.0077 | 0.7424 | 0.5802 | 0.6586 | 0.3447 | 0.3979 | -0.109 ± 0.0124 | -0.008 (5) |
| 40+ | 480 | 0.3736 | 0.1597 | +0.2139 ± 0.0183 | 1.0152 | 0.4842 | 0.7315 | 0.2427 | 0.2812 | -0.088 ± 0.0176 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5098 | 0.1901 | 0.1903 | -0.0002 ± 0.0002 | 0.5552 | 0.5554 | 0.5067 | 0.4916 | 0.5067 | -0.040 ± 0.0063 | -0.0154 (26) |
| 3-5 | 3521 | 0.1947 | 0.1938 | +0.0009 ± 0.0006 | 0.5668 | 0.564 | 0.511 | 0.4713 | 0.4786 | -0.044 ± 0.0076 | 0.01 (5) |
| 5-10 | 7870 | 0.1954 | 0.1921 | +0.0033 ± 0.0007 | 0.575 | 0.5625 | 0.5059 | 0.4316 | 0.449 | -0.038 ± 0.005 | -0.0117 (6) |
| 10-15 | 6530 | 0.2024 | 0.1902 | +0.0122 ± 0.0014 | 0.5945 | 0.5569 | 0.5061 | 0.3822 | 0.3959 | -0.050 ± 0.0055 | -0.0189 (18) |
| 15-25 | 9334 | 0.2152 | 0.1785 | +0.0367 ± 0.0017 | 0.6271 | 0.5247 | 0.5226 | 0.327 | 0.3334 | -0.060 ± 0.0044 | -0.014 (52) |
| 25-40 | 8401 | 0.25 | 0.1374 | +0.1126 ± 0.0026 | 0.7063 | 0.4194 | 0.559 | 0.2417 | 0.2264 | -0.077 ± 0.004 | -0.0095 (20) |
| 40+ | 6693 | 0.4014 | 0.0595 | +0.3420 ± 0.0034 | 1.0576 | 0.2135 | 0.6544 | 0.119 | 0.0808 | -0.073 ± 0.0029 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1148 | 0.1964 | 0.1976 | -0.0011 ± 0.0005 | 0.5726 | 0.5752 | 0.5004 | 0.4849 | 0.5209 | -0.061 ± 0.0137 | -0.0191 (11) |
| 3-5 | 824 | 0.2093 | 0.2081 | +0.0013 ± 0.0013 | 0.6057 | 0.6014 | 0.4962 | 0.4566 | 0.4624 | -0.105 ± 0.0166 | 0.002 (5) |
| 5-10 | 1760 | 0.2026 | 0.1981 | +0.0045 ± 0.0016 | 0.5906 | 0.5781 | 0.5101 | 0.4364 | 0.442 | -0.107 ± 0.0109 | -0.01 (10) |
| 10-15 | 1458 | 0.2114 | 0.2016 | +0.0098 ± 0.0029 | 0.6132 | 0.585 | 0.5376 | 0.4143 | 0.4383 | -0.105 ± 0.0119 | -0.0286 (7) |
| 15-25 | 1711 | 0.231 | 0.2116 | +0.0193 ± 0.0043 | 0.6593 | 0.6073 | 0.5796 | 0.3856 | 0.4325 | -0.104 ± 0.0112 | -0.03 (1) |
| 25-40 | 1012 | 0.2169 | 0.2067 | +0.0103 ± 0.0085 | 0.6237 | 0.5945 | 0.6517 | 0.3419 | 0.4783 | -0.057 ± 0.0132 | -0.0267 (3) |
| 40+ | 227 | 0.3091 | 0.1798 | +0.1294 ± 0.0253 | 0.8335 | 0.5309 | 0.7365 | 0.28 | 0.3789 | -0.075 ± 0.0259 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5750 | 0.1866 | 0.1872 | -0.0005 ± 0.0002 | 0.5492 | 0.5496 | 0.4864 | 0.471 | 0.485 | -0.037 ± 0.0058 | -0.0189 (44) |
| 3-5 | 4127 | 0.2052 | 0.2035 | +0.0017 ± 0.0006 | 0.5956 | 0.5898 | 0.4806 | 0.441 | 0.4398 | -0.055 ± 0.0071 | -0.0073 (22) |
| 5-10 | 8947 | 0.1956 | 0.1901 | +0.0055 ± 0.0007 | 0.5746 | 0.5573 | 0.4847 | 0.4108 | 0.41 | -0.057 ± 0.0046 | -0.0117 (42) |
| 10-15 | 7190 | 0.1946 | 0.1788 | +0.0157 ± 0.0012 | 0.5742 | 0.5295 | 0.4955 | 0.3721 | 0.3702 | -0.063 ± 0.005 | -0.0136 (14) |
| 15-25 | 9281 | 0.2108 | 0.1717 | +0.0391 ± 0.0017 | 0.6151 | 0.5066 | 0.5093 | 0.3146 | 0.3123 | -0.068 ± 0.0043 | -0.0533 (3) |
| 25-40 | 7238 | 0.2166 | 0.1232 | +0.0934 ± 0.0026 | 0.6264 | 0.3795 | 0.5247 | 0.2092 | 0.2206 | -0.052 ± 0.004 | -0.02 (4) |
| 40+ | 4914 | 0.3879 | 0.0481 | +0.3398 ± 0.0035 | 1.0112 | 0.1809 | 0.6365 | 0.1073 | 0.0637 | -0.076 ± 0.003 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1623 | 0.196 | 0.1956 | +0.0004 ± 0.0004 | 0.57 | 0.5688 | 0.5069 | 0.4919 | 0.4874 | -0.076 ± 0.0112 | -0.0221 (56) |
| 3-5 | 1141 | 0.1879 | 0.1878 | +0.0000 ± 0.001 | 0.5531 | 0.5516 | 0.4986 | 0.4588 | 0.4768 | -0.055 ± 0.0131 | -0.0194 (34) |
| 5-10 | 2317 | 0.1992 | 0.194 | +0.0052 ± 0.0014 | 0.5877 | 0.5709 | 0.5083 | 0.4346 | 0.4368 | -0.078 ± 0.0094 | -0.005 (78) |
| 10-15 | 1602 | 0.2152 | 0.2022 | +0.0130 ± 0.0028 | 0.6245 | 0.5878 | 0.5449 | 0.4222 | 0.4295 | -0.090 ± 0.0115 | 0.0012 (66) |
| 15-25 | 2092 | 0.2322 | 0.2082 | +0.0240 ± 0.0039 | 0.6628 | 0.6002 | 0.5922 | 0.3972 | 0.4345 | -0.088 ± 0.0101 | -0.0214 (59) |
| 25-40 | 1215 | 0.2418 | 0.2118 | +0.0299 ± 0.008 | 0.69 | 0.6068 | 0.6881 | 0.3764 | 0.4848 | -0.082 ± 0.0125 | -0.0252 (27) |
| 40+ | 451 | 0.3285 | 0.1978 | +0.1308 ± 0.0201 | 0.9384 | 0.5773 | 0.8078 | 0.3308 | 0.4479 | -0.092 ± 0.0188 | -0.1137 (8) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5856 | 0.1767 | 0.1767 | +0.0001 ± 0.0002 | 0.5236 | 0.5229 | 0.5089 | 0.4937 | 0.4997 | -0.042 ± 0.0055 | -0.0154 (103) |
| 3-5 | 4010 | 0.1934 | 0.1924 | +0.0010 ± 0.0006 | 0.5648 | 0.5621 | 0.502 | 0.4622 | 0.4703 | -0.041 ± 0.007 | -0.0212 (73) |
| 5-10 | 8185 | 0.1967 | 0.1901 | +0.0066 ± 0.0007 | 0.5804 | 0.5603 | 0.5022 | 0.4286 | 0.4217 | -0.062 ± 0.0049 | -0.0084 (134) |
| 10-15 | 5627 | 0.211 | 0.1941 | +0.0169 ± 0.0015 | 0.6141 | 0.5691 | 0.5378 | 0.4149 | 0.4064 | -0.073 ± 0.0059 | -0.0057 (111) |
| 15-25 | 6917 | 0.2318 | 0.1997 | +0.0322 ± 0.0021 | 0.6666 | 0.5786 | 0.5765 | 0.3812 | 0.3968 | -0.067 ± 0.0054 | -0.026 (108) |
| 25-40 | 4448 | 0.2578 | 0.1907 | +0.0671 ± 0.0041 | 0.7288 | 0.5549 | 0.6401 | 0.3279 | 0.3797 | -0.062 ± 0.0064 | -0.0277 (53) |
| 40+ | 2005 | 0.3693 | 0.1596 | +0.2097 ± 0.0092 | 1.0378 | 0.4754 | 0.7407 | 0.2411 | 0.2913 | -0.058 ± 0.0085 | -0.054 (15) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 8140 | 1.025 ± 0.031 | 1.087 | 0.168 | 0.1711 | 0.2156 | 0.203 |
| gen2 | 8140 | 0.822 ± 0.028 | 1.066 | 0.174 | 0.1713 | 0.233 | 0.2029 |
| gen1_elo | 8140 | 1.009 ± 0.03 | 1.077 | 0.1744 | 0.1712 | 0.2147 | 0.2031 |
| gen1_sr | 8140 | 1.008 ± 0.037 | 1.113 | 0.1335 | 0.1728 | 0.2292 | 0.2027 |
| gen1_ledger | 10441 | 0.868 ± 0.023 | 1.064 | 0.1905 | 0.1773 | 0.2171 | 0.1999 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 37,702)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 9,131 | 24.2% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 8,861 | 23.5% |
| BOOK_QUALITY | execution | 6,346 | 16.8% |
| POOR_DATA | data | 4,296 | 11.4% |
| LIMITED_DATA | data | 2,260 | 6.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 2,207 | 5.9% |
| IDENTITY_AMBIGUOUS | mapping | 1,541 | 4.1% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,431 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 1,053 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 575 | 1.5% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 24.2%, coverage 23.5%, data 17.4%, execution 16.8%, market_freshness/coverage 8.6%, mapping 4.1%, model_calibration_or_unknown 3.8%, model_calibration 1.5%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 95.1%, LOW_DATA_QUALITY 72.2%, THIN_PLAYER_HISTORY 60.3%, STALE_PLAYER_DATA 52.0%, STALE_KALSHI_QUOTE 48.3%, MODEL_INTERNAL_DISAGREEMENT 41.8%, ASYMMETRIC_SAMPLE_SIZE 33.2%, WIDE_SPREAD 23.4%, MODEL_HIGH_UNCERTAINTY 18.7%, PLAYER_IDENTITY_RISK 15.0%, LEVEL_TRANSFER_RISK 9.3%, LOW_DISPLAYED_LIQUIDITY 8.6%, EVENT_MAPPING_RISK 7.0%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.1%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.8%, POST_SETTLEMENT_OBSERVATION 23.5%, POSSIBLE_IN_PLAY_QUOTE 6.3%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 20,183)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,135 | 35.4% |
| STALE_QUOTE | market_freshness | 4,058 | 20.1% |
| BOOK_QUALITY | execution | 3,275 | 16.2% |
| POOR_DATA | data | 1,821 | 9.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,191 | 5.9% |
| IDENTITY_AMBIGUOUS | mapping | 855 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 693 | 3.4% |
| LIMITED_DATA | data | 668 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 347 | 1.7% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 139 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 35.4%, market_freshness 20.1%, execution 16.2%, data 12.3%, market_freshness/coverage 9.3%, mapping 4.2%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.2%, START_UNVERIFIABLE 97.3%, LOW_DATA_QUALITY 75.3%, THIN_PLAYER_HISTORY 62.4%, STALE_KALSHI_QUOTE 55.8%, STALE_PLAYER_DATA 45.3%, MODEL_INTERNAL_DISAGREEMENT 41.9%, ASYMMETRIC_SAMPLE_SIZE 34.4%, WIDE_SPREAD 22.5%, MODEL_HIGH_UNCERTAINTY 19.4%, PLAYER_IDENTITY_RISK 17.8%, LOW_DISPLAYED_LIQUIDITY 8.5%, EVENT_MAPPING_RISK 8.4%, LEVEL_TRANSFER_RISK 8.1%, MODEL_CALIBRATION_OUTLIER 4.6%, EXTERNAL_MARKET_REJECTION 1.7%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 38.2%, POST_SETTLEMENT_OBSERVATION 35.4%, POSSIBLE_IN_PLAY_QUOTE 6.4%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 16235, "IDENTITY_AMBIGUOUS": 3948}; ticker orientation: {"VERIFIED": 20183}.

Checks: discipline:AMBIGUOUS 1295, discipline:PASS 18888, identity_confidence:AMBIGUOUS 3595, identity_confidence:PASS 16588, level_mapping:NA 1307, level_mapping:PASS 18876, market_pair:AMBIGUOUS 517, market_pair:NA 427, market_pair:PASS 19239, model_complement:NA 389, model_complement:PASS 19794, namesake:AMBIGUOUS 6, namesake:PASS 20177, physical_match_id:NA 6669, physical_match_id:PASS 13514, player_ids:PASS 20183, same_pair_other_event:PASS 20183, ticker_orientation:PASS 20183

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,617 | 3.7% | 3.1% | 1.2% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 24, "market_freshness/coverage": 22} | 5.47 | 0.2222 / 0.2184 (867) | 25.7% | 2.4% | 3.2% | 3.0% |
| CHALLENGER | 13,376 | 16.6% | 6.0% | 11.0% | {"coverage": 1363, "market_freshness": 274, "market_freshness/coverage": 242, "data": 164, "model_calibration_or_unknown": 81, "execution": 41, "model_calibration": 40, "mapping": 17, "possible_market_error": 1} | 7.34 | 0.2215 / 0.2112 (3102) | 41.8% | 13.7% | 4.0% | 22.9% |
| DOUBLES | 2,796 | 46.3% | 46.4% | 6.4% | {"execution": 716, "mapping": 390, "market_freshness": 106, "market_freshness/coverage": 76, "coverage": 7} | 23.2 | 0.2983 / 0.2323 (704) | 8.4% | 0.0% | 100.0% | 6.5% |
| ITF_MEN | 26,971 | 25.4% | 17.7% | 33.9% | {"coverage": 2417, "market_freshness": 1432, "execution": 1046, "data": 1007, "market_freshness/coverage": 695, "mapping": 232, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.75 | 0.2176 / 0.1976 (5697) | 42.4% | 70.0% | 14.4% | 21.8% |
| ITF_WOMEN | 33,840 | 26.6% | 18.7% | 44.5% | {"coverage": 3269, "market_freshness": 1985, "execution": 1389, "data": 1217, "market_freshness/coverage": 792, "mapping": 210, "model_calibration_or_unknown": 98, "model_calibration": 23} | 12.45 | 0.2031 / 0.1935 (6587) | 43.0% | 57.3% | 10.1% | 22.1% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,931 | 5.9% | 5.0% | 1.5% | {"market_freshness": 111, "model_calibration_or_unknown": 52, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.65 | 0.2315 / 0.221 (812) | 30.3% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.5% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 523 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 16.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 969 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFMATCH-26NOV12VALRAT-RAT` | ITF_MEN | gen1_ledger | 92% / 4% | +88 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 10 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1333.0, ratio 3.64); no external reference |
| 6 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 7 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 8 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 9 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 10 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 11 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 12 | `KXITFMATCH-26NOV10KOUPOR-POR` | ITF_MEN | fair_v1 | 87% / 2% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.9h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 305 min (STALE); data POOR (grade D, thinner serve sample 1554.0, ratio 1.02); no external reference |
| 13 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 14 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 194 min (STALE); no external reference |
| 17 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 18 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 19 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 20 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 151 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 22 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 23 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 24 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 25 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 26 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 27 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 454 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 28 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 29 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 30 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 31 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 32 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 33 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 34 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 35 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 36 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 37 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 38 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 39 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 40 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 41 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 42 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 43 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 44 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 45 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 46 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 47 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 48 | `KXITFWMATCH-26NOV11CORROJ-ROJ` | ITF_WOMEN | fair_v1 | 87% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade D, thinner serve sample 531.0, ratio 1.04); no external reference |
| 49 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 50 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9734, "by_level_share_of_ge_25pp": {"ATP": 0.0121, "CHALLENGER": 0.1101, "DOUBLES": 0.0642, "ITF_MEN": 0.3389, "ITF_WOMEN": 0.4451, "OTHER": 0.0006, "WTA": 0.0145, "WTA125": 0.0145}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5575, "share_primary_cause_market_settled_or_in_play": 0.4468, "share_primary_cause_stale_quote_only": 0.2011}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 20183, "identity_ambiguous_share": 0.1956, "ticker_orientation": {"VERIFIED": 20183}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 13514, "with_external": 648, "coverage": 0.048, "external_status": {"EXTERNAL_STALE": 411, "AGREES_WITH_KALSHI": 224, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 411, "MODEL_LONE_OUTLIER": 224, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3457, "share_external_supports_model": 0.0201}, "pregame_clean_ge_25pp": {"n": 6135, "with_external": 616, "coverage": 0.1004, "external_status": {"EXTERNAL_STALE": 386, "AGREES_WITH_KALSHI": 217, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 386, "MODEL_LONE_OUTLIER": 217, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3523, "share_external_supports_model": 0.0211}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 480.0, "median_sample_ratio": 2.46, "median_min_matches": 18.0, "median_max_days_since_last": 246.0, "share_severe_asymmetry": 0.2069, "data_status": {"POOR": 11500, "LIMITED": 5065, "ADEQUATE": 3618}, "comparison_lt_10pp": {"median_thinner_serve_points": 1667.0, "median_sample_ratio": 1.71, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1642, "model_minus_observed": 0.0707, "kalshi_minus_observed": -0.0686, "brier_diff_model_minus_kalshi": 0.0035}, "4-10x": {"n": 1118, "model_minus_observed": 0.0874, "kalshi_minus_observed": -0.0566, "brier_diff_model_minus_kalshi": 0.0103}, "<2x": {"n": 3989, "model_minus_observed": 0.1036, "kalshi_minus_observed": -0.0192, "brier_diff_model_minus_kalshi": 0.0151}, ">=10x": {"n": 1391, "model_minus_observed": 0.1255, "kalshi_minus_observed": -0.0459, "brier_diff_model_minus_kalshi": 0.0178}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 8140, "model": {"intercept": -0.562, "slope": 0.822, "slope_se": 0.028}, "kalshi_mid_same_rows": {"intercept": 0.17, "slope": 1.066, "slope_se": 0.031}, "mean_extremity_model": 0.174, "mean_extremity_kalshi": 0.1713, "model_brier": 0.233, "kalshi_brier": 0.2029, "brier_diff_model_minus_kalshi": 0.0301, "brier_diff_se": 0.0021, "model_logloss": 0.6633, "kalshi_logloss": 0.5879}, "fair_v1": {"n": 8140, "model": {"intercept": -0.472, "slope": 1.025, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.215, "slope": 1.087, "slope_se": 0.031}, "mean_extremity_model": 0.168, "mean_extremity_kalshi": 0.1711, "model_brier": 0.2156, "kalshi_brier": 0.203, "brier_diff_model_minus_kalshi": 0.0126, "brier_diff_se": 0.0017, "model_logloss": 0.6203, "kalshi_logloss": 0.588}, "gen1_elo": {"n": 8140, "model": {"intercept": -0.461, "slope": 1.009, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.216, "slope": 1.077, "slope_se": 0.031}, "mean_extremity_model": 0.1744, "mean_extremity_kalshi": 0.1712, "model_brier": 0.2147, "kalshi_brier": 0.2031, "brier_diff_model_minus_kalshi": 0.0116, "brier_diff_se": 0.0017, "model_logloss": 0.619, "kalshi_logloss": 0.5881}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2542, "share_ge_15": 0.4504, "median_abs_gap": 13.23, "n": 53153}, "gen1_elo": {"share_ge_25": 0.252, "share_ge_15": 0.4459, "median_abs_gap": 13.01, "n": 53153}, "gen1_sr": {"share_ge_25": 0.3168, "share_ge_15": 0.5257, "median_abs_gap": 16.01, "n": 53153}, "gen2": {"share_ge_25": 0.3167, "share_ge_15": 0.5139, "median_abs_gap": 15.56, "n": 53153}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1518, "share_ge_15": 0.3554, "median_abs_gap": 10.72, "n": 40410}, "gen1_elo": {"share_ge_25": 0.1502, "share_ge_15": 0.3495, "median_abs_gap": 10.51, "n": 40410}, "gen1_sr": {"share_ge_25": 0.215, "share_ge_15": 0.4401, "median_abs_gap": 13.0, "n": 40413}, "gen2": {"share_ge_25": 0.2302, "share_ge_15": 0.4393, "median_abs_gap": 12.85, "n": 40414}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.47, "share_ge_25_all": 0.037, "share_ge_25_pregame_clean": 0.031}, "WTA": {"median_abs_gap_pregame_clean": 7.65, "share_ge_25_all": 0.0592, "share_ge_25_pregame_clean": 0.0503}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2339, "share_within_10pp_all": 0.4352, "share_within_10pp_pregame_clean": 0.4901, "corr_model_vs_mid_pregame_clean": 0.85}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1173, "model_brier": 0.1969, "kalshi_brier": 0.1969, "brier_diff_model_minus_kalshi": -0.0}, "10-15": {"n_settled": 1415, "model_brier": 0.2188, "kalshi_brier": 0.2094, "brier_diff_model_minus_kalshi": 0.0094}, "15-25": {"n_settled": 1802, "model_brier": 0.2254, "kalshi_brier": 0.2061, "brier_diff_model_minus_kalshi": 0.0193}, "25-40": {"n_settled": 1028, "model_brier": 0.2249, "kalshi_brier": 0.204, "brier_diff_model_minus_kalshi": 0.021}, "3-5": {"n_settled": 752, "model_brier": 0.2082, "kalshi_brier": 0.2076, "brier_diff_model_minus_kalshi": 0.0005}, "40+": {"n_settled": 212, "model_brier": 0.3052, "kalshi_brier": 0.1675, "brier_diff_model_minus_kalshi": 0.1377}, "5-10": {"n_settled": 1758, "model_brier": 0.2022, "kalshi_brier": 0.2004, "brier_diff_model_minus_kalshi": 0.0018}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'NO_SKILL:gen2|WTA', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.562, "slope": 0.822, "slope_se": 0.028}, "kalshi_slope": {"intercept": 0.17, "slope": 1.066, "slope_se": 0.031}, "n": 8140}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.502, "slope": 0.868, "slope_se": 0.023}, "kalshi_slope": {"intercept": 0.15, "slope": 1.064, "slope_se": 0.027}, "n": 10441}, "NO_SKILL:gen2|WTA": {"n_settled": 346, "model_brier": 0.25, "kalshi_brier": 0.2262, "brier_diff_model_minus_kalshi": 0.0238, "brier_diff_se": 0.0089, "corr_model_outcome": 0.2572, "corr_kalshi_outcome": 0.3102}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 704, "model_brier": 0.2983, "kalshi_brier": 0.2323, "brier_diff_model_minus_kalshi": 0.0661, "brier_diff_se": 0.011, "corr_model_outcome": 0.1074, "corr_kalshi_outcome": 0.2778}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
