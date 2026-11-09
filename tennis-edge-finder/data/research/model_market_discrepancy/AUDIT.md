# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-09T07:52Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 82,725): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 19.1%, 25-40 13.6%, 40+ 8.1%; median gap 11.85 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.7%, Challenger 10.9%, doubles 6.7%). Main tour: ATP 3.8% and WTA 6.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 18,006): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.5%, STALE_QUOTE 19.4%, BOOK_QUALITY 17.3%, POOR_DATA 9.1%, POSSIBLY_IN_PLAY_QUOTE 5.8%, IDENTITY_AMBIGUOUS 4.3%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.5%, market_freshness 19.4%, execution 17.3%, data 12.5%, market_freshness/coverage 9.3%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 53.9% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.8% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 18,006 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.1% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.7% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 494.0 points vs 1736.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.027, Gen-2 0.817, Gen-1 ledger 0.867 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 926 model 0.2231 vs Kalshi 0.2063; n 191 model 0.296 vs Kalshi 0.1751.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 350,892 model-market comparisons (575,042 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 116,700 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-09T07:32:21.209555+00:00'], shadow board 95,210 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-09T07:32:25.724504+00:00'], Model 4 43,079 rows, 29,240 settled tickers, 10,985 tickers with an external scan.
* By model: {"gen1_ledger": 78704, "gen1_elo": 47855, "fair_v1": 47855, "gen2": 47855, "gen1_sr": 47855, "model4_fundamental": 40426, "model4_conditioned": 40342}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 82,725 | 14.1 | 9.6 | 20.2 | 15.3 | 19.1 | 13.6 | 8.1 | 11.85 | 40.9% | 21.8% |
| MW fair_v1 | 47,855 | 12.8 | 8.6 | 18.7 | 15.4 | 19.6 | 14.8 | 10.0 | 13.06 | 44.5% | 24.9% |
| MW gen1_elo | 47,855 | 12.6 | 8.8 | 19.2 | 15.4 | 19.5 | 14.7 | 9.9 | 12.85 | 44.0% | 24.6% |
| MW gen1_ledger | 34,870 | 15.8 | 10.9 | 22.2 | 15.1 | 18.5 | 12.0 | 5.5 | 10.26 | 36.0% | 17.5% |
| MW gen1_sr | 47,855 | 10.1 | 7.3 | 16.7 | 13.9 | 20.7 | 18.7 | 12.7 | 15.83 | 52.0% | 31.3% |
| MW gen2 | 47,855 | 11.0 | 7.5 | 16.7 | 13.7 | 19.6 | 17.7 | 13.7 | 15.46 | 51.0% | 31.4% |
| all families model4_conditioned | 40,342 | 22.3 | 17.9 | 34.3 | 17.1 | 5.0 | 2.2 | 1.2 | 6.07 | 8.5% | 3.4% |
| all families model4_fundamental | 40,426 | 17.3 | 13.5 | 33.9 | 20.0 | 10.0 | 3.8 | 1.5 | 7.62 | 15.3% | 5.3% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.2%, >=15pp 40.9%, >=20pp 30.1%, >=25pp 21.8%, >=30pp 15.7%, >=40pp 8.1%, >=50pp 3.9%
Executable gap (model outside the book, before fees): median 8.41pp; >=10pp 45.1%, >=25pp 17.2%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,016 | 28.4 | 15.7 | 27.6 | 13.4 | 10.7 | 3.6 | 0.6 | 5.84 | 14.9% | 4.3% |
| CHALLENGER | 7,307 | 16.0 | 9.6 | 20.6 | 15.4 | 16.0 | 11.5 | 10.9 | 10.97 | 38.4% | 22.3% |
| ITF_MEN | 13,505 | 9.8 | 7.3 | 17.1 | 15.0 | 21.2 | 17.2 | 12.4 | 15.31 | 50.8% | 29.6% |
| ITF_WOMEN | 18,630 | 9.5 | 7.0 | 16.0 | 14.8 | 22.3 | 18.4 | 12.0 | 15.95 | 52.7% | 30.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,064 | 16.7 | 13.2 | 24.9 | 20.8 | 16.6 | 6.8 | 1.1 | 8.65 | 24.4% | 7.9% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,016 | 26.8 | 15.6 | 26.0 | 15.6 | 11.4 | 3.9 | 0.8 | 6.07 | 16.0% | 4.7% |
| CHALLENGER | 7,307 | 14.5 | 9.1 | 18.9 | 13.8 | 18.7 | 13.6 | 11.5 | 12.55 | 43.8% | 25.1% |
| ITF_MEN | 13,505 | 8.1 | 6.2 | 15.1 | 13.7 | 20.0 | 20.4 | 16.5 | 17.95 | 56.9% | 36.9% |
| ITF_WOMEN | 18,630 | 7.9 | 5.8 | 14.1 | 12.8 | 20.7 | 21.2 | 17.5 | 19.09 | 59.4% | 38.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,064 | 14.1 | 10.2 | 21.6 | 16.3 | 22.5 | 12.8 | 2.5 | 11.28 | 37.8% | 15.3% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,016 | 23.1 | 14.0 | 25.2 | 15.7 | 14.7 | 6.1 | 1.1 | 7.11 | 21.9% | 7.2% |
| CHALLENGER | 7,307 | 15.0 | 9.6 | 20.5 | 15.7 | 16.1 | 12.0 | 10.9 | 11.37 | 39.1% | 23.0% |
| ITF_MEN | 13,505 | 9.5 | 7.3 | 17.2 | 14.2 | 21.8 | 17.2 | 12.8 | 15.67 | 51.8% | 30.0% |
| ITF_WOMEN | 18,630 | 9.3 | 6.9 | 16.2 | 15.7 | 22.2 | 18.4 | 11.3 | 15.62 | 51.9% | 29.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,064 | 22.7 | 17.0 | 31.9 | 15.4 | 8.7 | 3.3 | 1.0 | 6.12 | 13.0% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,411 | 27.6 | 19.6 | 29.3 | 12.4 | 8.1 | 2.6 | 0.5 | 5.3 | 11.1% | 3.0% |
| CHALLENGER | 4,641 | 22.4 | 14.5 | 27.5 | 14.8 | 13.4 | 5.7 | 1.6 | 7.08 | 20.7% | 7.3% |
| DOUBLES | 2,591 | 4.8 | 4.5 | 12.9 | 11.0 | 20.4 | 24.4 | 22.0 | 23.23 | 66.7% | 46.4% |
| ITF_MEN | 9,977 | 12.9 | 9.6 | 21.4 | 15.6 | 21.6 | 12.9 | 5.9 | 11.77 | 40.5% | 18.8% |
| ITF_WOMEN | 12,046 | 13.4 | 9.2 | 19.9 | 15.6 | 21.5 | 14.9 | 5.5 | 12.26 | 41.9% | 20.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,799 | 23.7 | 16.1 | 31.5 | 17.0 | 8.9 | 2.6 | 0.2 | 6.56 | 11.7% | 2.8% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,891 | 28.9 | 15.9 | 28.0 | 13.3 | 10.4 | 3.2 | 0.3 | 5.67 | 13.9% | 3.5% |
| CHALLENGER | 5,157 | 20.7 | 11.9 | 25.6 | 18.2 | 16.0 | 6.0 | 1.6 | 8.3 | 23.5% | 7.5% |
| ITF_MEN | 9,836 | 12.0 | 8.7 | 20.7 | 17.3 | 22.0 | 14.0 | 5.3 | 12.39 | 41.4% | 19.4% |
| ITF_WOMEN | 13,662 | 11.4 | 8.6 | 18.9 | 17.1 | 24.2 | 15.2 | 4.8 | 13.2 | 44.1% | 20.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,950 | 17.0 | 13.2 | 25.2 | 21.2 | 16.6 | 6.2 | 0.6 | 8.48 | 23.4% | 6.9% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,891 | 27.1 | 16.0 | 26.3 | 15.6 | 11.3 | 3.4 | 0.4 | 5.98 | 15.1% | 3.8% |
| CHALLENGER | 5,157 | 18.3 | 11.5 | 23.8 | 16.2 | 19.1 | 9.4 | 1.8 | 8.99 | 30.3% | 11.2% |
| ITF_MEN | 9,837 | 9.6 | 7.2 | 17.6 | 15.9 | 21.8 | 18.6 | 9.1 | 14.89 | 49.6% | 27.8% |
| ITF_WOMEN | 13,663 | 8.9 | 6.9 | 16.1 | 14.4 | 22.6 | 20.5 | 10.7 | 16.49 | 53.8% | 31.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,950 | 14.3 | 10.3 | 21.8 | 16.5 | 22.6 | 12.5 | 1.9 | 11.05 | 37.0% | 14.4% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,347 | 27.9 | 19.8 | 29.3 | 12.6 | 7.8 | 2.4 | 0.3 | 5.24 | 10.5% | 2.7% |
| CHALLENGER | 4,103 | 23.7 | 15.4 | 28.7 | 15.0 | 12.8 | 4.0 | 0.4 | 6.61 | 17.3% | 4.5% |
| DOUBLES | 2,426 | 4.7 | 4.6 | 13.2 | 11.1 | 20.2 | 24.3 | 22.1 | 23.2 | 66.5% | 46.3% |
| ITF_MEN | 8,577 | 13.7 | 10.2 | 23.0 | 16.1 | 21.6 | 11.4 | 3.9 | 10.83 | 37.0% | 15.3% |
| ITF_WOMEN | 10,329 | 14.0 | 9.8 | 21.0 | 16.1 | 21.6 | 13.8 | 3.6 | 11.44 | 39.1% | 17.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,736 | 24.0 | 16.5 | 31.4 | 17.0 | 8.9 | 2.0 | 0.1 | 6.43 | 11.0% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,591 | 4.8 | 4.5 | 12.9 | 11.0 | 20.4 | 24.4 | 22.0 | 23.23 | 66.7% | 46.4% |
| singles | 32,279 | 16.7 | 11.4 | 22.9 | 15.5 | 18.3 | 11.0 | 4.2 | 9.73 | 33.5% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 9,878 | 12.6 | 9.0 | 19.9 | 15.5 | 19.6 | 14.0 | 9.4 | 12.65 | 43.0% | 23.4% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 31,188 | 13.4 | 8.7 | 18.7 | 15.2 | 19.2 | 14.8 | 10.0 | 12.91 | 44.0% | 24.8% |
| UNKNOWN | 6,376 | 10.5 | 7.5 | 17.1 | 16.3 | 21.5 | 15.9 | 11.1 | 14.32 | 48.6% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 13,637 | 19.4 | 11.8 | 22.4 | 15.9 | 15.0 | 9.2 | 6.3 | 8.92 | 30.4% | 15.5% |
| B | 5,852 | 12.7 | 8.6 | 19.6 | 15.6 | 19.7 | 12.9 | 11.1 | 12.81 | 43.6% | 24.0% |
| C | 6,793 | 12.0 | 8.8 | 19.5 | 15.6 | 18.7 | 14.6 | 10.8 | 12.99 | 44.1% | 25.4% |
| D | 7,719 | 11.7 | 8.3 | 17.8 | 15.2 | 21.8 | 15.8 | 9.4 | 13.92 | 47.0% | 25.2% |
| F | 13,854 | 7.4 | 5.6 | 14.9 | 14.7 | 23.4 | 20.8 | 13.2 | 17.82 | 57.5% | 34.0% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,398 | 24.6 | 16.1 | 29.0 | 15.0 | 10.6 | 3.4 | 1.3 | 6.36 | 15.2% | 4.7% |
| B | 4,871 | 16.6 | 10.8 | 24.3 | 16.8 | 18.9 | 9.6 | 3.0 | 9.62 | 31.4% | 12.6% |
| C | 6,853 | 11.0 | 7.8 | 19.6 | 14.6 | 21.0 | 15.7 | 10.4 | 13.67 | 47.1% | 26.1% |
| D | 5,205 | 14.5 | 10.1 | 21.3 | 15.3 | 20.9 | 12.6 | 5.3 | 11.24 | 38.8% | 17.9% |
| F | 8,543 | 10.2 | 8.4 | 16.1 | 14.5 | 23.4 | 19.5 | 7.9 | 15.38 | 50.8% | 27.4% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 15,408 | 17.7 | 10.8 | 21.5 | 15.7 | 15.3 | 10.1 | 8.9 | 10.0 | 34.3% | 19.0% |
| LIMITED | 10,484 | 13.6 | 9.7 | 20.4 | 15.8 | 19.5 | 13.4 | 7.7 | 11.91 | 40.5% | 21.1% |
| POOR | 21,963 | 9.0 | 6.6 | 16.0 | 14.9 | 22.8 | 18.9 | 11.9 | 16.2 | 53.5% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,021 | 23.6 | 18.0 | 33.0 | 15.6 | 6.4 | 3.0 | 0.4 | 5.91 | 9.8% | 3.4% |
| GAME_SPREAD | 6,761 | 22.9 | 15.3 | 32.0 | 16.8 | 9.0 | 3.3 | 0.7 | 6.68 | 12.9% | 4.0% |
| MATCH_WINNER | 34,870 | 15.8 | 10.9 | 22.2 | 15.1 | 18.5 | 12.0 | 5.5 | 10.26 | 36.0% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 16,670 | 28.2 | 16.8 | 30.8 | 12.6 | 9.0 | 2.4 | 0.3 | 5.59 | 11.7% | 2.7% |
| TOTAL_GAMES | 11,358 | 9.8 | 10.8 | 35.9 | 25.9 | 10.6 | 4.2 | 2.9 | 9.18 | 17.6% | 7.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,329 | 24.5 | 28.6 | 33.3 | 8.2 | 4.0 | 1.2 | 0.3 | 4.8 | 5.5% | 1.4% |
| GAME_SPREAD | 9,302 | 47.0 | 15.9 | 24.9 | 7.5 | 2.3 | 1.9 | 0.6 | 3.29 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,711 | 6.6 | 9.9 | 40.4 | 30.1 | 7.4 | 3.3 | 2.4 | 9.2 | 13.1% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,365 | 23.7 | 16.7 | 34.6 | 14.8 | 6.9 | 2.7 | 0.5 | 6.06 | 10.2% | 3.2% |
| GAME_SPREAD | 9,311 | 20.6 | 13.5 | 28.2 | 20.1 | 12.0 | 4.4 | 1.2 | 7.63 | 17.5% | 5.5% |
| TOTAL_GAMES | 16,750 | 10.0 | 10.8 | 36.3 | 24.4 | 11.4 | 4.5 | 2.6 | 9.05 | 18.5% | 7.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 47,855 | 44.5% | 24.9% | 13.06 | 35.3% | 15.0% | 10.67 |
| gen1_elo | 47,855 | 44.0% | 24.6% | 12.85 | 34.8% | 14.8% | 10.49 |
| gen1_sr | 47,855 | 52.0% | 31.3% | 15.83 | 43.9% | 21.5% | 12.97 |
| gen2 | 47,855 | 51.0% | 31.4% | 15.46 | 43.8% | 23.1% | 12.83 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,034 | 15.5 | 10.5 | 21.3 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 27,821 | 10.9 | 7.3 | 16.8 | 14.0 | 19.3 | 17.0 | 14.8 | 15.43 | 51.1% | 31.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 28,338 | 16.4 | 11.2 | 22.8 | 15.2 | 18.0 | 11.5 | 4.9 | 9.89 | 34.4% | 16.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 82,725 | 28338 | 23506 | 30881 | 24.8 | 130.4 | 1451.1 |
| ge_15pp | 33,837 | 9749 | 8373 | 15715 | 28.3 | 438.9 | 1451.1 |
| ge_25pp | 18,006 | 4646 | 3655 | 9705 | 33.8 | 584.7 | 1431.1 |
| lt_10pp | 36,266 | 14280 | 11116 | 10870 | 22.7 | 47.9 | 1421.1 |

Current slate `SL-20261109T075256Z-89c37333`: 271 priced rows, quote age at build {'median': 64.1, 'max': 64.2}, freshness {'STALE': 271}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 51 | 0.0 | 0.0 | 35.3 | 9.8 | 31.4 | 19.6 | 3.9 | 18.34 | 54.9% | 23.5% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,746 | 19.2 | 10.9 | 25.5 | 18.0 | 17.9 | 7.4 | 0.9 | 8.82 | 26.3% | 8.3% |
| KALSHI_LONE_OUTLIER | 30 | 6.7 | 6.7 | 73.3 | 6.7 | 3.3 | 3.3 | 0.0 | 6.16 | 6.7% | 3.3% |
| MARKETS_AGREE | 997 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,129 | 0.0 | 2.2 | 37.4 | 26.2 | 24.1 | 9.1 | 0.9 | 11.81 | 34.2% | 10.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 47,855 | 7982 (16.7%) | 26.7% | 1.0% | {"EXTERNAL_STALE": 4746, "AGREES_WITH_KALSHI": 2129, "ALL_AGREE": 997, "SUPPORTS_MODEL_DIRECTION": 49, "AGREES_WITH_MODEL": 30, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 21,289 | 2004 (9.4%) | 36.3% | 1.5% | {"EXTERNAL_STALE": 1247, "AGREES_WITH_KALSHI": 727, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 11,898 | 622 (5.2%) | 34.2% | 2.1% | {"EXTERNAL_STALE": 396, "AGREES_WITH_KALSHI": 213, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,531 | 591 (10.7%) | 34.9% | 2.2% | {"EXTERNAL_STALE": 372, "AGREES_WITH_KALSHI": 206, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 19,217 | 4557 (23.7%) | 18.5% | 0.9% | {"EXTERNAL_STALE": 2643, "ALL_AGREE": 997, "AGREES_WITH_KALSHI": 844, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 26, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 9,363 | 10.5 | 7.7 | 19.3 | 14.6 | 21.6 | 16.4 | 10.0 | 14.12 | 47.9% | 26.4% |
| 4-10x | 6,390 | 11.1 | 8.4 | 18.3 | 15.2 | 22.0 | 14.6 | 10.3 | 13.92 | 46.9% | 24.9% |
| <2x | 24,475 | 14.9 | 9.7 | 19.7 | 16.0 | 17.6 | 13.1 | 8.9 | 11.58 | 39.6% | 22.0% |
| >=10x | 7,627 | 10.3 | 6.4 | 15.1 | 14.4 | 21.7 | 18.9 | 13.2 | 16.43 | 53.8% | 32.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 12,579 | 12.4 | 8.6 | 19.8 | 16.2 | 19.0 | 13.6 | 10.4 | 12.78 | 43.1% | 24.0% |
| 300-1000 | 10,318 | 11.8 | 8.7 | 17.6 | 15.0 | 20.8 | 16.3 | 9.7 | 13.82 | 46.8% | 26.0% |
| <300 | 14,976 | 8.3 | 5.8 | 15.2 | 14.7 | 23.0 | 19.9 | 13.2 | 17.18 | 56.1% | 33.0% |
| >=3000 | 9,982 | 21.2 | 12.8 | 23.9 | 15.6 | 14.0 | 7.3 | 5.2 | 7.8 | 26.5% | 12.5% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1473 | 0.5495 | 0.4103 | 0.4854 | +0.064 | -0.075 | 0.0018 ± 0.004 |
| ratio 4-10x | 997 | 0.577 | 0.4327 | 0.4875 | +0.089 | -0.055 | 0.0081 ± 0.005 |
| ratio <2x | 3600 | 0.5364 | 0.4137 | 0.4378 | +0.099 | -0.024 | 0.0142 ± 0.0024 |
| ratio >=10x | 1230 | 0.567 | 0.3934 | 0.448 | +0.119 | -0.055 | 0.0148 ± 0.0051 |
| thinner_sample 1000-3000 | 2021 | 0.54 | 0.4123 | 0.4483 | +0.092 | -0.036 | 0.0112 ± 0.0033 |
| thinner_sample 300-1000 | 1651 | 0.5647 | 0.4243 | 0.4737 | +0.091 | -0.049 | 0.005 ± 0.0038 |
| thinner_sample <300 | 2353 | 0.5589 | 0.3911 | 0.4552 | +0.104 | -0.064 | 0.0128 ± 0.0036 |
| thinner_sample >=3000 | 1275 | 0.5289 | 0.4353 | 0.4463 | +0.083 | -0.011 | 0.0148 ± 0.0032 |
| data_status ADEQUATE | 2031 | 0.5316 | 0.4287 | 0.4402 | +0.091 | -0.011 | 0.0151 ± 0.0027 |
| data_status LIMITED | 1791 | 0.5488 | 0.4155 | 0.4662 | +0.083 | -0.051 | 0.0075 ± 0.0036 |
| data_status POOR | 3478 | 0.5608 | 0.4009 | 0.4597 | +0.101 | -0.059 | 0.0103 ± 0.0029 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1054 | 0.1979 | 0.1981 | -0.0003 ± 0.0005 | 0.5758 | 0.5765 | 0.5026 | 0.4875 | 0.5 | -0.093 ± 0.0145 | -0.0087 (8) |
| 3-5 | 673 | 0.2056 | 0.2055 | +0.0001 ± 0.0014 | 0.596 | 0.5941 | 0.5044 | 0.4646 | 0.4829 | -0.095 ± 0.018 | 0.01 (3) |
| 5-10 | 1567 | 0.2029 | 0.2016 | +0.0013 ± 0.0017 | 0.5925 | 0.587 | 0.5121 | 0.4383 | 0.4639 | -0.093 ± 0.0117 | -0.0143 (7) |
| 10-15 | 1268 | 0.2183 | 0.2093 | +0.0089 ± 0.0032 | 0.6283 | 0.6024 | 0.5239 | 0.4004 | 0.4251 | -0.104 ± 0.0131 | -0.055 (6) |
| 15-25 | 1621 | 0.2259 | 0.2085 | +0.0174 ± 0.0044 | 0.6469 | 0.6006 | 0.576 | 0.3814 | 0.4337 | -0.103 ± 0.0114 | -0.0045 (11) |
| 25-40 | 926 | 0.2231 | 0.2063 | +0.0168 ± 0.0089 | 0.6359 | 0.5937 | 0.6522 | 0.3425 | 0.4698 | -0.067 ± 0.0137 | -0.06 (2) |
| 40+ | 191 | 0.296 | 0.1751 | +0.1210 ± 0.0272 | 0.7965 | 0.5226 | 0.7305 | 0.2751 | 0.377 | -0.082 ± 0.0262 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5477 | 0.1855 | 0.1865 | -0.0009 ± 0.0002 | 0.5472 | 0.5483 | 0.4908 | 0.4756 | 0.5076 | -0.020 ± 0.0059 | -0.01 (28) |
| 3-5 | 3649 | 0.198 | 0.1963 | +0.0017 ± 0.0006 | 0.5766 | 0.5703 | 0.4828 | 0.443 | 0.4412 | -0.056 ± 0.0074 | 0.005 (6) |
| 5-10 | 7927 | 0.2014 | 0.1977 | +0.0036 ± 0.0007 | 0.5886 | 0.5764 | 0.4843 | 0.4107 | 0.423 | -0.046 ± 0.0051 | -0.0114 (22) |
| 10-15 | 6558 | 0.2022 | 0.1863 | +0.0159 ± 0.0013 | 0.5911 | 0.5465 | 0.4856 | 0.3617 | 0.3599 | -0.063 ± 0.0054 | -0.0379 (19) |
| 15-25 | 8315 | 0.2063 | 0.1671 | +0.0392 ± 0.0018 | 0.6046 | 0.4964 | 0.4999 | 0.3044 | 0.3025 | -0.070 ± 0.0045 | -0.0043 (51) |
| 25-40 | 6433 | 0.2228 | 0.126 | +0.0968 ± 0.0028 | 0.6397 | 0.387 | 0.527 | 0.2132 | 0.2198 | -0.059 ± 0.0043 | -0.0733 (3) |
| 40+ | 4307 | 0.3824 | 0.0437 | +0.3387 ± 0.0036 | 0.9958 | 0.1699 | 0.6309 | 0.1012 | 0.058 | -0.075 ± 0.003 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 846 | 0.2059 | 0.2063 | -0.0004 ± 0.0005 | 0.5928 | 0.5941 | 0.5059 | 0.491 | 0.5154 | -0.099 ± 0.0168 | -0.0117 (6) |
| 3-5 | 599 | 0.2119 | 0.2088 | +0.0031 ± 0.0015 | 0.607 | 0.6002 | 0.5138 | 0.4743 | 0.4508 | -0.133 ± 0.0201 | 0.01 (3) |
| 5-10 | 1347 | 0.2073 | 0.2055 | +0.0018 ± 0.0019 | 0.6009 | 0.5961 | 0.5408 | 0.4662 | 0.4944 | -0.087 ± 0.0127 | -0.01 (4) |
| 10-15 | 1177 | 0.213 | 0.2065 | +0.0064 ± 0.0033 | 0.6186 | 0.5989 | 0.562 | 0.4376 | 0.4766 | -0.101 ± 0.0138 | -0.04 (5) |
| 15-25 | 1708 | 0.2322 | 0.2123 | +0.0200 ± 0.0044 | 0.6603 | 0.609 | 0.5854 | 0.3898 | 0.4379 | -0.101 ± 0.0114 | -0.0183 (12) |
| 25-40 | 1199 | 0.2673 | 0.1994 | +0.0679 ± 0.0081 | 0.7453 | 0.5793 | 0.6609 | 0.347 | 0.3978 | -0.117 ± 0.0129 | -0.008 (5) |
| 40+ | 424 | 0.3719 | 0.1624 | +0.2095 ± 0.0196 | 1.0138 | 0.4909 | 0.7373 | 0.248 | 0.2925 | -0.088 ± 0.0187 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4694 | 0.1924 | 0.1926 | -0.0002 ± 0.0002 | 0.5606 | 0.5608 | 0.5076 | 0.4925 | 0.5081 | -0.040 ± 0.0066 | -0.0154 (26) |
| 3-5 | 3197 | 0.1929 | 0.1917 | +0.0012 ± 0.0006 | 0.5627 | 0.5589 | 0.5115 | 0.4718 | 0.4754 | -0.048 ± 0.0079 | 0.01 (5) |
| 5-10 | 7082 | 0.1969 | 0.1936 | +0.0033 ± 0.0008 | 0.5787 | 0.5665 | 0.509 | 0.4348 | 0.4521 | -0.040 ± 0.0053 | -0.0117 (6) |
| 10-15 | 5882 | 0.2024 | 0.191 | +0.0114 ± 0.0014 | 0.5942 | 0.5589 | 0.51 | 0.386 | 0.4028 | -0.048 ± 0.0058 | -0.0189 (18) |
| 15-25 | 8376 | 0.2175 | 0.1811 | +0.0364 ± 0.0018 | 0.6321 | 0.5312 | 0.5255 | 0.3299 | 0.3372 | -0.061 ± 0.0047 | -0.014 (52) |
| 25-40 | 7535 | 0.2509 | 0.1381 | +0.1129 ± 0.0027 | 0.7088 | 0.4213 | 0.561 | 0.2441 | 0.2281 | -0.079 ± 0.0043 | -0.0095 (20) |
| 40+ | 5900 | 0.4021 | 0.0581 | +0.3440 ± 0.0036 | 1.0595 | 0.2101 | 0.6544 | 0.118 | 0.0792 | -0.074 ± 0.0031 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1029 | 0.1959 | 0.1972 | -0.0014 ± 0.0005 | 0.5715 | 0.5748 | 0.5024 | 0.4871 | 0.5306 | -0.053 ± 0.0144 | -0.0191 (11) |
| 3-5 | 731 | 0.2073 | 0.2057 | +0.0015 ± 0.0014 | 0.6011 | 0.5957 | 0.4988 | 0.4591 | 0.4624 | -0.110 ± 0.0176 | 0.002 (5) |
| 5-10 | 1597 | 0.2034 | 0.1997 | +0.0037 ± 0.0017 | 0.5921 | 0.5817 | 0.5127 | 0.439 | 0.4496 | -0.105 ± 0.0115 | -0.01 (10) |
| 10-15 | 1282 | 0.2117 | 0.203 | +0.0087 ± 0.0031 | 0.6139 | 0.5886 | 0.5372 | 0.4139 | 0.4423 | -0.105 ± 0.0127 | -0.0286 (7) |
| 15-25 | 1548 | 0.2311 | 0.2131 | +0.0180 ± 0.0046 | 0.6597 | 0.6107 | 0.5868 | 0.3927 | 0.4432 | -0.106 ± 0.0117 | -0.03 (1) |
| 25-40 | 912 | 0.2125 | 0.2107 | +0.0019 ± 0.0089 | 0.6136 | 0.6038 | 0.6596 | 0.3488 | 0.4989 | -0.054 ± 0.0138 | -0.0267 (3) |
| 40+ | 201 | 0.3076 | 0.1831 | +0.1245 ± 0.0271 | 0.8325 | 0.54 | 0.7426 | 0.2875 | 0.3881 | -0.083 ± 0.0277 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5282 | 0.1855 | 0.1862 | -0.0007 ± 0.0002 | 0.5467 | 0.5475 | 0.4857 | 0.4704 | 0.49 | -0.032 ± 0.006 | -0.0189 (44) |
| 3-5 | 3787 | 0.2037 | 0.2019 | +0.0018 ± 0.0006 | 0.5926 | 0.5864 | 0.48 | 0.4405 | 0.4383 | -0.057 ± 0.0074 | -0.0073 (22) |
| 5-10 | 8074 | 0.196 | 0.1906 | +0.0055 ± 0.0007 | 0.5754 | 0.5585 | 0.4871 | 0.4131 | 0.4133 | -0.057 ± 0.0049 | -0.0117 (42) |
| 10-15 | 6502 | 0.1939 | 0.1791 | +0.0148 ± 0.0013 | 0.5725 | 0.5296 | 0.4946 | 0.3713 | 0.373 | -0.060 ± 0.0053 | -0.0136 (14) |
| 15-25 | 8382 | 0.212 | 0.1727 | +0.0393 ± 0.0018 | 0.618 | 0.5093 | 0.513 | 0.3184 | 0.3156 | -0.070 ± 0.0045 | -0.0533 (3) |
| 25-40 | 6391 | 0.2162 | 0.1265 | +0.0898 ± 0.0028 | 0.6256 | 0.3877 | 0.5284 | 0.2129 | 0.2303 | -0.049 ± 0.0043 | -0.02 (4) |
| 40+ | 4248 | 0.391 | 0.0488 | +0.3422 ± 0.0038 | 1.0191 | 0.1827 | 0.64 | 0.1075 | 0.0654 | -0.075 ± 0.0032 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1468 | 0.1983 | 0.1983 | +0.0000 ± 0.0004 | 0.5752 | 0.575 | 0.5086 | 0.4936 | 0.4966 | -0.069 ± 0.0119 | -0.0221 (56) |
| 3-5 | 1054 | 0.1887 | 0.1885 | +0.0001 ± 0.0011 | 0.5554 | 0.5533 | 0.4983 | 0.4584 | 0.4753 | -0.057 ± 0.0137 | -0.0194 (34) |
| 5-10 | 2123 | 0.1999 | 0.195 | +0.0049 ± 0.0014 | 0.5895 | 0.5734 | 0.5079 | 0.4343 | 0.4385 | -0.077 ± 0.0098 | -0.005 (78) |
| 10-15 | 1455 | 0.2144 | 0.2022 | +0.0122 ± 0.0029 | 0.6222 | 0.588 | 0.5419 | 0.419 | 0.4296 | -0.088 ± 0.0121 | 0.0012 (66) |
| 15-25 | 1912 | 0.2309 | 0.2078 | +0.0231 ± 0.0041 | 0.6589 | 0.5995 | 0.5917 | 0.3968 | 0.4367 | -0.089 ± 0.0105 | -0.0214 (59) |
| 25-40 | 1143 | 0.2399 | 0.2108 | +0.0291 ± 0.0083 | 0.6851 | 0.6046 | 0.6892 | 0.3772 | 0.4864 | -0.086 ± 0.0128 | -0.0252 (27) |
| 40+ | 413 | 0.3237 | 0.2014 | +0.1222 ± 0.021 | 0.9312 | 0.5862 | 0.8178 | 0.3419 | 0.4673 | -0.096 ± 0.0197 | -0.1137 (8) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5391 | 0.1782 | 0.1783 | -0.0001 ± 0.0002 | 0.5269 | 0.5266 | 0.5118 | 0.4965 | 0.5049 | -0.040 ± 0.0058 | -0.0154 (103) |
| 3-5 | 3730 | 0.1952 | 0.1944 | +0.0009 ± 0.0006 | 0.5695 | 0.567 | 0.5022 | 0.4624 | 0.4721 | -0.040 ± 0.0073 | -0.0212 (73) |
| 5-10 | 7574 | 0.1964 | 0.19 | +0.0065 ± 0.0008 | 0.5801 | 0.5602 | 0.5015 | 0.4279 | 0.4221 | -0.062 ± 0.0051 | -0.0084 (134) |
| 10-15 | 5176 | 0.2096 | 0.1934 | +0.0162 ± 0.0015 | 0.6104 | 0.5675 | 0.537 | 0.414 | 0.4082 | -0.071 ± 0.0062 | -0.0057 (111) |
| 15-25 | 6318 | 0.2317 | 0.2001 | +0.0315 ± 0.0022 | 0.6653 | 0.5798 | 0.5771 | 0.3817 | 0.3997 | -0.067 ± 0.0057 | -0.026 (108) |
| 25-40 | 4115 | 0.2568 | 0.1906 | +0.0662 ± 0.0043 | 0.7268 | 0.5548 | 0.6407 | 0.3283 | 0.3813 | -0.065 ± 0.0067 | -0.0277 (53) |
| 40+ | 1833 | 0.3683 | 0.16 | +0.2083 ± 0.0096 | 1.0391 | 0.4759 | 0.746 | 0.245 | 0.2979 | -0.061 ± 0.0089 | -0.054 (15) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 7300 | 1.027 ± 0.033 | 1.099 | 0.1686 | 0.1679 | 0.2152 | 0.2042 |
| gen2 | 7300 | 0.817 ± 0.03 | 1.07 | 0.1735 | 0.1682 | 0.2337 | 0.2041 |
| gen1_elo | 7300 | 1.012 ± 0.032 | 1.089 | 0.1749 | 0.168 | 0.2141 | 0.2043 |
| gen1_sr | 7300 | 1.005 ± 0.039 | 1.127 | 0.1334 | 0.1698 | 0.2296 | 0.2038 |
| gen1_ledger | 9568 | 0.867 ± 0.024 | 1.076 | 0.1895 | 0.1749 | 0.2169 | 0.2006 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 33,837)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 7,868 | 23.2% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,739 | 22.9% |
| BOOK_QUALITY | execution | 6,006 | 17.8% |
| POOR_DATA | data | 3,887 | 11.5% |
| LIMITED_DATA | data | 2,090 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,952 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 1,404 | 4.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,373 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 963 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 554 | 1.6% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 23.2%, coverage 22.9%, execution 17.8%, data 17.7%, market_freshness/coverage 8.6%, mapping 4.2%, model_calibration_or_unknown 4.1%, model_calibration 1.6%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.6%, LOW_DATA_QUALITY 71.4%, THIN_PLAYER_HISTORY 59.6%, STALE_PLAYER_DATA 51.9%, STALE_KALSHI_QUOTE 46.4%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 24.0%, MODEL_HIGH_UNCERTAINTY 18.7%, PLAYER_IDENTITY_RISK 15.3%, LEVEL_TRANSFER_RISK 9.9%, LOW_DISPLAYED_LIQUIDITY 8.3%, EVENT_MAPPING_RISK 7.2%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.3%, POST_SETTLEMENT_OBSERVATION 22.9%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 18,006)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,207 | 34.5% |
| STALE_QUOTE | market_freshness | 3,501 | 19.4% |
| BOOK_QUALITY | execution | 3,115 | 17.3% |
| POOR_DATA | data | 1,639 | 9.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,040 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 781 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 631 | 3.5% |
| LIMITED_DATA | data | 615 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 339 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 137 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.5%, market_freshness 19.4%, execution 17.3%, data 12.5%, market_freshness/coverage 9.3%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 74.7%, THIN_PLAYER_HISTORY 61.6%, STALE_KALSHI_QUOTE 53.9%, STALE_PLAYER_DATA 45.6%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 34.2%, WIDE_SPREAD 23.4%, MODEL_HIGH_UNCERTAINTY 19.3%, PLAYER_IDENTITY_RISK 18.3%, EVENT_MAPPING_RISK 8.8%, LEVEL_TRANSFER_RISK 8.7%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.5%, POST_SETTLEMENT_OBSERVATION 34.5%, POSSIBLE_IN_PLAY_QUOTE 6.2%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 14386, "IDENTITY_AMBIGUOUS": 3620}; ticker orientation: {"VERIFIED": 18006}.

Checks: discipline:AMBIGUOUS 1201, discipline:PASS 16805, identity_confidence:AMBIGUOUS 3289, identity_confidence:PASS 14717, level_mapping:NA 1213, level_mapping:PASS 16793, market_pair:AMBIGUOUS 492, market_pair:NA 411, market_pair:PASS 17103, model_complement:NA 373, model_complement:PASS 17633, namesake:AMBIGUOUS 6, namesake:PASS 18000, physical_match_id:NA 6108, physical_match_id:PASS 11898, player_ids:PASS 18006, same_pair_other_event:PASS 18006, ticker_orientation:PASS 18006

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,427 | 3.8% | 3.2% | 1.4% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 24, "market_freshness/coverage": 21} | 5.51 | 0.2235 / 0.2191 (831) | 25.1% | 2.4% | 3.0% | 2.9% |
| CHALLENGER | 11,948 | 16.5% | 6.2% | 10.9% | {"coverage": 1173, "market_freshness": 234, "market_freshness/coverage": 225, "data": 163, "model_calibration_or_unknown": 78, "execution": 41, "model_calibration": 38, "mapping": 17, "possible_market_error": 1} | 7.4 | 0.2211 / 0.2108 (2815) | 38.8% | 14.8% | 4.0% | 22.5% |
| DOUBLES | 2,591 | 46.4% | 46.3% | 6.7% | {"execution": 665, "mapping": 353, "market_freshness": 106, "market_freshness/coverage": 70, "coverage": 7} | 23.2 | 0.2973 / 0.232 (648) | 9.0% | 0.0% | 100.0% | 6.4% |
| ITF_MEN | 23,482 | 25.0% | 17.5% | 32.6% | {"coverage": 2068, "market_freshness": 1149, "execution": 993, "data": 859, "market_freshness/coverage": 591, "mapping": 206, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.67 | 0.2178 / 0.1998 (5004) | 40.2% | 68.9% | 15.1% | 21.6% |
| ITF_WOMEN | 30,676 | 26.5% | 18.9% | 45.1% | {"coverage": 2880, "market_freshness": 1751, "execution": 1333, "data": 1131, "market_freshness/coverage": 707, "mapping": 199, "model_calibration_or_unknown": 94, "model_calibration": 23} | 12.52 | 0.2024 / 0.1941 (5960) | 41.4% | 57.0% | 9.9% | 21.8% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,863 | 6.0% | 5.1% | 1.6% | {"market_freshness": 111, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.68 | 0.2307 / 0.2204 (798) | 30.1% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.6% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 404 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 638 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.4h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 509 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 869 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 12 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 21.3h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 1282 min (STALE); no external reference |
| 15 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 16 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 18 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 19 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 20 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 21 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 22 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 23 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 24 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 25 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 454 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 26 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 27 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 28 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 29 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 30 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 31 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 32 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 33 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 34 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 35 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 36 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 37 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 38 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 39 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 40 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 41 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 43 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 44 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 45 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 46 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 124 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 49 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 50 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.3h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 748 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9703, "by_level_share_of_ge_25pp": {"ATP": 0.0136, "CHALLENGER": 0.1094, "DOUBLES": 0.0667, "ITF_MEN": 0.3264, "ITF_WOMEN": 0.4508, "OTHER": 0.0007, "WTA": 0.0162, "WTA125": 0.0163}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.539, "share_primary_cause_market_settled_or_in_play": 0.4375, "share_primary_cause_stale_quote_only": 0.1944}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 18006, "identity_ambiguous_share": 0.201, "ticker_orientation": {"VERIFIED": 18006}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 11898, "with_external": 622, "coverage": 0.0523, "external_status": {"EXTERNAL_STALE": 396, "AGREES_WITH_KALSHI": 213, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 396, "MODEL_LONE_OUTLIER": 213, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3424, "share_external_supports_model": 0.0209}, "pregame_clean_ge_25pp": {"n": 5531, "with_external": 591, "coverage": 0.1069, "external_status": {"EXTERNAL_STALE": 372, "AGREES_WITH_KALSHI": 206, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 372, "MODEL_LONE_OUTLIER": 206, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3486, "share_external_supports_model": 0.022}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 494.0, "median_sample_ratio": 2.45, "median_min_matches": 19.0, "median_max_days_since_last": 240.0, "share_severe_asymmetry": 0.2082, "data_status": {"POOR": 10064, "LIMITED": 4673, "ADEQUATE": 3269}, "comparison_lt_10pp": {"median_thinner_serve_points": 1736.0, "median_sample_ratio": 1.69, "median_min_matches": 91.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1473, "model_minus_observed": 0.0641, "kalshi_minus_observed": -0.0751, "brier_diff_model_minus_kalshi": 0.0018}, "4-10x": {"n": 997, "model_minus_observed": 0.0895, "kalshi_minus_observed": -0.0548, "brier_diff_model_minus_kalshi": 0.0081}, "<2x": {"n": 3600, "model_minus_observed": 0.0986, "kalshi_minus_observed": -0.0241, "brier_diff_model_minus_kalshi": 0.0142}, ">=10x": {"n": 1230, "model_minus_observed": 0.1191, "kalshi_minus_observed": -0.0546, "brier_diff_model_minus_kalshi": 0.0148}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 7300, "model": {"intercept": -0.553, "slope": 0.817, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.18, "slope": 1.07, "slope_se": 0.033}, "mean_extremity_model": 0.1735, "mean_extremity_kalshi": 0.1682, "model_brier": 0.2337, "kalshi_brier": 0.2041, "brier_diff_model_minus_kalshi": 0.0296, "brier_diff_se": 0.0022, "model_logloss": 0.6649, "kalshi_logloss": 0.5908}, "fair_v1": {"n": 7300, "model": {"intercept": -0.449, "slope": 1.027, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.246, "slope": 1.099, "slope_se": 0.034}, "mean_extremity_model": 0.1686, "mean_extremity_kalshi": 0.1679, "model_brier": 0.2152, "kalshi_brier": 0.2042, "brier_diff_model_minus_kalshi": 0.011, "brier_diff_se": 0.0018, "model_logloss": 0.6195, "kalshi_logloss": 0.591}, "gen1_elo": {"n": 7300, "model": {"intercept": -0.437, "slope": 1.012, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.249, "slope": 1.089, "slope_se": 0.033}, "mean_extremity_model": 0.1749, "mean_extremity_kalshi": 0.168, "model_brier": 0.2141, "kalshi_brier": 0.2043, "brier_diff_model_minus_kalshi": 0.0098, "brier_diff_se": 0.0018, "model_logloss": 0.6176, "kalshi_logloss": 0.5911}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2486, "share_ge_15": 0.4449, "median_abs_gap": 13.06, "n": 47855}, "gen1_elo": {"share_ge_25": 0.246, "share_ge_15": 0.4405, "median_abs_gap": 12.85, "n": 47855}, "gen1_sr": {"share_ge_25": 0.3132, "share_ge_15": 0.5204, "median_abs_gap": 15.83, "n": 47855}, "gen2": {"share_ge_25": 0.3143, "share_ge_15": 0.5105, "median_abs_gap": 15.46, "n": 47855}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1504, "share_ge_15": 0.3531, "median_abs_gap": 10.67, "n": 36780}, "gen1_elo": {"share_ge_25": 0.1485, "share_ge_15": 0.3479, "median_abs_gap": 10.49, "n": 36780}, "gen1_sr": {"share_ge_25": 0.2149, "share_ge_15": 0.4385, "median_abs_gap": 12.97, "n": 36782}, "gen2": {"share_ge_25": 0.2305, "share_ge_15": 0.4381, "median_abs_gap": 12.83, "n": 36782}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.51, "share_ge_25_all": 0.038, "share_ge_25_pregame_clean": 0.0319}, "WTA": {"median_abs_gap_pregame_clean": 7.68, "share_ge_25_all": 0.0598, "share_ge_25_pregame_clean": 0.0508}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2365, "share_within_10pp_all": 0.4384, "share_within_10pp_pregame_clean": 0.4921, "corr_model_vs_mid_pregame_clean": 0.8501}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1054, "model_brier": 0.1979, "kalshi_brier": 0.1981, "brier_diff_model_minus_kalshi": -0.0003}, "10-15": {"n_settled": 1268, "model_brier": 0.2183, "kalshi_brier": 0.2093, "brier_diff_model_minus_kalshi": 0.0089}, "15-25": {"n_settled": 1621, "model_brier": 0.2259, "kalshi_brier": 0.2085, "brier_diff_model_minus_kalshi": 0.0174}, "25-40": {"n_settled": 926, "model_brier": 0.2231, "kalshi_brier": 0.2063, "brier_diff_model_minus_kalshi": 0.0168}, "3-5": {"n_settled": 673, "model_brier": 0.2056, "kalshi_brier": 0.2055, "brier_diff_model_minus_kalshi": 0.0001}, "40+": {"n_settled": 191, "model_brier": 0.296, "kalshi_brier": 0.1751, "brier_diff_model_minus_kalshi": 0.121}, "5-10": {"n_settled": 1567, "model_brier": 0.2029, "kalshi_brier": 0.2016, "brier_diff_model_minus_kalshi": 0.0013}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.553, "slope": 0.817, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.18, "slope": 1.07, "slope_se": 0.033}, "n": 7300}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.485, "slope": 0.867, "slope_se": 0.024}, "kalshi_slope": {"intercept": 0.174, "slope": 1.076, "slope_se": 0.028}, "n": 9568}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 648, "model_brier": 0.2973, "kalshi_brier": 0.232, "brier_diff_model_minus_kalshi": 0.0653, "brier_diff_se": 0.0115, "corr_model_outcome": 0.1062, "corr_kalshi_outcome": 0.2841}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
