# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-09T15:55Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 83,356): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.2%, 15-25 19.1%, 25-40 13.6%, 40+ 8.1%; median gap 11.84 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.7%, Challenger 11.1%, doubles 6.6%). Main tour: ATP 3.8% and WTA 6.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 18,151): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.5%, STALE_QUOTE 19.6%, BOOK_QUALITY 17.2%, POOR_DATA 9.1%, POSSIBLY_IN_PLAY_QUOTE 5.8%, IDENTITY_AMBIGUOUS 4.3%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.5%, market_freshness 19.6%, execution 17.2%, data 12.5%, market_freshness/coverage 9.2%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 54.0% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.7% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 18,151 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.1% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.9% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 491.5 points vs 1743.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.026, Gen-2 0.815, Gen-1 ledger 0.868 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 928 model 0.2236 vs Kalshi 0.2061; n 191 model 0.296 vs Kalshi 0.1751.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 353,345 model-market comparisons (579,479 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 117,196 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-09T15:39:56.997709+00:00'], shadow board 96,112 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-09T15:40:00.498320+00:00'], Model 4 43,257 rows, 29,319 settled tickers, 11,043 tickers with an external scan.
* By model: {"gen1_ledger": 79015, "gen1_elo": 48306, "fair_v1": 48306, "gen2": 48306, "gen1_sr": 48306, "model4_fundamental": 40595, "model4_conditioned": 40511}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 83,356 | 14.1 | 9.6 | 20.2 | 15.2 | 19.1 | 13.6 | 8.1 | 11.84 | 40.9% | 21.8% |
| MW fair_v1 | 48,306 | 12.8 | 8.6 | 18.8 | 15.3 | 19.6 | 14.8 | 10.0 | 13.05 | 44.5% | 24.9% |
| MW gen1_elo | 48,306 | 12.6 | 8.8 | 19.2 | 15.4 | 19.4 | 14.7 | 9.9 | 12.84 | 44.0% | 24.6% |
| MW gen1_ledger | 35,050 | 15.8 | 10.9 | 22.2 | 15.1 | 18.5 | 12.0 | 5.5 | 10.26 | 36.0% | 17.5% |
| MW gen1_sr | 48,306 | 10.0 | 7.3 | 16.7 | 13.9 | 20.7 | 18.7 | 12.7 | 15.83 | 52.0% | 31.3% |
| MW gen2 | 48,306 | 11.0 | 7.6 | 16.7 | 13.7 | 19.6 | 17.7 | 13.7 | 15.46 | 51.0% | 31.4% |
| all families model4_conditioned | 40,511 | 22.3 | 17.9 | 34.3 | 17.1 | 5.0 | 2.2 | 1.2 | 6.07 | 8.4% | 3.4% |
| all families model4_fundamental | 40,595 | 17.3 | 13.5 | 33.9 | 20.0 | 9.9 | 3.8 | 1.5 | 7.62 | 15.3% | 5.3% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.1%, >=15pp 40.9%, >=20pp 30.1%, >=25pp 21.8%, >=30pp 15.7%, >=40pp 8.1%, >=50pp 3.9%
Executable gap (model outside the book, before fees): median 8.41pp; >=10pp 45.1%, >=25pp 17.2%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,035 | 28.3 | 15.7 | 27.8 | 13.4 | 10.7 | 3.6 | 0.6 | 5.84 | 14.9% | 4.2% |
| CHALLENGER | 7,509 | 16.1 | 9.6 | 20.6 | 15.5 | 16.1 | 11.4 | 10.8 | 10.94 | 38.2% | 22.1% |
| ITF_MEN | 13,618 | 9.8 | 7.3 | 17.1 | 15.0 | 21.1 | 17.3 | 12.5 | 15.36 | 50.9% | 29.8% |
| ITF_WOMEN | 18,741 | 9.5 | 7.0 | 16.0 | 14.8 | 22.3 | 18.4 | 12.0 | 15.92 | 52.6% | 30.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,070 | 16.7 | 13.1 | 25.0 | 20.8 | 16.6 | 6.8 | 1.1 | 8.65 | 24.4% | 7.8% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,035 | 26.7 | 15.6 | 26.0 | 15.7 | 11.3 | 3.9 | 0.8 | 6.07 | 16.0% | 4.7% |
| CHALLENGER | 7,509 | 14.4 | 9.2 | 19.0 | 13.8 | 18.7 | 13.5 | 11.4 | 12.54 | 43.6% | 24.9% |
| ITF_MEN | 13,618 | 8.1 | 6.2 | 15.1 | 13.7 | 19.9 | 20.5 | 16.5 | 17.99 | 57.0% | 37.0% |
| ITF_WOMEN | 18,741 | 7.9 | 5.8 | 14.2 | 12.8 | 20.7 | 21.2 | 17.5 | 19.09 | 59.4% | 38.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,070 | 14.0 | 10.3 | 21.7 | 16.3 | 22.4 | 12.8 | 2.5 | 11.23 | 37.8% | 15.3% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,035 | 23.1 | 14.1 | 25.4 | 15.6 | 14.6 | 6.0 | 1.1 | 7.11 | 21.8% | 7.2% |
| CHALLENGER | 7,509 | 15.1 | 9.7 | 20.6 | 15.8 | 16.1 | 11.9 | 10.8 | 11.3 | 38.8% | 22.8% |
| ITF_MEN | 13,618 | 9.5 | 7.3 | 17.2 | 14.1 | 21.8 | 17.2 | 12.9 | 15.73 | 51.9% | 30.1% |
| ITF_WOMEN | 18,741 | 9.3 | 6.9 | 16.2 | 15.7 | 22.2 | 18.4 | 11.3 | 15.6 | 51.9% | 29.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,070 | 22.6 | 17.0 | 31.9 | 15.4 | 8.8 | 3.3 | 1.0 | 6.12 | 13.1% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,422 | 27.8 | 19.5 | 29.3 | 12.4 | 8.1 | 2.6 | 0.5 | 5.29 | 11.1% | 3.0% |
| CHALLENGER | 4,706 | 22.6 | 14.5 | 27.4 | 14.8 | 13.4 | 5.7 | 1.6 | 7.07 | 20.7% | 7.3% |
| DOUBLES | 2,603 | 4.8 | 4.5 | 12.9 | 10.9 | 20.4 | 24.3 | 22.0 | 23.22 | 66.7% | 46.3% |
| ITF_MEN | 10,027 | 12.9 | 9.6 | 21.4 | 15.6 | 21.7 | 13.0 | 5.9 | 11.79 | 40.6% | 18.9% |
| ITF_WOMEN | 12,086 | 13.4 | 9.2 | 19.9 | 15.7 | 21.5 | 14.8 | 5.5 | 12.24 | 41.8% | 20.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,801 | 23.6 | 16.1 | 31.5 | 17.0 | 8.9 | 2.5 | 0.2 | 6.57 | 11.7% | 2.8% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,910 | 28.8 | 15.9 | 28.2 | 13.3 | 10.4 | 3.1 | 0.3 | 5.67 | 13.9% | 3.5% |
| CHALLENGER | 5,335 | 20.7 | 11.9 | 25.6 | 18.2 | 16.1 | 6.0 | 1.6 | 8.33 | 23.6% | 7.5% |
| ITF_MEN | 9,925 | 12.0 | 8.6 | 20.6 | 17.2 | 22.0 | 14.2 | 5.4 | 12.44 | 41.5% | 19.6% |
| ITF_WOMEN | 13,740 | 11.4 | 8.6 | 18.9 | 17.1 | 24.2 | 15.1 | 4.8 | 13.16 | 44.1% | 19.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,956 | 17.0 | 13.2 | 25.3 | 21.1 | 16.5 | 6.2 | 0.6 | 8.46 | 23.4% | 6.8% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,910 | 27.1 | 15.9 | 26.3 | 15.7 | 11.2 | 3.4 | 0.4 | 5.99 | 15.0% | 3.8% |
| CHALLENGER | 5,335 | 18.1 | 11.6 | 23.9 | 16.2 | 19.2 | 9.4 | 1.8 | 9.0 | 30.4% | 11.2% |
| ITF_MEN | 9,926 | 9.6 | 7.2 | 17.6 | 15.9 | 21.8 | 18.6 | 9.2 | 14.91 | 49.7% | 27.9% |
| ITF_WOMEN | 13,741 | 8.9 | 6.9 | 16.0 | 14.3 | 22.6 | 20.6 | 10.7 | 16.51 | 53.8% | 31.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,956 | 14.3 | 10.4 | 21.9 | 16.5 | 22.6 | 12.5 | 1.9 | 11.03 | 37.0% | 14.4% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,356 | 28.0 | 19.7 | 29.3 | 12.6 | 7.8 | 2.4 | 0.3 | 5.24 | 10.5% | 2.7% |
| CHALLENGER | 4,168 | 23.9 | 15.4 | 28.5 | 14.9 | 12.8 | 4.0 | 0.5 | 6.59 | 17.3% | 4.5% |
| DOUBLES | 2,438 | 4.7 | 4.5 | 13.2 | 11.0 | 20.3 | 24.2 | 22.1 | 23.2 | 66.5% | 46.3% |
| ITF_MEN | 8,627 | 13.7 | 10.2 | 22.9 | 16.0 | 21.7 | 11.5 | 3.9 | 10.86 | 37.1% | 15.4% |
| ITF_WOMEN | 10,365 | 14.0 | 9.7 | 21.1 | 16.1 | 21.6 | 13.8 | 3.6 | 11.44 | 39.0% | 17.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,738 | 24.0 | 16.5 | 31.5 | 17.0 | 8.9 | 2.0 | 0.1 | 6.43 | 11.0% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,603 | 4.8 | 4.5 | 12.9 | 10.9 | 20.4 | 24.3 | 22.0 | 23.22 | 66.7% | 46.3% |
| singles | 32,447 | 16.7 | 11.4 | 22.9 | 15.4 | 18.3 | 11.0 | 4.2 | 9.72 | 33.5% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 9,952 | 12.7 | 9.1 | 19.9 | 15.5 | 19.6 | 13.9 | 9.4 | 12.64 | 42.9% | 23.3% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 31,553 | 13.4 | 8.7 | 18.8 | 15.2 | 19.2 | 14.8 | 10.0 | 12.9 | 44.0% | 24.8% |
| UNKNOWN | 6,388 | 10.5 | 7.5 | 17.1 | 16.3 | 21.5 | 16.0 | 11.1 | 14.39 | 48.6% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 13,798 | 19.3 | 11.8 | 22.4 | 16.0 | 15.0 | 9.2 | 6.3 | 8.95 | 30.4% | 15.4% |
| B | 5,912 | 12.8 | 8.5 | 19.6 | 15.5 | 19.7 | 12.8 | 11.1 | 12.79 | 43.6% | 23.9% |
| C | 6,853 | 12.0 | 8.7 | 19.6 | 15.6 | 18.7 | 14.6 | 10.8 | 12.93 | 44.0% | 25.4% |
| D | 7,762 | 11.7 | 8.4 | 17.8 | 15.2 | 21.7 | 15.8 | 9.4 | 13.88 | 46.9% | 25.2% |
| F | 13,981 | 7.4 | 5.6 | 14.9 | 14.6 | 23.4 | 20.9 | 13.3 | 17.85 | 57.5% | 34.2% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,465 | 24.8 | 16.0 | 28.9 | 15.0 | 10.5 | 3.4 | 1.3 | 6.35 | 15.2% | 4.7% |
| B | 4,887 | 16.6 | 10.8 | 24.4 | 16.8 | 18.9 | 9.6 | 3.0 | 9.6 | 31.4% | 12.6% |
| C | 6,880 | 10.9 | 7.7 | 19.6 | 14.6 | 21.1 | 15.7 | 10.4 | 13.65 | 47.1% | 26.1% |
| D | 5,223 | 14.5 | 10.1 | 21.3 | 15.3 | 20.9 | 12.6 | 5.3 | 11.24 | 38.8% | 17.9% |
| F | 8,595 | 10.2 | 8.4 | 16.1 | 14.5 | 23.4 | 19.5 | 7.9 | 15.4 | 50.8% | 27.4% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 15,610 | 17.7 | 10.8 | 21.5 | 15.8 | 15.3 | 10.0 | 8.9 | 10.0 | 34.2% | 19.0% |
| LIMITED | 10,563 | 13.6 | 9.6 | 20.5 | 15.8 | 19.4 | 13.3 | 7.7 | 11.89 | 40.5% | 21.1% |
| POOR | 22,133 | 9.0 | 6.6 | 16.0 | 14.8 | 22.7 | 18.9 | 11.9 | 16.21 | 53.6% | 30.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,050 | 23.6 | 18.0 | 33.0 | 15.6 | 6.4 | 2.9 | 0.4 | 5.9 | 9.8% | 3.4% |
| GAME_SPREAD | 6,783 | 22.9 | 15.3 | 32.1 | 16.8 | 9.0 | 3.3 | 0.7 | 6.68 | 12.9% | 4.0% |
| MATCH_WINNER | 35,050 | 15.8 | 10.9 | 22.2 | 15.1 | 18.5 | 12.0 | 5.5 | 10.26 | 36.0% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 16,726 | 28.2 | 16.8 | 30.8 | 12.6 | 8.9 | 2.4 | 0.3 | 5.59 | 11.6% | 2.7% |
| TOTAL_GAMES | 11,382 | 9.8 | 10.8 | 35.9 | 25.9 | 10.6 | 4.2 | 2.9 | 9.18 | 17.6% | 7.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,399 | 24.5 | 28.6 | 33.3 | 8.1 | 4.0 | 1.1 | 0.3 | 4.8 | 5.4% | 1.4% |
| GAME_SPREAD | 9,350 | 46.9 | 15.9 | 24.9 | 7.4 | 2.3 | 1.9 | 0.6 | 3.3 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,762 | 6.6 | 9.9 | 40.4 | 30.1 | 7.4 | 3.3 | 2.4 | 9.19 | 13.0% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,435 | 23.7 | 16.7 | 34.6 | 14.8 | 6.9 | 2.7 | 0.5 | 6.06 | 10.1% | 3.2% |
| GAME_SPREAD | 9,359 | 20.5 | 13.5 | 28.3 | 20.1 | 12.0 | 4.4 | 1.1 | 7.64 | 17.5% | 5.5% |
| TOTAL_GAMES | 16,801 | 10.0 | 10.8 | 36.4 | 24.4 | 11.4 | 4.4 | 2.6 | 9.04 | 18.4% | 7.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 48,306 | 44.5% | 24.9% | 13.05 | 35.3% | 15.0% | 10.66 |
| gen1_elo | 48,306 | 44.0% | 24.6% | 12.84 | 34.8% | 14.8% | 10.48 |
| gen1_sr | 48,306 | 52.0% | 31.3% | 15.83 | 43.8% | 21.5% | 12.96 |
| gen2 | 48,306 | 51.0% | 31.4% | 15.46 | 43.8% | 23.1% | 12.83 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,098 | 15.5 | 10.4 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 28,208 | 10.9 | 7.3 | 16.9 | 13.9 | 19.3 | 16.9 | 14.8 | 15.39 | 51.0% | 31.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 28,518 | 16.4 | 11.2 | 22.8 | 15.2 | 18.0 | 11.5 | 4.9 | 9.88 | 34.4% | 16.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 83,356 | 28518 | 23570 | 31268 | 24.9 | 130.9 | 1451.1 |
| ge_15pp | 34,090 | 9811 | 8394 | 15885 | 28.4 | 439.4 | 1451.1 |
| ge_25pp | 18,151 | 4676 | 3666 | 9809 | 34.1 | 584.4 | 1431.1 |
| lt_10pp | 36,560 | 14377 | 11149 | 11034 | 22.7 | 48.2 | 1421.1 |

Current slate `SL-20261109T155509Z-3b466f7c`: 373 priced rows, quote age at build {'median': 15.5, 'max': 15.6}, freshness {'AGING': 373}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 51 | 0.0 | 0.0 | 35.3 | 9.8 | 31.4 | 19.6 | 3.9 | 18.34 | 54.9% | 23.5% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,788 | 19.3 | 10.9 | 25.5 | 18.1 | 17.9 | 7.4 | 0.9 | 8.79 | 26.2% | 8.3% |
| KALSHI_LONE_OUTLIER | 31 | 6.5 | 6.5 | 74.2 | 6.5 | 3.2 | 3.2 | 0.0 | 6.21 | 6.5% | 3.2% |
| MARKETS_AGREE | 1,008 | 66.9 | 33.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.16 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,169 | 0.0 | 2.2 | 37.7 | 26.2 | 23.9 | 9.0 | 0.9 | 11.77 | 33.9% | 10.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 48,306 | 8076 (16.7%) | 26.9% | 1.0% | {"EXTERNAL_STALE": 4788, "AGREES_WITH_KALSHI": 2169, "ALL_AGREE": 1008, "SUPPORTS_MODEL_DIRECTION": 49, "AGREES_WITH_MODEL": 31, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 21,480 | 2019 (9.4%) | 36.4% | 1.5% | {"EXTERNAL_STALE": 1254, "AGREES_WITH_KALSHI": 735, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 12,013 | 627 (5.2%) | 34.4% | 2.1% | {"EXTERNAL_STALE": 398, "AGREES_WITH_KALSHI": 216, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,592 | 596 (10.7%) | 35.1% | 2.2% | {"EXTERNAL_STALE": 374, "AGREES_WITH_KALSHI": 209, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 19,414 | 4615 (23.8%) | 18.7% | 0.9% | {"EXTERNAL_STALE": 2668, "ALL_AGREE": 1008, "AGREES_WITH_KALSHI": 865, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 27, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 9,448 | 10.6 | 7.6 | 19.3 | 14.5 | 21.5 | 16.3 | 10.1 | 14.13 | 48.0% | 26.4% |
| 4-10x | 6,430 | 11.2 | 8.5 | 18.3 | 15.1 | 22.0 | 14.6 | 10.3 | 13.92 | 46.9% | 25.0% |
| <2x | 24,756 | 14.8 | 9.7 | 19.8 | 16.0 | 17.6 | 13.1 | 8.9 | 11.57 | 39.6% | 22.0% |
| >=10x | 7,672 | 10.4 | 6.4 | 15.1 | 14.3 | 21.7 | 18.9 | 13.2 | 16.44 | 53.8% | 32.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 12,721 | 12.4 | 8.5 | 19.8 | 16.2 | 19.1 | 13.5 | 10.4 | 12.73 | 43.0% | 23.9% |
| 300-1000 | 10,386 | 11.8 | 8.8 | 17.7 | 15.0 | 20.8 | 16.3 | 9.7 | 13.8 | 46.8% | 26.0% |
| <300 | 15,102 | 8.3 | 5.8 | 15.2 | 14.7 | 23.0 | 19.9 | 13.2 | 17.2 | 56.1% | 33.1% |
| >=3000 | 10,097 | 21.1 | 12.8 | 24.0 | 15.7 | 14.0 | 7.3 | 5.2 | 7.83 | 26.5% | 12.5% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1475 | 0.5496 | 0.4103 | 0.4847 | +0.065 | -0.074 | 0.0021 ± 0.004 |
| ratio 4-10x | 999 | 0.5772 | 0.4325 | 0.4865 | +0.091 | -0.054 | 0.0088 ± 0.005 |
| ratio <2x | 3615 | 0.5365 | 0.4138 | 0.4382 | +0.098 | -0.024 | 0.014 ± 0.0024 |
| ratio >=10x | 1232 | 0.5669 | 0.3933 | 0.4481 | +0.119 | -0.055 | 0.0147 ± 0.0051 |
| thinner_sample 1000-3000 | 2029 | 0.5402 | 0.4125 | 0.4485 | +0.092 | -0.036 | 0.0113 ± 0.0032 |
| thinner_sample 300-1000 | 1652 | 0.5647 | 0.4244 | 0.474 | +0.091 | -0.050 | 0.005 ± 0.0038 |
| thinner_sample <300 | 2360 | 0.5589 | 0.391 | 0.4551 | +0.104 | -0.064 | 0.013 ± 0.0036 |
| thinner_sample >=3000 | 1280 | 0.5288 | 0.4352 | 0.4453 | +0.084 | -0.010 | 0.0148 ± 0.0032 |
| data_status ADEQUATE | 2036 | 0.5315 | 0.4286 | 0.4396 | +0.092 | -0.011 | 0.0151 ± 0.0027 |
| data_status LIMITED | 1798 | 0.5489 | 0.4157 | 0.4666 | +0.082 | -0.051 | 0.0075 ± 0.0036 |
| data_status POOR | 3487 | 0.5609 | 0.4008 | 0.4597 | +0.101 | -0.059 | 0.0105 ± 0.0029 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1054 | 0.1979 | 0.1981 | -0.0003 ± 0.0005 | 0.5758 | 0.5765 | 0.5026 | 0.4875 | 0.5 | -0.093 ± 0.0145 | -0.0087 (8) |
| 3-5 | 676 | 0.2062 | 0.2059 | +0.0003 ± 0.0014 | 0.5972 | 0.5949 | 0.5047 | 0.4649 | 0.4808 | -0.098 ± 0.018 | 0.01 (3) |
| 5-10 | 1572 | 0.203 | 0.2018 | +0.0012 ± 0.0017 | 0.5926 | 0.5873 | 0.512 | 0.4382 | 0.4644 | -0.093 ± 0.0117 | -0.0143 (7) |
| 10-15 | 1272 | 0.2181 | 0.2094 | +0.0087 ± 0.0032 | 0.6279 | 0.6024 | 0.524 | 0.4005 | 0.4261 | -0.104 ± 0.013 | -0.055 (6) |
| 15-25 | 1628 | 0.2261 | 0.2086 | +0.0175 ± 0.0044 | 0.6473 | 0.6009 | 0.576 | 0.3814 | 0.4337 | -0.104 ± 0.0114 | -0.0045 (11) |
| 25-40 | 928 | 0.2236 | 0.2061 | +0.0174 ± 0.0089 | 0.637 | 0.5934 | 0.6523 | 0.3425 | 0.4688 | -0.068 ± 0.0137 | -0.06 (2) |
| 40+ | 191 | 0.296 | 0.1751 | +0.1210 ± 0.0272 | 0.7965 | 0.5226 | 0.7305 | 0.2751 | 0.377 | -0.082 ± 0.0262 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5489 | 0.1856 | 0.1865 | -0.0009 ± 0.0002 | 0.5474 | 0.5485 | 0.4909 | 0.4756 | 0.5072 | -0.021 ± 0.0059 | -0.01 (28) |
| 3-5 | 3663 | 0.1982 | 0.1964 | +0.0018 ± 0.0006 | 0.577 | 0.5705 | 0.4828 | 0.4431 | 0.4401 | -0.057 ± 0.0074 | 0.005 (6) |
| 5-10 | 7961 | 0.2014 | 0.1977 | +0.0037 ± 0.0007 | 0.5885 | 0.5763 | 0.4841 | 0.4104 | 0.4224 | -0.046 ± 0.005 | -0.0114 (22) |
| 10-15 | 6575 | 0.2021 | 0.1861 | +0.0160 ± 0.0013 | 0.5908 | 0.5461 | 0.4854 | 0.3615 | 0.3594 | -0.064 ± 0.0053 | -0.0379 (19) |
| 15-25 | 8354 | 0.2064 | 0.1671 | +0.0393 ± 0.0018 | 0.6048 | 0.4964 | 0.4998 | 0.3044 | 0.3023 | -0.070 ± 0.0045 | -0.0043 (51) |
| 25-40 | 6460 | 0.2231 | 0.1258 | +0.0973 ± 0.0028 | 0.6405 | 0.3866 | 0.527 | 0.2132 | 0.219 | -0.059 ± 0.0043 | -0.0733 (3) |
| 40+ | 4351 | 0.3823 | 0.0434 | +0.3389 ± 0.0036 | 0.9954 | 0.1691 | 0.6305 | 0.1011 | 0.0575 | -0.076 ± 0.003 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 850 | 0.2061 | 0.2065 | -0.0004 ± 0.0005 | 0.5931 | 0.5944 | 0.5058 | 0.491 | 0.5153 | -0.100 ± 0.0167 | -0.0117 (6) |
| 3-5 | 602 | 0.2121 | 0.2092 | +0.0029 ± 0.0015 | 0.6074 | 0.6011 | 0.5138 | 0.4743 | 0.4535 | -0.131 ± 0.0201 | 0.01 (3) |
| 5-10 | 1352 | 0.2071 | 0.2054 | +0.0017 ± 0.0019 | 0.6006 | 0.5959 | 0.5407 | 0.4661 | 0.4948 | -0.087 ± 0.0127 | -0.01 (4) |
| 10-15 | 1179 | 0.2133 | 0.2066 | +0.0066 ± 0.0033 | 0.6192 | 0.5991 | 0.5621 | 0.4377 | 0.4758 | -0.101 ± 0.0138 | -0.04 (5) |
| 15-25 | 1712 | 0.2324 | 0.2124 | +0.0200 ± 0.0044 | 0.6607 | 0.6093 | 0.5856 | 0.39 | 0.4381 | -0.101 ± 0.0114 | -0.0183 (12) |
| 25-40 | 1201 | 0.2674 | 0.1995 | +0.0679 ± 0.0081 | 0.7457 | 0.5794 | 0.6612 | 0.3472 | 0.398 | -0.118 ± 0.0129 | -0.008 (5) |
| 40+ | 425 | 0.372 | 0.1621 | +0.2098 ± 0.0196 | 1.0137 | 0.4903 | 0.737 | 0.248 | 0.2918 | -0.088 ± 0.0187 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4707 | 0.1925 | 0.1927 | -0.0002 ± 0.0002 | 0.5608 | 0.561 | 0.5075 | 0.4924 | 0.508 | -0.040 ± 0.0066 | -0.0154 (26) |
| 3-5 | 3211 | 0.193 | 0.1919 | +0.0011 ± 0.0006 | 0.5628 | 0.5593 | 0.5118 | 0.4722 | 0.4777 | -0.046 ± 0.0079 | 0.01 (5) |
| 5-10 | 7112 | 0.1967 | 0.1934 | +0.0033 ± 0.0008 | 0.5782 | 0.566 | 0.5086 | 0.4345 | 0.4521 | -0.039 ± 0.0053 | -0.0117 (6) |
| 10-15 | 5912 | 0.2028 | 0.191 | +0.0118 ± 0.0014 | 0.595 | 0.559 | 0.51 | 0.386 | 0.4012 | -0.050 ± 0.0058 | -0.0189 (18) |
| 15-25 | 8393 | 0.2173 | 0.181 | +0.0364 ± 0.0018 | 0.6317 | 0.5309 | 0.5254 | 0.3298 | 0.3371 | -0.061 ± 0.0047 | -0.014 (52) |
| 25-40 | 7581 | 0.2513 | 0.1378 | +0.1135 ± 0.0027 | 0.7096 | 0.4206 | 0.561 | 0.2439 | 0.2271 | -0.080 ± 0.0043 | -0.0095 (20) |
| 40+ | 5937 | 0.4024 | 0.0578 | +0.3446 ± 0.0036 | 1.06 | 0.2095 | 0.6545 | 0.1179 | 0.0787 | -0.075 ± 0.003 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1032 | 0.1958 | 0.1972 | -0.0014 ± 0.0005 | 0.5714 | 0.5747 | 0.5024 | 0.487 | 0.531 | -0.052 ± 0.0144 | -0.0191 (11) |
| 3-5 | 732 | 0.2073 | 0.2058 | +0.0015 ± 0.0014 | 0.6012 | 0.5959 | 0.4988 | 0.4592 | 0.4631 | -0.110 ± 0.0176 | 0.002 (5) |
| 5-10 | 1599 | 0.2035 | 0.1998 | +0.0037 ± 0.0017 | 0.5923 | 0.5819 | 0.5128 | 0.4391 | 0.4497 | -0.106 ± 0.0115 | -0.01 (10) |
| 10-15 | 1290 | 0.212 | 0.2035 | +0.0085 ± 0.0031 | 0.6144 | 0.5897 | 0.5374 | 0.414 | 0.4434 | -0.105 ± 0.0126 | -0.0286 (7) |
| 15-25 | 1553 | 0.2311 | 0.2131 | +0.0180 ± 0.0046 | 0.6597 | 0.6107 | 0.5868 | 0.3926 | 0.443 | -0.106 ± 0.0117 | -0.03 (1) |
| 25-40 | 914 | 0.2131 | 0.2105 | +0.0025 ± 0.0089 | 0.6148 | 0.6035 | 0.6597 | 0.3488 | 0.4978 | -0.055 ± 0.0138 | -0.0267 (3) |
| 40+ | 201 | 0.3076 | 0.1831 | +0.1245 ± 0.0271 | 0.8325 | 0.54 | 0.7426 | 0.2875 | 0.3881 | -0.083 ± 0.0277 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5305 | 0.1852 | 0.1858 | -0.0006 ± 0.0002 | 0.546 | 0.5468 | 0.4851 | 0.4698 | 0.4886 | -0.032 ± 0.006 | -0.0189 (44) |
| 3-5 | 3790 | 0.2038 | 0.2021 | +0.0018 ± 0.0006 | 0.5927 | 0.5866 | 0.48 | 0.4405 | 0.4388 | -0.056 ± 0.0074 | -0.0073 (22) |
| 5-10 | 8092 | 0.196 | 0.1905 | +0.0055 ± 0.0007 | 0.5753 | 0.5583 | 0.4871 | 0.4131 | 0.4131 | -0.057 ± 0.0049 | -0.0117 (42) |
| 10-15 | 6538 | 0.1943 | 0.1796 | +0.0147 ± 0.0013 | 0.5735 | 0.5307 | 0.4948 | 0.3715 | 0.3734 | -0.060 ± 0.0053 | -0.0136 (14) |
| 15-25 | 8412 | 0.2119 | 0.1727 | +0.0392 ± 0.0018 | 0.6178 | 0.5092 | 0.5128 | 0.3182 | 0.3154 | -0.070 ± 0.0045 | -0.0533 (3) |
| 25-40 | 6427 | 0.2166 | 0.1261 | +0.0905 ± 0.0028 | 0.6265 | 0.3868 | 0.5284 | 0.2129 | 0.229 | -0.050 ± 0.0043 | -0.02 (4) |
| 40+ | 4289 | 0.3907 | 0.0484 | +0.3422 ± 0.0038 | 1.0181 | 0.1816 | 0.6395 | 0.1071 | 0.0648 | -0.075 ± 0.0032 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1471 | 0.1981 | 0.1981 | +0.0000 ± 0.0004 | 0.5749 | 0.5747 | 0.5087 | 0.4937 | 0.4969 | -0.069 ± 0.0119 | -0.0221 (56) |
| 3-5 | 1054 | 0.1887 | 0.1885 | +0.0001 ± 0.0011 | 0.5554 | 0.5533 | 0.4983 | 0.4584 | 0.4753 | -0.057 ± 0.0137 | -0.0194 (34) |
| 5-10 | 2128 | 0.2001 | 0.1952 | +0.0049 ± 0.0014 | 0.59 | 0.5738 | 0.5078 | 0.4342 | 0.4384 | -0.077 ± 0.0098 | -0.005 (78) |
| 10-15 | 1458 | 0.2145 | 0.2024 | +0.0121 ± 0.0029 | 0.6224 | 0.5884 | 0.5419 | 0.419 | 0.43 | -0.087 ± 0.0121 | 0.0012 (66) |
| 15-25 | 1919 | 0.2306 | 0.2079 | +0.0227 ± 0.0041 | 0.6583 | 0.5997 | 0.5919 | 0.397 | 0.4377 | -0.088 ± 0.0105 | -0.0214 (59) |
| 25-40 | 1145 | 0.2399 | 0.2109 | +0.0290 ± 0.0083 | 0.6852 | 0.6047 | 0.689 | 0.377 | 0.4865 | -0.085 ± 0.0128 | -0.0252 (27) |
| 40+ | 414 | 0.3241 | 0.2011 | +0.1230 ± 0.021 | 0.9319 | 0.5854 | 0.8175 | 0.3416 | 0.4662 | -0.097 ± 0.0196 | -0.1137 (8) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5407 | 0.1779 | 0.178 | -0.0001 ± 0.0002 | 0.5264 | 0.5261 | 0.5118 | 0.4965 | 0.5051 | -0.040 ± 0.0058 | -0.0154 (103) |
| 3-5 | 3731 | 0.1952 | 0.1944 | +0.0009 ± 0.0006 | 0.5695 | 0.567 | 0.5022 | 0.4625 | 0.4723 | -0.040 ± 0.0073 | -0.0212 (73) |
| 5-10 | 7589 | 0.1966 | 0.1902 | +0.0065 ± 0.0008 | 0.5805 | 0.5606 | 0.5015 | 0.428 | 0.4222 | -0.062 ± 0.0051 | -0.0084 (134) |
| 10-15 | 5187 | 0.2095 | 0.1934 | +0.0162 ± 0.0015 | 0.6103 | 0.5673 | 0.5367 | 0.4137 | 0.4079 | -0.071 ± 0.0062 | -0.0057 (111) |
| 15-25 | 6332 | 0.2314 | 0.2 | +0.0314 ± 0.0022 | 0.6648 | 0.5795 | 0.577 | 0.3816 | 0.3997 | -0.068 ± 0.0057 | -0.026 (108) |
| 25-40 | 4122 | 0.2569 | 0.1906 | +0.0663 ± 0.0043 | 0.7269 | 0.5548 | 0.6407 | 0.3283 | 0.3811 | -0.065 ± 0.0067 | -0.0277 (53) |
| 40+ | 1838 | 0.3683 | 0.1599 | +0.2084 ± 0.0096 | 1.0389 | 0.4758 | 0.7457 | 0.245 | 0.2976 | -0.062 ± 0.0089 | -0.054 (15) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 7321 | 1.026 ± 0.033 | 1.098 | 0.1684 | 0.1677 | 0.2153 | 0.2043 |
| gen2 | 7321 | 0.815 ± 0.03 | 1.071 | 0.1734 | 0.168 | 0.2338 | 0.2042 |
| gen1_elo | 7321 | 1.011 ± 0.032 | 1.09 | 0.1747 | 0.1678 | 0.2142 | 0.2044 |
| gen1_sr | 7321 | 1.003 ± 0.039 | 1.126 | 0.1333 | 0.1696 | 0.2297 | 0.2039 |
| gen1_ledger | 9589 | 0.868 ± 0.024 | 1.076 | 0.1894 | 0.1748 | 0.2169 | 0.2007 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 34,090)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 7,980 | 23.4% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,797 | 22.9% |
| BOOK_QUALITY | execution | 6,029 | 17.7% |
| POOR_DATA | data | 3,909 | 11.5% |
| LIMITED_DATA | data | 2,100 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,960 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 1,412 | 4.1% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,382 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 963 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 557 | 1.6% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 23.4%, coverage 22.9%, execution 17.7%, data 17.6%, market_freshness/coverage 8.6%, mapping 4.1%, model_calibration_or_unknown 4.0%, model_calibration 1.6%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.6%, LOW_DATA_QUALITY 71.4%, THIN_PLAYER_HISTORY 59.6%, STALE_PLAYER_DATA 51.8%, STALE_KALSHI_QUOTE 46.6%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 33.0%, WIDE_SPREAD 24.0%, MODEL_HIGH_UNCERTAINTY 18.7%, PLAYER_IDENTITY_RISK 15.2%, LEVEL_TRANSFER_RISK 9.9%, LOW_DISPLAYED_LIQUIDITY 8.3%, EVENT_MAPPING_RISK 7.2%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.3%, POST_SETTLEMENT_OBSERVATION 22.9%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 18,151)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,259 | 34.5% |
| STALE_QUOTE | market_freshness | 3,554 | 19.6% |
| BOOK_QUALITY | execution | 3,124 | 17.2% |
| POOR_DATA | data | 1,653 | 9.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,044 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 785 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 631 | 3.5% |
| LIMITED_DATA | data | 619 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 343 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 138 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.5%, market_freshness 19.6%, execution 17.2%, data 12.5%, market_freshness/coverage 9.2%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 74.6%, THIN_PLAYER_HISTORY 61.6%, STALE_KALSHI_QUOTE 54.0%, STALE_PLAYER_DATA 45.5%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 34.2%, WIDE_SPREAD 23.3%, MODEL_HIGH_UNCERTAINTY 19.3%, PLAYER_IDENTITY_RISK 18.2%, EVENT_MAPPING_RISK 8.8%, LEVEL_TRANSFER_RISK 8.7%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.5%, POST_SETTLEMENT_OBSERVATION 34.5%, POSSIBLE_IN_PLAY_QUOTE 6.2%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 14512, "IDENTITY_AMBIGUOUS": 3639}; ticker orientation: {"VERIFIED": 18151}.

Checks: discipline:AMBIGUOUS 1205, discipline:PASS 16946, identity_confidence:AMBIGUOUS 3306, identity_confidence:PASS 14845, level_mapping:NA 1217, level_mapping:PASS 16934, market_pair:AMBIGUOUS 494, market_pair:NA 411, market_pair:PASS 17246, model_complement:NA 373, model_complement:PASS 17778, namesake:AMBIGUOUS 6, namesake:PASS 18145, physical_match_id:NA 6138, physical_match_id:PASS 12013, player_ids:PASS 18151, same_pair_other_event:PASS 18151, ticker_orientation:PASS 18151

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,457 | 3.8% | 3.2% | 1.3% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 24, "market_freshness/coverage": 21} | 5.51 | 0.2229 / 0.2184 (835) | 25.1% | 2.4% | 3.0% | 3.0% |
| CHALLENGER | 12,215 | 16.4% | 6.2% | 11.1% | {"coverage": 1189, "market_freshness": 245, "market_freshness/coverage": 226, "data": 166, "model_calibration_or_unknown": 82, "execution": 41, "model_calibration": 39, "mapping": 17, "possible_market_error": 1} | 7.42 | 0.2212 / 0.211 (2823) | 39.3% | 14.6% | 4.0% | 22.2% |
| DOUBLES | 2,603 | 46.3% | 46.3% | 6.6% | {"execution": 666, "mapping": 356, "market_freshness": 106, "market_freshness/coverage": 70, "coverage": 7} | 23.2 | 0.2973 / 0.232 (648) | 9.0% | 0.0% | 100.0% | 6.3% |
| ITF_MEN | 23,645 | 25.2% | 17.6% | 32.8% | {"coverage": 2085, "market_freshness": 1183, "execution": 997, "data": 874, "market_freshness/coverage": 591, "mapping": 207, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.71 | 0.218 / 0.1999 (5008) | 40.4% | 69.1% | 15.1% | 21.5% |
| ITF_WOMEN | 30,827 | 26.4% | 18.9% | 44.9% | {"coverage": 2899, "market_freshness": 1759, "execution": 1337, "data": 1131, "market_freshness/coverage": 710, "mapping": 199, "model_calibration_or_unknown": 94, "model_calibration": 23} | 12.5 | 0.2025 / 0.1941 (5984) | 41.5% | 57.0% | 9.9% | 21.8% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,871 | 6.0% | 5.1% | 1.6% | {"market_freshness": 111, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.68 | 0.2312 / 0.2209 (800) | 30.1% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.6% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 523 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 638 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 17.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 1025 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 172 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 12 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 547 min (STALE); no external reference |
| 15 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 16 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 18 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 15.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 928 min (STALE); no external reference |
| 19 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 20 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 21 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 22 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 23 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 24 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 25 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 454 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 26 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 27 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 28 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 29 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 30 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 31 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 32 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 33 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 34 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 35 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 36 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 37 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 38 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 39 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 40 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 41 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 768 min (STALE); no external reference |
| 43 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 44 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 45 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 46 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.1h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 446 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 49 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 50 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.3h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 748 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9705, "by_level_share_of_ge_25pp": {"ATP": 0.0134, "CHALLENGER": 0.1105, "DOUBLES": 0.0664, "ITF_MEN": 0.3277, "ITF_WOMEN": 0.4491, "OTHER": 0.0007, "WTA": 0.016, "WTA125": 0.0161}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5404, "share_primary_cause_market_settled_or_in_play": 0.4371, "share_primary_cause_stale_quote_only": 0.1958}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 18151, "identity_ambiguous_share": 0.2005, "ticker_orientation": {"VERIFIED": 18151}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 12013, "with_external": 627, "coverage": 0.0522, "external_status": {"EXTERNAL_STALE": 398, "AGREES_WITH_KALSHI": 216, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 398, "MODEL_LONE_OUTLIER": 216, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3445, "share_external_supports_model": 0.0207}, "pregame_clean_ge_25pp": {"n": 5592, "with_external": 596, "coverage": 0.1066, "external_status": {"EXTERNAL_STALE": 374, "AGREES_WITH_KALSHI": 209, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 374, "MODEL_LONE_OUTLIER": 209, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3507, "share_external_supports_model": 0.0218}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 491.5, "median_sample_ratio": 2.44, "median_min_matches": 19.0, "median_max_days_since_last": 240.0, "share_severe_asymmetry": 0.2079, "data_status": {"POOR": 10154, "LIMITED": 4695, "ADEQUATE": 3302}, "comparison_lt_10pp": {"median_thinner_serve_points": 1743.0, "median_sample_ratio": 1.69, "median_min_matches": 91.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1475, "model_minus_observed": 0.0648, "kalshi_minus_observed": -0.0744, "brier_diff_model_minus_kalshi": 0.0021}, "4-10x": {"n": 999, "model_minus_observed": 0.0907, "kalshi_minus_observed": -0.054, "brier_diff_model_minus_kalshi": 0.0088}, "<2x": {"n": 3615, "model_minus_observed": 0.0983, "kalshi_minus_observed": -0.0244, "brier_diff_model_minus_kalshi": 0.014}, ">=10x": {"n": 1232, "model_minus_observed": 0.1188, "kalshi_minus_observed": -0.0548, "brier_diff_model_minus_kalshi": 0.0147}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 7321, "model": {"intercept": -0.551, "slope": 0.815, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.181, "slope": 1.071, "slope_se": 0.033}, "mean_extremity_model": 0.1734, "mean_extremity_kalshi": 0.168, "model_brier": 0.2338, "kalshi_brier": 0.2042, "brier_diff_model_minus_kalshi": 0.0296, "brier_diff_se": 0.0022, "model_logloss": 0.6651, "kalshi_logloss": 0.591}, "fair_v1": {"n": 7321, "model": {"intercept": -0.45, "slope": 1.026, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.245, "slope": 1.098, "slope_se": 0.034}, "mean_extremity_model": 0.1684, "mean_extremity_kalshi": 0.1677, "model_brier": 0.2153, "kalshi_brier": 0.2043, "brier_diff_model_minus_kalshi": 0.011, "brier_diff_se": 0.0018, "model_logloss": 0.6198, "kalshi_logloss": 0.5912}, "gen1_elo": {"n": 7321, "model": {"intercept": -0.436, "slope": 1.011, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.249, "slope": 1.09, "slope_se": 0.033}, "mean_extremity_model": 0.1747, "mean_extremity_kalshi": 0.1678, "model_brier": 0.2142, "kalshi_brier": 0.2044, "brier_diff_model_minus_kalshi": 0.0098, "brier_diff_se": 0.0018, "model_logloss": 0.6178, "kalshi_logloss": 0.5913}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2487, "share_ge_15": 0.4447, "median_abs_gap": 13.05, "n": 48306}, "gen1_elo": {"share_ge_25": 0.246, "share_ge_15": 0.4402, "median_abs_gap": 12.84, "n": 48306}, "gen1_sr": {"share_ge_25": 0.3132, "share_ge_15": 0.5204, "median_abs_gap": 15.83, "n": 48306}, "gen2": {"share_ge_25": 0.3143, "share_ge_15": 0.5104, "median_abs_gap": 15.46, "n": 48306}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1505, "share_ge_15": 0.3531, "median_abs_gap": 10.66, "n": 37150}, "gen1_elo": {"share_ge_25": 0.1485, "share_ge_15": 0.3476, "median_abs_gap": 10.48, "n": 37150}, "gen1_sr": {"share_ge_25": 0.2151, "share_ge_15": 0.4384, "median_abs_gap": 12.96, "n": 37152}, "gen2": {"share_ge_25": 0.2305, "share_ge_15": 0.4381, "median_abs_gap": 12.83, "n": 37152}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.51, "share_ge_25_all": 0.0378, "share_ge_25_pregame_clean": 0.0318}, "WTA": {"median_abs_gap_pregame_clean": 7.68, "share_ge_25_all": 0.0597, "share_ge_25_pregame_clean": 0.0507}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2366, "share_within_10pp_all": 0.4386, "share_within_10pp_pregame_clean": 0.4922, "corr_model_vs_mid_pregame_clean": 0.8497}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1054, "model_brier": 0.1979, "kalshi_brier": 0.1981, "brier_diff_model_minus_kalshi": -0.0003}, "10-15": {"n_settled": 1272, "model_brier": 0.2181, "kalshi_brier": 0.2094, "brier_diff_model_minus_kalshi": 0.0087}, "15-25": {"n_settled": 1628, "model_brier": 0.2261, "kalshi_brier": 0.2086, "brier_diff_model_minus_kalshi": 0.0175}, "25-40": {"n_settled": 928, "model_brier": 0.2236, "kalshi_brier": 0.2061, "brier_diff_model_minus_kalshi": 0.0174}, "3-5": {"n_settled": 676, "model_brier": 0.2062, "kalshi_brier": 0.2059, "brier_diff_model_minus_kalshi": 0.0003}, "40+": {"n_settled": 191, "model_brier": 0.296, "kalshi_brier": 0.1751, "brier_diff_model_minus_kalshi": 0.121}, "5-10": {"n_settled": 1572, "model_brier": 0.203, "kalshi_brier": 0.2018, "brier_diff_model_minus_kalshi": 0.0012}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.551, "slope": 0.815, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.181, "slope": 1.071, "slope_se": 0.033}, "n": 7321}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.484, "slope": 0.868, "slope_se": 0.024}, "kalshi_slope": {"intercept": 0.176, "slope": 1.076, "slope_se": 0.028}, "n": 9589}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 648, "model_brier": 0.2973, "kalshi_brier": 0.232, "brier_diff_model_minus_kalshi": 0.0653, "brier_diff_se": 0.0115, "corr_model_outcome": 0.1062, "corr_kalshi_outcome": 0.2841}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
