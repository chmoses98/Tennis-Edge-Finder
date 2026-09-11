# Known limitations (2026-09-11)

## Blocked / external
* **Sandbox egress**: kalshi.com, docs.kalshi.com, api.elections.kalshi.com, tennis-data.co.uk, atptour.com,
  wtatennis.com, itftennis.com, sofascore/flashscore, wikipedia, GitHub raw content for other repos are all
  denied. Every network step runs on GitHub Actions and lands on the `tennis-data` branch.
* **Upstream Sackmann repos 404**: `JeffSackmann/tennis_atp` and `tennis_wta` were unavailable; data comes from
  public forks (`Kadantte/tennis_atp` max season 2026; `VictorSquidWei/tennis_wta` max season 2026 but WTA
  rows end 2026-04-27). Fork freshness must be re-checked on every bootstrap (manifest `max_season_file`,
  TENNIS-14).
* **tennis-data.co.uk 503** for every request from the runner: ATP 2020-2026 workbooks came from a mirror;
  WTA odds benchmark absent; ATP 2000-2019 odds absent.
* **First-ball truth: solved for ATP/WTA, unsolved below it** (updated 2026-09-11 by the first-ball wave).
  Kalshi still exposes only a nominal start and a close time. A live-score feed now supplies the missing
  evidence for ATP and WTA main tour and the Grand Slams (ESPN's public scoreboard, via state transitions).
  **Challenger, ITF and qualifying have no reachable source at all**: ESPN's tennis league index carries
  `atp` and `wta` only, ATP's own site is behind Cloudflare, SofaScore returns 403 to runner IPs,
  flashscore requires signed requests, livescore.com returns 503, and the ITF's own scoreboard is served by
  a provider whose API paths the site builds dynamically (a headless-browser probe observed the widget make
  zero data requests). Those matches stay START_UNKNOWN and are excluded from strict pregame research.
  **Doubles coverage is unverified.** See docs/FIRST_BALL_SOURCES.md.
* **Historical first-ball recovery is impossible from any reachable source.** Across 1,378 completed ESPN
  competitions, zero report a start differing from their scheduled time and none report an end time, so the
  field is a schedule. Prospective rows captured before first-ball polling stay START_UNKNOWN and are
  reclassified deterministically only if trustworthy truth ever arrives
  (`scripts/firstball/assess_historical_recovery.py` re-runs the check).
* **Feed lag is assumed, not measured.** No live-score source documents its latency, and lag pushes an
  observed lower bound LATER than the true first ball, which is the dangerous direction. A conservative
  120 s allowance widens every bracket until a source's real lag is measured against a second provider.
* **No draw feed**: tournament winner / round advancement markets are parsed but not priced live.
* **Kalshi fee coefficients** (0.07 taker, 0.0175 maker) are from the published schedule as recorded in the
  sibling NFL project, not byte-verified tonight (kalshi.com unreachable).
* **Contract-terms PDFs** downloaded (286) but not parsed; settlement rules come from `important_info` text
  (25 series) and observed settlements.

## Modelling
* Elo and the structural model are **worse than Pinnacle** on every cut (Brier gap ~0.014 and ~0.011; ensemble
  ~0.008). The walk-forward hybrid gives the model a small negative weight. There is no evidence of edge.
* Ratings ignore rest/fatigue/travel/form features (not yet ablated), injuries/withdrawals, court speed,
  indoor/outdoor beyond surface, altitude, weather.
* Serve/return abilities exist only where Sackmann serve stats exist (tour level + some Challengers);
  ITF/WTA-lower projections are Elo-only and flagged by data quality.
* Elo overconfidence: calibration slope ~0.83-0.89 on tour matches for K=180-250; the ensemble is ~1.05.
* Retirement mass is not modelled in derivative pricing (totals/spreads priced on completed-match
  distribution); the exchange settles determined markets and fair-prices the rest.
* Doubles: baseline prior only, unvalidated, not wired to live pricing.
* Cross-source id systems (Sackmann vs TML) are not linked; production uses Sackmann ids only.
* 2020 season gap (COVID) and partial 2025-26 ITF coverage in the forks.
* Same-surname Kalshi events (dup-digit tickers) and 19 events whose derivative-only markets lack both
  full names are excluded from projection (listed in the coverage report).

## Operations
* Scheduled crons cannot run from a non-default branch: capture continuity relies on the self-dispatching
  conductor (`tennis-capture.yml`); a failed dispatch stops the chain. Moving the workflows to the default
  branch enables plain `schedule:` triggers.
* First 5.7 h of capture (06:57-12:38 UTC) were lost to the >100 MB file rejection (fixed: gzip + shards).
* The projection pipeline uses discovery-time quotes when no capture quotes exist; quotes can be hours old.
