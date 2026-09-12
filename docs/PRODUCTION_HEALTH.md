# Production health gates (tennis_edge/health/gates.py)

| gate | name | PASS condition | evidence |
|---|---|---|---|
| TENNIS-1 | complete Kalshi tennis discovery | latest discovery complete, catalogue fully paginated, no failures, < 36 h old | data/kalshi/discovery/<run>/summary.json |
| TENNIS-2 | taxonomy normalization | no tennis series outside the family registry; >= 99.5 % of live markets PARSED or explicitly UNSUPPORTED | series_tennis.json + parser |
| TENNIS-3 | active-market mapping | zero UNPARSED among OPEN markets | markets/*.json (open) |
| TENNIS-4 | active-market projection | every open projectable market present in the latest projection run | data/research/projections/latest.json |
| TENNIS-5 | capture freshness | latest capture manifest <= 30 min old, no incomplete stage | data/kalshi/capture/<day>/<run>.manifest.json |
| TENNIS-6 | no post-start leakage | every ledger row generated before actual first ball (or scheduled - 5 min when unknown, counted) | ledger + starts |
| TENNIS-7 | player identity integrity | no AMBIGUOUS mapping used in production | link/mapping summaries |
| TENNIS-8 | sports truth health | >= 98 % of settled predictions have gradeable sports truth | settlement table |
| TENNIS-9 | exchange settlement health | zero unexplained sports/exchange conflicts; no unreviewed important_info id change | settlements + config/kalshi_settlement_rules.json |
| TENNIS-10 | CLV close coverage | canonical close for >= 95 % of settled pregame predictions (basis breakdown reported) | close table |
| TENNIS-11 | probability consistency | no invariant violation across a match's priced markets | payoffs.check_consistency |
| TENNIS-12 | append-only ledger | hash chain intact | data/research/ledger/*.jsonl |
| TENNIS-13 | reproducible artifacts | build manifest hash matches matches.parquet; source run ids recorded | data/processed/build_manifest.json |
| TENNIS-14 | data-source freshness | newest match-data snapshot <= 8 days old and covers the current season | data/sources/*/manifest.json |

UNKNOWN (evidence absent) is treated as not-PASS. Gates are never relaxed to go green; fix the pipeline.
`python -c "from tennis_edge.health.gates import run_all; [print(g.to_dict()) for g in run_all()]"`.

## First-ball submetrics (added 2026-09-11)

`tennis_edge.health.gates.first_ball_metrics()` derives these from evidence on disk and feeds gates
TENNIS-6, TENNIS-8 and TENNIS-10:

| metric | meaning |
|---|---|
| `truths`, `strict_truths`, `no_play` | matches with any first-ball truth, with A/B truth, and confirmed walkovers |
| `by_confidence` | A / B / C / UNKNOWN distribution |
| `bracket_seconds_median`, `bracket_seconds_p90` | the timestamp error bound actually being achieved |
| `contradictions`, `contradiction_rate` | material source disagreements, and their share |
| `chain_violations` | append-only integrity of the first-ball store |
| `observations`, `matches_observed` | raw polling volume and reach |
| `watchlist.levels_with_a_wired_source` / `levels_without_any_source` | the structural coverage gap, reported as counts |
| `watchlist.pct_covered_with_source_mapping` | share of watched matches at covered levels actually bound to a source |
| `pct_classifiable`, `pct_strict_pregame` | share of prospective observations with a class other than START_UNKNOWN, and the strict share |
| `executable_close_rows`, `strict_clv_rows` | closes and CLV rows that are first-ball anchored |
| `horizons_populated` / `horizons_total` | how many canonical decision horizons had a real quote |

### What changed in the gates

* **TENNIS-6** now prefers actual first-ball truth over the scheduled fallback for every match where
  truth exists.
* **TENNIS-8** is no longer only about settled-prediction sports truth. It also requires an intact
  first-ball hash chain and that at least 90% of watched matches *at levels with a wired source* are
  actually bound to that source. Levels with no source at all are reported as counts, never averaged in.
* **TENNIS-10** measures close coverage against **strict** first-ball-anchored closes. A close cut off at
  `scheduled_start - margin` no longer counts toward it. With no A/B truth yet the gate reports UNKNOWN,
  which is a failure for production purposes, by design.

Thresholds were not moved to accommodate any of this. The gates that fail, fail because the underlying
coverage does not exist yet, and that is the information they are meant to carry.


## Wave 3 additions

* **TENNIS-14 (fundamental staleness)** is red for the WOMEN only. ATP serve statistics reach 2026-09-01
  through the TML Challenger mirror; WTA stops at 2026-04-27 and a bounded search found no free, permitted
  replacement (`docs/DATA_SOURCES.md`). Results for both tours are current to 2026-09-11 via ESPN, so the
  Elo family is fresh on both sides and only the structural model is starved.
* **Identity confidence is now graded.** An exact full-name match carries 1.0 (0.9 if the player has not
  appeared in two years); a compound-surname alias carries 0.9. Qualification requires >= 0.95, so an
  aliased identity can restore board coverage but can never drive a SHADOW_BET.
* **The opportunity store** (`data/research/opportunities/`) is append-only and hash-chained, and
  `OpportunityStore.verify_chain()` checks both the chain and each row's own fingerprint. It belongs in the
  same daily integrity sweep as the prediction ledger and the first-ball store.
