# Data source registry (tennis-edge-finder)

Status labels: CONFIRMED (verified by download/inspection this session), LIKELY, UNKNOWN, UNUSABLE.
Retrieval date for everything below: 2026-09-11 (GitHub Actions runner; the dev sandbox has an egress
allowlist and cannot reach github.com raw content, tennis-data.co.uk, kalshi.com, docs.kalshi.com, atptour.com,
wtatennis.com, itftennis.com, sofascore, flashscore, wikipedia).

| source | type | purpose | reference | coverage | tours/levels | singles/doubles | key fields | update freq | access | auth | rate limits | licence | redistribution | known gaps | known biases | reliability | authority rank | production role | fallback role | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sackmann tennis_atp (via public fork `Kadantte/tennis_atp`, max season file 2026) | match results + serve stats + rankings + players | ATP main draw, qualifying+Challenger, Futures/ITF men | https://github.com/JeffSackmann/tennis_atp (upstream **404 on 2026-09-11**; data taken from a fork) | 1968-2026 (futures 1991-, qual/chall 1978-) | ATP tour, Challenger, ITF men | singles (+ doubles files to ~2019) | tourney_id/name/surface/level/date, ids, names, hand, ht, ioc, age, rank, score, best_of, round, minutes, w_/l_ serve stats | upstream was ~weekly; fork freshness unknown (max file 2026) | zip archive over HTTPS | none | GitHub | CC BY-NC-SA 4.0 | non-commercial + share-alike; a commercial deployment cannot ship these files | serve stats sparse below tour level; 2025-26 season files may be partial in the fork | winner-first score notation; ids numeric | high (community standard) | 1 | history spine for ATP/Challenger/ITF-M | TML for ATP main | CONFIRMED |
| Sackmann tennis_wta (via public fork `VictorSquidWei/tennis_wta`, max season 2026) | match results + rankings + players | WTA main, qualifying + ITF women + WTA 125 | https://github.com/JeffSackmann/tennis_wta (upstream 404; fork) | 1920-2026 (qual_itf 1968-) | WTA tour, WTA 125, ITF women | singles | as above | as above | zip | none | GitHub | CC BY-NC-SA 4.0 | as above | serve stats mostly absent below slams/1000s; no doubles | as above | high | 1 | history spine for WTA/ITF-W | none (only source) | CONFIRMED |
| TML-Database (Tennismylife) | match results + serve stats | ATP main tour 1968-2026 with ATP-site ids; independent maintenance | https://github.com/Tennismylife/TML-Database | 1968-2026 (daily updates per README) | ATP main tour (+ Challenger files via the gmalbert mirror 2000-2026) | singles | Sackmann schema + `indoor` | daily (README) | zip | none | GitHub | README: educational/research; redistribution/commercial use may need permission from TennisMyLife/ATP | restricted | ids are ATP-site alphanumeric (different id system) | scores occasionally omit RET | good | 2 | cross-check + freshest ATP results; Challenger coverage | primary if Sackmann fork stale | CONFIRMED |
| tennis-data.co.uk | results + bookmaker odds (B365, PS/Pinnacle, Max, Avg, ...) | historical bookmaker benchmark (pre-match prices) | http://www.tennis-data.co.uk/ | ATP 2000-, WTA 2007- | ATP/WTA main tour | singles | Location, Tournament, Date, Series, Court, Surface, Round, Best of, Winner/Loser (surname + initial), ranks, points, set scores, Comment, odds columns | weekly in season | xlsx per season | none | site returned **HTTP 503 to the runner for every URL** | free download, personal use per site | not for redistribution | capture time of odds undocumented (not certified closing lines); name format lossy | only two-way match-winner odds | good | 2 (benchmark only) | bookmaker benchmark | mirrors | UNUSABLE direct tonight; ATP 2020-2026 workbooks obtained from a mirror (below) |
| Mirror gmalbert/tennis-predictions | copies of tennis-data xlsx (ATP 2020-2026) + TML season files incl. `*_with_odds` merges 2020-2025 | fills the tennis-data gap | https://github.com/gmalbert/tennis-predictions | 2020-2026 ATP | ATP main | singles | as tennis-data / TML | unknown | zip | none | GitHub | third-party copy; underlying terms apply | restricted | WTA absent; provenance of odds merge unknown | none known | medium (MIRROR) | 3 | benchmark for the Elo-vs-market study | -- | CONFIRMED |
| Match Charting Project (Sackmann) | point-by-point charted matches (overview/serve/return stat files taken) | future serve/return features, tiebreak research | https://github.com/JeffSackmann/tennis_MatchChartingProject | 1970s-2026, volunteer-selected matches | ATP/WTA tour mostly | singles | charting-m/w-matches, stats-Overview/ServeBasics/ReturnOutcomes/KeyPoints | irregular | zip | none | GitHub | CC BY-NC-SA 4.0 | non-commercial | selection bias toward big matches | strong selection bias | high for charted matches | 3 | research only (not used in v0 models) | -- | CONFIRMED |
| Kalshi Trade API v2 (public GETs) | series/events/markets/orderbook/trades/candlesticks, historical tier | market discovery, capture, settlement truth | https://api.elections.kalshi.com/trade-api/v2 (docs.kalshi.com unreachable from sandbox) | live tier since cutoff (historical/cutoff 2026-07-05 for settled markets); archive tier before | all Kalshi tennis series (143) | both | see docs/KALSHI_MARKET_TAXONOMY.md | real time | REST (runner only; sandbox egress denied) | none for reads | ~20 rps basic tier; we use 5 | Kalshi ToS | observations are ours | orderbook only for open markets; no first-ball timestamps | last trade != executable | high | 1 (market truth) | market capture + exchange truth | -- | CONFIRMED |
| Kalshi contract terms PDFs (286 files) | rules | settlement semantics per series | assets.kalshi.com/contract_terms/*.pdf | current | tennis series | both | -- | on change | HTTPS | none | -- | Kalshi | -- | not parsed tonight (PDF) | -- | high | 1 | rules of record | important_info text | CONFIRMED (downloaded, unparsed) |
| ATP / WTA / ITF official sites, Grand Slam sites, draws, schedules, live scores | schedules, draws, first-ball times | actual start detection, futures draws | atptour.com, wtatennis.com, itftennis.com | -- | -- | -- | -- | -- | HTML/APIs | ToS | -- | official | scraping restricted | **blocked by sandbox egress**; runner reachability untested | -- | -- | 1 for schedules | first-ball truth, draws | -- | UNKNOWN (not reachable tonight) |
| TennisData.app free season files | results/odds | alternative benchmark | tennisdata.app | unknown | unknown | unknown | unknown | unknown | unknown | unknown | unknown | unknown | unknown | site unreachable from sandbox | -- | -- | -- | -- | -- | UNKNOWN |
| Weather / altitude / venue coordinates | environment | future features | e.g. open-meteo | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | not wired | -- | -- | -- | -- | -- | UNKNOWN |
| Kaggle mirrors (hakeem/atp-and-wta-tennis-data, dissfya/atp-tennis-2000-2026) | odds+results | benchmark | kaggle.com | 2000-2026 | ATP/WTA | singles | tennis-data schema | varies | needs Kaggle auth | yes | -- | per dataset | -- | credentials unavailable | -- | -- | 3 | WTA odds benchmark (future) | -- | UNKNOWN (auth) |

## Licensing note
Sackmann and MCP data are CC BY-NC-SA: models trained on them may be used for research; a commercial
product that redistributes the raw files or is itself commercial needs a separate basis. TML asks for
permission for redistribution/commercial use. tennis-data.co.uk is for personal use. The Kalshi
observations we capture ourselves are our own records of public API responses.

## Snapshots on the `tennis-data` branch
`tennis-edge-finder/data/sources/<run_id>/manifest.json` records every file's sha256, byte counts, row
counts, source URL/commit and the candidate list examined. Run ids: 20260911T071045Z (Sackmann forks + TML +
MCP), 20260911T070313Z (mirror odds), 20260911T063759Z (Kalshi discovery).


## Freshness, re-investigated 2026-09-12 (wave 2)

TENNIS-14 was failing because the fundamental sources were stale. The re-investigation, with evidence:

| source | reachable | freshest data | verdict |
|---|---|---|---|
| `JeffSackmann/tennis_atp` / `tennis_wta` (upstream) | **no**, HTTP 404 both | - | gone |
| 20 most recently pushed `tennis_atp` forks | yes | pushed 2026-06-10 (one), 2026-06-08 (all others) | **every fork froze with upstream**; chasing forks is wasted effort |
| `Kadantte/tennis_atp` (fork in use) | yes | ATP matches to 2026-06-01 | frozen |
| `VictorSquidWei/tennis_wta` (fork in use) | yes | WTA matches to 2026-04-27 | frozen |
| `gmalbert/tennis-predictions` (community mirror) | yes, pushed 2026-09-11 | **ATP to 2026-09-01** (challenger), 2026-08-30 (main) | freshest ATP available; TML-format, ATP-site ids |
| `Tennismylife/TML-Database` (upstream) | yes | 2026-01-22 | behind the mirror |
| tennis-data.co.uk | **no**, HTTP 503 | - | still down |
| ESPN site API scoreboard | yes | **current, both tours** | results only: no serve statistics, no surface |
| ESPN rankings API | yes | current | not yet ingested |

### What changed as a result

1. **A cross-system player crosswalk** (`tennis_edge/identity/crosswalk.py`). Production ratings used to
   exclude every non-Sackmann row, because merging id systems naively once produced duplicate rating
   entities. That exclusion cost three months of ATP results. The crosswalk binds foreign ids to
   canonical ones by normalised name and fails closed at every step: a name shared by two players in
   EITHER system maps to nothing, and a match with one unmapped player is left unmapped as a whole.
   4,701 of 4,991 mirror players crosswalked, 88,896 extra rows admitted, and **ATP ratings moved from
   as-of 2026-06-01 to as-of 2026-09-01**. WTA is unchanged: nothing fresher exists.
2. **An ESPN results feed** (`tennis_edge/data/espn_results.py`, `scripts/data/fetch_espn_results.py`).
   The only reachable source of CURRENT results for both tours, which matters most for WTA. Verified
   against a saved payload: 473 completed singles parsed from one board, 97% passing canonical
   validation, the remainder correctly quarantined as retirements. ESPN's regulation-length field is
   deliberately ignored, because it reports five sets for a men's slam even on a best-of-three
   qualifying match.

### Still stale, and honestly so

WTA fundamentals end 2026-04-27 and no free source was found to fix the history. TENNIS-14 continues to
fail rather than being relaxed. The knock-on cost is visible in the board accounting: the largest
fixable coverage blocker is UNMAPPED_IDENTITY, and most of those are recent arrivals absent from a
registry built on four-month-old data. **The coverage gap is largely the freshness gap wearing a
different hat.**


## ESPN results feed — operational notes (2026-09-12)

Live and publishing to `tennis-data` under `data/sources/espn/<run>/`, 5,471 completed singles covering
2026-03-28 to 2026-09-11 on both tours.

Two defects were found on its first unattended runs and both are fixed:

* The step died importing pandas (the sources job installs nothing, the Sackmann fetcher being
  stdlib-only) and `continue-on-error` turned that into a green step that published nothing. The step now
  installs pandas and fails loudly if the fetch produces no output.
* A combined event is returned by BOTH league boards carrying BOTH draws. Taking the tour from the league
  fetched filed 1,373 men's matches as WTA. `parse_scoreboard` now reads the tour from the grouping slug
  (women tested first, since "womens" contains "mens") and falls back to the league only when the
  grouping does not name a draw.

**Snapshot `20260912T065821Z` is QUARANTINED** — it carries the mislabelled split (779 ATP / 4,692 WTA
where the truth is 2,152 / 3,319). It is marked in place, not deleted; `tennis-data` is append-only
evidence. Do not ingest it.

The feed is **results-only**: no serve statistics, no reliable surface, no `best_of` (ESPN reports the
event's regulation length, which is wrong for qualifying, so the field is deliberately left empty). It can
refresh Elo-family ratings. It cannot feed Gen-2, so it does not close TENNIS-14.
