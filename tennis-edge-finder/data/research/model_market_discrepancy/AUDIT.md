# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-17T11:28Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 35,915): 0-3 14.6%, 3-5 9.5%, 5-10 20.0%, 10-15 15.2%, 15-25 18.8%, 25-40 13.6%, 40+ 8.3%; median gap 11.85 pp.
* **Where the extremes live**: 98.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.9%, Challenger 12.1%, doubles 6.7%). Main tour: ATP 1.9% and WTA 5.9% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 7,860): MARKET_ALREADY_SETTLED_WHEN_PRICED 36.6%, STALE_QUOTE 18.2%, BOOK_QUALITY 17.3%, POOR_DATA 8.4%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.4%, LIMITED_DATA 4.0%, IN_PLAY_QUOTE 3.2%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.5%. By class: coverage 36.6%, market_freshness 18.2%, execution 17.3%, data 12.4%, market_freshness/coverage 8.6%, mapping 4.4%, model_calibration_or_unknown 2.0%, model_calibration 0.5%.
* **Stale / settled / in-play**: 53.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 45.2% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 7,860 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.0% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 3.9%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 22.6% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 562.5 points vs 1821.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.058, Gen-2 0.855, Gen-1 ledger 0.876 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 368 model 0.2235 vs Kalshi 0.207; n 77 model 0.3005 vs Kalshi 0.1737.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 144,053 model-market comparisons (239,158 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 50,660 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-17T11:18:15.083983+00:00'], shadow board 39,923 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-17T11:18:18.521689+00:00'], Model 4 15,407 rows, 15,272 settled tickers, 5,218 tickers with an external scan.
* By model: {"gen1_ledger": 33534, "gen1_elo": 20077, "fair_v1": 20077, "gen2": 20077, "gen1_sr": 20077, "model4_fundamental": 15110, "model4_conditioned": 15101}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 35,915 | 14.6 | 9.5 | 20.0 | 15.2 | 18.8 | 13.6 | 8.3 | 11.85 | 40.7% | 21.9% |
| MW fair_v1 | 20,077 | 13.6 | 8.5 | 18.5 | 15.7 | 19.2 | 14.6 | 10.0 | 12.99 | 43.8% | 24.6% |
| MW gen1_elo | 20,077 | 13.2 | 9.0 | 19.7 | 15.1 | 19.2 | 14.3 | 9.7 | 12.48 | 43.1% | 23.9% |
| MW gen1_ledger | 15,838 | 15.8 | 10.8 | 21.9 | 14.7 | 18.3 | 12.3 | 6.2 | 10.38 | 36.8% | 18.5% |
| MW gen1_sr | 20,077 | 9.7 | 7.5 | 16.4 | 14.2 | 21.5 | 18.7 | 12.1 | 15.87 | 52.3% | 30.8% |
| MW gen2 | 20,077 | 11.4 | 7.1 | 16.5 | 14.1 | 20.0 | 17.7 | 13.2 | 15.43 | 50.9% | 30.9% |
| all families model4_conditioned | 15,101 | 21.6 | 19.7 | 34.7 | 17.0 | 4.6 | 1.4 | 1.0 | 5.86 | 7.0% | 2.3% |
| all families model4_fundamental | 15,110 | 16.7 | 13.3 | 35.2 | 19.7 | 10.9 | 3.0 | 1.2 | 7.67 | 15.2% | 4.2% |

Configurable thresholds (primary): >=5pp 76.0%, >=10pp 56.0%, >=15pp 40.7%, >=20pp 30.2%, >=25pp 21.9%, >=30pp 15.9%, >=40pp 8.3%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.49pp; >=10pp 45.4%, >=25pp 17.5%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,439 | 30.9 | 14.0 | 24.9 | 17.0 | 10.9 | 1.5 | 0.8 | 5.84 | 13.3% | 2.4% |
| CHALLENGER | 3,319 | 16.0 | 9.9 | 20.2 | 15.7 | 14.4 | 12.3 | 11.5 | 11.4 | 38.2% | 23.8% |
| ITF_MEN | 5,729 | 10.9 | 8.1 | 17.6 | 14.8 | 19.8 | 16.4 | 12.4 | 14.45 | 48.6% | 28.8% |
| ITF_WOMEN | 7,863 | 10.4 | 6.6 | 16.0 | 15.6 | 22.2 | 18.0 | 11.1 | 15.51 | 51.3% | 29.1% |
| WTA | 1,083 | 20.6 | 12.3 | 25.1 | 15.9 | 19.7 | 5.5 | 1.0 | 7.82 | 26.1% | 6.5% |
| WTA125 | 644 | 13.0 | 7.6 | 23.8 | 20.2 | 20.0 | 13.3 | 2.0 | 11.14 | 35.4% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,439 | 24.3 | 14.5 | 24.4 | 18.8 | 14.4 | 2.4 | 1.1 | 6.81 | 17.9% | 3.5% |
| CHALLENGER | 3,319 | 14.8 | 8.1 | 19.3 | 13.6 | 17.9 | 14.2 | 12.1 | 12.69 | 44.2% | 26.4% |
| ITF_MEN | 5,729 | 9.4 | 6.8 | 15.8 | 13.6 | 19.8 | 19.5 | 15.1 | 16.84 | 54.4% | 34.6% |
| ITF_WOMEN | 7,863 | 8.6 | 5.7 | 13.8 | 13.3 | 21.3 | 20.8 | 16.6 | 18.71 | 58.6% | 37.4% |
| WTA | 1,083 | 17.2 | 8.2 | 20.8 | 15.3 | 22.2 | 15.1 | 1.1 | 11.5 | 38.5% | 16.2% |
| WTA125 | 644 | 6.4 | 4.8 | 17.4 | 17.9 | 25.5 | 19.1 | 9.0 | 16.79 | 53.6% | 28.1% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,439 | 27.9 | 13.8 | 28.0 | 15.6 | 11.3 | 2.6 | 0.9 | 6.29 | 14.8% | 3.5% |
| CHALLENGER | 3,319 | 14.8 | 10.3 | 20.8 | 14.9 | 15.5 | 12.0 | 11.7 | 11.01 | 39.1% | 23.7% |
| ITF_MEN | 5,729 | 10.0 | 8.1 | 17.9 | 14.1 | 20.5 | 16.7 | 12.6 | 14.97 | 49.8% | 29.3% |
| ITF_WOMEN | 7,863 | 9.9 | 7.0 | 16.5 | 15.6 | 22.7 | 18.0 | 10.3 | 15.42 | 51.0% | 28.2% |
| WTA | 1,083 | 23.4 | 16.2 | 31.6 | 15.3 | 10.7 | 2.2 | 0.7 | 6.05 | 13.6% | 2.9% |
| WTA125 | 644 | 22.2 | 12.4 | 29.5 | 15.5 | 14.1 | 5.9 | 0.3 | 7.73 | 20.3% | 6.2% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 822 | 30.8 | 22.0 | 33.6 | 10.3 | 2.2 | 1.0 | 0.1 | 4.76 | 3.3% | 1.1% |
| CHALLENGER | 2,268 | 22.8 | 15.1 | 27.6 | 14.6 | 12.8 | 5.2 | 2.0 | 6.92 | 19.9% | 7.1% |
| DOUBLES | 1,085 | 5.3 | 3.9 | 11.1 | 10.9 | 20.2 | 24.7 | 24.0 | 24.1 | 68.8% | 48.7% |
| ITF_MEN | 4,829 | 14.7 | 8.7 | 20.7 | 15.5 | 20.8 | 12.5 | 7.1 | 11.86 | 40.4% | 19.6% |
| ITF_WOMEN | 5,196 | 11.8 | 9.3 | 19.4 | 14.9 | 22.3 | 16.4 | 5.9 | 13.04 | 44.6% | 22.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 773 | 21.7 | 16.3 | 28.5 | 16.4 | 12.0 | 4.7 | 0.4 | 6.97 | 17.1% | 5.1% |
| WTA125 | 716 | 21.1 | 13.8 | 22.5 | 18.4 | 14.1 | 8.0 | 2.1 | 8.2 | 24.2% | 10.1% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,425 | 30.8 | 14.0 | 25.1 | 17.0 | 10.9 | 1.5 | 0.8 | 5.84 | 13.2% | 2.3% |
| CHALLENGER | 2,359 | 20.8 | 12.5 | 25.5 | 18.2 | 14.9 | 5.8 | 2.3 | 8.19 | 23.1% | 8.1% |
| ITF_MEN | 4,169 | 13.3 | 10.1 | 20.9 | 16.6 | 20.2 | 13.3 | 5.7 | 11.54 | 39.1% | 18.9% |
| ITF_WOMEN | 5,868 | 12.4 | 8.0 | 18.2 | 17.7 | 23.6 | 15.0 | 5.1 | 13.09 | 43.6% | 20.1% |
| WTA | 1,061 | 20.7 | 11.7 | 25.4 | 15.9 | 19.8 | 5.4 | 1.0 | 7.85 | 26.2% | 6.4% |
| WTA125 | 618 | 13.4 | 7.4 | 23.3 | 20.6 | 20.7 | 12.9 | 1.6 | 11.25 | 35.3% | 14.6% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,425 | 24.2 | 14.6 | 24.5 | 18.8 | 14.4 | 2.4 | 1.1 | 6.81 | 17.9% | 3.5% |
| CHALLENGER | 2,359 | 19.0 | 10.4 | 24.3 | 16.3 | 18.1 | 9.3 | 2.5 | 9.0 | 30.0% | 11.8% |
| ITF_MEN | 4,170 | 11.1 | 8.0 | 18.2 | 15.3 | 21.9 | 16.9 | 8.5 | 14.11 | 47.3% | 25.5% |
| ITF_WOMEN | 5,868 | 9.7 | 6.5 | 15.3 | 14.6 | 23.3 | 20.0 | 10.6 | 16.42 | 53.8% | 30.6% |
| WTA | 1,061 | 17.1 | 8.1 | 20.7 | 15.4 | 22.3 | 15.3 | 1.1 | 11.62 | 38.7% | 16.4% |
| WTA125 | 618 | 6.2 | 5.0 | 17.5 | 18.3 | 25.4 | 19.6 | 8.1 | 16.66 | 53.1% | 27.7% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 801 | 30.7 | 22.2 | 33.8 | 10.5 | 1.6 | 1.0 | 0.1 | 4.76 | 2.8% | 1.1% |
| CHALLENGER | 1,952 | 24.6 | 16.4 | 29.8 | 14.3 | 11.9 | 2.4 | 0.5 | 6.28 | 14.8% | 2.9% |
| DOUBLES | 999 | 5.5 | 4.0 | 11.3 | 11.0 | 20.0 | 24.8 | 23.3 | 23.92 | 68.2% | 48.1% |
| ITF_MEN | 3,990 | 16.1 | 9.4 | 22.6 | 16.4 | 20.6 | 10.6 | 4.3 | 10.55 | 35.5% | 14.8% |
| ITF_WOMEN | 4,254 | 12.9 | 10.0 | 21.2 | 15.8 | 22.5 | 14.8 | 2.8 | 11.64 | 40.1% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 737 | 22.2 | 16.8 | 28.6 | 16.4 | 12.2 | 3.7 | 0.0 | 6.8 | 15.9% | 3.7% |
| WTA125 | 608 | 23.0 | 15.3 | 24.0 | 20.1 | 12.5 | 4.8 | 0.3 | 7.3 | 17.6% | 5.1% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,085 | 5.3 | 3.9 | 11.1 | 10.9 | 20.2 | 24.7 | 24.0 | 24.1 | 68.8% | 48.7% |
| singles | 14,753 | 16.6 | 11.3 | 22.7 | 15.0 | 18.2 | 11.4 | 4.9 | 9.85 | 34.5% | 16.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 4,713 | 13.3 | 8.8 | 19.3 | 15.7 | 18.1 | 14.6 | 10.2 | 12.76 | 42.9% | 24.9% |
| Grass | 229 | 10.5 | 11.3 | 18.3 | 14.0 | 22.7 | 15.3 | 7.9 | 14.16 | 45.9% | 23.1% |
| Hard | 12,993 | 14.0 | 8.5 | 18.5 | 15.2 | 19.6 | 14.4 | 9.9 | 12.96 | 43.8% | 24.2% |
| UNKNOWN | 2,142 | 12.1 | 7.3 | 16.9 | 18.6 | 19.1 | 15.7 | 10.3 | 13.38 | 45.1% | 26.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,873 | 19.9 | 10.7 | 21.2 | 16.9 | 15.7 | 8.9 | 6.7 | 9.45 | 31.3% | 15.6% |
| B | 2,629 | 13.9 | 9.1 | 19.6 | 16.3 | 18.5 | 12.3 | 10.3 | 12.04 | 41.2% | 22.6% |
| C | 2,916 | 12.6 | 9.6 | 20.0 | 14.1 | 19.1 | 14.6 | 10.0 | 12.69 | 43.7% | 24.6% |
| D | 3,420 | 11.8 | 7.9 | 17.4 | 15.8 | 21.9 | 15.3 | 9.8 | 13.95 | 47.1% | 25.2% |
| F | 5,239 | 8.1 | 5.4 | 14.9 | 14.8 | 21.8 | 21.6 | 13.5 | 17.98 | 56.9% | 35.1% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,677 | 23.3 | 15.8 | 28.8 | 15.1 | 11.0 | 4.3 | 1.6 | 6.64 | 17.0% | 5.9% |
| B | 2,354 | 14.9 | 10.1 | 24.0 | 16.4 | 19.3 | 10.9 | 4.2 | 10.18 | 34.5% | 15.2% |
| C | 3,125 | 12.1 | 7.8 | 17.9 | 14.4 | 20.9 | 15.7 | 11.1 | 13.8 | 47.7% | 26.9% |
| D | 2,330 | 14.2 | 9.8 | 20.6 | 13.7 | 21.2 | 13.8 | 6.7 | 11.86 | 41.8% | 20.5% |
| F | 3,352 | 10.5 | 7.7 | 15.2 | 14.0 | 23.4 | 20.3 | 8.9 | 16.15 | 52.6% | 29.2% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 6,642 | 18.1 | 9.7 | 20.4 | 16.6 | 16.3 | 9.9 | 9.1 | 10.5 | 35.2% | 19.0% |
| LIMITED | 4,649 | 14.6 | 10.5 | 20.7 | 15.2 | 18.5 | 13.0 | 7.5 | 11.31 | 39.0% | 20.5% |
| POOR | 8,786 | 9.6 | 6.5 | 15.9 | 15.2 | 21.8 | 19.0 | 11.9 | 16.0 | 52.7% | 31.0% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,350 | 30.2 | 24.0 | 35.5 | 7.0 | 2.1 | 1.0 | 0.1 | 4.62 | 3.2% | 1.1% |
| GAME_SPREAD | 3,078 | 25.5 | 16.1 | 36.0 | 17.3 | 4.3 | 0.6 | 0.2 | 6.02 | 5.0% | 0.8% |
| MATCH_WINNER | 15,838 | 15.8 | 10.8 | 21.9 | 14.7 | 18.3 | 12.3 | 6.2 | 10.38 | 36.8% | 18.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 6,355 | 32.6 | 19.0 | 30.7 | 10.5 | 5.7 | 1.2 | 0.3 | 4.82 | 7.2% | 1.5% |
| TOTAL_GAMES | 4,889 | 6.6 | 8.8 | 38.2 | 29.1 | 11.4 | 3.4 | 2.4 | 9.59 | 17.2% | 5.8% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,252 | 25.6 | 37.4 | 31.1 | 1.1 | 3.9 | 0.6 | 0.2 | 4.32 | 4.7% | 0.8% |
| GAME_SPREAD | 3,702 | 45.5 | 16.5 | 28.2 | 7.5 | 1.3 | 0.7 | 0.3 | 3.53 | 2.3% | 1.1% |
| TOTAL_GAMES | 6,147 | 3.8 | 6.5 | 41.7 | 36.3 | 7.3 | 2.4 | 2.0 | 9.82 | 11.7% | 4.4% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,252 | 26.4 | 18.2 | 36.7 | 9.4 | 6.5 | 2.3 | 0.4 | 5.54 | 9.3% | 2.7% |
| GAME_SPREAD | 3,702 | 19.4 | 13.4 | 29.9 | 20.9 | 13.1 | 2.5 | 0.8 | 7.78 | 16.3% | 3.3% |
| TOTAL_GAMES | 6,156 | 6.8 | 9.0 | 37.0 | 27.7 | 13.4 | 3.9 | 2.1 | 9.7 | 19.4% | 6.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 20,077 | 43.8% | 24.6% | 12.99 | 35.0% | 15.2% | 10.64 |
| gen1_elo | 20,077 | 43.1% | 23.9% | 12.48 | 33.9% | 14.9% | 10.11 |
| gen1_sr | 20,077 | 52.3% | 30.8% | 15.87 | 44.4% | 21.4% | 13.21 |
| gen2 | 20,077 | 50.9% | 30.9% | 15.43 | 44.1% | 22.8% | 13.01 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 10,720 | 16.5 | 10.4 | 21.6 | 17.2 | 19.6 | 11.3 | 3.4 | 10.41 | 34.3% | 14.7% |
| STALE | 9,357 | 10.2 | 6.2 | 15.0 | 13.9 | 18.8 | 18.3 | 17.5 | 17.35 | 54.6% | 35.9% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 9,306 | 17.6 | 11.7 | 23.4 | 14.7 | 16.8 | 11.1 | 4.7 | 9.34 | 32.6% | 15.8% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 35,915 | 9306 | 14192 | 12417 | 24.0 | 159.0 | 1400.4 |
| ge_15pp | 14,620 | 3034 | 4962 | 6624 | 26.9 | 462.1 | 1380.4 |
| ge_25pp | 7,860 | 1467 | 2167 | 4226 | 34.5 | 597.4 | 1380.4 |
| lt_10pp | 15,817 | 4902 | 6838 | 4077 | 22.1 | 48.1 | 1341.5 |

Current slate `SL-20261017T112819Z-7cce66e5`: 490 priced rows, quote age at build {'median': 10.5, 'max': 10.6}, freshness {'AGING': 490}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 11 | 0.0 | 0.0 | 36.4 | 0.0 | 45.5 | 18.2 | 0.0 | 20.19 | 63.6% | 18.2% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,764 | 21.5 | 10.9 | 23.1 | 18.0 | 18.9 | 7.0 | 0.6 | 8.52 | 26.5% | 7.5% |
| KALSHI_LONE_OUTLIER | 9 | 11.1 | 0.0 | 66.7 | 0.0 | 11.1 | 11.1 | 0.0 | 5.14 | 22.2% | 11.1% |
| MARKETS_AGREE | 317 | 69.4 | 30.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.1 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 616 | 0.0 | 3.4 | 36.4 | 26.9 | 24.2 | 8.3 | 0.8 | 11.65 | 33.3% | 9.1% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 20,077 | 2729 (13.6%) | 22.6% | 0.7% | {"EXTERNAL_STALE": 1764, "AGREES_WITH_KALSHI": 616, "ALL_AGREE": 317, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 10, "AGREES_WITH_MODEL": 9, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 8,787 | 681 (7.8%) | 30.1% | 1.3% | {"EXTERNAL_STALE": 467, "AGREES_WITH_KALSHI": 205, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 4,931 | 192 (3.9%) | 29.2% | 1.6% | {"EXTERNAL_STALE": 133, "AGREES_WITH_KALSHI": 56, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,351 | 181 (7.7%) | 29.8% | 1.7% | {"EXTERNAL_STALE": 124, "AGREES_WITH_KALSHI": 54, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 8,146 | 1565 (19.2%) | 15.7% | 0.6% | {"EXTERNAL_STALE": 980, "ALL_AGREE": 317, "AGREES_WITH_KALSHI": 245, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 7, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,883 | 11.2 | 7.7 | 19.4 | 14.8 | 22.0 | 14.4 | 10.4 | 13.83 | 46.9% | 24.8% |
| 4-10x | 2,585 | 12.8 | 8.9 | 19.9 | 15.4 | 18.6 | 15.1 | 9.2 | 12.59 | 42.9% | 24.3% |
| <2x | 10,501 | 15.4 | 9.2 | 18.9 | 16.6 | 17.7 | 13.1 | 9.1 | 11.9 | 39.8% | 22.1% |
| >=10x | 3,108 | 11.0 | 6.5 | 15.1 | 13.6 | 21.3 | 19.6 | 13.0 | 16.51 | 53.9% | 32.6% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 5,352 | 13.5 | 8.3 | 19.3 | 15.8 | 19.8 | 12.9 | 10.4 | 12.81 | 43.1% | 23.3% |
| 300-1000 | 4,487 | 12.0 | 8.7 | 17.3 | 15.8 | 20.8 | 15.8 | 9.6 | 13.73 | 46.2% | 25.4% |
| <300 | 5,939 | 9.1 | 6.0 | 15.6 | 14.6 | 21.4 | 20.3 | 13.0 | 16.92 | 54.7% | 33.3% |
| >=3000 | 4,299 | 21.6 | 11.8 | 22.9 | 16.9 | 13.7 | 7.4 | 5.7 | 8.3 | 26.8% | 13.1% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 628 | 0.5379 | 0.4043 | 0.4841 | +0.054 | -0.080 | 0.0009 ± 0.0059 |
| ratio 4-10x | 422 | 0.5842 | 0.4467 | 0.5071 | +0.077 | -0.060 | 0.0079 ± 0.0075 |
| ratio <2x | 1562 | 0.5364 | 0.4144 | 0.4507 | +0.086 | -0.036 | 0.0125 ± 0.0036 |
| ratio >=10x | 509 | 0.5463 | 0.3788 | 0.4204 | +0.126 | -0.042 | 0.0162 ± 0.0078 |
| thinner_sample 1000-3000 | 885 | 0.5431 | 0.4172 | 0.4667 | +0.076 | -0.050 | 0.007 ± 0.0048 |
| thinner_sample 300-1000 | 744 | 0.5601 | 0.4212 | 0.4839 | +0.076 | -0.063 | 0.0025 ± 0.0057 |
| thinner_sample <300 | 957 | 0.5431 | 0.3833 | 0.4336 | +0.110 | -0.050 | 0.0167 ± 0.0055 |
| thinner_sample >=3000 | 535 | 0.5292 | 0.4357 | 0.4636 | +0.066 | -0.028 | 0.0142 ± 0.005 |
| data_status ADEQUATE | 913 | 0.5331 | 0.4285 | 0.4589 | +0.074 | -0.030 | 0.0103 ± 0.0041 |
| data_status LIMITED | 782 | 0.5509 | 0.4218 | 0.4859 | +0.065 | -0.064 | 0.0037 ± 0.0052 |
| data_status POOR | 1426 | 0.5488 | 0.3937 | 0.4467 | +0.102 | -0.053 | 0.0136 ± 0.0045 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 481 | 0.1916 | 0.1931 | -0.0014 ± 0.0007 | 0.5612 | 0.5641 | 0.4941 | 0.4793 | 0.5301 | -0.041 ± 0.0209 | -0.01 (5) |
| 3-5 | 301 | 0.1905 | 0.1902 | +0.0002 ± 0.002 | 0.5605 | 0.5586 | 0.5064 | 0.4665 | 0.4817 | -0.078 ± 0.0258 | 0.02 (1) |
| 5-10 | 660 | 0.1976 | 0.197 | +0.0006 ± 0.0026 | 0.5807 | 0.5773 | 0.5105 | 0.436 | 0.4636 | -0.084 ± 0.0179 | -0.0167 (6) |
| 10-15 | 552 | 0.2137 | 0.2054 | +0.0083 ± 0.0048 | 0.616 | 0.5926 | 0.5185 | 0.3947 | 0.4221 | -0.085 ± 0.0193 | -0.048 (5) |
| 15-25 | 682 | 0.2307 | 0.2138 | +0.0168 ± 0.0069 | 0.6563 | 0.613 | 0.5746 | 0.3795 | 0.4355 | -0.084 ± 0.0176 | -0.0033 (9) |
| 25-40 | 368 | 0.2235 | 0.207 | +0.0165 ± 0.0141 | 0.6359 | 0.5959 | 0.6462 | 0.3376 | 0.4647 | -0.062 ± 0.0216 | -0.01 (1) |
| 40+ | 77 | 0.3005 | 0.1737 | +0.1268 ± 0.0425 | 0.8122 | 0.5199 | 0.743 | 0.2954 | 0.3766 | -0.118 ± 0.0418 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2259 | 0.1777 | 0.1789 | -0.0012 ± 0.0003 | 0.529 | 0.5303 | 0.479 | 0.4641 | 0.4985 | -0.020 ± 0.009 | -0.0129 (17) |
| 3-5 | 1390 | 0.1911 | 0.1891 | +0.0020 ± 0.0009 | 0.5619 | 0.5529 | 0.4789 | 0.4393 | 0.4317 | -0.065 ± 0.0119 | 0.0 (2) |
| 5-10 | 3056 | 0.1931 | 0.1904 | +0.0027 ± 0.0012 | 0.5689 | 0.5597 | 0.4817 | 0.4079 | 0.4241 | -0.047 ± 0.008 | -0.0119 (21) |
| 10-15 | 2639 | 0.2021 | 0.1833 | +0.0188 ± 0.0021 | 0.5905 | 0.5386 | 0.4787 | 0.3542 | 0.3414 | -0.075 ± 0.0083 | -0.0281 (16) |
| 15-25 | 3211 | 0.2087 | 0.1701 | +0.0386 ± 0.0028 | 0.6097 | 0.503 | 0.5008 | 0.3046 | 0.3058 | -0.070 ± 0.0073 | -0.0025 (44) |
| 25-40 | 2514 | 0.2208 | 0.1259 | +0.0950 ± 0.0044 | 0.6349 | 0.3884 | 0.5284 | 0.2154 | 0.2239 | -0.061 ± 0.0068 | -0.01 (1) |
| 40+ | 1708 | 0.3776 | 0.0429 | +0.3347 ± 0.0056 | 0.9826 | 0.1706 | 0.627 | 0.106 | 0.0556 | -0.086 ± 0.0047 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 358 | 0.1972 | 0.1976 | -0.0004 ± 0.0008 | 0.5756 | 0.5766 | 0.502 | 0.4868 | 0.5084 | -0.078 ± 0.0247 | -0.01 (3) |
| 3-5 | 247 | 0.2081 | 0.2074 | +0.0007 ± 0.0024 | 0.5981 | 0.5978 | 0.5148 | 0.4748 | 0.4818 | -0.077 ± 0.0305 | 0.02 (1) |
| 5-10 | 577 | 0.1978 | 0.1972 | +0.0006 ± 0.0028 | 0.5787 | 0.5771 | 0.5472 | 0.4723 | 0.5061 | -0.071 ± 0.0191 | -0.01 (4) |
| 10-15 | 508 | 0.2174 | 0.2097 | +0.0077 ± 0.0051 | 0.6227 | 0.6051 | 0.5682 | 0.4438 | 0.4783 | -0.088 ± 0.0212 | -0.04 (5) |
| 15-25 | 748 | 0.2281 | 0.2081 | +0.0200 ± 0.0066 | 0.6478 | 0.5984 | 0.5867 | 0.3901 | 0.4412 | -0.086 ± 0.0169 | -0.0133 (9) |
| 25-40 | 496 | 0.2663 | 0.1976 | +0.0686 ± 0.0126 | 0.7431 | 0.576 | 0.66 | 0.345 | 0.3952 | -0.112 ± 0.0198 | -0.0075 (4) |
| 40+ | 187 | 0.3663 | 0.1755 | +0.1909 ± 0.0303 | 1.0161 | 0.5215 | 0.74 | 0.2573 | 0.3155 | -0.074 ± 0.0297 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1900 | 0.1804 | 0.1807 | -0.0004 ± 0.0003 | 0.5348 | 0.5356 | 0.5006 | 0.4859 | 0.5079 | -0.033 ± 0.0101 | -0.0133 (15) |
| 3-5 | 1197 | 0.1914 | 0.1907 | +0.0007 ± 0.001 | 0.5575 | 0.5557 | 0.5147 | 0.4747 | 0.4845 | -0.040 ± 0.0129 | 0.02 (1) |
| 5-10 | 2720 | 0.1912 | 0.1883 | +0.0028 ± 0.0012 | 0.5647 | 0.5548 | 0.5097 | 0.4357 | 0.4555 | -0.042 ± 0.0084 | -0.0117 (6) |
| 10-15 | 2325 | 0.1981 | 0.1861 | +0.0119 ± 0.0022 | 0.582 | 0.5438 | 0.5173 | 0.3928 | 0.4095 | -0.051 ± 0.0091 | -0.0189 (18) |
| 15-25 | 3360 | 0.2161 | 0.1763 | +0.0399 ± 0.0029 | 0.6278 | 0.52 | 0.5311 | 0.3348 | 0.3348 | -0.073 ± 0.0073 | -0.0086 (42) |
| 25-40 | 2987 | 0.2491 | 0.1364 | +0.1127 ± 0.0043 | 0.7048 | 0.4177 | 0.5589 | 0.243 | 0.2243 | -0.086 ± 0.0068 | -0.0044 (18) |
| 40+ | 2288 | 0.401 | 0.0664 | +0.3346 ± 0.0062 | 1.055 | 0.2327 | 0.6628 | 0.1263 | 0.0962 | -0.069 ± 0.0053 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 462 | 0.1919 | 0.1944 | -0.0025 ± 0.0007 | 0.5623 | 0.5686 | 0.4942 | 0.4789 | 0.5498 | -0.006 ± 0.0209 | -0.0137 (8) |
| 3-5 | 344 | 0.1889 | 0.1869 | +0.0020 ± 0.0019 | 0.5543 | 0.5497 | 0.496 | 0.4564 | 0.4535 | -0.114 ± 0.0245 | 0.0067 (3) |
| 5-10 | 688 | 0.202 | 0.1976 | +0.0044 ± 0.0026 | 0.5912 | 0.5773 | 0.5032 | 0.4295 | 0.4331 | -0.098 ± 0.0174 | -0.0071 (7) |
| 10-15 | 540 | 0.2063 | 0.2057 | +0.0006 ± 0.0048 | 0.5999 | 0.5944 | 0.5366 | 0.4137 | 0.4759 | -0.061 ± 0.0193 | -0.0317 (6) |
| 15-25 | 630 | 0.2367 | 0.2098 | +0.0269 ± 0.0071 | 0.6738 | 0.6036 | 0.5826 | 0.3893 | 0.4159 | -0.112 ± 0.0181 | -0.03 (1) |
| 25-40 | 384 | 0.2112 | 0.212 | -0.0008 ± 0.0137 | 0.6093 | 0.6071 | 0.6513 | 0.3417 | 0.4948 | -0.043 ± 0.021 | 0.015 (2) |
| 40+ | 73 | 0.3169 | 0.1888 | +0.1280 ± 0.0458 | 0.8528 | 0.5544 | 0.747 | 0.2937 | 0.3836 | -0.098 ± 0.048 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2141 | 0.1832 | 0.1841 | -0.0009 ± 0.0003 | 0.5413 | 0.543 | 0.4823 | 0.467 | 0.4946 | -0.024 ± 0.0093 | -0.0163 (35) |
| 3-5 | 1485 | 0.1865 | 0.1832 | +0.0033 ± 0.0009 | 0.5498 | 0.542 | 0.4763 | 0.4368 | 0.4155 | -0.084 ± 0.0114 | -0.0094 (18) |
| 5-10 | 3252 | 0.1946 | 0.1877 | +0.0069 ± 0.0011 | 0.5743 | 0.5519 | 0.4794 | 0.4055 | 0.3939 | -0.071 ± 0.0076 | -0.01 (31) |
| 10-15 | 2497 | 0.1951 | 0.1806 | +0.0145 ± 0.0021 | 0.5746 | 0.5305 | 0.4965 | 0.3732 | 0.3765 | -0.063 ± 0.0085 | -0.015 (12) |
| 15-25 | 3293 | 0.21 | 0.169 | +0.0410 ± 0.0028 | 0.6145 | 0.5011 | 0.5037 | 0.3085 | 0.3025 | -0.075 ± 0.0072 | -0.03 (2) |
| 25-40 | 2459 | 0.2158 | 0.1245 | +0.0913 ± 0.0045 | 0.6234 | 0.3836 | 0.5253 | 0.2096 | 0.2265 | -0.057 ± 0.0068 | 0.01 (3) |
| 40+ | 1650 | 0.392 | 0.0467 | +0.3453 ± 0.006 | 1.0224 | 0.1805 | 0.6371 | 0.11 | 0.0576 | -0.088 ± 0.0051 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 804 | 0.1954 | 0.1955 | -0.0001 ± 0.0005 | 0.571 | 0.5711 | 0.5082 | 0.4931 | 0.4988 | -0.049 ± 0.0156 | -0.0224 (49) |
| 3-5 | 572 | 0.1941 | 0.1932 | +0.0009 ± 0.0015 | 0.5661 | 0.5627 | 0.4805 | 0.4407 | 0.4476 | -0.051 ± 0.0185 | -0.0194 (34) |
| 5-10 | 1199 | 0.197 | 0.1909 | +0.0061 ± 0.0019 | 0.5811 | 0.5635 | 0.4876 | 0.414 | 0.4103 | -0.066 ± 0.0129 | -0.005 (78) |
| 10-15 | 760 | 0.2073 | 0.1959 | +0.0113 ± 0.004 | 0.603 | 0.5734 | 0.506 | 0.3829 | 0.3974 | -0.055 ± 0.0162 | 0.0014 (64) |
| 15-25 | 1011 | 0.2337 | 0.2112 | +0.0225 ± 0.0057 | 0.666 | 0.6083 | 0.5653 | 0.3704 | 0.4115 | -0.057 ± 0.0145 | -0.0214 (59) |
| 25-40 | 582 | 0.2496 | 0.1957 | +0.0539 ± 0.0113 | 0.7041 | 0.569 | 0.6468 | 0.3344 | 0.4021 | -0.080 ± 0.017 | -0.0219 (26) |
| 40+ | 196 | 0.3734 | 0.1909 | +0.1825 ± 0.0318 | 1.0774 | 0.5624 | 0.7925 | 0.3008 | 0.3827 | -0.078 ± 0.0286 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2414 | 0.1864 | 0.1865 | -0.0000 ± 0.0003 | 0.5479 | 0.547 | 0.5039 | 0.4885 | 0.4988 | -0.034 ± 0.0088 | -0.0157 (88) |
| 3-5 | 1647 | 0.1877 | 0.1851 | +0.0027 ± 0.0008 | 0.5499 | 0.5437 | 0.4866 | 0.447 | 0.4341 | -0.059 ± 0.0107 | -0.0209 (69) |
| 5-10 | 3347 | 0.1931 | 0.1851 | +0.0081 ± 0.0011 | 0.5711 | 0.5481 | 0.4818 | 0.4081 | 0.3932 | -0.067 ± 0.0075 | -0.0082 (132) |
| 10-15 | 2246 | 0.2036 | 0.1894 | +0.0143 ± 0.0023 | 0.5948 | 0.557 | 0.5109 | 0.3878 | 0.3914 | -0.055 ± 0.0092 | -0.0053 (105) |
| 15-25 | 2823 | 0.2302 | 0.1977 | +0.0326 ± 0.0033 | 0.6638 | 0.5748 | 0.5566 | 0.3613 | 0.3773 | -0.063 ± 0.0084 | -0.0253 (107) |
| 25-40 | 1916 | 0.2541 | 0.1695 | +0.0846 ± 0.0059 | 0.7196 | 0.5013 | 0.6079 | 0.2938 | 0.3184 | -0.076 ± 0.0091 | -0.0229 (51) |
| 40+ | 922 | 0.3865 | 0.1301 | +0.2564 ± 0.0127 | 1.0944 | 0.3981 | 0.7091 | 0.2021 | 0.2158 | -0.070 ± 0.0113 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3121 | 1.058 ± 0.05 | 1.171 | 0.1685 | 0.1717 | 0.2116 | 0.2015 |
| gen2 | 3121 | 0.855 ± 0.045 | 1.131 | 0.1759 | 0.1717 | 0.23 | 0.2015 |
| gen1_elo | 3121 | 1.041 ± 0.049 | 1.156 | 0.1737 | 0.1721 | 0.2106 | 0.2014 |
| gen1_sr | 3121 | 1.062 ± 0.059 | 1.193 | 0.1355 | 0.1734 | 0.226 | 0.2012 |
| gen1_ledger | 5124 | 0.876 ± 0.034 | 1.077 | 0.1776 | 0.1859 | 0.2179 | 0.1972 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 14,620)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,636 | 24.9% |
| STALE_QUOTE | market_freshness | 3,046 | 20.8% |
| BOOK_QUALITY | execution | 2,609 | 17.8% |
| POOR_DATA | data | 1,606 | 11.0% |
| LIMITED_DATA | data | 1,051 | 7.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 788 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 698 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 596 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 411 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 178 | 1.2% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 24.9%, market_freshness 20.8%, data 18.2%, execution 17.8%, market_freshness/coverage 8.2%, model_calibration_or_unknown 4.8%, mapping 4.1%, model_calibration 1.2%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 95.7%, LOW_DATA_QUALITY 69.0%, THIN_PLAYER_HISTORY 57.7%, STALE_PLAYER_DATA 52.0%, STALE_KALSHI_QUOTE 45.3%, MODEL_INTERNAL_DISAGREEMENT 39.5%, ASYMMETRIC_SAMPLE_SIZE 31.7%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 17.7%, PLAYER_IDENTITY_RISK 14.2%, LEVEL_TRANSFER_RISK 8.3%, EVENT_MAPPING_RISK 8.0%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 3.4%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 27.2%, POST_SETTLEMENT_OBSERVATION 24.9%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 7,860)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,875 | 36.6% |
| STALE_QUOTE | market_freshness | 1,428 | 18.2% |
| BOOK_QUALITY | execution | 1,363 | 17.3% |
| POOR_DATA | data | 662 | 8.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 425 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 344 | 4.4% |
| LIMITED_DATA | data | 313 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 254 | 3.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 157 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 39 | 0.5% |

Cause class: coverage 36.6%, market_freshness 18.2%, execution 17.3%, data 12.4%, market_freshness/coverage 8.6%, mapping 4.4%, model_calibration_or_unknown 2.0%, model_calibration 0.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.9%, START_UNVERIFIABLE 98.1%, LOW_DATA_QUALITY 72.7%, THIN_PLAYER_HISTORY 60.1%, STALE_KALSHI_QUOTE 53.8%, STALE_PLAYER_DATA 47.0%, MODEL_INTERNAL_DISAGREEMENT 40.5%, ASYMMETRIC_SAMPLE_SIZE 33.5%, WIDE_SPREAD 23.2%, MODEL_HIGH_UNCERTAINTY 18.1%, PLAYER_IDENTITY_RISK 17.5%, EVENT_MAPPING_RISK 9.6%, LOW_DISPLAYED_LIQUIDITY 8.1%, LEVEL_TRANSFER_RISK 7.3%, MODEL_CALIBRATION_OUTLIER 4.4%, EXTERNAL_MARKET_REJECTION 1.0%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 39.3%, POST_SETTLEMENT_OBSERVATION 36.6%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 6287, "IDENTITY_AMBIGUOUS": 1573}; ticker orientation: {"VERIFIED": 7860}.

Checks: discipline:AMBIGUOUS 528, discipline:PASS 7332, identity_confidence:AMBIGUOUS 1374, identity_confidence:PASS 6486, level_mapping:NA 540, level_mapping:PASS 7320, market_pair:AMBIGUOUS 283, market_pair:NA 198, market_pair:PASS 7379, model_complement:NA 165, model_complement:PASS 7695, namesake:PASS 7860, physical_match_id:NA 2929, physical_match_id:PASS 4931, player_ids:PASS 7860, same_pair_other_event:PASS 7860, ticker_orientation:PASS 7860

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,261 | 1.9% | 1.9% | 0.5% | {"market_freshness": 22, "execution": 10, "data": 7, "model_calibration_or_unknown": 3, "market_freshness/coverage": 1} | 5.29 | 0.2072 / 0.2075 (267) | 15.9% | 1.4% | 5.1% | 1.6% |
| CHALLENGER | 5,587 | 17.0% | 5.8% | 12.1% | {"coverage": 581, "market_freshness/coverage": 121, "market_freshness": 112, "data": 63, "model_calibration_or_unknown": 46, "execution": 13, "model_calibration": 9, "mapping": 6} | 7.08 | 0.2171 / 0.2043 (1463) | 37.1% | 9.5% | 2.4% | 22.8% |
| DOUBLES | 1,085 | 48.7% | 48.1% | 6.7% | {"execution": 218, "mapping": 157, "market_freshness": 106, "market_freshness/coverage": 40, "coverage": 7} | 23.92 | 0.3251 / 0.2324 (329) | 21.6% | 0.0% | 100.0% | 7.9% |
| ITF_MEN | 10,558 | 24.6% | 16.9% | 33.1% | {"coverage": 1013, "execution": 525, "market_freshness": 406, "data": 354, "market_freshness/coverage": 205, "mapping": 95, "model_calibration_or_unknown": 2} | 11.12 | 0.2133 / 0.1944 (2590) | 36.3% | 61.2% | 12.4% | 22.7% |
| ITF_WOMEN | 13,059 | 26.4% | 19.0% | 43.8% | {"coverage": 1257, "market_freshness": 707, "execution": 568, "data": 517, "market_freshness/coverage": 263, "mapping": 80, "model_calibration_or_unknown": 44, "model_calibration": 10} | 12.57 | 0.203 / 0.1912 (2751) | 39.1% | 56.8% | 10.0% | 22.5% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,856 | 5.9% | 5.3% | 1.4% | {"market_freshness": 36, "model_calibration_or_unknown": 23, "execution": 15, "data": 11, "market_freshness/coverage": 10, "model_calibration": 9, "coverage": 4, "mapping": 1} | 7.45 | 0.2348 / 0.2274 (331) | 24.2% | 1.8% | 1.9% | 3.1% |
| WTA125 | 1,360 | 12.6% | 9.9% | 2.2% | {"market_freshness/coverage": 38, "model_calibration_or_unknown": 37, "market_freshness": 37, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.16 | 0.2172 / 0.2063 (472) | 22.9% | 7.5% | 4.7% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 5 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 6 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 7 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 9 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 10 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 11 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 12 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 13 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 14 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 15 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 16 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 17 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 18 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 19 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 20 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 22 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 23 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 24 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 25 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 26 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 27 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 28 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 9.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 553 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 29 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 30 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 31 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 32 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 33 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 162 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 34 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 35 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 874 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 36 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 37 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 38 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 33 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 39 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 40 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 41 | `KXITFWMATCH-26OCT16ESTLAB-LAB` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 68 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1475.0, ratio 2.28); no external reference |
| 42 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 43 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 44 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 45 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.8h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 359 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 46 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 47 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 48 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 49 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 50 | `KXATPCHALLENGERMATCH-26OCT13GIUSEA-SEA` | CHALLENGER | fair_v1 | 76% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 757 min (STALE); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9807, "by_level_share_of_ge_25pp": {"ATP": 0.0055, "CHALLENGER": 0.121, "DOUBLES": 0.0672, "ITF_MEN": 0.3308, "ITF_WOMEN": 0.4384, "OTHER": 0.0015, "WTA": 0.0139, "WTA125": 0.0218}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5377, "share_primary_cause_market_settled_or_in_play": 0.4522, "share_primary_cause_stale_quote_only": 0.1817}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 7860, "identity_ambiguous_share": 0.2001, "ticker_orientation": {"VERIFIED": 7860}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 4931, "with_external": 192, "coverage": 0.0389, "external_status": {"EXTERNAL_STALE": 133, "AGREES_WITH_KALSHI": 56, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 133, "MODEL_LONE_OUTLIER": 56, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.2917, "share_external_supports_model": 0.0156}, "pregame_clean_ge_25pp": {"n": 2351, "with_external": 181, "coverage": 0.077, "external_status": {"EXTERNAL_STALE": 124, "AGREES_WITH_KALSHI": 54, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 124, "MODEL_LONE_OUTLIER": 54, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.2983, "share_external_supports_model": 0.0166}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 562.5, "median_sample_ratio": 2.36, "median_min_matches": 20.0, "median_max_days_since_last": 204.0, "share_severe_asymmetry": 0.2029, "data_status": {"POOR": 4192, "LIMITED": 2233, "ADEQUATE": 1435}, "comparison_lt_10pp": {"median_thinner_serve_points": 1821.0, "median_sample_ratio": 1.68, "median_min_matches": 90.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 628, "model_minus_observed": 0.0538, "kalshi_minus_observed": -0.0798, "brier_diff_model_minus_kalshi": 0.0009}, "4-10x": {"n": 422, "model_minus_observed": 0.077, "kalshi_minus_observed": -0.0604, "brier_diff_model_minus_kalshi": 0.0079}, "<2x": {"n": 1562, "model_minus_observed": 0.0857, "kalshi_minus_observed": -0.0363, "brier_diff_model_minus_kalshi": 0.0125}, ">=10x": {"n": 509, "model_minus_observed": 0.1259, "kalshi_minus_observed": -0.0416, "brier_diff_model_minus_kalshi": 0.0162}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3121, "model": {"intercept": -0.546, "slope": 0.855, "slope_se": 0.045}, "kalshi_mid_same_rows": {"intercept": 0.23, "slope": 1.131, "slope_se": 0.052}, "mean_extremity_model": 0.1759, "mean_extremity_kalshi": 0.1717, "model_brier": 0.23, "kalshi_brier": 0.2015, "brier_diff_model_minus_kalshi": 0.0285, "brier_diff_se": 0.0034, "model_logloss": 0.656, "kalshi_logloss": 0.5848}, "fair_v1": {"n": 3121, "model": {"intercept": -0.412, "slope": 1.058, "slope_se": 0.05}, "kalshi_mid_same_rows": {"intercept": 0.302, "slope": 1.171, "slope_se": 0.053}, "mean_extremity_model": 0.1685, "mean_extremity_kalshi": 0.1717, "model_brier": 0.2116, "kalshi_brier": 0.2015, "brier_diff_model_minus_kalshi": 0.0101, "brier_diff_se": 0.0027, "model_logloss": 0.6107, "kalshi_logloss": 0.5847}, "gen1_elo": {"n": 3121, "model": {"intercept": -0.405, "slope": 1.041, "slope_se": 0.049}, "kalshi_mid_same_rows": {"intercept": 0.293, "slope": 1.156, "slope_se": 0.052}, "mean_extremity_model": 0.1737, "mean_extremity_kalshi": 0.1721, "model_brier": 0.2106, "kalshi_brier": 0.2014, "brier_diff_model_minus_kalshi": 0.0092, "brier_diff_se": 0.0027, "model_logloss": 0.6094, "kalshi_logloss": 0.5844}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2456, "share_ge_15": 0.4377, "median_abs_gap": 12.99, "n": 20077}, "gen1_elo": {"share_ge_25": 0.2393, "share_ge_15": 0.4309, "median_abs_gap": 12.48, "n": 20077}, "gen1_sr": {"share_ge_25": 0.3076, "share_ge_15": 0.5227, "median_abs_gap": 15.87, "n": 20077}, "gen2": {"share_ge_25": 0.3089, "share_ge_15": 0.5087, "median_abs_gap": 15.43, "n": 20077}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1517, "share_ge_15": 0.3497, "median_abs_gap": 10.64, "n": 15500}, "gen1_elo": {"share_ge_25": 0.149, "share_ge_15": 0.339, "median_abs_gap": 10.11, "n": 15499}, "gen1_sr": {"share_ge_25": 0.2144, "share_ge_15": 0.4442, "median_abs_gap": 13.21, "n": 15500}, "gen2": {"share_ge_25": 0.2277, "share_ge_15": 0.4409, "median_abs_gap": 13.01, "n": 15501}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.29, "share_ge_25_all": 0.019, "share_ge_25_pregame_clean": 0.0189}, "WTA": {"median_abs_gap_pregame_clean": 7.45, "share_ge_25_all": 0.0587, "share_ge_25_pregame_clean": 0.0528}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2403, "share_within_10pp_all": 0.4404, "share_within_10pp_pregame_clean": 0.498, "corr_model_vs_mid_pregame_clean": 0.8432}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 481, "model_brier": 0.1916, "kalshi_brier": 0.1931, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 552, "model_brier": 0.2137, "kalshi_brier": 0.2054, "brier_diff_model_minus_kalshi": 0.0083}, "15-25": {"n_settled": 682, "model_brier": 0.2307, "kalshi_brier": 0.2138, "brier_diff_model_minus_kalshi": 0.0168}, "25-40": {"n_settled": 368, "model_brier": 0.2235, "kalshi_brier": 0.207, "brier_diff_model_minus_kalshi": 0.0165}, "3-5": {"n_settled": 301, "model_brier": 0.1905, "kalshi_brier": 0.1902, "brier_diff_model_minus_kalshi": 0.0002}, "40+": {"n_settled": 77, "model_brier": 0.3005, "kalshi_brier": 0.1737, "brier_diff_model_minus_kalshi": 0.1268}, "5-10": {"n_settled": 660, "model_brier": 0.1976, "kalshi_brier": 0.197, "brier_diff_model_minus_kalshi": 0.0006}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.546, "slope": 0.855, "slope_se": 0.045}, "kalshi_slope": {"intercept": 0.23, "slope": 1.131, "slope_se": 0.052}, "n": 3121}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.522, "slope": 0.876, "slope_se": 0.034}, "kalshi_slope": {"intercept": 0.136, "slope": 1.077, "slope_se": 0.039}, "n": 5124}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 329, "model_brier": 0.3251, "kalshi_brier": 0.2324, "brier_diff_model_minus_kalshi": 0.0927, "brier_diff_se": 0.0173, "corr_model_outcome": 0.0177, "corr_kalshi_outcome": 0.2654}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
